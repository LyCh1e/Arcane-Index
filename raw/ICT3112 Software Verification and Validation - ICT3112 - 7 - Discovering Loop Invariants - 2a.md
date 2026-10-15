# ICT3112 - 7 - Discovering Loop Invariants - 2a

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **The Not Visited Slot Dr. David Sanan** ay Be = 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**Side cases** 

# **When the non-visited part is not empty (1)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

while (i < n) { A[i] **:= 0** ; i **:=** i + **1** ; } 

**The postcondition constrains cells the loop never reaches, for example: the cells of the array after a certain position keep their original values.** 

**Case 1** 

𝑃:   𝑛 = length(𝐴) ∧ 𝑖 = 0 𝑄:   𝐴[𝑘] = 0  for  0 ≤ 𝑘 < 𝑛 

**Case 2** 

𝑃:   0 ≤ 𝑛 ≤ length(𝐴) ∧ 𝑖 = 0 𝑄:   𝐴[𝑘] = 0  for  0 ≤ 𝑘 < 𝑛 

**Case 3** 

𝑃:   0 ≤ 𝑛 ≤ length(𝐴) ∧ 𝑖 = 0 ∧ 𝐴 = 𝐴0 𝑄:   𝐴[𝑘] = 0  for  0 ≤ 𝑘 < 𝑛 ∧  𝐴[𝑘] = 𝐴0[𝑘]  for  𝑛 ≤ 𝑘 < length(𝐴) 

# **When the non-visited part is not empty (1)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ n = length(A)  i = ∧ 0 } The postcondition constrains cells the loop never reaches, for example: the<br>cells of the array after a certain position keep their original values.<br>while (i < n) {<br>    A[i]  := 0 ; ■ reached by the loop ■ constrained by Q<br>    i  :=  i +  1 ; 𝑛<br>}<br>zeroed<br>{ A[k] =  0   for  0  ≤ k < n }<br>|<br>Slot Filled with<br>Visited 𝐴[𝑘] = 0  for  0 ≤ 𝑘 < 𝑖<br>Not visited — not needed: the loop zeroes every cell that   𝑄   talks about<br>Other relations — none<br>Bounds 0 ≤ 𝑖 ≤ 𝑛<br><!-- End of picture text -->

# **When the non-visited part is not empty (1)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ 0  ≤ n ≤ length(A) ∧<br>  i =  0 }<br>while (i < n) {<br>    A[i]  := 0 ;<br>    i  :=  i +  1 ;<br>}<br>{ A[k] =  0   for  0  ≤ k < n }<br><!-- End of picture text -->



<!-- Start of picture text -->
The postcondition constrains cells the loop never reaches, for example: the<br>cells of the array after a certain position keep their original values.<br>■ reached by the loop ■ constrained by Q<br>𝑛<br>zeroed never reached<br>|<br>Slot Filled with<br>Visited 𝐴[𝑘] = 0  for  0 ≤ 𝑘 < 𝑖<br>Not visited — not needed:   𝑄   says nothing about the cells after   𝑛<br>Other relations — none<br>Bounds 0 ≤ 𝑖 ≤ 𝑛<br><!-- End of picture text -->

# **When the non-visited part is not empty (1)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ 0  ≤ n ≤ length(A) ∧<br>  i =  0   A = A₀ ∧ }<br>while (i < n) {<br>    A[i]  := 0 ;<br>    i  :=  i +  1 ;<br>}<br>{ A[k] =  0   for  0  ≤ k < n<br>∧ A[k] = A₀[k]<br>     for n ≤ k < length(A) }<br><!-- End of picture text -->



<!-- Start of picture text -->
The postcondition constrains cells the loop never reaches, for example: the<br>cells of the array after a certain position keep their original values.<br>■ reached by the loop ■ constrained by Q<br>𝑛<br>zeroed never reached<br>|<br>Slot Filled with<br>Visited 𝐴[𝑘] = 0  for  0 ≤ 𝑘 < 𝑖<br>Not visited 𝐴[𝑘] = 𝐴0[𝑘]  for  𝑖 ≤ 𝑘 < length(𝐴)<br>Other relations — none<br>Bounds 0 ≤ 𝑖 ≤ 𝑛<br><!-- End of picture text -->

At the exit  𝑖 = 𝑛. The visited part gives the first half of  𝑄, and the not visited part becomes  𝐴[𝑘] = 𝐴0[𝑘]  for  𝑛 ≤ 𝑘 < length(𝐴), which is the second half. 

# **When the non-visited part is not empty (2)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ n = length(A)  A = A₀∧ The loop writes the array, and the body reads cells the loop has not reached<br>yet.<br>∧ l =  0   r = n − ∧ 1 }<br>while (l < r) { 𝑙 𝑟<br>    swap(A, l, r);<br>swapped not reached swapped<br>    l  :=  l +  1 ;<br>↑  swap reads  𝐴[𝑟], inside the region not reached<br>    r  :=  r −  1 ;<br>} Slot Filled with<br>{ A[k] = A₀[n− 1 −k]<br>𝐴[𝑘] = 𝐴0[𝑛 − 1 − 𝑘]  for  0 ≤ 𝑘 < 𝑙<br>     for  0  ≤ k < n } Visited<br>and for  𝑟 < 𝑘 < 𝑛<br>Not visited 𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟<br>Other relations 𝑙 + 𝑟 = 𝑛 − 1<br>Bounds 0 ≤ 𝑙   ∧   𝑙 ≤ 𝑟 + 1   ∧   𝑟 ≤ 𝑛 − 1<br><!-- End of picture text -->

# **When the non-visited part is not empty (2)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**The loop writes the array, and the body reads cells the loop has not reached yet.** 



<!-- Start of picture text -->
{ n = length(A)  A = A₀∧ The loop writes the array, and the body reads cells the loop has not reached<br>yet.<br>∧ l =  0   r = n − ∧ 1 }<br>while (l < r) {<br>The loop stops when  𝑙 ≥ 𝑟. With  𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two 𝑙 ≥ 𝑟. With  𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two . With  𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two 𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two   and  𝑙 + 𝑟 = 𝑛 − 1  there are two 𝑙 + 𝑟 = 𝑛 − 1  there are two   there are two<br>    swap(A, l, r); cases:<br>    l  :=  l +  1 ;<br>    r  :=  r −  1 ;<br>𝑛 even  (𝑛 = 6) 6 5 4 3 2 1 𝑙 = 𝑟 + 1: the middle region is<br>} 0 1 2 3 4 5 empty.<br>{ A[k] = A₀[n− 1 −k] 𝑟 𝑙<br>     for  0  ≤ k < n }<br>𝑛 odd  (𝑛 = 5) 5 4 3 2 1 𝑙 = 𝑟: one middle cell, which is its<br>own mirror:  𝑛 − 1 − 𝑘 = 𝑘.<br>0 1 2 3 4<br>𝑙𝑟<br><!-- End of picture text -->

The loop stops when  𝑙 ≥ 𝑟. With  𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two 𝑙 ≥ 𝑟. With  𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two . With  𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two 𝑙 ≤ 𝑟 + 1  and  𝑙 + 𝑟 = 𝑛 − 1  there are two   and  𝑙 + 𝑟 = 𝑛 − 1  there are two 𝑙 + 𝑟 = 𝑛 − 1  there are two   there are two cases: 

In both cases the two swapped regions and the middle cell cover the whole array, and that gives  𝑄. 

# **When the non-visited part is not empty (2)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
Slot Filled with<br>{ n = length(A)  A = A₀∧<br>𝐴[𝑘] = 𝐴0[𝑛 − 1 − 𝑘]  for  0 ≤ 𝑘 < 𝑙<br>∧ l =  0   r = n − ∧ Visited<br>1 }<br>and for  𝑟 < 𝑘 < 𝑛<br>while (l < r) {<br>Not visited 𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟<br>    swap(A, l, r);<br>    l  :=  l +  1 ; Other relations 𝑙 + 𝑟 = 𝑛 − 1<br>    r  :=  r −  1 ; Bounds 0 ≤ 𝑙   ∧   𝑙 ≤ 𝑟 + 1   ∧   𝑟 ≤ 𝑛 − 1<br>}<br>{ A[k] = A₀[n− 1 −k] Initial  (𝐴0) 1 2 3 4 5 6<br>0 1 2 3 4 5<br>     for  0  ≤ k < n }<br>After iteration 1 6 2 3 4 5 1<br>0 1 2 3 4 5<br>𝑙 𝑟<br><!-- End of picture text -->

First iteration:  𝑙 = 0  and  𝑟 = 5. The swap exchanges the first and the last cell. The middle cells  2, 3, 4, 5  still hold their original values. 

# **When the non-visited part is not empty (2)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
Slot Filled with<br>{ n = length(A)  A = A₀∧<br>𝐴[𝑘] = 𝐴0[𝑛 − 1 − 𝑘]  for  0 ≤ 𝑘 < 𝑙<br>∧ l =  0   r = n − ∧ Visited<br>1 }<br>and for  𝑟 < 𝑘 < 𝑛<br>while (l < r) {<br>Not visited 𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟<br>    swap(A, l, r);<br>    l  :=  l +  1 ; Other relations 𝑙 + 𝑟 = 𝑛 − 1<br>    r  :=  r −  1 ; Bounds 0 ≤ 𝑙   ∧   𝑙 ≤ 𝑟 + 1   ∧   𝑟 ≤ 𝑛 − 1<br>}<br>{ A[k] = A₀[n− 1 −k] Initial  (𝐴0) 1 2 3 4 5 6<br>0 1 2 3 4 5<br>     for  0  ≤ k < n }<br>After iteration 2 6 5 3 4 2 1<br>0 1 2 3 4 5<br>𝑙 𝑟<br><!-- End of picture text -->

Second iteration:  𝑙 = 1  and  𝑟 = 4. The swap exchanges  2  and  5. The middle cells  3 and  4  still hold their original values. 

# **When the non-visited part is not empty (2)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
Slot Filled with<br>{ n = length(A)  A = A₀∧<br>𝐴[𝑘] = 𝐴0[𝑛 − 1 − 𝑘]  for  0 ≤ 𝑘 < 𝑙<br>∧ l =  0   r = n − ∧ Visited<br>1 }<br>and for  𝑟 < 𝑘 < 𝑛<br>while (l < r) {<br>Not visited 𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟<br>    swap(A, l, r);<br>    l  :=  l +  1 ; Other relations 𝑙 + 𝑟 = 𝑛 − 1<br>    r  :=  r −  1 ; Bounds 0 ≤ 𝑙   ∧   𝑙 ≤ 𝑟 + 1   ∧   𝑟 ≤ 𝑛 − 1<br>}<br>{ A[k] = A₀[n− 1 −k] Initial  (𝐴0) 1 2 3 4 5 6<br>0 1 2 3 4 5<br>     for  0  ≤ k < n }<br>After iteration 3 6 5 4 3 2 1<br>0 1 2 3 4 5<br>𝑟 𝑙<br><!-- End of picture text -->

Third iteration:  𝑙 = 2  and  𝑟 = 3. The swap exchanges  3  and  4. Now  𝑙 = 𝑟 + 1, the guard is false, and the array is reversed. 

# **When the non-visited part is not empty (2)** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ n = length(A)  A = A₀∧<br>∧ l =  0   r = n − ∧ 1 }<br>while (l < r) {<br>    swap(A, l, r);<br>    l  :=  l +  1 ;<br>    r  :=  r −  1 ;<br>}<br>{ A[k] = A₀[n− 1 −k]<br>     for  0  ≤ k < n }<br><!-- End of picture text -->



<!-- Start of picture text -->
Slot Filled with<br>𝐴[𝑘] = 𝐴0[𝑛 − 1 − 𝑘]  for  0 ≤ 𝑘 < 𝑙<br>Visited<br>and for  𝑟 < 𝑘 < 𝑛<br>Not visited 𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟<br>Other relations 𝑙 + 𝑟 = 𝑛 − 1<br>Bounds 0 ≤ 𝑙   ∧   𝑙 ≤ 𝑟 + 1   ∧   𝑟 ≤ 𝑛 − 1<br>Initial  (𝐴0) 1 2 3 4 5 6<br>0 1 2 3 4 5<br>Snapshot 6 5 8 2 2 1 Accepted by the weaker invariant,<br>but the middle cells have nothing to<br>0 1 2 3 4 5<br>do with  𝐴0.<br>𝑙 𝑟<br><!-- End of picture text -->

The invariant describes what would be a valid snapshot after executing the loop any number of times. Without  𝐴[𝑘] = 𝐴0[𝑘]  for  𝑙 ≤ 𝑘 ≤ 𝑟, it accepts snapshots like this one, and it is too weak to prove that the array is reversed. 

