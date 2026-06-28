---
type: example
address: c-000087
title: "LeetCode 1946 — Maximum Element After Decreasing and Rearranging (Python)"
domain: computer-science
source: "[[sources/leetcode-max-element-rearranging]]"
concepts:
  - "[[concepts/greedy-patterns]]"
  - "[[concepts/sorting-and-searching]]"
  - "[[concepts/algorithm-complexity]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, greedy, sorting, computer-science]
---

# LeetCode 1946 — Maximum Element After Decreasing and Rearranging

> You may rearrange elements freely and decrease any element to any smaller positive integer. After operations: `arr[0] == 1` and `abs(arr[i] - arr[i-1]) <= 1` for all adjacent pairs. Return the maximum possible element value.

**Pattern**: [[concepts/greedy-patterns#Pattern 1 — Sort + Greedy Constraint Propagation|Sort + Greedy Constraint Propagation]]

---

## Solution

```python
from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()      # eliminate rearrangement degree of freedom
        arr[0] = 1      # hard requirement: first element must be 1

        for i in range(1, len(arr)):
            # Each element can be at most 1 more than its predecessor
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]  # last element is the maximum achievable value
```

---

## Why Each Step is Necessary

### Step 1 — `arr.sort()`

We can rearrange freely, so we choose the arrangement that maximises the final value. That arrangement is sorted ascending: it places the smallest elements first, giving each subsequent position the largest possible predecessor, maximising the `arr[i-1] + 1` budget at every step.

Any other ordering wastes budget. Example:

```
arr = [1, 100, 1000]

Unsorted attempt [1000, 100, 1]:
  arr[0] = 1
  arr[1] = min(100, 1+1) = 2
  arr[2] = min(1, 2+1) = 1  ← capped by its own small value, not the constraint
  Result: 1  ✗

Sorted [1, 100, 1000]:
  arr[0] = 1
  arr[1] = min(100, 2) = 2
  arr[2] = min(1000, 3) = 3
  Result: 3  ✓
```

### Step 2 — `arr[0] = 1`

The problem requires `arr[0] == 1`. Since we have already sorted and `arr[0]` is the smallest element (and all elements are ≥ 1 by constraint), we can always set it to 1.

### Step 3 — `arr[i] = min(arr[i], arr[i-1] + 1)`

The adjacency constraint allows `arr[i]` to be at most `arr[i-1] + 1`. The original sorted value `arr[i]` may already satisfy this (keep it) or exceed it (cap it). We never reduce below the predecessor because the sorted order guarantees `arr[i] >= arr[i-1]` before capping, so the effective choices are:

| Condition | Result |
|-----------|--------|
| `arr[i] <= arr[i-1] + 1` | Keep `arr[i]` — no cap needed |
| `arr[i] > arr[i-1] + 1` | Cap to `arr[i-1] + 1` — constraint violated otherwise |

### Step 4 — `return arr[-1]`

After propagation, the last element holds the largest value achievable under the constraints. No element further right exists to push it higher.

---

## Trace — `arr = [100, 1, 1000]`

After sort: `[1, 100, 1000]`

| i | arr[i] before | arr[i-1] + 1 | arr[i] after |
|---|--------------|--------------|-------------|
| 0 | 1 (forced) | — | **1** |
| 1 | 100 | 1+1 = 2 | **2** |
| 2 | 1000 | 2+1 = 3 | **3** |

Return **3** ✓

---

## Trace — `arr = [2, 2, 1, 2, 1]`

After sort: `[1, 1, 2, 2, 2]`

| i | arr[i] before | arr[i-1] + 1 | arr[i] after |
|---|--------------|--------------|-------------|
| 0 | 1 (forced) | — | **1** |
| 1 | 1 | 1+1 = 2 | **1** (already ≤ 2) |
| 2 | 2 | 1+1 = 2 | **2** |
| 3 | 2 | 2+1 = 3 | **2** (already ≤ 3) |
| 4 | 2 | 2+1 = 3 | **2** (already ≤ 3) |

Return **2** ✓

---

## Trace — `arr = [1, 2, 3, 4, 5]`

Already sorted. After sort: `[1, 2, 3, 4, 5]`

| i | arr[i] before | arr[i-1] + 1 | arr[i] after |
|---|--------------|--------------|-------------|
| 0 | 1 (forced) | — | **1** |
| 1 | 2 | 2 | **2** |
| 2 | 3 | 3 | **3** |
| 3 | 4 | 4 | **4** |
| 4 | 5 | 5 | **5** |

Return **5** ✓ — no caps needed; original array was already valid.

---

## Complexity

| Dimension | Value | Reason |
|-----------|-------|--------|
| Time | O(n log n) | Sorting dominates; propagation is O(n) |
| Space | O(1) | Modified in place; no auxiliary array |

---

## Related Problems

| LeetCode | Relation |
|----------|----------|
| 135 — Candy | Two-pass greedy; left-to-right then right-to-left constraint propagation |
| 455 — Assign Cookies | Sort + greedy matching of two arrays |
| 1005 — Maximize Sum of Array After K Negations | Sort + greedy sign-flip |
| 406 — Queue Reconstruction by Height | Sort + greedy insertion |
