# ICT3112 - 7 - Recepy for Loop Invariants - Example 3b

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Recipe for Loop Invariants** . if ie | **Example 3 — Fibonacci Numbers Refining the Candidate Dr. David Sanan** ay Be = 

# **Example 3 so far: the first candidate** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

5 · Check 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

**CHECK** 

establishment  ✓ preservation  ✗ 

We need to show  𝐼1 ∧ 𝐵 ⇒ 𝑅4: 

𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛 

{ a = F(n) } 

**✗ preservation fails** 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

The second conjunct holds as in the previous examples. For the first conjunct we need  𝑏 = 𝐹(𝑖+1). However, the left side says nothing about  𝑏, so we cannot prove it. 

## **Example 3 · Step 4 again — add the missing fact** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

**4 · Bounds** 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

{ a = F(n) } 

We go back to step 4 and add the missing fact. The trace already showed us that  𝑏 = 𝐹(𝑖+1). 

𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

_Usually, each variable that changes in the loop needs its own conjunct in the invariant._ 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

**Since the candidate has changed, we need to check all the conditions again from the beginning.** 

# **Example 3 · Establishment again — the rule** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 

Rule:   {𝑃}  𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0  {𝐼2} 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

We replace  𝑃  and  𝐼2  by our assertions: 

{𝑛 ≥ 0}  𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0 {𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛} 

As before, the triple holds when  𝑛 ≥ 0 ⇒ 𝑅3, where: 

{ a = F(n) } 

𝑅1 = 𝑤𝑝(𝑖 ≔ 0, 𝐼2) 𝑅2 = 𝑤𝑝(𝑏 ≔ 1, 𝑅1) 𝑅3 = 𝑤𝑝(𝑎 ≔ 0, 𝑅2) 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**5 · Check** 

# **Example 3 · Establishment again — the wp** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝑅1 = 𝐼2[𝑖 ← 0] = (𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 0] = (𝑎 = 𝐹(0) ∧ 𝑏 = 𝐹(0+1) ∧ 0 ≤ 0 ≤ 𝑛) 𝑅2 = 𝑅1[𝑏 ← 1] = (𝑎 = 𝐹(0) ∧ 1 = 𝐹(0+1) ∧ 0 ≤ 0 ≤ 𝑛) 𝑅3 = 𝑅2[𝑎 ← 0] = (0 = 𝐹(0) ∧ 1 = 𝐹(0+1) ∧ 0 ≤ 0 ≤ 𝑛) 

This time  𝑏  appears in the invariant, so the substitution  [𝑏 ← 1]  does change something. 

## **Example 3 · Establishment again — the implication** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

We need to show that the precondition implies  𝑅3: 

𝑛 ≥ 0 ⇒ 0 = 𝐹(0) ∧ 1 = 𝐹(0+1) ∧ 0 ≤ 0 ≤ 𝑛 

- 𝐹(0) = 0  by definition, so  0 = 𝐹(0)  holds. 

- 𝐹(0+1) = 𝐹(1) = 1  by definition, so  1 = 𝐹(0+1)  holds. 

- 0 ≤ 0  holds, and  0 ≤ 𝑛  holds since the precondition gives  𝑛 ≥ 0. 

{ a = F(n) } 

**✓ established (both equations)** 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

# **Example 3 · Preservation again — the rule** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 

Rule:   {𝐼2 ∧ 𝐵}  𝑐  {𝐼2} 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

We replace  𝐼2,  𝐵  and  𝑐: 

{𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛} 𝑡 ≔ 𝑎 + 𝑏;  𝑎 ≔ 𝑏;  𝑏 ≔ 𝑡;  𝑖 ≔ 𝑖 + 1 {𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛} 

The triple holds when  𝐼2 ∧ 𝐵 ⇒ 𝑅4, where: 

{ a = F(n) } 

𝑅1 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝐼2),      𝑅2 = 𝑤𝑝(𝑏 ≔ 𝑡, 𝑅1), 𝑅3 = 𝑤𝑝(𝑎 ≔ 𝑏, 𝑅2),      𝑅4 = 𝑤𝑝(𝑡 ≔ 𝑎 + 𝑏, 𝑅3) 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**5 · Check** 

# **Example 3 · Preservation again — the wp (1)** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

{ a = F(n) } 

First the last assignment,  𝑖 ≔ 𝑖 + 1: 

𝑅1 = 𝐼2[𝑖 ← 𝑖 + 1] = (𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 𝑖 + 1] = (𝑎 = 𝐹(𝑖+1) ∧ 𝑏 = 𝐹((𝑖+1)+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) = (𝑎 = 𝐹(𝑖+1) ∧ 𝑏 = 𝐹(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

Then  𝑏 ≔ 𝑡: 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝑅2 = 𝑅1[𝑏 ← 𝑡] 

= (𝑎 = 𝐹(𝑖+1) ∧ 𝑡 = 𝐹(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

# **Example 3 · Preservation again — the wp (2)** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

Then  𝑎 ≔ 𝑏: 𝑅3 = 𝑅2[𝑎 ← 𝑏] = (𝑎 = 𝐹(𝑖+1) ∧ 𝑡 = 𝐹(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛)[𝑎 ← 𝑏] = (𝑏 = 𝐹(𝑖+1) ∧ 𝑡 = 𝐹(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) Finally the first assignment,  𝑡 ≔ 𝑎 + 𝑏: 𝑅4 = 𝑅3[𝑡 ← 𝑎 + 𝑏] = (𝑏 = 𝐹(𝑖+1) ∧ 𝑡 = 𝐹(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛)[𝑡 ← 𝑎 + 𝑏] = (𝑏 = 𝐹(𝑖+1) ∧ 𝑎 + 𝑏 = 𝐹(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

So  𝑤𝑝(𝑐, 𝐼2) = 𝑅4. 

## **Example 3 · Preservation again — the implication** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

We need to show  𝐼2 ∧ 𝐵 ⇒ 𝑅4: 

𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 𝑏 = 𝐹(𝑖+1) ∧ 𝑎 + 𝑏 = 𝐹(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛 

First conjunct.  𝑏 = 𝐹(𝑖+1)  is already on the left side.    ✓ 

Second conjunct. We replace  𝑎  and  𝑏  using the left side, and then use the definition of 𝐹  with  𝑘 = 𝑖: 

{ a = F(n) } 

𝑎 + 𝑏 = 𝐹(𝑖) + 𝐹(𝑖+1) = 𝐹(𝑖+2) ✓ 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

Third conjunct. As in the previous examples.    ✓ 

**✓ preserved** 

The new fact about  𝑏  is what makes the proof work. It gives the first conjunct directly, and the second conjunct needs both equations. 

# **Example 3 · Postcondition at exit** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; 

} 

{ a = F(n) } 

Rule:   𝐼2 ∧ ¬𝐵 ⇒ 𝑄 

We replace  𝐼2,  𝐵  and  𝑄  by our assertions: 

𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ ¬(𝑖 < 𝑛) ⇒ 𝑎 = 𝐹(𝑛) 

- ¬(𝑖 < 𝑛)  is the same as  𝑖 ≥ 𝑛. 

- Together with  𝑖 ≤ 𝑛  from the invariant, this gives  𝑖 = 𝑛. 

- We replace  𝑖  by  𝑛  in  𝑎 = 𝐹(𝑖)  and we obtain  𝑎 = 𝐹(𝑛), which is  𝑄. 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

**✓ Q holds at the exit** 

## **Example 3 · Termination — the variant is bounded** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

We use the variant  𝐸 = 𝑛 − 𝑖. The termination rule has two conditions: (𝑎)    𝐼2 ∧ 𝐵 ⇒ 𝐸 ≥ 0 (𝑏)    {𝐼2 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼2 ∧ 𝐸 < 𝐸0} 

𝐸0  is the value of  𝐸  before the iteration. 

Condition (a). We replace  𝐼2,  𝐵  and  𝐸: 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 𝐸:  𝑛 − 𝑖 

𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 𝑛 − 𝑖 ≥ 0 

From  𝑖 < 𝑛  we get  𝑛 − 𝑖 > 0, so  𝑛 − 𝑖 ≥ 0  holds. 

**✓ (a) holds** 

# **Example 3 · Termination — the decrease rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

Condition (b). The part  𝐼2  of the postcondition is preservation, which we have already proved. So we only need to check  𝐸 < 𝐸0: 

{𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ∧ 𝑛 − 𝑖 = 𝐸0} 𝑡 ≔ 𝑎 + 𝑏;  𝑎 ≔ 𝑏;  𝑏 ≔ 𝑡;  𝑖 ≔ 𝑖 + 1 {𝑛 − 𝑖 < 𝐸0} 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 𝐸:  𝑛 − 𝑖 

We compute the weakest precondition from the last assignment: 𝑅1 = (𝑛 − 𝑖 < 𝐸0)[𝑖 ← 𝑖 + 1] = (𝑛 − (𝑖+1) < 𝐸0) 𝑅2 = 𝑅1[𝑏 ← 𝑡] = (𝑛 − (𝑖+1) < 𝐸0) 𝑅3 = 𝑅2[𝑎 ← 𝑏] = (𝑛 − (𝑖+1) < 𝐸0) 𝑅4 = 𝑅3[𝑡 ← 𝑎 + 𝑏] = (𝑛 − (𝑖+1) < 𝐸0) 𝑏,  𝑎  and  𝑡  do not appear in the variant, so the last three substitutions change nothing. 

## **Example 3 · Termination — the variant decreases** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 

We need to show  𝐼2 ∧ 𝐵 ∧ 𝑛 − 𝑖 = 𝐸0 ⇒ 𝑅4. The part we use is: 𝑛 − 𝑖 = 𝐸0 ⇒ 𝑛 − (𝑖+1) < 𝐸0 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; 

This holds, since  𝑛 − (𝑖+1) = (𝑛 − 𝑖) − 1 = 𝐸0 − 1 < 𝐸0. 

i **:=** i + **1** ; } { a = F(n) } 

**✓ the loop terminates** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**5 · Check** 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 

𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) 

∧ 0 ≤ 𝑖 ≤ 𝑛 

𝐸:  𝑛 − 𝑖 

# **Example 3 — the full cycle** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼2:  𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 𝐸:  𝑛 − 𝑖 

Establishment:   𝑛 ≥ 0 ⇒ 𝑤𝑝(𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0, 𝐼2) ✓ Preservation:   𝐼2 ∧ 𝑖 < 𝑛 ⇒ 𝑤𝑝(𝑐, 𝐼2) ✓ Postcondition at exit:   𝐼2 ∧ ¬(𝑖 < 𝑛) ⇒ 𝑎 = 𝐹(𝑛) ✓ Termination:   𝐸 = 𝑛 − 𝑖  is bounded and decreases    ✓ 

**PROPOSE** replace  𝑛  by  𝑖  in  𝑄, add the bounds 

**CHECK REFINE** establishment  ✓ add the missing fact preservation  ✗ 

_We then check again. All the conditions hold now, and the variant_ 𝐸 = 𝑛 − 𝑖 _shows that the loop terminates._ 

**Examples 1 and 2 worked at the first attempt, and Example 3 needed one correction. Harder loops may need several corrections.** 

