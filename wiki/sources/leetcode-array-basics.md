---
type: source
address: c-000075
title: "LeetCode Array Basics (1929, 1470, 485)"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-array-basics-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, arrays, computer-science]
---

# LeetCode Array Basics

Three Easy-tier LeetCode problems demonstrating fundamental array manipulation patterns in Python.

| Problem | Title | Pattern |
|---------|-------|---------|
| 1929 | Concatenation of Array | List concatenation / dual-index write |
| 1470 | Shuffle the Array | Split-midpoint interleaving |
| 485 | Max Consecutive Ones | Linear scan with running counter |

## Key Takeaways

- **Python list `+`** creates a new list — it does not modify either operand. `nums + nums` is O(n) time and O(n) space.
- **Index arithmetic** (`i` and `i + n`) is the canonical way to interleave two logical halves of a single array without slicing.
- **Running counter with reset** is the minimal sliding-window pattern: increment on match, zero on miss, update max inside the match branch.
- All three problems are O(n) time and O(1) extra space (output not counted).

## Related Concepts

- [[concepts/array-manipulation-patterns]] — full pattern catalogue
- [[concepts/algorithm-complexity]] — Big-O analysis applied here
- [[concepts/data-structures-fundamentals]] — arrays as a foundational structure

## Related Examples

- [[examples/leetcode-array-basics-python]] — working Python solutions with annotations
