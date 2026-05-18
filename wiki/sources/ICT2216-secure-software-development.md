---
type: source-index
title: "ICT2216 Secure Software Development"
course: ICT2216
institution: SIT
raw: ""
domain: secure-software-development
topics: [security-requirements, confidentiality, integrity, availability, authentication, authorisation, accountability, securityrat, owasp, BSIMM, OpenSAMM, CVE, NVD, MITRE-ATTCK, security-by-design, least-privilege, defence-in-depth, fail-secure, attack-surface, security-architecture]
ingested: 2026-05-11
---

# ICT2216 — Secure Software Development

Secure Software Development teaches the theory and practice of building security into software from the requirements stage, rather than bolting it on after deployment. The course argues that most security vulnerabilities originate in incomplete or absent security requirements — not in implementation defects alone.

## Course Overview

The module covers the full secure development lifecycle (SDLC), starting from threat-aware requirements elicitation through to secure design, implementation, and verification. Labs use industry tools (SecurityRAT, OWASP checklists) to make requirements engineering concrete and auditable.

## Key Topics

### Secure Software Concepts (Lectures 1 & 2)

Security must be addressed at the application layer — network-level controls (firewalls, IDS) alone are insufficient. Real-world case studies (7Pay, SolarWinds, Bybit, Log4Shell) illustrate how security failures occur across the SDLC.

See [[owasp-top-10]] for all 10 OWASP 2025 categories with scenarios and code examples.

See [[vulnerability-tracking-frameworks]] for CVE, NVD, CAPEC, MITRE ATT&CK, CVSS, BSIMM, OpenSAMM, and Microsoft SDL.

### Secure Software Requirements (Lectures 2–3 & Labs)

Security requirements are derived from the six pillars: **Confidentiality, Integrity, Availability** (CIA) and **Authentication, Authorisation, Accountability** (AAA). Each pillar produces a structured set of requirements tied to the application's functional and non-functional baseline.

Lecture 3 extends this with: General Application Security Requirements (session, error, configuration, and code management); Operational Requirements (deployment environment, archiving, anti-piracy); Other Requirements (TOC/TOU race conditions, procurement, GDPR); and adversarial artefacts — anti-requirements and abuse/misuse case modelling.

See [[secure-software-requirements]] for the full framework including risk identification, SANS SWAT checklist mapping, anti-requirements, and misuse case modelling.

### Threat Modeling (Lecture 3)

Requirements tell you *what* to protect; threat modeling tells you *how* attackers will actually break your system. Covers: threat agents (8 human types + non-human), identifying threats via trust boundaries / DFDs / entry-exit points / mis-actors, the 5-step threat modeling process, attack trees, and Microsoft STRIDE.

See [[threat-modeling]] for the full framework including STRIDE applied to DFD elements and STRIDE–OWASP mapping.

### Secure Software Design (Lecture 4)

Lecture 4 addresses the *design* phase of the SSDLC, arguing that **50% of security problems are design flaws** (not implementation bugs — McGraw, 2006). Even perfect code cannot fix a flawed design; security thinking must be embedded before a single line of code is written. The Banana Token hack (September 2023, $8.70 → $0.02 in under 3 hours) illustrates the catastrophic consequences of design-level vulnerabilities in the real world.

The lecture covers the ten **OWASP Security by Design Principles** — Minimise Attack Surface Area, Establish Secure Defaults, Least Privilege, Defence in Depth, Fail Securely, Don't Trust Services, Separation of Duties, Avoid Security by Obscurity, Keep Security Simple, and Fix Security Issues Correctly — and introduces **Security Architecture** (physical vs. logical views).

See [[security-by-design-principles]] for the full framework with worked examples and code snippets for each principle.

### SecurityRAT

SecurityRAT is an OWASP tool that automates security requirement selection based on the declared artifact type (web app, API, etc.) and compliance level. It maps requirements to OWASP ASVS 3.x identifiers and integrates with issue trackers.

See [[securityrat]] for setup, the CRLF gotcha, and usage notes.

## Labs

| Lab | Topic |
|-----|-------|
| Lab 1 | Docker and Docker Compose — Nginx, MySQL, Git server, Selenium Grid |
| Lab 2 | Defining Secure Software Requirements — CIA + AAA framework, SecurityRAT |
| Lab 3 | Microsoft Threat Modeling Tool — DFD creation, STRIDE auto-generation, threat triage |

## Concept Pages

| Concept | Description |
|---------|-------------|
| [[docker-compose]] | Docker Compose fundamentals — compose file, networking, volumes, all four services |
| [[secure-software-requirements]] | CIA + AAA pillars, OSA taxonomy, SSDLC requirement process, general/operational/other requirements, anti-requirements, abuse/misuse case modelling |
| [[threat-modeling]] | Threat agents, trust boundaries, DFDs, mis-actor categories, 5-step process, attack trees, Microsoft STRIDE |
| [[owasp-top-10]] | OWASP Top 10 (2025) — all 10 categories with scenarios, code examples, and mitigations |
| [[vulnerability-tracking-frameworks]] | CVE, NVD, CAPEC, MITRE ATT&CK, CVSS, BSIMM, OpenSAMM, Microsoft SDL |
| [[security-by-design-principles]] | 10 OWASP Security by Design Principles, design flaws vs. bugs, Security Architecture (physical vs. logical) |

## Examples

| Example | Description |
|---------|-------------|
| [[examples/ict2216-lab1-docker-compose]] | Full Lab 1 compose files, step-by-step build, port map |
| [[examples/ict2216-lab2-securityrat]] | Full Lab 2 SecurityRAT setup, CRLF fix, artifact generation walkthrough |

## Resources

| Resource | Description |
|----------|-------------|
| [[securityrat]] | OWASP SecurityRAT — Docker setup, default creds, usage |

## Related Courses

- [[ICT2113-software-modelling]] — Requirements Engineering lifecycle; CIA+AAA extends the SRS with security-specific requirements
- [[INF2002-human-computer-interaction]] — Needfinding and stakeholder analysis feed into security requirement elicitation
