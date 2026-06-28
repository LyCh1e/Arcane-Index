---
type: example
address: c-000095
title: "LeetCode 1768 — Merge Strings Alternately (Python)"
domain: computer-science
source: "[[sources/leetcode-merge-alternately]]"
concepts:
  - "[[concepts/array-manipulation-patterns]]"
created: 2026-06-28
updated: 2026-06-28
tags: [example, leetcode, python, two-pointers, strings, debugging, computer-science]
---

# LeetCode 1768 — Merge Strings Alternately

> Merge `word1` and `word2` by alternating characters starting from `word1`. Append the remaining characters of the longer string at the end.

**Pattern**: [[concepts/array-manipulation-patterns#Pattern 6 — Two-Pointer Merge|Two-Pointer Merge (Unequal Lengths)]]

---

## Debugging Case Study — The Original Buggy Code

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        newWord = []
        wordList1 = list(word1)
        wordList2 = list(word2)
        totalLength = len(wordList1) + len(wordList2)
        for i in range(totalLength):
            newWord.append(newWord + word1[i] + word2[i])  # Bug 1 + Bug 2
        return newWord                                       # Bug 3
```

### Bug 1 — `TypeError`: mixing list and string with `+`

```python
newWord.append(newWord + word1[i] + word2[i])
#              ^^^^^^^ list
#                       ^^^^^^^^^ str
# list + str → TypeError: can only concatenate list (not "str") to list
```

`newWord` is a list. You cannot concatenate it with a string using `+`. The intent was to append a single character, not concatenate the whole list.

**Fix**: append each character individually.

```python
newWord.append(word1[i])
newWord.append(word2[i])
```

### Bug 2 — `IndexError`: single index for two strings of different lengths

```python
for i in range(totalLength):      # totalLength = len(word1) + len(word2)
    ...word1[i]...word2[i]...     # once i >= len(word1), word1[i] → IndexError
```

`totalLength` is the sum of both lengths. When `i` reaches `len(word1)`, `word1[i]` is out of bounds. The loop assumes both strings are the same length — they are not in general.

**Fix**: two independent pointers, each bounded by its own string's length.

### Bug 3 — Wrong return type: returning a list instead of a string

```python
return newWord          # newWord is a list: ['a', 'p', 'b', 'q', ...]
# Expected:  "apbq..."  (str)
```

The function signature declares `-> str`. Returning the raw list fails the type contract and will not match any expected output in testing.

**Fix**: `return "".join(newWord)`

---

## Correct Implementation — Two-Pointer Approach

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i, j = 0, 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):        # word1 still has characters
                result.append(word1[i])
                i += 1
            if j < len(word2):        # word2 still has characters
                result.append(word2[j])
                j += 1

        return "".join(result)
```

### Why two `if` statements, not `if/elif`

```python
# WRONG — elif skips word2 on every step where word1 also had a character
if i < len(word1):
    result.append(word1[i]); i += 1
elif j < len(word2):           # ← never reached until word1 is exhausted
    result.append(word2[j]); j += 1

# CORRECT — both append independently each iteration
if i < len(word1):
    result.append(word1[i]); i += 1
if j < len(word2):             # ← checked regardless of the first branch
    result.append(word2[j]); j += 1
```

### Why `or` in the while condition, not `and`

```python
while i < len(word1) and j < len(word2):  # WRONG — exits as soon as the shorter ends
while i < len(word1) or  j < len(word2):  # CORRECT — continues until both are exhausted
```

---

## Trace on `word1="ab"`, `word2="pqrs"`

Expected output: `"apbqrs"`

| i | j | word1[i] | word2[j] | result |
|---|---|----------|----------|--------|
| 0 | 0 | a | p | ['a','p'] |
| 1 | 1 | b | q | ['a','p','b','q'] |
| — | 2 | *(i exhausted)* | r | ['a','p','b','q','r'] |
| — | 3 | *(i exhausted)* | s | ['a','p','b','q','r','s'] |

`"".join(result)` → `"apbqrs"` ✓

---

## Pythonic One-Liner — `zip_longest`

```python
from itertools import zip_longest

class Solution(object):
    def mergeAlternately(self, word1, word2):
        return "".join(
            a + b
            for a, b in zip_longest(word1, word2, fillvalue="")
        )
```

`zip_longest` pairs characters from both strings step by step. When one string is exhausted, it substitutes `fillvalue=""`, so `a + b` appends an empty string for the missing character — adding nothing, which is exactly the desired behaviour.

| Pair | a | b | a + b |
|------|---|---|-------|
| (0,0) | a | p | "ap" |
| (1,1) | b | q | "bq" |
| (2,—) | "" | r | "r" |  *(word1 exhausted; fillvalue="")* |
| (3,—) | "" | s | "s" |

Joined: `"apbqrs"` ✓

---

## Approach Comparison

| | Two-Pointer | `zip_longest` |
|--|-------------|--------------|
| **Clarity** | Explicit, self-documenting | Concise but requires knowing `zip_longest` |
| **Lines** | ~8 | 3 |
| **Time** | O(m + n) | O(m + n) |
| **Space** | O(m + n) | O(m + n) |
| **Interviews** | ✓ preferred | ✓ as follow-up |

---

## Related Problems

| LeetCode | Relation |
|----------|----------|
| 21 — Merge Two Sorted Lists | Same two-pointer merge idea on linked lists (with ordering constraint) |
| 88 — Merge Sorted Array | Two-pointer merge into a pre-allocated array, right-to-left variant |
| 1470 — Shuffle the Array | Pattern 2 (split-midpoint interleave) — single array, equal halves |
