---
type: source
address: c-000082
title: "LeetCode 1441 — Build an Array With Stack Operations"
domain: computer-science
source_type: chat-session
raw: raw/leetcode-stack-ops-2026-06-28.md
created: 2026-06-28
updated: 2026-06-28
tags: [source, leetcode, python, stack, simulation, greedy, computer-science]
---

# LeetCode 1441 — Build an Array With Stack Operations

Single Easy-tier problem introducing the **greedy stream simulation** paradigm and establishing the new [[concepts/simulation-patterns]] concept page.

| Aspect | Detail |
|--------|--------|
| Pattern | Greedy stream simulation with early exit |
| Data structure | Stack (simulated via output list) |
| Key constraint exploited | `target` is strictly increasing |

## Key Takeaways

- **Convert target to a set** before the loop. Testing membership `number in target_set` is O(1) vs O(|target|) for a list.
- **Push-Pop as discard**: the only way to skip a stream element is to push it then immediately pop it. There is no "skip" operation — the push is mandatory.
- **Early termination**: once `target_set` is empty we have built the full target. Continuing to iterate over the stream would produce extra Push-Pop pairs that add useless noise to the output. The constraint "do not read new integers once done" makes this stop mandatory, not optional.
- **The stream never needs to exceed `max(target)`**: since target is strictly increasing, the largest element we ever want is `target[-1]`. Numbers beyond that in the stream are never needed, so the loop always exits before reaching `n` in practice.

## Related Concepts

- [[concepts/simulation-patterns]] — Pattern 1 (Greedy Stream Simulation) introduced by this problem
- [[concepts/data-structures-fundamentals]] — stack operations (push/pop); this problem uses the stack as a conceptual frame, not as a Python data structure

## Related Examples

- [[examples/leetcode-stack-ops-python]] — annotated solution with full trace table
