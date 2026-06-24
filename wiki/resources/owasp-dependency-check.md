---
type: resource
status: established
created: 2026-06-23
updated: 2026-06-23
name: owasp-dependency-check
description: OWASP Dependency-Check — SCA tool that scans project dependencies for publicly disclosed CVE vulnerabilities via CPE matching; Docker and GitHub Actions support
metadata:
  type: reference
domain: secure-software-development
tags: [owasp, dependency-check, sca, cve, cpe, docker, github-actions, tool]
---

# OWASP Dependency-Check

Free, open-source **Software Composition Analysis (SCA)** tool. Scans a project's third-party dependencies to detect publicly disclosed vulnerabilities by matching them against the National Vulnerability Database (NVD) using **Common Platform Enumeration (CPE)** identifiers. Generates reports linking to CVE entries.

Addresses **OWASP Top 10 Proactive Control C2: Leverage Security Frameworks and Libraries** — keeping dependencies up to date with automated scanning.

## Run Modes

| Mode | How | Output |
|------|-----|--------|
| **Docker (local)** | `docker run owasp/dependency-check` | HTML/JSON/XML report on disk |
| **GitHub Actions** | `dependency-check/Dependency-Check_Action@main` | Artifact uploaded to Actions run |
| **CLI (standalone)** | `dependency-check.sh --scan . --format HTML` | HTML report on disk |
| **Maven/Gradle plugin** | Plugin block in `pom.xml` / `build.gradle` | Report in `target/` or `build/` |

## Docker Usage

```bash
docker pull owasp/dependency-check

# Linux / macOS — replace path with your project root
export pwd=/home/user/myproject/

docker run --rm \
  -v $pwd:/src \
  -v $pwd/odc-reports:/report \
  -v $pwd/odc-data:/usr/share/dependency-check/data \
  owasp/dependency-check \
  --scan /src \
  --format "HTML" \
  --out /report
```

Report lands at `odc-reports/dependency-check-report.html`.

**Volume breakdown:**

| Volume mount | Purpose |
|---|---|
| `$pwd:/src` | Project source to scan |
| `$pwd/odc-reports:/report` | Where the report is written |
| `$pwd/odc-data:/usr/share/dependency-check/data` | NVD data cache (avoids re-download on re-runs) |

## GitHub Actions Workflow

```yaml
name: OWASP Dependency Check

on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Run OWASP Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: "MyWebApp"
          path: "."
          format: "HTML"
          out: "dependency-check-report"

      - name: Upload Report
        uses: actions/upload-artifact@v4
        with:
          name: Dependency-Check-Report
          path: dependency-check-report
```

The report is downloadable from the **Artifacts** section of the GitHub Actions run.

## Comparison: Dependency Check Tools

| Tool | Approach | Auto-PRs | CVE database | Best for |
|------|----------|----------|-------------|---------|
| **OWASP Dependency-Check** | CPE → NVD matching | No | NVD (NIST) | Known CVE detection, audit reports |
| **Dependabot** | Registry version check | Yes | GitHub Advisory | Auto-updating outdated packages |
| **Renovate** | Registry version check | Yes | Multiple | Fine-grained update scheduling |

### Dependabot Configuration (`.github/dependabot.yml`)

```yaml
version: 2
updates:
  - package-ecosystem: "npm"   # or "maven", "gradle", "pip", "composer"
    directory: "/"
    schedule:
      interval: "daily"
```

Dependabot only checks against known registries (npm, PyPI, Maven Central) — it does not scan for CVEs directly; it raises PRs to update to newer versions which may patch vulnerabilities.

## Related

- [[concepts/github-actions-cicd]] — CI/CD pipeline anatomy; where this fits in the pipeline
- [[concepts/vulnerability-tracking-frameworks]] — CVSS, CVE, CWE, NVD context
- [[examples/ict2216-lab6-owasp-dependency-check]] — Lab 6 walkthrough
