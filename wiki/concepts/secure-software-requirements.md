---
type: concept
title: "Secure Software Requirements"
domain: secure-software-development
complexity: high
tags: [security, requirements, CIA, AAA, confidentiality, integrity, availability, authentication, authorisation, accountability, owasp, swat, NIST, SSDLC]
updated: 2026-05-11
---

# Secure Software Requirements

Security requirements are a structured extension of functional and non-functional requirements. They are derived from six pillars grouped into two triads: the **CIA triad** (data-focused) and the **AAA triad** (user-focused). Every pillar follows the same three-step pattern: identify the asset or actor, identify the risk, define the requirement.

**IEEE Standard 729 definition:**
> "A condition or capability needed by a user to solve a problem or achieve an objective."
> "A condition or capability that must be met or possessed by a system to satisfy a contract, standard, specification, or other formally imposed document."

> Without software requirements, software will fail. Without **secure** software requirements, organisations will fail.

---

## Types of Requirements

### Functional (Behavioural) Requirements — *WHAT*

Functions the system must perform — inputs, outputs, and their relationships.

*LMS example:* "The LMS shall allow instructors to upload documents."

### Non-Functional Requirements — *HOW*

Properties the system must possess — performance, compatibility, scalability.

*Example:* "User logins will take at most 20 seconds from submitting credentials to the first screen."

---

## OSA Taxonomy of Security Requirements

The Open Security Architecture (OSA) identifies four distinct types:

| Type | Description | Derived From |
|------|-------------|-------------|
| **Secure Functional Requirements** | Security constraints integrated into each functional requirement; includes what shall *not* happen | Misuse/abuse cases |
| **Functional Security Requirements** | Security *services* the system must provide (authentication, authorisation, backup, audit) | Best practices, policies, regulations |
| **Non-Functional Security Requirements** | Architectural security properties (robustness, performance, scalability) | Architectural principles, good-practice standards |
| **Secure Development Requirements** | Activities required *during development* to prevent vulnerabilities (data classification, coding guidelines, test methodology) | Frameworks such as CLASP |

---

## Requirement Process in the SSDLC

### 1. Feasibility Study

Before gathering requirements, establish context:
- **Stakeholders** — who is involved?
- **Assets** — what needs to be protected?
- **Threats to assets** — what could go wrong?
- **Attacker model** — employees, customers, script kiddies, criminals, nation-states (APTs)?

Sources for security requirements:
- Software functionality and business logic
- Policies, standards, guidelines, and patterns
- Regulations and compliance initiatives (PDPA, GDPR, PCI DSS)

### 2. Secure Requirement Gathering

Apply the **CIA-AAA model** (see below) to derive a structured set of requirements.

### 3. Secure Software Requirement Specification

Document requirements in a structured specification linked to functional requirements. Reference checklists (SANS SWAT, OWASP ASVS) to ensure completeness.

### 4. Secure Software Requirement Validation

Review requirements against attacker models, misuse cases, and compliance obligations. Validate with stakeholders before design begins.

---

## Why Requirements First

Most security vulnerabilities are not implementation bugs — they are missing requirements. A developer cannot implement "store passwords securely" if the requirement was never stated. Security requirements make implicit expectations explicit and auditable before a single line of code is written.

---

## CIA Triad (Data-Focused)

### Confidentiality

Sensitive information must not be disclosed to unauthorised parties.

1. **Define** — what data must be protected? (PII, credentials, session tokens, financial records, personal data under PDPA)
2. **Identify risks** — insecure storage, transmission without TLS, excessive logging, direct and indirect (side-channel) leakage
3. **Define requirements** — encrypt data at rest, in transit, and in processing; apply least-privilege access; mask sensitive fields in logs

**Data states to cover:**
- **At rest** — stored on disk or in a database
- **In transit** — transmitted over a network
- **In processing** — being computed or transformed

**Direct vs. indirect data leakage:**
- **Direct:** Alice hacks the database to read Bob's balance.
- **Indirect (side channel):** Alice determines Bob has a DBS account because the login failure response is slightly *slower* for valid usernames.

**Case Study — SingHealth Data Breach:** Suspicious database login activity was identified but not classified as a cyberattack. The organisation lacked an incident-reporting framework, and staff were unaware they needed to report to Singapore's Cyber Security Agency (CSA).

### Integrity

Prevention against unauthorised modification of the system or its data.

- **System integrity** — the system itself has not been tampered with.
- **Data integrity** — data has not been altered without authorisation.

1. **Identify** — which data must remain unmodified? (user records, transaction logs, configuration)
2. **Identify risks** — SQL injection, CSRF, insecure direct object references, log tampering, supply chain compromise
3. **Define requirements** — parameterised queries; CSRF tokens; input validation; immutable audit logs; checksums / digital signatures on released software

**Example:** Released software should include a computed **checksum** and the **hash function** used, enabling recipients to verify accuracy and completeness before installation.

### Availability

Ensures protection against unwanted destruction or disruption of services.

1. **Define** — what uptime and resilience levels are required? (captured in SLAs)
2. **Identify risks** — DoS/DDoS, single points of failure, resource exhaustion, infinite loops
3. **Define requirements** — rate limiting; redundant infrastructure; graceful degradation; tested backup/restore

**SLA terminology:**
- **MTD** — Maximum Tolerable Downtime
- **RTO** — Recovery Time Objective

**DDoS mitigation strategies:**
- DNS and server load balancing
- Content Distribution Network (CDN)
- Network firewall (Layer 3) and application firewall (Layer 5/7)
- **Hide all real IP addresses** (prevent direct volumetric attacks)

**Example availability requirements:**
- Five nines uptime (99.999%)
- Up to 300 concurrent users at any given time
- Mission-critical functionality restored within **1 hour**; mission-essential within **4 hours**; mission-support within **24 hours**

---

## AAA Triad (User-Focused)

### Authentication

Verifies that a user is who they claim to be.

**Factors of authentication:**
- Something you **know** (password, PIN)
- Something you **have** (smartphone, hardware token)
- Something you **are** (biometric)

1. **Define users** — who interacts with the system? (public users, registered users, admins, service accounts)
2. **Identify risks** — credential stuffing, brute force, session fixation, phishing
3. **Define requirements** — MFA for privileged accounts; secure session management; account lockout; password recovery flow

**NIST 800-63 Password Guidelines (current best practice):**

| Guideline | Recommendation |
|-----------|---------------|
| Minimum length | 8 characters |
| Complexity requirements | **None** — do not mandate special characters |
| Expiration | **No** mandatory expiration |
| Breach checking | **Yes** — check against known breached-password lists |

> The traditional approach (complex rules + frequent expiration) causes more harm: passwords are written down, reused, or follow predictable patterns (e.g., `r@Ymond1`). The average enterprise password is reused **2.7 times**.

**Design questions to answer:**
- How are passwords stored? (bcrypt / Argon2 with salt — never MD5/SHA-1 unsalted)
- What is the maximum password length? (ensure the hashing function handles it)
- What is the account recovery / forgot-password flow?

### Authorisation

Controls what an authenticated user is permitted to do.

1. **Determine** — are there different user roles? (guest, user, admin, superadmin)
2. **Identify risks** — privilege escalation, IDOR, missing function-level access control
3. **Define requirements** — role-based access control (RBAC); server-side enforcement; deny by default; least privilege per role

### Accountability

Ensures user actions can be traced and attributed.

1. **Define** — what information is needed for accountability? (who, what, when, from where)
2. **Identify risks** — log tampering, insufficient logging, missing timestamps, shared accounts
3. **Define requirements** — immutable audit log for all state-changing actions; log authentication events (success and failure); include user ID, timestamp, IP, action, and result

---

## Reference Checklists

- **SANS SWAT Checklist** — https://software-security.sans.org/resources/swat — practical web application security requirements grouped by category
- **OWASP ASVS** — Application Security Verification Standard — tiered requirements (Level 1 Opportunistic → Level 3 Advanced); used by SecurityRAT for automated requirement generation
- **SecurityRAT** — see [[securityrat]] — declare your artifact type, generate the applicable ASVS requirements automatically

---

## Key Frameworks for Secure Software Requirements

### PCI Software Security Framework (PCI SSF)

Requirements for organisations developing and maintaining payment software. Covers:
- Secure design
- Sensitive data protection
- Authentication and authorisation
- Vulnerability management

### NIST Secure Software Development Framework (SSDF)

A set of fundamental, sound, and secure software development practices. Organised around four practice groups:

| Group | Code | Focus |
|-------|------|-------|
| Prepare the Organisation | PO | Roles, tools, processes, and requirements |
| Protect the Software | PS | Source code and artefact protection |
| Produce Well-Secured Software | PW | Design, implementation, testing |
| Respond to Vulnerabilities | RV | Identifying, fixing, and disclosing vulnerabilities |

---

## Relationship to Functional Requirements

Security requirements do not replace functional requirements — they constrain them. For each functional requirement, ask: what is the confidentiality, integrity, availability, and access-control implication? A login feature implies authentication requirements; a data storage feature implies confidentiality and integrity requirements.

## Related

- [[requirements-engineering]] — general RE lifecycle; security requirements fit into the Specifying and Validating phases
- [[owasp-top-10]] — OWASP Top 10 maps directly onto what CIA-AAA requirements must prevent
- [[vulnerability-tracking-frameworks]] — BSIMM and OpenSAMM measure how well security requirements are adopted
- [[securityrat]] — tool that automates ASVS requirement selection
- [[ICT2216-secure-software-development]] — source course
