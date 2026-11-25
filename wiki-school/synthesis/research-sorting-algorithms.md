---
type: synthesis
title: "Research: Sorting Algorithms"
created: 2026-10-31
updated: 2026-10-31
tags:
  - research
  - sorting
  - algorithms
status: developing
related:
  - "[[sorting-and-searching]]"
  - "[[heapsort]]"
  - "[[shellsort]]"
  - "[[hybrid-sorting-algorithms]]"
  - "[[non-comparison-sorting]]"
  - "[[comparison-sort-lower-bound]]"
  - "[[simd-and-parallel-sorting]]"
sources:
  - "[[cpython-listsort-timsort-powersort]]"
  - "[[pdqsort-peters-2021]]"
  - "[[vqsort-vectorized-quicksort-2022]]"
  - "[[sorting-lower-bound-decision-tree]]"
---

# Research: Sorting Algorithms

## Overview

The wiki already covered bubble, selection, insertion, merge and quick sort ([[sorting-and-searching]]). This research fills the remaining families: heap and Shell sort, non-comparison sorts, the hybrids used in real libraries, the theoretical lower bound, and SIMD and parallel sorting.

## Key Findings

- Comparison sorts cannot beat Ω(n log n) worst case; merge sort and heapsort meet it (Source: [[sorting-lower-bound-decision-tree]]). Confidence: high.
- Counting and radix sort reach O(n + k) and O(d(n + k)) by using key structure (Source: [[non-comparison-sorting]]). Confidence: medium.
- Heapsort is O(n log n) in place but cache-unfriendly, so it serves mainly as the fallback in hybrids (Source: [[heapsort]]). Confidence: high.
- Python's sort keeps Timsort's run detection and galloping, but merge order is now powersort (Source: [[cpython-listsort-timsort-powersort]]). Confidence: high; version 3.11 medium.
- pdqsort is O(nk) for k distinct keys and linear on ascending, descending and constant input (Source: [[pdqsort-peters-2021]]). Confidence: high.
- vqsort claims up to 20 times the speed of standard-library sorts (Source: [[vqsort-vectorized-quicksort-2022]]). Confidence: medium, authors' own benchmarks.
- Shellsort complexity depends on the gap sequence; Ciura's sequence has no proven bound (Source: [[shellsort]]). Confidence: medium.

## Key Entities

- Tim Peters: author of Timsort.
- Orson R. L. Peters: author of pdqsort.
- Munro and Wild: authors of powersort.
- Marcin Ciura: author of the experimental Shellsort gap sequence.

## Key Concepts

- [[hybrid-sorting-algorithms]]: Timsort, Powersort, introsort, pdqsort.
- [[non-comparison-sorting]]: counting, radix, bucket.
- [[comparison-sort-lower-bound]]: decision-tree proof.
- [[simd-and-parallel-sorting]]: vqsort, ips4o.

## Contradictions

- Older web articles say Python uses Timsort; the CPython source notes say the merge policy is now powersort. The primary source is more credible.
- OpenDSA argues radix sort still performs comparisons, so the lower bound may apply to it; other course notes say it escapes the bound. The standard comparison-model reading favours the latter.

## Open Questions

- Which CPython release adopted powersort? Only a secondary source says 3.11.
- Bucket sort, bogosort-style curiosities, merge-insertion sort, smoothsort, cycle sort and library sort were not researched.
- The original ips4o and super scalar samplesort papers were not retrieved.
- Branchless partitioning in pdqsort needs the full paper.
- Max-pages and round limits were respected; no learned-sort or external-memory sorting coverage.

## Sources

- [[cpython-listsort-timsort-powersort]]: CPython maintainers, ongoing.
- [[pdqsort-peters-2021]]: Peters, 2021.
- [[vqsort-vectorized-quicksort-2022]]: vqsort authors, 2022.
- [[sorting-lower-bound-decision-tree]]: university course materials, undated.
