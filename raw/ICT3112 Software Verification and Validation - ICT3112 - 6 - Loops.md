# ICT3112 - 6 - Loops

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Loop Rule** . if ie | **Dr. David Sanan** ay Be 

# **Hoare Logic - Loop Rule** 

**[SKIP]** 

{𝑄} 𝑆𝐾𝐼𝑃 {𝑄} 

<u>{𝑃} 𝑐 ₁ {𝑅} {𝑅} 𝑐 ₂ {𝑄}</u> **[SEQ]** {𝑃} 𝑐; 𝑐 {𝑄}₁ ₂ 

<u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> 

**[WHILE]** 

{𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**[ASSIGN]** 

{𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 

<u>{𝑃 ∧ 𝐵} 𝑐 ₁ {𝑄} {𝑃 ∧ ¬𝐵} 𝑐 ₂ {𝑄}</u> **[IF]** {𝑃} 𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐 𝐸𝐿𝑆𝐸 𝑐 {𝑄}₁ ₂ 

𝑃 ⟶ 𝑃′    {𝑃′} 𝑐 {𝑄′} <u>𝑄′ ⟶ 𝑄</u> **[CONSEQUENCE]** {𝑃} 𝑐 {𝑄} 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Verification of loops is more complex than the other constructs because we need to provide the loop behaviour/specification in something we call invariant. 

An invariant is an assertion that holds before each iteration of the loop, during the loop execution, and when the loop finishes. When the loop finishes the guard of the loop is false. 

An assertion is an invariant of a loop if satisfies the following: 

The invariant is true before the loop is executed If the invariant is true before an iteration, then it is true after the iteration 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Verification of loops is more complex than the other constructs because we need to provide the loop behaviour/specification in something we call invariant. 

**while** (x > **0** ) x **:=** x - **1** ; 

Note that a specification or behaviour is given by a set of elements: Those conforming such behaviour. 

Without knowing the initial value of x, we know that the loop covers all numbers greater than zero (condition of the loop). A value of x greater than zero enables all the values between the initial value x’ and all positive numbers. From x = 3, the body of the loop will decrease it x to 3, 2, 1 

We always need to analyse corner cases. x = 1 is the last iteration of the loop, which adds x = 0 to loop behaviour 

# **Hoare Logic - Loop Rule – Checking Invariant** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**while** (x > **0** ) x **:=** x - **1** ; 

**How to check that the invariant is correct?** 

If 𝑃 is true before the execution of the program 𝑐, 𝑄 is satisfied after the execution of 𝑐, if the execution of 𝑐 terminates 

{𝑃} 𝑐 {𝑄} 

𝐼 ≡ 𝑥 ≥ 0 

An assertion is an invariant of a loop if satisfies the following: 

1. The invariant is true before the loop is executed (when the guard of the loop is satisfied) 

2. If the invariant is true before an iteration, then it is true after the iteration 

{𝐼} 𝑐 {𝐼} 

# **Hoare Logic - Loop Rule – Checking Invariant** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**while** (x > **0** ) x **:=** x - **1** ; 

**How to check that the invariant is correct?** 

If 𝑃 is true before the execution of the program 𝑐, 𝑄 is satisfied after the execution of 𝑐, if the execution of 𝑐 terminates 

{𝑃} 𝑐 {𝑄} 

𝐼 ≡ 𝑥 ≥ 0 

An assertion is an invariant of a loop if satisfies the following: 

1. The invariant is true before the loop is executed (when the guard of the loop is satisfied) 

2. If the invariant is true before an iteration, then it is true after the iteration 

{𝐼 ∧ 𝐵} 𝑐 {𝐼} 

Note that before the execution of an iteration, the guard of the loop is true! 

# **Hoare Logic - Loop Rule – Checking Invariant** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**while** (x > **0** ) x **:=** x - **1** ; 𝐼 ≡ 𝑥 ≥ 0 [ 

{𝐼 ∧ 𝐵} 𝑐 {𝐼} 



<!-- Start of picture text -->
ms) ae pases’<br><!-- End of picture text -->

We need to check that this triple is correct 

Apply assignment rule + consequence rule or WP The triple is true if 𝐼 ∧ 𝐵 implies WP(c, 𝑥 ≥ 0) 

𝑊𝑃 ≡ {𝑥 ≥ 0}[𝑥 ← 𝑥 − 1] 

𝑊𝑃 ≡ {𝑥 ≥ 1} - by substituting x by x – 1 and moving adding 1 to both sides of the inequality 

𝑥 ≥ 0 ∧ 𝑥 > 0 ⟹ 𝑥 ≥ 1 ✓ 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

<u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> **[WHILE]** {𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

If when the invariant and the guard of the loop are true (in a given state) the execution of the loop preserves the invariant, then if the loop finishes, it terminates in a state where the invariant is _true_ and the guard of the loop is _false_ . 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**while** (x > **0** ) x **:=** x - **1** ; 

<u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> 

{𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

𝐼 ≡ 𝑥 ≥ 0 𝐵 ≡ 𝑥 > 0 𝑐 ≡ 𝑥 ≔ 𝑥 − 1 

<u>{𝑥 ≥ 0 ∧ 𝑥 > 0} 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0}</u> 

{𝑥 ≥ 0} 𝑊𝐻𝐼𝐿𝐸 𝑥 > 0 𝐷𝑂 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0 ∧ ¬(𝑥 > 0)} 

{𝑥 > 0} 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0} 

<u>{𝑥 > 0} 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0}</u> 

{𝑥 ≥ 0} 𝑊𝐻𝐼𝐿𝐸 𝑥 > 0 𝐷𝑂 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0 ∧ 𝑥 ≤ 0} 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->

**while** (x > **0** ) x **:=** x - **1** ; 

<u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> 

{𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

𝐼 ≡ 𝑥 ≥ 0 𝐵 ≡ 𝑥 > 0 𝑐 ≡ 𝑥 ≔ 𝑥 − 1 



<!-- Start of picture text -->
(ke<br>> O}x = x —1{x > 0}<br>{x => O}[x — x — 1] = {x = 1}<br>{x > 0} > {x = 1}<br><!-- End of picture text -->

<u>{𝑥 ≥ 0 ∧ 𝑥 > 0} 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0}</u> 

{𝑥 ≥ 0} 𝑊𝐻𝐼𝐿𝐸 𝑥 > 0 𝐷𝑂 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0 ∧ ¬(𝑥 > 0)} 

{𝑥 > 0} 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0} <u>{𝑥 > 0} 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0}</u> {𝑥 ≥ 0} 𝑊𝐻𝐼𝐿𝐸 𝑥 > 0 𝐷𝑂 𝑥 ≔ 𝑥 − 1 {𝑥 = 0} 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**while** (x ≥ **0** ) x **:=** x - **1** ; 

Let’s consider a loop where the guard is 𝑥 ≥ 0 instead of 𝑥 > 0 <u>{𝑥 ≥ 0} 𝑥 ≔ 𝑥 − 1 {𝑥 ≥ 0}</u> {𝑥 ≥ 0} 𝑊𝐻𝐼𝐿𝐸 𝑥 ≥ 0 𝐷𝑂 𝑥 ≔ 𝑥 − 1 {𝑥 = 0} Is 𝑥 ≥ 0 a valid invariant? 

Consider the case when 𝑥 = 0 the execution of the loop changes the variable to 𝑥 = −1, which is out of the range of the invariant, and therefore it is not preserved. So 𝑥 ≥ 0 is not a valid invariant in this case 

Give an invariant for this case {𝑥 ≥ −1} 

Changing the guard of the loop has other consequences for the specification. What are they? What would the postcondition be in this case? 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

<u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> 

{𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

This rule forces us to use 𝐼 as precondition and 𝐼 ∧ ¬𝐵 postcondition 

But often we want to use some other precondition 𝑃 and postcondition 𝑄. We can use the Consequence rule to do that. In fact it is that common that there is a rule for it 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} Consequence rule 

𝑃 ⇒ 𝐼 <u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> 𝐼 ∧ ¬𝐵 ⇒ 𝑄 {𝑃} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝑄} 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**A rule to check loop termination** 

<u>{𝐼 ∧ 𝐵 ∧ (𝐸 = 𝑛)} 𝑐 {𝐼 ∧ 𝐸 < 𝑛}</u> 𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0 {𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

To check termination we add a variant. A variant is an expression that it is greater than or equal to zero when the loop is executed. And it decreases after each iteration. 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**A rule to check loop termination** 

<u>{𝐼 ∧ 𝐵 ∧ (𝐸 = 𝑛)} 𝑐 {𝐼 ∧ 𝐸 < 𝑛}</u> 𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0 

{𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

{i = **0** }; **while** (i < **10** ){ i **:=** i+ **1** ; } 

Variant = 10 - i Invariant i <=10 

**Prove it is true!!!** 

{𝑖 ≤ 10 ∧ 𝑖 < 10 ∧ (10 − 𝑖 = 𝑛)} 𝑖 ≔ 𝑖 + 1 {𝑖 ≤ 10 ∧ 10 − 𝑖 < 𝑛} I: 𝑖 ≤ 10     B: 𝑖 < 10     V = n: 10 − 𝑖 = 𝑛     V < n: 10 − 𝑖 < 𝑛 

{𝑖 ≤ 10 ∧ 𝑖 < 10 ∧ (10 − 𝑖 = 𝑛)} ⇒ {𝑖 ≤ 10 ∧ 10 − 𝑖 < 𝑛}[𝑖 ← 𝑖 + 1] {𝑖 ≤ 10 ∧ 𝑖 < 10 ∧ (10 − 𝑖 = 𝑛)} ⇒ {𝑖 + 1 ≤ 10 ∧ 10 − (𝑖 + 1) < 𝑛} 

{𝑖 ≤ 10 ∧ 𝑖 < 10 ∧ (10 − 𝑖 = 𝑛)} ⇒ {𝑖 ≤ 9 ∧ 9 − 𝑖 < 𝑛} 

# **Hoare Logic - Loop Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**A rule to check loop termination** 

<u>{𝐼 ∧ 𝐵 ∧ (𝐸 = 𝑛)} 𝑐 {𝐼 ∧ 𝐸 < 𝑛}</u> 𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0 {𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

{i = **10** }; **while** (i > **0** ){ i **:=** i- **1** ; } 

Invariant i >= 0 Variant = i {𝑖 ≥ 0 ∧ 𝑖 > 0 ∧ (𝑖 = 𝑛)} 𝑖 ≔ 𝑖 − 1 {𝑖 ≥ 0 ∧ 𝑖 < 𝑛} I: 𝑖 ≥ 0     B: 𝑖 > 0     V = n: 𝑖 = 𝑛     V < n: 𝑖 < 𝑛 {𝑖 ≥ 0 ∧ 𝑖 > 0 ∧ (𝑖 = 𝑛)} ⇒ {𝑖 ≥ 0 ∧ 𝑖 < 𝑛}[𝑖 ← 𝑖 − 1] {𝑖 ≥ 0 ∧ 𝑖 > 0 ∧ (𝑖 = 𝑛)} ⇒ {𝑖 − 1 ≥ 0 ∧ 𝑖 − 1 < 𝑛} 

**Prove it is true!!!** 

## **Loop Rule: the precondition given by the invariant** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

The precondition given by the loop rule is the invariant   𝐼 

together with a check that the invariant is correct, which must hold in every state 

(𝐵 ∧ 𝐼) ⟹ 𝑤𝑝(𝑐, 𝐼) 

and a check that when the loop finishes we obtain the postcondition, which must hold in every state 

(¬𝐵 ∧ 𝐼) ⟹ 𝑄 

Precondition:  𝐼 

Checks, in every state:  (𝐵 ∧ 𝐼) ⟹ 𝑤𝑝(𝑐, 𝐼)   and   (¬𝐵 ∧ 𝐼) ⟹ 𝑄 

