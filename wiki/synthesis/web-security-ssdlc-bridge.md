---
type: synthesis
status: established
title: "Attack Patterns at Code Level ↔ SSDLC Process: INF1005 × ICT2216"
domain: web-development × secure-software-development
sources:
  - concepts/web-security-and-devops
  - concepts/secure-software-requirements
  - concepts/owasp-top-10
complexity: high
updated: 2026-05-14
tags: [synthesis, web-security, SSDLC, OWASP, ASVS, injection, XSS, CSRF, authentication, STRIDE, threat-modelling, INF1005, ICT2216]
---

# Attack Patterns at Code Level ↔ SSDLC Process: INF1005 × ICT2216

INF1005 and ICT2216 both teach security, but from opposing directions. INF1005 teaches a developer encountering an attack and reaching for a code-level fix. ICT2216 teaches an engineer specifying, verifying, and tracking security requirements across an entire development lifecycle. The attacks and the fixes are identical — the difference is whether they are discovered reactively at the keyboard or mandated proactively in a requirements document.

---

## 1. The Two Perspectives

| Perspective | Module | Question Asked |
|---|---|---|
| **Code-level** | INF1005 | "My application is vulnerable to XSS — what do I change?" |
| **Process-level** | ICT2216 | "How do I ensure XSS prevention is specified, implemented, verified, and auditable before deployment?" |

A developer who only knows INF1005 can fix individual vulnerabilities they have already been told about. A developer who also knows ICT2216 designs systems in which those vulnerabilities have no opportunity to appear undetected.

---

## 2. Vulnerability-by-Vulnerability Mapping

### 2.1 SQL Injection

**INF1005 view** ([[concepts/web-security-and-devops|Web Security and DevOps]]): SQL injection occurs when user input is concatenated directly into a query string. The fix is a prepared statement:

```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->bindValue(':id', $_GET['id']);
$stmt->execute();
```

**OWASP 2025 mapping** ([[concepts/owasp-top-10|OWASP Top 10]]): A05:2025 Injection (formerly A01:2021 Injection). The code-level attack maps directly to this category. A Java example from the OWASP page is structurally identical to the PHP vulnerability above.

**ICT2216 / ASVS mapping**: OWASP ASVS Chapter V5 — Input Validation and Sanitisation. The formal security requirement that a developer's prepared-statement fix is *satisfying* reads approximately:

> "Verify that the application uses parameterised queries or stored procedures to prevent injection attacks wherever user-supplied data is passed to an interpreter."

The developer sees the fix as a coding technique. The security engineer sees it as the implementation of a traceable, verifiable ASVS Level 1 requirement, generated automatically by SecurityRAT when "web application" is declared as the artefact type.

**STRIDE connection**: SQL injection realises the **Tampering** and **Information Disclosure** threats from the STRIDE model. Tampering because a successful injection can modify or delete records (`DELETE FROM users`); Information Disclosure because it can dump the entire database.

---

### 2.2 Cross-Site Scripting (XSS)

**INF1005 view**: XSS — both reflected and stored — is defeated by output encoding and Content Security Policy headers:

```php
$safe = htmlspecialchars($_POST["comment"]);
```

**OWASP 2025 mapping**: Also A05:2025 Injection. The OWASP page distinguishes three forms — Reflected, Stored, and DOM-based — and notes that DOM XSS occurs when JavaScript writes attacker-controlled data into the page without sanitisation (`innerHTML`).

**ICT2216 / ASVS mapping**: ASVS V5 again covers output encoding requirements. The specific requirements distinguish between:
- V5.3 — Output encoding for the specific context (HTML body, HTML attribute, JavaScript, CSS, URL)
- V5.5 — Content Security Policy headers

A developer who knows only INF1005 will apply `htmlspecialchars()`. An engineer working to ASVS Level 2 will additionally specify HTTP response headers (CSP), verify them in a security test, and attach the test result to the requirement ticket in SecurityRAT.

**STRIDE connection**: XSS realises **Tampering** (modifying the page a victim sees), **Information Disclosure** (stealing session cookies via `document.cookie`), and **Spoofing** (impersonating a user once their session token is captured).

---

### 2.3 Cross-Site Request Forgery (CSRF)

**INF1005 view**: CSRF forces an authenticated user to execute state-changing actions on a site where they are logged in. Defence is a CSRF token in every state-changing form:

```html
<input type="hidden" name="csrf-token" value="randomUniqueToken123">
```

**OWASP 2025 mapping**: CSRF does not occupy a dedicated A0x slot in the 2025 list but falls under A01:2025 Broken Access Control, since the attack exploits the server's failure to verify that a request was deliberately initiated by the authenticated user.

**ICT2216 / ASVS mapping**: ASVS V4 — Access Control — requires that every state-changing request be validated for origin and intent. ASVS V3 — Session Management — requires that session tokens cannot be used to forge requests from external origins.

**STRIDE connection**: CSRF realises **Spoofing** (a request arrives appearing to originate from a legitimate user) and **Tampering** (the attacker modifies state — transferring funds, changing an email address — without the user's knowledge).

---

### 2.4 Broken Authentication and Password Storage

**INF1005 view** ([[concepts/web-security-and-devops|Web Security and DevOps]]): Passwords must never be stored as plaintext or MD5. The fix is bcrypt with salting:

```php
$hash = password_hash($password, PASSWORD_BCRYPT);
$valid = password_verify($inputPassword, $storedHash);
```

Rate limiting and account lockout defend against brute-force enumeration.

**OWASP 2025 mapping**: A07:2025 Authentication Failures. OWASP calls out unsalted/fast hashes explicitly: "Password database uses unsalted or fast hashes → rainbow table or GPU cracking exposes all passwords."

**ICT2216 / ASVS mapping**: ASVS V2 — Authentication. The [[concepts/secure-software-requirements|Secure Software Requirements]] page documents the CIA-AAA derivation: Authentication requirements are generated by asking "who interacts with the system?" and "what could go wrong?" The NIST 800-63 guidelines (no mandatory rotation, no complexity rules, check against breached-password lists, use MFA for privileged accounts) are the *content* of the ASVS V2 requirements.

**STRIDE connection**: Weak authentication realises **Spoofing** — an attacker assumes the identity of a legitimate user — which is precisely the S in STRIDE.

---

## 3. The STRIDE → Attack Mapping

STRIDE is a threat-modelling framework taught in ICT2216 for identifying potential threats during design. Each STRIDE category has one or more concrete attacks from INF1005 that realise it at code level:

| STRIDE Threat | Description | Concrete Attacks (INF1005) |
|---|---|---|
| **Spoofing** | Attacker uses someone else's credentials | Session hijacking (via XSS cookie theft), CSRF, credential stuffing against weak auth |
| **Tampering** | Unauthorised data modification | SQL injection (UPDATE/DELETE), CSRF (state-changing requests), insecure deserialisation |
| **Repudiation** | Denial of actions; no audit trail | Insufficient logging (OWASP A09), missing timestamps, tampered log files |
| **Information Disclosure** | Unauthorised data access | SQL injection (SELECT dump), XSS cookie theft, verbose error messages |
| **Denial of Service** | Service disruption | Brute-force login, DDoS, resource exhaustion (A10 — Mishandling Exceptional Conditions) |
| **Elevation of Privilege** | Gaining unauthorised permissions | IDOR (A01), insecure deserialisation (role = "admin"), OWASP A02 misconfiguration |

A threat-modelling session during design (ICT2216) that surfaces "Spoofing via credential theft" should generate ASVS V2 and V3 requirements covering password hashing, MFA, and session token management — all of which correspond to bcrypt, lockout, and CSRF token implementations (INF1005).

---

## 4. The Key Insight: What and How vs Specify and Verify

| Aspect | INF1005 Teaches | ICT2216 Teaches |
|---|---|---|
| Scope | A single vulnerable file | The entire SSDLC from requirements to deployment |
| Artefact | A code fix | A requirement, test case, and audit trail |
| Timing | Reactive (vulnerability found → fixed) | Proactive (requirement written → implemented → verified) |
| Verification | "It works now" | Structured testing against ASVS levels; evidence attached to requirement |
| Tooling | IDE, browser dev tools | SecurityRAT, threat-modelling tools, ASVS checklists |
| Standard | Implicit best practice | Formally referenced: OWASP ASVS, NIST SSDF, PCI SSF |

The developer who only takes INF1005 can patch vulnerabilities they encounter. The professional who also takes ICT2216 can demonstrate to an auditor, with evidence, that every applicable ASVS requirement was specified in the design phase, implemented in the code, and tested before release. This is what separates a secure product from a product that happens not to have been exploited yet.

---

## 5. ASVS Verification Level Summary

| ASVS Level | Intended For | Approach |
|---|---|---|
| **Level 1** | All applications | Penetration testing; minimum baseline |
| **Level 2** | Applications handling sensitive data | Security testing; covers most INF1005 attack vectors formally |
| **Level 3** | Critical infrastructure, high-value targets | Architecture review + code review + security testing |

A web application containing user authentication and a database (i.e., every INF1005 lab project) should meet at minimum ASVS Level 1. ASVS Level 2 formally specifies all of the defences taught as code techniques in INF1005.

---

## See Also

- [[concepts/web-security-and-devops|Web Security and DevOps]] — code-level attack vectors, bcrypt, CSRF tokens, STRIDE table
- [[concepts/secure-software-requirements|Secure Software Requirements]] — CIA-AAA triads, ASVS, SecurityRAT, NIST SSDF, OSA taxonomy
- [[concepts/owasp-top-10|OWASP Top 10 (2025)]] — full catalogue of vulnerability categories with attack scenarios
- [[concepts/server-side-web-development|Server-Side Web Development]] — PHP PDO prepared statements, Express routes where injection vulnerabilities originate
