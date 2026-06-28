---
type: source
address: c-000094
title: "LeetCode 1768 — Merge Strings Alternately"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-merge-alternately-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, two-pointers, strings, debugging, computer-science]
---

# LeetCode 1768 — Merge Strings Alternately

Easy problem. Interleave two strings character by character; append the remainder of the longer string. Fills out **Pattern 6 — Two-Pointer Merge (Unequal Lengths)** in [[concepts/array-manipulation-patterns]].

Notable because this problem was submitted with three distinct bugs, making it a useful **debugging case study** in addition to a pattern example.

## Key Takeaways

- **Two separate pointers** (`i` and `j`) are required whenever the two inputs may have different lengths. A single shared index causes an `IndexError` once the shorter input is exhausted.
- **`list.append(char)`** is the correct idiom for building a character list one element at a time. `list.append(list + str)` is a `TypeError` — you cannot concatenate a list and a string with `+`.
- **`"".join(lst)`** converts a character list to a string. Returning the raw list is a type error (return value must be `str`).
- **`zip_longest` idiom**: `"".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))` is a Pythonic one-liner. The `fillvalue=""` means the shorter string contributes an empty string once exhausted, so appending it adds nothing — clean and correct.

## Bug Summary

| Bug | Root Cause | Fix |
|-----|-----------|-----|
| `TypeError` in append | `newWord + word1[i]` mixes list and str | `newWord.append(word1[i])` |
| `IndexError` at loop | Single index `i` for both words | Two independent pointers `i`, `j` |
| Wrong return type | `return newWord` returns a list | `return "".join(newWord)` |

## Related Concepts

- [[concepts/array-manipulation-patterns]] — Pattern 6 (Two-Pointer Merge, Unequal Lengths)

## Related Examples

- [[examples/leetcode-merge-alternately-python]] — buggy code dissected line by line; two correct implementations
