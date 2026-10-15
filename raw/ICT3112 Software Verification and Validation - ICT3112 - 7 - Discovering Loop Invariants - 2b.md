# ICT3112 - 7 - Discovering Loop Invariants - 2b

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **Bounds and Relations Dr. David Sanan** ay Be = 

# **The importance of the variable bounds** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** s = ∧ **0** i = ∧ **0** } while (i < n) { s **:=** s + **1** ; i **:=** i + **1** ; } { s = n } 

_The second example of the template again, with a different bound._ 

**Slot Filled with** Visited _— none_ Not visited _— the loop reads no data_ Other relations 𝑠 = 𝑖 **Bounds** 𝑖 ≤ 𝑛 + 1 

𝐼′ = (𝑠 = 𝑖) ∧ (𝑖 ≤ 𝑛 + 1) 

The proposed invariant holds at the start and it is preserved, so it is a valid invariant for this loop. 

𝐼′ ∧ ¬𝐵:   𝑠 = 𝑖 ∧ 𝑖 ≤ 𝑛 + 1 ∧ 𝑖 ≥ 𝑛    ⇒    𝑠 = 𝑛 ? However, it is too weak: from  𝑖 ≥ 𝑛  and  𝑖 ≤ 𝑛 + 1  we only get  𝑠 = 𝑛 ∨ 𝑠 = 𝑛 + 1. 

_Often, like in real programming, we do not calculate the bounds of the variables correctly, and that leads to wrong specifications._ 

# **When the other relations slot is needed** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ n = length(A)  A = A₀∧ ∧ i = **0** } while (i < n) { m **:=** minIndex(A, i, n− **1** ); swap(A, i, m); i **:=** i + **1** ; } 

- { sorted(A[ **0** ..n− **1** ]) 

- ∧ perm(A, A₀) } 

_minIndex(A, i, n−1)  is the position of a smallest element of  A[i..n−1]._ 

Selection sort writes into the part it has not reached, and it needs a fact about **both** regions: 

**Slot Filled with** Visited 𝐴[0..𝑖−1]  is sorted Not visited _—_ 𝑄 _says nothing about the order of the rest_ every element of  𝐴[0..𝑖−1]  ≤  every element of  𝐴[𝑖..𝑛−1] **Other relations** perm(𝐴, 𝐴0) Bounds 0 ≤ 𝑖 ≤ 𝑛 

Without the first relation, preservation fails. A state that shows it:  𝐴 = [5, 2, 7],  𝑖 = 1. The visited part  [5]  is sorted, but the loop puts  2  after it, and  [5, 2]  is not sorted. 

**This fact names elements on both sides of** 𝑖 **, so it belongs to neither region alone. That is what the other relations slot is for.** 

# **All four slots at once** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ **0** ≤ m ≤ length(A) ∧ A = A₀  c = ∧ **0** i = ∧ **0** } while (i < m) { A[i] **:= 0** ; c **:=** c + **1** ; i **:=** i + **1** ; } 

- { A[k] = **0** for **0** ≤ k < m ∧ A[k] = A₀[k] 

- for m ≤ k < length(A) ∧ c = m } 

_Zero the first  m  cells, without modifying the rest. Then count in  c  how many cells have been modified._ 

**Slot** 

## **Filled with** 

𝐴[𝑘] = 0  for  0 ≤ 𝑘 < 𝑖 𝐴[𝑘] = 𝐴0[𝑘]  for  𝑖 ≤ 𝑘 < length(𝐴) 

Visited 

Not visited 

Other relations 

𝑐 = 𝑖 0 ≤ 𝑖 ≤ 𝑚 

Bounds 

𝐼 = (𝐴[𝑘] = 0 for 0 ≤ 𝑘 < 𝑖) ∧ (𝐴[𝑘] = 𝐴0[𝑘] for 𝑖 ≤ 𝑘 < length(𝐴)) ∧  (𝑐 = 𝑖) ∧ (0 ≤ 𝑖 ≤ 𝑚) 

At the exit  𝑖 = 𝑚. The visited part gives the first part of  𝑄, the not visited part gives the second part, and  𝑐 = 𝑖  gives  𝑐 = 𝑚. If we drop any of the four conjuncts, one part of  𝑄  can no longer be proved. 

