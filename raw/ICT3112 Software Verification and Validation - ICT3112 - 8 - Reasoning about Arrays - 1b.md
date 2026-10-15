# ICT3112 - 8 - Reasoning about Arrays - 1b

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Reasoning about Arrays** . if ie | **Reading: The Rule Dr. David Sanan** ay Be = 

# **Where we stopped: reading out of bounds** 



<!-- Start of picture text -->
INSTITUTEOF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>x  :=  a[i];<br>{ x >  0 }<br><!-- End of picture text -->

The rule [ASSIGN] gives: 



<!-- Start of picture text -->
{a[i] >0} x:=ali] {x >0}<br><!-- End of picture text -->



<!-- Start of picture text -->
[ASSIGN]<br>(Qe E]} x=E {Q}<br><!-- End of picture text -->

## After the repair: 

Suppose **sizeof(a) = 5** (arrays start at position 0, so the valid indices are 0 … 4) and **i = 7** : 



<!-- Start of picture text -->
4 0 9 2 5<br>a [| | | | ft] a[7] does not exist, so the read fails<br>0 1 2 3 4<br><!-- End of picture text -->



<!-- Start of picture text -->
{ a[i] >  0   def(a[i]) ∧ }<br>x  :=  a[i];<br>{ x >  0 }<br><!-- End of picture text -->



<!-- Start of picture text -->
def(a[l]) = 0 <I < sizeof(a)<br><!-- End of picture text -->



<!-- Start of picture text -->
So the corrected precondition is: a[i] > 0A def (al[i])<br><!-- End of picture text -->

# **The same happens for every read** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>x  :=  a[i] + a[j];<br>{ x >  0 }<br><!-- End of picture text -->

Another example: an expression with two reads. 

We substitute as usual, and then we add one definedness conjunct for each read in the expression: 



<!-- Start of picture text -->
Q: x>0<br>E: ali]+afj]<br><!-- End of picture text -->



<!-- Start of picture text -->
[ASSIGN]<br>{(Q[xcE}} x=E (Q<br><!-- End of picture text -->



<!-- Start of picture text -->
. .<br>{a[i] + aly] > 0}<br>x := ali] + af[j] {x > 0}<br><!-- End of picture text -->



<!-- Start of picture text -->
Substitution: Q[x < a[i] + a[j]] = (a[i] + afj] > 0)<br><!-- End of picture text -->

# **The same happens for every read** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>x  :=  a[i] + a[j];<br>{ x >  0 }<br><!-- End of picture text -->

Another example: an expression with two reads. 

We substitute as usual, and then we add one definedness conjunct for each read in the expression: 



<!-- Start of picture text -->
an<br>E: afi|+afj]<br><!-- End of picture text -->



<!-- Start of picture text -->
[ASSIGN]<br>(Q[xcE]} x=E (Q<br><!-- End of picture text -->



<!-- Start of picture text -->
{a[i] + a[j] > 0A def (afi})}<br>. .<br>x := ali] + af[j] {x > 0}<br><!-- End of picture text -->



<!-- Start of picture text -->
The first read, afi], must be defined<br><!-- End of picture text -->

# **The same happens for every read** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
{ ? }<br>x  :=  a[i] + a[j];<br>{ x >  0 }<br><!-- End of picture text -->

Another example: an expression with two reads. 

We substitute as usual, and then we add one definedness conjunct for each read in the expression: 



<!-- Start of picture text -->
Q: x>0<br>E: afi} +afj]<br><!-- End of picture text -->



<!-- Start of picture text -->
[ASSIGN]<br>(Q[xcE]} x=E (Q<br><!-- End of picture text -->



<!-- Start of picture text -->
. . - .<br>{a[t] + a[j] > 0 A def(a[i}) Adef(al))}<br>x = ali] + af] {x > 0}<br><!-- End of picture text -->



<!-- Start of picture text -->
The second read, a[j], must be defined<br><!-- End of picture text -->

**We can see a pattern here…** 

# **The rule for reading: [ARRAY-READ]** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
We use ordinary substitution, plus a definedness condition for every array read a[/] that occurs in E:<br><!-- End of picture text -->

**[ARRAY-READ]** 



<!-- Start of picture text -->
b (Qe za /\ defaliy) «=F (Q}<br><!-- End of picture text -->



<!-- Start of picture text -->
where def(a[l]) @ 0 <I < sizeof (a)<br><!-- End of picture text -->



<!-- Start of picture text -->
* The big A is a conjunction with one def(a[/]) for each array read al[/] in E.<br><!-- End of picture text -->



<!-- Start of picture text -->
« If E contains no array read, the conjunction is empty and the rule is exactly [ASSIGN].<br><!-- End of picture text -->



<!-- Start of picture text -->
* I can be any expression (i, i+1, x{[j], ...). The condition applies to the whole index expression.<br><!-- End of picture text -->

# **Checking [ARRAY-READ] · Step 1 — substitution** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->

**1 · Substitute** 

2 · Definedness 



<!-- Start of picture text -->
{ ? }<br>x  :=  a[i +  1 ];<br>{ x = a[i +  1 ] }<br><!-- End of picture text -->



<!-- Start of picture text -->
Q: x=alit1]<br>E: afi+]]<br><!-- End of picture text -->



<!-- Start of picture text -->
[ARRAY-READ]<br>« d<br>ore elnf\ def(altD)<br>x=E {Q}<br><!-- End of picture text -->



<!-- Start of picture text -->
We apply [ARRAY-READ]. Note that the index of the read is the expression i+ 1.<br><!-- End of picture text -->

First the substitution, as in [ASSIGN]: 



<!-- Start of picture text -->
Q[x — afi+ 1]] = (« = ali t+ 1))[x < afi + 1]]<br><!-- End of picture text -->



<!-- Start of picture text -->
= (afit+1] =ali+1]))<br><!-- End of picture text -->



<!-- Start of picture text -->
= true<br><!-- End of picture text -->

_Any value is equal to itself, so this part is always true._ 

# **Checking [ARRAY-READ] · Step 2 — definedness** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->

1 · Substitute **2 · Definedness** 



<!-- Start of picture text -->
{ ? }<br>x  :=  a[i +  1 ];<br>{ x = a[i +  1 ] }<br><!-- End of picture text -->



<!-- Start of picture text -->
Q: x=ali+1]<br>E: afi+1]<br><!-- End of picture text -->



<!-- Start of picture text -->
The substitution gave true. The only read in E is ali+ 1], so we add one<br>conjunct:<br><!-- End of picture text -->



<!-- Start of picture text -->
def(alit+1]) 30 <i+1 <sizeof(a)<br><!-- End of picture text -->

The precondition is: 



<!-- Start of picture text -->
trueAQ <i+1< sizeof(a) S 0<i+1<sizeof(a)<br><!-- End of picture text -->



<!-- Start of picture text -->
[ARRAY-READ]<br>(axe eA /\ deft)<br>a[I]EE<br>x=E {Q}<br><!-- End of picture text -->



<!-- Start of picture text -->
{0 <i+1<-sizeof(a)} x:=alit+1] {x=ali+1]}<br><!-- End of picture text -->

- **✓ The part given by the substitution is always true, so the only real requirement is that the read is defined.** 

