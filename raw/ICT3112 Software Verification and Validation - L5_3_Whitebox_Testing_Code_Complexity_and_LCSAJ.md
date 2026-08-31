# L5 3 Whitebox Testing Code Complexity and LCSAJ

## Slide 1

1

## Slide 2

2
WHITEBOX TESTING: CODE 
COMPLEXITY and LCSAJ 
COVERAGE

## Slide 3

3
WHITEBOX TESTING: 
CYCLOMATIC COMPLEXITY

## Slide 4

4
• Cyclomatic complexity measures the complexity of a program 
(developed by Thomas McCabe 1976)
• Measuring the number of independent paths in a program's source code.
• An independent path is any path in a program that introduces at least a new 
set of statements or a new conditional (i.e., a new edge).
• Cyclomatic complexity provides a calculation for an upper bound for a 
number of test cases required to guarantee coverage of all program 
statements and decisions.
WHITEBOX TESTING: CYCLOMATIC COMPLEXITY

## Slide 5

5
• Cyclomatic Complexity is defined as:
C = E – N + 2
where:
• E = the number of edges in the graph
• N = the number of nodes in the graph
This formulae gives exactly the MIN number of basis paths. 
• Basis paths are independent and non-looping paths, that can be used to 
generate all possible paths through code (module) in linear combinations—
note that: basis paths don’t necessarily cover all possible paths.
WHITEBOX TESTING: CYCLOMATIC COMPLEXITY

## Slide 6

6
Threshold Complexity Values: When is cyclomatic complexity "too high“?
• Originally, more than a 10 needed justification (e.g., the use of a large 
switch statement). In 1994 McCabe et al. produced a paper on “Software 
Complexity” with the following thresholds:
WHITEBOX TESTING: CYCLOMATIC COMPLEXITY
Range Interpretation
1-4 Simple module with low risk 
5-10 Marginal module with low risk
11-20 Complex module, moderate risk
21-50 Complex module, high risk
>50 Untestable module, very high risk

## Slide 7

7
BASIS PATH TESTING
1. Model the software code as Control Flow Graph (CFG)
2. Compute its Cyclomatic Complexity.
3. Select a set of basis paths (according to the result of phase 2). 
4. Create a test case for each basis path. 
5. Execute test cases.
(this technique ensures avoidance of redundant path testing and 
guarantees at least full branch coverage, at the worst case.)
WHITEBOX TESTING: CYCLOMATIC COMPLEXITY

## Slide 8

8
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
BASIS PATH TESTING

## Slide 9

9
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
BASIS PATH TESTING
Basis path calculations: 
• Back to the example (edges–nodes +2) 
12-11+2 = 3 paths.
Hence, 3 basis paths required.
1. num<0 (Input:-1; expected: “nope”).
2. num=0 (Input: 0; expected result: ‘1’).
3. num>0 (Input: 3; expected result: ‘6’).

## Slide 10

10
WHITEBOX TESTING: LCSAJ 
(an alternative metric)

## Slide 11

11
Linear Code Sequence And Jump (LCSAJ): is a white box testing technique 
to identify code coverage. Code is broken down into sections (tuples) from 
the beginning of the program or branch, terminating at the end of the 
program or branch.
LCSAJ is a program unit comprising a code sequence that terminates in a jump 
or the beginning of another LCSAJ program unit. 
• An LCSAJ unit is represented as a tuple (X, Y, Z) where X and Y are, 
respectively, locations of the first and last statements in the unit, and Z is the 
location to which the statement at Y jumps.
LCSAJ provides 100% of Decision Coverage
WHITEBOX TESTING: LCSAJ

## Slide 12

13
• The last statement in an LCSAJ tuple (X, 
Y, Z) may jump to the program exit. 
• When executing from statements X to Y, 
and then jumping to statement Z, we say 
that LCSAJ (X, Y, Z) program unit is 
“traversed” or “exercised”.
WHITEBOX TESTING: LCSAJ
Pseudo code, simple example:
1.//begin-code
2. int num;
3. input (num);
4. If (num<0) 
5. {Then print “less”;}
6. Else {
7. {print “more”;}
8. //End-of-code

## Slide 13

14
• The last statement in an LCSAJ tuple (X, 
Y, Z) may jump to the program exit. 
• When executing from statements X to Y, 
and then jumping to statement Z, we say 
that LCSAJ (X, Y, Z) program unit is 
“traversed” or “exercised”.
WHITEBOX TESTING: LCSAJ
Pseudo code, simple example:
1.//begin-code
2. int num;
3. input (num);
4. If (num<0) 
5. {Then print “less”;}
6. Else {
7. {print “more”;}
8. //End-of-code
Tuple 1
exit

## Slide 14

15
• The last statement in an LCSAJ tuple (X, 
Y, Z) may jump to the program exit. 
• When executing from statements X to Y, 
and then jumping to statement Z, we say 
that LCSAJ (X, Y, Z) program unit is 
“traversed” or “exercised”.
WHITEBOX TESTING: LCSAJ
Pseudo code, simple example:
1.//begin-code
2. int num;
3. input (num);
4. If (num<0) 
5. {Then print “less”;}
6. Else {
7. {print “more”;}
8. //End-of-code
Tuple 2
exit

## Slide 15

16
• The last statement in an LCSAJ tuple (X, 
Y, Z) may jump to the program exit. 
• When executing from statements X to Y, 
and then jumping to statement Z, we say 
that LCSAJ (X, Y, Z) program unit is 
“traversed” or “exercised”.
WHITEBOX TESTING: LCSAJ
Pseudo code, simple example:
1.//begin-code
2. int num;
3. input (num);
4. If (num<0) 
5. {Then print “less”;}
6. Else {
7. {print “more”;}
8. //End-of-code
Tuple 3
exit

## Slide 16

17
WHITEBOX TESTING: LCSAJ
Pseudo code, simple example:
1.//begin-code
2. int num;
3. input (num);
4. If (num<0) 
5. {Then print “less”;}
6. Else {
7. {print “more”;}
8. //End-of-code
• The last statement in an LCSAJ tuple (X, 
Y, Z) may jump to the program exit. 
• When executing from statements X to Y, 
and then jumping to statement Z, we say 
that LCSAJ (X, Y, Z) program unit is 
“traversed” or “exercised”.
LCSAJ Coverage: 
Path 1: X = -5.
Path 2: X = 5.
Path 1 covers LCSAJ tuple (1, 6, exit). 
Path 2 covers tuples: (1, 4, 7) and 
(7, 8, exit). 
This gives full LCSAJ coverage. …this is 
an alternative metric to CFG-based 
analysis of coverage.

## Slide 17

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of this video may be 
reproduced, or transmitted in any form or by and means, 
including recording, or other electronic or mechanical 
methods, without the prior permission of the creator, 
except in the case of certain other noncommercial uses 
permitted by copyright law.
