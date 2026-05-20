---
type: meta
title: "Lint Report 2026-05-21"
created: 2026-05-21
updated: 2026-05-21
tags: [meta, lint]
status: complete
---

# Lint Report: 2026-05-21

## Summary

- Pages scanned: 117
- Issues found: 28
- Auto-fixed: 0
- Needs review: 28

---

## Sub-Index Mismatches (Check 8a)

### `wiki/concepts/_index.md` — count wrong ❌

Header claims **58 pages**; domain table sums to **57** (row "Secure Software Development" reads 7 but only 6 pages exist on disk); actual disk count is **56**.

```
concepts/_index.md: lists 58 pages (header) / 57 (domain table), found 56 on disk.
Secure Software Development row: claims 7, actual 6.
```

Suggest: update header to `56 concept pages across 12 domains` and correct the SSD domain row to `6`.

### `wiki/examples/_index.md` — missing entry ❌

Lists **3** pages; disk has **4**. Missing page not listed in sub-index:

- [[examples/ict2216-lab3-threat-modeling-tool]] — present in `wiki/index.md` and on disk, absent from `examples/_index.md`.

Suggest: add the missing row to the sub-index Pages table.

---

## Missing Pages (Check 4)

### `wiki/areas/agile-project-management.md` — does not exist ❌

Five pages carry `domain: agile-project-management` in their frontmatter but no area overview page exists, and `wiki/areas/_index.md` does not list the domain:

- [[concepts/scrum-framework]]
- [[sources/scrum-guide-2020]]
- [[learning/scrum-open-assessment-study-notes]]
- [[learning/scrum-master-exam-study-notes]]
- [[learning/psm1-cheatsheet-study-notes]]

Suggest: create `wiki/areas/agile-project-management.md` and add a row to `wiki/areas/_index.md`.

---

## Cross-Reference Gaps (Check 5)

### `wiki/sources/_index.md` — ICT2216 entry incomplete

The ICT2216 source row in `sources/_index.md` lists only 5 concepts but 6 exist on disk. Missing:

- [[concepts/security-by-design-principles]] — on disk, not listed under the ICT2216 "Secure Software Development" section.

Suggest: add the missing link to the ICT2216 row in `sources/_index.md`.

---

## Frontmatter Gaps (Check 6)

### `status:` field missing from all concept pages (56 pages) ❌

Zero of 56 concept pages carry a `status:` field. Dataview queries (e.g. "Seed Pages") that filter on `status = "seed"` will return no results.

Suggested values: `seed | developing | established | archived`

Recommend a mass auto-fix (safe to apply) — add `status: established` to all existing concept pages (they are mature pages, not seeds).

### `created:` field missing from most pages ❌

Only 5 pages in the entire vault carry a `created:` field:

| Page | created |
|------|---------|
| [[concepts/docker-compose]] | 2026-05-11 |
| [[examples/ict2216-lab1-docker-compose]] | 2026-05-11 |
| [[examples/ict2216-lab2-securityrat]] | 2026-05-11 |
| [[learning/docker-windows-crlf]] | 2026-05-11 |
| [[resources/securityrat]] | 2026-05-11 |

The remaining ~112 pages lack `created:`. This also blocks DragonScale post-rollout classification (see Address Validation below).

Recommend: backfill `created:` using `updated:` dates as a proxy where `updated:` is the earliest known date per page.

### `scrum-framework.md` — missing `created:` and `status:`

[[concepts/scrum-framework]] specifically has neither field; as the only Agile concept page it will not surface in any Dataview status or recency queries.

---

## Orphan Pages (Check 1)

These pages have no inbound wikilinks from any content page. They are structural index files, not content orphans, but are noted for awareness:

- [[gaps/_index.md]] — no content or inbound links; Gaps section of `wiki/index.md` says `*(none yet)*`
- [[entities/_index.md]] — no entities exist yet; Entities section of `wiki/index.md` says `*(none yet)*`

No action required unless structural indexes should be linked from area pages.

---

## Address Validation (Check 9)

DragonScale is **active** (`.vault-meta/address-counter.txt` and `scripts/allocate-address.sh` both present). Rollout baseline: **2026-04-23** (set in `.vault-meta/legacy-pages.txt`).

### Errors

**Counter drift** ❌

`.vault-meta/address-counter.txt` contains `3`, but the highest `c-` address observed in page frontmatter is `c-000031`. The counter is behind by at least 28. Any new allocation without rebuilding will produce duplicate addresses.

> Note: `flock` is unavailable on Windows; `allocate-address.sh --peek` exits with code 1 and cannot be run directly. Counter verification and rebuild must be performed in a WSL or Linux environment.
>
> Fix: open WSL, navigate to the vault root, and run:
> ```bash
> bash scripts/allocate-address.sh --rebuild
> ```

**Post-rollout pages missing `address:` field** ❌

Five pages have `created: 2026-05-11` (post-rollout) and no `address:` in frontmatter, even though `raw/.manifest.json` maps them to addresses:

| Page | Manifest address |
|------|-----------------|
| [[concepts/docker-compose]] | `c-000003`* (as `lightweight-rcm`; check mapping) |
| [[examples/ict2216-lab1-docker-compose]] | not in manifest (informational) |
| [[examples/ict2216-lab2-securityrat]] | not in manifest (informational) |
| [[learning/docker-windows-crlf]] | not in manifest (informational) |
| [[resources/securityrat]] | not in manifest (informational) |

Fix: run `wiki-ingest` or manually add `address:` field using `allocate-address.sh` once counter drift is resolved.

**Address-map mismatches** ❌

`raw/.manifest.json` maps approximately 31 `c-NNNNNN` addresses to concept pages, but only 13 of those pages carry an `address:` frontmatter field. The remaining ~18 pages are in the manifest but lack the matching frontmatter field. This means any tooling that reads frontmatter (not the manifest) will not find their addresses.

Pages IN manifest but WITHOUT matching frontmatter `address:`:
- All pages from `c-000002` (`requirements-engineering`) through `c-000018` (`sets-functions-relations`) — 17 concept pages
- Plus `c-000001` (`wiki/concepts/DragonScale Memory.md`) — **page does not exist on disk** (see below)

**Dead manifest entry** ❌

`raw/.manifest.json` maps `wiki/concepts/DragonScale Memory.md` → `c-000001`, but this file does not exist on disk. This is a phantom entry.

Suggest: remove the `wiki/concepts/DragonScale Memory.md` key from `address_map` in `raw/.manifest.json`.

### Address Validation Summary

| Check | Status |
|-------|--------|
| Counter state | ❌ Drift: file=3, max observed=31 |
| Highest c- address observed | `c-000031` |
| Post-rollout pages checked | 5 (0 passing, 5 errors — missing `address:`) |
| Legacy pages pending backfill | ~112 (no `created:` field; treated as legacy) |
| Address-map dead entries | 1 (`DragonScale Memory.md`) |
| Address-map frontmatter mismatches | ~18 pages |

---

## Semantic Tiling (Check 10)

`scripts/tiling-check.py` is present. `flock` is not available on Windows; script cannot run. Skipped.

> To enable: run in WSL with `ollama pull nomic-embed-text` first.

---

## Stale Claims (Check 3)

No cross-source contradictions identified in this pass. The Scrum pages are all consistent with the 2020 Scrum Guide. No action required.

---

## Writing Style Check

No systematic style violations detected in spot-check of concept pages. Pages follow declarative present tense and British English spelling conventions.

---

## Recommended Actions (Priority Order)

| Priority | Action | Safe to auto-fix? |
|----------|--------|------------------|
| 🔴 High | Fix counter drift — run `--rebuild` in WSL | No (requires WSL) |
| 🔴 High | Remove dead manifest entry (`DragonScale Memory.md`) | Yes |
| 🔴 High | Add missing `ict2216-lab3-threat-modeling-tool` to `examples/_index.md` | Yes |
| 🟠 Medium | Create `wiki/areas/agile-project-management.md` | Yes |
| 🟠 Medium | Fix `concepts/_index.md` header and SSD domain count | Yes |
| 🟠 Medium | Add `security-by-design-principles` to ICT2216 row in `sources/_index.md` | Yes |
| 🟡 Low | Backfill `address:` frontmatter for 18 mapped concept pages | No (counter must be fixed first) |
| 🟡 Low | Add `status: established` to all 56 concept pages | Yes (mass) |
| 🟡 Low | Backfill `created:` dates from `updated:` values | Yes (mass) |
