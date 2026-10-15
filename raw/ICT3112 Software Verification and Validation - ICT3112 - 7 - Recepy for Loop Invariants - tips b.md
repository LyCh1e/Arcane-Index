# ICT3112 - 7 - Recepy for Loop Invariants - tips b

# **ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Tips** . if ie | **Mistakes in Practice Dr. David Sanan** ay Be 

## **Too weak: an example** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } { s = n(n+ **1** )/ **2** } 

The sum  1 + 2 + … + 𝑛  again, with a candidate that is too simple: _Proposed invariant:_ 

𝐼1:    0 ≤ 𝑖 ≤ 𝑛 

- **Establishment** :  0 ≤ 0 ≤ 𝑛, since  𝑛 ≥ 0.   ✓ 

- **Preservation** :  𝑖 < 𝑛  gives  0 ≤ 𝑖 + 1 ≤ 𝑛.   ✓ 

**This is a correct invariant of the loop. But is it useful?** 

## **Too weak: diagnosis and fix** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } { s = n(n+ **1** )/ **2** } 

At the exit,  𝐼1 ∧ 𝑖 ≥ 𝑛  gives  𝑖 = 𝑛, but it says nothing about  𝑠. 

- **✗ The postcondition at exit fails.** 

**A state that shows the failure** :  𝑛 = 3,  𝑖 = 3,  𝑠 = 100. It satisfies  𝐼1 ∧ ¬𝐵, but  𝑄  needs  𝑠 = 6. 

The candidate accepts a wrong state, so it is too weak. 

The fact that rules this state out is the result computed so far: 

𝐼2:    𝑠 = 𝑖(𝑖+1)/2 ∧ 0 ≤ 𝑖 ≤ 𝑛 

**Rule of thumb: if the invariant is too weak, strengthen it with the missing fact about the result.** 

## **Too strong: an example** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } { s = n(n+ **1** )/ **2** } 

**Why not simply use the postcondition as the invariant?** _Proposed invariant:_ 𝐼1:    𝑠 = 𝑛(𝑛+1)/2 ∧ 0 ≤ 𝑖 ≤ 𝑛 

This looks attractive, since the postcondition at exit holds immediately:  𝐼1  already contains  𝑄. 

**But let’s check the first condition.** 

## **Too strong: diagnosis and fix** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } { s = n(n+ **1** )/ **2** } 

We check establishment right after  𝑖 ≔ 0;  𝑠 ≔ 0. 

- **✗ Establishment fails.** 

**A state that shows the failure** :  𝑛 = 3,  𝑖 = 0,  𝑠 = 0, right after the initialisation. This state really happens, but  𝐼1  rejects it, since it needs  𝑠 = 6. The candidate rejects a real state, so it is too strong. 

The candidate describes the end of the loop, not every loop head. We weaken it by replacing  𝑛  by  𝑖: 

𝐼2:    𝑠 = 𝑖(𝑖+1)/2 ∧ 0 ≤ 𝑖 ≤ 𝑛 

**Rule of thumb: if the invariant is too strong, weaken it by replacing constants by progress variables.** 

## **Missing bounds: an example** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ b ≥ **0** } p **:= 0** ;  i **:= 0** ; while (i < b) { p **:=** p + a; i **:=** i + **1** ; } { p = a · b } 

The multiplication from the exercises, with only the loop equation: _Proposed invariant:_ 𝐼1:    𝑝 = 𝑎 ⋅ 𝑖 

- **Establishment** :  𝑝 = 0 = 𝑎 ⋅ 0.   ✓ 

- **Preservation** :  𝑝 = 𝑎 ⋅ 𝑖  gives  𝑝 + 𝑎 = 𝑎 ⋅ (𝑖+1).   ✓ 

**The equation is correct, so what can go wrong?** 

## **Missing bounds: diagnosis and fix** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ b ≥ **0** } p **:= 0** ;  i **:= 0** ; while (i < b) { 

At the exit, the negated guard only gives  𝑖 ≥ 𝑏. From that alone,  𝑖 = 𝑏  does not follow. 

- **✗ The postcondition at exit fails.** 

p **:=** p + a; i **:=** i + **1** ; } { p = a · b } 

**A state that shows the failure** :  𝑎 = 2,  𝑏 = 3,  𝑖 = 4,  𝑝 = 8. It satisfies  𝑝 = 𝑎 ⋅ 𝑖  and  𝑖 ≥ 𝑏, but  𝑎 ⋅ 𝑏 = 6. 

The counter is beyond its final value, so the candidate is missing a bound. 

The fact that rules this state out is the range of the counter: 

𝐼2:    𝑝 = 𝑎 ⋅ 𝑖 ∧ 0 ≤ 𝑖 ≤ 𝑏 

𝑖 ≥ 𝑏 ∧ 𝑖 ≤ 𝑏 ⇒ 𝑖 = 𝑏 ⇒ 𝑝 = 𝑎 ⋅ 𝑏 ✓ 

## **Missing extra facts: an example** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ **1** ≤ n ≤ length(A) } m **:=** A[ **0** ];  i **:= 1** ; while (i < n) { if (A[i] > m) m **:=** A[i]; i **:=** i + **1** ; } 

{ m = max(A[ **0** ..n− **1** ]) } 

The maximum of an array, a search loop. The candidate says that  𝑚  is an upper bound of the visited part: 

_Proposed invariant:_ 

𝐼1:    (𝑚 ≥ 𝐴[𝑘]  for all  0 ≤ 𝑘 < 𝑖) ∧ 1 ≤ 𝑖 ≤ 𝑛 

- **Establishment** : the visited part only contains  𝐴[0], and  𝑚 = 𝐴[0].   ✓ 

- **Preservation** : the if statement keeps  𝑚 ≥  every visited element.   ✓ 

## **Missing extra facts: diagnosis and fix** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ **1** ≤ n ≤ length(A) } m **:=** A[ **0** ];  i **:= 1** ; while (i < n) { if (A[i] > m) m **:=** A[i]; i **:=** i + **1** ; } 

{ m = max(A[ **0** ..n− **1** ]) } 

At the exit,  𝑖 = 𝑛, so  𝑚 ≥ 𝐴[𝑘]  for all  0 ≤ 𝑘 < 𝑛. Is  𝑚  the maximum? 

- **✗ The postcondition at exit fails.** 

**A state that shows the failure** :  𝐴 = [6, 2, 7],  𝑛 = 3,  𝑖 = 3,  𝑚 = 1000. It satisfies  𝐼1 ∧ ¬𝐵, but  𝑚  is not in  𝐴. 

The candidate accepts a wrong state: it never says that  𝑚  is one of the elements. 

The fact that rules this state out is a witness, a position where  𝑚  is found: 

𝐼2:    𝐼1 ∧ (𝑚 = 𝐴[𝑗]  for some  0 ≤ 𝑗 < 𝑖) 

It is established at the start:  𝑚 = 𝐴[0]  and  𝑖 = 1, so  𝑗 = 0. 

**Rule of thumb: for search and max loops, include both the property of the visited part and the witness.** 

## **Which condition fails, and how to fix it** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

The check that fails, and the bad state it gives, tell us how to fix the invariant: 

|**Check that fails**|**The bad state**|**Type of problem**|**How to fix it**|
|---|---|---|---|
|**Establishment**|a real state at the first loop head that the<br>candidate rejects|too strong|weaken: replace constants by progress<br>variables|
|**Preservation**|a state that satisfies𝐼 ∧ 𝐵, but not𝐼<br>after one pass|missing extra facts|add the fact that the body needs|
|**Postcondition at**<br>**exit**|a state that satisfies𝐼 ∧ ¬𝐵, with the<br>counter beyond its final value|missing bounds|add the range of the counter|
|**Postcondition at**<br>**exit**|a state that satisfies𝐼 ∧ ¬𝐵, with a<br>wrong result|too weak|add the result computed so far, or a<br>witness|



**After each fix, check all three conditions again, since fixing one condition can break another.** 

