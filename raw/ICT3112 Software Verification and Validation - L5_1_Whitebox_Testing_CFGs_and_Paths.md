# L5 1 Whitebox Testing CFGs and Paths

## Slide 1

1

## Slide 2

2
WHITEBOX TESTING: 
CONTROL FLOW GRAPHS 
and PATHS

## Slide 3

3
WHITEBOX TESTING: 
CONTROL FLOW GRAPHS

## Slide 4

4
• Each statement (or set of statements) is represented by a node, so 
you need to number each node in the program uniquely.
• Each transition between statements is represented by an edge.
• The goal is to model the program/functions using a series of nodes
and edges: produce a control flow graph. 
• Once modelled, we aim to verify the model by:
1. Select the test paths you wish to exercise (level of coverage).
2. Design test cases for selected paths (creating specific Unit tests).
3. Running a set of test cases to verify that the code meets its specification.
WHITEBOX TESTING: CONTROL FLOW GRAPHS

## Slide 5

5
WHITEBOX TESTING: CONTROL FLOW GRAPHS
Node
Edge
Sequence If-then-else Case / Switch
Junction While loop Do until loop

## Slide 6

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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 7

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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 8

17
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 9

18
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 10

19
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 11

20
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 12

21
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 13

22
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 14

23
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 15

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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 16

25
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 17

26
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 18

27
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 19

28
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
WHITEBOX TESTING: CONTROL FLOW GRAPHS
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

## Slide 20

29
WHITEBOX TESTING: 
CONTROL FLOW PATHS

## Slide 21

30
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
WHITEBOX TESTING: CONTROL FLOW PATHS
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

## Slide 22

31
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
WHITEBOX TESTING: CONTROL FLOW PATHS

## Slide 23

32
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
WHITEBOX TESTING: CONTROL FLOW PATHS

## Slide 24

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of this video may be 
reproduced, or transmitted in any form or by and means, 
including recording, or other electronic or mechanical 
methods, without the prior permission of the creator, 
except in the case of certain other noncommercial uses 
permitted by copyright law.
