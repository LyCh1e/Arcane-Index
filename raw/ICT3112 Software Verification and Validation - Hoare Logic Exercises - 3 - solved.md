# Hoare Logic Exercises - 3 - solved

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

# **Hoare Logic: Exercise Set 3** 

Worked solutions: weakest preconditions and validity checks for sequences, conditionals and loops 

**How to read these solutions** 

The sheet asks for two kinds of answer. When the precondition is shown as { ?? }, we compute the weakest precondition (WP). When both the precondition and the postcondition are given, we check that the triple is valid, which means that the given precondition implies the computed WP. 

Every exercise follows the same order. First the triple is stated. Then the WP is computed step by step in a table. Then the result is stated or the check is carried out. The exercise ends with the complete proof outline. 

In the program boxes, program statements are written in black monospace, for example x := x + 1;. Assertions are written in blue between braces, for example { x ≥ 0 }. The grey text after // on the right explains why an assertion holds at that point. 

Symbols: ∧ is "and", ∨ is "or", ¬ is "not", ⇒ is "implies" (the sheet writes it as →). Q[x ← e] means "Q with every occurrence of x replaced by the expression e". 

**Conventions used in this sheet** 

**Primed names are initial values.** A name such as x′ is a logical variable. It records the value that x had when the program started, and the program never assigns to it. Since the program cannot change xʹ, the substitution rule never replaces it. 

**Links to primed names.** When a postcondition mentions x′, the precondition must contain x = x′. Otherwise nothing in the precondition says what xʹ is, and the triple cannot be proved. 

**Integers.** All variables are integers. This matters in several simplifications, for example n < 0 is the same as n ≤ −1. 

**Loop syntax.** Loops are written as while (B) do { … }, with braces around the body. 

## **1. Sequential composition (exercises a to e)** 

**Rules used in this section** 

**Assignment rule.** WP(x := e, Q) = Q[x ← e]. We take the postcondition Q and replace every occurrence of x by the expression e. 

Page 1 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Sequence rule.** WP(S1; S2, Q) = WP(S1, WP(S2, Q)). As a consequence, we start with the last statement and work upwards. The simplified WP of one row of the table is the postcondition of the next row. 

**Checking a triple.** The triple {P} S {Q} is valid when P ⇒ WP(S, Q). 

### **Exercise a** 

**Find the weakest** **<mark>p</mark> recondition** { ?? } **a := x + 2; b := a - y; c := b + 3;** <u>{ c = x − y + 5 }</u> 

**Step 1. Compute the WP from the last statement to the first** 

|**Goal: c**<br>W|**ompute**WP(S, Q) <br>P(a := x + 2; b :=|**, that is:**<br>a − y; c := b + 3,  c = x|− y + 5)||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|3|c := b + 3|c = x − y + 5|[c ← b + 3]|b + 3 = x − y + 5<br>which simplifies to<br>b = x − y + 2|
|2|b := a - y|b = x − y + 2|[b ← a − y]|a − y = x − y + 2<br>which simplifies to<br>a = x + 2|
|1|a := x + 2|a = x + 2|[a ← x + 2]|x + 2 = x + 2<br>which simplifies to<br>True|



#### **Step 2. Result** 

The weakest precondition is True. In this case the postcondition holds after the program in every starting state. We can confirm it by following the values: c = b + 3 = (a − y) + 3 = (x + 2 − y) + 3 = x − y + 5. 

Page 2 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{True}|_// weakest precondition_|
|{x + 2 = x + 2}|_// equivalent to True_|
|**a := x + 2;**||
|{ a = x + 2 }||
|**b := a - y;**||
|{b = x − y + 2}||
|**c := b + 3;**||
|{c = x −y+ 5}|_// postcondition_|



### **Exercise b** 

**Check the triple** { x ≥ 0 ∧ y = 2 ∧ x = x′ } **z := x + y; x := z - 1;** { x = x′ + 1 ∧ z = x′ + 2 } 

The conjunct x = x′ is needed because the postcondition talks about xʹ. 

**Step 1. Compute the WP from the last statement to the first** 

**To prove** P ⇒ WP(S, Q) **, that is:** x ≥ 0 ∧ y = 2 ∧ x = x′ ⇒  WP(z := x + y; x := z − 1,  x = x′ + 1 ∧ z = x′ + 2) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|x := z - 1|x = x′ + 1 ∧ z = x′ + 2|[x ← z − 1]|z − 1 = x′ + 1 ∧ z = x′ + 2<br>which simplifies to|
|||||z = x′ + 2|
|||||Both conjuncts say the same thing.|
|1|z := x + y|z = x′ + 2|[z ← x + y]|x + y = x′ + 2|



**Step 2. Compare the precondition with the WP** 

|**Formula**|**Reason**|
|---|---|
|x + y = x′ + y|From x = xʹ in the precondition.|
|= x′ + 2|From y = 2 in the precondition.|



Therefore the precondition implies the WP, and the triple is valid. The conjunct x ≥ 0 is not used. The precondition is stronger than necessary. 

Page 3 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x ≥ 0 ∧y= 2 ∧ x = x′}|_// given precondition_|
|{x +y= x′ + 2}|_// since x = xʹ and y = 2_|
|**z := x + y;**||
|{z = x′ + 2}|_// same as z − 1 = xʹ + 1_∧_z = xʹ + 2_|
|**x := z - 1;**||
|{x = x′ + 1 ∧ z = x′ + 2}|_// postcondition_|



### **Exercise c** 

**Find the weakest** **<mark>p</mark> recondition** { ?? } **x := y + 4; y := x - 2;** <u>{ y = y′ + 2 }</u> 

**Step 1. Compute the WP from the last statement to the first** 

|**Goal: c**<br>W|**ompute**WP(S, Q)<br>P(x := y + 4; y :=|**, that is:**<br>x − 2,  y = y′ + 2)|||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|2|y := x - 2|y = y′ + 2|[y ← x − 2]|x − 2 = y′ + 2<br>which simplifies to<br>x = y′ + 4|
|1|x := y + 4|x = y′ + 4|[x ← y + 4]|y + 4 = y′ + 4<br>which simplifies to<br>y = y′|



**Step 2. Result** 

The weakest precondition is y = y′. This condition only says that yʹ really is the initial value of y. As a consequence, the program increases y by 2 in every starting state: the final y is (y + 4) − 2. 

|**Proof outline**||
|---|---|
|{ y=y′}|_// weakest precondition_|
|**x := y + 4;**||
|{ x = y′ + 4 }||
|**y := x - 2;**||
|{ y=y′ + 2}|_// postcondition_|



Page 4 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise d** 

**Check the triple** { x = 1 ∧ y = 2 ∧ x = x′ } **t := x + y; y := t + y;** { y = 2 · x′ + 3 } 

The conjunct x = x′ is needed because the postcondition talks about xʹ. 

**Step 1. Compute the WP from the last statement to the first** 

**To prove** P ⇒ WP(S, Q) **, that is:** x = 1 ∧ y = 2 ∧ x = x′ ⇒  WP(t := x + y; y := t + y,  y = 2 · x′ + 3) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|y := t + y|y = 2 · x′ + 3|[y ← t + y]|t + y = 2 · x′ + 3|
|1|t := x + y|t + y = 2 · x′ + 3|[t ← x + y]|(x + y) + y = 2 · x′ + 3<br>which simplifies to<br>x + 2 · y = 2 · x′ + 3|



**Step 2. Compare the precondition with the WP** 

|**Formula**|**Reason**|
|---|---|
|x + 2 · y = 1 + 2 · 2 = 5|From x = 1 and y = 2.|
|2 · x′ + 3 = 2 · 1 + 3 = 5|From xʹ = x = 1.|



Both sides are equal to 5, so the precondition implies the WP and the triple is valid. 

|**Proof outline**||
|---|---|
|{x = 1 ∧y= 2 ∧ x = x′}|_// given precondition_|
|{x + 2 ·y= 2 · x′ + 3}|_// both sides equal 5_|
|**t := x + y;**||
|{t + y = 2 · x′ + 3}||
|**y := t + y;**||
|{ y= 2 · x′ + 3}|_// postcondition_|



### **Exercise e** 

**Find the weakest precondition** { ?? } **p := q + 2 * r; r := p - r;** { r = q + r′ } 

Page 5 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 1. Compute the WP from the last statement to the first** 

|**Goal: c**<br>W|**ompute**WP(S, Q)<br>P(p := q + 2 · r; r|**, that is:**<br>:= p − r,  r = q + r′)|||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|2|r := p - r|r = q + r′|[r ← p − r]|p − r = q + r′|
|1|p := q + 2<br>* r|p − r = q + r′|[p ← q +<br>2 · r]|(q + 2 · r) − r = q + r′<br>which simplifies to<br>q + r = q + r′<br>that is<br>r = r′|



#### **Step 2. Result** 

The weakest precondition is r = r′. As in exercise c, it only says that rʹ is the initial value of r. The program sets r to q + r in every starting state. Note that the variable q is not changed by the program, so q in the postcondition is the same as q at the start. 

|**Proof outline**||
|---|---|
|{r = r′}|_// weakest precondition_|
|{ (q+ 2 · r)− r =q+ r′}|_// equivalent to r = rʹ_|
|**p := q + 2 * r;**||
|{p − r = q + r′}||
|**r := p - r;**||
|{r =q+ r′}|_// postcondition_|



Page 6 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **2. Conditional statement (exercises f to k)** 

**Rules used in this section Conditional rule.** WP(if B then S1 else S2, Q) = (B ⇒ WP(S1, Q)) ∧ (¬B ⇒ WP(S2, Q)). **Method.** First compute the WP of each branch with respect to the same postcondition Q. Then combine the two results with the formula above and simplify. Finally state the result, or check that the given precondition implies it. 

**Two facts that help with the simplification.** An implication A ⇒ B is true when every state that satisfies A also satisfies B. If B is true in every state, then A ⇒ B is true whatever A is. **In the proof outline** , each branch starts with the precondition together with the guard (then branch) or its negation (else branch). That assertion must imply the WP of the branch. 

### **Exercise f** 

**Check the triple** { x ≥ 0 ∧ y ≥ 0 ∧ x = x′ ∧ y = y′ } **if (x > y) then z := x - y; else z := y - x;** { z = |x′ − y′| } 

The conjuncts x = x′ ∧ y = y′ are needed because the postcondition talks about xʹ and yʹ. 

**Step 1. Compute the WP of each branch** 

|**To prove**|P ⇒ WP(S, Q|)**, that is:**|||
|---|---|---|---|---|
|x ≥<br>⇒  W|0 ∧ y ≥ 0 ∧ x<br>P(if (x > y) t|= x′ ∧ y = y′<br>hen z := x − y else|z := y − x,  z =||x′ − y′|)|
|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|then|x > y|z := x - y|[z ← x − y]|x − y = |x′ − y′||
|else|x ≤ y|z := y - x|[z ← y − x]|y − x = |x′ − y′||



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x > y ⇒ x − y = |x′ − y′|)|Conditional rule.|
|∧ (x ≤ y ⇒ y − x = |x′ − y′|)||



Page 7 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 3. Compare the precondition with the WP** 

Under the precondition, xʹ = x and yʹ = y. We replace xʹ and yʹ and check each implication. 

|**Implication**|**Why it holds**|
|---|---|
|x > y ⇒ x − y = |x − y||If x > y then x − y is positive, and the absolute value of<br>a positive number is the number itself.|
|x ≤ y ⇒ y − x = |x − y||If x ≤ y then x − y is zero or negative, so |x − y| = −(x −<br>y) = y − x.|



Both implications hold, so the triple is valid. The conjuncts x ≥ 0 ∧ y ≥ 0 are not used. The program computes the distance between x and y for any two integers. 

|**Proof outline**||
|---|---|
|{x ≥ 0 ∧y≥ 0 ∧ x = x′ ∧y=y′}|_// given precondition_|
|**if (x > y) then {**||
|{x = x′ ∧y=y′ ∧ x >y }|_// precondition_∧_guard_|
|{x −y=|x′ −y′| }|_// xʹ − yʹ is positive_|
|**z := x - y;**||
|{z = |x′ − y′|}||
|**} else {**||
|{x = x′ ∧y=y′ ∧ x ≤y }|_// precondition_∧_¬guard_|
|{ y− x =|x′ −y′| }|_// xʹ − yʹ is zero or negative_|
|**z := y - x;**||
|{z = |x′ − y′|}||
|**}**||
|{z =|x′ −y′| }|_// postcondition_|



### **Exercise g** 

**Find the weakest precondition** { ?? } **if (n < 0) then n := -n; else n := n + 1;** { n ≥ 1 } 

Page 8 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Step 1. Compute the WP of each branch** 

|**Goal: co**|**mpute**WP(S,|Q)**, that is:**|||
|---|---|---|---|---|
|WP(|if (n < 0) the|n n := −n else n :|= n + 1,  n ≥ 1)||
|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|then|n < 0|n := -n|[n ← −n]|−n ≥ 1  =  n ≤ −1|
|else|n ≥ 0|n := n + 1|[n ← n + 1]|n + 1 ≥ 1  =  n ≥ 0|



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (n < 0 ⇒ n ≤ −1) ∧ (n ≥ 0 ⇒ n ≥ 0)|Conditional rule.|
|= True ∧ True|For integers, n < 0 and n ≤ −1 describe the same<br>values. The second implication has the same formula<br>on both sides.|
|= True||



#### **Step 3. Result** 

The weakest precondition is True. A negative n becomes at least 1 when its sign is changed, and a nonnegative n becomes at least 1 when it is increased by 1. 

|**Proof outline**||
|---|---|
|{True}|_// weakest precondition_|
|**if (n < 0) then {**||
|{n < 0}|_// precondition_∧_guard_|
|{−n ≥ 1}|_// n < 0 gives n ≤ −1 for integers_|
|**n := -n;**||
|{ n ≥ 1 }||
|**} else {**||
|{n ≥ 0}|_// precondition_∧_¬guard_|
|{n + 1 ≥ 1}|_// same as n ≥ 0_|
|**n := n + 1;**||
|{ n ≥ 1 }||
|**}**||
|{n ≥ 1}|_// postcondition_|



### **Exercise h** 

In this exercise n is a real number. The program and the postcondition are the same as in exercise g, so the exercise shows how the answer depends on the type of n. 

Page 9 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Find the weakest precondition (n is a real number)** { ?? } **if (n < 0) then n := -n; else n := n + 1;** { n ≥ 1 } 

**Step 1. Compute the WP of each branch** 

**Goal: compute** WP(S, Q) **, that is:** WP(if (n < 0) then n := −n else n := n + 1,  n ≥ 1) 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|n < 0|n := -n|[n ← −n]|−n ≥ 1  =  n ≤ −1|
|else|n ≥ 0|n := n + 1|[n ← n + 1]|n + 1 ≥ 1  =  n ≥ 0|



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (n < 0 ⇒ n ≤ −1) ∧ (n ≥ 0 ⇒ n ≥ 0)|Conditional rule. The branch WPs are the same as in g.|
|= (n < 0 ⇒ n ≤ −1) ∧ True|The second implication has the same formula on both<br>sides.|
|= n ≥ 0 ∨ n ≤ −1|A⇒B is the same as ¬A∨B. For real numbers, n < 0<br>no longer implies n ≤ −1, so the first implication does<br>not simplify to True.|



#### **Step 3. Result** 

The weakest precondition is n ≤ −1 ∨ n ≥ 0. The values strictly between −1 and 0 are excluded. For example, n = −0.5 enters the then branch and ends with n = 0.5, which is less than 1. Over the integers there is no value between −1 and 0, which is why the answer of g is True. 

Page 10 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{n ≤ −1 ∨ n ≥ 0}|_// weakest precondition_|
|**if (n < 0) then {**||
|{ (n ≤ −1 ∨ n ≥ 0)∧ n < 0}|_// precondition_∧_guard_|
|{−n ≥ 1}|_// n < 0 rules out n ≥ 0, so n ≤ −1_|
|**n := -n;**||
|{n ≥ 1}||
|**} else {**||
|{ (n ≤ −1 ∨ n ≥ 0)∧ n ≥ 0}|_// precondition_∧_¬guard_|
|{n + 1 ≥ 1}|_// same as n ≥ 0_|
|**n := n + 1;**||
|{ n ≥ 1 }||
|**}**||
|{n ≥ 1}|_// postcondition_|



### **Exercise i** 

|**Check the triple**|
|---|
|{x = x′ ∧ y = y′}|
|**if (x = 0) then**|
|**y := y + 1;**|
|**else**|
|**y := y - 1;**|
|{ (x′ = 0 ⇒ y = y′ + 1)∧(x′ ≠ 0 ⇒ y = y′ − 1) }|



#### **Step 1. Compute the WP of each branch** 

Only y is assigned, so the substitution changes y and leaves xʹ and yʹ alone. 

**To prove** P ⇒ WP(S, Q) **, that is:** x = x′ ∧ y = y′ ⇒  WP(if (x = 0) then y := y + 1 else y := y − 1,  (x′ = 0 ⇒ y = y′ + 1) ∧ (x′ ≠ 0 ⇒ y = y′ − 1)) 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|x = 0|y := y + 1|[y ← y + 1]|(x′ = 0 ⇒ y + 1 = y′ + 1) ∧ (x′ ≠ 0 ⇒ y + 1 = y′ −<br>1)<br>which simplifies to<br>(x′ = 0 ⇒ y = y′) ∧ (x′ ≠ 0 ⇒ y = y′ − 2)|
|else|x ≠ 0|y := y - 1|[y ← y − 1]|(x′ = 0 ⇒ y − 1 = y′ + 1) ∧ (x′ ≠ 0 ⇒ y − 1 = y′ −<br>1)<br>which simplifies to<br>(x′ = 0 ⇒ y = y′ + 2) ∧ (x′ ≠ 0 ⇒ y = y′)|



Page 11 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x = 0 ⇒ (x′ = 0 ⇒ y = y′) ∧ (x′ ≠ 0 ⇒ y = y′ −<br>2))|Conditional rule.|
|∧ (x ≠ 0 ⇒ (x′ = 0 ⇒ y = y′ + 2) ∧ (x′ ≠ 0 ⇒ y =<br>y′))||



**Step 3. Compare the precondition with the WP** 

We assume x = x′ ∧ y = y′ and consider the two possible cases for x. 

|**Case**|**Why WP_if holds**|
|---|---|
|Casex = 0|Then xʹ = 0. The first implication of the then WP holds,<br>since y = yʹ. The second holds because its premise xʹ ≠<br>0 is false. The else part of WP_if holds because its<br>premise x ≠ 0 is false.|
|Casex ≠ 0<br>herefore the triple is valid. In each branch, one of the<br>ecause its premise is false. This is why the linkx = x′i<br>bout x, with the postcondition, which talks about xʹ.|Then xʹ ≠ 0. The then part of WP_if holds because its<br>premise x = 0 is false. In the else WP, the first<br>implication holds because xʹ = 0 is false, and the<br>second holds since y = yʹ.<br>two implications of the postcondition is true onl<br>s needed: it connects the guard, which talks|
|**Proof outline**||
|{x = x′ ∧y=y′}<br>**if (x = 0) then {**|_// given precondition_|
|{x = x′ ∧y=y′ ∧ x = 0}<br>{ (x′ = 0 ⇒y+ 1 =y′ + 1)∧(x′ ≠ 0 ⇒y+ 1 =y′<br>**y := y + 1;**<br>{ (x′ = 0 ⇒ y = y′ + 1)∧(x′ ≠ 0 ⇒ y = y′ − 1) }|_// precondition_∧_guard_<br>− 1) }<br>_// xʹ = 0 and y = yʹ_|
|**} else {**||
|{x = x′ ∧y=y′ ∧ x ≠ 0}|_// precondition_∧_¬guard_|
|{ (x′ = 0 ⇒y− 1 =y′ + 1)∧(x′ ≠ 0 ⇒y− 1 =y′<br>**y := y - 1;**<br>{ (x′ = 0 ⇒ y = y′ + 1) ∧ (x′ ≠ 0 ⇒ y = y′ − 1) }<br>**}**|− 1) }<br>_// xʹ ≠ 0 and y = yʹ_|
|{ (x′ = 0 ⇒y=y′ + 1)∧(x′ ≠ 0 ⇒y=y′ − 1) }|_// postcondition_|



Therefore the triple is valid. In each branch, one of the two implications of the postcondition is true only because its premise is false. This is why the link x = x′ is needed: it connects the guard, which talks about x, with the postcondition, which talks about xʹ. 

Page 12 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise j** 

**Find the weakest precondition** { ?? } **if (a + b > 10) then c := a - b; else c := b - a;** { c ≤ |a − b| } 

**Step 1. Compute the WP of each branch** 

**Goal: compute** WP(S, Q) **, that is:** WP(if (a + b > 10) then c := a − b else c := b − a,  c ≤ |a − b|) 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|a + b > 10|c := a - b|[c ← a − b]|a − b ≤ |a − b|<br>This is always true, since every number is at most its<br>absolute value.<br>= True|
|else|a + b ≤ 10|c := b - a|[c ← b − a]|b − a ≤ |a − b|<br>This is always true, since b − a = −(a − b) and the<br>negation of a number is also at most its absolute value.<br>= True|



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (a + b > 10 ⇒ True) ∧ (a + b ≤ 10 ⇒ True)|Conditional rule.|
|= True|An implication with a true conclusion is true.|



#### **Step 3. Result** 

The weakest precondition is True. The guard does not matter here: both branches set c to a value that is at most |a − b|. 

Page 13 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{True}|_// weakest precondition_|
|**if (a + b > 10) then {**||
|{a + b > 10}|_// precondition_∧_guard_|
|{a − b ≤|a − b| }|_// always true_|
|**c := a - b;**||
|{c ≤ |a − b|}||
|**} else {**||
|{a + b ≤ 10}|_// precondition_∧_¬guard_|
|{b − a ≤|a − b| }|_// always true_|
|**c := b - a;**||
|{ c ≤ |a − b| }||
|**}**||
|{c ≤|a − b| }|_// postcondition_|



### **Exercise k** 

We use the definition: even(x) means x mod 2 = 0. 

**Check the triple** <u>{ even(x) }</u> **if (x mod 2 = 0) then x := x + 2; else x := x + 1;** { even(x) } 

**Step 1. Compute the WP of each branch** 

**To prove** P ⇒ WP(S, Q) **, that is:** even(x) ⇒  WP(if (x mod 2 = 0) then x := x + 2 else x := x + 1,  even(x)) 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|x mod 2 = 0|x := x + 2|[x ← x + 2]|even(x + 2)<br>Adding 2 does not change parity, so this is the same as:<br>even(x)|
|else|x mod 2 ≠ 0|x := x + 1|[x ← x + 1]|even(x + 1)<br>Adding 1 changes parity, so this is the same as:<br>¬even(x)|



Page 14 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x mod 2 = 0 ⇒ even(x)) ∧ (x mod 2 ≠ 0 ⇒<br>¬even(x))|Conditional rule.|
|= True ∧ True|By definition even(x) is x mod 2 = 0, so each<br>implication has the same formula on both sides.|
|= True||



#### **Step 3. Compare the precondition with the WP** 

The given precondition even(x) implies True, so the triple is valid. The WP shows that the precondition is stronger than needed: the program makes x even from any starting value. 

The else branch deserves attention. Under the precondition, the assertion at the start of that branch is even(x) ∧ x mod 2 ≠ 0, which is False. The else branch can never run when the precondition holds, and an assertion that is False implies any formula. Its proof obligation is therefore satisfied without any work. 



<!-- Start of picture text -->
Proof outline<br>{ even(x) } // given precondition<br>if (x mod 2 = 0) then {<br>{ even(x) ∧ x mod 2 = 0 } // precondition  ∧  guard<br>{ even(x + 2) } // adding 2 keeps x even<br>x := x + 2;<br>{ even(x) }<br>} else {<br>{ even(x) ∧ x mod 2 ≠ 0 } // precondition  ∧  ¬guard = False<br>{ even(x + 1) } // False implies any formula<br>x := x + 1;<br>{ even(x) }<br>}<br>{ even(x) } // postcondition<br><!-- End of picture text -->

Page 15 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **3. Loops (exercises l to o)** 

**Rules used in this section** 

**While rule (combined with the consequence rule).** To prove {P} while B do S {Q} we need an invariant I and three obligations: 

(1) **Establishment:** P ⇒ I. The invariant holds before the first iteration. When the loop is preceded by initialisation statements, the obligation is P ⇒ WP(init, I). 

(2) **Preservation:** {I ∧ B} S {I}. We compute WP(S, I) and prove the implication I ∧ B ⇒ WP(S, I). 

(3) **Exit:** I ∧ ¬B ⇒ Q. When the loop stops, the guard is false and the invariant still holds, and together they must give the postcondition. 

(4) **Termination.** A variant E is an integer expression with two properties: (4a) I ∧ B ⇒ E ≥ 0, and (4b) I ∧ B ∧ E = E₀ ⇒ WP(S, E < E₀), where E₀ is the value of E before the iteration. The lecture slides call this value n; we write E₀ because n is often a program variable in these exercises. 

**How each obligation is presented.** First we write the implication out in full, with the actual formulas, in a green box. Then we prove it line by line. 

**Two kinds of replacement appear in the proofs.** The first is the assignment rule, WP(x := e, Q) = Q[x ← e], which we use to compute a WP; the tables show it in the column Substitution. The second is replacement of equals by equals: when the assumptions contain an equation such as i = 0, we may replace i by 0 in the formula we are proving. The two look similar, but only the first one comes from a program statement. 

**Where the invariant comes from.** We start from the postcondition, trace the variables at the loop head, generalise the postcondition by replacing the final value with the loop counter, and add bounds for the counter. 

#### **Finding a precondition when the program contains a loop** 

For exercises m and n the precondition is { ?? } and the program is an initialisation followed by a loop. The WP of a loop cannot be computed by substitution alone, since we do not know in advance how many times the body runs. We therefore proceed in two parts. 

**Part 1: a valid precondition.** We find an invariant I and prove preservation and exit. Then we compute WP(init, I), the WP of the initialisation statements with respect to I. Every state that satisfies this WP makes I true at the loop head, so the whole triple is valid from that state. We take this WP as the precondition P, so the establishment obligation P ⇒ WP(init, I) holds. This part is a proof. 

**Part 2: it is the weakest.** Part 1 does not show that a weaker precondition is impossible, since a different invariant could give a weaker answer. We show it separately: for every state that falsifies our precondition, we run the program by hand and show that the postcondition fails. 

Page 16 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise l** 

**Check the triple** { x = x′ ∧ x′ ≥ 0 ∧ z = 0 } **while (x > 0) do { z := z + 2; x := x - 1; }** { z = 2 · x′ } 

**Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for xʹ = 3. 

|**At the loop head**|**x**|**z**|**2 ·(xʹ − x)**|
|---|---|---|---|
|before iteration 1|3|0|0|
|before iteration 2|2|2|2|
|before iteration 3|1|4|4|
|at exit (x = 0)|0|6|6|



Here the loop counts down. The number of completed iterations is x′ − x, and each iteration adds 2 to z. Therefore z = 2 · (x′ − x) at every loop head. At the exit x = 0, and the formula becomes the postcondition. The counter x never goes below 0, which gives the bound x ≥ 0. The variant is x itself. 

**Invariant** I  ≡  z = 2 · (x′ − x) ∧ x ≥ 0 **Guard** B  ≡  x > 0 **Variant** E  =  x 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** x = x′ ∧ x′ ≥ 0 ∧ z = 0 ⇒ z = 2 · (x′ − x) ∧ x ≥ 0 

The precondition contains the equations z = 0 and x = xʹ. We replace z by 0 and x by xʹ in the conclusion. 

|**Step of theproof**|**Reason**|
|---|---|
|(z = 2 · (x′ − x) ∧ x ≥ 0)[z ← 0, x ← x′]|Replace z by 0 and x by xʹ, using P.|
|= 0 = 2 · (x′ − x′) ∧ x′ ≥ 0||
|= 0 = 0 ∧ x′ ≥ 0|xʹ − xʹ = 0.|
|= True|xʹ ≥ 0 is part of P.|



Page 17 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

|**To pro**<br>z =<br>⇒|**ve**I ∧ B ⇒ WP(bo<br>2 · (x′ − x) ∧ x<br>WP(z := z + 2; x|dy, I)**, that is:**<br>≥ 0 ∧ x > 0<br>:= x − 1,  z = 2 · (x′ − x) ∧ x ≥|0)||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|2|x := x - 1|z = 2 · (x′ − x) ∧ x ≥ 0|[x ← x − 1]|z = 2 · (x′ − (x − 1)) ∧ x − 1 ≥ 0<br>which simplifies to<br>z = 2 · (x′ − x) + 2 ∧ x ≥ 1|
|1|z := z + 2|z = 2 · (x′ − x) + 2 ∧ x ≥ 1|[z ← z + 2]|z + 2 = 2 · (x′ − x) + 2 ∧ x ≥ 1<br>which simplifies to<br>z = 2 · (x′ − x) ∧ x ≥ 1|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** z = 2 · (x′ − x) ∧ x ≥ 0 ∧ x > 0 ⇒ z = 2 · (x′ − x) ∧ x ≥ 1 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|z = 2 · (x′ − x)|Part of I.|
|x ≥ 1|From the guard x > 0, since x is an integer.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** z = 2 · (x′ − x) ∧ x ≥ 0 ∧ ¬(x > 0) ⇒ z = 2 · x′ 



|**Step of theproof**|**Reason**|
|---|---|
|¬(x > 0)  =  x ≤ 0|Negation of the guard.|
|x ≥ 0 ∧ x ≤ 0  gives  x = 0|Combine with x ≥ 0 from I.|
|z = 2 · (x′ − 0) = 2 · x′|Replace x by 0 in z = 2 · (xʹ − x).|



**Step 5. Termination with the variant** E = x **(4a) The variant is not negative while the loop runs.** 

Page 18 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** z = 2 · (x′ − x) ∧ x ≥ 0 ∧ x > 0 ⇒ x ≥ 0 

Part of I (it also follows from the guard). 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** z = 2 · (x′ − x) ∧ x ≥ 0 ∧ x > 0 ∧ x = E₀ ⇒  WP(z := z + 2; x := x − 1,  x < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|x := x - 1|x < E₀|[x ← x − 1]|x − 1 < E₀|
|1|z := z + 2|x − 1 < E₀|[z ← z + 2]|x − 1 < E₀<br>z does not occur.|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** z = 2 · (x′ − x) ∧ x ≥ 0 ∧ x > 0 ∧ x = E₀ ⇒ x − 1 < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|x − 1 = E₀ − 1 < E₀|Replace x by E₀.|



#### **Step 6. Proof outline** 

**Proof outline** <u><mark>{ x = x′ ∧ x′ ≥ 0 ∧ z = 0 }</mark></u> _// given precondition_ <u><mark>{ z = 2 · (x′ − x) ∧ x ≥ 0 }</mark></u> _// establishment: P_ ⇒ _I_ **while (x > 0) do {** <u><mark>{ z = 2 · (x′ − x) ∧ x ≥ 0 ∧ x > 0 }</mark></u> _// I_ ∧ _B_ <u><mark>{ z + 2 = 2 · (x′ − x) + 2 ∧ x ≥ 1 }</mark></u> _// preservation: implied by I_ ∧ _B_ **z := z + 2;** { z = 2 · (x′ − (x − 1)) ∧ x − 1 ≥ 0 } **x := x - 1;** <u><mark>{ z = 2 · (x′ − x) ∧ x ≥ 0 }</mark></u> _// I holds again_ **}** <u><mark>{ z = 2 · (x′ − x) ∧ x ≥ 0 ∧ ¬(x > 0) }</mark></u> _// I_ ∧ _¬B_ <u><mark>{ z = 2 · x′ }</mark></u> _// exit: x = 0_ 

Page 19 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

Page 20 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise m** 

|**Find**|**the weakest precondition**|
|---|---|
|{ ??|}|
|**i :**|**= 0;**|
|**s :**|**= 0;**|
|**whi**|**le (i < n) do {**|
||**s := s + 1;**|
||**i := i + 1;**|
|**}**||
|{s =|n}|



#### **Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for n = 3. 

|**At the loop head**|**i**|**s**|
|---|---|---|
|before iteration 1|0|0|
|before iteration 2|1|1|
|before iteration 3|2|2|
|at exit (i = n)|3|3|



The two variables are always equal, so s = i. The counter stops at n, which gives the bound i ≤ n. We do not need a lower bound for i in this exercise. 

**Invariant** I  ≡  s = i ∧ i ≤ n **Guard** B  ≡  i < n **Variant** E  =  n − i 

#### **Step 2. Establishment:** P ⇒ WP(init, I) 

The precondition is unknown, so we compute WP(init, I) for the two initial assignments and take the result as the precondition P. 

**Goal: compute** WP(init, I) **, that is:** WP(i := 0; s := 0,  s = i ∧ i ≤ n) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|s := 0|s = i ∧ i ≤ n|[s ← 0]|0 = i ∧ i ≤ n|
|1|i := 0|0 = i ∧ i ≤ n|[i ← 0]|0 = 0 ∧ 0 ≤ n<br>which simplifies to<br>n ≥ 0|



**To prove** P ⇒ WP(init, I) **, written out in full** n ≥ 0 

Page 21 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

⇒ 0 = 0 ∧ 0 ≤ n 

With P equal to the computed WP, the obligation holds by construction. We still write it out, to show what the precondition must guarantee. 

|**Step of theproof**|**Reason**|
|---|---|
|0 = 0|Always true.|
|0 ≤ n|This is P itself.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** s = i ∧ i ≤ n ∧ i < n ⇒  WP(s := s + 1; i := i + 1,  s = i ∧ i ≤ n) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|i := i + 1|s = i ∧ i ≤ n|[i ← i + 1]|s = i + 1 ∧ i + 1 ≤ n|
|1|s := s + 1|s = i + 1 ∧ i + 1 ≤ n|[s ← s + 1]|s + 1 = i + 1 ∧ i + 1 ≤ n|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** 

s = i ∧ i ≤ n ∧ i < n ⇒ s + 1 = i + 1 ∧ i + 1 ≤ n 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|s + 1 = i + 1|Replace s by i, using s = i from I.|
|i + 1 ≤ n|From the guard i < n.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** s = i ∧ i ≤ n ∧ ¬(i < n) ⇒ s = n 

Page 22 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|¬(i < n)  =  i ≥ n|Negation of the guard.|
|i ≤ n ∧ i ≥ n  gives  i = n|Combine with i ≤ n from I.|
|s = i  becomes  s = n|Replace i by n.|



**Step 5. Show that n ≥ 0 is the weakest precondition** Steps 2 to 4 prove that n ≥ 0 is a valid precondition. Now consider any state with n < 0. After the initialisation i = 0, so the guard 0 < n is false and the body never runs. The program ends with s = 0. The postcondition s = n would require n = 0, which contradicts n < 0. Every state outside n ≥ 0 therefore fails the postcondition, so no weaker precondition exists. 

**Result.** The weakest precondition is n ≥ 0. 

**Step 6. Termination with the variant** E = n − i 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** s = i ∧ i ≤ n ∧ i < n ⇒ n − i ≥ 0 

From the guard i < n we get n − i > 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** s = i ∧ i ≤ n ∧ i < n ∧ n − i = E₀ ⇒  WP(s := s + 1; i := i + 1,  n − i < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|i := i + 1|n − i < E₀|[i ← i + 1]|n − (i + 1) < E₀|
|1|s := s + 1|n − (i + 1) < E₀|[s ← s + 1]|n − (i + 1) < E₀<br>s does not occur.|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** s = i ∧ i ≤ n ∧ i < n ∧ n − i = E₀ ⇒ n − (i + 1) < E₀ 

Page 23 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|n − (i + 1) = E₀ − 1 < E₀|Replace n − i by E₀.|



#### **Step 7. Proof outline** 

|**Proof outline**||
|---|---|
|{n ≥ 0}|_// weakest precondition_|
|{0 = 0 ∧ 0 ≤ n}|_// equivalent to n ≥ 0_|
|**i := 0;**||
|{ 0 = i ∧ i ≤ n }||
|**s := 0;**||
|{s = i ∧ i ≤ n}|_// I holds at the loop head_|
|**while (i < n) do {**||
|{s = i ∧ i ≤ n ∧ i < n}|_// I_∧_B_|
|{s + 1 = i + 1 ∧ i + 1 ≤ n}|_// preservation: implied by I_∧_B_|
|**s := s + 1;**||
|{ s = i + 1 ∧ i + 1 ≤ n }||
|**i := i + 1;**||
|{s = i ∧ i ≤ n}|_// I holds again_|
|**}**||
|{s = i ∧ i ≤ n ∧ ¬(i < n) }|_// I_∧_¬B_|
|{s = n}|_// exit: i = n_|



Page 24 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise m (second part): integer division** 

The loop computes the quotient q and the remainder r of the division of x by y by repeated subtraction. 

|**Check the triple**<br>{ x = x′ ∧ y = y′ ∧ x′ ≥ 0 ∧ y′ > 0 ∧ q = 0 ∧ r = x }|
|---|
|**while (r >= y) do {**|
|**r := r - y;**|
|**q := q + 1;**|
|**}**|
|{ x′ = q · y′ + r ∧ 0 ≤ r < y′ }|



#### **Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for xʹ = 17 and yʹ = 5. 

|**At the loop head**|**q**|**r**|**q ·yʹ + r**|
|---|---|---|---|
|before iteration 1|0|17|17|
|before iteration 2|1|12|17|
|before iteration 3|2|7|17|
|at exit (r < 5)|3|2|17|



The value q · y′ + r stays equal to xʹ, because each iteration moves one copy of yʹ from r into q. The remainder never becomes negative, since the body only subtracts when r ≥ y. The part r < y′ of the postcondition is the negated guard, so it does not belong in the invariant. The program never assigns to y, so y = y′ stays true, and we keep it in the invariant because preservation needs it. 

**Invariant** I  ≡  x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 **Guard** B  ≡  r ≥ y **Variant** E  =  r 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** x = x′ ∧ y = y′ ∧ x′ ≥ 0 ∧ y′ > 0 ∧ q = 0 ∧ r = x ⇒ x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 

The precondition contains the equations q = 0 and r = x = xʹ. We replace q by 0 and r by xʹ in the conclusion. 

Page 25 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|I[q ← 0, r ← x′]|Replace q by 0 and r by xʹ, using q = 0, r = x and x = xʹ|
|= x′ = 0 · y′ + x′ ∧ 0 ≤ x′ ∧ y = y′ ∧ y′ > 0|from P.|
|= True ∧ 0 ≤ x′ ∧ y = y′ ∧ y′ > 0|0 · yʹ + xʹ = xʹ.|
|= True|xʹ ≥ 0, y = yʹ and yʹ > 0 are all part of P.|



The conjunct x′ ≥ 0 of the precondition is the only fact that gives 0 ≤ r at the start. Without it the triple could not be proved: for x = −3 and y = 2 the loop does not run and the program ends with r = −3. 

#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 ∧ r ≥ y ⇒  WP(r := r − y; q := q + 1,  x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|q := q + 1|x′ = q · y′ + r ∧ 0 ≤ r ∧ y =|[q ← q + 1]|x′ = (q + 1) · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧|
|||y′ ∧ y′ > 0||y′ > 0|
|1|r := r - y|x′ = (q + 1) · y′ + r ∧ 0 ≤ r|[r ← r − y]|x′ = (q + 1) · y′ + (r − y) ∧ 0 ≤ r − y|
|||∧ y = y′ ∧ y′ > 0||∧ y = y′ ∧ y′ > 0|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 ∧ r ≥ y ⇒ x′ = (q + 1) · y′ + (r − y) ∧ 0 ≤ r − y ∧ y = y′ ∧ y′ > 0 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|(q + 1) · y′ + (r − y) = q · y′ + y′ + r − y′|Expand, and replace y by yʹ, using y = yʹ from I.|
|= q · y′ + r = x′|The two copies of yʹ cancel. Then use xʹ = q · yʹ + r from<br>|
|0 ≤ r − y|I.<br>From the guard r ≥ y.|
|y = y′ ∧ y′ > 0|Part of I.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 ∧ ¬(r ≥ y) ⇒ 

Page 26 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

x′ = q · y′ + r ∧ 0 ≤ r < y′ 

|**Step of theproof**|**Reason**|
|---|---|
|¬(r ≥ y)  =  r < y|Negation of the guard.|
|r < y′|Replace y by yʹ, using y = yʹ from I.|
|x′ = q · y′ + r ∧ 0 ≤ r|Part of I.|



#### **Step 5. Termination with the variant** E = r 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 ∧ r ≥ y ⇒ r ≥ 0 

From r ≥ y = yʹ > 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 ∧ r ≥ y ∧ r = E₀ ⇒  WP(r := r − y; q := q + 1,  r < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|q := q + 1|r < E₀|[q ← q + 1]|r < E₀|
|||||q does not occur.|
|1|r := r - y|r < E₀|[r ← r − y]|r − y < E₀|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** x′ = q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0 ∧ r ≥ y ∧ r = E₀ ⇒ r − y < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|r − y = E₀ − y′|Replace r by E₀ and y by yʹ.|
|E₀ − y′ < E₀|Since yʹ > 0.|



Page 27 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

The condition y′ > 0 is essential for termination. If y were 0, the body would not change r, and the loop would run forever for any x ≥ 0. The condition x′ ≥ 0 is not needed for termination; it is needed for 0 ≤ r at the exit. 

**Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{x = x′ ∧y=y′ ∧ x′ ≥ 0 ∧y′ > 0 ∧q= 0 ∧ r = x}|_// given precondition_|
|{x′ =q·y′ + r ∧ 0 ≤ r ∧y=y′ ∧y′ > 0}|_// establishment: P_⇒_I_|
|**while (r >= y) do {**||
|{x′ =q·y′ + r ∧ 0 ≤ r ∧y=y′ ∧y′ > 0 ∧ r ≥y }|_// I_∧_B_|
|{x′ =(q+ 1)·y′ +(r −y)∧ 0 ≤ r −y∧y=y′ ∧y′ > 0}|_// preservation_|
|**r := r - y;**||
|{x′ =(q + 1)· y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0}||
|**q := q + 1;**||
|{x′ =q·y′ + r ∧ 0 ≤ r ∧y=y′ ∧y′ > 0}<br>**}**|_// I holds again_|
|{x′ =q·y′ + r ∧ 0 ≤ r ∧y=y′ ∧y′ > 0 ∧ ¬(r ≥y) }|_// I_∧_¬B_|
|{x′ =q·y′ + r ∧ 0 ≤ r <y′}|_// exit_|



Page 28 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise n** 

|**Find**|**the weakest precondition**|
|---|---|
|{ ??|}|
|**i :**|**= 0;**|
|**s :**|**= 0;**|
|**whi**|**le (i <= n) do {**|
||**s := s + i;**|
||**i := i + 1;**|
|**}**||
|{s =|n ·(n + 1)/ 2}|



**Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for n = 3. 

|**At the loop head**|**i**|**s**|**i ·(i − 1) / 2**|
|---|---|---|---|
|before iteration 1|0|0|0|
|before iteration 2|1|0|0|
|before iteration 3|2|1|1|
|before iteration 4|3|3|3|
|at exit (i = n + 1)|4|6|6|



This loop differs from exercise 3b of the previous sheet in two ways. The body adds i before increasing it, and the guard is i ≤ n. As a consequence, at the loop head s holds the sum 0 + 1 + … + (i − 1), which is i · (i − 1) / 2. At the exit i = n + 1, and the formula becomes (n + 1) · n / 2, which is the postcondition. The counter starts at 0 and stops at n + 1, which gives the bounds 0 ≤ i ≤ n + 1. 

**Invariant** I  ≡  s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1 **Guard** B  ≡  i ≤ n **Variant** E  =  n + 1 − i 

#### **Step 2. Establishment:** P ⇒ WP(init, I) 

The precondition is unknown, so we compute WP(init, I) for the two initial assignments and take the result as the precondition P. 

Page 29 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Goal: compute** WP(init, I) **, that is:** WP(i := 0; s := 0,  s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|s := 0|s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n<br>+ 1|[s ← 0]|0 = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1|
|1|i := 0|0 = i · (i − 1) / 2 ∧ 0 ≤ i ≤|[i ← 0]|0 = 0 · (0 − 1) / 2 ∧ 0 ≤ 0 ≤ n + 1|
|||n + 1||which simplifies to<br>n ≥ −1|



**To prove** P ⇒ WP(init, I) **, written out in full** 

n ≥ −1 ⇒ 0 = 0 · (0 − 1) / 2 ∧ 0 ≤ 0 ≤ n + 1 

With P equal to the computed WP, the obligation holds by construction. We write it out to show where the bound on n comes from. 

|**Step of theproof**|**Reason**|
|---|---|
|0 = 0 · (0 − 1) / 2|0 · (−1) / 2 = 0.|
|0 ≤ 0|Always true.|
|0 ≤ n + 1|This is n ≥ −1, which is P.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1 ∧ i ≤ n ⇒  WP(s := s + i; i := i + 1,  s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|i := i + 1|s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n<br>+ 1|[i ← i + 1]|s = (i + 1) · i / 2 ∧ 0 ≤ i + 1 ≤ n + 1|
|1|s := s + i|s = (i + 1) · i / 2 ∧ 0 ≤ i + 1<br>≤ n + 1|[s ← s + i]|s + i = (i + 1) · i / 2 ∧ 0 ≤ i + 1 ≤ n<br>+ 1|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1 ∧ i ≤ n ⇒ s + i = (i + 1) · i / 2 ∧ 0 ≤ i + 1 ≤ n + 1 

Page 30 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|s + i = i · (i − 1) / 2 + i|Replace s, using I.|
|= i · (i − 1) / 2 + 2 · i / 2 = i · (i + 1) / 2|Write i with denominator 2 and factor out i.|
|0 ≤ i + 1|From 0 ≤ i.|
|i + 1 ≤ n + 1|From the guard i ≤ n.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1 ∧ ¬(i ≤ n) ⇒ s = n · (n + 1) / 2 



|**Step of theproof**|**Reason**|
|---|---|
|¬(i ≤ n)  =  i > n  =  i ≥ n + 1|Negation of the guard, for integers.|
|i ≤ n + 1 ∧ i ≥ n + 1  gives  i = n + 1|Combine with i ≤ n + 1 from I.|
|s = (n + 1) · ((n + 1) − 1) / 2 = n · (n + 1) / 2|Replace i by n + 1 in the invariant.|



#### **Step 5. Show that n ≥ −1 is the weakest precondition** 

Consider any state with n ≤ −2. After the initialisation i = 0, so the guard 0 ≤ n is false and the body never runs. The program ends with s = 0. However, for n ≤ −2 both n and n + 1 are negative, so n · (n + 1) / 2 is positive. For example, n = −2 gives (−2) · (−1) / 2 = 1. The postcondition fails, so no weaker precondition exists. 

**Result.** The weakest precondition is n ≥ −1. 

**Why the answer is not n ≥ 0** 

The precondition n ≥ 0 is valid, but it is not the weakest one. For n = −1 the loop does not run and s = 0, and the postcondition also gives (−1) · 0 / 2 = 0. Therefore the state n = −1 satisfies the postcondition even though the loop does nothing. 

The invariant method finds this case automatically: the bound i ≤ n + 1 at i = 0 gives exactly n ≥ −1. 

**Step 6. Termination with the variant** E = n + 1 − i 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** 

Page 31 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 



From the guard i ≤ n we get n + 1 − i ≥ 1. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1 ∧ i ≤ n ∧ n + 1 − i = E₀ ⇒  WP(s := s + i; i := i + 1,  n + 1 − i < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|i := i + 1|n + 1 − i < E₀|[i ← i + 1]|n + 1 − (i + 1) < E₀|
|1|s := s + i|n + 1 − (i + 1) < E₀|[s ← s + i]|n + 1 − (i + 1) < E₀<br>s does not occur.|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** s = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1 ∧ i ≤ n ∧ n + 1 − i = E₀ ⇒ n + 1 − (i + 1) < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|n + 1 − (i + 1) = E₀ − 1 < E₀|Replace n + 1 − i by E₀.|



Page 32 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 7. Proof outline** 

|**Proof outline**||
|---|---|
|{n ≥ −1}|_// weakest precondition_|
|{0 = 0 ·(0 − 1) /2 ∧ 0 ≤ 0 ≤ n + 1}|_// equivalent to n ≥ −1_|
|**i := 0;**||
|{0 = i ·(i − 1)/ 2 ∧ 0 ≤ i ≤ n + 1}||
|**s := 0;**||
|{s = i ·(i − 1) /2 ∧ 0 ≤ i ≤ n + 1}|_// I holds at the loop head_|
|**while (i <= n) do {**||
|{s = i ·(i − 1) /2 ∧ 0 ≤ i ≤ n + 1 ∧ i ≤ n}|_// I_∧_B_|
|{s + i =(i + 1)· i/2 ∧ 0 ≤ i + 1 ≤ n + 1}|_// preservation: implied by I_∧_B_|
|**s := s + i;**||
|{ s = (i + 1) · i / 2 ∧ 0 ≤ i + 1 ≤ n + 1 }||
|**i := i + 1;**||
|{s = i ·(i − 1) /2 ∧ 0 ≤ i ≤ n + 1}|_// I holds again_|
|**}**||
|{s = i ·(i − 1) /2 ∧ 0 ≤ i ≤ n + 1 ∧ ¬(i ≤ n) }|_// I_∧_¬B_|
|{s = n ·(n + 1) /2}|_// exit: i = n + 1_|



Page 33 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise o: Fibonacci numbers** 

We use the definition fib(0) = 0, fib(1) = 1 and fib(k) = fib(k − 1) + fib(k − 2) for k ≥ 2. This program is similar to exercise 3d of the previous sheet, but it does not use a temporary variable. 

**Check the tri** **<mark>p</mark> le** <u>{ x = 0 ∧ y = 1 ∧ z = 1 ∧ 1 ≤ n }</u> **while (z < n) do { y := x + y; x := y - x; z := z + 1; }** { y = fib(n) } 

#### **Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for n = 5. 

|**At the loop head**|**z**|**x**|**y**|**fib(z − 1)**|**fib(z)**|
|---|---|---|---|---|---|
|before iteration 1|1|0|1|0|1|
|before iteration 2|2|1|1|1|1|
|before iteration 3|3|1|2|1|2|
|before iteration 4|4|2|3|2|3|
|at exit (z = n)|5|3|5|3|5|



Generalising the postcondition y = fib(n) gives y = fib(z). This is not enough on its own, since the body computes the new y from x and y. The trace shows that x is always fib(z − 1). The counter starts at 1 and stops at n, which gives the bounds 1 ≤ z ≤ n. 

**Invariant** I  ≡  y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n **Guard** B  ≡  z < n **Variant** E  =  n − z 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** x = 0 ∧ y = 1 ∧ z = 1 ∧ 1 ≤ n ⇒ y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n 

The precondition contains the equations x = 0, y = 1 and z = 1. We replace x, y and z by these values in the conclusion. 

Page 34 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|I[x ← 0, y ← 1, z ← 1]|Replace x, y and z, using P.|
|= 1 = fib(1) ∧ 0 = fib(1 − 1) ∧ 1 ≤ 1 ≤ n||
|= True ∧ True ∧ True ∧ 1 ≤ n|fib(1) = 1 and fib(0) = 0 by definition.|
|= True|1 ≤ n is part of P.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n ∧ z < n ⇒  WP(y := x + y; x := y − x; z := z + 1,  y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|z := z + 1|y = fib(z) ∧ x = fib(z − 1)<br>∧ 1 ≤ z ≤ n|[z ← z + 1]|y = fib(z + 1) ∧ x = fib(z)<br>∧ 1 ≤ z + 1 ≤ n|
|2|x := y - x|y = fib(z + 1) ∧ x = fib(z)<br>∧ 1 ≤ z + 1 ≤ n|[x ← y − x]|y = fib(z + 1) ∧ y − x = fib(z)<br>∧ 1 ≤ z + 1 ≤ n|
|1|y := x + y|y = fib(z + 1) ∧ y − x =<br>fib(z)|[y ← x + y]|x + y = fib(z + 1) ∧ (x + y) − x =<br>fib(z)|
|||∧ 1 ≤ z + 1 ≤ n||∧ 1 ≤ z + 1 ≤ n<br>which simplifies to<br>x + y = fib(z + 1) ∧ y = fib(z) ∧ 1 ≤<br>z + 1 ≤ n|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n ∧ z < n ⇒ x + y = fib(z + 1) ∧ y = fib(z) ∧ 1 ≤ z + 1 ≤ n 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|x + y = fib(z − 1) + fib(z)|Replace x and y, using I.|
|= fib(z + 1)|Since z ≥ 1, we have z + 1 ≥ 2, so the recursive case of<br>the definition applies.|
|y = fib(z)|Part of I.|
|1 ≤ z + 1|From 1 ≤ z.|
|z + 1 ≤ n|From the guard z < n.|



Page 35 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

Row 1 of the table shows the trick of the program: in the substitution [y ← x + y], the expression (x + y) − x simplifies to y. The statement x := y - x therefore sets x to the old value of y. 

**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n ∧ ¬(z < n) ⇒ y = fib(n) 



|**Step of theproof**|**Reason**|
|---|---|
|¬(z < n)  =  z ≥ n|Negation of the guard.|
|z ≤ n ∧ z ≥ n  gives  z = n|Combine with z ≤ n from I.|
|y = fib(z)  becomes  y = fib(n)|Replace z by n.|



**Step 5. Termination with the variant** E = n − z 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n ∧ z < n ⇒ n − z ≥ 0 

From the guard z < n we get n − z > 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n ∧ z < n ∧ n − z = E₀ ⇒  WP(y := x + y; x := y − x; z := z + 1,  n − z < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|z := z + 1|n − z < E₀|[z ← z + 1]|n − (z + 1) < E₀|
|2|x := y - x|n − (z + 1) < E₀|[x ← y − x]|n − (z + 1) < E₀<br>x does not occur.|
|1|y := x + y|n − (z + 1) < E₀|[y ← x + y]|n − (z + 1) < E₀<br>y does not occur.|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** y = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n ∧ z < n ∧ n − z = E₀ ⇒ 

Page 36 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### n − (z + 1) < E₀ 

|**Step of theproof**|**Reason**|
|---|---|
|n − (z + 1) = E₀ − 1 < E₀|Replace n − z by E₀.|



#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{x = 0 ∧y= 1 ∧ z = 1 ∧ 1 ≤ n}|_// given precondition_|
|{ y= fib(z)∧ x = fib(z − 1)∧ 1 ≤ z ≤ n}<br>**while (z < n) do {**|_// establishment: P_⇒_I_|
|{ y= fib(z)∧ x = fib(z − 1)∧ 1 ≤ z ≤ n ∧ z < n}|_// I_∧_B_|
|{x +y= fib(z + 1)∧y= fib(z)∧ 1 ≤ z + 1 ≤ n}|_// preservation: implied by I_∧_B_|
|**y := x + y;**||
|{ y = fib(z + 1) ∧ y − x = fib(z) ∧ 1 ≤ z + 1 ≤ n }||
|**x := y - x;**||
|{y = fib(z + 1)∧ x = fib(z)∧ 1 ≤ z + 1 ≤ n}||
|**z := z + 1;**||
|{ y= fib(z)∧ x = fib(z − 1)∧ 1 ≤ z ≤ n}|_// I holds again_|
|**}**||
|{ y= fib(z)∧ x = fib(z − 1)∧ 1 ≤ z ≤ n ∧ ¬(z < n) }<br>{ y= fib(n) }|_// I_∧_¬B_<br>_// exit: z = n_|



Page 37 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **Summary of answers** 

|**Exercise**|**Task**|**Answer**|
|---|---|---|
|a|find the WP|True|
|b|check|Valid. The conjunct x ≥ 0 of the precondition is not needed.|
|c|find the WP|y = y′|
|d|check|Valid.|
|e|find the WP|r = r′|
|f|check|Valid. The conjuncts x ≥ 0∧y ≥ 0 of the precondition are not needed.|
|g|find the WP|True|
|h|find the WP|n ≤ −1 ∨ n ≥ 0(n is a real number).|
|i|check|Valid.|
|j|find the WP|True|
|k|check|Valid. The WP isTrue, so the precondition is stronger than needed.|
|l|check|Valid. Invariantz = 2 · (x′ − x) ∧ x ≥ 0, variant x.|
|m|find the WP|n ≥ 0. Invariants = i ∧ i ≤ n.|
|m (second<br>part)|check|Valid. The conjunctx′ ≥ 0of the precondition is needed for0 ≤ r. Invariantx′<br>= q · y′ + r ∧ 0 ≤ r ∧ y = y′ ∧ y′ > 0, variant r.|
|n|find the WP|n ≥ −1. Invariants = i · (i − 1) / 2 ∧ 0 ≤ i ≤ n + 1.|
|o|check|Valid. Invarianty = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n, variant n − z.|



Page 38 

