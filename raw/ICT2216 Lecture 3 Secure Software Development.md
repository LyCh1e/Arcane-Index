# ICT2216 Secure Software Development
## Lecture 3: Secure Software Requirements (Part 2) & Threat Modeling

---

## Part 1 — Secure Software Requirements (Continued)

### Agenda
- Functional Security Requirements (continued)
  - Authorisation Requirements
  - Accountability Requirements
  - General (Application) Security Requirements
  - Operational Security Requirements
  - Other Security Requirements
- Develop Artifacts
  - Anti-requirements
  - Abuse / Misuse Case Modeling
- Software Security Frameworks
  - PCI Software Security Framework
  - NIST Secure Software Development Framework (SSDF)

---

### Authorisation Requirements

Authorisation defines **when a principal may perform an action**.

- Example: Alice is allowed to access her own account, but not Bob's account
- Defines the variety of **access control policies** in the system

**Types of access control:**
- **User-based** — permissions tied directly to individual user accounts
- **Role-based (RBAC)** — permissions tied to roles assigned to users

**Example Authorisation Requirements:**
- Access to highly sensitive secret files will be restricted to authorised users only
- Users shall not be required to re-send credentials after successful authentication (session-based access)
- All unauthenticated users will inherit read-only permissions as part of the *guest* role
- Authenticated users will default to read and write permissions as part of the *general user* role
- Only members of the *administrator* role will have all general user rights, plus permissions to execute privileged operations

**Key question to consider:** How are you going to manage existing users' permissions as they change roles?

---

### Accountability Requirements

Accountability is about **building records of user actions** — it acts as a **detective control**, helping identify:
- When an unauthorised user makes a change
- When an authorised user makes an *unauthorised* change

**Security requirement specifications should define:**
- What to log (what events and data)
- How to log (format, detail level)
- When to log (triggers)
- Storage, rotation, and disposal of logs
- Compliance with industry security standards and best practices

**Requirements for log integrity:**
- Log files must be **protected from tampering**
- Appropriate **access control** on log storage
- Retain enough information to determine the circumstances of a breach or misbehaviour

**Examples:**
- "Every action made on the banking website is logged and retained by the bank."
- "All failed logon attempts will be logged along with the timestamp and the IP address where the request originated."

---

### General (Application) Security Requirements

From an application security perspective, general security requirements should address **session, error, and configuration management**:

1. Session Management
2. Error Management
3. Configuration Management
4. Code Management

---

#### Session Management

Sessions maintain **authenticated state** across a stateless protocol like HTTP.

- On successful authentication, a **Session ID** is issued to track the session
- Requirements must define:
  - **Uniqueness and randomness** of Session IDs (non-guessable)
  - **Expiry** — how long a session remains valid
  - **Non-reusability** — session IDs must not be reused after logout

**Design questions:**
- Does your application allow **concurrent login**?
  - If not: how do you invalidate the previous session?
  - If yes: how do you notify or manage multiple active sessions?
- **Session timeout:** How long before an idle session expires? What is the user experience impact?

---

#### Error Management

When unexpected conditions occur, applications produce errors and stack traces.

- From a security perspective: clearly define **what level of information** should be disclosed in error messages
- Avoid **disclosure threats** — revealing internal application architecture, design details, or configuration information

> Bad practice: Showing a full stack trace to the end user, which may expose framework versions, file paths, or database structure.

---

#### Configuration Management

Configurations drive application features and functionality. Requirements should specify:

- **Initialisation and disposal** of global variables
- **Hashing or encryption** of sensitive configuration data
- Measures to prevent sensitive data leakage from configuration files

---

#### Code Management

- How is the source code stored? (e.g., GitHub, private repositories)
- How is the project deployed? (CI/CD pipeline security)
- How do you **prevent hardcoded credentials** from being committed to version control?

> Real risk: Developers accidentally pushing API keys, passwords, or tokens directly into public repositories.

---

### Operational Security Requirements

Once software is deployed, security must be considered during **operations** to avoid unwanted disclosure or leakage:

1. **Deployment Environment**
2. **Archiving**
3. **Anti-Piracy**

---

#### Deployment Environment

- Security requirements should capture information about the **environment** in which the software is deployed and who will use it
- Drives **environment compliance** and **industry standard** requirements
- Includes not just the production environment, but also the **development and testing environments**

---

#### Archiving

Required for **business continuity**, regulatory compliance, and organisational retention policy.

Requirements should specify:
- **Where** data will be stored (media type)
- **How** data will be stored (online/offline, format, encryption)
- **Data retrieval policy**
- Compliance with organisational and regulatory retention periods

---

#### Anti-Piracy

Part of **Commercial Off-The-Shelf (COTS)** requirements. Includes:
- **Code obfuscation** — making reverse engineering harder
- **Code signing** — verifying authenticity of the software
- **Anti-tampering** mechanisms
- **Licensing** enforcement
- **IP Protection** mechanisms

> Must be addressed during requirement gathering to avoid future legal obligations.

---

### Other Security Requirements

**Sequencing & Timing:**
- Design flaws in sequencing and timing can lead to **race conditions** or **TOC/TOU (Time-of-Check / Time-of-Use)** attacks
- Requirements should identify: race windows, atomic operation needs, or mutex (mutual exclusion / resource locking) requirements

**Procurement Needs:**
- Required when getting proposals from qualified contractors
- Should specify: scope of procurement, evaluation process, deliverables
- Includes selection of **IDE, libraries, and programming language**

**International Regulation:**
- International compliance needs must be captured during requirement gathering
- Example: **GDPR** (General Data Protection Regulation)

---

### Develop Artifacts

> **General Principle:** Once you know what a system does, look at it from the adversary's perspective.
> - How can they *disrupt* the system?
> - How can they *profit* from the system?

Two main techniques:
1. **Anti-requirements**
2. **Abuse / Misuse Case Modeling**

---

### Anti-Requirements

Standard requirements take the form:
> "The system shall [do something] given [inputs]"

**Anti-requirements** describe the things you **do not** want your system to do.

**How to develop anti-requirements:**
1. Consider **undesirable outcomes** — what outcomes are unacceptable?
2. Explore the **inputs** — what inputs could lead to those outcomes?

**Example:**

*Requirement:* The system shall produce a unique identifier valid for N days into the future, given a time, an integer N (0 < N ≤ 7), and a valid authorisation token.

| Undesirable Outcomes | Problematic Inputs |
|---|---|
| System crash | Time mis-formatted |
| Non-unique identifier produced | N ≤ 0 or N > 7 |
| Identifier with incorrect validity period | Invalid authorisation token |

---

### Abuse / Misuse Case Modeling

- **Use cases** describe what a system *should* do
- **Abuse cases** describe what it *should not* do

Abuse cases can illustrate security requirements visually using UML.

**Process:**
1. Start with existing use cases
2. Consider how each process can be **interdicted or corrupted**
3. Identify **attackers** (analogous to identifying actors in use cases)
4. Model using UML diagrams
5. Update with corresponding **security requirements**

---

**Exercise — ATM System:**

Functional use cases:
- Login
- Withdraw Money
- Logout

Abuse / misuse cases to model:
- **Shoulder snooping** — attacker observes PIN entry
- **Steal card** — attacker takes the physical card
- **Copy card** — attacker clones the card (skimming)

**Derived ATM Security Requirements:**

**Input Validation:**
- PIN: 6 input fields, digits 0–9 only
- Characters: English characters in ASCII or Unicode (4 languages used in Singapore)
- Only positive numbers allowed for withdrawal amounts (syntactic)
- Total withdrawal must not exceed account balance (semantic)

**Velocity Checking:**
- PIN blocked after **3 wrong attempts**
- Limit login attempts per hour (e.g., Gmail-style blocking)
- Limit transactions per minute and withdrawal amounts per day

**Transaction Integrity:**
- Operations can be interrupted — just because a transaction starts does not mean it completes
- If a user forgets to remove their ATM card:
  - Alert the user with sounds
  - Do not dispense cash until card is removed
  - Swallow the card after a timeout to prevent misuse

**Visibility:**
- Do not display the PIN as it is typed (mask input)
- Do not display account information once the card is removed

---

### Software Security Frameworks

> "How can I ensure the application is secure in the design phase?"

Follow international standards when designing your application.

---

#### Payment Card Industry Software Security Framework (PCI SSF)

One of the most stringent security requirement frameworks — designed to:
- Protect payment transactions and data
- Minimise vulnerabilities
- Defend payment software from attacks throughout the software lifecycle

**PCI SSF Requirement Example:**

*Requirement:* Sensitive production data is protected when retained on vendor systems and securely deleted when no longer needed.

*Test Requirements:*
- Assess that a mature process exists to ensure sensitive production data protection and secure deletion
- Verify that sensitive production data is **not resident on vendor systems** unless approved and justified
- Confirm data is appropriately protected where retained
- Confirm secure deletion processes render data **irretrievable**

> **Discussion:** Can I use real customer data in a development environment? (UAT = User As A Tester?)

---

#### NIST Secure Software Development Framework (SSDF)

> https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04232020.pdf

Intended to facilitate communications about secure software development practices amongst **business owners, software developers, and cybersecurity professionals**.

Provides a **core set of high-level secure software development practices.**

**Example — Design Software to Meet Security Requirements (PW.1):**
- Identify and evaluate applicable security requirements for the software's design
- Determine what security risks the software is likely to face in production
- Determine how those risks should be mitigated by the software's design
- Justify any risk-based decisions to relax or waive security requirements

**Specific NIST SSDF actions:**
- Train the development team (especially security champions) or collaborate with a threat modeling expert to create threat and attack models using a **risk-based approach**
- Perform **more rigorous assessments** for high-risk areas: sensitive data protection, authentication, authorisation, access control, and credential management
- **Review vulnerability reports and statistics** for previous versions of the software

---

### Conclusion — Secure Software Requirements

Before you design any application, **always consider security requirements**:

| Category | Key Concern |
|---|---|
| Confidentiality | Prevent unauthorised data disclosure (at rest, in transit, in processing) |
| Integrity | Prevent unauthorised modification; use hashing and digital signatures |
| Availability | Ensure uptime SLAs; plan for DDoS; define MTD and RTO |
| Authentication | Verify identity; implement MFA; follow NIST 800-63 password guidelines |
| Authorisation | Define who can do what; implement RBAC; apply least privilege |
| Accountability | Log all significant actions; protect logs; meet retention requirements |

---

### References
- PCI Secure SLC Standard: https://www.pcisecuritystandards.org/documents/PCI-Secure-SLC-Standard-v1_0.pdf
- SANS SWAT Checklist: https://software-security.sans.org/resources/swat
- NIST Password Guidelines: https://www.bankinfosecurity.com/whitepapers/best-practices-for-implementing-nist-password-guidelines-special-w-5593

---
---

## Part 2 — Threat Modeling

### Opening Question
> After understanding secure requirements… are they enough?

Requirements alone don't tell you *how* attackers will actually try to break your system. **Threat modeling** provides a more systematic and disciplined way to reason about security threats.

---

### Agenda
- Introduction to Threats
- Identifying Threats (trust boundaries, entry/exit points, data flows, mis-actors)
- Introduction to Threat Modeling
- Attack Trees
- Microsoft STRIDE
- CVSS

---

### What Is a Threat?

Threats to software include:
- **Disclosure threats** — against confidentiality
- **Alteration threats** — against integrity
- **Destruction threats** — against availability
- Authentication bypass, privilege escalation, impersonation
- Man-in-the-middle attacks, session hijacking, relay attacks, injection

> **Risk vs. Threat:**
> - A **threat** is a potential negative event or action that could exploit a vulnerability
> - A **risk** is the *likelihood* and *impact* of that threat being realised

---

### Types of Threats

#### Human Threats

| Threat Agent | Description |
|---|---|
| **Ignorant User** | Causes unintentional errors; best mitigated through user education |
| **Accidental Discoverer** | Normal user who stumbles upon a functional mistake and gains unintended access — never sought to bypass security |
| **Curious Attacker** | Ordinary user who notices an anomaly and decides to explore it further |
| **Script Kiddie** | Executes hacker scripts without understanding the impact; often doesn't hide their footprint |
| **Insider** | Disgruntled employee or contractor with privileged insider knowledge — one of the most dangerous threat agents |
| **Organised Cybercriminals** | Highly skilled, professionally paid attackers seeking high financial gain |
| **Third-party / Supplier** | Can embed malicious logic (logic bombs, Trojans) in software as it moves through the supply chain |
| **Nation-State Hackers** | The most powerful and well-resourced threat actors |

#### Non-Human Threats
- **OS Threats** — vulnerabilities at the operating system level
- **Malware Threats** — viruses, ransomware, spyware
- **Network Threats** — interception, spoofing, flooding
- **AI Threats** — emerging threat category (AI-driven attacks)

---

### Identifying Threats — Key Steps

#### 1. Identify Trust Boundaries

> A **trust boundary** is the point at which the trust level or privilege changes.

- Identification of trust boundaries is critical to ensure adequate levels of protection are designed within each boundary
- Examples: boundary between public internet and internal network, between user and admin roles, between frontend and backend

---

#### 2. Identify Entry Points and Exit Points

**Entry points** — items that take in inputs; each is a potential threat source:
- Every entry point must be explicitly identified and safeguarded
- Web application examples: Search page, Login page, Registration page, Checkout page, Account Maintenance page

**Exit points** — items that display or output information from the system:
- Exit points can be sources of **information leakage**
- Web application examples: Search Results page, Product page, View Cart page

---

#### 3. Identify Privileged Functionality

- Identify any functionality that allows **elevation of privilege** or execution of privileged operations
- Examples: all administrator functions, critical business transactions (e.g., fund transfers, user role changes)

---

#### 4. Identify Data Flows

**Data Flow Diagrams (DFDs)** help understand how the application:
- Accepts data
- Processes data
- Handles data as it crosses different **trust boundaries**

DFD elements:
- **External entities** — users, external systems
- **Processes** — application logic
- **Data stores** — databases, files
- **Data flows** — arrows showing data movement

**Example — College Library Website:**

Actors:
- **Students** — Login, search, request books
- **Staff** — Login, search, request books
- **Librarians** — Login, add books, add users, search, request books

A DFD for the login flow would show: User → Login Process → Authentication Store → Session Token returned to User

---

#### 5. Identify Mis-actors (Attackers)

Both **human and non-human** mis-actors must be considered.

**Human mis-actor examples:**
- External hackers
- Hacktivist groups
- Rogue administrators
- Fraudulent sales administrators

**Non-human mis-actor examples:**
- Malware
- Ransomware

**Mis-actor categories by network position:**

| Mis-actor Type | Capabilities | Example Attacks |
|---|---|---|
| **Web attacker** (anonymous internet user) | Measure request/response size and timing; run parallel sessions; send malformed inputs | SQL injection, XSS, CSRF, buffer overflow |
| **Network attacker** (on the same unencrypted network) | Read/measure other messages; intercept, duplicate, modify messages | Session hijacking, denial of service |
| **Co-located attacker** (on the same machine) | Read/write user files and memory; snoop keystrokes; read/write to display | Password theft |

**Threat model implications:**

| Assumed Threat Model | Implication |
|---|---|
| Web attacker only | Message traffic can be considered secure; no need to encrypt (e.g., telnet on internal network) |
| Network attacker | Must use encryption: Secure Wi-Fi (link layer), IPSec (network layer), SSL/TLS (application layer) |
| Co-located attacker | Do not store unencrypted secrets (passwords, tokens) in local files or memory |

> **Warning — Bad Models:** Any assumptions you make in your threat model are potential weaknesses an adversary can exploit. Assuming "no network attacker" may be invalid due to the prevalence of Wi-Fi networks.

---

### Introduction to Threat Modeling

Threat modeling is a **structured approach** to identifying and addressing security risks during design — before writing code.

**The threat modeling process:**
1. Define security requirements
2. Create an application diagram (DFD, architecture diagram)
3. Identify threats
4. Mitigate threats
5. Validate that threats have been mitigated

**A threat model should include:**
- A description / design / model of what you're concerned about
- A list of **assumptions** (that can be revisited as the threat landscape changes)
- A list of **potential threats** to the system
- A list of **actions** to take for each threat
- A way of **validating** the model and verifying the success of mitigations

---

### Techniques for Determining Threats

Two main techniques:
1. **Attack Trees** — visual, goal-oriented representation of how an attacker achieves an objective
2. **Categorised Threat Lists** — structured catalogues of known threat types

Popular categorised threat lists:
- NSA IAM methodology
- OCTAVE risk modeling
- OWASP Top 10
- CWE Top 25
- **Microsoft STRIDE** ← covered in detail below

---

### Attack Trees

**Attack trees** depict attacks on a system in a tree structure:
- The **root** = the attacker's goal
- The **leaves** = the individual ways to achieve that goal
- Each goal is represented as a separate tree

**Usage:** A system threat analysis produces a *set* of attack trees, one per attacker goal. This makes it easy to reason about how complex, multi-step attacks can be broken down and defended.

**Example structure:**
```
[Root: Gain unauthorised access to account]
├── [Steal credentials]
│   ├── Phishing
│   ├── Credential stuffing
│   └── Keylogging
└── [Bypass authentication]
    ├── SQL injection on login
    └── Session token forgery
```

---

### Microsoft STRIDE

STRIDE is a **goal-based threat modeling framework** — it considers the goals of the attacker to categorise threats systematically.

| Letter | Threat | Violated Property |
|---|---|---|
| **S** | Spoofing | Authentication |
| **T** | Tampering | Integrity |
| **R** | Repudiation | Non-repudiation |
| **I** | Information Disclosure | Confidentiality |
| **D** | Denial of Service | Availability |
| **E** | Elevation of Privilege | Authorisation |

---

#### S — Spoofing

**Involves:** Illegally accessing and using another user's authentication information (e.g., username and password).

- Attacker impersonates a legitimate user or system
- Countermeasures: strong authentication, MFA, certificate-based identity

---

#### T — Tampering

**Involves:** Malicious modification of data.

Examples:
- Unauthorised changes to persistent data in a database
- Alteration of data flowing between two systems over a network

- Countermeasures: integrity checks (hashing, digital signatures), input validation, TLS

---

#### R — Repudiation

**Involves:** A user performs an action and later *denies* doing it — and no evidence exists to prove otherwise.

Example: A user performs an illegal operation in a system that lacks the ability to trace the action.

**Non-repudiation** counters this threat:
- Example: A user purchases an item and signs for it on receipt — the vendor keeps the signed receipt as evidence

> **Repudiation vs. Non-Repudiation:**
> - *Repudiation* = the threat (user can deny an action)
> - *Non-repudiation* = the property/control that prevents successful denial

- Countermeasures: comprehensive audit logs, digital signatures on transactions, timestamping

---

#### I — Information Disclosure

**Involves:** Exposure of information to individuals who should not have access.

Examples:
- A user can read a file they were not granted access to
- An intruder reads data in transit between two computers

- Countermeasures: access control, encryption (TLS), need-to-know principle, data classification

---

#### D — Denial of Service

**Involves:** Attacks that deny service to valid users — making a web server temporarily unavailable or unusable.

- Protection against DoS threats is essential for **system availability and reliability**
- Countermeasures: rate limiting, CDNs, load balancers, network firewalls, WAFs

---

#### E — Elevation of Privilege

**Involves:** An unprivileged user gains privileged access and can compromise or destroy the entire system.

- The attacker effectively bypasses all system defences and becomes part of the trusted system
- Countermeasures: principle of least privilege, sandboxing, input validation to prevent injection, proper access control enforcement

---

### STRIDE Summary Table

| Threat | Example Attack | Key Countermeasure |
|---|---|---|
| Spoofing | Credential theft, session hijacking | Strong authentication, MFA |
| Tampering | SQL injection, man-in-the-middle | Input validation, integrity checks, TLS |
| Repudiation | Illegal action with no audit trail | Logging, digital signatures |
| Information Disclosure | Unauthorised file access, packet sniffing | Access control, encryption |
| Denial of Service | Flood attack, resource exhaustion | Rate limiting, DDoS mitigation |
| Elevation of Privilege | Exploiting buffer overflow, insecure deserialization | Least privilege, sandboxing, input validation |

---

### References
- Microsoft Threat Modeling Tool Threats: https://docs.microsoft.com/en-us/azure/security/azure-security-threat-modeling-tool-threats
- Threat Modeling — 12 Available Methods (SEI Blog): https://insights.sei.cmu.edu/sei_blog/2018/12/threat-modeling-12-available-methods.html
- CVSS Specification Document: https://www.first.org/cvss/specification-document

---

*End of Lecture 3*
