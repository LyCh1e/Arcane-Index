---
type: concept
title: "Hybrid Sorting Algorithms: Timsort, Powersort, Introsort, pdqsort"
domain: computer-science
complexity: high
tags: [sorting, timsort, powersort, introsort, pdqsort, autoresearch]
created: 2026-10-31
updated: 2026-10-31
status: developing
related:
  - "[[concepts/sorting-and-searching]]"
  - "[[concepts/heapsort]]"
  - "[[sources/cpython-listsort-timsort-powersort]]"
  - "[[sources/pdqsort-peters-2021]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Hybrid Sorting Algorithms

Production libraries combine several classical algorithms so that each covers the others' weaknesses.

## Comparison

| Algorithm | Components | Stable | Used by |
|-----------|-----------|--------|---------|
| Timsort / Powersort | Run detection, binary insertion sort, galloping merge | Yes | Python `list.sort()` |
| Introsort | Quicksort, insertion sort, heapsort fallback on depth limit | No | C++ `std::sort` implementations |
| pdqsort | Introsort structure, bad-partition counter, pattern detection | No | Rust `sort_unstable`, Boost.Sort |

## Timsort and Powersort

1. Scan for maximal ascending or strictly descending runs; reverse descending runs in place.
2. Extend runs shorter than `minrun` using binary insertion sort.
3. Merge runs using a stack. **Galloping** (exponential search after 7 consecutive wins) copies blocks when one run dominates.
4. CPython's merge order now follows **powersort** (Munro and Wild), replacing the Fibonacci-style policy whose invariants did not hold. Real Python's glossary dates this to Python 3.11 (Source: [[sources/cpython-listsort-timsort-powersort]]; confidence: medium on the version).

Memory use is at most N/2 pointers, and structured input can need as few as N−1 comparisons. Older web articles that still say "Python uses Timsort" are partly outdated: the run-detection ideas remain, the merge policy differs.

## Introsort

Introsort runs quicksort and switches to heapsort when recursion depth exceeds a limit proportional to log n. That guarantees O(n log n) worst case while keeping quicksort's average speed. Small ranges finish with insertion sort.

## pdqsort

Pattern-defeating quicksort replaces the depth limit with a count of *bad partitions* and shuffles elements to break patterns. It sorts ascending, descending and all-equal input in linear time and is O(nk) for k distinct keys (Source: [[sources/pdqsort-peters-2021]]).

## Choosing

Use a stable hybrid (Timsort-family) for objects with secondary keys or partly ordered data. Use pdqsort or introsort for primitives where stability is irrelevant.
