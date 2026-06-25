---
type: concept
status: established
created: 2026-05-30
updated: 2026-06-25
name: github-actions-cicd
description: GitHub Actions CI/CD — workflow syntax, triggers, jobs, steps, secrets, Docker integration, and pipeline design
metadata:
  type: concept
domain: devops
complexity: medium
tags: [github-actions, ci-cd, devops, docker, automation, yaml]
---

# GitHub Actions CI/CD

## DevOps and DevSecOps

**DevOps** — coined by Patrick Debois (DevOpsDays, 2009) — bridges developers and operations teams to achieve faster, lower-risk delivery: *continuously improving software with small changes and small risks, rather than big changes with big risks.*

**DevSecOps** (also DevOpsSec or SecDevOps) embeds **security and compliance throughout the DevOps pipeline** rather than treating security as a final gate before release. Security is a shared responsibility from the first commit to production.

> DevSecOps may be understood as **extending Agile beyond the software team** to include security and operations as continuous, automated concerns.

### CI vs CD vs Continuous Deployment

| Term | Description | Deployment |
|------|-------------|------------|
| **Continuous Integration (CI)** | Automated build and test on every code commit | No deployment |
| **Continuous Delivery (CD)** | Automated up to a deployment-ready state | **Manual** trigger for production |
| **Continuous Deployment** | Fully automated pipeline end-to-end | **Automatic** to production |

> **Key distinction:** Continuous Delivery requires a human to approve the final production push; Continuous Deployment eliminates that gate entirely.

---

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

## CD: Deploying to EC2 via SSH

When CI jobs all pass, a `deploy` job can SSH into a remote server and restart the application. This is the standard CD pattern for EC2/VPS targets that cannot be reached via Docker registry push.

### Required GitHub Secrets

Add these via **Settings → Secrets and variables → Actions** or via the CLI:

```bash
gh secret set EC2_HOST    --body "ubuntu@<ip>"
gh secret set EC2_SSH_KEY --body "$(cat path/to/key.pem)"
```

Secrets are encrypted at rest (libsodium), masked in logs, and inaccessible to fork PRs. They cannot be read back after being set — write-only.

### Only deploy on push, not on PRs

Use an `if:` condition on the deploy job to prevent it running on pull requests:

```yaml
deploy:
  needs: [security-scan]
  if: github.event_name == 'push' && github.ref == 'refs/heads/main'
```

### Full Deploy Job Pattern

```yaml
deploy:
  name: Deploy to EC2
  runs-on: ubuntu-latest
  needs: [security-scan]
  if: github.event_name == 'push' && github.ref == 'refs/heads/main'

  env:
    REMOTE_DIR: ~/my-repo

  steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Write SSH key
      run: |
        mkdir -p ~/.ssh
        echo "${{ secrets.EC2_SSH_KEY }}" > ~/.ssh/deploy.pem
        chmod 600 ~/.ssh/deploy.pem

    - name: Test SSH connection
      run: |
        result=$(ssh -i ~/.ssh/deploy.pem \
          -o StrictHostKeyChecking=no \
          -o LogLevel=ERROR \
          -o ConnectTimeout=10 \
          "${{ secrets.EC2_HOST }}" "echo ok")
        if [[ "$result" != "ok" ]]; then
          echo "SSH failed: $result"
          exit 1
        fi

    - name: Create git archive
      run: git archive --format=tar HEAD -o /tmp/app.tar

    - name: Upload archive to EC2
      run: |
        scp -i ~/.ssh/deploy.pem \
          -o StrictHostKeyChecking=no \
          -o LogLevel=ERROR \
          /tmp/app.tar "${{ secrets.EC2_HOST }}:~/app.tar"

    - name: Extract and restart
      run: |
        ssh -i ~/.ssh/deploy.pem \
          -o StrictHostKeyChecking=no \
          -o LogLevel=ERROR \
          "${{ secrets.EC2_HOST }}" \
          "mkdir -p $REMOTE_DIR && cd $REMOTE_DIR && tar xf ~/app.tar &&
           docker compose up -d --build 2>&1 | tail -20"

    - name: Health check
      run: |
        health=$(ssh -i ~/.ssh/deploy.pem \
          -o StrictHostKeyChecking=no \
          -o LogLevel=ERROR \
          "${{ secrets.EC2_HOST }}" \
          "curl -sk https://localhost/api/health")
        echo "Health: $health"

    - name: Clean up SSH key
      if: always()
      run: rm -f ~/.ssh/deploy.pem
```

### Why `git archive` instead of `git clone`?

Private repos cannot be cloned on EC2 without credentials. `git archive --format=tar HEAD` bundles only the committed files from the current HEAD — no `.git` directory, no history — and is uploaded via SCP. Files in `.gitignore` (`.env`, TLS certs) must be pushed separately on first-time setup.

### SSH stdout contamination — the `-o LogLevel=ERROR` fix

Without `LogLevel=ERROR`, SSH prints `Warning: Permanently added '<host>' (ED25519) to the list of known hosts.` to **stderr**. If you redirect stderr to stdout with `2>&1` to capture the result of a command, this warning gets mixed into the variable and breaks equality checks:

```bash
# BROKEN — warning contaminates $result
result=$(ssh ... "$HOST" "echo ok" 2>&1)
[[ "$result" == "ok" ]]  # fails: $result = "Warning: Permanently added...\nok"

# FIXED — warning suppressed at source
result=$(ssh -o LogLevel=ERROR ... "$HOST" "echo ok")
[[ "$result" == "ok" ]]  # passes
```

Always add `-o LogLevel=ERROR` (and `-o StrictHostKeyChecking=no`) to SSH/SCP calls in CI pipelines. See [[learning/ssh-stdout-known-hosts-warning]].

## Action Version Management

### Node 20 Deprecation (Sep 2025)

GitHub runners stopped supporting Node 20 as a runner runtime in September 2025. Actions whose internal bundle still targets Node 20 produce a deprecation warning. Fix by pinning to newer minor/patch releases that bundle Node 24:

| Action | Node 24-compatible version |
|--------|---------------------------|
| `actions/checkout` | `@v4.3.0` |
| `actions/setup-node` | `@v4` (floating, auto-resolves) |
| `actions/upload-artifact` | `@v4.6.2` |
| `actions/setup-python` | `@v5.6.0` |
| `github/codeql-action/*` | `@v4` |

### CodeQL v3 → v4 (Dec 2026)

`github/codeql-action` v3 is deprecated in December 2026. Bump all three occurrences:

```yaml
uses: github/codeql-action/init@v4
uses: github/codeql-action/analyze@v4
uses: github/codeql-action/upload-sarif@v4
```

### Pinned vs Floating Tags

- **Floating major** (`@v4`) — always resolves to latest v4.x.x. Convenient but may lag after a new Node-runtime bump until GitHub's cache refreshes.
- **Pinned minor** (`@v4.3.0`) — predictable, but beware linters that auto-bump to a non-existent patch version (e.g. `@v4.3.0` → `@v4.4.2` where `v4.4.2` does not exist).

See [[learning/github-actions-version-deprecations]] for the full deprecation reference and the linter double-substitution trap.

## Related

- [[concepts/software-configuration-management]] — CI/CD theory (Booch/Fowler), git workflow
- [[concepts/nginx-reverse-proxy-and-tls]] — Nginx setup tested by the Actions workflow
- [[examples/ict2216-lab5-github-actions]] — Full Lab 5 walkthrough
- [[examples/ict2216-project-deployment-phases-9-12]] — EC2 deployment context (deploy.sh / deploy.ps1)
