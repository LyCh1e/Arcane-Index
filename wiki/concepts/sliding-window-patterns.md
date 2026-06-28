---
type: concept
address: c-000092
title: "Sliding Window Patterns"
domain: computer-science
complexity: medium
created: 2026-06-28
updated: 2026-06-28
tags: [concept, sliding-window, two-pointers, strings, arrays, algorithms, computer-science]
related:
  - concepts/array-manipulation-patterns
  - concepts/algorithm-complexity
  - concepts/greedy-patterns
---

# Sliding Window Patterns

The sliding window technique maintains a contiguous subarray or substring `[left, right]` and slides it across the input to find the optimum window satisfying a constraint. It eliminates the O(N²) cost of checking every possible window by reusing work from the previous step.

**Core invariant**: at all times, the window `[left, right]` satisfies the problem's validity constraint. When adding `s[right]` would violate it, advance `left` until the window is valid again.

**When to reach for sliding window**:
- "Longest/shortest subarray/substring with property X"
- "Maximum/minimum sum of subarray of size k"
- "Number of subarrays satisfying condition X"
- The constraint is a function only of the *contents* of the current window, not its position

---

## Pattern 1 — Variable-Size Window: Shrink-Left with Set

**Problem shape**: find the longest window in which all elements are unique (or satisfy some "no duplicates" constraint). Shrink from the left one step at a time until valid.

```python
seen  = set()
left  = 0
res   = 0

for right in range(len(s)):
    # Shrink from the left until s[right] is no longer a duplicate
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    # Window [left, right] is now valid
    seen.add(s[right])
    res = max(res, right - left + 1)

return res
```

**Complexity analysis**: `right` advances N times total. `left` also advances at most N times total across the entire loop (it never moves backward). Therefore the total number of operations is at most 2N → **O(N) time**. Space is O(M) for the set, where M is the character/value domain size.

**Key detail**: the `while` inner loop looks like O(N²), but the amortised cost is O(1) per step of `right` because `left` can only advance N times in total.

**LeetCode**: 3 — Longest Substring Without Repeating Characters; 904 — Fruit Into Baskets (at most 2 distinct values).

---

## Pattern 2 — Variable-Size Window: Jump-Left with Last-Index Map

**Problem shape**: same as Pattern 1, but instead of shrinking one step at a time, jump `left` directly to the position after the last occurrence of the duplicate. Requires knowing *where* each element last appeared.

```python
last_seen = {}   # element → most recent index it was seen at
start     = 0
res       = 0

for end, char in enumerate(s):
    # Jump start only if the previous occurrence is INSIDE the current window
    if char in last_seen and last_seen[char] >= start:
        start = last_seen[char] + 1

    res = max(res, end - start + 1)
    last_seen[char] = end   # always update to the latest index

return res
```

**Why `last_seen[char] >= start` matters**:

```
s = "abba"

After processing index 1 (char='b'):  last_seen = {a:0, b:1}, start=0
At index 2 (char='b'):
  last_seen['b'] = 1, which is >= start(0) → jump start to 2  ✓

After processing index 2 (char='b'):  last_seen = {a:0, b:2}, start=2
At index 3 (char='a'):
  last_seen['a'] = 0, which is < start(2) → do NOT jump (that 'a' is outside our window)
  Without the guard: start would jump back to 1, widening the window — wrong.  ✗
```

**Advantage over Pattern 1**: a single O(1) dict lookup and integer update per character instead of a potentially multi-step `while` shrink. Same asymptotic complexity, significantly fewer operations in practice.

**LeetCode**: 3 — Longest Substring Without Repeating Characters (optimised); 76 — Minimum Window Substring (variant).

---

## Pattern 3 — Fixed-Size Window (Placeholder)

*To be filled when the first fixed-window problem is ingested.*

**Problem shape**: compute a metric (sum, max, count) over every contiguous subarray of exactly size k. Slide the window by adding `s[right]` and removing `s[right - k]` at each step.

```python
# Skeleton
window_sum = sum(nums[:k])
res = window_sum
for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]
    res = max(res, window_sum)
return res
```

**LeetCode**: 643 — Maximum Average Subarray I; 1456 — Maximum Number of Vowels in a Substring of Given Length.

---

## Pattern 4 — At-Most-K Window (Placeholder)

*To be filled when the first "at most k distinct elements" problem is ingested.*

**Problem shape**: find the longest subarray/substring with at most k distinct values. Shrink left when the count of distinct values exceeds k.

**LeetCode**: 340 — Longest Substring with At Most K Distinct Characters; 992 — Subarrays with K Different Integers.

---

## General Principles

### Choosing between Pattern 1 and Pattern 2

| Criterion | Pattern 1 (shrink-left) | Pattern 2 (jump-left) |
|-----------|------------------------|----------------------|
| Implementation simplicity | ★★★★★ | ★★★☆☆ |
| Runtime in practice | Slower (repeated removals) | Faster (one dict lookup) |
| Handles "outside-window" duplicates | Naturally (while loop just doesn't fire) | Requires `>= start` guard |
| When to use | First attempt, interviews, clarity | When performance matters |

### The window validity invariant

Every sliding window solution maintains an invariant: the window `[left, right]` is always valid *after* the loop body completes. The shrink step (while loop or jump) restores validity before updating the result. Violating this ordering is the most common sliding window bug.

### Updating `res` *after* restoring validity

```python
# Correct — window is valid before we measure it
while invalid:
    shrink_left()
update_result()

# Wrong — measuring an invalid window
update_result()
while invalid:
    shrink_left()
```

---

## Complexity Summary

| Pattern | Time | Extra Space |
|---------|------|-------------|
| Variable window — shrink-left (set) | O(N) | O(M) |
| Variable window — jump-left (map) | O(N) | O(M) |
| Fixed window | O(N) | O(1) |
| At-most-k window | O(N) | O(k) |

M = character/value domain size; O(1) when domain is a fixed constant (e.g. ASCII 128).

---

## See Also

- [[concepts/array-manipulation-patterns]] — linear scan patterns; Pattern 3 (running counter) is the conceptual precursor to sliding window
- [[concepts/algorithm-complexity]] — amortised analysis of the two-pointer advance
- [[concepts/greedy-patterns]] — greedy choice at each window step
- [[examples/leetcode-longest-substring-python]] — worked examples for Patterns 1 and 2
