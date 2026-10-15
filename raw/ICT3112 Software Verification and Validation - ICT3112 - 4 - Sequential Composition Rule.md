# ICT3112 - 4 - Sequential Composition Rule

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Sequential Composition Rule** . if ie | **Dr. David Sanan** ay Be = 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{𝑄} 𝑆𝐾𝐼𝑃 {𝑄} 

**[SKIP]** 

**[ASSIGN]** {𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 

<u>{𝑃} 𝑐 ₁ {𝑅} {𝑅} 𝑐 ₂ {𝑄}</u> **[SEQ]** {𝑃} 𝑐; 𝑐 {𝑄}₁ ₂ 

<u>{𝑃 ∧ 𝐵} 𝑐 ₁ {𝑄} {𝑃 ∧ ¬𝐵} 𝑐 ₂ {𝑄}</u> **[IF]** {𝑃} 𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐 𝐸𝐿𝑆𝐸 𝑐 {𝑄}₁ ₂ 

<u>{𝐼 ∧ 𝐵} 𝑐 {𝐼}</u> {𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

**[WHILE]** 

𝑃 ⟶ 𝑃′    {𝑃′} 𝑐 {𝑄′} <u>𝑄′ ⟶ 𝑄</u> **[CONSEQUENCE]** {𝑃} 𝑐 {𝑄} 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

We have seen how to check a triple correctness when the program is a single assignment. 



And how to calculate the weakest precondition of a program from a given postcondition 

𝑤𝑝(𝑥 ≔ 𝑥 + 1, 𝑥 = 1) = {𝑥 = 0} 

**How to check correctness of a triple when we have a sequence of instructions?** 



The same that we _chain_ instructions, we _chain_ assertions. 



We need to find an intermediate assertion serving as postcondition of 𝑥 ≔ 𝑥 + 1 and at the same time precondition of 𝑥 ≔ 𝑥 + 2 

{𝑥 = 0} 𝑥 ≔ 𝑥 + 1 {𝑥 = 1} 𝑥 ≔ 𝑥 + 2 {𝑥 = 3} 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

We then need to prove the triples for each statement to obtain the correctness of their sequential composition 







# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**What happens when we have more than two instructions?** 

{b = b′  c = c′  a = a′∧ ∧ } c **:=** a + b; // i1 

<u>{𝑃} 𝑐 ₁ {𝑅₁} {𝑅₁} 𝑐 ₂ {𝑅₂}</u> 

a **:=** a - c; // i2 <u>{𝑃} 𝑐₁; 𝑐 ₂ {𝑅₂} {𝑅₂} 𝑐 ₃ {𝑄}</u> How many intermediate rules do we need b **:=** b + a // i3 to add when our program is a sequence {𝑃} 𝑐; 𝑐; 𝑐 {𝑄}₁ ₂ ₃ {b = **0** c = a′ + b′  a = −b′∧ ∧ } of 𝑛 instructions? 

We recursively apply the sequential composition rule starting from the end, adding intermediate assertions. 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**What happens when we have more than two instructions?** 

{b = b′  c = c′  a = a′∧ ∧ } c **:=** a + b; // i1 a **:=** a - c; // i2 b **:=** b + a // i3 {b = **0** c = a′ + b′  a = −b′∧ ∧ } 

<u>{𝑃} 𝑐 ₁ {𝑅₁} {𝑅₁} 𝑐 ₂ {𝑅₂} {𝑃} 𝑐₁; 𝑐 ₂ {𝑅₂} {𝑅₂} 𝑐 ₃ {𝑄}</u> {𝑃} 𝑐; 𝑐; 𝑐 {𝑄}₁ ₂ ₃ 

We recursively apply the sequential composition rule starting from the end, adding intermediate assertions. 

Problem: calculating the intermediate assertions become tedious, and maybe difficult sometimes Solution: _Weakest Precondition Calculus!_ 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

If we look at the branch tree, and knowing that we can apply wp for each instruction, intuitively we can apply wp on each instruction to calculate the (weakest) intermediate assertion 



From the top application we can observe that wp for sequential composition is: 

And when they are 𝑛 instructions: 

sequential composition is: 𝑤𝑝(𝑐; ⋯; 𝑐, 𝑄) = 𝑤𝑝(𝑐 ⋯ 𝑐_𝑛−1, 𝑤𝑝(𝑐, 𝑄)) ≡₁ ₙ ₁ ₙ 𝑤𝑝(𝑐; 𝑐, 𝑄) = 𝑤𝑝(𝑐, 𝑤𝑝(𝑐, 𝑄))₁ ₂ ₁ ₂ 𝑤𝑝(𝑐, 𝑤𝑝(𝑐, 𝑤𝑝(⋯, 𝑤𝑝(𝑐, 𝑄))))₁ ₂ ₙ 𝑤𝑝(𝑐; 𝑐; 𝑐, 𝑄) = 𝑤𝑝(𝑐, 𝑤𝑝(𝑐, 𝑤𝑝(𝑐, 𝑄)))₁ ₂ ₃ ₁ ₂ ₃ 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

Let’s now check the correctness of this code by using wp {𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} 𝑅₃ ≡ 𝑤𝑝(𝑖1, 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′) ≡ 𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′ c **:=** a + b; // i1 𝑅₂ ≡ 𝑤𝑝(𝑖2, 𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′ a **:=** a - c; // i2 𝑅₁ ≡ 𝑤𝑝(𝑖3, 𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ (𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) b **:=** b + a // i3 𝑄 ≡ {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 

Hoare triple calculated by WP 

{𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} c **:=** a + b; // i1 a **:=** a - c; // i2 b **:=** b + a // i3 {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

𝑃 ⟶ 𝑃′ 

{𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′} c **:=** a + b; // i1 a **:=** a - c; // i2 b **:=** b + a // i3 {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

{𝑃} 𝑐 {𝑄} 

{𝑃′} 𝑐 {𝑄′} 

We link the precondition we want to calculate 𝑃 with the one that we have calculated 𝑃′ by using the consequence rule 

We have calculated this Hoare Triple and it is correct by WP theory. 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

Consequence rule 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 

Hoare triple calculated by WP 

{𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} c **:=** a + b; // i1 a **:=** a - c; // i2 b **:=** b + a // i3 {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

𝑃 ⟶ 𝑃′ 

{𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′} c **:=** a + b; // i1 a **:=** a - c; // i2 b **:=** b + a // i3 {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

{𝑃} 𝑐 {𝑄} 

{𝑃′} 𝑐 {𝑄′} 

𝑄′ and 𝑄 are the same since we calculated the weakest precondition starting from 𝑄. 

We have calculated this Hoare Triple and it is correct by WP theory. 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> 

{𝑃} 𝑐 {𝑄} 

Consequence rule 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 

Hoare triple calculated by WP 

{𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} c **:=** a + b; // i1 a **:=** a - c; // i2 b **:=** b + a // i3 {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

𝑃 ⟶ 𝑃′ 

{𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′} c **:=** a + b; // i1 a **:=** a - c; // i2 b **:=** b + a // i3 {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

{𝑃} 𝑐 {𝑄} 

{𝑃′} 𝑐 {𝑄′} 

By calculating 𝑃 ⟶ 𝑃′ we have all the necessary to obtain {𝑃} 𝑐 {𝑄} 

We have calculated this Hoare Triple and it is correct by WP theory. 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

Consequence rule 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Let’s now check the correctness of this code by using wp 

{𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} 𝑅₃ ≡ 𝑤𝑝(𝑖1, 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′) ≡ Show that:𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′ c **:=** a + b; {𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} ⇒// i1 𝑅₂ ≡ 𝑤𝑝(𝑖2, 𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ 𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′ 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′ a **:=** a - c; // i2 𝑅₁ ≡ 𝑤𝑝(𝑖3, 𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ (𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) b **:=** b + a // i3 𝑄 ≡ {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Let’s now check the correctness of this code by using wp 

{𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} 𝑅₃ ≡ 𝑤𝑝(𝑖1, 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′) ≡ HINT!! Show that:𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′ c **:=** a + b; 𝑏 = 𝑏′ ∧ 𝑎 = 𝑎′ ≡// i1 𝑅₂ ≡ 𝑤𝑝(𝑖2, 𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ 𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′ 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′ a **:=** a - c; // i2 𝑅₁ ≡ 𝑤𝑝(𝑖3, 𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ (𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) b **:=** b + a // i3 𝑄 ≡ {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

# **Hoare Logic - Sequential Composition Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Let’s now check the correctness of this code by using wp {𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} 𝑅₃ ≡ 𝑤𝑝(𝑖1, 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′) ≡ HINT!! and that:𝑏 + 𝑎 − (𝑎 + 𝑏) = 0 ∧ (𝑏 + 𝑎) = 𝑎′ + 𝑏′ ∧ 𝑎 − (𝑏 + 𝑎) = −𝑏′ c **:=** a + b; {𝑏 = 𝑏′ ∧ 𝑐 = 𝑐′ ∧ 𝑎 = 𝑎′} ⇒ {𝑏 = 𝑏′ ∧ 𝑎 = 𝑎′}// i1 𝑅₂ ≡ 𝑤𝑝(𝑖2, 𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ 𝑏 + 𝑎 − 𝑐 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 − 𝑐 = −𝑏′ a **:=** a - c; // i2 𝑅₁ ≡ 𝑤𝑝(𝑖3, 𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) ≡ (𝑏 + 𝑎 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′) b **:=** b + a // i3 𝑄 ≡ {𝑏 = 0 ∧ 𝑐 = 𝑎′ + 𝑏′ ∧ 𝑎 = −𝑏′} 

