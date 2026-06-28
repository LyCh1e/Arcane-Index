---
type: source
address: c-000078
title: "LeetCode 645 — Set Mismatch"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-set-mismatch-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, arrays, frequency-count, computer-science]
---

# LeetCode 645 — Set Mismatch

Single Easy-tier problem demonstrating two new array patterns not previously in the wiki: **frequency counting** and the **math sum identity**.

| Approach | Pattern | Space |
|----------|---------|-------|
| Manual dict | Frequency count | O(n) |
| `Counter` | Frequency count (stdlib) | O(n) |
| Math | Sum identity | O(1) |

## Key Takeaways

- **Frequency count** is the go-to pattern when the problem reduces to "how many times does each value appear?" Build a dict or array of counts in one pass, then scan the counts for anomalies in a second pass.
- **`dict.get(key, default)`** is cleaner than `if key in dict` when you need a fallback value — avoids a double lookup.
- **Math sum identity**: `sum(1..n) = n*(n+1)//2`. When one element is duplicated and one is missing, `sum(nums) - sum(set(nums))` yields the duplicate directly. This reduces space from O(n) to O(1) at the cost of readability.
- All three approaches are O(n) time.

## Related Concepts

- [[concepts/array-manipulation-patterns]] — Pattern 4 (Frequency Count) and Pattern 5 (Math Sum Identity) added from this ingest

## Related Examples

- [[examples/leetcode-set-mismatch-python]] — three annotated Python solutions
- [[examples/leetcode-array-basics-python]] — earlier array pattern examples (1929, 1470, 485)
