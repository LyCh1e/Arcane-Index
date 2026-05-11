# ICT2216 Secure Software Development
## Lecture 2: Secure Software Concepts (Part 2) & Secure Software Requirements

---

## Part 1 — Vulnerability Tracking & Software Assurance Methodologies

### Agenda (Continued from Lecture 1)
- Vulnerability Tracking — CVEs, NVD, CAPEC, MITRE ATT&CK
- Software Assurance Methodologies — BSIMM, OpenSAMM, Microsoft SDLC

---

### Vulnerability Tracking

> "As a software developer, how can I learn about an attack so that I can do the proper patching?"
> "As a security engineer, where can I get day-one attack information to prevent it from affecting my system?"

**Tools to subscribe to:**
- **CVE** — Common Vulnerabilities and Exposures
- **NVD** — National Vulnerability Database

**Tools to understand attack patterns:**
- **CAPEC** — Common Attack Pattern Enumeration and Classification
- **MITRE ATT&CK**

---

### Common Vulnerability Scoring System (CVSS)

CVSS provides a standardised numerical score (0–10) representing the severity of a vulnerability, based on factors like:
- Attack vector and complexity
- Privileges required
- User interaction needed
- Impact on Confidentiality, Integrity, and Availability

---

### CVE — Common Vulnerabilities and Exposures

> https://cve.org/

- A publicly available directory of known information security vulnerabilities and exposures
- Each vulnerability is assigned a unique **CVE ID** (e.g., `CVE-2026-7791`)
- Developers and researchers can submit new findings to CVE

---

### NVD — National Vulnerability Database

> https://nvd.nist.gov/

Extends CVE data with:
- **Impact analysis** of the vulnerability
- **Mitigation methodologies**
- **CVSS Severity Rating**
- **Fix information**
- **Vulnerable software versions**
- **SCAP Mappings**
- **CPE (Common Platform Enumeration) Information**

---

### CAPEC — Common Attack Pattern Enumeration and Classification

- A publicly available catalog of **common attack patterns**
- Helps developers and security engineers understand how adversaries exploit weaknesses
- Each attack pattern captures:
  - How the attack is designed and executed
  - Guidance on mitigating the attack's effectiveness
- Useful for those developing applications or administering cyber-enabled capabilities

---

### MITRE ATT&CK

> A globally-accessible knowledge base of adversary **tactics and techniques** based on real-world observations.

- Organises attacker behaviour into tactics (the *why*) and techniques (the *how*)
- Covers multiple platforms: Enterprise, Mobile, ICS
- Provides **mitigation techniques** mapped to specific attack categories
- Widely used for threat intelligence, red teaming, and security gap analysis

---
---

### Software Assurance Methodologies

Three standard models:
1. **BSIMM** — Building Security In Maturity Model
2. **OpenSAMM** — Open Software Assurance Maturity Model
3. **Microsoft SDL** — Secure Software Development Life Cycle

---

### 1. BSIMM — Building Security In Maturity Model

> Started in 2008 by Gary McGraw and others; inspired by the Capability Maturity Model (CMM)

- Examines **Software Security Initiatives (SSIs)** across organisations
- Acts as a "measuring stick" — describes the state of the art in real-world software security
- Now at **BSIMM-16 (January 2026):**
  - 128 activities
  - 8 industries
  - 111 organisations
  - ~91,200 applications protected
  - ~223,700 developers covered

#### BSIMM Goals
For organisations running a Software Security Initiative, BSIMM aims to:
- Inform **risk management decisions**
- Clarify the "right things to do" for stakeholders
- **Reduce costs** through standard, repeatable processes
- **Improve code quality**

Activities are rolled out according to the **maturity level** of the organisation.

#### BSIMM Software Security Framework

| Domain | Practices |
|---|---|
| Governance | Strategy & Metrics, Compliance & Policy, Training |
| Intelligence | Attack Models, Security Features & Design, Standards & Requirements |
| SSDL Touchpoints | Architecture Analysis, Code Review, Security Testing |
| Deployment | Penetration Testing, Software Environment, Configuration Management & Vulnerability Management |

- 12 practices across 4 domains
- Each practice has **maturity levels 1–3**
- Over 128 activities in total

#### BSIMM16 Key Trends (2026)
- **AI is the defining challenge:** Organisations must secure AI-powered coding assistants *and* defend against AI-enabled attacks
- **Government regulations are accelerating investment:** Global mandates push focus on software supply chain transparency and securing dev environments
- **Software supply chain security is rising rapidly:** Focus expanding from internally developed code to the entire supply chain ecosystem
- **Training is shifting:** Traditional multi-day courses replaced by **just-in-time, bite-sized learning** that fits modern dev workflows

---

### 2. OpenSAMM — Open Software Assurance Maturity Model

> An open framework under the **OWASP project**

- Helps organisations formulate and implement a **software security strategy** tailored to their specific risks
- Defines **Business Functions**, each with **3 Security Practices**
- Security Practices cover all areas relevant to software security assurance

#### Maturity Levels (per Practice)

| Level | Description |
|---|---|
| 0 | Implicit starting point — Practice not fulfilled |
| 1 | Initial understanding and ad hoc provision of the Practice |
| 2 | Increased efficiency and/or effectiveness |
| 3 | Comprehensive mastery of the Practice at scale |

#### Scorecards
- **Gap analysis:** Capture scores from detailed assessments vs. expected performance levels
- **Demonstrating improvement:** Compare scores before and after an iteration of the assurance programme

---

### 3. Microsoft Secure Development Lifecycle (SDL)

> Developed by Microsoft to help developers build secure software and meet compliance requirements

- Introduces **security and privacy considerations throughout all phases** of development
- Helps reduce development costs while building highly secure software
- Aligns with the phases of the SSDLC already covered in this module

---

### Summary — Secure Software Concepts

1. **Relationship between Software and Security** — network controls alone are insufficient; application-layer security is required
2. **Software Vulnerabilities:**
   - OWASP Top 10 (2025)
   - CVEs and NVD for tracking and impact assessment
   - CAPEC for understanding attack patterns
   - MITRE ATT&CK for real-world adversary tactics
3. **Software Assurance Methodologies:**
   - BSIMM — maturity model based on real-world data
   - OpenSAMM — open framework for tailored security strategy
   - Microsoft SDL — lifecycle-integrated security practices

---
---

## Part 2 — Secure Software Requirements

### Opening Case Studies

**Ransomware Attacks:** Growing threat to organisations of all sizes

**MyRepublic Data Breach (Singapore):**
- Unauthorised access occurred on a **third-party data storage platform** used to store mobile customer personal data
- The breach was contained after discovery
- Highlights risks of third-party data storage and the importance of vendor security

---

### Agenda
- Introduction to Secure Software Requirements (IEEE Standard 729)
- Requirement Process in SSDLC
  - Feasibility Study
  - Secure Requirement Gathering
  - Secure Software Requirement Specification
  - Secure Software Requirement Validation
- Examples: PCI Software Security Framework, NIST SSDF

---

### Introduction to Secure Software Requirements

**IEEE Standard 729 Definition:**
> "A condition or capability needed by a user to solve a problem or achieve an objective."
> "A condition or capability that must be met or possessed by a system to satisfy a contract, standard, specification, or other formally imposed document."

> **Without Software Requirements, Software will Fail.**
> **Without Secure Software Requirements, Organisations will [fail].**

---

### Types of Software Requirements

#### Functional (Behavioural) Requirements — *WHAT*
- Functions the system must perform
- Inputs expected, outputs produced, and relationships between them

**Examples (LMS):**
1. The LMS shall allow the administrator to create modules
2. The LMS shall allow instructors to upload documents
3. The LMS shall provide appropriate viewers for users to read documents

#### Non-Functional Requirements — *HOW*
- Properties the system must possess

**Examples:**
- The system shall run on Windows 7, Windows 10, and macOS 10.4
- User logins will take at most 20 seconds from submitting credentials to seeing the first screen
- The system will require less than 10 Mbps network speed to handle 100 concurrent users

---

### What Are Security Requirements?

> "Robust software security requirements help you lock down what your software does so that it can be used only as intended." — Jamie Boote

**Open Security Architecture (OSA) Taxonomy:**

| Type | Description | Derived From |
|---|---|---|
| **Secure Functional Requirements** | Security-related description integrated into each functional requirement; includes what shall *not* happen | Misuse cases |
| **Functional Security Requirements** | Security *services* the system must provide (e.g., authentication, authorisation, backup, clustering) | Best practices, policies, regulations |
| **Non-Functional Security Requirements** | Architectural security properties (e.g., robustness, performance, scalability) | Architectural principles, good practice standards |
| **Secure Development Requirements** | Required activities *during development* to assure the outcome is not subject to vulnerabilities (e.g., data classification, coding guidelines, test methodology) | Best practice frameworks like CLASP |

**Connection to prior modules:**
- INF2001 covered Functional & Non-Functional Requirements
- ICT2216 adds: Secure Functional Requirements, Functional Security Requirements, Non-Functional Security Requirements (CIA-AAA)

---

### Requirement Process in SSDLC

1. Feasibility Study
2. Secure Requirement Gathering
3. Secure Software Requirement Specification
4. Secure Software Requirement Validation

---

### 1. Feasibility Study

Any discussion about software security should start with:
- **Stakeholders** — who is involved?
- **Assets** — what needs to be protected?
- **Threats to assets** — what could go wrong?
- **Attacker model** — employees, customers, script kiddies, criminals, nation-states (APTs)?

**Sources for security requirements:**
- Software functionality
- Policies, standards, guidelines, patterns, and practices to comply with
- Regulations and compliance initiatives

---

### 2. Secure Requirement Gathering

Typical security requirements follow the **CIA-AAA** model:

1. Confidentiality
2. Integrity
3. Availability
4. Authentication
5. Authorisation
6. Accountability

---

#### Confidentiality Requirements

Sensitive information must not be leaked to unauthorised parties:
- **Privacy** for individuals
- **Confidentiality** for data

Consider confidentiality controls for data:
- **At Rest** — stored on disk or database
- **In Transit** — transmitted over a network
- **In Processing** — when being computed or transformed

Security checklist should specify:
- Protocols to use
- Encryption strength
- Random Number Generator processes

> Reference: SANS Securing Web Application Technologies (SWAT) Checklist — https://software-security.sans.org/resources/swat

**Data requirements to consider:**
- What data does the application need to store?
  - Personal data?
  - Financial data?
  - Communication data?
  - Credit card information?
- **Personal Data Protection Act (PDPA)** must be considered!

**Data Leakage — Direct vs. Indirect:**
- **Direct:** Alice hacks into the bank to view Bob's balance
- **Indirect (side channel):** Alice determines Bob has a DBS account because the login failure response is slightly *slower* for valid usernames

**Case Study — SingHealth Data Breach:**
- Suspicious login activity on the database was identified but not categorised as a cyberattack
- Lacked an **incident reporting framework**
- Staff were unfamiliar with security policies and unaware the issue needed to be reported to Singapore's Cyber Security Agency (CSA)

---

#### Integrity Requirements

Prevention against unauthorised modifications:
- **System integrity** — the system itself has not been tampered with
- **Data integrity** — data has not been altered without authorisation

Ensures **reliability and accuracy** of information.

Security controls:
- **Hashing** — verify data has not changed
- **Digital Signatures** — verify authenticity and integrity
- Specifications: protocols, salt length, hash function choice

**Example:** Released software should provide the recipient with a computed **checksum** and the **hash function** used, so the recipient can validate accuracy and completeness.

> **Discussion:** Is downloading software from an official website always safe? (Not necessarily — supply chain attacks can compromise official channels)

> Reference: OWASP Security Code Checklist (also relates to static code analysis covered in the second half of the module)

---

#### Availability Requirements

Ensures protection against unwanted destruction or disruption of services.

Should be captured as part of **Service Level Agreement (SLA)** components:
- **MTD** — Maximum Tolerable Downtime
- **RTO** — Recovery Time Objective

**(Distributed) Denial of Service (DoS) attacks** compromise availability by:
- Flooding the system with useless work
- Cutting off access to the network
- Triggering infinite loops (non-termination)

**DDoS Mitigation Strategies:**
- DNS load balancing
- Server load balancing
- Content Distribution Network (CDN)
- Firewalls:
  - Layer 3: Network Firewall
  - Layer 5/7: Application Firewall
- **Hide all IP addresses**

**Example Availability Requirements:**
- The software shall ensure high availability of **five nines (99.999%)**
- Up to **300 concurrent users** at any given point in time
- Software and data shall be replicated across data centres for load balancing and redundancy
- Mission-critical functionality restored within **1 hour** of disruption
- Mission-essential functionality restored within **4 hours** of disruption
- Mission-support functionality restored within **24 hours** of disruption

---

#### Authentication Requirements

**Factors of authentication:**
- Something you **know** (password, PIN)
- Something you **have** (smartphone, token)
- Something you **are** (biometric)

**2-Factor Authentication (2FA):**
- Passwords alone can be weak
- Biometrics can be too invasive
- Users can lose devices
- Use **2 or more factors** for stronger authentication
  - e.g., online banking: password + OTP on smartphone
  - SingPass 2FA

**Password Requirements to consider:**
- How to handle (store) user passwords?
- How to enforce password complexity?
- Password expiry policy?
- Forgot password / account recovery flow?

**Problem with complex password policies:**
- More passwords are written down
- More passwords are reused (average enterprise password reused **2.7 times**)
- Predictable "complexity" patterns (e.g., `r@Ymond1`) undermine the purpose

**New NIST Password Guidelines (NIST 800-63):**
- **8-character minimum**
- **No complexity or special character requirements**
- **No password expiration**
- **Check against dictionaries and lists of previously breached passwords**

> **Design Question:** What maximum password length should your application allow?
> What maximum username length should your application allow?

---

#### Authorisation Requirements *(preview — covered further in upcoming lectures)*

- What can each authenticated user *do*?
- Role-based access control (RBAC)?
- Principle of least privilege?

#### Accountability Requirements *(preview)*

- How are actions logged and attributed to users?
- Audit trails?
- Non-repudiation?

---

### Other Security Requirement Areas *(upcoming)*

- Abuse/Misuse Cases — deriving security requirements from attacker perspectives
- Artifact development
- Functional Security Requirements coverage: CIA, Authentication, Authorisation, Accountability

---

### Key Frameworks for Secure Software Requirements

#### Payment Card Industry Software Security Framework (PCI SSF)
- Requirements for organisations developing and maintaining payment software
- Covers secure design, data protection, authentication, and vulnerability management

#### NIST Secure Software Development Framework (SSDF)
- A set of fundamental, sound, and secure software development practices
- Organised around four groups:
  - **Prepare the Organisation (PO)**
  - **Protect the Software (PS)**
  - **Produce Well-Secured Software (PW)**
  - **Respond to Vulnerabilities (RV)**

---

*End of Lecture 2*
