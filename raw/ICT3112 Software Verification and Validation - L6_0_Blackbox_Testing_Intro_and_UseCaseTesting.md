# L6 0 Blackbox Testing Intro and UseCaseTesting

## Slide 1

1

## Slide 2

2
BLACKBOX TESTING: 
INTRODUCTION + 
USE CASE TESTING

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
USE CASE TESTING

## Slide 5

5
• Objective: Use case testing is a Blackbox test design technique that 
allows the designing of test cases which execute user Scenarios.
• Scope: 
• Tests functional system characteristics mostly from the user’s 
point of view (opposed to the system/developer point of view)
• Derived from:
• Use cases or business processes. 
• Where Use cases must be readable, correct, specific, clear, 
complete, stable, up-to-date, well documented.
BLACKBOX TESTING: USE CASE TESTING

## Slide 6

6
• Use case – “series of transactions between a user and system that 
yields a tangible result”.
• Use case comprises: Actors, Preconditions, Postconditions,
Primary system flow, Alternative flows
• Pros: 
• Describes real use of system (more convenient for end system user/customer). 
• Can describe business flow excluding technical details, or it can be at system level.
• Can represent a type of process flow model, similar to classic flow models. 
E.g., data-flow diagrams, cause-effect graphs etc.
BLACKBOX TESTING: USE CASE TESTING

## Slide 7

7
• E.g., The following is a subset of Use Cases in a resource management system. 
Students can request equipment and have it provided to them via a locker-based 
system.
BLACKBOX TESTING: USE CASE TESTING E.G.
request 
resource

## Slide 8

8
Overview Student requests to loan an item.
Actors Student, PO
Student is logged into the system and selected to 
request a resource
Preconditions
Postconditions The loan request is send to the PO
BLACKBOX TESTING: USE CASE TESTING E.G.
request 
resource
• Focusing on “request resource” allows us to begin breaking this 
into testable scenarios.

## Slide 9

9
• From this information we can map a 
flow diagram. A subset of a larger 
diagram is given here.
BLACKBOX TESTING: USE CASE TESTING E.G.
request 
resource

## Slide 10

10
Actor actions System responses
2. System checks for eligibility and 
passes the request.
A-1 Student is ineligible for a item loan 
1. Student enters the details 
of the item they wish to loan.
3. Student selects item from 4. System displays loan request to PO
selection of item type
BLACKBOX TESTING: USE CASE TESTING E.G.
Primary system flow:

## Slide 11

11
Actor actions System responses
2. A-1 Student is ineligible for a item 
loan. 
1. Student enters the details 
of the item they wish to loan.
3. System displays failed eligibility 
message to student.
BLACKBOX TESTING: USE CASE TESTING E.G.
Alternative flow:

## Slide 12

12
Now we can start to model this Use case as Scenarios, which 
allows us to:
• Create tests for existing use cases or situations where 
test cases don’t exist.
• Verify correctness and testability of user requirements more 
transparently. 
• Focus testing on the most frequently used use cases.
• Identify and design test case to cover Use case primary 
system flow. 
• Identify and design test cases to cover each alternate flow 
at least once.
BLACKBOX TESTING: USE CASE TESTING E.G.

## Slide 13

13
Test Cases System initial state Test data input Expected results
1. System grants 
eligibility.
2. Allows selection of 
item with ID 001.
3. Displays loan 
request to PO.
Item type: 
MSP430. 
Item ID: 001.
Time: ASAP.
Student logged into 
system on request loan 
page.
TC#1. Student 
request valid 
loan
1. System fails 
eligibility.
2. Displays failed 
eligibility message 
to student. 
Item type: 
Chemical X.
Time: ASAP.
Student logged into 
system on request loan 
page.
TC#2. Student 
invalid loan 
(alternative)
BLACKBOX TESTING: USE CASE TESTING E.G.
Now we can drive some Scenario test cases system flow:

## Slide 14

14
These Scenarios can be use to detect:
• Defects derived from real world use of the system. 
•Integration defects caused by the interaction and interface of 
difference components. 
• Testing a system using Scenarios derived from Use cases may detect 
defects that occur in real use of the system better.
• E.g., if test cases detect that a system gets to a state/situation which it 
can’t leave. E.g., if the system could get stuck after a failed eligibility 
check, then we need to know this and adjust the system accordingly.
BLACKBOX TESTING: USE CASE TESTING E.G.

## Slide 15

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of this video may be 
reproduced, or transmitted in any form or by and means, 
including recording, or other electronic or mechanical 
methods, without the prior permission of the creator, 
except in the case of certain other noncommercial uses 
permitted by copyright law.
