---
type: source
status: ingested
title: "Pattern-defeating Quicksort (Peters, 2021)"
source_type: paper
author: "Orson R. L. Peters"
date_published: 2021-06-09
date_ingested: 2026-10-31
url: "https://arxiv.org/abs/2106.05123"
confidence: high
key_claims:
  - "A Dutch national flag partition without three-way comparisons gives O(nk) worst case for k distinct keys"
  - "Hybrid of quicksort, insertion sort and a heapsort fallback, designed as an improvement on introsort"
  - "Linear time on ascending, descending and all-equal inputs"
  - "Adopted by Rust (sort_unstable) and Boost.Sort"
tags: [sorting, quicksort, pdqsort, introsort, autoresearch]
related:
  - "[[concepts/hybrid-sorting-algorithms]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Pattern-defeating Quicksort (Peters, 2021)

**Type:** arXiv paper (cs.DS), 20 pages, submitted 9 June 2021. Reference implementation: `orlp/pdqsort` on GitHub.

## Summary

The paper presents a quicksort variant that detects patterns in its input and exploits them instead of degrading.

## Contributions to the topic

- **Partitioning.** A new solution to the Dutch national flag problem needs no three-way comparisons and yields a worst case of O(nk) for inputs with k distinct elements.
- **Hybrid structure.** It keeps the introsort layout (quicksort, insertion sort for small ranges, heapsort fallback) but triggers the fallback after too many *bad partitions* rather than on recursion depth alone. It also shuffles some elements to break adversarial patterns.
- **Pattern handling.** Strictly ascending, strictly descending and all-equal inputs sort in linear time, as do ascending inputs with one out-of-place element (Source: web search summary of the reference repository).
- **Adoption.** It is a drop-in replacement for `std::sort`, is used by Rust's `sort_unstable`, and appears in Boost.Sort.
- **Limitation.** It is unstable, so it cannot replace a sort where equal-key order matters.

> [!gap] Branchless partitioning and the exact adversarial analysis are not covered in the abstract page fetched. Verify against the full paper.
