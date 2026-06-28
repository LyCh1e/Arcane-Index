---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 1929 — Concatenation of Array"
  - "LeetCode 1470 — Shuffle the Array"
  - "LeetCode 485 — Max Consecutive Ones"
language: Python
difficulty: Easy
---

# LeetCode Array Basics — Chat Session 2026-06-28

Three Easy-tier array manipulation problems solved in Python.

---

## Problem 1 — Concatenation of Array (LeetCode 1929)

Given an integer array `nums` of length `n`, return an array `ans` of length `2n`
where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n`.

### Examples

Input: nums = [1,2,1] → Output: [1,2,1,1,2,1]
Input: nums = [1,3,2,1] → Output: [1,3,2,1,1,3,2,1]

### Solutions

```python
# Pythonic — list concatenation
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# Explicit — maps directly to the problem definition
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
```

Complexity: Time O(n), Space O(n) output (O(1) extra).

---

## Problem 2 — Shuffle the Array (LeetCode 1470)

Given array `nums` of 2n elements in form [x1,x2,...,xn,y1,y2,...,yn],
return [x1,y1,x2,y2,...,xn,yn].

### Examples

Input: nums = [2,5,1,3,4,7], n = 3 → Output: [2,3,5,4,1,7]
Input: nums = [1,2,3,4,4,3,2,1], n = 4 → Output: [1,4,2,3,3,2,4,1]

### Solutions

```python
# Explicit loop
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])      # x[i] at index i
            ans.append(nums[i + n])  # y[i] at index i + n
        return ans

# One-liner with nested comprehension
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [val for i in range(n) for val in (nums[i], nums[i + n])]
```

Complexity: Time O(n), Space O(n) output (O(1) extra).

---

## Problem 3 — Max Consecutive Ones (LeetCode 485)

Given a binary array `nums`, return the maximum number of consecutive 1s.

### Examples

Input: nums = [1,1,0,1,1,1] → Output: 3
Input: nums = [1,0,1,1,0,1] → Output: 2

### Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                max_count = max(max_count, current)
            else:
                current = 0
        return max_count
```

Dry run on [1,1,0,1,1,1]:
num=1: current=1, max=1
num=1: current=2, max=2
num=0: current=0, max=2
num=1: current=1, max=2
num=1: current=2, max=2
num=1: current=3, max=3

Complexity: Time O(n), Space O(1).
