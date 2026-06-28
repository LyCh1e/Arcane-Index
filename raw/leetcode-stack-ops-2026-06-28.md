---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 1441 — Build an Array With Stack Operations"
language: Python
difficulty: Easy
---

# LeetCode 1441 — Build an Array With Stack Operations

Given a strictly increasing integer array `target` and integer `n`, return the sequence
of "Push" / "Pop" stack operations to build target by reading from the stream [1, n].

Rules:
- Pick the next integer from the stream and Push it.
- Optionally Pop immediately if it is unwanted.
- Stop as soon as the stack equals target.

## Examples

Input: target = [1,3], n = 3  → Output: ["Push","Push","Pop","Push"]
Input: target = [1,2,3], n = 3 → Output: ["Push","Push","Push"]
Input: target = [1,2], n = 4  → Output: ["Push","Push"]

## Solution

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_set = set(target)

        for number in range(1, n + 1):
            # Stop early once we've built the full target
            if not target_set:
                break

            if number in target_set:
                # We want this number — push and keep it
                operations.append("Push")
                target_set.remove(number)
            else:
                # We don't want this number — push then immediately pop it
                operations.append("Push")
                operations.append("Pop")

        return operations
```

Walkthrough on target=[1,3], n=3:
- number=1: in target_set → ["Push"], target_set={3}
- number=2: not in set   → ["Push","Push","Pop"], target_set={3}
- number=3: in target_set → ["Push","Push","Pop","Push"], target_set={}
- target_set empty → break

Output: ["Push","Push","Pop","Push"] ✓

Complexity: Time O(n), Space O(|target|) for the set (O(1) extra beyond output).
