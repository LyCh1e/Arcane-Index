# ICT3112 - 8 - Reasoning about Arrays - 3a

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Reasoning about Arrays** . if ie | **Exercise 1 Dr. David Sanan** ay Be = 

## **Reminder: [ARRAY-ASSIGN] and the axioms** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

The rule for writing into an array: 

**[ARRAY-ASSIGN]** 

   - ⊢  {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽] ∈ 𝐸𝑑𝑒𝑓(𝑏[𝐽])}  𝑎[𝐼] ≔ 𝐸  {𝑄} 

- 𝑑𝑒𝑓(𝑎[𝐼])  requires the write to be defined, and the conjunction adds the conditions of [ARRAY-READ] for the reads in  𝐸. 

The two **select–store axioms** give the value read from an updated array: 

𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸         if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]     if  𝐽 ≠ 𝐼 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

# **Part 3 · Exercises** 

**Applying the rules step by step** 

## **Exercise 1 — increment a cell** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store 

3 · Definedness 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

Find the precondition that [ARRAY-ASSIGN] gives for: 

{  ?  }  𝑎[𝑖] ≔ 𝑎[𝑖] + 1  {𝑎[𝑖] > 0} 

𝑄:  𝑎[𝑖] > 0 

𝐼:  𝑖 

𝐸:  𝑎[𝑖] + 1 

- Step 1: substitute the updated array for  𝑎  in  𝑄. 

- Step 2: simplify with the select–store axioms. 

- Step 3: add the definedness conditions. 

### **[ARRAY-ASSIGN]** 

**Try it yourself before looking at the next slide.** 

{𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Exercise 1 · Step 1 — substitution** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

𝑄:  𝑎[𝑖] > 0 𝐼:  𝑖 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 𝑎[𝑖] + 1. 

𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

The rule substitutes the updated array  𝑎[𝐼 ↦ 𝐸]  for  𝑎  in  𝑄 

𝐸:  𝑎[𝑖] + 1 

### **[ARRAY-ASSIGN]** 

{𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Exercise 1 · Step 1 — substitution** 

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 𝑎[𝑖] + 1. 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

𝑄[𝑎 ← 𝑎[𝑖 ↦ 𝑎[𝑖] + 1]] 

𝑄:  𝑎[𝑖] > 0 𝐼:  𝑖 

We replace  𝐼  by  𝑖  and  𝐸  by  𝑎[𝑖] + 1 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

𝐸:  𝑎[𝑖] + 1 

### **[ARRAY-ASSIGN]** 

{𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Exercise 1 · Step 1 — substitution** 

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 𝑎[𝑖] + 1. 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

(𝑎[𝑖] > 0)[𝑎 ← 𝑎[𝑖 ↦ 𝑎[𝑖] + 1]] 

𝑄:  𝑎[𝑖] > 0 𝐼:  𝑖 

We write  𝑄  explicitly 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

𝐸:  𝑎[𝑖] + 1 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Exercise 1 · Step 1 — substitution** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

𝑄:  𝑎[𝑖] > 0 𝐼:  𝑖 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 𝑎[𝑖] + 1. 

𝑎[𝑖 ↦ 𝑎[𝑖] + 1][𝑖] > 0 

The array  𝑎  in  𝑄  is replaced by the updated array 

𝐸:  𝑎[𝑖] + 1 

- Only the  𝑎  of  𝑄  is replaced. The  𝑎[𝑖] + 1  inside the update is not substituted, since it is evaluated in the state before the assignment. 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

- ∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Exercise 1 · Step 2 — select–store** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute 

**2 · Select–store** 

3 · Definedness 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

𝑄:  𝑎[𝑖] > 0 𝐼:  𝑖 

𝐸:  𝑎[𝑖] + 1 

We read the updated array at the same position where we wrote:  𝐽 = 𝐼 = 𝑖. The first select–store axiom applies, so no case split is needed. 

𝑎[𝑖 ↦ 𝑎[𝑖] + 1][𝑖] > 0 

𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸  when  𝐽 = 𝐼 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 1 · Step 2 — select–store** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 

3 · Definedness 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

𝑄:  𝑎[𝑖] > 0 𝐼:  𝑖 

𝐸:  𝑎[𝑖] + 1 

We read the updated array at the same position where we wrote:  𝐽 = 𝐼 = 𝑖. The first select–store axiom applies, so no case split is needed. 

𝑎[𝑖] + 1 > 0 

The read gives back  𝐸 = 𝑎[𝑖] + 1, the value written 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

𝑄[𝑎 ← 𝑎[𝑖 ↦ 𝑎[𝑖] + 1]] ⟺ 𝑎[𝑖] + 1 > 0 

## **Exercise 1 · Step 3 — definedness** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store 

**3 · Definedness** 

{ ? } a[i] **:=** a[i] + **1** ; { a[i] > **0** } 

The write changes  𝑎[𝑖], and the only read in  𝐸  is also  𝑎[𝑖]. Since it is the same cell, one condition covers both: 

𝑑𝑒𝑓(𝑎[𝑖]) ∧ 𝑑𝑒𝑓(𝑎[𝑖]) ⟺ 0 ≤ 𝑖 < 𝑠𝑖𝑧𝑒𝑜𝑓(𝑎) 

𝑄:  𝑎[𝑖] > 0 

{𝑎[𝑖] + 1 > 0 ∧ 0 ≤ 𝑖 < 𝑠𝑖𝑧𝑒𝑜𝑓(𝑎)}  𝑎[𝑖] ≔ 𝑎[𝑖] + 1  {𝑎[𝑖] > 0} 

𝐼:  𝑖 

𝐸:  𝑎[𝑖] + 1 

- **✓ For integers,** 𝑎[𝑖] + 1 > 0 **is the same as** 𝑎[𝑖] ≥ 0 **, so the cell must not be negative before the write.** 

### **[ARRAY-ASSIGN]** 

{𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

We can check it with  𝑎 = [4, 0, 9]  and  𝑖 = 1:  𝑎[1] = 0 ≥ 0, and after the write  𝑎[1] = 1 > 0.  ✓ 

