---
type: area
status: established
title: "Secure Software Development"
domain: secure-software-development
source: [[sources/ICT2216-secure-software-development]]
updated: 2026-05-14
tags: [area, secure-software-development]
---

# Secure Software Development

**Source**: ICT2216 — Secure Software Development, SIT.

---

## What I Know

Security is not a feature — it is a quality attribute built in from requirements through deployment. ICT2216 covers the Secure Software Development Lifecycle (SSDLC), OWASP ASVS verification levels, vulnerability tracking, and practical deployment with Docker.

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/secure-software-requirements\|Secure Software Requirements]] | CIA triad, AAA (Authentication/Authorisation/Audit), BCIC analysis, general/operational/other requirements, anti-requirements, misuse case modelling |
| [[concepts/threat-modeling\|Threat Modeling]] | Threat agents (8 human types), trust boundaries, DFDs, mis-actor network categories, attack trees, Microsoft STRIDE |
| [[concepts/owasp-top-10\|OWASP Top 10 (2025)]] | Top 10 web application security risks, ASVS verification levels 1–3, SecurityRAT |
| [[concepts/vulnerability-tracking-frameworks\|Vulnerability Tracking Frameworks]] | CVE/CWE/NVD/CVSS, software assurance frameworks |
| [[concepts/docker-compose\|Docker & Docker Compose]] | Containers, images, Compose multi-service stacks, volume mounts, networking |
| [[concepts/secure-input-validation\|Secure Input Validation]] | Allow-list vs block-list, Unicode normalisation, ReDoS, SQL injection prevention (prepared statements, allow-list, escaping) |
| [[concepts/secure-deployment-practices\|Secure Deployment Practices]] | Component security (OWASP Dependency-Check, SBOM), security logging rules (log injection, PII exclusion, centralisation), GitHub Secrets, Docker security best practices, logging testing considerations |
| [[concepts/security-testing-and-verification\|Security Testing and Verification]] | Testing pyramid, SDLC security integration, OWASP ASVS (14 categories, 3 levels), ASVS V2.1 password rules, V2.4 storage, V2.5 recovery, V10 malicious code, WSTG 11 test categories, authentication testing (lockout, CAPTCHA, account enumeration), security test report structure |
| [[concepts/security-terminology\|Security Terminology]] | Encoding vs escaping vs sanitisation vs serialisation; encryption vs hashing vs digital signatures; authentication vs authorisation; federated identity (IdP, RP/SP, Principal) |
| [[concepts/access-control\|Access Control]] | IAA framework (Identification → Authentication → Authorisation); knowledge/token/biometric factors; password attacks (brute force, dictionary, rainbow tables) and defences (salted hashing, bcrypt); graphical authentication; biometrics (FAR/TAR/ROC, modality comparison, spoofing/bias); DAC, RBAC, MAC models; POLP; Separation of Duties |

---

## Key Ideas

- **SSDLC**: security requirements are elicited early (using BCIC + CIA+AAA), not bolted on at deployment — every SDLC phase has a security counterpart
- **OWASP ASVS levels**: Level 1 = opportunistic (all apps); Level 2 = standard (most apps); Level 3 = advanced (high-value/high-risk apps)
- **CIA+AAA unpacks McCall's Integrity**: Confidentiality (access control) + Integrity (accuracy) + Availability (uptime) + Authentication + Authorisation + Audit
- **Docker isolation principle**: each service runs in its own container; services communicate via defined network interfaces, not shared state
- **Vulnerability scoring (CVSS)**: 0–10 scale; Base score from exploitability (attack vector, complexity, privileges) × impact (confidentiality, integrity, availability)

---

## Cross-Domain Connections

- [[synthesis/web-security-ssdlc-bridge|Web Security ↔ SSDLC]] — INF1005's code-level attack defences map to ICT2216's ASVS requirements and SSDLC process
- [[synthesis/re-elicitation-cia-aaa-security-requirements|RE × Security]] — McCall Integrity ↔ CIA+AAA; RE lifecycle ↔ SSDLC requirements phase
- [[concepts/web-security-and-devops|Web Security & DevOps]] — INF1005's practical security perspective (XSS, SQLi, bcrypt)

---

## Study Notes

*(none yet — ICT2216 study-notes page not yet created)*
