# ICT3112 - 3 - Consequence Rule

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Consequence Rule** . if ie | **Dr. David Sanan** ay Be 

# **Hoare Logic - Consequence Rule** 



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

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triples obtained by the reasoning rules we have seen until now ([SKIP] and [ASSIGN]) are specifications given in terms of weakest precondition. Suppose we want to verify the following triple {𝑥 > 120} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101} 

Applying the Assignment rule, we obtain the following {(𝑥 > 101)[𝑥 ← 𝑥 + 1]} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101} {𝑥 + 1 > 101} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101} {𝑥 > 100} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101} 

How to bridge the gap? 

Consequence Rule 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

A first version helping to bridge the precondition we want to verify with the precondition we obtain through Hoare Logic 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄}</u> {𝑃} 𝑐 {𝑄} 

If we have proven {𝑃′} 𝑐 {𝑄} and 𝑃 ⟶ 𝑃′ then we obtain {𝑃} 𝑐 {𝑄} 

**Back to the previous example** 

{𝑥 > 120} ⟶ {𝑥 > 100} <u>{𝑥 > 100}</u> 𝑥 ≔ 𝑥 + 1 <u>{𝑥 > 101}</u> {𝑥 > 120} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101} 

{𝑥 > 120} = {𝑥 == 121 ∨ 𝑥 == 122 ∨ ⋯} ⟶ {𝑥 > 100} = {𝑥 == 101 ∨ 𝑥 == 102 ∨ ⋯ ∨ 𝑥 == 121 ∨ 𝑥 == 122 ⋯} 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

A first version helping to bridge the precondition we want to verify with the precondition we obtain through Hoare Logic 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄}</u> {𝑃} 𝑐 {𝑄} 

If we have proven {𝑃′} 𝑐 {𝑄} and 𝑃 ⟶ 𝑃′ then we obtain {𝑃} 𝑐 {𝑄} 

**Back to the previous example** 

{𝑥 > 120} ⟶ {𝑥 > 100} <u>{𝑥 > 100}</u> 𝑥 ≔ 𝑥 + 1 <u>{𝑥 > 101}</u> {𝑥 > 120} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101} 

{𝑥 > 120} ≡ {121, 122, …} ⊆ {𝑥 > 100} ≡ {101, 102, … 121, 122, …} 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**What happens with the postcondition?** 

{𝑥 > 100} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101 ∨ 𝑥 < 99} 

Complex postconditions make the verification more difficult. Especially when the program to verify includes loops and branch conditions. BS 

We can apply the consequence rule over the postcondition to strengthen it and make it simpler for the verification {𝑥 > 100} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101} 

<u>{𝑃} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

{𝑥 > 100} 𝑥 ≔ 𝑥 + 1 <u>{𝑥 > 101}</u> 𝑥 > 101 ⟶ 𝑥 > 101 ∨ 𝑥 < 99 {𝑥 > 100} 𝑥 ≔ 𝑥 + 1 {𝑥 > 101 ∨ 𝑥 < 99} 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

## **The complete rule** 

Weaken the precondition 𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄}</u> {𝑃} 𝑐 {𝑄} 

Strengthen the postcondition <u>{𝑃} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> **[CONSEQUENCE]** {𝑃} 𝑐 {𝑄} 

Textbooks often name this rule from its conclusion: the conclusion has a stronger precondition and a weaker postcondition than the triple we proved. 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Let’s apply both** 𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100} {𝑃} 𝑐 {𝑄} Weaken the precondition Strengthen the postcondition 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 𝑃 ⟶ 𝑃′ {1 ≤ 𝑥 ≤ 9} 𝑦 ≔ 𝑥 ∗ 10 {10 ≤ 𝑦 ≤ 90} 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 

𝑃   {2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100}   𝑄 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Let’s apply both** 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

{2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100} Weaken the precondition Strengthen the postcondition 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 {1 ≤ 𝑥 ≤ 9} 𝑦 ≔ 𝑥 ∗ 10 {10 ≤ 𝑦 ≤ 90} 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 𝑄′ ⟶ 𝑄 

𝑃   {2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100}   𝑄 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Let’s apply both** 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

{2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100} Weaken the precondition Strengthen the postcondition 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 {1 ≤ 𝑥 ≤ 9} 𝑦 ≔ 𝑥 ∗ 10 {10 ≤ 𝑦 ≤ 90} {𝑃′} 𝑐 {𝑄′} 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 

𝑃   {2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100}   𝑄 

# **Hoare Logic - Consequence Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Let’s apply both** 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

{2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100} Weaken the precondition Strengthen the postcondition 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 2 ≤ 𝑥 ≤ 8 ⟶ 1 ≤ 𝑥 ≤ 9 {1 ≤ 𝑥 ≤ 9} 𝑦 ≔ 𝑥 ∗ 10 {10 ≤ 𝑦 ≤ 90} 10 ≤ 𝑦 ≤ 90 ⟶ 0 ≤ 𝑦 ≤ 100 

𝑃   {2 ≤ 𝑥 ≤ 8} 𝑦 ≔ 𝑥 ∗ 10 {0 ≤ 𝑦 ≤ 100}   𝑄 

{𝑃} 𝑐 {𝑄} 

