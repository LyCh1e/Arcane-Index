# L1 Software VV Intro

## Slide 1

SOFTWARE VERIFICATION & VALIDATION
[PART 1]: INTRODUCTION

## Slide 2

2
AGENDA
• Module Introduction
• Verification & Validation Motivation
• Software Quality
• Introduction
• Software Quality Metrics
• Software Quality Standards
• Introduction to Software Verification & Validation
• Please Note (first half):
• ~Team Based Learning (involving Flipped Classroom)
• 5 TBL sessions (5 iRATs and 5 tRATS total – 1 of each per session) worth *20%* of overall grade
• 4 Lab Assessments weeks 2-5 worth *15%* of overall grade
• No Labs this week (set up your systems and begin e-learning Lec. 2—see LMS for details)

## Slide 3

3
MODULE INTRODUCTION

## Slide 4

4
WHY 
V&V?
Source: somewhere on the internet (it’s a common SE RE meme)
MODULE INTRODUCTION
How the Customer 
explained it
How the Project 
Lead understood it
How the Analyst 
designed it
How Programmers 
wrote it
How Consultants 
described it
How the project 
was documented
What features 
were working
What the customer 
was billed for
How the product 
was supported
What the customer 
really needed

## Slide 5

5
Software V&V is the process of checking that a software 
system meets specifications and that it fulfills its intended 
purpose.
Source: Doug Amos, Mentor, DVCon 2018
MODULE INTRODUCTION

## Slide 6

6
MODULE INTRODUCTION
1
st Part of V&V: informal
2
nd Part of V&V: formal
Incomplete coverage
• Limited amount of simulation
• Spot check (tests) limited number of input sequences
• Some corner cases unchecked (IE, incomplete)
• Designer provides test vectors (aided by tools)
Complete coverage
• Uses mathematically precise models 
• Verifies specified properties across all behaviours 
Can identify subtle interactions and corner cases 
without enumerating individual tests 
• Assurance remains limited by the model, properties 
and assumptions; complements testing

## Slide 7

7
WEEK TOPIC
1
Introduction to Software Quality
Introduction to Software V&V (NO LABS)
2
Introduction to Software Testing, Static and Dynamic testing theory,
Unit Testing, TDD, (BDD)
RATs 1 + Lab Assessment 1
3
Introduction to TDD. Whitebox testing theory part 1
RATs 2 + Lab Assessment 2 
4
Introduction to BDD. Whitebox testing theory part 2.
RATs 3 + Lab Assessment 3
5
Introduction to Automated testing. Blackbox testing theory part 1.
RATs 4 + Lab Assessment 4
6
Introduction to Dependency Injection and Mocking. Blackbox testing theory 
part 2. RATs 5 + Consultation Labs/*Lab Assessment 5*
MODULE INTRODUCTION: SCHEDULE

## Slide 8

8
WEEK TOPIC
8
Intro to Formal Methods.
Hoare Logic Rules for Assignment and sequential composition
Lab: Intro to Frama C. Formal Verification of C code (i)
9
Hoare Logic Rules for conditional statements (IF)
Lab: Introduction to Frama-C. Formal Verification of C code. (ii)
10 Hoare Logic Rule for Loops and Quiz I
Lab: Intro to Frama-C. Formal Verification of C code (iii).
Project Assessment Introduction
11 Loop Invariants and how to calculate them
Lab: Frama-C and LLMs
12 Reasoning on Arrays
Lab: Project Verification Workshop and Consultation
13 Revision Lecture and Quiz II
Lab: Project Evaluation Quiz
MODULE INTRODUCTION: SCHEDULE

## Slide 9

9
N.B., The RATs will assess lab exercises (including notes in Lab PDFs) and lecture content
Also note: CA %s are provisional due to new technology being used–may need to adjust for 
fairness later
ASSESSMENT TASK WEIGHTING
Final exam (MCQ + short answer) *30% (15% first half and 15% second half)
Lab Assessments *15% (3.75% for each assessment, scored out 
of 10)
iRATs and tRATs for Weeks 2- 6 (RATS 1-5) 20% (4% total each: 2.5% iRAT, 1.5% tRAT)
CA for Weeks 8-13 35%
MODULE INTRODUCTION: ASSESSMENTS

## Slide 10

10
MODULE INTRODUCTION: Team Based Learning 
(provisional plan)
Revision/consul
tation with 
peers
<=0th min
LMS iRAT with 
Respondus
browser
20 mins
Team revision 
and discussion 
in groups
~20 mins
LMS tRAT with 
Respondus
(but done as 
individuals)
15 mins
Discussion of 
solutions in 
lecture format 
50 mins
Before 11:00 -> Self-revision/Consultation
11:00-11:20 -> begin iRAT (5mins for enter/exiting quiz, 19+1min for quiz)
11:25-11:50 -> Rejoin main Zoom, then go into break-out rooms (~20mins)
11:50-11:05 -> begin tRAT (5mins for enter/exiting quiz, 14+1min for quiz)
12:10 -> Discussion of solutions (runs until 13:00 end)

## Slide 11

11
• S.H. Kan, Metrics and Models in Software Quality Engineering,
(2nd ed.), Addison-Wesley, 2002.
• Capers Jones, McGraw-Hill, Applied software measurement
(2nd ed.): assuring productivity and quality,
McGraw-Hill, Inc. Hightstown, NJ, USA ©1997.
• Software Testing Primer v2, Nick Jenkins 2017
(under creative commons 4.0 License, i.e., free PDF)
• E. Clarke, O. Grumberg, D. Peled, Model Checking,
Cambridge, MA: The MIT Press, 1999
MODULE INTRODUCTION: REFERENCES
“Testing is a search for the truth”
“You can hope your software works or 
you can know it works – through testing.” 
Nick Jenkins

## Slide 12

12
Software Quality
• Explain the necessity of ensuring software quality in software engineering
• Explain intrinsic software quality metrics and customer-oriented metrics
• Explain and distinguish between the factors contributing to poor software quality software
• Understand the definition of software quality and software quality assurance
• Apply software quality metrics in software quality assurance
Software Verification & Validation
• Distinguish between verification and validation
• Distinguish among the different types of software V & V (static and dynamic)
• Understand the definition of software V & V
MODULE INTRODUCTION: TODAY’s LOs

## Slide 13

13
V&V MOTIVATION

## Slide 14

14
Some BIG failures in Software
• Therac-25 Radiation Overdosing (1985-87)
• Radiation machine for treatment of cancer patients 
• At least 6 cases of overdose in period (3 fatal)
• 1985–1987 (≈100-times dose) Three cancer patients died
• Source: Software Design error in the control software (race condition)
• Code was NOT independently reviewed
• Never tested with the combination of software and hardware until assembled at the hospital
https://e n.wikipedia.org/wiki/Therac-25
http://hackaday.com/2015/10/26/killed-by-a-machine-the-therac-25/
MODULE INTRODUCTION: MOTIVATION

## Slide 15

15
Some BIG failures in Software
• Crash of the European Ariane 5-missile in June 1996 
• Costs: more than $500 million 
• Source: Software Flaw in the control software: data conversion 
from a 64-bit floating point to 16-bit signed integer.
https://en.wikipedia.org/wiki/Ariane_5
(https://www.youtube.com/watch?gl=SG&v=gp_D8r-2hwk&hl=en-GB)
MODULE INTRODUCTION: MOTIVATION

## Slide 16

16
MODULE INTRODUCTION: MOTIVATION
Cost of Software Failures:
• 2002: An estimated $59.5 billion annually (for United States) 
• More than a third of these costs (an estimated $22.2 billion) could be eliminated by an improved 
testing infrastructure, even though not all errors can be removed 
• 2021: “An estimated $2.08 trillion in the United States alone over the past year”.
[from Consortium for Information & Software Quality (CISQ), in partnership with 
Synopsys, “The Cost of Poor Software Quality in the U.S.”]
• CISQ 2022 estimates (US) cost of poor software quality is at least $2.41 trillion
• (Initial estimate that CrowdStrike issue (alone) on 19 July 2024 will result in financial 
losses of 5.4 billion USD. 
–source: Parametrix)
Source: US Department of Commerce 2002
https://www.synopsys.com/blogs/software-security/poor-software-quality-costsus/#:~:text=There%20is%20some%20marginally%20good,%242.1%20trillion%20for%20that%2
0year.)

## Slide 17

17
a BIG investor in Formal Methods (V&V)
• Verification of a product shows proof of compliance with 
requirements—that the product can meet each “shall” 
statement as proven though performance of a test, analysis, 
inspection, or demonstration (or combination of these).
• Validation of a product shows that the product accomplishes 
the intended purpose in the intended environment—that it 
meets the expectations of the customer and other stakeholders 
as shown through performance of a test, analysis, inspection, 
or demonstration.
https://www.nasa.gov/reference/2-4-distinctions-between-product-verification-andproduct-validation/?utm_source=chatgpt.com
MODULE INTRODUCTION: MOTIVATION
NASA’s Formal Methods 
Symposium (NFM)
https://ti.arc.nasa.gov/ev
ents/nfm-2020/
https://shemesh.larc.nasa.
gov/nfm2021/
https://nfm2022.caltech.e
du/
https://conf.researchr.org/
home/nfm-2024...
NASA Formal Methods 
Symposium (NFM) 2026

## Slide 18

18
Verification: 
“Are we building the product right”
• The software should conform to its specification.
Validation:
“Are we building the right product” 
• The software should do what the user really requires.
V&V: DEFINITIONS

## Slide 19

19
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

## Slide 20

20
Static: Concerned with analysis of the static system representation 
to discover problems (no executing code)
• May be supplement by tool-based document and AI code analysis
• One example: Code and (AI) document inspections 
Dynamic: Concerned with exercising and observing product behaviour
• The system is executed with test data and its operational behaviour is observed
• Example: Software testing
SOFTWARE V&V: TYPES

## Slide 21

21
Testing done without executing the program Testing done by executing the program
Can be performed prior to code compilation Performed after code compilation
Testing focus is on prevention of defects Testing focus is on finding defects
Time-consuming and rigorous process that 
relies on human analysis
A process that can be automated into the 
continuous integration process
Lower cost to find and prevent defects Higher cost to find and fix defects
SOFTWARE V&V
STATIC VS DYNAMIC

## Slide 22

22
SOFTWARE QUALITY

## Slide 23

23
Quality is necessary to help prevent mistakes and failures:
• Therac-25
• ESA's Ariane 5 Rocket Crash
SOFTWARE QUALITY

## Slide 24

24
➢Human factor
➢Communication failure
➢Unrealistic development timeframe
➢Poor design logic
➢Poor coding practices
➢Lack of version control
➢Buggy third-party tools
➢Lack of skilled testing
➢Last-minute changes
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
NOTE:
We have consolidated this traditional list 
of causes into six broader categories of 
factors contributing to poor software 
quality. This adjusted set is informed by 
DORA’s sociotechnical perspective on 
current software-development practice.
DORA: https://dora.dev/

## Slide 25

25
➢Human factor
➢Communication failure
➢Last-minute changes
➢Unrealistic development timeframe
➢Poor design logic
➢Poor coding practices
➢Lack of version control
➢Buggy third-party tools
➢Lack of skilled testing
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
Course categorisation based on the DORA Core Model and capabilities ISO/IEC/IEEE 12207:2026 lifecycle processes, and 
NIST’s Secure Software Development Framework (NIST SP 800-218 )
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback

## Slide 26

26
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback
Example:
 An ambiguous late requirement is 
implemented hurriedly, merged without 
adequate review and released after 
incomplete regression testing.
That is, one defect can span multiple 
categories

## Slide 27

27
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback
The skills, communication, ownership and working 
culture that determine how information is shared, 
decisions are challenged and risks are managed.
Contributing conditions
• Vague, incomplete or misunderstood 
communication 
• Gaps in knowledge or experience 
• Unclear ownership and handovers 
• Fatigue and excessive cognitive load 
• A culture in which people are reluctant to 
report concerns

## Slide 28

28
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback
Unrealistic schedules, excessive simultaneous 
work and late changes reduce the time available 
for analysis, design, review and testing.
Contributing conditions
• Unrealistic deadlines or insufficient resources 
• Too much work in progress 
• Large changes delivered in one batch 
• Late changes to requirements, platforms or 
infrastructure 
• Insufficient time for impact analysis and 
regression testing

## Slide 29

29
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback
Requirements, architecture or design decisions do 
not adequately account for stakeholder needs, 
operating conditions, risks or technical feasibility.
Contributing conditions
• Ambiguous or missing requirements 
• Misapplication of technology 
• Choosing the easiest solution without assessing 
feasibility 
• Tightly coupled components 
• Invalid assumptions about reused components 
• Inadequate consideration of failure and 
recovery

## Slide 30

30
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and 
maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback
Implementation decisions introduce defects or 
make software difficult to understand, test, 
maintain and modify safely.
Contributing conditions
• Missing or inappropriate exception handling 
• Missing input, datatype, range or boundary 
validation 
• Unsafe concurrency or resource handling 
• Duplicated and overly complex code 
• Inconsistent coding standards 
• AI-generated code accepted without adequate 
review

## Slide 31

31
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback
Quality depends on being able to reproduce a 
release, trace every change and understand the 
third-party software included in the product.
Contributing conditions
• No version control 
• Builds created from inconsistent component 
versions 
• Environment and configuration drift 
• Outdated, vulnerable or incompatible 
dependencies 
• Unverified third-party libraries, APIs, tools or 
services

## Slide 32

32
SOFTWARE QUALITY: FACTORS CONTRIBUTING TO 
POOR SOFTWARE QUALITY
➢People, Communication and 
Organisation culture
➢Planning, workload and change 
pressure
➢Requirements, architecture and 
design
➢Implementation and maintainability
➢Configuration, dependencies and 
software supply chain
➢Verification, delivery and 
operational feedback
Inadequate review, testing, delivery controls and 
operational feedback allow defects to remain 
undetected, recur or affect users for longer.
Contributing conditions
• Insufficient testing knowledge, time or priority 
• Tests covering only expected or “positive-path” 
behaviour 
• Weak or unreliable regression automation 
• Unrealistic test data or environments 
• Limited monitoring and observability 
• Failure information not used to improve the system

## Slide 33

33
Software Quality is:
1. Degree to which a system, component, or process meets specified requirements
2. Degree to which a system, component, or process meets customer or user needs or 
expectations
SOFTWARE QUALITY: IEEE DEFINITION
Software Quality Assurance (SQA) is:
1. A planned and systematic pattern of all actions necessary to provide adequate 
confidence that an item or product conforms to established technical requirements
2. A set of activities designed to evaluate the process by which the products are 
developed or manufactured
N.B., SQA and Software Quality Management (SQM) are often used interchangeably

## Slide 34

34
MINI-QUIZ 1

## Slide 35

35
MINIQUIz
• Questions to help you retain this information!
• You can discuss with the people around you. 
•Write down/type up your answers as a group 
• This is a MEMORY exercise, so there is no point in cheating!

## Slide 36

36
TOTAL UP MARKS 
•Score out of 10
Repeat to learn, so learn to repeat!
miniQuiz

## Slide 37

37

## Slide 38

38
SOFTWARE QUALITY 
METRICS
Measuring Quality
“When a measure becomes a target, it 
stops being a measure.” 
paraphrase of Goodhart's law, 
attributed to Edwards Deming

## Slide 39

39
Two levels of metrics:
✓ Intrinsic software quality metrics
• Reliability: Availability, Failure intensity
• Defect density
✓ Customer oriented metrics
• Customer problems
• Customer satisfaction
SOFTWARE QUALITY METRICS

## Slide 40

40
Intrinsic software quality metrics:
• Reliability: by how long the software can run before encountering 
a “failure”.
• Defect density (rate): number of defects contained in software, 
relative to its size. 
SOFTWARE QUALITY METRICS

## Slide 41

41
RELIABILITY: AVAILABILITY

## Slide 42

42
AVAILABILITY factors:
• MTTF: Mean Time To Failure 
(average operating time from restoration/start-up until the next failure.)
Software system A: MTTF= 200 hours 
One failure can be expected every 200 hours
• MTTR: Mean Time To Repair (average time to restore a system after a failure)
Software system A: MTTR= 10 hours 
It takes 10 hours to track and fix errors that caused a failure on average
• MTBF: Mean Time Between Failures (MTBF = MTTF + MTTR)
Software system A: MTBF=MTTF+MTTR=200+10=210 hours 
Once the failure occurs, the next failure is expected to occur after 210 hours
SOFTWARE QUALITY METRICS: RELIABILITY

## Slide 43

43
AVAILABILITY factors:
• MTTF: Mean Time To Failure 
(average operating time from restoration/start-up until the next failure.)
Software system A: MTTF= 200 hours 
One failure can be expected every 200 hours
• MTTR: Mean Time To Repair (average time to restore a system after a failure)
Software system A: MTTR= 10 hours 
It takes 10 hours to track and fix errors that caused a failure on average
• MTBF: Mean Time Between Failures (MTBF = MTTF + MTTR)
Software system A: MTBF=MTTF+MTTR=200+10=210 hours 
Once the failure occurs, the next failure is expected to occur after 210 hours
SOFTWARE QUALITY METRICS: RELIABILITY
NOTE:
In many modern software engineering and DevOps
contexts, we often assume that MTTR is so small (seconds 
or minutes) compared to MTTF (thousands of hours) that 
they treat them as practically identical:
MTBF ~= MTTF
For this module we will maintain the textbook calculation 
and consider that MTTR is not necessarily negligible

## Slide 44

44
Availability = MTTF / MTBF = MTTF / (MTTF + MTTR)
Software system A Availability = 200/210 = 95.2%
Classes of Systems according to Availability:
SOFTWARE QUALITY METRICS: RELIABILITY
The U.S. government mandates that its air traffic control system cannot be unavailable for 
more than three seconds per year. 
source: "Metrics and Models in Software Quality Engineering" by Stephen H.

## Slide 45

45
RELIABILITY: FAILURE 
INTENSITY

## Slide 46

46
Failure Intensity: The number of failures per time unit.
Use () to denote the Failure Intensity from time 
The number of failures observed per unit time after  time units of 
executing the system, from the beginning. This is also called the failure 
intensity at time .
[N.B., this may seem like a probability, but Failure rate can be more than 1
because it is a rate.] ) # of failuresin [ , ]
( ) (

    

+ 
= f
SOFTWARE QUALITY METRICS: RELIABILITY

## Slide 47

47
[NOTE] DIFFERENCES IN TIME:
• Execution time (t): How much CPU time was used by the test; e.g.,
5 hours of CPU processing time: t = 5 CPU-hours
• Calendar time (t): How much actual time was used by the test; e.g., 
12:00 – 17:00, 5 hours of clock time: t = 5 hours
“t = 5” may not mean the same as “t = 5”
Execution time VS Calendar time
If multiple threads are running then possibly 
• CPU time > Calendar time. However, 
if the program is suspended and awaiting IO then 
• CPU time < Calendar time.
SOFTWARE QUALITY METRICS: RELIABILITY

## Slide 48

48
Observations (failure intensity):
As we observe a failure and the corresponding fault/error is fixed:
• There will be fewer faults remaining in the system 
• Failure intensity will be smaller with each fault fixed
In other words, as the cumulative failure count increases, the failure
intensity decreases
Note: these module invoke a perfect-debugging assumption, commonly used by reliabilitygrowth models. That is, correcting the fault responsible for an observed failure reduces the 
expected failure intensity.
SOFTWARE QUALITY METRICS: RELIABILITY

## Slide 49

49
There are two classic ways to model the decrement processes:
1. The decrease in failure intensity after observing a failure and fixing the 
corresponding fault is constant. 
 
2. The decrease in failure intensity after observing a failure and fixing the 
corresponding fault reduces (smaller than the previous decrease) 
Basic model 
Logarithmic
model
SOFTWARE QUALITY METRICS: RELIABILITY
Prominent Reliability models, Ref: Musa Basic model and Musa/Okomoto Logarithmic model

## Slide 50

50
v0
Basic
Log
μ : Mean failures exp.
λ : failure intensity
Initial failure intensity, λ0
λ: Failure intensity
λ0: Initial failure intensity
 at start of execution
μ: Average total number of 
 failures at a given point 
 in time
v0: Total number of failures
 over infinite time 
SOFTWARE QUALITY METRICS: RELIABILITY
Adapted from: Software Testing & Quality Assurance by Paulo Alencar

## Slide 51

51
0: the initial failure intensity at the start of execution
: the average (expected) number of failures experienced at time 
0: the total number of failures over infinite time
The average number of failures at time  is given as:
SOFTWARE QUALITY METRICS: RELIABILITY
Basic Model












= − − 


  
0
0 1 exp 0 ( )
 (𝜏) = 0 1 −
𝜇
𝑣0

## Slide 52

52
Assume a program will experience 100 failures in infinite time. 
• It has now experienced 50 failures. 
• The initial failure intensity was 10 failures/CPU-hour. 
5 failures/CPU - hour
100
50 ( ) 1 10 1
0
0
=






=  − 





= −


  
➢ The number of failures experienced after 10 CPU hours is:
10 100 [1 exp( 1)] 63 failures
100
10 ( ) 100 1 exp  =  − − =










   =  − − 
➢ The number of failures experienced after 100 CPU hours is:
𝜇(𝜏) = 100 ∗ 1 − exp −
10
100
∗ 100 = 100 ∗ [1 − exp( − 10)] = ~100 failures
➢ The current failure intensity is:
SOFTWARE QUALITY METRICS: RELIABILITY












= − − 


  
0
0 ( )
0 1 exp

## Slide 53

53
: failure intensity decay parameter
0: the initial failure intensity at the start of execution
: the average (expected) number of failures experienced at time 
The average number of failures at time  is given as:
SOFTWARE QUALITY METRICS: RELIABILITY
Logarithmic Model
() = 0exp( - )
ln( 1)
1
( ) = 0 +

 

## Slide 54

54
Assume:
• the initial failure intensity 0 = 10 failures/CPU-hour, 
•  = 0.02/failure, It has now experienced 50 failures. ( ) = 0 exp(−) = 10exp(−0.02 50) = 3.68 failures/CPU - hour
➢ The number of failures experienced after 10 CPU hours is:
ln(10 0.02 10 1) 55 failures
0.02
1
( ) =   + =
➢ The number of failures experienced after 100 CPU hours is:
ln(10 0.02 100 1) 152 failures
0.02
1
( ) =   + =
➢ The current failure intensity is:
Less failures than 
Basic model (63 
failures)
More failures 
than Basic model 
(100 failures)
SOFTWARE QUALITY METRICS: RELIABILITY
ln( 1)
1
( ) = 0 +

 

## Slide 55

55
Basic Model:
✓More suitable for a fixed, stable release where faults contribute 
similarly, each fix produces a comparable reduction in failure 
intensity, and cumulative failures approach a finite plateau.
Logarithmic Model:
✓More suitable when fault exposure is uneven: frequently 
encountered faults are corrected early, producing larger initial 
improvements followed by diminishing gains and a long tail of 
rare failures.
SOFTWARE QUALITY METRICS: RELIABILITY

## Slide 56

56
SOFTWARE QUALITY METRICS: RELIABILITY
Software Quality Reliability Metrics Provide:
✓Ready to release?
✓Need more testing?
✓When will the Availability objective be achieved?
“A bug found at design time costs ten times less to 
fix than one in coding and a hundred times less than 
one found after launch” 
Barry Boehm

## Slide 57

57
DEFECT DENSITY

## Slide 58

58
Size: lines of code, usually expressed in thousand lines of code (KLOC), or
 the number of function points
Lines Of Code (LOC):
- Different tools may count differently 
- Defect density in normally completed with the counting method for LOC
- Not recommended to compare defect densities of two products written in different 
languages
SOFTWARE QUALITY METRICS: DEFECT DENSITY

## Slide 59

59
How to calculate LOC
SOFTWARE QUALITY METRICS: DEFECT DENSITY
Do you include blank 
lines and comments? 
…LOC isn’t always a 
useful measure. 
There’s also function points 
(remember SE 101)
*Just be consistent in your measurements*

## Slide 60

60
How to provide 
Release-to-release 
Improvement:
Software Quality Defect Density Metric 
Provides:
✓Any improvement on Defect Density
in a new release?
✓If yes, how much is the improvement 
on Defect Density? 
SOFTWARE QUALITY METRICS: DEFECT DENSITY

## Slide 61

61
DEFECT DENSITY FACTORS:
SSI: Shipped Source Instructions 
CSI: new and Changed Source Instructions
SSI (current release) = SSI (previous release)
+ CSI (for the current version)
- deleted code
- changed code (to avoid double count in both SSI and CSI)
SOFTWARE QUALITY METRICS: DEFECT DENSITY

## Slide 62

62
• Initial Release of Software X:
• KCSI = KSSI = 50 KLOC 
• Total number of defects =100
• Defect density = Defects/KCSI = 100/50 = 2.0 defects/KLOC
• Second Release of Software X:
• KCSI = 20 KLOC
• Total number of additional (i.e., in CSI) defects = 36 
• Defect density of KCSI = Defect/KCSI = 36/20 = 1.8 defects/KLOC
• [KSSI (current) = 50 + 20 (new and changed lines of code)
- 4 (assuming, e.g. 20% are changed/deleted lines of code )
= 66 KLOC]
Software Quality 
Management:
(2.0 - 1.8)/2.0 = 10% 
defect density 
improvement over
the 1
st release
SOFTWARE QUALITY METRICS: DEFECT DENSITY

## Slide 63

63
CUSTOMER ORIENTATED 
METRICS

## Slide 64

64
Customer oriented metrics:
• Customer problems metric
• Customer satisfaction metric
SOFTWARE QUALITY METRICS: CUSTOMER METRICS

## Slide 65

65
Customer PROBLEMS metric:
How do we measure problems?
Usually expressed in terms of Problems per User Month (PUM)
TNP: Total Number of Problems reported by customers for a time period
TNM: Total Number of License-months of the software during the period
PUM= TNP/ TNM
SOFTWARE QUALITY METRICS: CUSTOMER METRICS

## Slide 66

66
Customer SATISFACTION metric:
How do we measure satisfaction?
• It is often measured on the five-point scale:
• Very satisfied, Satisfied, Neutral, Dissatisfied, Very dissatisfied 
Key dimensions to measure: 
• IBM: CUPRIMDSO (Capability/functionality, Usability, Performance, 
Reliability, Installability, Maintainability, Documentation/Information, Service 
and Overall)
• HP: FURPS (Functionality, Usability, Reliability, Performance and Service)
SOFTWARE QUALITY METRICS: CUSTOMER METRICS

## Slide 67

67
MINI-QUIZ 2

## Slide 68

68
MINIQUIz
• Questions to help you retain this information!
• You can discuss with the people around you. 
•Write down/type up your answers as a group 
• This is a MEMORY exercise, so there is no point in cheating!

## Slide 69

69
TOTAL UP MARKS 
•Score out of 20
•Score today out of 30
Repeat to learn, so learn to repeat!
miniQuiz

## Slide 70

70
Software Quality
• Explain the necessity of ensuring software quality in software engineering
• Explain intrinsic software quality metrics and customer oriented metrics
• Explain and distinguish between the factors contributing to poor software quality software
• Understand the definition of software quality and software quality assurance
• Apply software quality metrics in software quality assurance
Software Verification & Validation
• Distinguish between verification and validation
• Distinguish among the different types of software V & V (static and dynamic)
• Understand the definition of software V & V
MODULE SUMMARY: TODAY’s LOs
