---
name: ict2216-lab6-owasp-dependency-check
description: ICT2216 Lab 6 — Integrating OWASP Dependency Check locally via Docker and into GitHub Actions CI/CD pipeline
metadata:
  type: example
domain: secure-software-development
course: ICT2216
created: 2026-06-23
tags: [owasp, dependency-check, sca, cve, docker, github-actions, lab]
---

# ICT2216 Lab 6 — Integrating OWASP Dependency Check

**Lab file:** `Lab6/X06-Integrating OWASP Dependency Check.pdf`

## Lab Structure

| Step | Topic |
|------|-------|
| 3.3 | Run OWASP Dependency Check locally via Docker |
| 3.4 | Add OWASP Dependency Check to GitHub Actions workflow |
| 4 | Explore alternative tools: Dependabot / Renovate |

## Pre-requisites

- Docker Desktop (development laptop)
- Docker Engine (Team VM)
- GitHub account
- Team project web app

## Step 3.3 — Local Scan via Docker

### Pull the image

```bash
docker pull owasp/dependency-check
```

### Run the scan (Linux/macOS)

```bash
# Set to your project root
export pwd=/home/cloak/site/

docker run --rm \
  -v $pwd:/src \
  -v $pwd/odc-reports:/report \
  -v $pwd/odc-data:/usr/share/dependency-check/data \
  owasp/dependency-check \
  --scan /src \
  --format "HTML" \
  --out /report
```

Report is saved to `odc-reports/dependency-check-report.html`.

**Windows adaptation:** Replace `export pwd=...` + `$pwd` with `$env:PWD = "C:\path\to\project"` + `$env:PWD` in PowerShell, or use absolute paths directly in the `-v` flags.

## Step 3.4 — GitHub Actions Integration

Create `.github/workflows/dependency-check.yml`:

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

After committing, the workflow runs on every push/PR. View the report under **Actions → Run → Artifacts → Dependency-Check-Report** on GitHub.

## Step 4 — Alternative Tools

### Dependabot

- Checks for **outdated** dependencies and auto-creates PRs to update them
- Works with: npm, Maven, Gradle, Composer, pip, etc.
- Only checks against known registries (npm, PyPI, Maven Central) — not a CVE scanner

Enable via `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"   # or "maven", "gradle", "pip"
    directory: "/"
    schedule:
      interval: "daily"
```

### Renovate

- Similar to Dependabot but with finer scheduling and grouping control
- Also auto-raises PRs for dependency updates

## Key Concepts

| Term | Meaning |
|------|---------|
| **SCA** | Software Composition Analysis — scanning third-party dependencies for known vulnerabilities |
| **CPE** | Common Platform Enumeration — standardised identifier used to match software to NVD entries |
| **CVE** | Common Vulnerabilities and Exposures — public list of known security vulnerabilities |
| **NVD** | National Vulnerability Database — NIST database of CVEs with CVSS scores |
| **OWASP C2** | Proactive Control: Leverage Security Frameworks and Libraries (keep them updated) |

## Related

- [[resources/owasp-dependency-check]] — full tool reference with all run modes
- [[concepts/github-actions-cicd]] — CI/CD pipeline; where the dependency scan job fits
- [[concepts/vulnerability-tracking-frameworks]] — CVE/CVSS/NVD context
- [[examples/ict2216-lab5-github-actions]] — Lab 5: GitHub Actions foundation this lab builds on
