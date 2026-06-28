---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 3 — Longest Substring Without Repeating Characters"
language: Python
difficulty: Medium
---

# LeetCode 3 — Longest Substring Without Repeating Characters

Find the length of the longest substring of s that contains no repeating characters.

## Examples

"abcabcbb" → 3 ("abc")
"bbbbb"    → 1 ("b")
"pwwkew"   → 3 ("wke")

## Approach 1 — Brute Force O(N²)

Generate every starting point i, expand j, break on duplicate.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                res = max(res, j - i + 1)
        return res
```

## Approach 2 — Sliding Window with Set O(N)

Two pointers left/right. Expand right; when duplicate found, shrink left one step at a time
until the window is valid again.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res
```

Each character is visited at most twice (once by right, once by left). O(N) total.

## Approach 3 — Optimised Sliding Window with Last-Index Map O(N)

Instead of shrinking left one step at a time, jump directly to last_seen[char] + 1.
max() guard prevents moving left backward when the duplicate is outside the current window.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}   # char → last index where it appeared
        start = 0
        res = 0
        for end, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            res = max(res, end - start + 1)
            last_seen[char] = end
        return res
```

The `and last_seen[char] >= start` guard ensures we only jump if the previous
occurrence is inside the current window. Single pass, no inner loop.

Complexity summary:
Approach    Time    Space
Brute force O(N²)   O(M)
Sliding window O(N) O(M)
Optimised SW O(N)   O(M)
M = character set size (128 for ASCII); effectively O(1) space since M is fixed.
