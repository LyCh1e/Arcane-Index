---
type: resource
status: established
created: 2026-07-23
updated: 2026-07-23
name: gitea-and-act-runner
description: Gitea (self-hosted git + web UI) and its act_runner (GitHub-Actions-compatible CI executor) — setup, admin bootstrap, and runner registration
metadata:
  type: resource
tags: [gitea, act-runner, git, ci-cd, self-hosted]
---

# Gitea + `act_runner`

Gitea is a lightweight, self-hostable Git service with a web UI (repos, issues, PRs, wiki) and its own GitHub-Actions-compatible CI system, "Gitea Actions." `act_runner` is the executor that actually picks up and runs `.gitea/workflows/*.yml` files — without it registered, workflows sit queued forever.

## Docker Compose Setup

```yaml
gitea:
  image: gitea/gitea:latest
  environment:
    - GITEA__database__DB_TYPE=sqlite3
    - GITEA__security__INSTALL_LOCK=true      # skip the setup wizard
    - GITEA__server__ROOT_URL=http://localhost:3001/
    - GITEA__actions__ENABLED=true            # required for Actions to work at all
  volumes:
    - gitea_data:/data
  ports:
    - "3001:3000"   # web UI
    - "2222:22"     # SSH clone
```

## Admin Account: No Env-Var Bootstrap

Unlike some Docker images, Gitea's official image has **no** `GITEA_ADMIN_USERNAME`/`PASSWORD` env vars for auto-provisioning an admin account (a long-standing open feature request, [go-gitea/gitea#31671](https://github.com/go-gitea/gitea/issues/31671)). Bootstrap it manually after the container is up:

```bash
docker compose exec -u git gitea gitea admin user create \
  --username myuser --password 'pw' --email me@localhost \
  --admin --must-change-password=false
```

Note `-u git` — running the CLI as the container's default (root) user fails with `Gitea is not supposed to be run as root`.

Full name (as opposed to login username) isn't a CLI flag either; set it via the API after creating the user:
```bash
curl -u user:pw -X PATCH http://host:3001/api/v1/user/settings \
  -H "Content-Type: application/json" -d '{"full_name":"Display Name"}'
```

## Registering `act_runner`

1. Get a registration token (repo-scoped is simplest for a single project):
   ```bash
   curl -u admin:pw -X POST \
     "http://host:3001/api/v1/repos/{owner}/{repo}/actions/runners/registration-token"
   ```
2. Add the runner as a compose service:
   ```yaml
   act-runner:
     image: gitea/act_runner:latest
     environment:
       - GITEA_INSTANCE_URL=http://gitea:3000       # internal service name, not the host port
       - GITEA_RUNNER_REGISTRATION_TOKEN=<token>
       - GITEA_RUNNER_LABELS=ubuntu-latest:docker://catthehacker/ubuntu:act-latest
       - CONFIG_FILE=/config.yaml
     volumes:
       - ./act-runner/config.yaml:/config.yaml:ro
       - /var/run/docker.sock:/var/run/docker.sock   # DooD — see the networking gotchas page
       - act_runner_data:/data
   ```
3. `GITEA_RUNNER_LABELS` maps the workflow's `runs-on: ubuntu-latest` to a real Docker image (`catthehacker/ubuntu:act-latest`, ~2.3GB, includes Node.js pre-installed — required since actions like `actions/checkout` are themselves Node-based and won't run in a bare image).

See [[learning/gitea-act-runner-dood-networking]] for the four networking/config bugs hit getting a `docker compose`-based workflow to actually run under this setup, and [[examples/ict2216-practical-test-secure-webapp]] for the full pipeline this was built for.

## Related

- [[concepts/github-actions-cicd]] — workflow YAML syntax (Gitea Actions is GitHub-Actions-compatible)
- [[concepts/docker-compose]] — general compose reference
