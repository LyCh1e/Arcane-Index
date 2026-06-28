---
type: example
address: c-000093
title: "LeetCode 3 — Longest Substring Without Repeating Characters (Python)"
domain: computer-science
source: "[[sources/leetcode-longest-substring]]"
concepts:
  - "[[concepts/sliding-window-patterns]]"
  - "[[concepts/algorithm-complexity]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, sliding-window, two-pointers, strings, computer-science]
---

# LeetCode 3 — Longest Substring Without Repeating Characters

> Find the length of the longest substring of `s` that contains no repeating characters.

**Patterns**: [[concepts/sliding-window-patterns#Pattern 1 — Variable-Size Window: Shrink-Left with Set|Shrink-Left Sliding Window]] · [[concepts/sliding-window-patterns#Pattern 2 — Variable-Size Window: Jump-Left with Last-Index Map|Jump-Left Sliding Window]]

---

## Approach 1 — Brute Force (Baseline)

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n   = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break           # duplicate found — this start point is exhausted
                seen.add(s[j])
                res = max(res, j - i + 1)
        return res
```

O(N²) time — recomputes overlapping substrings from scratch at every starting index. Useful as a reference implementation to verify the faster approaches.

---

## Approach 2 — Sliding Window with Set

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen  = set()
        left  = 0
        res   = 0

        for right in range(len(s)):
            # Restore window validity: shrink from the left until s[right] is unique
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Window [left, right] is now valid — add the new character
            seen.add(s[right])
            res = max(res, right - left + 1)

        return res
```

### Why O(N) and not O(N²)?

The `while` loop looks like it makes this quadratic, but `left` only ever moves **forward**. Across the entire execution, `left` advances at most N times in total. Combined with `right` advancing N times, the total operations are ≤ 2N → **O(N)**.

### Trace on `"pwwkew"`

| right | s[right] | seen before | while fires? | left after | seen after | res |
|-------|----------|-------------|-------------|------------|-----------|-----|
| 0 | p | {} | No | 0 | {p} | 1 |
| 1 | w | {p} | No | 0 | {p,w} | 2 |
| 2 | w | {p,w} | **Yes** — remove p(0),w(1)… | 2 | {} → {w} | 2 |
| 3 | k | {w} | No | 2 | {w,k} | 2 |
| 4 | e | {w,k} | No | 2 | {w,k,e} | **3** |
| 5 | w | {w,k,e} | **Yes** — remove w(2) | 3 | {k,e} → {k,e,w} | 3 |

Return **3** ✓

---

## Approach 3 — Optimised Sliding Window (Last-Index Map)

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}   # char → most recent index it appeared at
        start     = 0
        res       = 0

        for end, char in enumerate(s):
            # Jump start only if the duplicate is INSIDE the current window
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1

            res = max(res, end - start + 1)
            last_seen[char] = end   # update to latest occurrence

        return res
```

### The `>= start` guard — why it is essential

```
s = "a b b a"
     0 1 2 3

Processing end=3, char='a':
  last_seen['a'] = 0
  Is 0 >= start (which is 2 after handling the second 'b')? → NO
  → Do NOT jump. The 'a' at index 0 is outside the current window [2,3].
  → Without the guard: start would jump to 1, giving window [1,3] = "bba" — invalid!
```

### Trace on `"pwwkew"`

| end | char | last_seen before | `>= start`? | start after | res | last_seen after |
|-----|------|-----------------|------------|------------|-----|----------------|
| 0 | p | {} | — | 0 | 1 | {p:0} |
| 1 | w | {p:0} | — | 0 | 2 | {p:0,w:1} |
| 2 | w | {p:0,w:1} | 1≥0 ✓ | **2** | 2 | {p:0,w:2} |
| 3 | k | {p:0,w:2} | — | 2 | 2 | {…,k:3} |
| 4 | e | {…,k:3} | — | 2 | **3** | {…,e:4} |
| 5 | w | {…,w:2} | 2≥2 ✓ | **3** | 3 | {…,w:5} |

Return **3** ✓ — identical result; no inner loop, one dict lookup per character.

---

## Approach Comparison

| | Brute Force | Sliding Window | Optimised SW |
|--|-------------|---------------|--------------|
| **Time** | O(N²) | O(N) | O(N) |
| **Space** | O(M) | O(M) | O(M) |
| **Inner loop** | `for j` | `while s[right] in seen` | None |
| **Start jump** | Reset to i+1 | One step left | Direct to `last_seen[char]+1` |
| **Clarity** | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| **Write first?** | ✓ reference | ✓ default | Only if perf critical |

M = character set size; O(1) in practice for fixed alphabets.

---

## Related Problems

| LeetCode | Relation |
|----------|----------|
| 904 — Fruit Into Baskets | Sliding window, at-most-2-distinct values |
| 76 — Minimum Window Substring | Sliding window, minimum valid window (harder) |
| 1004 — Max Consecutive Ones III | Pattern 3 + k-flip, related to running counter |
| 340 — Longest Substring ≤ K Distinct | Generalised Pattern 4 placeholder in [[concepts/sliding-window-patterns]] |
