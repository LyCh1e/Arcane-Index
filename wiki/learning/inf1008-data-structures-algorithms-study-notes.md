---
type: learning
title: "INF1008 Data Structures and Algorithms — Exam Study Notes"
domain: computer-science
source: "[[sources/INF1008-data-structures-algorithms|INF1008 Source]]"
complexity: high
updated: 2026-05-14
tags: [learning, algorithms, data-structures, exam-prep, complexity, sorting, graphs, searching]
---

# INF1008 Data Structures and Algorithms — Exam Study Notes

Dense Q&A and definition cards for exam preparation. Covers complexity analysis, data structure operations, sorting, graph algorithms, and string matching.

---

## 1. Algorithm Complexity

> [!question]- State the formal Big-Oh definition.
> f(n) = O(g(n)) if there exist constants **c > 0** and **n₀ > 0** such that:
> > f(n) ≤ c · g(n)   for all n ≥ n₀
>
> "f grows **no faster than** g." Used to express worst-case upper bounds.
> Related notations:
> - **Ω(g(n))** — lower bound: f grows at least as fast as g
> - **Θ(g(n))** — tight bound: f grows at exactly the same rate as g (both O and Ω)

> [!question]- State the Master Theorem with its three cases and give one example of each.
> Solves recurrences of the form **T(n) = a·T(n/b) + f(n)**.
> Let **c_crit = log_b(a)** (critical exponent).
>
> | Case | Condition | Result | Example |
> |------|-----------|--------|---------|
> | **Case 1** | f(n) = O(n^(c_crit − ε)) for some ε > 0 | T(n) = Θ(n^c_crit) — recursion dominates | Strassen: a=7, b=2, c_crit≈2.81; f(n)=O(n²) < O(n^2.81) → **Θ(n^2.81)** |
> | **Case 2** | f(n) = Θ(n^c_crit · logᵏ n) | T(n) = Θ(n^c_crit · log^(k+1) n) — balanced | Merge Sort: a=2, b=2, c_crit=1; f(n)=Θ(n) → **Θ(n log n)** |
> | **Case 3** | f(n) = Ω(n^(c_crit + ε)) and regularity holds | T(n) = Θ(f(n)) — combining step dominates | (Rare in standard algorithms) |
>
> Binary Search: T(n) = T(n/2) + O(1); a=1, b=2, c_crit=0; f(n)=Θ(1)=Θ(n⁰) → Case 2 → **Θ(log n)**

> [!question]- List the common complexity classes from fastest to slowest with examples.
> | Class | Name | Example |
> |-------|------|---------|
> | O(1) | Constant | Array index, hash lookup |
> | O(log n) | Logarithmic | Binary search, BST operation |
> | O(n) | Linear | Linear search, array scan |
> | O(n log n) | Linearithmic | Merge sort, heap sort |
> | O(n²) | Quadratic | Bubble/selection/insertion sort |
> | O(n³) | Cubic | Naive matrix multiplication |
> | O(2ⁿ) | Exponential | Subset enumeration |
> | O(n!) | Factorial | Permutation generation, TSP brute force |

---

## 2. Data Structure Complexities

> [!question]- State the key operation complexities for core data structures.
> | Structure | Access | Search | Insert | Delete | Notes |
> |-----------|--------|--------|--------|--------|-------|
> | **Array** | O(1) | O(n) | O(n) | O(n) | Shifting required for mid-insert |
> | **Stack / Queue** | O(n) | O(n) | O(1) | O(1) | LIFO / FIFO; push/pop/enqueue/dequeue at O(1) |
> | **Linked List** | O(n) | O(n) | O(1) head | O(1) w/ ptr | No random access; insert at head always O(1) |
> | **BST** | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg | Degrades to O(n) if unbalanced (sorted input) |
> | **AVL / Red-Black** | O(log n) | O(log n) | O(log n) | O(log n) | Guaranteed O(log n); AVL stricter balance |
> | **Heap** | O(1) min/max | O(n) | O(log n) | O(log n) | extract-min/max is O(log n); build-heap is O(n) |
> | **Hash Table** | N/A | O(1) avg | O(1) avg | O(1) avg | Worst case O(n) if all keys collide |
> | **B-Tree / B+ Tree** | O(log n) | O(log n) | O(log n) | O(log n) | Designed for disk I/O; high fanout |

> [!question]- When should you use a Stack vs a Queue?
> **Stack (LIFO)**: when you need to reverse order or backtrack — function call management, DFS traversal, expression evaluation (infix → postfix), undo/redo, bracket matching.
> **Queue (FIFO)**: when you need first-come-first-served order — BFS traversal, task scheduling, print spooling.
> Rule of thumb: DFS needs a stack; BFS needs a queue.

> [!question]- What is the difference between AVL trees and Red-Black trees?
> Both are self-balancing BSTs with O(log n) operations.
> - **AVL**: stricter balance — height difference between subtrees ≤ 1 at every node. Faster lookups; more rotations on insert/delete. Preferred for **read-heavy** workloads.
> - **Red-Black**: less strict balance — up to 2× height difference allowed. Fewer rotations on insert/delete. Used in Java `TreeMap`/`TreeSet`, C++ `std::map`, Linux kernel scheduler. Preferred for **write-heavy** workloads.

---

## 3. Sorting Algorithms

> [!question]- Compare the five core sorting algorithms across time, space, stability, and in-place.
> | Algorithm | Best | Average | Worst | Space | Stable | In-place |
> |-----------|------|---------|-------|-------|--------|---------|
> | **Bubble** | O(n)† | O(n²) | O(n²) | O(1) | Yes | Yes |
> | **Selection** | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
> | **Insertion** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
> | **Merge** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
> | **Quick** | O(n log n) | O(n log n) | O(n²) | O(log n)† | No | Yes |
>
> † Bubble O(n) requires early-exit flag on already-sorted input. Quick Sort space is recursion stack depth.

> [!question]- Quick Sort: when does the worst case occur and how is it mitigated?
> **Worst case O(n²)** occurs when the pivot is always the smallest or largest element — e.g., choosing the first element as pivot on an **already-sorted or reverse-sorted** array. Each partition produces one subarray of size n−1 and one empty, giving a recursion depth of n.
> **Mitigations**:
> - **Randomised pivot**: choose a random element as pivot → expected O(n log n)
> - **Median-of-three**: choose the median of first, middle, and last elements → avoids worst case for nearly-sorted input
> Quick Sort is fastest in practice for most inputs due to cache locality and small constants.

> [!question]- When would you choose Insertion Sort over Merge Sort or Quick Sort?
> **Insertion Sort** is preferred when:
> - n < ~20 (small arrays) — low overhead, no recursion
> - The array is already nearly sorted — O(n) in the best case
> - Used as the base case in hybrid algorithms (Timsort, Introsort)
> Merge Sort is preferred when stability is required and O(n) auxiliary space is acceptable (e.g., sorting linked lists, Java `Arrays.sort()` for objects). Quick Sort (randomised) is the default choice for large arrays when stability is not required.

---

## 4. Graph Algorithms — Traversal and Ordering

> [!question]- DFS vs BFS: data structure, time complexity, and when to use each.
> | | DFS | BFS |
> |-|-----|-----|
> | Data structure | **Stack** (or recursion call stack) | **Queue** |
> | Time complexity | O(V + E) | O(V + E) |
> | Space complexity | O(V) | O(V) |
> | Use for | Cycle detection, topological sort, connected components, maze solving | **Shortest path in unweighted graphs**, level-order traversal, web crawlers |
>
> Key BFS property: vertices are visited in **non-decreasing order of distance** from the source.

> [!question]- Describe two algorithms for topological sort.
> Topological sort is only valid on a **DAG** (directed acyclic graph). A cycle makes topological ordering impossible.
> **DFS-based**:
> 1. Run DFS on the graph
> 2. When a vertex finishes (all descendants explored), push it onto a stack
> 3. Output the stack in LIFO order — this is a valid topological ordering
>
> **Kahn's algorithm (BFS-based)**:
> 1. Compute in-degree of every vertex
> 2. Enqueue all vertices with in-degree 0
> 3. Repeatedly dequeue a vertex, output it, and decrement in-degree of its neighbours; enqueue neighbours whose in-degree drops to 0
>
> Both run in O(V + E). Applications: build systems (Makefile), course prerequisites, compiler dependency resolution.

---

## 5. Minimum Spanning Trees and Shortest Paths

> [!question]- Prim's vs Kruskal's — state the key difference and when to use each.
> | | Prim's | Kruskal's |
> |-|--------|-----------|
> | Strategy | Grow MST one **vertex** at a time via min-edge crossing the cut | Add cheapest **edge** globally that does not form a cycle |
> | Data structure | Priority queue of crossing edges | Sort all edges; Union-Find for cycle detection |
> | Time | O(E log V) | O(E log E) = O(E log V) |
> | Best for | **Dense graphs** (many edges, fewer distinct edge sorts needed) | **Sparse graphs** (sorting a small edge list is cheap) |
>
> Both algorithms are greedy and produce the same MST (for graphs with unique edge weights).

> [!question]- Dijkstra vs Bellman-Ford — why does Dijkstra fail on negative-weight edges?
> **Dijkstra's algorithm** uses a greedy approach: once a vertex is extracted from the min-heap with distance d, that distance is treated as final. A negative-weight edge could later provide a shorter path to an already-finalised vertex, violating the algorithm's correctness invariant.
> **Bellman-Ford** relaxes all edges V−1 times, allowing distances to be updated regardless of discovery order. It runs in **O(VE)** — significantly slower than Dijkstra's O(E log V) — but:
> - Handles **negative-weight edges**
> - Detects **negative-weight cycles** (by running one more iteration: if any distance still decreases, a negative cycle exists)
> Use Dijkstra for GPS/routing (no negative weights); use Bellman-Ford for currency arbitrage detection or distance-vector routing protocols.

---

## 6. String Matching

> [!question]- Brute Force string matching — complexity and weakness.
> Try every starting position in text T (length n) and compare with pattern P (length m) character by character.
> - Time: **O(n × m)** worst case
> - Space: O(1)
> Weakness: adversarial inputs (e.g., pattern "aaab" in text "aaaa…a") force many comparisons before each mismatch, approaching O(nm).

> [!question]- KMP algorithm — what does the failure function do and what is the total complexity?
> The **failure function** (prefix function) `f[i]` = length of the longest proper prefix of `P[0..i]` that is also a suffix of `P[0..i]`.
> *Example*: P = "ABABC" → f = [0, 0, 1, 2, 0]
> When a mismatch occurs at position j in the pattern, instead of restarting from scratch, the algorithm uses `f[j−1]` to skip ahead — effectively reusing knowledge of the already-matched portion.
> - Preprocessing (build failure function): **O(m)**
> - Search: **O(n)** — each character in T is examined at most twice
> - Total: **O(n + m)**
> KMP is optimal for single-pattern search when the pattern has repeated structure (long failure function values). It guarantees linear time regardless of input.

---

## Quick Reference

| Algorithm / Structure | Best Case | Worst Case | Space | Notes |
|----------------------|-----------|------------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(1) | Stable; teaching only |
| Selection Sort | O(n²) | O(n²) | O(1) | Not stable; min writes |
| Insertion Sort | O(n) | O(n²) | O(1) | Stable; best for small/nearly-sorted |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Stable guarantee |
| Quick Sort | O(n log n) | O(n²) | O(log n) | Fastest in practice; not stable |
| Binary Search | O(1) | O(log n) | O(1) | Requires sorted array |
| Brute Force String | O(n) | O(nm) | O(1) | Simple; slow adversarial |
| KMP | O(n+m) | O(n+m) | O(m) | Failure function enables skipping |
| Dijkstra | O(E log V) | O(E log V) | O(V+E) | Non-negative weights only |
| Bellman-Ford | O(VE) | O(VE) | O(V) | Handles negative weights |
| Prim's MST | O(E log V) | O(E log V) | O(V+E) | Dense graphs |
| Kruskal's MST | O(E log E) | O(E log E) | O(V+E) | Sparse graphs |

## See Also

- [[concepts/algorithm-complexity|Algorithm Complexity]]
- [[concepts/data-structures-fundamentals|Data Structures Fundamentals]]
- [[concepts/sorting-and-searching|Sorting and Searching]]
- [[concepts/graph-algorithms|Graph Algorithms]]
