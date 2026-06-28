---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 1946 — Maximum Element After Decreasing and Rearranging"
language: Python
difficulty: Medium
---

# LeetCode 1946 — Maximum Element After Decreasing and Rearranging

Operations allowed (any number of times):
- Decrease any element to a smaller positive integer.
- Rearrange elements in any order.

Constraints after operations:
- arr[0] must be 1.
- abs(arr[i] - arr[i-1]) <= 1 for all adjacent pairs.

Return the maximum possible value of any element.

## Examples

Input: [2,2,1,2,1] → Output: 2
Input: [100,1,1000] → Output: 3
Input: [1,2,3,4,5]  → Output: 5

## Solution

```python
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]
```

Walkthrough on [100, 1, 1000]:
- After sort: [1, 100, 1000]
- arr[0] = 1
- arr[1] = min(100, 1+1) = 2
- arr[2] = min(1000, 2+1) = 3
- Return 3 ✓

Walkthrough on [2,2,1,2,1]:
- After sort: [1,1,2,2,2]
- arr[0] = 1
- arr[1] = min(1, 1+1) = 1
- arr[2] = min(2, 1+1) = 2
- arr[3] = min(2, 2+1) = 2
- arr[4] = min(2, 2+1) = 2
- Return 2 ✓

Why sorting works: we want to build up as steadily as possible. Sorting ensures every element
is >= its predecessor, giving the best chance to increment by 1 at each step.

Complexity: Time O(n log n) — sort dominates. Space O(1) — modified in place.
