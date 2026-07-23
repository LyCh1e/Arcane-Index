---
type: learning
status: resolved
created: 2026-07-23
updated: 2026-07-23
name: gitea-act-runner-dood-networking
description: Four distinct Docker-outside-of-Docker (DooD) networking/config bugs hit while getting a real Gitea Actions act_runner to execute a docker-compose-based CI workflow
metadata:
  type: learning
skill: devops
tags: [docker, dood, act-runner, gitea-actions, networking, ci-cd]
---

# Gitea `act_runner` + Docker-outside-of-Docker: 4 Gotchas

Getting a self-hosted Gitea Actions runner to actually execute a `docker compose`-based CI workflow (not just accept the YAML) surfaced four distinct bugs, each with a different failure signature. Logged together because they all stem from the same root confusion: **the job "container" is a sibling of the app containers it manages, not a parent** — it shares the host's Docker daemon via a mounted socket, but has its own filesystem and its own network namespace.

## 1. Duplicate `docker.sock` mount → `failed to create container: Duplicate mount point`

`act_runner` auto-detects DooD mode (it notices its own container has `/var/run/docker.sock` mounted) and propagates that same mount into every job container it spawns. Also specifying `-v /var/run/docker.sock:/var/run/docker.sock` in `container.options` in `config.yaml` doubles it up.

**Fix**: don't set `container.options` for the socket at all — it's automatic.

## 2. Isolated per-job network → `Could not resolve host: gitea`

By default `act_runner` creates a fresh, isolated bridge network per job. `actions/checkout@v4` then can't resolve the Gitea server's hostname to clone the repo, since Gitea (and any other persistent services) live on the docker-compose project's own network.

**Fix**: pin job containers to the existing project network in `config.yaml`:
```yaml
container:
  network: "practicaltest_default"   # <project>_default from docker-compose
```

## 3. Bind mounts silently become empty directories inside DooD job containers

A relative bind mount in `docker-compose.yml` (`./big-file.txt:/data/file.txt:ro`) works fine when run directly on the host. Run the identical `docker compose up` from *inside* a DooD job container, and the path gets resolved by the **host's** dockerd against the **host's** filesystem — but the checked-out repo the job is working with lives inside a Docker-managed volume, not a real host directory. Docker's default behavior for a missing bind-mount source is to silently create an empty directory rather than error, so the app sees `IsADirectoryError: [Errno 21] Is a directory: '/data/passwords.txt'` instead of a clear "no such file."

**Fix**: don't rely on bind mounts for anything a DooD-run compose stack needs. Bake the file into the image at build time instead (`COPY` it in the Dockerfile), building from a wider context (repo root) if the file lives outside the service's own subdirectory.

## 4. `127.0.0.1` from inside a sibling container is *its own* loopback

The most subtle one. A job container and an app container (e.g. `web`) are both attached to the same Docker network, but that does **not** mean they share a loopback interface. `curl https://127.0.0.1:8443/login` from inside the job container tries to reach port 8443 on the *job container itself* — nothing is listening there, and depending on the environment this can hang rather than fail fast (looked identical to a stuck job in the Gitea Actions UI: status stayed `in_progress` well past the loop's timeout, because the underlying `curl` call itself was hanging).

Two valid fixes, situational:
- **Reach a service by its Compose service name** (`http://web:8443`) — works only if the job container and that service are on the *same* Docker network. If the service was spun up under a different `COMPOSE_PROJECT_NAME` (e.g. `ci` vs the persistent stack's `practicaltest`), it gets its own separate network and the name won't resolve — and worse, if both networks happen to share an alias, you can silently hit the *wrong* container.
- **Reach a host-published port via `host.docker.internal`** — Docker Desktop's stable DNS name for the host machine, resolvable from any container including DooD siblings, regardless of which network they're on. This is the correct fix when the job spins up its own throwaway copy of a service via `docker compose up` under a project name that doesn't match anything already running.

Verified quickly with a disposable container: `docker run --rm curlimages/curl:latest curl -sk https://host.docker.internal/login` reached a host-published port instantly, no network wrangling required.

## Diagnostic pattern that cracked it

When a Gitea Actions job step appears stuck `in_progress` well past its own timeout logic:
1. Check `docker ps -a` for containers matching the job's compose project prefix — are they actually running / did they exit with an error?
2. Try the same `curl`/`docker run` command that the job step runs, but directly from the host shell — if it works from the host but not from the job, the difference is almost always the network namespace.
3. Tail the job's raw logs (`GET .../actions/jobs/{id}/logs`) rather than trusting the structured job-status API — status can lag, but the log stream shows exactly which line the job is stuck on.

## Related

- [[examples/ict2216-practical-test-secure-webapp]] — the build these bugs were found in
- [[concepts/docker-compose]] — general Docker Compose networking reference
- [[concepts/github-actions-cicd]] — GitHub/Gitea Actions workflow anatomy
- [[resources/gitea-and-act-runner]] — act_runner setup reference
