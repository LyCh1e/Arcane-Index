---
type: learning
status: established
created: 2026-05-31
updated: 2026-05-31
name: docker-volume-host-dir-created-as-root
description: Docker creates the host-side bind-mount directory as root if it does not already exist — fix with sudo chown
metadata:
  type: feedback
---

# Docker: Bind-Mount Host Directory Created as Root

**Why:** When Docker starts a container with a bind mount (`./nginx/certs:/etc/nginx/certs:ro`) and the host-side path does not exist, Docker creates it automatically — but as **root**, not as the current user.

Any subsequent attempt to write files into that directory as a non-root user fails with "Permission denied".

## Symptom
```
scp: dest open "nginx/certs/cert.pem": Permission denied
```
Or:
```
chmod: changing permissions of 'nginx/certs': Operation not permitted
```
`ls -la` confirms: `drwxr-xr-x 2 root root ... nginx/certs`

## Fix
```bash
sudo chown <user>:<user> ~/project/nginx/certs
```
Then SCP or write files normally.

## Prevention
Create the directory yourself before running `docker compose up`:
```bash
mkdir -p nginx/certs
```
When the directory already exists and is user-owned, Docker will not recreate it.

## Context
Observed during EC2 deployment of TrialGuard (ICT2216 project, 2026-05-30). The `nginx/certs` directory is gitignored; Docker created it as root on first `docker compose up --build -d`, blocking subsequent SCP of TLS cert files. See [[examples/ict2216-project-deployment-phases-9-12]].
