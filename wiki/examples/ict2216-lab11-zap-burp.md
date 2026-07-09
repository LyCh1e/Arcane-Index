---
type: example
status: established
created: 2026-07-09
updated: 2026-07-09
name: ict2216-lab11-zap-burp
description: ICT2216 Lab 11 — Vulnerability assessment with OWASP ZAP and fuzz testing with Burp Suite against DVWA
metadata:
  type: example
domain: secure-software-development
course: ICT2216
tags: [owasp-zap, burp-suite, dast, fuzzing, dvwa, intruder, vulnerability-assessment, lab]
---

# ICT2216 Lab 11 — Vulnerability Assessment with OWASP ZAP & Fuzzing with Burp Suite

**Lab files:** `Lab11/X11a - Vulnerability Assessment with OWASP ZAP.pdf`, `Lab11/X11b - Fuzzing with Burp Suite.pdf`
**Target:** DVWA (Damn Vulnerable Web Application), hosted locally via XAMPP — reused across both parts
**Concept reference:** [[concepts/security-testing-and-verification]] (DAST Tools section)

## Lab Structure

| Part | Tool | Technique |
|------|------|-----------|
| X11a | OWASP ZAP | Automated Scan (spider + passive + active scan) |
| X11b | Burp Suite Community | Intruder (Cluster bomb fuzzing + Grep-Extract) |

## Part A — OWASP ZAP

**Setup:** Install ZAP (https://www.zaproxy.org/); clone/download DVWA from https://github.com/digininja/DVWA (only the official repo is supported); host on XAMPP web root; initialise via the setup page; confirm `http://localhost/login.php` loads.

**Workflow:**
1. ZAP → **Automated Scan** → enter `http://localhost` as target
2. Traditional spider (fast, HTML-only) vs Ajax spider (slower, needed for JS-generated links) — traditional was sufficient for DVWA
3. **Attack** → spider crawls, passive scan runs on every page found, then active scan attacks all discovered pages/params
4. **Alerts** tab surfaces findings, e.g.: Directory Browsing, X-Frame-Options Header Not Set, Absence of Anti-CSRF Tokens, Cookie No HttpOnly Flag, Cookie Without SameSite Attribute, Server Leaks Info via X-Powered-By, X-Content-Type-Options Header Missing, Loosely Scoped Cookie
5. **Report → HTML** exports a Summary-of-Alerts table (by risk level) + per-finding Alert Detail section

## Part B — Burp Suite Intruder

**Setup:** Install Burp Suite Community Edition; reuse DVWA from Part A; clone fuzzing wordlists from https://github.com/1N3/IntruderPayloads (Windows clone can error — works on Linux).

**Key gotcha:** Burp must proxy the browser traffic, so DVWA must be accessed via the machine's **IP address**, not `localhost` — a proxy can't intercept loopback-only traffic in the same way reliably across all setups, and the lab explicitly calls this out.

**Workflow:**
1. Browser → manual proxy `127.0.0.1:8080` (Burp's default listen port)
2. Submit any login attempt on DVWA (`a`/`a`) so Burp captures the POST to `login.php`
3. **Action → Send to Intruder**
4. **Positions** tab: **Clear §** removes all auto-highlighted fields, then manually `Add §` around just the `username` and `password` values — fuzzing every field at once would be noisy/pointless here
5. **Attack type = Cluster bomb** — tries every (username, password) combination from two independent payload sets, unlike Sniper (single set) or Pitchfork (lockstep pairing)
6. **Payloads** tab: payload set 1 (username) = `passwords_quick.txt`; payload set 2 (password) = same file (reused for simplicity — a real assessment would use a username list for set 1)
7. **Start attack** — with two ~28-entry sets, Cluster bomb produces ~784 requests (28×28), taking a while
8. **Grep-Extract** (Options tab): captured the `Location:` response header into its own results column. Failed logins redirect to `login.php`; a successful login redirects to `index.php` — sortable in one column instead of opening every response
9. Sorted result: `admin` / `password` → `Location: index.php` → confirmed valid credentials
10. Verified manually: proxy off, logged into DVWA with `admin`/`password` → success

## Why Grep-Extract Matters

Without it, confirming a Cluster bomb result against ~800 rows means opening each response individually to check the `Location:` header. Grep-Extract turns an O(n) manual inspection into a one-time config + a sort — the same "turn qualitative inspection into a filterable column" pattern is reusable for any Intruder attack where success/failure isn't visible from `Status`/`Length` alone (e.g. same response length for both outcomes, which defeats length-based heuristics).

## Legal Note

**Both parts stress: scanning/fuzzing a site without authorised permission is a criminal offence.** All testing here targets a locally hosted DVWA instance the student controls — never point ZAP or Burp Intruder at a third-party target without written authorisation.

## Related

- [[concepts/security-testing-and-verification]] — DAST Tools section (ZAP vs Burp comparison, attack-type reference), WSTG/ASVS framing these tools operationalise
- [[examples/ict2216-lab9-sonarqube]] — SAST counterpart (static, not dynamic, analysis)
- [[examples/ict2216-lab6-owasp-dependency-check]] — SCA counterpart (dependency vulnerabilities, not runtime behaviour)
