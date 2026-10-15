# ICT3112 - 7 - Discovering Loop Invariants - 0b

**ICT3112 Introduction to Formal Verification of Programs Hoare Logic – Discovering & Reasoning about Loop Invariants** . if ie | **Fitting the Specification Dr. David Sanan** ay Be = 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ x ≥ **0** } while (x > **0** ) x **:=** x − **1** ; { x = **0** } 

We have already seen that the invariant  𝐼 ≡ 𝑥 ≥ 0  works for this loop: 

- Establishment:  𝑥 ≥ 0 ⇒ 𝑥 ≥ 0 

- Preservation:  𝑥 ≥ 0 ∧ 𝑥 > 0  gives  𝑥 ≥ 1, so after  𝑥 ≔ 𝑥 − 1  we still have 𝑥 ≥ 0 

𝐼 ≡ 𝑥 ≥ 0 

- Postcondition at exit:  𝑥 ≥ 0 ∧ 𝑥 ≤ 0 ⇒ 𝑥 = 0 

**What if** 𝑥 **can be any integer number?** 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ x = X } while (x > **0** ) x **:=** x − **1** ; { x = **0** } 

**What if** 𝑥 **can be any integer number?** 

If  𝑥 ≥ 0, we are in the case we have already seen, and the invariant works: 

- with  𝑥 > 0  the loop runs, and eventually  𝑥  gets the value zero; 

𝐼 ≡ 𝑥 ≥ 0 

- with  𝑥 = 0  the loop is not executed, and the program ends with  𝑥 = 0. 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ x = X } while (x > **0** ) x **:=** x − **1** ; { x = **0** } 

**What if** 𝑥 **can be any integer number?** 

If  𝑥 < 0, the guard  𝑥 > 0  is false from the start. The loop is not executed, and  𝑥  keeps its initial value  𝑋, which is negative. 

𝐼 ≡ 𝑥 ≥ 0 

For example, with  𝑋 = −5:  the loop does not run,  𝑥 = −5  at the end, and  𝑥 = 0  is false. 

**Not only the invariant is a problem: the postcondition itself is wrong for this program. We first need to adapt the postcondition.** 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ x = X } while (x > **0** ) x **:=** x − **1** ; { (x < **0** x = X)∧ ∨ x = **0** } 

**What if** 𝑥 **can be any integer number?** 

The new postcondition: 

(𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 = 0 

𝐼 ≡ 𝑥 ≥ 0 

If  𝑥  is less than zero, then  𝑥  does not change. Otherwise, it becomes zero. 

Does our invariant still fit this specification? 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ x = X } while (x > **0** ) x **:=** x − **1** ; { (x < **0** x = X)∧ ∨ x = **0** } 

𝐼 ≡ 𝑥 ≥ 0 

**What if** 𝑥 **can be any integer number?** 

The previous invariant still fits the postcondition at exit: 𝑥 ≥ 0 ∧ 𝑥 ≤ 0    ⇒    (𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 = 0 

Why?  𝑥 ≥ 0 ∧ 𝑥 ≤ 0  means  𝑥 = 0, which is the second part of the “or”. So the implication holds. 

- **✓ The exit is not the problem** 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ x = X } while (x > **0** ) x **:=** x − **1** ; { (x < **0** x = X)∧ ∨ x = **0** } 

𝐼 ≡ 𝑥 ≥ 0 

**What if** 𝑥 **can be any integer number?** 

However, the precondition does not imply the invariant: 𝑥 = 𝑋    ⇏    𝑥 ≥ 0 

When  𝑥  is a negative number, it is not greater than or equal to zero. For example,  𝑋 = −5:  𝑥 = −5  is true, but  𝑥 ≥ 0  is false. 

- **✗ Establishment fails** 

𝑥 ≥ 0 _is still an invariant of the runs that start with_ 𝑥 ≥ 0 _. It just does not fit this specification._ 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->

{ x = X } while (x > **0** ) x **:=** x − **1** ; { (x < **0** x = X)∧ ∨ x = **0** } 

**What if** 𝑥 **can be any integer number?** 

The new invariant only needs to extend the previous one, to say that the loop does not modify  𝑥  when  𝑥  is a negative number. That is exactly the way the postcondition does it. 

𝐼 ≡ 𝑥 ≥ 0 

𝐼 ≡ (𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 ≥ 0 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>INSTITUTE OF<br>TECHNOLOGY<br><!-- End of picture text -->

{ x = X } while (x > **0** ) x **:=** x − **1** ; { (x < **0** x = X)∧ 

∨ x = **0** } 

**What if** 𝑥 **can be any integer number?** 

This invariant satisfies the three loop conditions, and the loop terminates: 

## **Establishment** 

𝑥 = 𝑋 ⇒ (𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 ≥ 0 

𝐼 ≡ (𝑥 < 0 ∧ 𝑥 = 𝑋) 

∨ 𝑥 ≥ 0 

## **Preservation** 

((𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 ≥ 0) ∧ 𝑥 > 0  gives  𝑥 ≥ 1, so after  𝑥 ≔ 𝑥 − 1  we have 𝑥 ≥ 0 

## **Postcondition at exit** 

((𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 ≥ 0) ∧ 𝑥 ≤ 0    ⇒    (𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 = 0 

## **Termination** 

variant  𝑉 = 𝑥:  𝑥 > 0  while the loop runs, and every iteration decreases it by one 

# **Invariants are as good as they fit our specification** 



<!-- Start of picture text -->
SINGAPORE<br>TECHNOLOGY<br>SiT INSTITUTE OF<br><!-- End of picture text -->



<!-- Start of picture text -->
{ x = X }<br>while (x >  0 )<br>    x  :=  x −  1 ;<br>{ (x <  0   x = X)∧<br>∨ x =  0 }<br><!-- End of picture text -->

Let’s compare the two invariants for this specification: 

**Postcondition at Invariant Establishment Preservation exit** 𝑥 ≥ 0 **✗ ✓ ✓** (𝑥 < 0 ∧ 𝑥 = 𝑋) ∨ 𝑥 ≥ 0 **✓ ✓ ✓** 

𝐼 ≡ (𝑥 < 0 ∧ 𝑥 = 𝑋) 

∨ 𝑥 ≥ 0 

An invariant is a contract for the loop: a property of every snapshot at the loop head. 

A loop has many invariants. An invariant is only useful if it fits the specification we want to prove: the precondition implies it, the body preserves it, and together with the negated guard it gives the postcondition. 

