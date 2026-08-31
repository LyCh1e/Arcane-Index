# L6 2 Blackbox Testing DecisionTableTesting and StateTransitionTesting

## Slide 1

1

## Slide 2

2
BLACKBOX TESTING: 
DECISION TABLE TESTING 
and STATE TRANSITION 
TESTING

## Slide 3

3
BLACKBOX TESTING: INTRODUCTION
BB testing: “a procedure to 
derive and/or select test cases 
based on an analysis of the 
specification, either functional 
or non-functional, of a 
component or system without 
reference to its internal 
structure.”
BlackBox 
testing 
techniques
Techniques and topics:
Boundary values analysis
State transition testing
Equivalence partitioning
Use case testing
Decision table testing

## Slide 4

4
BLACKBOX TESTING: 
DECISION TABLE TESTING

## Slide 5

5
• What are Decision tables for?
• They are a precise way to model 
complicated logic. 
• The representation is a useful 
basis for test design.
• How do they work? 
• Decision tables associate 
decisions (system conditions) with 
actions to be performed. 
• Decisions & Actions can either be 
true or false (Yes/No)
BLACKBOX TESTING: DECISION TABLE TESTING
Rule 1 Rule 2
Decision 1 Yes/No Yes/No
Decision 2 Yes/No Yes/No
Decision 3 ---------- Yes/No
Action 1 Yes/No Yes/No
Action 2 Yes/No Yes/No
Columns yield business rule that 
defines a unique combination of 
conditions that result in the 
execution of actions 
Triggering 
conditions 
unreachable 
decision

## Slide 6

6
• For example 1: Let’s consider a system that calculates the price of movie tickets:
• Basic price $20
• Students receive 10% discount 
• Young people under 21 years receive 5% discount 
• Discounts are accumulative 
BLACKBOX TESTING: DECISION TABLE TESTING
Rule 1 Rule 2 Rule 3 Rule 4
Is the customer Yes Yes No No
a student?
Aged below 21? Yes No Yes No
Give a discount 15% 10% 5% None
up to:

## Slide 7

7
How to get to tests? 
• Tests execute a combination of decisions shown in a decision table.
• They should be designed to cover each rule (column) at least once. 
Constraints of Decision Tables:
• The order decisions are evaluated doesn’t affect the resulting action. 
• The order rules are evaluated doesn’t affect the resulting action. 
• Once a rule has been satisfied and action is taken, no other rule needs to be examined.
• If multiple actions can result from the execution of a single rule, the order in which the 
actions take place is ignored.
• For n binary decisions, there should be 2ncases considered (max).
• Find test input values that will force each test to result in the action.
BLACKBOX TESTING: DECISION TABLE TESTING
Source: Boris Beizer “Software Testing Techniques”

## Slide 8

8
• For example 2: Let’s consider that our movie system asks for a movie id and checks its 
validity (3 digits between 100-300), if invalid the system returns to “Welcome Screen”.
• If valid, the system asks for payment details and checks its validity. If the payment details are 
valid, it supplies the movie ticket, if invalid it rejects payment.
BLACKBOX TESTING: DECISION TABLE TESTING
Rule 1 Rule 2 Rule 3
Movie ID is valid? N Y Y
Is payment valid? ---- N Y
Show welcome screen Y N N
Reject payment N Y N
Supply movie tickets N N Y
Input: 
Movie ID = 209
card num=“12345678”
Input: 
Movie ID = 113
card num=“12”
Input: 
Movie ID = 332
Test Case

## Slide 9

9
BLACKBOX TESTING: 
STATE TRANSITION TESTING

## Slide 10

10
What is State Transition Testing for?
• Test design technique in which test cases are designed to execute valid and invalid state
transitions in a system. 
How to use State Transition Testing? 
• Model your system using states, the transitions between those states, the inputs/events which 
cause those transitions, and the outputs/actions which may result from those transitions.
Specific applications of State Transition Testing:
• Used to test protocols between systems, humans and machines, and between system modules.
• User transaction flows where transactions can stay in the system indefinitely (e.g., online users).
• High level control function within an operating system (e.g. security handling of read/write 
permissions). 
BLACKBOX TESTING: STATE TRANSITION TESTING

## Slide 11

11
• State = describes a combination of attributes or conditions of interest. 
It’s a set of variables, characterizing a unique situation in a system, 
that have specific values.
• Includes initial, final states; 
• and states may have a duration
• Transition = As a result of inputs (events) to a state, the system’s state changes: 
makes a transition. Transitions link states (can return to the same state). 
• caused by associated events or inputs
• when in starting state and an event or input occurs then transition to target state
• Input/Event= cause transitions, marked beside the line with directional arrows (transitions).
• Events or inputs are considered instantaneous phenomena in our models (e.g., user inputs)
• Output/Action = associated with every combination of input and transition
BLACKBOX TESTING: STATE TRANSITION TESTING
State
Input / output

## Slide 12

12
BLACKBOX TESTING: STATE TRANSITION TESTING
Current state Input Output Next state 
Wait for recognized face 
(S1)
Face = 
unrecognized
System keeps 
door locked
Wait for recognized 
face (S1)
Wait for recognized face 
(S1)
Face = recognized System unlocks 
door 
Face Recognized 
unlocked door (S2)
Face Recognized 
unlocked door (S2)
Set lock off Sensors disabled 
& alarm off
????
Unspecified behavior 
(S1 doesn’t capture 
state after this 
transition)
Face=recognized / 
System unlocks 
door
Door reclosed / 
sensors activated
Set lock Off/ 
sensors disabled & 
alarm off
face detected / 
system on 
No face 
detected / 
system idle
S1
Wait for 
recognized 
Face
S2 Face 
Recognized 
unlocked 
door
S3
Wait to 
Activate 
System
Face=unrecognized / 
System keeps door 
locked
For example 1, Let’s consider a Face recognition door lock.
Although S1 doesn’t 
capture state after this 
transition, let’s assume it’s 
accurate, so not to 
complicate our example

## Slide 13

13
How to derive a State Transition diagram for testing?
• The information is derived from system specification, not from reading or executing code.
• The states must be unique and of a finite number.
What do we learn from mapping a system in this way?
• Noticing unspecified behaviours and transitions (see previous slide’s table, row 3)
• Unreachable states
• Dead states (cannot be left) 
• How do we define tests form these diagrams?
• Simple state transition testing means a test is defined for each state transition.
• This achieves coverage called 0-switch coverage.
• Better coverage is achieved by testing each state transition pair.
• This is called 1-switch or simply switch coverage.
BLACKBOX TESTING: STATE TRANSITION TESTING

## Slide 14

14
BLACKBOX TESTING: STATE TRANSITION TESTING
Face=recognized / 
System unlocks 
door
Face=unrecognized / 
System keeps door 
locked
Door reclosed / 
sensors activated
Set lock Off/ 
sensors disabled & 
alarm off
face detected / 
system on 
No face 
detected / 
system idle
S1
Wait for 
recognized 
Face
S2 Face 
Recognized 
unlocked 
door
S3
Wait to 
Activate 
System
Test Case 1 2 3 4 5 6
Start State S1 S1 S2 S2 S3 S3
Input FU FR DR SLO NFD FD
Expected Output DL UD SA SD&AO SI SO
Finish State S1 S2 S3 S1 S3 S1
First level of coverage: 0-switch (exercise all transitions).

## Slide 15

15
BLACKBOX TESTING: STATE TRANSITION TESTING
Test Case 1 2 3 4 5 6 7 8 9 10
Start State S1 S1 S1 S2 S2 S2 S2 S3 S3 S3
Input FU FR FR SLO SLO DR DR NFD FD FD
Expected Output DL UD UD SD&AO SD&AO SA SA SI SO SO
Next State S1 S2 S2 S1 S1 S3 S3 S3 S1 S1
Input FR SLO DR FU FR NFD FD FD FU FR
Expected Output UD SD&AO SA DL UD SI SO SO DL UD
Final State S2 S1 S3 S1 S2 S3 S1 S1 S1 S2
Second level of coverage: 1-switch (exercise all unique state-transitions pairs; I.E., 
excluding S1-S1-S1, and S3-S3-S3)*
Face=recognized 
/ System unlocks 
door
Face=unrecognized 
/ System keeps 
door locked
Door reclosed / 
sensors
activated
Set lock Off/ 
sensors disabled 
& alarm off face detected / 
system on 
No face 
detected / 
system idle
S1 S2 S3
*this is in accordance with 
the SELA Software and 
Education Labs (ISTQB
assessors) . This is the 
definition we’ll stick to in 
the course; however, I 
believe there may be a 
slight discrepancy with the 
original author of n-switch 
testing, T S Chow.

## Slide 16

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of this video may be 
reproduced, or transmitted in any form or by and means, 
including recording, or other electronic or mechanical 
methods, without the prior permission of the creator, 
except in the case of certain other noncommercial uses 
permitted by copyright law.
