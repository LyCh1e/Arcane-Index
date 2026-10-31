---
type: concept
title: "Shellsort"
domain: computer-science
complexity: medium
tags: [sorting, shellsort, gap-sequence, insertion-sort, autoresearch]
created: 2026-10-31
updated: 2026-10-31
status: developing
related:
  - "[[concepts/sorting-and-searching]]"
  - "[[concepts/hybrid-sorting-algorithms]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Shellsort

Shellsort generalises insertion sort. It sorts elements that lie a fixed **gap** apart, shrinks the gap and repeats, finishing with gap 1 (plain insertion sort on a nearly sorted array).

## Complexity depends on the gap sequence

- Worst case is O(n²) for the worst known gap sequences.
- Worst case is O(n log² n) for the best known worst-case gap sequences.
- The sequence with the best asymptotic bound has a very large constant factor, which motivated further sequences. (Source: Wikipedia mirrors; arXiv 2301.00316, "Optimization Perspectives on Shellsort".)

## Ciura sequence

Ciura (2001) found the gaps 1, 4, 10, 23, 57, 132, 301, 701, 1750 experimentally, optimising the number of comparisons, which relates more directly to running time than other measures. **No complexity bound is proven for it.** Values beyond 701 were not determined experimentally; the sequence is extended by a recursive formula. Confidence: medium (secondary sources).

## Properties

In place (O(1) space) and unstable. It is useful where recursion or auxiliary memory is unavailable.
