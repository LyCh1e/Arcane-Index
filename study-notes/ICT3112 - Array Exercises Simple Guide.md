# ICT3112 Array Exercises: The Simple Version

## The big idea in one sentence

When a program reads or writes an array, you must prove two things: the **maths works out**, and **every index is inside the array** (no out-of-bounds).

---

## Part 0: The three tools you need

### Tool 1: Reading an array (`x := a[i]`)

Do exactly what you'd do for a normal assignment: replace `x` in the postcondition with `a[i]`.
Then add one extra check: **is `i` a valid index?**

> **Valid index** means `0 ≤ i < sizeof(a)`. This is written `def(a[i])` ("a[i] is defined").

**Rule of thumb:** one bounds check for **every** array read you see.

### Tool 2: Writing an array (`a[i] := E`)

You can't just "replace `a[i]`". Instead, you treat the **whole array** as becoming a new array:

```
a[i ↦ E]   =   "array a, but cell i now holds E"
```

So you replace every `a` in the postcondition with `a[i ↦ E]`.

### Tool 3: Reading from the new array (select–store)

Once you have `a[i ↦ E][j]`, ask one question: **is `j` the cell that was written?**

| Case | Answer | Think of it as |
|---|---|---|
| `j = i` | `E` | You read the cell you just wrote, so you get the new value |
| `j ≠ i` | `a[j]` | You read some other cell, which hasn't changed |

If the program doesn't tell you whether `j = i`, **keep both cases** and join them with "or":

```
(j = i ∧ …) ∨ (j ≠ i ∧ …)
```

### The 3-step recipe for any array write

1. **Substitute:** replace `a` with `a[i ↦ E]`.
2. **Simplify:** use the table above (split into cases if needed).
3. **Bounds:** add `0 ≤ i < sizeof(a)`, plus a bounds check for every array read inside `E`. Put brackets around step 2 first.

---

## Exercise 1: Two reads, no writes

```
{ 0 ≤ i ∧ i+1 < sizeof(a) }
x := a[i+1] − a[i]
{ x + a[i] = a[i+1] }
```

**In plain words:** `x` is the gap between two neighbouring cells. Prove that adding the gap back to the left cell gives the right cell.

**Step 1: Substitute `x`.**
```
a[i+1] − a[i] + a[i] = a[i+1]
```
The `− a[i]` and `+ a[i]` cancel, leaving `a[i+1] = a[i+1]`, which is **always true**.

**Step 2: Add bounds checks.** There are two reads, `a[i+1]` and `a[i]`, so there are two checks:
```
0 ≤ i+1 < sizeof(a)   and   0 ≤ i < sizeof(a)
```
These simplify to `0 ≤ i ∧ i+1 < sizeof(a)`.

**Step 3: Compare.** That's exactly the precondition. ✓

**Lesson:** sometimes the maths is trivially true and the **only** thing that matters is the bounds.

**Trap:** if the precondition were just `0 ≤ i < sizeof(a)`, it fails. With `a = [4, 7]` and `i = 1`, the program reads `a[2]`, which doesn't exist.

---

## Exercise 2: Read, then write

```
{ 0 ≤ i < sizeof(a) ∧ 0 ≤ j < sizeof(a) ∧ a[j] > 0 }
x := 2 * a[j];
a[i] := x
{ a[i] ≥ a[j] }
```

**In plain words:** double `a[j]` and store it in cell `i`. Prove cell `i` ends up at least as big as cell `j`.

Work **backwards** from the last line.

**Step 1: Handle `a[i] := x` (the write).**
Replace `a` with `a[i ↦ x]`:
```
a[i ↦ x][i]  ≥  a[i ↦ x][j]
```

**Step 2: Simplify each read.**
- Left side reads cell `i`, which is the written cell, so it's `x`.
- Right side reads cell `j`. We don't know whether `j = i`, so we split:
  - if `j = i`: it's `x`, giving `x ≥ x`, which is always true
  - if `j ≠ i`: it's `a[j]`, giving `x ≥ a[j]`

Joined: `j = i  ∨  x ≥ a[j]`

**Step 3: Add bounds** (brackets first):
```
(j = i ∨ x ≥ a[j]) ∧ 0 ≤ i < sizeof(a)
```

**Step 4: Handle `x := 2 * a[j]` (the read).** Replace `x` with `2·a[j]`:
```
(j = i ∨ 2·a[j] ≥ a[j]) ∧ bounds
```
`2·a[j] ≥ a[j]` is the same as `a[j] ≥ 0`. So the result is:
```
(j = i ∨ a[j] ≥ 0) ∧ 0 ≤ i < sizeof(a) ∧ 0 ≤ j < sizeof(a)
```

**Step 5: Check the precondition.** It gives `a[j] > 0`, which means `a[j] ≥ 0`. ✓

**Trap (exam favourite):** what if the precondition said `a[i] > 0` instead?
That's a fact about the cell that gets **overwritten**, so it's useless.
Counterexample: `i = 0`, `j = 1`, `a = [3, −2]`. Then `x = −4` and `a` becomes `[−4, −2]`, so `−4 ≥ −2` is **false**. ✗

---

## Exercise 3: Dot product loop

```
{ sizeof(a) = n ∧ sizeof(b) = n }
i := 0; s := 0;
while (i < n) {
    s := s + a[i] * b[i];
    i := i + 1;
}
{ s = a[0]·b[0] + a[1]·b[1] + … + a[n−1]·b[n−1] }
```

**In plain words:** multiply matching cells and add them all up.

### Find the invariant: "what's true every time we're at the top of the loop?"

Trace with `a = [2, −1, 3]` and `b = [4, 5, 1]`:

| i | s | s is the sum of… |
|---|---|---|
| 0 | 0 | nothing yet |
| 1 | 8 | 2·4 |
| 2 | 3 | 2·4 + (−1)·5 |
| 3 | 6 | 2·4 + (−1)·5 + 3·1 |

So `s` = the sum of the **first `i` pairs** (cells 0 up to `i − 1`).

**Invariant:**
```
s = Σ(k = 0 .. i−1) a[k]·b[k]     ← the sum so far
∧ sizeof(a) = n ∧ sizeof(b) = n   ← sizes (needed for bounds!)
∧ 0 ≤ i ≤ n                       ← i stays in range
```

### Why do the sizes go in the invariant?

Inside the loop you can **only** use the invariant and the guard (`i < n`). The body reads `a[i]` and `b[i]`, so you need `i < sizeof(a)`. You get it from `i < n` and `sizeof(a) = n`, but only if the size fact is in the invariant.

### The four checks

| Check | Why it works |
|---|---|
| **Start** (true before the loop) | `i = 0`, so the sum of nothing is `0 = s` ✓ |
| **Keep** (stays true after one pass) | New sum = old sum + `a[i]·b[i]`, which is exactly what the body adds ✓ |
| **Finish** (gives the postcondition) | Loop stops when `i ≥ n`; with `i ≤ n` that means `i = n`, so the sum covers all `n` pairs ✓ |
| **Stops** (variant) | `n − i` goes down by 1 each pass and is never negative while looping ✓ |

**Trap:** if the guard were `i ≤ n`, the last pass would read `a[n]`, which is out of bounds. The proof catches the bug because the bounds check `n < n` is false.

---

## Exercise 4: Writing into a second array

```
{ sizeof(a) = n ∧ sizeof(b) = n }
i := 0;
while (i < n) {
    b[i] := 2 * a[i];
    i := i + 1;
}
{ every b[k] = 2·a[k] }
```

**In plain words:** fill `b` with double each value of `a`.

### Invariant: "the cells we've filled so far are correct"

```
(∀k. 0 ≤ k < i ⇒ b[k] = 2·a[k])    ← cells 0 to i−1 are done
∧ sizeof(a) = n ∧ sizeof(b) = n     ← sizes
∧ 0 ≤ i ≤ n                         ← range
```

Picture it like this:

```
index:  0   1   …   i−1  |  i   …   n−1
        done ✓ done ✓     |  not filled yet
```

### The key step (Keep check)

After one pass, cell `i` is written and `i` goes up by 1. So we need cells `0 … i` to be correct.
- For the **new cell** `k = i`: it holds `2·a[i]`, and we need `2·a[i]`. ✓ (true automatically)
- For the **old cells** `k < i`: they weren't touched, so they're still correct from the invariant. ✓

### The other checks
- **Start:** `i = 0`, so "cells 0 to −1 are correct" is about no cells at all, which is automatically true.
- **Finish:** `i = n`, so all cells are correct.
- **Stops:** variant `n − i`.

**Trap (aliasing):** this only works if `a` and `b` are **different arrays**. If they point to the same memory in C, writing `b[i]` also changes `a[i]`, and the proof breaks. (Frama-C uses `\separated` to rule this out.)

---

## Cheat sheet

| If you see… | Do this |
|---|---|
| A read `a[i]` | Add `0 ≤ i < sizeof(a)` |
| A write `a[i] := E` | Replace `a` with `a[i ↦ E]` |
| `a[i ↦ E][j]` and you don't know if `j = i` | Split: `(j = i ∧ …) ∨ (j ≠ i ∧ …)` |
| A loop over an array | Put `sizeof(a) = n` in the invariant |
| A loop that fills cells | Invariant: "cells `0 … i−1` are done" |
| A loop that reads the same cell it writes (`a[i] := a[i] + 1`) | Also add "cells `i … n−1` are untouched" |
| Guard `i ≤ n` on an array loop | Probably a bug: reads `a[n]` |
