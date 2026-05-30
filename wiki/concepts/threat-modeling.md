---
type: concept
title: "Threat Modeling"
domain: secure-software-development
complexity: high
tags: [security, threat-modeling, STRIDE, attack-trees, DFD, trust-boundaries, threat-agents]
updated: 2026-05-30
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
| **Threat** | A potential negative event or action that could exploit a vulnerability — a *possibility*, not yet realised |
| **Attack** | The *realisation* of a threat — when a threat agent acts and the threat becomes concrete |
| **Risk** | The consequence or probability of harm that arises when an attack occurs |
| **Vulnerability** | A weakness that a threat can exploit |

**Threat → Attack → Risk: the conceptual triangle**

These three terms are related but distinct. A threat is a possibility. An attack is that possibility acted upon. Risk is the resulting consequence — and crucially, **risk can be zero even when an attack occurs**, if the system is sufficiently protected.

*Example:* A SQL injection attempt (attack) is made against your login form. If your system uses parameterised queries and returns only a generic error message, the risk of sensitive data disclosure is zero — the attack occurred but your controls rendered it harmless. Risk is the product of likelihood *and* impact; strong controls reduce both.

This distinction matters for threat modelling: you model threats (possibilities) to design controls that reduce risk (consequences) — you cannot prevent all attacks, but you can ensure that when attacks happen, the consequences are negligible.

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
- **AI Threats** — emerging and growing category; key attack vectors:
  - **Data poisoning** — injecting malicious training data to corrupt an AI model's outputs or decision boundaries
  - **Prompt injection** — crafting user inputs that override an AI chatbot's system instructions, causing it to disclose restricted information or execute unintended actions
  - Applications using AI chatbots are exposed to both: a malicious user can use prompt injection to extract sensitive data or manipulate the system's behaviour in ways the developer never anticipated

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

*Worked example — typosquatting:* An attacker registers `amazom.com` (double letter) — a domain visually indistinguishable from `amazon.com` at a glance. The site is an exact replica of the legitimate login page. Users enter their credentials, believing they are on the real site. The attacker harvests credentials. The user was spoofed by an identity that looked legitimate.

### T — Tampering
Malicious modification of data — in a database, in transit, or in configuration.
- **Countermeasures:** input validation, integrity checks (hashing/digital signatures), TLS in transit, immutable audit logs

*Worked example — checkout parameter tampering:* At checkout, an application sends a `user_code` field in the POST request identifying whose payment method to charge. An attacker discovers this parameter and modifies `user_code=126` (their own account) to `user_code=123` (a victim's account). The payment is charged to the victim's linked credit card; the attacker receives the goods. The server trusted client-supplied data it should have derived from the authenticated session.

### R — Repudiation
A user performs an action and later denies it, with no evidence to prove otherwise.

> *Repudiation* is the threat. *Non-repudiation* is the countermeasure property — the system's ability to prove what happened despite the attacker's denial.
- **Countermeasures:** comprehensive audit logs with timestamps and user IDs, digital signatures on critical transactions, log tamper protection

*Worked example — signed delivery receipt:* When a parcel is delivered, the recipient signs a receipt confirming delivery. If the customer later claims the parcel never arrived, the signed receipt constitutes non-repudiable proof — the customer's own signature makes denial impossible. The software equivalent: a digital signature on a fund transfer, or a hash-chained audit log entry, provides the same non-repudiable evidence that a specific authenticated user performed a specific action at a specific time.

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
