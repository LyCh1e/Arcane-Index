---
name: ict2216-project-deployment-phases-9-12
description: TrialGuard EC2 deployment — git archive SCP method, health checks, compliance report, daily backups, cert generation, sensitive-info cleanup from git history
metadata:
  type: project
---

# ICT2216 Project — Phases 9–12: Frontend Wiring, Hardening, and EC2 Deployment

## Phase 9 — Frontend Integration (verified 2026-05-30)

All React pages wired to live Flask backend via Playwright smoke test:
- Signup → TOTP QR displayed after registration
- MFA login → redirects by role (participant→/patient, researcher→/researcher, admin→/admin)
- ProtectedRoute guards → unauthenticated access redirects to /login
- Cross-role guard → participant at /admin redirects to /login
- Admin portal → live user list, suspend/activate, live audit log (hash-chained)
- Logout → clears server session (subsequent API calls return 401)

## Phase 10 — Security Hardening

### 10.1 Input Validation
- Field allowlists per endpoint (e.g. `_REGISTER_FIELDS = frozenset({'username','email','password','role'})`)
- Extra keys → 400 + `unexpected_input` audit entry
- Clinical data range bounds: `_MEASUREMENT_RANGES = {'heart_rate': (30, 220), ...}`
- ISO 8601 datetime enforced on `recorded_at`

### 10.2 HTTPS — Self-Signed Cert
Generate on **Linux/EC2** (not Windows — see [[learning/windows-openssl-strawberry-broken]]):
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /tmp/key.pem -out /tmp/cert.pem \
  -subj "/CN=medi.trialguard.com/O=TrialGuard/C=SG"
```
Cert is gitignored — push manually via SCP every time it changes.

### 10.3 Security Headers (nginx)
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "no-referrer" always;
add_header Content-Security-Policy "default-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self' data:;" always;
```

## Phase 11 — EC2 Deployment

### The Problem: Private Repo, No GitHub Access on EC2
EC2 instance cannot authenticate to GitHub for private repos. Solution: `git archive` + SCP.

```powershell
# Windows PowerShell — run from repo root
$PEM  = "<path\to\key.pem>"
$HOST = "<user>@<ec2-ip>"

# Fix key permissions first (once)
icacls $PEM /inheritance:r /grant:r "$env:USERNAME:F"

# Package and upload
git archive --format=tar HEAD -o "$env:TEMP\trialguard.tar"
scp -i $PEM "$env:TEMP\trialguard.tar" "${HOST}:~/trialguard.tar"

# Extract on EC2
ssh -i $PEM $HOST "mkdir -p ~/ICT2216-Secure-Software-Development && cd ~/ICT2216-Secure-Software-Development && tar xf ~/trialguard.tar"

# Copy .env (never committed) and certs (gitignored) separately
scp -i $PEM .env "${HOST}:~/ICT2216-Secure-Software-Development/.env"
ssh -i $PEM $HOST "sudo chown <user>:<user> ~/ICT2216-Secure-Software-Development/nginx/certs"
scp -i $PEM nginx\certs\cert.pem "${HOST}:~/ICT2216-Secure-Software-Development/nginx/certs/cert.pem"
scp -i $PEM nginx\certs\key.pem  "${HOST}:~/ICT2216-Secure-Software-Development/nginx/certs/key.pem"

# Deploy
ssh -i $PEM $HOST "cd ~/ICT2216-Secure-Software-Development && docker compose up --build -d"
```

### Gotchas Encountered
1. **nginx/certs dir owned by root** — Docker creates the host-side mount directory as root if it doesn't exist. Fix: `sudo chown <user>:<user> nginx/certs`. See [[learning/docker-volume-host-dir-created-as-root]].
2. **`chmod` fails on `:ro` mount** — backup.sh entrypoint used `chmod +x /backup.sh` but the script is mounted read-only. Fix: call `sh /backup.sh` instead. See [[learning/docker-ro-mount-chmod-fails]].
3. **Sensitive info committed** — username, IP, key filename accidentally included in a README commit. Fix: `git commit --amend` + `git push --force`. See [[learning/git-amend-remove-sensitive-push]].

### Verified Container Status (2026-05-30)
```
flask        Up (healthy)   0.0.0.0:8080->8080/tcp
pii_vault    Up (healthy)   8888/tcp
mysql        Up (healthy)   3306/tcp
vault_db     Up (healthy)   3306/tcp
mongodb      Up (healthy)   27017/tcp
nginx        Up             0.0.0.0:80->80, 0.0.0.0:443->443/tcp
db-backup    Up             (runs mysqldump every 24h)
```

HTTPS 200 OK ✅ | HTTP→HTTPS 301 ✅ | Security headers ✅ | `/api/health` → `{"status":"ok"}` ✅

## Phase 12 — Could Have Completions

### Health Checks (docker-compose.yml)
Flask/pii_vault use Python urllib one-liner — no curl needed in slim images:
```yaml
healthcheck:
  test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8080/api/health')"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```
nginx `depends_on` updated to `flask: condition: service_healthy`.

### Compliance Report Endpoint
`GET /api/admin/compliance-report` — requires `admin` role, returns:
```json
{
  "generated_at": "2026-05-30T...",
  "users": {"total": 5, "by_role": {"admin": 1, "participant": 3, "researcher": 1}},
  "trials": {"total": 2, "by_status": {...}, "by_risk_level": {...}},
  "participants": {"total": 3, "active": 2, "withdrawn": 1, "pii_purged": 1},
  "consents": {"total": 3, "active": 2},
  "audit_log": {"total_events": 47, "failure_events": 3}
}
```
Every export writes a `compliance_report_export` audit entry.

### Daily DB Backup Service
```yaml
db-backup:
  image: mysql:8.0
  entrypoint: >
    sh -c "while true; do sh /backup.sh; sleep 86400; done"
  volumes:
    - ./backup/backup.sh:/backup.sh:ro
    - db_backups:/backups
```
`backup.sh` dumps both MySQL databases, rotates to 7 most recent files.
Note: must use `sh /backup.sh` not `chmod +x /backup.sh && /backup.sh` — see [[learning/docker-ro-mount-chmod-fails]].
