# L5 2 Whitebox Testing Code Coverage

## Slide 1

1
WHITEBOX TESTING: 
CONTROL FLOW CODE 
COVERAGE

## Slide 2

2
WHITEBOX TESTING: CONTROL FLOW COVERAGE
Path 
(coverage)
Multi-condition
Decision & 
Condition
Condition
Decision
State
ment
Statement Coverage:
Every Statement is 
exercised at least once (this 
would be 100% statement 
coverage).

## Slide 3

3
WHITEBOX TESTING: CONTROL FLOW COVERAGE
Path 
(coverage)
Multi-condition
Decision & 
Condition
Condition
Decision
State
ment
Decision (aka Branch) 
Coverage:
Every decision / branch 
that has a True or False
outcome is evaluated at 
least once.

## Slide 4

4
WHITEBOX TESTING: CONTROL FLOW COVERAGE
Path 
(coverage)
Multi-condition
Decision & 
Condition
Condition
Decision
State
ment
Condition Coverage:
Each condition, with either 
True or False outcomes 
(compound decision), is 
exercised for True and 
False at least once.

## Slide 5

5
WHITEBOX TESTING: Coverage Clarifications
Path 
(coverage)
Multi-condition
Decision & 
Condition
Condition
Decision
State
ment
Coverage Clarification:
Please note that this diagram only 
represents the general levels of 
coverage. I.E., “Condition” is 
generally more coverage than 
Decision and Statement. However, as 
we’ll see later, Condition coverage 
may not cover all decisions and, 
consequentially, may not cover all 
statements either. Practically speaking 
though, when implementing Condition
coverage, it should be done to cover 
all decisions and statements also.

## Slide 6

6
WHITEBOX TESTING: CONTROL FLOW COVERAGE
Path 
(coverage)
Multi-condition
Decision & 
Condition
Condition
Decision
State
ment
Decision & Condition 
Coverage:
Every condition and 
decision are exercised.

## Slide 7

7
WHITEBOX TESTING: CONTROL FLOW COVERAGE
Path 
(coverage)
Multi-condition
Decision & 
Condition
Condition
Decision
State
ment
Multiple Condition 
Coverage:
All possible combinations of 
inner conditions are 
exercised.

## Slide 8

8
WHITEBOX TESTING: CONTROL FLOW COVERAGE
Path 
(coverage)
Multi-condition
Decision & 
Condition
Condition
Decision
State
ment
Path coverage:
All possible control paths 
are exercised, including 
loops (0, min, normal, max 
times).

## Slide 9

9
WHITEBOX TESTING: CONTROL FLOW COVERAGE
STATEMENT TESTING
• Each statement must be executed at least once.
• Find the minimum number of paths required to cover all 
statements.
• Considerations:
• Programs (normally) contain several alternate paths due to the presence 
of decision points. 
• Paths may go through loops which repeat a sequence of instructions 
several times.
Coverage (%) = (num statements executed/num statements executable) *100

## Slide 10

10
Pseudo code, Factorial example:
1.int i=1, facto=1;
2 input num;
3. If (num<0) 
4. {Then print “nope”;}
5. Else {
6. While (i<=num)
7. { facto=facto*i;
8. i++;
9. } //End-while
10. Print(facto);
11. } //End-if
WHITEBOX TESTING: CONTROL FLOW COVERAGE
1
5
2
3
11
4
10
6
7
8
9
Statement Coverage Example:
To cover all statements only 2 paths
need to be exercised:
TC#1, I.E., Path 1: num>0
TC#2, I.E., Path 2: num<0
There is 1 other path that we do 
not exercise, but that could identify 
defects.

## Slide 11

11
Pseudo code, Factorial example:
1.int i=1, facto=1;
2 input num;
3. If (num<0) 
4. {Then print “nope”;}
5. Else {
6. While (i<=num)
7. { facto=facto*i;
8. i++;
9. } //End-while
10. Print(facto);
11. } //End-if
1
5
2
3
11
4
10
6
7
8
9
Statement Coverage
Path1: num>0
WHITEBOX TESTING: CONTROL FLOW COVERAGE

## Slide 12

12
Pseudo code, Factorial example:
1.int i=1, facto=1;
2 input num;
3. If (num<0) 
4. {Then print “nope”;}
5. Else {
6. While (i<=num)
7. { facto=facto*i;
8. i++;
9. } //End-while
10. Print(facto);
11. } //End-if
1
5
2
3
11
4
10
6
7
8
9
Statement Coverage
Path 2: num<0
WHITEBOX TESTING: CONTROL FLOW COVERAGE

## Slide 13

13
WHITEBOX TESTING: CONTROL FLOW COVERAGE
DECISION/BRANCH TESTING
• A decision (branch) is an executable statement that may transfer control to another 
statement—excluding those that simply branch to the next statement.
• In branch/decision testing every possible branch is tested regardless of the 
outcome; unlike statement testing, where if there is no statement on the branch, it is 
not tested. 
• Every decision that has a True or False outcome is evaluated at least once. Hence:
• Cases with multiple exits would have test cases for each exit.
• Statement coverage is guaranteed.
Coverage (%) = 
(num decision outcomes executed/num decision outcomes possible)*100

## Slide 14

14
Pseudo code, Factorial example:
1.int i=1, facto=1;
2 input num;
3. If (num<0) 
4. {Then print “nope”;}
5. Else {
6. While (i<=num)
7. { facto=facto*i;
8. i++;
9. } //End-while
10. Print(facto);
11. } //End-if
WHITEBOX TESTING: CONTROL FLOW COVERAGE
1
5
2
3
11
4
10
6
7
8
9
Decision Coverage Example:
2 decisions: “if” and “while”.
Need to test both for True and False. This 
can be achieved by 2 paths:
Path 1: num<0: 1,2,3,4,11
Path 2: num>0: 1,2,3,5,6,7,8,9,10,11
(same paths as statement coverage.)
The situation where num=0 is achieved 
while using the num>0 path (2), hence no 
need for:
X=0: 1,2,3,5,6,10,11

## Slide 15

15
Pseudo code, Factorial example:
1.int i=1, facto=1;
2 input num;
3. If (num<0) 
4. {Then print “nope”;}
5. Else {
6. While (i<=num)
7. { facto=facto*i;
8. i++;
9. } //End-while
10. Print(facto);
11. } //End-if
1
5
2
3
11
4
10
6
7
8
9
Decision coverage:
Path1: num>0
WHITEBOX TESTING: CONTROL FLOW COVERAGE

## Slide 16

16
Pseudo code, Factorial example:
1.int i=1, facto=1;
2 input num;
3. If (num<0) 
4. {Then print “nope”;}
5. Else {
6. While (i<=num)
7. { facto=facto*i;
8. i++;
9. } //End-while
10. Print(facto);
11. } //End-if
1
5
2
3
11
4
10
6
7
8
9
Decision coverage:
Path 2: num<0
WHITEBOX TESTING: CONTROL FLOW COVERAGE

## Slide 17

17
WHITEBOX TESTING: CONTROL FLOW COVERAGE
CONDITION TESTING
• Test cases are designed to execute all true/false conditional outcomes.
• Each condition alternative is executed for both a true and a false result.
Coverage example: 
if (clouds<5 && daytime=true) then sunny=true
• Test daytime=true and clouds<5 or clouds>5 and get the branches covered 
for true and false (like in decision coverage).
• However, for condition coverage, we need to test cases, where 
daytime=true/false and we don’t care about clouds, and where clouds<5 
or clouds>5 and don’t care about daytime. To get full condition coverage.

## Slide 18

18
WHITEBOX TESTING: CONTROL FLOW COVERAGE
CONDITION TESTING
Coverage (%) = (num conditions executed for both true and false/
num possible conditions)*100 
It’s Not necessarily a superset of decision coverage. Example:
If (X and Y)
print(“tested”); 
Condition Coverage:
Just needs to check for X being T/F and 
Y being T/F. Hence, could be covered 
with X = T and Y = F; or X=F and Y=T.
But only 1 branch is executed!

## Slide 19

19
WHITEBOX TESTING: CONTROL FLOW COVERAGE
CONDITION TESTING
Coverage (%) = (num conditions executed for both true and false/
num possible conditions)*100 
It’s Not necessarily a superset of decision coverage. Example:
If (X and Y)
print(“tested”); 
Decision Coverage:
Just needs to check for X=T and Y=T, 
and either one being false (e.g., X=T
Y=F)
Both branches are executed! ..but not all 
conditions! Hence: Decision & Condition

## Slide 20

20
WHITEBOX TESTING: CONTROL FLOW COVERAGE
MULTIPLE CONDITION TESTING
• Test all combinations of true (T) and false (F) within multi-conditionals.
• This coverage >= statement coverage, condition coverage, decision 
coverage and decision & condition coverage.
If (cloudy=F && daytime=T && shade=F ) then sunny=T
Decision Coverage:
Just needs to check: 
1: cloudy=F, daytime=T, shade=F;
2: cloudy=T, daytime=T, shade=F;

## Slide 21

21
WHITEBOX TESTING: CONTROL FLOW COVERAGE
MULTIPLE CONDITION TESTING
• Test all combinations of true (T) and false (F) within multi-conditionals.
• This coverage >= statement coverage, condition coverage, decision 
coverage and decision & condition coverage.
If (cloudy=F && daytime=T && shade=F ) then sunny=T
Condition Coverage:
Just needs to check: 
1: cloudy=T, daytime=T, shade=T;
2: cloudy=F, daytime=F, shade=F;

## Slide 22

22
WHITEBOX TESTING: CONTROL FLOW COVERAGE
MULTIPLE CONDITION TESTING
• Test all combinations of true (T) and false (F) within multi-conditionals.
• This coverage >= statement coverage, condition coverage, decision 
coverage and decision & condition coverage.
If (cloudy=F && daytime=T && shade=F ) then sunny=T
Multi-Condition Coverage: Needs to check: 
1: cloudy=T, daytime=T, shade=T; 5: cloudy=F, daytime=T, shade=F;
2: cloudy=F, daytime=F, shade=F; 6: cloudy=F, daytime=F, shade=T;
3: cloudy=T, daytime=F, shade=F; 7: cloudy=F, daytime=T, shade=T;
4: cloudy=T, daytime=T, shade=F; 8: cloudy=T, daytime=F, shade=T;

## Slide 23

23
WHITEBOX TESTING: CONTROL FLOW COVERAGE
PATH TESTING
• Exercising all possible paths of the code.
• For functions with loops, the number of paths can be enormous!
Hence, limiting loop execution to lower number of cases must be done. 
E.g., based on a combination of the loop variables:
Loop Coverage, I.E.,: Check limited set of possible loop combinations:
• Zero iteration.
• One iteration.
• Typical number of iterations.
• Max (feasibly high) iterations.

## Slide 24

24
Pseudo code, Factorial example:
1.int i=1, facto=1;
2 input num;
3. If (num<0) 
4. {Then print “nope”;}
5. Else {
6. While (i<=num)
7. { facto=facto*i;
8. i++;
9. } //End-while
10. Print(facto);
11. } //End-if
WHITEBOX TESTING: CONTROL FLOW COVERAGE
1
5
2
3
11
4
10
6
7
8
9
PATH TESTING: LOOPS
Path Coverage: 
• Zero: i>num, no executions 
• Min: i=num, executed once 
• Typical: num=i+10, 10 executions
• Max: max difference between “num” 
and ‘i’ where i<num. 
(practically, for loop coverage, “num” may be 
assigned a very large int opposed to the Max.)

## Slide 25

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of these slides, nor PDFs, 
may be reproduced, or transmitted in any form or by 
and means, including recording, or other electronic or 
mechanical methods, without the prior permission of the 
creator, except in the case of certain other 
noncommercial uses permitted by copyright law.
