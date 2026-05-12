---
type: synthesis
title: "Security Requirements Are RE: McCall's Integrity ↔ CIA-AAA"
domains: [software-engineering, secure-software-development]
courses: [ICT2113, ICT2216]
maturity: established
tags: [requirements-engineering, security, CIA, AAA, mccall, integrity, elicitation, srs, bcic, synthesis]
updated: 2026-05-12
---

# Security Requirements Are RE: McCall's Integrity ↔ CIA-AAA

ICT2113 teaches Requirements Engineering as a general-purpose discipline. ICT2216 teaches Secure Software Development beginning with security requirements. These two bodies of knowledge are not separate subjects — **security requirements are a specialised application of RE**, and every RE concept has a direct security counterpart.

The key insight is the bridge through **McCall's Integrity feature**: the one quality feature in McCall's model that maps cleanly onto the entire CIA+AAA framework.

---

## The Bridge: McCall's Integrity → CIA-AAA

McCall's Software Quality Model (1977) lists eleven quality features across three perspectives. One feature stands out for security:

| McCall Feature | Perspective | Definition |
|----------------|------------|------------|
| **Integrity** | Product Operation | Does the system resist unauthorised access? |

This single feature is deliberately broad. ICT2216 unpacks it into six concrete pillars:

```
McCall's Integrity
        │
        ├── CIA Triad (data-focused)
        │       ├── Confidentiality  — unauthorised read
        │       ├── Integrity        — unauthorised write/modify
        │       └── Availability     — unauthorised denial of service
        │
        └── AAA Triad (user-focused)
                ├── Authentication   — verify who the user is
                ├── Authorisation    — control what they may do
                └── Accountability   — trace what they did
```

McCall's model names the quality goal; CIA+AAA operationalises it. When an SRS requirement is labelled as satisfying **Integrity (McCall)**, it should be traceable to one or more of the six CIA-AAA pillars.

---

## The Same Three-Step Pattern

Both RE and secure-requirements derivation follow the same underlying process, just with different vocabulary:

| RE Step (ICT2113) | Security Step (ICT2216) | What Happens |
|-------------------|------------------------|--------------|
| **Eliciting** — extract needs from stakeholders | **Feasibility Study** — identify stakeholders, assets, threats, attacker model | Discover *what must be protected* and *from whom* |
| **Analysing** (BCIC) — decompose, clarify, interpret, categorise | **CIA-AAA derivation** — identify asset → identify risk → define requirement | Resolve ambiguity; produce atomic, verifiable statements |
| **Specifying** — write formal SRS | **Secure Requirement Specification** — document in SRS referencing ASVS/SWAT checklists | Produce an auditable, traceable record |
| **Validating** — check against stakeholder needs | **Secure Requirement Validation** — review against attacker models and misuse cases | Confirm completeness before design begins |
| **Managing** (iRTM) — track changes and trace to design/test | **iRTM extended with threat model** — trace each security requirement to its threat and its mitigating control | Ensure no threat is unaddressed |

The structures are isomorphic. A security analyst performing CIA-AAA derivation is executing the RE lifecycle with a threat-model lens.

---

## BCIC Applied to Security Requirements

The **BCIC framework** (Breakdown → Clarify → Interpret → Categorise) resolves ambiguous requirements. Security requirements are particularly prone to the ambiguity that BCIC targets:

| BCIC Step | Security Example: "The system shall be secure" |
|-----------|------------------------------------------------|
| **Breakdown** | Decompose: passwords must be hashed; data in transit must be encrypted; admin actions must be logged |
| **Clarify** | Remove vague terms: "encrypted" → "AES-256 at rest, TLS 1.3 in transit"; "hashed" → "bcrypt with cost factor ≥ 12" |
| **Interpret** | Surface hidden requirements: "passwords hashed" implies a password-recovery flow must not expose the original password |
| **Categorise** | Functional Security Requirement (the hashing behaviour) + Non-Functional Security Requirement (performance of the hashing function under load) |

Without BCIC, "the system shall be secure" enters the SRS unchallenged — unambiguous on the surface, meaningless to a developer.

---

## OSA Taxonomy Maps to RE Requirement Types

The Open Security Architecture classifies security requirements into four types. These map onto the standard RE functional/non-functional split:

| OSA Type | RE Type | Description |
|----------|---------|-------------|
| **Secure Functional Requirements** | Functional (constrained) | What the system shall *not* do; derived from misuse/abuse cases |
| **Functional Security Requirements** | Functional | Security *services* the system must provide (auth, audit logs, backup) |
| **Non-Functional Security Requirements** | Non-Functional | Architectural properties: robustness, performance under attack |
| **Secure Development Requirements** | Process constraint | Activities during development (coding guidelines, threat modelling) |

RE categorises requirements as functional or non-functional. ICT2216 refines this: for security, functional requirements split further into *what the system does* and *what the system must prevent* — the second class (misuse/abuse cases) is invisible in standard RE but essential in security.

---

## iRTM Extended for Security

The standard iRTM traces: `Source → Requirement ID → Design artefact → Test case`.

A security-extended iRTM adds two columns:

| Source | Req ID | Threat (CIA-AAA) | Design artefact | Test case |
|--------|--------|-----------------|-----------------|-----------|
| PDPA regulation | SEC-01 | Confidentiality | EncryptionService | TC-SEC-01 |
| Attacker model (brute force) | SEC-02 | Authentication | LoginController (lockout) | TC-SEC-02 |
| Audit policy | SEC-03 | Accountability | AuditLogRepository | TC-SEC-03 |

The **Threat** column links each requirement back to the risk that motivated it. This makes impact analysis concrete: if the attacker model changes, the iRTM shows exactly which requirements need review.

---

## McCall's Other Features and Security

McCall's Integrity is the obvious bridge, but security concerns touch other features too:

| McCall Feature | Security Dimension |
|----------------|--------------------|
| **Integrity** | CIA + AAA — the primary mapping |
| **Reliability** | Availability — the system must not fail under attack (DoS resilience) |
| **Correctness** | Integrity — the system must not produce incorrect output due to injection |
| **Maintainability** | Secure Development Requirements — code must be maintainable so vulnerabilities can be patched quickly |
| **Testability** | Every CIA-AAA requirement must be verifiable (Mag7: Verifiable) |

McCall's model was not designed with cybersecurity in mind (1977). CIA-AAA is a more precise modern decomposition of what *Integrity* in McCall's sense actually requires in practice.

---

## The Mag7 Applied to Security Requirements

The **Mag7 quality attributes** for requirements apply directly to security requirements. They are especially hard to satisfy in the security domain:

| Mag7 Attribute | Challenge in Security Requirements |
|----------------|-----------------------------------|
| **Correct** | Threat models change; a correct requirement today may be incomplete tomorrow |
| **Unambiguous** | "Secure" and "encrypted" are the most commonly ambiguous terms in SRS documents |
| **Complete** | Misuse cases are systematically harder to enumerate than use cases |
| **Consistent** | Availability requirements (high uptime) can conflict with Confidentiality requirements (aggressive session expiry) |
| **Ranked** | Security requirements often lack prioritisation; all are treated as equally critical |
| **Verifiable** | "The system shall resist SQL injection" must become a specific parameterised-query requirement with a defined test |
| **Traceable** | Each security requirement must trace back to a specific threat in the attacker model |

---

## Common Pitfall: Security as an Afterthought

The RE lifecycle places **Specifying** after **Eliciting** and **Analysing**. A common failure pattern is treating security as a constraint to bolt on at the Specifying stage, rather than as a source of requirements to elicit:

```
Wrong:  Elicit functional requirements → Specify → Add "must be secure" as constraint
Correct: Elicit functional requirements + threat model → Analyse with CIA-AAA lens → Specify with security requirements integrated
```

The ICT2216 principle that "most vulnerabilities are missing requirements, not implementation bugs" is a restatement of the RE principle that ambiguous or incomplete elicitation is the root cause of system failure.

---

## Summary

```
ICT2113 RE                           ICT2216 Security
─────────────────────────────────────────────────────────
McCall Integrity           ←→        CIA + AAA (6 pillars)
RE Lifecycle (5 activities)←→        SSDLC requirement phases
BCIC Framework             ←→        Identify asset → risk → requirement
OSA: Functional vs Non-Func←→        RE: Functional vs Non-Functional
Mag7 quality attributes    ←→        Quality of security requirements
iRTM                       ←→        iRTM + Threat column
Misuse cases               ←→        Abuse/attack scenarios (new in security)
SRS                        ←→        Secure Software Requirement Specification
```

Security requirements engineering is Requirements Engineering with a threat model as the primary elicitation lens. Every concept from ICT2113 applies; ICT2216 adds the CIA-AAA framework as the structured decomposition of what "secure" actually means.

---

## See Also

- [[concepts/requirements-engineering]] — RE lifecycle, BCIC, Mag7, McCall's model, iRTM
- [[concepts/secure-software-requirements]] — CIA+AAA pillars, OSA taxonomy, SSDLC process
- [[concepts/owasp-top-10]] — concrete vulnerabilities that arise when security requirements are missing
- [[concepts/vulnerability-tracking-frameworks]] — BSIMM/OpenSAMM measure how well security requirements are adopted across the SDLC
- [[sources/ICT2113-software-modelling]] — source for RE concepts
- [[sources/ICT2216-secure-software-development]] — source for security requirements
