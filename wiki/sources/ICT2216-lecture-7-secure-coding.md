---
type: source
address: c-000096
title: "ICT2216 Lecture 7 — Secure Software Implementation (Part 2): References for Secure Coding"
domain: secure-software-development
course: ICT2216
source_type: lecture-notes
raw: "raw/ICT2216 Lecture 7 Secure Software Development.md"
created: 2026-07-02
updated: 2026-07-02
tags: [source, ICT2216, owasp, secure-coding, input-validation, sql-injection, redos, docker, github-secrets, logging, component-security]
---

# ICT2216 Lecture 7 — Secure Software Implementation (Part 2)

Covers the principal OWASP reference resources for secure coding and applies them to practical implementation. Two new concept pages are introduced: [[concepts/secure-input-validation]] and [[concepts/secure-deployment-practices]].

## Coverage

| Part | Topic | Concept Page |
|------|-------|-------------|
| 1 | OWASP Top 10 Proactive Controls (C1–C10) — framework overview | Referenced across both concept pages |
| 2 | Input Validation Cheat Sheet; ReDoS; SQL Injection Prevention Cheat Sheet | [[concepts/secure-input-validation]] |
| 3 | OWASP SKF — code examples, checklists, labs | [[concepts/secure-deployment-practices]] |
| 4 | OWASP Secure Coding Practices — Database and File Management checklists | [[concepts/secure-deployment-practices]] |
| 5 | Secrets management — GitHub Secrets | [[concepts/secure-deployment-practices]] |
| 6 | Docker development workflow and security best practices | [[concepts/secure-deployment-practices]] |

## Key Takeaways

- **OWASP Proactive Controls** (C1–C10) are the *defensive* counterpart to the OWASP Top 10 (which lists *risks*). The controls are grouped: access (C1, C5, C7), cryptography (C2), input/exception (C3), secure development (C4), components (C6), browser (C8), logging (C9), SSRF (C10).
- **ReDoS** is a DoS attack unique to regular expressions — crafted inputs cause catastrophic backtracking in NFA-based engines, hanging web servers, WAFs, and databases. Evil patterns: `(a+)+`, `([a-zA-Z]+)*`, `(a|aa)+`. Mitigation: use RE2 (linear-time), set timeouts, avoid nested quantifiers.
- **Allow-list beats block-list** always — block lists are trivially bypassed by encoding, case changes, or alternate representations; allow lists reject everything not explicitly permitted.
- **Parameterised queries** (prepared statements) are the gold standard for SQL injection prevention. Escaping is a last resort. Least privilege on the DB account is a mandatory secondary defence.
- **Never hardcode secrets** in Dockerfiles, `docker-compose.yml`, or any committed file. Inject via GitHub Secrets → environment variables at runtime.
- **Security logging rules**: never log sensitive data (passwords, PII, session tokens); encode before logging (log injection); centralise and protect log integrity; set appropriate log level (never TRACE in production — see OpenAI Codex SSD wear case study).

## Case Studies in This Lecture

| Case | Secure Coding Lesson |
|------|---------------------|
| OpenAI Codex — 37 TB/21 days SSD writes | Default TRACE logging in production is both a security risk (sensitive data) and an operational risk (SSD exhaustion) |
| Examena face verification bypass | Verification must fail closed — missing baseline should deny, not pass |
| CISA: 52% of critical OSS uses memory-unsafe code | Prefer memory-safe languages; keep C/C++ components patched |
| Leap seconds — `23:59:60` | Input validation must account for real-world edge cases, not just attack patterns |
| LastPass breach — developer endpoint | MFA protects the authentication event, not an already-authenticated session on a compromised machine |
| DeepSeek iOS — 3DES, hardcoded keys, PII in cleartext | Textbook violations: weak crypto, hardcoded keys, insecure storage |

## OWASP Resources Introduced

| Resource | URL | Purpose |
|----------|-----|---------|
| Top 10 Proactive Controls | https://owasp.org/www-project-proactive-controls/ | 10 most important defensive controls |
| Cheat Sheet Series | https://cheatsheetseries.owasp.org/ | 78+ topic-specific guidance sheets |
| SKF | https://demo.securityknowledgeframework.org/ | Code examples, checklists, labs |
| Secure Coding Practices Guide | https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/ | Checklist format across 12 areas |
| Dependency-Check | https://owasp.org/www-project-dependency-check/ | SCA — scans dependencies for CVEs |

## Related Concepts

- [[concepts/secure-input-validation]] — input validation, allow-list, ReDoS, SQL injection prevention (new)
- [[concepts/secure-deployment-practices]] — secrets management, Docker, security logging, component security (new)
- [[concepts/owasp-top-10]] — the vulnerability risk list; Proactive Controls are the corresponding defences
- [[concepts/secure-design-implementation]] — upstream design decisions; cryptography and logging design covered there
