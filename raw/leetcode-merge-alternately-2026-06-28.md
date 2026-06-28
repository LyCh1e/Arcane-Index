---
source_type: chat-session
fetched: 2026-06-28
problems:
  - "LeetCode 1768 — Merge Strings Alternately"
language: Python
difficulty: Easy
---

# LeetCode 1768 — Merge Strings Alternately

Merge word1 and word2 by adding letters in alternating order, starting with word1.
If one string is longer, append the additional letters at the end.

Examples:
  word1="abc", word2="pqr" → "apbqcr"
  word1="ab",  word2="pqrs" → "apbqrs"
  word1="abcd", word2="pq"  → "apbqcd"

## Buggy original code (from user)

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        newWord = []
        wordList1 = list(word1)
        wordList2 = list(word2)
        totalLength = len(wordList1) + len(wordList2)
        for i in range(totalLength):
            newWord.append(newWord + word1[i] + word2[i])
        return newWord
```

Bugs:
1. `newWord + word1[i] + word2[i]` — TypeError: concatenates list + str + str
2. Single index i shared between both words — IndexError when lengths differ
3. `return newWord` — returns list, not str

## Fixed code

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        newWord = []
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                newWord.append(word1[i])
                i += 1
            if j < len(word2):
                newWord.append(word2[j])
                j += 1
        return "".join(newWord)
```

Two separate pointers handle unequal lengths. Each pointer advances independently.
"".join(newWord) converts the character list to a string.

## Alternate: zip_longest one-liner

```python
from itertools import zip_longest
return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
```
