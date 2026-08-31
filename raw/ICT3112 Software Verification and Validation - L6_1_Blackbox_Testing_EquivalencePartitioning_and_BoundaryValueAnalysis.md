# L6 1 Blackbox Testing EquivalencePartitioning and BoundaryValueAnalysis

## Slide 1

1

## Slide 2

2
BLACKBOX TESTING: 
EQUIVALENCE 
PARTITIONING and
BOUNDARY VALUE 
ANALYSIS

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
Boundary value analysis
State transition testing
Equivalence partitioning
Use case testing
Decision table testing

## Slide 4

4
BLACKBOX TESTING: 
EQUIVALENCE 
PARTITIONING

## Slide 5

5
• What is Equivalence Partitioning for?
• Designed to minimize number of test cases while still covering a large 
amount system requirements.
• How does Equivalence Partitioning work?
• All test inputs are divided into groups called Equivalence Partitions.
• Test inputs include human inputs, input via interfaces to the system, interface 
parameters in integration testing, and inputs from hardware, etc. 
• Each Equivalence Partition should be processed by the system in a similar 
way, signifying expectation of equivalent results. 
• Testing a single member of an Equivalence Partition should be equivalent 
to testing any other partition member.
BLACKBOX TESTING: EQUIVALENCE PARTITIONING

## Slide 6

6
For example 1 a): Let’s consider we have a function that is meant to take in 
inputs as positive Integer between 0 and 100. We may consider the following 3 
Equivalence Partitions: 
• Valid (+90, +10…) 
• Invalid (+110, -10…)
BLACKBOX TESTING: EQUIVALENCE PARTITIONING
0 100
Valid
Invalid Invalid

## Slide 7

7
For example 1 b): Let’s consider we have a function that is meant to take in 
inputs as positive Integer between 0 and 100. We may consider the following 3 
Equivalence Partitions: 
• Valid (+90, +10…) 
• Invalid 2 (+110…)
• Invalid 1 (-10…)
BLACKBOX TESTING: EQUIVALENCE PARTITIONING
0 100
Valid
Invalid 1 Invalid 2

## Slide 8

8
For example 2: Let’s consider binary search in an unsorted array of 
10 entries of positive integers lower than 99, the Equivalence Partitions could be:
• Inputs where precondition==true and element is an array member, e.g. 12. 
• Inputs where precondition==true and element isn’t an array member, e.g. 95.
• Inputs where the precondition==false, e.g. -19, 150, 1000, etc.
BLACKBOX TESTING: EQUIVALENCE PARTITIONING
45 10 7 8 12 56 17 11 73 50

## Slide 9

9
Disadvantages Advantages
• Usually easy to analyze 
• Applicable for all test levels
• Minimizes amount of test cases while 
still covering a large amount system 
requirements
• Can be used to partition both inputs 
and outputs
• Excludes some inputs 
• No rule to choose inputs 
• Very limited focus 
• No guarantee that all elements of 
an Equivalence Partition are treated 
in the same way
BLACKBOX TESTING: EQUIVALENCE PARTITIONING

## Slide 10

10
BLACKBOX TESTING: 
BOUNDARY VALUE 
ANALYSIS

## Slide 11

11
• What is Boundary Value Analysis for?
• Designing test cases based on boundary value inputs and to ensure proper 
functionality of the system. Assumes testing boundaries is likely to yield defects
• Complement to Equivalence Partitioning by selecting the max and min values of 
partitions for boundary values.
• How does Boundary Value Analysis work? 
• Test input values are selected at, and just beyond the boundaries of 
Equivalence Partitions–choosing values on each boundary.
• Tests cover both valid and invalid boundaries.
• Both input and output boundaries are used to determine tests.
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS

## Slide 12

12
For example 1 [as seen for Equivalence Partitioning example 1 a)]: Let’s 
consider we have a function that is meant to take in inputs as positive Integer 
between 0 and 100. We may consider the following boundary values: 
• Valid: 0, 100 (low & high) (in some interpretations, we could add 1, 99, to test 
each boundary with 3 Tests).
• Invalid: -1, 101 (low & high).
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
0 100
Valid
Invalid Invalid
-1 101

## Slide 13

13
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
As well as value, we need to consider both input representation and format.
• Continuing the previous example (1): 
• Now assume that inputs must be in a 3 digit format (system will complete entry 
with leading 0s). 
Valid: Try to enter 1 digit 
and verify system (system 
adds 2 leading zeros).
Valid: Try to enter 
3 digits.
Invalid: If you try to 
enter 4 digits the 
system won’t allow it.
Invalid: if you try to 
enter a null value, the 
system won’t allow it.

## Slide 14

14
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
• For example 2 (as seen for Equivalence Partitioning): Let’s consider 
binary search in an unsorted array of 10 entries of positive integers lower than 
99, the Boundary Values could be:
• Inputs where precondition==true, e.g. 0, 98. 
• Inputs where precondition==true and element is the 1st array member, 45. 
• Inputs where precondition==true and element is the last array member, 50. 
• Inputs where precondition==true and element isn’t an array member, e.g. 95.
• Inputs where the precondition==false, e.g. -1, 99.
45 10 7 8 12 56 17 11 73 50

## Slide 15

15
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
Considering String inputs: length and collating sequence 
(order in which characters are sorted—e.g., ASCII) 
• General rule, test for: empty string, one char string, typical string, and max size string. 
Let’s consider boundary values for example 3: enter “First Name”, between 1 – 10 CAPITAL 
letter characters. 
First Name:
•Valid: First Name of 
• one character: “G”
• Lower Valid: “A”
(Note: if we combined these into one test, we’d be unsure whether it 
fails due to lower boundary of ASCII or lower boundary of string size.)
•Valid: First Name of 
• 10 characters “BORDERNAME”
• Upper Valid: “Z” Invalid: First Name of 
• 11 characters, “FAKEBIGNAME”
• Upper Invalid: “[” (ASCII 91)
Invalid: First Name:
• Null, 
• Lower invalid character: 
“@” (ASCII 64)

## Slide 16

16
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
Considering Date inputs: 
• format (dd/mm/yy, mm/dd/yyyy, etc.), 
• restrictions within the calendar (# of days in a month)
• don’t forget leap years. 
• Let’s consider boundary values for example 4: Enter “start date” in 
dd/mm/yyyy format.
• Assumptions:
• None of them are older than 120 years.
• Date can be in the future, but not beyond today + 1Month (31 days).

## Slide 17

17
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
Param Valid Invalid
• Invalid low boundary: 0
• Invalid high boundary: 
#of_days_in_month +1
(29 or 30 or 31 or 32) 
• Valid low boundary: 1
• Valid high boundary: 
#of_days_in_month
(28, 29, 30 or 31)
dd
• Invalid low boundary: 0
• Invalid high boundary: 13
• Valid low boundary: 1
• Valid high boundary: 12
mm
• Invalid low boundary: Today -121
• Invalid high boundary: Today +32 
days
• Valid low boundary: today -120
• Valid high boundary: Today 
+31 days.
yyyy

## Slide 18

18
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
Parameter Valid Invalid
• Invalid low boundary: -01
• Invalid high boundary: 24
• Valid low boundary: 00
• Valid high boundary: 23
hh
• Invalid low boundary: -01
• Invalid high boundary: 60
• Valid low boundary: 00
• Valid high boundary: 59
mm
Considering Time inputs:
• Format (HH:MM; HH:MM:SS), 
• 12 or 24 hour clock. 
Let’s consider boundary values for example 5: enter “start time” in format HH:MM. 
• Assumptions: 24 hours clock, and Time can be in the future.

## Slide 19

19
Given a range of values, 
create valid tests for 
each end, and invalid 
tests just beyond each 
end of the range. 
Also consider output 
conditions. 
1
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS
Given values, without 
a specified range, use 
min and max of values, 
and one beneath
and beyond these 
values.
2
Given files, test the 
first and last records 
(input or output).
Given Sets of values, 
test for each value 
within the set, and 
the set’s size.
3
Example output conditions: Billing system 
produces a report, in which total number of 
subscribers mustn't exceed 6,000,000.
Valid outputs: 0 and 6,000,000 
Invalid outputs: -1 and 6,000,001
In other cases, 
consider any extreme 
input or output 
conditions, and test 
for each of them. 
4
Consider a general process for generating boundary tests:

## Slide 20

20
Disadvantages Advantages
• Applicable for all test levels.
• Can expose potential user interface/user input 
problems. 
• Very clear guidelines for determining tests.
• Capable of identifying a high amount of defects.
• Excludes some inputs.
• Doesn’t consider 
dependencies between 
the combinations of 
input values. 
BLACKBOX TESTING: BOUNDARY VALUE ANALYSIS

## Slide 21

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of this video may be 
reproduced, or transmitted in any form or by and means, 
including recording, or other electronic or mechanical 
methods, without the prior permission of the creator, 
except in the case of certain other noncommercial uses 
permitted by copyright law.
