# ICT3112 - 1 - Hoare Logic and Skip Rule - Copy

# **ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Skip Rule** . if ie | **Dr. David Sanan** ay Be 

## **Axiomatic Semantics (Hoare Logic)** 



<!-- Start of picture text -->
INSTITUTE OF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
Sir Tony Hoare<br>My PhD<br>Myself Supervisor My PhD<br>Colleague<br>dl | 1 J , 4 a y yi ), a<br>L L i } B D 2019.10.11 02:07<br><!-- End of picture text -->

Hoare Logic provides a systematic approach to calculate whether a program **C** reaches a set of states **Q (postcondition)** when starting from an assumption **P (precondition)** , if the execution of **C** terminates. 

Hoare triple   {𝑃} 𝐶 {𝑄} 



<!-- Start of picture text -->
Precondition {𝑥 = 0 ∧ 𝑦 = 1}<br>𝑥 ≔ 𝑥 + 𝑦<br>Postcondition<br>{𝑥 = 1 ∧ 𝑦 = 1}<br><!-- End of picture text -->

## **Axiomatic Semantics (Hoare Logic)** 



<!-- Start of picture text -->
INSTITUTEOF<br>TECHNOLOGY<br>SiTee<br><!-- End of picture text -->



<!-- Start of picture text -->
Sir Tony Hoare<br>My PhD<br>Myself Supervisor My PhD<br>Colleague<br>ie ‘al r ga 4<br>gy f A le Bie<br>7moe ff ‘ | bi4r | &a2019.10.11 02:07<br><!-- End of picture text -->



<!-- Start of picture text -->
{𝑥 = 0 ∧ 𝑦 = 1}<br><!-- End of picture text -->

Represents the set of states where 𝑥 = 0 and 𝑦 = 1 

{𝑥 ≥ 0 ∧ 𝑦 ≥ 1} 

Represents the set of states {(𝑥 = 0, 𝑦 = 1), (𝑥 = 1, 𝑦 = 1), ⋯ , (𝑥 = 0, 𝑦 = 2), (𝑥 = 1, 𝑦 = 2), ⋯ } {(𝑥 = 𝑚, 𝑦 = 𝑛). 𝑚 ≥ 0 ∧ 𝑛 ≥ 1} 

## **Axiomatic Semantics (Hoare Logic)** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

⊢ {𝑄} 𝑆𝐾𝐼𝑃 {𝑄} 

**[SKIP]** 

⊢ {𝑄[𝑥 ← 𝐸]} 𝑥 ≔ 𝐸 {𝑄} 

**[ASSIGN]** 

⊢ {𝑃} 𝑐 ₁ <u>{𝑅}    ⊢ {𝑅} 𝑐 ₂ {𝑄}</u> **[SEQ]** ⊢ {𝑃} 𝑐; 𝑐 {𝑄}₁ ₂ 

⊢ {𝑃 ∧ 𝐵} 𝑐 ₁ <u>{𝑄}    ⊢ {𝑃 ∧ ¬𝐵} 𝑐 ₂ {𝑄}</u> **[IF]** ⊢ {𝑃} 𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐 𝐸𝐿𝑆𝐸 𝑐 {𝑄}₁ ₂ 

⊢ {𝐼 ∧ 𝐵} 𝑐 {𝐼} 

⊢ {𝐼} 𝑊𝐻𝐼𝐿𝐸 𝐵 𝐷𝑂 𝑐 {𝐼 ∧ ¬𝐵} 

**[WHILE]** 

𝑃 ⟶ 𝑃′    ⊢ {𝑃′} 𝑐 {𝑄′} <u>𝑄′ ⟶ 𝑄</u> **[CONSEQUENCE]** ⊢ {𝑃} 𝑐 {𝑄} 

## **Why we need SKIP: how a program executes** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

A program runs one step at a time. At each step we look at a pair made of the program still to run and the current state. 

⟨ program still to run , current state ⟩ 

SKIP is the program with nothing left to run. It has no step to take. 

**SKIP marks the end of the first program in a sequence** 

⟨𝑥 ≔ 1; 𝑦 ≔ 𝑥 + 1, (𝑥 = 0, 𝑦 = 0)⟩ → ⟨𝑆𝐾𝐼𝑃; 𝑦 ≔ 𝑥 + 1, (𝑥 = 1, 𝑦 = 0)⟩ → ⟨𝑦 ≔ 𝑥 + 1, (𝑥 = 1, 𝑦 = 0)⟩ → ⟨𝑆𝐾𝐼𝑃, (𝑥 = 1, 𝑦 = 2)⟩ 

the program and the state at the start 

the assignment is done, so it becomes SKIP 𝑆𝐾𝐼𝑃; 𝑐 steps to 𝑐, so the second program starts 

only SKIP is left, so the execution has terminated 

### **SKIP fills a missing ELSE** 

**What this means for Hoare logic** 

𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐   is written as   𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐 𝐸𝐿𝑆𝐸 𝑆𝐾𝐼𝑃 If 𝐵 is false:   ⟨𝐼𝐹 𝐵 𝑇𝐻𝐸𝑁 𝑐 𝐸𝐿𝑆𝐸 𝑆𝐾𝐼𝑃, 𝑠⟩ → ⟨𝑆𝐾𝐼𝑃, 𝑠⟩ The execution ends and the state 𝑠 is unchanged. 

SKIP takes no step, so the final state is the initial state. Any 𝑄 that holds before SKIP still holds after it. ⊢ {𝑄} 𝑆𝐾𝐼𝑃 {𝑄} 

## **Hoare Logic SKIP** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

Skip does not change the values of any variable. 

The set of variables in a program together with their values is called _program state_ Skip does not change the program state 

{𝑥 = 0} 𝑆𝐾𝐼𝑃 {𝑥 = 0} {𝑥 = 𝑛} 𝑆𝐾𝐼𝑃 {𝑥 = 𝑛} {𝑥 = 𝑛 ∧ 𝑦 = 𝑚} 𝑆𝐾𝐼𝑃 {𝑥 = 𝑛 ∧ 𝑦 = 𝑚} {𝑥 ≥ 𝑛} 𝑆𝐾𝐼𝑃 {𝑥 ≥ 𝑛} 

⊢ {𝑄} 𝑆𝐾𝐼𝑃 {𝑄} 

**[SKIP]** 

{𝑥 = 0} 𝑆𝐾𝐼𝑃 {𝑥 = 1} **INVALID TRIPLE!!!!!!** 

