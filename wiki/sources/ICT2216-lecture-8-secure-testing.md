---
type: source
address: c-000100
title: "ICT2216 Lecture 8 — Secure Software Implementation (Part 3): Test Automation & Security Testing References"
course: ICT2216
domain: secure-software-development
ingested: 2026-07-09
raw: "raw/ICT2216 Lecture 8 Secure Software Development.md"
tags: [source, ICT2216, security-testing, ASVS, WSTG, test-automation, authentication-testing]
---

# ICT2216 Lecture 8 — Secure Software Implementation (Part 3)

Test Automation & Security Testing References

---

## Summary

Lecture 8 introduces the formal frameworks for **verifying** security controls — the complement to Lecture 7's focus on implementing them. The primary frameworks are the OWASP ASVS (what to verify) and OWASP WSTG (how to test it). The lecture then demonstrates specific authentication testing procedures and concludes with guidance on security test reporting.

---

## Case Studies Covered

| Case Study | Key Lesson |
|---|---|
| Singpass Passkey Rollout (1 July 2025) | Passkeys eliminate interception risk — no password or OTP is transmitted; FIDO2/WebAuthn private key stays on device |
| 282 iOS AI Apps Leaking API Keys | Three categories of insecure credential handling: plaintext keys (54), open relay servers (92), replayable tokens (136) |
| OAuth Flaws in Grammarly, Vidio, Bukalapak | Failed to validate `redirect_uri`/`client_id` binding — a code issued for one site was accepted by another (cross-site token theft) |
| Twitter Code Review by Printing | Illustrates why manual review at scale is unworkable; structured peer review + automated SAST in CI/CD is the correct approach |

---

## Concept Pages Generated

| Page | Coverage |
|------|---------|
| [[concepts/security-testing-and-verification\|Security Testing and Verification]] (c-000101) | Testing pyramid, SDLC integration, ASVS levels and categories, WSTG test cases, authentication testing, security test report structure |
| [[concepts/secure-deployment-practices\|Secure Deployment Practices]] (c-000098) | Extended with logging testing section: what to exclude from logs, log rotation, access control, and anomaly detection |

---

## OWASP Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| OWASP ASVS | https://owasp.org/www-project-application-security-verification-standard/ | Verification requirements catalogue |
| OWASP WSTG | https://owasp.org/www-project-web-security-testing-guide/ | Test case procedures |
| WSTG Reporting | https://owasp.org/www-project-web-security-testing-guide/stable/5-Reporting/README | Report structure guidance |
| NIST SP 800-63 | https://pages.nist.gov/800-63-3/ | Digital identity guidelines aligned with ASVS V2.1 |
| SecLists (common passwords) | https://github.com/danielmiessler/SecLists/tree/master/Passwords | Breached password lists for ASVS 2.1.7 |

---

## Key Takeaways

- The **testing pyramid** dictates resource allocation: unit tests (bulk), integration/API tests (some), UI/end-to-end tests (few)
- **ASVS** translates security requirements into specific, testable verification requirements (14 categories, 3 levels)
- **WSTG** provides the actual test procedures for each ASVS verification requirement
- Password requirements (ASVS V2.1) align with NIST SP 800-63: min 12 chars, no complexity rules, no forced rotation, check against breached lists, allow all Unicode
- Credential storage (ASVS V2.4): bcrypt work factor ≥10 or PBKDF2 iterations ≥100,000; salt ≥32 bits, unique per credential
- Account lockout should trigger at 3–5 failed attempts; time-based automatic unlock; CAPTCHA supplements but does not replace lockout
- Generic error messages are mandatory — never differentiate between "username not found" and "wrong password"
- Security test reports must include executive summary, per-finding severity ratings, proof of concept, and remediation recommendations
