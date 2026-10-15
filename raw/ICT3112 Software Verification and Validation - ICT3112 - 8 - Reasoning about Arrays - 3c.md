# ICT3112 - 8 - Reasoning about Arrays - 3c

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Reasoning about Arrays** . if ie | **Exercise 2, Part 2 Dr. David Sanan** ay Be = 

## **Exercise 2 so far: steps 1 and 2** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute 2 · Select–store 3 · Definedness 

{  ?  }  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]} 

Step 1 · the updated array replaces 𝑎 in 𝑄 

𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑖] = 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑗] 

Step 2 · the read at position 𝑖 

2⋅𝑎[𝑗] = 𝑎[𝑖 ↦ 2⋅𝑎[𝑗]][𝑗] 

Step 2 · the read at position 𝑗 

(𝑗 = 𝑖 ∧ 2⋅𝑎[𝑗] = 2⋅𝑎[𝑗]) ∨ (𝑗 ≠ 𝑖 ∧ 2⋅𝑎[𝑗] = 𝑎[𝑗]) 

Result of steps 1 and 2 

𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

## **Exercise 2 · Testing the precondition on values** 



<!-- Start of picture text -->
1 · Substitute 2 · Select–store 3 · Definedness<br>{𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0}  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]}<br>We take   𝑎 = [4, 0, 9]   and try three choices of   𝑖   and   𝑗 .<br>Case 1:    𝑖 = 0 ,    𝑗 = 0<br>𝑎 4 0 9<br>0 1 2<br>𝑖𝑗<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>a[i]  := 2  * a[j];<br>{ a[i] = a[j] }<br>𝑄:  𝑎[𝑖] = 𝑎[𝑗]<br>𝐼:  𝑖<br>𝐸:  2⋅𝑎[𝑗]<br><!-- End of picture text -->

Precondition:  𝑗 = 𝑖, so the precondition holds  ✓ We execute  𝑎[0] ≔ 2⋅𝑎[0] = 8. 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

## **Exercise 2 · Testing the precondition on values** 



<!-- Start of picture text -->
1 · Substitute 2 · Select–store 3 · Definedness<br>{𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0}  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]}<br>We take   𝑎 = [4, 0, 9]   and try three choices of   𝑖   and   𝑗 .<br>Case 1:    𝑖 = 0 ,    𝑗 = 0<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>a[i]  := 2  * a[j];<br>We take   𝑎 = [4, 0, 9]<br>{ a[i] = a[j] }<br>Case 1:    𝑖 = 0 ,    𝑗 = 0<br>𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝑎 8 0 9<br>𝐼:  𝑖 0 1 2<br>𝐸:  2⋅𝑎[𝑗] 𝑖𝑗<br><!-- End of picture text -->

Precondition:  𝑗 = 𝑖, so the precondition holds  ✓ We execute  𝑎[0] ≔ 2⋅𝑎[0] = 8. 

**Postcondition:** 𝑎[𝑖] = 𝑎[𝑗] = 8 **, since both name the same cell  ✓** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

## **Exercise 2 · Testing the precondition on values** 



<!-- Start of picture text -->
1 · Substitute 2 · Select–store 3 · Definedness<br>{𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0}  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]}<br>We take   𝑎 = [4, 0, 9]   and try three choices of   𝑖   and   𝑗 .<br>Case 2:    𝑖 = 0 ,    𝑗 = 1<br>𝑎 4 0 9<br>0 1 2<br>𝑖 𝑗<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>a[i]  := 2  * a[j];<br>{ a[i] = a[j] }<br>𝑄:  𝑎[𝑖] = 𝑎[𝑗]<br>𝐼:  𝑖<br>𝐸:  2⋅𝑎[𝑗]<br><!-- End of picture text -->

Precondition:  𝑗 ≠ 𝑖, but  𝑎[1] = 0, so the precondition holds  ✓ We execute  𝑎[0] ≔ 2⋅𝑎[1] = 0. 

## **Exercise 2 · Testing the precondition on values** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>a[i]  := 2  * a[j];<br>{ a[i] = a[j] }<br>𝑄:  𝑎[𝑖] = 𝑎[𝑗]<br>𝐼:  𝑖<br>𝐸:  2⋅𝑎[𝑗]<br><!-- End of picture text -->

1 · Substitute **2 · Select–store** 3 · Definedness {𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0}  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]} _We take_ 𝑎 = [4, 0, 9] _and try three choices of_ 𝑖 _and_ 𝑗 _._ **Case 2:** 𝑖 = 0 **,** 𝑗 = 1 



<!-- Start of picture text -->
𝑎 0 0 9<br>0 1 2<br>𝑖 𝑗<br><!-- End of picture text -->

Precondition:  𝑗 ≠ 𝑖, but  𝑎[1] = 0, so the precondition holds  ✓ We execute  𝑎[0] ≔ 2⋅𝑎[1] = 0. 

**Postcondition:** 𝑎[𝑖] = 𝑎[0] = 0 **and** 𝑎[𝑗] = 𝑎[1] = 0 **✓** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

## **Exercise 2 · Testing the precondition on values** 



<!-- Start of picture text -->
1 · Substitute 2 · Select–store 3 · Definedness<br>{𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0}  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]}<br>We take   𝑎 = [4, 0, 9]   and try three choices of   𝑖   and   𝑗 .<br>Case 3:    𝑖 = 0 ,    𝑗 = 2<br>𝑎 4 0 9<br>0 1 2<br>𝑖 𝑗<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>a[i]  := 2  * a[j];<br>{ a[i] = a[j] }<br>𝑄:  𝑎[𝑖] = 𝑎[𝑗]<br>𝐼:  𝑖<br>𝐸:  2⋅𝑎[𝑗]<br><!-- End of picture text -->

Precondition:  𝑗 ≠ 𝑖  and  𝑎[2] = 9 ≠ 0, so the precondition is false  ✗ We execute  𝑎[0] ≔ 2⋅𝑎[2] = 18. 

## **Exercise 2 · Testing the precondition on values** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute 

**2 · Select–store** 3 · Definedness {𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0}  𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]} 



<!-- Start of picture text -->
{ ? }<br>a[i]  := 2  * a[j];<br>{ a[i] = a[j] }<br><!-- End of picture text -->

_We take_ 𝑎 = [4, 0, 9] _and try three choices of_ 𝑖 _and_ 𝑗 _._ 

**Case 3:** 𝑖 = 0 **,** 𝑗 = 2 



<!-- Start of picture text -->
𝑄:  𝑎[𝑖] = 𝑎[𝑗]<br>𝐼:  𝑖<br>𝐸:  2⋅𝑎[𝑗]<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑎 18 0 9<br>0 1 2<br>𝑖 𝑗<br><!-- End of picture text -->

Precondition:  𝑗 ≠ 𝑖  and  𝑎[2] = 9 ≠ 0, so the precondition is false  ✗ We execute  𝑎[0] ≔ 2⋅𝑎[2] = 18. 

**Postcondition:** 𝑎[𝑖] = 18 **but** 𝑎[𝑗] = 9 **, so the postcondition fails  ✗** _This is expected: the precondition is false, so the rule makes no promise about this execution._ 

# **Exercise 2 · Step 3 — definedness** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store 

**3 · Definedness** 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

𝐸:  2⋅𝑎[𝑗] 

For definedness we need two conjuncts: the write  𝑎[𝑖]  must be defined, and every read in  𝐸  (here  𝑎[𝑗]) must be defined. 

{𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0} 

The result of steps 1 and 2 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **Exercise 2 · Step 3 — definedness** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store 

**3 · Definedness** 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

𝐸:  2⋅𝑎[𝑗] 

For definedness we need two conjuncts: the write  𝑎[𝑖]  must be defined, and every read in  𝐸  (here  𝑎[𝑗]) must be defined. 

{(𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0) ∧ 𝑑𝑒𝑓(𝑎[𝑖])} 

1.  The write  𝑎[𝑖]  must be defined 

### **[ARRAY-ASSIGN]** 

{𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] 

∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **Exercise 2 · Step 3 — definedness** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Substitute 

2 · Select–store 

**3 · Definedness** 

{ ? } a[i] **:= 2** * a[j]; { a[i] = a[j] } 

𝑄:  𝑎[𝑖] = 𝑎[𝑗] 𝐼:  𝑖 

𝐸:  2⋅𝑎[𝑗] 

For definedness we need two conjuncts: the write  𝑎[𝑖]  must be defined, and every read in  𝐸  (here  𝑎[𝑗]) must be defined. 

{(𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0) ∧ 𝑑𝑒𝑓(𝑎[𝑖]) ∧ 𝑑𝑒𝑓(𝑎[𝑗])} 

2.  The read  𝑎[𝑗]  in  𝐸  must be defined 

**[ARRAY-ASSIGN]** {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽]∈𝐸𝑑𝑒𝑓(𝑏[𝐽])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

_The parentheses matter: the definedness conditions must hold in both cases of the disjunction._ 

{(𝑗 = 𝑖 ∨ 𝑎[𝑗] = 0) ∧ 0 ≤ 𝑖 < 𝑠𝑖𝑧𝑒𝑜𝑓(𝑎) ∧ 0 ≤ 𝑗 < 𝑠𝑖𝑧𝑒𝑜𝑓(𝑎)} 𝑎[𝑖] ≔ 2⋅𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]} 

# **Summary — the two array rules** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**[ARRAY-READ]** 

⊢  {𝑄[𝑥 ← 𝐸] ∧ ⋀𝑎[𝐼] ∈ 𝐸𝑑𝑒𝑓(𝑎[𝐼])}  𝑥 ≔ 𝐸  {𝑄} 

**[ARRAY-ASSIGN]** 

   - ⊢  {𝑄[𝑎 ← 𝑎[𝐼 ↦ 𝐸]] ∧ 𝑑𝑒𝑓(𝑎[𝐼]) ∧ ⋀𝑏[𝐽] ∈ 𝐸𝑑𝑒𝑓(𝑏[𝐽])}  𝑎[𝐼] ≔ 𝐸  {𝑄} 

- Reads: we substitute as usual, and every read must be defined (its index must be within the bounds). 

- Writes: we substitute the whole updated array, and then the select–store axioms give the cases needed for aliasing. 

# **Exercises for home and the next session** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

Compute the precondition given by [ARRAY-ASSIGN] for each triple (be careful with aliasing): 1)      {  ?  }  𝑎[𝑖] ≔ 𝑎[𝑗]  {𝑎[𝑖] = 𝑎[𝑗]} 2)      {  ?  }  𝑎[𝑖] ≔ 0  {𝑎[𝑖] < 𝑎[𝑗]} 3)      {  ?  }  𝑎[𝑎[𝑖]] ≔ 1  {𝑎[𝑎[𝑖]] = 1}     (tricky!) 

•  Next session: arrays and loops. We will see loop invariants that describe a whole part of an array, for example when we initialise an array or compute its sum. 

