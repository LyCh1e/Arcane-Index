# ICT3112 - 7 - Recepy for Loop Invariants - 0a

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **Recipe, Steps 1 to 3 Dr. David Sanan** ay Be = 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**A recipe for discovering invariants** 

# **Where does an invariant come from?** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } { s = n(n+ **1** )/ **2** } 



<!-- Start of picture text -->
𝐼 = ?<br><!-- End of picture text -->

All we have is the program and its contract. Nobody gives us the invariant. 

The while rule needs an invariant before it says anything. Without one, we cannot even start the proof. 

**Let’s rebuild the invariant of this loop by following a recipe, step by step.** 

# **What the recipe can promise** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Finding an invariant and checking an invariant are two different activities: 

### **Proposing a candidate** 

Steps  1 · Q,  2 · Trace,  3 · Generalise,  4 · Bounds This part is a heuristic. No algorithm finds the invariant of every loop. The steps give us good candidates for the loops of this course. 

**Checking a candidate** Step  5 · Check This part is mechanical. Establishment, preservation and the postcondition at exit are implications that we can prove, or show to be false. 

When a check fails, the failed check and a state that breaks it tell us what to try next. So we never have to guess blindly: we propose, check, and refine. 

# **Step 1: start from the postcondition** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**1 · Q** 

2 · Trace 

3 · Generalise 

4 · Bounds 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } 

{ s = n(n+ **1** )/ **2** } 

Everything we know is written in the contract, so we start from the postcondition: 

𝑄:    𝑠 = 𝑛(𝑛 + 1)/2 

   - **Progress variable** :  𝑖. It counts the passes, from 0 up to  𝑛. 

   - **Result variable** :  𝑠.  𝑄  constrains its value at the end. 

- At the exit,  𝐼 ∧ ¬𝐵  must give  𝑄. So  𝑄  is the material we use to build  𝐼. 

- |NY 

# **Step 2: trace the values at the loop head** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

**2 · Trace** 

3 · Generalise 

4 · Bounds 5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } 

{ s = n(n+ **1** )/ **2** } 

An invariant is true at every loop head, so we look at the loop heads: 

|**At the loop head**|𝑖|𝑠|
|---|---|---|
|before pass 1|0|0|
|before pass 2|1|1|
|before pass 3|2|3|
|before pass 4|3|6|



We look for a relation whose shape is the same on every row: 𝑠  takes the values  0, 1, 3, 6, that is  1 + 2 + … + 𝑖 = 𝑖(𝑖 + 1)/2. Oe 

The trace is taken at the loop head, after the whole body has run. So it also settles whether the formula needs  𝑖  or  𝑖 − 1. 

# **Step 3: generalise the postcondition** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

**3 · Generalise** 

4 · Bounds 5 · Check 

At a loop head the loop is half-way, and  𝑠  holds a partial result. So  𝑄, as it is { n ≥ **0** } written, is false there. i **:= 0** ;  s **:= 0** ; while (i < n) { 𝑠 = 𝑛(𝑛 + 1)/2      ⟶      𝑠 = 𝑖(𝑖 + 1)/2 i **:=** i + **1** ; s **:=** s + i; (replace  𝑛  by  𝑖) } { s = n(n+ **1** )/ **2** } Replacing the final value  𝑛  by the progress variable  𝑖  turns “at the end” into “so far”. The result matches the trace: we found the same formula in two independent ways. re 

# **Step 3 in detail: what exactly gets replaced?** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

**3 · Generalise** 

4 · Bounds 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { i **:=** i + **1** ; s **:=** s + i; } 

{ s = n(n+ **1** )/ **2** } 

“The final value” is the value that the progress variable has at the exit: 

¬𝐵 ∧ bounds  ⇒    𝑖 = 𝑛       (the final value of  𝑖  is  𝑛) 

Generalising is a substitution in  𝑄: we replace that final value by the progress variable. 



<!-- Start of picture text -->
𝐼 = 𝑄[𝑛 ≔ 𝑖]<br><!-- End of picture text -->

Sanity check:  𝐼[𝑖 ≔ 𝑛] ≡ 𝑄. If putting  𝑛  back in place of  𝑖  does not give  𝑄, we replaced the wrong thing. 

# **Step 3 in detail: which occurrences?** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

1 · Q 

2 · Trace 

**3 · Generalise** 

4 · Bounds 

5 · Check 

{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { s **:=** s + n; i **:=** i + **1** ; } { s = n · n } 

𝑄  may mention  𝑛  several times, and not every  𝑛  is the final value of  𝑖. 

𝑄:    𝑠 = 𝑛 ⋅ 𝑛 𝑠 = 𝑖 ⋅ 𝑖       or       𝑠 = 𝑖 ⋅ 𝑛  ? One  𝑛  counts the passes. The other  𝑛  is the amount added in each pass, a constant of the problem. Which one is which? - 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

## **Step 3 in detail: the trace and the checks decide** 



<!-- Start of picture text -->
1 · Q<br><!-- End of picture text -->

2 · Trace **3 · Generalise** 4 · Bounds 

|Trace<br>**3 · Genera**|**lise**|4 · Bou|nds|5 · Check|
|---|---|---|---|---|
|**At the loop head (**𝑛 = 4**)**|𝑖|𝑠|𝑖 ⋅ 𝑛|𝑖 ⋅ 𝑖|
|before pass 1|0|0|0|0|
|before pass 2|1|4|4|1|
|before pass 3|2|8|8|4|
|before pass 4|3|12|12|9|



{ n ≥ **0** } i **:= 0** ;  s **:= 0** ; while (i < n) { s **:=** s + n; i **:=** i + **1** ; } { s = n · n } 

Preservation for each candidate: 

𝑠 = 𝑖 ⋅ 𝑛:   we need  𝑠 + 𝑛 = (𝑖 + 1) ⋅ 𝑛, and  (𝑖 + 1) ⋅ 𝑛 = 𝑖 ⋅ 𝑛 + 𝑛.   ✓ 𝑠 = 𝑖 ⋅ 𝑖:   we need  𝑠 + 𝑛 = (𝑖 + 1)<sup>2</sup> , but  (𝑖 + 1)<sup>2</sup> = 𝑖<sup>2</sup> + 2𝑖 + 1.   ✗ 

Replace the occurrences that count the passes, and keep the constants of the problem. When in doubt, trace, and then check. 

