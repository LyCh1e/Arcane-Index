---
type: concept
title: "Threat Modeling"
domain: secure-software-development
complexity: high
tags: [security, threat-modeling, STRIDE, attack-trees, DFD, trust-boundaries, threat-agents]
updated: 2026-05-15
status: established
created: 2026-05-15
---

# Threat Modeling

Security requirements tell you *what* to protect. Threat modeling tells you *how* attackers will actually try to break your system. It is a **structured, design-time process** for identifying and addressing security risks before writing code.

> Requirements alone are not enough. Threat modeling provides the disciplined adversarial perspective that requirements analysis cannot.

---

## What Is a Threat?

| Term | Definition |
|------|-----------|
| **Threat** | A potential negative event or action that could exploit a vulnerability |
| **Risk** | The *likelihood × impact* of a threat being realised |
| **Vulnerability** | A weakness that a threat can exploit |

**Threat categories (by CIA triad):**
- **Disclosure threats** — against confidentiality (information exposure)
- **Alteration threats** — against integrity (data or system modification)
- **Destruction threats** — against availability (denial of service, data loss)

Additional threat types: authentication bypass, privilege escalation, impersonation, man-in-the-middle, session hijacking, relay attacks, injection.

---

## Threat Agents

### Human Threats

| Threat Agent | Description |
|---|---|
| **Ignorant User** | Causes unintentional errors; best mitigated through user education |
| **Accidental Discoverer** | Normal user who stumbles upon a functional mistake and gains unintended access — never sought to bypass security |
| **Curious Attacker** | Ordinary user who notices an anomaly and decides to explore it further |
| **Script Kiddie** | Executes hacker scripts without understanding the impact; often leaves a visible footprint |
| **Insider** | Disgruntled employee or contractor with privileged knowledge — one of the most dangerous threat agents |
| **Organised Cybercriminals** | Highly skilled, professionally funded attackers seeking financial gain |
| **Third-party / Supplier** | Can embed malicious logic (logic bombs, Trojans) in software during supply chain handoff |
| **Nation-State Hackers** | The most powerful and well-resourced threat actors; conduct APTs |

### Non-Human Threats

- **OS Threats** — vulnerabilities at the operating system level
- **Malware** — viruses, ransomware, spyware, worms
- **Network Threats** — interception, spoofing, flooding
- **AI Threats** — emerging category of AI-driven and AI-assisted attacks

---

## Identifying Threats — Five Steps

### 1. Identify Trust Boundaries

> A **trust boundary** is the point at which the trust level or privilege changes.

- Trust boundaries demarcate zones of different security levels
- Every crossing of a trust boundary is a potential attack surface
- Examples: public internet ↔ internal network; user ↔ administrator roles; frontend ↔ backend API

Adequate protection must be designed *within* each boundary — not just at the perimeter.

### 2. Identify Entry Points and Exit Points

**Entry points** — all inputs the application accepts; each is a potential threat surface:
- Every entry point must be explicitly identified and safeguarded with input validation
- Web application examples: Login page, Search, Registration, Checkout, Account Maintenance

**Exit points** — all outputs the application produces; each is a potential information leakage point:
- Exit points can reveal internal state, data, or errors
- Web application examples: Search Results, Product page, View Cart, Error pages

### 3. Identify Privileged Functionality

- Any functionality that allows **elevation of privilege** or executes privileged operations
- Examples: administrator functions, fund transfers, user role changes, configuration changes

### 4. Identify Data Flows (Data Flow Diagrams)

**Data Flow Diagrams (DFDs)** model how data moves through the system across trust boundaries.

**DFD elements:**

| Symbol | Element | Description |
|--------|---------|-------------|
| Rectangle | External entity | User, external system, or service outside the trust boundary |
| Circle / Oval | Process | Application logic that transforms or routes data |
| Parallel lines | Data store | Database, file system, cache |
| Arrow | Data flow | Movement of data between elements |

**Why DFDs matter for security:** data that crosses a trust boundary is at risk. Every arrow crossing a trust boundary in a DFD represents a potential threat that must be modelled.

**Example — Library Website Login Flow:**
```
[Student] → (Login Request) → [Login Process] → [Auth Store] → (Session Token) → [Student]
```
Actors: Students (login, search, request books), Staff (same), Librarians (login, add books, add users, search).

### 5. Identify Mis-actors

Both human and non-human adversaries must be considered.

**Mis-actor categories by network position:**

| Mis-actor Type | Capabilities | Example Attacks |
|---|---|---|
| **Web attacker** (anonymous internet user) | Measure request/response size and timing; run parallel sessions; send malformed inputs | SQL injection, XSS, CSRF, buffer overflow |
| **Network attacker** (on the same unencrypted network) | Read/measure/intercept/duplicate/modify messages | Session hijacking, denial of service, MITM |
| **Co-located attacker** (on the same machine) | Read/write user files and memory; snoop keystrokes; access display | Password theft, credential harvesting |

**Threat model implications:**

| Assumed Threat Model | Implication |
|---|---|
| Web attacker only | Message traffic can be considered secure from eavesdropping |
| Network attacker | Encryption required: Secure Wi-Fi (link layer), IPSec (network layer), TLS (application layer) |
| Co-located attacker | Never store unencrypted secrets in local files or memory |

> **Warning:** Any assumption in your threat model is a potential weakness. Assuming "no network attacker" is invalid in environments with Wi-Fi networks.

---

## The Threat Modeling Process

**Five-step process:**

1. **Define security requirements** — CIA+AAA pillars, regulatory constraints
2. **Create an application diagram** — DFD or architecture diagram showing trust boundaries, data flows, entry/exit points
3. **Identify threats** — use STRIDE, attack trees, or other catalogues against each DFD element
4. **Mitigate threats** — design countermeasures for each identified threat
5. **Validate mitigations** — verify that each threat has been addressed (test, review, checklist)

**A threat model must document:**
- A description or model of what is being protected
- A list of **assumptions** (explicitly stated — assumptions are potential attack surface)
- A list of **potential threats**
- A list of **mitigating actions** per threat
- A method for **validating** that mitigations succeeded

---

## Attack Trees

Attack trees are a **visual, goal-oriented** technique for representing how an attacker can achieve an objective.

**Structure:**
- **Root node** = the attacker's goal
- **Leaf nodes** = individual tactics that directly achieve a sub-goal
- **AND nodes** = all children must succeed
- **OR nodes** = any one child suffices

A full threat analysis produces one attack tree per attacker goal.

**Example:**
```
[Goal: Gain unauthorised access to account]
├── OR: [Steal credentials]
│        ├── Phishing
│        ├── Credential stuffing
│        └── Keylogging
└── OR: [Bypass authentication]
         ├── SQL injection on login form
         └── Session token forgery
```

**Value:** Attack trees make complex, multi-step attacks tractable — each leaf maps to a defensive control and a test case.

---

## Microsoft STRIDE

STRIDE is a **goal-based threat categorisation framework** — it classifies threats by the attacker's objective, mapped to the security property they violate.

| Letter | Threat | Violated Property | Example |
|--------|--------|-------------------|---------|
| **S** | Spoofing | Authentication | Impersonating another user with stolen credentials |
| **T** | Tampering | Integrity | Modifying data in a database or in transit |
| **R** | Repudiation | Non-repudiation | Performing an illegal action and denying it later |
| **I** | Information Disclosure | Confidentiality | Reading a file you were not granted access to |
| **D** | Denial of Service | Availability | Flooding a server to make it unavailable |
| **E** | Elevation of Privilege | Authorisation | An unprivileged user gaining administrative access |

### S — Spoofing
Illegally accessing and using another user's authentication information.
- **Countermeasures:** strong authentication, MFA, certificate-based identity, anti-phishing controls

### T — Tampering
Malicious modification of data — in a database, in transit, or in configuration.
- **Countermeasures:** input validation, integrity checks (hashing/digital signatures), TLS in transit, immutable audit logs

### R — Repudiation
A user performs an action and later denies it, with no evidence to prove otherwise.

> *Repudiation* is the threat. *Non-repudiation* is the countermeasure property.
- **Countermeasures:** comprehensive audit logs with timestamps and user IDs, digital signatures on critical transactions, log tamper protection

### I — Information Disclosure
Exposure of information to parties who should not have access.
- **Countermeasures:** access control (RBAC, least privilege), encryption (TLS, at-rest), data classification, sanitised error messages (no stack traces)

### D — Denial of Service
Attacks that make a service temporarily or permanently unavailable to valid users.
- **Countermeasures:** rate limiting, CDNs, load balancers, network firewalls, WAFs, DDoS mitigation services

### E — Elevation of Privilege
An unprivileged user gains privileged access and can compromise or destroy the entire system.
- **Countermeasures:** principle of least privilege, sandboxing, input validation (prevents injection-based privilege escalation), proper server-side access control enforcement

---

## STRIDE Summary Table

| Threat | Key Countermeasures | Related OWASP Categories |
|--------|---------------------|--------------------------|
| Spoofing | MFA, certificate identity, session binding | A07 — Identification & Authentication Failures |
| Tampering | Input validation, TLS, digital signatures | A03 — Injection; A08 — Software & Data Integrity |
| Repudiation | Audit logs, digital signatures, timestamps | A09 — Security Logging & Monitoring Failures |
| Information Disclosure | RBAC, encryption, sanitised errors | A02 — Cryptographic Failures; A05 — Security Misconfiguration |
| Denial of Service | Rate limiting, CDN, WAF | A04 — Insecure Design |
| Elevation of Privilege | Least privilege, sandboxing, access control | A01 — Broken Access Control |

---

## STRIDE Applied to DFD Elements

Different DFD elements are susceptible to different STRIDE categories:

| DFD Element | Applicable STRIDE Threats |
|-------------|--------------------------|
| External entity | S (spoofing the entity's identity) |
| Process | S, T, R, I, D, E (all threats apply to application logic) |
| Data store | T (tampering with stored data), I (reading data unauthorised), D (destroying stored data) |
| Data flow | T (intercepting and modifying), I (eavesdropping), D (blocking the flow) |

---

## Related

- [[concepts/secure-software-requirements|Secure Software Requirements]] — CIA+AAA pillars, OSA taxonomy, anti-requirements, misuse case modelling
- [[concepts/owasp-top-10|OWASP Top 10]] — threat catalogue that maps directly to STRIDE categories
- [[concepts/vulnerability-tracking-frameworks|Vulnerability Tracking Frameworks]] — CVSS scores quantify threat severity; CAPEC catalogues attack patterns
- [[concepts/web-security-and-devops|Web Security & DevOps]] — concrete attack implementations (SQLi, XSS, CSRF) that realise STRIDE threats
- [[synthesis/web-security-ssdlc-bridge|Web Security ↔ SSDLC]] — how INF1005 code-level attacks map to ICT2216 STRIDE categories and ASVS requirements
- [[sources/ICT2216-secure-software-development|ICT2216]] — source course
