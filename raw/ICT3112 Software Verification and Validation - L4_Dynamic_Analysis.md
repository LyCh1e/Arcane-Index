# L4 Dynamic Analysis

## Slide 1

1
DYNAMIC ANALYSIS: 
SOFTWARE TESTING

## Slide 2

2
“You can hope your software works or you can know it works—through 
software testing” –Software Testing Primer, Nick Jenkins
• Testing is the process of executing a program with the intent of 
finding errors.
• Testing can be used to show the presence of bugs, but never to show 
their absence.
SOFTWARE TESTING: INTRODUCTION

## Slide 3

3
Good Testing Practices part 1:
1. A good test case has a high probability of detecting undiscovered 
defects, not necessarily showing the program works correctly.
2. It is insufficient to be the only one testing your own code/program.
3. Every test case should have a description of the expected result.
4. Write test cases for valid as well as invalid input conditions.
SOFTWARE TESTING: BEST PRACTICES

## Slide 4

4
Good Testing Practices part 2:
5. Thoroughly inspect the results of each test.
6. Ensure Testability is a key objective in your software design.
7. Never alter the program to make testing easier.
8. Testing, like almost every other activity, must start with objectives.
SOFTWARE TESTING: BEST PRACTICES

## Slide 5

5
Core types of testing: Black box vs White box testing 
• Black box includes all testing where only the 
inputs and outputs are considered
• The inner workings are unknown, or just simply 
not considered for the purposes of Black Box testing.
• White box testing also evaluated the inputs 
and outputs 
• but specifically considers the inner workings of 
the software
SOFTWARE TESTING: INTRODUCTION

## Slide 6

6
Core types of testing: Regression vs Retesting
Retesting and Regression testing are subtly different
• Retesting:
• The process of rerunning tests that found defects to ensure that the defect has been 
fixed.
• Regression testing:
• Is the repeating of tests in parallel areas of the code to ensure that the code fixes do 
not introduce new errors or unexpected behaviours elsewhere.
“In empirical studies it’s estimated that up to 50% of bug fixes actually 
introduce additional errors into the code”–Software Testing Primer, Nick Jenkins
SOFTWARE TESTING: INTRODUCTION

## Slide 7

7
V-Model of Testing
SOFTWARE TESTING: OVERVIEW Verification
Validation

## Slide 8

8
UNIT TESTING (AKA COMPONENT TESTING)
• Objective: Verify functionality and search for defects in software 
components that are separately testable. E.g., classes, functions.
• Scope: Test functional and non-functional characteristics of software 
components. Non-functional characteristics include performance (e.g., 
DB access), resource allocation (e.g., memory leaks), usability, etc.
• Derived from: Component specifications and requirements, detailed 
design documents.
• Conductor: Developers.
SOFTWARE TESTING: LEVELS

## Slide 9

9
INTEGRATION TESTING
• Objective: To test program interfaces and confirm that programs/ 
components are linked together correctly.
• Scope: Test functional and non-functional characteristics of integration 
between components. E.g., non-functional characteristics like 
performance.
• Derived from: Software and system design, interface specification 
and design documents, use cases.
• Conductor: Developers, testing team (depending on level of 
integration).
SOFTWARE TESTING: LEVELS

## Slide 10

10
SYSTEM TESTING
• Objective: Test the behavior of the system/product as defined by 
project scope, to verify its readiness for acceptance testing.
• Scope: Test the functional and non-functional requirements of the 
system. 
• Derived from: System requirement specifications, use cases, functional 
specification, risk analysis report.
• Conductor: Testing team. (Depending on company size, developers.)
SOFTWARE TESTING: LEVELS

## Slide 11

11
ACCEPTANCE TESTING
• Objective: Establish confidence in the system, parts of the system or 
specific characteristics of the system. Assess system readiness for 
deployment.
• Scope: Test system functional and performance requirements, also test 
system reliability and usability. 
• Derived from: User requirements, system requirements, business 
processes, use cases, risk analysis report.
• Conductor: Customer or users of the system.
SOFTWARE TESTING: LEVELS

## Slide 12

12
ACCEPTANCE TESTING: OPERATIONAL TESTING
• Alpha (a) testing: Simulated or actual operational testing by 
users/customers, or independent test team on site, but not by the 
developers. Commonly used for mainstream software as a form of 
internal acceptance testing.
• Beta (b) testing : Operational testing by potential or existing 
users/customers at external site determining whether 
component/system satisfies the user/customer needs and fits within 
business processes. Commonly used as a form of external acceptance 
testing for mainstream software to acquire feedback from the market.
SOFTWARE TESTING: LEVELS

## Slide 13

13
MAIN TESTING TYPES
• Functional: testing functionality performed by the system. I.E., testing what 
the system should do. (based on requirements specification, use cases and 
etc.) This is predominantly Black box testing.
• Non-functional: testing characteristics of software product. Testing attributes 
of a component/system that don’t relate to functionality, e.g. reliability, 
efficiency, usability, maintainability and portability: “How (well) the system 
works”. Usually Black-box and considers external behavior.
• Structural: testing internal structures of components/systems. (White box)
• Retesting & Regression: testing based on changes done to the software.
SOFTWARE TESTING: TYPES OF TESTING

## Slide 14

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of these slides, nor PDFs, 
may be reproduced, or transmitted in any form or by 
and means, including recording, or other electronic or 
mechanical methods, without the prior permission of the 
creator, except in the case of certain other 
noncommercial uses permitted by copyright law.
