---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 1365 — How Many Numbers Are Smaller Than the Current Number"
  - "LeetCode 448 — Find All Numbers Disappeared in an Array"
language: Python
difficulty: Easy
note: "LeetCode 645 (Set Mismatch) appears in the same session but was already ingested separately."
---

# LeetCode Count & Missing — Chat Session 2026-06-28

Two Easy-tier problems demonstrating prefix sum on a frequency array and set difference.

---

## Problem 1 — How Many Numbers Are Smaller Than the Current Number (LeetCode 1365)

For each nums[i], count how many j (j != i) satisfy nums[j] < nums[i].
Constraint: 0 <= nums[i] <= 100.

### Examples

Input: [8,1,2,2,3] → Output: [4,0,1,1,3]
Input: [6,5,4,8]   → Output: [2,1,0,3]
Input: [7,7,7,7]   → Output: [0,0,0,0]

### Approach 1 — Brute Force O(n²)

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for current_number in nums:
            how_many_are_smaller = 0
            for other_number in nums:
                if other_number < current_number:
                    how_many_are_smaller += 1
            result.append(how_many_are_smaller)
        return result
```

Note: no j != i check needed — a number equal to itself does not satisfy <.

### Approach 2 — Prefix Sum on Frequency Array O(n)

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: count occurrences of each value 0-100
        freq = [0] * 101
        for num in nums:
            freq[num] += 1

        # Step 2: prefix sum so freq[i] = count of numbers <= i
        for i in range(1, 101):
            freq[i] += freq[i - 1]

        # Step 3: freq[num-1] = count of numbers < num
        result = []
        for num in nums:
            smaller_count = freq[num - 1] if num > 0 else 0
            result.append(smaller_count)
        return result
```

Walkthrough on [8,1,2,2,3]:
- After freq count:  freq[1]=1, freq[2]=2, freq[3]=1, freq[8]=1
- After prefix sum:  freq[0]=0, freq[1]=1, freq[2]=3, freq[3]=4, freq[8]=5
- Lookups: 8→freq[7]=4 ✓, 1→freq[0]=0 ✓, 2→freq[1]=1 ✓, 3→freq[2]=3 ✓

Complexity: Time O(n), Space O(1) (fixed 101-element array).

### Approach 3 — Sort + Index trick O(n log n)

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]
```

.index() returns the first occurrence — for duplicates this is correct because everything
before the first occurrence in the sorted list is strictly smaller.

Complexity: Time O(n log n), Space O(n).

---

## Problem 2 — Find All Numbers Disappeared in an Array (LeetCode 448)

Given nums of length n where all values in [1,n], return all values in [1,n] not in nums.

### Examples

Input: [4,3,2,7,8,2,3,1] → Output: [5,6]
Input: [1,1]             → Output: [2]

### Solution — Set Difference

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_set = set(range(1, len(nums) + 1))
        present  = set(nums)
        missing  = full_set - present
        return list(missing)

# One-liner equivalent
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
```

Walkthrough on [4,3,2,7,8,2,3,1]:
- full_set = {1,2,3,4,5,6,7,8}
- present  = {1,2,3,4,7,8}
- missing  = {5,6} ✓

Complexity: Time O(n), Space O(n).
