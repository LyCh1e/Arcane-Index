---
type: concept
title: "Algorithm Complexity"
domain: computer-science
course: INF1008
complexity: medium
tags: [big-oh, complexity, asymptotic, master-theorem, recursion]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000004
---

# Algorithm Complexity

Algorithm complexity analysis answers the question: **how does resource consumption scale as input size grows?** It provides a machine-independent vocabulary for comparing algorithms and predicting performance under real-world loads. Time complexity (operations) and space complexity (memory) are both studied, but time is the primary focus.

## Formal Definitions

Let f(n) and g(n) be functions from positive integers to positive reals.

### Big-Oh — O (Upper Bound)

f(n) = O(g(n)) if there exist constants c > 0 and n₀ > 0 such that:

> f(n) ≤ c · g(n) for all n ≥ n₀

"f grows **no faster than** g." Used for worst-case guarantees.

### Big-Omega — Ω (Lower Bound)

f(n) = Ω(g(n)) if there exist constants c > 0 and n₀ > 0 such that:

> f(n) ≥ c · g(n) for all n ≥ n₀

"f grows **at least as fast as** g." Used for best-case / lower-bound proofs.

### Big-Theta — Θ (Tight Bound)

f(n) = Θ(g(n)) if f(n) = O(g(n)) AND f(n) = Ω(g(n)).

"f grows **at exactly the same rate as** g (up to constants)." The most informative classification.

## Common Complexity Classes

Ordered from fastest to slowest:

| Class | Name | Example algorithms |
|-------|------|--------------------|
| O(1) | Constant | Array index access, hash lookup |
| O(log n) | Logarithmic | Binary search, BST operations |
| O(n) | Linear | Linear search, array traversal |
| O(n log n) | Linearithmic | Merge sort, Heap sort |
| O(n²) | Quadratic | Bubble/Selection/Insertion sort |
| O(n³) | Cubic | Naive matrix multiplication |
| O(2^n) | Exponential | Subset enumeration, naive recursion |
| O(n!) | Factorial | Permutation generation, TSP brute force |

Practical rule: O(n²) is acceptable for n ≤ ~10,000; O(n log n) for n ≤ ~10,000,000; O(n) for essentially any n.

## Asymptotic Rules

These rules simplify complexity analysis:

1. **Drop constants**: 5n² → O(n²)
2. **Drop lower-order terms**: n² + n + 1 → O(n²)
3. **Sum rule**: O(f) + O(g) = O(max(f, g))
4. **Product rule**: O(f) · O(g) = O(f · g)
5. **Loop rule**: a loop with O(n) iterations and O(g(n)) body → O(n · g(n))
6. **Logarithm base doesn't matter**: O(log₂ n) = O(log₁₀ n) (differ by constant factor)

## Best, Worst, and Average Case

The **same algorithm** can have different complexities depending on input:

- **Best case** (Ω): most favourable input (e.g., already-sorted array for Insertion Sort → O(n))
- **Worst case** (O): most adversarial input (e.g., reverse-sorted for Insertion Sort → O(n²))
- **Average case** (Θ): expected over all possible inputs — often hardest to compute, requires probabilistic analysis
- **Amortised**: average cost per operation over a sequence of operations (e.g., dynamic array append is O(1) amortised)

Big-Oh in practice almost always means worst-case unless specified otherwise.

## Master Theorem

The Master Theorem solves recurrences of the form:

> T(n) = a · T(n/b) + f(n)

where a ≥ 1 (subproblems), b > 1 (size reduction factor), f(n) is the work per level.

Let c_crit = log_b(a):

| Case | Condition | Result |
|------|-----------|--------|
| **Case 1** | f(n) = O(n^(c_crit - ε)) | T(n) = Θ(n^c_crit) — recursion dominates |
| **Case 2** | f(n) = Θ(n^c_crit · log^k n) | T(n) = Θ(n^c_crit · log^(k+1) n) — balanced |
| **Case 3** | f(n) = Ω(n^(c_crit + ε)) + regularity | T(n) = Θ(f(n)) — combining step dominates |

### Examples

- **Merge Sort**: T(n) = 2T(n/2) + O(n) → a=2, b=2, c_crit=1, f(n)=O(n) → Case 2 → **O(n log n)**
- **Binary Search**: T(n) = T(n/2) + O(1) → a=1, b=2, c_crit=0, f(n)=O(1) → Case 2 → **O(log n)**
- **Strassen's Matrix Multiply**: T(n) = 7T(n/2) + O(n²) → c_crit = log₂7 ≈ 2.81 > 2 → Case 1 → **O(n^2.81)**

## Recursion Tree Method

When the Master Theorem doesn't apply (unequal subproblem sizes, non-polynomial f(n)):

1. Draw the recursion tree — each node is a subproblem, cost = work at that node
2. Sum the cost at each level
3. Multiply by the number of levels (tree height)
4. Sum across all levels

The recursion tree method is also useful for gaining intuition before applying the Master Theorem.

## Space Complexity

Space complexity counts memory beyond the input:
- **In-place** algorithms use O(1) auxiliary space (Insertion Sort, Quick Sort)
- Merge Sort requires O(n) auxiliary space for the merge buffer
- Recursion depth contributes O(depth) stack space (DFS on a tree → O(h) where h is height)

## See Also

- [[data-structures-fundamentals]] — each structure's operation complexities
- [[sorting-and-searching]] — applying complexity analysis to concrete algorithms
- [[graph-algorithms]] — O(V+E) analysis for traversal algorithms
- [[INF1008-data-structures-algorithms]] — source course
