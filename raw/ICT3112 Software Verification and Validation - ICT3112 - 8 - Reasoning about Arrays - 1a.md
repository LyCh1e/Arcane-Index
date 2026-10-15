# ICT3112 - 8 - Reasoning about Arrays - 1a

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Reasoning about Arrays** . if ie | **Reading: The Problem Dr. David Sanan** ay Be = 

# **Hoare Logic – the rules so far** 



- **[SKIP]   [ASSIGN]   [SEQ]   [IF]   [WHILE]   [CONSEQUENCE]** 

- All these rules work with simple variables, where each name holds one value. 

- The most important one is the assignment rule: we substitute the expression for the variable in the postcondition. 

**[ASSIGN]** 



<!-- Start of picture text -->
F {Q[x E]} x=E {Q}<br><!-- End of picture text -->



<!-- Start of picture text -->
1.{2?}x :=y+1f{x > 0}<br><!-- End of picture text -->



<!-- Start of picture text -->
2.(x >O0)[xyt 1]<br><!-- End of picture text -->



<!-- Start of picture text -->
3.(yv+1>0)<br><!-- End of picture text -->



<!-- Start of picture text -->
4.fy+1>0}x =yt1{x > 0}<br><!-- End of picture text -->

**Today we look at what happens when the program reads from and writes to arrays.** 

# **Today’s objectives** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

- Understand why array cells cannot be treated like ordinary variables. 

- A rule for **reading** from an array, where every read must be defined: **[ARRAY-READ]** 

- A rule for **writing** to an array position, which is a variant of the assignment rule: **[ARRAY-ASSIGN]** 

- We build each rule step by step from an example, as we did for [ASSIGN]. 

- Two exercises where we apply the rules step by step. 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**Part 1 · Reading from an array** 

# **A first attempt at array reads** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>x  :=  a[i];<br>{ x >  0 }<br><!-- End of picture text -->



<!-- Start of picture text -->
ali] looks like any other expression, so we apply [ASSIGN] as usual:<br><!-- End of picture text -->



<!-- Start of picture text -->
Q[x < ali]] = Ge > 0)[x < afi]] = (afi] > 0)<br><!-- End of picture text -->



<!-- Start of picture text -->
Q: x>0<br>E: ail<br><!-- End of picture text -->



<!-- Start of picture text -->
[ASSIGN]<br>(lee El} x= FE (Q}<br><!-- End of picture text -->

## This gives the triple: 



<!-- Start of picture text -->
{a[i] > 0} x:=ali] {x >0}<br><!-- End of picture text -->



<!-- Start of picture text -->
Substituting afi] for x in the postcondition seems to work...<br><!-- End of picture text -->



<!-- Start of picture text -->
Is the precondition a[i] > 0 really enough for this triple to hold?<br><!-- End of picture text -->

# **What can go wrong: reading out of bounds** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
{ a[i] >  0 }<br>x  :=  a[i];<br>{ x >  0 }<br><!-- End of picture text -->



<!-- Start of picture text -->
Q: x>0<br>E: afi]<br><!-- End of picture text -->



<!-- Start of picture text -->
Suppose   sizeof(a) = 5   (arrays start at position 0, so the valid indices are 0 … 4) and<br>i = 7 :<br>4 0 9 2 5<br>a Lf | ft tf] a[7] does not exist, so the read fails<br>0 1 2 3 4<br><!-- End of picture text -->



<!-- Start of picture text -->
* If i is outside the bounds, a[i] is undefined. We are accessing an undefined<br>position, and no postcondition can be guaranteed in that case.<br><!-- End of picture text -->



<!-- Start of picture text -->
[ASSIGN]<br>(Q[xe E]} x=E {Q}<br><!-- End of picture text -->

- To guarantee correctness, the precondition must also guarantee that every array read is **defined** : the position accessed in the array is within the array limits. 



<!-- Start of picture text -->
Assume a function sizeof(a) giving the size of array a, and abbreviate:<br><!-- End of picture text -->



<!-- Start of picture text -->
def(a[l]) = 0 <I < sizeof(a)<br><!-- End of picture text -->

# **What can go wrong: reading out of bounds** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
{ a[i] >  0   def(a[i]) ∧ }<br>x  :=  a[i];<br>{ x >  0 }<br><!-- End of picture text -->



<!-- Start of picture text -->
Q: x>0<br>E: afi]<br><!-- End of picture text -->



<!-- Start of picture text -->
Suppose   sizeof(a) = 5   (arrays start at position 0, so the valid indices are 0 … 4) and<br>i = 7 :<br>4 0 9 2 5<br>a Lf | ft tf] a[7] does not exist, so the read fails<br>0 1 2 3 4<br><!-- End of picture text -->



<!-- Start of picture text -->
* If i is outside the bounds, a[i] is undefined. We are accessing an undefined<br>position, and no postcondition can be guaranteed in that case.<br><!-- End of picture text -->



<!-- Start of picture text -->
[ASSIGN]<br>(Q[xe E]} x=E {Q}<br><!-- End of picture text -->

- To guarantee correctness, the precondition must also guarantee that every array read is **defined** : the position accessed in the array is within the array limits. 



<!-- Start of picture text -->
Assume a function sizeof(a) giving the size of array a, and abbreviate:<br><!-- End of picture text -->



<!-- Start of picture text -->
def(a[l]) = 0 <I < sizeof(a)<br><!-- End of picture text -->



<!-- Start of picture text -->
So the corrected precondition is: ali] > 0A def(ali])<br><!-- End of picture text -->

