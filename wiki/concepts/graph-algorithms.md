---
type: concept
title: "Graph Algorithms"
domain: computer-science
course: INF1008
complexity: high
tags: [graphs, dfs, bfs, topological-sort, dijkstra, bellman-ford, prims, kruskals, mst, shortest-path]
updated: 2026-05-11
---

# Graph Algorithms

Graphs are the most general relational data structure: they model anything with entities (nodes/vertices) and relationships (edges). Road networks, social networks, dependency graphs, state machines, and neural networks are all graphs. Graph algorithms are consequently among the most widely applied in computing.

## Graph Fundamentals

### Graph Types

| Type | Description | Example |
|------|-------------|---------|
| **Undirected** | Edges have no direction (A-B = B-A) | Social friendships, road networks |
| **Directed (Digraph)** | Edges have direction (A→B ≠ B→A) | Web links, dependencies |
| **Weighted** | Edges carry numeric values | Road distances, network latency |
| **DAG** | Directed Acyclic Graph — no cycles | Task scheduling, build dependencies |
| **Tree** | Connected, undirected, acyclic | File systems, parse trees |

### Graph Representations

**Adjacency Matrix**: V×V matrix where cell [i][j] = 1 (or weight) if edge i→j exists.
- Space: O(V²)
- Edge lookup: O(1)
- Iterating neighbours: O(V)
- Best for: dense graphs (E ≈ V²), edge existence queries

**Adjacency List**: array of V lists; list[i] contains all neighbours of vertex i.
- Space: O(V + E)
- Edge lookup: O(degree)
- Iterating neighbours: O(degree)
- Best for: sparse graphs (E << V²) — most real-world graphs

## Traversal Algorithms

### Depth-First Search (DFS)

Explore as far as possible along each branch before backtracking. Implemented with a **stack** (explicit or call stack via recursion).

```
DFS(G, start):
    mark start as visited
    for each neighbour v of start:
        if v not visited:
            DFS(G, v)
```

- Time: O(V + E) — each vertex and edge visited once
- Space: O(V) for visited set + O(V) recursion depth
- Applications:
  - Cycle detection
  - Topological sort
  - Strongly connected components (Kosaraju/Tarjan)
  - Maze solving
  - Finding connected components

DFS on trees traverses nodes in pre/in/post-order depending on when the node is processed relative to its children.

### Breadth-First Search (BFS)

Explore all neighbours at distance k before any at distance k+1. Implemented with a **queue**.

```
BFS(G, start):
    enqueue start; mark visited
    while queue not empty:
        v = dequeue
        for each neighbour u of v:
            if u not visited:
                mark u visited; enqueue u
```

- Time: O(V + E)
- Space: O(V) for queue
- Applications:
  - **Shortest path in unweighted graphs** (BFS from source = shortest hop count)
  - Level-order traversal of trees
  - Finding connected components
  - Web crawlers (page = vertex, link = edge)

Key property: BFS visits vertices in non-decreasing order of their distance from the source.

## Topological Sort

Only valid on **DAGs** (a cycle makes topological ordering impossible). A topological ordering is a linear sequence of vertices such that for every edge u→v, u appears before v.

**DFS-based algorithm**:
1. Run DFS; when a vertex finishes (all descendants explored), push to a stack
2. Output stack in LIFO order

Time: O(V + E). A DAG has at least one vertex with in-degree 0 (Kahn's algorithm alternative uses a queue and processes in-degree 0 vertices).

Applications: Build systems (Makefile), compiler dependency resolution, course prerequisite ordering, task scheduling.

## Minimum Spanning Trees (MST)

Given a connected, undirected, weighted graph, an MST is a spanning tree (connects all V vertices) with **minimum total edge weight**. A graph has exactly one MST if all edge weights are distinct.

### Prim's Algorithm

Greedy: grow the MST one vertex at a time by always adding the minimum-weight edge that connects the current MST to a new vertex.

1. Start with any vertex; mark it in MST
2. Maintain a priority queue of edges crossing the cut (MST ↔ non-MST)
3. Extract minimum-weight edge; add its new vertex to MST
4. Add all edges from new vertex to priority queue (if other endpoint not in MST)
5. Repeat until all vertices in MST

- Time: O(E log V) with binary heap, O(E + V log V) with Fibonacci heap
- Best for: **dense graphs** (processes edges efficiently)

### Kruskal's Algorithm

Greedy: sort all edges by weight; add each edge if it doesn't form a cycle.

1. Sort all edges by weight: O(E log E)
2. For each edge (u, v) in order: if u and v in different components, add edge (use Union-Find)
3. Stop when V-1 edges added

- Time: O(E log E) = O(E log V) for sorting
- Uses **Union-Find (Disjoint Set Union)** for cycle detection: O(α(V)) per operation
- Best for: **sparse graphs**

Both Prim's and Kruskal's produce the same MST (for graphs with unique edge weights).

## Shortest Path Algorithms

### Dijkstra's Algorithm

Single-source shortest paths for graphs with **non-negative weights**.

1. Initialise dist[source]=0, all others=∞
2. Maintain a min-heap of (distance, vertex) pairs
3. Extract minimum; for each neighbour v: if dist[u] + w(u,v) < dist[v], update dist[v] and push to heap
4. Repeat until heap empty

- Time: O(E log V) with binary heap
- Space: O(V + E)
- Correctness: relies on non-negative weights — a negative edge would allow already-finalised vertices to be improved

Applications: GPS navigation, network routing (OSPF protocol), game pathfinding (A* is Dijkstra with heuristic).

### Bellman-Ford Algorithm

Single-source shortest paths for graphs with **negative-weight edges** (but no negative-weight cycles).

1. Initialise dist[source]=0, all others=∞
2. Repeat V-1 times: for every edge (u, v, w): if dist[u] + w < dist[v], update dist[v]
3. Run one more iteration: if any dist[v] updates, a negative-weight cycle exists

- Time: O(VE) — significantly slower than Dijkstra
- Space: O(V)
- Detects negative cycles (Dijkstra cannot)

Applications: Currency arbitrage detection (negative cycle = profit cycle), routing protocols (distance-vector, e.g., RIP).

## Algorithm Selection Guide

| Problem | Algorithm | Condition |
|---------|-----------|-----------|
| Traverse all vertices | DFS or BFS | Any graph |
| Shortest path (unweighted) | BFS | Unweighted |
| Shortest path (non-negative weights) | Dijkstra | No negative edges |
| Shortest path (negative weights) | Bellman-Ford | No negative cycles |
| All-pairs shortest paths | Floyd-Warshall | Dense graphs |
| Minimum spanning tree (dense) | Prim's | Connected, undirected, weighted |
| Minimum spanning tree (sparse) | Kruskal's | Connected, undirected, weighted |
| Ordering with dependencies | Topological Sort | DAG only |
| Cycle detection | DFS | Any directed graph |

## See Also

- [[data-structures-fundamentals]] — heaps (Prim's/Dijkstra), union-find (Kruskal's), queues (BFS), stacks (DFS)
- [[algorithm-complexity]] — O(V+E), O(E log V) analysis
- [[INF1008-data-structures-algorithms]] — source course
