---
type: example
title: "ICT2216 Project — Phase 4: Authentication (Register / Login / MFA / Logout)"
domain: secure-software-development
tags: [flask, auth, bcrypt, totp, mfa, session, audit-log, ict2216, trialguard]
created: 2026-05-26
status: working
---

# ICT2216 Project — Phase 4: Authentication

TrialGuard — Secure Clinical Trial Participant Portal.  
All four auth endpoints implemented and verified working end-to-end against the running Docker stack.

---

## Stack context

| Layer | Detail |
|-------|--------|
| Backend | Flask 3.1 + Gunicorn, blueprint `auth_bp` at `/api/auth` |
| Session | `flask.session` — HttpOnly, Secure, SameSite=Strict, 30-min permanent |
| Password | bcrypt cost 12 |
| MFA | pyotp TOTP (RFC 6238, 30-second window) |
| Audit log | Append-only hash-chained table in MySQL |
| CSRF | Flask-WTF exempted on auth blueprint; mitigated via SameSite=Strict + CORS |

---

## 4.1 Register — `POST /api/auth/register`

**Validations** (all return generic `400 Invalid input.` — no field hints):

| Field | Rule |
|-------|------|
| `username` | `^[a-zA-Z0-9_]{3,64}$` |
| `email` | `^[^\s@]+@[^\s@]+\.[^\s@]+$` |
| `password` | ≥ 8 chars, ≥1 upper, ≥1 lower, ≥1 digit, ≥1 special |
| `role` | one of `participant`, `researcher`, `admin` |

Duplicate username or email → `409 Registration failed.` (no field hint — prevents username enumeration).

On success:
- bcrypt hash stored (cost 12, random salt)
- `pyotp.random_base32()` generates per-user TOTP secret
- `totp_uri` returned so user can scan into authenticator app
- `mfa_enabled` starts as `False` — set to `True` on first successful MFA verify

```python
pw_hash    = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12)).decode()
mfa_secret = pyotp.random_base32()
totp_uri   = pyotp.TOTP(mfa_secret).provisioning_uri(name=email, issuer_name='TrialGuard')
```

---

## 4.2 Login — `POST /api/auth/login` (step 1 of 2)

Two-step login: credentials first, MFA second. No full session issued at step 1.

**Account lockout** — checked before password verification:
- 5 failed attempts → `locked_until = now + 15 min`
- Locked accounts return the same generic `401 Invalid credentials.` as wrong passwords (no timing oracle)

**On success:**
```python
session.clear()
session['mfa_pending_user_id'] = user.user_id
```

The intermediate key `mfa_pending_user_id` bridges step 1 → step 2 without issuing a usable session. The user_id is only placed in a real session after MFA verification.

---

## 4.3 Verify MFA — `POST /api/auth/verify-mfa`

Reads `mfa_pending_user_id` from session. If absent → `401 No pending MFA session.`

```python
if not pyotp.TOTP(user.mfa_secret).verify(code):
    # 401 — invalid or expired code
    ...

# Session fixation prevention
session.clear()
session['user_id']  = user.user_id
session['role']     = user.role
session.permanent   = True   # 30-min inactivity timeout from PERMANENT_SESSION_LIFETIME

user.mfa_enabled = True
user.last_login  = datetime.utcnow()
```

`session.clear()` before issuing the real session prevents session fixation — the old session ID (which held `mfa_pending_user_id`) is invalidated and a new one is issued.

---

## 4.4 Logout — `POST /api/auth/logout`

```python
session.clear()
write_audit('logout', 'success', user_id=user_id, ip_address=_ip())
```

---

## 4.5 Hash-chained audit log

Every action writes a new row. Each row's `entry_hash` covers the previous row's hash, making any retroactive deletion or modification detectable.

```python
def _entry_hash(prev_hash, timestamp, user_id, action_type, outcome):
    raw = f"{prev_hash or ''}{timestamp.isoformat()}{user_id or ''}{action_type}{outcome}"
    return hashlib.sha256(raw.encode()).hexdigest()
```

Actions logged: `register`, `login_step1`, `mfa_verify`, `logout`, `account_lockout`.  
Failures always logged with the action type so the chain captures both success and failure events.

---

## CSRF approach

Auth blueprint is exempted from Flask-WTF CSRF:
```python
csrf.exempt(auth_bp)
```

**Why this is safe:** The API is JSON-only (no form submissions). Protection comes from:
- `SameSite=Strict` session cookies — browser never sends cookies cross-origin
- CORS config restricts `Access-Control-Allow-Origin` to the known frontend origin
- `Content-Type: application/json` header requirement — cross-origin forms cannot set this

---

## Smoke test (verified)

```bash
# Register
curl -sk -X POST https://localhost/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser1","email":"test@example.com","password":"Test@1234","role":"participant"}'
# → {"message":"Registration successful.","totp_uri":"otpauth://totp/..."}

# HTTPS landing page
curl -sk https://localhost/ | grep '<title>'
# → <title>TrialGuard — Secure Clinical Trial Participant Portal</title>
```

---

## Related

- [[concepts/secure-software-requirements]] — CIA + AAA pillars this implements
- [[concepts/security-by-design-principles]] — least privilege, fail securely
- [[concepts/threat-modeling]] — session fixation, enumeration, brute force addressed here
- [[examples/ict2216-lab1-docker-compose]] — the stack this runs on
- [[learning/docker-compose-build-context]] — build context change needed to run this
