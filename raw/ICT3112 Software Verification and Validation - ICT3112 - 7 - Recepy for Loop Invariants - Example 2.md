# ICT3112 - 7 - Recepy for Loop Invariants - Example 2



# **ICT3112** 

**Introduction to Formal Verification of Programs** . if ie | **Recipe for Loop Invariants Example 2 — Powers of two Dr. David Sanan** ay Be = 

## **Example 2 — Powers of two** 

1 · Q 2 · Trace 3 · Generalise 



<!-- Start of picture text -->
4 · Bounds<br><!-- End of picture text -->



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->

**The loop computes** 2<sup>𝑛</sup> **by doubling** 𝑟 **,** 𝑛 **times** 



<!-- Start of picture text -->
{ n ≥  0 }<br>r  := 1 ;  i  := 0 ;<br>while  (i < n) {<br>    r  := 2  * r;<br>    i  :=  i +  1 ;<br>}<br>{ r =  2 ⁿ }<br><!-- End of picture text -->

- We use the same recipe, but now the loop multiplies the result instead of adding to it. 

- Try to do each step yourself before looking at the next slide. 

## **Example 2 · Steps 1–2 — Q and the trace** 

3 · Generalise 

4 · Bounds 

**1 · Q** 

**2 · Trace** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; 

i **:=** i + **1** ; } 

{ r = **2** ⁿ } 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

|**at loop head**|𝑖|𝑟|•𝑖is the progress variable and𝑟is the re|
|---|---|---|---|
|before pass 1|0|1|variable.|
|before pass 2|1|2|•  The values of𝑟are1, 2, 4, 8, which are|
|before pass 3|2|4|powers of two.|
|before pass 4|3|8|•  So we can guess that𝑟 = 2<sup>𝑖</sup>at the loop<br>head.|



- 𝑖  is the progress variable and  𝑟  is the result variable. 



<!-- Start of picture text -->
𝑃:  𝑛 ≥ 0<br><!-- End of picture text -->

𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

### **Example 2 · Steps 3–4 — generalise and add bounds** 

**3 · Generalise** 

**4 · Bounds** 

1 · Q 

2 · Trace 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

𝑟 = 2<sup>𝑛</sup> ⟶    𝑟 = 2<sup>𝑖</sup> (we replace  𝑛  by  𝑖) 

We add the bounds of the progress variable, as in Example 1: 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

5 · Check 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑟 = 2<sup>𝑛</sup> 

## **Example 2 · Step 5 — what we need to check** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } 

{ r = **2** ⁿ } 

𝑃:  𝑛 ≥ 0 

The loop rule, together with the consequence rule, gives three conditions. A fourth condition gives termination: 

1.  Establishment:   {𝑃}  𝑟 ≔ 1;  𝑖 ≔ 0  {𝐼} 

2.  Preservation:   {𝐼 ∧ 𝐵}  𝑐  {𝐼} 

3.  Postcondition at exit:   𝐼 ∧ ¬𝐵 ⇒ 𝑄 

4.  Termination:   𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0   and   {𝐼 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼 ∧ 𝐸 < 𝐸0} 

The loop is preceded by  𝑟 ≔ 1;  𝑖 ≔ 0, so establishment is a triple for these assignments, and not only  𝑃 ⇒ 𝐼. 

𝑐  is the body of the loop:  𝑟 ≔ 2⋅𝑟;  𝑖 ≔ 𝑖 + 1 

𝐵:  𝑖 < 𝑛 

**To check a triple we use the weakest precondition:** 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

{𝑅}  𝑐  {𝑆}  holds when  𝑅 ⇒ 𝑤𝑝(𝑐, 𝑆) 𝑤𝑝(𝑥 ≔ 𝑒, 𝑆) = 𝑆[𝑥 ← 𝑒] 

𝑤𝑝(𝑐1;  𝑐2, 𝑆) = 𝑤𝑝(𝑐1, 𝑤𝑝(𝑐2, 𝑆)) 

So we compute the weakest precondition from the last assignment to the first. 

## **Example 2 · Establishment — the rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } 

{ r = **2** ⁿ } 

Rule:   {𝑃}  𝑟 ≔ 1;  𝑖 ≔ 0  {𝐼} 

We replace  𝑃  and  𝐼  by our assertions: 

{𝑛 ≥ 0}  𝑟 ≔ 1;  𝑖 ≔ 0  {𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛} 

The triple holds when the precondition implies the weakest precondition: 𝑛 ≥ 0 ⇒ 𝑤𝑝(𝑟 ≔ 1;  𝑖 ≔ 0, 𝐼) 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

By the rule for sequences we start from the last assignment: 𝑤𝑝(𝑟 ≔ 1;  𝑖 ≔ 0, 𝐼) = 𝑤𝑝(𝑟 ≔ 1, 𝑤𝑝(𝑖 ≔ 0, 𝐼)) 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

We call  𝑅1 = 𝑤𝑝(𝑖 ≔ 0, 𝐼)  and  𝑅2 = 𝑤𝑝(𝑟 ≔ 1, 𝑅1). 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 2 · Establishment — computing the wp** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 

First the last assignment,  𝑖 ≔ 0: 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

𝑅1 = 𝑤𝑝(𝑖 ≔ 0, 𝐼) = 𝐼[𝑖 ← 0] = (𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 0] = (𝑟 = 2<sup>0</sup> ∧ 0 ≤ 0 ≤ 𝑛) 

Then the first assignment,  𝑟 ≔ 1: 

𝑅2 = 𝑤𝑝(𝑟 ≔ 1, 𝑅1) = 𝑅1[𝑟 ← 1] = (𝑟 = 2<sup>0</sup> ∧ 0 ≤ 0 ≤ 𝑛)[𝑟 ← 1] = (1 = 2<sup>0</sup> ∧ 0 ≤ 0 ≤ 𝑛) 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

So  𝑤𝑝(𝑟 ≔ 1;  𝑖 ≔ 0, 𝐼) = 𝑅2. 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**5 · Check** 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 2 · Establishment — the implication** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } 

{ r = **2** ⁿ } 

We need to show that the precondition implies  𝑅2: 

𝑛 ≥ 0 ⇒ 1 = 2<sup>0</sup> ∧ 0 ≤ 0 ≤ 𝑛 

- 2<sup>0</sup> = 1, so the conjunct  1 = 2<sup>0</sup> holds. 

- 0 ≤ 0  holds, and  0 ≤ 𝑛  holds since the precondition gives  𝑛 ≥ 0. 

**✓ established** 

#### 𝑃:  𝑛 ≥ 0 

_Establishment holds because_ 2<sup>0</sup> = 1 _, so the initial value of_ 𝑟 _is important. With_ 𝑟 ≔ 0 _the first conjunct would be_ 0 = 2<sup>0</sup> _, which is false._ 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 2 · Preservation — the rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

Rule:   {𝐼 ∧ 𝐵}  𝑐  {𝐼} 

We replace  𝐼,  𝐵  and  𝑐  by our invariant, the guard and the body of the loop: 

{𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛} 𝑟 ≔ 2⋅𝑟; 𝑖 ≔ 𝑖 + 1 {𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛} 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

The triple holds when  𝐼 ∧ 𝐵 ⇒ 𝑤𝑝(𝑐, 𝐼). We start from the last assignment: 𝑤𝑝(𝑐, 𝐼) = 𝑤𝑝(𝑟 ≔ 2⋅𝑟, 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝐼)) 

We call  𝑅1 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝐼)  and  𝑅2 = 𝑤𝑝(𝑟 ≔ 2⋅𝑟, 𝑅1). 

## **Example 2 · Preservation — computing the wp** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 

First the last assignment,  𝑖 ≔ 𝑖 + 1: 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

𝑅1 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝐼) = 𝐼[𝑖 ← 𝑖 + 1] = (𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 𝑖 + 1] = (𝑟 = 2<sup>𝑖+1</sup> ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

Then the first assignment,  𝑟 ≔ 2⋅𝑟: 

𝑅2 = 𝑤𝑝(𝑟 ≔ 2⋅𝑟, 𝑅1) = 𝑅1[𝑟 ← 2⋅𝑟] = (𝑟 = 2<sup>𝑖+1</sup> ∧ 0 ≤ 𝑖+1 ≤ 𝑛)[𝑟 ← 2⋅𝑟] 

𝑃:  𝑛 ≥ 0 

= (2⋅𝑟 = 2<sup>𝑖+1</sup> ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

So  𝑤𝑝(𝑐, 𝐼) = 𝑅2. 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**5 · Check** 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 2 · Preservation — the implication** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

We need to show  𝐼 ∧ 𝐵 ⇒ 𝑅2: 

𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 2⋅𝑟 = 2<sup>𝑖+1</sup> ∧ 0 ≤ 𝑖+1 ≤ 𝑛 

First conjunct. We replace  𝑟  using  𝑟 = 2<sup>𝑖</sup> from the left side: 

2⋅𝑟 = 2⋅2<sup>𝑖</sup> = 2<sup>𝑖+1</sup> ✓ 

Second conjunct. From  0 ≤ 𝑖  we get  0 ≤ 𝑖+1, and from  𝑖 < 𝑛  we get  𝑖+1 ≤ 𝑛.    ✓ 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

**✓ preserved** 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 2 · Postcondition at exit** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } 

{ r = **2** ⁿ } 

Rule:   𝐼 ∧ ¬𝐵 ⇒ 𝑄 

We replace  𝐼,  𝐵  and  𝑄  by our assertions: 

𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ ¬(𝑖 < 𝑛) ⇒ 𝑟 = 2<sup>𝑛</sup> 

- ¬(𝑖 < 𝑛)  is the same as  𝑖 ≥ 𝑛. 

- Together with  𝑖 ≤ 𝑛  from the invariant, this gives  𝑖 = 𝑛. 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

- We replace  𝑖  by  𝑛  in  𝑟 = 2<sup>𝑖</sup> and we obtain  𝑟 = 2<sup>𝑛</sup> , which is  𝑄. 

   - **✓ Q holds at the exit** 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

### **Example 2 · Termination — the variant is bounded** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

We use the variant  𝐸 = 𝑛 − 𝑖. The termination rule has two conditions: (𝑎)    𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0 (𝑏)    {𝐼 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼 ∧ 𝐸 < 𝐸0} 

𝐸0  is the value of  𝐸  before the iteration. 

Condition (a). We replace  𝐼,  𝐵  and  𝐸: 

𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 𝑛 − 𝑖 ≥ 0 

#### 𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 𝑄:  𝑟 = 2<sup>𝑛</sup> 𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

From  𝑖 < 𝑛  we get  𝑛 − 𝑖 > 0, so  𝑛 − 𝑖 ≥ 0  holds. 

**✓ (a) holds** 

𝐸:  𝑛 − 𝑖 

## **Example 2 · Termination — the decrease rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } 

{ r = **2** ⁿ } 

Condition (b):   {𝐼 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼 ∧ 𝐸 < 𝐸0} The part  𝐼  of the postcondition is preservation, which we have already proved. So we only need to check  𝐸 < 𝐸0. We replace  𝐼,  𝐵,  𝐸  and  𝑐: 

{𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ∧ 𝑛 − 𝑖 = 𝐸0} 

𝑟 ≔ 2⋅𝑟; 𝑖 ≔ 𝑖 + 1 

{𝑛 − 𝑖 < 𝐸0} 

𝑃:  𝑛 ≥ 0 

We call  𝑅1 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝑛 − 𝑖 < 𝐸0)  and  𝑅2 = 𝑤𝑝(𝑟 ≔ 2⋅𝑟, 𝑅1). 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝐸:  𝑛 − 𝑖 

### **Example 2 · Termination — the variant decreases** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 

First the last assignment,  𝑖 ≔ 𝑖 + 1: 𝑅1 = (𝑛 − 𝑖 < 𝐸0)[𝑖 ← 𝑖 + 1] = (𝑛 − (𝑖+1) < 𝐸0) 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

Then the first assignment,  𝑟 ≔ 2⋅𝑟: 

𝑅2 = 𝑅1[𝑟 ← 2⋅𝑟] = (𝑛 − (𝑖+1) < 𝐸0) 

𝑟  does not appear in  𝑅1, so this substitution changes nothing. 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑟 = 2<sup>𝑛</sup> 𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 𝐸:  𝑛 − 𝑖 

We need to show  𝐼 ∧ 𝐵 ∧ 𝑛 − 𝑖 = 𝐸0 ⇒ 𝑅2. The part we use is: 

𝑛 − 𝑖 = 𝐸0 ⇒ 𝑛 − (𝑖+1) < 𝐸0 

This holds, since  𝑛 − (𝑖+1) = (𝑛 − 𝑖) − 1 = 𝐸0 − 1 < 𝐸0. 

**✓ the loop terminates** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**5 · Check** 

## **Example 2 — summary of the checks** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } r **:= 1** ;  i **:= 0** ; **while** (i < n) { r **:= 2** * r; i **:=** i + **1** ; } { r = **2** ⁿ } 

Establishment:   𝑛 ≥ 0 ⇒ 𝑤𝑝(𝑟 ≔ 1;  𝑖 ≔ 0, 𝐼) ✓ Preservation:   𝐼 ∧ 𝑖 < 𝑛 ⇒ 𝑤𝑝(𝑐, 𝐼) ✓ Postcondition at exit:   𝐼 ∧ ¬(𝑖 < 𝑛) ⇒ 𝑟 = 2<sup>𝑛</sup> ✓ Termination:   𝐸 = 𝑛 − 𝑖  is bounded and decreases    ✓ 

- Again, the first candidate satisfies all the conditions. 

- Is this always the case? No. In the next example the first candidate does not work. 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑟 = 2<sup>𝑛</sup> 

𝐼:  𝑟 = 2<sup>𝑖</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝐸:  𝑛 − 𝑖 

