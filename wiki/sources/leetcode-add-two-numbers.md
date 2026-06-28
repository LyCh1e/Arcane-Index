---
type: source
address: c-000088
title: "LeetCode 2 — Add Two Numbers"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-add-two-numbers-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, linked-list, carry, computer-science]
---

# LeetCode 2 — Add Two Numbers

Medium-tier linked list problem. First LeetCode problem in the wiki to use a linked list — establishes the new [[concepts/linked-list-patterns]] concept page.

| Aspect | Detail |
|--------|--------|
| Pattern | Simultaneous traversal with carry propagation |
| Sub-pattern | Dummy head node |
| Input format | Digits stored in reverse order (LSB first) |

## Key Takeaways

- **Dummy head node**: create `ListNode(0)` as a sentinel before the loop. Every digit — including the first — attaches via `current.next = ListNode(digit)`. Without it, you need an `if result is None` special case on the first iteration. Return `dummy.next` to skip the sentinel.
- **Simultaneous traversal**: `while l1 or l2 or carry` is the canonical loop condition for traversing two lists of unequal length. Default the exhausted list's digit to 0 (`l1.val if l1 else 0`) rather than branching.
- **Carry persistence**: continue the loop even after both lists are exhausted if `carry != 0`. Adding `[9,9,9]` + `[1]` produces a carry on the last step that needs its own node; forgetting this silently truncates the result.
- **Reverse order is a gift**: digits are stored LSB-first, so the first nodes are the least significant digits — exactly the order we process them in grade-school addition. No reversal needed.

## Related Concepts

- [[concepts/linked-list-patterns]] — Pattern 1 (Dummy Head Node) and Pattern 2 (Simultaneous Traversal with Carry) introduced by this problem
- [[concepts/data-structures-fundamentals]] — linked list memory model; singly linked list traversal

## Related Examples

- [[examples/leetcode-add-two-numbers-python]] — annotated solution with full digit-by-digit trace
