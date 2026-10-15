# ICT3112 - 7 - Recepy for Loop Invariants - exercises

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **Exercises Dr. David Sanan** ay Be = 

# **Exercise 1 (guided): multiplication** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ b ≥ **0** } p **:= 0** ;  i **:= 0** ; while (i < b) { p **:=** p + a; i **:=** i + **1** ; } { p = a · b } 

𝑄:  𝑝 = 𝑎 ⋅ 𝑏. Here  𝑏  is the number of passes, and  𝑎  is the amount added in each pass, a constant of the problem. So we replace  𝑏  by  𝑖, and we keep  𝑎. 

𝐼:    𝑝 = 𝑎 ⋅ 𝑖 ∧ 0 ≤ 𝑖 ≤ 𝑏 𝑉 = 𝑏 − 𝑖 

**Establishment** :  0 = 𝑎 ⋅ 0, and  0 ≤ 0 ≤ 𝑏  since  𝑏 ≥ 0. **Preservation** :  𝑎 ⋅ (𝑖+1) = 𝑎 ⋅ 𝑖 + 𝑎, and  𝑖 < 𝑏  gives  𝑖 + 1 ≤ 𝑏. **Postcondition at exit** :  𝑖 ≥ 𝑏  and  𝑖 ≤ 𝑏  give  𝑖 = 𝑏, so  𝑝 = 𝑎 ⋅ 𝑏. 

# **Exercise 2: factorial** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  f **:= 1** ; while (i < n) { i **:=** i + **1** ; f **:=** f * i; } { f = n! } 

**Your task:** 

- Use the recipe to find the invariant  𝐼. 

- Check establishment and preservation. 

- Show that  𝑄  holds at the exit, and give a variant. 

Hint: look at the order of the two statements in the body. The variable  𝑖  is increased before it is used. 

_Pause the video, and come back when you have your answer._ 

# **Exercise 2: solution** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  f **:= 1** ; while (i < n) { i **:=** i + **1** ; f **:=** f * i; } { f = n! } 

𝑓 = 𝑛!    ⟶    𝑓 = 𝑖!, plus the bounds: 

𝐼:    𝑓 = 𝑖! ∧ 0 ≤ 𝑖 ≤ 𝑛 

**Establishment** :   1 = 0!, and  0 ≤ 0 ≤ 𝑛  since  𝑛 ≥ 0. **Preservation** :   the body needs  𝑓 ⋅ (𝑖+1) = (𝑖+1)!, and  (𝑖+1)! = 𝑖! ⋅ (𝑖+1). 

**Postcondition at exit** :   𝑖 ≥ 𝑛  and  𝑖 ≤ 𝑛  give  𝑖 = 𝑛, so  𝑓 = 𝑛!. 

**Variant** :   𝑉 = 𝑛 − 𝑖. 

If you wrote  𝑓 = (𝑖+1)!  or  𝑓 = (𝑖−1)!, check the trace: at the first loop head  𝑖 = 0 and  𝑓 = 1 = 0!. 

# **Exercise 3: sum of the first n odd numbers** 

**Your task:** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { s **:=** s + ( **2** *i + **1** ); i **:=** i + **1** ; } { s = n² } 

- Find the invariant by generalising the postcondition. 

- Give a variant. 

- Check establishment and preservation. 

A trace with a few rows will help you to convince yourself. 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

_Pause the video, and come back when you have your answer._ 

# **Exercise 3: solution** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { s **:=** s + ( **2** *i + **1** ); i **:=** i + **1** ; } { s = n² } 

𝐼:    𝑠 = 𝑖<sup>2</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 At the loop heads: 𝑖 = 0,  𝑠 = 0 𝑖 = 1,  𝑠 = 1 𝑖 = 2,  𝑠 = 4 𝑖 = 3,  𝑠 = 9 **Establishment** :   𝑠 = 0 = 0<sup>2</sup> , and  0 ≤ 0 ≤ 𝑛. **Preservation** :   the body needs  𝑠 + (2𝑖 + 1) = (𝑖+1)<sup>2</sup> , and  (𝑖+1)<sup>2</sup> = 𝑖<sup>2</sup> + 2𝑖 + 1. 

**Postcondition at exit** :   𝑖 = 𝑛, so  𝑠 = 𝑖<sup>2</sup> becomes  𝑠 = 𝑛<sup>2</sup> . **Variant** :   𝑉 = 𝑛 − 𝑖. 

# **Exercise 4: sum of an array** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ n = length(A) } i **:= 0** ;  s **:= 0** ; while (i < n) { s **:=** s + A[i]; i **:=** i + **1** ; } 

**Your task:** 

- Generalise the postcondition:  𝑠  is the sum of the first  𝑖  elements. 

- What are the bounds? 

- What is the variant? 

{ s = A[ **0** ] + … + A[n− **1** ] } 

_Pause the video, and come back when you have your answer._ 

# **Exercise 4: solution** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n = length(A) } i **:= 0** ;  s **:= 0** ; while (i < n) { s **:=** s + A[i]; i **:=** i + **1** ; } 

{ s = A[ **0** ] + … + A[n− **1** ] } 

We describe the part of the array that has already been processed, the visited part: 

𝐼:    𝑠 = 𝐴[0] + … + 𝐴[𝑖−1] ∧ 0 ≤ 𝑖 ≤ 𝑛 

- **Relation** :  𝑠  is the sum of  𝐴[0..𝑖−1]. When  𝑖 = 0  this is an empty sum, which 

- is 0. 

- **Bounds** :  0 ≤ 𝑖 ≤ 𝑛. **Variant** :  𝑛 − 𝑖. 

**Preservation** :  𝑠 + 𝐴[𝑖]  is the sum of  𝐴[0..𝑖], which is what the invariant says after  𝑖  becomes  𝑖 + 1. **Postcondition at exit** :  𝑖 = 𝑛, so  𝑠  is the sum of  𝐴[0..𝑛−1]. 

## **Exercise 5: find a state that breaks the candidate** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Each candidate below is wrong on purpose. For each one, say which check fails, and write down a concrete state that shows the failure. Then use the state to fix the candidate. 



<!-- Start of picture text -->
(a) (b) (c)<br>{ b ≥  0 } { n ≥  0 } { n ≥  0   s = ∧ 0   i = ∧ 0 }<br>p  := 0 ;  i  := 0 ; i  := 0 ;  s  := 0 ; while (i < n) {<br>while (i < b) { while (i < n) {     s  :=  s +  1 ;<br>    p  :=  p + a;     s  :=  s + ( 2 *i +  1 );     i  :=  i +  1 ;<br>    i  :=  i +  1 ;     i  :=  i +  1 ; }<br>} } { s = n }<br>{ p = a · b } { s = n² }<br>𝑝 = 𝑎 ⋅ 𝑖 𝑠 = 𝑛 2  ∧ 0 ≤ 𝑖 ≤ 𝑛 0 ≤ 𝑖 ≤ 𝑛 ∧ 0 ≤ 𝑠 ≤ 𝑛<br><!-- End of picture text -->

_Pause the video, and come back when you have your three states._ 

# **Exercise 5: solution** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Each candidate below is wrong on purpose. For each one, say which check fails, and write down a concrete state that shows the failure. Then use the state to fix the candidate. 

**(a)** 

**(b)** 

### **(c)** 

{ b ≥ **0** } p **:= 0** ;  i **:= 0** ; while (i < b) { p **:=** p + a; i **:=** i + **1** ; 

} 

{ p = a · b } 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { s **:=** s + ( **2** *i + **1** ); i **:=** i + **1** ; 

} 

{ s = n² } 

{ n ≥ **0** s = ∧ **0** i = ∧ **0** } while (i < n) { s **:=** s + **1** ; i **:=** i + **1** ; 

} 

{ s = n } 

𝑝 = 𝑎 ⋅ 𝑖 

𝑠 = 𝑛<sup>2</sup> ∧ 0 ≤ 𝑖 ≤ 𝑛 

0 ≤ 𝑖 ≤ 𝑛 ∧ 0 ≤ 𝑠 ≤ 𝑛 

#### Fails: **Postcondition at exit** 

Bad state:  𝑎 = 2, 𝑏 = 3, 𝑖 = 4, 𝑝 = 8. It satisfies  𝐼 ∧ ¬𝐵, but  𝑎 ⋅ 𝑏 = 6. **Fix:  add the bound** 0 ≤ 𝑖 ≤ 𝑏 

#### Fails: **Establishment** 

Bad state:  𝑛 = 2, 𝑖 = 0, 𝑠 = 0: the state right after the initialisation. The candidate rejects it, since  𝑛<sup>2</sup> = 4. **Fix:  weaken: replace** 𝑛 **by** 𝑖 

#### Fails: **Preservation** 

Bad state:  𝑛 = 3, 𝑖 = 0, 𝑠 = 3. It satisfies  𝐼 ∧ 𝐵, but after one pass  𝑠 = 4 > 𝑛. 

**Fix:  add the relation** 𝑠 = 𝑖 

# **Summary** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**1** 

A valid invariant satisfies establishment, preservation and the postcondition at exit. For termination we also need a variant. 

> **2** We can find it by tracing the values at the loop head, and looking for a relation that always holds. 

> **3** We always include the bounds of the counter, so that  𝐼 ∧ ¬𝐵  implies  𝑄. 

> **4** We generalise the postcondition by replacing the final value by the progress variable. 

We always check the candidate. When a check fails, we write down a state that breaks it, and the **5** state tells us what to change. 

