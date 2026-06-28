---
type: example
address: c-000084
title: "LeetCode 1441 — Build an Array With Stack Operations (Python)"
domain: computer-science
source: "[[sources/leetcode-stack-ops]]"
concepts:
  - "[[concepts/simulation-patterns]]"
  - "[[concepts/data-structures-fundamentals]]"
  - "[[concepts/algorithm-complexity]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, stack, simulation, greedy, computer-science]
---

# LeetCode 1441 — Build an Array With Stack Operations

> Given a strictly increasing `target` and integer `n`, return the "Push"/"Pop" operation sequence that builds `target` by reading from the stream `[1, n]`.

**Pattern**: [[concepts/simulation-patterns#Pattern 1 — Greedy Stream Simulation with Early Exit|Greedy Stream Simulation with Early Exit]]

---

## Solution

```python
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_set = set(target)          # O(1) membership; convert once

        for number in range(1, n + 1):
            if not target_set:            # all target elements matched — stop
                break

            if number in target_set:
                operations.append("Push") # keep this number
                target_set.remove(number) # mark as satisfied
            else:
                operations.append("Push") # must read from stream …
                operations.append("Pop")  # … then immediately discard

        return operations
```

---

## Why Each Design Decision Matters

**`set(target)` not `target` directly**

```python
# Slow — O(|target|) per check, O(n × |target|) total
if number in target:

# Fast — O(1) per check, O(n) total
target_set = set(target)
if number in target_set:
```

For this problem's constraints (target ≤ 100 elements, n ≤ 100) the difference is unmeasurable. The pattern still matters: any time you repeatedly test membership against a fixed collection, convert to a set first.

**`target_set.remove(number)` enables the clean exit guard**

Removing matched elements means `not target_set` evaluates to `True` the moment the last element is found. Without this, you would need a separate counter or index to track progress.

**Push-Pop is mandatory, not optional**

The problem states you must read the next integer from the stream (Push) before you can discard it (Pop). You cannot simply skip a number. Every stream element that is not in target **must** generate a Push-Pop pair, not nothing.

---

## Full Trace — `target = [1, 3]`, `n = 3`

| number | in target_set? | operations appended | target_set after |
|--------|---------------|--------------------|--------------------|
| 1 | ✅ Yes | `["Push"]` | `{3}` |
| 2 | ❌ No | `["Push", "Push", "Pop"]` | `{3}` |
| 3 | ✅ Yes | `["Push", "Push", "Pop", "Push"]` | `{}` |
| — | `target_set` empty → break | | |

Output: `["Push", "Push", "Pop", "Push"]` ✓

---

## Full Trace — `target = [1, 2, 3]`, `n = 3`

| number | in target_set? | operations appended | target_set after |
|--------|---------------|--------------------|--------------------|
| 1 | ✅ Yes | `["Push"]` | `{2, 3}` |
| 2 | ✅ Yes | `["Push", "Push"]` | `{3}` |
| 3 | ✅ Yes | `["Push", "Push", "Push"]` | `{}` |
| — | `target_set` empty → break | | |

Output: `["Push", "Push", "Push"]` ✓

---

## Full Trace — `target = [1, 2]`, `n = 4`

| number | in target_set? | operations appended | target_set after |
|--------|---------------|--------------------|--------------------|
| 1 | ✅ Yes | `["Push"]` | `{2}` |
| 2 | ✅ Yes | `["Push", "Push"]` | `{}` |
| — | `target_set` empty → break | | |

Output: `["Push", "Push"]` ✓

Numbers 3 and 4 are never read from the stream — the early exit fires at `number = 2`.

---

## Complexity

| Dimension | Value | Reason |
|-----------|-------|--------|
| Time | O(n) | One pass through the stream, at most |
| Space | O(\|target\|) | The set; output array not counted |
| Practical bound | O(max(target)) | Loop always exits at `target[-1]`; n only matters if no early exit |

---

## Related Problems

| LeetCode | Relation |
|----------|----------|
| 1700 — Number of Students Unable to Eat Lunch | Stream + stack simulation; sandwiches consumed in order |
| 946 — Validate Stack Sequences | Verify a push/pop sequence is valid for a given input |
| 232 — Implement Queue Using Stacks | Stack-as-structure rather than stack-as-process |
