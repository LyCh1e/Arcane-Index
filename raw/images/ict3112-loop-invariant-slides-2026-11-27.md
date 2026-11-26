---
source_type: image
original_file: 5 slide screenshots (1795710839148_image.png, 1795710894835_image.png, 1795710910155_image.png, 1795710933924_image.png, 1795711044863_image.png)
fetched: 2026-11-27
course: ICT3112
---

# Image: ICT3112 loop-invariant slides (finding and fixing invariants)

Five SIT ICT3112 lecture slides on discovering loop invariants and repairing failed candidates.

## Slide 1: Drawing the data to find the invariant

1. Draw the data, and mark where the progress variable is.
2. Write what is true in each region of the picture.
3. Add the bounds of the progress variable.

Diagram: an array from 0 to n, split at i. The left part (0 to i) is "visited": what Q asks for, restricted to this part. The right part (i to n) is "not visited": what is still true here, usually the original values.

I = (visited) ∧ (not visited) ∧ (0 ≤ i ≤ n)

Array sum: visited: s = A[0] + ⋯ + A[i − 1]. Not visited: nothing to say, the loop only reads A. Bounds: 0 ≤ i ≤ n.

## Slide 2: The template in all the loops we have seen

The same four slots as in the template recording. The picture gives the region slots.

| Loop | Visited | Not visited | Other relations | Bounds |
|---|---|---|---|---|
| Countdown with a counter | — | — | c + x = C + X | x ≥ 0 |
| Integer division | — | — | a = b·q + r | 0 ≤ r |
| Array sum | s = A[0] + ⋯ + A[i − 1] | — (only reads A) | — | 0 ≤ i ≤ n |
| Zero-fill | A[k] = 0 for k < i | A[k] = A₀[k] for k ≥ i | — | 0 ≤ i ≤ m |
| Reverse in place | front and back swapped | middle: A[k] = A₀[k] | l + r = n − 1 | on l and r |
| Selection sort | sorted prefix | — | perm(A, A₀), prefix ≤ rest | 0 ≤ i ≤ n |

The bounds slot is always filled. Facts that are not about one region go in the other relations slot.

## Slide 3: Common mistakes when proposing an invariant

- Too weak: it is true and preserved, but I ∧ ¬B does not imply Q.
- Too strong: it is close to Q, but it is false before the first iteration.
- Missing bounds: we found the equation of the loop, but not the facts that fix the final value of the counter.
- Missing extra facts: in max or search loops one equation is not enough: we may also need facts about the prefix, or a witness.

When a candidate fails, first find out which kind of failure it is. Then strengthen or weaken the invariant accordingly.

## Slide 4: What to do when a check fails

1. Say which check fails: establishment, preservation, or the postcondition at exit.
2. Write down a concrete state that shows the failure, with a number for every variable.
3. Ask what the state tells you.
4. Change the candidate, and check all three conditions again.

- The candidate rejects a real state: it is too strong, so we weaken it.
- The candidate accepts a wrong state: it is too weak, so we add the fact that rules the state out.

Establishment failures give the first kind of state. Preservation and exit failures give the second kind.

## Slide 5: Which condition fails, and how to fix it

The check that fails, and the bad state it gives, tell us how to fix the invariant:

| Check that fails | The bad state | Type of problem | How to fix it |
|---|---|---|---|
| Establishment | a real state at the first loop head that the candidate rejects | too strong | weaken: replace constants by progress variables |
| Preservation | a state that satisfies I ∧ B, but not I after one pass | missing extra facts | add the fact that the body needs |
| Postcondition at exit | a state that satisfies I ∧ ¬B, with the counter beyond its final value | missing bounds | add the range of the counter |
| Postcondition at exit | a state that satisfies I ∧ ¬B, with a wrong result | too weak | add the result computed so far, or a witness |

After each fix, check all three conditions again, since fixing one condition can break another.
