# ICT3112 - 8 - Reasoning about Arrays - 2a

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Reasoning about Arrays** . if ie | **Writing: The Problem Dr. David Sanan** ay Be = 

# **Reminder: the rule for reading, [ARRAY-READ]** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
We use ordinary substitution, plus a definedness condition for every array read a[/] that occurs in E:<br><!-- End of picture text -->

**[ARRAY-READ]** 



<!-- Start of picture text -->
b (Qe za /\ defaliy) «=F (Q}<br><!-- End of picture text -->



<!-- Start of picture text -->
where def(a[l]) @ 0 <I < sizeof (a)<br><!-- End of picture text -->

Today: programs that write into an array, with statements such as 𝑎[𝑖]≔1. 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**Part 2 · Writing to an array** 

# **A first approach: treating a[I] as a variable** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

We treat the cell  𝑎[𝐼]  as if it were a variable and reuse [ASSIGN] (plus the definedness of the write): we replace the occurrences of  𝑎[𝐼]  in  𝑄. 

**[NAÏVE WRITE]** 

⊢  {𝑄[𝑎[𝐼] ← 𝐸] ∧ 𝑑𝑒𝑓(𝑎[𝐼])}  𝑎[𝐼] ≔ 𝐸  {𝑄} 

It seems correct for this example: 

{𝑥[5] + 1 > 0 ∧ 𝑑𝑒𝑓(𝑥[5])}  𝑥[5] ≔ 𝑥[5] + 1  {𝑥[5] > 0} 

_Here the only read in_ 𝐸 _is_ 𝑥[5] _, the same cell we write, so_ 𝑑𝑒𝑓(𝑥[5]) _also covers the read. In general we would add the definedness of every array read in_ 𝐸 _, as we saw in the rule for reading._ 

**It seems to work. Is there a problem?** 

# **The naive rule when Q reads another cell** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

**[NAÏVE WRITE]** {𝑄[𝑎[𝐼] ← 𝐸] ∧ 𝑑𝑒𝑓(𝑎[𝐼])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

**What if the postcondition reads the array at a different index?** The postcondition mentions  𝑎[𝑗], while the assignment writes  𝑎[𝑖]. The naive rule replaces the occurrences of  𝑎[𝑖]  in  𝑄  by  1. However,  𝑄 contains no  𝑎[𝑖], so nothing changes: 

𝑄[𝑎[𝑖] ← 1] = (𝑎[𝑗] = 0) 

{𝑎[𝑗] = 0 ∧ 𝑑𝑒𝑓(𝑎[𝑖])}  𝑎[𝑖] ≔ 1  {𝑎[𝑗] = 0} 

**According to the rule, the write cannot change** 𝑎[𝑗] **.  Is this true?** 

# **The naive rule fails when i = j: aliasing** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ a[j] =  0   def(a[i]) ∧ }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

Take  𝑎 = [4, 0, 9]  and  𝑖 = 𝑗 = 1.  The precondition holds, since  𝑎[1] = 0 ✓ 



<!-- Start of picture text -->
𝑎 4 0 9<br>0 1 2<br><!-- End of picture text -->

before:  𝑎[𝑗] = 0 



<!-- Start of picture text -->
𝑖𝑗<br><!-- End of picture text -->

Now we execute  𝑎[𝑖] ≔ 1, which writes position  𝑖 = 1. 

### **[NAÏVE WRITE]** 

{𝑄[𝑎[𝐼] ← 𝐸] ∧ 𝑑𝑒𝑓(𝑎[𝐼])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

# **The naive rule fails when i = j: aliasing** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ a[j] =  0   def(a[i]) ∧ }<br>a[i]  := 1 ;<br>{ a[j] =  0 }<br><!-- End of picture text -->

𝑄:  𝑎[𝑗] = 0 𝐼:  𝑖 𝐸:  1 

Take  𝑎 = [4, 0, 9]  and  𝑖 = 𝑗 = 1.  The precondition holds, since  𝑎[1] = 0 ✓ 

𝑎 4 **1** 9 after:  𝑎[𝑗] = 1, so the postcondition is 0 1 2 false  ✗ 



<!-- Start of picture text -->
𝑖𝑗<br><!-- End of picture text -->

Now we execute  𝑎[𝑖] ≔ 1, which writes position  𝑖 = 1. 

### **[NAÏVE WRITE]** 

{𝑄[𝑎[𝐼] ← 𝐸] ∧ 𝑑𝑒𝑓(𝑎[𝐼])} 𝑎[𝐼] ≔ 𝐸  {𝑄} 

𝑎[𝑖]  and  𝑎[𝑗]  are different names for the **same cell** when  𝑖 = 𝑗. This is called **aliasing** . 

Substitution cannot detect this, so the naive rule is not sound: its precondition holds before the write, but the postcondition is false after it. 

## **Why the naive rule fails: a write changes the array** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Why does it not work? A write changes the array, not only one position.** 

- The variable being assigned is not the cell. It is  𝑎  itself: after the write,  𝑎  denotes a new array. 

- The new array agrees with the old one everywhere except (possibly) at position  𝐼. 

- So we should substitute the whole array for  𝑎, and for that we need a notation for “𝑎  updated at  𝐼”. 

𝑎[𝐼] ≔ 𝐸     behaves like     𝑎 ≔ 𝑎[𝐼 ↦ 𝐸] 

**Now we have one assignment to one variable,** 𝑎 **, so the idea of [ASSIGN] applies again.** 

