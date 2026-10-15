# Hoare Logic Exercises - 1 - solved

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

# **Hoare Logic: Deductive Verification Exercises** 

Worked solutions: implications, triples with skip, weakest preconditions, intermediate assertions and loop invariants 

**How to read these solutions** 

Sections 1 and 2 are answered in tables, with one row per item. Each row says whether the item is valid and gives the reason. When an item is not valid, the reason contains a counterexample, which is one concrete state where the formula fails. 

Sections 3 to 5 follow the same order as the previous exercise sets. First the triple is stated. Then the weakest precondition (WP) is computed step by step in a table. Then the result is stated or the check is carried out. The exercise ends with the complete proof outline. 

In the program boxes, program statements are written in black monospace, for example x := x + 1;. Assertions are written in blue between braces, for example { x ≥ 0 }. The grey text after // on the right explains why an assertion holds at that point. 

Symbols: ∧ is "and", ∨ is "or", ¬ is "not", ⇒ is "implies". Q[x ← e] means "Q with every occurrence of x replaced by the expression e". 

**Conventions used in this sheet** 

**Primed names are initial values.** A name such as x′ is a logical variable. It records the value that x had when the program started, and the program never assigns to it. The substitution rule therefore never replaces it. 

**Unassigned names are constants.** In Section 4, n and m are never assigned. They behave like constants, so the substitution rule leaves them alone. 

**Integers.** All program variables are integers, and x div 2 and x mod 2 are integer division and remainder. The one exception is exercise 3b, where the variables are real numbers. 

**Loop syntax.** Loops are written as while (B) do { … }, with braces around the body. 

Page 1 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **1. Which implications are valid?** 

**What "valid" means** 

An implication A ⇒ B is false in exactly one situation: A is true and B is false. In every other situation it is true. The table shows the four cases. 

An implication is **valid** when it is true in every state, that is for every value of its program variables and every truth value of the formulas A, B and P. 

As a consequence, there are two quick ways to see that an implication is valid. If the premise can never be true, the implication is valid. If the conclusion is always true, the implication is valid. To show that an implication is **not valid** , we give one state where the premise is true and the conclusion is false. 

|**A**|**B**|**A**⇒**B**|
|---|---|---|
|False|False|True|
|False|True|True|
|True|False|False|
|True|True|True|



Page 2 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**#**|**Implication**|**Valid?**|**Reason**|
|---|---|---|---|
|1|False ⇒ True|Valid|The premise is never true.|
|2|True ⇒ False|**Not valid**|The premise is true and the conclusion is false in every<br>state. This is the only false row of the truth table.|
|3|True ⇒ True|Valid|The conclusion is always true.|
|4|False ⇒ False|Valid|The premise is never true.|
|5|False ⇒ P|Valid|The premise is never true, so the conclusion does not<br>matter.|
|6|P ⇒ True|Valid|The conclusion is always true, so the premise does not<br>matter.|
|7|P ⇒ False|**Not valid**|The formula is equivalent to¬P. It fails for any P that can<br>be true, for example P = True. It is valid only in the special<br>case where P can never be true.|
|8|True ⇒ P|**Not valid**|The formula is equivalent to P itself. It fails for any P that<br>can be false, for example P = False. It is valid only when P is<br>valid.|
|9|x = x + 1 ⇒ True|Valid|The conclusion is always true. In addition, the premise is<br>never true, since no integer equals itself plus 1.|
|10|x = x + 1 ⇒ y = y + 1|Valid|The premise is false for every x. The conclusion is also<br>always false, but this does not matter.|
|11|5 = 5 ⇒ 6 > 3|Valid|This isTrue ⇒ True.|
|12|x > y ⇒ x < y|**Not valid**|Counterexample: x = 2, y = 1. The premise 2 > 1 is true and<br>the conclusion 2 < 1 is false. The implication is true in some<br>states (those with x ≤ y), but valid requires every state.|
|13|B ∧ A ⇒ A|Valid|Whenever B∧A is true, A is true.|
|14|A ⇒ A ∨ B|Valid|Whenever A is true, the disjunction A∨B is true.|
|15|A ∨ B ⇒ A|**Not valid**|Counterexample: A = False, B = True. The premise is true<br>and the conclusion is false.|
|16|A ∨ B ⇒ B|**Not valid**|Counterexample: A = True, B = False.|
|17|True ∧ False ⇒ True ∨ False|Valid|The premise simplifies to False and the conclusion to True.<br>Either fact alone makes the implication valid.|
|18|A ∧ B ⇒ A ∨ B|Valid|If both A and B are true, then at least one of them is true.|
|19|A ∨ B ⇒ A ∧ B|**Not valid**|Counterexample: A = True, B = False. At least one is true,<br>but not both.|



Page 3 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **2. Which triples are valid?** 

**Rule used in this section** 

**Skip rule.** {Q} skip {Q}. Since skip changes nothing, WP(skip, Q) = Q. 

**Consequence.** The triple {P} skip {Q} is valid exactly when P ⇒ Q is valid. Each triple in this section therefore reduces to an implication, and we can reuse the reasoning of Section 1. 

|**#**|**Triple**|**Reduces to**|**Valid?**|**Reason**|
|---|---|---|---|---|
|1|{False} skip {False}|False ⇒ False|Valid|The premise is never true.|
|2|{False} skip {True}|False ⇒ True|Valid|The premise is never true.|
|3|{True} skip {False}|True ⇒ False|**Not valid**|Every starting state satisfies the<br>precondition, and no final state<br>satisfies False.|
|4|{True} skip {True}|True ⇒ True|Valid|The conclusion is always true.|
|5|{x = x + 1} skip {y = y + 1}|x = x + 1 ⇒ y = y + 1|Valid|No state satisfies the precondition,<br>so there is nothing to check.|
|6|{x = x′ + 1} skip {y′ = y + 1}|x = x′ + 1 ⇒ y′ = y + 1|**Not valid**|The precondition says nothing about<br>y. Counterexample: xʹ = 0, x = 1, yʹ =<br>y = 5. The precondition holds, skip<br>keeps y = 5, and yʹ = y + 1 is false.|
|7|{True} skip {0 = 3}|True ⇒ False|**Not valid**|The postcondition 0 = 3 is False.|
|8|{2 = 2} skip {5 = 5}|True ⇒ True|Valid|Both assertions are True.|
|9|{x ≠ y} skip {False}|x ≠ y ⇒ False|**Not valid**|Counterexample: x = 1, y = 2.|
|10|{x ≠ y} skip {True}|x ≠ y ⇒ True|Valid|The postcondition is always true.|
|11|{False} skip {x > 3}|False ⇒ x > 3|Valid|The premise is never true.|
|12|{x > 0} skip {x ≥ 0}|x > 0 ⇒ x ≥ 0|Valid|Every positive x is also non-negative.|
|13|{x ≥ 0} skip {x > 0}|x ≥ 0 ⇒ x > 0|**Not valid**|Counterexample: x = 0.|



Page 4 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **3. Fill in the precondition** 

**Rules used in this section** 

**Assignment rule.** WP(x := e, Q) = Q[x ← e]. **Sequence rule.** WP(S1; S2, Q) = WP(S1, WP(S2, Q)), so we start with the last statement and work upwards. **Conditional rule.** WP(if B then S1 else S2, Q) = (B ⇒ WP(S1, Q)) ∧ (¬B ⇒ WP(S2, Q)). 

### **Exercise 3a** 

**Find the weakest precondition** <u>{ ? }</u> **y := x; y := x + x + y;** { y = 3 · x } 

**Step 1. Compute the WP from the last statement to the first** 

|**Goal: c**<br>W|**ompute**WP(S, Q)<br>P(y := x; y := x +|**, that is:**<br>x + y,  y = 3 · x)|||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|2|y := x + x<br>+ y|y = 3 · x|[y ← x + x<br>+ y]|x + x + y = 3 · x<br>which simplifies to|
|||||y = x|
|1|y := x|y = x|[y ← x]|x = x<br>which simplifies to<br>True|



#### **Step 2. Result** 

The weakest precondition is True. The first statement makes y equal to x, so the second statement computes x + x + x = 3 · x from any starting state. 

|**Proof outline**||
|---|---|
|{True}|_// weakest precondition_|
|{x = x}|_// equivalent to True_|
|**y := x;**||
|{ y = x }||
|**y := x + x + y;**||
|{ y= 3 · x}|_// postcondition_|



### **Exercise 3b** 

In this exercise the variables are real numbers. 

Page 5 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Find the weakest precondition** { ? } **z := x + 2; y := z + z; x := z + y;** { x > z ∧ y = 3 } 

**Step 1. Compute the WP from the last statement to the first** 

**Goal: compute** WP(S, Q) **, that is:** WP(z := x + 2; y := z + z; x := z + y,  x > z ∧ y = 3) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|x := z + y|x > z ∧ y = 3|[x ← z + y]|z + y > z ∧ y = 3<br>which simplifies to<br>y > 0 ∧ y = 3<br>that is<br>y = 3|
|2|y := z + z|y = 3|[y ← z + z]|z + z = 3<br>which simplifies to<br>z = 3 / 2|
|1|z := x + 2|z = 3 / 2|[z ← x + 2]|x + 2 = 3 / 2<br>which simplifies to<br>x = −1 / 2|



#### **Step 2. Result** 

The weakest precondition is x = −1/2. We can confirm it by running the program from x = −1/2: z = 3/2, then y = 3/2 + 3/2 = 3, then x = 3/2 + 3 = 9/2. Both 9/2 > 3/2 and y = 3 hold. 

|**Proof outline**||
|---|---|
|{x = −1/2}|_// weakest precondition_|
|{x + 2 = 3/2}|_// equivalent_|
|**z := x + 2;**||
|{z = 3 / 2}||
|**y := z + z;**||
|{ y= 3}|_// z + z = 3_|
|**x := z + y;**||
|{x > z ∧y= 3}|_// postcondition_|



Page 6 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 3c** 



<!-- Start of picture text -->
Find the weakest precondition<br>{ ? }<br>if (x - y > 0) then {<br>z := x;<br>} else {<br>z := y;<br>}<br>{ z ≤ y ∧ z ≤ x }<br><!-- End of picture text -->

**Step 1. Compute the WP of each branch** 

**Goal: compute** WP(S, Q) **, that is:** WP(if (x − y > 0) then z := x else z := y,  z ≤ y ∧ z ≤ x) 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|x − y > 0|z := x|[z ← x]|x ≤ y ∧ x ≤ x  =  x ≤ y|
|else|x − y ≤ 0|z := y|[z ← y]|y ≤ y ∧ y ≤ x  =  y ≤ x|



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x > y ⇒ x ≤ y) ∧ (x ≤ y ⇒ y ≤ x)|Conditional rule. The guard x − y > 0 is the same as x ><br>y.|
|= (x ≤ y ∨ x ≤ y) ∧ (x > y ∨ y ≤ x)|A⇒B is the same as ¬A∨B.|
|= x ≤ y ∧ y ≤ x|The first disjunction repeats x ≤ y. In the second, x > y<br>already implies y ≤ x.|
|= x = y||



#### **Step 3. Result** 

The weakest precondition is x = y. The program stores the larger of x and y in z. The larger value is at most both x and y only when the two values are equal. 

Page 7 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x =y }|_// weakest precondition_|
|**if (x - y > 0) then {**||
|{x =y∧ x −y> 0}|_// precondition_∧_guard = False_|
|{x ≤y }|_// False implies any formula_|
|**z := x;**||
|{z ≤ y ∧ z ≤ x}||
|**} else {**||
|{x =y∧ x −y≤ 0}|_// precondition_∧_¬guard_|
|{ y≤ x}|_// from x = y_|
|**z := y;**||
|{ z ≤ y ∧ z ≤ x }||
|**}**||
|{z ≤y∧ z ≤ x}|_// postcondition_|



### **Exercise 3d** 

|**Find the weakest precondition**|
|---|
|{?}|
|**if (x > 0) then {**|
|**x := x + 1;**|
|**} else {**|
|**x := z;**|
|**}**|
|{ even(x) }|



**Step 1. Compute the WP of each branch** 

|**Goal: co**<br>WP(|**mpute**WP(S, Q<br>if (x > 0) then|)**, that is:**<br>x := x + 1 else x|:= z,  even(x))||
|---|---|---|---|---|
|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|then|x > 0|x := x + 1|[x ← x + 1]|even(x + 1)<br>Adding 1 changes parity, so this is the same as:<br>¬even(x)|
|else|x ≤ 0|x := z|[x ← z]|even(z)|



Page 8 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x > 0 ⇒ ¬even(x)) ∧ (x ≤ 0 ⇒ even(z))|Conditional rule.|
|= (x > 0 ∧ ¬even(x)) ∨ (x ≤ 0 ∧ even(z))|Equivalent form. Exactly one of the guards x > 0 and x<br>≤ 0 is true, so the formula holds when the condition<br>attached to that guard holds.|



#### **Step 3. Result** 

The weakest precondition is (x > 0 ⇒ ¬even(x)) ∧ (x ≤ 0 ⇒ even(z)). In words: if x is positive it must be odd, and if x is zero or negative then z must be even. This WP cannot be simplified further, since it really depends on both x and z. 

|**Proof outline**||
|---|---|
|{ (x > 0 ⇒ ¬even(x))∧(x ≤ 0 ⇒ even(z)) }|_// weakest precondition_|
|**if (x > 0) then {**||
|{¬even(x) }|_// precondition_∧_guard_|
|{even(x + 1) }|_// x is odd, so x + 1 is even_|
|**x := x + 1;**||
|{ even(x) }||
|**} else {**||
|{even(z) }|_// precondition_∧_¬guard_|
|**x := z;**||
|{ even(x) }||
|**}**||
|{even(x) }|_// postcondition_|



Page 9 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **4. Prove the following Hoare triples** 

**What R1, R2 and R3 are** 

The labels R1, R2 and R3 mark the places where an intermediate assertion must be written. R1 is the assertion just before the first statement, R2 is the assertion just before the second statement, and R3 is the assertion just before the third statement. 

**Method.** We compute each Ri as a weakest precondition, starting with the last statement. Then we check that the given precondition implies R1. 

### **Exercise 4a** 

**Prove the tri** **<mark>p</mark> le** { x = x′ ∧ y = y′ } **<mark>k := x + n;</mark>** _// R1 before this statement_ **<mark>x := y - m;</mark>** _// R2 before this statement_ **<u><mark>y := k + y;</mark></u>** _// R3 before this statement_ { x = y′ − m ∧ y = x′ + n + y′ } 

**Step 1. Compute R3, R2 and R1** 

|**To pro**<br>x =<br>⇒|**ve**P ⇒ WP(S, Q)**,**<br>x′ ∧ y = y′<br>WP(k := x + n; x|**that is:**<br>:= y − m; y := k + y,  x = y′ −|m ∧ y = x′ + n|+ y′)|
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|R3|y := k + y|x = y′ − m<br>∧ y = x′ + n + y′|[y ← k + y]|x = y′ − m<br>∧ k + y = x′ + n + y′|
|R2|x := y - m|x = y′ − m<br>∧ k + y = x′ + n + y′|[x ← y − m]|y − m = y′ − m<br>∧ k + y = x′ + n + y′<br>which simplifies to<br>y = y′ ∧ k = x′ + n<br>The first conjunct gives y = yʹ. Using it in<br>the second gives k = xʹ + n.|
|R1|k := x + n|y = y′ ∧ k = x′ + n|[k ← x + n]|y = y′ ∧ x + n = x′ + n<br>which simplifies to<br>y = y′ ∧ x = x′|



#### **Step 2. Compare the precondition with R1** 

R1 is y = y′ ∧ x = x′, which is the given precondition with the conjuncts in a different order. Therefore the triple is valid. 

Page 10 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x = x′ ∧y=y′}|_// given precondition_|
|{ y=y′ ∧ x = x′}|_// R1, same as the precondition_|
|**k := x + n;**||
|{ y=y′ ∧ k = x′ + n}|_// R2_|
|**x := y - m;**||
|{x =y′ − m ∧ k +y= x′ + n +y′}|_// R3_|
|**y := k + y;**||
|{x =y′ − m ∧y= x′ + n +y′}|_// postcondition_|



### **Exercise 4b** 

|**Prove the triple**||
|---|---|
|{x = x′ ∧ y = y′}||
|**x := x +y;**|_// R1 before this statement_|
|**y := x + n;**|_// R2 before this statement_|
|**x := x -y + n - m;**|_// R3 before this statement_|
|{ x = −m ∧ y = x′ + n + y′ }||



#### **Step 1. Compute R3, R2 and R1** 

|**To pro**<br>x<br>⇒|**ve**P ⇒ WP(S, Q)**,**<br>= x′ ∧ y = y′<br>WP(x := x + y; y|**that is:**<br>:= x + n; x := x − y + n − m,|x = −m ∧ y = x′|+ n + y′)|
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|R3|x := x - y<br>+ n - m|x = −m<br>∧ y = x′ + n + y′|[x ← x − y<br>+ n − m]|x − y + n − m = −m<br>∧ y = x′ + n + y′<br>which simplifies to<br>x = y − n<br>∧ y = x′ + n + y′|
|R2|y := x + n|x = y − n<br>∧ y = x′ + n + y′|[y ← x + n]|x = (x + n) − n<br>∧ x + n = x′ + n + y′<br>which simplifies to<br>x = x′ + y′<br>The first conjunct is always true.|
|R1|x := x + y|x = x′ + y′|[x ← x + y]|x + y = x′ + y′|



#### **Step 2. Compare the precondition with R1** 

From x = x′ and y = y′ we get x + y = x′ + y′. Therefore the precondition implies R1, and the triple is valid. 

Page 11 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x = x′ ∧y=y′}|_// given precondition_|
|{x +y= x′ +y′}|_// R1, since x = xʹ and y = yʹ_|
|**x := x + y;**||
|{x = x′ +y′}|_// R2_|
|**y := x + n;**||
|{x =y− n ∧y= x′ + n +y′}|_// R3_|
|**x := x - y + n - m;**||
|{x = −m ∧y= x′ + n +y′}|_// postcondition_|



### **Exercise 4c** 

|**Prove the triple**||
|---|---|
|{y ≥ z ∧ z ≥ y}||
|**z := z +y;**|_// R1 before this statement_|
|**x := 3 * z +y;**|_// R2 before this statement_|
|{ x = 7 · y }||



#### **Step 1. Compute R2 and R1** 

This exercise has two statements, so there are only two intermediate assertions. 

|**To pro**<br>y<br>⇒|**ve**P ⇒ WP(S, Q)**,**<br>≥ z ∧ z ≥ y<br>WP(z := z + y; x|**that is:**<br>:= 3 · z + y,  x = 7 · y)|||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|R2|x := 3 * z<br>+ y|x = 7 · y|[x ← 3 · z +<br>y]|3 · z + y = 7 · y<br>which simplifies to<br>z = 2 · y|
|R1|z := z + y|z = 2 · y|[z ← z + y]|z + y = 2 · y<br>which simplifies to<br>z = y|



**Step 2. Compare the precondition with R1** 

**To prove** P ⇒ R1 **, written out in full** y ≥ z ∧ z ≥ y ⇒ z = y 



|**Formula**|**Reason**|
|---|---|
|y ≥ z ∧ z ≥ y  ⇒  z = y|If each number is at least the other, the two numbers|
||are equal.|



Page 12 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

Therefore the triple is valid. The precondition is written in an indirect way on purpose: the proof has to notice that the two inequalities together give the equation z = y. 

|**Proof outline**||
|---|---|
|{ y≥ z ∧ z ≥y }|_// given precondition_|
|{z =y }|_// R1, from the two inequalities_|
|**z := z + y;**||
|{z = 2 ·y }|_// R2_|
|**x := 3 * z + y;**||
|{x = 7 ·y }|_// postcondition_|



Page 13 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **5. Proof outlines and loop invariants** 

**Rules used in this section** 

**While rule (combined with the consequence rule).** To prove {P} while B do S {Q} we need an invariant I and three obligations: 

(1) **Establishment:** P ⇒ I. The invariant holds before the first iteration. When the loop is preceded by initialisation statements, the obligation is P ⇒ WP(init, I). 

(2) **Preservation:** {I ∧ B} S {I}. We compute WP(S, I) and prove the implication I ∧ B ⇒ WP(S, I). 

(3) **Exit:** I ∧ ¬B ⇒ Q. When the loop stops, the guard is false and the invariant still holds, and together they must give the postcondition. 

(4) **Termination.** A variant E is an integer expression with two properties: (4a) I ∧ B ⇒ E ≥ 0, and (4b) I ∧ B ∧ E = E₀ ⇒ WP(S, E < E₀), where E₀ is the value of E before the iteration. The lecture slides call this value n; we write E₀ because n is often a program variable in these exercises. 

**How each obligation is presented.** First we write the implication out in full, with the actual formulas, in a green box. Then we prove it line by line. 

**Two kinds of replacement appear in the proofs.** The first is the assignment rule, WP(x := e, Q) = Q[x ← e], which we use to compute a WP; the tables show it in the column Substitution. The second is replacement of equals by equals: when the assumptions contain an equation such as i = 0, we may replace i by 0 in the formula we are proving. The two look similar, but only the first one comes from a program statement. 

**Where the invariant comes from.** We start from the postcondition, trace the variables at the loop head, generalise the postcondition by replacing the final value with the loop counter, and add bounds for the counter. 

### **Exercise 5a** 

**Give a** **<mark>p</mark> roof outline and a loo** **<mark>p</mark> invariant** { x = x′ ∧ y = y′ ∧ y ≥ 0 } **while (y > 0) do { x := x + 1; y := y - 1; }** { x = x′ + y′ } 

#### **Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for xʹ = 2 and yʹ = 3. 

Page 14 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**At the loop head**|**x**|**y**|**x +y**|
|---|---|---|---|
|before iteration 1|2|3|5|
|before iteration 2|3|2|5|
|before iteration 3|4|1|5|
|at exit (y = 0)|5|0|5|



Each iteration moves one unit from y to x, so the sum x + y never changes and stays equal to x′ + y′. The counter y never goes below 0. At the exit y = 0, and the sum becomes the postcondition. 

**Invariant** I  ≡  x + y = x′ + y′ ∧ y ≥ 0 **Guard** B  ≡  y > 0 **Variant** E  =  y 

#### **Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** x = x′ ∧ y = y′ ∧ y ≥ 0 ⇒ x + y = x′ + y′ ∧ y ≥ 0 

The precondition contains the equations x = xʹ and y = yʹ. We replace x by xʹ and y by yʹ in the first conjunct of the conclusion. 

|**Step of theproof**|**Reason**|
|---|---|
|(x + y = x′ + y′)[x ← x′, y ← y′]<br>= x′ + y′ = x′ + y′|Replace x and y, using x = xʹ and y = yʹ from P.|
|= True|Both sides are the same expression.|
|y ≥ 0|Part of P.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** x + y = x′ + y′ ∧ y ≥ 0 ∧ y > 0 ⇒  WP(x := x + 1; y := y − 1,  x + y = x′ + y′ ∧ y ≥ 0) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|y := y - 1|x + y = x′ + y′ ∧ y ≥ 0|[y ← y − 1]|x + (y − 1) = x′ + y′ ∧ y − 1 ≥ 0|
|1|x := x + 1|x + (y − 1) = x′ + y′ ∧ y −|[x ← x + 1]|(x + 1) + (y − 1) = x′ + y′ ∧ y − 1 ≥|
|||1 ≥ 0||0<br>which simplifies to<br>x + y = x′ + y′ ∧ y ≥ 1|



Page 15 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** x + y = x′ + y′ ∧ y ≥ 0 ∧ y > 0 ⇒ x + y = x′ + y′ ∧ y ≥ 1 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|x + y = x′ + y′|Part of I.|
|y ≥ 1|From the guard y > 0, since y is an integer.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** x + y = x′ + y′ ∧ y ≥ 0 ∧ ¬(y > 0) ⇒ x = x′ + y′ 



|**Step of theproof**|**Reason**|
|---|---|
|¬(y > 0)  =  y ≤ 0|Negation of the guard.|
|y ≥ 0 ∧ y ≤ 0  gives  y = 0|Combine with y ≥ 0 from I.|
|x + 0 = x′ + y′, that is x = x′ + y′|Replace y by 0 in x + y = xʹ + yʹ.|



**Step 5. Termination with the variant** E = y 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** x + y = x′ + y′ ∧ y ≥ 0 ∧ y > 0 ⇒ y ≥ 0 

Part of I. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

Page 16 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** x + y = x′ + y′ ∧ y ≥ 0 ∧ y > 0 ∧ y = E₀ ⇒  WP(x := x + 1; y := y − 1,  y < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|y := y - 1|y < E₀|[y ← y − 1]|y − 1 < E₀|
|1|x := x + 1|y − 1 < E₀|[x ← x + 1]|y − 1 < E₀<br>x does not occur.|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** 

x + y = x′ + y′ ∧ y ≥ 0 ∧ y > 0 ∧ y = E₀ ⇒ y − 1 < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|y − 1 = E₀ − 1 < E₀|Replace y by E₀.|



**Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{x = x′ ∧y=y′ ∧y≥ 0}|_// given precondition_|
|{x +y= x′ +y′ ∧y≥ 0}|_// establishment: P_⇒_I_|
|**while (y > 0) do {**||
|{x +y= x′ +y′ ∧y≥ 0 ∧y> 0}|_// I_∧_B_|
|{ (x + 1)+(y− 1)= x′ +y′ ∧y− 1 ≥ 0}|_// preservation: implied by I_∧_B_|
|**x := x + 1;**||
|{ x + (y − 1) = x′ + y′ ∧ y − 1 ≥ 0 }||
|**y := y - 1;**||
|{x +y= x′ +y′ ∧y≥ 0}|_// I holds again_|
|**}**||
|{x +y= x′ +y′ ∧y≥ 0 ∧ ¬(y> 0) }|_// I_∧_¬B_|
|{x = x′ +y′}|_// exit: y = 0_|



Page 17 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 5b** 

|**Give a proof outlin**|**e and a loop invariant**|
|---|---|
|{ x = x′ ∧ y = y′|∧ y ≥ 0 }|
|**z := 0;**||
|**a := 1;**||
|**while (a <=**|**y) do {**|
|**z := z +**|**x;**|
|**a := a +**|**1;**|
|**}**||
|{z = x · y}||



#### **Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for x = 4 and y = 3. 

|**At the loop head**|**a**|**z**|**x ·(a − 1)**|
|---|---|---|---|
|before iteration 1|1|0|0|
|before iteration 2|2|4|4|
|before iteration 3|3|8|8|
|at exit (a = y + 1)|4|12|12|



The counter a starts at 1, so after k iterations a = k + 1 and z holds k copies of x. Therefore z = x · (a − 1). The loop stops when a = y + 1, and then the formula becomes z = x · y. The counter starts at 1 and stops at y + 1, which gives the bounds 1 ≤ a ≤ y + 1. 

**Invariant** I  ≡  z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1 **Guard** B  ≡  a ≤ y **Variant** E  =  y + 1 − a 

#### **Step 2. Establishment:** P ⇒ WP(init, I) 

The loop is preceded by initialisation statements. We first compute the WP of these statements with respect to I, from the last one to the first. 

**To prove** P ⇒ WP(init, I) **, that is:** x = x′ ∧ y = y′ ∧ y ≥ 0 ⇒  WP(z := 0; a := 1,  z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|a := 1|z = x · (a − 1) ∧ 1 ≤ a ≤ y<br>+ 1|[a ← 1]|z = x · (1 − 1) ∧ 1 ≤ 1 ≤ y + 1<br>which simplifies to<br>z = 0 ∧ y ≥ 0|
|1|z := 0|z = 0 ∧ y ≥ 0|[z ← 0]|0 = 0 ∧ y ≥ 0<br>which simplifies to<br>y ≥ 0|



Page 18 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**To prove** P ⇒ WP(init, I) **, written out in full** 

x = x′ ∧ y = y′ ∧ y ≥ 0 ⇒ 0 = 0 ∧ y ≥ 0 



|**Step of theproof**|**Reason**|
|---|---|
|0 = 0|Always true.|
|y ≥ 0|Part of P.|



**Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1 ∧ a ≤ y ⇒  WP(z := z + x; a := a + 1,  z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|a := a + 1|z = x · (a − 1) ∧ 1 ≤ a ≤ y|[a ← a + 1]|z = x · ((a + 1) − 1) ∧ 1 ≤ a + 1 ≤ y|
|||+ 1||+ 1|
|||||which simplifies to|
|||||z = x · a ∧ 1 ≤ a + 1 ≤ y + 1|
|1|z := z + x|z = x · a ∧ 1 ≤ a + 1 ≤ y + 1|[z ← z + x]|z + x = x · a ∧ 1 ≤ a + 1 ≤ y + 1|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1 ∧ a ≤ y ⇒ z + x = x · a ∧ 1 ≤ a + 1 ≤ y + 1 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|z + x = x · (a − 1) + x|Replace z, using I.|
|= x · a|Factor out x.|
|1 ≤ a + 1|From 1 ≤ a.|
|a + 1 ≤ y + 1|From the guard a ≤ y.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** 

Page 19 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1 ∧ ¬(a ≤ y) ⇒ z = x · y 



|**Step of theproof**|**Reason**|
|---|---|
|¬(a ≤ y)  =  a > y  =  a ≥ y + 1|Negation of the guard, for integers.|
|a ≤ y + 1 ∧ a ≥ y + 1  gives  a = y + 1|Combine with a ≤ y + 1 from I.|
|z = x · ((y + 1) − 1) = x · y|Replace a by y + 1 in the invariant.|



**Step 5. Termination with the variant** E = y + 1 − a 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1 ∧ a ≤ y ⇒ y + 1 − a ≥ 0 

From the guard a ≤ y we get y + 1 − a ≥ 1. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1 ∧ a ≤ y ∧ y + 1 − a = E₀ ⇒  WP(z := z + x; a := a + 1,  y + 1 − a < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|a := a + 1|y + 1 − a < E₀|[a ← a + 1]|y + 1 − (a + 1) < E₀|
|1|z := z + x|y + 1 − (a + 1) < E₀|[z ← z + x]|y + 1 − (a + 1) < E₀<br>z does not occur.|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** z = x · (a − 1) ∧ 1 ≤ a ≤ y + 1 ∧ a ≤ y ∧ y + 1 − a = E₀ ⇒ y + 1 − (a + 1) < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|y + 1 − (a + 1) = E₀ − 1 < E₀|Replace y + 1 − a by E₀.|



Page 20 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{x = x′ ∧y=y′ ∧y≥ 0}|_// given precondition_|
|{0 = 0 ∧y≥ 0}|_// implied by y ≥ 0_|
|**z := 0;**||
|{z = 0 ∧ y ≥ 0}||
|**a := 1;**||
|{z = x ·(a − 1)∧ 1 ≤ a ≤y+ 1}|_// I holds at the loop head_|
|**while (a <= y) do {**||
|{z = x ·(a − 1)∧ 1 ≤ a ≤y+ 1 ∧ a ≤y }|_// I_∧_B_|
|{z + x = x · a ∧ 1 ≤ a + 1 ≤y+ 1}|_// preservation: implied by I_∧_B_|
|**z := z + x;**||
|{ z = x · a ∧ 1 ≤ a + 1 ≤ y + 1 }||
|**a := a + 1;**||
|{z = x ·(a − 1)∧ 1 ≤ a ≤y+ 1}|_// I holds again_|
|**}**||
|{z = x ·(a − 1)∧ 1 ≤ a ≤y+ 1 ∧ ¬(a ≤y) }|_// I_∧_¬B_|
|{z = x ·y }|_// exit: a = y + 1_|



Page 21 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 5c: multiplication by halving and doubling** 

The sheet gives the hint x = x div 2 + x div 2 + x mod 2 and the invariant x′ · y′ = x · y + z ∧ x ≥ 0. The program multiplies xʹ by yʹ by halving x and doubling y. When x is odd, the copy of y that halving would lose is added to z. 

**Give a proof outline** { x = x′ ∧ y = y′ ∧ x′ ≥ 0 ∧ y′ > 0 } **z := 0; while (!(x = 0)) do { if (x mod 2 = 1) then { z := z + y; } else { skip; } y := y * 2; x := x div 2; }** <u>{ z = x′ · y′ }</u> 

**Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for xʹ = 6 and yʹ = 5. 

|**At the loop head**|**x**|**y**|**z**|**x ·y + z**|
|---|---|---|---|---|
|before iteration 1|6|5|0|30|
|before iteration 2|3|10|0|30|
|before iteration 3|1|20|10|30|
|at exit (x = 0)|0|40|30|30|



The value x · y + z stays at 30 = 6 · 5. At the exit x = 0, so z alone holds the product. The conjunct x ≥ 0 is needed for three reasons. It guarantees that x mod 2 is 0 or 1, so the two branches of the conditional cover all cases. It gives x div 2 ≥ 0, which keeps x ≥ 0 true after the body. Together with the guard x ≠ 0 it gives x > 0, so the variant x strictly decreases. 

**Invariant** I  ≡  x′ · y′ = x · y + z ∧ x ≥ 0 **Guard** B  ≡  ¬(x = 0), that is x ≠ 0 **Variant** E  =  x 

#### **Step 2. Establishment:** P ⇒ WP(init, I) 

The loop is preceded by initialisation statements. We first compute the WP of these statements with respect to I, from the last one to the first. 

Page 22 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**To prove** P ⇒ WP(init, I) **, that is:** x = x′ ∧ y = y′ ∧ x′ ≥ 0 ∧ y′ > 0 ⇒  WP(z := 0,  x′ · y′ = x · y + z ∧ x ≥ 0) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|1|z := 0|x′ · y′ = x · y + z ∧ x ≥ 0|[z ← 0]|x′ · y′ = x · y + 0 ∧ x ≥ 0|
|||||which simplifies to<br>x′ · y′ = x · y ∧ x ≥ 0|



**To prove** P ⇒ WP(init, I) **, written out in full** 

x = x′ ∧ y = y′ ∧ x′ ≥ 0 ∧ y′ > 0 ⇒ x′ · y′ = x · y ∧ x ≥ 0 

The precondition contains the equations x = xʹ and y = yʹ. We replace x by xʹ and y by yʹ in the conclusion. 

|**Step of theproof**|**Reason**|
|---|---|
|(x′ · y′ = x · y ∧ x ≥ 0)[x ← x′, y ← y′]<br>= x′ · y′ = x′ · y′ ∧ x′ ≥ 0|Replace x and y, using P.|
|= True ∧ x′ ≥ 0|Both sides of the equation are the same.|
|= True|xʹ ≥ 0 is part of P. The conjunct yʹ > 0 of P is not used in<br>the proof.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

The body is a conditional followed by two assignments. We first go back through the two assignments, and then through the conditional. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** x′ · y′ = x · y + z ∧ x ≥ 0 ∧ x ≠ 0 ⇒  WP(if (x mod 2 = 1) then z := z + y else skip; y := y · 2; x := x div 2,  x′ · y′ = x · y + z ∧ x ≥ 0) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|x := x div<br>2|x′ · y′ = x · y + z ∧ x ≥ 0|[x ← x div<br>2]|x′ · y′ = (x div 2) · y + z ∧ x div 2 ≥ 0|
|2|y := y * 2|x′ · y′ = (x div 2) · y + z<br>∧ x div 2 ≥ 0|[y ← y · 2]|x′ · y′ = (x div 2) · (y · 2) + z ∧ x div<br>2 ≥ 0<br>which we write as<br>x′ · y′ = 2 · (x div 2) · y + z ∧ x div 2<br>≥ 0|



We call the result of row 2 R. Now we compute the WP of the conditional with respect to R, with the conditional rule. 

Page 23 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|x mod 2 = 1|z := z + y|[z ← z + y]|x′ · y′ = 2 · (x div 2) · y + y + z ∧ x div 2 ≥ 0|
|else|x mod 2 ≠ 1|skip|—|x′ · y′ = 2 · (x div 2) · y + z ∧ x div 2 ≥ 0|
|||||The skip rule gives WP(skip, R) = R.|



Combining the two branches gives WP(body, I) = (x mod 2 = 1 ⇒ x′ · y′ = 2 · (x div 2) · y + y + z ∧ x div 2 ≥ 0) ∧ (x mod 2 ≠ 1 ⇒ x′ · y′ = 2 · (x div 2) · y + z ∧ x div 2 ≥ 0). 

**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** x′ · y′ = x · y + z ∧ x ≥ 0 ∧ x ≠ 0 ⇒ (x mod 2 = 1 ⇒ x′ · y′ = 2 · (x div 2) · y + y + z ∧ x div 2 ≥ 0) ∧ (x mod 2 ≠ 1 ⇒ x′ · y′ = 2 · (x div 2) · y + z ∧ x div 2 ≥ 0) 

We assume the facts above the arrow. The hint can be written as 2 · (x div 2) = x − x mod 2. Since x ≥ 0, the remainder x mod 2 is 0 or 1, so we check the two cases. 

|**Step of theproof**|**Reason**|
|---|---|
|Casex mod 2 = 1:|The hint gives 2 · (x div 2) = x − 1.|
|2 · (x div 2) · y + y + z = (x − 1) · y + y + z||
|= x · y + z = x′ · y′|Simplify, then use I.|
|Casex mod 2 = 0:|The hint gives 2 · (x div 2) = x. Then use I.|
|2 · (x div 2) · y + z = x · y + z = x′ · y′||
|x div 2 ≥ 0|Since x ≥ 0. This holds in both cases.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** x′ · y′ = x · y + z ∧ x ≥ 0 ∧ ¬(x ≠ 0) ⇒ z = x′ · y′ 



|**Step of theproof**|**Reason**|
|---|---|
|¬(x ≠ 0)  =  x = 0|Negation of the guard.|
|x′ · y′ = 0 · y + z = z|Replace x by 0 in the invariant.|



#### **Step 5. Termination with the variant** E = x 

#### **(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** 

Page 24 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

x′ · y′ = x · y + z ∧ x ≥ 0 ∧ x ≠ 0 ⇒ x ≥ 0 

Part of I. This is one of the places where the conjunct x ≥ 0 of the invariant is needed. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** x′ · y′ = x · y + z ∧ x ≥ 0 ∧ x ≠ 0 ∧ x = E₀ ⇒  WP(if (x mod 2 = 1) then z := z + y else skip; y := y · 2; x := x div 2,  x < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|x := x div|x < E₀|[x ← x div|x div 2 < E₀|
||2||2]||
|2|y := y * 2|x div 2 < E₀|[y ← y · 2]|x div 2 < E₀<br>y does not occur.|



The conditional only assigns to z, which does not occur in x div 2 < E₀. The WP of both branches, and therefore of the conditional, is x div 2 < E₀. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** x′ · y′ = x · y + z ∧ x ≥ 0 ∧ x ≠ 0 ∧ x = E₀ ⇒ x div 2 < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|x > 0|From x ≥ 0 and x ≠ 0.|
|x div 2 ≤ x / 2 < x = E₀|Halving a positive number makes it strictly smaller.<br>Then replace x by E₀.|



Page 25 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{x = x′ ∧y=y′ ∧ x′ ≥ 0 ∧y′ > 0}|_// given precondition_|
|{x′ ·y′ = x ·y+ 0 ∧ x ≥ 0}|_// since x = xʹ, y = yʹ, xʹ ≥ 0_|
|**z := 0;**||
|{x′ ·y′ = x ·y+ z ∧ x ≥ 0}|_// I holds at the loop head_|
|**while (!(x = 0)) do {**||
|{x′ ·y′ = x ·y+ z ∧ x ≥ 0 ∧ x ≠ 0}|_// I_∧_B_|
|**if (x mod 2 = 1) then {**||
|{x′ ·y′ = x ·y+ z ∧ x ≥ 0 ∧ x ≠ 0 ∧ x mod 2 = 1}|_// precondition_∧_guard_|
|{x′ ·y′ = 2 ·(x div 2)·y+y+ z ∧ x div 2 ≥ 0}|_// by the hint, 2 · (x div 2) = x − 1_|
|**z := z + y;**||
|{x′ ·y′ = 2 ·(x div 2)·y+ z ∧ x div 2 ≥ 0}|_// R_|
|**} else {**||
|{x′ ·y′ = x ·y+ z ∧ x ≥ 0 ∧ x ≠ 0 ∧ x mod 2 ≠ 1}|_// precondition_∧_¬guard_|
|{x′ ·y′ = 2 ·(x div 2)·y+ z ∧ x div 2 ≥ 0}<br>**skip;**|_// by the hint, 2 · (x div 2) = x_|
|{x′ ·y′ = 2 ·(x div 2)·y+ z ∧ x div 2 ≥ 0}<br>**}**|_// R_|
|{x′ ·y′ = 2 ·(x div 2)·y+ z ∧ x div 2 ≥ 0}|_// R after the conditional_|
|**y := y * 2;**||
|{ x′ · y′ = (x div 2) · y + z ∧ x div 2 ≥ 0 }||
|**x := x div 2;**||
|{x′ ·y′ = x ·y+ z ∧ x ≥ 0}|_// I holds again_|
|**}**||
|{x′ ·y′ = x ·y+ z ∧ x ≥ 0 ∧ ¬(x ≠ 0) }|_// I_∧_¬B_|
|{z = x′ ·y′}|_// exit: x = 0_|



Page 26 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Exercise 5d** 

**Give a proof outline and a loop invariant** { x = n } **while (x > 0) do { x := x - 2; }** { x ≤ 0 } 

#### **Step 1. Find the invariant and the variant** 

The postcondition x ≤ 0 is exactly the negated guard ¬(x > 0). As a consequence, the exit step needs nothing from the invariant, and the simplest invariant works: True. A more informative invariant such as x ≤ n is also correct, but it is not needed here. 

**Invariant** I  ≡  True **Guard** B  ≡  x > 0 **Variant** E  =  x 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** x = n ⇒ True 



|**Step of theproof**|**Reason**|
|---|---|
|x = n ⇒ True|Any formula implies True.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

|**To pro**<br>Tr<br>⇒|**ve**I ∧ B ⇒ WP(body, I)**, that is:**<br>ue ∧ x > 0<br>WP(x := x − 2,  True)|||
|---|---|---|---|
|**Step**|**Statement**<br>**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|1|x := x - 2<br>True|[x ← x − 2]|True<br>x does not occur in True, so the<br>substitution changes nothing.|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** True ∧ x > 0 

Page 27 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

⇒ True 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|True ∧ x > 0 ⇒ True|Any formula implies True.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** True ∧ ¬(x > 0) ⇒ x ≤ 0 



|**Step of theproof**|**Reason**|
|---|---|
|True ∧ ¬(x > 0)  =  ¬(x > 0)|True is the neutral element of∧.|
|¬(x > 0)  =  x ≤ 0|Negation of the guard. This is the postcondition.|



**Step 5. Termination with the variant** E = x 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** True ∧ x > 0 ⇒ x ≥ 0 

From the guard x > 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

|**To pro**|**ve**I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀)**, that is:**|||
|---|---|---|---|
|Tr|ue ∧ x > 0 ∧ x = E₀|||
|⇒|WP(x := x − 2,  x < E₀)|||
|**Step**|**Statement**<br>**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|1|x := x - 2<br>x < E₀|[x ← x − 2]|x − 2 < E₀|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** True ∧ x > 0 ∧ x = E₀ 

Page 28 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

⇒ x − 2 < E₀ 



**Ste** **<mark>p</mark> of the** **<mark>p</mark> roof Reason** x − 2 = E₀ − 2 < E₀ Replace x by E₀. The variant decreases by 2. 

The invariant True is enough for partial correctness, and the variant gives termination. The value n in the precondition is not used. 

#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{x = n}|_// given precondition_|
|{True}|_// establishment_|
|**while (x > 0) do {**||
|{True ∧ x > 0}|_// I_∧_B_|
|{True}|_// WP of x := x - 2 with respect to True_|
|**x := x - 2;**||
|{True}|_// I holds again_|
|**}**||
|{True ∧ ¬(x > 0) }|_// I_∧_¬B_|
|{x ≤ 0}|_// exit_|



Page 29 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 5e** 

**Give a proof outline and a loop invariant** { x = 0 ∧ y = 0 ∧ 0 ≤ n } **while (y < n) do { y := y + 1; x := x + y; }** { x = 0 + 1 + … + n } 

**Step 1. Find the invariant and the variant** 

As the hint in the sheet asks, we write x as an unevaluated sum. Each new value of x is the previous expression plus the new y. 

|**Iteration**|**x**|**y**|
|---|---|---|
|0 (before the loop)|0|0|
|1|0 + 1|1|
|2|0 + 1 + 2|2|
|3|0 + 1 + 2 + 3|3|
|4|0 + 1 + 2 + 3 + 4|4|



In every row, the last number of the sum is the current value of y. Therefore x = 0 + 1 + … + y at every loop head. The part about y is the usual counter bound 0 ≤ y ≤ n. At the exit y = n, and the sum becomes the postcondition. 

**Invariant** I  ≡  x = 0 + 1 + … + y ∧ 0 ≤ y ≤ n **Guard** B  ≡  y < n **Variant** E  =  n − y 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** x = 0 ∧ y = 0 ∧ 0 ≤ n ⇒ x = 0 + 1 + … + y ∧ 0 ≤ y ≤ n 

The precondition contains the equations x = 0 and y = 0. We replace x and y by 0 in the conclusion. 

Page 30 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|I[x ← 0, y ← 0]|Replace x and y, using P.|
|= 0 = 0 + 1 + … + 0 ∧ 0 ≤ 0 ≤ n||
|= 0 = 0 ∧ True ∧ 0 ≤ n|The sum up to 0 has the single term 0.|
|= True|0 ≤ n is part of P. Without it the bound y ≤ n would fail<br>at the start.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

|**To pro**<br>x =<br>⇒|**ve**I ∧ B ⇒ WP(bo<br>0 + 1 + … + y ∧<br>WP(y := y + 1; x|dy, I)**, that is:**<br>0 ≤ y ≤ n ∧ y < n<br>:= x + y,  x = 0 + 1 + … + y ∧|0 ≤ y ≤ n)||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|2|x := x + y|x = 0 + 1 + … + y ∧ 0 ≤ y<br>≤ n|[x ← x + y]|x + y = 0 + 1 + … + y ∧ 0 ≤ y ≤ n|
|1|y := y + 1|x + y = 0 + 1 + … + y ∧ 0<br>≤ y ≤ n|[y ← y + 1]|x + (y + 1) = 0 + 1 + … + (y + 1)<br>∧ 0 ≤ y + 1 ≤ n|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** x = 0 + 1 + … + y ∧ 0 ≤ y ≤ n ∧ y < n ⇒ x + (y + 1) = 0 + 1 + … + (y + 1) ∧ 0 ≤ y + 1 ≤ n 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|x + (y + 1) = (0 + 1 + … + y) + (y + 1)|Replace x, using I.|
|= 0 + 1 + … + (y + 1)|This is the sum with one more term.|
|0 ≤ y + 1|From 0 ≤ y.|
|y + 1 ≤ n|From the guard y < n.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** x = 0 + 1 + … + y ∧ 0 ≤ y ≤ n ∧ ¬(y < n) ⇒ x = 0 + 1 + … + n 

Page 31 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|¬(y < n)  =  y ≥ n|Negation of the guard.|
|y ≤ n ∧ y ≥ n  gives  y = n|Combine with y ≤ n from I.|
|x = 0 + 1 + … + n|Replace y by n in the invariant.|



**Step 5. Termination with the variant** E = n − y 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** x = 0 + 1 + … + y ∧ 0 ≤ y ≤ n ∧ y < n ⇒ n − y ≥ 0 

From the guard y < n we get n − y > 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** x = 0 + 1 + … + y ∧ 0 ≤ y ≤ n ∧ y < n ∧ n − y = E₀ ⇒  WP(y := y + 1; x := x + y,  n − y < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|x := x + y|n − y < E₀|[x ← x + y]|n − y < E₀|
|||||x does not occur.|
|1|y := y + 1|n − y < E₀|[y ← y + 1]|n − (y + 1) < E₀|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** x = 0 + 1 + … + y ∧ 0 ≤ y ≤ n ∧ y < n ∧ n − y = E₀ ⇒ n − (y + 1) < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|n − (y + 1) = E₀ − 1 < E₀|Replace n − y by E₀.|



Page 32 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{x = 0 ∧y= 0 ∧ 0 ≤ n}|_// given precondition_|
|{x = 0 + 1 + … +y∧ 0 ≤y≤ n}|_// establishment: P_⇒_I_|
|**while (y < n) do {**||
|{x = 0 + 1 + … +y∧ 0 ≤y≤ n ∧y< n}|_// I_∧_B_|
|{x +(y+ 1)= 0 + 1 + … +(y+ 1)∧ 0 ≤y+ 1 ≤ n}|_// preservation: implied by I_∧_B_|
|**y := y + 1;**||
|{ x + y = 0 + 1 + … + y ∧ 0 ≤ y ≤ n }||
|**x := x + y;**||
|{x = 0 + 1 + … +y∧ 0 ≤y≤ n}|_// I holds again_|
|**}**||
|{x = 0 + 1 + … +y∧ 0 ≤y≤ n ∧ ¬(y< n) }|_// I_∧_¬B_|
|{x = 0 + 1 + … + n}|_// exit: y = n_|



Page 33 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 5f: Fibonacci numbers** 

The sheet defines fib(0) = 0, fib(1) = 1 and fib(n) = fib(n − 1) + fib(n − 2) for n > 1. 

**Check the tri** **<mark>p</mark> le** { x = 0 ∧ y = 1 ∧ z = 1 ∧ 1 ≤ n } **while (z < n) do { y := x + y; x := y - x; z := z + 1; }** { y = fib(n) } 

The check {I ∧ z < n} body {I} suggested in the sheet is the preservation step below. The negated guard is used only in the exit step I ∧ ¬(z < n) ⇒ y = fib(n). 

**Step 1. Find the invariant and the variant** 

We complete the table from the sheet, and write each value as a Fibonacci number. 

|**Iteration**|**x**|**y**|**z**|
|---|---|---|---|
|0|0 = fib(0)|1 = fib(1)|1|
|1|1 = fib(1)|1 = fib(2)|2|
|2|1 = fib(2)|2 = fib(3)|3|
|3|2 = fib(3)|3 = fib(4)|4|
|4|3 = fib(4)|5 = fib(5)|5|



In every row, y is the Fibonacci number with index z, and x is the one just before it. Therefore y = fib(z) and x = fib(z − 1). The counter starts at 1 and stops at n, which gives the bounds 1 ≤ z ≤ n. 

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

|**Exercise**|**Answer**|
|---|---|
|1|Valid: 1, 3, 4, 5, 6, 9, 10, 11, 13, 14, 17, 18. Not valid: 2, 7, 8, 12, 15, 16, 19.|
|2|Valid: 1, 2, 4, 5, 8, 10, 11, 12. Not valid: 3, 6, 7, 9, 13.|
|3a|WPTrue.|
|3b|WPx = −1/2.|
|3c|WPx = y.|
|3d|WP(x > 0 ⇒ ¬even(x)) ∧ (x ≤ 0 ⇒ even(z)).|
|4a|Valid. R1y = y′ ∧ x = x′, R2y = y′ ∧ k = x′ + n, R3x = y′ − m ∧ k + y = x′ + n + y′.|
|4b|Valid. R1x + y = x′ + y′, R2x = x′ + y′, R3x = y − n ∧ y = x′ + n + y′.|
|4c|Valid. R1z = y, R2z = 2 · y.|
|5a|Invariantx + y = x′ + y′ ∧ y ≥ 0, varianty.|
|5b|Invariantz = x · (a − 1) ∧ 1 ≤ a ≤ y + 1, varianty + 1 − a.|
|5c|Invariantx′ · y′ = x · y + z ∧ x ≥ 0, variantx.|
|5d|InvariantTrue, variantx.|
|5e|Invariantx = 0 + 1 + … + y ∧ 0 ≤ y ≤ n, variantn − y.|
|5f|Invarianty = fib(z) ∧ x = fib(z − 1) ∧ 1 ≤ z ≤ n, variantn − z.|



Page 38 

