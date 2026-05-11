---
type: source-index
title: "ICT2216 Secure Software Development"
course: ICT2216
institution: SIT
raw: ""
domain: secure-software-development
topics: [security-requirements, confidentiality, integrity, availability, authentication, authorisation, accountability, securityrat, owasp]
ingested: 2026-05-11
---

# ICT2216 — Secure Software Development

Secure Software Development teaches the theory and practice of building security into software from the requirements stage, rather than bolting it on after deployment. The course argues that most security vulnerabilities originate in incomplete or absent security requirements — not in implementation defects alone.

## Course Overview

The module covers the full secure development lifecycle (SDLC), starting from threat-aware requirements elicitation through to secure design, implementation, and verification. Labs use industry tools (SecurityRAT, OWASP checklists) to make requirements engineering concrete and auditable.

## Key Topics

### Secure Software Requirements (Lab 2)

Security requirements are derived from the six pillars: **Confidentiality, Integrity, Availability** (CIA) and **Authentication, Authorisation, Accountability** (AAA). Each pillar produces a structured set of requirements tied to the application's functional and non-functional baseline.

See [[secure-software-requirements]] for the full framework including risk identification and SANS SWAT checklist mapping.

### SecurityRAT

SecurityRAT is an OWASP tool that automates security requirement selection based on the declared artifact type (web app, API, etc.) and compliance level. It maps requirements to OWASP ASVS 3.x identifiers and integrates with issue trackers.

See [[securityrat]] for setup, the CRLF gotcha, and usage notes.

## Labs

| Lab | Topic |
|-----|-------|
| Lab 1 | Docker and Docker Compose — Nginx, MySQL, Git server, Selenium Grid |
| Lab 2 | Defining Secure Software Requirements — CIA + AAA framework, SecurityRAT |

## Concept Pages

| Concept | Description |
|---------|-------------|
| [[docker-compose]] | Docker Compose fundamentals — compose file, networking, volumes, all four services |
| [[secure-software-requirements]] | CIA + AAA pillars, risk identification, SANS SWAT mapping |

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
