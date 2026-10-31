---
type: concept
title: "Sorting and Searching Algorithms"
domain: computer-science
course: INF1008
complexity: high
tags: [sorting, searching, bubble-sort, merge-sort, quick-sort, binary-search, kmp, boyer-moore]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000006
---

# Sorting and Searching Algorithms

Sorting and searching are among the most frequently performed operations in software. Understanding the trade-offs between algorithms — time complexity, space, stability, and practical constants — determines whether a feature runs in milliseconds or seconds.

## Sorting Algorithms

### Stability and In-Place Defined

- **Stable**: equal elements retain their original relative order after sorting (important when sorting by secondary keys)
- **In-place**: uses O(1) auxiliary space (ignoring recursion stack)

### Bubble Sort

Repeatedly compare adjacent pairs; swap if out of order. Each full pass "bubbles" the largest unsorted element to its correct position.

| Case | Complexity |
|------|-----------|
| Best (already sorted) | O(n) with early-exit flag |
| Average | O(n²) |
| Worst (reverse sorted) | O(n²) |

Space: O(1). Stable: Yes. Practical use: essentially none — teaching tool only.

### Selection Sort

Find the minimum in the unsorted portion; swap it with the first unsorted element. Repeat.

| Case | Complexity |
|------|-----------|
| All cases | O(n²) |

Space: O(1). Stable: No (swapping breaks stability). Practical use: minimises swaps (useful when writes are expensive — e.g., flash memory).

### Insertion Sort

Build a sorted subarray from left to right by inserting each new element in the correct position.

| Case | Complexity |
|------|-----------|
| Best (already sorted) | O(n) |
| Average | O(n²) |
| Worst (reverse sorted) | O(n²) |

Space: O(1). Stable: Yes. Practical use: excellent for small arrays (n < 20) and nearly-sorted data. Used as the base case in Timsort and Introsort.

### Merge Sort

Divide-and-conquer: split array in half, recursively sort each half, merge the two sorted halves.

| Case | Complexity |
|------|-----------|
| All cases | O(n log n) |

Space: O(n) auxiliary for merge buffer. Stable: Yes.

Practical use: preferred when stability is required and O(n) space is acceptable. Default for sorting linked lists (no random access needed). Java's `Arrays.sort()` for objects uses a variant (Timsort).

**Merge step**: two-pointer technique — compare heads, emit smaller, advance that pointer. O(n) per level, O(log n) levels → O(n log n) total.

### Quick Sort

Divide-and-conquer: choose a **pivot**, partition array so all elements < pivot are left, all > pivot are right. Recursively sort each partition.

| Case | Complexity |
|------|-----------|
| Best / Average | O(n log n) |
| Worst (already sorted, bad pivot) | O(n²) |

Space: O(log n) avg recursion stack. Stable: No.

Practical use: fastest in practice for most inputs due to cache locality and small constants. Java's `Arrays.sort()` for primitives; C's `qsort`. Mitigate worst case with **randomised pivot** or **median-of-three**.

**Partition schemes**: Lomuto (simpler, slightly slower) vs Hoare (original, fewer swaps).

## Complete Sorting Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Teaching only |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Min writes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Small/nearly-sorted |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Stable guarantee |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fastest in practice |

## Searching Algorithms

### Linear Search

Check each element sequentially until found or exhausted.

- Time: O(n) all cases
- Space: O(1)
- Works on: unsorted and sorted arrays, linked lists
- Use when: array is small, unsorted, or searched rarely

### Binary Search

On a **sorted** array: compare target with middle element; recurse on left or right half.

- Time: O(log n)
- Space: O(1) iterative, O(log n) recursive
- Requires: sorted, random-access array
- Use when: array is large and sorted (or can be kept sorted)

```
low = 0, high = n-1
while low ≤ high:
    mid = (low + high) / 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: low = mid + 1
    else: high = mid - 1
return NOT_FOUND
```

Common bug: `(low + high) / 2` can overflow for large indices — use `low + (high - low) / 2`.

## String Searching Algorithms

String search finds the first occurrence of a pattern P (length m) in a text T (length n).

### Brute Force

Try every starting position in T; compare with P character by character.

- Time: O(nm) worst case
- Space: O(1)
- Simple but slow for adversarial inputs (e.g., searching "aaab" in "aaaa...a")

### KMP — Knuth-Morris-Pratt

Preprocesses the pattern to build a **failure function** (also called partial match table / prefix function). When a mismatch occurs, instead of restarting from scratch, skip ahead using the failure function.

**Failure function** `f[i]` = length of the longest proper prefix of `P[0..i]` that is also a suffix.

Example for P = "ABABC":
- f[0]=0, f[1]=0, f[2]=1, f[3]=2, f[4]=0

- Preprocessing: O(m)
- Search: O(n) — each character in T examined at most twice
- Total: **O(n + m)**
- Space: O(m) for failure function

KMP is optimal for single-pattern search when the pattern has repeated structure.

### Boyer-Moore

Preprocesses the pattern using two heuristics:
1. **Bad Character Rule**: when mismatch at position j in pattern, shift pattern so the mismatched text character aligns with its rightmost occurrence in the pattern (or skip past the pattern if not found)
2. **Good Suffix Rule**: when mismatch after matching k characters, shift pattern so the matched suffix aligns with its next occurrence (or use a safe shift)

Uses the larger of the two shifts. Scans **right-to-left** within the pattern.

- Preprocessing: O(m + alphabet_size)
- Search: O(n/m) best case (sublinear!), O(nm) worst case
- Average: **O(n/m)** — faster than KMP for large alphabets and long patterns

Boyer-Moore is preferred for text editors and search tools on natural language (large alphabet, long patterns). `grep` uses a variant (Boyer-Moore-Horspool).

## When to Use Which Algorithm

| Scenario | Recommendation |
|----------|---------------|
| n < 20, any order | Insertion Sort |
| Large n, stability required | Merge Sort |
| Large n, best average performance | Quick Sort (randomised pivot) |
| Already nearly sorted | Insertion Sort |
| External sort (disk) | Merge Sort |
| Array is sorted, find element | Binary Search |
| Array is unsorted, find element | Linear Search (or sort first) |
| Single pattern search, repeated prefixes | KMP |
| Single pattern, large alphabet, long pattern | Boyer-Moore |

## See Also

- [[synthesis/research-sorting-algorithms]] — heap, Shell, hybrid, non-comparison and SIMD sorts
- [[concepts/heapsort]], [[concepts/shellsort]], [[concepts/hybrid-sorting-algorithms]], [[concepts/non-comparison-sorting]], [[concepts/comparison-sort-lower-bound]]
- [[algorithm-complexity]] — formal complexity analysis and Master Theorem
- [[data-structures-fundamentals]] — heaps enable Heap Sort; hash tables enable O(1) lookup
- [[graph-algorithms]] — DFS/BFS use stacks/queues
- [[INF1008-data-structures-algorithms]] — source course
