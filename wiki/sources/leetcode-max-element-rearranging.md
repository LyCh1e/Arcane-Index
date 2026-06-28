---
type: source
address: c-000085
title: "LeetCode 1946 — Maximum Element After Decreasing and Rearranging"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-max-element-rearranging-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, greedy, sorting, computer-science]
---

# LeetCode 1946 — Maximum Element After Decreasing and Rearranging

Medium-tier problem introducing the **Sort + Greedy Constraint Propagation** paradigm and establishing the new [[concepts/greedy-patterns]] concept page.

| Aspect | Detail |
|--------|--------|
| Pattern | Sort + greedy constraint propagation |
| Key operation | `arr[i] = min(arr[i], arr[i-1] + 1)` |
| Why sorting first | Places the smallest values at the front so each step has the maximum "budget" for the next |

## Key Takeaways

- **Sort to eliminate the rearrangement degree of freedom**: since we can rearrange freely, we lose nothing by sorting. Sorted order is the only arrangement where greedy propagation produces the optimal result.
- **Greedy constraint propagation** (`arr[i] = min(arr[i], arr[i-1] + 1)`): cap each element at one more than its predecessor. This is locally optimal — taking less here can never help, and taking more violates the adjacency constraint. Applied left-to-right on a sorted array, it produces the globally optimal sequence.
- **The answer is always `arr[-1]`** after propagation: the last element in a sorted, constraint-propagated array is the maximum achievable value.
- **In-place modification is safe here** because we process left-to-right and each `arr[i]` only depends on `arr[i-1]`, which is already finalised.

## Related Concepts

- [[concepts/greedy-patterns]] — Pattern 1 (Sort + Greedy Constraint Propagation) introduced by this problem
- [[concepts/sorting-and-searching]] — sorting as a preprocessing step

## Related Examples

- [[examples/leetcode-max-element-rearranging-python]] — annotated solution with two full traces
