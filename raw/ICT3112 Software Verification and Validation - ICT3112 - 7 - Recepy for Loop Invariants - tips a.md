# ICT3112 - 7 - Recepy for Loop Invariants - tips a

# **ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Tips** . if ie | **Pictures and Mistakes Dr. David Sanan** ay Be 

## **Drawing the data to find the invariant** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**1** Draw the data, and mark where the progress variable is. **2** Write what is true in each region of the picture. **3** Add the bounds of the progress variable. 

0 𝑖 𝑛 **visited not visited** what  𝑄  asks for, restricted to this part what is still true here, usually the original values 𝐼  =  (visited)    (not visited)    ∧ ∧ (0 ≤ 𝑖 ≤ 𝑛) 

**Array sum** :   visited:  𝑠 = 𝐴[0] + … + 𝐴[𝑖−1].   Not visited: nothing to say, the loop only reads  𝐴.   Bounds:  0 ≤ 𝑖 ≤ 𝑛. 

_All the invariants in these recordings can be found from a picture like this one, where each slot describes one region of the data._ 

## **Two progress variables give three regions** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n = length(A)  A = A₀∧ ∧ l = **0** r = n − ∧ **1** } while (l < r) { swap(A, l, r); l **:=** l + **1** ; r **:=** r − **1** ; } 

{ A[k] = A₀[n− **1** −k] for **0** ≤ k < n } 

Reversing an array in place: two progress variables move towards each other. 

𝑙 

𝑟 

**swapped** 

**not reached swapped** 

**Visited** :  𝐴[𝑘] = 𝐴0[𝑛−1−𝑘]  for  0 ≤ 𝑘 < 𝑙  and for  𝑟 < 𝑘 < 𝑛 **Not visited** :  𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟 **Bounds and relation** :  0 ≤ 𝑙 ∧ 𝑙 ≤ 𝑟 + 1 ∧ 𝑟 ≤ 𝑛 − 1 ∧ 𝑙 + 𝑟 = 𝑛 − 1 

With two progress variables, the bounds also keep the regions in order, so they do not overlap. 

Some facts are not about one region. They hold for the whole data during the whole loop, and they go in the other relations slot: 

𝑎 = 𝑏 ⋅ 𝑞 + 𝑟 _integer division: no data to split_ 

perm(𝐴, 𝐴0) _sorting: true for the whole array_ 

## **The template in all the loops we have seen** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

The same four slots as in the template recording. The picture gives the region slots: 

|**Loop**|**Visited**|**Not visited**|**Other relations**|**Bounds**|
|---|---|---|---|---|
|**Countdown with a**<br>**counter**|—|—|𝑐 + 𝑥 = 𝐶 + 𝑋|𝑥 ≥ 0|
|**Integer division**|—|—|𝑎 = 𝑏 ⋅ 𝑞 + 𝑟|0 ≤ 𝑟|
|**Array sum**|𝑠 = 𝐴[0] + … + 𝐴[𝑖−1]|— (only reads𝐴)|—|0 ≤ 𝑖 ≤ 𝑛|
|**Zero-fill**|𝐴[𝑘] = 0for𝑘 < 𝑖|𝐴[𝑘] = 𝐴0[𝑘]for𝑘 ≥ 𝑖|—|0 ≤ 𝑖 ≤ 𝑚|
|**Reverse in place**|front and back swapped|middle:𝐴[𝑘] = 𝐴0[𝑘]|𝑙 + 𝑟 = 𝑛 − 1|on𝑙and𝑟|
|**Selection sort**|sorted prefix|—|perm(𝐴, 𝐴0), prefix  ≤  rest|0 ≤ 𝑖 ≤ 𝑛|



**The bounds slot is always filled. Facts that are not about one region go in the other relations slot.** 

## **Common mistakes when proposing an invariant** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Too weak** 

It is true and preserved, but  𝐼 ∧ ¬𝐵  does not imply  𝑄. 

**Too strong** 

It is close to  𝑄, but it is false before the first iteration. 

**Missing bounds** 

We found the equation of the loop, but not the facts that fix the final value of the counter. 

**Missing extra facts** 

In max or search loops one equation is not enough: we may also need facts about the prefix, or a witness. 

_When a candidate fails, first find out which kind of failure it is. Then strengthen or weaken the invariant accordingly._ 

## **What to do when a check fails** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

> **1** Say which check fails: establishment, preservation, or the postcondition at exit. 

> **2** Write down a concrete state that shows the failure, with a number for every variable. 

> **3** Ask what the state tells you. 

> **4** Change the candidate, and check all three conditions again. 

The candidate **rejects** a real state _it is too strong, so we weaken it_ 

The candidate **accepts** a wrong state _it is too weak, so we add the fact that rules the state out_ 

_Establishment failures give the first kind of state. Preservation and exit failures give the second kind._ 

