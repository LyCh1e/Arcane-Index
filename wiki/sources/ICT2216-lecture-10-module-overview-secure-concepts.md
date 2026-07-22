---
type: source
title: "ICT2216 Lecture 10 — Module Overview & Secure Software Concepts"
address: c-000121
course: ICT2216
domain: secure-software-development
format: lecture-notes
confidence: high
tags: [ssdlc, quality-gates, agile-security, owasp, case-studies, ict2216]
created: 2026-07-22
ingested: 2026-07-22
---

# Source: ICT2216 Lecture 10 — Module Overview & Secure Software Concepts

> **Note on file naming:** The raw file is named `ICT2216 Lecture 10 Secure Software Development.md`, but its internal heading reads *"Lecture 1: Module Overview & Secure Software Concepts"*. This appears to be a packaging or labelling discrepancy — the content covers introductory module material and foundational secure software concepts, not a tenth lecture topic. Filed under its actual content.

**Raw file:** `raw/ICT2216 Lecture 10 Secure Software Development.md`
**Course:** ICT2216 Secure Software Development
**Lecturers:** Tram Truong Huu, Raymond Chan

---

## Content Summary

| Part | Topic | Disposition |
|------|-------|-------------|
| Part 1 — Module Overview | Teaching team, schedule, IS vs SE collaboration, SSDLC overview, Security Quality Gates, Sprint+Security approaches | **New** — Security Quality Gates and Sprint+Security detail added to wiki |
| Part 2 — Secure Software Concepts | CIA triad motivation, case studies, software vulnerability categories, OWASP Top 10 (2025), CVE/NVD/MITRE ATT&CK | OWASP Top 10 already fully in [[owasp-top-10]]; new 2025/2026 case studies added |

---

## New Case Studies (2025/2026)

Four real-world incidents presented in the lecture that were not previously in the vault:

### HSBC India — Uppercase Password Anomaly (2026)

From April 2026, HSBC India required customers to enter internet banking passwords **in uppercase only**. Standard practice dictates that credentials are stored as **one-way salted hashes** — making the original casing completely unreadable by the bank. Requiring uppercase implies either:
- **Plaintext password storage**, or
- A deeply flawed legacy authentication system that compares characters case-insensitively

Additionally, forcing uppercase **halves the effective character set**, dramatically reducing brute-force resistance.

→ Maps to **OWASP A04:2025 Cryptographic Failures**

### X (Twitter) Insider Data Breach (2025)

Approximately **2.8 billion user profiles** were allegedly exfiltrated by a disgruntled X employee during the company's mass-layoff period. A ~400 GB dataset was published on Breach Forums on 28 March 2025. Neither X nor mainstream media initially acknowledged the breach.

Key lesson: **Insider threats** are among the hardest risks to prevent through technical controls alone — privileged access, combined with insufficient monitoring and alerting, made this possible.

→ Maps to **OWASP A09:2025 Security Logging & Alerting Failures** (breach not monitored or disclosed)

### Europcar GitLab Breach

A threat actor compromised **GitLab repositories** belonging to Europcar Mobility Group:
- Stole source code for Android and iOS applications
- Stole personal data of at least **200,000 customers**
- Threatened to release **37 GB** of stolen data unless extortion demands were met

→ Maps to **OWASP A03:2025 Software Supply Chain Failures** (source code repository compromise)

### Gladinet CentreStack — CVE-2025-30406 (CVSS 9.0)

A critical vulnerability in the Gladinet CentreStack file-sharing platform, added to CISA's Known Exploited Vulnerabilities (KEV) catalogue.

**Root cause:** A **hard-coded `machineKey`** in the IIS `web.config` file. Attackers who discovered this key could forge **ViewState payloads** and pass them to the server, triggering **server-side deserialisation** and achieving **Remote Code Execution (RCE)**.

Timeline:
- Exploited as a zero-day in March 2025
- Patch released: version 16.4.10315.56368 (3 April 2025)
- Temporary mitigation: rotate the `machineKey` value

→ Maps to **OWASP A04:2025 Cryptographic Failures** (hardcoded cryptographic key) + **OWASP A08:2025 Software and Data Integrity Failures** (insecure deserialisation leading to RCE)

---

## Key Claims

- Security activities must be embedded at **every SDLC phase transition** via formal quality gates — not bolted on at the end
- **Every Sprint** approach (security in every sprint) is preferred over **Security Sprint** (a dedicated security-only sprint), aligned with Microsoft SDL
- A sprint where security requirements are not completed is deemed **incomplete** and software cannot be released
- Network-layer controls (firewall, IDS) cannot protect against application-layer vulnerabilities — CIA must be enforced at the application layer
- *"There is no perfect solution when developing an application."*

---

## Concepts Linked

- [[concepts/owasp-top-10]] — Full OWASP Top 10 (2025) reference; case studies from this lecture added
- [[concepts/secure-design-implementation]] — Security Quality Gates + Sprint+Security approaches added
- [[concepts/secure-software-requirements]] — CIA-AAA model, requirement process
- [[concepts/security-testing-and-verification]] — Penetration testing as Gate 4 activity
- [[concepts/static-code-analysis]] — Secure Code Review as Gate 3 activity

---

## External References

- OWASP Top 10 (2025): https://owasp.org/www-project-top-ten/
- Microsoft SDL: https://www.microsoft.com/en-us/securityengineering/sdl
- Gladinet CVE-2025-30406: CISA KEV catalogue
- HSBC India uppercase passwords: reported April 2026
- X/Twitter Breach Forums post: ThinkingOne, 28 March 2025
