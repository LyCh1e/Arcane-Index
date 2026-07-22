---
type: source
address: c-000122
title: "ICT2216 Lecture 9 — Spoken Transcript (Static Code Analysis)"
source_type: lecture-transcript
course: ICT2216
domain: secure-software-development
created: 2026-07-22
updated: 2026-07-22
tags: [source, transcript, ICT2216, SAST, static-analysis, code-auditing, microsoft-sdl, git-branching]
related:
  - sources/ICT2216-lecture-9-static-code-analysis
  - concepts/static-code-analysis
  - concepts/security-testing-and-verification
  - concepts/software-configuration-management
---

# ICT2216 Lecture 9 — Spoken Transcript (Static Code Analysis)

**Course:** ICT2216 Secure Software Development  
**Lecturer:** Raymond Chan  
**Format:** Verbatim Zoom lecture transcript  
**Companion notes source:** [[sources/ICT2216-lecture-9-static-code-analysis]] (c-000112)

The companion source page (c-000112, from formatted lecture notes) covers all case studies, the full static analysis pipeline, 6 techniques, tool catalogue, and pen testing methodologies. This transcript source captures the **narrative and pedagogical context** not present in the slides.

---

## Net-New Content (vs Lecture Notes)

### 1. Microsoft SDL Historical Progression

Raymond's live account of how Microsoft evolved its QA and static analysis practices:

| Era | Approach | Problem |
|-----|----------|---------|
| **1990s** | Manual code inspection via CVS (pre-Git) | Team: Author → Code Reviewer → Verifier → Approver → Committer. Works for small codebases; breaks down as system grows |
| **Early 1990s** | Massive unit testing across configurations and platforms | Tests took **weeks to run**; Blue Screen of Death still occurred |
| **2000s** | Static analysis enters — **Static Driver Verification (SDV) framework** | Motivated by third-party device drivers (printer, USB, display) being the primary source of BSOD crashes |

**Key insight:** Microsoft couldn't control third-party driver quality, so they provided a static analysis framework that scanned driver code for errors (e.g., interrupt enable/disable correctness) before distribution. This is the origin of modern SAST in the Windows ecosystem.

→ Added to [[concepts/static-code-analysis]] — "Historical Context" section

---

### 2. What Static Analysis Cannot Detect — Design Errors

Lecturer's live example of a design error invisible to static tools:

> *"If you add the salt AFTER the password is already hashed, static analysis will never tell you that is wrong."*

A developer who hashes the password first, then appends the salt to the digest (rather than salting first, then hashing), has implemented the cryptographic logic in the wrong order. The code is syntactically correct and logically consistent — no tool can infer that the **intended** security property (uniqueness of the hash per user) is violated. This is a semantic, domain-specific design error.

This class of errors — design intent errors — is why **human code review cannot be replaced by automated tooling** for high-assurance systems.

→ Added to [[concepts/static-code-analysis]] — "Limitations" section

---

### 3. LLM vs Classical Static Analysis — Determinism Advantage

> *"Every time you use the same tool on the same source code, it will come up with the same result. Unlike LLM, which may come up with a different result each time."*

Classical static analysis tools are **deterministic** — same input always produces the same finding set. This is essential for:
- **Reproducibility** of security reports
- **Compliance** and formal verification pipelines
- **Tracking** whether a previously flagged issue was fixed (fixed if the finding disappears next run)

LLMs can supplement static analysis (e.g., explaining a finding, suggesting a fix) but cannot replace it in any context where reproducibility is required.

---

### 4. Code Auditing — Professional Pricing and Scope

Raymond's account of a real secure code auditing engagement:

> *"I took almost two months to review their source code — they had encryption implementations and personal data handling."*

**Pricing models used in practice:**

| Model | Basis | Typical context |
|-------|-------|----------------|
| Per line of code | Total LoC reviewed × rate | Large, well-scoped codebases |
| Per man-day | Days of engineer time × daily rate | Complex systems with custom encryption or bespoke logic |

**Indicative range:** SGD 50,000 – 100,000+ for banking or healthcare applications (100K+ LoC, multiple class files, encryption implementations, PII handling).

**What auditors are responsible for:** Saying the code is secure — auditors bear accountability for findings they miss. This is why human judgment cannot be outsourced to AI alone.

→ Added to [[concepts/security-testing-and-verification]] — "Code Inspection / Security Audit" section

---

### 5. Phone Number Encryption — PCI DSS Exception

Discussion point raised during review of student project submissions:

- Phone numbers are **PII under PDPA** — implies encryption obligation
- But phone numbers, **unlike passwords**, cannot simply be hashed — they must be retrieved to send OTPs or notifications
- **PCI DSS** provides a partial exception for phone number storage because a phone number alone is not uniquely identifiable to an individual without additional context
- Options available:
  - **Public-key infrastructure** — encrypt at rest with asymmetric key; decrypt only at send-time
  - **Table segregation** — store phone numbers in a separate, access-controlled table; reduce exposure surface
  - **Format-preserving encryption** — allows search operations on encrypted values

This remains a **grey area** — the right choice depends on the threat model, data classification, and regulatory jurisdiction.

---

### 6. Production Git Branching Model — 7 Branches

Described as Raymond's recommended model for production applications:

```
live (production)
  ↑
hotfix ──────────────────────────────────────┐
  ↑                                          │
UAT ◄──── bug-fix ◄── (issues found in UAT) │
  ↑                                          │
development ◄── feature/[developer-name] ───┘
```

| Branch | Purpose |
|--------|---------|
| `live` | Running production code; only hotfix and UAT merges in |
| `hotfix` | Urgent fixes to production; merged to live IMMEDIATELY then back to UAT/dev |
| `UAT` | User acceptance testing; reflects latest development ready for testing |
| `bug-fix` | All issues found in UAT; merged back to UAT and development |
| `development` | Main integration branch; always contains latest code (without full testing) |
| `feature` or `[developer-name]` | Individual work in progress; pulled from and pushed to development |

**Full cycle:**  
`feature` (develop) → push to `development` → push to `UAT` → (bugs found) → `bug-fix` → back to `UAT` → test passes → push to `live` → (production bug found) → `hotfix` → push to `live` immediately → back to `UAT` and `development`

**Key discipline:** `live` always reflects the production state. Hotfix bypasses UAT for speed but is immediately back-tested through UAT to ensure the fix doesn't introduce regressions.

→ Added to [[concepts/software-configuration-management]] — "Production Branching Model" section

---

## Key Quotes

> *"Human has to always be in the loop. If you need to find someone to be responsible, you always point to human, not the AI agent."*

> *"Statistical analysis is still very useful to detect classic security vulnerabilities — buffer overflow, unvalidated input, memory errors, race conditions, hardcoded API keys."*

> *"If there are too many false positives, the time needed to verify them will be huge. Acceptable level of false negatives is even more important."*

> *"The heap is still a challenge — most static analysis tools disregard the heap completely because it is a source of both false positives and false negatives."*

---

## Case Studies (Already in c-000112)

All four case studies mentioned in the transcript (Indirect Prompt Injection, Bandai Channel, Phone Number, Genshin Impact) are already documented in [[sources/ICT2216-lecture-9-static-code-analysis]] (c-000112). Not duplicated here.
