# L5 0 Whitebox Testing Intro

## Slide 1

1
WHITEBOX TESTING: 
INTRODUCTION

## Slide 2

2
WHITEBOX TESTING: INTRODUCTION
Component
(Unit) 
testing
Integration 
testing
Whitebox 
testing 
techniques
System 
testing
WB testing: “a procedure 
to derive and/or select 
test cases based on an 
analysis of the internal 
structure of a component 
or system.”

## Slide 3

3
WHITEBOX TESTING: INTRODUCTION
WB testing: “a procedure 
to derive and/or select 
test cases based on an 
analysis of the internal 
structure of a component 
or system.”
Whitebox 
testing 
techniques
Path testing
Data flow testing
Decision testing
Condition testing
LCSAJ coverage
Statement testing
Techniques and topics:
Categories:
• Control flow: used to identify the execution paths 
through a module/program and design test 
cases to cover those paths.
• Data flow: used to identify the improper use of 
data values that occur due to coding errors.

## Slide 4

4
WHITEBOX TESTING: 
DATA FLOW

## Slide 5

5
Used to identify defects caused due to improper use of data values, e.g.:
• References to the value of a variable without first assigning a value to it.
• Variables defined and then destroyed without being used.
• Variables destroyed and then used.
• Variables defined and then re-defined again.
Data flow testing is done by:
• Static testing (reviewing and verification of data flow graph); 
• Dynamic testing – design and execute test cases where:
• Every “define” is traced to each of its “uses”.
• Every “use” is traced from its corresponding “define”.
• For every variable create at least one test case for a define-use pair.
WHITEBOX TESTING: DATA FLOW
Thank you 
modern IDEs!
Thankfully, 
IDEs do a lot 
of this static 
checking for 
us. However, 
it’s important 
to understand 
what these 
checks are.

## Slide 6

6
WHITEBOX TESTING: 
CONTROL FLOW

## Slide 7

7
• A testing approach that identifies the execution paths. 
• Creates and executes test cases to cover those paths. 
• Exercising all control flows can be impractical or impossible. 
Concerns:
• Should we execute all possible paths?
• If not, how many paths do we need to execute?
• What level of coverage is to be achieved?
• I.e., what is a sufficient coverage level?
WHITEBOX TESTING: CONTROL FLOW
for (x=0; x<100; x++)
for (y=0; y<100; y++)
for (z=0; z<100; z++)
print (“testing”);
How many paths 
exist that need to be 
tested here?

## Slide 8

8
•Control flow graphs: 
• a sequence of events (paths) to be followed in the execution level 
of a component or system.
•Control flow paths: 
• a sequence of events, e.g. executable statements, in a component 
or system, starting from its entry to its exit point.
WHITEBOX TESTING: CONTROL FLOW

## Slide 9

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of these slides, nor PDFs, 
may be reproduced, or transmitted in any form or by 
and means, including recording, or other electronic or 
mechanical methods, without the prior permission of the 
creator, except in the case of certain other 
noncommercial uses permitted by copyright law.
