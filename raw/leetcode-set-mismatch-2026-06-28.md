---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 645 — Set Mismatch"
language: Python
difficulty: Easy
---

# LeetCode 645 — Set Mismatch

Given an integer array `nums` of length n representing a set of 1→n with one number
duplicated and one number missing, return [duplicate, missing].

## Examples

Input: nums = [1,2,2,4] → Output: [2,3]
Input: nums = [1,1]     → Output: [1,2]

## Solutions

### Approach 1 — Manual frequency dict (most readable)

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Count how many times each number appears
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        duplicate = -1
        missing = -1

        # Check every number from 1 to n
        for i in range(1, n + 1):
            if seen.get(i, 0) == 2:    # appears twice → it's the duplicate
                duplicate = i
            elif seen.get(i, 0) == 0:  # never appears → it's missing
                missing = i

        return [duplicate, missing]
```

Walkthrough on [1,2,2,4]:
- seen = {1:1, 2:2, 4:1}
- i=1 → count 1, normal
- i=2 → count 2 → duplicate = 2
- i=3 → count 0 → missing = 3
- i=4 → count 1, normal
- Return [2, 3] ✓

### Approach 2 — Counter

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)

        duplicate = missing = -1
        for i in range(1, n + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i

        return [duplicate, missing]
```

### Approach 3 — Math / O(1) space

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = sum(nums) - sum(set(nums))       # extra value added by duplicate
        missing   = n * (n + 1) // 2 - sum(set(nums))  # what's missing from expected sum
        return [duplicate, missing]
```

Why it works:
- sum(nums) includes the duplicate twice; sum(set(nums)) counts it once → difference is the duplicate.
- n*(n+1)//2 is the expected sum of 1→n; subtracting actual unique values gives the missing number.

Complexity (all approaches): Time O(n), Space O(n) for dict/Counter, O(1) for math.
