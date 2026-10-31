---
type: source
status: ingested
title: "Sorting Lower Bound Course Materials (OpenDSA, Hawaii ICS 311, UNL, Tulane)"
source_type: lecture-notes
author: "Multiple university course authors"
date_published: undated
date_ingested: 2026-10-31
url: "https://opendsax.cs.vt.edu/ODSA/RST/en/Sorting/SortingLowerBound.rst"
confidence: high
key_claims:
  - "Any comparison sort corresponds to a binary decision tree with at least n! leaves"
  - "Height h >= log2(n!) = Omega(n log n) by Stirling's approximation"
  - "Merge sort and heapsort are asymptotically optimal comparison sorts"
  - "Counting and radix sort avoid the bound by using key structure"
tags: [sorting, lower-bound, decision-tree, autoresearch]
related:
  - "[[concepts/comparison-sort-lower-bound]]"
  - "[[concepts/non-comparison-sorting]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Sorting Lower Bound Course Materials

**Type:** several consistent university lecture sets. These are undated, so treat them as foundational rather than current.

## Summary

The sources agree on the decision-tree proof of the Ω(n log n) bound and on why counting and radix sort escape it.

## Contributions to the topic

- **Proof outline.** Each internal node of the tree is a comparison and each leaf an output ordering. There are n! orderings, so the tree has at least n! leaves. A binary tree of height h has at most 2^h leaves, so h ≥ log₂(n!), which is Ω(n log n) by Stirling's approximation.
- **Corollary.** Merge sort and heapsort are asymptotically optimal among comparison sorts.
- **Escape routes.** Counting and radix sort use the range or digits of the keys rather than pairwise comparisons.
- **Disagreement.** OpenDSA argues that radix sort still performs comparisons in a different form, so the bound can apply to it in a general model. The other sources use the standard reading in which the bound holds only for the comparison model.
