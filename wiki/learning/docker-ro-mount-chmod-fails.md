---
name: docker-ro-mount-chmod-fails
description: chmod fails on files mounted read-only (:ro) into a Docker container — use sh script.sh instead of chmod +x
metadata:
  type: feedback
---

# Docker: `chmod` Fails on Read-Only Mounts

**Rule:** Never `chmod` a file that is mounted `:ro` into a container. Use `sh script.sh` instead of making it executable.

**Why:** A `:ro` bind mount makes the entire mounted path immutable from inside the container at the filesystem level. `chmod` is a write operation on the file's metadata — it fails with:
```
chmod: changing permissions of '/backup.sh': Read-only file system
```

## The Pattern That Breaks
```yaml
entrypoint: >
  sh -c "chmod +x /backup.sh && while true; do /backup.sh; sleep 86400; done"
volumes:
  - ./backup/backup.sh:/backup.sh:ro   # :ro makes chmod impossible
```

## The Fix
```yaml
entrypoint: >
  sh -c "while true; do sh /backup.sh; sleep 86400; done"
```
`sh /backup.sh` executes the script via the shell interpreter — execute permission on the file is irrelevant because the shell binary is what runs, not the file directly.

## Alternative if You Need the File Executable
Copy it to a writable location first:
```yaml
entrypoint: >
  sh -c "cp /backup.sh /tmp/backup.sh && chmod +x /tmp/backup.sh && /tmp/backup.sh"
```

## Context
Observed in `db-backup` service of TrialGuard docker-compose.yml (ICT2216 project, 2026-05-30). The `backup.sh` script was mounted `:ro` for safety, causing the container to restart-loop on `chmod`. See [[examples/ict2216-project-deployment-phases-9-12]].
