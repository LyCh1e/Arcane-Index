# ICT3112 - 7 - Recepy for Loop Invariants - 0b

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **Recipe, Steps 3 to 5 Dr. David Sanan** ay Be = 

# **Where we stopped: steps 1 to 3 for the sum** 



<!-- Start of picture text -->
1 · Q<br><!-- End of picture text -->



<!-- Start of picture text -->
2 · Trace 3 · Generalise 4 · Bounds<br><!-- End of picture text -->



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->



<!-- Start of picture text -->
{ n ≥  0 }<br>i  := 0 ;  s  := 0 ;<br>while (i < n) {<br>    i  :=  i +  1 ;<br>    s  :=  s + i;<br>}<br>{ s = n(n+ 1 )/ 2 }<br><!-- End of picture text -->



<!-- Start of picture text -->
At the loop head 𝑖 𝑠<br>before pass 1 0 0<br>before pass 2 1 1<br>before pass 3 2 3<br>before pass 4 3 6<br>𝑠 = 𝑛(𝑛 + 1)/2      ⟶      𝑠 = 𝑖(𝑖 + 1)/2<br><!-- End of picture text -->

(replace  𝑛  by  𝑖) 

# **Step 3: four ways to build a candidate** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 2 · Trace **3 · Generalise** 4 · Bounds 5 · Check 

Replacing a constant by a progress variable is the most common way to build a candidate, but it is not the only one: 

**Way When to use it Example Replace a constant by a** 𝑄  describes a result over the whole range, and The sum:  𝑠 = 𝑛(𝑛 + 1)/2  becomes **progress variable** the loop builds it one step at a time. 𝑠 = 𝑖(𝑖 + 1)/2 Part of  𝑄  is already given by the negated guard **Drop a conjunct** Searching for a value at the exit. The loop works on the range from both ends at the **Use two progress variables** Reversing an array in place same time. **Add the fact that preservation** A candidate fails preservation, since the body uses The Fibonacci numbers (Example 3) **needs** a variable that the candidate says nothing about. 

These four ways cover almost every loop in this course. They do not cover every loop: some loops need an idea that none of them gives. 

# **Building a candidate by dropping a conjunct** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace **3 · Generalise** 

4 · Bounds 

5 · Check 

{ n = length(A)  i = ∧ **0** } while (i < n && A[i] ≠ v) i **:=** i + **1** ; 

{ (A[k] ≠ v  for **0** ≤ k < i) 

∧ (i = n  A[i] = v) ∨ } 

𝑄  says that no cell before  𝑖  contains  𝑣, and that the loop stopped at the end or at a cell that contains  𝑣: 

𝑄:    (𝐴[𝑘] ≠ 𝑣 for 0 ≤ 𝑘 < 𝑖)  ∧  (𝑖 = 𝑛 ∨ 𝐴[𝑖] = 𝑣) 

The guard is  𝑖 < 𝑛 ∧ 𝐴[𝑖] ≠ 𝑣, so at the exit  ¬𝐵  is  𝑖 ≥ 𝑛 ∨ 𝐴[𝑖] = 𝑣. With the bound  𝑖 ≤ 𝑛, this is exactly the second conjunct of  𝑄. 

Since  𝐼 ∧ ¬𝐵  must give  𝑄, the invariant only needs the part of  𝑄  that  ¬𝐵 does not give. We drop the second conjunct and add the bounds: 𝐼 = (𝐴[𝑘] ≠ 𝑣 for 0 ≤ 𝑘 < 𝑖) ∧ (0 ≤ 𝑖 ≤ 𝑛) Use this way when part of  𝑄  looks like the negated guard. Eee 

## **Building a candidate with two progress variables** 



<!-- Start of picture text -->
1 · Q<br><!-- End of picture text -->

2 · Trace **3 · Generalise** 

4 · Bounds 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

5 · Check 

{ n = length(A)  A = A₀∧ ∧ l = **0** r = n − ∧ **1** } while (l < r) { swap(A, l, r); l **:=** l + **1** ; r **:=** r − **1** ; } 

{ A[k] = A₀[n− **1** −k] for **0** ≤ k < n } 

𝑄:  𝐴[𝑘] = 𝐴0[𝑛 − 1 − 𝑘]  for  0 ≤ 𝑘 < 𝑛. The loop does not go from left to right: in each pass it swaps one cell at each end. 

𝑙 

### 𝑟 



<!-- Start of picture text -->
swapped not reached swapped<br><!-- End of picture text -->

So the one range  0 ≤ 𝑘 < 𝑛  becomes the two parts done so far, one for each progress variable: 

𝐴[𝑘] = 𝐴0[𝑛 − 1 − 𝑘]   for  0 ≤ 𝑘 < 𝑙  and for  𝑟 < 𝑘 < 𝑛 

Two progress variables replace one quantity, so we record how they are linked, and what is still untouched:   𝑙 + 𝑟 = 𝑛 − 1   and   𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟. 

Po 

Use this way when the loop works on the range from both ends at the same time. Po essi—i‘is_CS 

# **Adding the fact that preservation needs** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

**3 · Generalise** 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } a **:= 0** ;  b **:= 1** ;  i **:= 0** ; while (i < n) { t **:=** a + b; a **:=** b; b **:=** t; i **:=** i + **1** ; } { a = F(n) } 

Replacing  𝑛  by  𝑖  gives a first candidate: 

𝑎 = 𝐹(𝑖) ∧ 0 ≤ 𝑖 ≤ 𝑛 

Computing backwards through the body, preservation needs  𝑏 = 𝐹(𝑖 + 1)  before the body. The candidate says nothing about  𝑏, so preservation fails. 

A state that shows the failure, with  𝑛 ≥ 1:   𝑖 = 0,  𝑎 = 0,  𝑏 = 7. It satisfies the candidate, but after one pass  𝑎 = 7, and  𝐹(1) = 1. 

The fact that rules this state out is exactly what the body needs. We add it: 

𝑎 = 𝐹(𝑖) ∧ 𝑏 = 𝐹(𝑖 + 1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

Use this way when preservation fails. Example 3 goes through this case in full. 

# **Step 4: add the bounds** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

**4 · Bounds** 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } { s = n(n+ **1** )/ **2** } 

When the loop stops, the guard only tells us  𝑖 ≥ 𝑛. On its own, that gives nothing: 𝑖  could be  𝑛,  𝑛 + 1  or  1000. 

¬𝐵:  𝑖 ≥ 𝑛    ∧    𝑖 ≤ 𝑛    ⇒    𝑖 = 𝑛 

𝐼:    𝑠 = 𝑖(𝑖 + 1)/2 ∧ 0 ≤ 𝑖 ≤ 𝑛 

The bound  𝑖 ≤ 𝑛  turns “the loop stopped” into “𝑖  reached  𝑛”. With  𝑖 = 𝑛, the invariant becomes  𝑄. 

# **Step 5: check the candidate** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } 

{ s = n(n+ **1** )/ **2** } 

Steps 1 to 4 produce a **candidate** . Only the checks make it an invariant: 

- **Establishment** : is it true before the first pass? 

- **Preservation** : does one pass of the body keep it true? 

- **Postcondition at exit** : together with  ¬𝐵, does it give  𝑄? 

**Propose Check Refine** Q with n replaced by i, plus one of the checks fails? make it stronger or weaker the bounds 

When a check fails, write down a state that shows the failure. The fact that rules this state out is what the candidate is missing. 

## **The recipe, the template and the picture together** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

The template and the picture of the data are not separate methods. They are tools that we use inside the recipe: 

**1 · Q 2 · Trace 3 · Generalise 4 · Bounds 5 · Check** Name the progress Record the values Draw the data to Fill the bounds slot Establishment, variable and the of the variables at find its regions. Go of the template, so preservation, result variable. the loop head. through the four that the exit gives postcondition at slots of the the final value of exit. A failed check template. Choose the progress gives a state that one of the four variable. shows what is ways to build the missing. candidate. 

Most of the thinking happens in step 3. The other steps prepare it and check it. 

# **A practical recipe** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1** Write the postcondition  𝑄, and identify the progress variable and the result variable. 

**2** Trace a few loop-head states, and find what the variables mean “so far”. 

Generalise  𝑄: replace the final value by the progress variable, or use one of the other ways to build a **3** candidate. 

**4** Add the bounds, and any missing facts. 

Check establishment, preservation and the postcondition at exit. If one fails, find a state that shows the **5** failure, and refine the candidate. 

**6** Finally, add a variant for termination. 

**Discovery is iterative:  propose  →  check  →  refine. It is normal that the first candidate does not work.** 

