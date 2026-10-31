---
type: source
status: ingested
title: "Vectorized and Performance-Portable Quicksort (vqsort, 2022)"
source_type: paper
author: "Highway / vqsort authors"
date_published: 2022-05
date_ingested: 2026-10-31
url: "https://arxiv.org/abs/2205.05982"
confidence: medium
key_claims:
  - "Claimed up to 20 times faster than standard-library sorts on CPUs for non-tuple keys"
  - "Sorting networks form the base case for n <= 256"
  - "Plugging vqsort into ips4o yields geometric-mean speedups of 1.59 (parallel) and 2.89 (single core)"
  - "Runs across seven instruction sets including AVX-512, SVE and RISC-V V"
tags: [sorting, simd, vqsort, ips4o, parallel, autoresearch]
related:
  - "[[concepts/simd-and-parallel-sorting]]"
  - "[[synthesis/research-sorting-algorithms]]"
---

# Vectorized and Performance-Portable Quicksort (vqsort, 2022)

**Type:** arXiv paper 2205.05982. Production-ready open-source code accompanies it.

## Summary

The paper describes vqsort, a SIMD quicksort that is portable across instruction sets rather than tied to AVX-512.

## Contributions to the topic

- **Speed claim.** The authors state that it is the fastest known sort for non-tuple keys on CPUs, up to 20 times faster than standard-library implementations. Vendor-style speed claims are authors' own measurements.
- **Design.** Sorting networks handle the base case (n ≤ 256). A vectorised, cache-aware, robust pivot-sampling step and a portable partitioning routine complete the design.
- **Relation to ips4o.** ips4o is a parallel, in-place samplesort, described as state of the art for parallel comparison sorting. Using vqsort as its base case gives geometric-mean speedups of 1.59 in parallel and 2.89 single-core.
- **Coverage.** Supports floating-point and 16- to 128-bit integer keys across seven instruction sets on four platforms. The implementation is typically single-threaded and limited to a small set of key types.

> [!gap] The speed claim is not independently verified here. The ips4o original paper and super scalar samplesort were not retrieved.
