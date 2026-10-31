---
type: concept
title: "SIMD and Parallel Sorting: vqsort and ips4o"
domain: computer-science
complexity: high
tags: [sorting, simd, parallel, vqsort, ips4o, autoresearch]
created: 2026-10-31
updated: 2026-10-31
status: developing
related:
  - "[[concepts/hybrid-sorting-algorithms]]"
  - "[[sources/vqsort-vectorized-quicksort-2022]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# SIMD and Parallel Sorting

## vqsort

A vectorised quicksort using sorting networks for the base case (n ≤ 256), vectorised cache-aware pivot sampling and portable partitioning. The authors claim up to 20 times the speed of standard-library sorts for non-tuple keys. It supports floating-point and 16- to 128-bit integer keys on seven instruction sets, and is typically single-threaded (Source: [[sources/vqsort-vectorized-quicksort-2022]]; confidence: medium, authors' own benchmarks).

## ips4o

A parallel, in-place samplesort regarded as state of the art for parallel comparison sorting. Using vqsort as its base case gives geometric-mean speedups of 1.59 (parallel) and 2.89 (single core).

## Takeaway

Sorting networks and SIMD matter most for small base cases; algorithm choice at scale then depends on parallelism, key type and instruction-set support. AVX-512 is still not widely available, which motivates the portable design.

> [!gap] The original ips4o paper and super scalar samplesort were not retrieved.
