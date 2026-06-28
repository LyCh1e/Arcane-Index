---
type: concept
address: c-000089
title: "Linked List Patterns"
domain: computer-science
complexity: medium
created: 2026-06-28
updated: 2026-06-28
tags: [concept, linked-list, algorithms, python, computer-science]
related:
  - concepts/data-structures-fundamentals
  - concepts/algorithm-complexity
  - concepts/simulation-patterns
---

# Linked List Patterns

Recurring patterns for traversing, constructing, and manipulating singly linked lists. Linked lists lack random access — every operation is sequential — so the patterns here are built around pointer manipulation rather than index arithmetic.

**Python `ListNode` definition** (used across LeetCode):

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next
```

---

## Pattern 1 — Dummy Head Node

**Problem shape**: build a new linked list node by node. The first node has no predecessor to attach to.

**Without dummy** — requires a special case:

```python
result = None
for ...:
    node = ListNode(digit)
    if result is None:          # special case: first node
        result = node
        current = result
    else:
        current.next = node     # normal case
        current = current.next
```

**With dummy** — uniform code throughout:

```python
dummy   = ListNode(0)           # sentinel; its val is never used
current = dummy

for ...:
    current.next = ListNode(digit)   # identical for every node including the first
    current = current.next

return dummy.next               # skip the sentinel, return the real list
```

**Why it works**: `dummy` is a pre-existing node, so `current.next =` is always a valid assignment. The sentinel's value is irrelevant — it exists solely to give `current` somewhere to live before the first real node is created.

**When to use**: any time you are constructing a linked list from scratch inside a loop.

**LeetCode**: 2 — Add Two Numbers; 21 — Merge Two Sorted Lists; 23 — Merge k Sorted Lists; 206 — Reverse Linked List (variant).

---

## Pattern 2 — Simultaneous Traversal with Carry

**Problem shape**: traverse two lists of potentially different lengths in lockstep, combining values at each position with a carry that propagates to the next position. Continue until both lists and the carry are all exhausted.

```python
carry = 0

while l1 is not None or l2 is not None or carry != 0:

    # Safely read from each list; default to 0 if exhausted
    digit1 = l1.val if l1 is not None else 0
    digit2 = l2.val if l2 is not None else 0

    total  = digit1 + digit2 + carry
    carry  = total // 10          # 1 if total >= 10, else 0
    digit  = total % 10           # ones-place digit to store

    # Attach digit to output (pair with Pattern 1 — Dummy Head)
    current.next = ListNode(digit)
    current = current.next

    # Advance each pointer only if that list has more nodes
    if l1 is not None: l1 = l1.next
    if l2 is not None: l2 = l2.next
```

**Three critical details**:

| Detail | Why it matters |
|--------|---------------|
| `or carry != 0` in the while condition | A final carry (e.g. 9+9=18) needs its own node after both lists are exhausted |
| `digit1 = l1.val if l1 else 0` | Treats an exhausted list as an infinite stream of zeros — no branching needed |
| `carry = total // 10` | Integer division always produces 0 or 1 for single-digit inputs; generalises to multi-digit with no changes |

**Why digits-in-reverse-order is convenient**: LSB-first storage means the head of each list is the ones digit — exactly where grade-school addition starts. No reversal step needed before or after.

**Complexity**: O(max(m, n)) time, O(max(m, n)) space for the output list.

**LeetCode**: 2 — Add Two Numbers; 445 — Add Two Numbers II (MSB-first variant, requires reversal or a stack).

---

## Pattern 3 — Fast and Slow Pointer (Placeholder)

*To be filled when the first cycle-detection or middle-finding problem is ingested.*

Common shapes:
- **Cycle detection**: fast pointer moves 2 steps, slow moves 1. If they meet, a cycle exists (Floyd's algorithm).
- **Middle of list**: when fast reaches the end, slow is at the middle.
- **nth from end**: advance fast by n steps first, then move both until fast hits the end.

**LeetCode**: 141 — Linked List Cycle; 876 — Middle of the Linked List; 19 — Remove nth Node From End.

---

## Pattern 4 — In-Place Reversal (Placeholder)

*To be filled when the first reversal problem is ingested.*

Common shape: reverse a linked list or a segment of one using three pointers (`prev`, `curr`, `next_node`).

**LeetCode**: 206 — Reverse Linked List; 92 — Reverse Linked List II; 25 — Reverse Nodes in k-Group.

---

## General Principles

### Always check `None` before dereferencing

```python
# Will crash if l1 is None
val = l1.val

# Safe
val = l1.val if l1 is not None else 0
```

### Draw the pointer state at each step

Linked list bugs are almost always pointer ordering bugs — e.g. overwriting `curr.next` before saving `curr.next.next`. Draw boxes and arrows for at least one example before coding.

### The dummy node is almost always worth it

The three extra lines (create dummy, set `current = dummy`, return `dummy.next`) eliminate an entire class of first-node bugs. Use it by default for list construction.

---

## Complexity Summary

| Pattern | Time | Space |
|---------|------|-------|
| Dummy head construction | O(n) | O(n) output |
| Simultaneous traversal with carry | O(max(m, n)) | O(max(m, n)) output |
| Fast/slow pointer | O(n) | O(1) |
| In-place reversal | O(n) | O(1) |

---

## See Also

- [[concepts/data-structures-fundamentals]] — linked list memory model, singly vs doubly linked
- [[concepts/algorithm-complexity]] — Big-O for pointer traversal
- [[examples/leetcode-add-two-numbers-python]] — worked examples for Patterns 1 and 2
