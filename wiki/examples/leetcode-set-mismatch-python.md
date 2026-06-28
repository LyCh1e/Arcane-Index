---
type: example
address: c-000079
title: "LeetCode 645 — Set Mismatch (Python)"
domain: computer-science
source: "[[sources/leetcode-set-mismatch]]"
concepts:
  - "[[concepts/array-manipulation-patterns]]"
  - "[[concepts/algorithm-complexity]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, arrays, frequency-count, computer-science]
---

# LeetCode 645 — Set Mismatch

> A set of integers 1→n has one number duplicated and one number missing. Given the resulting array, return `[duplicate, missing]`.

**Patterns used**: [[concepts/array-manipulation-patterns#Pattern 4 — Frequency Count|Frequency Count]] · [[concepts/array-manipulation-patterns#Pattern 5 — Math Sum Identity|Math Sum Identity]]

---

## Approach 1 — Manual Frequency Dict (Most Readable)

```python
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Pass 1: count how many times each number appears
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        duplicate = -1
        missing   = -1

        # Pass 2: check every valid number 1→n for anomalies
        for i in range(1, n + 1):
            if seen.get(i, 0) == 2:    # appears twice → duplicate
                duplicate = i
            elif seen.get(i, 0) == 0:  # never appears → missing
                missing = i

        return [duplicate, missing]
```

### Why `seen.get(i, 0)` instead of `seen[i]`

`seen[i]` raises `KeyError` if `i` was never in `nums`. `.get(i, 0)` returns 0 safely, which is exactly the "never appeared" count we want to detect the missing number.

### Trace on `[1, 2, 2, 4]`

**Pass 1** — build `seen`:

| num | seen after |
|-----|-----------|
| 1 | `{1: 1}` |
| 2 | `{1: 1, 2: 1}` |
| 2 | `{1: 1, 2: 2}` |
| 4 | `{1: 1, 2: 2, 4: 1}` |

**Pass 2** — scan 1→4:

| i | count | result |
|---|-------|--------|
| 1 | 1 | normal |
| 2 | 2 | `duplicate = 2` |
| 3 | 0 | `missing = 3` |
| 4 | 1 | normal |

Return `[2, 3]` ✓

**Complexity**: Time O(n) · Space O(n)

---

## Approach 2 — `collections.Counter`

```python
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n     = len(nums)
        count = Counter(nums)   # same as a frequency dict, built in one call

        duplicate = missing = -1
        for i in range(1, n + 1):
            if count[i] == 2:   # Counter returns 0 for missing keys by default
                duplicate = i
            elif count[i] == 0:
                missing = i

        return [duplicate, missing]
```

`Counter` is a `dict` subclass that returns 0 for missing keys automatically — the same behaviour `.get(key, 0)` produces manually. Use this when terseness matters more than avoiding an import.

**Complexity**: Time O(n) · Space O(n)

---

## Approach 3 — Math / O(1) Space

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        actual_sum  = sum(set(nums))        # sum of unique values actually present
        expected    = n * (n + 1) // 2      # sum of 1→n (Gauss formula)

        duplicate = sum(nums) - actual_sum   # nums includes duplicate twice; set removes one copy
        missing   = expected  - actual_sum   # what's absent from the unique values

        return [duplicate, missing]
```

### Why it works

| Expression | Meaning |
|-----------|---------|
| `sum(nums)` | Correct sum + duplicate (because duplicate is counted twice) |
| `sum(set(nums))` | Correct sum − missing (because missing never appears) |
| `sum(nums) − sum(set(nums))` | = duplicate |
| `n*(n+1)//2 − sum(set(nums))` | = missing |

**Example** with `[1, 2, 2, 4]`, n=4:

- `sum(nums)` = 1+2+2+4 = 9
- `sum(set(nums))` = 1+2+4 = 7
- `duplicate` = 9 − 7 = **2** ✓
- `expected` = 4×5//2 = 10
- `missing` = 10 − 7 = **3** ✓

**Complexity**: Time O(n) · Space O(n) for the `set` (though it only stores unique values); truly O(1) if using XOR or index-marking approaches.

> [!key-insight] The O(1) space version requires the XOR trick or in-place index negation (see LeetCode 287 — Find the Duplicate Number for the full treatment).

---

## Approach Comparison

| Approach | Time | Space | Readability | When to use |
|----------|------|-------|-------------|-------------|
| Manual dict | O(n) | O(n) | ★★★★★ | Interviews, clarity required |
| `Counter` | O(n) | O(n) | ★★★★☆ | Quick solutions, stdlib available |
| Math | O(n) | O(n)* | ★★★☆☆ | Space-constrained, showing off |

*The `set()` call still allocates O(n) here; true O(1) requires a different technique.

---

## Related Problems

| LeetCode | Relation |
|----------|----------|
| 268 — Missing Number | Simpler version: only find missing, no duplicate |
| 287 — Find the Duplicate Number | Only find duplicate; harder constraints (no extra space) |
| 41 — First Missing Positive | Generalised missing number in unsorted array |
| 485 — Max Consecutive Ones | Same frequency-scan structure applied to runs |
