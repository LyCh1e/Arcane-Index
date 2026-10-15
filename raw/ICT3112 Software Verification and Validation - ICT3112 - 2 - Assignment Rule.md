# ICT3112 - 2 - Assignment Rule

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Assignment Rule** . if ie | **Dr. David Sanan** ay Be 

# **Hoare Logic - Assignment Rule** 

**[SKIP]** 

{𝑄} 𝑆𝐾𝐼𝑃 {𝑄} 

<u>{𝑃} 𝑐 ₁ {𝑅} {𝑅} 𝑐 ₂ {𝑄}</u> **[SEQ]** {𝑃} 𝑐; 𝑐 {𝑄}₁ ₂ 

<u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> {𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

**[WHILE]** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**[ASSIGN]** 

{𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 

<u>{𝑃 ∧ 𝐵} 𝑐 ₁ {𝑄} {𝑃 ∧ ¬𝐵} 𝑐 ₂ {𝑄}</u> **[IF]** {𝑃} 𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐 𝐸𝐿𝑆𝐸 𝑐 {𝑄}₁ ₂ 

𝑃 ⟶ 𝑃′    {𝑃′} 𝑐 {𝑄′} <u>𝑄′ ⟶ 𝑄</u> **[CONSEQUENCE]** {𝑃} 𝑐 {𝑄} 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
Assigned Variable Assignment expression<br>𝑥 ≔ 𝑥′<br><!-- End of picture text -->

We assign variable 𝑥′ to variable 𝑥 

If we want to assert that the value of 𝑥 is equal to zero after the assignment 



What precondition do we need to set to make this Hoare triple correct? 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Assigned Variable Assignment expression 



<!-- Start of picture text -->
𝑥 ≔ 𝑥′<br><!-- End of picture text -->

We assign variable 𝑥′ to variable 𝑥 

If we want to assert that the value of 𝑥 is equal to zero after the assignment 

{𝑥′ = 0} 𝑥 ≔ 𝑥′ {𝑥 = 0} 

𝑥′ must be equal to 0 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Assigned Variable Assignment expression 𝑥 ≔ 𝑦 + 𝑧 

We assign expression 𝑦 + 𝑧 to variable 𝑥 

If we want to assert that the value of 𝑥 is equal to some constant 𝑐 after the assignment 

{??} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 = 𝑐} 

What precondition do we need to set to make this Hoare triple correct? 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Assigned Variable 

Assignment expression 



<!-- Start of picture text -->
𝑥 ≔ 𝑦 + 𝑧<br><!-- End of picture text -->

We assign expression 𝑦 + 𝑧 to variable 𝑥 

If we want to assert that the value of 𝑥 is equal to some constant 𝑐 after the assignment 

{𝑦 + 𝑧 = 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 = 𝑐} 

𝑦 + 𝑧 must be equal to 𝑐 

If we want to assert that the value of 𝑥 is greater than some constant 𝑐 after the assignment 

{??} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐} 

What precondition do we need to set to make this Hoare triple correct? 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Assigned Variable 

Assignment expression 

𝑥 ≔ 𝑦 + 𝑧 

We assign expression 𝑦 + 𝑧 to variable 𝑥 

If we want to assert that the value of 𝑥 is equal to some constant 𝑐 after the assignment 

{𝑦 + 𝑧 = 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 = 𝑐} 

𝑦 + 𝑧 must be equal to 𝑐 

If we want to assert that the value of 𝑥 is greater than some constant 𝑐 after the assignment 

{𝑦 + 𝑧 > 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐} 

𝑦 + 𝑧 must be greater than 𝑐 

If we want to assert that the value of 𝑥 is greater than some constant 𝑐 after the assignment and that 𝑦 is greater than some constant 𝑐′ 

{??} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐 ∧ 𝑦 > 𝑐′} 

What precondition do we need to set to make this Hoare triple correct? 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Assigned Variable 

Assignment expression 

𝑥 ≔ 𝑦 + 𝑧 

We assign expression 𝑦 + 𝑧 to variable 𝑥 

If we want to assert that the value of 𝑥 is equal to some constant 𝑐 after the assignment 

{𝑦 + 𝑧 = 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 = 𝑐} 

𝑦 + 𝑧 must be equal to 𝑐 

If we want to assert that the value of 𝑥 is greater than some constant 𝑐 after the assignment 

{𝑦 + 𝑧 > 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐} 

𝑦 + 𝑧 must be greater than 𝑐 

If we want to assert that the value of 𝑥 is greater than some constant 𝑐 after the assignment and that 𝑦 is greater than some constant 𝑐′ 

{𝑦 + 𝑧 > 𝑐 ∧ 𝑦 > 𝑐′} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐 ∧ 𝑦 > 𝑐′} 𝑦 + 𝑧 must be greater than 𝑐 and 𝑦 must be greater than 𝑐′ 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**We can see a pattern here** 

{𝑥′ = 0} 𝑥 ≔ 𝑥′ {𝑥 = 0} {𝑦 + 𝑧 = 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 = 𝑐} {𝑦 + 𝑧 > 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐} {𝑦 + 𝑧 > 𝑐 ∧ 𝑦 > 𝑐′} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐 ∧ 𝑦 > 𝑐′} 

{??} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐 ∧ 𝑦 > 𝑥} 

# **Hoare Logic - Assignment Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**We can see a pattern here** 

{𝑥′ = 0} 𝑥 ≔ 𝑥′ {𝑥 = 0} {𝑦 + 𝑧 = 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 = 𝑐} {𝑦 + 𝑧 > 𝑐} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐} {𝑦 + 𝑧 > 𝑐 ∧ 𝑦 > 𝑐′} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐 ∧ 𝑦 > 𝑐′} {𝑦 + 𝑧 > 𝑐 ∧ 𝑦 > 𝑦 + 𝑧} 𝑥 ≔ 𝑦 + 𝑧 {𝑥 > 𝑐 ∧ 𝑦 > 𝑥} 

**[ASSIGN]** 

{𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 

If the result of executing the assignment 𝑥 ≔ 𝐸 satisfies the predicate 𝑄 then its precondition is equal to substituting the assigned variable 𝑥 by the assignment expression 𝐸 in 𝑄 

# **Hoare Logic - Assignment Rule** 

{𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**[ASSIGN]** 

{??} 𝑦 ≔ 𝑦 + 1 {𝑦 = 2} Assigned Variable: 𝑦 Assignment expression: 𝑦 + 1 

# **Hoare Logic - Assignment Rule** 

{𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**[ASSIGN]** 

{(𝑦 = 2)[𝑦 ← 𝑦 + 1]} 𝑦 ≔ 𝑦 + 1 {𝑦 = 2} {𝑦 + 1 = 2} 𝑦 ≔ 𝑦 + 1 {𝑦 = 2} {𝑦 = 1} 𝑦 ≔ 𝑦 + 1 {𝑦 = 2} 

# **Hoare Logic - Assignment Rule** 

{𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**[ASSIGN]** 

{??} 𝑦 ≔ 𝑦 + 𝑥 {𝑦 = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′} {(𝑦 = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′)[𝑦 ← 𝑦 + 𝑥]} 𝑦 ≔ 𝑦 + 𝑥 {𝑦 = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′} {𝑦 + 𝑥 = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′} 𝑦 ≔ 𝑦 + 𝑥 {𝑦 = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′} {𝑦 + 𝑥′ = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′} 𝑦 ≔ 𝑦 + 𝑥 {𝑦 = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′} {𝑦 = 𝑦′ ∧ 𝑥 = 𝑥′} 𝑦 ≔ 𝑦 + 𝑥 {𝑦 = 𝑦′ + 𝑥′ ∧ 𝑥 = 𝑥′} 

# **Hoare Logic - Weakest Precondition Calculus** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare Logic gives us several rules to determine whether a Hoare triple is correct. Especially when we have large programs, it is convenient to have a methodology telling us how to calculate the precondition, that can be automated. 

Dijkstra’s Weakest Precondition Calculus follows similar principles to Hoare logic, allowing us to calculate the weakest precondition of a program and the postcondition we are looking for. 

𝑤𝑝(𝑐, 𝑄) 

Biggest (weakest) set of states (precondition) such that starting from a state belonging to it the execution of 𝑐 ends in a state satisfying 𝑄 

{𝑤𝑝(𝑐, 𝑄)} 𝑐 {𝑄} 

∀𝑃. (𝑃 ⇒ 𝑤𝑝(𝑐, 𝑄)) ⇒ {𝑃} 𝑐 {𝑄} 

# **Hoare Logic - Weakest Precondition Calculus** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

∀𝑃. (𝑃 ⇒ 𝑤𝑝(𝑐, 𝑄)) ⇒ {𝑃} 𝑐 {𝑄} 𝑤𝑝(𝑥 ≔ 𝐸, 𝑄) = 𝑄[𝑥 ← 𝐸] ∀𝑃. (𝑃 ⇒ 𝑄[𝑥 ← 𝐸]) ⇒ {𝑃} 𝑐 {𝑄} 

The weakest precondition for the assignment rule matches the Hoare logic triple for the assignment rule. 

{𝑤𝑝(𝑥 ≔ 𝐸, 𝑄)} 𝑐 {𝑄} 

# **Hoare Logic - Weakest Precondition Calculus** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{𝑤𝑝(𝑥 ≔ 𝐸, 𝑄)} 𝑐 {𝑄} 𝑤𝑝(𝑥 ≔ 𝐸, 𝑄) = 𝑄[𝑥 ← 𝐸] 

{??} 𝑥 ≔ 𝑦 ∗ 𝑧 {𝑥 > 0} 

# **Hoare Logic - Weakest Precondition Calculus** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{𝑤𝑝(𝑥 ≔ 𝐸, 𝑄)} 𝑐 {𝑄} 𝑤𝑝(𝑥 ≔ 𝐸, 𝑄) = 𝑄[𝑥 ← 𝐸] 

{𝑤𝑝(𝑥 ≔ 𝑦 ∗ 𝑧, 𝑄)} 𝑥 ≔ 𝑦 ∗ 𝑧 {𝑥 > 0} 𝑤𝑝(𝑥 ≔ 𝑦 ∗ 𝑧, 𝑄) = 𝑄[𝑥 ← 𝑦 ∗ 𝑧] 𝑤𝑝(𝑥 ≔ 𝑦 ∗ 𝑧, 𝑄) = (𝑥 > 0)[𝑥 ← 𝑦 ∗ 𝑧] 𝑤𝑝(𝑥 ≔ 𝑦 ∗ 𝑧, 𝑄) = 𝑦 ∗ 𝑧 > 0 

{𝑦 ∗ 𝑧 > 0} 𝑥 ≔ 𝑦 ∗ 𝑧 {𝑥 > 0} 

