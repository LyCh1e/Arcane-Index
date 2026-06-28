---
type: concept
address: c-000076
title: "Array Manipulation Patterns"
domain: computer-science
complexity: medium
created: 2026-06-28
updated: 2026-06-28
tags: [concept, arrays, algorithms, python, frequency-count, computer-science]
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

## Pattern 4 — Frequency Count

**Problem shape**: detect which values appear too many times or not at all by building a count of every value in one pass, then scanning the counts for anomalies in a second pass.

```python
# Manual dict — clearest intent
seen = {}
for num in nums:
    seen[num] = seen.get(num, 0) + 1   # .get(key, 0) avoids KeyError on first occurrence

for i in range(1, n + 1):
    if seen.get(i, 0) == 2:   # appeared twice → duplicate
        duplicate = i
    elif seen.get(i, 0) == 0: # never appeared → missing
        missing = i

# stdlib shorthand — identical semantics, Counter returns 0 for absent keys
from collections import Counter
count = Counter(nums)
```

**When to use**: any problem that reduces to "how many times does each value appear?" — duplicates, missing values, majority elements, anagram detection.

**Key Python detail**: `dict.get(key, 0)` vs `Counter[key]` — both return 0 for absent keys; `Counter` is a `dict` subclass so the behaviour is guaranteed. Raw `dict[key]` raises `KeyError` for absent keys.

**Complexity**: O(n) time, O(n) space (the count structure).

**LeetCode**: 645 — Set Mismatch; 169 — Majority Element; 242 — Valid Anagram.

---

## Pattern 5 — Math Sum Identity

**Problem shape**: when the expected sum of a range is known and one anomaly (duplicate or missing) has shifted the actual sum, arithmetic alone identifies the anomaly in O(1) extra space.

```python
n = len(nums)
expected   = n * (n + 1) // 2    # Gauss formula: sum of 1→n
actual_sum = sum(set(nums))       # sum of unique values actually present

duplicate = sum(nums) - actual_sum  # nums double-counts the duplicate; set removes one copy
missing   = expected  - actual_sum  # expected − actual unique sum = what is absent
```

**Why it works**:

| Expression | What it equals |
|-----------|---------------|
| `sum(nums)` | Correct sum + duplicate |
| `sum(set(nums))` | Correct sum − missing |
| `sum(nums) − sum(set(nums))` | = duplicate |
| `n*(n+1)//2 − sum(set(nums))` | = missing |

**Limitation**: `set()` still allocates O(n) here. True O(1) requires XOR or in-place index-negation (see LeetCode 287).

**When to use**: problems over the range 1→n where the expected aggregate (sum, XOR, product) is computable from a closed-form formula and only one or two elements deviate.

**Complexity**: O(n) time, O(n) space for `set()` (logically O(1) extra beyond input).

**LeetCode**: 645 — Set Mismatch; 268 — Missing Number; 136 — Single Number (XOR variant).

---

## Pattern 7 — Prefix Sum on Frequency Array

**Problem shape**: values are constrained to a small fixed range [0, R]. Count occurrences of every value into a freq array of size R+1, then accumulate a prefix sum so that `freq[i]` answers "how many values are ≤ i?" in O(1). "How many values are < x?" is then `freq[x - 1]`.

```python
R = 100                       # upper bound of value range
freq = [0] * (R + 1)

# Pass 1 — count occurrences
for num in nums:
    freq[num] += 1

# Pass 2 — prefix sum: freq[i] = count of values <= i
for i in range(1, R + 1):
    freq[i] += freq[i - 1]

# Query — how many values < x?
def count_less_than(x):
    return freq[x - 1] if x > 0 else 0
```

**Key insight**: the prefix sum converts a frequency table into a cumulative distribution in one O(R) pass. All subsequent per-element queries are O(1) lookups rather than O(n) scans.

**When to use**: values are bounded to a known small range (constraint clue: `0 <= nums[i] <= 100`). Outperforms the sort+index trick (O(n log n)) and the brute force (O(n²)) when R is small.

**Complexity**: O(n + R) time, O(R) space — effectively O(n) and O(1) when R is a fixed constant.

**LeetCode**: 1365 — How Many Numbers Are Smaller Than the Current Number; 315 — Count of Smaller Numbers After Self (generalised, harder).

---

## Pattern 8 — Set Difference

**Problem shape**: find all values from an expected universe that are absent from a given array. The universe is computable (e.g., `range(1, n+1)`), and the array may contain duplicates.

```python
full_set = set(range(1, len(nums) + 1))   # expected universe
present  = set(nums)                       # values actually seen
missing  = full_set - present              # set difference: in full but not in present
return list(missing)

# One-liner
return list(set(range(1, len(nums) + 1)) - set(nums))
```

**Python `set` operators**:

| Operator | Method | Meaning |
|----------|--------|---------|
| `A - B` | `A.difference(B)` | Elements in A not in B |
| `A & B` | `A.intersection(B)` | Elements in both |
| `A \| B` | `A.union(B)` | Elements in either |
| `A ^ B` | `A.symmetric_difference(B)` | Elements in one but not both |

**Complexity**: O(n) time, O(n) space (both sets).

**LeetCode**: 448 — Find All Numbers Disappeared in an Array; 349 — Intersection of Two Arrays.

---

## Pattern 6 — Two-Pointer Merge (Reference)

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
| Frequency count | O(n) | O(n) |
| Math sum identity | O(n) | O(n)* |
| Prefix sum on freq array | O(n + R) | O(R)† |
| Set difference | O(n) | O(n) |

*`set()` is O(n); true O(1) requires XOR or index-negation variants.
†R = value range (e.g. 101 for 0–100 constraint); effectively O(n) / O(1) when R is a fixed constant.
Output arrays are not counted as "extra" space.

---

## See Also

- [[concepts/data-structures-fundamentals]] — arrays, dynamic arrays, memory layout
- [[concepts/algorithm-complexity]] — Big-O analysis
- [[concepts/sorting-and-searching]] — patterns requiring ordered arrays
- [[examples/leetcode-array-basics-python]] — worked examples for patterns 1–3
- [[examples/leetcode-set-mismatch-python]] — worked examples for patterns 4–5
- [[examples/leetcode-count-missing-python]] — worked examples for patterns 7–8
