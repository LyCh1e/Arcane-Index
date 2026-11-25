---
source_type: pdf-text-extract
original_file: ICT3112 - Array exercises with solutions.pdf
fetched: 2026-11-25
---

ICT3112 – Array exercises with solutions
In these exercises we use the two rules for arrays that we saw in the lecture, together with the select–
store axioms. The first two exercises have no loop, so we only apply the rules to one or two statements.
In the last three exercises the array accesses are inside a loop, so we also need to find a loop invariant
and prove it, following the same recipe that we used in the lecture on loop invariants.

The two rules are:
[ARRAY-READ]          { Q[x ← E] ∧ def(E) }          x := E     { Q }

[ARRAY-ASSIGN]        { Q[a ← a[I ↦ E]] ∧ def(a[I]) ∧ def(E) }                  a[I] := E     { Q }
In these rules, a[I ↦ E] is the array a where position I now holds the value E, and def(a[I]) is the
condition 0 ≤ I < sizeof(a), which says that position I exists in the array. The condition def(E) joins with ∧
one condition def(b[J]) for every array read b[J] that appears in E, and it is simply true when E does not
read any array.

When we read a position of an updated array, the select–store axioms give us its value:
a[I ↦ E][J] = E                if J = I
a[I ↦ E][J] = a[J]             if J ≠ I
Remember that the weakest precondition of a sequence of statements is calculated from the last
statement to the first. In all the exercises, two arrays with different names are different arrays, so a
write to b never changes a.

Try each exercise on your own before you read its solution.

Exercise 1: Reading two cells of an array
In this exercise the program reads from the array but never writes to it, and there is no loop, so the only
rule we need is [ARRAY-READ]. Consider the following triple, where a is an array of integers and i and x
are integers:
{ 0 ≤ i ∧ i + 1 < sizeof(a) }
x := a[i + 1] - a[i];
{ x + a[i] = a[i + 1] }
    •   a) Using [ARRAY-READ], calculate wp(x := a[i + 1] - a[i], x + a[i] = a[i + 1]) and simplify it.
    •   b) Show that the precondition implies the weakest precondition, so the triple is valid.
    •   c) Suppose that we replace the precondition by 0 ≤ i < sizeof(a). Is the triple still valid? If it is not,
        give values of i and a for which the program goes wrong.

Solution
a) [ARRAY-READ] works in two steps. First it substitutes the expression E for x in the postcondition Q,
exactly as the assignment rule does, and then it adds one definedness condition for every array read in
E. In this program E is a[i + 1] − a[i], which reads the array twice, so we will add def(a[i + 1]) and def(a[i]).

The substitution gives:

Q[x ← a[i + 1] − a[i]]          = a[i + 1] − a[i] + a[i] = a[i + 1]
                                 = a[i + 1] = a[i + 1]
                                 = true
The two definedness conditions are:
def(a[i + 1])       =   0 ≤ i + 1 < sizeof(a)
def(a[i])           =   0 ≤ i < sizeof(a)
We join the substitution and the two conditions with ∧:
wp   =   true ∧ 0 ≤ i + 1 < sizeof(a)                ∧    0 ≤ i < sizeof(a)
     =   0 ≤ i ∧ i + 1 < sizeof(a)
The last line is a simplification of the four inequalities, since 0 ≤ i already gives 0 ≤ i + 1, and i + 1 <
sizeof(a) already gives i < sizeof(a).

The substitution gave true, which means that the postcondition holds whatever values the array
contains. As a consequence, the only real requirement of this program is that both reads are inside the
array.

b) We must show that the precondition implies the weakest precondition that we calculated in part a),
so the implication that we have to prove is:
0 ≤ i    ∧   i + 1 < sizeof(a)            ⇒       0 ≤ i    ∧   i + 1 < sizeof(a)
The two sides of the implication are the same formula. An implication of the form P ⇒ P is always true,
since in every state where the left side is true, the right side is the same statement and is therefore true
as well. As a consequence, the implication holds and the triple is valid.

c) With the new precondition, the implication that we have to prove is:
0 ≤ i < sizeof(a)           ⇒       0 ≤ i     ∧   i + 1 < sizeof(a)
The first conjunct on the right side, 0 ≤ i, appears on the left side, so it follows immediately. The second
conjunct, i + 1 < sizeof(a), does not follow from the left side. The left side only says i < sizeof(a), and
since i and sizeof(a) are integers, this is the same as i + 1 ≤ sizeof(a), which still allows i + 1 = sizeof(a). In
that situation i is the last position of the array, and the read a[i + 1] is outside the array. As a
consequence, the implication does not hold and the triple is not valid any more.

For example, take a = [4, 7] and i = 1, where sizeof(a) = 2 and the precondition holds since 0 ≤ 1 < 2. The
program then reads a[2], which does not exist, since the only valid positions of this array are 0 and 1.

Exercise 2: Reading and then writing an array
In this exercise the program reads a cell of the array into x and then writes x into a cell, so we use
[ARRAY-READ] for the first statement and [ARRAY-ASSIGN] for the second. We calculate the weakest
precondition from the last statement to the first, and we work through the write in the three steps that
we followed in the lecture: substitute, select–store and definedness.

Consider the following program, where a is an array of integers and i, j and x are integers:
1    { 0 ≤ i < sizeof(a)        ∧   0 ≤ j < sizeof(a)          ∧   a[j] > 0 }
2    R1:
3    x := 2 * a[j];
4    R2:

5    a[i] := x;
6    { a[i] ≥ a[j] }
     •   a) Using [ARRAY-ASSIGN] and the select–store axioms, calculate R2 = wp(a[i] := x, a[i] ≥ a[j]).
         Show the substitution step, the select–store step and the definedness condition, and then
         simplify the result.
     •   b) Using [ARRAY-READ], calculate R1 = wp(x := 2 * a[j], R2) and simplify the result.
     •   c) Show that the precondition implies R1, so the triple is valid. Then suppose that the
         precondition has a[i] > 0 instead of a[j] > 0. Does this new precondition imply R1? If it does not,
         give values of i, j and the array a for which the program does not satisfy the postcondition, and
         explain which case of the select–store axioms causes the problem.

Solution
a) The postcondition Q is a[i] ≥ a[j], the program writes position i, and the value it writes is x.

Step 1, substitute. [ARRAY-ASSIGN] replaces every occurrence of a in Q by the updated array a[i ↦ x],
which is the array a where position i now holds x:
Q[a ← a[i ↦ x]]          =       a[i ↦ x][i]     ≥   a[i ↦ x][j]
Step 2, select–store. The substituted formula reads the updated array twice, once at position i and once
at position j, and we simplify the two reads one at a time with the select–store axioms.

We start with the read on the left side, a[i ↦ x][i]. This read is at position i, which is the position that was
written, so the first axiom gives a[i ↦ x][i] = x, and the formula becomes:
x    ≥   a[i ↦ x][j]
The read on the right side, a[i ↦ x][j], is at position j, and the axiom that we can apply depends on
whether j is the written position i. The program does not tell us whether j = i or j ≠ i, since both
situations are possible, so we have to consider the two cases. Since j = i ∨ j ≠ i is always true, every state
belongs to exactly one of these two cases.

     •   If j = i, the read is at the position that was written, so the first axiom gives a[i ↦ x][j] = x, and the
         formula becomes x ≥ x.
     •   If j ≠ i, the read is at a different position, so the second axiom gives a[i ↦ x][j] = a[j], and the
         formula becomes x ≥ a[j].

We now put the two cases together in one formula, where each case keeps its condition, so that the
formula is true in a state exactly when the case that applies to that state is true:
(j = i     ∧   x ≥ x)        ∨    (j ≠ i   ∧    x ≥ a[j])
Finally we simplify this formula. Since x ≥ x is always true, the first case reduces to j = i:
j = i    ∨     (j ≠ i    ∧       x ≥ a[j])
The distributive law turns this formula into (j = i ∨ j ≠ i) ∧ (j = i ∨ x ≥ a[j]), and since j = i ∨ j ≠ i is always
true, we obtain:
j = i    ∨     x ≥ a[j]
Step 3, definedness. The write needs def(a[i]), which is 0 ≤ i < sizeof(a). The value x does not read the
array, so def(x) is true and adds nothing.
R2   =   (j = i      ∨   x ≥ a[j])         ∧   0 ≤ i < sizeof(a)

The parentheses are needed, since the definedness condition must hold in both cases of the disjunction.

b) The assignment x := 2 * a[j] reads a[j], so [ARRAY-READ] replaces x by 2 · a[j] in R2 and adds def(a[j]):
R1   =   R2[x ← 2 · a[j]] ∧ def(a[j])
     =   (j = i ∨ 2 · a[j] ≥ a[j]) ∧                 0 ≤ i < sizeof(a)        ∧    0 ≤ j < sizeof(a)
If we subtract a[j] from both sides, 2 · a[j] ≥ a[j] becomes a[j] ≥ 0, so the result is:
R1   =   (j = i     ∨   a[j] ≥ 0)      ∧   0 ≤ i < sizeof(a)         ∧   0 ≤ j < sizeof(a)
c) For the precondition of the program, the implication that we have to prove is:
0 ≤ i < sizeof(a) ∧ 0 ≤ j < sizeof(a) ∧ a[j] > 0
    ⇒     (j = i ∨ a[j] ≥ 0) ∧ 0 ≤ i < sizeof(a) ∧                           0 ≤ j < sizeof(a)
The right side is a conjunction of three formulas, so we show that each of them follows from the left
side.

     •   The bounds 0 ≤ i < sizeof(a) and 0 ≤ j < sizeof(a) appear on the left side, so they follow
         immediately.
     •   For the disjunction j = i ∨ a[j] ≥ 0, it is enough to show one of its two parts, since a disjunction is
         true as soon as one of its parts is true. The left side gives a[j] > 0, and a number that is greater
         than 0 is also greater than or equal to 0, so a[j] ≥ 0 holds. As a consequence, the disjunction is
         true whether j is equal to i or not, and we do not need to know which of the two cases applies.

Since the three conjuncts of the right side follow from the left side, the implication holds and the triple is
valid.

Now suppose that the specification contains a mistake, where the precondition says a[i] > 0 instead of
a[j] > 0:
{ 0 ≤ i < sizeof(a)         ∧   0 ≤ j < sizeof(a)         ∧   a[i] > 0 }
With the new precondition, the implication that we have to prove becomes:
0 ≤ i < sizeof(a) ∧ 0 ≤ j < sizeof(a) ∧ a[i] > 0
    ⇒     (j = i ∨ a[j] ≥ 0) ∧ 0 ≤ i < sizeof(a) ∧                           0 ≤ j < sizeof(a)
The bounds still follow from the left side, as before, so the problem is the disjunction j = i ∨ a[j] ≥ 0, and
we look at it in the two possible cases. If j = i, the first part of the disjunction is true, so the disjunction
holds. If j ≠ i, the first part is false, so the disjunction needs a[j] ≥ 0, but the left side says nothing about
a[j], since the only fact it gives about the contents of the array is a[i] > 0, and a[i] is a different cell. As a
consequence, the implication does not hold, which means that we can find a state that satisfies the left
side but not the right side.

For example, take i = 0, j = 1 and a = [3, −2], where both indices are inside the array and a[0] = 3 > 0, so
the new precondition holds. The program first executes x := 2 * a[1], which gives x = −4, and then a[0] :=
−4, which gives a = [−4, −2]. The postcondition a[0] ≥ a[1] becomes −4 ≥ −2, which is false.

The problem comes from the second select–store axiom, the case j ≠ i. In this case the cell a[j] in the
postcondition is not the cell that was written, so it keeps its old value, and the postcondition becomes 2
· a[j] ≥ a[j], which is false for every negative value of a[j]. In the case j = i, both sides of the postcondition
read the cell that was written, so the postcondition becomes x ≥ x, which is always true. The fact a[i] > 0
does not help, since it describes the old value of the cell that the write replaces, which is why the
precondition has to talk about a[j] instead.

Exercise 3: A loop that reads two arrays
In this exercise we prove a loop that computes the dot product of two arrays a and b, which is the sum
of the products a[k] · b[k] over all the positions k. The loop reads both arrays but never writes to them,
so the array rule we need is [ARRAY-READ], and for the loop we follow the recipe from the lecture on
loop invariants.
{ sizeof(a) = n ∧ sizeof(b) = n }
i := 0;
s := 0;
while (i < n) {
    s := s + a[i] * b[i];
    i := i + 1;
}
{ s = Σ(k = 0 .. n−1) a[k] · b[k] }
We write Σ(k = 0 .. m) e(k) for the sum e(0) + e(1) + … + e(m). In the proof we use two facts about this
sum. The first is that the sum over an empty range, for example Σ(k = 0 .. −1), is 0. The second is that Σ(k
= 0 .. m) = Σ(k = 0 .. m−1) + e(m), which separates the last term from the rest of the sum.

Find a loop invariant I, prove establishment, preservation and postcondition at exit, and give a variant.

Solution
Step 1, Q and the progress variable. The progress variable is i, which goes from 0 up to n, and the result
variable is s, since Q describes the value of s at the end.

Step 2, trace the loop head. We run the loop with a = [2, −1, 3], b = [4, 5, 1] and n = 3, and we write
down the values of i and s each time we reach the loop head:

At the loop head                   i             s            Products added so far

Before pass 1                      0             0            none

Before pass 2                      1             8            2·4

Before pass 3                      2             3            2·4 + (−1)·5

At exit                            3             6            2·4 + (−1)·5 + 3·1

At every loop head, s holds the sum of the products a[k] · b[k] for the positions k below i, which are the
positions that the loop has already visited.

Step 3, generalise the postcondition. The final value of i is n, so we replace the n in the upper limit of
the sum by i:
s = Σ(k = 0 .. i−1) a[k] · b[k]
If we substitute n for i in this formula we obtain Q again, so the undo-check passes. The formula also
agrees with every row of the trace, for example before pass 3, where the sum for k = 0 and k = 1 is 8 − 5
= 3.

Step 4, add the bounds. The bounds are 0 ≤ i ≤ n. We also add the facts sizeof(a) = n and sizeof(b) = n to
the invariant, since the reads a[i] and b[i] in the body need def(a[i]) and def(b[i]), and inside the body

the only facts we can use are I and the guard. The program never writes to a or b, so these two facts stay
true during the whole loop.

The invariant does not need to say anything about the cells that the loop has not reached yet. Since the
program never writes to a or b, every cell that the body reads still holds the value that Q talks about.
I:       s = Σ(k = 0 .. i−1) a[k] · b[k]          ∧       sizeof(a) = n    ∧       sizeof(b) = n    ∧       0 ≤ i ≤
n
Step 5, check the three obligations.

Establishment. We must show sizeof(a) = n ∧ sizeof(b) = n ⇒ wp(i := 0; s := 0, I). Neither assignment
reads an array, so we use the ordinary assignment rule twice:
wp(s := 0, I)       =   0 = Σ(k = 0 .. i−1) a[k]·b[k]            ∧   sizeof(a) = n         ∧   sizeof(b) = n
∧ 0 ≤ i ≤ n

wp(i := 0, …)       =   0 = Σ(k = 0 .. −1) a[k]·b[k]             ∧   sizeof(a) = n         ∧   sizeof(b) = n
∧ 0 ≤ 0 ≤ n
Now we write the implication that we have to prove, with the precondition on the left and the weakest
precondition on the right:
sizeof(a) = n ∧ sizeof(b) = n
    ⇒     0 = Σ(k = 0 .. −1) a[k]·b[k]                ∧    sizeof(a) = n       ∧    sizeof(b) = n       ∧    0 ≤ 0
≤ n
We go through the conjuncts on the right side one by one.

     •    The sum Σ(k = 0 .. −1) has no terms, since there is no k with 0 ≤ k ≤ −1, and a sum with no terms
          is 0. As a consequence, the first conjunct is 0 = 0, which is true.
     •    The size facts sizeof(a) = n and sizeof(b) = n appear on the left side.
     •    In 0 ≤ 0 ≤ n, the part 0 ≤ 0 is true, and the part 0 ≤ n is the one that needs an argument. The left
          side says that n = sizeof(a), and the size of an array is the number of its elements, which can
          never be negative, so 0 ≤ n holds.

Since every conjunct of the right side follows from the left side, the invariant is established.

Preservation. We must show I ∧ i < n ⇒ wp(s := s + a[i] * b[i]; i := i + 1, I). The second statement is an
ordinary assignment, and the first one reads two cells, so [ARRAY-READ] adds def(a[i]) and def(b[i]):
wp(i := i + 1, I)
  = s = Σ(k = 0 .. i) a[k]·b[k]              ∧   sizeof(a) = n       ∧    sizeof(b) = n        ∧   0 ≤ i + 1 ≤
n

wp(s := s + a[i] * b[i], …)
  = s + a[i]·b[i] = Σ(k = 0 .. i) a[k]·b[k] ∧                    sizeof(a) = n         ∧   sizeof(b) = n        ∧
0 ≤ i + 1 ≤ n
     ∧ 0 ≤ i < sizeof(a) ∧ 0 ≤ i < sizeof(b)
Now we write the implication that we have to prove, with I ∧ i < n on the left and the weakest
precondition on the right:
s = Σ(k = 0 .. i−1) a[k]·b[k] ∧ sizeof(a) = n ∧ sizeof(b) = n ∧ 0 ≤ i ≤ n ∧
i < n
    ⇒     s + a[i]·b[i] = Σ(k = 0 .. i) a[k]·b[k] ∧ sizeof(a) = n ∧ sizeof(b) = n

∧   0 ≤ i + 1 ≤ n
          ∧ 0 ≤ i < sizeof(a)            ∧   0 ≤ i < sizeof(b)
We show that each conjunct on the right side follows from the left side.

    •   The equation about the sum is the step that needs most care. We separate the last term of the
        sum on the right side, which gives Σ(k = 0 .. i) a[k]·b[k] = Σ(k = 0 .. i−1) a[k]·b[k] + a[i]·b[i]. The left
        side tells us that Σ(k = 0 .. i−1) a[k]·b[k] is equal to s, so we can replace this part of the sum by s,
        and the whole sum becomes s + a[i]·b[i]. As a consequence, the equation becomes s + a[i]·b[i] =
        s + a[i]·b[i], which is true.
    •   The size facts sizeof(a) = n and sizeof(b) = n appear on the left side.
    •   For 0 ≤ i + 1, the left side gives 0 ≤ i, and if we add 1 to a number that is at least 0, the result is at
        least 1, so it is also at least 0.
    •   For i + 1 ≤ n we need the guard i < n. Since i and n are integers, there is no integer strictly
        between i and i + 1, so if i is smaller than n, then i + 1 is at most n. For example, if n = 5, the
        guard allows i to be at most 4, and then i + 1 is at most 5. The bound i ≤ n from the invariant
        would not be enough here, since it allows i = n, and then i + 1 = n + 1.
    •   For 0 ≤ i < sizeof(a), the part 0 ≤ i is on the left side, and for i < sizeof(a) we combine the guard i <
        n with the fact sizeof(a) = n, which gives i < sizeof(a). The condition 0 ≤ i < sizeof(b) follows in the
        same way from the fact sizeof(b) = n.

Since every conjunct of the right side follows from the left side, the invariant is preserved.

Postcondition at exit. We must show that the invariant together with the negated guard implies the
postcondition:
s = Σ(k = 0 .. i−1) a[k]·b[k] ∧ sizeof(a) = n                     ∧   sizeof(b) = n        ∧   0 ≤ i ≤ n      ∧
¬(i < n)
    ⇒     s = Σ(k = 0 .. n−1) a[k]·b[k]
The negated guard ¬(i < n) is the same as i ≥ n, and the invariant gives i ≤ n, so i = n, since a number that
is both at least n and at most n must be equal to n. If we replace i by n in the equation of the invariant,
we obtain s = Σ(k = 0 .. n−1) a[k]·b[k], which is exactly the right side.

Step 6, variant. The variant is V = n − i, which is never negative while the loop runs, since i ≤ n, and
which decreases by 1 in every pass, since the body executes i := i + 1.

What happens with a wrong guard
Suppose that we write the guard as i ≤ n instead of i < n. The invariant does not change, but in
preservation we now assume I ∧ i ≤ n, which allows i = n. For i = n the definedness condition 0 ≤ i <
sizeof(a) becomes n < n, which is false, so the proof fails in the pass that would read a[n], one position
after the end of the array. In this way the definedness conditions find the out-of-bounds read without
running the program.

Exercise 4: A loop that writes into a second array
In this exercise the loop reads every element of an array a, doubles it, and writes the result into a
second array b. The postcondition describes every position of b, so we write it with a universal
quantifier, and as a consequence the invariant also has a quantifier. When we apply [ARRAY-ASSIGN] in
preservation, the substitution happens inside that quantifier, which is the new part of this exercise.

{ sizeof(a) = n ∧ sizeof(b) = n }
i := 0;
while (i < n) {
    b[i] := 2 * a[i];
    i := i + 1;
}
{ ∀k. 0 ≤ k < n ⇒ b[k] = 2 · a[k] }
The postcondition says that for every position k between 0 and n − 1, the cell b[k] holds twice the value
of a[k]. The quantifier is bounded on both sides, so it only talks about positions that exist in both arrays.

Find a loop invariant I, prove establishment, preservation and postcondition at exit, and give a variant.

Solution
Step 1, Q and the progress variable. The progress variable is i, which goes from 0 up to n. The result is
the array b, since Q describes every cell of b, while the array a is only read.

Step 2, trace the loop head. We run the loop with a = [3, −1, 4] and n = 3, where b starts with the values
[9, 9, 9]:

At the loop head                                      i                   b

Before pass 1                                         0                   [9, 9, 9]

Before pass 2                                         1                   [6, 9, 9]

Before pass 3                                         2                   [6, −2, 9]

At exit                                               3                   [6, −2, 8]

At every loop head, the cells of b below position i already hold 2 · a[k], while the cells from position i
onwards still hold the values that b had before the loop.

Step 3, generalise the postcondition. The final value of i is n, so we replace the n in the range 0 ≤ k < n
by i:
∀k. 0 ≤ k < i ⇒ b[k] = 2 · a[k]
If we substitute n for i we obtain Q again, so the undo-check passes.

Step 4, add the bounds. The bounds are 0 ≤ i ≤ n. As in Exercise 3, we also add the two size facts, since
the body needs def(b[i]) for the write and def(a[i]) for the read.

The invariant does not need to say anything about the cells that the loop has not reached yet. The
postcondition says nothing about the old values of b, since the loop overwrites every cell of b, and the
body only reads a, which the program never writes.
I:    (∀k. 0 ≤ k < i ⇒ b[k] = 2 · a[k])              ∧    sizeof(a) = n       ∧   sizeof(b) = n     ∧   0 ≤ i
≤ n
Step 5, check the three invariant obligations.

Establishment. We must show sizeof(a) = n ∧ sizeof(b) = n ⇒ wp(i := 0, I):
wp(i := 0, I) = (∀k. 0 ≤ k < 0 ⇒ b[k] = 2 · a[k])                    ∧   sizeof(a) = n       ∧   sizeof(b)
= n ∧ 0 ≤ 0 ≤ n

The implication that we have to prove is:
sizeof(a) = n ∧ sizeof(b) = n
    ⇒     (∀k. 0 ≤ k < 0 ⇒ b[k] = 2 · a[k])                 ∧    sizeof(a) = n        ∧    sizeof(b) = n       ∧
0 ≤ 0 ≤ n
We go through the conjuncts on the right side one by one.

    •   The quantifier says that every k with 0 ≤ k < 0 satisfies b[k] = 2 · a[k]. There is no integer k with 0
        ≤ k < 0, so there is no position to check, and a statement about every element of an empty range
        is true. If this seems strange, read the quantifier as an implication, “for every k, if 0 ≤ k < 0 then
        b[k] = 2 · a[k]”, where the condition 0 ≤ k < 0 is false for every k, and an implication with a false
        condition is true.
    •   The size facts appear on the left side.
    •   The part 0 ≤ 0 is true, and 0 ≤ n holds since n = sizeof(a) and the size of an array is never
        negative.

As a consequence, the implication holds and the invariant is established.

Preservation. We must show I ∧ i < n ⇒ wp(b[i] := 2 * a[i]; i := i + 1, I). We start with the last statement,
which is an ordinary assignment:
wp(i := i + 1, I) = (∀k. 0 ≤ k < i + 1 ⇒ b[k] = 2 · a[k])                         ∧       sizeof(a) = n    ∧
sizeof(b) = n ∧ 0 ≤ i + 1 ≤ n
Now we apply [ARRAY-ASSIGN] to the write b[i] := 2 * a[i], where the written position is i and the value
written is 2 · a[i].

Step 1, substitute. We replace every occurrence of b by the updated array b[i ↦ 2·a[i]]. The occurrences
of a stay as they are, since the program writes to b and a is a different array:
(∀k. 0 ≤ k < i + 1 ⇒ b[i ↦ 2·a[i]][k] = 2 · a[k])                    ∧   sizeof(a) = n           ∧   sizeof(b[i
↦ 2·a[i]]) = n ∧ 0 ≤ i + 1 ≤ n
Step 2, select–store. Inside the quantifier the formula reads the updated array at position k, and we do
not know whether k is the written position i, so for each k we keep both cases:
∀k. 0 ≤ k < i + 1 ⇒ ( (k = i             ∧   2·a[i] = 2·a[k])       ∨    (k ≠ i       ∧    b[k] = 2·a[k]) )
For k = i the first case becomes 2·a[i] = 2·a[i], which is true, so the position i always satisfies the formula.
As a consequence, the quantifier only needs to hold for the other positions 0 ≤ k < i, where k ≠ i and the
second case applies:
∀k. 0 ≤ k < i ⇒ b[k] = 2 · a[k]
The update changes the value stored in one cell but not the number of cells, so sizeof(b[i ↦ 2·a[i]]) =
sizeof(b).

Step 3, definedness. The write needs def(b[i]), and the read a[i] in the value written needs def(a[i]). If we
put the three steps together, we get:
wp(b[i] := 2 * a[i], …)          =   (∀k. 0 ≤ k < i ⇒ b[k] = 2 · a[k])                ∧    sizeof(a) = n       ∧
sizeof(b) = n
                                     ∧   0 ≤ i + 1 ≤ n       ∧   0 ≤ i < sizeof(b)           ∧   0 ≤ i <
sizeof(a)

Now we write the implication that we have to prove, with I ∧ i < n on the left and the weakest
precondition on the right:
(∀k. 0 ≤ k < i ⇒ b[k] = 2 · a[k]) ∧ sizeof(a) = n ∧ sizeof(b) = n ∧ 0 ≤ i ≤ n
∧ i < n
    ⇒     (∀k. 0 ≤ k < i ⇒ b[k] = 2 · a[k]) ∧ sizeof(a) = n ∧ sizeof(b) = n
         ∧ 0 ≤ i + 1 ≤ n ∧ 0 ≤ i < sizeof(b) ∧ 0 ≤ i < sizeof(a)
We show that each conjunct on the right side follows from the left side.

    •   The quantified formula on the right side is the same as the quantified formula on the left side,
        so it follows immediately. This is a result of the select–store step, where the case k = i turned
        out to be always true, so the cell that the body writes does not need any fact from the invariant.
    •   The size facts appear on the left side.
    •   The bound 0 ≤ i + 1 follows from 0 ≤ i, since adding 1 to a number that is at least 0 gives a
        number that is at least 1.
    •   The bound i + 1 ≤ n follows from the guard i < n, since i and n are integers and there is no integer
        strictly between i and i + 1. The bound i ≤ n from the invariant would not be enough, since it
        allows i = n, and then i + 1 = n + 1.
    •   In the two definedness conditions, 0 ≤ i is on the left side, while i < sizeof(b) and i < sizeof(a)
        follow from the guard i < n together with the facts sizeof(b) = n and sizeof(a) = n.

As a consequence, the implication holds and the invariant is preserved.

Postcondition at exit. We must show that the invariant together with the negated guard implies the
postcondition:
(∀k. 0 ≤ k < i ⇒ b[k] = 2 · a[k]) ∧ sizeof(a) = n                      ∧   sizeof(b) = n       ∧   0 ≤ i ≤ n
∧ ¬(i < n)
    ⇒    ∀k. 0 ≤ k < n ⇒ b[k] = 2 · a[k]
The negated guard ¬(i < n) is the same as i ≥ n, and together with i ≤ n it gives i = n. If we replace i by n in
the quantified formula of the invariant, we obtain exactly the right side.

Step 6, variant. The variant is V = n − i, which is never negative since i ≤ n, and which decreases by 1 in
every pass.

Why a and b must be different arrays
In step 1 of [ARRAY-ASSIGN] we replaced b and left a unchanged, which is correct only because a and b
are different arrays. In C, two pointers can refer to the same memory, and in that situation the write b[i]
:= 2 * a[i] would also change a[i]. The postcondition would then require a[k] = 2 · a[k] for every position
k, which only holds when every element is 0, so the program would not satisfy its specification. We will
meet this problem again in the labs, when we verify C programs that use pointers.

