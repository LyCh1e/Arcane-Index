---
name: github-actions-cicd
description: GitHub Actions CI/CD — workflow syntax, triggers, jobs, steps, secrets, Docker integration, and pipeline design
metadata:
  type: concept
domain: devops
complexity: medium
created: 2026-05-30
tags: [github-actions, ci-cd, devops, docker, automation, yaml]
---

# GitHub Actions CI/CD

## What is GitHub Actions?

GitHub Actions is a CI/CD (Continuous Integration / Continuous Deployment) automation platform built into GitHub. It runs automated workflows in response to GitHub events (push, pull_request, schedule, etc.) on GitHub-hosted or self-hosted runners.

**Why it matters for secure software:** Automated pipelines enforce that every code change is built, tested, and scanned before merging — preventing untested or insecure code from reaching production.

## Workflow File Location

Workflow files live at:

```
.github/workflows/<workflow-name>.yml
```

Multiple `.yml` files = multiple independent workflows.

## Workflow Anatomy

```yaml
name: Workflow display name

on:                        # Trigger(s)
  push:
    branches: [main]
  pull_request:            # Also runs on PRs targeting any branch
  schedule:
    - cron: '0 3 * * *'   # Cron syntax: min hour dom month dow

jobs:
  job-id:                  # Arbitrary identifier
    runs-on: ubuntu-latest # Runner OS (ubuntu-latest, windows-latest, macos-latest)

    steps:
      - name: Human-readable step name
        uses: actions/checkout@v4      # Reusable Action from Marketplace

      - name: Run a shell command
        run: echo "Hello"

      - name: Multi-line shell
        run: |
          echo "line 1"
          echo "line 2"

      - name: Use an output from previous step
        run: echo "${{ steps.step-id.outputs.some-output }}"
```

## Key Concepts

### Triggers (`on:`)

| Trigger | Description |
|---------|-------------|
| `push` | On every push (optionally filter by `branches`, `paths`) |
| `pull_request` | On PR open/update |
| `schedule` | Cron-based (UTC) |
| `workflow_dispatch` | Manual trigger from GitHub UI |
| `release` | On GitHub release creation |

### Runners (`runs-on:`)

GitHub provides hosted runners:
- `ubuntu-latest` — most common, Docker pre-installed
- `windows-latest`, `macos-latest`

Self-hosted runners run on your own infrastructure (team VM) — required for deployment to private networks.

### Actions (`uses:`)

Pre-built reusable units from GitHub Marketplace:

| Action | Purpose |
|--------|---------|
| `actions/checkout@v4` | Check out repo code into runner workspace |
| `actions/setup-python@v5` | Set up Python with specified version |
| `actions/setup-node@v4` | Set up Node.js |
| `docker/build-push-action@v5` | Build + push Docker image |

### Expressions and Context

| Expression | Value |
|-----------|-------|
| `${{ github.workspace }}` | Absolute path to checked-out repo on runner |
| `${{ github.sha }}` | Full commit SHA |
| `${{ github.ref }}` | Branch/tag ref (e.g. `refs/heads/main`) |
| `${{ secrets.MY_SECRET }}` | Secret stored in repo/org settings |
| `${{ env.MY_VAR }}` | Environment variable |

### Secrets

Store sensitive values (tokens, passwords, SSH keys) in **Settings → Secrets and variables → Actions**, never in workflow YAML:

```yaml
steps:
  - name: Deploy
    env:
      SSH_KEY: ${{ secrets.DEPLOY_SSH_KEY }}
    run: echo "$SSH_KEY" | ssh-add -
```

### Jobs and Dependencies

Jobs run in parallel by default. Use `needs:` to sequence them:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps: [...]

  test:
    needs: build           # Runs after build completes
    runs-on: ubuntu-latest
    steps: [...]

  deploy:
    needs: [build, test]   # Runs after both
    runs-on: ubuntu-latest
    steps: [...]
```

## Docker in GitHub Actions

Ubuntu runners have Docker pre-installed. Run containers directly in `run:` steps:

```yaml
- name: Start Nginx
  run: |
    docker run -d --name my-nginx -p 8080:80 \
      -v ${{ github.workspace }}/index.html:/usr/share/nginx/html/index.html:ro \
      nginx:latest

- name: Test
  run: |
    sleep 5
    curl -s http://localhost:8080/ | grep "Hello World"

- name: Stop
  run: docker stop my-nginx
```

Or use Docker Compose:

```yaml
- name: Start stack
  run: docker compose up -d

- name: Run tests against stack
  run: pytest tests/integration/

- name: Teardown
  run: docker compose down
```

## A Complete Nginx Test Workflow

```yaml
name: Test Nginx Hello World Page

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test-nginx:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Start Nginx with Docker
        run: |
          docker run -d --name test-nginx -p 8080:80 \
            -v ${{ github.workspace }}/index.html:/usr/share/nginx/html/index.html:ro \
            nginx:latest

      - name: Wait for Nginx to start
        run: sleep 5

      - name: Test Hello World Page
        run: |
          curl -s -o response.html http://localhost:8080/index.html
          grep "Hello World" response.html

      - name: Stop Nginx container
        run: docker stop test-nginx
```

## Self-Hosted Runner (Team VM Deployment)

To deploy to a private VM:

1. Go to **Settings → Actions → Runners → New self-hosted runner** in your GitHub repo
2. Follow the instructions on the VM to install and register the runner
3. Use `runs-on: self-hosted` (or custom label) in the workflow
4. The runner must have Docker installed and your deployment credentials

```yaml
jobs:
  deploy:
    runs-on: self-hosted   # Runs on your team VM
    steps:
      - uses: actions/checkout@v4
      - name: Deploy via Docker Compose
        run: |
          docker compose pull
          docker compose up -d --build
```

## CI/CD Pipeline Stages (Secure Software)

A typical secure pipeline:

```
Push to main
    │
    ▼
Build (docker build / compile)
    │
    ▼
Unit Tests (pytest, jest, etc.)
    │
    ▼
SAST — Static Analysis (e.g. Semgrep, Bandit)         ← Lab 8
    │
    ▼
Dependency Scan (OWASP Dependency-Check)               ← Lab 6
    │
    ▼
Container Build + Push to Registry
    │
    ▼
Deploy to Staging (docker compose up on self-hosted)
    │
    ▼
DAST — Dynamic Analysis (OWASP ZAP)                    ← Lab 11
    │
    ▼
Release / Tag
```

## Related

- [[concepts/software-configuration-management]] — CI/CD theory (Booch/Fowler), git workflow
- [[concepts/nginx-reverse-proxy-and-tls]] — Nginx setup tested by the Actions workflow
- [[examples/ict2216-lab5-github-actions]] — Full Lab 5 walkthrough
