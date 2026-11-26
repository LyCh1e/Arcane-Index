# Loop Invariants and Variants: The Simple Version

## 1. What are we trying to prove?

A loop proof answers two questions:

| Question | Tool |
|---|---|
| Does the loop give the **right answer**? | The **invariant** |
| Does the loop **ever stop**? | The **variant** |

### Invariant

A statement that is **true every time the loop reaches its check** (`while (...)`):
before the first pass, after every pass, and when it exits.

> Think of it as a **progress report**: "here's what I've done so far".

### Variant

A **number that goes down every pass** and **can't go below 0** while the loop runs.

> Think of it as a **countdown**: "this many steps left". A countdown can't run forever.

---

## 2. How to FIND the invariant (5 steps)

### Step 1: Find the progress variable and its exit value

The **progress variable** is the counter that moves every pass (`i`, `a`, `r`…).
Ask: **what value does it have when the loop stops?**

- `i := 0; while (i < n) … i := i + 1` → exits at `i = n`
- `i := n; while (i > 0) … i := i − 1` → exits at `i = 0`

### Step 2: Rewrite the postcondition with that exit value, then swap it for the variable

The postcondition is true at the **end**. The invariant is the same statement, but for the
**middle** of the loop. So:

1. Make the exit value visible in the postcondition.
2. Replace the exit value with the progress variable.

> Example: postcondition `s = 2·n`, loop exits at `i = n`, so replace `n` with `i`: `s = 2·i`.

### Step 3: Check with a trace table

Pick small numbers. Write the variables at **each check** of the loop head.
Add a column for your formula. **Every row must match.**

### Step 4: Add the bounds

Write where the counter starts and where it stops, e.g. `0 ≤ i ≤ n`.
You need this at the exit, to turn "guard is false" into "counter = exit value".

### Step 5: Undo-check

Put the exit value back into your invariant. You must get the postcondition.
If you don't, the invariant is wrong.

---

## 2b. For arrays: draw the data (from the lecture slides)

When the loop walks through an array, the "replace n with i" trick isn't enough. Draw a picture instead.

**Step 1: Draw the data and mark where the progress variable is.**

```
0                       i                       n
+-----------------------+-----------------------+
|        visited        |      not visited      |
+-----------------------+-----------------------+
  what Q asks for,        what is still true here,
  restricted to this part usually the original values
```

**Step 2: Write what is true in each region.**

- **Visited:** the postcondition, but only for cells `0 … i−1`.
- **Not visited:** what is still true there, usually "the cells still hold their original values" (`A[k] = A₀[k]`).

**Step 3: Add the bounds of the progress variable** (e.g. `0 ≤ i ≤ n`).

```
I  =  (visited)  ∧  (not visited)  ∧  (0 ≤ i ≤ n)
```

> **Array sum:** visited is `s = A[0] + … + A[i−1]`. Not visited has nothing to say, because the loop
> only **reads** `A`. Bounds: `0 ≤ i ≤ n`.

## 2c. The four-slot template

Every invariant from the course fits into **four slots**. Fill the ones that apply:

| Slot | What goes in it |
|---|---|
| **Visited** | What Q says, restricted to the part already processed |
| **Not visited** | What is still true in the unprocessed part (usually the original values) |
| **Other relations** | Facts that are not about one region (equations linking variables, permutation facts) |
| **Bounds** | The range of the progress variable. **Always filled.** |

How the course's loops fill the slots:

| Loop | Visited | Not visited | Other relations | Bounds |
|---|---|---|---|---|
| Countdown with a counter | — | — | `c + x = C + X` | `x ≥ 0` |
| Integer division | — | — | `a = b·q + r` | `0 ≤ r` |
| Array sum | `s = A[0] + … + A[i−1]` | — (only reads `A`) | — | `0 ≤ i ≤ n` |
| Zero-fill | `A[k] = 0` for `k < i` | `A[k] = A₀[k]` for `k ≥ i` | — | `0 ≤ i ≤ m` |
| Reverse in place | front and back swapped | middle: `A[k] = A₀[k]` | `l + r = n − 1` | on `l` and `r` |
| Selection sort | sorted prefix | — | `perm(A, A₀)`, prefix ≤ rest | `0 ≤ i ≤ n` |

The examples in this file fit the same slots:

| Example | Visited | Not visited | Other relations | Bounds |
|---|---|---|---|---|
| 1 (easy) | — | — | `s = 2·i` | `0 ≤ i ≤ n` |
| 2 (medium) | — | — | `s = n(n+1)/2 − i(i+1)/2` | `0 ≤ i ≤ n` |
| 3 (hard) | `a[k] = a₀[k] + 1` for `k < i` | `a[k] = a₀[k]` for `k ≥ i` | `sizeof(a) = n` | `0 ≤ i ≤ n` |

**Quick rule:** if the loop only reads the array, the not-visited slot is empty. If it writes the array, you almost always need it.

---

## 3. How to PROVE it (the 4 checks)

| # | Check | You assume | You show | How |
|---|---|---|---|---|
| 1 | **Start** (establishment) | The precondition | `I` holds before the loop | Substitute the start-up assignments into `I`, simplify |
| 2 | **Keep** (preservation) | `I` **and** the guard | `I` holds after one pass | Work backwards through the body (substitute), then use `I` + guard |
| 3 | **Finish** (exit) | `I` **and** NOT guard | The postcondition | Combine `¬guard` with the bounds to get the exit value, substitute |
| 4 | **Stop** (termination) | `I` **and** the guard | Variant `≥ 0` and it goes down | Usually: guard gives `≥ 0`; body changes counter by 1 |

### The substitution trick (used in checks 1 and 2)

To see what must be true **before** `x := E`, take the statement you want **after** it,
and replace every `x` with `E`.

```
want after:   s = 2·i
statement:    i := i + 1
need before:  s = 2·(i + 1)
```

With several statements, start from the **last** one and work **upwards**.

### Choosing the variant (quick rule)

Read it off the guard:

| Guard | Try the variant |
|---|---|
| `i < n` or `i <= n` (counting up) | `n − i` (or `n + 1 − i` for `<=`) |
| `i > 0` (counting down) | `i` |
| `s <= n` (something growing) | `n − s` |

---

## 4. Example 1 (Easy): Adding 2 each time

```
{ n ≥ 0 }
i := 0;
s := 0;
while (i < n) do {
    s := s + 2;
    i := i + 1;
}
{ s = 2·n }
```

### Find the invariant

**Step 1:** progress variable is `i`. It starts at 0 and exits at `i = n`.

**Step 2:** postcondition `s = 2·n`, so replace `n` with `i` and get `s = 2·i`.

**Step 3:** trace with `n = 3`:

| At the check | i | s | 2·i |
|---|---|---|---|
| before pass 1 | 0 | 0 | 0 ✓ |
| before pass 2 | 1 | 2 | 2 ✓ |
| before pass 3 | 2 | 4 | 4 ✓ |
| at exit | 3 | 6 | 6 ✓ |

**Step 4:** `i` goes from 0 to `n`, so the bounds are `0 ≤ i ≤ n`.

```
Invariant  I:  s = 2·i  ∧  0 ≤ i ≤ n
Variant    V:  n − i
```

**Step 5 (undo-check):** put `i = n` in and get `s = 2·n`. ✓

### Prove it

**1. Start.** Substitute `i := 0; s := 0` into `I`:
`0 = 2·0 ∧ 0 ≤ 0 ≤ n`. The first two parts are always true, and `0 ≤ n` comes from the precondition. ✓

**2. Keep.** Assume `s = 2·i ∧ 0 ≤ i ≤ n ∧ i < n`.
Work backwards through the body:
- after `i := i + 1` we need `s = 2·(i+1) ∧ 0 ≤ i+1 ≤ n`
- after `s := s + 2` we need `s + 2 = 2·(i+1) ∧ 0 ≤ i+1 ≤ n`

Show it:
- `s + 2 = 2i + 2 = 2(i+1)` ✓ (using `s = 2i`)
- `0 ≤ i+1` ✓ (since `0 ≤ i`)
- `i+1 ≤ n` ✓ (from the **guard** `i < n`)

**3. Finish.** Assume `I ∧ i ≥ n`.
`i ≥ n` and `i ≤ n` give `i = n`, so `s = 2·n`. ✓

**4. Stop.** `V = n − i`.
- Guard `i < n` gives `n − i > 0`. ✓
- `i` goes up by 1, so `V` goes down by 1. ✓

---

## 5. Example 2 (Medium): Counting down

```
{ n ≥ 0 }
i := n;
s := 0;
while (i > 0) do {
    s := s + i;
    i := i − 1;
}
{ s = n(n+1)/2 }
```

The loop adds `n + (n−1) + … + 1`.

### The trap

The easy shortcut "replace `n` with `i`" gives `s = i(i+1)/2`. **This is wrong.**
Trace row 1: `i = n`, `s = 0`, but `n(n+1)/2 ≠ 0`. ✗

Why? This loop counts **down**, so it exits at `i = 0`, **not** `i = n`.
You must replace the **exit value** (0), not `n`.

### Find the invariant

**Step 1:** progress variable is `i`. It starts at `n` and exits at `i = 0`.

**Step 2:** make the exit value 0 visible in the postcondition. Subtracting a term that equals 0 at exit changes nothing:

```
s = n(n+1)/2 − 0·(0+1)/2
```

Now replace the 0s with `i`:

```
s = n(n+1)/2 − i(i+1)/2
```

In words: **what's been added = total − what's still left to add**.

**Step 3:** trace with `n = 4` (total = 10):

| At the check | i | s | 10 − i(i+1)/2 |
|---|---|---|---|
| before pass 1 | 4 | 0 | 10 − 10 = 0 ✓ |
| before pass 2 | 3 | 4 | 10 − 6 = 4 ✓ |
| before pass 3 | 2 | 7 | 10 − 3 = 7 ✓ |
| before pass 4 | 1 | 9 | 10 − 1 = 9 ✓ |
| at exit | 0 | 10 | 10 − 0 = 10 ✓ |

**Step 4:** `i` goes from `n` down to 0, so the bounds are `0 ≤ i ≤ n`.

```
Invariant  I:  s = n(n+1)/2 − i(i+1)/2  ∧  0 ≤ i ≤ n
Variant    V:  i
```

**Step 5 (undo-check):** put `i = 0` in and get `s = n(n+1)/2 − 0`. ✓

### Prove it

**1. Start.** Substitute `i := n; s := 0`:
`0 = n(n+1)/2 − n(n+1)/2 ∧ 0 ≤ n ≤ n`. The equation is `0 = 0` ✓, and `0 ≤ n` comes from the precondition. ✓

**2. Keep.** Assume `I ∧ i > 0`.
Work backwards:
- after `i := i − 1` we need `s = n(n+1)/2 − (i−1)i/2 ∧ 0 ≤ i−1 ≤ n`
- after `s := s + i` we need `s + i = n(n+1)/2 − (i−1)i/2 ∧ 0 ≤ i−1 ≤ n`

Show the equation, using `s = n(n+1)/2 − i(i+1)/2`:

```
s + i = n(n+1)/2 − (i² + i)/2 + i
      = n(n+1)/2 − (i² + i − 2i)/2
      = n(n+1)/2 − (i² − i)/2
      = n(n+1)/2 − (i−1)i/2   ✓
```

Bounds:
- `0 ≤ i − 1` ✓ (from the **guard** `i > 0`, so `i ≥ 1`)
- `i − 1 ≤ n` ✓ (since `i ≤ n`)

**3. Finish.** Assume `I ∧ i ≤ 0`.
`i ≤ 0` and `0 ≤ i` give `i = 0`, so `s = n(n+1)/2`. ✓

Notice the **lower** bound `0 ≤ i` does the work here (in Example 1 it was the upper bound).

**4. Stop.** `V = i`.
- Guard `i > 0` gives `V > 0`. ✓
- `i` goes down by 1 each pass. ✓

---

## 6. Example 3 (Hard): Adding 1 to every array cell

```
{ sizeof(a) = n ∧ a = a₀ }
i := 0;
while (i < n) do {
    a[i] := a[i] + 1;
    i := i + 1;
}
{ ∀k. 0 ≤ k < n ⇒ a[k] = a₀[k] + 1 }
```

`a₀` is a name for the **original** array, so we can talk about "the old values".

### Find the invariant

**Step 1:** progress variable is `i`. It goes from 0 to `n`.

**Step 2:** postcondition says "cells 0 to n−1 are +1". Replace `n` with `i`:

```
∀k. 0 ≤ k < i ⇒ a[k] = a₀[k] + 1      ("cells done so far are +1")
```

**Step 3:** picture the array at the check:

```
index:   0  …  i−1   |   i  …  n−1
holds:   a₀[k] + 1   |   a₀[k]
         done ✓      |   not touched yet
```

Trace with `a₀ = [5, 2, 7]`:

| At the check | i | a |
|---|---|---|
| before pass 1 | 0 | [5, 2, 7] |
| before pass 2 | 1 | [**6**, 2, 7] |
| before pass 3 | 2 | [**6**, **3**, 7] |
| at exit | 3 | [**6**, **3**, **8**] |

**Step 4:** bounds `0 ≤ i ≤ n`. Arrays also need the size fact `sizeof(a) = n`,
because the body reads `a[i]` and must prove `i` is a valid index.

### The trap: "done so far" is not enough

Try `I₁: (∀k. 0 ≤ k < i ⇒ a[k] = a₀[k] + 1) ∧ sizeof(a) = n ∧ 0 ≤ i ≤ n`.

The **Keep** check fails. The body reads `a[i]` and adds 1, so to get `a₀[i] + 1`
you need to know `a[i] = a₀[i]` (that cell hasn't been changed yet). `I₁` says nothing about cell `i`.

Counterexample state: `n = 3, i = 1, a₀ = [5, 2, 7], a = [6, 9, 7]`.
It satisfies `I₁` (cell 0 is correct), but after one pass `a[1] = 10`, not `3`. ✗

**Fix:** add the "not touched yet" part:

```
Invariant  I:  (∀k. 0 ≤ k < i ⇒ a[k] = a₀[k] + 1)     ← done so far
             ∧ (∀k. i ≤ k < n ⇒ a[k] = a₀[k])          ← not touched yet
             ∧ sizeof(a) = n                           ← size
             ∧ 0 ≤ i ≤ n                               ← bounds
Variant    V:  n − i
```

> **Rule:** if the body **reads the same cell it writes**, you need the "not touched yet" part.

### Prove it

**1. Start.** `i = 0` and `a = a₀`:
- "done so far" is `∀k. 0 ≤ k < 0 …`, which covers **no cells**, so it's automatically true ✓
- "not touched yet" is `∀k. 0 ≤ k < n ⇒ a[k] = a₀[k]`, true because `a = a₀` ✓
- `sizeof(a) = n` and `0 ≤ 0 ≤ n` come from the precondition ✓

**2. Keep.** Assume `I ∧ i < n`. After one pass, cell `i` has been written and `i` is one bigger.
Check each cell `k` in the new array:

| Cell | What happened | Why it's correct |
|---|---|---|
| `k < i` | not written | was `a₀[k] + 1` by "done so far" ✓ |
| `k = i` | written: `a[i] + 1` | `a[i] = a₀[i]` by "not touched yet", so the new value is `a₀[i] + 1` ✓ |
| `k > i` | not written | still `a₀[k]` by "not touched yet" ✓ |

So the new "done so far" covers `0 … i`, and "not touched yet" covers `i+1 … n−1`, which matches `I` with `i + 1`. ✓

Also:
- valid index: `0 ≤ i` (from `I`) and `i < n = sizeof(a)` (guard + size) ✓
- the write doesn't change the size, so `sizeof(a) = n` stays ✓
- `i + 1 ≤ n` from the **guard** ✓

(Formally this uses select–store: reading `a[i ↦ E][k]` gives `E` if `k = i`, else `a[k]`.)

**3. Finish.** Assume `I ∧ i ≥ n`. So `i = n`.
- "done so far" becomes `∀k. 0 ≤ k < n ⇒ a[k] = a₀[k] + 1`, which is the postcondition ✓
- "not touched yet" covers `n … n−1`, no cells (fine) ✓

**4. Stop.** `V = n − i`: guard gives `> 0`, and `i` goes up by 1. ✓

---

## 7. When it goes wrong (from the lecture slides)

### The four common mistakes

| Mistake | What it looks like |
|---|---|
| **Too weak** | It's true and it's kept, but `I ∧ ¬B` does **not** give `Q`. It doesn't say enough |
| **Too strong** | It's close to `Q`, but it's **false before the first pass** |
| **Missing bounds** | You found the loop's equation, but not the facts that fix the counter's final value |
| **Missing extra facts** | In max or search loops one equation isn't enough: you also need facts about the prefix, or a **witness** (a position where the answer was found) |

### What to do when a check fails (4 steps)

1. **Say which check fails:** establishment (start), preservation (keep), or the postcondition at exit (finish).
2. **Write down a concrete bad state**, with a number for **every** variable.
3. **Ask what the state tells you:**
   - The candidate **rejects a real state**, so it's **too strong**. **Weaken** it.
   - The candidate **accepts a wrong state**, so it's **too weak**. **Add the fact that rules the state out.**
4. **Change the candidate, then check all three conditions again.** Fixing one can break another.

Establishment failures give the first kind of state (real but rejected). Preservation and exit failures give the second kind (wrong but accepted).

### Which check fails, and how to fix it

| Check that fails | The bad state | Problem | Fix |
|---|---|---|---|
| **Establishment** | A real state at the first loop check that the candidate rejects | Too strong | Weaken: replace constants by progress variables |
| **Preservation** | A state that satisfies `I ∧ B`, but not `I` after one pass | Missing extra facts | Add the fact the body needs |
| **Exit** | A state that satisfies `I ∧ ¬B`, with the counter **beyond** its final value | Missing bounds | Add the range of the counter |
| **Exit** | A state that satisfies `I ∧ ¬B`, with a **wrong result** | Too weak | Add the result computed so far, or a witness |

### The bad states from this file's examples

| Example | Bad candidate | Check that fails | Bad state | Fix |
|---|---|---|---|---|
| 2 (medium) | `s = i(i+1)/2` | Establishment | `n = 4, i = 4, s = 0` (real, but `0 ≠ 10`) | Weaken: subtract the part still to add, `n(n+1)/2 − i(i+1)/2` |
| 2 (medium) | equation without `0 ≤ i` | Exit | `n = 4, i = −2, s = 9` (counter past 0, and `9 ≠ 10`) | Add the bound `0 ≤ i` |
| 3 (hard) | visited part only | Preservation | `n = 3, i = 1, a₀ = [5,2,7], a = [6,9,7]` | Add the not-visited slot `a[k] = a₀[k]` for `k ≥ i` |

### Other quick checks

| Symptom | Fix |
|---|---|
| Trace row 1 or the **undo-check** doesn't match | Did you replace the **exit value**? (Count-down loops exit at 0) |
| Part of `Q` is exactly "NOT guard" | Leave that part out of `I`, or establishment fails |
| Array read can't be proved in bounds | Add `sizeof(a) = n` to `I` |

---

## 8. Exam answer template

```
Invariant  I:  <formula>  ∧  <bounds>
Variant    V:  <expression>

1. Start:   Pre ⇒ I[after start-up assignments]      — show by substitution
2. Keep:    I ∧ B ⇒ I[after body]                    — substitute bottom-up, use guard
3. Finish:  I ∧ ¬B ⇒ Post                            — ¬B + bounds give exit value
4. Stop:    I ∧ B ⇒ V ≥ 0, and V decreases each pass
```

Always include a **trace table**. It's quick, it earns marks, and it catches wrong guesses before
you waste time on the proof.
