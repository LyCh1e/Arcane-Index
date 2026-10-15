# ICT3112 - 5 - Conditional Rule

# **ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Conditional Rule** . if ie | **Dr. David Sanan** ay Be 

## **Hoare Logic - Conditional Rule** 

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

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ P } **if** (B) { c₁ 

On a conditional statement, from the initial state σ, we find two cases: a)  σ satisfies the branching condition in that case it will execute the if branch. It will execute 𝑐₁ 

} **else** { 

b)  σ does not satisfy the branching condition in that case it will execute the else branch 𝑐₂ 

c₂ 

} 

{ Q } 

Some equivalence that will be useful in what it follows 

- σ ∈ 𝑃 is equivalent to saying:  σ satisfies 𝑃 and 𝑃 σ is True 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ P } **if** (B) { c₁ } **else** { 

**a)** σ **satisfies the branching condition in that case it will execute the if branch. It will execute** 𝑐₁ 

Because of the definition of a Hoare triple: a Hoare triple is true if starting from any state belonging to 𝑃 the execution of 𝑐 ends in a state satisfying 𝑄, if the execution of 𝑐 terminates. 

1) σ ∈ 𝑃 

c₂ } { Q } 

Because σ satisfies the branching condition it must belong to the set of states satisfying B 

2) σ ∈ 𝑃 ∧ σ ∈ 𝐵 

- 3) From 1) and 2) any state before executing 𝑐₁ satisfies 𝑃 ∧ 𝐵 

- 4) After 𝑐₁ is executed the conditional statement finishes and it must satisfy the postcondition 𝑄. Therefore when 𝑐₁ is executed it must satisfy 𝑄 

{𝑃 ∧ 𝐵} 𝑐 {𝑄}₁ 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ P } **if** (B) { c₁ } **else** { 

**b)** σ **does not satisfy the branching condition in that case it will execute the else branch. It will execute** 𝑐₂ 

Because of the definition of a Hoare triple: a Hoare triple is true if starting from any state belonging to 𝑃 the execution of 𝑐 ends in a state satisfying 𝑄, if the execution of 𝑐 terminates. 

1) σ ∈ 𝑃 

c₂ } { Q } 

Because σ does not satisfy the branching condition it must belong to the set of states not satisfying B 

2) σ ∈ 𝑃 ∧ σ ∉ 𝐵 

- 3) From 1) and 2) any state before executing 𝑐₂ satisfies 𝑃 ∧ ¬𝐵 

- 4) After 𝑐₂ is executed the conditional statement finishes and it must satisfy the postcondition 𝑄. Therefore when 𝑐₂ is executed it must satisfy 𝑄 

{𝑃 ∧ ¬𝐵} 𝑐 {𝑄}₂ 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ P } **if** (B) { c₁ } <u>{𝑃 ∧ 𝐵} 𝑐 ₁ {𝑄} {𝑃 ∧ ¬𝐵} 𝑐 ₂ {𝑄}</u> **else** { **[IF]** c₂ {𝑃} 𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐 𝐸𝐿𝑆𝐸 𝑐 {𝑄}₁ ₂ } { Q } 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**One example!!** 

{ x + y = **0** } **if** (x = y) { x **:=** y + **1** } **else** { x **:= 1** − x } { x = y + **1** } 

𝑃 = 𝑥 + 𝑦 = 0 𝐵 = 𝑥 = 𝑦 

{𝑥 + 𝑦 = 0 ∧ 𝑥 = 𝑦} 𝑥 ≔ 𝑦 + 1 {𝑥 = 𝑦 + 1} 

{𝑥 + 𝑦 = 0 ∧ ¬(𝑥 = 𝑦)} 𝑥 ≔ 1 − 𝑥 {𝑥 = 𝑦 + 1} 

{𝑥 + 𝑦 = 0} 𝐼𝐹 𝑥 = 𝑦 𝑇𝐻𝐸𝑁 𝑥 ≔ 𝑦 + 1 𝐸𝐿𝑆𝐸 𝑥 ≔ 1 − 𝑥 {𝑥 = 𝑦 + 1} 

Prove the correctness of these triples: 

{𝑥 + 𝑦 = 0 ∧ 𝑥 = 𝑦} 𝑥 ≔ 𝑦 + 1 {𝑥 = 𝑦 + 1} {𝑥 + 𝑦 = 0 ∧ ¬(𝑥 = 𝑦)} 𝑥 ≔ 1 − 𝑥 {𝑥 = 𝑦 + 1} 

## **Hoare Logic - Conditional Rule** 

The definition of wp is: 𝑤𝑝(𝑖𝑓 𝐵 𝑡ℎ𝑒𝑛 𝑐 𝑒𝑙𝑠𝑒 𝑐) =₁₁ ₂ 𝐵 ⇒ 𝑤𝑝(𝑐, 𝑄) ∧ ¬𝐵 ⇒ 𝑤𝑝(𝑐, 𝑄)₁₁ ₂ 

{ x + y = **0** } 𝑤𝑝(𝑖𝑓 𝐵 𝑡ℎ𝑒𝑛 𝑐 𝑒𝑙𝑠𝑒 𝑐) =₁₁ ₂ **if** (x = y) { x **:=** y + **1** 𝐵 ⇒ 𝑤𝑝(𝑐, 𝑄) ∧ ¬𝐵 ⇒ 𝑤𝑝(𝑐, 𝑄)₁₁ } **else** { x **:= 1** − x In our example } 𝑤𝑝(𝑥 ≔ 𝑦 + 1, 𝑥 = 𝑦 + 1) = 𝑇𝑟𝑢𝑒 { x = y + **1** } 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

Check that it is true! 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ x + y = **0** } **if** (x = y) { x **:=** y + **1** } **else** { x **:= 1** − x } { x = y + **1** } 

The definition of wp is: 𝑤𝑝(𝑖𝑓 𝐵 𝑡ℎ𝑒𝑛 𝑐 𝑒𝑙𝑠𝑒 𝑐) =₁ ₂ 𝐵 ⇒ 𝑤𝑝(𝑐, 𝑄) ∧ ¬𝐵 ⇒ 𝑤𝑝(𝑐, 𝑄)₁ ₂ 

In our example 𝑤𝑝(𝑥 ≔ 𝑦 + 1, 𝑥 = 𝑦 + 1) = 𝑇𝑟𝑢𝑒 𝑤𝑝(𝑥 ≔ 1 − 𝑥, 𝑥 = 𝑦 + 1) = 1 − 𝑥 = 𝑦 + 1 𝑤𝑝(𝑖𝑓, 𝑥 = 𝑦 + 1) = 𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧ 𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 

{ x + y = **0** } **if** (x = y) { 𝑃 ⟶ 𝑃′ x **:=** y + **1** } **else** { x **:= 1** − x } { x = y + **1** } {𝑃} 𝑐 {𝑄} 

### Hoare triple calculated by WP 

By the consequence rule, the triple will be correct if: 



<!-- Start of picture text -->
{𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧<br>𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1}<br>if  (x = y) {<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃′} 𝑐 {𝑄′}<br><!-- End of picture text -->

𝑃 ⇒ 𝑤𝑝(𝑖𝑓, 𝑄) 

We link the precondition we want to calculate 𝑃 with the one that we have calculated 𝑃′ by using the consequence rule 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

Consequence rule 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 



<!-- Start of picture text -->
{ x + y =  0 }<br>if  (x = y) {<br>𝑃 ⟶ 𝑃′<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃} 𝑐 {𝑄}<br><!-- End of picture text -->

Hoare triple calculated by WP 

By the consequence rule, the triple will be correct if: 



<!-- Start of picture text -->
{𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧<br>𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1}<br>if  (x = y) {<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃′} 𝑐 {𝑄′}<br><!-- End of picture text -->

𝑃 ⇒ 𝑤𝑝(𝑖𝑓, 𝑄) 

𝑄′ and 𝑄 are the same since we calculated the weakest precondition starting from 𝑄. 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

Consequence rule 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 



<!-- Start of picture text -->
{ x + y =  0 }<br>if  (x = y) {<br>𝑃 ⟶ 𝑃′<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃} 𝑐 {𝑄}<br><!-- End of picture text -->

### Hoare triple calculated by WP 

By the consequence rule, the triple will be correct if: 



<!-- Start of picture text -->
{𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧<br>𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1}<br>if  (x = y) {<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃′} 𝑐 {𝑄′}<br><!-- End of picture text -->

𝑃 ⇒ 𝑤𝑝(𝑖𝑓, 𝑄) 

By calculating 𝑃 ⟶ 𝑃′ we have all the necessary to obtain {𝑃} 𝑐 {𝑄} 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

Consequence rule 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 



<!-- Start of picture text -->
{ x + y =  0 }<br>if  (x = y) {<br>𝑃 ⟶ 𝑃′<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃} 𝑐 {𝑄}<br><!-- End of picture text -->

### Hoare triple calculated by WP 

By the consequence rule, the triple will be correct if: 



<!-- Start of picture text -->
{𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧<br>𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1}<br>if  (x = y) {<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃′} 𝑐 {𝑄′}<br><!-- End of picture text -->

𝑥 + 𝑦 = 0 ⇒ 𝑤𝑝(𝑖𝑓, 𝑥 = 𝑦 + 1) 

By calculating 𝑃 ⟶ 𝑃′ we have all the necessary to obtain {𝑃} 𝑐 {𝑄} 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

Consequence rule 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

Hoare triple that we want to calculate 

{ x + y = **0** } **if** (x = y) { 𝑃 ⟶ 𝑃′ x **:=** y + **1** } **else** { x **:= 1** − x } { x = y + **1** } {𝑃} 𝑐 {𝑄} 

### Hoare triple calculated by WP 

By the consequence rule, the triple will be correct if: 



<!-- Start of picture text -->
{𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧<br>𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1}<br>if  (x = y) {<br>    x  :=  y +  1<br>}<br>else {<br>    x  := 1  − x<br>}<br>{ x = y +  1 }<br>{𝑃′} 𝑐 {𝑄′}<br><!-- End of picture text -->

𝑥 + 𝑦 = 0 ⇒ 𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧ 𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1 

By calculating 𝑃 ⟶ 𝑃′ we have all the necessary to obtain {𝑃} 𝑐 {𝑄} 

𝑃 ⟶ 𝑃′ <u>{𝑃′} 𝑐 {𝑄′} 𝑄′ ⟶ 𝑄</u> {𝑃} 𝑐 {𝑄} 

Consequence rule 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Show that the implication is correct!** 

{ x + y = **0** } **if** (x = y) { x **:=** y + **1** } **else** { 

x **:= 1** − x } 

{ x = y + **1** } 

𝑥 + 𝑦 = 0 ⇒ 𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧ 𝑥 ≠ 𝑦 ⇒ 1 − 𝑥 = 𝑦 + 1 

Remember:  𝑥 + 𝑦 = 0  is equal to  𝑥 = −𝑦 When we have  𝐴 ⇒ 𝐵  we assume  𝐴  and we show  𝐵 For example, if we need to show  𝑥 = 𝑦 + 1 ⇒ 𝑥 > 𝑦 We assume  𝑥 = 𝑦 + 1 

and based in this assumption we need to show that  𝑥 > 𝑦  is true From the assumption we substitute  𝑥  with  𝑦 + 1  in  𝑥 > 𝑦 we need to show that  𝑦 + 1 > 𝑦 **Which is trivially true!** 

## **Hoare Logic - Conditional Rule** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**Show that the implication is correct!** 

{ x + y = **0** } **if** (x = y) { x **:=** y + **1** } 

**else** { 

x **:= 1** − x } 

{ x = y + **1** } 

𝑥 + 𝑦 = 0 ⇒ 𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧ 𝑥 ≠ 𝑦 ⇒ 𝑥 = −𝑦 

Since  𝑥 + 𝑦 = 0 ≡ 𝑥 = −𝑦  we need to show 

𝑥 = −𝑦 ⇒ 𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 ∧ 𝑥 ≠ 𝑦 ⇒ 𝑥 = −𝑦 

From here we need to show: 

1)  𝑥 = −𝑦 ⇒ 𝑥 = 𝑦 ⇒ 𝑇𝑟𝑢𝑒 

✓   (Because  𝐴 ⇒ 𝑇𝑟𝑢𝑒) 

2)  𝑥 = −𝑦 ⇒ 𝑥 ≠ 𝑦 ⇒ 𝑥 = −𝑦 

✓ 

𝑥 = −𝑦 ⇒ 𝑥 = −𝑦 ∨ 𝑥 = 𝑦 𝑥 = −𝑦 ∨ 𝑥 = 𝑦 ≡ 𝑥 ≠ 𝑦 ⇒ 𝑥 = −𝑦 

(Because  𝐴 ⇒ 𝐴 ∨ 𝐵) (Because  𝐴 ⇒ 𝐵 ≡ ¬𝐴 ∨ 𝐵) 

