---
type: example
address: c-000077
title: "LeetCode Array Basics — Python Solutions"
domain: computer-science
source: "[[sources/leetcode-array-basics]]"
concepts:
  - "[[concepts/array-manipulation-patterns]]"
  - "[[concepts/algorithm-complexity]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, arrays, computer-science]
---

# LeetCode Array Basics — Python Solutions

Three Easy-tier array problems demonstrating patterns 1–3 from [[concepts/array-manipulation-patterns]].

---

## 1929 — Concatenation of Array

> Given `nums` of length `n`, return `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]`.

**Pattern**: [[concepts/array-manipulation-patterns#Pattern 1 — Concatenation|Concatenation]]

```python
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
```

The `+` operator on Python lists constructs a new list by copying both operands end-to-end. This is equivalent to:

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i]     = nums[i]   # first copy
            ans[i + n] = nums[i]   # second copy
        return ans
```

The explicit version maps directly to the problem definition and works identically in languages without operator overloading for lists (Java, C++).

**Complexity**: Time O(n) · Space O(n) output, O(1) extra.

---

## 1470 — Shuffle the Array

> Given `nums = [x1,…,xn,y1,…,yn]`, return `[x1,y1,x2,y2,…,xn,yn]`.

**Pattern**: [[concepts/array-manipulation-patterns#Pattern 2 — Split-Midpoint Interleaving|Split-Midpoint Interleaving]]

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])      # X[i] at index i
            ans.append(nums[i + n])  # Y[i] at index i + n
        return ans
```

The key insight: `nums[i]` and `nums[i + n]` are the i-th elements of the two logical halves. No slicing required.

**One-liner** (same complexity, avoids repeated `append` call overhead):

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [val for i in range(n) for val in (nums[i], nums[i + n])]
```

The nested comprehension iterates `i` over `range(n)`, then for each `i` unpacks the tuple `(nums[i], nums[i + n])` into two consecutive output values.

**Trace on `[2,5,1,3,4,7]`, n=3**:

| i | nums[i] | nums[i+3] | appended |
|---|---------|-----------|----------|
| 0 | 2 | 3 | 2, 3 |
| 1 | 5 | 4 | 5, 4 |
| 2 | 1 | 7 | 1, 7 |

Output: `[2,3,5,4,1,7]` ✓

**Complexity**: Time O(n) · Space O(n) output, O(1) extra.

---

## 485 — Max Consecutive Ones

> Given a binary array `nums`, return the maximum number of consecutive 1s.

**Pattern**: [[concepts/array-manipulation-patterns#Pattern 3 — Linear Scan with Running Counter|Linear Scan with Running Counter]]

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current   = 0
        for num in nums:
            if num == 1:
                current  += 1
                max_count = max(max_count, current)
            else:
                current = 0
        return max_count
```

`max_count` is updated **inside** the `if` block — the maximum can only increase when `current` increases, so there is no need to call `max()` on every reset.

**Trace on `[1,1,0,1,1,1]`**:

| num | current | max_count |
|-----|---------|-----------|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 0 | 0 | 2 |
| 1 | 1 | 2 |
| 1 | 2 | 2 |
| 1 | 3 | **3** |

**Complexity**: Time O(n) · Space O(1).

---

## Pattern Comparison

| Problem | Pattern | Time | Extra Space | Python idiom |
|---------|---------|------|-------------|--------------|
| 1929 | Concatenation | O(n) | O(1) | `nums + nums` |
| 1470 | Split-midpoint interleave | O(n) | O(1) | nested list comprehension |
| 485 | Linear scan / running counter | O(n) | O(1) | `current`/`max_count` variables |

---

## Extension Problems

| LeetCode | Relation |
|----------|----------|
| 1004 — Max Consecutive Ones III | Pattern 3 extended with at-most-k flips (sliding window) |
| 1920 — Build Array from Permutation | Pattern 1 variant with permutation mapping |
| 896 — Monotonic Array | Pattern 3 variant checking monotone condition |
