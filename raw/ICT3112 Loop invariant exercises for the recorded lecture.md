---
source_type: pdf-text-extract
original_file: ICT3112 - Loop invariant exercises for the recorded lecture.pdf
fetched: 2026-11-25
---

ICT3112 – Loop invariant exercises for the recorded lecture

Exercise 1 · Summing 1..n by counting down
This loop compute the sum of the n first numbers decreasing the counter.
{ n ≥ 0 }
i := n;
s := 0;
while (i > 0) {
    s := s + i;
    i := i - 1;
}
{ s = n(n+1)/2 }

Step 1 · Q and the progress variable
The progress variable is i, which starts at n and decreases by 1 on every pass until the guard i > 0
becomes false. The result variable is s, since Q constrains s at the end. The value of i when the loop stops
is 0, and this is the value that step 3 will replace.

Step 2 · Trace the loop head (n = 4)
At the loop head                          i               s               n(n+1)/2 − s

Before pass 1                             4               0               10

Before pass 2                             3               4               6

Before pass 3                             2               7               3

Before pass 4                             1               9               1

At exit                                   0               10              0

The values of s are 4, 4 + 3, 4 + 3 + 2 and so on, so s holds the sum of the numbers from i + 1 up to n,
which are the numbers the loop has already added. The last column shows what is still missing from the
total, and it runs 10, 6, 3, 1, 0, which is i(i+1)/2, the sum 1 + … + i of the numbers the loop has not added
yet.

Step 3 · Generalise the postcondition
If we use the invariant that we saw in the recorded lectures, I == s = i(i+1)/2, we observe that the trace
rejects this candidate at the first row, since i = 4 and s = 0 while 4·5/2 = 10. The undo-check also fails,
since substituting the final value i := 0 in s = i(i+1)/2 gives s = 0, which is not Q.

The reason is that the final value of i is 0, and Q does not show where that belongs to. We make it visible
by subtracting a term that is zero at exit, which leaves Q unchanged:
Q:    s = n(n+1)/2 − 0·(0+1)/2
Now we replace the final value 0 by the progress variable i:

s = n(n+1)/2 − i(i+1)/2
The undo-check passes, since i := 0 gives Q back, and the trace agrees on every row (for example, before
pass 3 we have 10 − 3 = 7). The equation can also be read as a conserved quantity, s + i(i+1)/2 =
n(n+1)/2, which says that what has been added plus what is still to be added is always the total.

Step 4 · Add the bounds
The progress variable starts at n and the guard stops it at 0, so the bounds are 0 ≤ i ≤ n. The bound that
matters at exit is 0 ≤ i, since the negated guard only gives i ≤ 0.
I:    s = n(n+1)/2 − i(i+1)/2          ∧   0 ≤ i ≤ n

Step 5 · Check the three obligations
Establishment. We must show n ≥ 0 ⇒ wp(i := n; s := 0, I), calculating from the last assignment.
wp(s := 0, I)      =   0 = n(n+1)/2 − i(i+1)/2           ∧   0 ≤ i ≤ n
wp(i := n, …)      =   0 = n(n+1)/2 − n(n+1)/2           ∧   0 ≤ n ≤ n
                   =   true ∧ n ≥ 0
                   =   n ≥ 0
Since n ≥ 0 ⇒ n ≥ 0, the invariant is established.

Preservation. We must show I ∧ i > 0 ⇒ wp(s := s + i; i := i − 1, I).
wp(i := i − 1, I)          =   s = n(n+1)/2 − (i−1)i/2 ∧ 0 ≤ i − 1 ≤ n
wp(s := s + i, …)          =   s + i = n(n+1)/2 − (i−1)i/2 ∧ 0 ≤ i − 1                  ∧   i − 1 ≤ n
For the equation, we start from s = n(n+1)/2 − i(i+1)/2, which I gives us, and add i to both sides:
s + i    =   n(n+1)/2 − (i² + i)/2 + 2i/2
         =   n(n+1)/2 − (i² − i)/2
         =   n(n+1)/2 − (i−1)i/2          ✓
For the bounds, the guard i > 0 gives i ≥ 1 since i is an integer, and as a consequence 0 ≤ i − 1. The upper
bound i ≤ n from I gives i − 1 ≤ n. In this loop the guard is needed for the lower bound, whereas in the
exam question it was needed for the upper bound.

Postcondition at exit. We must show I ∧ ¬(i > 0) ⇒ s = n(n+1)/2. The negated guard is i ≤ 0, and together
with 0 ≤ i from I it gives i = 0. Substituting i = 0 in the equation gives s = n(n+1)/2 − 0, which is Q.

Without 0 ≤ i the step fails. For example, i = −2 and s = n(n+1)/2 − 1 satisfy the equation (since (−2)(−1)/2
= 1) and i ≤ 0, but s is not n(n+1)/2.

Step 6 · Variant
The variant is V = i. While the loop runs, the guard gives i > 0, so V ≥ 0, and each pass executes i := i − 1,
so V decreases by exactly 1. A non-negative integer cannot decrease forever, so the loop terminates.

The rule “replace n by i” is a shortcut that only works when the progress variable ends at n. The general
rule is to replace the final value of the progress variable, and the undo-check (substitute the final value
back and obtain Q) catches the case where the shortcut gives the wrong candidate.

Exercise 2 · Sum of odd numbers with a helper variable
This loop computes n² as 1 + 3 + 5 + …, where the next odd number is kept in a separate variable k. As a
consequence, the first candidate from the recipe fails preservation.
{ n ≥ 0 }
i := 0;
s := 0;
k := 1;
while (i < n) {
    s := s + k;
    k := k + 2;
    i := i + 1;
}
{ s = n * n }

Step 1 · Q and the progress variable
The progress variable is i, which counts the passes from 0 up to n. The result variable is s, since Q
constrains s at the end. The variable k is a helper that changes in the body but does not appear in Q, so
we note it down, since helpers often matter later.

Step 2 · Trace the loop head (n = 4)
At the loop head                                      i                   s                    k

Before pass 1                                         0                   0                    1

Before pass 2                                         1                   1                    3

Before pass 3                                         2                   4                    5

Before pass 4                                         3                   9                    7

At exit                                               4                   16                   9

The values of s are 0, 1, 4, 9, 16, which are i·i. The values of k are 1, 3, 5, 7, 9, which are 2i + 1, so k
always holds the odd number that the next pass will add.

Steps 3 and 4 · Generalise and add the bounds: candidate I₁
Q mentions n twice, and deck 7 showed with s := s + n that not every occurrence of n has to be replaced.
The trace decides which ones. Replacing only one occurrence gives s = i · n, which is 4 before pass 2
while s is 1, so that choice is wrong. Replacing both gives s = i · i, which matches every row. Adding the
bounds gives the first candidate:
I₁:       s = i · i    ∧   0 ≤ i ≤ n

Step 5 · Check I₁
Establishment. Calculating backwards through k := 1, s := 0 and i := 0 gives 0 = 0 · 0 ∧ 0 ≤ 0 ≤ n, which is n
≥ 0, so the precondition implies it.

Preservation. We must show I₁ ∧ i < n ⇒ wp(s := s + k; k := k + 2; i := i + 1, I₁).

wp(i := i + 1, I₁)           =   s = (i+1)·(i+1) ∧ 0 ≤ i + 1 ≤ n
wp(k := k + 2, …)            =   s = (i+1)·(i+1) ∧ 0 ≤ i + 1 ≤ n                        (k does not occur)
wp(s := s + k, …)            =   s + k = (i+1)·(i+1) ∧ 0 ≤ i + 1 ≤ n
From I₁ we know s = i², so the equation we need is i² + k = i² + 2i + 1, which holds only when k = 2i + 1.
The candidate I₁ says nothing about k, so the implication cannot be proved. A concrete state shows the
gap: i = 0, s = 0, k = 5 and n = 3 satisfy I₁ and the guard, but after one pass s = 5 and i = 1, which breaks s =
i · i.

That state never occurs in a real run, since k really is 2i + 1 on every row of the trace. The failure is that I₁
does not record this fact, so the proof cannot use it. Following the diagnosis cheat-sheet, preservation
fails because the body needs a fact about a changing variable that I does not track.

Refine · Add the missing fact: candidate I₂
We go back to step 4 (“add the bounds and any missing facts”) and add the relation that the trace
already showed. It belongs in the other relations slot of the template, since it links k to i and is not
about a region of data.
I₂:       s = i · i     ∧   k = 2i + 1      ∧   0 ≤ i ≤ n

Step 5 again · Re-check I₂ from the start
Establishment. We must show n ≥ 0 ⇒ wp(i := 0; s := 0; k := 1, I₂).
wp(k := 1, I₂)          =   s = i · i ∧ 1 = 2i + 1 ∧ 0 ≤ i ≤ n
wp(s := 0, …)           =   0 = i · i ∧ 1 = 2i + 1 ∧ 0 ≤ i ≤ n
wp(i := 0, …)           =   0 = 0 ∧ 1 = 1 ∧ 0 ≤ 0 ≤ n
                        =   n ≥ 0
Preservation. We must show I₂ ∧ i < n ⇒ wp(s := s + k; k := k + 2; i := i + 1, I₂).
wp(i := i + 1, I₂)           =   s = (i+1)·(i+1) ∧ k = 2(i+1) + 1 ∧ 0 ≤ i + 1 ≤ n
wp(k := k + 2, …)            =   s = (i+1)·(i+1) ∧ k + 2 = 2i + 3 ∧ 0 ≤ i + 1 ≤ n
wp(s := s + k, …)            =   s + k = (i+1)·(i+1) ∧ k + 2 = 2i + 3 ∧ 0 ≤ i + 1 ≤ n
Each conjunct now follows from I₂ ∧ i < n:

      •   From s = i² and k = 2i + 1 we get s + k = i² + 2i + 1 = (i+1)².
      •   From k = 2i + 1 we get k + 2 = 2i + 3.
      •   From 0 ≤ i we get 0 ≤ i + 1, and since i and n are integers, i < n gives i + 1 ≤ n.

The two equations support each other in the same way as in the Fibonacci example, since the new value
of s uses the fact about k.

Postcondition at exit. The negated guard gives i ≥ n, and with i ≤ n from I₂ we obtain i = n, so s = i · i
becomes s = n · n, which is Q. The conjunct k = 2i + 1 is not used at exit; it is needed only for
preservation.

Step 6 · Variant
The variant is V = n − i, which is non-negative while the loop runs because i ≤ n, and which decreases by
1 on each pass because of i := i + 1.

Exercise 3 · Integer square root
This loop has no counter that runs to a fixed final value, since it stops as soon as the next square would
exceed n. As a consequence, step 3 cannot replace a constant by the progress variable, and we use
another way to obtain the invariant from Q: remove the conjunct of Q that the negated guard already
gives.
{ n ≥ 0 }
r := 0;
while ((r+1) * (r+1) ≤ n) {
    r := r + 1;
}
{ 0 ≤ r ∧ r * r ≤ n ∧ n < (r+1) * (r+1) }
The postcondition says that r is the largest non-negative integer whose square does not exceed n, so for
n = 10 the program must return r = 3.

Step 1 · Q and the progress variable
The progress variable is r, which increases by 1 on each pass. In this loop r is also the result variable,
since Q constrains r. The loop does not stop at a value written in the program, but when the guard
(r+1)·(r+1) ≤ n becomes false.

Step 2 · Trace the loop head (n = 10)
At the loop head               r          r·r         (r+1) · (r+1)           Guard (r+1)² ≤ 10

Before pass 1                  0          0           1                       true

Before pass 2                  1          1           4                       true

Before pass 3                  2          4           9                       true

At exit                        3          9           16                      false

On every row r ≥ 0 and r · r ≤ 10. The third conjunct of Q, 10 < (r+1)², is false on the first three rows (1, 4
and 9 are not greater than 10) and becomes true only at exit.

Step 3 · Generalise the postcondition
There is no final value to replace, so we look at the three conjuncts of Q one at a time:

    •     0 ≤ r holds on every row of the trace.
    •     r · r ≤ n holds on every row of the trace.
    •     n < (r+1) · (r+1) is exactly the negated guard ¬((r+1)·(r+1) ≤ n), and the trace shows that it is false
          at the loop head before every pass.

The third conjunct cannot be part of the invariant, since an invariant must be true at every loop head. It
does not need to be, since the while rule gives us ¬B at exit for free. We therefore keep the other two
conjuncts.

If we use Q itself as the invariant we observe that it is too strong. Establishment requires n ≥ 0 ⇒ wp(r :=
0, Q), and wp(r := 0, Q) = 0 ≤ 0 ∧ 0 ≤ n ∧ n < 1, which holds only when n = 0. For n = 10 the candidate is
false before the first pass.

Step 4 · The bounds
The progress variable starts at 0 and only increases, so 0 ≤ r is its lower bound. The conjunct r · r ≤ n
plays the role of the upper bound, since it says how far r may have travelled: never beyond the largest
value whose square fits in n. The invariant is therefore made only of bounds on r, which is possible
because the result of this loop is the final position of r itself.
I:    0 ≤ r    ∧   r · r ≤ n

Step 5 · Check the three obligations
Establishment. We must show n ≥ 0 ⇒ wp(r := 0, I).
wp(r := 0, I)      =   0 ≤ 0    ∧   0 · 0 ≤ n
                   =   n ≥ 0
Preservation. We must show I ∧ (r+1)·(r+1) ≤ n ⇒ wp(r := r + 1, I).
wp(r := r + 1, I)       =   0 ≤ r + 1     ∧   (r+1) · (r+1) ≤ n
The first conjunct follows from 0 ≤ r. The second conjunct is the guard itself, so the guard supplies
exactly the fact that the body needs. If we try to prove I ⇒ wp(r := r + 1, I) without the guard cannot
obtain (r+1)² ≤ n.

Postcondition at exit. We must show I ∧ ¬((r+1)·(r+1) ≤ n) ⇒ Q. The negated guard is n < (r+1)·(r+1), so
the left-hand side is 0 ≤ r ∧ r · r ≤ n ∧ n < (r+1)·(r+1), which is Q.

Step 6 · Variant
The variant is V = n − r. While the loop runs, the guard gives (r+1)² ≤ n, and since r + 1 ≥ 1 (from 0 ≤ r) we
have r + 1 ≤ (r+1)², so r + 1 ≤ n and V ≥ 1. Each pass executes r := r + 1, so V decreases by exactly 1. The
bound 0 ≤ r is used here, which gives a second reason to keep it, besides delivering the first conjunct of
Q.

When Q is a conjunction, compare each conjunct with the negated guard. The conjunct that ¬B gives at
exit stays out of the invariant, and the remaining conjuncts are the candidate.

Exercise 4 · multiplication by 2
All variables in this question are integers. Consider the following program:
1   { n ≥ 0 }
2   i := n;
3   s := 0;
4   while (i > 0) {
5       s := s + 2;
6       i := i - 1;
7   }
8   { s = 2 * n }
The proposed loop invariant is I: s + 2 * i = 2 * n ∧ 0 ≤ i ≤ n.

    •    a) Establishment. Show that the invariant holds before the first iteration, that is, prove { n ≥ 0 } i
         := n; s := 0 { I }.
    •    b) Preservation. Show that the loop body preserves the invariant.
    •    c) Postcondition at exit. Show that the invariant guarantees the postcondition when the loop
         exits. Explain which part of I is needed in this step and why.
    •    d) Give a variant for the loop and explain why it shows that the loop terminates.

a) Establishment. We must show n ≥ 0 ⇒ wp(i := n; s := 0, I), calculating from the last assignment.
wp(s := 0, I)                               =    (s + 2 * i = 2 * n ∧ 0 ≤ i ≤ n)[s ← 0]
                                            =    0 + 2 * i = 2 * n ∧ 0 ≤ i ≤ n

wp(i := n, 2 * i = 2 * n ∧ 0 ≤ i ≤ n)
                                = 2 * n = 2 * n ∧ 0 ≤ n ≤ n
                                = true ∧ 0 ≤ n
                                = n ≥ 0
Since n ≥ 0 ⇒ n ≥ 0, the invariant is established.



b) Preservation. The preservation triple is { I ∧ i > 0 } s := s + 2; i := i − 1 { I }, so we must show I ∧ i > 0 ⇒
wp(s := s + 2; i := i − 1, I).
wp(i := i − 1, I)           =   s + 2 * (i − 1) = 2 * n            ∧   0 ≤ i − 1 ≤ n

wp(s := s + 2, …)           =   (s + 2) + 2 * (i − 1) = 2 * n ∧ 0 ≤ i − 1 ≤ n
                            =   s + 2 * i = 2 * n ∧ 0 ≤ i − 1 ∧ i − 1 ≤ n
Implication: s + 2 * i = 2 * n ∧ 0 ≤ i ≤ n ∧ i > 0 ⇒ s + 2 * i = 2 * n ∧ 0 ≤ i − 1 ∧ i − 1 ≤ n.

The equation s + 2 * i = 2 * n appears in the hypothesis. Since i is an integer, i > 0 gives i ≥ 1, and as a
consequence 0 ≤ i − 1. The bound i ≤ n gives i − 1 ≤ n. Hence the invariant is preserved.

c) Postcondition at exit. The loop exits when ¬(i > 0), that is, i ≤ 0. We must show s + 2 * i = 2 * n ∧ 0 ≤ i ≤
n ∧ i ≤ 0 ⇒ s = 2 * n.

From 0 ≤ i and i ≤ 0 we obtain i = 0. Substituting i = 0 in s + 2 * i = 2 * n gives s = 2 * n.

The bound 0 ≤ i is the part of I that is needed, since the negated guard only gives i ≤ 0. Without it, the
exit does not give i = 0. For example, i = −1 and s = 2 * n + 2 satisfy s + 2 * i = 2 * n and i ≤ 0, but s ≠ 2 * n.

d) Variant. V = i.

V ≥ 0 while the loop runs, since the guard gives i > 0 (and the invariant gives 0 ≤ i). Each iteration
executes i := i − 1, so V decreases by exactly 1. A non-negative integer cannot decrease forever, so the
loop terminates.

Exercise 5 · 4*n+1
All variables in this question are integers. Consider the following program:
1    { n ≥ 0 }
2    i := 0;
3    s := 1;
4    while (i < n) {
5        s := s + 4;
6        i := i + 1;
7    }
8    { s = 4 * n + 1 }

Calculating the invariant:

Step 1 · Q and the progress variable. The progress variable is i, which counts the passes from 0 up to n,
so its final value is n. The result variable is s, since Q constrains s at the end.

Step 2 · Trace the loop head (n = 4). The table of part (a) gives the values below, and the last column
compares s with 4 * i.

At the loop head                                 i                s                s−4*i

Before iteration 1                               0                1                1

Before iteration 2                               1                5                1

Before iteration 3                               2                9                1

Before iteration 4                               3                13               1

At exit                                          4                17               1

Each pass adds 4 to s, and s starts at 1 instead of 0, so s is always 4 more than its value one row above
and 1 more than 4 * i. The relation that keeps the same shape on every row is therefore s = 4 * i + 1.

Step 3 · Generalise the postcondition. Q is s = 4 * n + 1, and n occurs once, as the number of passes,
since each pass adds 4. Replacing that final value n by the progress variable i gives:
s = 4 * i + 1
The undo-check passes, since substituting n for i in s = 4 * i + 1 gives s = 4 * n + 1, which is Q. The trace
also agrees on every row.

In an answer like s = 4 * i, the trace rejects it at the first row, since s = 1 while 4 * 0 = 0. The undo-check
rejects it as well, since substituting n for i in s = 4 * i gives s = 4 * n, which is not Q.

Step 4 · Add the bounds. The progress variable starts at 0 and the guard stops it at n, so the bounds are
0 ≤ i ≤ n. The bound that matters at exit is i ≤ n, since the negated guard only gives i ≥ n.
I:    s = 4 * i + 1       ∧   0 ≤ i ≤ n
Step 5 · Check the three obligations.

Establishment. We must show n ≥ 0 ⇒ wp(i := 0; s := 1, I), calculating from the last assignment.

wp(s := 1, I)         =   (s = 4 * i + 1 ∧ 0 ≤ i ≤ n)[s ← 1]
                      =   1 = 4 * i + 1 ∧ 0 ≤ i ≤ n

wp(i := 0, …)         =   1 = 4 * 0 + 1 ∧ 0 ≤ 0 ≤ n
                      =   true ∧ 0 ≤ n
                      =   n ≥ 0
Since n ≥ 0 ⇒ n ≥ 0, the invariant is established. For the wrong candidate s = 4 * i, the same calculation
gives 1 = 0 ∧ …, which is false, and n ≥ 0 does not imply false, so establishment fails.

Preservation. The preservation triple is { I ∧ i < n } s := s + 4; i := i + 1 { I }, so we must show I ∧ i < n ⇒
wp(s := s + 4; i := i + 1, I).
wp(i := i + 1, I)          =   s = 4 * (i + 1) + 1          ∧   0 ≤ i + 1 ≤ n

wp(s := s + 4, …)          =   s + 4 = 4 * (i + 1) + 1 ∧ 0 ≤ i + 1 ≤ n
                           =   s + 4 = 4 * i + 5 ∧ 0 ≤ i + 1 ≤ n
                           =   s = 4 * i + 1 ∧ 0 ≤ i + 1 ∧ i + 1 ≤ n
The last line subtracts 4 from both sides of the equation. Each conjunct now follows from I ∧ i < n:

    •    The equation s = 4 * i + 1 appears in I.
    •    From 0 ≤ i we get 0 ≤ i + 1.
    •    Since i and n are integers, the guard i < n gives i + 1 ≤ n. This is the only place where the guard is
         used, and without it the upper bound could not be preserved.

Postcondition at exit. We must show s = 4 * i + 1 ∧ 0 ≤ i ≤ n ∧ i ≥ n ⇒ s = 4 * n + 1. From i ≤ n and i ≥ n we
obtain i = n, and substituting i = n in s = 4 * i + 1 gives s = 4 * n + 1, which is Q.

Without i ≤ n the step fails. For example, i = n + 1 and s = 4 * n + 5 satisfy s = 4 * i + 1 and i ≥ n, but s ≠ 4 *
n + 1. The lower bound 0 ≤ i is not used in this step or in establishment, which is why the marking guide
accepts an answer without it.

Step 6 · Variant. The variant is V = n − i, which is non-negative while the loop runs because i ≤ n, and
which decreases by exactly 1 on each pass because of i := i + 1. Part (c) of the question does not ask for
it, but it completes the total-correctness argument in the recording.

Exercise 6 · Incrementing every cell of an array in place
This loop adds 1 to every cell of an array, and the body reads the cell a[i] before writing it. Since a[i]
belongs to the region the loop has not reached yet.
{ n = sizeof(a) ∧ a = a₀ }
i := 0;
while (i < n) {
    a[i] := a[i] + 1;
    i := i + 1;
}
{ ∀k. 0 ≤ k < n ⇒ a[k] = a₀[k] + 1 }
Here a₀ is a logical constant that records the array as it was before the loop, so Q can talk about the
original values. The program never assigns a₀, so a substitution for a never touches a₀.

Step 1 · Q and the progress variable
The progress variable is i, which runs from 0 up to n. The result is the array a itself, and Q describes
every cell of it.

Step 2 · Trace the loop head (a₀ = [5, 2, 7], n = 3)
At the loop head                                            i                   a

Before pass 1                                               0                   [5, 2, 7]

Before pass 2                                               1                   [6, 2, 7]

Before pass 3                                               2                   [6, 3, 7]

At exit                                                     3                   [6, 3, 8]

At every loop head the array has two regions. The cells with index below i already hold a₀[k] + 1, and the
cells from i onwards still hold their original value a₀[k].
index:      0 … i−1       | i … n−1
holds:      a₀[k] + 1     | a₀[k]
            produced so far | not touched yet

Steps 3 and 4 · Generalise and add the bounds: candidate I₁
The final value of i is n, and the n that marks the end of the range in Q is the one that counts the passes,
so we replace it by i. The undo-check passes, since i := n gives Q back.

Two more facts go in. The bounds are 0 ≤ i ≤ n. The body writes a[i], which requires def(a[i]), that is 0 ≤ i
< sizeof(a), and the proof can only use the precondition fact n = sizeof(a) inside the loop if I carries it.
Writing a cell does not change the number of cells, so this conjunct is preserved without effort.
I₁:       (∀k. 0 ≤ k < i ⇒ a[k] = a₀[k] + 1)            ∧       sizeof(a) = n   ∧   0 ≤ i ≤ n

Step 5 · Check I₁
Establishment holds, since after i := 0 the range 0 ≤ k < 0 is empty and 0 ≤ 0 ≤ n follows from n =
sizeof(a) ≥ 0.

Preservation. We calculate wp(a[i] := a[i] + 1; i := i + 1, I₁), writing aʹ for a[i ↦ a[i] + 1] to keep the lines
short.
wp(i := i + 1, I₁)                    =   (∀k. 0 ≤ k < i+1 ⇒ a[k] = a₀[k] + 1)                  ∧    sizeof(a) = n
∧ 0 ≤ i+1 ≤ n

wp(a[i] := a[i] + 1, …)               =   (∀k. 0 ≤ k < i+1 ⇒ aʹ[k] = a₀[k] + 1)                  ∧   sizeof(aʹ) =
n ∧ 0 ≤ i+1 ≤ n
                                          ∧   0 ≤ i < sizeof(a)
(definedness)
The quantified conjunct covers the cells 0 ≤ k < i + 1, which we split into the cells k < i and the cell k = i:

      •   For 0 ≤ k < i we have k ≠ i, so the second select-store axiom gives aʹ[k] = a[k], and a[k] = a₀[k] + 1
          is what I₁ says. ✓
      •   For k = i the first select-store axiom gives aʹ[i] = a[i] + 1, so we need a[i] + 1 = a₀[i] + 1, that is a[i]
          = a₀[i]. The candidate I₁ says nothing about cell i. ✗

A concrete state shows the gap: n = 3, i = 1, a₀ = [5, 2, 7] and a = [6, 9, 7] satisfy I₁ and the guard, but
after one pass a[1] = 10 while a₀[1] + 1 = 3. The real loop never reaches this state, but I₁ does not exclude
it, so the proof cannot go through.

The diagnosis is that the body reads a[i] from the region the loop has not reached, and I₁ does not record
that this region still holds its original values. This is exactly the case in which the not touched yet slot is
required.

Refine · Add the not touched yet slot: candidate I₂
I₂:     (∀k. 0 ≤ k < i ⇒ a[k] = a₀[k] + 1)                       produced so far
      ∧ (∀k. i ≤ k < n ⇒ a[k] = a₀[k])                           not touched yet
      ∧ sizeof(a) = n                                             other relations
      ∧ 0 ≤ i ≤ n                                                 bounds

Step 5 again · Re-check I₂ from the start
Establishment. We must show n = sizeof(a) ∧ a = a₀ ⇒ wp(i := 0, I₂).
wp(i := 0, I₂)         = (∀k. 0 ≤ k < 0 ⇒ a[k] = a₀[k] + 1)
                        ∧ (∀k. 0 ≤ k < n ⇒ a[k] = a₀[k])
                        ∧ sizeof(a) = n ∧ 0 ≤ 0 ≤ n
The first conjunct is true because its range is empty. The second follows from a = a₀. The last two follow
from n = sizeof(a), since a size is never negative.

Preservation. We must show I₂ ∧ i < n ⇒ wp(a[i] := a[i] + 1; i := i + 1, I₂), with aʹ = a[i ↦ a[i] + 1] as before.
wp(…, I₂)       = (∀k. 0 ≤ k < i+1 ⇒ aʹ[k] = a₀[k] + 1)
                 ∧ (∀k. i+1 ≤ k < n ⇒ aʹ[k] = a₀[k])
                 ∧ sizeof(aʹ) = n ∧ 0 ≤ i+1 ≤ n
                 ∧ 0 ≤ i < sizeof(a)
Each conjunct now follows from I₂ ∧ i < n:

      •   Definedness. 0 ≤ i comes from the bounds, and i < n = sizeof(a) comes from the guard and the
          size conjunct.

    •   Produced so far, k < i. Since k ≠ i, aʹ[k] = a[k] = a₀[k] + 1 by the first conjunct of I₂.
    •   Produced so far, k = i. aʹ[i] = a[i] + 1, and the not touched yet conjunct with k = i gives a[i] = a₀[i],
        which we may use since i ≤ i < n by the guard. So aʹ[i] = a₀[i] + 1.
    •   Not touched yet. For i + 1 ≤ k < n we have k ≠ i, so aʹ[k] = a[k], and a[k] = a₀[k] by the second
        conjunct of I₂, since the range i + 1 ≤ k < n lies inside i ≤ k < n.
    •   Size. aʹ has the same cells as a, so sizeof(aʹ) = sizeof(a) = n.
    •   Bounds. 0 ≤ i gives 0 ≤ i + 1, and since i and n are integers, i < n gives i + 1 ≤ n.

The write moves cell i from the not touched yet region into the produced so far region, and the select-
store axioms are what show that no other cell changes.

Postcondition at exit. The negated guard gives i ≥ n, and with i ≤ n we get i = n. The first conjunct
becomes ∀k. 0 ≤ k < n ⇒ a[k] = a₀[k] + 1, which is Q, and the second conjunct now has the empty range n
≤ k < n, so it says nothing.

Step 6 · Variant
The variant is V = n − i, which is non-negative because i ≤ n and decreases by 1 on each pass.

