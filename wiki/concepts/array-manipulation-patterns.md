---
type: concept
address: c-000076
title: "Array Manipulation Patterns"
domain: computer-science
complexity: medium
created: 2026-06-28
updated: 2026-06-28
tags: [concept, arrays, algorithms, python, computer-science]
related:
  - concepts/data-structures-fundamentals
  - concepts/algorithm-complexity
  - concepts/sorting-and-searching
---

# Array Manipulation Patterns

Recurring patterns for transforming arrays in-place or producing a new array. All patterns here are O(n) time. Understanding them as named patterns — not one-off tricks — makes the solutions to new array problems immediately recognisable.

---

## Pattern 1 — Concatenation

**Problem shape**: produce a doubled array where the second half is identical to the first.

```python
# Python: list + operator creates a new list
result = nums + nums          # most readable
result = nums * 2             # equivalent for exact duplication

# Language-agnostic: pre-allocate and dual-write
n = len(nums)
ans = [0] * (2 * n)
for i in range(n):
    ans[i]     = nums[i]
    ans[i + n] = nums[i]
```

**When to use**: any problem where `ans[i] == nums[i]` and `ans[i + n] == nums[i]`.

**Complexity**: O(n) time, O(n) space (the output).

**LeetCode**: 1929 — Concatenation of Array.

---

## Pattern 2 — Split-Midpoint Interleaving

**Problem shape**: a single array encodes two logical arrays side by side (first half = X, second half = Y); output must interleave them as X[0], Y[0], X[1], Y[1], …

```python
# Index arithmetic — no slicing needed
n = len(nums) // 2
for i in range(n):
    ans.append(nums[i])        # X[i] lives at index i
    ans.append(nums[i + n])    # Y[i] lives at index i + n

# One-liner with nested comprehension
return [val for i in range(n) for val in (nums[i], nums[i + n])]
```

**Key insight**: treat a single array as two logical sequences using the offset `n`. This avoids creating intermediate slices (`nums[:n]`, `nums[n:]`), keeping extra space at O(1).

**Complexity**: O(n) time, O(n) space (the output).

**LeetCode**: 1470 — Shuffle the Array.

---

## Pattern 3 — Linear Scan with Running Counter

**Problem shape**: find the longest contiguous subarray satisfying a condition (e.g., all 1s, all equal, monotone).

```python
max_count = 0
current   = 0
for val in nums:
    if condition(val):
        current  += 1
        max_count = max(max_count, current)
    else:
        current = 0            # reset on mismatch
return max_count
```

**Why update `max_count` inside the `if`**: the maximum can only grow when `current` grows, so checking there avoids a redundant comparison on every reset.

**Variants**:

| Variant | Change |
|---------|--------|
| Longest run of a specific value | `if val == target:` |
| Longest non-decreasing run | `if val >= prev:` + track `prev` |
| Longest run with at most *k* exceptions | track `exceptions`; reset only when `exceptions > k` |

**Complexity**: O(n) time, O(1) space.

**LeetCode**: 485 — Max Consecutive Ones; 1004 — Max Consecutive Ones III (k-exception variant).

---

## Pattern 4 — Two-Pointer Merge (Reference)

For interleaving two *separate* arrays of equal length into one output:

```python
i, j, k = 0, 0, 0
while i < len(a) and j < len(b):
    result[k] = a[i]; k += 1; i += 1
    result[k] = b[j]; k += 1; j += 1
```

Distinct from Pattern 2 because the inputs are separate arrays, not logical halves of one.

---

## Python-Specific Notes

| Operation | Notes |
|-----------|-------|
| `a + b` | Creates a new list; O(n + m) |
| `a * k` | Repeats `a` exactly `k` times; O(n·k) |
| `[val for i in range(n) for val in (a[i], b[i])]` | Nested comprehension for interleave; single pass |
| `list.extend(other)` | Appends all elements of `other` in place; O(len(other)) |

**List comprehension vs `append` loop**: equivalent in semantics; list comprehension is typically 20–30% faster in CPython due to bytecode optimisation, but both are O(n).

---

## Complexity Summary

| Pattern | Time | Extra Space |
|---------|------|-------------|
| Concatenation (dual-write) | O(n) | O(1) |
| Split-midpoint interleave | O(n) | O(1) |
| Linear scan / running counter | O(n) | O(1) |

Output arrays are O(n) in all cases but are not counted as "extra" space.

---

## See Also

- [[concepts/data-structures-fundamentals]] — arrays, dynamic arrays, memory layout
- [[concepts/algorithm-complexity]] — Big-O analysis
- [[concepts/sorting-and-searching]] — patterns requiring ordered arrays
- [[examples/leetcode-array-basics-python]] — worked examples for patterns 1–3
