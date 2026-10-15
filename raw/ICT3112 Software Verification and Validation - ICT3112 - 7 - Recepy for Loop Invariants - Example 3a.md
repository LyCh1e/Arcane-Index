# ICT3112 - 7 - Recepy for Loop Invariants - Example 3a

# **ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Recipe for Loop Invariants** . if ie | **Example 3 — Fibonacci Numbers The First Candidate Fails Dr. David Sanan** ay Be = 

## **Example 3 — Fibonacci numbers** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 2 · Trace 3 · Generalise 

4 · Bounds 

5 · Check 

**In this loop two variables change in the body** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

_where_ 

𝐹(0) = 0,  𝐹(1) = 1,  𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 

- The body updates both  𝑎  and  𝑏, and the new value of each one depends on the other. 

- This time our first candidate will not work. We will see which condition fails and why. 

### **Example 3 · Step 1 — Q and the progress variable** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Q** 

2 · Trace 

3 · Generalise 

4 · Bounds 

5 · Check 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { 

𝑄:  𝑎 = 𝐹(𝑛) 

t **:=** a + b; 

a **:=** b; b **:=** t; i **:=** i + **1** ; } 

- 𝑖  is the progress variable:  0, 1, 2, …, 𝑛. 

- 𝑎  is the result variable, since  𝑄  tells us the value of  𝑎  at the end. 

- 𝑏  is an auxiliary variable. We should not forget it, since auxiliary variables are often needed in the invariant. 

{ a = F(n) } 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑎 = 𝐹(𝑛) 

𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 

## **Example 3 · Step 2 — trace the loop head** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

**2 · Trace** 3 · Generalise 

4 · Bounds 

5 · Check 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

|**at loop head**|𝑖|𝑎|𝑏|
|---|---|---|---|
|before pass 1|0|0|1|
|before pass 2|1|1|1|
|before pass 3|2|1|2|
|before pass 4|3|2|3|
|before pass 5|4|3|5|



- The values of  𝑎  are  0, 1, 1, 2, 3, which is  𝐹(𝑖). 

- The values of  𝑏  are  1, 1, 2, 3, 5, which is  𝐹(𝑖+1), so  𝑏  is always one position ahead of  𝑎. 

- We will need this second observation later. 

{ a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 

### **Example 3 · Step 3 — generalise the postcondition** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

**3 · Generalise** 

4 · Bounds 

5 · Check 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

𝑎 = 𝐹(𝑛)    ⟶    𝑎 = 𝐹(𝑖) 

(we replace  𝑛  by  𝑖) 

This is the same step that worked for the two previous examples. 

{ a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 

𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 

### **Example 3 · Step 4 — add the bounds: first candidate** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

**4 · Bounds** 

5 · Check 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { 

𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

t **:=** a + b; 

a **:=** b; 

b **:=** t; 

i **:=** i + **1** ; } { a = F(n) } 

We use the same form as before: the result computed so far, plus the bounds of the counter. 

**The candidate seems complete, so the next step is to check it.** 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 

## **Example 3 · Step 5 — what we need to check** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; 

**while** (i < n) { t **:=** a + b; 

a **:=** b; 

b **:=** t; 

i **:=** i + **1** ; } 

{ a = F(n) } 

The loop rule, together with the consequence rule, gives three conditions. A fourth condition gives termination: 

1.  Establishment:   {𝑃}  𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0  {𝐼1} 

2.  Preservation:   {𝐼1 ∧ 𝐵}  𝑐  {𝐼1} 

3.  Postcondition at exit:   𝐼1 ∧ ¬𝐵 ⇒ 𝑄 

4.  Termination:   𝐼1 ∧ 𝐵 ⇒ 𝐸 ≥ 0   and   {𝐼1 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼1 ∧ 𝐸 < 𝐸0} 

The loop is preceded by  𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0, so establishment is a triple for these assignments, and not only  𝑃 ⇒ 𝐼1. 

𝑐  is the body of the loop:  𝑡 ≔ 𝑎 + 𝑏;  𝑎 ≔ 𝑏;  𝑏 ≔ 𝑡;  𝑖 ≔ 𝑖 + 1 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

**To check a triple we use the weakest precondition:** 

{𝑅}  𝑐  {𝑆}  holds when  𝑅 ⇒ 𝑤𝑝(𝑐, 𝑆) 

𝑤𝑝(𝑥 ≔ 𝑒, 𝑆) = 𝑆[𝑥 ← 𝑒] 

𝑤𝑝(𝑐1;  𝑐2, 𝑆) = 𝑤𝑝(𝑐1, 𝑤𝑝(𝑐2, 𝑆)) 

So we compute the weakest precondition from the last assignment to the first. 

## **Example 3 · Establishment — the rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

{ a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

Rule:   {𝑃}  𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0  {𝐼1} 

We replace  𝑃  and  𝐼1  by our assertions: 

{𝑛 ≥ 0}  𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0  {𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛} 

The triple holds when  𝑛 ≥ 0 ⇒ 𝑤𝑝(𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0, 𝐼1). There are three assignments, so we apply the assignment rule three times, from the last one: 𝑅1 = 𝑤𝑝(𝑖 ≔ 0, 𝐼1) 𝑅2 = 𝑤𝑝(𝑏 ≔ 1, 𝑅1) 

𝑅3 = 𝑤𝑝(𝑎 ≔ 0, 𝑅2) 

Then  𝑤𝑝(𝑎 ≔ 0;  𝑏 ≔ 1;  𝑖 ≔ 0, 𝐼1) = 𝑅3. 

## **Example 3 · Establishment — computing the wp** 

2 · Trace 3 · Generalise 

4 · Bounds 

1 · Q 

𝑅1 = 𝐼1[𝑖 ← 0] = (𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 0] = (𝑎 = 𝐹(0) ∧ 0 ≤ 0 ≤ 𝑛) 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

𝑅2 = 𝑅1[𝑏 ← 1] = (𝑎 = 𝐹(0) ∧ 0 ≤ 0 ≤ 𝑛)[𝑏 ← 1] = (𝑎 = 𝐹(0) ∧ 0 ≤ 0 ≤ 𝑛) 

𝑏  does not appear in  𝑅1, so this substitution changes nothing. 

𝑅3 = 𝑅2[𝑎 ← 0] = (𝑎 = 𝐹(0) ∧ 0 ≤ 0 ≤ 𝑛)[𝑎 ← 0] 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->

= (0 = 𝐹(0) ∧ 0 ≤ 0 ≤ 𝑛) 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 3 · Establishment — the implication** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; 

We need to show that the precondition implies  𝑅3: 

𝑛 ≥ 0 ⇒ 0 = 𝐹(0) ∧ 0 ≤ 0 ≤ 𝑛 

- 𝐹(0) = 0  by the definition of  𝐹, so the conjunct  0 = 𝐹(0)  holds. 

- 0 ≤ 0  holds, and  0 ≤ 𝑛  holds since the precondition gives  𝑛 ≥ 0. 

i **:=** i + **1** ; 

} 

**✓ established** 

{ a = F(n) } 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑎 = 𝐹(𝑛) 

𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 3 · Preservation — the rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

{ a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

Rule:   {𝐼1 ∧ 𝐵}  𝑐  {𝐼1} 

We replace  𝐼1,  𝐵  and  𝑐  by our candidate, the guard and the body of the loop: 

{𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛} 𝑡 ≔ 𝑎 + 𝑏;  𝑎 ≔ 𝑏;  𝑏 ≔ 𝑡;  𝑖 ≔ 𝑖 + 1 {𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛} 

The triple holds when  𝐼1 ∧ 𝐵 ⇒ 𝑤𝑝(𝑐, 𝐼1). The body has four assignments, so we apply the assignment rule four times, from the last one to the first: 

𝑅1 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝐼1),      𝑅2 = 𝑤𝑝(𝑏 ≔ 𝑡, 𝑅1), 𝑅3 = 𝑤𝑝(𝑎 ≔ 𝑏, 𝑅2),      𝑅4 = 𝑤𝑝(𝑡 ≔ 𝑎 + 𝑏, 𝑅3) Then  𝑤𝑝(𝑐, 𝐼1) = 𝑅4. 

## **Example 3 · Preservation — computing the wp** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

{ a = F(n) } 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝑅1 = 𝐼1[𝑖 ← 𝑖 + 1] = (𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 𝑖 + 1] = (𝑎 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

𝑅2 = 𝑅1[𝑏 ← 𝑡] = (𝑎 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

𝑅3 = 𝑅2[𝑎 ← 𝑏] = (𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 𝑅4 = 𝑅3[𝑡 ← 𝑎 + 𝑏] = (𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

- 𝑏  does not appear in  𝑅1, and  𝑡  does not appear in  𝑅3, so those two substitutions change nothing. 

- The important substitution is  [𝑎 ← 𝑏]: it turns the fact about  𝑎  into a fact about  𝑏. 

## **Example 3 · Preservation — the implication** 

3 · Generalise 

4 · Bounds 

1 · Q 

2 · Trace 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; **while** (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } 

{ a = F(n) } 

We need to show  𝐼1 ∧ 𝐵 ⇒ 𝑅4: 

𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 𝑏 = 𝐹(𝑖+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛 

The second conjunct holds as in the previous examples. For the first conjunct we need  𝑏 = 𝐹(𝑖+1). However, the left side says nothing about  𝑏, so we cannot prove it. 

**✗ preservation fails** 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑎 = 𝐹(𝑛) 𝐹(0) = 0,  𝐹(1) = 1 𝐹(𝑘+2) = 𝐹(𝑘) + 𝐹(𝑘+1) 𝐼1:  𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

- This is not because  𝑏 = 𝐹(𝑖+1)  is false. In fact, it holds in every execution of the loop. 

- The problem is that the invariant does not include this fact, so the proof cannot use it. 

**The invariant is missing a fact about a variable that changes in the loop.** 

