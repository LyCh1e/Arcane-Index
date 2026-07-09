---
type: concept
address: c-000098
title: "Secure Deployment Practices"
domain: secure-software-development
complexity: high
created: 2026-07-02
updated: 2026-07-02
tags: [concept, docker, github-secrets, security-logging, component-security, owasp, devops, devsecopss, secure-coding]
related:
  - concepts/secure-input-validation
  - concepts/secure-design-implementation
  - concepts/owasp-top-10
---

# Secure Deployment Practices

Covers the operational security controls that protect applications during build, deployment, and runtime. These are the practical implementations of OWASP Proactive Controls C6 (Component Security), C9 (Security Logging and Monitoring), and the DevSecOps toolchain for secrets management and containerisation.

---

## Component Security (OWASP C6)

**The problem:** Most application code is not original — it is primarily composed of third-party libraries and frameworks. Vulnerable dependencies introduce risk regardless of how clean the application code itself is.

**OWASP Proactive Control C6: Keep Your Components Secure**

### Identify Trusted Dependencies (Before Adding)

Before bringing a library into your project, assess:
- Is it actively maintained? (Recent commits, responsive issue tracker)
- Does it have a security track record? (Few CVEs, fast patch response)
- How many open-source projects use it? (Higher adoption = more audit eyes)
- Does it pull in a large transitive dependency graph? (More surface area)

**Key principle:** Where possible, use security features **already embedded in frameworks you are already using** rather than adding yet more third-party libraries. Each additional dependency is additional attack surface.

### Monitor and Update Continuously

Third-party components receive new CVE disclosures regularly. Your dependency versions must be:
- **Tracked** — know exactly what version of every dependency you are running
- **Monitored** — receive notifications when a CVE is disclosed against a version you use
- **Updated** — patch in a timely fashion; prioritise by CVSS severity

**Version pinning — the debate:**

| Position | Argument |
|----------|----------|
| **Pin versions** | Prevents unexpected breaking changes; safe if test coverage is insufficient |
| **Update freely** | Delays leave you on a vulnerable version; minor updates are almost always safe; sufficient automated tests catch regressions |

Recommended policy (balancing both):
- **Patch and minor updates** (e.g., `1.2.3 → 1.2.4`, `1.2.x → 1.3.0`): allow CI/CD to auto-apply — these are almost always bug fixes and security patches
- **Major updates** (e.g., `1.x → 2.0`): require manual review — may introduce breaking API changes that automated tests may not cover

The underlying principle: **automated test coverage is the prerequisite for safe automatic updates**. If your test suite does not cover sufficient functionality, version pinning is the safer fallback. If it does, frequent small updates are more secure than infrequent large ones.

### Key Tools

| Tool | Purpose |
|------|---------|
| **OWASP Dependency-Check** | SCA — inspects project dependencies, generates CPE/CVE report against NVD |
| **OWASP Dependency-Track** | Monitors SBOM (Software Bill of Materials) files for new CVEs on a schedule |
| **Retire.JS** | Scans JavaScript libraries for known vulnerabilities |
| **Renovate / Dependabot** | Automated dependency-update pull requests |
| **Harbor** | Open-source container image registry with RBAC and built-in vulnerability scanning |

**How OWASP Dependency-Check works:**

```
1. Inspect dependency manifests (requirements.txt, package.json, pom.xml)
   ↓
2. Collect evidence about each: name, version, CPE identifier
   ↓
3. Cross-reference against NVD (National Vulnerability Database)
   ↓
4. Generate report: dependency → CVE → CVSS score → reference URL
   ↓
5. Auto-update: initial download 10+ min; subsequent updates are small JSON deltas
```

**SBOM (Software Bill of Materials):** A formal, machine-readable inventory of all components in a software product — first-party code, third-party libraries, and their transitive dependencies. Required by US Executive Order 14028 for software supplied to federal agencies. Enables automated CVE monitoring via Dependency-Track.

---

## Security Logging and Monitoring (OWASP C9)

Covers the **implementation** of security logging. Design-level decisions (what to log, log schema, retention) are in [[concepts/secure-design-implementation#Accountability Design]].

**OWASP Proactive Control C9: Implement Security Logging and Monitoring**

### Definitions

| Term | Meaning |
|------|---------|
| **Logging** | Recording events for debugging and diagnostics |
| **Security logging** | Recording security-relevant events at runtime (authentication, authorisation changes, high-value transactions) |
| **Monitoring** | Live review of logs using automation; generates alerts |

### The Four Implementation Rules

**Rule 1 — Encode and validate before logging (prevent log injection)**

Log injection: an attacker inserts fake log entries — newlines, special characters, or control sequences — to confuse forensic analysts or corrupt log structure.

```python
# Vulnerable: raw user input in log
logging.info(f"Login attempt for: {username}")
# Attack: username = "admin\nINFO: Login successful for: admin"
# ← inserts a fake success log entry

# Safe: sanitise before logging
safe_username = username.replace('\n', ' ').replace('\r', ' ')
logging.info("Login attempt for: %s", safe_username)
# Or: use a structured logger that serialises to JSON — newlines cannot break JSON fields
```

**Log injection → reverse shell (why this matters beyond forensic contamination):**

In Ethical Hacking courses, IS students learn to use log injection as a vector for obtaining a reverse shell:
1. Attacker identifies that user input is written to a log file without sanitisation
2. Attacker injects a newline followed by a shell command payload
3. If the log is processed by a script, aggregator, or SIEM that evaluates log content (e.g., a shell script that `tail`s the log and pipes to a processor), the injected command executes
4. The attacker then connects back on the reverse shell port
5. Finally, the attacker deletes or modifies the log entry to remove the audit trail — which is why log integrity protection (append-only storage, centralised forwarding) is a mandatory companion to log encoding

This sequence illustrates why sanitising before logging is a **security control**, not just a data quality measure.

**Rule 2 — Never log sensitive information**

The following must **never** appear in log files:

- Passwords or password hashes
- Session tokens or JWT contents
- Credit card numbers, CVVs
- National ID / NRIC / passport numbers
- Full API keys or secrets
- Any PII beyond what is strictly necessary for forensic attribution

> **The OpenAI Codex case study:** Default `TRACE`-level logging caused ~37 TB written in 21 days to an SQLite file, wearing out consumer SSDs and logging raw WebSocket payload bodies — including potentially sensitive content. Always set the **minimum necessary log level** for production. `TRACE` and `DEBUG` are for development only.

```python
# Log level hierarchy (most verbose → least)
# TRACE → DEBUG → INFO → WARNING → ERROR → CRITICAL

# Development: DEBUG or INFO
# Staging: INFO or WARNING
# Production: WARNING or ERROR (minimum necessary)
logging.basicConfig(level=logging.WARNING)   # production setting
```

**Rule 3 — Protect log integrity**

Attackers who compromise a system will attempt to modify or delete logs to cover their tracks.

| Protection | Implementation |
|-----------|----------------|
| File permissions | Logs owned by the application user; not world-writable |
| Append-only / WORM storage | Cloud log services (AWS CloudWatch, Azure Monitor) are write-once by default |
| Log rotation | Rotate and compress old logs to prevent tampering via overwrite |
| Cryptographic signing | Sign log files so tampering is detectable |

**Rule 4 — Forward logs to a centralised, secure logging service**

- Distributed systems: logs from all nodes must be centralised so a single compromised node cannot destroy evidence
- Central aggregation enables correlation across services (one log event rarely tells the full story)
- Enables alerting: set thresholds on login failures, error rates, privilege escalations

**Centralised logging stack options:**
- ELK stack (Elasticsearch + Logstash + Kibana)
- AWS CloudWatch Logs
- Google Cloud Logging
- Splunk / Datadog (commercial)

> **Log4Shell reminder (CVE-2021-44228):** The Apache Log4J library itself had a critical RCE vulnerability exploited at massive scale in 2021. Your logging library is a dependency — apply the same component security hygiene to it as to any other library. Check that `log4j-core` is ≥ 2.17.1; if using Java, prefer `logback` or `slf4j` with a patched Log4J binding.

### Logging Libraries

| Library | Runtime | Notes |
|---------|---------|-------|
| **Log4J** | Java | Widely used; had CVE-2021-44228; ensure ≥ 2.17.1 |
| **Logback** | Java | Successor to Log4J 1.x; considered safer default |
| **winston** | Node.js | Popular, flexible, multiple transports |
| **Pino** | Node.js | Extremely fast, low-overhead, structured (JSON) output |
| **structlog** | Python | Structured logging with context binding |

---

## Secrets Management — GitHub Secrets

**The question:** How do you securely store database credentials, API keys, and other secrets used in your application and CI/CD pipeline?

**Never do this:**

```dockerfile
# Dockerfile — WRONG: secret baked into image layer
ENV DB_PASSWORD=mysecretpassword123
ARG DB_HOST=prod.db.example.com
```

```yaml
# docker-compose.yml — WRONG: hardcoded in committed file
services:
  db:
    environment:
      POSTGRES_PASSWORD: mysecretpassword123
```

Anything committed to a repository — even a private one — can be extracted from git history indefinitely. Private repositories have been breached (see LastPass case study).

### GitHub Secrets

GitHub Actions provides **encrypted environment variables** (Secrets):

| Property | Detail |
|----------|--------|
| Storage | Encrypted at rest in GitHub infrastructure |
| Injection | Decrypted and injected as environment variables at workflow runtime |
| Log masking | Automatically masked in all workflow logs — never visible |
| Fork isolation | **Not passed** to workflows triggered by pull requests from forks (security feature) |
| Types | Repository secrets (all workflows) or Environment secrets (scoped to staging/production) |

```yaml
# .github/workflows/deploy.yml — CORRECT
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy with database credentials
        env:
          DB_HOST:     ${{ secrets.DB_HOST }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
          API_KEY:     ${{ secrets.THIRD_PARTY_API_KEY }}
        run: ./deploy.sh
```

**What to store as Secrets:**
- Database connection strings, hostnames, and passwords
- API keys and tokens (AWS credentials, third-party service keys, payment processor keys)
- TLS certificates and private keys used in deployment
- Any credential referenced in `docker-compose.yml` or Dockerfile

### Local Development — `.env` Files

For local development, use a `.env` file (never committed):

```bash
# .env  ← in .gitignore
DB_HOST=localhost
DB_PASSWORD=localdevpassword
```

```python
# Python — load .env with python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()   # reads .env if present; environment variables take priority
db_host = os.getenv("DB_HOST")
```

```
# .gitignore
.env
.env.*
!.env.example   # ← commit a template with dummy values only
```

---

## Docker Security

### Docker Development Workflow

```
Write code → Dockerfiles → docker build → docker-compose.yml → docker-compose up → test → git push (triggers CI/CD → push to registry)
```

Each stage introduces specific security risks.

### Dockerfile Security Best Practices

```dockerfile
# WRONG — insecure Dockerfile
FROM node:latest                        # 1. Unpinned tag
RUN npm install                         # 2. No lockfile; installs latest versions
COPY . .                                # 3. Copies .env, .git, credentials
ENV DB_PASSWORD=mysecretpassword        # 4. Secret in image metadata (visible via docker inspect)
                                        # 5. Runs as root (no USER instruction)

# CORRECT — secure Dockerfile
FROM node:18.17.1-alpine                # 1. Pinned exact version
RUN apk add --no-cache python3 g++ make

WORKDIR /app

COPY package*.json ./
RUN npm ci --production                 # 2. Uses lockfile; only installs declared versions

COPY . .                                # 3. .dockerignore excludes sensitive files

EXPOSE 3000

USER node                               # 5. Non-root user at runtime
CMD ["node", "server.js"]
```

```
# .dockerignore
.env
.env.*
.git
*.md
node_modules   # don't copy — npm ci installs inside container
credentials.json
*.pem
*.key
```

**Security rules — Dockerfile:**

| Rule | Reason |
|------|--------|
| Pin base image to an exact version tag | `latest` changes without warning; reproducibility and auditability require a fixed digest |
| Run as a non-root user (`USER`) | If the container is compromised, the attacker has limited OS privileges |
| Use multi-stage builds | Build secrets, intermediate build tools, and source code can be excluded from the final runtime image |
| Use `.dockerignore` | Prevents accidental inclusion of `.env`, `.git`, credentials, and other sensitive files |
| Never use `ENV` or `ARG` for secrets | Values are visible in image metadata (`docker inspect`, `docker history`) and in any image layer |

### Docker Compose Security Best Practices

```yaml
# docker-compose.yml — CORRECT
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db
      - DB_PASSWORD=${DB_PASSWORD}      # ← substituted from .env (dev) or host env (CI)
    depends_on:
      - db
    networks:
      - internal                        # ← not exposed to external network

  db:
    image: postgres:15.4-alpine         # ← pinned version
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - internal                        # ← not directly internet-accessible
    # NO ports: section — DB not accessible outside the internal network

volumes:
  postgres_data:

networks:
  internal:
    driver: bridge
```

**Security rules — Docker Compose:**

| Rule | Reason |
|------|--------|
| Use `${VAR}` substitution, not hardcoded values | Values come from `.env` (dev) or GitHub Secrets (CI); compose file stays safe to commit |
| Add `.env` to `.gitignore` | Prevents accidental credential commit |
| Apply network segmentation | Only expose ports that must be reachable externally; database containers should be on internal networks only |
| Use named volumes for persistent data | More portable and auditable than bind mounts; permissions are more predictable |
| Pin image versions | Same reason as Dockerfile — reproducibility and auditability |

---

## Database Security Checklist (OWASP Secure Coding Practices)

| Control | Implementation |
|---------|---------------|
| Parameterised queries | See [[concepts/secure-input-validation#Defence 1 — Prepared Statements]] |
| Least-privilege DB account | Application user: SELECT/INSERT/UPDATE only; no DROP, CREATE, or GRANT |
| No hardcoded credentials | Store in environment variables or secrets vault; never in source code |
| Encrypt connection strings | Use SSL/TLS for DB connections; validate server certificate |
| Close connections promptly | Use connection pooling; release connections in `finally` blocks |
| Remove default credentials | Change all default DB admin passwords at setup; enforce strong passwords |
| Disable unnecessary DB features | Remove sample schemas, unused stored procedures, utility packages |
| Separate credentials per trust level | App user ≠ admin user ≠ read-only reporting user |

---

## File Upload Security Checklist (OWASP Secure Coding Practices)

| Control | Why |
|---------|-----|
| Require authentication before upload | Unauthenticated upload is an open door for malware staging |
| Validate by file header, not extension | Extension is trivially renamed; magic bytes (file signature) are harder to fake |
| Restrict allowed file types to business need | A blog platform needs images — not `.php`, `.exe`, or `.sh` |
| Do not store uploads in the web root | Files in the web root may be directly executed by the web server |
| Disable execution on upload directories | Set `noexec` on the filesystem mount; configure web server to deny execution |
| Scan uploads for malware | Integrate a virus scanner (ClamAV, cloud AV API) on ingest |
| Never send the absolute server path to the client | Path disclosure enables directory traversal and targeted attacks |
| Detect and reject ZIP bombs | ZIP bombs (decompression bombs) are small compressed files that expand to enormous sizes — a 42 KB file can decompress to 4.5 PB, exhausting disk space and RAM (DoS). Implement decompressed-size limits and nested-compression-ratio checking before extracting any archive |

**ZIP bomb (CPOM attack) detail:**

When your application accepts ZIP or archive uploads and decompresses them automatically:
- Check the reported uncompressed size in the ZIP metadata before extracting — reject if it exceeds a safe threshold
- Check the compression ratio — legitimate files rarely compress beyond 95%; ratios above 99% are suspicious
- Recursively check nested archives (ZIP within ZIP within ZIP) — each layer compounds the decompression ratio
- Set a hard limit on the total decompressed output size and abort extraction when the limit is reached

Libraries: Python `zipfile` does not protect against ZIP bombs by default — implement manual size tracking. The `defusedxml` pattern (safe-by-default parsing) does not exist for ZIP; you must add checks explicitly.

---

## OWASP Proactive Controls Reference (C1–C10)

| Control | Focus Area | Primary Concept Page |
|---------|-----------|---------------------|
| C1 — Implement Access Control | RBAC, least privilege, deny by default | [[concepts/secure-design-implementation]] |
| C2 — Use Cryptography to Protect Data | TLS, AES, bcrypt, no roll-your-own | [[concepts/secure-design-implementation]] |
| C3 — Validate All Input & Handle Exceptions | Allow-list, ReDoS, SQL injection prevention | [[concepts/secure-input-validation]] |
| C4 — Address Security from the Start | Threat modelling, secure SDLC | [[concepts/secure-design-implementation]] |
| C5 — Secure By Default Configurations | No default credentials, minimal attack surface | This page |
| C6 — Keep Your Components Secure | SCA, SBOM, CVE monitoring, Dependency-Check | This page |
| C7 — Secure Digital Identities | MFA, passwordless, session management | [[concepts/secure-design-implementation]] |
| C8 — Leverage Browser Security Features | CSP, HSTS, SameSite cookies | [[concepts/owasp-top-10]] |
| C9 — Implement Security Logging and Monitoring | Log injection, PII exclusion, centralisation | This page |
| C10 — Stop Server-Side Request Forgery | SSRF prevention, URL allow-listing | [[concepts/owasp-top-10]] |

---

## See Also

- [[concepts/secure-input-validation]] — input validation, ReDoS, SQL injection prevention in depth
- [[concepts/secure-design-implementation]] — cryptography design, authentication, authorisation, accountability
- [[concepts/owasp-top-10]] — the vulnerability risk list; proactive controls are the corresponding defences
- [[sources/ICT2216-lecture-7-secure-coding]] — source lecture
