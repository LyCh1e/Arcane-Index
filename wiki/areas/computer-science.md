---
type: area
status: established
title: "Computer Science"
domain: computer-science
source: [[sources/INF1008-data-structures-algorithms]]
updated: 2026-05-14
tags: [area, computer-science]
---

# Computer Science

**Source**: INF1008 — Data Structures and Algorithms, SIT.

---

## What I Know

Foundational computer science: how to measure algorithmic efficiency and choose the right data structure and algorithm for a given problem. Every data structure has a complexity profile; choosing correctly is the difference between O(n) and O(n²).

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/algorithm-complexity\|Algorithm Complexity]] | Big-Oh, Big-Omega, Big-Theta, Master Theorem (3 cases), recurrence relations, space complexity |
| [[concepts/data-structures-fundamentals\|Data Structures Fundamentals]] | Arrays, linked lists, stacks, queues, trees (BST/AVL/Heap), hash tables, B-Trees — with complexity tables |
| [[concepts/sorting-and-searching\|Sorting and Searching]] | Bubble/Selection/Insertion/Merge/Quick sort; brute-force, KMP, Boyer-Moore string search |
| [[concepts/graph-algorithms\|Graph Algorithms]] | DFS/BFS, topological sort, MST (Prim's/Kruskal's), shortest paths (Dijkstra/Bellman-Ford) |
| [[concepts/array-manipulation-patterns\|Array Manipulation Patterns]] | Concatenation, split-midpoint interleaving, linear scan with running counter; Python idioms |
| [[concepts/simulation-patterns\|Simulation Patterns]] | Greedy stream simulation with early exit; state-machine and grid simulation (placeholders) |
| [[concepts/greedy-patterns\|Greedy Patterns]] | Sort + greedy constraint propagation; interval greedy and two-pass greedy (placeholders) |

---

## Key Ideas

- **Algorithm ≠ data structure**: a data structure stores; an algorithm operates. The combination determines overall complexity
- **Master Theorem cases**: T(n) = aT(n/b) + f(n). Compare f(n) to n^(log_b a). If f is smaller → Case 1 (O(n^log_b_a)); if equal → Case 2 (O(n^log_b_a × log n)); if larger → Case 3 (O(f(n)))
- **AVL vs Heap**: AVL supports ordered search (O(log n) all ops); Heap supports priority access (O(1) peek, O(log n) insert/delete) — different tools for different jobs
- **Graph choice**: DFS for connectivity/cycle detection/topological sort; BFS for shortest-hop path; Dijkstra for weighted shortest path (no negative edges); Bellman-Ford when negative weights exist
- **KMP vs Brute Force**: KMP preprocesses the pattern (O(m)) to build a failure function, making the search O(m+n) rather than O(m×n)

---

## Cross-Domain Connections

- [[concepts/database-indexing-transactions|Database Indexing]] — B+ trees are the algorithmic engine behind database indexes; B-Tree theory from INF1008 applies directly
- [[concepts/nosql-and-data-warehousing|NoSQL]] — hash tables underpin key-value stores; graph traversal algorithms underpin graph databases
- [[synthesis/maths-to-ml-bridge|Mathematics → ML]] — algorithm complexity determines training feasibility for ML models

---

## Study Notes

[[learning/inf1008-data-structures-algorithms-study-notes|INF1008 Study Notes]] — exam-prep summaries
