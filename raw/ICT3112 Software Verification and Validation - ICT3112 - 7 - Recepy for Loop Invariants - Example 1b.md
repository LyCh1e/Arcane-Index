# ICT3112 - 7 - Recepy for Loop Invariants - Example 1b

# **ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Recipe for Loop Invariants** . if ie | **Example 1 — Sum of Even Numbers Preservation, Exit and Termination Dr. David Sanan** ay Be = 

## **Example 1 so far: the candidate and the checks** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 4 · Bounds 

5 · Check 



<!-- Start of picture text -->
{ n ≥  0 }<br><!-- End of picture text -->

i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; 

s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

1.  Establishment:   {𝑃}  𝑖 ≔ 0;  𝑠 ≔ 0  {𝐼} 

**✓ established** 

2.  Preservation:   {𝐼 ∧ 𝐵}  𝑐  {𝐼} 

3.  Postcondition at exit:   𝐼 ∧ ¬𝐵 ⇒ 𝑄 

4.  Termination:   𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0   and   {𝐼 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼 ∧ 𝐸 < 𝐸0} 

**To check a triple we use the weakest precondition:** 

{𝑅}  𝑐  {𝑆}  holds when  𝑅 ⇒ 𝑤𝑝(𝑐, 𝑆) 𝑤𝑝(𝑥 ≔ 𝑒, 𝑆) = 𝑆[𝑥 ← 𝑒] 𝑤𝑝(𝑐1;  𝑐2, 𝑆) = 𝑤𝑝(𝑐1, 𝑤𝑝(𝑐2, 𝑆)) 

So we compute the weakest precondition from the last assignment to the first. 

𝑄:  𝑠 = 𝑛(𝑛+1) 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 1 · Preservation — the rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

Rule:   {𝐼 ∧ 𝐵}  𝑐  {𝐼} 

We replace  𝐼,  𝐵  and  𝑐  by our invariant, the guard and the body of the loop: 

{𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛} 𝑖 ≔ 𝑖 + 1; 𝑠 ≔ 𝑠 + 2⋅𝑖 

{𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛} 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑠 = 𝑛(𝑛+1) 𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

The triple holds when  𝐼 ∧ 𝐵 ⇒ 𝑤𝑝(𝑐, 𝐼). As before, we start from the last assignment: 

𝑤𝑝(𝑐, 𝐼) = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝑤𝑝(𝑠 ≔ 𝑠 + 2⋅𝑖, 𝐼)) 

We call  𝑅1 = 𝑤𝑝(𝑠 ≔ 𝑠 + 2⋅𝑖, 𝐼)  and  𝑅2 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝑅1). 

## **Example 1 · Preservation — computing the wp** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 𝑄:  𝑠 = 𝑛(𝑛+1) 

First the last assignment,  𝑠 ≔ 𝑠 + 2⋅𝑖: 

𝑅1 = 𝑤𝑝(𝑠 ≔ 𝑠 + 2⋅𝑖, 𝐼) = 𝐼[𝑠 ← 𝑠 + 2⋅𝑖] = (𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑠 ← 𝑠 + 2⋅𝑖] = (𝑠 + 2⋅𝑖 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛) 

Then the first assignment,  𝑖 ≔ 𝑖 + 1: 

𝑅2 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝑅1) = 𝑅1[𝑖 ← 𝑖 + 1] = (𝑠 + 2⋅𝑖 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛)[𝑖 ← 𝑖 + 1] = (𝑠 + 2⋅(𝑖+1) = (𝑖+1)((𝑖+1)+1) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) = (𝑠 + 2(𝑖+1) = (𝑖+1)(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛) 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

Every  𝑖  in  𝑅1  is replaced, including the one inside  𝑠 + 2⋅𝑖. The last line only simplifies (𝑖+1)+1  to  𝑖+2. 

## **Example 1 · Preservation — the implication** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } { s = n(n+ **1** ) } 

We need to show  𝐼 ∧ 𝐵 ⇒ 𝑅2: 

𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 𝑠 + 2(𝑖+1) = (𝑖+1)(𝑖+2) ∧ 0 ≤ 𝑖+1 ≤ 𝑛 

First conjunct. We replace  𝑠  using  𝑠 = 𝑖(𝑖+1)  from the left side: 𝑠 + 2(𝑖+1) = 𝑖(𝑖+1) + 2(𝑖+1) = (𝑖+1)(𝑖+2) ✓ 

Second conjunct. From  0 ≤ 𝑖  we get  0 ≤ 𝑖+1, and from  𝑖 < 𝑛  we get  𝑖+1 ≤ 𝑛.    ✓ 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 𝑄:  𝑠 = 𝑛(𝑛+1) 

**✓ preserved** 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

## **Example 1 · Postcondition at exit** 

2 · Trace 3 · Generalise 

1 · Q 

4 · Bounds 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->



<!-- Start of picture text -->
5 · Check<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

Rule:   𝐼 ∧ ¬𝐵 ⇒ 𝑄 

We replace  𝐼,  𝐵  and  𝑄  by our assertions: 

𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ ¬(𝑖 < 𝑛) ⇒ 𝑠 = 𝑛(𝑛+1) 

- ¬(𝑖 < 𝑛)  is the same as  𝑖 ≥ 𝑛. 

- Together with  𝑖 ≤ 𝑛  from the invariant, this gives  𝑖 = 𝑛. 

𝑃:  𝑛 ≥ 0 

- We replace  𝑖  by  𝑛  in  𝑠 = 𝑖(𝑖+1)  and we obtain  𝑠 = 𝑛(𝑛+1), which is  𝑄. 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

**✓ Q holds at the exit** 

### **Example 1 · Termination — the variant is bounded** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

We use the variant  𝐸 = 𝑛 − 𝑖. The termination rule has two conditions: 

(𝑎)    𝐼 ∧ 𝐵 ⇒ 𝐸 ≥ 0 (𝑏)    {𝐼 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼 ∧ 𝐸 < 𝐸0} 

𝐸0  is the value of  𝐸  before the iteration. We do not call it  𝑛, since  𝑛  is already a variable of our program. 

Condition (a). We replace  𝐼,  𝐵  and  𝐸: 

𝑃:  𝑛 ≥ 0 

𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ⇒ 𝑛 − 𝑖 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

From  𝑖 < 𝑛  we get  𝑛 − 𝑖 > 0, so  𝑛 − 𝑖 ≥ 0  holds. 

**✓ (a) holds** 

𝐸:  𝑛 − 𝑖 

## **Example 1 · Termination — the decrease rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

Condition (b):   {𝐼 ∧ 𝐵 ∧ 𝐸 = 𝐸0}  𝑐  {𝐼 ∧ 𝐸 < 𝐸0} The part  𝐼  of the postcondition is preservation, which we have already proved. So we only need to check  𝐸 < 𝐸0. We replace  𝐼,  𝐵,  𝐸  and  𝑐: 

{𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 ∧ 𝑖 < 𝑛 ∧ 𝑛 − 𝑖 = 𝐸0} 

𝑖 ≔ 𝑖 + 1; 𝑠 ≔ 𝑠 + 2⋅𝑖 

{𝑛 − 𝑖 < 𝐸0} 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

As before, we start from the last assignment: 

𝑄:  𝑠 = 𝑛(𝑛+1) 𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝐸:  𝑛 − 𝑖 

𝑤𝑝(𝑐, 𝑛 − 𝑖 < 𝐸0) = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝑤𝑝(𝑠 ≔ 𝑠 + 2⋅𝑖, 𝑛 − 𝑖 < 𝐸0)) 

We call  𝑅1 = 𝑤𝑝(𝑠 ≔ 𝑠 + 2⋅𝑖, 𝑛 − 𝑖 < 𝐸0)  and  𝑅2 = 𝑤𝑝(𝑖 ≔ 𝑖 + 1, 𝑅1). 

### **Example 1 · Termination — the variant decreases** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

First the last assignment,  𝑠 ≔ 𝑠 + 2⋅𝑖: 

𝑅1 = (𝑛 − 𝑖 < 𝐸0)[𝑠 ← 𝑠 + 2⋅𝑖] = (𝑛 − 𝑖 < 𝐸0) 

𝑠  does not appear in  𝑛 − 𝑖 < 𝐸0, so this substitution changes nothing. 

Then the first assignment,  𝑖 ≔ 𝑖 + 1: 

𝑅2 = 𝑅1[𝑖 ← 𝑖 + 1] = (𝑛 − 𝑖 < 𝐸0)[𝑖 ← 𝑖 + 1] 

= (𝑛 − (𝑖+1) < 𝐸0) 

𝑃:  𝑛 ≥ 0 𝐵:  𝑖 < 𝑛 𝑄:  𝑠 = 𝑛(𝑛+1) 𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 𝐸:  𝑛 − 𝑖 

We need to show  𝐼 ∧ 𝐵 ∧ 𝑛 − 𝑖 = 𝐸0 ⇒ 𝑅2. The part we use is: 

𝑛 − 𝑖 = 𝐸0 ⇒ 𝑛 − (𝑖+1) < 𝐸0 

This holds, since  𝑛 − (𝑖+1) = (𝑛 − 𝑖) − 1 = 𝐸0 − 1 < 𝐸0. 

**✓ the loop terminates** 

## **Example 1 — summary of the checks** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

1 · Q 

2 · Trace 

3 · Generalise 

4 · Bounds 

**5 · Check** 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; **while** (i < n) { i **:=** i + **1** ; 

s **:=** s + **2** *i; } 

{ s = n(n+ **1** ) } 

Establishment:   𝑛 ≥ 0 ⇒ 𝑤𝑝(𝑖 ≔ 0;  𝑠 ≔ 0, 𝐼) ✓ Preservation:   𝐼 ∧ 𝑖 < 𝑛 ⇒ 𝑤𝑝(𝑐, 𝐼) ✓ Postcondition at exit:   𝐼 ∧ ¬(𝑖 < 𝑛) ⇒ 𝑠 = 𝑛(𝑛+1) ✓ Termination:   𝐸 = 𝑛 − 𝑖  is bounded and decreases    ✓ 

- The conditions hold for our first candidate, so we do not need to change it. 

- For simple loops that accumulate a result, the recipe often gives the invariant at the first attempt. 

𝑃:  𝑛 ≥ 0 

𝐵:  𝑖 < 𝑛 

𝑄:  𝑠 = 𝑛(𝑛+1) 

𝐼:  𝑠 = 𝑖(𝑖+1) ∧ 0 ≤ 𝑖 ≤ 𝑛 

𝐸:  𝑛 − 𝑖 

