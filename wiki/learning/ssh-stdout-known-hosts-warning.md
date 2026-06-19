---
name: ssh-stdout-known-hosts-warning
description: SSH "Permanently added to known hosts" warning contaminates stdout when using 2>&1, breaking equality checks in CI scripts
metadata:
  type: feedback
domain: devops
status: resolved
created: 2026-06-19
tags: [ssh, ci-cd, github-actions, debugging]
---

# SSH: "Permanently added to known hosts" Contaminates stdout

## The bug

In a GitHub Actions (or any CI) script, you SSH to a new host and capture the output to check it:

```bash
result=$(ssh -i key.pem -o StrictHostKeyChecking=no "$HOST" "echo ok" 2>&1)
if [[ "$result" != "ok" ]]; then
  echo "SSH failed: $result"
  exit 1
fi
```

This always fails on the first connection to a host — even when SSH itself succeeds. The runner exits with:

```
SSH failed: Warning: Permanently added '18.223.111.152' (ED25519) to the list of known hosts.
```

## Root cause

`-o StrictHostKeyChecking=no` suppresses the interactive host-key prompt but does **not** suppress the informational log message that SSH writes to **stderr** when it adds the host to `~/.ssh/known_hosts`. With `2>&1`, stderr is merged into stdout, so the warning lands in `$result` before the `echo ok` output.

## Fix

Add `-o LogLevel=ERROR` to silence all SSH informational messages (level INFO and below). Remove `2>&1` so stderr goes to the runner log but does not pollute the captured variable:

```bash
result=$(ssh -i key.pem \
  -o StrictHostKeyChecking=no \
  -o LogLevel=ERROR \
  -o ConnectTimeout=10 \
  "$HOST" "echo ok")
if [[ "$result" != "ok" ]]; then
  echo "SSH failed: $result"
  exit 1
fi
```

Apply `LogLevel=ERROR` to **every** SSH and SCP call in the workflow — not just the connectivity test — so no warnings appear anywhere.

## SSH LogLevel values (low → high verbosity)

| Level | What it shows |
|-------|---------------|
| `QUIET` | Fatal errors only |
| `ERROR` | Errors + fatal |
| `INFO` (default) | Errors + informational (includes "Permanently added...") |
| `VERBOSE` / `DEBUG` | Full protocol trace |

Use `ERROR` for CI pipelines. Use `DEBUG3` when diagnosing connection failures.

## When this appears

- Any CI runner (GitHub Actions, GitLab CI, Jenkins) connecting to an EC2 instance or VPS for the first time
- The runner's `~/.ssh/known_hosts` is empty (ephemeral runners start clean every job)
- Even if you pre-populate `known_hosts` with `ssh-keyscan`, the log message appears on subsequent connections too unless `LogLevel=ERROR` is set

## Related

- [[concepts/github-actions-cicd]] — Full CD deploy job pattern with the fix applied
