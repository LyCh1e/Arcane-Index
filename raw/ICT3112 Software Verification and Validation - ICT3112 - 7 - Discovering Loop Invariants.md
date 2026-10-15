# ICT3112 - 7 - Discovering Loop Invariants

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **What an Invariant Is Dr. David Sanan** ay Be = 

# **Hoare Logic – Loop Invariants** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**Recap: the rule we already have** 

{𝐼 ∧ 𝐵}  𝑐  {𝐼} **[WHILE]** {𝐼}  𝑤ℎ𝑖𝑙𝑒  𝐵  𝑑𝑜  𝑐  {𝐼 ∧ ¬𝐵} 

- **Partial correctness** : if the loop terminates, the postcondition holds. 

- The rule needs an invariant  𝐼, but it assumes that we already have one. 

**Today’s question: where does** 𝐼 **come from, and how do we know that it is right?** 

## **Checks for proving a loop correct using an invariant** 



<!-- Start of picture text -->
INSTITUTEOF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->

**Three conditions (four, if we also want termination) to prove a postcondition from an invariant:** 

1. **Establishment** :   𝑃 ⇒ 𝐼 

2. **Preservation** :   {𝐼 ∧ 𝐵}  𝑐  {𝐼} 

3. **Postcondition at exit** :   𝐼 ∧ ¬𝐵 ⇒ 𝑄 



<!-- Start of picture text -->
4. Termination: an integer variant V with V => 0, and V J decreases in every iteration<br><!-- End of picture text -->

𝑃 ⇒ 𝐼        {𝐼 ∧ 𝐵}  𝑐  {𝐼}        𝐼 ∧ ¬𝐵 ⇒ 𝑄        𝑉 ≥ 0, 𝑉 ↓ 



<!-- Start of picture text -->
{P} while B do c {Q}<br><!-- End of picture text -->

_The first and the third checks come from the consequence rule: we choose_ 𝐼 _so that_ 𝑃 ⇒ 𝐼 _(start)  and_ 𝐼 ∧ ¬𝐵 ⇒ 𝑄 _(finish)._ 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**What invariants are…** 

# **Invariants capture the behaviour of loops** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ Invariant } while (B) P; 

{ Invariant  ¬B ∧ } 

An invariant provides a loop **specification** , a contract, with the expected behaviour of the loop. 

The contract tells us what output we can expect from the loop when we start from a given input. The invariant is the precondition of the loop, and the invariant together with the negated guard is its postcondition. 

Like the specifications of programs, the specification of a loop is **not unique** . 

# **Invariants capture the behaviour of loops** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
{ x ≥  0   x = X ∧ }<br>while (x >  0 )<br>    x  :=  x −  1 ;<br>{ x ≥  0   x ≤ ∧ 0 }<br>𝐼 ≡ 𝑥 ≥ 0<br><!-- End of picture text -->

𝑋 _is a logical variable: it names the initial value of_ 𝑥 _._ 

This invariant is the contract of the loop: 

- Before the loop:  𝑥 ≥ 0 

- After the loop:  𝑥 ≥ 0 ∧ ¬(𝑥 > 0), that is,  𝑥 ≥ 0 ∧ 𝑥 ≤ 0 

The specification is not unique:  𝑥 ≥ 0 ∧ 𝑥 ≤ 𝑋  is also an invariant of this loop. 

# **Invariants capture the behaviour of loops** 



{ x ≥ **0** x = X ∧ } while (x > **0** ) x **:=** x − **1** ; { x ≥ **0** x ≤ ∧ **0** } 

The postcondition after executing the body becomes the precondition of the following iteration. 

If we unfold the iterations and write the specification of each one as a pre- and postcondition, we can see why it is called an invariant. 

𝑥 ≔ 𝑥 − 1 

{𝑃}    𝑥 ∈ 𝑃 ∧ 𝑥 ∈ 𝐵 {𝑄} de 𝑥 ≔ 𝑥 − 1 {𝑃}    𝑥 ∈ 𝑃 ∧ 𝑥 ∈ 𝐵 {𝑄} de 𝑥 ≔ 𝑥 − 1 {𝑃}    𝑥 ∈ 𝑃 ∧ 𝑥 ∈ 𝐵 {𝑄} de 

**…** 

{𝑃}    𝑥 ∈ 𝑃 ∧ 𝑥 ∉ 𝐵 fd) 

_the guard is false, so the loop stops_ 

# **Invariants capture the behaviour of loops** 



{ x ≥ **0** x = X ∧ } while (x > **0** ) x **:=** x − **1** ; { x ≥ **0** x ≤ ∧ **0** } 

The precondition and the postcondition of the body must be the **same predicate** , so that one contract works for every iteration: 

If we unfold the iterations and write the specification of each one as a pre- and postcondition, we can see why it is called an invariant. 



<!-- Start of picture text -->
𝑥 ≔ 𝑥 − 1<br>{𝐼}    𝑥 ∈ 𝐼 ∧ 𝑥 ∈ 𝐵 {𝐼}<br>de<br>𝑥 ≔ 𝑥 − 1<br>{𝐼}    𝑥 ∈ 𝐼 ∧ 𝑥 ∈ 𝐵 {𝐼}<br>de<br>𝑥 ≔ 𝑥 − 1<br>{𝐼}    𝑥 ∈ 𝐼 ∧ 𝑥 ∈ 𝐵 {𝐼}<br>de<br><!-- End of picture text -->

{𝐼 ∧ 𝐵}  𝑐  {𝐼} **…** {𝐼}    𝑥 ∈ 𝐼 ∧ 𝑥 ∉ 𝐵 fd) 

_the guard is false, so the loop stops_ 

# **Invariants capture the behaviour of loops** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ x ≥  0   x = X ∧ }<br>while (x >  0 )<br>    x  :=  x −  1 ;<br>{ x ≥  0   x ≤ ∧ 0 }<br>𝐼 ≡ 𝑥 ≥ 0<br><!-- End of picture text -->

**But what does an invariant tell us about the execution of a loop?** 

It represents **snapshots** of the loop execution: a photo of the state each time the program reaches the loop head. 



<!-- Start of picture text -->
Run 1 𝑥 = 37 𝑥 = 12 𝑥 = 2<br>Run 2 𝑥 = 100 𝑥 = 25 𝑥 = 0<br><!-- End of picture text -->

- **✓** 𝑥 ≥ 0 **holds in every snapshot.** 

**Let’s add a bit more information to the state…** 

# **Invariants capture the behaviour of loops** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ x ≥  0   x = X  y = Y ∧ ∧ }<br>while (x >  0 )<br>    x  :=  x −  1 ;<br>{ x ≥  0   x ≤ ∧ 0 }<br><!-- End of picture text -->

𝐼 ≡ 𝑥 ≥ 0 ∧ 𝑦 = 𝑌 

**But what does an invariant tell us about the execution of a loop?** 

It represents **snapshots** of the loop execution: a photo of the state each time the program reaches the loop head. 



<!-- Start of picture text -->
Run 1 𝑥 = 37, 𝑦 = 50 𝑥 = 12, 𝑦 = 50 𝑥 = 2, 𝑦 = 50<br>Run 2 𝑥 = 100, 𝑦 = 100 𝑥 = 25, 𝑦 = 100 𝑥 = 0, 𝑦 = 100<br><!-- End of picture text -->

- **✓** 𝑥 ≥ 0 **in every snapshot, and** 𝑦 **always keeps its initial value:** 𝑦 = 𝑌 **.** 

The invariant also describes what the loop does **not** change. 

## **Invariants capture the behaviour of loops: another example** 

𝐼 ≡    𝑚 ≥ 𝐴[𝑘]   for all  0 ≤ 𝑘 < 𝑖 ∧    𝑚 = 𝐴[𝑗]   for some  0 ≤ 𝑗 < 𝑖 

{ **1** ≤ n ≤ length(A) ∧ m = A[ **0** ]  i = ∧ **1** } while (i < n) { if (A[i] > m) m **:=** A[i]; i **:=** i + **1** ; } 



<!-- Start of picture text -->
            ∧    1 ≤ 𝑖 ≤ 𝑛<br>𝐴 6 2 7 3 1 6<br>[TTT<br>0 1 2 3 4 5<br>𝑖 = 1, 𝑚 = 6 𝑖 = 3, 𝑚 = 7 𝑖 = 6, 𝑚 = 7<br>rsa<br>𝐴 6 2 7 3 1 23 19 11 17 31 45 28<br>(TTTTTEITITi<br>0 1 2 3 4 5 6 7 8 9 10 11<br>te<br>𝑖 = 1, 𝑚 = 6 𝑖 = 5, 𝑚 = 7 𝑖 = 7, 𝑚 = 23<br>eea ee<br>𝑖 = 9, 𝑚 = 23 𝑖 = 10, 𝑚 = 31 𝑖 = 12, 𝑚 = 45<br>rsee<br><!-- End of picture text -->

{ m = max(A[ **0** ..n− **1** ]) } 



# **Why are invariants important?** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
{ x ≥  0   x = X ∧ }<br>while (x >  0 )<br>    x  :=  x −  1 ;<br>{ x =  0 }<br><!-- End of picture text -->

To verify the loop by following each iteration, we would need to unfold it: 



<!-- Start of picture text -->
𝑥 ≔ 𝑥 − 1<br>{𝑃}    𝑥 > 0 {𝑄}<br>Ce<br>𝑥 ≔ 𝑥 − 1<br>{𝑃}    𝑥 > 0 {𝑄}<br>a<br>…<br>{𝑃}    𝑥 ≤ 0<br><!-- End of picture text -->

_the guard is false, so the loop stops_ 

2<sup>64</sup> **iterations in the worst case, for a 64-bit architecture. Unbounded, if we consider mathematical integers.** 

# **Why are invariants important?** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->

**With Hoare Logic we only need to check a few rules:** 

𝑃 ⇒ 𝐼        {𝐼 ∧ 𝐵}  𝑐  {𝐼}        𝐼 ∧ ¬𝐵 ⇒ 𝑄        𝑉 ≥ 0, 𝑉 ↓ 



<!-- Start of picture text -->
{P} while B c {Q}<br><!-- End of picture text -->

1. **Establishment** :   𝑃 ⇒ 𝐼 

2. **Preservation** :   {𝐼 ∧ 𝐵}  𝑐  {𝐼} 

3. **Postcondition at exit** :   𝐼 ∧ ¬𝐵 ⇒ 𝑄 

4. **Termination** :  an integer variant  𝑉  with  𝑉 ≥ 0, and  𝑉  decreases in every iteration 

**Preservation is about one single iteration, but an arbitrary one. So a fixed, small number of checks replaces an unbounded number of iterations.** 

