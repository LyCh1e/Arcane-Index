---
type: example
address: c-000081
title: "LeetCode 1365 & 448 — Count Smaller / Find Disappeared (Python)"
domain: computer-science
source: "[[sources/leetcode-count-missing]]"
concepts:
  - "[[concepts/array-manipulation-patterns]]"
  - "[[concepts/algorithm-complexity]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, arrays, prefix-sum, set-difference, computer-science]
---

# LeetCode 1365 & 448 — Count Smaller / Find Disappeared

---

## 1365 — How Many Numbers Are Smaller Than the Current Number

> For each `nums[i]`, count how many elements in the array are strictly smaller. Return the counts as an array.
> Constraint: `0 <= nums[i] <= 100`.

**Patterns**: [[concepts/array-manipulation-patterns#Pattern 7 — Prefix Sum on Frequency Array|Prefix Sum on Frequency Array]] · brute force (Pattern 3 variant)

---

### Approach 1 — Brute Force (Clearest Intent)

```python
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for current_number in nums:
            # Count how many numbers in the whole array are smaller
            how_many_are_smaller = 0
            for other_number in nums:
                if other_number < current_number:
                    how_many_are_smaller += 1
            result.append(how_many_are_smaller)

        return result
```

**Why no `j != i` guard?** A number never satisfies `other_number < current_number` when they are the same element — the strict `<` excludes equality automatically.

**Complexity**: Time O(n²) · Space O(1) extra

---

### Approach 2 — Prefix Sum on Frequency Array (Optimal)

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: count occurrences of each value in the range 0-100
        freq = [0] * 101
        for num in nums:
            freq[num] += 1

        # Step 2: running total so freq[i] = "how many values ≤ i"
        for i in range(1, 101):
            freq[i] += freq[i - 1]

        # Step 3: freq[num - 1] = "how many values < num"
        result = []
        for num in nums:
            result.append(freq[num - 1] if num > 0 else 0)
        return result
```

**Why `freq[num - 1]`?** After the prefix sum, `freq[i]` is the count of values ≤ i. We want values **strictly less than** `num`, which is everything ≤ `num - 1`, i.e. `freq[num - 1]`. The `if num > 0` guard handles `num = 0` (nothing can be smaller than 0).

**Trace on `[8, 1, 2, 2, 3]`:**

After counting:

| index | 0 | 1 | 2 | 3 | … | 8 |
|-------|---|---|---|---|---|---|
| freq  | 0 | 1 | 2 | 1 | … | 1 |

After prefix sum:

| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------|---|---|---|---|---|---|---|---|---|
| freq  | 0 | 1 | 3 | 4 | 4 | 4 | 4 | 4 | 5 |

Lookups:
- `8` → `freq[7]` = 4 ✓
- `1` → `freq[0]` = 0 ✓
- `2` → `freq[1]` = 1 ✓
- `2` → `freq[1]` = 1 ✓
- `3` → `freq[2]` = 3 ✓

Output: `[4, 0, 1, 1, 3]` ✓

**Complexity**: Time O(n + 101) → O(n) · Space O(101) → O(1) fixed

---

### Approach 3 — Sort + Index Trick

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]
```

**How it works**: after sorting, each element's position is exactly the count of elements smaller than it. `.index()` returns the **first** occurrence, so duplicates all report the same (correct) count.

**Trace on `[8, 1, 2, 2, 3]`:**

`sorted_nums = [1, 2, 2, 3, 8]`

| num | first index in sorted | result |
|-----|----------------------|--------|
| 8   | 4 | 4 ✓ |
| 1   | 0 | 0 ✓ |
| 2   | 1 | 1 ✓ |
| 2   | 1 | 1 ✓ |
| 3   | 3 | 3 ✓ |

**Complexity**: Time O(n log n) · Space O(n)

---

### Approach Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Clearest intent; too slow for large n |
| Prefix sum | O(n) | O(1) | Optimal; requires bounded value range |
| Sort + index | O(n log n) | O(n) | Elegant; no range constraint needed |

---

## 448 — Find All Numbers Disappeared in an Array

> Given `nums` of length n where `1 <= nums[i] <= n`, return all integers in `[1, n]` not present in `nums`.

**Pattern**: [[concepts/array-manipulation-patterns#Pattern 8 — Set Difference|Set Difference]]

---

### Solution — Set Difference

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Every number that should be present
        full_set = set(range(1, len(nums) + 1))

        # Every number that actually is present
        present = set(nums)

        # Whatever should be there but isn't
        missing = full_set - present

        return list(missing)
```

**One-liner** (same logic, no intermediate variables):

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
```

**Trace on `[4, 3, 2, 7, 8, 2, 3, 1]`**, n=8:

- `full_set` = {1, 2, 3, 4, 5, 6, 7, 8}
- `present`  = {1, 2, 3, 4, 7, 8}
- `missing`  = {5, 6} ✓

**Trace on `[1, 1]`**, n=2:

- `full_set` = {1, 2}
- `present`  = {1}
- `missing`  = {2} ✓

**Complexity**: Time O(n) · Space O(n)

> [!key-insight] The `-` operator on Python sets is **set difference**, not subtraction. `A - B` returns a new set of elements in A that are not in B. It is O(|A| + |B|) in CPython.

---

## Related Problems

| LeetCode | Relation |
|----------|----------|
| 268 — Missing Number | Single missing value from 1→n; math sum or XOR |
| 645 — Set Mismatch | One duplicate + one missing; [[examples/leetcode-set-mismatch-python]] |
| 41 — First Missing Positive | Missing positive in unsorted, unbounded array |
| 242 — Valid Anagram | Set/freq comparison between two strings |
