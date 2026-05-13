---
type: concept
title: "Deadlocks"
domain: operating-systems
source: [[sources/ICT1012-operating-systems]]
complexity: high
updated: 2026-05-13
tags: [concept, operating-systems, deadlocks, bankers-algorithm, resource-allocation, synchronisation]
---

# Deadlocks

Covers the conditions that cause deadlock, how to model them with resource allocation graphs, and the four system-level strategies: prevention, avoidance, detection, and recovery.

---

## 1. Deadlock Characterisation

A **deadlock** is a situation where a set of processes are each waiting for a resource held by another process in the set — forming a circular chain from which no process can escape.

### Four Necessary Conditions

All four conditions must hold simultaneously for deadlock to occur:

| Condition | Description |
|-----------|-------------|
| **Mutual exclusion** | At least one resource must be held in a non-shareable mode — only one process at a time can use it |
| **Hold and wait** | A process holds at least one resource and is waiting to acquire additional resources held by other processes |
| **No preemption** | Resources cannot be forcibly taken from a process; they must be released voluntarily |
| **Circular wait** | A set {P₀, P₁, …, Pₙ} exists such that P₀ waits for a resource held by P₁, P₁ waits for one held by P₂, …, Pₙ waits for one held by P₀ |

---

## 2. Resource Allocation Graph

A directed graph used to describe resource allocation state:

- **Nodes**: processes (circles) and resource types (rectangles with dots for instances)
- **Request edge**: P → R (process P is requesting resource R)
- **Assignment edge**: R → P (one instance of R is assigned to P)

### Interpreting the Graph

| Graph state | Conclusion |
|-------------|-----------|
| No cycle | No deadlock |
| Cycle, all resources have exactly one instance | **Deadlock exists** |
| Cycle, some resources have multiple instances | Deadlock **possible** but not guaranteed |

**Example — deadlock**:
```
P1 → R1 → P2 → R2 → P1   (cycle, single instances → deadlock)
```

**Example — cycle without deadlock**:
```
P1 → R1 ← P3   (P3 will release R1, breaking the cycle)
P2 → R1
```

---

## 3. Deadlock Prevention

Prevent deadlock by **invalidating at least one** of the four necessary conditions.

| Condition to break | How | Cost |
|-------------------|-----|------|
| **Mutual exclusion** | Make resources shareable | Not possible for inherently non-shareable resources (e.g., a printer) |
| **Hold and wait** | Require a process to request all resources before starting; or release all before requesting new ones | Low utilisation; possible starvation |
| **No preemption** | If a process cannot get a resource, it releases all it holds; reclaim resources from waiting processes | Only works for resources with saveable/restoreable state (CPU registers, memory) |
| **Circular wait** | Impose a **total ordering** on resource types; require processes to request resources in increasing order | Most practical; widely used |

### Ordered Resource Acquisition (preventing circular wait)

Assign each resource type a unique integer. A process may only request resource of type Rⱼ if all currently held resources Rᵢ satisfy i < j.

```c
// Example ordering: mutex1 (type 1) < mutex2 (type 2)
// All threads must acquire mutex1 before mutex2
lock(mutex1);
lock(mutex2);
/* critical work */
unlock(mutex2);
unlock(mutex1);
```

---

## 4. Deadlock Avoidance

Rather than preventing deadlock structurally, avoidance algorithms **dynamically examine resource allocation state** before granting each request, ensuring the system never enters an unsafe state.

**Requires a priori information**: each process must declare the **maximum** number of each resource type it may need.

### Safe State

A state is **safe** if there exists a **safe sequence** — an ordering of processes {P₁, P₂, …, Pₙ} such that each Pᵢ's remaining resource needs can be satisfied by the currently available resources plus all resources held by Pⱼ where j < i.

```
Safe   → no deadlock can occur (by definition)
Unsafe → deadlock may occur (not guaranteed, but possible)
```

### Banker's Algorithm

For a system with **multiple resource types**. Data structures:

| Structure | Size | Meaning |
|-----------|------|---------|
| `Available[j]` | m (resource types) | Number of available instances of resource type j |
| `Max[i][j]` | n × m | Maximum demand of process i for resource type j |
| `Allocation[i][j]` | n × m | Resources currently allocated to process i |
| `Need[i][j]` | n × m | Remaining need: `Need[i][j] = Max[i][j] − Allocation[i][j]` |

#### Safety Algorithm

Determine whether the current state is safe:

```
Work  = Available            (copy of available vector)
Finish[i] = false for all i  (no process finished yet)

Loop:
  Find i such that: Finish[i] == false  AND  Need[i] ≤ Work
  If found:
    Work = Work + Allocation[i]   (process finishes, releases resources)
    Finish[i] = true
  Else if all Finish[i] == true:
    State is SAFE
  Else:
    State is UNSAFE (deadlock possible)
```

Time complexity: O(m × n²)

#### Resource-Request Algorithm

When process Pᵢ requests `Request[i]`:

```
1. If Request[i] > Need[i]:  error — exceeded maximum claim
2. If Request[i] > Available: Pᵢ must wait (resources not available)
3. Pretend to allocate:
      Available  = Available  − Request[i]
      Allocation[i] = Allocation[i] + Request[i]
      Need[i]    = Need[i]    − Request[i]
4. Run Safety Algorithm on new state:
      If safe  → grant the request
      If unsafe → roll back (restore old state), Pᵢ waits
```

### Worked Example

**3 processes, 3 resource types (A, B, C). Available = (3, 3, 2)**

| Process | Max (A,B,C) | Allocation (A,B,C) | Need (A,B,C) |
|---------|------------|-------------------|--------------|
| P0 | 7,5,3 | 0,1,0 | 7,4,3 |
| P1 | 3,2,2 | 2,0,0 | 1,2,2 |
| P2 | 9,0,2 | 3,0,2 | 6,0,0 |
| P3 | 2,2,2 | 2,1,1 | 0,1,1 |
| P4 | 4,3,3 | 0,0,2 | 4,3,1 |

Safe sequence: **P1 → P3 → P4 → P0 → P2**

- P1: Need(1,2,2) ≤ Available(3,3,2) → Work becomes (5,3,2)
- P3: Need(0,1,1) ≤ Work(5,3,2) → Work becomes (7,4,3)
- P4: Need(4,3,1) ≤ Work(7,4,3) → Work becomes (7,4,5)
- P0: Need(7,4,3) ≤ Work(7,4,5) → Work becomes (7,5,5)
- P2: Need(6,0,0) ≤ Work(7,5,5) → done

State is safe.

---

## 5. Deadlock Detection

Used when neither prevention nor avoidance is employed. The OS allows deadlocks to occur, then detects and recovers.

### Single Instance per Resource Type — Wait-For Graph

Derived from resource allocation graph by removing resource nodes and collapsing edges:

- **Edge P → Q**: process P is waiting for process Q to release a resource

**A cycle in the wait-for graph = deadlock.**

Detection algorithm: cycle detection in a directed graph → **O(n²)** where n = number of processes.

### Multiple Instances — Detection Algorithm

Similar structure to the Banker's Safety Algorithm:

```
Work  = Available
Finish[i] = false  if Allocation[i] ≠ 0, else true

Loop:
  Find i such that: Finish[i] == false  AND  Request[i] ≤ Work
  If found:
    Work = Work + Allocation[i]
    Finish[i] = true
  Else:
    Break

Any i where Finish[i] == false → process Pᵢ is deadlocked
```

Time complexity: **O(m × n²)**

### When to Invoke Detection?

- **Every resource request**: immediate detection, high overhead
- **Periodically** (e.g., every hour): lower overhead, deadlock may persist longer
- **When CPU utilisation drops below threshold**: pragmatic heuristic

---

## 6. Deadlock Recovery

Once a deadlock is detected, the OS must break it.

### Process Termination

| Strategy | Description | Cost |
|----------|-------------|------|
| **Abort all** deadlocked processes | Immediate but loses all work in progress | High |
| **Abort one at a time** | Re-run detection after each abort until deadlock resolved | More work but selective |

**Selection criteria for which process to abort**: priority, how long it has run, resources it holds, resources it needs, how many processes would be affected.

### Resource Preemption

Select a **victim** process and preempt its resources:

1. **Select a victim**: minimise cost (priority, progress, resource count)
2. **Rollback**: revert the victim process to a safe state (may require checkpointing)
3. **Starvation risk**: the same process may always be chosen as victim → add rollback count as a cost factor

---

## Summary

```
Deadlock requires all 4 conditions simultaneously:
  Mutual exclusion + Hold-and-wait + No preemption + Circular wait

Prevention: break one condition structurally
  → Ordered acquisition (circular wait) is most practical

Avoidance: never enter unsafe state
  → Banker's algorithm: Safety + Resource-Request algorithms

Detection: allow deadlock, then find and break it
  → Wait-for graph (single instance) → cycle = deadlock
  → Detection algorithm (multiple instances) → O(m × n²)

Recovery: terminate processes or preempt resources
```

---

## See Also

- [[concepts/cpu-scheduling-and-synchronisation|CPU Scheduling and Synchronisation]] — semaphore misuse that causes deadlock; priority inversion
- [[concepts/os-processes-and-threads|OS Fundamentals, Processes, and Threads]] — process model; IPC that creates resource dependencies
- [[concepts/memory-and-virtual-memory|Memory Management and Virtual Memory]] — frame allocation policies that can cause thrashing (analogous resource exhaustion)
- [[sources/ICT1012-operating-systems|ICT1012 Source Page]]
