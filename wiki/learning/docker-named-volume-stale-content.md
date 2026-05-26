---
type: learning
title: "Docker Named Volumes: Rebuilding the Image Does NOT Update an Existing Volume"
domain: devops
tags: [docker, docker-compose, volumes, frontend, nginx, stale-build, gotcha]
created: 2026-05-26
status: resolved
---

# Docker Named Volumes: Rebuilding the Image Does NOT Update an Existing Volume

## The Bug

After editing frontend source files, rebuilding the images, and restarting nginx, the browser still showed the old UI. Source code changes had no effect.

```
# These commands do NOT fix a stale volume
docker compose build frontend-build nginx
docker compose up -d --no-deps nginx
```

The running site kept serving the old JS bundle even though the image had new code.

## Root Cause

The frontend dist files were served via a **named volume** shared between two services:

```yaml
services:
  frontend-build:
    build: ./frontend
    volumes:
      - frontend_dist:/app/dist      # build writes dist here

  nginx:
    volumes:
      - frontend_dist:/usr/share/nginx/html:ro   # nginx reads from here

volumes:
  frontend_dist:
```

The frontend Dockerfile runs `npm run build` during `docker build`, writing the dist files into the image at `/app/dist`. When `docker compose up` starts the `frontend-build` container for the **first time**, the volume is empty, so Docker copies the image's `/app/dist` into the volume.

**The critical rule:** Docker only seeds a volume from image contents when the volume is **new and empty**. Once the volume has content, it is **never overwritten** — not even when you rebuild the image with new content.

So:
- First `docker compose up --build` → volume is empty → seeded from image ✓
- Edit source → `docker compose build` → new image with new dist → BUT volume still has old dist ✗
- Nginx reads the volume → old files served ✗

## The Fix

Delete the volume before each build so it is always re-seeded from the new image:

```python
def purge_frontend_volume():
    vol = "ict2216-secure-software-development_frontend_dist"

    # Stop containers holding the volume
    subprocess.run(["docker", "compose", "stop", "nginx", "frontend-build"],
                   capture_output=True)

    # Remove stopped containers still referencing it
    result = subprocess.run(
        ["docker", "ps", "-a", "--filter", f"volume={vol}", "--format", "{{.ID}}"],
        capture_output=True, text=True,
    )
    for cid in result.stdout.split():
        subprocess.run(["docker", "rm", cid.strip()], capture_output=True)

    # Delete the volume (silently succeeds if it doesn't exist yet)
    subprocess.run(["docker", "volume", "rm", vol], capture_output=True)
```

Then run `docker compose up -d --build` — the volume is empty so Docker re-seeds it from the freshly built image.

Manual equivalent:
```bash
docker compose stop nginx frontend-build
docker rm <container-id-holding-volume>
docker volume rm ict2216-secure-software-development_frontend_dist
docker compose up -d --build
```

## Why `docker volume rm` fails without removing containers first

A volume cannot be removed while any container (even stopped/exited ones) references it. You must `docker rm` the stopped containers before `docker volume rm` will succeed.

```
Error response from daemon: remove ..._frontend_dist: volume is in use - [980a8f...]
```

## Does every service have this problem?

No — only services that use a **named volume as an artifact hand-off** between two containers.

| Service | Pattern | Stale volume risk? |
|---------|---------|-------------------|
| `frontend-build` → `nginx` | `frontend_dist` volume passes dist files | **Yes** — fix needed |
| `flask` | Code baked into image, container runs directly from it | No |
| `pii_vault` | Same as flask | No |
| `mysql` / `mongodb` | Named volumes hold *data*, not build artifacts | No (data must persist) |

Flask and pii_vault code is embedded in the image via `COPY` during `docker build`. `docker compose up --build` rebuilds the image and starts a fresh container from it — no intermediate volume, no stale content risk.

The pattern to watch for: **two services sharing a named volume where one is a build step and the other is the runtime server**. That's the only shape that produces stale content.

## General Rule

> If your compose stack uses a named volume to pass build artifacts between services, **any rebuild must delete and recreate the volume** — otherwise nginx (or whatever consumer) will keep serving stale content indefinitely.

Alternative patterns that avoid this problem:
- **Multi-stage Dockerfile**: copy dist directly into the nginx image (`COPY --from=builder /app/dist /usr/share/nginx/html`) — no shared volume needed
- **Bind mount**: mount `./frontend/dist` directly — changes on disk are reflected immediately (good for dev, not prod)

## Related

- [[concepts/docker-compose]] — Docker Compose reference, build context, volumes
- [[learning/docker-compose-build-context]] — build context controls what COPY can see
- [[examples/ict2216-project-phase4-auth]] — the project this was encountered in
