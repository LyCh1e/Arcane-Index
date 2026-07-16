---
type: source
address: c-000112
title: "ICT2216 Lecture 9 — Static Code Analysis (Part 1)"
source_type: lecture-notes
course: ICT2216
domain: secure-software-development
created: 2026-07-16
updated: 2026-07-16
tags: [source, ICT2216, SAST, static-analysis, secure-software-development, penetration-testing]
related:
  - concepts/static-code-analysis
  - concepts/security-testing-and-verification
  - examples/ict2216-lab8-static-code-analysis
  - examples/ict2216-lab9-sonarqube
---

# ICT2216 Lecture 9 — Static Code Analysis (Part 1)

**Course:** ICT2216 Secure Software Development  
**Topic:** Static Code Analysis — theory, techniques, tools, and integration with software assurance  
**File:** `raw/ICT2216 Lecture 9 Secure Software Development.md`

---

## Case Studies

### Indirect Prompt Injection in GPT-4o / GPT-5

Tenable researchers found 7 vulnerabilities in OpenAI's GPT-4o and GPT-5. The attack vector: **indirect prompt injection** — malicious instructions embedded in content processed by the LLM (documents, webpages, tool results) that redirect the model's behaviour. Claude-family "Fable-5" was observed using layered defences: at least 3 classifiers (input, output mid-generation, conversation history). Implication: AI-integrated systems must treat all external content as untrusted.

### AI-Assisted Cyberattack — Bandai Channel (July 2025)

A 15-year-old student in Japan used a ChatGPT-generated programme to cancel 46,812 subscriber accounts on Bandai Channel (4 Nov 2024). LLMs significantly lower the barrier to entry for cyberattacks — functional exploit code is now accessible to non-technical actors.

### Phone Number Encryption

MongoDB database showing PII phone numbers in plaintext. Under PDPA, phone numbers are PII. Risk-based decision: for financial applications with MFA over SMS, encrypt at rest. Operational tradeoff: encrypted fields cannot be searched without decryption or deterministic/format-preserving encryption.

### Genshin Impact — Missing Account Security Controls

miHoYo implemented only CAPTCHA. Missing: rate limiting, IP locking, per-account lockout, 2FA, password complexity enforcement, login anomaly notifications, country/IP detection. Result: accounts vulnerable to brute-force and credential stuffing despite being an entertainment product with real monetary value.

---

## Content Summary

| Topic | Covered |
|---|---|
| LLM random number generation security | ✓ (never use LLM for CSPRNG) |
| Testing vs. static analysis comparison | ✓ |
| Types of security testing | ✓ (dependency, client-side) |
| QA evolution at Microsoft (SDV) | ✓ |
| Code inspection / security audit | ✓ (third-party review, Gerrit workflow) |
| OWASP Testing Framework phases (1–5) | ✓ |
| Penetration testing methodologies | ✓ (ISSAF, OSSTMM, PTES, NIST 800-115, PTF) |
| Static analysis definition and pipeline | ✓ (AST → CFG → Call Graph) |
| 6 static analysis techniques | ✓ (pattern matching, data flow, control flow, abstract interpretation, model checking, theorem proving) |
| False positives and negatives | ✓ |
| Criteria for a successful tool | ✓ (5 must-haves) |
| Heap limitation | ✓ |
| Tool comparison | ✓ (Coverity, Fortify, Checkmarx, Veracode, Bandit, Semgrep, SonarQube) |

---

## Key Concepts Extracted

- [[concepts/static-code-analysis]] — deep concept page: pipeline, 6 techniques, false +/-, heap limitation, tool catalogue
- [[concepts/security-testing-and-verification]] — updated: penetration testing methodologies + code inspection section

---

## Key Takeaways

1. LLMs produce statistically predictable output — never use for cryptographic randomness; always use a CSPRNG (`secrets` in Python, `SecureRandom` in Java, `/dev/urandom`)
2. Static analysis examines **all paths simultaneously** without executing the program — covers paths that tests never exercise
3. The spectrum: Type Checking (simple) → Static Analysis tools → Program Verification (formal proof)
4. The 6 techniques increase in power and cost: pattern matching → data flow → control flow → abstract interpretation → model checking → theorem proving
5. False positives drive "alert fatigue"; false negatives are invisible but more dangerous
6. The heap is the primary limitation — most tools cannot model dynamic heap state precisely
7. OSSTMM is best used as a supporting reference for ISO 27001, not a hands-on pen testing guide

---

## External References

| Resource | URL |
|---|---|
| Trail of Bits — Auditing Source Code | https://trailofbits.github.io/ctf/vulnerabilities/source.html |
| ISSAF v0.2.1 | https://untrustednetwork.net/files/issaf0.2.1.pdf |
| OSSTMM v3 | https://www.isecom.org/OSSTMM.3.pdf |
| Top 10 Static Code Analysis Tools | https://www.devopsschool.com/blog/top-10-static-code-analysis-tool/ |
