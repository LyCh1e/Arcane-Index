---
type: concept
address: c-000083
title: "Simulation Patterns"
domain: computer-science
complexity: medium
created: 2026-06-28
updated: 2026-06-28
tags: [concept, simulation, greedy, stack, streams, computer-science]
related:
  - concepts/data-structures-fundamentals
  - concepts/algorithm-complexity
  - concepts/array-manipulation-patterns
---

# Simulation Patterns

Problems that ask you to **replay a process** — reading a stream, operating a machine, executing instructions — and record what happens. The key skill is translating the problem's rules directly into code without over-engineering, then finding the constraint that allows an early exit.

Simulation problems look hard because they describe a complex system, but the solution is often a faithful one-pass re-enactment of the rules.

---

## Pattern 1 — Greedy Stream Simulation with Early Exit

**Problem shape**: you receive a sequential stream of values 1→n and a sorted target sequence. Decide per element whether to "keep" or "discard" it, recording the operations performed. Stop as soon as the target is fully matched.

```python
target_set = set(target)          # O(1) membership test; convert once before the loop

for number in range(1, n + 1):
    if not target_set:            # early exit — target already built
        break

    if number in target_set:
        operations.append("Push") # keep: record the keep operation
        target_set.remove(number) # mark this target element as satisfied
    else:
        operations.append("Push") # discard: must still "touch" the element …
        operations.append("Pop")  #          … then immediately undo it
```

**Why convert target to a set?**
The loop checks `number in target` on every iteration. If target is a list, that is O(|target|) per check → O(n × |target|) total. Converting to a set once makes every check O(1) → O(n) total. For LeetCode constraints (target up to 100 elements) the difference is negligible, but the pattern is correct practice.

**Why remove from the set rather than use an index?**
Removal from the set lets the `if not target_set` guard work as a clean "all matched" signal in O(1), without maintaining a separate pointer.

**Early exit correctness**: once `target_set` is empty, every remaining stream element would produce a Push-Pop pair (it is not in target). The problem states "do not read new integers once done" — the early exit is required, not optional.

**The effective stream bound**: since target is strictly increasing, the loop will always exit at or before `number == target[-1]`. The parameter `n` only matters if target is empty (pathological case) or if you forget the early exit.

**Complexity**: O(n) time, O(|target|) space for the set.

**LeetCode**: 1441 — Build an Array With Stack Operations.

---

## Pattern 2 — State-Machine Simulation (Placeholder)

*To be filled when the first state-machine simulation problem is ingested.*

Common shape: a list of instructions drives state transitions; record the state at each step or the final state after all instructions.

---

## Pattern 3 — Grid / Board Simulation (Placeholder)

*To be filled when the first grid simulation problem is ingested.*

Common shape: an agent moves across a 2D grid according to direction instructions; simulate each step and check boundary conditions or visited cells.

---

## General Principles

### Translate rules literally first
Write the simulation exactly as the problem describes — one rule, one `if` branch. Optimise only after the brute force is correct. Many simulation problems accept the direct translation without further optimisation.

### Identify the early exit condition
Most simulation problems have a condition under which further steps are provably no-ops or forbidden. Finding it early turns O(n) brute-force loops into significantly faster practical runs.

### Use the right structure for "have I seen this?"
| Lookup need | Structure | Time |
|-------------|-----------|------|
| "Is x in the target set?" | `set` | O(1) |
| "How many times have I seen x?" | `dict` / `Counter` | O(1) |
| "What was the last element?" | stack / variable | O(1) |
| "What is the next ordered element?" | sorted list + pointer | O(1) amortised |

### Watch for mandatory vs optional operations
In stream problems, "push" is often **mandatory** (you must read from the stream) while "pop" is **optional**. Confusing these leads to missing operations in the output.

---

## Complexity Summary

| Pattern | Time | Space |
|---------|------|-------|
| Greedy stream simulation | O(n) | O(\|target\|) |

---

## See Also

- [[concepts/data-structures-fundamentals]] — stacks, queues, and their operation costs
- [[concepts/algorithm-complexity]] — Big-O for simulation loops
- [[concepts/array-manipulation-patterns]] — related single-pass array patterns
- [[examples/leetcode-stack-ops-python]] — worked example for Pattern 1
