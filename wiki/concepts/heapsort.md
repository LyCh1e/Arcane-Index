---
type: concept
title: "Heapsort"
domain: computer-science
complexity: medium
tags: [sorting, heapsort, heap, in-place, autoresearch]
created: 2026-10-31
updated: 2026-10-31
status: developing
related:
  - "[[concepts/sorting-and-searching]]"
  - "[[concepts/data-structures-fundamentals]]"
  - "[[concepts/hybrid-sorting-algorithms]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Heapsort

Heapsort builds a binary max-heap in the array, then repeatedly swaps the root with the last heap element, shrinks the heap by one and sifts the new root down.

## Properties

| Property | Value | Confidence |
|----------|-------|-----------|
| Worst, average, best time | O(n log n) | high |
| Auxiliary space | O(1), in place | high |
| Stable | No | high |

(Sources: Wikipedia mirrors; University of Washington CSE 373 handout, 2019.)

## Heap construction

- **Bottom-up (sift-down) construction is O(n).** Most nodes sit near the leaves and sift down only a short distance.
- **Top-down (sift-up) construction is O(n log n)**, because it is equivalent to inserting n elements one at a time.
- The overall sort remains O(n log n) either way, since the n extractions dominate.

## Practical position

Heapsort is usually somewhat slower than a well-implemented quicksort because its memory access pattern uses the cache poorly. Its value lies in the guaranteed O(n log n) worst case with O(1) extra space, which is why introsort and pdqsort use it as the fallback when quicksort partitions degrade (see [[concepts/hybrid-sorting-algorithms]]).

> [!gap] A claim that bottom-up heapsort variants improve cache behaviour comes only from a patent filing (low confidence). Verify with a textbook or paper.
