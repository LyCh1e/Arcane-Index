---
type: learning
title: "Docker Compose: Build Context Controls What COPY Can See"
domain: devops
tags: [docker, docker-compose, build-context, dockerfile, COPY, gotcha]
created: 2026-05-26
status: resolved
---

# Docker Compose: Build Context Controls What COPY Can See

## The Bug

Moving `requirements.txt` from `backend/requirements.txt` to the repo root broke the Docker build:

```
COPY requirements.txt .
# → COPY failed: file not found in build context
```

The Dockerfile was unchanged. The `COPY` path hadn't changed. But the file had moved one directory up.

**Why:** `COPY` paths are **relative to the build context**, not to the Dockerfile's location. The build context was `./backend`, so Docker could only see files inside `backend/`. The root-level `requirements.txt` was invisible to it.

## The Fix

Change the build context to the repo root and scope the app-code COPY explicitly:

```yaml
# Before (context = service subdirectory)
services:
  flask:
    build: ./backend

# After (context = repo root, Dockerfile specified explicitly)
services:
  flask:
    build:
      context: .
      dockerfile: backend/Dockerfile
```

```dockerfile
# Before (inside backend/Dockerfile — worked when context was ./backend)
COPY . .

# After (context is now repo root — scope the copy to just the backend code)
COPY requirements.txt .
COPY backend/ .
```

The `requirements.txt` at the root is now reachable, and the backend app code is still correctly copied in.

**Why:** `COPY backend/ .` copies the *contents* of `backend/` into the container's `WORKDIR`. The trailing `/` on the source is important — it copies the contents, not a `backend/` subdirectory.

## General Rule

> The build context is a snapshot of the filesystem sent to the Docker daemon. Only files inside the context are available to `COPY` and `ADD`. The Dockerfile location within that context does not matter.

```
repo root/                   ← build context (context: .)
  requirements.txt           ← visible to COPY
  backend/
    Dockerfile               ← dockerfile: backend/Dockerfile
    app/
      ...                    ← visible to COPY backend/ .
```

## When to use this pattern

Use `context: .` (repo root) when:
- A shared file (requirements, certs, config) needs to be accessible to multiple Dockerfiles
- A Dockerfile is in a subdirectory but needs files from the parent

Use `context: ./service-dir` (service subdirectory) when:
- Each service is fully self-contained with no shared files from the root

## Related

- [[concepts/docker-compose]] — full Docker Compose reference
- [[learning/docker-windows-crlf]] — another Docker gotcha on Windows
