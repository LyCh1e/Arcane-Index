---
type: example
address: c-000090
title: "LeetCode 2 — Add Two Numbers (Python)"
domain: computer-science
source: "[[sources/leetcode-add-two-numbers]]"
concepts:
  - "[[concepts/linked-list-patterns]]"
  - "[[concepts/data-structures-fundamentals]]"
  - "[[concepts/algorithm-complexity]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, linked-list, carry, computer-science]
---

# LeetCode 2 — Add Two Numbers

> Two linked lists store non-negative integers in **reverse order** (LSB first). Return their sum as a linked list in the same format.

**Patterns**: [[concepts/linked-list-patterns#Pattern 1 — Dummy Head Node|Dummy Head Node]] · [[concepts/linked-list-patterns#Pattern 2 — Simultaneous Traversal with Carry|Simultaneous Traversal with Carry]]

---

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result_head  = ListNode(0)   # dummy sentinel — skip at the end
        current_node = result_head
        carry        = 0

        # Continue while either list has digits remaining, or there is a leftover carry
        while l1 is not None or l2 is not None or carry != 0:

            # Read current digit from each list; use 0 if that list is exhausted
            top_digit_of_l1 = l1.val if l1 is not None else 0
            top_digit_of_l2 = l2.val if l2 is not None else 0

            # Grade-school column addition
            column_sum     = top_digit_of_l1 + top_digit_of_l2 + carry
            carry          = column_sum // 10   # 1 if sum >= 10, else 0
            digit_to_store = column_sum % 10    # ones-place only

            # Attach digit and advance the output pointer
            current_node.next = ListNode(digit_to_store)
            current_node = current_node.next

            # Advance each input pointer (only if not exhausted)
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        return result_head.next   # skip the dummy sentinel
```

---

## Design Decisions

### Why a dummy head node?

```python
# Without dummy: first node needs a special case
result = None
...
if result is None:
    result = ListNode(digit)
    current = result
else:
    current.next = ListNode(digit)
    current = current.next

# With dummy: every node is identical
result_head = ListNode(0)
current = result_head
...
current.next = ListNode(digit)   # same code for every iteration
current = current.next
```

The dummy node trades 3 lines of setup for the elimination of an entire conditional branch. It is the single most common linked-list construction technique.

### Why `or carry != 0` in the loop condition?

Without it, a carry produced on the very last digit pair is silently dropped:

```
l1 = [9, 9]  →  99
l2 = [1]     →   1
Expected sum →  100  →  [0, 0, 1]

Without carry check: loop exits after 2 steps → result is [0, 0]  ✗
With carry check:    loop runs a 3rd time    → result is [0, 0, 1] ✓
```

### Why `l1.val if l1 is not None else 0`?

This models an exhausted list as an infinite stream of leading zeros — the same mathematical identity used in grade-school addition when one number has fewer digits. One expression, no branching.

---

## Trace — `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]` (342 + 465 = 807)

| Step | digit1 | digit2 | carry in | column_sum | digit stored | carry out |
|------|--------|--------|----------|-----------|--------------|-----------|
| 1 | 2 | 5 | 0 | 7 | **7** | 0 |
| 2 | 4 | 6 | 0 | 10 | **0** | 1 |
| 3 | 3 | 4 | 1 | 8 | **8** | 0 |
| — | — | — | carry=0, both lists exhausted → stop | | | |

Result list: `[7, 0, 8]` → represents **807** ✓

---

## Trace — `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`

9,999,999 + 9,999 = 10,009,998 → stored as `[8,9,9,9,0,0,0,1]`

| Step | digit1 | digit2 | carry in | column_sum | digit | carry out |
|------|--------|--------|----------|-----------|-------|-----------|
| 1 | 9 | 9 | 0 | 18 | **8** | 1 |
| 2 | 9 | 9 | 1 | 19 | **9** | 1 |
| 3 | 9 | 9 | 1 | 19 | **9** | 1 |
| 4 | 9 | 9 | 1 | 19 | **9** | 1 |
| 5 | 9 | 0 | 1 | 10 | **0** | 1 |
| 6 | 9 | 0 | 1 | 10 | **0** | 1 |
| 7 | 9 | 0 | 1 | 10 | **0** | 1 |
| 8 | 0 | 0 | 1 | 1  | **1** | 0 |

l2 exhausted after step 4; steps 5–7 use `digit2 = 0`. Step 8 runs because `carry = 1` — the `or carry != 0` guard keeps the loop alive for this final node.

Result list: `[8,9,9,9,0,0,0,1]` ✓

---

## Complexity

| Dimension | Value | Reason |
|-----------|-------|--------|
| Time | O(max(m, n)) | One pass; each node visited exactly once |
| Space | O(max(m, n)) | Output list; +1 node if final carry |

---

## Related Problems

| LeetCode | Relation |
|----------|----------|
| 445 — Add Two Numbers II | Same problem but MSB-first; requires stack or reversal before addition |
| 21 — Merge Two Sorted Lists | Simultaneous traversal without carry; dummy head essential |
| 206 — Reverse Linked List | Foundation for 445; in-place reversal pattern |
| 141 — Linked List Cycle | Fast/slow pointer pattern (Pattern 3 in [[concepts/linked-list-patterns]]) |
