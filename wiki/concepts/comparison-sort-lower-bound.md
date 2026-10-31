---
type: concept
title: "Comparison Sort Lower Bound"
domain: computer-science
complexity: medium
tags: [sorting, lower-bound, decision-tree, autoresearch]
created: 2026-10-31
updated: 2026-10-31
status: developing
related:
  - "[[concepts/algorithm-complexity]]"
  - "[[concepts/non-comparison-sorting]]"
  - "[[sources/sorting-lower-bound-decision-tree]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Comparison Sort Lower Bound

Every comparison-based sorting algorithm needs Ω(n log n) comparisons in the worst case.

## Proof

1. Model the algorithm as a binary decision tree: internal nodes are comparisons, leaves are output orderings.
2. A correct algorithm must distinguish all n! input orderings, so the tree has at least n! leaves.
3. A binary tree of height h has at most 2^h leaves, so 2^h ≥ n!, giving h ≥ log₂(n!).
4. By Stirling's approximation, log₂(n!) = Θ(n log n).

(Source: [[sources/sorting-lower-bound-decision-tree]]; confidence: high.)

## Consequences

- Merge sort and heapsort are asymptotically optimal comparison sorts.
- Real implementations approach the bound closely: CPython's sort uses 19,606,028 comparisons at n = 2²⁰ against lg(n!) ≈ 19,458,756 (Source: [[sources/cpython-listsort-timsort-powersort]]).
- The bound applies to the comparison model only. Counting and radix sort exploit key structure (see [[concepts/non-comparison-sorting]]).
