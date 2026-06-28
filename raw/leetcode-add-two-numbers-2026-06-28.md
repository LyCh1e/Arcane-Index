---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 2 — Add Two Numbers"
language: Python
difficulty: Medium
---

# LeetCode 2 — Add Two Numbers

Two non-empty linked lists store a non-negative integer in reverse order (least significant
digit first). Add them and return the sum as a linked list in the same reverse format.

## Examples

l1=[2,4,3], l2=[5,6,4]       → [7,0,8]       (342 + 465 = 807)
l1=[0],     l2=[0]            → [0]
l1=[9,9,9,9,9,9,9], l2=[9,9,9,9] → [8,9,9,9,0,0,0,1]

## Solution (readable version)

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result_head = ListNode(0)   # dummy sentinel — avoids special-casing first node
        current_node = result_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            top_digit_of_l1 = l1.val if l1 is not None else 0
            top_digit_of_l2 = l2.val if l2 is not None else 0

            column_sum    = top_digit_of_l1 + top_digit_of_l2 + carry
            carry         = column_sum // 10   # 1 if sum >= 10, else 0
            digit_to_store = column_sum % 10   # ones-place digit

            current_node.next = ListNode(digit_to_store)
            current_node = current_node.next

            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        return result_head.next   # skip the dummy sentinel
```

Walkthrough on [2,4,3] + [5,6,4]:
- Step 1: 2+5+0=7, carry=0, digit=7
- Step 2: 4+6+0=10, carry=1, digit=0
- Step 3: 3+4+1=8, carry=0, digit=8
- Loop ends (both lists exhausted, carry=0)
- Result: [7,0,8] → 807 ✓

Why dummy node: lets current_node.next = ListNode(digit) work identically for every
step including the first — no special case needed.

Why `or carry != 0` in the while condition: after both lists are exhausted, a leftover
carry (e.g. from [9,9]+[1]) still needs its own node.

Complexity: Time O(max(m,n)), Space O(max(m,n)) for the output list.
