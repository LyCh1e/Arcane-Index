---
type: concept
title: "Non-Comparison Sorting: Counting, Radix and Bucket Sort"
domain: computer-science
complexity: medium
tags: [sorting, counting-sort, radix-sort, bucket-sort, autoresearch]
created: 2026-10-31
updated: 2026-10-31
status: developing
related:
  - "[[concepts/sorting-and-searching]]"
  - "[[concepts/comparison-sort-lower-bound]]"
  - "[[sources/sorting-lower-bound-decision-tree]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Non-Comparison Sorting

These algorithms use the structure of the keys (range or digits) instead of pairwise comparisons, so the Ω(n log n) bound does not constrain them in the standard model (see [[concepts/comparison-sort-lower-bound]]).

## Counting sort

Count occurrences of each key in 0..k−1, convert counts to prefix sums, then place elements into the output array. Time O(n + k), space O(n + k). It is **stable** when elements are placed by scanning the input backwards, and it suits small key ranges.

## Radix sort

Sort by one digit at a time using a stable subroutine, usually counting sort.

| Variant | Direction | Notes |
|---------|-----------|-------|
| LSD | Least significant digit first | Each pass must be stable, because order from lower digits must survive higher-digit passes |
| MSD | Most significant digit first | Recursive: each bucket is sorted by the next digit independently |

Total time is O(d(n + k)) for d digits of base k. For strings, LSD costs Ω(‖R‖) even when distinguishing prefixes are short, and MSD switches to string quicksort for small buckets because a counting pass costs Ω(σ) regardless of bucket size (Source: Helsinki string-algorithms lecture notes; confidence: medium).

## Bucket sort

Distribute elements into buckets by value, sort each bucket and concatenate. Expected O(n) time holds only for roughly uniform input; the worst case is dominated by the per-bucket sort.

> [!gap] Bucket sort was not covered by a retrieved source in this session; the description is standard textbook material and needs a citation.
