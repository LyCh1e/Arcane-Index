# L2 Intro to Testing

## Slide 1

INTRODUCTION TO TESTING 
CONCEPTS

## Slide 2

2
Error, Mistake:
• A human action that produces an incorrect result.
Fault, Bug, Defect:
• A flaw in a component/system that can cause the component/system to 
fail to perform its required function. 
• E.G., an incorrect requirement statement or data definition.
• (A defect in the requirement statement or data definition, if encountered during 
execution, would likely cause a failure of the component/system.)
Failure:
• Critical deviation of the component/system from its expected delivery, 
service or result.
TESTING FUNDAMENTALS: DEFINITIONS

## Slide 3

3
TESTING FUNDAMENTALS: DEFINITIONS
FAILURE
DEFECT
ERROR
DEFECT
Error creates a defect in 
the code (or software, 
documentation, etc.)
FAILURE
Defective code executed 
and the system fails; i.e., 
there is a failure. 
ERROR
Human makes a mistake 
in some aspect of 
Software Engineering

## Slide 4

4
“If the objective of testing was to prove that a program is free of bugs, 
then not only would testing be practically impossible, but it would also be 
theoretically impossible.”
Bill Hetzel, The Complete Guide for Software Testing, 1988
Core tenets of testing:
a) Testing can show that defects are present, but cannot prove that 
there are no defects. 
b) Testing reduces the probable presence of undiscovered defects in 
the software but, in the case where no defects are found while 
testing, it does not prove that the software is faultless.
TESTING FUNDAMENTALS: DEFINITIONS

## Slide 5

5
• Testing the Requirements
• Wrong, Missing, Inconsistency, Incomplete, Assumptions, 
Implementation, Ambiguous.
• Testing the Design
• Wrong logic, Wrong Algorithm, Conflicting Interfaces, 
Inconsistency with requirements. 
• Testing the Code
• Coding standards, Not initialized variables, Level of nesting, 
Assignments errors, Wrong condition, No exception handling, Poor 
documentation.
TESTING FUNDAMENTALS: DEFINITIONS

## Slide 6

6
Development testing: which is usually done by developers or testers in a 
controlled environment (either development or testing environment), the goal 
is to identify defects in the software by causing as many failures as possible 
and fix them.
Operational testing: is performed in order to evaluate a system in its 
operational environment. The main objective during this phase may be to 
assess the system reliability and availability.
Acceptance testing: is about meeting the customer business requirements 
and processes. Acceptance testing helps the user determine whether to 
accept the system or not.
Maintenance testing: aims to assure that no new defects will manifest as 
failures in the system after a change has been introduced to the system.
TESTING FUNDAMENTALS: DEFINITIONS

## Slide 7

7
TESTING FUNDAMENTALS: OVERVIEW
0%
5%
10%
15%
20%
25%
30%
35%
40%
45%
0
5
10
15
20
25
30
35
Requirements
Gathering +Design
Code Implementation
(Unit testing)
Integration + System
testing
Early Customer
Feedback
Post-production
Release
Average Cost per Defect
Proportional cost Bug distribution
Source: National Institute of standards and technology – the economic impact of inadequate infrastructure for software 
testing, May 02

## Slide 8

8
Testing is designed to: “Provide information regarding the quality of the 
software” Hetzel 1988
We are either Preventing Defects or Detecting Defects
• Effective testing: Focus on producing a desired result that answers 
the business goals for the system.
• Efficient testing: Focus on getting the largest amount of test 
coverage with the smallest number of tests.
TESTING FUNDAMENTALS: DEFINITIONS

## Slide 9

9
Testing Vs Debugging: essentially, nowadays these may refer to the 
same practice. However, traditionally you had system testers that 
tested the system to locate errors and get developers to fix. 
• Debugging is what developers do while writing code. Currently, 
these divisions between Tester and Developer have gone and 
developers are more responsible for their own code’s testing. 
TESTING FUNDAMENTALS: CLARIFICATIONS

## Slide 10

10
Pesticide Paradox: the more you test a software program, the more 
immune it becomes to your tests.
• To overcome this, tests must be continually developed and executed 
in different parts of the program to find more bugs. 
• 80% in 20% rule: tests should focus on the areas where testers 
expect to find and later observe high defect density
• Pareto principle: 80/20 rule also applies to defects and bugs.
TESTING FUNDAMENTALS: ISSUES

## Slide 11

11
VALIDATION VERIFICATION
Model/specification
inspection
Goal analysis
Integration 
testing
TESTING
Automated 
testing
Usability 
testing System 
testing
Regression 
testing
Acceptance 
testing
Unit 
testing
Modelling via formal 
methods eg UML
Prototyping
Style checkers
Proofs of 
correctness
Static analysis: 
Code 
Inspections
Robustness 
analysis
Consistency 
checking
Model 
Checking
V&V: VENN
Static 
analysis: 
Reviews

## Slide 12

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of these slides, nor PDFs, 
may be reproduced, or transmitted in any form or by 
and means, including recording, or other electronic or 
mechanical methods, without the prior permission of the 
creator, except in the case of certain other 
noncommercial uses permitted by copyright law.
