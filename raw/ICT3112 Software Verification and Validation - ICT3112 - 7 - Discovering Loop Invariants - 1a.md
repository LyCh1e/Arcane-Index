# ICT3112 - 7 - Discovering Loop Invariants - 1a

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **The Template Dr. David Sanan** ay Be = 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**A template for invariants** 

# **A template guide for building invariants** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

As a guide, we can identify four components in an invariant: 

𝐼  =  (bounds)    (relations among the variables)    (visited)    (not visited)∧ ∧ ∧ 

|**Component**|**Meaning**|**When you need it**|
|---|---|---|
|**Bounds**|Where the progress variables can be, for example0 ≤<br>𝑖 ≤ 𝑛.|It turns “the loop stopped” into “𝑖reached𝑛”.|
|**Relations among the**<br>**variables**|A fact that is not about one region alone:𝑎 = 𝑏⋅𝑞 +<br>𝑟,𝑐 + 𝑥 = 𝑋,  perm(𝐴, 𝐴0),  prefix ≤ everything<br>ahead.|When the loop preserves something all the way through, or<br>when the body needs to know something about the part it<br>has not reached.|
|**Visited**|What𝑄asks for, restricted to the part already visited.|Whenever𝑄constrains a result built up over the data.|
|**Not visited**|What is still true of the part the loop has not reached.|When preservation or𝑄needs a fact about the part not<br>yet reached.|



**Not every component is always present, and the categories may overlap, as we will see later. The template is a guide for easy understanding.** 

𝐼 = (produced so far)  (bounds)∧ 𝐼 = (other relations)  (bounds)∧ _the loop only reads its data, like a sum no data to split, like integer division_ 

𝐼 = (bounds) _nothing but a counter:  while (x > 0)  x := x − 1_ 

# **Example 1: bounds only** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ x ≥  0 }<br>while (x >  0 )<br>    x  :=  x −  1 ;<br>{ x =  0 }<br><!-- End of picture text -->



<!-- Start of picture text -->
Slot Filled with<br>Visited — nothing is built up<br>Not visited — no data to split<br>Other relations — none<br>Bounds 𝑥 ≥ 0<br><!-- End of picture text -->



<!-- Start of picture text -->
𝐼 = 𝑥 ≥ 0<br><!-- End of picture text -->

The negation of the loop condition gives  𝑥 ≤ 0, the bounds give  𝑥 ≥ 0, and together they give  𝑥 = 0, which is  𝑄. 

# **Example 2: increasing two variables** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** s = ∧ **0** i = ∧ **0** } while (i < n) { s **:=** s + **1** ; i **:=** i + **1** ; } { s = n } 

_An accumulator counts the passes with two variables (yes, they are redundant)._ 

**Slot Filled with** Visited _— none_ Not visited _— the loop reads no data_ Other relations 𝑠 = 𝑖 Bounds 0 ≤ 𝑖 ≤ 𝑛 𝐼 = (𝑠 = 𝑖) ∧ (0 ≤ 𝑖 ≤ 𝑛) 

To show  𝐼 ∧ ¬𝐵 ⇒ 𝑄:  from  0 ≤ 𝑖 ≤ 𝑛  and  ¬𝐵, that is  𝑖 ≥ 𝑛, we get  𝑖 = 𝑛. But  𝑄  is about  𝑠, so  𝐼  must say how  𝑠  and  𝑖  are related:  𝑠 = 𝑖  and  𝑖 = 𝑛  give 𝑠 = 𝑛. 

Preservation:  𝑠 = 𝑖  gives  𝑠 + 1 = 𝑖 + 1  after the body.  Establishment:  𝑠 = 0  and 𝑖 = 0  at the start. 

# **Example 2: a redundant conjunct** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** s = ∧ **0** i = ∧ **0** } while (i < n) { s **:=** s + **1** ; i **:=** i + **1** ; } { s = n } 

**Slot Filled with** Visited _— none_ Not visited _— the loop reads no data_ Other relations 𝑠 = 𝑖,   0 ≤ 𝑠 ≤ 𝑛 Bounds 0 ≤ 𝑖 ≤ 𝑛 

_An accumulator counts the passes with two variables (yes, they are redundant)._ 

𝐼 = (𝑠 = 𝑖) ∧ (0 ≤ 𝑖 ≤ 𝑛) ∧ (0 ≤ 𝑠 ≤ 𝑛) 

We can add  0 ≤ 𝑠 ≤ 𝑛. It is true at every loop head, but it adds no information:  𝑠 = 𝑖 and  0 ≤ 𝑖 ≤ 𝑛  already imply it. 

An invariant should contain what is needed. Facts that follow from the others only make the proofs longer. 

# **Example 3: decrease and increase** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ x = X  X ≥ ∧ **0** c = C ∧ } while (x > **0** ) { x **:=** x − **1** ; c **:=** c + **1** ; } { c = X + C } 

**Slot Filled with** Visited _— no data to split_ Not visited _— no data to split_ Other relations 𝑐 + 𝑥 = 𝐶 + 𝑋 Bounds 𝑥 ≥ 0 

𝐼 = (𝑐 + 𝑥 = 𝐶 + 𝑋) ∧ (𝑥 ≥ 0) 

To prove  𝐼 ∧ ¬𝐵 ⇒ 𝑄: (1)  ¬𝐵  gives  𝑥 ≤ 0, and the bound gives  𝑥 ≥ 0, so  𝑥 = 0. (2)  𝑐 + 𝑥 = 𝐶 + 𝑋  with  𝑥 = 0  gives  𝑐 = 𝐶 + 𝑋, which is  𝑄. 

Preservation: the body takes one away from  𝑥  and adds one to  𝑐, so  𝑐 + 𝑥  does not change. 

