---
type: example
status: established
created: 2026-07-23
updated: 2026-07-23
name: ict2216-practical-test-secure-webapp
description: ICT2216 Practical Test — Flask HTTPS login app, Postgres breach-password check, Gitea, SonarQube, ESLint, and a self-hosted Gitea Actions CI/CD pipeline, all in one docker-compose stack
metadata:
  type: example
domain: secure-software-development
course: ICT2216
tags: [flask, docker-compose, gitea, act-runner, sonarqube, eslint, csrf, owasp-c7, ci-cd, dood]
---

# ICT2216 Practical Test — Secure Web App + Full DevSecOps Stack

A single local `docker-compose.yml` grew, feature-request by feature-request, into a complete DevSecOps loop: a Flask app hardened per OWASP Proactive Control C7, its own git host, its own SAST scanner, and a CI/CD pipeline that actually runs on a self-hosted Gitea Actions runner.

## Final Stack (one `docker-compose.yml`)

| Service | Role |
|---|---|
| `web` | Flask app, HTTPS on 443→8443, non-root |
| `db` | Postgres — app users table + breached-password hash table |
| `db-init` | One-shot loader: SHA-1-hashes a 100k NCSC password list into `breached_passwords` |
| `gitea` | Self-hosted git + web UI, port 3001 |
| `act-runner` | Gitea Actions runner (DooD) |
| `sonarqube` + `sonarqube-db` | SAST dashboard, dedicated Postgres |
| `sonarqube-proxy` | nginx TLS termination in front of SonarQube (port 9000/9001) |
| `sonarqube-init` | One-shot: waits for SonarQube, changes default `admin/admin` password via API |

## Security Features Implemented (OWASP Proactive Control C7 — Secure Digital Identity)

- **Password hashing**: PBKDF2-SHA256, 600k iterations (`werkzeug.security.generate_password_hash`), never the plaintext env var compared directly
- **Breach-password check**: submitted passwords are SHA-1-hashed and checked against a `breached_passwords` table loaded from a public NCSC password-frequency list — same convention as Have I Been Pwned's k-anonymity API (SHA-1 is fine here; it's a lookup key, not a storage hash — see the `# NOSONAR` justification in `app.py`)
- **Account lockout**: 5 failed attempts → 15 minute lockout, tracked per-IP in memory
- **CSRF protection**: `Flask-WTF`'s `CSRFProtect(app)` + hidden `csrf_token()` field in every POST form. Flask-WTF also validates the `Referer` header on HTTPS requests — a real browser sends this automatically on form submit, but `curl`/`requests` calls in tests must set it explicitly or the request 400s with "The referrer header is missing."
- **Non-root containers**: every custom Dockerfile (`web`, `db-init`, `sonarqube-init`, `sonarqube-proxy`) creates and switches to a non-root user. The one wrinkle: binding port 443 requires `CAP_NET_BIND_SERVICE` as root, so the app listens on **8443 internally** and Docker's port mapping (`443:8443`) does the privileged-port translation instead.
- **Minimum password length** (8 chars) enforced both client-side (`minlength`) and server-side

## SonarQube: Local Scan, Then Fix the Findings

Ran a real scan via `sonarsource/sonar-scanner-cli` against the local instance (`docker run --network <project>_default ... -Dsonar.host.url=http://sonarqube:9000`). Findings and fixes:

| Finding | Fix |
|---|---|
| 3× CSRF hotspot (mixed GET/POST routes, no CSRF protection) | Added Flask-WTF `CSRFProtect` |
| 4× "Docker image runs as root" | Added `USER <non-root>` to every Dockerfile |
| 2× "hashing data" (SHA-1 usage) | Inline comment + `# NOSONAR` justifying breach-check use, not storage |
| 6× hardcoded-password-literal hotspots in test files | Marked Reviewed/Safe via API (`api/hotspots/change_status`) — dummy test credentials, not real secrets |

After the fixes: 0 bugs, vulnerabilities dropped from 6→2 (both `verify=False` in test files, intentional against a self-signed cert), hotspots 13→6 (remainder = accepted false positives, marked Safe).

## Gitea Actions CI/CD: 5 Jobs, One Local Runner

Pipeline (`.gitea/workflows/ci.yml`): `dependency-check` (pip-audit) → `eslint-security-scan` (ESLint + `eslint-plugin-security`, flat config) → `integration-test` (pytest + requests) → `ui-test` (Playwright, real browser form submission) → `sonarqube-scan`.

Registering and running an actual `act_runner` (not just writing the YAML) surfaced a cluster of Docker-outside-of-Docker (DooD) networking gotchas — see [[learning/gitea-act-runner-dood-networking]] for the full list (duplicate `docker.sock` mount, isolated per-job networks, `127.0.0.1` meaning the wrong container, bind mounts silently becoming empty directories, and a buggy `${{ env.X }}` string-interpolation bug in the runner's expression evaluator).

`pip-audit` in the `dependency-check` job caught a real CVE — Flask 3.0.3 had `PYSEC-2026-2151`, fixed by bumping to 3.1.3. This is the whole point of running the scan for real instead of just writing the workflow file and calling it done.

## Related

- [[concepts/docker-compose]] — DooD gotchas section added from this session
- [[concepts/github-actions-cicd]] — Gitea Actions as a self-hosted GH-Actions-compatible alternative
- [[learning/gitea-act-runner-dood-networking]] — full gotcha list with fixes
- [[resources/gitea-and-act-runner]] — Gitea + act_runner setup reference
- [[examples/ict2216-lab9-sonarqube]] — the original SonarQube Docker Compose lab this build extended
- [[concepts/secure-input-validation]], [[concepts/secure-deployment-practices]] — OWASP C7 background
