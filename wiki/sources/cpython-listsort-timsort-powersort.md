---
type: source
status: ingested
title: "CPython listsort.txt — Timsort and Powersort"
source_type: official-documentation
author: "Tim Peters (original); later maintainers; Munro and Wild (powersort)"
date_published: 2002
date_ingested: 2026-10-31
url: "https://github.com/python/cpython/blob/main/Objects/listsort.txt"
confidence: high
key_claims:
  - "Runs are detected, descending runs reversed in place, short runs extended to minrun by binary insertion sort"
  - "Galloping mode starts after MIN_GALLOP = 7 consecutive wins from one side"
  - "Merge order now uses powersort instead of the original Fibonacci-style policy"
  - "Temporary storage reaches at most N/2 pointers"
tags: [sorting, timsort, powersort, python, autoresearch]
related:
  - "[[concepts/hybrid-sorting-algorithms]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# CPython listsort.txt — Timsort and Powersort

**Type:** official implementation notes, maintained alongside `Objects/listobject.c`.

## Summary

The file documents the algorithm behind `list.sort()` and `sorted()`. It is the primary reference for Timsort and is the best available description of how the algorithm behaves in practice.

## Contributions to the topic

- **Run detection.** `count_run()` finds the next maximal run, reverses it in place if it is strictly descending, and extends short runs to `minrun` elements with binary insertion sort.
- **Minrun.** A newer scheme by Stefan Pochmann (2025) varies run lengths slightly so that the number of runs at each level of the merge tree is a power of two. `MAX_MINRUN` is 64, so runs fall roughly between 32 and 64 elements. The older fixed value is described as a historical choice that could produce unbalanced merges.
- **Galloping.** Galloping begins after `MIN_GALLOP` (7) consecutive wins by one run. It probes at exponentially growing offsets and then binary-searches the narrowed region. The threshold adapts: it falls when galloping pays off and rises when it does not.
- **Merge policy.** The original Fibonacci-style policy is replaced by **powersort** (Munro and Wild) because the intended invariants of the old policy were not preserved. The file does not state the CPython version of the change.
- **Comparison counts.** At n = 1,048,576 on random data the algorithm uses 19,606,028 comparisons against a lower bound of lg(n!) ≈ 19,458,756. On the adversarial `!sort` input it uses 2,097,150 comparisons, down from 20,434,212 under the old merge policy.
- **Memory.** Temporary storage reaches at most N/2 pointers on random data and may be negligible on structured data.

> [!gap] The version in which CPython adopted powersort (3.11) comes from a secondary source (Real Python glossary), not from this file.
