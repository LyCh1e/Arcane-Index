---
type: source
address: c-000080
title: "LeetCode 1365 & 448 — Count Smaller / Find Disappeared"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-count-missing-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, arrays, prefix-sum, set-difference, computer-science]
---

# LeetCode 1365 & 448 — Count Smaller / Find Disappeared

Two Easy-tier problems that introduce two new patterns to the wiki.

| Problem | Title | Pattern |
|---------|-------|---------|
| 1365 | How Many Numbers Are Smaller Than the Current Number | Prefix sum on frequency array |
| 448 | Find All Numbers Disappeared in an Array | Set difference |

## Key Takeaways

- **Prefix sum on a bounded frequency array**: when values are constrained to a small fixed range (here 0–100), build a freq array of that size and convert it to a prefix sum in O(range) time. `freq[i]` then gives "how many values ≤ i" in O(1). Lookup for "how many values < x" is simply `freq[x-1]`. This trades O(n) dict/sort overhead for a fixed-size O(1) space structure.
- **Sort + index trick**: `sorted_list.index(val)` returns the first position of `val`, which equals the count of elements strictly less than it. Elegant but O(n log n); inferior to the prefix sum when the value range is bounded.
- **Set difference** (`set(A) - set(B)`) finds elements present in A but absent in B in O(|A| + |B|) time. The idiom `set(range(1, n+1)) - set(nums)` is the natural expression for "which values in the expected range are missing?"
- LeetCode 1365 does **not** require the `j != i` guard in the brute force — a value equal to itself fails the strict `<` check automatically.

## Related Concepts

- [[concepts/array-manipulation-patterns]] — Pattern 7 (Prefix Sum on Frequency Array) and Pattern 8 (Set Difference) added from this ingest

## Related Examples

- [[examples/leetcode-count-missing-python]] — annotated solutions with traces
- [[examples/leetcode-set-mismatch-python]] — earlier frequency-count pattern (Pattern 4)
- [[examples/leetcode-array-basics-python]] — earlier array patterns (1–3)
