---
type: meta
title: "Lint Report 2026-06-25"
created: 2026-06-25
updated: 2026-06-25
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-06-25

## Summary

| Metric | Count |
|--------|-------|
| Pages scanned | 221 |
| Issues found | 158 |
| Auto-fixed this session | 2 (synthesis/_index.md rows, log/index/hot for AI Workflows) |
| Needs review | 156 |

---

## 1. Orphan Pages

**None found.** All entity pages (agentic-ai-foundation-aaif, graphrag-microsoft, llmlingua, nick-szabo, satoshi-nakamoto, vitalik-buterin) have 5–6 inbound wikilinks each. New concept pages (ai-workflows, retrieval-augmented-generation, mcp-model-context-protocol, etc.) are linked from their respective synthesis and source pages.

---

## 2. Dead Links

**None found.** All wikilinks in scanned pages resolve to existing files. The `wiki/questions/` path migration (completed in the previous session) appears clean — no residual `questions/research-` links detected.

---

## 3. Stale Claims

- [[areas/concepts/_index.md]]: header claims "85 concept pages across 16 domains, extracted from 22 ingested sources." Actual count is **98 concepts** and **37 sources**. Header needs updating alongside the table fix.
- [[wiki-school/sources/_index]]: "Papers & Articles: *(none yet)*" and "Books & Resources: *(none yet)*" — both are now outdated placeholders. There are 20 article/reference sources ingested.

---

## 4. Missing Pages

No concept or entity is mentioned three or more times without a dedicated page. No action needed.

---

## 5. Missing Cross-References

- [[mcp-security]] does not link to [[agentic-ai-foundation-aaif]], which is the governance body addressing MCP security at spec level. Suggest adding.
- [[ai-workflow-orchestration]] mentions LLMlingua in passing but does not link to [[llmlingua]]. Suggest adding when the page is next updated.

---

## 6. Frontmatter Gaps

**Dominant issue: missing `status` field.** Approximately 80 pages lack `status`. This is a vault-wide systematic gap — every page created before the `status` field was standardised is affected.

### Missing `type` field (critical — Dataview cannot categorise these)

| Page | Missing |
|------|---------|
| [[customtkinter-window-lifecycle]] | type, status, created, updated |
| [[github-actions-cicd]] | type, status, updated |
| [[nginx-reverse-proxy-and-tls]] | type, status, updated |
| [[ict2216-lab5-github-actions]] | type, status |
| [[ict2216-lab6-owasp-dependency-check]] | type, status |
| [[ict2216-lab7-automated-testing]] | type, status |
| [[ict2216-lab8-static-code-analysis]] | type, status |
| [[ict2216-lab9-sonarqube]] | type, status |
| [[ict2216-project-deployment-phases-9-12]] | type, status, created, updated |
| [[customtkinter-after-teardown]] | type, status, created, updated |
| [[docker-ro-mount-chmod-fails]] | type, status, created, updated |
| [[docker-volume-host-dir-created-as-root]] | type, status, created, updated |
| [[git-amend-remove-sensitive-push]] | type, status, created, updated |

### Missing `status` only (systematic — all areas/ and most older concepts)

All 16 `areas/` pages are missing `status` and `created`. All concepts created before 2026-05 are missing `status`. Approx. 65 pages total. Suggest a batch fix: set `status: established` for all `areas/` pages and all pre-May-2026 concept pages, `status: developing` for all learning/example pages.

### Recommended batch fix (safe to auto-apply on request)

```
areas/: status: established, created: 2026-05-[date per file]
concepts/ (pre-rollout): status: established
concepts/ (post-rollout, no address yet): status: developing
learning/: status: developing
examples/: status: developing
```

---

## 7. Empty Sections

- [[wiki-school/sources/_index]]: `## Papers & Articles` and `## Books & Resources` sections contain only `*(none yet)*` — both are now populated on disk. Fix: replace with actual links.
- [[wiki-school/entities/_index]]: all four category sections contain `*(none yet)*`. Fix: populate with the 6 existing entity pages.

---

## 8. Stale Index Entries

**[[wiki-school/index]]**: No dead entries found. All pages referenced in the main index exist on disk.

---

## 8a. Sub-Index Mismatches ⚠️

### `wiki/concepts/_index.md` — lists 85, disk has **98** → **13 missing**

| Missing Page | Suggested Domain Section |
|---|---|
| [[ai-workflows]] | AI Engineering (new section) |
| [[ai-workflow-orchestration]] | AI Engineering (new section) |
| [[retrieval-augmented-generation]] | AI Engineering (new section) |
| [[rag-architectures]] | AI Engineering (new section) |
| [[mcp-model-context-protocol]] | AI Engineering (new section) |
| [[mcp-security]] | AI Engineering (new section) |
| [[context-compression-llm]] | AI Engineering (new section) |
| [[kv-cache-compression]] | AI Engineering (new section) |
| [[prompt-compression]] | AI Engineering (new section) |
| [[blockchain-technology]] | Blockchain / Distributed Systems (new section) |
| [[github-actions-cicd]] | Software Engineering (DevOps subsection) |
| [[nginx-reverse-proxy-and-tls]] | Web Development |
| [[customtkinter-window-lifecycle]] | Programming Fundamentals |

### `wiki/sources/_index.md` — lists 17, disk has **37** → **20 missing**

**Course notes missing from index:**

| Source | Domain |
|---|---|
| [[INF1002-programming-fundamentals]] | programming-fundamentals |
| [[INF1006-computer-networks]] | computer-networks |
| [[INF1007-ethics-professional-conduct]] | it-ethics |
| [[INF2001-intro-software-engineering]] | software-engineering |
| [[INF2004-embedded-systems-programming]] | embedded-systems |

**Articles / references missing from index:**

| Source | Domain |
|---|---|
| [[anthropic-mcp-launch-2024]] | ai-engineering |
| [[mcp-spec-2025-11-25]] | ai-engineering |
| [[mcp-first-year-2025]] | ai-engineering |
| [[anthropic-building-effective-agents]] | ai-engineering |
| [[aws-agentic-ai-patterns-2025]] | ai-engineering |
| [[anthropic-effective-context-engineering]] | ai-engineering |
| [[acon-context-compression-agents]] | ai-engineering |
| [[factory-ai-compression-evaluation-2025]] | ai-engineering |
| [[kv-cache-compression-review-2025]] | ai-engineering |
| [[pinecone-rag-guide]] | ai-engineering |
| [[humanloop-rag-architectures-2025]] | ai-engineering |
| [[atlantic-council-cbdc-tracker-2026]] | blockchain |
| [[chainalysis-crypto-crime-report-2025]] | blockchain |
| [[hacken-smart-contract-vulnerabilities-2025]] | blockchain |
| [[layer2-scaling-comparison-2025]] | blockchain |

### `wiki/learning/_index.md` — lists 8, disk has **18** → **10 missing**

| Missing Page | Category |
|---|---|
| [[customtkinter-after-teardown]] | debugging |
| [[docker-compose-build-context]] | devops |
| [[docker-named-volume-stale-content]] | devops |
| [[docker-ro-mount-chmod-fails]] | devops |
| [[docker-volume-host-dir-created-as-root]] | devops |
| [[git-amend-remove-sensitive-push]] | git |
| [[research-software-testing]] | software-engineering |
| [[ssh-stdout-known-hosts-warning]] | devops |
| [[vite-react-spa-migration]] | web-development |
| [[windows-openssl-strawberry-broken]] | devops |

### `wiki/entities/_index.md` — lists 0, disk has **6** → **6 missing**

| Missing Page | Category |
|---|---|
| [[agentic-ai-foundation-aaif]] | organisation |
| [[graphrag-microsoft]] | technology |
| [[llmlingua]] | technology |
| [[nick-szabo]] | person |
| [[satoshi-nakamoto]] | person |
| [[vitalik-buterin]] | person |

### `wiki/areas/_index.md` — 16 listed, 16 on disk → ✓ Complete

### `wiki/synthesis/_index.md` — 13 listed, 13 on disk → ✓ Complete *(fixed this session)*

---

## 9. Address Validation (DragonScale)

**DragonScale is ACTIVE** (`scripts/allocate-address.sh` and `.vault-meta/address-counter.txt` present).

| Metric | Value |
|---|---|
| Counter file value | 67 |
| Highest c- address observed | c-000067 |
| Total addressed pages | 66 |
| Address format errors | 0 |
| Duplicate addresses | 0 |
| `flock` availability | ❌ Not available on Windows — allocator script blocked |

**⚠️ `flock` unavailable**: `allocate-address.sh --peek` fails on Windows because `flock` is a Linux utility not present in Git Bash. The counter file can be read directly (`67`), but the script cannot be invoked. Counter consistency cannot be fully validated programmatically. Workaround: read `.vault-meta/address-counter.txt` directly and compare manually.

**Counter note**: Counter file contains `67`. Highest observed address is `c-000067`. Whether this represents drift depends on whether the counter is pre- or post-increment. Since the script cannot run, this is flagged as an informational item rather than a confirmed error.

### Address Errors (post-rollout pages without address)

**76 pages** created on or after 2026-04-23 are missing `address:` in their frontmatter. Per DragonScale spec, these are **errors** — address assignment is required for all post-rollout pages. Assignment is `wiki-ingest`'s responsibility; do not auto-assign during lint.

Most affected folders:
- `concepts/` (new pages from AI engineering, RAG, MCP sessions)
- `learning/` (newer debug notes)
- `examples/` (ICT2216 lab pages)
- `sources/` (all recently ingested articles)

To resolve: run `wiki-ingest` on each unaddressed page, or manually invoke `allocate-address.sh` and insert the returned address into each page's frontmatter.

---

## 10. Semantic Tiling

**Skipped — `python3` command not found on Windows PATH.**

`scripts/tiling-check.py` exists but Python is aliased as `python` (not `python3`) in this environment. `tiling-check.py --peek` returned exit code 49 (unexpected). To enable:

1. Add Python to PATH as `python3`, or create a `python3` shim pointing to the system Python.
2. Re-run `tiling-check.py --peek` to confirm readiness.
3. Run `tiling-check.py --report wiki/meta/tiling-report-2026-06-25.md`.

---

## Recommended Actions

| Priority | Action | Safe to Auto-Fix? |
|---|---|---|
| High | Add 13 missing pages to `concepts/_index.md` | Yes |
| High | Add 20 missing pages to `sources/_index.md` | Yes |
| High | Add 10 missing pages to `learning/_index.md` | Yes |
| High | Add 6 missing pages to `entities/_index.md` | Yes |
| Medium | Batch-add `status:` field to ~80 pages | Yes (with review) |
| Medium | Assign addresses to 76 post-rollout pages | No — use wiki-ingest |
| Low | Fix `python3` alias to enable semantic tiling | Manual |
| Low | Update concepts/_index.md header (85→98 concepts) | Yes |
| Low | Add cross-ref: mcp-security → agentic-ai-foundation-aaif | Yes |
