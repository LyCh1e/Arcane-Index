---
type: concept
title: "Secure Software Requirements"
domain: secure-software-development
complexity: high
tags: [security, requirements, CIA, AAA, confidentiality, integrity, availability, authentication, authorisation, accountability, owasp, swat]
created: 2026-05-11
---

# Secure Software Requirements

Security requirements are a structured extension of functional and non-functional requirements. They are derived from six pillars grouped into two triads: the **CIA triad** (data-focused) and the **AAA triad** (user-focused). Every pillar follows the same three-step pattern: identify the asset or actor, identify the risk, define the requirement.

## Why Requirements First

Most security vulnerabilities are not implementation bugs — they are missing requirements. A developer cannot implement "store passwords securely" if the requirement was never stated. Security requirements make implicit expectations explicit and auditable before a single line of code is written.

---

## CIA Triad (Data-Focused)

### Confidentiality

Prevents unauthorised disclosure of data.

1. **Define** — what data must be protected? (PII, credentials, session tokens, financial records)
2. **Identify risks** — who could access it without authorisation? (insecure storage, transmission without TLS, excessive logging)
3. **Define requirements** — encrypt data at rest and in transit; apply least-privilege access; mask sensitive fields in logs

### Integrity

Ensures data is accurate and has not been tampered with.

1. **Identify** — which data must remain unmodified? (user records, transaction logs, configuration)
2. **Identify risks** — SQL injection, CSRF, insecure direct object references, log tampering
3. **Define requirements** — parameterised queries; CSRF tokens; input validation; immutable audit logs

### Availability

Ensures the system is accessible to authorised users when needed.

1. **Discuss** — what uptime and resilience levels are required?
2. **Identify risks** — DoS/DDoS, single points of failure, resource exhaustion, unplanned downtime
3. **Define requirements** — rate limiting; redundant infrastructure; graceful degradation; tested backup/restore

---

## AAA Triad (User-Focused)

### Authentication

Verifies that a user is who they claim to be.

1. **Define users** — who interacts with the system? (public users, registered users, admins, service accounts)
2. **Identify risks** — credential stuffing, brute force, session fixation, phishing
3. **Define requirements** — strong password policy; MFA for privileged accounts; secure session management; account lockout

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

- **SANS SWAT Checklist** — `https://www.sans.org/cloud-security/swat/` — practical web application security requirements grouped by category
- **OWASP ASVS** — Application Security Verification Standard — tiered requirements (Level 1 Opportunistic → Level 3 Advanced); used by SecurityRAT for automated requirement generation
- **SecurityRAT** — see [[securityrat]] — declare your artifact type, generate the applicable ASVS requirements automatically

---

## Relationship to Functional Requirements

Security requirements do not replace functional requirements — they constrain them. For each functional requirement, ask: what is the confidentiality, integrity, availability, and access-control implication? A login feature implies authentication requirements; a data storage feature implies confidentiality and integrity requirements.

## Related

- [[requirements-engineering]] — general RE lifecycle; security requirements fit into the Specifying and Validating phases
- [[securityrat]] — tool that automates ASVS requirement selection
- [[ICT2216-secure-software-development]] — source course
