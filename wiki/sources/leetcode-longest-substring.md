---
type: source
address: c-000091
title: "LeetCode 3 — Longest Substring Without Repeating Characters"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-longest-substring-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, sliding-window, two-pointers, strings, computer-science]
---

# LeetCode 3 — Longest Substring Without Repeating Characters

Classic Medium problem. Introduces the **Sliding Window** paradigm and establishes the new [[concepts/sliding-window-patterns]] concept page. Three approaches in ascending order of sophistication.

| Approach | Time | Space | Technique |
|----------|------|-------|-----------|
| Brute force | O(N²) | O(M) | All substrings from every start |
| Sliding window | O(N) | O(M) | Two pointers, shrink left one step |
| Optimised SW | O(N) | O(M) | Two pointers, jump left via last-index map |

## Key Takeaways

- **Sliding window** is the pattern for "longest/shortest subarray/substring satisfying a constraint": maintain a window `[left, right]`, expand right greedily, shrink left when the constraint is violated.
- **Set vs last-index map**: the set approach shrinks left one step at a time (simpler); the map approach jumps left in one step (faster in practice, same asymptotic). For this problem the map also handles the edge case where a duplicate is *outside* the current window — the `max(start, last_seen[char] + 1)` guard prevents a backward jump.
- **Space is effectively O(1)**: the set/dict is bounded by the character set size M (128 for ASCII, 26 for lowercase only), which is a fixed constant regardless of input length.
- **Brute force insight**: the nested loop formulation `seen = set(); for j in range(i, n)` is a clean reference implementation — useful to write first, then optimise away the outer loop with the sliding window.

## Related Concepts

- [[concepts/sliding-window-patterns]] — Pattern 1 (Shrink-Left Sliding Window) and Pattern 2 (Jump-Left Sliding Window) introduced by this problem

## Related Examples

- [[examples/leetcode-longest-substring-python]] — all three approaches with step traces
