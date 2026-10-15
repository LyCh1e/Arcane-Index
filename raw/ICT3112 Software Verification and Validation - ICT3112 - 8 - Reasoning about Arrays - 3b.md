# ICT3112 - 8 - Reasoning about Arrays - 3b

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Reasoning about Arrays** . if ie | **Exercise 2, Part 1 Dr. David Sanan** ay Be = 

# **Reminder: three steps, rule and axioms** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store 3 · Definedness 

The rule for writing into an array: 

**[ARRAY-ASSIGN]** 

   - ⊢  {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽] ∈ 𝐸𝑑𝑒𝑓(𝑏[𝐽])}  𝑎[𝐼] ≔ 𝐸  {𝑄} 

- 𝑑𝑒𝑓(𝑎[𝐼])  requires the write to be defined, and the conjunction adds the conditions of [ARRAY-READ] for the reads in  𝐸. 

The two **select–store axioms** give the value read from an updated array: 

𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸         if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]     if  𝐽 ≠ 𝐼 

## **Exercise 2 — write at position i, read at position j** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store 3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

Find the precondition that [ARRAY-ASSIGN] gives for: 

{  ?  }  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]} 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

𝐸:  2⋅𝑎[𝑗] 

- We follow the same three steps as before, but now  𝑄  reads the array at two positions,  𝑖  and  𝑗. 

- This time the select–store axioms will give us a real case analysis. 

### **[ARRAY-ASSIGN]** 

**Try it yourself before looking at the next slide.** 

- {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **Exercise 2 · Step 1 — substitution** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 2⋅𝑎[𝑗]. 

𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

The rule substitutes the updated array  𝑎[𝐼 ↦ 𝐸]  for  𝑎  in  𝑄 

𝐸:  2⋅𝑎[𝑗] 

### **[ARRAY-ASSIGN]** 

{𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **Exercise 2 · Step 1 — substitution** 

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 2⋅𝑎[𝑗]. 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄[𝑎 ← 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]]] 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

We replace  𝐼  by  𝑖  and  𝐸  by  2⋅𝑎[𝑗] 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

𝐸:  2⋅𝑎[𝑗] 

### **[ARRAY-ASSIGN]** 

{𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **Exercise 2 · Step 1 — substitution** 

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 2⋅𝑎[𝑗]. 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

(𝑎[𝑖] = 𝑎[𝑗])[𝑎 ← 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]]] 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

We write  𝑄  explicitly 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

𝐸:  2⋅𝑎[𝑗] 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **Exercise 2 · Step 1 — substitution** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1 · Substitute** 

2 · Select–store 

3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

We match the statement with the rule:  𝐼 = 𝑖  and  𝐸 = 2⋅𝑎[𝑗]. 

𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑖] = 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑗] 

Both occurrences of  𝑎  in  𝑄  now refer to the updated array 

𝐸:  2⋅𝑎[𝑗] 

- This is what the naive rule missed: it would only have rewritten  𝑎[𝑖], and it would have left  𝑎[𝑗]  unchanged. 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

- ∧ 𝑑𝑒𝑓(𝑎[𝐼]) 

∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

Left read: it reads position  𝑖, which is the cell we wrote  (𝐽 = 𝐼). 

𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑖] = 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑗] 

𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸  when  𝐽 = 𝐼 

𝐸:  2⋅𝑎[𝑗] 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 𝐸:  2⋅𝑎[𝑗] 

Left read: it reads position  𝑖, which is the cell we wrote  (𝐽 = 𝐼). 

2⋅𝑎[𝑗] = 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑗] 

It simplifies to  𝐸 = 2⋅𝑎[𝑗], the value assigned in the statement 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 

3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

𝐸:  2⋅𝑎[𝑗] 

Right read: position  𝑗  can be the written cell  𝑖  or any other cell. Since we cannot tell, we use both cases of the axioms. 

2⋅𝑎[𝑗] = 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑗] 

𝐽 = 𝑗  may or may not be equal to  𝐼 = 𝑖 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 𝐸:  2⋅𝑎[𝑗] 

Right read: position  𝑗  can be the written cell  𝑖  or any other cell. Since we cannot tell, we use both cases of the axioms. 

(𝑗 = 𝑖 ∧ 2⋅𝑎[𝑗] = 2⋅𝑎[𝑗]) ∨ (𝑗 ≠ 𝑖 ∧ 2⋅𝑎[𝑗] = 𝑎[𝑗]) 

Case  𝑗 = 𝑖: the read gives  𝐸 = 2⋅𝑎[𝑗].   Case  𝑗 ≠ 𝑖: it gives  𝑎[𝑗] 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 𝐸:  2⋅𝑎[𝑗] 

Right read: position  𝑗  can be the written cell  𝑖  or any other cell. Since we cannot tell, we use both cases of the axioms. 

(𝑗 = 𝑖 ∧ 𝑡𝑟𝑢𝑒) ∨ (𝑗 ≠ 𝑖 ∧ 2⋅𝑎[𝑗] = 𝑎[𝑗]) 

2⋅𝑎[𝑗] = 2⋅𝑎[𝑗]  is always true 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 

3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 𝐸:  2⋅𝑎[𝑗] 

Right read: position  𝑗  can be the written cell  𝑖  or any other cell. Since we cannot tell, we use both cases of the axioms. 

𝑗 = 𝑖 ∨ (𝑗 ≠ 𝑖 ∧ 2⋅𝑎[𝑗] = 𝑎[𝑗]) 

𝐴 ∧ 𝑡𝑟𝑢𝑒 ≡ 𝐴 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 𝐸:  2⋅𝑎[𝑗] 

Right read: position  𝑗  can be the written cell  𝑖  or any other cell. Since we cannot tell, we use both cases of the axioms. 

𝑗 = 𝑖 ∨ (𝑗 ≠ 𝑖 ∧ 𝑎[𝑗] = 0) 

For integers,  2⋅𝑥 = 𝑥 ⟺ 𝑥 = 0 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

## **Exercise 2 · Step 2 — select–store on each read** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 

3 · Definedness 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 𝐸:  2⋅𝑎[𝑗] 

Right read: position  𝑗  can be the written cell  𝑖  or any other cell. Since we cannot tell, we use both cases of the axioms. 



<!-- Start of picture text -->
𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0<br><!-- End of picture text -->

𝐴 ∨ (¬𝐴 ∧ 𝐵) ≡ 𝐴 ∨ 𝐵,  and  𝑗 ≠ 𝑖  is  ¬(𝑗 = 𝑖) 

**Select–store axioms** 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝐸   if  𝐽 = 𝐼 𝑎[𝐼 ↦ 𝐸][𝐽] = 𝑎[𝐽]   if  𝐽 ≠ 𝐼 

𝑄[𝑎 ← 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]]] ⟺ 𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0 

