---
name: ict2216-lab9-sonarqube
description: ICT2216 Lab 9 — Static analysis using SonarQube via Docker Compose (PostgreSQL backend), local scanner, and GitHub Actions integration
metadata:
  type: example
domain: secure-software-development
course: ICT2216
created: 2026-06-23
tags: [sonarqube, sast, static-analysis, docker-compose, github-actions, quality-gate, lab]
---

# ICT2216 Lab 9 — Static Analysis Using SonarQube

**Lab file:** `Lab9/X09 - SonarQube.pdf`
**Support files:** `Lab9/sonarqube-compose.yml`, `Lab9/sonarqube.yml`

## Lab Structure

| Step | Topic |
|------|-------|
| 3 | Spin up SonarQube via Docker Compose (+ PostgreSQL) |
| 4 | Create project in SonarQube UI, generate token, run local scanner |
| 5 | GitHub Actions workflow sending results to SonarQube dashboard |
| 6 | View analysis report in SonarQube UI |
| 7 | Fix Docker OOM issue |

## Step 3 — SonarQube via Docker Compose

```bash
docker-compose -f sonarqube-compose.yml up
```

Two containers: `sonarqube:latest` (port 9000) + `postgres:latest`. SonarQube connects to Postgres via JDBC. Four named volumes for data/extensions/logs/postgresql persistence.

- UI: `http://localhost:9000`
- Default credentials: `admin` / `admin`

## Step 4 — Create Project and Run Local Scanner

**UI flow:**
1. Projects → **Create a local project**
2. Set project display name, project key, main branch name
3. Next → **Use global settings**
4. Analysis method → **Locally**
5. **Generate a project token** (copy it — needed for scanner and GitHub secrets)
6. Select language/OS → copy the `sonar-scanner` command

**Run scanner via Docker (no local install needed):**

```bash
docker run --rm --network host \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli \
  -Dsonar.projectKey=<your-project-key> \
  -Dsonar.sources=/usr/src \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=<sonar-token>
```

**Dashboard shows:** Quality Gate (Passed/Failed), Security issues, Reliability issues, Maintainability issues, Coverage %, Duplications %, Security Hotspots count.

## Step 5 — GitHub Actions Integration

### Prerequisites
- SonarQube must be reachable via a **public domain** (not localhost) from GitHub Actions runners
- Two GitHub Secrets required:

| Secret | Value |
|--------|-------|
| `SONAR_TOKEN` | Token generated in SonarQube UI → My Account → Security |
| `SONAR_HOST_URL` | Public URL of your SonarQube instance |

### Workflow (`sonarqube.yml` → `.github/workflows/sonarqube.yml`)

```yaml
name: SonarQube Analysis

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  sonarqube:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 18
      - run: npm install
      - uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

On push: scanner runs → results sent to SonarQube dashboard.

## Step 6 — View Report

```
http://localhost:9000/dashboard?id=<your-project-key>
```

## Step 7 — Docker OOM Fix

SonarQube is memory-hungry. If the container dies with OOM:

```bash
docker run --memory=3g <rest-of-command>
```

## SonarQube vs ESLint (Lab 8 comparison)

| Feature | ESLint (Lab 8) | SonarQube (Lab 9) |
|---------|---------------|-------------------|
| Analysis type | Linting + style + security plugins | Deep semantic SAST |
| Report format | SARIF → GitHub Code Scanning | SonarQube Dashboard |
| Language support | JS/TS (primarily) | 25+ languages |
| Setup complexity | npm package | Docker Compose + scanner |
| CI integration | GitHub Action uploads SARIF | GitHub Action pushes to SonarQube |
| Security focus | Plugins required | Built-in rules + Quality Gates |

## Related

- [[examples/ict2216-lab8-static-code-analysis]] — Lab 8: ESLint + SARIF (lighter SAST, same pipeline)
- [[concepts/github-actions-cicd]] — workflow anatomy; secrets; job structure
- [[concepts/docker-compose]] — Docker Compose patterns used here
- [[resources/owasp-dependency-check]] — complementary SCA tool (Lab 6)
