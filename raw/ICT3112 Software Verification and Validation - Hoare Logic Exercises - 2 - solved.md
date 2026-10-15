# Hoare Logic Exercises - 2 - solved

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

# **Hoare Logic: Exercise Set 2** 

Worked solutions for sequential composition, conditional statements and loops 

**How to read these solutions** 

Every exercise follows the same order. First the triple to prove is stated. Then the weakest precondition (WP) is computed step by step in a table. Then the given precondition is compared with the computed WP. The exercise ends with the complete proof outline. 

In the program boxes, program statements are written in black monospace, for example x := x + 1;. Assertions are written in blue between braces, for example { x ≥ 0 }. The grey text after // on the right explains why an assertion holds at that point. 

Symbols: ∧ is "and", ∨ is "or", ¬ is "not", ⇒ is "implies". Q[x ← e] means "Q with every occurrence of x replaced by the expression e". 

## **1. Sequential composition** 

**Rules used in this section** 

**Assignment rule.** WP(x := e, Q) = Q[x ← e]. We take the postcondition Q and replace every occurrence of x by the expression e. 

**Sequence rule.** WP(S1; S2, Q) = WP(S1, WP(S2, Q)). As a consequence, we start with the last statement and work upwards. The WP of one statement becomes the postcondition of the statement above it. 

**Final check.** The triple {P} S {Q} is valid when P ⇒ WP(S, Q). When P is stronger than the WP, the consequence rule closes the gap. 

**How to read the WP tables.** Each row handles one statement, starting from the last one. The simplified WP of a row is the postcondition of the next row. 

### **Exercise 1a** 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** <u>{ a > 2 }</u> **a := a * 2; b := a + 1;** { b > 5 } 

Page 1 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 1. Compute the WP from the last statement to the first** 

|**To prov**<br>a ><br>⇒|**e**P ⇒ WP(S, Q)**,**<br>2<br>WP(a := a · 2; b :|**that is:**<br>= a + 1,  b > 5)|||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|2|b := a + 1|b > 5|[b ← a + 1]|a + 1 > 5<br>which simplifies to<br>a > 4|
|1|a := a * 2|a > 4|[a ← a · 2]|a · 2 > 4<br>which simplifies to<br>a > 2|



#### **Step 2. Compare the precondition with the WP** 

The given precondition is a > 2. The computed WP is a > 2. The two assertions are identical, so P ⇒ WP holds and the triple is valid. 

|**Proof outline**||
|---|---|
|{a > 2}|_// given precondition = WP_|
|**a := a * 2;**||
|{a > 4}|_// WP of b := a + 1_|
|**b := a + 1;**||
|{b > 5}|_// postcondition_|



### **Exercise 1b** 

|**Triple to prove**|
|---|
|{x = 5}|
|**y := x + 1;**|
|**x := y * y;**|
|{ x = 36 }|



**Step 1. Compute the WP from the last statement to the first** 

|**To pro**<br>x<br>⇒|**ve**P ⇒ WP(S, Q)**,**<br>= 5<br>WP(y := x + 1; x|**that is:**<br>:= y · y,  x = 36)|||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|2|x := y * y|x = 36|[x ← y · y]|y · y = 36|
|1|y := x + 1|y · y = 36|[y ← x + 1]|(x + 1) · (x + 1) = 36<br>which simplifies to<br>x + 1 = 6 ∨ x + 1 = −6<br>which gives<br>x = 5 ∨ x = −7|



Page 2 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 2. Compare the precondition with the WP** 

The given precondition x = 5 is not identical to the WP x = 5 ∨ x = −7. However, x = 5 ⇒ (x = 5 ∨ x = −7) is true, since x = 5 makes the left part of the disjunction true. The precondition is stronger than the WP, so the consequence rule completes the proof. 

|**Proof outline**||
|---|---|
|{x = 5}|_// given precondition_|
|{x = 5 ∨ x = −7}|_// consequence rule: x = 5 implies the WP_|
|**y := x + 1;**||
|{ y·y= 36}|_// WP of x := y * y_|
|**x := y * y;**||
|{x = 36}|_// postcondition_|



### **Exercise 1c** 

This program swaps the values of a and b without a temporary variable. A and B are logical variables that record the initial values. 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** { a = A ∧ b = B } **a := a + b; b := a - b; a := a - b;** { a = B ∧ b = A } 

**Step 1. Compute the WP from the last statement to the first** 

**To prove** P ⇒ WP(S, Q) **, that is:** a = A ∧ b = B ⇒  WP(a := a + b; b := a − b; a := a − b,  a = B ∧ b = A) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|a := a - b|a = B ∧ b = A|[a ← a − b]|a − b = B ∧ b = A|
|2|b := a - b|a − b = B ∧ b = A|[b ← a − b]|a − (a − b) = B ∧ a − b = A<br>which simplifies to<br>b = B ∧ a − b = A|
|1|a := a + b|b = B ∧ a − b = A|[a ← a + b]|b = B ∧ (a + b) − b = A<br>which simplifies to<br>b = B ∧ a = A|



#### **Step 2. Compare the precondition with the WP** 

The WP b = B ∧ a = A is the given precondition a = A ∧ b = B with the two conjuncts in a different order. Therefore P ⇒ WP holds. 

Page 3 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Proof outline** <u><mark>{ a = A ∧ b = B }</mark></u> _// given precondition = WP_ **a := a + b;** { b = B ∧ a − b = A } **b := a - b;** { a − b = B ∧ b = A } **a := a - b;** <u><mark>{ a = B ∧ b = A }</mark></u> _// postcondition_ 

### **Exercise 1d** 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** { x = y } **x := x * 3; z := x + y; y := z - x;** <u>{ y = x / 3 }</u> 

**Step 1. Compute the WP from the last statement to the first** 

**To prove** P ⇒ WP(S, Q) **, that is:** x = y ⇒  WP(x := x · 3; z := x + y; y := z − x,  y = x / 3) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|y := z - x|y = x / 3|[y ← z − x]|z − x = x / 3<br>which simplifies to<br>z = x + x / 3<br>that is<br>z = 4 · x / 3|
|2|z := x + y|z = 4 · x / 3|[z ← x + y]|x + y = 4 · x / 3<br>which simplifies to<br>y = x / 3|
|1|x := x * 3|y = x / 3|[x ← x · 3]|y = (x · 3) / 3<br>which simplifies to<br>y = x|



#### **Step 2. Compare the precondition with the WP** 

The WP is y = x, which is the given precondition x = y written the other way round. Therefore P ⇒ WP holds. 

Page 4 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x =y }|_// given precondition = WP_|
|**x := x * 3;**||
|{ y = x / 3 }||
|**z := x + y;**||
|{ z = 4 · x / 3 }||
|**y := z - x;**||
|{ y= x/3}|_// postcondition_|



### **Exercise 1e** 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** { x = 10 } **x := x + y; y := y - 1; z := x - y;** <u>{ z = 11 }</u> 

**Step 1. Compute the WP from the last statement to the first** 

**To prove** P ⇒ WP(S, Q) **, that is:** x = 10 ⇒  WP(x := x + y; y := y − 1; z := x − y,  z = 11) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|3|z := x - y|z = 11|[z ← x − y]|x − y = 11|
|2|y := y - 1|x − y = 11|[y ← y − 1]|x − (y − 1) = 11<br>which simplifies to<br>x − y + 1 = 11<br>that is<br>x − y = 10|
|1|x := x + y|x − y = 10|[x ← x + y]|(x + y) − y = 10<br>which simplifies to<br>x = 10|



#### **Step 2. Compare the precondition with the WP** 

The WP x = 10 is identical to the given precondition. Therefore the triple is valid. 

Page 5 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x = 10}|_// given precondition = WP_|
|**x := x + y;**||
|{ x − y = 10 }||
|**y := y - 1;**||
|{ x − y = 11 }||
|**z := x - y;**||
|{z = 11}|_// postcondition_|



Page 6 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **2. Conditional statement** 

**Rules used in this section** 

**Conditional rule.** WP(if B then S1 else S2, Q) = (B ⇒ WP(S1, Q)) ∧ (¬B ⇒ WP(S2, Q)). 

**Method.** First compute the WP of each branch with respect to the same postcondition Q. Then combine the two results with the formula above and simplify. Finally check that the given precondition implies the combined WP. 

**Two facts that help with the simplification.** An implication A ⇒ B is true when every state that satisfies A also satisfies B. The implication A ⇒ B can also be written as ¬A ∨ B. 

**In the proof outline** , each branch starts with the precondition together with the guard (then branch) or its negation (else branch). That assertion must imply the WP of the branch. 

**Exercise 2a** 

**Triple to prove** { True } **if (x < 0) then y := -x; else y := x;** { y ≥ 0 } 

**Step 1. Compute the WP of each branch** 

|**To prove**|P ⇒ WP(S,|Q)**, that is:**|||
|---|---|---|---|---|
|True<br>⇒  W|P(if (x < 0)|then y := −x else|y := x,  y ≥ 0)||
|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|then|x < 0|y := -x|[y ← −x]|(y ≥ 0)[y ← −x]  =  −x ≥ 0  =  x ≤ 0|
|else|x ≥ 0|y := x|[y ← x]|(y ≥ 0)[y ← x]  =  x ≥ 0|



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x < 0 ⇒ x ≤ 0) ∧ (x ≥ 0 ⇒ x ≥ 0)|Conditional rule.|
|= True ∧ True|Every x below 0 is also at most 0. The second<br>implication has the same formula on both sides.|
|= True||



Page 7 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 3. Compare the precondition with the WP** 

The given precondition is True and the WP is True. Therefore the triple is valid. The program computes the absolute value of x, which is never negative. 

|**Proof outline**||
|---|---|
|{True}|_// given precondition_|
|**if (x < 0) then {**||
|{x < 0}|_// precondition_∧_guard_|
|{−x ≥ 0}|_// since x < 0 implies −x > 0_|
|**y := -x;**||
|{y ≥ 0}||
|**} else {**||
|{x ≥ 0}|_// precondition_∧_¬guard = branch WP_|
|**y := x;**||
|{y ≥ 0}||
|**}**||
|{ y≥ 0}|_// postcondition_|



### **Exercise 2b** 

The program stores the maximum of a and b in max. The postcondition Q is (max = a ∨ max = b) ∧ max ≥ a ∧ max ≥ b. It says that max is one of the two values and that it is not smaller than either of them. 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** <u>{ True }</u> **if (a > b) then max := a; else max := b;** <u>{ (max = a ∨ max = b) ∧ max ≥ a ∧ max ≥ b }</u> 

Page 8 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 1. Compute the WP of each branch** 

|**To prove**<br>True<br>⇒  W|P ⇒ WP(S, Q<br><br>P(if (a > b)|)**, that is:**<br>then max := a els|e max := b,  (ma|x = a ∨ max = b) ∧ max ≥ a ∧ max ≥ b)|
|---|---|---|---|---|
|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|then|a > b|max := a|[max ← a]|(a = a ∨ a = b) ∧ a ≥ a ∧ a ≥ b<br>The formulaa = ais true, so the disjunction is true. The<br>formulaa ≥ ais also true. What remains is:<br>a ≥ b|
|else|a ≤ b|max := b|[max ← b]|(b = a ∨ b = b) ∧ b ≥ a ∧ b ≥ b<br>For the same reason, what remains is:<br>b ≥ a|



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (a > b ⇒ a ≥ b) ∧ (a ≤ b ⇒ b ≥ a)|Conditional rule.|
|= True ∧ True|If a is strictly greater than b, then a ≥ b. The formulas a<br>≤ b and b ≥ a say the same thing.|
|= True||



#### **Step 3. Compare the precondition with the WP** 

The given precondition True implies the WP True. Therefore the triple is valid. 

|**Proof outline**||
|---|---|
|{True}|_// given precondition_|
|**if (a > b) then {**||
|{a > b}|_// precondition_∧_guard_|
|{ (a = a ∨ a = b)∧ a ≥ a ∧ a ≥ b}|_// equivalent to a ≥ b, implied by a > b_|
|**max := a;**||
|{ (max = a ∨ max = b) ∧ max ≥ a ∧ max ≥ b }||
|**} else {**||
|{a ≤ b}|_// precondition_∧_¬guard_|
|{ (b = a ∨ b = b)∧ b ≥ a ∧ b ≥ b}<br>**max := b;**|_// equivalent to b ≥ a, implied by a ≤ b_|
|{ (max = a ∨ max = b) ∧ max ≥ a ∧ max ≥ b }||
|**}**||
|{ (max = a ∨ max = b)∧ max ≥ a ∧ max ≥ b}|_// postcondition_|



Page 9 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 2c** 

|**Triple to pro**|**ve**|
|---|---|
|{ x = 20 ∨|x = 10 }|
|**if (x >**|**10) then**|
|**y :=**|**x - 5;**|
|**else**||
|**y :=**|**x + 5;**|
|{ y = 15 }||



**Step 1. Compute the WP of each branch** 

**To prove** P ⇒ WP(S, Q) **, that is:** x = 20 ∨ x = 10 ⇒  WP(if (x > 10) then y := x − 5 else y := x + 5,  y = 15) 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|x > 10|y := x - 5|[y ← x − 5]|x − 5 = 15  =  x = 20|
|else|x ≤ 10|y := x + 5|[y ← x + 5]|x + 5 = 15  =  x = 10|



#### **Step 2. Combine the two branches** 

This combination needs more work than the previous ones, since neither implication is true on its own. We rewrite each implication A ⇒ B as ¬A ∨ B and then distribute. 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x > 10 ⇒ x = 20) ∧ (x ≤ 10 ⇒ x = 10)|Conditional rule.|
|= (x ≤ 10 ∨ x = 20) ∧ (x > 10 ∨ x = 10)|A⇒B is the same as ¬A∨B.|
|= (x ≤ 10 ∧ x > 10) ∨ (x ≤ 10 ∧ x = 10)<br>∨ (x = 20 ∧ x > 10) ∨ (x = 20 ∧ x = 10)|Distribute∧over∨. This gives four cases.|
|= False ∨ x = 10 ∨ x = 20 ∨ False|The first and last cases are contradictions. In the two<br>middle cases the equality already implies the<br>inequality.|
|= x = 20 ∨ x = 10||



#### **Step 3. Compare the precondition with the WP** 

The given precondition x = 20 ∨ x = 10 is exactly the WP. Therefore the triple is valid. In words: the only value above 10 that produces y = 15 is 20, and the only value at or below 10 that produces y = 15 is 10. 

Page 10 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x = 20 ∨ x = 10}|_// given precondition = WP_|
|**if (x > 10) then {**||
|{ (x = 20 ∨ x = 10)∧ x > 10}|_// precondition_∧_guard_|
|{x − 5 = 15}|_// the guard rules out x = 10, so x = 20_|
|**y := x - 5;**||
|{y = 15}||
|**} else {**||
|{ (x = 20 ∨ x = 10)∧ x ≤ 10}|_// precondition_∧_¬guard_|
|{x + 5 = 15}|_// ¬guard rules out x = 20, so x = 10_|
|**y := x + 5;**||
|{ y = 15 }||
|**}**||
|{ y= 15}|_// postcondition_|



### **Exercise 2d** 

This program combines an assignment and a conditional. We write Q for the postcondition (x = 0 ∧ z = 0) ∨ (x ≠ 0 ∧ z = 1). We first compute the WP of the conditional with respect to Q, and then the WP of z := 1 with respect to that result. 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** { True } **z := 1; if (x = 0) then z := 0; else skip;** { (x = 0 ∧ z = 0) ∨ (x ≠ 0 ∧ z = 1) } 

**Step 1. Compute the WP of each branch** 

|**To prove**<br>True<br>⇒  W|P ⇒ WP(S, Q<br><br>P(z := 1; if (|)**, that is:**<br>x = 0) then z :=|0 else skip,  (x =|0 ∧ z = 0) ∨ (x ≠ 0 ∧ z = 1))|
|---|---|---|---|---|
|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|then|x = 0|z := 0|[z ← 0]|(x = 0 ∧ 0 = 0) ∨ (x ≠ 0 ∧ 0 = 1)<br>The formula0 = 0is true and0 = 1is false, so this<br>reduces to:<br>x = 0|
|else|x ≠ 0|skip|—|The skip rule givesWP(skip, Q) = Q:<br>(x = 0 ∧ z = 0) ∨ (x ≠ 0 ∧ z = 1)|



Page 11 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x = 0 ⇒ x = 0)|Conditional rule.|
|∧ (x ≠ 0 ⇒ (x = 0 ∧ z = 0) ∨ (x ≠ 0 ∧ z = 1))||
|= True ∧ (x ≠ 0 ⇒ z = 1)|The first implication is trivially true. In the second one<br>we may assume x ≠ 0. In this case the first disjunct is<br>false and the second reduces to z = 1.|
|= x ≠ 0 ⇒ z = 1||



#### **Step 3. Go through the assignment z := 1** 

**The same proof continues with the first statement. Step 2 gave the WP of the conditional, so what remains is:** 

|Tr<br>⇒|ue<br>WP(z := 1,  x ≠|0 ⇒ z = 1)|||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|1|z := 1|x ≠ 0 ⇒ z = 1|[z ← 1]|x ≠ 0 ⇒ 1 = 1<br>which simplifies to<br>True|



#### **Step 4. Compare the precondition with the WP** 

The given precondition True implies the WP True. Therefore the triple is valid. 

|**Proof outline**||
|---|---|
|{True}|_// given precondition_|
|{x ≠ 0 ⇒ 1 = 1}|_// equivalent to True_|
|**z := 1;**||
|{x ≠ 0 ⇒ z = 1}|_// WP of the conditional_|
|**if (x = 0) then {**||
|{ (x ≠ 0 ⇒ z = 1)∧ x = 0}|_// precondition_∧_guard_|
|{x = 0}|_// WP of z := 0_|
|**z := 0;**||
|{ (x = 0 ∧ z = 0) ∨ (x ≠ 0 ∧ z = 1) }||
|**} else {**||
|{ (x ≠ 0 ⇒ z = 1)∧ x ≠ 0}|_// precondition_∧_¬guard_|
|{x ≠ 0 ∧ z = 1}|_// modus ponens_|
|{ (x = 0 ∧ z = 0)∨(x ≠ 0 ∧ z = 1) }<br>**skip;**|_// the second disjunct holds_|
|{ (x = 0 ∧ z = 0)∨(x ≠ 0 ∧ z = 1) }||
|**}**||
|{ (x = 0 ∧ z = 0)∨(x ≠ 0 ∧ z = 1) }|_// postcondition_|



Page 12 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 2e** 

**Triple to prove** { x ≥ −1 } **if (x > 0) then x := x - 1; else x := x + 1;** { x ≥ 0 } 

**Step 1. Compute the WP of each branch** 

**To prove** P ⇒ WP(S, Q) **, that is:** x ≥ −1 ⇒  WP(if (x > 0) then x := x − 1 else x := x + 1,  x ≥ 0) 

|**Branch**|**Entered**<br>**when**|**Statement**|**Substitution**|**WP of the branch with respect to Q**|
|---|---|---|---|---|
|then|x > 0|x := x - 1|[x ← x − 1]|x − 1 ≥ 0  =  x ≥ 1|
|else|x ≤ 0|x := x + 1|[x ← x + 1]|x + 1 ≥ 0  =  x ≥ −1|



**Step 2. Combine the two branches** 

|**Formula**|**Reason**|
|---|---|
|WP_if = (x > 0 ⇒ x ≥ 1) ∧ (x ≤ 0 ⇒ x ≥ −1)|Conditional rule.|
|= True ∧ (x ≤ 0 ⇒ x ≥ −1)|x is an integer, so x > 0 and x ≥ 1 describe the same<br>values.|
|= x > 0 ∨ x ≥ −1|A⇒B is the same as ¬A∨B.|
|= x ≥ −1|Every x > 0 already satisfies x ≥ −1.|



#### **Step 3. Compare the precondition with the WP** 

The given precondition x ≥ −1 is exactly the WP. Therefore the triple is valid. 

Page 13 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Proof outline**||
|---|---|
|{x ≥ −1}|_// given precondition = WP_|
|**if (x > 0) then {**||
|{x ≥ −1 ∧ x > 0}|_// precondition_∧_guard_|
|{x − 1 ≥ 0}|_// x > 0 gives x ≥ 1 for integers_|
|**x := x - 1;**||
|{x ≥ 0}||
|**} else {**||
|{x ≥ −1 ∧ x ≤ 0}|_// precondition_∧_¬guard_|
|{x + 1 ≥ 0}|_// from x ≥ −1_|
|**x := x + 1;**||
|{ x ≥ 0 }||
|**}**||
|{x ≥ 0}|_// postcondition_|



Page 14 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **3. Loops** 

**Rules used in this section** 

**While rule (combined with the consequence rule).** To prove {P} while B do S {Q} we need an invariant I and three obligations: 

(1) **Establishment:** P ⇒ I. The invariant holds before the first iteration. When the loop is preceded by initialisation statements, the obligation is P ⇒ WP(init, I). 

(2) **Preservation:** {I ∧ B} S {I}. We compute WP(S, I) and prove the implication I ∧ B ⇒ WP(S, I). 

(3) **Exit:** I ∧ ¬B ⇒ Q. When the loop stops, the guard is false and the invariant still holds, and together they must give the postcondition. 

(4) **Termination.** A variant E is an integer expression with two properties: (4a) I ∧ B ⇒ E ≥ 0, and (4b) I ∧ B ∧ E = E₀ ⇒ WP(S, E < E₀), where E₀ is the value of E before the iteration. The lecture slides call this value n; we write E₀ because n is often a program variable in these exercises. 

**How each obligation is presented.** First we write the implication out in full, with the actual formulas, in a green box. Then we prove it line by line. 

**Two kinds of replacement appear in the proofs.** The first is the assignment rule, WP(x := e, Q) = Q[x ← e], which we use to compute a WP; the tables show it in the column Substitution. The second is replacement of equals by equals: when the assumptions contain an equation such as i = 0, we may replace i by 0 in the formula we are proving. The two look similar, but only the first one comes from a program statement. 

**Where the invariant comes from.** We follow the recipe from the lecture. We start from the postcondition, trace the variables at the loop head, generalise the postcondition by replacing the final value with the loop counter, and add bounds for the counter. 

### **Exercise 3a: factorial** 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** { n ≥ 0 ∧ f = 1 ∧ i = 0 } **while (i < n) do { i := i + 1; f := f * i; }** { f = n! } 

**Step 1. Find the invariant and the variant** 

The postcondition is f = n!. The table traces the variables at the loop head for n = 4. 

Page 15 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**At the loop head**|**i**|**f**|**i!**|
|---|---|---|---|
|before iteration 1|0|1|1|
|before iteration 2|1|1|1|
|before iteration 3|2|2|2|
|before iteration 4|3|6|6|
|at exit (i = n)|4|24|24|



At every loop head, f equals i!. This is the postcondition with n replaced by the counter i. The counter starts at 0 and stops at n, which gives the bounds 0 ≤ i ≤ n. The counter moves towards n by one at each iteration, so the distance n − i is the variant. 

**Invariant** I  ≡  f = i! ∧ 0 ≤ i ≤ n **Guard** B  ≡  i < n **Variant** E  =  n − i 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** n ≥ 0 ∧ f = 1 ∧ i = 0 ⇒ f = i! ∧ 0 ≤ i ≤ n 

The precondition contains the equations f = 1 and i = 0. We replace f by 1 and i by 0 in the conclusion, and check that the result is true. 

|**Step of theproof**|**Reason**|
|---|---|
|(f = i! ∧ 0 ≤ i ≤ n)[f ← 1, i ← 0]|Replace f by 1 and i by 0, using f = 1 and i = 0 from P.|
|= 1 = 0! ∧ 0 ≤ 0 ≤ n||
|= True ∧ True ∧ 0 ≤ n|0! = 1, and 0 ≤ 0 is true.|
|= True|0 ≤ n is the conjunct n ≥ 0 of P.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** f = i! ∧ 0 ≤ i ≤ n ∧ i < n ⇒  WP(i := i + 1; f := f · i,  f = i! ∧ 0 ≤ i ≤ n) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|f := f * i|f = i! ∧ 0 ≤ i ≤ n|[f ← f · i]|f · i = i! ∧ 0 ≤ i ≤ n|
|1|i := i + 1|f · i = i! ∧ 0 ≤ i ≤ n|[i ← i + 1]|f · (i + 1) = (i + 1)! ∧ 0 ≤ i + 1 ≤ n|



Page 16 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** f = i! ∧ 0 ≤ i ≤ n ∧ i < n ⇒ f · (i + 1) = (i + 1)! ∧ 0 ≤ i + 1 ≤ n 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|f · (i + 1) = i! · (i + 1)|Replace f by i!, using f = i! from I.|
|= (i + 1)!|Definition of factorial: (i + 1)! = i! · (i + 1).|
|0 ≤ i + 1|From 0 ≤ i.|
|i + 1 ≤ n|From the guard i < n, since i and n are integers.|



The bound i + 1 ≤ n needs the guard. Without the guard, i ≤ n would only give i + 1 ≤ n + 1. 

**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** f = i! ∧ 0 ≤ i ≤ n ∧ ¬(i < n) ⇒ f = n! 



|**Step of theproof**|**Reason**|
|---|---|
|¬(i < n)  =  i ≥ n|Negation of the guard.|
|i ≤ n ∧ i ≥ n  gives  i = n|Combine with i ≤ n from I.|
|f = i!  becomes  f = n!|Replace i by n, using i = n.|



**Step 5. Termination with the variant** E = n − i 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** f = i! ∧ 0 ≤ i ≤ n ∧ i < n ⇒ n − i ≥ 0 

From the guard i < n we get n − i > 0, so n − i ≥ 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

Page 17 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** f = i! ∧ 0 ≤ i ≤ n ∧ i < n ∧ n − i = E₀ ⇒  WP(i := i + 1; f := f · i,  n − i < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|f := f * i|n − i < E₀|[f ← f · i]|n − i < E₀|
|||||f does not occur, so nothing changes.|
|1|i := i + 1|n − i < E₀|[i ← i + 1]|n − (i + 1) < E₀|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** f = i! ∧ 0 ≤ i ≤ n ∧ i < n ∧ n − i = E₀ ⇒ n − (i + 1) < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|n − (i + 1) = (n − i) − 1 = E₀ − 1|Rearrange, then replace n − i by E₀.|
|E₀ − 1 < E₀|Always true. The variant decreases by exactly 1.|



#### **Step 6. Proof outline** 

**Proof outline** <u><mark>{ n ≥ 0 ∧ f = 1 ∧ i = 0 }</mark></u> _// given precondition_ <u><mark>{ f = i! ∧ 0 ≤ i ≤ n }</mark></u> _// establishment: P_ ⇒ _I_ **while (i < n) do {** <u><mark>{ f = i! ∧ 0 ≤ i ≤ n ∧ i < n }</mark></u> _// I_ ∧ _B_ <u><mark>{ f · (i + 1) = (i + 1)! ∧ 0 ≤ i + 1 ≤ n }</mark></u> _// preservation: implied by I_ ∧ _B_ **i := i + 1;** { f · i = i! ∧ 0 ≤ i ≤ n } **f := f * i;** <u><mark>{ f = i! ∧ 0 ≤ i ≤ n }</mark></u> _// I holds again_ **}** <u><mark>{ f = i! ∧ 0 ≤ i ≤ n ∧ ¬(i < n) }</mark></u> _// I_ ∧ _¬B_ <u><mark>{ f = n! }</mark></u> _// exit: i = n_ 

Page 18 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 3b: sum of 1 to n** 

**Triple to prove** { n ≥ 0 ∧ s = 0 ∧ i = 0 } **while (i < n) do { i := i + 1; s := s + i; }** { s = n · (n + 1) / 2 } 

**Step 1. Find the invariant and the variant** 

The postcondition is s = n · (n + 1) / 2. The table traces the variables at the loop head for n = 4. 

|**At the loop head**|**i**|**s**|**i ·(i + 1) / 2**|
|---|---|---|---|
|before iteration 1|0|0|0|
|before iteration 2|1|1|1|
|before iteration 3|2|3|3|
|before iteration 4|3|6|6|
|at exit (i = n)|4|10|10|



At every loop head, s is the sum 1 + 2 + … + i, which equals i · (i + 1) / 2. This is the postcondition with n replaced by i. The bounds and the variant are the same as in 3a. 

**Invariant** I  ≡  s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n **Guard** B  ≡  i < n **Variant** E  =  n − i 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** n ≥ 0 ∧ s = 0 ∧ i = 0 ⇒ s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n 

The precondition contains the equations s = 0 and i = 0. We replace s and i by these values in the conclusion. 

|**Step of theproof**|**Reason**|
|---|---|
|(s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n)[s ← 0, i ← 0]|Replace s by 0 and i by 0, using s = 0 and i = 0 from P.|
|= 0 = 0 · (0 + 1) / 2 ∧ 0 ≤ 0 ≤ n||
|= True ∧ True ∧ 0 ≤ n|0 · 1 / 2 = 0, and 0 ≤ 0 is true.|
|= True|0 ≤ n is the conjunct n ≥ 0 of P.|



Page 19 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n ∧ i < n ⇒  WP(i := i + 1; s := s + i,  s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|s := s + i|s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n|[s ← s + i]|s + i = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n|
|1|i := i + 1|s + i = i · (i + 1) / 2 ∧ 0 ≤ i|[i ← i + 1]|s + (i + 1) = (i + 1) · (i + 2) / 2|
|||≤ n||∧ 0 ≤ i + 1 ≤ n|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n ∧ i < n ⇒ s + (i + 1) = (i + 1) · (i + 2) / 2 ∧ 0 ≤ i + 1 ≤ n 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|s + (i + 1) = i · (i + 1) / 2 + (i + 1)|Replace s by i · (i + 1) / 2, using I.|
|= i · (i + 1) / 2 + 2 · (i + 1) / 2|Write i + 1 with denominator 2.|
|= (i + 1) · (i + 2) / 2|Factor out (i + 1).|
|0 ≤ i + 1|From 0 ≤ i.|
|i + 1 ≤ n|From the guard i < n.|



**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n ∧ ¬(i < n) ⇒ s = n · (n + 1) / 2 



|**Step of theproof**|**Reason**|
|---|---|
|¬(i < n)  =  i ≥ n|Negation of the guard.|
|i ≤ n ∧ i ≥ n  gives  i = n|Combine with i ≤ n from I.|
|s = i · (i + 1) / 2  becomes  s = n · (n + 1) / 2|Replace i by n, using i = n.|



Page 20 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

**Step 5. Termination with the variant** E = n − i 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n ∧ i < n ⇒ n − i ≥ 0 

From the guard i < n we get n − i > 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n ∧ i < n ∧ n − i = E₀ ⇒  WP(i := i + 1; s := s + i,  n − i < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|s := s + i|n − i < E₀|[s ← s + i]|n − i < E₀|
|||||s does not occur, so nothing changes.|
|1|i := i + 1|n − i < E₀|[i ← i + 1]|n − (i + 1) < E₀|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** s = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n ∧ i < n ∧ n − i = E₀ ⇒ n − (i + 1) < E₀ 



|**Step of theproof**|**Reason**|
|---|---|
|n − (i + 1) = (n − i) − 1 = E₀ − 1|Rearrange, then replace n − i by E₀.|
|E₀ − 1 < E₀|Always true.|



Page 21 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{n ≥ 0 ∧ s = 0 ∧ i = 0}|_// given precondition_|
|{s = i ·(i + 1) /2 ∧ 0 ≤ i ≤ n}|_// establishment: P_⇒_I_|
|**while (i < n) do {**||
|{s = i ·(i + 1) /2 ∧ 0 ≤ i ≤ n ∧ i < n}|_// I_∧_B_|
|{s +(i + 1)=(i + 1)·(i + 2) /2 ∧ 0 ≤ i + 1 ≤ n}|_// preservation: implied by I_∧_B_|
|**i := i + 1;**||
|{ s + i = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n }||
|**s := s + i;**||
|{s = i ·(i + 1) /2 ∧ 0 ≤ i ≤ n}|_// I holds again_|
|**}**||
|{s = i ·(i + 1) /2 ∧ 0 ≤ i ≤ n ∧ ¬(i < n) }|_// I_∧_¬B_|
|{s = n ·(n + 1) /2}|_// exit: i = n_|



Page 22 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 3c: integer square root** 

The loop increases i until its square is larger than n. As a consequence, at the exit i − 1 is the integer square root of n: it is the largest number whose square is at most n. 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** <u>{ n ≥ 0 ∧ s = 1 ∧ i = 1 }</u> **while (s <= n) do { i := i + 1; s := i * i; }** <u>{ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n < i · i }</u> 

**Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for n = 5. 

|**At the loop head**|**i**|**s**|**(i − 1) ·(i − 1)**|**i · i**|
|---|---|---|---|---|
|before iteration 1|1|1|0|1|
|before iteration 2|2|4|1|4|
|at exit (s > 5)|3|9|4|9|



Three facts hold at every loop head. First, s = i · i, since s starts as 1 · 1 and the body always sets s to the square of the new i. Second, i ≥ 0, since i starts at 1 and only increases. Third, the previous candidate i − 1 is not too large, that is (i − 1) · (i − 1) ≤ n. At the start this is 0 · 0 ≤ n, which holds because n ≥ 0. The part n < i · i of the postcondition is the negated guard, so it does not belong in the invariant. 

**Invariant** I  ≡  s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n **Guard** B  ≡  s ≤ n **Variant** E  =  n − s 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** n ≥ 0 ∧ s = 1 ∧ i = 1 ⇒ s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n 

The precondition contains the equations s = 1 and i = 1. We replace s and i by these values in the conclusion. 

Page 23 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|I[s ← 1, i ← 1]|Replace s by 1 and i by 1, using P.|
|= 1 = 1 · 1 ∧ 1 ≥ 0 ∧ (1 − 1) · (1 − 1) ≤ n||
|= True ∧ True ∧ 0 ≤ n|Evaluate each conjunct.|
|= True|0 ≤ n is the conjunct n ≥ 0 of P.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

We compute WP(body, I) with the assignment rule, starting with the last statement of the body. Each row replaces one variable, as shown in the column Substitution. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n ∧ s ≤ n ⇒  WP(i := i + 1; s := i · i,  s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|s := i * i|s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i<br>− 1) ≤ n|[s ← i · i]|i · i = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤<br>n<br>The first conjunct is always true, so this<br>simplifies to:<br>i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n|
|1|i := i + 1|i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n|[i ← i + 1]|i + 1 ≥ 0 ∧ (i + 1 − 1) · (i + 1 − 1) ≤<br>n<br>which simplifies to<br>i + 1 ≥ 0 ∧ i · i ≤ n|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n ∧ s ≤ n ⇒ i + 1 ≥ 0 ∧ i · i ≤ n 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|i + 1 ≥ 0|From i ≥ 0.|
|i · i = s ≤ n|Replace i · i by s, using s = i · i from I. Then use the|
||guard s ≤ n.|



This is the step where the guard does the work. The guard says that the current i is not too large. After i := i + 1, the old i becomes the previous candidate, and the fact i · i ≤ n becomes (i − 1) · (i − 1) ≤ n for the new i. 

**Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** 

Page 24 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n ∧ ¬(s ≤ n) ⇒ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n < i · i 



|**Step of theproof**|**Reason**|
|---|---|
|¬(s ≤ n)  =  s > n|Negation of the guard.|
|n < s = i · i|Replace s by i · i, using I. This gives the part n < i · i.|
|i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n|Both are part of I.|



**Step 5. Termination with the variant** E = n − s 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n ∧ s ≤ n ⇒ n − s ≥ 0 

Directly from the guard s ≤ n. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, that is:** s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n ∧ s ≤ n ∧ n − s = E₀ ⇒  WP(i := i + 1; s := i · i,  n − s < E₀) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|2|s := i * i|n − s < E₀|[s ← i · i]|n − i · i < E₀|
|1|i := i + 1|n − i · i < E₀|[i ← i + 1]|n − (i + 1) · (i + 1) < E₀|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** s = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n ∧ s ≤ n ∧ n − s = E₀ ⇒ n − (i + 1) · (i + 1) < E₀ 

Page 25 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|n − (i + 1) · (i + 1) = n − i · i − 2 · i − 1|Expand the square.|
|= (n − s) − 2 · i − 1|Replace i · i by s, using I.|
|= E₀ − 2 · i − 1|Replace n − s by E₀.|
|E₀ − 2 · i − 1 < E₀|Since i ≥ 0, we subtract at least 1.|



#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{n ≥ 0 ∧ s = 1 ∧ i = 1}|_// given precondition_|
|{s = i · i ∧ i ≥ 0 ∧(i − 1)·(i − 1)≤ n}|_// establishment: P_⇒_I_|
|**while (s <= n) do {**||
|{s = i · i ∧ i ≥ 0 ∧(i − 1)·(i − 1)≤ n ∧ s ≤ n}|_// I_∧_B_|
|{i + 1 ≥ 0 ∧ i · i ≤ n}|_// preservation: i · i = s ≤ n_|
|**i := i + 1;**||
|{ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n }||
|**s := i * i;**||
|{s = i · i ∧ i ≥ 0 ∧(i − 1)·(i − 1)≤ n}|_// I holds again_|
|**}**||
|{s = i · i ∧ i ≥ 0 ∧(i − 1)·(i − 1)≤ n ∧ ¬(s ≤ n) }|_// I_∧_¬B_|
|{i ≥ 0 ∧(i − 1)·(i − 1)≤ n < i · i}|_// exit_|



Page 26 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

### **Exercise 3d: Fibonacci numbers** 

We use the definition fib(0) = 0, fib(1) = 1 and fib(k) = fib(k − 1) + fib(k − 2) for k ≥ 2. The variable a holds the current Fibonacci number and b holds the previous one. 

**Tri** **<mark>p</mark> le to** **<mark>p</mark> rove** <u>{ n ≥ 1 ∧ a = 1 ∧ b = 0 ∧ i = 1 }</u> **while (i < n) do { temp := a; a := a + b; b := temp; i := i + 1; }** { a = fib(n) } 

**Step 1. Find the invariant and the variant** 

The table traces the variables at the loop head for n = 5. 

|**At the loop head**|**i**|**a**|**b**|**fib(i)**|**fib(i − 1)**|
|---|---|---|---|---|---|
|before iteration 1|1|1|0|1|0|
|before iteration 2|2|1|1|1|1|
|before iteration 3|3|2|1|2|1|
|before iteration 4|4|3|2|3|2|
|at exit (i = n)|5|5|3|5|3|



Generalising the postcondition a = fib(n) gives a = fib(i). This alone is not enough. The body computes the new a from a and b, so preservation needs to know what b is. The trace shows that b is always fib(i − 1). The counter starts at 1, which gives the bounds 1 ≤ i ≤ n. 

**Invariant** I  ≡  a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n **Guard** B  ≡  i < n **Variant** E  =  n − i 

**Step 2. Establishment:** P ⇒ I 

**To prove** P ⇒ I **, written out in full** n ≥ 1 ∧ a = 1 ∧ b = 0 ∧ i = 1 ⇒ a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n 

The precondition contains the equations a = 1, b = 0 and i = 1. We replace a, b and i by these values in the conclusion. 

Page 27 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

|**Step of theproof**|**Reason**|
|---|---|
|I[a ← 1, b ← 0, i ← 1]|Replace a, b and i, using P.|
|= 1 = fib(1) ∧ 0 = fib(0) ∧ 1 ≤ 1 ≤ n||
|= True ∧ True ∧ True ∧ 1 ≤ n|fib(1) = 1 and fib(0) = 0 by definition.|
|= True|1 ≤ n is part of P. Without it the bound 1 ≤ i ≤ n would<br>fail at the start.|



#### **Step 3. Preservation:** I ∧ B ⇒ WP(body, I) 

The body has four statements, so the WP table has four rows. We start with the last statement. 

**To prove** I ∧ B ⇒ WP(body, I) **, that is:** a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n ∧ i < n ⇒  WP(temp := a; a := a + b; b := temp; i := i + 1,  a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n) 

|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|---|---|---|---|---|
|4|i := i + 1|a = fib(i) ∧ b = fib(i − 1)<br>∧ 1 ≤ i ≤ n|[i ← i + 1]|a = fib(i + 1) ∧ b = fib(i)<br>∧ 1 ≤ i + 1 ≤ n|
|3|b := temp|a = fib(i + 1) ∧ b = fib(i)<br>∧ 1 ≤ i + 1 ≤ n|[b ← temp]|a = fib(i + 1) ∧ temp = fib(i)<br>∧ 1 ≤ i + 1 ≤ n|
|2|a := a + b|a = fib(i + 1) ∧ temp =<br>fib(i)<br>∧ 1 ≤ i + 1 ≤ n|[a ← a + b]|a + b = fib(i + 1) ∧ temp = fib(i)<br>∧ 1 ≤ i + 1 ≤ n|
|1|temp := a|a + b = fib(i + 1) ∧ temp =<br>fib(i)<br>∧ 1 ≤ i + 1 ≤ n|[temp ← a]|a + b = fib(i + 1) ∧ a = fib(i)<br>∧ 1 ≤ i + 1 ≤ n|



**To prove** I ∧ B ⇒ WP(body, I) **, written out in full** a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n ∧ i < n ⇒ a + b = fib(i + 1) ∧ a = fib(i) ∧ 1 ≤ i + 1 ≤ n 

We assume all the facts above the arrow and prove each conjunct below it. 

|**Step of theproof**|**Reason**|
|---|---|
|a + b = fib(i) + fib(i − 1)|Replace a and b, using I.|
|= fib(i + 1)|Since i ≥ 1, we have i + 1 ≥ 2, so the recursive case of<br>the definition applies.|
|a = fib(i)|Part of I.|
|1 ≤ i + 1|From 1 ≤ i.|
|i + 1 ≤ n|From the guard i < n.|



Page 28 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### **Step 4. Exit:** I ∧ ¬B ⇒ Q 

**To prove** I ∧ ¬B ⇒ Q **, written out in full** a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n ∧ ¬(i < n) ⇒ a = fib(n) 



|**Step of theproof**|**Reason**|
|---|---|
|¬(i < n)  =  i ≥ n|Negation of the guard.|
|i ≤ n ∧ i ≥ n  gives  i = n|Combine with i ≤ n from I.|
|a = fib(i)  becomes  a = fib(n)|Replace i by n.|



#### **Step 5. Termination with the variant** E = n − i 

**(4a) The variant is not negative while the loop runs.** 

**To prove** I ∧ B ⇒ E ≥ 0 **, written out in full** a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n ∧ i < n ⇒ n − i ≥ 0 

From the guard i < n we get n − i > 0. 

**(4b) Each iteration makes the variant strictly smaller.** We compute WP(body, E < E₀) with the same substitutions as in the preservation step. 

|**To pro**<br>a<br>⇒|**ve**I ∧ B ∧ E = E₀<br>= fib(i) ∧ b = fib(<br>WP(temp := a; a|⇒ WP(body, E < E₀)**, that is:**<br>i − 1) ∧ 1 ≤ i ≤ n ∧ i < n ∧ n −<br>:= a + b; b := temp; i := i + 1,|i = E₀<br>n − i < E₀)||
|---|---|---|---|---|
|**Step**|**Statement**|**Postcondition Q**|**Substitution**|**WP = Q after the substitution**|
|4|i := i + 1|n − i < E₀|[i ← i + 1]|n − (i + 1) < E₀|
|3|b := temp|n − (i + 1) < E₀|[b ← temp]|n − (i + 1) < E₀<br>b does not occur.|
|2|a := a + b|n − (i + 1) < E₀|[a ← a + b]|n − (i + 1) < E₀<br>a does not occur.|
|1|temp := a|n − (i + 1) < E₀|[temp ← a]|n − (i + 1) < E₀<br>temp does not occur.|



**To prove** I ∧ B ∧ E = E₀ ⇒ WP(body, E < E₀) **, written out in full** 

a = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n ∧ i < n ∧ n − i = E₀ ⇒ 

Page 29 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

#### n − (i + 1) < E₀ 

|**Step of theproof**|**Reason**|
|---|---|
|n − (i + 1) = E₀ − 1 < E₀|Replace n − i by E₀.|



#### **Step 6. Proof outline** 

|**Proof outline**||
|---|---|
|{n ≥ 1 ∧ a = 1 ∧ b = 0 ∧ i = 1}|_// given precondition_|
|{a = fib(i)∧ b = fib(i − 1)∧ 1 ≤ i ≤ n}|_// establishment: P_⇒_I_|
|**while (i < n) do {**||
|{a = fib(i)∧ b = fib(i − 1)∧ 1 ≤ i ≤ n ∧ i < n}|_// I_∧_B_|
|{a + b = fib(i + 1)∧ a = fib(i)∧ 1 ≤ i + 1 ≤ n}|_// preservation: implied by I_∧_B_|
|**temp := a;**||
|{ a + b = fib(i + 1) ∧ temp = fib(i) ∧ 1 ≤ i + 1 ≤ n }<br>**a := a + b;**||
|{a = fib(i + 1)∧ temp = fib(i)∧ 1 ≤ i + 1 ≤ n}<br>**b := temp;**||
|{ a = fib(i + 1) ∧ b = fib(i) ∧ 1 ≤ i + 1 ≤ n }||
|**i := i + 1;**||
|{a = fib(i)∧ b = fib(i − 1)∧ 1 ≤ i ≤ n}|_// I holds again_|
|**}**||
|{a = fib(i)∧ b = fib(i − 1)∧ 1 ≤ i ≤ n ∧ ¬(i < n) }|_// I_∧_¬B_|
|{a = fib(n) }|_// exit: i = n_|



Page 30 

ICT3112 Introduction to Formal Verification of Programs · Hoare Logic exercises 

## **Summary of answers** 

|**Exercise**|**Answer**|
|---|---|
|1a|Valid. WPa > 2, equal to the precondition.|
|1b|Valid. WPx = 5 ∨ x = −7, implied byx = 5.|
|1c|Valid. WPb = B ∧ a = A, equal to the precondition.|
|1d|Valid. WPy = x, equal to the precondition.|
|1e|Valid. WPx = 10, equal to the precondition.|
|2a|Valid. WPTrue.|
|2b|Valid. WPTrue.|
|2c|Valid. WPx = 20 ∨ x = 10, equal to the precondition.|
|2d|Valid. WPTrue.|
|2e|Valid. WPx ≥ −1, equal to the precondition.|
|3a|Valid. Invariantf = i! ∧ 0 ≤ i ≤ n, variantn − i.|
|3b|Valid. Invariants = i · (i + 1) / 2 ∧ 0 ≤ i ≤ n, variantn − i.|
|3c|Valid. Invariants = i · i ∧ i ≥ 0 ∧ (i − 1) · (i − 1) ≤ n, variantn − s.|
|3d|Valid. Invarianta = fib(i) ∧ b = fib(i − 1) ∧ 1 ≤ i ≤ n, variantn − i.|



Page 31 

