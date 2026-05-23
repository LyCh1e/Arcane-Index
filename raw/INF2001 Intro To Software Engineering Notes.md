# INF2001 – Introduction to Software Engineering
### Complete Lecture Notes

> Singapore Institute of Technology

---

## Table of Contents

1. [Week 1: Introduction to Software Engineering & SDLC](#week-1-introduction-to-software-engineering-sdlc)
2. [Week 2: Requirements Engineering](#week-2-requirements-engineering)
3. [Week 3: Use Case Diagram and Activity Diagram](#week-3-use-case-diagram-and-activity-diagram)
4. [Week 4: Class Diagram and Sequence Diagram](#week-4-class-diagram-and-sequence-diagram)
5. [Week 5: Project Management](#week-5-project-management)
6. [Week 8 (Part 1): Introduction to Software Engineering Design](#week-8-part-1-introduction-to-software-engineering-design)
7. [Week 8 (Part 2): Component Diagram](#week-8-part-2-component-diagram)
8. [Week 9 (Part 1): Software Architecture & Architectural Patterns](#week-9-part-1-software-architecture-architectural-patterns)
9. [Week 9 (Part 2): Design Patterns](#week-9-part-2-design-patterns)
10. [Week 10 (Part 1): Blackbox Testing](#week-10-part-1-blackbox-testing)
11. [Week 10 (Part 2): Whitebox Testing](#week-10-part-2-whitebox-testing)
12. [Week 11 (Part 1): Software Maintenance](#week-11-part-1-software-maintenance)
13. [Week 11 (Part 2): Software Configuration Management](#week-11-part-2-software-configuration-management)

---

## Week 1: Introduction to Software Engineering & SDLC

### Slide 1

INF2001
Introduction to Software Engineering
Week 1
A/Prof Frank Guan

### Slide 2

2
TODAY
- Motivation for Software 
Engineering
- What is Software Engineering
- Types of Software Development 
Lifecycle (SDLC)

### Slide 3

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
In 1968…
- Reveal of Boeing 747
- Apollo 8 - 1st manned 
spacecraft (soon followed 
by Apollo 11)
3

### Slide 4

IN 1968 THE MAJOR COMPLAINTS WERE:
Projects were unmanageable and 
code difficult to maintain. Software was of low 
quality
4

### Slide 5

Software Engineering: The Reality in Numbers
5

### Slide 6

Software Engineering: the Reality in Numbers
6

### Slide 7

STANDISH REPORT, 1995
We Are Getting Better…
51%
33%
16%
2015
52%
19%
29%
7

### Slide 8

CHAOS Resolution by Project Size 
SUCCESSFUL CHALLENGED FAILED
Grand 2% 7% 17%
Large 6% 17% 24%
Medium 9% 26% 31%
Moderate 21% 32% 17%
Small 62% 16% 11%
Total 100% 100% 100%
The resolution of all 
software projects by 
size from FY2011-
FY2015 with the new 
CHAOS database.
8 CHAOS Report—a long-standing study by the Standish Group that analyzes success and failure rates of IT and software projects

### Slide 9

Cutter Consortium Data
- 2002 survey of information technology 
organisations
- 78% have been involved in disputes ending in litigation
- For the organisations that entered into litigation:
- In 67% of the disputes, the functionality of the information 
system as delivered did not meet up to the claims of the 
developers.
- In 56% of the disputes, the promised delivery date slipped 
several times.
- In 45% of the disputes, the defects were so severe that the 
information system was unusable.
9

### Slide 10

Raising Demand for Software
- Student management systems
- E-commerce website
- Generative AI solutions
- …
10

### Slide 11

Defining “SOFTWARE”
11

### Slide 12

Defining “SOFTWARE ENGINEERING”
12

### Slide 13

Defining “SOFTWARE ENGINEERING”
“The application of a systematic, disciplined, 
quantifiable approach to the development, 
operation and maintenance of software.”
13

### Slide 14

Defining “SOFTWARE ENGINEERING”
“The application of a systematic, disciplined, 
quantifiable approach to the development, 
operation and maintenance of software.”
14

### Slide 15

Defining “SOFTWARE ENGINEERING”
“The application of a systematic, disciplined, 
quantifiable approach to the development, 
operation and maintenance of software.”
15

### Slide 16

Defining “SOFTWARE ENGINEERING”
“The application of a systematic, disciplined, 
quantifiable approach to the development, 
operation and maintenance of software.”
16

### Slide 17

Defining “SOFTWARE ENGINEERING”
“The application of a systematic, disciplined, 
quantifiable approach to the development, 
operation and maintenance of software.”
It’s not just coding!
17

### Slide 18

Defining “SOFTWARE ENGINEERING”
“Software engineering is a discipline whose aim 
is the production of fault-free software, 
delivered on time and within budget, that 
satisfies the user’s needs”
18

### Slide 19

Defining “SOFTWARE ENGINEERING”
- Programming in the large
- many people, more complex systems
- Disciplined development
- Repeatable practices
- Full life-cycle of activities
- A dual emphasis:
- Product: what is produced
- Process: how the product is produced
19

### Slide 20

Fault-free Software
- What are Faults?
- software behaviours unaccounted for in its design
- Examples
- Can you give me a few examples?
- How can we lessen our chances of faults?
- use a well-defined process that includes rigorous design, testing, 
and programming techniques
20

### Slide 21

Time and Budget Case Studies
California DMV software (1987-1993)
- attempt to merge driver & vehicle registration systems
- Plan: $28 million over 5 years.
- spent 7 years and $50 million …
before pulling the plug
❖Estimated cost of over $200 million and at least 5 years delay
Round 2: 
California DMV software (2006-2013)
➢ Project stopped after spending $134 million due to 
“significant concerns with the lack of progress”
➢ 3 months before the original expected delivery date
➢ Some of the functions were delivered
Data from: IEEE SPECTRUM, 2013 Los 
Angeles Times, 2013
21

### Slide 22

Time and Budget Case Studies
Digital Media Initiative (DMI) by BBC, UK
- To modernise the Corporation's production and archiving 
methods by using connected digital production and media asset 
management systems.
- Plan: ~£81.7 million
- Actual cost: >£98 million (>SGD200 million)
- 2008 - 2013
- Project scrapped due to bad management and outpaced by 
changing technology.
- By 2013, much cheaper Commercial Off The Shelf (COTS) 
alternatives by then existed.
Data from: BBC abandons £100m digital project
22

### Slide 23

Economic Aspects: Example
- Coding Method CMnew is 10% faster than currently used Coding Method 
CMold. 
Should it be used?
- Common sense answer: 
Of course!
- Software Engineering answer:
- Consider the cost of training
- Consider the impact of introducing a new technology
- Consider the effect of CMnew on maintenance 
23

### Slide 24

Satisfies User’s Needs
- Functionality and Usability
- does what the user’s tasks require
- efficient to use & error rates kept to a minimum
- easy to learn
- leads to high user satisfaction
- Bad (even if correct) user interfaces cost
- money (5% satisfaction ⇒ up to 85% profits)
- lives (Therac-25)
- User interfaces hard to get right
24

### Slide 25

However
25

### Slide 26

Software Development Activities
- Understand User requirements(what the client needs)
- Analysis and design software architecture(high level and 
detailed)
- Implement and document the design
- Testing(verify and validate)
- Deploy the product
- Fix bugs after deployment
- Add features after deployment
- Planning and Team Management
26
Requirement 
specification
Analysis and 
Design
Implementation
Testing
Deployment
Maintenance

### Slide 27

Typical Classical Phases
- Requirements phase
- Explore the concept
- Elicit the client’s requirements
- Analysis (specification) phase
- Analyse the client’s requirements
- Draw up the specification document
- Draw up the software project management plan
- “What the product is supposed to do”
27

### Slide 28

Typical Classical Phases - Design phase - Architectural design, followed by - Detailed design - “How the product does it” - Implementation phase - Coding - Unit testing - Integration - Acceptance testing
28

### Slide 29

Typical Classical Phases 
- Postdelivery maintenance
- Corrective maintenance
- Perfective maintenance
- Adaptive maintenance
- Retirement
29

### Slide 30

Phase Cost Approximation
- 1976–1981 data 
Maintenance constitutes 67% of total cost
- Good software is maintained
(for 10, 20 years or more)
- Bad software is discarded
- We should design our software with 
maintenance in mind
We need techniques, tools and practices 
to reduce maintenance costs!
2% 67%
5%
6%
5%
7%
8%
Maintenance
Requirements
Specification (Analysis)
Design
Module Coding
Module Testing
30

### Slide 31

Maintenance
maintenance
development
Classical perceptions:
31

### Slide 32

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
MAINTENANCE
Modern perception:
32
development
Maintenance 
Modern perception:
The process that occurs when a 
software artefact is modified
because of a problem or because of 
a need for improvement or 
adaptation
(adopted by IEEE)

### Slide 33

Importance Of Post-delivery Maintenance
- Good software is maintained (for 10, 20 years and more), 
- Bad software is discarded
- Software is a model of reality, which is constantly changing
- Different types of maintenance
- Corrective maintenance [about 20%]
- Enhancement
❖Perfective maintenance [about 60%]
❖Adaptive maintenance [about 20%]
33

### Slide 34

TIME (= COST) Of Post-delivery Maintenance
34
Between 1976 and 1981 Between 1992 and 1998

### Slide 35

Consequence Of Relative Costs Of Phases
- Return to CMold and CMnew
- Reducing the coding cost by 10% yields 
at most a 2% reduction in total costs
- Consider the expenses and disruption 
incurred
- Reducing postdelivery maintenance cost 
by 10% yields a 6-7% reduction in overall 
costs
35

### Slide 36

Requirements, Analysis, And Design Aspects
The cost of detecting and correcting a fault at each phase
36

### Slide 37

Requirements, Analysis, and Design Aspects
- To correct a fault early in the life cycle
- Usually just a document needs to be changed
- To correct a fault late in the life cycle
- Change the code and the documentation
- Test the change itself
- Perform regression testing
- Reinstall the product on the client’s computer(s)
37

### Slide 38

It is vital to improve our requirements, analysis, 
and design techniques
- To find faults as early as possible
- To reduce the overall number of faults (and, hence, the overall 
cost)
- To reduce the cost of maintenance 
38

### Slide 39

What is the best way to arrange the phases in a workflow?
- Which phase should come first?
- Should we work in parallel or sequential?
- Can we go through a phase more than once?
- Would your choice be affected by the type, size, and context of the 
project and hosting organisation?
39
Requirement 
specification
Analysis and 
Design Implementation
Testing Deployment Maintenance

### Slide 40

Software Life Cycle
- A life cycle: the steps performed when building a product
- A life cycle model: 
- The steps to follow when building software
- A theoretical description of what should be done
- Having a defined process (model) is essential
- Maturity of the process is some gauge of success of organisation
actual
40

### Slide 41

Waterfall Life-cycle Model
Classical model (1970)
41

### Slide 42

The Waterfall Process – 1970
- W. Royce “Managing the Development of 
Large Software Systems”
- Sequential & Distinct phases: one phase is 
completed and the next one begins 
- Document-driven (Plan and document 
approach) 
- Big Design Up Front (BDUF) 
42
Requirement 
specification
Analysis and 
Design
Implementation
Verification 
Validation
Deployment
Maintenance

### Slide 43

The Waterfall Process – Feedback loops
- The rationale is that the earlier you catch a bug 
the cheaper to fix it
- However, it is not realistic
- Thus, you keep going back, then you must 
move forward again in sequence
43
Requirement 
specification
Analysis and 
Design
Implementation
Verification 
Validation
Deployment
Maintenance

### Slide 44

Did the Waterfall Model Work?
44

### Slide 45

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
US Department of 
Defence (DOD) 
experienced an 
alarming amount of 
software failure 
using Waterfall
They hired an expert, Jarzombek 
(1999), to investigate the cause of 
failure 
45

### Slide 46

Among the 
systems that 
worked, not all 
features were 
used

### Slide 47

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
Misinterpretation 
of requirements 
from users
47

### Slide 48

SIT INF2001 - AY24/25, Tri 1
Attributes of the Waterfall Process
The Good
- Waterfall model is easy to understand
due to its simple linear structure and 
clearly defined stages
- Provides structure to less experienced 
staff
- Facilitates project management
- It helps to define the goals and 
deliverables at the early stage of the 
project
The Bad
- Success depends on precise requirements 
- No working model of the software until 
the end of the life cycle 
- High amounts of risk / uncertainty. 
- When in a later stage, it is very difficult to 
make any changes to the product 
- Not realistic: Does not reflect real 
processes 
- Expensive 
48

### Slide 49

SIT INF2001 - AY24/25, Tri 1
When to Use Waterfall Model?
When to Use
- Requirements are very well known 
and understood
- Technology is understood
- If you are building a new version of 
an existing product (with some 
exceptions) 
- Low-risk in-house projects 
- Small and simple Projects 
- Government projects that heavily 
regulated. 
When Not to Use
- Not a great choice for complex and 
long-term project 
- Doesn’t work for maintenance type 
project 
- When client is strict with timeline 
and budget 
- New idea that have not done before 
- Technology is new or team doesn’t 
know it. 
49

### Slide 50

Rapid Prototyping Model
A variation of the Waterfall model
50

### Slide 51

Rapid Prototyping Model
- Linear model
- Instead of ‘Requirements’: 
- Listen to customer
- Build prototype
- Customer “test drives” prototype
- Should be quick (can’t be long)
- Challenges:
- “Throw-away” phenomenon
- Demos can set unrealistic expectations
- Compromises that solidify
51

### Slide 52

KEY POINTS: Rapid Prototyping
- Do not turn the prototype into product
- Rapid prototyping may replace 
specification phase — never the design 
phase
- Comparison:
- Waterfall model — try to get it right first time
- Rapid prototyping — frequent changes, then 
discard
- But both method only have one shot for delivery 
at the end
52

### Slide 53

Did the Rapid Prototyping Model Work?
- When do customers see anything working? 
(at the end)
- The customers don’t know what they want till they see 
something working.
- Same issues as Waterfall 
(one shot delivery and expensive) 
53

### Slide 54

The Spiral Model
54

### Slide 55

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
The Spiral Model - 15 years later… - 4 Specific phases - Uses in iterations - Combines planning and documentation
with prototyping in iterations 
- There is an emphasis on risk analysis - The radius of the iteration reflects the 
accumulated cost involved 
- Customer is involved throughout 
55

### Slide 56

SIT INF2001 - AY24/25, Tri 1
Attributes of the Spiral Model
The Good
- Customers see the product as it 
evolves. 
- Risk management is part of the lifecycle (in every iteration) 
- Project monitoring and scheduling are 
easy because of the clear phases 
- Features can be added 
The Bad
- Iterations are very long - they could be 0.5-2 
years 
- A lot of documentation for every iteration 
- You can’t start a phase till the other ends 
- Need staff who are experts in risk 
- identification and resolution 
- Cost of the process is high (eg. time in 
prototyping) 
- Requires Stakeholder engagement 
56

### Slide 57

SIT INF2001 - AY24/25, Tri 1
When to Use the Spiral Model?
When to Use
- High Risk and large systems 
- Can be used for totally new 
ideas 
When Not to Use
- Client is not available 
- Progress is urgent 
- When client is strict with 
timeline and budget 
- Low risk and low budget projects 
(unnecessary expenses) 
57

### Slide 58

The Rational Unified Process
58

### Slide 59

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
The Rational Unified 
Process
- Introduced in 2003
- Closely tied to UML (Unified model language) and 
component-based modelling
- The Unified Process is not a series of steps for 
constructing a software product
- No such single “one size fits all” methodology could 
exist
- There is a wide variety of different types of software
- The Unified Process is an adaptable methodology
- It must be modified for the specific software 
product to be developed
59

### Slide 60

The Rational Unified Process (Framework)
60
Time
A Phase represents the Business context of a step
Workflow: Technical context
https://www.scnsoft.com/blog/software-development-models

### Slide 61

Phases of Business Context
Inception
- Begin to make the 
initial business 
case
- Set tentative 
schedule and 
budget
- Risk assessment 
- Understand the 
domain
- Usually short
61
Elaboration
- To refine the 
initial 
requirements and 
define priorities of use cases 
- Refine the 
software 
architecture 
- Refine the 
business case 
- Refine the 
project 
management 
plan
Construction
- Emphasis is on 
Implementation
and Testing
- Integration 
testing of 
subsystems 
- Product testing 
of the overall 
system 
- Operational 
releases 
- Usually longer 
than the rest 
Transition
- Move to 
customers’ real 
environment 
(deployment) 
- Ensure that the 
requirements are 
met 
- Correct Faults 
- Complete manuals 
- Driven by 
feedback from 
client

### Slide 62

Example of the Rational United Process
62
Technically you can have as many 
iterations as you want.
The above case is typically used.
https://www.scnsoft.com/blog/software-development-models
You can deliver a component here or 
deliver all of them at the end in parallel

### Slide 63

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
Key Points for the Rational Unified Process
- Use case and architecture centric 
- Deals with software in components with defined interfaces 
- The Unified Process framework is an adaptable methodology
It has to be modified for the specific software product to be developed 
63

### Slide 64

SIT INF2001 - AY24/25, Tri 1
Attributes of the Rational Unified Process
The Good
- Business Process tied to the development 
process 
- Tool support for gradual improvement of a 
project 
- Risk Mitigation 
- Focus on quality of design 
- A framework that allows the use of other 
models 
- Doesn’t need all requirements to be known at 
the beginning 
- Deliver value early (if needed) 
The Bad
- Complicated 
- Expensive tools are needed 
- Only good for medium and large- scale 
projects 
- Extensive Documentation and planning (a lot 
of overhead) 
64

### Slide 65

SIT INF2001 - AY24/25, Tri 1
When to Use the Rational Unified Process?
When to Use
- Medium to large projects 
- Budget and schedule can be 
strict 
- You need to show value early 
(you can show something 
working in the first iteration of 
construction phase) 
- Engineers experienced with 
object-oriented design 
When Not to Use
- Small simple projects
- Limited budget projects 
65

### Slide 66

Agile Approaches
68

### Slide 67

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 
1
Agile is a Mindset
69

### Slide 68

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 1
CHAOS 
Resolution by 
Agile Versus 
Waterfall 
70
The resolution by Agile 
versus Waterfall from 
FY2011-FY2015 with in 
the new CHAOS database

### Slide 69

Agile Manifesto
- Signed in 2001 by “independent-minded practitioners”
“We are uncovering better ways of developing software by doing it and helping others do 
it. 
Through this work we have come to value: 
- That is , while there is value in the items on the right, we value the items on the left 
more.”
71
Individual & Interactions Over Processed & Tools
Working Software Over Comprehensive 
Documentation
Customer Collaboration Over Contract Negotiation
Responding to Change Over Following A Plan

### Slide 70

Principles of Agile Method
- Embraces change as a fact of life
- Continuous improvement over fixed phase 
- Incremental delivery (1-4 weeks) 
- Increments have value 
- Emphasize Test driven development 
- Small teams 
- Customer involvement (not during iterations) 
- The automation of tasks where possible 
- Light-weight documentation 
- Velocity is the way to measure progress (how to predict progress with past 
progress) 
- Self management
72

### Slide 71

73
Source: Emmanuel Peña Alvarez

### Slide 72

SIT ICT2101/2201 Introduction to Software Engineering, AY21/22, Tri 
1
Types of Agile 
Methods
74
Scrum 
Kanban 
https://getnave.com/blog/kanban-workflow/

### Slide 73

Practising Agile
- Gives the client confidence to know that a new version with additional 
functionality will arrive every 3 weeks 
- The developers know that they will have 3 weeks (but no more) to 
deliver a new iteration 
- Without client interference of any kind
- If it is impossible to complete the entire task in the timebox, the work 
may be reduced (“descoped”) 
- Agile processes demand fixed time, not fixed features 
75

### Slide 74

SIT INF2001 - AY24/25, Tri 1
When to Use the Agile Method?
When to Use
- Lightweight methods suit smallto medium-size projects (or 
large projects divided into 
components) 
- Used for time-critical
applications and prototypes 
- Requirements are sure to 
change, new or uncertain 
- Technology is new
When Not to Use
- Do not have a good team 
(attitude and skills) 
- For large projects where 
customer needs specific 
documentation and formal 
communication 
- Large Systems that can’t be 
broken into modules for smaller 
teams 
76

### Slide 75

SIT INF2001 - AY24/25, Tri 1
Attributes of the Agile Method
The Good
- Flexible to change and continuous 
feedback which increases the change 
of building the right product 
- Customer Satisfaction 
- Early value delivery and early to 
market 
- Team Ownership (self organizing 
team) 
The Bad
- May require some rework (since we 
didn’t know EVERYTHING upfront) 
- Requires close collaboration with the 
client
- Good tools for automation are a must 
have (poor ones might delay you) 
- Not every individual/team can adopt 
Agile values, setup needs trust and 
communication 
77

### Slide 76

What is covered today
- Motivation
- Developing software is not simple, and often not done well.
- Developing software is not the same as coding. There is much more to it.
- We need to have good systems and processes in place.
- We want to keep maintenance in mind when developing.
- We want to detect faults as early as possible.
- Software Development Life Cycle (SDLC)
- Software models – their Pros, Cons, and when to use them
79


---

## Week 2: Requirements Engineering

### Slide 1

INF2001
Introduction to Software Engineering
Week 2
A/Prof Frank Guan

### Slide 2

Recap of last week
- Motivation for Software Engineering
- What is Software Engineering
- Types of Software Development Lifecycle (SDLC)

### Slide 3

Agenda for today
- Software requirements
- The process of requirement engineering
- Requirements modelling

### Slide 4

Software Requirements
- Descriptions of the services that a software system should 
provide and the constraints on its operation.
- Reflects the needs of stakeholders.
- Requirements should be specific and quantifiable.
4

### Slide 5

Specifying Requirements is Challenging
- Software is intangible, which makes it difficult to comprehend and 
communicate. 
- The client might not be clear about what they want.
- Terminology can be interpreted in multiple ways depending on the 
person or the context in which it was used. 
- There are many possible sources of requirements
- Direct users (end users) and indirect users (all other stakeholders) 
5

### Slide 6

Understanding Requirements
6
Environment
(User World + Problem Domain)
The System
(Machine World)
System
Requirement 
Specifications:
Bridging user 
requirements to what 
the system can do
The real-world
assumptions related to 
our system
User Requirements:
What the user wants 
to do (from their 
perspectives
Software system (code, 
frameworks, DBS etc.)
Hardware system 
(device, server machine, 
etc.)
Solution Domain

### Slide 7

Levels of Requirements & Readers
7
Environment
(User World + Problem Domain)
The System
(Machine World)
- System End-users
- Client engineers
- System architects
- Software developers
- Client managers
- System end-users
- Client engineers
- Contractor managers
- System architects
- Client engineers (maybe)
- System architects
- Software developers
System meets the world
High level Level of Details Very specific

### Slide 8

Requirements Engineering: The Process
Preparing requirements should be a systematic, organised, and quantifiable
8

### Slide 9

1 - Elicitation 2 - Analysis
3 - Validation 4 - Management
Activities of 
Requirements 
Engineering
9
Refining and extending the 
initial requirements
Are we building the right 
product?
The process of 
requirements discovery
Needed because of the 
changing requirements

### Slide 10

Requirements Elicitation 
The Starting Point of Every Project
10

### Slide 11

Stakeholder
- a stakeholder is any individual, group, or organization that has an 
interest in, is affected by, or can influence the development, 
operation, and success of a software system.
- IEEE: A stakeholder is an individual or organization that is materially affected 
by the outcome of the system or project.
- PMBOK (Project Management Body of Knowledge): A stakeholder is any 
individual, group, or organization that may affect, be affected by, or perceive 
itself to be affected by a decision, activity, or outcome of a project.

### Slide 12

Categories of Stakeholders
- Primary stakeholders (direct users & owners):
- End-users (who use the system daily)
- Product owners or clients (who request and fund the software)
- System administrators (who manage and maintain the system)
- Secondary stakeholders (indirectly involved or affected):
- Managers (who rely on system reports or efficiency)
- Customer support teams (who assist users with issues)
- Marketing and sales (who sell or promote the product)
- External stakeholders:
- Regulators or government agencies (who set compliance requirements)
- Investors (who fund the software development company)
- Competitors (indirectly influencing design/market decisions)
- Internal stakeholders:
- Software developers and testers
- UX/UI designers
- Project managers
- Quality assurance teams

### Slide 13

Examples of stakeholders
- If you are developing a mobile banking app:
- End-users → customers who use the app to transfer money.
- Client/Bank → the organization funding the app.
- Developers & Testers → the engineering team building it.
- IT Security Team → ensures compliance with cybersecurity standards.
- Regulators → financial authorities ensuring laws are followed.
- Customer service staff → help customers if the app fails.

### Slide 14

The Start of a Software Development Journey
- Deep dive to fish out your stakeholders needs.
- Your stakeholder may know what they want, but not necessary 
what is required.
- Most of the time stakeholders come into the project from various 
domains expertise. Understanding the domain will significantly 
improve your understanding of their needs.
- As your stakeholder understand their needs and project better, 
their requirements will naturally evolve. So be prepared to walk 
with them through this journey.
14

### Slide 15

What is the “moving target” problem? 
- A change in the requirements while the software product is being 
developed
- Any change made to a software product can potentially cause a 
regression fault
- A fault in an apparently unrelated part of the software
- If there are too many changes
- The entire product may have to be redesigned and re-implemented
How do we solve it?
- There is no solution to the moving target problem
15

### Slide 16

Requirements Engineering: Elicitation
- The process of requirements discovery
- It is different from requirements gathering 
- In Elicitation, the focus is on what user needs, not just wants (“Ethical 
duty”) 
- Involves actively interacting with stakeholders to extract requirements 
- Focus on what the stakeholders need, not how it will be done. 
- The focus is on the problem, not the technical solution 
16

### Slide 17

Requirements discovery methods
1. Interviews
2. Focus groups
3. Documents
4. Observations
5. Prototyping
6. Questionnaires
7. Scenarios
17

### Slide 18

Interviews
- Purpose
- To capture stakeholders’ needs, goals, and pain points.
- To clarify unclear or ambiguous requirements.
- To explore both functional and non-functional requirements.
- Types of Interviews
- Structured → predefined questions, consistent format, easier to compare answers.
- Unstructured → open-ended, free discussion, more flexibility.
- Semi-structured → mix of both; allows consistency with room for exploration.
- Preparation
- Identify relevant stakeholders (end-users, managers, domain experts, etc.).
- Prepare a question guide (open- and closed-ended questions).
- Set clear goals for what information is needed.
18

### Slide 19

Interviews
- Conducting the Interview
- Build rapport with the interviewee.
- Start with general questions, then move to specifics.
- Use open-ended questions to encourage detailed responses (e.g., “Can 
you describe how you currently perform this task?”).
- Use closed-ended questions to confirm facts (e.g., “How many reports 
do you generate weekly?”).
- Listen actively and avoid leading questions.

### Slide 20

Interviews
- Advantages
- Provides deep insights and context-specific information.
- Allows clarification of vague requirements immediately.
- Can uncover hidden needs and real pain points.
- Builds trust and engagement with stakeholders.
- Disadvantages / Challenges
- Time-consuming if many stakeholders are involved.
- Responses may be biased or incomplete.
- Requires good interviewing skills to avoid misinterpretation.
- Hard to cover large groups of users compared to surveys.

### Slide 21

Focus Group
- Purpose
- To gather requirements, opinions, and expectations from a group of stakeholders simultaneously.
- To stimulate discussion and generate ideas through group interaction.
- To uncover conflicts, consensus, and priorities among different users.
- Structure
- Typically involves 6–12 participants (users, clients, domain experts).
- Led by a facilitator/moderator who guides the discussion.
- May use prompts such as scenarios, prototypes, or storyboards to trigger feedback.
- Preparation
- Carefully select a diverse but relevant group of participants.
- Prepare guiding questions/topics (e.g., current pain points, desired features, usability concerns).
- Ensure a neutral and comfortable environment for open discussion.

### Slide 22

Focus Group
- Conducting the Focus Group
- Moderator introduces goals and sets ground rules.
- Encourage participants to share experiences, needs, and suggestions.
- Use open-ended prompts (e.g., “What do you find most frustrating in 
the current system?”).
- Record or document the discussion for later analysis.
- Manage dominant voices and encourage quieter participants to share.

### Slide 23

Focus Group
- Advantages
- Encourages brainstorming and creativity through group dynamics.
- Can reveal shared requirements and common pain points quickly.
- Provides insights into conflicting priorities between stakeholders.
- Faster than one-on-one interviews for collecting diverse views.
- Disadvantages / Challenges
- Risk of groupthink (participants conforming to dominant opinions).
- Strong personalities may overshadow others.
- Not ideal for sensitive or confidential requirements.
- Requires a skilled moderator to keep the discussion productive.

### Slide 24

Existing Documentation
- Purpose
- To extract useful information about the system, processes, and constraints from already 
available documents.
- Helps analysts understand the current system and business domain before engaging 
stakeholders.
- Serves as a baseline for identifying gaps and improvements.
- Types of Documentation to Review
- Business documents: policies, procedures, contracts, regulations.
- System documents: user manuals, technical specifications, source code documentation.
- Process documentation: workflow charts, SOPs (standard operating procedures).
- Historical documents: bug reports, change requests, meeting minutes.
- Standards & compliance docs: industry regulations, legal requirements.

### Slide 25

Existing Documentation
- Process
- Collect relevant documents from the client or organization.
- Analyze for requirements-related information (functional, nonfunctional, constraints).
- Highlight assumptions, ambiguities, or inconsistencies.
- Validate findings with stakeholders (documents may be outdated or 
inaccurate).

### Slide 26

Existing Documentation
- Advantages
- Provides objective, written evidence (less biased than personal opinions).
- Saves time — reduces the need to “start from scratch.”
- Helps analysts prepare better for stakeholder interviews/focus groups.
- Useful for understanding regulatory and compliance requirements.
- Disadvantages / Challenges
- Documentation may be outdated or incomplete.
- Risk of misinterpretation if the analyst is not familiar with the domain.
- May not reflect real-world practices (users often deviate from official processes).
- Still requires validation with stakeholders.

### Slide 27

Observation
- Purpose
- To directly watch how stakeholders perform tasks in their real work environment.
- Helps identify requirements that may not be articulated during interviews or focus 
groups.
- Captures actual workflows, pain points, and user behaviors.
- Types of Observation
- Passive observation: Analyst observes silently without interfering.
- Active observation / participant observation: Analyst interacts, asks clarifying 
questions, or even performs the task.
- Shadowing: Following a user throughout their workday to see the full workflow.

### Slide 28

Observation
- Preparation
- Identify which processes, roles, or tasks to observe.
- Get permission and explain the purpose to participants.
- Prepare checklists or observation guides (e.g., steps followed, tools used, 
time taken, errors faced).
- Conducting the Observation
- Observe the sequence of tasks, tools, interactions, and bottlenecks.
- Take detailed notes, photos, or video recordings (if permitted).
- Minimize interference so users behave naturally.
- Ask clarifying questions after the activity (to avoid disrupting workflow).

### Slide 29

Observation
- Advantages
- Reveals real practices, not just what stakeholders say they do.
- Identifies workarounds and hidden needs that may not appear in documentation.
- Helps discover non-functional requirements (usability, performance).
- Provides context for system integration with real-world workflows.
- Disadvantages / Challenges
- Can be time-consuming, especially for complex processes.
- Stakeholders may alter their behavior if they know they’re being watched 
(“Hawthorne effect”).
- Some tasks may be sensitive (e.g., in healthcare, finance).
- Observed data may need careful interpretation to avoid bias.

### Slide 30

Prototyping
- Purpose
- To make requirements more tangible by creating a working model of the system.
- To help stakeholders articulate requirements they may struggle to express verbally.
- To validate assumptions early and reduce misunderstandings.
- Types of Prototypes
- Throwaway (rapid) prototypes → quickly built to explore ideas, then discarded.
- Evolutionary prototypes → incrementally refined until they evolve into the final system.
- Low-fidelity prototypes → sketches, wireframes, mock-ups.
- High-fidelity prototypes → interactive demos, partial system implementations.
- Process
- Build an initial mock-up or simplified version of the system.
- Show it to stakeholders and gather feedback.
- Refine the prototype iteratively until requirements are clearer.
- Use it as a communication tool between developers and stakeholders.

### Slide 31

Prototyping
- Advantages
- Makes abstract requirements concrete and visual.
- Helps uncover usability issues and hidden needs early.
- Encourages active participation from stakeholders.
- Reduces risk of delivering the wrong system.
- Disadvantages / Challenges
- Can be time-consuming and costly if not managed properly.
- Stakeholders may confuse prototype with the final product.
- Risk of focusing too much on UI/visuals while ignoring deeper system 
requirements.
- If used as throwaway, effort may feel “wasted” if not reused.

### Slide 32

Questionnaire
- Purpose
- To gather requirements, opinions, or preferences from a wide audience.
- To collect both quantitative data (e.g., frequency of use, importance ratings) and qualitative data
(e.g., open-ended feedback).
- Useful for validating requirements across many users.
- Structure
- Closed-ended questions → multiple choice, Likert scale (1–5 rating), yes/no.
- Open-ended questions → free text responses to capture detailed opinions.
- Often a mix of both for balance between measurability and insights.
- Preparation
- Define clear objectives (e.g., “What features are most important to users?”).
- Keep it concise (shorter surveys have higher response rates).
- Pilot test the questionnaire before distribution.
- Choose an appropriate delivery method (online form, email, printed survey).

### Slide 33

Questionnaire
- Advantages
- Can reach large numbers of stakeholders quickly and cheaply.
- Provides quantifiable results that can be statistically analyzed.
- Anonymity may encourage more honest responses.
- Easy to compare responses across different user groups.
- Disadvantages / Challenges
- Responses may lack depth compared to interviews or focus groups.
- Poorly designed questions can lead to ambiguous or biased results.
- Risk of low response rate, reducing representativeness.
- No chance for immediate clarification (unlike interviews).

### Slide 34

Scenarios
- Purpose
- To describe realistic, story-like use situations of the system.
- To help stakeholders visualize how the system will support their goals.
- To uncover requirements related to workflows, exceptions, and edge cases.
- Structure
- Actors (who is involved — users, systems, external entities).
- Context (the situation or environment in which the scenario occurs).
- Goals (what the actor is trying to achieve).
- Steps/Interactions (sequence of actions between user and system).
- Variations/Exceptions (what happens if things go wrong).

### Slide 35

Scenarios
- Advantages
- Easy for stakeholders to relate to and validate (natural language, story-like).
- Helps discover both functional and non-functional requirements.
- Reveals exceptions and alternative flows that might be missed in interviews or 
questionnaires.
- Provides a foundation for use cases, test cases, and prototyping.
- Disadvantages / Challenges
- May oversimplify complex systems if not detailed enough.
- Can be time-consuming to create comprehensive scenarios for all possible cases.
- Risk of focusing too much on specific examples rather than general requirements.

### Slide 36

Can We Blend the Elicitation Techniques?
- In most cases, YES!
- We blend the techniques to be: 
- more effective with our engagement with the stakeholders
- Speed up the requirements discovery
- Often, requirements are not standalone. Blending the 
techniques could bring up these types of requirements or relate 
one requirement to another.
36

### Slide 37

More about Elicitation Techniques
37
https://www.youtube.com/watch?v=kCJFBmAAvV4

### Slide 38

Requirements Engineering: Analysis
- Refining and extending the initial requirements
- Extract more details that would help in mapping to a solution
- Could lead to many modifications or the addition of new 
requirements.
38

### Slide 39

Requirements Engineering: Validation
“Are we building the RIGHT product? "
- Validity: 
Does the system provide the functions that best support the needs?
- Consistency: 
Are there any requirements conflicts?
- Verifiability: 
Can the requirements be checked?
- Realism: 
Can the requirements be implemented given available budget and technology 
- Completeness:
Are all functions required by the stakeholders included? 
39

### Slide 40

Requirements Engineering: Validation Techniques
40
Requirements 
Reviews & 
Walkthrough
Systematic manual 
analysis of the 
requirements
Prototyping
Use an 
interactive/executable 
model of the system 
to check 
requirements.
Test-case 
Generation
Develop test cases for 
each requirement to 
check testability

### Slide 41

Requirements Engineering: Management
The process of managing changing requirements during the 
requirements engineering process and system development
41
Elicitation Analysis Validation
Management
High
level
Detailed
level

### Slide 42

Requirements Modelling
Representation of requirements in standardized and uniform way
42

### Slide 43

Two Major Types of Requirements
43
Functional Requirements
“What”
Non-Functional Requirements
“How well”
Action/Tasks that the software 
product must be able to perform 
from the user perspective
Quality Attributes of the software 
product Design Constraints, such as 
Platform constraints and Response 
times

### Slide 44

Functional User Requirements
Requirements may be high-level statements of what the system 
should do. These are called Functional User Requirements.
For example, in a Patient Management System (PMS) for a group of clinics:
44
A user shall be able to search the appointments lists for all clinics
The system shall generate each day, for each clinic, a list of 
patients who are expected to attend appointments that day.
Each staff member using the system shall be uniquely identified 
by his/her eight-digit employee number.

### Slide 45

Functional System Requirements
- Should describe the user requirements 
in detail. 
- Map a problem to a solution without 
implementation detail and in the user’s 
language. 
- Describe the interaction between the 
system and its environment. 
- The details of a requirement can highly 
affect your planning and negotiation
with the client. 
45
Details can come from:
What does the system do?
What are the alternative scenarios 
of success?
What are the input/output?
What happens when an error 
occurs?

### Slide 46

Discussion: Functional User Requirements
Patient Management System (PMS)
- Is everything in this statement ready for you to design the 
solution for this requirement? 
- Do you have any further questions?
- Is the statement clear? 
46
A user shall be able to search the appointments lists for all clinics

### Slide 47

Possibility 1:
You may want to ask…
- Who: All users? Or specific roles? 
- Input: search by what? Dates, Text search? Names? IDs? A 
combination of above? 
- Output: How information to show? With names, id and 
what? What other info to list in the result page? 
- Alternative scenarios: if no records are found, should a 
recommendation of close results be shown. 
- Exceptions: Are users allowed to enter invalid dates? 
47
A user shall be able to search the appointments lists for all clinics
With this, you can start 
design (the solution). 
Note:
No implementation or 
technical details. Only 
details that will affect your 
planning.

### Slide 48

Non-Functional Requirements – “How Well”
- How well will the system perform? 
- Quality Attributes: 
- Reliability 
- Security
- Usability
- Performance 
- Design Constraints
- Platform constraints
- Response times 
- Some are more important than the others for different industries. 
- Fill out the context of the overall Functional Requirements and determine 
overall quality.
48

### Slide 49

Quality Attributes & Design Constraints
Product requirements Organizational requirements External requirements
Specify or constrain the 
behaviour of the Software.
- Performance requirements
- Reliability requirements
- Security requirements
- …
Broad system requirements
derived from policies and procedures 
in the organization.
- Operational process requirements
- Development process requirements
- Environmental requirements
- …
Derived from factors external to 
the system and its development 
process.
- Regulatory requirements
- Legislative Requirements
- Ethical requirements
- … 
49
Supplementary reading to further your understanding:
Berander, P., Damm, L. O., Eriksson, J., Gorschek, T., Henningsson, K., Jönsson, P., ... & Wohlin, C. (2005). Software quality attributes and 
trade-offs. Blekinge Institute of Technology, 97(98), 19.

### Slide 50

Examples of Non-Functional Requirements
- Product Requirement
The Patient Management System (PMS) shall be available to all clinics 
during normal working hours (Mon-Fri, 08:30-17:30). Downtime within 
the normal working hours shall not exceed five seconds in any one day.
- Organisational Requirement
Users of the PMS shall authenticate themselves using their health 
authority identity card.
- External Requirement
The PMS shall implement patient privacy provisions as set out in HStan03-2006-priv.
50

### Slide 51

SIT INF2001 - AY24/25, Tri 1
What Makes a Requirement Good? (1/2)
1. Verifiable
- Stated in such a way that it can be 
tested by inspection, analysis, or 
demonstration. 
2. Clear & Concise
- must consist of a single requirement,
- must be easily read and understood by 
nontechnical people, and
- not susceptible to multiple 
interpretations 
3. Traceable
- has a unique identity or number, 
- cannot be separated or broken into 
smaller requirements, and
- can easily be traced through to 
specification, design, and testing 
4. Viable
- can be met using existing technology, 
- can be achieved within the budget, 
- can be met within the schedule, and 
- does the organization have the 
necessary skills
51

### Slide 52

SIT INF2001 - AY24/25, Tri 1
What Makes a Requirement Good? (2/2)
5. Consistent
- does not conflict with other 
requirements 
- uses the same terminology 
throughout the requirement 
specification, and
- does not duplicate other 
requirements or pieces of them 
6. Implementation Free
- allows the system developer to 
decide what technology is best 
suited to achieve the function. 
7. Complete
- contains all the information that is 
needed to define the system 
function, and
- leaves no one guessing (For how 
long?, 50 % of what? What units) 
52

### Slide 53

“Medical staff shall be able to use all the system functions after four 
hours of training. After this training, the average number of errors made 
by experienced users shall not exceed two per hour of system use.”
NON-FUNCTIONAL REQUIREMENTS
53
“The system should be easy to use by medical staff and should 
be organized in such a way that user errors are minimized.”

### Slide 54

Writing Requirements
Communicating requirements right to their respective audience is critical to the 
success of the project 
54

### Slide 55

Requirements Specification Can Be Represented In the Following 
Formats:
1 - Natural 
language
2 - Structured 
natural 
language 
4 - Graphical 
notations
3 -
Mathematical 
specifications
55

### Slide 56

1 - Natural Language Specifications
3.2 The system shall measure the blood sugar 
and deliver insulin, if required, every 10 minutes.
(Changes in blood sugar are relatively slow so 
more frequent measurement is unnecessary; less 
frequent measurement could lead to 
unnecessarily high sugar levels.)
56
3.6 The system shall run a self-test routine every 
minute with the conditions to be tested and the 
associated actions defined in Table 1. (A self-test 
routine can discover hardware and software 
problems and alert the user to the fact the 
normal operation may be impossible.)
-The requirements are 
written using numbered 
sentences in natural 
language. 
-Each sentence should 
express one requirement. 
-Supplemented by 
diagrams and tables

### Slide 57

1 - Natural Language Specifications
57
Benefits:
Expressive, intuitive and universal. This means that the requirements can 
be understood by users and customers. 
Problems: 
- Lack of clarity: Precision is difficult without making the document 
difficult to read. 
- Requirements confusion: Functional and non-functional requirements 
tend to be mixed-up. 
- Requirements mix: Several different requirements may be expressed 
together.

### Slide 58

2 - Structured Natural Language
- Requirements are written in a standard way.
- Example of form-based specification:
- Definition of the function or entity.
- Description of inputs and where they come from.
- Description of outputs and where they go to.
- Information about the information needed for the 
computation and other entities used.
- Description of the action to be taken.
- Pre and post conditions (if appropriate).
- The side effects (if any) of the function.
58

### Slide 59

3 - Formal Specification
These notations are based on mathematical concepts such as 
finite-state machines or sets. 
59
https://ai2-s2-public.s3.amazonaws.com/

### Slide 60

3 - Formal Specification
Advantages
- Unambiguous specifications, can reduce the ambiguity in a requirements document 
Disadvantages
- Requires experts and takes more time. 
- Most customers don’t understand a formal specification. They cannot check that it 
represents what they want and are reluctant to accept it as a system contract

### Slide 61

4 - Graphical Notations 
Specifications
- Graphical models, supplemented by text 
annotations, are used to define the 
functional requirements for the system; 
- UML use case and sequence diagrams are 
commonly used.
61

### Slide 62

Requirements Selection
- Who are your stakeholders?
- Client
- Users
- Organisation / environment
- APIs used / legacy systems
- Payors
- Rate your stakeholders based on decision making.
- Use your stakeholders’ rating to rate each requirement to filter 
requirements by priority.
62

### Slide 63

Prioritising Requirements
- MoSCoW Prioritisation. 
-Categorise your requirements into the following groups.
❖Must-have
❖Should-have
❖Could-have
❖Will-not-have
- Common practise to give a unique identifier to each requirement.
- Identify the tasks required to achieve each requirement.
- Give a unique identifier for each task and file them as an issue in your 
team’s Kanban board.
63

### Slide 64

Put all together - Software Requirements Specification (SRS)
- Definition
- A formal document that captures the complete description of a software system’s 
requirements, including what the system should do and the constraints under which it 
must operate.
- Purpose:
- Serves as an agreement between stakeholders (clients, users, and developers).
- Provides a clear, structured, and unambiguous reference for design, implementation, 
and testing.
- Reduces misunderstandings and scope creep during development.
- Characteristics of a Good SRS (IEEE standard):
- Correct → reflects true stakeholder needs.
- Unambiguous → precise and clearly stated.
- Complete → all necessary requirements covered.
- Consistent → no conflicts or contradictions.
- Verifiable → requirements can be tested.
- Modifiable → easy to update when requirements change.
- Traceable → each requirement can be tracked through design, implementation, and 
testing.

### Slide 65

What are covered today
- Software requirements
- The process of requirement engineering
- Requirements modelling


---

## Week 3: Use Case Diagram and Activity Diagram

### Slide 1

INF2001
Introduction to Software Engineering
Week 3
A/Prof Frank Guan

### Slide 2

1 - Elicitation 2 - Analysis
3 - Validation 4 - Management
Activities of 
Requirements 
Engineering
2
Refining and extending the 
initial requirements
Are we building the right 
product?
The process of 
requirements discovery
Needed because of the 
changing requirements

### Slide 3

Moving from a Problem to Solution
3
Requirement 
specification
Analysis and 
Design
Implementation
Testing
Deployment
Environment Maintenance
(User World + Problem Domain)
The System
(Machine World)
System
Requirement 
Specifications:
Bridging user 
requirements to what 
the system can do
The real-world
assumptions related to 
our system
User Requirements:
What the user wants 
to do (from their 
perspectives
Software system (code, 
frameworks, DBS etc)
Hardware system 
(device, server machine, 
etc)
Solution Domain

### Slide 4

4
What if we skip the Analysis & 
Design phase and go directly to 
implementation?

### Slide 5

SIT ICT2x01 Introduction to Software Engineering, AY22/23, Tri 1
In terms of Designing 
a House…
- After collecting your requirements, 
you will have a high-level concept of 
the clients requirements.
- Your models are mostly Conceptual
design for communicating with the 
client.
5
Source: https://www.autodesk.com/products/revitlt/features?plc=RVTLT&term=1-YEAR&support=ADVANCED&quantity=1

### Slide 6

When Building 
the House…
6
- Besides the high-level 
conceptual design, you will 
need detailed models for 
execution and 
implementation

### Slide 7

How to do Modeling ?

### Slide 8

8
Use Cases
- Use Case
- describes how a user (actor) interacts with a system to achieve a specific goal
- Focuses on functional requirements (what the system should do).
- Captures the system’s intended behavior in various scenarios.
- Benefits of Use Cases:
- Bridge between requirements and system design.
- Help stakeholders understand system behavior without technical details.
- Provide a basis for:
❖ System design
❖ Test case development
❖ Project planning

### Slide 9

Example 1: Library Management System
- Functional Requirement (FR):
“The system shall allow members to borrow and return books.”
- Derived Use Cases:
- Search Book (goal) – member (actor) searches for a book.
- Borrow Book (goal) – member (actor) borrows a book (includes Check 
Availability).
- Return Book (goal) – member (actor) returns borrowed book.
- Renew Book (goal) – member (actor) extends borrowing period.
- Pay Fine (goal) – member (actor) pays overdue fines.

### Slide 10

Example 2: ATM System
- Functional Requirement (FR):
“The system shall enable bank customers to withdraw, deposit, and check 
their balance using an ATM.”
- Derived Use Cases:
- Authenticate User (goal) – customer (actor) inserts card & enters PIN.
- Withdraw Cash (goal) – customer (actor) takes out money (includes Authenticate 
User).
- Deposit Cash (goal) – customer (actor) deposits money (includes Authenticate 
User).
- Check Balance (goal) – customer (actor) views account balance.
- Print Receipt (goal) – system (actor) prints transaction details.

### Slide 11

11
Exercise: which of these requirements should be 
represented directly in a use case?
- Special deals may not run longer than 6 months.
- Customers only become preferred after 1 year.
- A customer has one and only one sales contact.
- Database response time is less than 2 seconds.
- Web site uptime requirement is 99.8%.
- Number of simultaneous users will be 200 max.
Answer: NONE. These requirements are non-functional.

### Slide 12

12
Use cases vs. internal features
- consider software to run a cell phone:
Use Cases
 call someone
 receive a call
 send a message
 memorize a number
Point of view: user
Internal Functions
 transmit / receive data
 energy (battery)
 user I/O (display, keys, ...)
 phone-book mgmt.
Point of view: developer / 
designer

### Slide 13

13
Actors and goals
- Actor: anything with behavior (acts on the system)
- primary actor: initiates interaction to achieve goal
- supporting actor: performs sub-goals in use case
- Goal: the desired outcome an actor wants to achieve through interaction with 
the system.
- It expresses why the actor is using the system in the first place.
- Every use case should ultimately fulfill a goal.
- Example:
- Actor: Customer
- Goal: Withdraw money from ATM

### Slide 14

Examples of Goals in different domains
- ATM System: Withdraw money, Deposit money, Check balance.
- E-commerce Site: Search product, Add to cart, Make payment.
- Library System: Borrow book, Return book, Pay fine.
- Learning Platform: Upload material, Enroll in course, Take quiz.

### Slide 15

Types of goals
- User Goals (Primary Goals)
- The main objectives that external actors want to accomplish.
- Directly drive the creation of use cases.
- Example: Book a flight ticket, Borrow a book, Purchase a product.
- Sub-Goals (Supporting Goals)
- Steps needed to achieve a larger goal.
- Often modeled as “include” use cases in UML.
- Example: Authenticate User (supports Withdraw Cash).

### Slide 16

Levels of use case goals
- Summary Level – high-level, business-oriented goal.
- Example: Manage customer banking.
- User Goal Level – a complete interaction with a meaningful result.
- Example: Withdraw money.
- Sub-function Level – low-level supporting steps.
- Example: Enter PIN, Validate account.

### Slide 17

A good Use Case
Focuses on interaction 
- Starts with a request from an actor to the system. 
- Ends with the production of all the answers to the request. 
Focuses on essential behaviours, from the actor’s point of view 
- Does not describe internal system activities. 
- Does not describe the GUI in detail. 
Concise, clear, accessible to non-programmers 
- Easy to read.
- Summary fits on a page.
- Main success scenario and extensions. 
17

### Slide 18

How to present Use Cases?

### Slide 19

19
Presenting Use Cases
Step 1. Summary of Use Cases
1a. Actor / goal list
1b. UML use case diagram
Step 2. Description of each Use Case

### Slide 20

20
1a. Actor / goal list
- To create a list or table of actors and their "goals"
ACTOR USE CASES INITIATED
Club Member Submit Promotion Order
Submit Regular Order
Potential Member Submit New Subscription
Past Member Submit Subscription Renewal
Membership Services Dept. Request Membership
Marketing Department Create New Monthly Promotion
Create New Seasonal Promotion
Create New Subscription Program
Request Promotion Reports
Request Sales Reports
Membership Services System Send New Subscription Offer
Send Club Promotion
Send Subscription Renewal

### Slide 21

21
1b. Use Case diagram
Control System
Set limits
Calibrate
Take profile
Scan
Liaison Physicist
Hardware Specialist
Experimental
Physicist
- Actor: stick-man
- Use Cases: ellipses 
with use case name 
inside
- Actor-case 
association: line

### Slide 22

What are Use Cases in the Use Case Diagram?
- An actual use case of the system by an actor or actors.
- There should not be processes or not part of a process in the Use Case 
diagram.
- Hence, in a Use Case diagram, there should not be any flow of the 
system.
- The Use Case diagram captures what each actor can use the system for.
22

### Slide 23

Notation of Use Case diagrams
23
Actor of the system
Name of the system
Actor of the system
Name of the Use Case Use Case
System’s Boundary

### Slide 24

24
Another Example: Use Case diagram

### Slide 25

Use Case diagrams: Actors
- An actor is a member of the world outside 
the software product 
- It is usually easy to identify an actor
- An actor is frequently a user of the software 
product 
- In general, an actor plays a role with regard 
to the software product. This role is 
- As a user; or
- As an initiator; or
- As someone who plays a critical part in the use case 
25

### Slide 26

Name Actors base on the functions it plays
26

### Slide 27

Use Case diagrams: more on actors
- An actor need not be a human being 
Example: An e-commerce information system has to interact with the 
credit card company information system 
- The credit card company information system is an actor from the viewpoint 
of the e-commerce information system 
- The e-commerce information system is an actor from the viewpoint of the 
credit card company information system
27

### Slide 28

Use Case should achieve Goal but NOT flow
28
“A use case is the 
specification of a set of 
actions performed by a 
system, which yields an 
observable result that is 
typically of value for one 
or more actors or other 
stakeholders of the 
system.” 
User Goal

### Slide 29

Use Case Diagram Stereotypes <<include>>
- Check Balance includes Validate 
Pin use case
- Validation Pin process is required
in the flow of Check Balance (not 
optional) 
- Validate Pin use case is extracted
for reusability since other use 
cases use it. 
- Validate Pin is not created to 
stand on its own as a use case 
29

### Slide 30

How to Use Stereotypes <<include>>
- “Validation Pin" use case process is required in 
the flow of "Check Balance" use case. This means 
that whenever "Check Balance" use case occurs, 
the entire "Validation Pin" use case processes 
must always take place.
- It usually only make economical sense to use 
<<include>> when the included use case is 
required by more than one use cases. In the case 
of our example, “Check Balance” and “Withdraw 
Cash” use cases required “Validation Pin” use 
case.
30

### Slide 31

Use Case Diagram Stereotypes <<extend>>
- “Report Forgery“ use case 
extends “Validate ID Card" use 
case to add to its functionality 
- An optional additional use case 
that usually depends on a set of 
condition(s) in the validate ID card 
use case
- Note the arrow direction 
31

### Slide 32

- Accompany the use case diagrams.
- A detailed description of the user's interaction with the software product 
to achieve a goal. 
- Should describe what will happen in all possible scenarios
2. Writing a Use Case description
32

### Slide 33

SIT INF2001 - AY24/25, Tri 1
Use Case Description Template (Simplified)
Use Case ID: A unique identifier 
Use case Name: Action name 
Description: quick overview 
Primary Actor: an entity that acts on the system 
(Person, external hardware (like a timer), or another 
system. 
Pre-conditions: Indicates what the system will ensure 
is true before letting the use case start. 
Main success scenario: steps needed for the user to 
achieve the main goal (assuming success in all steps) 
Alternative Scenarios: Describe all the other scenarios 
for this use case – including exceptions. 
Post-conditions: Indicates what the system will 
ensure is true after the use case is done. (can be 
specific to different scenarios) 
Priority: Low, medium, high 
Non-Functional Requirements (if any): Any specific 
non-functional dependencies ? 
33

### Slide 34

Example of Use Case Description
ID: UC-6
Name: Register for courses 
Description: Student accesses the system and views the courses currently available for him to 
register, selects the courses and registers for them. 
Primary Actor: Student 
Preconditions: Student is logged into system. 
Main Success Scenario: 
1. Student chooses to register a new course
2. System displays list of courses available for registration.
3. Student selects one or more courses to register for.
4. Student submits information.
5. System registers student for the selected courses, displays a confirmation message.
6. System sends a confirmation email. 
34

### Slide 35

Main and Alternative Scenarios
Main Success Scenario: 
1. Student chooses to register a new 
course
2. System displays list of courses 
available for registration.
3. Student selects one or more 
courses to register for.
4. Student submits information.
5. System registers student for the 
selected courses, displays a 
confirmation message.
6. System sends a confirmation email. 
35
Alternative Scenarios: 
2a. No courses available for this student 
2a1. System displays error message saying no 
courses are available and provides the reason. 
5a. Some courses could not be registered. 
5a1. System displays error message showing 
the courses that were successfully registered, 
and provides the reason for those that were not 
6a. Email was not sent 
6a1. System gives a message that the 
confirmation email was not sent, and offer retry 
option 
6a2. Student can choose to retry or quit 
screen

### Slide 36

Example of Use Case Description
ID: UC-6
Name: Register for courses 
Description: Student accesses the system and views the courses currently available for him to 
register, selects the courses and registers for them. 
Primary Actor: Student 
Preconditions: Student is logged into system. Student fees are paid.
Main Success Scenario: 
1. Student chooses to register a new course
2. System displays list of courses available for registration.
3. Student selects one or more courses to register for.
4. Student submits information.
5. System registers student for the selected courses, displays a confirmation message.
6. System sends a confirmation email. 
36

### Slide 37

Example of Use Case Description
ID: UC-6
Name: Register for courses 
Description: Student accesses the system and views the courses currently available for him to register, selects the courses and registers for them. 
Primary Actor: Student 
Preconditions: Student is logged into system. Student fees are paid.
Main Success Scenario: 
1. Student chooses to register a new course.
2. System displays list of courses available for registration.
3. Student selects one or more courses to register for.
4. Student submits information.
5. System registers student for the selected courses, displays a confirmation message.
6. System sends a confirmation email. 
Alternative Scenarios: 
2a. No courses available for this student
2a1. System displays error message saying no courses are available and provides the reason. 
5a. Some courses could not be registered.
5a1. System displays error message showing the courses that were successfully registered, and provides the reason for those that were not
6a. Email was not sent 
6a1. System gives a message that the confirmation email was not sent, and offer retry option 
6a2. Student can choose to retry or quit screen 
Post conditions: Main: Student has one or more course registered. Email sent 6a. Email was not sent 
Priority: High 
37

### Slide 38

Activity diagram

### Slide 39

39
Activity Diagram
- Activity diagrams describe the 
workflow behavior of a system.
- Activity diagrams are used in process modeling 
and analysis of during requirements engineering.
- A typical business process which synchronizes 
several external incoming events can be 
represented by activity diagrams. 
- They are most useful for understanding 
workflow analysis of synchronous 
behaviors across a process.

### Slide 40

40
Activity Diagram
- The main reason to use activity 
diagrams is to model the workflow behind 
the system being designed.
- Activity diagrams are also be used for 
- documenting existing process 
- analyzing new Process Concepts 
- finding reengineering opportunities.

### Slide 41

41
Activity Diagram concepts
- An activity is trigged by one or more events 
and activity may result in one or more 
events that may trigger other activity or 
processes. 
- Events start from start symbol and end with 
finish marker having activities in between 
connected by events. 
- The activity diagram represents the 
decisions, iterations and parallel/random 
behavior of the processing. 
- They capture actions performed. 
- They stress on work performed in 
operations (methods).

### Slide 42

42
Activity Diagram Example
Fork
Branch
Start State
Merge Join
Activity
End State

### Slide 43

43
Components - Start Point (initial node) - Indicates where the flow begins. - End Point - Represented by a bullseye (circle with dot inside). - Activity - Represented by a rounded rectangle. - Each action is a step in the workflow. - Decision - Represented by a diamond. - Used for conditional flows (yes/no, if/else). - Flow / Transition - Arrows showing the sequence of activities. - Fork & Join - Represented by thick horizontal/vertical bars. - Fork → splits flow into parallel activities. - Join → synchronizes parallel flows
Activity

### Slide 44

44
Components
- An activity is an ongoing, though interruptible, 
execution of a step in a workflow (such as an 
operation or transaction)
- Represented with a rounded rectangle. 
- Text in the activity box should represent an activity 
(verb phrase in present tense). 
- A decision may be shown by labeling multiple 
output transitions of an activity with different guard 
conditions. 
- For convenience a stereotype is provided for a decision: the 
traditional diamond shape, with one or more incoming 
arrows and with two or more outgoing arrows, each labeled 
by a distinct guard condition with no event trigger. 
Activity

### Slide 45

45
Components
- A fork is used when multiple activities are occurring at the 
same time.
- A branch describes what activities will take place based on 
a set of conditions.
- All branches at some point are followed by a merge to 
indicate the end of the conditional behavior started by that 
branch.
- After the merge all of the parallel activities must be combined 
by a join before transitioning into the final activity state.
Activity

### Slide 46

46
Example: withdraw 
money from a bank 
account through an 
ATM

### Slide 47

47
Disadvantages
- A disadvantage of activity diagrams is that they do not explicitly present 
which objects execute which activities, and the way that the messaging 
works between them. 
- Labeling of each activity with the responsible object can be done. 
- It is useful to draw an activity diagram early in the modeling of a process, to help 
understand the overall process.

### Slide 48

48
References
- Activity Diagrams
- http://pigseye.kennesaw.edu/~dbraun/csis4650/A&D/UML_tutorial/activity.htm
- http://isds.bus.lsu.edu/cvoc/learn/bpr/cprojects/spring1998/modeling/activity.html
- http://www-106.ibm.com/developerworks/rational/library/2802.html
- Fast Track UML 2 (from Books 24x7)

### Slide 49

Summary of today
- Use case
- Use case diagram
- Activity diagram


---

## Week 4: Class Diagram and Sequence Diagram

### Slide 1

INF2001
Introduction to Software Engineering
Week 4
A/Prof Frank Guan

### Slide 2

Recap of last week
- Use case
- Use case diagram
- Activity diagram

### Slide 3

You have the use cases now. What’s next?
ID: UC-6
Name: Register for courses 
Description: Student accesses the system and views the courses currently available for him to 
register, selects the courses and registers for them. 
Primary Actor: Student 
Preconditions: Student is logged into system. 
Main Success Scenario: 
1. Student chooses to register a new course
2. System displays list of courses available for registration.
3. Student selects one or more courses to register for.
4. Student submits information.
5. System registers student for the selected courses, displays a confirmation message.
6. System sends a confirmation email.

### Slide 4

Before that, let’s have a recap about OOP

### Slide 5

What is Object-oriented Programming?
- A computer programming model that organises software 
design around objects. 
- An object represents a real-world physical thing or a data 
record.
- An object can be defined as a data field that has unique 
attributes and behaviours.
- More details covered in module INF1009.

### Slide 6

The Object-Oriented Paradigm
- A software system is structured as a collection of encapsulated 
objects. Classification of objects are known as Classes.
- Each object has its data and its actions
- The overall behaviour of the system arises out of the interactions
between the individual objects.
6

### Slide 7

Benefits: the Object-Oriented Paradigm
- Increase REUSE due to the modularity
- Increase maintainability since it accommodates for changes 
while protecting the existing structure 
- Help enforcing good design techniques 
- It’s real-world-like design makes it more understandable by 
non-technical audience. 
7

### Slide 8

Object-Oriented Analysis
- Classes and objects
- Noun extraction
- Modelling 
- Class diagram
- Class types
- Scenarios 
- Sequence diagram
8

### Slide 9

Object-Oriented Analysis
- OO is (claimed to be) a more ‘natural’ mapping between the real-world
objects and the system-world objects
- We generalise real-world objects into types: people, buildings, cars, 
food, etc.
- Uses concepts and categorising the concepts of real-world objects into 
Classes
- Closer to the way how 
humans think
Student
- name
- matric
- transcript
+ get_name();
+ get_transcript();
9

### Slide 10

Class
A program template to define the data (attributes) 
maintained by the object and actions performed by it
Object
Instance of the class
10

### Slide 11

Jodie Daria Jane Brittany Joe
Student
- name
- matric
+ get_name();
+ get_transcript();
Student
:Student
- name:string[20] = “Jodie”
- matric:Matric = 16SIC987
+ get_name():string[20];
+ get_transcript():Transcript;
class
object
(An instance of 
Student class)
11

### Slide 12

Objects & Instances
- An object (instance of a class) is a self contained entity. 
- Each object has identity, state, and services. 
12

### Slide 13

Object
An object's identity is 
the unique reference to that 
object in the environment. 
Name: Ann Tan
IC: ABCDEF123
13

### Slide 14

Object
The object's state is the data it 
stores in fields (variables/attributes)
Mood: Happy
Age: 20
Matriculated: Yes
14

### Slide 15

Object
Services (methods/functions) 
describe the behaviours that the object 
advertises for use by other objects.
+get_my_name()
+get_my_transcript()
15

### Slide 16

Let’s come back to Use Case
Buttons in elevators
Buttons on each floor, 
outside the elevators
How to proceed from Use Case to Classes?

### Slide 17

Modelling the Domain: The Beginnings
- Start identifying the Entities in the domain your software is 
intended to work under.
Entity definition:
“A thing with distinct and independent existence”, 
Oxford Dictionary.

### Slide 18

How to extract Entity Class and their attributes?
- Deduce the classes from use cases of the software and their scenarios
- identify the items that play a role
- Often there are many scenarios
- Possible danger: too many candidate classes
- easier to add later than remove
- Quickly you will realized that there are so many possibilities and can be 
confusing.
- In the following slides, we will introduce an approach you can start with. 
18

### Slide 19

Write a Solution Abstract to Begin
- Start with the most prominent actor. If your solution has more than one, 
just choose one of the most prominent actor first to establish your 
model. You can expand your model once you have establish it.
- Write the solution abstract in a sentence or two that includes the
❖ Thing/Object,
❖ Address a need, and
❖ Actor
- Repeat the sentence structure until you cover the abstraction of the software 
product in a single paragraph.
19

### Slide 20

20
Elevator Case Study
To help illustrate the approach in the following 
slides, we will use the Elevator system found in 
many buildings as a case study.

### Slide 21

Noun Extraction
Stage 1. Concise solution description
Describe the an abstraction of software product in a 
single paragraph: 
“The buttons in the elevator and on floors are used 
to control the movement of N elevators in a building 
with M floors for the user.
The buttons to illuminate to feedback that the 
request is accepted for user.
The buttons to off illumination to feedback that the 
cancel request is accepted for user. 
The elevator to remain on its current floor with its 
doors closed when there are no user requests.”
21
Buttons in elevators
Buttons on each floor, 
outside the elevators

### Slide 22

Noun Extraction
Stage 2. Identify the nouns
Identify the nouns in the informal description
Use the nouns as candidate classes
“The buttons in the elevator and on floors are used 
to control the movement of N elevators in a building 
with M floors for the user.
The buttons to illuminate to feedback that the 
request is accepted for user.
The buttons to off illumination to feedback that the 
cancel request is accepted for user. 
The elevator to remain on its current floor with its 
doors closed when there are no user requests.”
22

### Slide 23

Noun Extraction
1. Nouns Identification
- button, elevator, floor, movement, building, illumination, request, door
- Exclude nouns outside problem boundary 
- eliminates: floor, building, door
- Exclude abstract nouns (may become attributes or services)
- eliminates: movement, illumination, request
2. Remove duplicates and convert to Singular
3. Candidate classes: 
- Elevator and Button
4. Subclasses:
- Elevator Button and Floor Button
23

### Slide 24

Class Confirmation Criteria
A noun should become a class if: 
- Needed Remembrance
- Needed Services (Operations)
- Multiple Attributes
24

### Slide 25

A Class Can be Any of the Following
- Tangible Entity
- Abstract Entity
- Role
- Event
25

### Slide 26

Identifying Services & Behaviours
- Candidate classes (from nouns): 
Elevator, Elevator Button, Floor Button 
- Services and behaviours of objects can be considered based on 
verbs in the textual descriptions (use case, scenarios)
26

### Slide 27

- Goals
-Maintainable (change without breaking other parts) 
-Reusable & Organized – help enforce good design 
-Decrease dependency (loose coupling)
-Helps team to divide labor (reliably) – Help in our 
process 
28
B
WeatherAPI
A
NewsWeather
How do you implement the concepts of OO?

### Slide 28

Object Namespaces
Defining an object belonging to a class
Object Identifier : Class Identifier
29
A : NewsWeather
B : WeatherAPI
Object A is an object 
in NewsWeather 
Class
Object B is an object 
in WeatherAPI Class

### Slide 29

Principles of Object-Oriented Design
Encapsulation
Information 
hiding
Inheritance
Polymorphism
30

### Slide 30

31
Encapsulation
Information 
hiding

### Slide 31

Encapsulation
– grouping of data and functions into a component
– selective hiding of attributes and operations
Class Name
List of attributes
List of services
Object Name: Class Name
List of typed attributes
with possibly assigned values
List of methods with possibly 
specified parameters & return type 
32

### Slide 32

Information Hiding & Encapsulation
Apply the same concepts for everything
- Method
- Class
- Module/ Component 
- A whole application (e.g., API to google maps)
33

### Slide 33

How to Use Encapsulation & Information Hiding
System development is concentrated on what the services an 
object provides can do, not how it does it. Services
Internal 
states are 
regulated
Access to internal state can be regulated by the specification 
of an object's operations. Operations can be provided to 
create a new instance (a constructor), alter an object's state
(a mutator) or access the state (an accessor). 
No direct 
access
Encapsulation and information hiding of the state and 
internal behaviour of an object so that is not directly 
accessible to external service clients. 
34

### Slide 34

Member Visibility
private protected public
only accessible 
from other 
members of the 
same class
accessible by 
members of 
classes in the same 
package and by 
members of subclasses
globally accessible. The 
public members of a 
class provide its 
Application 
Programming Interface 
(API), which species 
how other objects can 
interact with instances 
of the class
35

### Slide 35

Member Visibility Modifier
36

### Slide 36

Member Visibility Modifier: PlantUML
37
A common tool used for creating the module content is PlantUML. 
These are PlantUML’s legends. Notice that they are similar to the 
standard notation.

### Slide 37

Student
name
matricNo
yearOfStudy
programme
validateMatricNo
registerForCourse
ict567:Student
-name:string[20] = “Ann Tan”
-matricNo:string[9]
-yearOfStudy:int = 2015
-Programme:string[50]
+validateMatricNo(matricNo):boolean
+registerForModule(moduleID)
Class Name
List of attributes
List of services
Object Name: Class Name
List of typed attributes
with possibly assigned values
List of methods with possibly 
specified parameters & return type 
38
Example

### Slide 38

Principles of Object-Oriented Design
Encapsulation
Information 
hiding
Inheritance
Polymorphism
39

### Slide 39

Inheritance
Polymorphism
40

### Slide 40

Inheritance
enables re-use of higher level 
class specifications among more 
detailed implementations. 
Polymorphism
enables multiple implementations 
to handle the same message from 
a client in different ways, in a 
manner which is transparent to 
the client.
41

### Slide 41

Case Study: Animal Class
42
Animal
- name: <String>
- weight: <Integer>
- colour: <ColourSet>
- eat()
- speak()

### Slide 42

Meow…
Woof…
Quack…
speak()
Animal Animal Animal
43

### Slide 43

Case Study: Animal Class
How can you deal with the variations?
44
Animal
- name: <String>
- weight: <Integer>
- colour: <ColourSet>
- Type: {dog, cat, duck}
- eat()
- speak()
- swim()
- listenMusic()
- setType()
Are these good ideas?

### Slide 44

Case Study: Animal Class
It works but a terrible design
45
Animal
- name: <String>
- weight: <Integer>
- colour: <ColourSet>
- Type: {dog, cat, duck}
- eat()
- speak()
- swim()
- listenMusic()
- setType()
- You have to check in listenMusic() and 
swim() for the type of animal before you 
can execute anything.
- You have added types of animals and 
you need to do set and get.
- The animal class will become really big 
and keep changing a lot. Many if 
conditions will be added.

### Slide 45

Case Study: Animal Class
It works but a terrible design
46
Animal
- name: <String>
- weight: <Integer>
- colour: <ColourSet>
- Type: {dog, cat, duck}
- eat()
- speak()
- swim()
- listenMusic()
- setType()
- Let’s look at other object-oriented 
design methods.
- How about Inheritance?

### Slide 46

Inheritance 
The sub-class inherits the properties and behaviours of the super class.
47

### Slide 47

Use INHERITANCE to Reuse Objects
- In inheritance, the sub- class inherits the properties and 
behaviours of the super class. 
- Sometimes it is very clear if you find the “is a” relationship 
among entities.
- Duck “ is a” Animal 
48

### Slide 48

What if the Animals behave differently only for some behaviours?
49
Meow…
Woof…
Quack…
speak()
Animal Animal Animal

### Slide 49

Polymorphism 
50
public void speak(){ 
 System.out.println(“speaking"); 
} 
public void speak(){ 
 System.out.println(“meow"); 
} 
public void speak(){ 
 System.out.println(“woof"); 
} 
public void speak(){ 
 System.out.println(“Quack"); 
}

### Slide 50

Coding 
Example of 
Inheritance & 
Polymorphism
51

### Slide 51

How about interactions among objects?

### Slide 52

Problem
- Buttons do not communicate directly 
with elevators
- We need an additional class: Elevator 
Controller
53

### Slide 53

54

### Slide 54

Normal Scenario: Elevator
55

### Slide 55

56
Sequence diagram
- Sequence diagram: an "interaction diagram" that models a 
single scenario executing in the system
- Visualize interactions over time
- Clarify system behavior
- Bridge between requirements and design
- Identify responsibilities and collaboration
- Facilitate communication

### Slide 56

57
Key parts of a Sequence Diagram
- Participant: an object or entity that acts 
in the sequence diagram
- sequence diagram starts with an 
unattached "found message" arrow
- Message: communication between 
participant objects
- The axes in a sequence diagram:
- horizontal: which object/participant is 
acting
- vertical: time (down -> forward in 
time)

### Slide 57

58
Sequence diagram from use case

### Slide 58

59
Representing objects
- Squares with object type, optionally preceded by object name 
and colon
- write object's name if it clarifies the diagram
- object's "life line" represented by dashed vert. line

### Slide 59

60
- Message (method call) indicated by horizontal arrow to other objects
- write message name and arguments above arrow
Messages between objects

### Slide 60

61
Messages (continued)
- Message (method call) indicated by horizontal arrow to other objects
- dashed arrow back indicates return
- different arrowheads for normal / concurrent (asynchronous) methods

### Slide 61

62
Lifetime of objects - creation: arrow with 'new' 
written above it - notice that an object 
created after the start of 
the scenario appears 
lower than the others
- deletion: an X at bottom of 
object's lifeline - Java doesn't explicitly 
delete objects; they fall 
out of scope and are 
garbage-collected

### Slide 62

63
Indicating method calls
- activation: thick box over object's life line; drawn when 
object's method is on the stack
- either that object is running its code, or it is on the stack 
waiting for another object's method to finish
- nest to indicate recursion
Activation
Nesting

### Slide 63

64
Indicating selection and loops
- frame: box around part of a sequence diagram to indicate selection or loop
- if -> (opt) [condition]
- if/else -> (alt) [condition], separated by horizontal dashed line
- loop -> (loop) [condition or items to loop over]

### Slide 64

65
Linking sequence diagrams
- if one sequence diagram is too large or refers to another diagram, indicate it with either:
- an unfinished arrow and comment
- a "ref" frame that names the other diagram
- when would this occur in our system?
Verify customer credit
Customer Info ref
Approved?

### Slide 65

66
Example sequence diagram
sd Example
loop
StoreFront Cart Inventory
AddItem
ReserveItem
PlaceItemInOrder
Checkout
ProcessOrder
ConfirmOrder

### Slide 66

67
Why not just code it?
- Sequence diagrams can be somewhat close to the code level. 
So why not just code up that algorithm rather than drawing it 
as a sequence diagram?
 A good sequence diagram is still a bit above the level of the real 
code (not all code is drawn on diagram)
 Sequence diagrams are language-agnostic (can be implemented 
in many different languages
 Non-coders can do sequence diagrams
 Easier to do sequence diagrams as a team
 Can see many objects/classes at a time on same page (visual 
bandwidth)

### Slide 67

Recap
- OOP
- Class diagrams
- Sequence diagrams

### Slide 68

Admin info
PLEASE double check your 
grouping info with created LMS
folders. 
1 2


---

## Week 5: Project Management

### Slide 1

INF2001
Introduction to Software Engineering
Week 5
A/Prof Frank Guan

### Slide 2

SIT INF2001 - AY24/25, Tri 1
Recap of last week
- Object-oriented analysis and design
- Class diagram
- Sequence diagram

### Slide 3

SIT INF2001 - AY24/25, Tri 1
Project management
- “The application of knowledge, skills, tools, and techniques to 
project activities to meet the project requirements.” 
-- PMBOK, 7th edition

### Slide 4

SIT INF2001 - AY24/25, Tri 1
Project management
- The process of 
- scoping, 
- planning, 
- staffing, 
- organising, 
- directing, and 
- controlling the development of an acceptable system at a minimum cost within 
a specified time frame.

### Slide 5

SIT INF2001 - AY24/25, Tri 1
Planning: Gantt Chart (sample)
5

### Slide 6

SIT INF2001 - AY24/25, Tri 1
Gantt Chart: Google Sheets Templates
6

### Slide 7

SIT INF2001 - AY24/25, Tri 1
Project management activities (task-related)
1. Negotiate scope
2. Identify tasks
3. Estimate task duration
4. Specify inter-task dependency (in term of time sequence)
5. Assign resources
6. Direct team effort
7. Monitor and control progress
8. Assess project results and experiences 
7

### Slide 8

SIT INF2001 - AY24/25, Tri 1
Work breakdown structure (WBS)
Breaking work down into smaller tasks is a widely adopted 
productivity strategy aimed at rendering tasks more feasible and less 
intimidating.
8

### Slide 9

SIT INF2001 - AY24/25, Tri 1
WORK BREAKDOWN STRUCTURE (WBS)
0
Goal of Project
1
Phase 1 … 
2
Phase 2 … 
3
Phase 3…
1.1
activity 1.1 … 
1.2
activity 1.2 … 
1.2.1
task 1.2.1 … 
1.2.2
task 1.2.2 … 
A task could be 
broken down to two 
or more subtasks, 
but no task should 
have more than six 
subtasks.
- The 100% coverage rule
- Mutually exclusive elements
- Elements are planned by 
outcomes, not actions
9

### Slide 10

SIT INF2001 - AY24/25, Tri 1 10
Appropriate level of detail: Continue to break the work down until a task list is developed which meets the following criteria:
- one (and only one) owner can be assigned to each of the lowest level tasks
- clearly defined outputs are evident for each task
- quality can be monitored through performance criteria associated with each output
- the tasks communicate the work to be accomplished to the person who is accountable
- the likelihood that a task is omitted or work flow forgotten is minimised
- each task is well enough defined and small enough so that estimates of duration are credible
- the project is broken down to the level at which you want to track
- as a general rule, the lowest level tasks should have durations between two and twenty days and effort that equates to not
more than 1 person week
No forgotten tasks: Project delays are often caused by forgotten tasks, rather than inaccurate estimates. Ensure you have
included tasks for:
- planning the project
- approval cycles
- key project meetings
- management/customer interfaces
- quality inspections/fixing defects
- training
- management
- test planning, development & execution
- project reviews and project closing
WBS Completion Checklist

### Slide 11

SIT INF2001 - AY24/25, Tri 1
EXAMPLE
https://www.projectconnections.com/knowhow/subsets/
sample-templates/Templ_TaskID_WBS_05_12_00.doc
11

### Slide 12

SIT INF2001 - AY24/25, Tri 1
Gantt Chart: Google Sheets Templates
12

### Slide 13

SIT INF2001 - AY24/25, Tri 1
Planning & estimating for software development
Before starting to build software, it is essential to plan the entire
project effort in detail (as much as possible)
Planning continues throughout the project lifecycle
- Initial planning is not enough
- The earliest possible time that detailed planning can take place is after 
the specifications are complete
13

### Slide 14

SIT INF2001 - AY24/25, Tri 1
The Cone of Uncertainty
14
Ideal Cost Estimation

### Slide 15

SIT INF2001 - AY24/25, Tri 1
Case Study: Planning & Estimating
Example
- Cost estimate of $1 million during the 
requirements workflow
- Likely actual cost is in the range ($0.25M, $4M)
- Cost estimate of $1 million at the end of the 
requirements workflow 
- Likely actual cost is in the range ($0.5M, $2M)
- Cost estimate of $1 million at the end of the 
analysis workflow (earliest appropriate time)
- Likely actual cost is in the range ($0.67M, $1.5M)
15

### Slide 16

SIT INF2001 - AY24/25, Tri 1
Planning & the Software Process
This model is old (1976)
- Estimating techniques have improved
- But the shape of the curve is likely to be similar
16
In people-months

### Slide 17

SIT INF2001 - AY24/25, Tri 1
Estimating duration and cost
- Accurate duration estimation is critical 
- Lose credibility, lose money or lose the contract
- Accurate cost estimation is critical
- Lose money or lose the contract
- However, there are too many variables for an accurate estimate 
of cost or duration 
17

### Slide 18

SIT INF2001 - AY24/25, Tri 1
Estimating and 
- Estimate → Plan → work 
- adjust your estimation →
adjust your plan → continue …
- Accumulate history data, repeat 
your existing success (and your 
estimates)
18

### Slide 19

SIT INF2001 - AY24/25, Tri 1
SOFTWARE ESTIMATION
-Estimation of Size
- Estimation of Effort
- Estimation of Cost 
(dependent on organisation)
19
Size 
estimation
Requirements
Functional and nonfunctional requirements, 
as described in RSD

### Slide 20

SIT INF2001 - AY24/25, Tri 1
Size estimation issues
The bigger the project, the harder to estimate
20

### Slide 21

SIT INF2001 - AY24/25, Tri 1
Size Estimation: How to Approach
1. Decompose the problem into smaller problems before 
estimating
2. What are the metrics for measuring size? 
21

### Slide 22

SIT INF2001 - AY24/25, Tri 1
Size Estimation
Basic software metrics are usually measured in
- Lines of Code (LOC)
- Function Points (FP)
- Use Case Points (UCP)
22

### Slide 23

SIT INF2001 - AY24/25, Tri 1
Using Lines Of Code (LOC) to Estimate
- Source code is only a small part of the total software effort
- Remember requirements, design, testing, deployment, etc.
- Different languages lead to different lengths of code
- It is not clear how to count lines of code
- - Executable lines of code? - Data definitions? 
- - Changed/deleted lines? - Comments? 
- Not everything written is delivered to the client
- A report, screen, or GUI generator can generate thousands of lines of 
code in minutes
- LOC is accurately known only when the product completed
23

### Slide 24

SIT INF2001 - AY24/25, Tri 1
Function points
Function points is a standard unit for 
measuring the size of an application system 
based on the functional view of the system.
24

### Slide 25

SIT INF2001 - AY24/25, Tri 1
- Requirements will be signed off between the developer and the client 
- Requirements are typically assumed to represent the complete set of user 
requirements. 
Function Points
(size estimation)
Requirement 
Specifications Non-functional 
Requirements
Functional 
Requirements
Complexity &
Difficulty
Standard
Function 
Points
From Requirements to Function Points
25

### Slide 26

SIT INF2001 - AY24/25, Tri 1
Steps
Step 1. Compute Unadjusted Function Points (UFP)
Step 2. Compute the Technical Complexity Factor (TCF)
Step 3. Calculate the number of Function Points (FP)

### Slide 27

SIT INF2001 - AY24/25, Tri 1
Determining the Number of Unadjusted Function 
Points (UFP)
- Based on the number of following types of components:
- inputs (Inp/EI input screens, dialog boxes, tables, form submissions…)
- outputs (Out/EO, output screens, model displays, reports, output files…) 
- inquiries (Inq/EQ, search request…)
- master files/logical files (Maf/ILF, user data or control information – database, files…)
- interfaces (Inf/EIF, remote databases, cloud-based apps…)
- For each type of components you need to identify the number of 
Simple / Average / Complex type of component
27

### Slide 28

SIT INF2001 - AY24/25, Tri 1
- Figure out the functions for each component. 
- For “Input item”, there are 3 functions. E.g.
- A user enters new items into the system (Simple Complexity)
- A user enters a sale transaction (Simple Complexity) 
- Another system sends over a new data (Simple Complexity) 
- For “Output item”, there are 2 functions with “Simple Complexity”
- …
- And so on…

### Slide 29

SIT INF2001 - AY24/25, Tri 1
Example (UFP Computations)
Information Metrics Count of 
Functions
Weighting factor
Simple Average Complex
External Inputs (EI) 3 X 3 4 6 = 9
External Outputs (EO) 2 X 4 5 7 = 8
External enQuiries (EQ) 2 X 3 4 6 = 6
Internal Logical Files 
(ILFs) 1 X 7 10 15 = 7
External Interface Files 
(EIFs) 4 X 5 7 10 = 20
Count Total (UFP) 50
We assume all functions receive simple processing
29
- The Unadjusted Function 
Points (UFP) is the sum of 
the weights that quantifies 
the size of information 
processing.
- How can we adjust the 
value?
- By considering the nonfunctional requirements

### Slide 30

SIT INF2001 - AY24/25, Tri 1
Technical Complexity Factor
Step 1. compute UFP (unadjusted function points)
Step 2. Compute the Technical Complexity Factor (TCF) 
- Assign a value from 0 (“not present”) to 5 (“strong 
influence throughout”) to each of 14 factors.
By considering the
non-functional requirements
30

### Slide 31

SIT INF2001 - AY24/25, Tri 1
Function Points Analysis
Step 1. compute UFP (unadjusted 
function points)
Step 2. Compute the Technical 
Complexity Factor (TCF) 
- Assign a value from 0 (“not present”) 
to 5 (“strong influence throughout”) 
to each of 14 factors.
0
0
4
3
2
0
2
0
5
1
5
2
0
3
31
Technical
Complexity Factors 0 1 2 3 4 5
Degree of Influence
27

### Slide 32

SIT INF2001 - AY24/25, Tri 1
Technical Complexity Factor
- Add the 14 factors to give the total Degree of Influence (DI)
𝑇𝑇𝑇𝑇𝑇𝑇 = 0.65 + 0.01 × 𝐷𝐷𝐷𝐷
- In our example: 𝑇𝑇𝑇𝑇𝑇𝑇 = 0.65 + 0.01 × 27 =
0.92
Technical Complexity Factor = Complexity Adjustment Value
0
0
4
3
2
0
2
0
5
1
5
2
0
3
32
Given to 
you
Calculated
27

### Slide 33

SIT INF2001 - AY24/25, Tri 1
What Is The Source Of 
The Values?
- General data from statistics
- Accumulate your own history data
- Adjust the values accordingly
33

### Slide 34

SIT INF2001 - AY24/25, Tri 1
Function Point Analysis
Step 1. compute UFP (unadjusted function points)
Step 2. Compute the Technical Complexity Factor (TCF) 
Step 3. The number of function points (FP) is then given by
𝐹𝐹 = 𝑈𝑈 × 𝑇𝑇𝑇𝑇𝑇𝑇
Unadjusted Function Points. 
Representing the functional 
requirements: 
What the software should do
Technical Complexity Factor. 
A number between 0.65 and 1.35. 
Adjusting the number of function points 
based on the relative complexities of the 
project. 
(Non-functional requirements) 34

### Slide 35

SIT INF2001 - AY24/25, Tri 1
Function Point Analysis
Step 1. compute UFP (unadjusted function points)
Step 2. Compute the Technical Complexity Factor (TCF) 
Step 3. The number of function points (FP) is then given by
𝐹𝐹 = 𝑈𝑈 × 𝑇𝑇𝑇𝑇𝑇𝑇
35
For our example:
- UFP = 50
- TCF = 0.92
- FP = 50 * 0.92 = 46

### Slide 36

SIT INF2001 - AY24/25, Tri 1
Use Case Points (UCP) is an alternative to estimate the project size 
besides the Lines of Code (LOC) and Function Points (FP) methods.
37
Use Case Points (UCP)

### Slide 37

SIT INF2001 - AY24/25, Tri 1
When to Apply Use Case Points (UCP)?
- We want to estimate early in the project based on Use Cases.
- For example:
❖ Consider your team project, do you have the necessary details to count Functional points (FP) at week 2?
❖ The likelihood is you don’t have the necessary details to count Functional points (FP).
- We will use Use Case Points 
38

### Slide 38

SIT INF2001 - AY24/25, Tri 1
Case Study
39
ID: UC-6
Name: Register for courses 
Description: Student accesses the system and views the courses currently available for him to register, selects the courses and registers for them. 
Primary Actor: Student 
Preconditions: Student is logged into system. Student fees are paid.
Main Success Scenario: 
1. Student chooses to register a new course.
2. System displays list of courses available for registration.
3. Student selects one or more courses to register for.
4. Student submits information.
5. System registers student for the selected courses, displays a confirmation message.
6. System sends a confirmation email. 
Alternative Scenarios: 
2a. No courses available for this student
2a1. System displays error message saying no courses are available and provides the reason. 
5a. Some courses could not be registered.
5a1. System displays error message showing the courses that were successfully registered, and provides the reason for those that were not
6a. Email was not sent 
6a1. System gives a message that the confirmation email was not sent, and offer retry option 
6a2. Student can choose to retry or quit screen 
Post conditions: Main: Student has one or more course registered. Email sent 6a. Email was not sent 
Priority: High

### Slide 39

SIT INF2001 - AY24/25, Tri 1
Calculating Use Case Points (UCP)
40
A Function of
The number and 
complexity of the 
Use Cases
The Development 
Environment 
(team motivation, 
language, etc.)
The number and 
complexity of the 
Actors
Non-functional ( + ) * Requirements
*

### Slide 40

SIT INF2001 - AY24/25, Tri 1
How to start
41
A Function of
The number and 
complexity of the 
Use Cases
The Development 
Environment 
(team motivation, 
language, etc.)
The number and 
complexity of the 
Actors
Non-functional
Requirements

### Slide 41

SIT INF2001 - AY24/25, Tri 1
Given a use case and assuming it has all its scenarios. 
42
ID: UC-6
Name: Register for courses 
Description: Student accesses the system and views the courses currently available for him 
to register, selects the courses and registers for them. 
Primary Actor:Student 
Preconditions: Student is logged into system. Student fees are paid.
Main Success Scenario: 
1. Student chooses to register a new course.
2. System displays list of courses available for registration.
3. Student selects one or more courses to register for.
4. Student submits information.
5. System registers student for the selected courses, displays a confirmation message.
6. System sends a confirmation email. 
Alternative Scenarios: 
2a. No courses available for this student
2a1. System displays error message saying no courses are available and provides the 
reason. 
5a. Some courses could not be registered.
5a1. System displays error message showing the courses that were successfully 
registered, and provides the reason for those that were not
6a. Email was not sent 
6a1. System gives a message that the confirmation email was not sent, and offer 
retry option 
6a2. Student can choose to retry or quit screen 
Post conditions: Main: Student has one or more course registered. Email sent 6a. Email was 
not sent 
Priority: High

### Slide 42

SIT INF2001 - AY24/25, Tri 1
Identify Transactions in a Use Case
- Transactions are not necessarily steps in a use case
- A transaction is a roundtrip from User to System to User
- For example: 
- For simplicity, if the user interaction is missing, you can count 
System to User as a transaction, for example:
43
(1) The user selects an X.
(2) The system shows the Ys connected with this X.
(3) The user also selects one or more Ys and submits.
(4) The system searches for hits and shows the results.
2a1. System displays error message saying no courses 
are available and provides the reason.
} Transaction 1
} Transaction 2
} One Transaction
User System
User System

### Slide 43

SIT INF2001 - AY24/25, Tri 1
Calculation Example
44
ID: UC-6
Name: Register for courses 
Description: Student accesses the system and views the courses currently available for 
him to register, selects the courses and registers for them. 
Primary Actor: Student 
Preconditions: Student is logged into system. Student fees are paid.
Main Success Scenario: 
1. Student chooses to register a new course.
2. System displays list of courses available for registration.
3. Student selects one or more courses to register for.
4. Student submits information.
5. System registers student for the selected courses, displays a confirmation 
message.
6. System sends a confirmation email. 
Alternative Scenarios: 
2a. No courses available for this student
2a1. System displays error message saying no courses are available and provides the 
reason. 
5a. Some courses could not be registered.
5a1. System displays error message showing the courses that were successfully 
registered, and provides the reason for those that were not
6a. Email was not sent 
6a1. System gives a message that the confirmation email was not sent, and offer 
retry option 
6a2. Student can choose to retry or quit screen 
Post conditions: Student has one or more course registered. Email sent 6a. Email was not 
sent 
Priority: High 
Count number of transactions, 
including alternative Scenarios. 
The total number of transactions 
is 7
Transaction 1
Transaction 2
Transaction 3
Transaction 4
Transaction 5
Transaction 7
Transaction 6

### Slide 44

SIT INF2001 - AY24/25, Tri 1
Determine the Complexity of the Use Case
Using the number of transactions, you can decide on the complexity of the 
use case.
We have 7 transactions for our Case Study, which means we fall under the 
average complexity classification. Thus, the weight for this use case is 10.
45
Use Case 
complexity 
Number of 
Transactions Weight 
Simple <=3 5 
Average 4 To 7 10 
Complex >7 15

### Slide 45

SIT INF2001 - AY24/25, Tri 1
Repeat the processes for all use cases
46
Use Case complexity and weight Number of use cases Product of Weight with number 
Simple (5) 2 5*2 = 10 
Average (10) 12 10*12= 120 
Complex (15) 20 15*20 = 300 
10 + 120 + 300 = 430 (Unadjusted Weight of Use cases)
Then add up the values for “Unadjusted Weight of Use Cases”

### Slide 46

SIT INF2001 - AY24/25, Tri 1
Consideration When Calculating Use Case Points (UCP)
47
A Function of
The number and 
complexity of the 
Use Cases
The Development 
Environment 
(team motivation, 
language, etc.)
The number and 
complexity of the 
Actors
Non-functional
Requirements

### Slide 47

SIT INF2001 - AY24/25, Tri 1
Identifying Actors
Actors can be
- Users interacting through Graphical User interface 
- Users interacting through a command line (text 
based) 
- Components interacting through well define API 
- Components or systems interacting through 
protocols (HTTP, SOAP, TCP/IP, etc) 
Actor 
Classification Type of Actor Weight 
Simple Components interacting 
through well defined API 1 
Average 
External system that must 
interact with the system 
using standard 
communication protocols 
(e.g. SOAP, TCP/IP, FTP, 
HTTP, database) 
2 
Complex 
Human actor using a GUI 
application interface or 
text-based interface 
3

### Slide 48

SIT INF2001 - AY24/25, Tri 1
Calculating All Actors in Our Case Study
Actor Type Number of Actors Product 
Simple (1) 2 1*2 = 2 
Average (2) 4 2*4= 8 
Complex (3) 8 3*8 = 24 
Total 34
49
Unadjusted Weight of actors = 
2 + 8 + 24 = 34
Total Unadjusted Points (UUCW) = Unadjusted Transactions Weight + Unadjusted Actors Weight
= 430 + 34
= 464

### Slide 49

SIT INF2001 - AY24/25, Tri 1
Consideration When Calculating Use Case Points (UCP)
50
A Function of
The number and 
complexity of the 
Use Cases
The Development 
Environment 
(team motivation, 
language, etc.)
The number and 
complexity of the 
Actors
Non-functional
Requirements

### Slide 50

SIT INF2001 - AY24/25, Tri 1
Determining the Technical Complexity Factors
These are the factors that could 
influence the development of the 
software. 
The weight here represents the impact 
of such factor. This is given to you.
Developers should assess the 
importance of each factor on their 
project. 
Factor Description Weight 
T1 Distributed system 2.0 
T2 Response time/performance objectives 1.0 
T3 End-user efficiency 1.0 
T4 Internal processing complexity 1.0 
T5 Code reusability 1.0 
T6 Easy to install 0.5 
T7 Easy to use 0.5 
T8 Portability to other platforms 2.0 
T9 System maintenance 1.0 
T10 Concurrent/parallel processing 1.0 
T11 Security features 1.0 
T12 Access for third parties 1.0 
T13 End user training 1.0

### Slide 51

SIT INF2001 - AY24/25, Tri 1
Calculating the Technical Complexity Factors
52
Factor Description Weight 
T1 Distributed system 2.0 
T2 Response time/performance objectives 1.0 
T3 End-user efficiency 1.0 
T4 Internal processing complexity 1.0 
T5 Code reusability 1.0 
T6 Easy to install 0.5 
T7 Easy to use 0.5 
T8 Portability to other platforms 2.0 
T9 System maintenance 1.0 
T10 Concurrent/parallel processing 1.0 
T11 Security features 1.0 
T12 Access for third parties 1.0 
T13 End user training 1.0 
0 1 2 3 4 5
Degree of Influence Given to you
Weight * Degree of Influence
Product
3
3 
5 
2 
0 
1 
5 
4 
3 
4 
3 
5 
0 
6.0 
3.0 
5.0 
2.0 
0.0 
0.5 
2.5 
8.0 
3.0 
4.0 
3.0 
5.0 
0.0 
Total = 42
https://en.wikipedia.org/wiki/Use_Case_Points 
Assessment by Developers

### Slide 52

SIT INF2001 - AY24/25, Tri 1
Technical Complexity Factor (TCF) Including the Complexity Adjustment
- Add the 13 factors to give total Degree of Influence (DI)
𝑇𝑇𝑇𝑇𝑇𝑇 = 0.6 + 0.01 × 𝐷𝐷𝐷𝐷
- In our example: 𝑇𝑇𝑇𝑇𝑇𝑇 = 0.6 + 0.01 × 42 = 1.02
53
Given to 
you
Calculated

### Slide 53

SIT INF2001 - AY24/25, Tri 1
Consideration When Calculating Use Case Points (UCP)
54
A Function of
The number and 
complexity of the 
Use Cases
The Development 
Environment 
(team motivation, 
language, etc.)
The number and 
complexity of the 
Actors
Non-functional
Requirements

### Slide 54

SIT INF2001 - AY24/25, Tri 1
Environmental Factors
- There are several factors in the 
development environment that 
could affect the size of a project. 
- For example: the motivation level of 
the team, their experience with the 
application, and other factors affect 
the calculation of use case points. 
- Karner considers 8 environment 
factors 
55
Factors Contributing to Efficiency 
Familiar with Development Process 1.5 
Part time workers -1 
Analyst capability 0.5 
Application experience 0.5 
Object oriented experience 1 
Motivation 1 
Difficult programming language -1 
Stable requirements 2

### Slide 55

SIT INF2001 - AY24/25, Tri 1
Calculating Environment Factors
- There are several factors in the 
development environment that 
could affect the size of a project. 
- The factors are rated on a scale 0, 
1, 2, 3, 4 and 5: 0 means that it is 
irrelevant and 5 means it is 
essential. 
56
0 1 2 3 4 5
Degree of Influence
Environmental Factors Weight Assessment 
Familiar with Development Process 1.5 
Part time workers -1 
Analyst capability 0.5 
Application experience 0.5 
Object oriented experience 1 
Motivation 1 
Difficult programming language -1 
Stable requirements 2

### Slide 56

SIT INF2001 - AY24/25, Tri 1
Environmental Factor Including the Complexity Adjustment
- Add the 8 factors to give Degree of Influence (DI)
𝐸𝐸 = 1.4 + (−0.03 × 𝐸𝐸 𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸)
57
Calculated
Given to 
you

### Slide 57

SIT INF2001 - AY24/25, Tri 1
Calculating Use Case Points (UCP)
58
A Function of
The number and 
complexity of the 
Use Cases
The Development 
Environment 
(team motivation, 
language, etc.)
The number and 
complexity of the 
Actors
Non-functional
Requirements
( + ) * *
UCP = UUCW * TCF * EF

### Slide 58

SIT INF2001 - AY24/25, Tri 1
Software Estimation
- Estimation of Size
-Estimation of Effort
- Estimation of Cost 
(dependent on organisation)
59

### Slide 59

SIT INF2001 - AY24/25, Tri 1
Effort Estimation
- Effort estimation, an important term used in software 
engineering and has a great value in the industry. 
- As in software industries, Cost of the project and Time to 
complete the project is predicted by estimating efforts. 
- There are many traditional methods for estimating efforts. 
60

### Slide 60

SIT INF2001 - AY24/25, Tri 1
Typical Formulas 
E = 5.2 x (KLOC)^0.91 Walston-Felix Model
E = 5.5 + 0.73 x (KLOC)^1.16 Bailey-Basili Model
E = 3.2 x (KLOC)^1.05 COCOMO Basic Model
E = 5.288 x (KLOC)^1.047 Doty Model for KLOC > 9
E = -12.39 + 0.0545 FP Albrecht and Gaffney Model
E = 60.62 x 7.728 x 10^- 8 FP^3 Kemerer Model
E = 585.7 + 15.12 FP Matson, Barnett, and Mellichamp Model
61
We will use this!

### Slide 61

SIT INF2001 - AY24/25, Tri 1
Constructive Cost Model: COCOMO
- COCOMO is the traditional cost estimation model in which size is the 
major input parameter (1981, Barry Boehm). 
- Uses empirically derived formulas to predict effort. 
- Input: e.g., use case points (UCP)
- Output: the effort in months/hours of work for one person. 
- COCOMO has three models: Basic, intermediate and Advanced 
62

### Slide 62

SIT INF2001 - AY24/25, Tri 1
BASIC COCOMO
First classifies the software project:
- Organic software consists of 
- small and simple projects 
- Done in small teams that have good experience in the subject. 
- The project requirements are not so rigid (i.e., graphing software developed for CAD group). 
- Semi-detached software is 
- mid-sized software 
- Developed by less experienced developers 
- According to more rigid requirements (i.e., transaction software for specific hardware and database 
software). 
- Embedded software has very tight requirements and must be made within hardware, software and 
operational constraints (i.e., computer-controlled fire alarm system).
63

### Slide 63

SIT INF2001 - AY24/25, Tri 1
Effort Estimation using Use Case Points 
- The creator of UCP has given the following range of estimation of hours 
for each UCP: 15 to 30 hours. 
- The estimated effort in developer-hours of a project of size 450 UCP falls 
between 
(15 ~ 30) * 450 (in hours) 
64

### Slide 64

SIT INF2001 - AY24/25, Tri 1
Estimate Task Duration
Estimate each task 
(size)
Estimate the effort 
(time)
Monitor the progress 
(compare with the 
estimation)
Adjust your 
estimation
65

### Slide 65

SIT INF2001 - AY24/25, Tri 1
Estimate Task Duration
A simple estimation model
1. Estimate the minimum amount of time it would take to perform the task
- the optimistic duration (OD). 
2. Estimate the maximum amount of time it would take to perform the task
- the pessimistic duration (PD). 
3. Estimate the expected duration (ED) that will be needed to perform the task. 
4. Calculate a weighted average of the most likely duration (D) as follows:
𝐷𝐷 =
1 × 𝑶𝑶𝑶𝑶 + 4 × 𝑬𝑬 + (1 × 𝑷𝑷 )
6
66

### Slide 66

SIT INF2001 - AY24/25, Tri 1
What We Have Learned
- Project planning
- Task scheduling
- Task management 
67

### Slide 67

SIT INF2001 - AY24/25, Tri 1
About Week 5 Labtorial
- Exercises on Project Planning
- No assignment but presentations are needed

### Slide 68

SIT INF2001 - AY24/25, Tri 1
About Quiz (1/2)
- Online “LMS->INF2001->Assessments->Quizzes”
- Date: 6 Oct 2025
- Start from 9:00am and latest start time is 9:15am
- Duration: 1 hour
- MCQ + short answer questions
- Close-book quiz
- Requires
- RespondusLockDown Browser
- Web camera
- Blank papers + pen/pencil
- Calculator is allowed

### Slide 69

SIT INF2001 - AY24/25, Tri 1
About Quiz (2/2)
- Make sure a conducive environment with stable network connection
- On-campus room booked for you in case of need (Punggol Campus: 
E2-03-02-SR220)
- Students with special needs for extra time, please email to me by 30 
Sep 2025. 
- In case of absence due to valid reasons, a make-up in-person quiz 
with higher difficulty will be conducted. Otherwise, “0” mark for 
absence without valid reasons.
- “0” mark for those who miss both online quiz and in-person makeup quiz.

### Slide 70

SIT INF2001 - AY24/25, Tri 1
About Group Project
- More info about presentation arrangements will be shared later 
on LMS
- More info about PEER Evaluation will be shared later
- Please double check your team members again
- Please work together with your team


---

## Week 8 (Part 1): Introduction to Software Engineering Design

### Slide 1

INTRODUCTION TO 
SOFTWARE ENGINEERING DESIGN
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?

### Slide 2

OUTLINE
-Intro software engineering design
-Software Design activities
-Software Design Fundamentals - Design Principles

### Slide 3

Software Engineering Design
Formally, software engineering design is defined as
The process of identifying, evaluating, validating, and 
specifying the architectural, detailed, and construction
models required to build software that meets its intended 
functional and nonfunctional requirements; and 
The result/product of such process.

### Slide 4

Importance of Software Design
From 
product
development 
perspective Design forms the 
foundation for all 
other development 
activities: Construction, 
Testing, Maintenance
Requirements are mapped to 
conceptual models of 
software. Provide models 
that represent structure and 
behavior
Main 
components 
and interfaces 
are identified
Quality of future system is 
born. Provide means to 
evaluate quality attributes, 
e.g., usability.
Solutions can be 
reused in other 
projects

### Slide 5

Importance of Software Design
From 
Project 
management 
perspective
Good software design help 
minimize effects of 
requirements’ volatility. 
This can minimize impact on schedule 
and cost.
Shields the project from having 
“one guy” owning the whole 
system. Multiple personnel 
owns multiple components. If one 
leaves the company, it is easier 
to replace…
Increases efficiency in human 
resource allocation. 
Designs decompose systems so 
that teams can work on different 
parts of the problem in parallel. 
By decomposing system, teams can 
work in distributed fashion. 
Design helps improve 
project management.
Planning, organization, 
staffing, and tracking

### Slide 6

Software Design Challenges
Requirements volatility
Inconsistent development processes
Fast, and ever-changing technology
Ethical and professional practices
Managing design influences

### Slide 7

Software Design Process
A software design process is a set of activities and 
controls that specify how resources work together 
for the production of software design artefacts. 
7

### Slide 8

OUTLINE
-Definition – software engineering design
-Software Design activities
-Software Design Fundamentals - Design Principles

### Slide 9

Design Activities in Software Engineering Process
Otero, 2012

### Slide 10

Design Activities in Software Engineering Process
Otero, 2012

### Slide 11

Design Activities in Software Engineering Process
Software Architecture
- Macrodesign approach for creating models that depict the quality and function of the software system
- Provides black-box models used to evaluate system’s projected capabilities and lays the foundation 
 for all subsequent work in the software engineering life cycle.
- Focus on non-functional requirements
Detailed Design
- Builds on software architecture to provide white-box design elements of the structure and behavior 
 of the software system
- Activity that deals with refining software architecture to reach a point where the software design, 
 including architecture and detailed design, is deemed sufficiently complete for construction to begin.
- Focus on addressing functional requirements with 2 major tasks : interface and component design.
Construction Design
Required to support system’s quality attributes, such as performance, maintainability, and testability.
Human-Computer Interface
General principles are applied to optimize the interface between humans and computers
Software Design Documentation
include the necessary information that properly captures the design of the system.
Software Design Management
Set of activities required to efficiently create and implement quality design artifacts, within schedule and budget constraints.

### Slide 12

Software 
Architecture
Lays the foundation for 
all subsequent work in 
the software 
engineering lifecycle
FOUNDATION
They serve as important 
communication, 
reasoning, and analysis 
tool that
supports the 
development and 
growth of the system 
COMMUNICATION
It provides the major 
structural components 
and interfaces of the 
system.
STRUCTURAL
It focuses on the quality 
aspects of the system 
before detailed design 
or
construction can begin.
QUALITY
12

### Slide 13

Refines the architecture to 
reach a point where the 
software design, including 
architecture and detailed 
design, is deemed sufficiently 
complete for the construction 
phase to begin.
FOLLOWS ARCHITECTURE
Focuses on functional 
requirements, whereas 
the architecture focuses 
mostly on non-functional, 
or quality, requirements
FUNCTIONAL
detailed design focuses 
mostly on the internals 
of those components and 
interfaces.
INTERNAL DESIGN
Builds on the software 
architecture to provide 
a white-box approach 
to design the structure 
and behavior of the 
system.
WHITE-BOX
Detailed Design
13

### Slide 14

Software Design Process
ARCHITECTURE 
DESIGN
DETAILED 
DESIGN
CONSTRUCTION 
DESIGN
It is seen that architectural designs are elaborated through detailed design, which are further 
elaborated through construction design. In practice, design activities are not carried out in such orderly 
and controlled fashion. Quite a bit of iteration occurs between these activities.
14

### Slide 15

OUTLINE
-Definition – software engineering design
-Software Design activities
-Software Design Fundamentals - Design Principles

### Slide 16

Software Design Fundamentals - Design Principles
- Modularization
- Abstraction
- Encapsulation
- Coupling and cohesion
- Separation of interface and implementation
- Sufficiency 
- Completeness

### Slide 17

Modularization
- Modularization is the process of continuous decomposition of the software system 
until fine-grained components are created. 
- It turns out that two other principles can effectively guide designers during this 
process
- Abstraction
- Encapsulation

### Slide 18

Coupling and Cohesion
- Cohesion is defined as the degree to which all elements of a module, class, or 
component work together as a functional unit. High cohesion is good, and low 
cohesion is bad.
- Coupling is defined as the degree of interdependence between two or more 
classes, modules, or components. Tight coupling is bad, and loose coupling is good.
Loose coupling
High Cohesion

### Slide 19

Separation of interface and implementation
This principle involves defining a
component by specifying a public
interface (known to the client of
the component) that is separate
from the details of how the
component is realized.
Interface
Implementation
Visible
Hidden

### Slide 20

Completeness and sufficiency
- Completeness measures how well designed units provide the required 
services to achieve the intent (no less).
- Sufficiency measures how well the designed units are at providing 
only the services that are sufficient for achieving the intent (no more).

### Slide 21

SUMMARY
-Definition – software engineering design
-Design activities
-Software Design Fundamentals - Design 
Principles
…. Next lecture, we will dive deeper into 
Software Architecture And Detailed Design


---

## Week 8 (Part 2): Component Diagram

### Slide 1

SOFTWARE ANALYSIS AND DESIGN
- COMPONENT DIAGRAM
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?

### Slide 2

Requirement 
Specification
Analysis and Design
Deployment
Maintenance
Testing
Implementation
W1 Introduction to SDLC
W2 Requirements Engineering
W3 Use Case Diagram
W3 Activity Diagram
W4 OOP, Class Diagram, Sequence Diagram
W5 Project Management
W8 Component Diagram
W9 Software Architecture and Detailed Design
W10 Blackbox , Whitebox testing, UAT
W11 Software Configuration Management
W11 Software Maintenance and Refactoring
Software Development Activities

### Slide 3

SIT Internal
McConnell, S., & Mcconnell, S. (2004). Code Complete. In Code Complete. Microsoft Press.
Levels of Software Design 
What we have done so far

### Slide 4

SIT Internal
UML Modeling
Taken from https://www.visual-paradigm.com/

### Slide 5

SIT Internal
Taken from https://www.visual-paradigm.com/
UML Modeling
Requirements
Use Case 
Diagram
Class 
Diagram
Sequence 
Diagram
Component 
Diagram
All diagrams are used to model the SAME requirements, but tell 
different (complementary) story

### Slide 6

SIT Internal
What are Software Components?
- Components are independent unit within a system that 
encapsulates a collection of data and functions that are 
semantically related.
- Components are higher-level abstractions than objects
and encapsulate (hides) their internal structure.
- A component collaborate with other components through 
well-defined interfaces.
- It can be a collection of classes (packages), a Web 
service, a resource (hardware or software)
- We design components to be modular, portable, 
replaceable, and reusable.
- Make discussions easier at a higher level. Especially with 
the clients.

### Slide 7

SIT Internal
McConnell, S., & Mcconnell, S. (2004). Code Complete. In Code Complete. Microsoft Press.
Levels of Software Design 
1. What we have done so far
2. We can further encapsulate our 
classes into components!

### Slide 8

SIT Internal
Component Diagram Notation
In the diagram, a component is represented by a 
box with a ‘plug' widget stereotype. 
Each component has a label (in this case, A and B)

### Slide 9

SIT Internal
Component Providing Interface Notation
component A is providing an interface I, which is 
shown as a facet (but looks like a lollipop) 
stereotype attached to the component. 
Providing interfaces
A is providing an 
interface for other 
components to 
collaborate with it. 
A can define exactly 
how it accepts 
collaboration

### Slide 10

SIT Internal
Component Requiring Interface Notation
component B requires interface I, denoted 
by a connector, called a receptacle drawn 
around the facet.

### Slide 11

SIT Internal
Nested Components
Part of component A's functionality is 
provided by sub-component B.

### Slide 12

SIT Internal
Ports and Delegates
Component A can delegate responsibility for interface I to subcomponent C. This relationship can be shown by drawing a 
<<delegate>> dependency from sub-component C to a shaded 
box on component A's boundary that provides the interface. 
This shaded box is called a port.
<<delegate>> <<delegate>>
To keep consistent with UML 2.5.1 publication, we will use solid line and no arrow head for <<delegate>> (UML2.5.1 pg.214)

### Slide 13

SIT Internal
<<delegate>> <<delegate>>
Sub-component D delegates the 
required interfaces on component B's 
port. The delegation is drawn from subcomponent D's required interface to the
port on component B.
Ports and Delegates

### Slide 14

SIT Internal
Ports and Delegates
- Components use the ports and delegates concept to model how 
components interact with other (external) components and how the 
responsibility for realizing external requests are delegates throughout 
parts of the components.
Ports are used to model 
access points for allowing 
external environment access 
to component services 15
Delegation are used to model the link 
between external provided interfaces to the 
realization of those interfaces internally

### Slide 15

SIT Internal
Component Diagram at a Glance
A component diagram breaks down the actual system under development into various 
high levels of functionality. Each component is responsible for one clear aim within the 
entire system and only interacts with other essential elements on a need-to-know basis.
https://www.omg.org/spec/UML/2.5.1/PDF page 214
Required interface
Provided interface
Port

### Slide 16

SIT Internal
Exercise 1
- Consider a client collection system that is 
decomposed into three subsystems ClientManager, 
SensorManager and VideoManager. 
- The client collection system requires a collection 
schedule interface ISchedule , which provides the 
information for activating sensor and video nodes to 
begin collection. The interface ISchedule is actually 
required by ClientManager. 
- The client collection system provides a client data 
interface IClientData, which provides the collected 
data to the external system. The interface 
IClientData is actually provided by ClientManager.
- ClientManager controls SensorManager and 
VideoManager through ISensorControl and 
IVideoControl (interfaces) respectively.

### Slide 17

SIT Internal
For your project - Go back to your class diagram and think 
of how you can encapsulate your classes 
into components
- You most probably will need to update 
your class diagram to include (new) 
interface classes that are now modelled in 
your component diagram
- What about database?
Your class diagram does not have 
database inside, though you may have 
classes that interact with the external 
database
- So how do you include database in your 
design?
You usually include database in 
Architecture Diagram

### Slide 18

SIT Internal
- Components are higher level abstractions that objects and encapsulates/hides internal
structure – do not provide too much details
- Given a component, any lollipop or socket should have a ‘matching/paired’ socket or
lollipop. There should not be any ‘dangling’ lollipop or socket that does not have a
corresponding connection (unless it’s to external component)
- Do not share lines in the notation
- Use Port when you want to represent a specific point of interaction provided by an 
encapsulated component.
- Double check your modeling especially when a component only has required but no 
provide or vice versa. At times it may be the wrong interface, or something is missing
- User interface/dashboard do not need to be a separate component
- A component can have both a required interface and provided interface
- A ball can be shared by more than one component
Common Mistakes

### Slide 19

SIT Internal
McConnell, S., & Mcconnell, S. (2004). Code Complete. In Code Complete. Microsoft Press.
SUMMARY
1. What we have done so far
2. We can further encapsulate our 
classes into components!

### Slide 20

SIT Internal
<<component>>
<<component>>
ClientCollectionSystem
<<component>>
Port1 Port2
ClientManager
<<component>>
IClientData IClientData ISchedule ISchedule
ISensorControl
SensorManager
<<component>>
IVideoControl
VideoManager
<<component>>
<<delegate>> <<delegate>>
Components are independent unit within a system that 
encapsulates a collection of data and functions that 
are semantically related.
Abstraction Principle:
Focuses on essential characteristics of 
entities—in their active context—while 
deferring unnecessary details
Therefore, we really can’t say at this point what the 
SensorManager will be! It could end up being one class, a 
bunch of classes, one function, etc. 
The same applies to all other 
components!
Sensor functions Video capture functions
Requires collection schedule Provides collection 
and health data
Everything that you see in the component diagram
is an abstraction!
Although a good start, too many details are 
still missing to be able to build this system!
SUMMARY

### Slide 21

SIT Internal
SUMMARY
- Components are higher-level 
abstractions than objects and 
encapsulate (hides) their internal 
structure.
- A component collaborate with 
other components through welldefined interfaces.


---

## Week 9 (Part 1): Software Architecture & Architectural Patterns

### Slide 1

INTRODUCTION TO SOFTWARE ARCHITECTURE
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?

### Slide 2

Recap – W8 Component Diagram and Intro to Software Design

### Slide 3

Recap - Ports and Delegates
Component A can delegate responsibility for interface I to subcomponent C. This relationship can be shown by drawing a 
<<delegate>> dependency from sub-component C to a shaded 
box on component A's boundary that provides the interface. 
This shaded box is called a port.
<<delegate>> <<delegate>>
To keep consistent with UML 2.5.1 publication, we will use solid line and no arrow head for <<delegate>>
I

### Slide 4

4
Components are independent unit within a system that 
encapsulates a collection of data and functions that 
are semantically related.
Abstraction Principle:
Focuses on essential characteristics of 
entities—in their active context—while 
deferring unnecessary details
Therefore, we really can’t say at this point what the 
SensorManager will be! It could end up being one class, a 
bunch of classes, one function, etc. 
The same applies to all other 
components!
Sensor functions Video capture functions
Requires collection schedule Provides collection 
and health data
Everything that you see in the component diagram
is an abstraction!
Although a good start, too many details are 
still missing to be able to build this system!
Recap – Component

### Slide 5

Recap - Diagrams
Requirements
Use Case 
Diagram
Class 
Diagram
Sequence 
Diagram
Component 
Diagram
All diagrams are used to model the SAME requirements, but tell 
different (complementary) story

### Slide 6

SO FAR THIS WEEK (W9)
Introduction to Software Architecture
Introduction to Software Architecture - Video

### Slide 7

OVERALL AGENDA
-Intro to Software Architecture - – pre-recorded videos
-Overview of Architecture
- C4 model
- 4+1 model
-Architectural Patterns
-Layered
-Client Server
-Model-View-Controller

### Slide 8

Overview of Software Architecture
- So far, you have seen a 
logical solution to the Blog Post 
problem:
- Requirements/SRS
- Analysis
- Class diagrams, sequence / 
communication diagrams
- Component Diagram
- But, something is still not very 
clear…
- Platforms (Web, Mobile?)
- Hardware (How many 
databases?, how many web 
servers?...)

### Slide 9

- For the blog post app, one possible 
organization:
- A mobile native app
- App application logic is on the device
- A local database is used
Overview of Software 
Architecture

### Slide 10

- For the blog post app, another 
possible organization:
- A mobile native app
- App application logic is on the device
- The database is hosted on a server
Overview of Software 
Architecture

### Slide 11

- For the blog post app, yet 
another possible organization:
- A very “thin” mobile native app 
with UI only
- All logic is deployed on a server 
and exposed as services to the 
UI class (Web Services)
- The database is on the same 
server as well
Overview of Software 
Architecture

### Slide 12

Overview of Software Architecture
- Stakeholders’ concerns serve as driving force behind 
architectural decisions. 
- The bottom line when deciding the architecture:
- Our FUNCTIONAL and NON-FUNCTIONAL requirements dictate 
what we do
- Manage trade-offs
- E.g. Weight vs Speed – The heavier a car is the slower it accelerates!
- We adhere to Software Quality Requirements

### Slide 13

Software Quality Requirements
Quality Description
Usability Degree of complexity when learning / using system
Maintainability Degree of complexity in fixing any issues or in making changes to the
system without affecting the current working components
Security Ability to protect or defend its information / system
Performance Capacity to accomplish useful work under resource constraints
Reliability Systems failure rate (includes all existing subsystems)
Portability
Portability Degree of complexity when adapting the system to other software or
hardware environments
Testability Degree of complexity when verifying and validating the systems functions
Availability Systems uptime: The degree to which a system or component is operational
and accessible when required for use
Interoperability Systems ability to collaborate with other software or hardware systems

### Slide 14

My Blog Post
Architecture Decision Example (Blog Application)
Mobile Web Native App
Works on any mobile browser Need an app for each platform
Needs to be Online Can be Offline
Slower, lagging interface Faster, smooth interface
Small size Could take up space
Easier to update web app Pushing updates to all versions
Cheaper More expensive to develop and maintain
Little client hardware used Use hardware capabilities of device (like sensors)

### Slide 15

OVERALL AGENDA
-Intro to Software Architecture - – pre-recorded videos & iRAT
-Overview of Architecture
- C4 model
- 4+1 model
-Architectural Patterns
-Layered
-Client Server
-Model-View-Controller

### Slide 16

C4 Model - Context, Container, Component, Code
- Where to start? Abstraction!
- C4 model is a simple starting point
- Simplified version of UML and 4+1 Model 
(talk about soon)
- Architectural documentation standard for 
software systems that breaks a software 
system down into 4 levels
- Makes it easier for software developers to 
describe and understand how a software 
system works
- Minimize the gap between software 
architecture model / description and source 
code
- System context and container diagrams are 
usually sufficient for most software 
development teams.
http://C4model.com
https://www.youtube.com/watch?v=x2-rSnhpw0g&t=5s

### Slide 17

C4 Model - Context, Container, Component, 
Code
Level 1: System Context Diagram Level 2: Container Diagram

### Slide 18

C4 Model - Context, Container, Component, 
Code
Level 3: Component Diagram Level 4: Code

### Slide 19

C4 Model - Context, Container, Component, 
Code
- Wait, Component Diagram and Class diagrams are part of Software 
Architecture? ...... Of course, from what you’ve done it also includes:
- Class Diagram
- Sequence Diagram
- Component Diagram 
- There are different levels and views to the architecture to suit all 
stakeholders
- A good architecture diagram clearly communicates what it needs to, to 
who it needs to communicate it to!

### Slide 21

4+1 View of Architecture
- A model for documentation
software architecture
- The decisions made can be 
organized around four views:
- Logical, development, physical, process
- Then, it can be illustrated by a few 
selected use cases, or scenarios (fifth 
view).
- Communicate architecture to 
different stakeholders
Logical 
View
Development 
View
Process
View
Physical
View
User View
(Scenarios)

### Slide 22

4+1 View of Architecture
Wikipedia : 4+1 Architectural View Model
Logical view functionality that the system provides to end-users. 
(class diagrams, state diagrams, component diagram)
Process view dynamic aspects of the system, system processes and how they communicate, focuses 
on the run time behaviour of the system. 
(sequence diagram, communication diagram, activity diagram.)
Development/Implementation 
view
system from a programmer's perspective, concerned with software management. 
(Package diagram, source code)
Physical/Deployment view system from a system engineer’s perspective, concerned with the topology of software 
components on the physical layer as well as the physical connections between these 
components. 
(Deployment diagram)
Use Case / Scenarios View describe sequences of interactions between objects and between processes. They are 
used to identify architectural elements and to illustrate and validate the architecture 
design. They also serve as a starting point for tests of an architecture prototype.

### Slide 23

24
Logical View Development View
Process View Physical View
User View
4+1 - Put it all together

### Slide 24

Key Tasks in Architectural Design
- Key tasks that need to be performed during software architecture. 
- Identifying stakeholders concern
- Identifying appropriate architectural views
- Identifying architectural styles and patterns
- Identifying influences of architectural decisions in organizations
- Identifying the system’s major components and interfaces
- Evaluating and validating the architecture
- Establishing policies for ensuring architectural design synchronicity
25

### Slide 25

OVERALL AGENDA
-Intro to Software Architecture - – pre-recorded videos & iRAT
-Overview of Architecture
- C4 model
- 4+1 model
-Architectural Patterns
-Layered
-Client Server
-Model-View-Controller

### Slide 26

What are Patterns?
- Formal Definition
- A solution to a recurring problem in a context
- In software, we see similar problems over and over
- Access to, and CRUD operations with a DB, creating Objects, observing and Reacting to events, 
etc.
Architectural styles and architectural patterns 
provide generic, reusable solutions that can be easily 
understood.
- So, using existing ideas and SOLUTIONS, 
regardless of the technical specifics of the 
individual problem

### Slide 27

Architectural Pattern Classification
A list of common types of systems appropriate for classifying architectural patterns
ICT2101/ICT2201 Introduction to Software Engineering 28
Type Description Examples
DatacenteredSystems that serve as a centralized repository for data, while allowing clients to 
access and perform work on the data
IDE, Student Information 
Management System
Data flow Systems oriented around the transport and transformation of a stream of data Sensor Data Processing 
System
Distributed Systems that primarily involve interaction between several independent 
processing units connected via a network
Email System
Interactive Systems that serve users or user-centric systems E-shopping Website
Hierarchical Systems where components can be structured as a hierarchy (vertically and 
horizontally) to reflect different levels of abstraction and responsibility
Android Operation
System

### Slide 28

Suitable Architecture Patterns 
29
Type Patterns
Data-centered Blackboard Pattern
Data flow Pipe and Filter Pattern
Distributed Client–Server Pattern
Peer-to-peer Pattern
Broker Pattern
Interactive Model–View–Controller Pattern
Hierarchical Main Program and Subroutine
Layered Pattern
More details will be covered in Software Design module
The system is too complicated to be 
represented by a single pattern? 
Consider combination. 
Refer to chapter 4, Software Engineering Design: Theory and Practice. Carlos E. Otero

### Slide 29

Hierarchical -
Layered Software Architecture
- Most common architecture pattern is the layered architecture pattern
- Components or classes are organized into horizontal layers
- Each layer performing a specific role within the application
- The most popular layers are
- Presentation Layer
- Application / Business Layer
- Data Layer

### Slide 30

Hierarchical -
Layered Software Architecture
- Presentation Layer
- The logic in the presentation layer should focus on user 
interface concerns. A presentation layer devoid of 
business logic will be easier to test.
- Business / Application Layer
- Holds implementation for the business logic of the 
application, including such things as business riles, 
validations, and calculation logic. Business entities for 
the application’s domain are placed in this layer
- Data
- The data layer provides functionality to access and 
managed data. The data layer contains a data store for 
persistent storage, such as RDBMS. It provides services 
and data for the business layer
Presentation
Business
Data

### Slide 31

Hierarchical -
Layered Software Architecture
- Each layer is a level of abstraction
around a role
- Each layer is not concerned with the 
“how” of the other layers
- For e.g. the business layer does not 
need to know about how to format 
customer data for display on a 
screen or even where the customer 
data is coming from
Presentation
Layer
Business
Layer
Persistence
Layer
Component Component Component
Component Component Component
Component Component Component
Database
Components,
Packages,
Classes

### Slide 32

Hierarchical -
Layered Software Architecture
- The layers are usually closed: as a 
request moves from layer to layer, it 
must go through the layer right below it 
to get to the bottom layer
- Layers of isolation: the changes made 
in one layer of the architecture 
generally does not impact or affect 
components in other layers: the 
change is isolated to the components 
within that layer, and possibly another 
associated layer.
Presentation
Layer
Business
Layer
Persistence
Layer
Component Component Component
Component Component Component
Component Component Component
Database
Components,
Packages,
Classes Request

### Slide 33

Hierarchical -
Layered Software Architecture
- Disadvantages:
- More code will be necessary for layered applications. This is to provide the 
interfaces and other logic that are necessary for the communication between 
multiple layers
- Development teams have to be diligent about placing code in the correct 
layer so as not to leak logic to a layer that belongs to another layer
- There can be inefficiencies in having a request go through multiple layers. In 
addition, moving from one layer to another sometimes requires data 
representations to be transformed.

### Slide 34

Distributed -
Client-Server Pattern
- A popular architectural pattern present in today’s modern systems
- It decomposes software systems into two main components: The client 
and the server
- There can be multiple clients connected to a single server
Client Server
<<Request>>
<<Response>>
A client requests 
some resources or 
calls some service
The server responds to 
the requests of the client
2-Tier Architecture

### Slide 35

Application of Client-Server Pattern
- Consider an email system similar to Outlook
- Two components: EmailClient and EmailServer components.
- EmailServer provides two separate services to the client, implemented by two 
sub-components: Retrieval and Transport
- The Retrieval component provides facilities for the client to access and 
download emails stored on the server via the IMAP interface, an email retrieval 
protocol
- The Transport component allows the client to submit emails for delivery to other 
users, via the SMTP interface, an email transport protocol

### Slide 36

Application of Client-Server Pattern

### Slide 37

Interactive -
Model-View-Controller (MVC)
- The MVC pattern is widely used in 
interactive applications that require 
flexible incorporation of human- computer interfaces
- MVC decomposes applications into 
three main components that handle 
independently the system’s input, 
processing and output
- A number of popular web and 
application development 
frameworks make use of this 
pattern. A few examples include 
Ruby on Rails, ASP.NET MVC and 
Spring MVC.
Model
View Controller
Sends
State
Changes
Updates
model
Selects view
Sends user actions

### Slide 38

Interactive -
Model-View-Controller (MVC)
Model
View Controller
Sends
State
Changes
Updates
model
Selects view
Sends user actions
Model:
- Contains domain-specific knowledge
- Often linked to a database
- One model can link to different views
View:
- Presents data to the user
- Allows user interaction
- Does no processing
Controller:
- Controls the flow of 
information between 
the model and the view
- Receives messages from 
the view (where events 
come from)
- Sends messages to the 
model (tells what data 
to display)

### Slide 39

Application of MVC
- Consider a real estate housing market system that allows users to find 
properties for sale:
- The real estate system composed of two views, each with their own controller 
and a model that contains all real estate information
- The two views are designed uniquely for usability on a standard PC and a 
smart phone
- Both views support display. For input, PCView component support interactive 
buttons and menu options, while a smart phone is much smaller, SmartPhoneView
only supports speech recognition.

### Slide 40

Application of MVC
From component diagram, fit the diagram into the suitable architecture pattern

### Slide 41

OVERALL AGENDA
-Intro to Software Architecture - – pre-recorded videos & iRAT
-Overview of Architecture
- C4 model
- 4+1 model
-Architectural Patterns
-Layered
-Client Server
-Model-View-Controller

### Slide 42

SUMMARY
- The 4+1 Model provides a standard for 5 software architecture diagrams
- The C4 Model provides a four key concetps together with some conventions of how 
to describe the static structure of a software system.
C4 Model 4+1

### Slide 43

SUMMARY
Hierarchical -
Layered Software Architecture
Interactive -
Model-View-Controller (MVC)
Client Server
<<Request>>
<<Response>>
A client requests 
some resources or 
calls some service
The server responds to 
the requests of the client
Model
View Controller
Sends
State
Changes
Updates
model
Selects view
Sends user actions
Distributed -
Client-Server Pattern


---

## Week 9 (Part 2): Design Patterns

### Slide 1

INTRODUCTION TO DETAILED DESIGN
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?
DETAILED DESIGN

### Slide 2

SO FAR THIS WEEK (W9)
Introduction to Detailed Design
Introduction to Detailed Design - Video

### Slide 3

OVERALL AGENDA
-Intro to Detailed Design - pre-recorded videos
-Design Patterns

### Slide 4

DESIGN CHALLENGES
- Designing software is hard. What is needed:
- Good problem decomposition
- A design with flexibility, modularity and elegance
- Design often emerge from iterative process (trial and error)
- Successful designs do exist
- Two designs are almost never identical; however
- They exhibit some recurring characteristics

### Slide 5

Design patterns
Each pattern describes a problem which occurs over 
and over again in our environment, and then 
describes the core of the solution to that problem, in 
such a way that you can use this solution a million 
times over, without ever doing it the same way twice.
Christopher Alexander (1977)

### Slide 6

Design Patterns – Motivating Example
Problem: operate on every element of an array
Solution: use a ‘for’ loop
for (int i = 0; i < a.Length; i++) {
// do something with a[i]
}
The variable names and operation may be different every time, 
but the structure of the solution is the same.

### Slide 7

Design patterns 
Do you know any patterns (OO or not) that would solve the following 
problems?
- store an arbitrary number of items of the same type, the number of which might change 
throughout the execution of the program
- divide a problem into smaller versions of itself
- maintain a sorted collection of objects

### Slide 8

Design Patterns
Design patterns in software engineering were 
popularised by Erich Gamma, Richard Helm, 
Ralph Johnson and John Vlissides
- known as “the Gang of Four” (or GoF)
- Design Patterns: Elements of Reusable ObjectOriented Software (1995)
We will focus on object-oriented patterns in this course.

### Slide 9

Design Patterns
The Gang of Four divided patterns into three groups:
- creational patterns, for instantiating objects
- structural patterns, for managing relationships between objects
- behavioural patterns, for implementing common behaviours
Each pattern is described using a subset of the template used by the 
Gang of Four.
- Our template is based on the one used by Millett (2010).

### Slide 10

Design Pattern Template
Pattern Name
Intent
A brief description of the problem that the pattern is designed to solve.
Applicability
A list of situations in which the pattern can be useful.
UML Diagram
A UML class diagram illustrating the pattern.
Code Example
An example implementation

### Slide 11

Design Patterns
Creational 
Design Pattern
Factory
Abstract 
Factory
Builder
Prototype
Singleton
Structural 
Design Pattern
Adapter
Bridge
Composite
Decorator
Façade
Flyweight
Proxy
Behavioral Design Patterns
Chain of Responsibility
Command
Interpreter
Iterator
Mediator
Memento
Observer
State
Strategy
Template Method
Visitor

### Slide 12

Creational Design Pattern - Factory
- Problem : 
- An abstract class has many concrete subclasses
- Abstract class cannot be instantiated
- We many need to create and store many instances for the abstract class based 
on a concrete class
- We may need to add new concrete subclasses
- Solution:
A factory is a class responsible for instantiating 
other classes.
CreateProduct()

### Slide 13

Creational Design Pattern - Factory
Intent
To provide a method by which objects can be created, allowing subclasses to 
decide which concrete class should be used.
Applicability
- when the concrete type of an object must be determined at run-time
- when more concrete types might be developed over time
- to encapsulate the logic of choosing the appropriate concrete type in a single 
function
Frequency of use

### Slide 14

Creational Design Pattern - Factory 
UML Diagram
Client
+CreateProduct() : IProduct
Factory
<<Interface>> ProductA ProductB
IProduct
creates creates
Visual Paradigm Enterprise Edition(Singapore Institute of Technology)

### Slide 15

Factory – How It Works
The Factory.CreateProduct() method is often static
- otherwise, the Client must instantiate a Factory first
The client invokes Factory.CreateProduct() with some parameters:
IProduct prod = Factory.CreateProduct("A");
Factory.CreateProduct() decides which subclass to instantiate 
according to the parameters:
switch (productType) {
case "A": return new ProductA();
case "B": return new ProductB();
}

### Slide 16

Creational Design Pattern - Singleton
Intent
To ensure that only one instance of a class exists.
Applicability
- for providing access to unique resources (e.g. the console)
- for grouping global variables
Frequency of use
-instance : Singleton
-Singleton()
+GetInstance() : Singleton
Singleton
Visual Paradigm Enterprise Edition(Singapore

### Slide 17

Design Patterns
- Other useful / interesting patterns
- Observer Pattern (Behavioral):
- A class that generates events maintains a list of 
observers (or listeners) that will be notified when an 
event arrives
- Composite Pattern (Structural)
- Re-use existing classes in new context and build 
complex structure from simpler components
Observer Pattern
Composite Pattern

### Slide 18

OVERALL AGENDA
-Intro to Detailed Design -
pre-recorded videos & iRAT
-Design Patterns
https://refactoring.guru/design-patterns

### Slide 19

SUMMARY
Architecture Patterns Design Patterns 
Role
Example
Level
Problem addressed
https://www.simform.com/blog/software-architecture-patterns/
Definition
Fundamental structural organization for software 
system
Specification that could help in implementation of 
a software
Conversion of software characteristics to high 
level structure 
Description of all units of software system to support 
coding
Layered, client server, MVC Creational, Structural, Behavioral
Large level tools – concerns with large scale 
components, global properties & mechanism 
Small level tools – concerns schemes for refining 
and building smaller subsystem
System partitioning, interfaces, scalability, 
reliability, security
Problems in software construction


---

## Week 10 (Part 1): Blackbox Testing

### Slide 1

INTRODUCTION TO BLACKBOX TESTING
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?

### Slide 2

Recap – W8 Component Diagram and Intro to Software Design

### Slide 3

Recap – W9 Software Architecture & Detailed Design

### Slide 4

SO FAR THIS WEEK (W10)
Introduction to Software Testing
Introduction to Software Testing - Video

### Slide 5

OVERALL AGENDA
-Introduction to Software Testing – prerecorded video 
-Software Testing Techniques
-Non-Execution Based Testing
-Execution Based Testing
-Black Box Testing
-White Box Testing

### Slide 6

Non-Execution-Based Testing
- Checking for quality without running test cases
- Underlying principles
- We should not review our own work
- Group synergy
- Techniques
- Walkthrough
- Inspection
- Technical Review (a.k.a. Peer Reviews)

### Slide 7

“A static analysis technique in which a designer or 
programmer leads members of the development 
team and other interested parties through a 
software product, and the participants ask 
questions and make comments about possible 
errors, violation of development standards, and 
other problems.” 
Major objectives:
a) Find anomalies
b) Improve the software product 
c) Consider alternatives
d) Evaluate conformance to standards and 
specifications
(IEEE Standard for Software Reviews)
WALKTHROUGHS
In walkthroughs, we detect faults, not correct them!

### Slide 8

INSPECTIONS
“The purpose of an inspection is to detect and identify software product 
anomalies. “
This is a systematic examination that:
a) Verifies that the software product satisfies its specifications 
b) Verifies that the software product satisfies specified quality attributes 
c) Verifies that the software product conforms to applicable regulations, standards, 
guidelines, plans, and procedures 
d) Identifies deviations from standards and specifications 
e) Collects software engineering data
(for example, anomaly and effort data) (optional) 
f) Uses the collected software engineering data to improve the inspection process 
 and its supporting documentation (for example, checklists) (optional)”
(IEEE Standard for Software Reviews)

### Slide 9

METRICS FOR INSPECTIONS
- Inspection rate (e.g., design pages inspected per hour)
- Fault density (e.g., faults per KLOC inspected)
- Fault detection rate (e.g., faults detected per hour)
- Fault detection efficiency (e.g., number of major, minor faults 
detected per hour)
- Does a 50% increase in the fault detection rate mean 
that
- Quality has decreased? Or
- The inspection process is more efficient?

### Slide 10

Walkthrough
Five-step, formal process
- Overview
- Preparation
- Inspection
- Rework
- Follow-up
Inspection
Two-step, informal process
-Preparation
-Analysis

### Slide 11

Software Testing Techniques
- Sample Inspection Log
http://www.stellman-greene.com/applied-software-project-management/applied-software-project-management-review-practices/ last viewed February 2015

### Slide 12

OVERALL AGENDA
-Introduction to Software Testing
-Software Testing Techniques
-Non-Execution Based Testing
-Walkthrough
-Inspection
-Execution Based Testing
-Black Box Testing
-White Box Testing

### Slide 13

Execution Based Testing
- Execution Based Testing
- Testing via running code
- No false positives
- Can be automated
- Tests correctness, utility, reliability, robustness, performance
- Techniques
- Blackbox Testing
- Whitebox Testing

### Slide 14

WHAT SHOULD BE TESTED?
- Definition of execution-based testing
“The process of inferring certain behavioral properties of the 
product based, in part, on the results of executing the 
product in a known environment with selected inputs”
We hardly ever really
know the environment
We don’t always have 
control over all inputs.
How many test cases 
do we need?
Which inputs should 
we use?

### Slide 15

WHAT SHOULD BE TESTED? 
- Definition of execution-based testing
“The process of inferring certain behavioral properties of the 
product based, in part, on the results of executing the 
product in a known environment with selected inputs”
- First, we need to test correctness, 
What else?
We need to test for whatever the 
specification documents specify

### Slide 16

WHAT SHOULD BE TESTED? 
Correctness A product is correct if it satisfies its specifications
Specifications may be incorrect themselves.
Specifications may be correct, but incomplete –
allowing for “incorrect” implementations to meet the specification.
Utility The extent to which the product meets the user’s needs
Ease of use
Useful functions
Reliability A measure of the frequency and criticality of failure
Mean time between failures
Time (and cost) to repair the results of a failure
Robustness A function of
The range of operating conditions
The effect of invalid input
Performance The extent to which space and time constraints are met
May affect correctness, robustness, reliability…

### Slide 17

EXECUTION-BASED TESTING TECHNIQUES
- Two main categories for testing:
White box testing
- A.K.A 
glass box, clear box testing, 
transparent box testing, 
structural testing, 
logic driven testing
- Tests based on internal 
structures or workings of an 
application
Black box testing
- A.K.A 
functional testing, behavioural 
testing
- Tests the observable 
functionality of an application

### Slide 18

BLACK BOX TESTING
- Validates conformity to the specifications.
- Introduces a series of inputs to a system and compares the outputs against the predefined test specification (only).
- Black Box testing is applicable to all forms of testing : unit, integrations, system, 
acceptance
- The tests are architecture independent 
- Given a chosen input, we do not care how the output is produced, only whether that 
output is the desired and expected output.
- Test can be functional or non functional
- Designing the tests require no knowledge underlying system, 
- Does not require a software engineer or programming skills. INPUT APPLICATION OUTPUT

### Slide 19

BLACK BOX TESTING
- Different techniques provide different guarantees and assurances 
regarding the system under test.
- Black box testing techniques include:
- Equivalence partitioning
- Boundary value analysis
- Decision table testing
- All-pairs testing (and N-wise testing)
- State transition analysis
- Cause–effect graph
- Error guessing
Different 
ways of 
choosing 
inputs for 
the tests

### Slide 20

Black Box Testing – Equivalence Partitioning
- Divide input values into valid and invalid partitions and selecting 
representative values from each partition as test data.
- Inputs are divided into different equivalent data classes
- Each partition is tested once as all inputs within are considered 
“equivalent”
Possible input values
Partition 1 Partition 2 …. Partition n
Choose one value from each partition for testing

### Slide 21

Black Box Testing
Equivalence Partitioning
Example: 
Imagine testing for an input form that requires 
user to enter a percentage value (%). The form 
only accepts value between 50-90%. 
- Invalid partition 1: < 50
- Valid Partition : 50-90
- Invalid partition 2: > 90
To test: 
Choose 30 from Invalid Partition 1 –System should reject
Choose 60 from Valid partition –System should accept 
Choose 100 from Invalid Partition 2 –System should reject
< 50 50-90 > 90

### Slide 22

Black Box Testing
Equivalence Partitioning
For equivalence partitioning, how do you know how many partitions?
It would depend on the range of all your possible input values and what 
function you are testing. The goal is to come up with as few partitions as 
possible that can cover the whole range of possible input values.
How do you choose the specific test value for each partition?
Randomly as long as the test value is within that partition. 
This is different from boundary value analysis, where you _must_ choose 
the boundary values and values near the boundaries

### Slide 23

Black Box Testing - Boundary Value Analysis 
- Similar to equivalence partitioning, but test values at the boundary
- More application errors occur at the boundaries.
Possible input values
Partition 1 Partition 2 …. Partition n
Choose values at and near the boundaries for testing
Boundary 
values
Boundary 
values
Boundary 
values

### Slide 24

Black Box Testing
Boundary Value Analysis 
Example: 
Imagine testing for an input form that requires user 
to enter a percentage value (%). The form only 
accepts value between 50-90%. 
To test: 
- Choose 49 –System should reject
- Choose 50 –System should accept 
- Choose 51 –System should accept 
- Choose 89 –System should accept 
- Choose 90 –System should accept 
- Choose 91 –System should reject
< 50 50 90 > 90
Boundary 
values
Boundary 
values
49 50 51 89 90 91

### Slide 25

- A decision table is a tabular form that 
presents a set of cause and their 
corresponding effects. 
- A decision table consists of a number of
columns (rules) that comprise all test 
situations.
Causes Values 1 2 3 4 5 6 7 8
Cause 1 Y, N Y Y Y Y N N N N
Cause 2 Y, N Y Y N N Y Y N N
Cause 3 Y, N Y N Y N Y N Y N
Effects
Effect 1 X X X
Effect 2 X X X
Combinations
Black Box Testing – Decision table

### Slide 26

1. List all causes in the decision table
2. Calculate the number of possible combinations
3. Fill columns with all possible combinations (inputs)
4. Add effects to the table (expected outputs)
5. Reduce test combinations
6. Check covered combinations
Cause (Inputs) and Effect (Outputs)
Causes Values 1 2 3 4 5 6 7 8
Cause 1 Y, N Y Y Y Y N N N N
Cause 2 Y, N Y Y N N Y Y N N
Cause 3 Y, N Y N Y N Y N Y N
Effects
Effect 1 X X X
Effect 2 X X X
Combinations
Black Box Testing – Decision Tables

### Slide 27

Black Box Testing - Decision Tables
Causes Values
C1 Email Y,N
C2 Password Y,N
Example 1: Testing login to system: username & password
1. List all causes in the decision table

### Slide 28

Black Box Testing - Decision Tables
Causes Values
C1 Email Y,N
C2 Password Y,N
Number of possible combinations: NumOfValuesOfCause(1) * NumOfValuesOfCause(2)
 2 * 2 = 4 // so there will be 4 combinations (Columns)
Example 1: testing login to system: username & password
1. List all causes in the decision table
2. Calculate the number of possible combinations
NumOfValuesOfCause(1) * NumOfValuesOfCause(2) * … * NumOfValuesOfCause(n)
Causes Values
C1 Email Y,N
C2 Password Y,N

### Slide 29

Black Box Testing - Decision Tables
Causes Values 1 2 3 4
C1 Email Y,N N N Y Y
C2 Password Y,N N Y N Y
3. Fill columns with all possible combinations (inputs)

### Slide 30

Black Box Testing - Decision Tables
Causes Values 1 2 3 4
C1 Email Y,N N N Y Y
C2 Password Y,N N Y N Y
Effects
E1 Accept x
E2 Reject x x x
4. Add effects to the table (expected outputs)
Causes Values 1 2 3 4
C1 Email Y,N N N Y Y
C2 Password Y,N N Y N Y

### Slide 31

Black Box Testing - Decision Tables
Causes Values 1 2 3 4
C1 Email Y,N N N Y Y
C2 Password Y,N N Y N Y
Effects
E1 Accept x
E2 Reject x x x
5. Reduce Test Combinations
Causes Values 1-2 3 4
C1 Email Y,N N Y Y
C2 Password Y,N - N Y
Effects
E1 Accept x
E2 Reject x x
Reduced based on 
indifferent combination. 
If no e-mail then state of 
password doesn’t matter
Reduced from 4 test 
cases to 3

### Slide 32

Black Box Testing - Decision Tables
Example 2: Account access to withdraw money
1. List all causes in the decision table
Causes Values
C1 A/C Exists Y/N
C2 Pin 
Correct
Y/N
C3 Balance 
Available
Y/N

### Slide 33

Black Box Testing - Decision Tables
Example 2: Account access to withdraw money
1. List all causes in the decision table
2. Calculate the number of possible combinations
Causes Values
C1 A/C Exists Y/N
C2 Pin 
Correct
Y/N
C3 Balance 
Available
Y/N
2*2*2 = 8 // so there will be 8 combinations columns)
Causes Values
C1 A/C Exists Y/N
C2 Pin 
Correct
Y/N
C3 Balance 
Available
Y/N
NumOfValuesOfCause(1) * NumOfValuesOfCause(2) * … * NumOfValuesOfCause(n)

### Slide 34

Black Box Testing - Decision Tables
3. Fill columns with all possible combinations (inputs)
Causes Values 1 2 3 4 5 6 7 8
C1 A/C Exists Y/N N N N N Y Y Y Y
C2 Pin 
Correct
Y/N N N Y Y N N Y Y
C3 Balance 
Available
Y/N N Y N Y N Y N Y

### Slide 35

Black Box Testing - Decision Tables
4. Add effects to the table (expected outputs)
Causes Values 1 2 3 4 5 6 7 8
C1 A/C Exists Y/N N N N N Y Y Y Y
C2 Pin Correct Y/N N N Y Y N N Y Y
C3 Balance 
Available
Y/N N Y N Y N Y N Y
Effects
E1 Withdrawal x
E2 Denied x x x x x x x

### Slide 36

Black Box Testing - Decision Tables
5. Reduce Test Combinations
Causes Values 1 2 3 4 5 6 7 8
C1 A/C Exists Y/N N N N N Y Y Y Y
C2 Pin Correct Y/N N N Y Y N N Y Y
C3 Balance 
Available
Y/N N Y N Y N Y N Y
Effects
E1 Withdrawal x
E2 Denied x x x x x x x
Causes Values 1-4 5-6 7 8
C1 A/C Exists Y/N N Y Y Y
C2 Pin Correct Y/N - N Y Y
C3 Balance 
Available
Y/N - - N Y
Effects
E1 Withdrawal x
E2 Denied x x x
indifferent 
combination. 
Reduced from 8 test 
cases to 4

### Slide 37

Black Box Testing - Decision Tables
- Once you have reduced your decision table, you can come up with specific 
test cases to be passed to Software Testing Engineer/QA Engineer. 
- Tester does not need to be a programmer or even technical, they just need 
to be able to follow a test case
- Decision table testing is not suited to the systems that have a large number 
of causes
- Modules related to performance testing and optimization may provide 
solutions to this

### Slide 38

Black Box Testing - Decision Tables
Test Scenario Test Case Pre-Conditions Test Data Test Steps Expected Result Actual Result Pass/Fail
Invalid Withdrawal 
#1 A/C does not exist User does not have an account
Account Number: 
999999 
PIN: 1234 
Balance: N/A 
Withdrawal 
Amount: $100
1. Insert card or 
enter account 
details 
2. Enter PIN (any) 
3. Request 
withdrawal amount
Withdrawal denied Withdrawal failed Pass
Invalid Withdrawal 
#2
A/C exists, PIN is 
correct, but 
balance is 
insufficient
User has an existing 
account, correct 
PIN, but insufficient 
balance
Account Number: 
123456 
PIN: 1234 
Balance: $50 
Withdrawal 
Amount: $100
1. Insert card or 
enter account 
details 
2. Enter correct PIN 
3. Request 
withdrawal amount
Withdrawal denied … ….
Invalid Withdrawal 
#3
A/C exists, but PIN 
is incorrect
User has an existing 
account, but 
incorrect PIN
Account Number: 
123456 
PIN: 9999 
Balance: $500 
Withdrawal 
Amount: $100
1. Insert card or 
enter account 
details 
2. Enter incorrect 
PIN 
3. Request 
withdrawal amount
Withdrawal denied … ….
Valid Withdrawal
A/C exists, PIN is 
correct, balance is 
available
User has an existing 
account, correct 
PIN, and sufficient 
balance
Account Number: 
123456 
PIN: 1234 
Balance: $500 
Withdrawal 
Amount: $100
1. Insert card or 
enter account 
details 
2. Enter correct PIN 
3. Request 
withdrawal amount
Withdrawal is 
successful … ….
Actual Result and Pass/Fail columns would be filled after running the tests

### Slide 39

OVERALL AGENDA
-Introduction to Software Testing
-Software Testing Techniques
-Non-Execution Based Testing
-Execution Based Testing
-Black Box Testing
-White Box Testing

### Slide 40

SUMMARY
- Quality assurance consists of many activities which fall into the realm of 
verification and validation
- Everyone is responsible for QA (but should have dedicated)
- Non-Execution based testing:
- Walkthrough
- Inspection (more formal)

### Slide 41

SUMMARY
- Execution based testing:
- Black Box – based on specification only
- Equivalence partitioning
- Boundary value analysis
- Decision Tables
- White Box – looking into the code (next!)
- All are limited to specific test-cases


---

## Week 10 (Part 2): Whitebox Testing

### Slide 1

INTRODUCTION TO WHITEBOX TESTING
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?

### Slide 2

PREVIOUSLY
-Introduction to Software Testing
-Software Testing Techniques
-Non-Execution Based Testing
-Execution Based Testing
-Black Box Testing
-White Box Testing
-UAT & Application Packaging

### Slide 3

AGENDA
-What is White-Box testing
-White-box testing techniques overview
-Coverage Testing
  - Coverage Criteria
  - Statement Coverage
  - Control Flow Graphs
  - Branch Coverage
  - Path Coverage
-Basis Path / Control Flow Testing
-UAT & Application Packaging

### Slide 4

What is White-Box Testing
- What is in the Box?
- Black-box testing considers only inputs and outputs
- White-box testing looks inside the box - at the code
- Both Black-box and White-Box testing are execution-based test
- White-Box testing has many names:
- Structural Testing, Logic Driven Testing, Clear/Open/Glass Box Testing
- White-Box testing and Black-Box testing are complementary techniques
- Black-Box testing cannot reveal errors due to implementation details
- White-Box testing cannot reveal errors due to missing paths

### Slide 5

What is White-Box Testing
- The goal of White-Box Testing:
- To uncover as many bugs as possible in a small but carefully selected subset of 
the input domain
- To process every single character in code and test for errors
- Usually impractical to cover the entire input domain
- “Executing a faulty statement is a necessary condition for revealing 
fault” – This means, we must execute a faulty statement to reveal that it 
is faulty.
1. Exhaustive testing 
is not possible
2. Provide the 
strongest guarantees 
about the system at 
minimum effort (cost)

### Slide 6

AGENDA
-What is White-Box testing
-White-box testing techniques overview
-Coverage Testing
  - Coverage Criteria
  - Statement Coverage
  - Control Flow Graphs
  - Branch Coverage
  - Path Coverage
-Basis Path / Control Flow Testing
-UAT & Application Packaging

### Slide 7

White-Box Testing Techniques
- Control-Flow Testing
- Data-Flow Testing
- Branch Testing
- Statement Coverage
- Decision Coverage
- Modified Condition / Decision Coverage
- Prime Path Testing
- Path Testing

### Slide 8

White-Box Testing Techniques
- Testing can be done at many levels including:
- Unit Testing: Testing Individual Modules
- Integration Testing: Tests between units, interactions among modules
- Regression Testing: Tests we perform every time we change our system to 
ensure changes behave as expected and unchanged code doesn’t behave any 
differently
- Other Types of Tests:
- Acceptance Testing
- Load Testing
- Alpha / Beta Testing

### Slide 9

AGENDA
-What is White-Box testing
-White-box testing techniques overview
-Coverage Testing
  - Coverage Criteria
  - Statement Coverage
  - Control Flow Graphs
  - Branch Coverage
  - Path Coverage
-Basis Path / Control Flow Testing
-UAT & Application Packaging

### Slide 10

Coverage Criteria
- Coverage-Criteria is defined in terms of the Test Requirements
- In simple terms, what are the interesting cases we can identify in the code 
(interesting based on what we want to cover)
- Results in Test-Specification and Test-Cases
- Test Specification
- What must our inputs be to get these interesting cases to be executed
- Test Case
- Concrete values applied based on our Test Specification logic, with expected 
output from that statement

### Slide 11

Statement Coverage
- Test Requirements: Statements in the Program
- Coverage Measure: 
- Process: Highlight each line of code that is actually run based on a 
Test-Case

### Slide 12

Statement Coverage
- Statement testing focuses on verifying whether each statement in the 
code executes at least once. However, it doesn’t guarantee coverage 
of all possible execution paths, as it doesn’t test different combinations 
of conditions that might influence program flow. 
- Example:
def example_function(x, y):
 if x > 0:
 print("X is positive")
 if y > 0:
 print("Y is positive")
 if x > 0 and y > 0:
 print("Both X and Y are positive")
You can cover all statement with a single 
test case where x=1 and y=1
However, there are more paths!
Path 1: x > 0 and y > 0
Path 2: x > 0 and y < 0
Path 3: x < 0 and y > 0
Path 4: x < 0 and y < 0

### Slide 13

Control-Flow Graph
- A control-flow-graph (CFG) helps us visualize both statements and the 
flow of control in a module.
- Statements are represented as nodes
- Flow of control within the code represented with edges
- A node with more than one outgoing edge, each edge is referred to as a 
branch (leads us later to discussing branch coverage)
Nodes
Edges
PATH
branches branches
Path is the route we can take with the 
code from start to finish
This diagram has 2 paths

### Slide 14

Control Flow Graphs
- Structured Programming Constructs
Sequence
for loop
If then
If then else
select case
while loop

### Slide 15

Control Flow Graphs
- Structured Programming Constructs
Sequence While Loop

### Slide 16

Control Flow Graphs
- Structured Programming Constructs
Sequence For loop
If-Then If-Then-Else Select Case
While Loop

### Slide 17

Control-Flow Graph - Simple Branching Example 
1. void CheckSavings(int income, int expenses) {
2. int result = income - expenses;
3. if (result >= 500)
4. Console.WriteLine("Not bad, you save this much:", result);
5. else if (result < 500)
6. Console.WriteLine("Reduce those expenses, your savings is this much:", result);
7. } // code exit
1
2
3
4
6
5
7
Entry Point
T F
T
F
Exit Point
TEST SPECIFICATION:
Requirement #1 : input income – expense must be greater than or equal to 500
Requirement #2 : input income – expense must be less than 500
Statement Coverage : What inputs to cover all statements?

### Slide 18

Control-Flow Graph - Simple Branching Example 
1. void CheckSavings(int income, int expenses) {
2. int result = income - expenses;
3. if (result >= 500)
4. Console.WriteLine("Not bad, you save this much:", result);
5. else if (result < 500)
6. Console.WriteLine("Reduce those expenses, your savings is this much:", result);
7. } // code exit
1
2
3
4
6
5
7
Entry Point
T F
T
F
Exit Point
TEST SPECIFICATION:
Requirement #1 : input income – expense must be greater than or equal to 500
Requirement #2 : input income – expense must be less than 500
TEST CASE (CONCRETE VALUES):
#1 ((income=[1000], expenses[200]), (output_text=“Not Bad, you save this much: 800”, output_value=[800]))
#2 ((income=[400], expenses[400]), (output_text=“Reduce those expenses, your savings are: 0”, output_value=[0]))
Statement Coverage : What inputs to cover all statements?

### Slide 19

Control-Flow Graph - Loop Example
1. void TruthLoop(int greatness) {
2. for (int i = 0; i < 10 ; i++) {
3. if (greatness > 10)
4. Console.WriteLine("I am so great!");
5. else
6. Console.WriteLine("I am not so great!");
 }
7. } // code exit 5
Exit Point
1
2
3
4
6 7
T F
T F
Entry Point
Loop

### Slide 20

Control-Flow Graph
Branches:
- For every node that has more than one outgoing edge, count those edges
- Example 1: 1 node with more than one outgoing edge, 2 branches
- Example 2: 2 nodes with more than one outgoing edge, 4 branches
Cyclomatic Complexity (M) 
Software metric used to indicate the complexity of a program
Number of linearly independent paths
M = E – N + 2P
E = Number of edges
N = Number of nodes
P = Number of connected components
 (don’t worry about this one, just make it 1)
Example 1 : 7-7+2(1) = 2
Example 2 : 8-7+2(1) = 3 Example 1 Example 2

### Slide 21

5
Exit Point
T
1
2
3
4
6 7
F
T F
Entry Point
Loop
Control Flow Graphs – Cyclomatic Complexity (M) 
1
2
3
4
6
5
7
Entry Point
T F
T
Exit Point
Example 1: 
M=7-7+2(1) = 2
Example 2 : 
M=8-7+2(1) = 3

### Slide 22

Branch Coverage
- Statements testing may not reveal all possible paths that the code may 
take, hence may not show all necessary tests we should run
- Branch Coverage attempts to explore all possible branches (in theory)
- Branch Coverage (%) = (Number Branches Executed & Tested)/ (Total Number of Branches)
- Test Requirements: Branches in the program
- Coverage Measure: Number of Executed Braches / Total Number of Branches

### Slide 23

Control-Flow Graph - Simple Branching Example 
1. void CheckSavings(int income, int expenses) {
2. int result = income - expenses;
3. if (result >= 500)
4. Console.WriteLine("Not bad, you save this much:", result);
5. else if (result < 500)
6. Console.WriteLine("Reduce those expenses, your savings is this much:", result);
7. } // code exit
1
2
3
4
6
5
7
Entry Point
T F
T
F
Exit Point
TEST SPECIFICATION:
Requirement #1 : input income – expense must be greater than or equal to 500
Requirement #2 : input income – expense must be less than 500
Statement Coverage : What inputs to cover all statements?
TEST CASE (CONCRETE VALUES):
#1 ((income=[1000], expenses[200]), (output_text=“Not Bad, you save this much: 800”, output_value=[800]))
#2 ((income=[400], expenses[400]), (output_text=“Reduce those expenses, your savings are: 0”, output_value=[0]))

### Slide 24

Branch Coverage - Simple Branching Example 
1. void CheckSavings(int income, int expenses) {
2. int result = income - expenses;
3. if (result > 500)
4. Console.WriteLine("Not bad, you save this much:", result);
5. else if (result < 500)
6. Console.WriteLine("Reduce those expenses, your savings is this much:", result);
7. } // code exit
1
2
3
4
6
5
7
Entry Point
T F
T
F
Exit Point
TEST SPECIFICATION:
Requirement #1 : input income – expense must be greater than 500
Requirement #2 : input income – expense must be less than 500
F
TEST CASE (CONCRETE VALUES):
#1 ((income=[1000], expenses[200]), (output_text=“Not Bad, you save this much: 800”, output_value=[800]))
#2 ((income=[400], expenses[400]), (output_text=“Reduce those expenses, your savings are: 0”, output_value=[0]))
We need to change our test cases because we have a new branch!
Statement Coverage = 100%
Branch Coverage = 75% (only 3 of 4 branches have been explored)

### Slide 25

Path Coverage
- Generate coverage such that all the paths in the program are covered
- Very expensive, any non-trivial program may have a virtually infinite number 
of paths
5
Exit Point
1
2
3
4
6 7
T F
T F
Entry Point
Loop

### Slide 26

AGENDA
-What is White-Box testing
-White-box testing techniques overview
-Coverage Testing
  - Coverage Criteria
  - Statement Coverage
  - Control Flow Graphs
  - Branch Coverage
  - Path Coverage
-Basis Path / Control Flow Testing
-UAT & Application Packaging

### Slide 27

Control Flow Testing
- Type of white-box testing that tests all possible independent paths in 
the control flow graph of a program
- Best executed for procedures
- The guarantee
- Every statement of the program has been executed at least once and every 
transition was tested
- The method helps:
- Figure out how many test cases are needed
- Figure out how to construct each test (what to test)

### Slide 28

Control Flow Testing
- Basis Paths
- A set of paths, such that any other path can be “constructed” out of a 
combination of the basis paths
- Designed to test all possible paths at least once (linearly independent)
- Results in 100% statement coverage and 100% branch coverage.
- Therefore, basis paths include all the edges of the graph
- The size of the set is related to the Cyclomatic Complexity of the graph
Code Flow
graph
Basis 
Paths
Test 
cases

### Slide 29

Cyclomatic complexity
- The cyclomatic number is an upper bound for the number of paths in 
the set of basis paths
A
B C
D
E
F G
H
cyclomatic number:
M = E – N + 2P = 9-8+2 = 3 
Looking at it, minimum tests needed: 2 
If just want to go through each node and edges, then 2 
path is enough, however, a complete test would require 
3 paths: ABDEFH, ABDEGH, ACDE

### Slide 30

Determine a set of basis paths
Steps
Pick a “baseline” path that corresponds to normal execution (aim to have 
as many decisions as possible)
To get succeeding basis paths, back-track the baseline until you reach a 
decision node. “Flip” the decision (take another alternative) and continue 
as much of the baseline as possible
Repeat this until all decisions have been flipped. When you reach M 
(Cyclomatic complexity) basis paths, you’re done!

### Slide 31

Determine a set of basis paths
Pick a "baseline" path 
that corresponds to 
normal execution (aim to 
have as many decisions 
as possible.) 
Path 1: A - B - C - E - F - G – J - K - L 
Pick a “baseline” path that 
corresponds to normal execution 
(aim to have as many decisions as 
possible)

### Slide 32

Path 1: Path 1: A - B - C - E - F - G – J - K - L 
Determine a set of basis paths
Path 2: A - B - C - E - F – H – J - K - L 
Path 3: A - B - C - E - F – I – J - K - L 
Path 4: A - B - C - D - K - L 
To get succeeding basis paths, backtrack the baseline until you reach a 
decision node. “Flip” the decision 
(take another alternative) and 
continue as much of the baseline as 
possible

### Slide 33

Path 1: Path 1: A - B - C - E - F - G – J - K - L 
Determine a set of basis paths
Repeat this until all decisions have 
been flipped. When you reach V(G) 
basis paths, you're done. 
Path 2: A - B - C - E - F – H – J - K - L 
Path 3: A - B - C - E - F – I – J - K - L 
Path 4: A - B - C - D - K - L 
Repeat this until all 
decisions have been 
flipped. When you reach M 
(Cyclomatic complexity) 
basis paths, you’re done!
M = E – N + 2P
M = 14 – 12 + 2(1) = 4

### Slide 34

Almost there, last step
Code Flow
graph
Basis 
Paths
Test 
cases
Translate each 
path to a test 
case
Source code
Path 1: A - B - C - E - F - G – J - K - L 
Path 2: A - B - C - E - F – H – J - K - L 
Path 3: A - B - C - E - F – I – J - K - L 
Path 4: A - B - C - D - K - L 
Path Var 1 Var 2 … Var n Exp
Outp
ut
Path 1
…
Path 4

### Slide 35

CONTROL FLOW TESTING
A Test Case
“A set of test inputs, execution conditions, and expected results 
developed for a particular objective, such as to exercise a 
particular program path or to verify compliance with a specific 
requirement.” (IEEE)
Practically – a set of instruction for running a specific test.

### Slide 36

Advantages and Disadvantages 
Whitebox Testing
Advantages
- Attempts to test all functionalities
- It identifies error in the hidden code and 
thus makes debugging process swift.
- It removes extra lines of code which are 
not required in the program thereby 
optimizing the program and increases the 
efficiency.
- It helps in evaluating all the loops and 
paths.
- It can provide stability and usability of 
the test cases.
- Thoroughness achieved in white box 
testing is far more than black box testing.
Disadvantages
- Testers must have a knowledge of 
programming which may be expensive
- 100% coverage is rarely possible, so bugs 
may be missed
- Changes in the code may require all the 
scenarios to be tested again or 
redeveloped.
- Developing test cases takes time
- If the application is large then complete 
testing through white box techniques is not 
feasible.

### Slide 37

For the project – White Box Testing
- Select a feature/method (that is different from the one you cover in 
Black Box Testing)
- Provide a description and pseudocode of the method/feature
- Construct CFG and calculate cyclomatic complexity
- Show basis path and provide test cases to cover all paths

### Slide 38

AGENDA
-What is White-Box testing
-White-box testing techniques overview
-Coverage Testing
-Coverage Criteria
-Statement Coverage
-Control Flow Graphs
-Branch Coverage
-Path Coverage
-Basis Path / Control Flow Testing
-UAT & Application Packaging

### Slide 39

Small Detour - User Acceptance Testing
- User acceptance testing is not system testing
- Unit, Functional and Integration tests should have been 
completed by this phase
- Technically not looking for major errors, wishfully not looking 
for any errors
- System Testing
- Ensure Software does not crash and meets documented 
requirements
- Does system accept correct inputs and give the correct 
outputs (Black-Box Testing)
- Ensure important segments of code have been tested 
thoroughly (White-Box Testing)
- Check resource consumption and load times etc.
Requirement 
Specification
Analysis and 
Design
Deployment
Maintenance
Testing
Implementation
You
Are
Here

### Slide 40

What’s left BEFORE release (UAT)
“User Acceptance Testing is the last phase of the software testing process. 
During UAT, actual software users test the software to make sure it can handle 
required tasks in real-world scenarios, according to specifications. UAT is one 
of the final and critical software project procedures that must occur before
newly developed software is rolled out to the market” – Techopedia
Testing
You
Are
Here
Who should perform UAT?
Subject matter expert (SME), that should know the requirements, know 
what system is supposed to be built and be able to work from those 
expectations, e.g owner, client or end-users of the application.

### Slide 41

Application Packaging
- The process of developing a final deliverable to:
- ensures a consistent, stable and reliable standard environment;
- increases the efficiency of software management by streamlining the software 
deployment along with any customization needed;
- mitigates security issues;
- decreases risks for business disruption;
- helps reduce the on-going administration and support costs.

### Slide 42

Application Packaging
- In simple terms
- Document the process of installation (Read-Me File, Wiki)
- Ensure process of installation of your system is documented for all supporting 
technology and devices
- All prerequisites included, part of install package
- Auto-installer include, one click to installation!
- Any required supporting documents, manuals etc. included during installation or 
provided in an easy to reach source
- Any licensing agreements clearly visible to the user

### Slide 43

SUMMARY
-What is White-Box testing
-White-box testing techniques overview
-Coverage Testing
  - Coverage Criteria
  - Statement Coverage
  - Control Flow Graphs
  - Branch Coverage
  - Path Coverage
-Control Flow Testing
-Basis Path
-UAT & Application Packaging

### Slide 44

Summary
- Whitebox testing is an execution-based test, complementary to black box testing
- Explores what is inside the code rather than just inputs and outputs
- Coverage testing includes: 
- Statement coverage, Branch coverage, and Path coverage (and more)
- CFG helps us visualise both statements and the control flow of a module
- Number of linearly independent paths is referred to as Cyclomatic Complexity
- M=E-N + 2P
- Basis paths are paths from which any other path can be constructed out of a 
combination of the basis paths
- Process for determining basis paths can be achieved in 3 steps
- 1. pick a baseline path
- 2. back-track the baseline until you reach a decision node, then flip
- 3. repeat until all decisions have been flipped
- Can be used to establish suitable test cases


---

## Week 11 (Part 1): Software Maintenance

### Slide 1

SOFTWARE MAINTENANCE
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?

### Slide 2

SO FAR THIS WEEK 
Introduction to Software Maintenance
Introduction to Software Maintenance - Video

### Slide 3

AGENDA
-Overview of Software Maintenance 
-Type of Maintenance Activities
-Refactoring
prerecorded video

### Slide 4

Refactoring
“A change made to the internal structure of software to make it easier 
to understand and cheaper to modify without changing its observable 
behaviour.” – Fowler, 2000

### Slide 5

Refactoring
- Refactoring is:
- Restructuring (rearranging) code…
- … in a series of small, semantics-preserving transformations (i.e. the code 
keeps working)…
- … in order to make the code easier to maintain and modify
- Refactoring is not the same thing as:
- Adding features
- Debugging code
- Rewriting code

### Slide 6

Refactoring Process
6
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test 
case
Identifying 
refactoring 
opportunity
Y
N

### Slide 7

Identifying Refactoring Opportunity
7
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test 
case
Identifying 
refactoring 
opportunity
While you undertake tasks like code review, 
correcting defects and source code 
comprehension, you should also be observant 
of poor software design in the source code. 
Fowler [2000] refers to these as bad
smells.

### Slide 8

What is “Code Smell”?
8
Watch the code smell video on LMS

### Slide 9

Some “Bad Smell” Code Patterns
Cloning
(Duplicate Code)
Complex Structures
- Long methods
- Large classes
Variables and Parameters
- Long parameter list
- Feature envy
- Data clumps
- Primitive obsession
- Temporary field
Control structures and 
Polymorphism
- Switch statements
- Refused bequest
- Alternative classes with 
different interfaces
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test 
case
Identifying 
refactoring 
opportunity

### Slide 10

Smell Code Pattern #1 –
Cloning/Duplicate Code
- Causes
- Multiple programmers
- Unaware their colleague has already written similar code
- Purposeful duplication
- Rushing to meet deadlines with copy and paste
- Why is it a bad smell?
- If you find a bug in the original, you have to fix all the clones as well
Cloning
(Duplicate Code)
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 11

Smell Code Pattern #1 –
Cloning/Duplicate Code
- Refactoring Technique: Extract Method
- Create a new method that encapsulates duplicated code
- Replace code clones with method call
Cloning
(Duplicate Code)
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 12

Smell Code Pattern #2
Large Class
- Causes
- Small classes can get bloated over time as 
the program grows
- Why is it a bad smell?
- The class may become a non-realistic OO 
model, e.g. has phone details as part of the 
professor class
- May have responsibility confusion
Complex Structures
- Long methods
- Large classes
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 13

Smell Code Pattern #2
Large Class
- Refactoring technique: Extract class
- Create a new class
- Move the fields and methods responsible for the relevant functionality into the new class
Complex Structures
- Long methods
- Large classes
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 14

Smell Code Pattern #3
Feature Envy
- Causes
- Indication of a method that was incorrectly placed in the wrong class
- Why is it a bad smell?
- Indicates an abstraction fault or sometimes may indicate the method was 
incorrectly placed in the wrong class
Variables and 
Parameters
- Long parameter list
- Feature envy
- Data clumps
- Primitive obsession
- Temporary field
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 15

Smell Code Pattern #3
Feature Envy
Refactoring Technique: Move Method
- Move the method with feature envy to the class containing the most frequently 
used methods and data items
Variables and 
Parameters
- Long parameter list
- Feature envy
- Data clumps
- Primitive obsession
- Temporary field
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 16

Smell Code Pattern #4
switch statements
- Causes
- The cases in a switch statement contain logic for different 
types of instances of the same class
- In object-oriented code, this indicates new subclasses should 
be created
- Why is it a bad smell?
- The same switch/case structure appears in many places
Control structures and 
Polymorphism
- Switch statements
- Refused bequest
- Alternative classes with 
different interfaces
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 17

Smell Code Pattern #4
switch statements
Refactoring technique: Extract subclass & Extract 
Method
- Create new subclasses
- Extract method to move case block logic into 
methods on the new subclass
- Use polymorphism to substitute the switch block
Extract 
Subclass
Control structures and 
Polymorphism
- Switch statements
- Refused bequest
- Alternative classes with 
different interfaces
Commit 
refactoring Run test Apply refactoring
Plan 
refactoring
Create test case
Identifying 
refactoring 
opportunity

### Slide 18

AGENDA Requirement 
Specification
Analysis and 
Design
Deployment
Maintenance
Testing
Implementation
-Overview of Software Maintenance
-Type of Maintenance Activities
-Refactoring

### Slide 19

Summary
TLM3004 20
Software Maintenance 
- Maintenance Cost Estimation
- Four types of Maintenance Activity
Software Refactoring
- Process 
- Bad smell code patterns
- Refactoring techniques
- sourcemarking.com and 
refactoring.guru

### Slide 20

https://societysbackend.com/p/devin-has-exposed-software-engineers

### Slide 21

This week’s lab 
- There is no lab exercise nor lab submission
- Use the time to work on your group project
- Prepare for your presentation next week – wireframe for all use cases


---

## Week 11 (Part 2): Software Configuration Management

### Slide 1

SOFTWARE CONFIGURATION MANAGEMENT
A/P Indri Atmosukarto
Indriyati@singaporetech.edu.sg
Question / Comments?
1

### Slide 2

Recap – W8 Component Diagram and Intro to Software Design

### Slide 3

Recap – W9 Software Architecture & Detailed Design

### Slide 4

- Non-Execution based testing: walkthrough, inspection
- Execution based testing:
- Black Box – based on specification only
- Equivalence partitioning
- Boundary value analysis
- Decision Tables
- White Box – looking into the code – Control Flow Testing
- All are limited to specific test-cases
Recap – W10 Software Testing

### Slide 5

For your project:
- Select a feature / method you want to test. Provide a description of the method/feature
- Create the decision table, (and reduce if applicable)
- Provide the test cases that corresponds to the decision table
Recap – W10 Software Testing – Decision Table

### Slide 6

Recap – W10 Software Testing - White box Testing

### Slide 7

For your project:
- Select a different feature / method you want to test. Provide a description and 
pseudocode of the method/feature
- Construct CFG and calculate cyclomatic complexity
- Show basis path and provide test cases to cover path
Recap – W10 Software Testing – Whitebox testing

### Slide 8

SO FAR THIS WEEK 
Software Configuration Management
Software Configuration Management- Video

### Slide 9

OVERALL AGENDA
-Overview of Software Configuration Management
-Configuration Item Identification
-Change Management
-Version Management
-System Building
-Release Management
9
Pre-recorded video

### Slide 10

Overview of Software Configuration 
Management
Change 
Control
Version 
Management
System 
Building
Release 
Management
- Keeping track of 
change requests
- Working out the 
costs and impact of 
changes
- Deciding changes
- Keeping track of 
multiple versions
- Preventing 
interference
- Assembling program 
components, data 
and libraries
- Compiling
- Preparing for 
external release
- Keeping track of 
released versions
10

### Slide 11

Change Control
Change Control is intended to ensure that 
- system evolution is a managed process 
- priority is given to the most urgent and cost-effective changes.
It is concerned with 
- analyzing the costs and benefits of proposed changes, 
- approving those changes that are worthwhile
- tracking which components in the system have been changed. 
11

### Slide 12

Change Control Process
Submission of 
Change Request 
Technical and 
business 
evaluation and 
impact analysis
Approval by 
Change Control 
Board (CCB)
Engineering 
Change Order 
(ECO) is 
generated stating
Configuration 
Items checked out
Changes made 
and reviewed
Configuration 
Items checked in
12
Submission
Decision
Commitment & Evaluation

### Slide 13

Factors of Change Analysis
- The consequence of not making the change
- The benefits of the change
- The number of users affected by the change
- The cost of making the change
- The product release cycle
13

### Slide 14

Identify items for 
change
Submit CR
CR
Complete
Change Analysis
Inform Requester
CR 
Feasible?
Assign Developer
Implement Change
Verified
Ok? BASELINE
YES
YES
YES
NO
NO
Change Required
NO
14

### Slide 15

Change Management
- Change requester completes all boxes in Section A and passes to Project Manager
- Project Manager arranges investigation of 
request, depending on outcome request rejected, or given a priority and cost, and 
with investigator completes Section B & C.
- Form is then retained in project files.
- Once change is implemented, Section D is 
signed-off
15

### Slide 16

OVERALL AGENDA
-Overview of Software Configuration Management
-Configuration Item Identification
-Change Management
-Version Management
-System Building
-Release Management
16
Pre-recorded video

### Slide 17

Version Management
- Process of keeping track of different versions of Configuration Items
- It also involves ensuring that changes made by different developers to 
these versions do not interfere with each other
- Resolve Conflicts
- Enable Collaboration
17

### Slide 18

Version Management - Terminology
-
18
- A configuration item at one point in its development. It differs in 
some way from other itself at another point. 
- A version has revisions and variants
Version
- A configuration item linked to another via revision-of relationship, 
and ordered in time Revision
- functionally equivalent versions, but designed for different settings, e.g. Variant hardware and software
- A shared database of versions of configuration item and metaRepository information about changes to these items.
1.2 1.3 1.4

### Slide 19

Version Management - Terminology
-
19
- An isolated and private environment where a developer can work (edit, 
change, compile, test) without interfering and affecting other developers
- Examples: Local directory under version control, Private workspace on the 
server
Workspace
- An action of copy items from repository to workspace
Check out
Check in - An action of copy items from workspace to repository 
- The creation of a new work flow from a existing version. The new work flow Branching and the existing one may then develop independently. 
Merging - Combining the changes to a file simultaneously made by different users

### Slide 20

Version Management
Base() {….}
Base() {….}
feature A(){….}
Base() {….}
feature A(){….}
feature B(){….}
Base() {….}
feature A(){arg}
feature B(){….}
feature C(){….}
Base() {….}
feature A(){….}
Base() {….}
feature A(){arg}
DEV
V1.0
V2.0
V2.0
V3.0
V2.1
V2.2
branch
20

### Slide 21

OVERALL AGENDA
-Overview of Software Configuration Management
-Configuration Item Identification
-Change Management
-Version Management
-System Building
-Release Management
21
Pre-recorded video

### Slide 22

System Building
- System building is the process of creating a complete, executable
system by compiling and linking the system components, external 
libraries, configuration files, etc.
22

### Slide 23

OVERALL AGENDA
-Overview of Software Configuration Management
-Configuration Item Identification
-Version Control System
-Change Management
-Version Management
-System Building
-Release Management
23
Pre-recorded video

### Slide 24

Release Management
- The formal distribution of an approved version
- An instance of a system which is distrusted to users outside of the 
development team
- It is usually possible to identify two types of release
- Major Release which deliver significant new functionality
- Minor Release which repair bugs and fix customer problems that have been 
reported
24

### Slide 25

Release Management
- As well as the executable code of the system, a release may also 
include:
- Configuration files defining how the release should be configured for 
particular installations;
- Data files, such as files of error messages, that are needed for successful 
system operation;
- An installation program that is used to help install the system on target 
hardware;
- Electronic and paper documentation describing the system;
- Packaging and associated publicity that have been designed for that release
25

### Slide 26

Release Management
- Version distributed to the 
public
- Track history of releases
- May include additional config 
items (Installer, Config, How-To 
files)
- Enable development of 
hotfixes
- EG. Branch from Master, fix 
something, Merge back to 
Master (release and hot-fix 
versions)
26
Good() {….}
Bad(){.bug.}
Good() {….}
Bad(){}
Good() {….}
Bad(){.bug.}
Good() {….}
Bad(){.fix.}
Master
V2.0
V2.1
f2.0
f2.1
branch

### Slide 27

Version and Release Management
- Both change and version management are common features you can 
get from Version Control Systems (VCS)
- You’ll find change management in many places
27

### Slide 28

Version Control System
- Plenty of videos available on the workflow for various Version Control 
Systems
- GitHub is a popular system that is regularly used
- Includes features from Trello for project management
- It is free for us to use with a suitable number of features
- Can declare public and private projects
https://github.com/pricing 28

### Slide 29

Version Control System - Git Workflow
https://www.youtube.com/watch?v=3a2x1iJFJWc
add Commit
Commit -a
Push
Fetch
Merge
Pull
diff Head
diff
Clone
Workspace
(local directory)
Index
(stage)
Local repository
(HEAD) Remote Repository
For more details, refer to 
GIT tutorial

### Slide 30

Continuous Integration
31

### Slide 31

Integration Hell
The term integration hell refers to a situation where a software developer 
spends more time trying to re-integrate altered source code into a software 
system than they did creating the new feature in the first place. 
[Fowler,2006]
32

### Slide 32

Continuous Integration 
Continuous Integration is a software development practice where members of a team 
integrate their work frequently, usually each person integrates at least daily. 
Each integration is verified by an automated build (including test) to detect 
integration errors as quickly as possible.
The term was first used by Grady Booch in 1994. 
33

### Slide 33

Integration Frequency
34
Figure: divergence between trunk and feature branches over time
VS

### Slide 34

35
Continuous Integration 
https://developers.redhat.com/blog/2017/09/06/continuous-integration-a-typical-process/

### Slide 35

Summary 
- SDLC with CI/CD 
- The software development life cycle (SDLC) consists of several key stages: 
development, testing, deployment, and maintenance. CI/CD automates and 
integrates these stages to enable faster, more reliable releases. 
- When code is pushed to a git repository, it triggers an automated build and 
test process. End-to-end (e2e) test cases are run to validate the code. If tests 
pass, the code can be automatically deployed to staging/production. If 
issues are found, the code is sent back to development for bug fixing. This 
automation provides fast feedback to developers and reduces risk of bugs in 
production. 
Difference between CI and CD - Continuous Integration (CI) automates the build, test, and merge process. It 
runs tests whenever code is committed to detect integration issues early. This 
encourages frequent code commits and rapid feedback. 
- Continuous Delivery (CD) automates release processes like infrastructure 
changes and deployment. It ensures software can be released reliably at 
any time through automated workflows. CD may also automate the manual 
testing and approval steps required before production deployment. 
CI/CD Pipeline - A typical CI/CD pipeline has several connected stages:   - Developer commits code changes to source control   - CI server detects changes and triggers build   - Code is compiled, tested (unit, integration tests)   - Test results reported to developer   - On success, artifacts are deployed to staging environments   - Further testing may be done on staging before release   - CD system deploys approved changes to production 
36

### Slide 36

Four steps to Continuous Integration
37
CI Server 
Setup
Testing 
Automation
Building 
Automation
Repository 
Setup

### Slide 37

Step 1 : Source code repository
- Tools Example
- Rules
- Keeps track of every change in your codebase 
- If you can generate something, don’t store it in your repository
- Commit as much as possible
38
CI Server 
Setup
Testing 
Setup
Building 
Automation
Repository 
Setup

### Slide 38

Step 2 : Build Automation
- Common build tools 
- Makefiles, Ant, Maven
- shell scripts
39
System building is the process of creating a 
complete, executable system by compiling and 
linking the system components, external libraries, 
configuration files, etc.
CI Server 
Setup
Testing 
Automation
Building 
Automation
Repository 
Setup

### Slide 39

Step 3: Testing Automation
40
CI Server 
Setup
Testing 
Automation
Building 
Automation
Repository 
Setup

### Slide 40

Step 4: CI Server Setup
- Many products, but same functionalities 
- Define trigger
- E.g., Check-in, 12am everyday
- Keep developers informed of build result 
41
CI Server 
Setup
Testing 
Automation
Building 
Automation
Repository 
Setup
while true do
begin
 if trigger_happens then
 begin
 if not build then
 report_error;
 if not test then
 report_error;
 end;
 sleep;
end;
CI Server in Essence

### Slide 41

Continuous integration practices 
minimize the disruption caused by 
rapid, concurrent changes to 
software systems.
TLM3004 42

### Slide 42

SUMMARY
-Overview of Software Configuration Management
-Configuration Item Identification
-Change Management
-Version Management
-System Building
-Release Management
-Version Control System
43
Pre-recorded video

### Slide 43

SUMMARY
TLM3004 44
CHANGE MANAGEMENT CONTINUOUS INTEGRATION


---
