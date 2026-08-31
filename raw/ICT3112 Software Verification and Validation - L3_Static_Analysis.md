# L3 Static Analysis

## Slide 1

1
STATIC 
ANALYSIS/TESTING

## Slide 2

2
Static analysis (aka static testing):
• Testing of a component or system at the specification or 
implementation level, without executing the code.
• The primary options are Reviews (inspections) and 
Code Inspections
Definition by IEEE 1028-1997:
• “A process or meeting during which a software product is (examined 
by) project personnel, managers, users, customers, user representatives, 
or other interested parties for comment or approval.”
STATIC ANALYSIS: DEFINITION

## Slide 3

3
Inspection (Fagan 1976)
“Inspections are a formal, efficient, and economical method of finding 
errors in design and code.”
Technical Reviews (Freedman and Weinberg 1986)
“... to provide management with reliable information as to the quality of 
the intermediate products being produced.”
Structured Walkthrough (Yourdon 1985)
“It is simply a peer group review of any product.”
STATIC ANALYSIS: REVIEWS

## Slide 4

4
STATIC ANALYSIS: REVIEW BENEFITS
REF: Fagan “Advances in Inspections” IEEE Transactions on Software Engineering

## Slide 5

5
Benefits obtained by exercising static testing techniques:
• Early detection of defects
• Defects are cheaper to correct
• Reduction in dynamic testing time and cost. 
• Reduction in maintenance costs.
•Improved development productivity. 
•Improved communications.
• Early or on-time delivery of high quality products.
STATIC ANALYSIS: REVIEW BENEFITS

## Slide 6

6
STATIC ANALYSIS: TYPES OF REVIEWS
Ad Hoc 
Reviews
Walkthroughs
Technical 
Reviews
Inspections
Ad Hoc Reviews
Informal
A quick way to get 
another perspective that 
can find errors. Ad hoc 
reviews are the most 
informal type of review 
with little impact beyond 
solving current problems.

## Slide 7

7
STATIC ANALYSIS: TYPES OF REVIEWS
Ad Hoc 
Reviews
Walkthroughs
Technical 
Reviews
Inspections
Walkthroughs
Partially formal
A walkthrough is a review 
in which the author of a 
work product describes the 
product to a group of 
peers and solicits 
comments (Hollocker 1990)

## Slide 8

8
STATIC ANALYSIS: TYPES OF REVIEWS
Ad Hoc 
Reviews
Walkthroughs
Technical 
Reviews
Inspections
Technical Reviews
Semi formal
It’s a meeting that 
discusses the product. 
Focus is on technical 
content of requirement 
documentation. It’s led 
by a trained moderator 
or by a technical expert.

## Slide 9

9
STATIC ANALYSIS: TYPES OF REVIEWS
Ad Hoc 
Reviews
Walkthroughs
Technical 
Reviews
Inspections
Inspections
Formal
Used to collect quantitative 
quality data. Inspection of 
the detailed design, code, 
and requirements are 
performed. Process includes 
moderator and author of 
artefact inspected.

## Slide 10

10
STATIC ANALYSIS: TYPES OF REVIEWS
Examples
• Code review by team lead
• Test cases review done by 
colleagues
Ad hoc review
• No formal process
• There may be pair 
programming or technical lead 
review of designs and code 
• Documentation is optional
• Main purpose: inexpensive way 
to detect defects at the earliest

## Slide 11

11
STATIC ANALYSIS: TYPES OF REVIEWS
Examples
• Review of the architecture
design of hardware
• Review of system common 
infrastructure definition
• Review of the usability
principles of Microsoft Office
Walkthrough
• Led by author of the product
• Scenarios, dry runs, peer 
groups
• Optional preparation meeting 
and documentation is optional 
• Can vary from informal to 
extremely formal
• Main purpose: learn, gain 
understanding, identify 
defects

## Slide 12

12
STATIC ANALYSIS: TYPES OF REVIEWS
Examples
• Review the design of database 
structure (tables, relations, etc.)
• Review of Software 
requirements specification
• Software design description
• Software test documentation
• Software user documentation
• System build procedures
• Installation procedures
• Release notes
Technical review
• Documented 
• Defect identification process 
• Led by a moderator
• Preparation meeting required
• Main purpose: discuss, make 
decisions, evaluate 
alternatives, find defects, 
solve technical problems and 
check compliance with 
specifications, plans, 
regulations and standards

## Slide 13

13
STATIC ANALYSIS: TYPES OF REVIEWS
Examples
• Formal code inspection with 
group leader resulting with 
inspection report 
• Test scenario design review 
by designers group 
Inspection
• Involves peer examination 
• Led by moderator 
• Includes metrics 
• Formal process based on rules 
and supporting checklists 
• Has entry and exit criteria
• Preparation meeting is required 
• Formal follow-up process 
• Main purpose: finding defects

## Slide 14

14
Code Inspections: 
• Involves examining the source code with the aim of discovering anomalies 
and defects
• Intended for defect detection, not correction
• Very effective technique for discovering errors
• Saves time and money – the earlier in the development process an error is 
found, the better 
STATIC ANALYSIS: CODE INSPECTION
STATIC: CODE INSPECTIONS CHECKLIST (EXAMPLE)

## Slide 15

15
Fault class Static analysis check
Data faults Variables used before initialization
Variables declared but never used
Variables assigned twice but never used between assignments
Possible array bound violations
Undeclared variables
Control faults Unreachable code
Unconditional branches into loops
Input/output faults Variables output twice with no intervening assignment
Interface faults Parameter type mismatches
Parameter number mismatches
Non-usage of the results of functions
Uncalled functions and procedures
Storage management faults Unassigned pointers
Pointer arithmetic
Exception management faults Have all possible error conditions been taken into account?
STATIC: CODE INSPECTIONS CHECKLIST (EXAMPLE)
STATIC ANALYSIS: CODE INSPECTION

## Slide 16

16
Objective: To find defects in source code and software models:
• Automatically analyze the code before its actual execution.
• Locate defects which are hard to find during dynamic testing, e.g. 
dead code, dead locks, etc. 
• To be used by developers before and during component (unit) and 
integration testing. 
• Tools will automatically check for many of the previously mentioned 
issues; e.g., Resharper (for C#) https://www.jetbrains.com/resharper/
STATIC ANALYSIS: CODE INSPECTION TOOLS

## Slide 17

17
• Early detection of defects. 
• Early warning about suspicious aspects of code or design using 
metrics, i.e. code complexity. 
• Can identify defects that are hard to find during dynamic testing. 
• Detecting dependencies and inconsistencies in code or design (e.g. 
connections between tables). 
•Improved maintainability of code and design. 
• Leads to (focuses on) future improvements and prevention of defects. 
• Static analysis tools and activity is supported by some compilers
STATIC ANALYSIS: TOOL BENFITS

## Slide 18

Copyright © 2023 by Ryan Fraser Kirwan
All rights reserved. No part of these slides, nor PDFs, 
may be reproduced, or transmitted in any form or by 
and means, including recording, or other electronic or 
mechanical methods, without the prior permission of the 
creator, except in the case of certain other 
noncommercial uses permitted by copyright law.
