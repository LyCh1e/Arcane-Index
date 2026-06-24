---
type: index
status: established
title: "Gaps Index"
updated: 2026-05-14
tags: [index, gaps]
---

# Gaps

Open questions, contradictions between sources, and topics where knowledge is missing or shallow. Detected by lint run on 2026-05-14.

---

## Summary

| Category | Count | Priority |
|----------|-------|----------|
| Stale index pages | 2 | High |
| Link style inconsistencies | ~20 pages | Medium |
| Missing synthesis pages | 0 | Resolved 2026-05-14 |
| Orphaned concept clusters | 3 clusters | Low |
| Empty learning/ folder | — | Medium |
| Missing areas/ pages | 8 domains | Low |

---

## 1. Stale Index Pages

### `wiki/sources/_index.md` — Missing 7 sources

Last updated 2026-05-11. Only lists 8 of 15 ingested sources. Missing:

| Missing Source | Ingested |
|----------------|---------|
| ICT2216 Secure Software Development | 2026-05-11 |
| ICT2112 Software Design | 2026-05-12 |
| INF2003 Database Systems | 2026-05-12 |
| ICT1011 Computer Organisation and Architecture | 2026-05-13 |
| ICT1012 Operating Systems | 2026-05-13 |
| INF1005 Web Systems & Technologies | 2026-05-14 |

**Fix**: rebuild `sources/_index.md` to include all 15 sources.

### `wiki/concepts/_index.md` — Shows placeholder despite 52 concept pages

Still shows "empty — ingest a source to populate". Needs a full domain-grouped listing.

---

## 2. Link Style Inconsistencies

Several earlier-ingested concept pages use short wikilinks (`[[page-name]]`) rather than the vault's established full-path style (`[[concepts/page-name|Display Label]]`). These work in Obsidian (filenames are unique) but are inconsistent.

**Affected pages** (uses short-form links internally):
- `wiki/concepts/ml-foundations.md` — all See Also links
- `wiki/concepts/algorithm-complexity.md` — all See Also links
- `wiki/concepts/hci-fundamentals.md` — all See Also links and source links
- `wiki/concepts/android-architecture.md` — all See Also links
- `wiki/concepts/software-design-process.md` — internal inline links and See Also

**Fix**: normalise to `[[concepts/xxx|Display Name]]` format during next lint pass.

---

## 4. Missing Synthesis Pages

The following cross-domain connections are noted in concept pages but no synthesis page exists to document the connection explicitly.

### 4a. Mathematics → Machine Learning bridge ✓ RESOLVED

**Domains**: mathematics × machine-learning
**Page created**: [[synthesis/maths-to-ml-bridge|Mathematics Foundations → Machine Learning: The Hidden Curriculum]]
**Resolved**: 2026-05-14

### 4b. Web Security × Secure Software Development ✓ RESOLVED

**Domains**: web-development × secure-software-development
**Page created**: [[synthesis/web-security-ssdlc-bridge|Attack Patterns at Code Level ↔ SSDLC Process]]
**Resolved**: 2026-05-14

### 4c. ICT1011 → ICT1012 Architecture Bridge ✓ RESOLVED

**Domains**: computer-architecture × operating-systems
**Page created**: [[synthesis/ict1011-ict1012-architecture-bridge|Hardware Paging → OS Virtual Memory: The ICT1011 → ICT1012 Handover]]
**Resolved**: 2026-05-14

### 4d. REST API cross-stack synthesis ✓ RESOLVED

**Domains**: web-development × mobile-development
**Page created**: [[synthesis/rest-api-cross-stack|REST API: Server Design (INF1005) ↔ Android Client (INF2007)]]
**Resolved**: 2026-05-14

---

## 5. Orphaned Concept Clusters

These clusters have no inbound links from outside their own domain. They are self-contained but not connected to the rest of the vault graph. They are not broken — they are simply isolated.

### Mathematics cluster (10 pages)
`discrete-mathematics-foundations`, `combinatorics`, `propositional-logic`, `predicate-logic-and-proofs`, `sets-functions-relations`, `descriptive-statistics`, `probability-theory`, `probability-distributions`, `linear-algebra-matrices`, `eigenvalues-and-svd`

**Connections that could be made**: probability distributions → ML model evaluation; linear algebra → neural networks/PCA; propositional logic → predicate logic → formal methods (if ingested).

### Machine Learning cluster (6 pages)
`ml-foundations`, `ml-data-understanding`, `ml-model-training-evaluation`, `decision-trees-and-ensembles`, `neural-networks-linear-models`, `clustering-and-dimensionality-reduction`

**Connections that could be made**: ml-foundations → algorithm-complexity (computational cost of training); ml-model-training-evaluation → probability-distributions (statistical foundations); neural-networks → linear-algebra-matrices (matrix multiplication in forward pass).

### Software Engineering cluster — partial isolation
`lightweight-rcm`, `sorting-and-searching`, `graph-algorithms` — not linked from other concept pages in their own domain (e.g., `lightweight-rcm` is not linked from `requirements-engineering`; `sorting-and-searching` is not linked from `data-structures-fundamentals`).

---

## 6. Empty `learning/` Folder

Only one page exists: `wiki/learning/docker-windows-crlf.md` (a resolved bug/lesson).

No study notes or flashcard-style summaries exist for any of the 15 ingested modules. The vault's stated purpose includes exam preparation. All 15 modules are exam-relevant.

**Highest priority** (based on module complexity and exam weight):
1. ICT1012 Operating Systems — 5 concept pages, high density
2. INF2003 Database Systems — 6 concept pages, heavy SQL/normalisation
3. INF1008 Data Structures & Algorithms — 4 concept pages, algorithm-heavy
4. INF2008 Machine Learning — 6 concept pages, mathematical foundations

---

## 7. Missing `areas/` Pages

The vault structure defines `areas/` for topic domain overviews, but no pages exist there. Eight domains are represented:

`operating-systems`, `computer-architecture`, `web-development`, `software-engineering`, `database-systems`, `machine-learning`, `mathematics`, `mobile-development`, `hci`, `secure-software-development`

Area pages would provide a single-page "what do I know about this domain?" entry point.

---

## Open Questions

| Question | Domain | Status |
|----------|--------|--------|
| Does the OWASP Top 10 concept page cover XSS/SQLi from the web developer's code-level perspective, or only from the ICT2216 process perspective? | web-security | Resolved — both perspectives documented in [[synthesis/web-security-ssdlc-bridge\|web-security-ssdlc-bridge]] |
| Are there cross-module exam questions that span ICT1011 + ICT1012 (hardware paging → OS virtual memory)? | computer-architecture / OS | Resolved — [[synthesis/ict1011-ict1012-architecture-bridge\|ict1011-ict1012-architecture-bridge]] documents the full handover |
| Which ML algorithms have O(n²) or worse training complexity? | ML / algorithms | `[!gap]` — not documented in either `algorithm-complexity.md` or ML pages |

---

## Contradictions

*(none detected — no sources have been ingested that conflict with existing pages)*

---

## Research Needed

| Topic | Domain | Reason |
|-------|--------|--------|
| Testing (unit/integration/TDD/Selenium/Jest) | web-development / software-engineering | Referenced in INF1005 and ICT2216 but no dedicated concept page |
| Modern frontend frameworks (React/Next.js depth) | web-development | INF1005 Ch. 21 gives only a surface overview |
| Git and version control | devops | Referenced in DevOps section but no concept page |
