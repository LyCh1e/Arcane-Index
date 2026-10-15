# ICT3112 - 0 - Introduction - Copy

# **ICT3112 Introduction to Formal Verification of Programs** . if ie | **Dr. David Sanan** ay Be 

### **Why Formal Verification????** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

## **Why Formal Verification????** 

### **Why Formal Verification????** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

**A Fact:** 

**Software Has Errors** 

**But why?** 



<!-- Start of picture text -->
Warning message<br>Se Error! Cancel<br><!-- End of picture text -->

### **Why Formal Verification????** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

### **Because software is complex!!!** 

**Programs are very large** 

**Humans are prone to have mistakes!** 

**Those errors are often in critical systems** 

### **Why Formal Verification????** 

**Therac-25 and excess of radiation** 

**Ariane 5 explosion Problem:** Conversion overflow from a software that wasn’t necessary when the software was deployed **Consequence:** 370M$ lost 

**Problem:** Arithmetic overflow and removal of HW to control certain errors. **Consequence:** At least 3 people died 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Patriot missile System Problem:** desynchronization of clocks **Consequence:** 28 soldiers died and about 100 were wounded 

### **Why Formal Verification????** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE<br>pee<br>SiT OF<br><!-- End of picture text -->

#### **Blockchain** 



<!-- Start of picture text -->
4 function MetaCoin() {<br>5 lances[tx.origin] = 10f 2;<br>6}a<br>1<br>8 all — |<br>9 nction sendCoin(addressances [msg.sender] ro mmarunt)false;Ce fProot<br>10 psg. ender] - 5<br>ll * wae eceiver] += a._ LI<br>16 :<br>18}. = ®!<br>17 dasa 0 0<br>a) oou <<<br>—— % i.<br><!-- End of picture text -->

- $0.25bn in 2020 

- $1.55bn in 2021 

- $3.6bn in 2022 

- $1.2bn until Sep 2023 

### **Verification vs Validation** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
Testing<br>VALIDATION VERIFICATION<br>Model/Specification Unit Testing Style Checkers<br>Acceptance Testing<br>Inspection<br>Regression  Integration<br>Testing Consistency<br>Testing<br>Goal Analysis Usability Testing Checking<br>System Automated  Static Analysis:<br>Testing Testing<br>Code Inspections<br>Modelling via Formal Methods<br>Robustness<br>(e.g., UML)<br>Model Proofs of<br>Analysis<br>Checking Correctness<br>Prototyping<br>Formal Methods<br>Methods based on testing (Unit Cases, Fuzzing, etc) are incomplete and cannot<br>find all errors<br><!-- End of picture text -->

### **Why Formal Verification????** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

**Errors are often in critical systems** 

Methods based on testing (Unit Cases, Fuzzing, etc) are incomplete and cannot find all errors 

**Errors in Critical System are fatal. We want zero errors** 

### **Why Formal Verification????** 

{x=0} **void main** (){ x **:=** x+ **1** ; x **:=** x+ **1** ; } 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

If x is a global variable initialized to 0 at the beginning of the program, what is its value at the end? 

{x=2} 

### **Why Formal Verification????** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

∧ {x=x’  y=y’} 



<!-- Start of picture text -->
void main (){<br>   x := x+y;<br>   y := x-y;<br>   x := x-y;<br>}<br><!-- End of picture text -->

**I promise you that it is true!!!** 

∧ {x=y’  y=x’} 



<!-- Start of picture text -->
INSTITUTE OF<br>Logic and System Properties TECHNOLOGY<br>SiTee<br>ee — ee ee ee<br>I|<br>Proposition<br>I |<br>Hoare<br>al Logic<br>II<br>Logic<br>I<br>(deductive<br>I | Reasoning)<br>First Order  Logic<br>|<br>System<br>Logic |<br>I<br>I|<br>Temporal<br>|<br>Logic<br>I |<br>Higher- (Automatic<br>I|<br>Order Logic Reasoning)<br>I |<br>Assertions<br>L_-—-—-—-—~——! (Properties) I  promise  prove it to you that is true!!!<br>Program Reasoning<br>State Machine Reasoning<br><!-- End of picture text -->

### **Before Going Further** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

This course relies on logical concepts you learnt in the first year: 

How to formalize real world statements in Propositional and First Order Logic 

How to prove assertions in those logics (at least informally). 

