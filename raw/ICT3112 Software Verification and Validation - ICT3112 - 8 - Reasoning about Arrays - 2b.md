# ICT3112 - 8 - Reasoning about Arrays - 2b

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Reasoning about Arrays** . if ie | **Writing: The Rule Dr. David Sanan** ay Be = 

# **Where we stopped: the naive rule and aliasing** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

The naive rule gives this triple: 

{𝑎[𝑗] = 0 ∧ 𝑑𝑒𝑓(𝑎[𝑖])}  𝑎[𝑖] ≔ 1  {𝑎[𝑗] = 0} 

**[NAÏVE WRITE]** {𝑄[𝑎[𝐼] ← 𝐸] ∧ 𝑑𝑒𝑓(𝑎[𝐼])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

Take  𝑎 = [4, 0, 9]  and  𝑖 = 𝑗 = 1.  The precondition holds, since  𝑎[1] = 0 ✓ 

before:  𝑎[𝑗] = 0 

𝑎 4 **0** 9 0 1 2 

When 𝑖=𝑗, the names 𝑎[𝑖] and 𝑎[𝑗] refer to the same cell. This is called **aliasing** . 

#### 𝑖𝑗 

𝑎 4 **1** 9 after:  𝑎[𝑗] = 1, so the postcondition is 0 1 2 false  ✗ 𝑖𝑗 

𝑎[𝐼] ≔ 𝐸     behaves like     𝑎 ≔ 𝑎[𝐼 ↦ 𝐸] 

## **Updating an array and reading the updated array** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

𝑎[𝐼 ↦ 𝐸]  is the array equal to  𝑎  everywhere, except that position  𝐼  stores  𝐸.  Example:  𝑎[1 ↦ 7] 



<!-- Start of picture text -->
𝑎 4 0 9 4 7 9<br>𝑎[1 ↦ 7]<br>0 1 2 0 1 2<br><!-- End of picture text -->

Reading an updated array is done in the logic by the **select–store axioms** , which make a case split on the index: 

𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸         if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]     if  𝐽 ≠ 𝐼 _For example,_ 𝑎[1 ↦ 7][1] = 7 _and_ 𝑎[1 ↦ 7][2] = 𝑎[2] = 9 _._ 

**These two equations are all we need to simplify the precondition after the substitution.** 

# **The rule for writing: [ARRAY-ASSIGN]** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

We start from the naive rule, which substitutes the cell: 

**[NAÏVE WRITE]** 

⊢  {𝑄[𝑎[𝐼] ← 𝐸] ∧ 𝑑𝑒𝑓(𝑎[𝐼])}  𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **The rule for writing: [ARRAY-ASSIGN]** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

Instead of the cell, we substitute the **updated array** for  𝑎  in  𝑄: 

**[ARRAY-ASSIGN]** 

⊢  {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼])}  𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **The rule for writing: [ARRAY-ASSIGN]** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

We also require every array read in  𝐸  to be defined, as in [ARRAY-READ]: 

**[ARRAY-ASSIGN]** 

⊢  {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽] ∈ 𝐸𝑑𝑒𝑓(𝑏[𝐽])}  𝑎[𝐼] ≔ 𝐸  {𝑄} 

- The rule now handles aliasing: every occurrence of  𝑎  in  𝑄  refers to the updated array, and the select–store axioms give the two cases  𝐽 = 𝐼  and  𝐽 ≠ 𝐼. 

- 𝑑𝑒𝑓(𝑎[𝐼])  requires the write to be defined, and the conjunction adds the conditions of [ARRAY-READ] for the reads in  𝐸. 

## **Back to the counterexample · Step 1 — substitution** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Substitute** 

2 · Select–store 3 · Definedness 

{ ? } a[i] **:= 1** ; { a[j] = **0** } 𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

We apply [ARRAY-ASSIGN] to the triple of the counterexample. First we substitute the updated array for  𝑎  in  𝑄: 



<!-- Start of picture text -->
𝑄[𝑎 ← 𝑎[𝑖 ↦ 1]]<br><!-- End of picture text -->

𝐼 = 𝑖  and  𝐸 = 1, so the updated array is  𝑎[𝑖 ↦ 1] 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Back to the counterexample · Step 1 — substitution** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Substitute** 

2 · Select–store 3 · Definedness 

{ ? } a[i] **:= 1** ; { a[j] = **0** } 𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

We apply [ARRAY-ASSIGN] to the triple of the counterexample. First we substitute the updated array for  𝑎  in  𝑄: 

(𝑎[𝑗] = 0)[𝑎 ← 𝑎[𝑖 ↦ 1]] 

We write  𝑄  explicitly 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Back to the counterexample · Step 1 — substitution** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Substitute** 

2 · Select–store 3 · Definedness 

{ ? } a[i] **:= 1** ; { a[j] = **0** } 

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 

𝐸:  1 

We apply [ARRAY-ASSIGN] to the triple of the counterexample. First we substitute the updated array for  𝑎  in  𝑄: 

𝑎[𝑖 ↦ 1][𝑗] = 0 

Every  𝑎  in  𝑄  is replaced by the updated array  𝑎[𝑖 ↦ 1] 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

_The naive rule left_ 𝑎[𝑗] = 0 _unchanged. Now the read of_ 𝑎[𝑗] _refers to the array after the write._ 

## **Back to the counterexample · Step 2 — select–store** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 3 · Definedness 



<!-- Start of picture text -->
{ ? }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 

𝐸:  1 

The read  𝑎[𝑖 ↦ 1][𝑗]  has the form  𝑎[𝐼 ↦ 𝐸][𝐽]  with  𝐼 = 𝑖,  𝐸 = 1  and  𝐽 = 𝑗. 

𝑎[𝑖 ↦ 1][𝑗] = 0 

We do not know whether  𝑗 = 𝑖, so we use both axioms 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Back to the counterexample · Step 2 — select–store** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 

3 · Definedness 



<!-- Start of picture text -->
{ ? }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

We do not know whether  𝑗 = 𝑖, so we use both select–store axioms, one for each case: 

(𝑗 = 𝑖 ∧ 1 = 0) ∨ (𝑗 ≠ 𝑖 ∧ 𝑎[𝑗] = 0) 

Case  𝐽 = 𝐼  gives  𝐸 = 1;   case  𝐽 ≠ 𝐼  gives  𝑎[𝐽] = 𝑎[𝑗] 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Back to the counterexample · Step 2 — select–store** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 

3 · Definedness 



<!-- Start of picture text -->
{ ? }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

We do not know whether  𝑗 = 𝑖, so we use both select–store axioms, one for each case: 

(𝑗 = 𝑖 ∧ 𝑓𝑎𝑙𝑠𝑒) ∨ (𝑗 ≠ 𝑖 ∧ 𝑎[𝑗] = 0) 

1 = 0  is false 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Back to the counterexample · Step 2 — select–store** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 

3 · Definedness 



<!-- Start of picture text -->
{ ? }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

We do not know whether  𝑗 = 𝑖, so we use both select–store axioms, one for each case: 



<!-- Start of picture text -->
𝑗 ≠ 𝑖 ∧ 𝑎[𝑗] = 0<br><!-- End of picture text -->

𝐴 ∧ 𝑓𝑎𝑙𝑠𝑒 ≡ 𝑓𝑎𝑙𝑠𝑒,  and  𝑓𝑎𝑙𝑠𝑒 ∨ 𝐵 ≡ 𝐵 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 



<!-- Start of picture text -->
𝑄[𝑎 ← 𝑎[𝑖 ↦ 1]] ⟺ 𝑗 ≠ 𝑖 ∧ 𝑎[𝑗] = 0<br><!-- End of picture text -->

## **Back to the counterexample · Step 3 — definedness** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store **3 · Definedness** 

{ j ≠ i  a[j] = ∧ **0** ∧ def(a[i]) } a[i] **:= 1** ; { a[j] = **0** } 

The write is  𝑎[𝑖], and  𝐸 = 1  contains no array read, so we add only  𝑑𝑒𝑓(𝑎[𝑖]): 

{𝑗 ≠ 𝑖 ∧ 𝑎[𝑗] = 0 ∧ 𝑑𝑒𝑓(𝑎[𝑖])}  𝑎[𝑖] ≔ 1  {𝑎[𝑗] = 0} 

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 

- **✓ the rule now requires  j ≠ i** 

𝐸:  1 

This is exactly the condition that excludes the counterexample, where  𝑖 = 𝑗 = 1. 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **The naive rule and [ARRAY-ASSIGN] side by side** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

### **Naive approach:** 

{𝑎[𝑗] = 0 ∧ 𝑑𝑒𝑓(𝑎[𝑖])}  𝑎[𝑖] ≔ 1  {𝑎[𝑗] = 0} 

**Correct rule, [ARRAY-ASSIGN]:** 

{𝑗 ≠ 𝑖 ∧ 𝑎[𝑗] = 0 ∧ 𝑑𝑒𝑓(𝑎[𝑖])}  𝑎[𝑖] ≔ 1  {𝑎[𝑗] = 0} 

_With_ 𝑎 = [4, 0, 9] _and_ 𝑖 = 𝑗 = 1 _, the correct precondition is false, so the rule makes no promise about this execution._ 

