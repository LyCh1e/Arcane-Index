---
type: concept
address: c-000101
title: "Security Testing and Verification"
domain: secure-software-development
complexity: high
created: 2026-07-09
updated: 2026-07-09
tags: [concept, security-testing, ASVS, WSTG, test-automation, authentication-testing, owasp, penetration-testing, SDLC, DAST, zap, burp-suite, fuzzing]
related:
  - concepts/secure-input-validation
  - concepts/secure-deployment-practices
  - concepts/owasp-top-10
  - concepts/secure-design-implementation
  - concepts/software-testing-fundamentals
  - examples/ict2216-lab11-zap-burp
---

# Security Testing and Verification

Security testing verifies that implemented security controls operate as expected and meet security requirements. It is not an afterthought — it is integrated across every phase of the SDLC. The two primary OWASP frameworks are **ASVS** (what to verify) and **WSTG** (how to test it).

---

## The Testing Pyramid

The testing pyramid models the ideal distribution of testing resources across layers:

```
        /\
       /  \        ← UI / End-to-End Tests  (few)
      /    \          Brittle, slow, expensive to maintain
     /------\
    /        \     ← Integration / API Tests  (some)
   /          \       Focus: automated, API-centric
  /            \
 /--------------\
/                \  ← Unit Tests  (many)
\________________/   Fast, cheap, reliable; solid foundation
```

**Rising with the pyramid:**

| Property | Direction | Implication |
|---|---|---|
| Complexity of tests | ↑ Increases | Harder to write and maintain |
| Fragility | ↑ Increases | More dependencies that can break |
| Maintenance cost | ↑ Increases | More expensive to update after changes |
| Execution time | ↑ Increases | Slower feedback cycle |
| Time to locate a bug | ↑ Increases | Root cause harder to pinpoint |

**Key principle:** Unit tests should form the **bulk** of your test suite. Integration and UI tests should focus on **highly automated, API-centric** scenarios.

**Security testing objective:** Verify that security controls operate as expected. Security testing is never exhaustive — not all security tests can be automated; a balanced approach of automated and manual testing is required.

---

## Security Testing in the SDLC

Security testing is integrated at every phase — not bolted on at the end. The OWASP Testing Framework advocates: **test early and test often**.

| SDLC Phase | Security Testing Activity |
|---|---|
| Definition | Policy review |
| Design & Architecture | Architecture review, UML model review |
| Development | Code review, code walkthroughs |
| Testing | Unit and system tests, penetration testing, configuration audits |
| Deployment | Configuration audits, operational health checks |
| Maintenance | Regression tests, acceptance tests |

---

## Penetration Testing Methodologies

The OWASP Testing Framework defines **5 phases** integrated throughout the SDLC (Before Development, During Definition/Design, During Development, During Deployment, During Maintenance).

Major methodologies for structured penetration tests:

| Methodology | Description |
|---|---|
| **OWASP Testing Guide (WSTG)** | Comprehensive web application security testing guide — the primary reference for this course |
| **PTES** | Penetration Testing Execution Standard — standardised methodology covering all phases of a full penetration test |
| **NIST 800-115** | Technical guide to information security testing and assessment |
| **PTF** | Penetration Testing Framework — structured framework for all phases |
| **ISSAF** | Information Systems Security Assessment Framework (draft 0.2.1) — peer-reviewed; covers security processes and hardening across many domains (Unix, Windows, database, wireless, web, VPN, IDS, etc.) |
| **OSSTMM** | Open Source Security Testing Methodology Manual v3 — covers operational security: physical, workflow, human (social engineering), wireless, telecom, data networks, compliance. Best used as a **supporting reference for ISO 27001** rather than a hands-on pen testing guide. |
| **PCI Penetration Testing Guide** | Requirements for penetration testing in payment card environments |

> **Why ISO 27001?** ISO 27001 is the international standard for Information Security Management Systems (ISMS). Enterprise clients and government contracts commonly require ISO 27001 certification as a prerequisite.

---

## Code Inspection (Security Audit)

**Code inspection / security audit** involves a systematic review of source code by a **third party** (not the original developer) to discover bugs, security breaches, and violations of programming conventions.

| Aspect | Detail |
|---|---|
| **Benefit** | Humans generalise beyond single runs; experienced reviewers recognise patterns from past vulnerabilities |
| **Drawback** | Expensive, time-consuming, requires skilled reviewers, provides no completeness guarantee |
| **Key principle** | Must be done by someone other than the original author — the author is too close to spot their own assumptions |

**Code review workflow (e.g., Gerrit):**

| Role | Responsibility |
|---|---|
| **Submitter** | Submits code for review |
| **Code Reviewer** | Reviews changes; approves or requests changes |
| **Verifier** | Runs automated checks |
| **Approver** | Final approval gate before merge |
| **Committer** | Merges approved changes into the target branch |

Reference: Trail of Bits — Auditing Source Code: https://trailofbits.github.io/ctf/vulnerabilities/source.html

### Professional Engagement — Scope and Pricing

In commercial secure code auditing engagements, two pricing models are common:

| Model | Basis | Suitable for |
|-------|-------|-------------|
| **Per line of code** | Total LoC reviewed × agreed rate | Well-scoped, medium-sized codebases |
| **Per man-day** | Number of engineer review days × daily rate | Complex systems: custom encryption, bespoke logic, PII handling |

**Indicative range (Singapore market, 2024–2026):** SGD 50,000 – 100,000+ for banking, healthcare, or government applications with 10,000+ LoC, encryption implementations, or significant personal data scope.

**Accountability:** The auditing party bears responsibility for any findings they miss. This is why auditors do not simply outsource findings to AI — if a false negative goes undetected and later causes a breach, the auditor's report is the accountability trail. Human judgment remains the final gate.

---

## Test Frameworks

### Unit Testing

**Unit tests** validate individual units — a single method or class — in isolation.

**What to test for secure software (authentication example):**
- Required fields are enforced
- Field length constraints (min/max)
- Valid email address format
- Unique email address constraint
- Password complexity rules (or lack thereof, per NIST)
- Password confirmation matching

Frameworks: **PHPUnit**, **PyUnit (unittest)**, **JUnit**

### Integration and UI Testing

**Integration/system tests** validate multiple units working together or the application as a whole.

**Example stack (Java/Selenium):**
- **Maven** — build and dependency management
- **TestNG** — test automation framework (`@Test` annotations)
- **Selenium WebDriver** — automates real browser interactions

Workflow: Dev push → Jenkins trigger → Maven build → TestNG/Selenium runs → results reported.

---

## OWASP Application Security Verification Standard (ASVS)

Reference: https://owasp.org/www-project-application-security-verification-standard/

ASVS is a **catalogue of verification requirements** for security controls. It bridges security requirements and test cases:

```
Security Requirements → OWASP ASVS → Verification Requirements → OWASP WSTG → Test Cases
```

### ASVS Verification Levels

| Level | Target Application | Testing Approach |
|---|---|---|
| **Level 1** | Low assurance / all apps | Completely penetration testable; minimal additional verification |
| **Level 2** | Apps with sensitive data (most apps) | Recommended baseline; requires security reviews and DevSecOps integration |
| **Level 3** | Most critical apps | High-value transactions, medical data, highest-trust requirements; formal reviews, unit testing, and hybrid approaches |

### ASVS 14 Verification Categories

| Category | Description |
|---|---|
| V1 | Architecture, Design and Threat Modelling Requirements |
| V2 | Authentication Verification Requirements |
| V3 | Session Management Verification Requirements |
| V4 | Access Control Verification Requirements |
| V5 | Validation, Sanitisation and Encoding Verification Requirements |
| V6 | Stored Cryptography Verification Requirements |
| V7 | Error Handling and Logging Verification Requirements |
| V8 | Data Protection Verification Requirements |
| V9 | Communications Verification Requirements |
| V10 | Malicious Code Verification Requirements |
| V11 | Business Logic Verification Requirements |
| V12 | File and Resources Verification Requirements |
| V13 | API and Web Service Verification Requirements |
| V14 | Configuration Verification Requirements |

---

## ASVS V2 — Authentication Verification Requirements

### V2.1: Password Security Requirements

All requirements map to **CWE-521** (Weak Password Requirements) and **NIST SP 800-63 §5.1.1.2**:

| ID | Requirement |
|---|---|
| 2.1.1 | Passwords must be **at least 12 characters** (after collapsing multiple spaces into one) |
| 2.1.2 | Passwords of **at least 64 characters** must be permitted; passwords **over 128 characters** must be denied |
| 2.1.3 | Password **truncation must not occur** (consecutive spaces may be collapsed) |
| 2.1.4 | **Any printable Unicode character** must be permitted, including spaces and emoji |
| 2.1.5 | Users must be able to **change their password** |
| 2.1.6 | Password change must require **current and new password** |
| 2.1.7 | Passwords must be checked against a **breached password list** (e.g., top 1,000–10,000 most common, or via zero-knowledge-proof API); if breached, user must choose a new one |
| 2.1.8 | A **password strength meter** must be shown |
| 2.1.9 | **No password composition rules** that restrict character types (no forced uppercase/lowercase/number/special character requirements) |
| 2.1.10 | **No periodic credential rotation** or password history requirements |
| 2.1.11 | **Paste functionality, browser password helpers, and external password managers** must be permitted |
| 2.1.12 | Users must be able to **temporarily view their masked password** (or the last typed character) |

> These requirements align directly with **NIST SP 800-63**: no complexity rules, no forced rotation, minimum 12 characters (8 if MFA is required), all Unicode permitted.

### V2.4: Credential Storage Requirements

| ID | Requirement | CWE |
|---|---|---|
| 2.4.1 | Passwords **must be salted and hashed** using an approved one-way key derivation or password hashing function resistant to offline attacks | 916 |
| 2.4.2 | Salt must be **at least 32 bits**, randomly generated, unique per credential | 916 |
| 2.4.3 | If PBKDF2 is used, **iteration count ≥ 100,000** (or as large as server performance allows) | 916 |
| 2.4.4 | If bcrypt is used, **work factor ≥ 10** (or as large as server performance allows) | 916 |
| 2.4.5 | An additional key derivation round **should use a secret salt known only to the verifier**, stored separately (e.g., in a Hardware Security Module) | 916 |

### V2.5: Credential Recovery Requirements

| ID | Requirement | CWE |
|---|---|---|
| 2.5.1 | Activation or recovery secrets must **not be sent in cleartext** | 640 |
| 2.5.2 | **Password hints and knowledge-based "secret questions" must not be used** | 640 |
| 2.5.3 | Recovery must **not reveal the current password** | 640 |
| 2.5.4 | **Shared or default accounts** ("root", "admin", "sa") must not be present | 16 |
| 2.5.5 | Users must be **notified when an authentication factor is changed or replaced** | 304 |
| 2.5.6 | Forgotten password recovery must use a **secure mechanism** — TOTP, soft token, mobile push, or offline recovery | 640 |
| 2.5.7 | If OTP/MFA factors are lost, identity must be re-verified at the **same level as during enrolment** | 308 |

### V10: Malicious Code Verification Requirements

| ID | Requirement | CWE |
|---|---|---|
| 10.1.1 | A **code analysis tool** must be in use to detect potentially malicious code (unsafe time functions, unsafe file operations, unexpected network connections) | 749 |
| 10.2.1 | Source code and third-party libraries must **not contain unauthorised phone-home or data collection**; where present, user permission must be obtained | 359 |
| 10.2.2 | Application must **not request unnecessary permissions** to privacy-related features (contacts, cameras, microphones, location) | 272 |
| 10.2.3 | Source code and third-party libraries must **not contain backdoors** (hardcoded/undocumented accounts, code obfuscation, rootkits, anti-debugging, hidden functionality) | 507 |
| 10.2.4 | Source code and third-party libraries must **not contain time bombs** (date/time functions used in suspicious conditions) | 511 |

---

## OWASP Web Security Testing Guide (WSTG)

Reference: https://owasp.org/www-project-web-security-testing-guide/

WSTG provides the concrete **test procedures** for each ASVS verification requirement, organised into 11 test categories:

| Category | Code Prefix |
|---|---|
| Information Gathering | OTG-INFO-### |
| Configuration and Deployment Management Testing | OTG-CONFIG-### |
| Identity Management Testing | OTG-IDENT-### |
| Authentication Testing | OTG-AUTHN-### |
| Authorisation Testing | OTG-AUTHZ-### |
| Session Management Testing | OTG-SESS-### |
| Input Validation Testing | OTG-INPVAL-### |
| Testing for Error Handling | OTG-ERR-### |
| Testing for Weak Cryptography | OTG-CRYPST-### |
| Business Logic Testing | OTG-BUSLOGIC-### |
| Client Side Testing | OTG-CLIENT-### |

### How to Use ASVS + WSTG Together

Given a security requirement, the workflow is:

1. Security requirement → select appropriate **ASVS category** → obtain specific verification requirements
2. Verification requirements → select appropriate **WSTG category** → obtain test procedures
3. Execute tests → record results in **WSTG checklist** → compile security test report

**Example — password requirement (ASVS V2.1 → WSTG OTG-AUTHN-007):**

*WSTG test objectives for OTG-AUTHN-007 (Testing for Weak Password Policy):*

1. What characters are permitted and forbidden?
2. Can users rotate through a history of previous passwords to reset back to an original? (history bypass)
3. When must a user change their password? (Note: NIST/NCSC recommend against forced expiry)
4. How often can a password be reused? Is a history of the previous 8 passwords maintained?
5. How different must the next password be from the last?
6. Is the user prevented from using their username or account information in the password?
7. What are the minimum and maximum password lengths? Are they appropriate for the sensitivity of the account?
8. Is it possible to set a common password such as `Password1` or `123456`?

---

## Authentication Testing

### Testing Account Lockout (OTG-AUTHN-003)

Account lockout mechanisms must balance protecting accounts from brute force against protecting legitimate users from denial of access. Lockout typically triggers after 3–5 failed attempts.

**Example test sequence:**

| Step | Action | Expected Result |
|---|---|---|
| 1 | 3 incorrect passwords, then correct password | Login succeeds — lockout not triggered yet |
| 2 | 4 incorrect passwords, then correct password | Login succeeds — lockout not triggered yet |
| 3 | 5 incorrect passwords, then correct password | "Your account is locked out." |
| 4 | Correct password, 5 minutes later | Still locked |
| 5 | Correct password, 10 minutes later | Still locked |
| 6 | Correct password, 15 minutes later | Login succeeds — automatic unlock after timeout |

**Unlock mechanism assurance levels (lowest to highest):**

1. Time-based automatic lockout and unlock
2. Self-service unlock (unique, one-time-use link to registered email)
3. Manual administrator unlock
4. Manual administrator unlock with positive user identification

### CAPTCHA — Supplement, Not a Replacement

CAPTCHA may **hinder** brute force attacks but must **not replace** a proper lockout mechanism. CAPTCHA can be bypassed if implemented incorrectly.

**Common CAPTCHA flaws:**
- Challenge is trivially defeated (simple arithmetic, limited question pool)
- Checking HTTP response code rather than the response value
- Server-side logic defaults to "solved" on error
- CAPTCHA result **not validated server-side** — validation is client-side only
- CAPTCHA input field is not properly escaped (injection surface)

**How to evaluate CAPTCHA effectiveness (10-point checklist):**

1. Attempt to automate solutions to the challenges presented
2. Attempt to submit a request without solving CAPTCHA via the normal UI
3. Attempt to submit with an intentional CAPTCHA failure
4. Submit directly to the server via a proxy, bypassing the client-side CAPTCHA check
5. Fuzz CAPTCHA data entry points with injection payloads and special characters
6. Check whether the solution is the alt-text, filename, or a hidden field value
7. Attempt to re-submit a previously known-good CAPTCHA response (replay)
8. Check if clearing cookies bypasses CAPTCHA (shown only after N failures)
9. In multi-step flows, attempt to skip directly to the step after CAPTCHA
10. Check for alternative API endpoints (e.g., a mobile API) that do not enforce CAPTCHA

### Account Enumeration — Generic Error Messages (OTG-AUTHN, OTG-IDENT-05)

An application must **never reveal whether the username or password was incorrect** — differentiated error messages enable an attacker to enumerate valid accounts.

**✅ Correct (generic) error messages:**
```
Authentication failed.
Return to Login page.
```

**❌ Incorrect (revealing) error messages:**
```
Login for User foo: invalid password.
```

The second format confirms that the username `foo` exists, allowing an attacker to build a list of valid accounts before launching a targeted credential attack.

**Username policy testing (OTG-IDENT-05):**
- Determine whether a consistent account name structure (e.g., first-initial + surname) makes accounts guessable
- Evaluate whether application responses differ for valid vs. invalid usernames
- Test for username enumeration via error messages, response timing, and page content differences

**Remediation:** Return identical generic messages for all invalid credential combinations — do not differentiate between "username not found" and "incorrect password."

---

## DAST Tools: OWASP ZAP and Burp Suite

**DAST (Dynamic Application Security Testing)** exercises a *running* application from the outside — as opposed to SAST (e.g. SonarQube, ESLint — see [[examples/ict2216-lab9-sonarqube]]) which analyses source code without executing it. DAST tools implement WSTG test procedures automatically: spidering discovers the site map, passive/active scanning and fuzzing probe it for weaknesses.

### OWASP ZAP — Automated Vulnerability Scanning

ZAP (Zed Attack Proxy) is a free, open-source DAST tool. The **Automated Scan** workflow:

1. Enter target URL → ZAP **spiders** the app to build a site map:
   - **Traditional spider** — parses HTML links; fast, misses JS-generated (AJAX) links
   - **Ajax spider** — drives a real/headless browser so JS-rendered links are followed; slower, needed for SPA-style apps
2. **Passive scan** — analyses each discovered response without sending extra requests (headers, cookies, information leakage)
3. **Active scan** — actively attacks discovered pages/parameters (injects payloads, similar to WSTG input-validation and config tests)
4. Findings land in the **Alerts** tab, each with a risk rating (High/Medium/Low/Informational) — directly usable in the **Findings** section of a WSTG-style report (see Security Test Reporting above)
5. **Report** menu exports an HTML/other-format report with a Summary-of-Alerts table by risk level plus per-finding detail — structurally the same shape as the report format described above

Common findings ZAP surfaces via passive scanning: missing `X-Frame-Options` (clickjacking), absent anti-CSRF tokens, cookies missing `HttpOnly`/`SameSite`, information leakage via `X-Powered-By`, missing `X-Content-Type-Options`.

### Burp Suite — Manual/Targeted Fuzz Testing

Burp Suite (Community Edition, free) is a proxy-centric toolkit. Where ZAP automates discovery+scanning, Burp's **Intruder** is used for *targeted* fuzzing — e.g. brute-forcing a login form:

1. Configure the browser to proxy through Burp (`127.0.0.1:8080`); submit a request through the app so Burp captures it
2. **Send to Intruder** → **Positions** tab: mark the fields to fuzz with `§...§` markers (clear the auto-selected ones and mark only the fields of interest, e.g. username + password)
3. Choose an **attack type**:
   - **Sniper** — one payload set, cycled through each position in turn
   - **Battering ram** — one payload set, same value in every position simultaneously
   - **Pitchfork** — multiple payload sets, iterated in lockstep (position *i* takes item *i* from each set)
   - **Cluster bomb** — multiple payload sets, every combination tried (Cartesian product) — used for independent username×password brute-forcing
4. **Payloads** tab: assign a payload set per position (e.g. a wordlist file via "Runtime file" payload type — see [1N3/IntruderPayloads](https://github.com/1N3/IntruderPayloads) for ready-made fuzzing lists)
5. **Start attack** — results table shows response status/length per payload combination
6. **Grep-Extract** (Options tab): define a snippet to pull out of each response (e.g. the `Location:` redirect header) into its own results column — turns "manually inspect every response" into "sort one column" to spot the interesting outcome (e.g. a redirect to `index.php` instead of back to `login.php` signals a successful login)

### ZAP vs Burp — Complementary, Not Competing

| | OWASP ZAP | Burp Suite (Community) |
|---|---|---|
| Primary mode | Automated crawl + scan | Manual/scripted proxy-driven testing |
| Best for | Broad coverage, quick baseline VA | Targeted fuzzing of a specific parameter/flow |
| Output | Alerts tab + exportable report | Intruder results table (no built-in report in Community edition) |
| Cost | Free, fully open source | Free tier limited (no scanner); Pro adds active scanning |

### Legal Note

Both tools actively send attack traffic to the target. **Scanning or fuzzing a system without authorisation is a criminal offence** in most jurisdictions (e.g. under the Computer Misuse Act) — only ever point these at systems you own or have explicit written permission to test, such as a locally hosted DVWA instance.

---

## Security Test Reporting

Reference: https://owasp.org/www-project-web-security-testing-guide/stable/5-Reporting/README

A security test report must be easy to understand and must highlight all risks found in a clear, actionable way.

### Standard Report Structure

1. **Introduction** — scope, objectives, methodology, tools used
2. **Executive Summary** — high-level findings for non-technical stakeholders; overall risk rating
3. **Findings** — for each vulnerability found:
   - Vulnerability name and category
   - Affected component / URL / parameter
   - Severity rating (Critical / High / Medium / Low / Informational)
   - Description and proof of concept
   - Remediation recommendation
   - References (CVE, CWE numbers earn bonus marks in academic context)
4. **Appendices** — the WSTG checklist showing all test cases conducted and their pass/fail results

### Severity Ratings

| Rating | Meaning |
|---|---|
| **Critical** | Remote code execution, authentication bypass, mass data exfiltration |
| **High** | Significant privilege escalation, sensitive data exposure |
| **Medium** | Requires user interaction or specific conditions; notable risk |
| **Low** | Limited impact; informational or defence-in-depth concern |
| **Informational** | Best practice improvement; no direct exploitable risk |

---

## See Also

- [[concepts/static-code-analysis]] — SAST deep dive: pipeline, 6 techniques (pattern matching → theorem proving), false positives/negatives, heap limitation, tool catalogue
- [[concepts/secure-input-validation]] — input validation, ReDoS, SQL injection prevention
- [[concepts/secure-deployment-practices]] — security logging implementation and logging testing considerations
- [[concepts/owasp-top-10]] — the vulnerability risk list; ASVS requirements address each risk
- [[concepts/secure-design-implementation]] — authentication design, cryptography, session management
- [[concepts/software-testing-fundamentals]] — general testing theory (ISTQB); security testing applies the same rigour
- [[sources/ICT2216-lecture-8-secure-testing]] — Lecture 8 source
- [[sources/ICT2216-lecture-9-static-code-analysis]] — Lecture 9 source: static analysis techniques, pen testing methodologies, case studies
- [[examples/ict2216-lab11-zap-burp]] — hands-on: OWASP ZAP vulnerability assessment + Burp Suite fuzzing against DVWA
