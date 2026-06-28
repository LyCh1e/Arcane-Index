---
type: concept
address: c-000086
title: "Greedy Patterns"
domain: computer-science
complexity: medium
created: 2026-06-28
updated: 2026-06-28
tags: [concept, greedy, sorting, algorithms, computer-science]
related:
  - concepts/sorting-and-searching
  - concepts/algorithm-complexity
  - concepts/simulation-patterns
  - concepts/array-manipulation-patterns
---

# Greedy Patterns

A **greedy algorithm** makes the locally optimal choice at each step with the expectation that local optima compose into a global optimum. Greedy solutions are fast (typically O(n) or O(n log n)) but require a correctness proof — not every problem admits a greedy solution.

**The greedy design checklist**:
1. Identify what "locally optimal" means at each step.
2. Prove (or convince yourself) that a locally optimal choice never rules out a globally optimal solution — the **greedy choice property**.
3. Verify that the problem has **optimal substructure**: an optimal solution to the whole problem contains optimal solutions to its sub-problems.

If both properties hold, greedy works. If not, dynamic programming is usually the next option.

---

## Pattern 1 — Sort + Greedy Constraint Propagation

**Problem shape**: elements can be rearranged freely and decreased (but not increased). A constraint links adjacent elements. Maximise some aggregate value.

**Template**:

```python
arr.sort()          # rearrange optimally in one step
arr[0] = 1          # apply the hard boundary condition for the first element

for i in range(1, len(arr)):
    # cap each element at the maximum the constraint allows given its predecessor
    arr[i] = min(arr[i], arr[i - 1] + 1)

return arr[-1]      # last element is the maximum achievable value
```

**Why sort first?**
Sorting eliminates the rearrangement degree of freedom in one O(n log n) step. After sorting, every element is ≥ its predecessor, so the greedy cap `min(arr[i], arr[i-1] + 1)` has the best possible "budget" at each position. Any other ordering would waste budget on earlier positions, reducing the final maximum.

**Why the greedy cap is correct?**
At position `i`, the maximum permitted value given `arr[i-1]` is `arr[i-1] + 1`. Taking anything less reduces all subsequent maxima — there is no future benefit to under-using the budget now. Taking anything more violates the adjacency constraint. Therefore `min(arr[i], arr[i-1] + 1)` is uniquely optimal.

**In-place safety**: left-to-right propagation only reads `arr[i-1]`, which is already finalised. No auxiliary array needed.

**Complexity**: O(n log n) time (sort dominates), O(1) extra space.

**LeetCode**: 1946 — Maximum Element After Decreasing and Rearranging.

---

## Pattern 2 — Interval Greedy (Placeholder)

*To be filled when the first interval-scheduling or interval-merging problem is ingested.*

Common shape: given a list of intervals, select the maximum number of non-overlapping intervals, or merge all overlapping ones. Sort by end time; greedily pick the interval that ends earliest.

---

## Pattern 3 — Two-Pass Greedy (Placeholder)

*To be filled when the first two-direction greedy problem is ingested.*

Common shape: a constraint from the left and a separate constraint from the right both affect each element. Make one left-to-right pass, then one right-to-left pass, combining the results.

Example problems: Candy (LeetCode 135), Trapping Rain Water (42).

---

## Greedy vs Dynamic Programming

| Property | Greedy | Dynamic Programming |
|----------|--------|---------------------|
| Choice at each step | Irrevocable — commit immediately | Deferred — explore all options |
| Time | O(n) or O(n log n) typically | O(n²) or O(n·k) typically |
| Correctness condition | Greedy choice property + optimal substructure | Optimal substructure alone |
| When to try first | Local optimum clearly composes globally | Choices interact; past decisions affect future options |

**Rule of thumb**: if sorting the input and making one left-to-right pass solves the problem, it is almost certainly greedy.

---

## Complexity Summary

| Pattern | Time | Extra Space |
|---------|------|-------------|
| Sort + constraint propagation | O(n log n) | O(1) |

---

## See Also

- [[concepts/sorting-and-searching]] — sort as greedy pre-processing
- [[concepts/algorithm-complexity]] — Big-O trade-offs between greedy and DP
- [[concepts/simulation-patterns]] — related paradigm: faithful rule replay
- [[examples/leetcode-max-element-rearranging-python]] — worked example for Pattern 1
