# ICT3112 - 7 - Recepy for Loop Invariants - Example 1a

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Recipe for Loop Invariants** . if ie | **Example 1 — Sum of Even Numbers The Candidate and Establishment Dr. David Sanan** ay Be = 

# **Example 1 — Sum of even numbers** 

3 · Generalise 

1 · Q 2 · Trace 

4 · Bounds 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->

**The loop computes** 2 + 4 + … + 2𝑛 



<!-- Start of picture text -->
{ n ≥  0 }<br>i  := 0 ;  s  := 0 ;<br>while  (i < n) {<br>    i  :=  i +  1 ;<br>    s  :=  s +  2 *i;<br>}<br>{ s = n(n+ 1 ) }<br><!-- End of picture text -->

- This loop is very similar to the one we used to introduce the recipe. 

- We will follow the recipe step by step to find its invariant. 

## **Example 1 · Step 1 — Q and the progress variable** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Q** 

2 · Trace 

3 · Generalise 

4 · Bounds 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; 

s **:=** s + **2** *i; } 

𝑄:  𝑠 = 𝑛(𝑛+1) 

- 𝑖  is the progress variable: it counts the iterations of the loop, from  0  up to  𝑛. 

- 𝑠  is the result variable, since  𝑄  tells us what the value of  𝑠  must be at the end. 

{ s = n(n+ **1** ) } 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 

# **Example 1 · Step 2 — trace the loop head** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

**2 · Trace** 3 · Generalise 

4 · Bounds 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

|**at loo**|**p head**|𝑖|𝑠|
|---|---|---|---|
|before|pass 1|0|0|
|before|pass 2|1|2|
|before|pass 3|2|6|
|before|pass 4|3|12|
|before|pass 5|4|20|



- The values of  𝑠  are  0, 2, 6, 12, 20, … •  Each value is a product of two consecutive numbers: 

   - 0 = 0⋅1,  2 = 1⋅2,  6 = 2⋅3, 12 = 3⋅4,  20 = 4⋅5 

- So we can guess that  𝑠 = 𝑖(𝑖+1)  every time we reach the loop head. 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 

## **Example 1 · Step 3 — generalise the postcondition** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

**3 · Generalise** 

4 · Bounds 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; 

s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

𝑃:  𝑛 ≥ 0 

𝑠 = 𝑛(𝑛+1)    ⟶    𝑠 = 𝑖(𝑖+1) 

(we replace  𝑛  by  𝑖) 

- We get the same equation that we guessed from the trace, so both approaches agree. 

- This equation is the main part of the invariant, but the invariant is not complete yet. 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 

# **Example 1 · Step 4 — add the bounds** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

**4 · Bounds** 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

We add bounds for the progress variable, since  𝑖  starts at  0  and never goes beyond  𝑛: 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

_The bound_ 𝑖 ≤ 𝑛 _is what allows us to conclude that_ 𝑖 = 𝑛 _when the loop finishes._ 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 

# **Example 1 · Step 5 — what we need to check** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; 

s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

𝑃:  𝑛 ≥ 0 

The loop rule, together with the consequence rule, gives three conditions. A fourth condition gives termination: 

1.  Establishment:   {𝑃}  𝑖 ≔ 0;  𝑠 ≔ 0  {𝐼} 

2.  Preservation:   {𝐼 ∧ 𝐵}  𝑐  {𝐼} 

3.  Postcondition at exit:   𝐼 ∧ ¬𝐵 ⇒ 𝑄 

4.  Termination:   𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0   and   {𝐼 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼 ∧ 𝐸 < 𝐸0} 

The loop is preceded by  𝑖 ≔ 0;  𝑠 ≔ 0, so establishment is a triple for these assignments, and not only  𝑃 ⇒ 𝐼. 

𝑐  is the body of the loop:  𝑖 ≔ 𝑖 + 1;  𝑠 ≔ 𝑠 + 2⋅𝑖 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

**To check a triple we use the weakest precondition:** 

{𝑅}  𝑐  {𝑆}  holds when  𝑅 ⇒ 𝑤𝑝(𝑐, 𝑆) 𝑤𝑝(𝑥 ≔ 𝑒, 𝑆) = 𝑆[𝑥 ← 𝑒] 𝑤𝑝(𝑐1;  𝑐2, 𝑆) = 𝑤𝑝(𝑐1, 𝑤𝑝(𝑐2, 𝑆)) 

So we compute the weakest precondition from the last assignment to the first. 

# **Example 1 · Establishment — the rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

Rule:   {𝑃}  𝑖 ≔ 0;  𝑠 ≔ 0  {𝐼} 

We replace  𝑃  and  𝐼  by our assertions: 

{𝑛 ≥ 0}  𝑖 ≔ 0;  𝑠 ≔ 0  {𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛} 

The triple holds when the precondition implies the weakest precondition: 𝑛 ≥ 0 ⇒ 𝑤𝑝(𝑖 ≔ 0;  𝑠 ≔ 0, 𝐼) 

By the rule for sequences we start from the last assignment: 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑤𝑝(𝑖 ≔ 0;  𝑠 ≔ 0, 𝐼) = 𝑤𝑝(𝑖 ≔ 0, 𝑤𝑝(𝑠 ≔ 0, 𝐼)) 

𝑄:  𝑠 = 𝑛(𝑛+1) 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

We call  𝑅1 = 𝑤𝑝(𝑠 ≔ 0, 𝐼)  and  𝑅2 = 𝑤𝑝(𝑖 ≔ 0, 𝑅1). We compute them on the next slide. 

# **Example 1 · Establishment — computing the wp** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } { s = n(n+ **1** ) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑠 = 𝑛(𝑛+1) 𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

First the last assignment,  𝑠 ≔ 0: 

𝑅1 = 𝑤𝑝(𝑠 ≔ 0, 𝐼) = 𝐼[𝑠 ← 0] = (𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑠 ← 0] = (0 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛) 

Then the first assignment,  𝑖 ≔ 0: 

𝑅2 = 𝑤𝑝(𝑖 ≔ 0, 𝑅1) = 𝑅1[𝑖 ← 0] = (0 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 0] = (0 = 0⋅(0+1) ∧ 0 ≤ 0 ≤ 𝑛) 

So  𝑤𝑝(𝑖 ≔ 0;  𝑠 ≔ 0, 𝐼) = 𝑅2. The blue terms show what each substitution put in place of the variable. 

# **Example 1 · Establishment — the implication** 

2 · Trace 3 · Generalise 

4 · Bounds 

1 · Q 

We need to show that the precondition implies  𝑅2: 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; 

𝑛 ≥ 0 ⇒ 0 = 0⋅(0+1) ∧ 0 ≤ 0 ≤ 𝑛 

- 0⋅(0+1) = 0⋅1 = 0, so the conjunct  0 = 0⋅(0+1)  holds. 

s **:=** s + **2** *i; } 

- 0 ≤ 0  holds. 

- 0 ≤ 𝑛  holds, since the precondition gives  𝑛 ≥ 0. 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**5 · Check** 

{ s = n(n+ **1** ) } 

**✓ established** 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

