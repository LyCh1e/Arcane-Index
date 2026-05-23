# INF2004 Embedded Systems Programming — Lecture Notes
> Singapore Institute of Technology  
> Module Lead: Muhamed Fauzi Bin Abbas

---
## Table of Contents
1. [W0: Module Overview](#w0-module-overview)
2. [W1: Introduction to Embedded Systems](#w1-introduction-to-embedded-systems)
3. [W2: Requirements & Testing](#w2-requirements-testing)
4. [Interrupt Principles](#interrupt-principles)
5. [Timer & PWM](#timer-pwm)
6. [W5.1: Embedded Operating System (RTOS)](#w51-embedded-operating-system-rtos)
7. [W5.2: Finite State Machine](#w52-finite-state-machine)
8. [W6.1: Testing](#w61-testing)
9. [W6.2: Sensor Fusion](#w62-sensor-fusion)
10. [W8: Optimizations](#w8-optimizations)
11. [W10: Edge Computing](#w10-edge-computing)

---

# W0: Module Overview
*16 slides*

---

## Slide 1
Module Overview
INF2004 Embedded Systems Programming


## Slide 2
Who are we?
Lecture
• Muhamed Fauzi Bin Abbas
(Module Lead)
• fauzi.abbas@singaporetech.edu.sg
Lab Instructors
• Aw Kok Seng
(Lead Professional Officer)
• kokseng.aw@singaporetech.edu.sg
• Deric Ng
(Senior Professional Officer)
• deric.ng@singaporetech.edu.sg
• Paul Fong
(Adjunct Faculty)
• af_lee.kim.fong@singaporetech.edu.sg
• Kelvin Goh
(Adjunct Faculty)
• af_goh.soo.meng.kelvin@singaporetech.edu.sg
• Kang Liat Chuan
(Adjunct Faculty)
• af_liat.chuan.kang@singaporetech.edu.sg
Lab Manager
• Haja Mohideen S/O Packir Rowther
(Senior Assistant Manager)
• haja.rowther@singaporetech.edu.sg
Email header: [INF2004] xxxxxxx
compulsory


## Slide 3
Teaching Activities
• Lectures - 2 hours per week (via Zoom)
• Monday, 11.00 AM – 1.00 PM
• Laboratory – 2 hours per week starting from Week 1
Lab Group Day Timeslot Location Lab Instructors
P1 (SE) Wednesday 9 AM – 11 AM E2-05-14
Fauzi, Kelvin, Aw, Kang, Haja
P2 (SE) Wednesday 9 AM – 11 AM E2-05-05
P3 (CSC) Wednesday 11 AM – 1 PM E2-05-14
Fauzi, Kelvin, Aw, Kang, Haja
P4 (CSC) Wednesday 11 AM – 1 PM E2-05-05
P5 (IS-DCO) Monday 4 PM – 6 PM E2-05-14
Fauzi, Kelvin, Aw, Fong, Haja
P6 (IS-DCO) Monday 4 PM – 6 PM E2-05-05
P7 (AAI) Thursday 9 AM – 11 AM E2-05-14 Aw, Ng, Haja
Week 8: No Lab
Week 9: 2PM – 6PM


## Slide 4
How are the Lectures conducted?
TLDR; We flip you then we guide you. ☺


## Slide 5
How are the Lab sessions conducted?
We guide you... Then we test you. :P


## Slide 6
How are the Project work conducted?
Own Time, Own Target for six weeks with check-ins.


## Slide 7
How are you Assessed?
• Lecture Quiz (30%)
• Test your understanding of the lecture concepts.
• xSITe-based quiz, i.e. mcq, fill in the blanks, etc
• Conducted in Week 12.
• Each week, a topic quiz will be released, and you can attempt it unlimited times, and it is not graded. It will randomly pick
from a set of 5 questions.
• In Week 12, you will have ONLY 1 attempt to sit for the quiz that will comprise all topics (questions randomly picked) and
be graded. 100 Questions in 30 minutes!
• There will be a notification on xSITe if the question pool is updated.


## Slide 8
How are you Assessed?
• Lab Assignments (15% = 3% x 5)
• Test your knowledge based on your lab sessions.
• Submit a mini code assignment for each lab session.
• Hands-on Lab Test (20%)
• 90 mins individual in-person programming test in
Week 12 (TBC)
• Group Project (35%)
• Test your ability to work on a complex project
• Team comprised of 4-5 students
• Team members must be within the same timeslot sessions
• Six grading stages:
• Requirements + Design (Report)
• Driver Demo (Demo)
• Test Plan (Report)
• Partial Integration (Demo)
• Final Report (Report)
• Final Run (Demo)


## Slide 9
Assessment (in Summary)
Activities % Deadline Assessment Type
Lab Assignments 15% A week after each lab Submit a mini code assignment
Requirements & Design (Project) 5% Week 5 Submit a 3-5 pages document
Driver Demo (Project) 5% Week 6 (Lab Sessions) Demonstrate device driver
Test Plan + Traceability (Project) 5% Week 9 Submit a 3-5 pages document
Partial Integration (Project) 8% Week 10 (Lab Sessions) Demonstrate sub-components
Lecture Quiz 30% Week 12 (TBC) xSITe-based quiz
Hands-on Lab Test 20% Week 12 (TBC) Individual in-person programming test
Final Report + Test Result (Project) 2% Week 13 Submit a consolidated final report
Final Demo (Project) 10% Week 13 (Lab Sessions) Final Demo


## Slide 10
Additional Reference Materials
• Embedded C Coding Standard (https://barrgroup.com/embeddedsystems/books/embedded-c-coding-standard)
• Barr, Michael, and Anthony Massa. Programming embedded systems: with C and GNU
development tools. O'Reilly Media, Inc., 2006.
• C-programming (https://www.cprogramming.com/tutorial/c-tutorial.html)
• What is Unary Operator in C? (https://www.scaler.com/topics/unary-operator-in-c/)
• C Programming Language Tutorial. (https://www.geeksforgeeks.org/c-programminglanguage/)


## Slide 11
Reference Materials (Raspberry Pi Pico)
1. Official Raspberry Pi Pico Documentation: The official Raspberry Pi Foundation provides extensive
documentation on the Pico, covering topics from getting started to detailed hardware specifications.
(https://www.raspberrypi.org/documentation/rp2040/getting-started/)
2. Raspberry Pi Pico Datasheet: A detailed technical document outlining the hardware specifications and
capabilities of the RP2040, the microcontroller chip on the Pico.
(https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf)
3. Raspberry Pi Pico Python SDK: This is the official documentation for the MicroPython environment on the
Raspberry Pi Pico. It covers modules, functions, and other MicroPython-specific features.
(https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf)
4. Raspberry Pi Pico C/C++ SDK: For those who prefer to program in C or C++, the Raspberry Pi Foundation
provides an SDK for that too. (https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-c-sdk.pdf)
5. Pico Examples: The Raspberry Pi Foundation's GitHub repository contains a plethora of example projects and
code snippets to help users get started with the Pico. (https://github.com/raspberrypi/pico-examples)
6. Community Forums: The Raspberry Pi Foundation's forums and other online communities are invaluable
resources for troubleshooting, project ideas, and general discussions about the Pico.
(https://www.raspberrypi.org/forums/)


## Slide 12
Module Schedule
REQUIREMENTS
ADC
TIMER & PWM
DIGITAL COMMS
RTOS SENSORS FUSION
GPIO
EDGE
1 hour 1 hour 1 hour 1 hour
INTRO
(LABS) SENSOR FUSION + EDGE
W1
W2
W3
W4
W5
W6
INTERRUPTS
(LABS) GPIO + DIG. COMMS
DEBUGGING
(LABS) INTERRUPTS + TIMER
(LABS) ISSUE PICO + SETUP
TESTING
(LABS) PWM + ADC
Lecture (online) Lab Session (in Punggol)
(LABS) OPTIMISATION + DEBUGGING
PROJECT
W7 BREAK
PRACTICAL LAB TEST
W8
W9
W10
W11
W12
W13
PUBLIC HOLIDAY
FINAL DEMONSTRATION
CONSULTATION / SPECIAL TOPIC
DEVICE DRIVER DEMO
CONSULTATION / SPECIAL TOPIC
CONSULTATION / SPECIAL TOPIC OTOT
QUIZ
PARTIAL INTEGRATION DEMO
Wednesday, 19 Nov @ 2pm
OTOT
OTOT


## Slide 13
Microcontroller boards used in this module
Raspberry Pico W Raspberry Pico


## Slide 14
Ground Rules…
• We are here for those who want to learn
• Participate in lecture
• You have a question/doubt, whom better to ask than “yours truly” ☺
• Speak now or forever hold your peace…
• All queries should go to the discussion forum, especially if they are topic-related.
• This module has no exams (most of you asked for it during your video interview)
• We generally assess you on materials covered in lectures & lab sessions…
• Discussion is encouraged, BUT plagiarism will not be tolerated!
• Gen AI??
• How to write unique code?
• Please ensure your laptop is working before any assessment!
• I will not arrange make-up due to laptop/hardware failures.
• If you are unwell, get MC and submit it officially. If you missed any graded assessments, please email the
Module Lead (Fauzi) until you receive a response.
• If you have done a reasonably complex Embedded System project before, you may try to submit it as a
substitute for your project component. Please drop me an email, and we can discuss further. ☺
any time
assessments


## Slide 15
Updates
• Raspberry Pi Pico will only be loaned to you in the Week 1 Lab session.
• There will be a lab in Week 1 (this week)
• Project components will be entirely issued by Week 6.
• Please complete the survey questions
• This will help us, help you better.
• Please come for the labs on time (or earlier)
• If you are stuck in your project progress…
• Ask any of us for assistance.
• Keep asking us for help if you are lost/stuck/confused.
• Don’t be shy; everyone here has paid their school fees…
Email header: [INF2004] xxxxxxx
compulsory


## Slide 16
Permissions
• Students enrolled in this module automatically grant the Singapore Institute of Technology
the use of anonymised work submitted in this module. The usage of submitted work is
granted only for educational and research purposes, and the author’s identity of any work
will not be revealed or implied.
• Students who choose to withhold consent and not give permission for the usage of
anonymised submissions are to inform the Module Coordinator via email, before the start
of the second session of the module (Week 02).
• Students must seek Module Lead (Fauzi) permission before submitting any work that
came from this module for any competition, seminars, workshops, exhibitions, etc.


---

# W1: Introduction to Embedded Systems
*35 slides*

---

## Slide 1
Introduction to
Embedded Systems
Programming


## Slide 2
Embedded Systems?
https://www.flickr.com/photos/wilgengebroed/8249565455
Cyber-Physical Systems (CPS)
http://www.imm.dtu.dk/~jbjo/cps.html


## Slide 3
An Embedded System (ES) is ….
• a computing system that does a specific task
inside a machine or larger electrical system.
(Cambridge Dictionary)
• a computer system that is embedded into a
larger electrical or mechanical system
performing specific dedicated tasks of that
larger system. (Prof. Peter Waszecki)
• a controller with a dedicated function within a
larger mechanical or electrical system, often
with real-time computing constraints. (Wikipedia)
• a combination of computer hardware and
software, either fixed in capability or
programmable, designed for a specific function
or functions within a larger system.
(internetofthingsagenda.techtarget.com)
• …


## Slide 5
Analogue & Digital World
The human world is
analogue and continuous,
while the computer world
is digital and discrete.
Embedded systems must
use a mix of analogue and
digital electronics to
represent the corresponding
signals.


## Slide 6
Properties of Embedded Systems
• …are an embedded or integral part of a device, often
including hardware and electromechanical parts.
• ...are dedicated to handle specific tasks that are known
and assigned to them at design-time.
• …use sensors and actuators to interact with the real
world.
• …have strict timing constraints due to their interaction
with the physical world in a safety-critical environment.
• …use limited resources (e.g. memory, processing
power, power, etc.) compared to general-purpose
computers.
• …are based on microcontrollers (i.e. CPUs with
integrated memory and/or peripheral interfaces).


## Slide 7
Timing characteristics
Many embedded systems have real-time constraints…but what is real-time?
A real-time system is one in which the correctness of the
application depends on both their functional and temporal
results (the time at which the result is produced).
In other words, a late answer is a wrong answer.
Soft real-time constraints
▪ Tasks are allowed to miss deadlines
occasionally
▪ A late response can degrade the system
performance
▪ A missed deadline causes no significant
danger
▪ E.g., mobile phone, air-conditioning,
refrigerator
Non real-time constraints
▪ Tasks have no deadlines
A late response usually does not
significantly affect the performance and
functionality
▪ A late response causes no danger
▪ E.g., TV remote control, lawn sprinkler,
window lifter
Consequences of tasks missing their deadlines helps to classify real-time systems:
Hard real-time constraints
▪ It is imperative that tasks meets their
deadlines at all times
▪ A late response is not considered even if
its value is correct
▪ Missed deadline can have catastrophic
consequences
▪ E.g., nuclear reactor temperature, airbag controller, flight control system


## Slide 8
Different Embedded Systems Hardware Options
Microcontroller (µC) System on Chip (SoC) Application Specific
Integrated Chip (ASIC)
Microprocessor (µP) Digital Signal
Processor (DSP)
Field-Programmable
Gate Array (FPGA)
Graphics Processing
Unit (GPU)
Neural Processing
Unit (NPU)


## Slide 9
Microprocessor Microcontroller


## Slide 10
System on Chip (SoC)
Apple A16 Bionic
• Qualcomm - Snapdragon
• Samsung - Exynos
• Huawei - Kirin
• MediaTek - Dimensity, Helio
• Apple - A-series (e.g., A16
Bionic), M-series (e.g., M1,
M2)
• NVIDIA - Tegra
• Google - Tensor
• Broadcom - BCM series
(used in Raspberry Pi)
• Intel - Atom, Movidius
• AMD - Ryzen Embedded
• Rockchip - RK series
• Unisoc - Tiger series
• Allwinner - A-series
Other SoC


## Slide 11
Microcontroller SoC


## Slide 12
Evolution of Computing


## Slide 13
Edge-Fog-Cloud Architecture
Ref: Cao, Hung & Wachowicz, M. & Renso, Chiara & Carlini, Emanuele. (2019). Analytics Everywhere: Generating Insights From the Internet of Things. IEEE Access. 7. 71749-71769. 10.1109/ACCESS.2019.2919514.
Countless Billions Millions Thousands


## Slide 14
Why embedded software must be done right
Why It Matters:
• Ubiquity (Everywhere)
• Found in almost every device
• (e.g., washing machines, smartwatches, cars).
• Mission-Critical (Life or Death)
• Controls critical systems
• (e.g., pacemakers, airplane autopilots).
• Core Competency (Essential Skill)
• Companies rely on it for success
• (e.g., Tesla’s car software is as essential as its engines).
• Unique Challenges
• Works with limited memory, power, and must run without crashing
• (e.g., a car airbag must always respond instantly).
The Imperative for Excellence:
• Proactive Quality (Fix problems early)
• Don’t wait for errors to show up in real life. Test and catch
them during development.
• Example: A phone bug can be patched later, but a bug in
an airbag system must be fixed before the car is sold.
• Rigorous Standards (Follow strict rules)
• Use proven methods, safety checks, and certifications to
ensure reliability.
• Example: Airplane software follows aviation standards
(DO-178C) to guarantee safety before flights.
Embedded software is the "hidden brain" inside devices we use daily. It makes things work properly, from phones
and cars to medical equipment and airplanes. Its pervasive nature means that its quality directly impacts safety,
reliability, and business success.


## Slide 15
One Software Mistake Is All It Takes
Ref: https://www.simscale.com/blog/nasa-mars-climate-orbiter-metric/
http://www.b737.org.uk/mcas.htm
• Poorly designed software can severely damage a brand's
reputation and could lead to the company's collapse


## Slide 16
Embedded Software: More Than Just Code
Embedded software development presents unique and
significant challenges that differentiate it from traditional
desktop or web application development. The tight integration
with hardware and stringent performance requirements demand
a specialised approach.
Key Challenges:
• Resource Constraints
• Real-Time Requirements
• Hardware-Software Co-Design.
• Concurrency and Interrupts.
• Reliability and Safety.
• Debugging Difficulties.
Many embedded systems are mission-critical, performing
functions where failure is unacceptable and can lead to:
• Safety Risks
• Significant Financial or Business Loss


## Slide 17
The Deadly Race Condition: A Therac-25 Case Study
• The Bug:
• Race condition between UI and control software
• triggered by a specific sequence of rapid keystrokes
• causing lethal radiation overdoses instead of therapeutic doses.
• Reproduction Difficulty:
• A “Heisenbug” (disappeared when observed)
• debugger or logging altered timing, preventing the issue from manifesting.
• Took years and multiple deaths to identify the exact cause.
• High Cost of Failure:
• At least six lethal overdoses, deaths, and severe injuries.
• Multiple lawsuits, reputation damage, complete software redesign, and new safety protocols.
• Immense financial cost (recalls, legal fees, lost business) and immeasurable human cost.
https://web.stanford.edu/class/archive/cs/cs240/cs240.1236/old//sp2014/readings/therac-25.pdf


## Slide 18
The Systemic Flaw:
Toyota's Spaghetti Code Issue
Safety Concerns:
The entangled nature of the code
created an environment where a
small change in one area could have
unintended and potentially
dangerous consequences in another.
https://www.safetyresearch.net/toyota-unintended-acceleration-and-the-big-bowl-of-spaghetti-code/
Toyota's car software is famously difficult to maintain and debug due to its unstructured design, a style
known as "spaghetti code“. This complexity posed a significant obstacle during investigations into unintended
acceleration incidents, making it challenging to pinpoint the source of the problem.
Complexity:
The code was a monolithic,
interconnected block without clear
modularity, making it difficult to isolate
and fix bugs.
Debugging Challenges:
Engineers struggled to trace the flow of
logic and identify the source of errors,
leading to prolonged and costly
investigations.


## Slide 19
The Ariane 5's Fatal Integer Overflow
A classic and well-documented example of a single line of code
leading to catastrophic failure is the Ariane 5 rocket crash.
The rocket, which was carrying a payload worth half a billion
dollars, was destroyed just 37 seconds into its maiden flight.
The root cause was a software bug in the onboard inertial
reference system.
The "Bad Line" of Code: The software was written to handle a
64-bit floating-point number representing the horizontal velocity
of the rocket and convert it to a 16-bit signed integer. The
original code was reused from the Ariane 4 rocket, which had a
much slower flight profile.
During the Ariane 5's ascent, the horizontal velocity value was
larger than what a 16-bit integer could hold, resulting in an
integer overflow.
The specific line of code that failed was:
B_H = (float) H_O / 65536.0;
The value of B_H was stored in a variable that was too small.
This single line of code, which failed to perform a simple range
check, led to a chain of events:
1. The overflow caused a crucial variable to hold a
nonsensical value.
2. The flight control system interpreted this garbage data as
a severe error.
3. The system, believing it was in a critical fault state, shut
down the rocket's engines, causing it to veer off course
and self-destruct.
The cost of this one line of code was half a billion dollars and a
major setback for the European space program.


## Slide 20
What is the SDLC?
STRUCTURED APPROACH TO
SOFTWARE DEVELOPMENT
ENSURES REPEATABILITY AND
QUALITY
CRITICAL IN EMBEDDED SYSTEMS
DUE TO SAFETY, TIMING, AND
RESOURCE CONSTRAINTS


## Slide 21
Waterfall Development Cycle (MODEL)
REQUIREMENT
ANALYSIS
SYSTEM DESIGN
ARCHITECTURE
DESIGN
MODULE DESIGN
IMPLEMENTATION
TESTING
DEPLOYMENT &
MAINTENANCE
Product
Requirements
Software
Requirements
High Level
Design
Detailed
Design
Source
Code
Production
System
• Effective for well-understood domains
• Works best if you don’t make many big mistakes
• Any problem encountered requires backtracking


## Slide 22
Verification and Validation
Development Cycle (V-MODEL)
REQUIREMENT
ANALYSIS
SYSTEM DESIGN
ARCHITECTURE
DESIGN
MODULE DESIGN
IMPLEMENTATION
ACCEPTANCE
TESTING
SYSTEM TESTING
INTEGRATION
TESTING
UNIT TESTING
USER ACCEPTANCE TEST PLAN
& RESULTS
SYSTEM TEST PLAN
& RESULTS
INTEGRATION TEST PLAN
& RESULTS
UNIT TEST PLAN
& RESULTS
PRODUCT
REQUIREMENTS
SOFTWARE
REQUIREMENTS
HIGH LEVEL
DESIGN
DETAILED
DESIGN
‘TECHNICAL’
PRODUCT
INTEGRATION
TEST RESULT
UNIT TEST
RESULT
SOURCE
CODE • Emphasizes traceability


## Slide 23
Embedded vs General Software Engineering
Embedded General
Runs on resource-constrained microcontrollers or
SoCs
Runs on general-purpose computers with
abundant resources
Updates may require physical access or re-flashing
devices
Updates and patches can be deployed easily
Tightly coupled with hardware; resources managed
manually (hw/sw co-design)
Abstracted from hardware; OS handles resource
management
Focus on timing constraints, power consumption,
and reliability
Focus on performance, scalability,
maintainability
Tools often specific to MCU vendor and hardware Wide choice of development tools and
environments
Testing often on target hardware under real
conditions (more complex)
Testing mainly in simulated or virtual
environments


## Slide 24
Embedded
Constraints
Memory and processing limits
Timing and real-time deadlines
Hardware coupling
(specific MCU/peripheral sets)
Environmental constraints
Limited debugging visibility
(no full OS-level tools).
etc…


## Slide 25
Lessons from 50+ Years of SW DEV
Dividing up into
subsystems is critical Bad architecture will doom a project.
Process formality is a
good investment
Traceability, formal reviews, etc.
Skipping steps costs more in the end.
Requirements change Suggests using an iterated approach.
Finding bugs early is
important
Traceability from high to low levels.
Layered testing.
Peer reviews most cost effective for this.


## Slide 26
Mold Before the Gold:
Sniffing Out Bugs early
Product Testing
Software Testing
Code Peer Review
Design Peer Review
BUGS
The remaining bugs must be
swatted here; expensive to
resolve and might be too late.
Majority of the bugs
should be caught here;
cheaper to resolve
SOFTWARE
FAILURES
or else….


## Slide 27
Building an Embedded System Application
https://xkcd.com/303/


## Slide 28
HARDWARE
MACHINE LANGUAGE
ASSEMBLY LANGUAGE
HIGH-LEVEL LANGUAGE
FORTRAN C PASCAL
Low-level languages for different ES H/W
Assembly vs Machine Code: https://www.youtube.com/watch?v=Mv2XQgpbTNE
• Low-level language
• good for squeezing the best performance from the underlying hardware
• compact and more optimised code
• High-level language required to improve:
• Productivity
• Code abstraction
• Portable
• Only a machine understands low-level language
• need a compiler to translate the high-level language


## Slide 29
Assembly vs C
AssemblyC
str fp, [sp, #-4]!
add fp, sp, #0
sub sp, sp, #12
mov r3, #6
str r3, [fp, #-8]
ldr r3, [fp, #-8]
add r3, r3, #5
str r3, [fp, #-8]
mov r3, #0
mov r0, r3
add sp, fp, #0
ldr fp, [sp], #4
bx lr
int add() {
 int a = 6;
 a = 5 + a;
 return 0; }
mov r3, #6
add r3, r3, #5
ARM
GCC 8.2


## Slide 30
C/Assembly Code into Binary File
LINKER
Binary File
(.bin)
Object Files (.o) Linker Script (.ld)
Object Files (.o)
Assembly Files (.s)
C Files (.c)
assembler
compiler
Startup Code (crt0.s)
Reset Code (reset.s) Memory
Loader /
Locator
C Library (.a) / C-SDK


## Slide 31
Compiler / Assembler
• Compiler
• Translate programs written in human-readable language into an
equivalent set of opcode for a particular processor
• Cross compiling - compiling on a host for a target platform
• Native compiling - compiling for the same architecture you're running under
• Example: GCC, KEIL, IAR, CCS, etc.
• Assembler
• One-to-one translation
• https://www.youtube.com/watch?v=Mv2XQgpbTNE
cross compiling


## Slide 32
C/Assembly Code into Binary File
LINKER
Binary File
(.bin)
Object Files (.o) Linker Script (.ld)
Object Files (.o)
Assembly Files (.s)
C Files (.c)
assembler
compiler
Startup Code (crt0.s)
Reset Code (reset.s) Memory
Loader /
Locator
C Library (.a) / C-SDK


## Slide 33
Startup code
• A small block of assembly language code that prepares the way for the execution of
software written in a high-level language.
• Most cross-compilers for embedded systems include an assembly language file called
startup.asm or crt0.s (short for C runtime).
• Typical startup code:
• Disable interrupt
• Copy data into RAM
• Zero uninitialized data area
• Allocate space and initialize the stack
• Create and initialize the heap
• Enable interrupt
• Call main


## Slide 34
C/Assembly Code into Binary File
LINKER
Binary File
(.bin)
Linker Script (.ld)
C Library (.a) / C-SDK
Object Files (.o)
Object Files (.o)
Assembly Files (.s)
C Files (.c)
assembler
compiler
Startup Code (crt0.s)
Reset Code (reset.s) Memory
Loader /
Locator


## Slide 35
Linker
• takes one or more object files generated by a compiler/assembler
and combines them into a single executable file.
• cross-file dependencies are resolved properly, e.g. if you define a variable/function
in one .c file, and use it in another .c file, the linker connects the two together.
• link `reuse’ library files; static and dynamic
• every link is controlled by a linker script, that describes how the executable are mapped
onto the memory during execution.


## Slide 36
Prof, Explain It to Me in Plain English
The C SDK (Software Development Kit) for
the Raspberry Pi Pico provides a collection
of libraries, functions, and tools that simplify
hardware interaction. It abstracts the lowlevel details of the microcontroller, allowing
the user to focus on writing high-level
application code. The SDK offers pre-written
code to manage peripherals, such as GPIO,
PWM, UART, and others.
Similar Terms:
• Application Programming Interface (API)
• Development Framework, e.g. Arduino
• Board Support Package (BSP)
• Toolkit / Toolchain
• Middleware
• Library
The compiler is a tool that translates the user's
C source code into machine code (binary) that
the Raspberry Pi Pico can understand. The
compiler processes the source code, linking it
with the necessary libraries from the C SDK,
and generates an executable binary file. This
binary file is typically in the form of a .uf2 or .bin
file.
The bootloader is a small program pre-installed
on the Raspberry Pi Pico. It is responsible for
loading the compiled binary into the
microcontroller's flash memory and executing it.
When the Raspberry Pi Pico is powered on or
reset, the bootloader checks for the presence of
a new binary file (e.g., via USB) and writes it to
flash memory if found. If no new binary is
detected, it simply runs the existing program
stored in flash.
C SDK Compiler Bootloader
COMPILER
C SDK
SOURCE
CODE
.UF2
BOOTLOADER/
DEBUGGER


---

# W2: Requirements & Testing
*12 slides*

---

## Slide 1
Requirements & Testing in
Embedded Software Development


## Slide 2
Why Clear Requirements Matter
Defines 'What' The
Software Must Do
(Not 'How')
Prevents Costly
Redesign
Must Include Hardware
Specifications, Realtime Constraints, Safety
Requirements.
Traceability To Tests
Ensures Validation.
… in Embedded Systems


## Slide 3
The Art of Requirements: Spectrum of Detail
Transmit a reading every minute.
Transmit an encrypted sensor reading every 60 ±1 s, with a minimum
end-to-end reliability of 99%.
Transmit a 32-bit floating-point sensor reading every 60 ±1 s via TLS 1.3 encryption using a 2048-bit RSA
certificate, serialised in a JSON object with the key 'timestamp' (Unix epoch) and 'value', and implement
a three-attempt retry mechanism with an exponential backoff of 1, 2, and 4 seconds upon transmission
failure.
Send readings regularly


## Slide 4
Why This Matters: Traceability
REQUIREMENT: THE
"WHAT" THE SYSTEM MUST
DO.
DESIGN: THE "HOW" THE
SYSTEM WILL MEET THE
REQUIREMENT.
TESTING: THE VALIDATION
THAT THE "WHAT" AND
"HOW" WERE CORRECTLY
IMPLEMENTED.
A well-written requirement is the cornerstone of a structured development process. It enables
traceability, which is the ability to follow a requirement through every stage of the lifecycle.
Without a clear and measurable requirement, there can be no definitive design or test case, making
it impossible to prove that the system performs as intended.


## Slide 5
◼ Anti-Patterns:
⚫ Requirements aren’t written down
⚫ Requirements incomplete, imprecise
⚫ “Be like last version, except…”
◼ Requirements
⚫ Requirements faults can defeat a
design before it is even built
⚫ Describe what system does
– Also what it’s not supposed to do
⚫ Precise, testable language
– Each requirement traces to system test
Requirements Overview
◼ 2005:
$170M
FBI Virtual Case
File project
terminated
◼ Requirements issues:
⚫ Requirements not defined when
development contract signed
⚫ “We will know it when we see it”
⚫ Repeated requirements changes
⚫ Scope creep (new requirements
added) of 80%


## Slide 6
Characteristics of
Good
Requirements
• Precise, concise, and minimally constrained
• States what the system must do, not how to do it
• Uses consistent terminology
Clear & Focused
• Written with “shall” (mandatory) or “should” (advisory)
• Where possible, includes numeric targets with tolerances (e.g., 500 ms
±10%, less than X)
• Requirement satisfaction can be tested with a clear yes/no outcome
Verifiable
• Each requirement has a unique id (e.g., R-7.3)
• Cleanly maps to a test
Traceable
• Supported by rationale or commentary
• Fits within the overall system context
• Conflicting requirements are resolved or prioritised
Justified & Coherent


## Slide 7
Problematic
Requirements
• The system must display the current room temperature on the LCD.
Untraceable (no label)
• R-1.1: The thermostat shall always maintain a comfortable room temperature.
Untestable
• R-1.2: The display should be easily readable.
Imprecise
• R-2.1: The system shall update the temperature reading every 2 seconds.
No measurement tolerance
• R-3.1: Pressing the 'up' button shall increase the target temperature, and pressing
the 'down' button should decrease it, but if the temperature is at its maximum,
pressing the 'up' button should instead turn on the backlight, which can also be
turned on by pressing and holding the 'mode' button for 3 seconds.
Overly complex
• R-4.1: The system shall read the temperature from the LM35 sensor via the I2C
bus and store the value in a signed 16-bit integer before displaying it on the LCD.
Describes implementation


## Slide 8
NON-Functional
Requirements
• System-level qualities, not tied to a single component
• Examples: performance, reliability, dependability
• Often verified at the overall system boundary
1. Emergent Properties
• Throughput, latency, response time
• Real-time deadlines and scheduling guarantees
2. Performance & Timeliness
• Negative requirements (“system shall not …”)
• Safety mechanisms to prevent or mitigate hazards
• Many behaviours are emergent and require system-wide assurance
3. Safety, Security & Dependability
• Size, Weight, and Power consumption limits
• Allocated as a budget across subsystems
4. Resource Constraints
• Compliance with standards (e.g., ISO 26262, DO-178C)
• Mandated technology or platform choices
• Business constraints: cost ceilings, deadlines, staffing
5. Design & Project Constraints


## Slide 9
Product vs. Engineering Requirements
(Car Navigation System Example)
Product
Requirements
• Define what the customer wants
• Written in user language, focus on value
• Example:
• The system shall provide turn-by-turn driving
directions.
• The system shall recalculate the route if the
driver misses a turn.
• The system shall display maps that are easy to
read, day or night.
• The system shall provide estimated time of
arrival (ETA) to the destination.
• The system shall accept voice commands for
hands-free operation.
Engineering
Requirements
• Translate product needs into technical,
measurable terms
• Written for engineers to design and test
• Example:
• The GPS module shall provide position updates
at ≥1 Hz with accuracy of ±3 m.
• The system shall recompute a new route within 2
seconds after deviation detection.
• The LCD shall support brightness from 200–800
nits with automatic adjustment.
• The ETA shall be calculated using current GPS
speed and road segment data.
• The microphone and DSP shall support voice
recognition with ≥95% accuracy in 65 dB
ambient noise.


## Slide 10
REQUIREMENTS
APPROACHES
Text Document
Simple list of requirements
Works well if domain experts
Improves over time
UML Use Cases
Show activities performed by actors
Requirements expressed as scenarios attached to
each use case
Agile User Stories
Each story = one system interaction
Format: “As a [user], I want [goal], so that
[benefit].”
Functional
Decomposition
Start with main system functions
Break into detailed sub-functions
Builds a “functional architecture”
Prototyping
Customers knows when they see it
Paper mock-ups can help refine requirements


## Slide 11
Example of a Software Requirements
https://ntrs.nasa.gov/api/citations/20240011318/downloads/TM-20240011318.pdf


## Slide 13
Wrap-Up & Preview
• SDLC choice impacts cost, schedule, and quality
• Good requirements form the backbone of all models
• Clear, Concise, Correct, Coherent, Complete and Confirmable
• Next: Hands-on - Writing Embedded Requirements


---

# Interrupt Principles
*21 slides*

---

## Slide 1
Title: Interrupt principles
Lecturer: Professor Ian McLoughlin
Date: 2020-07


## Slide 2
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Professor Ian McLoughlin
ICT Cluster
Singapore Institute of Technology
General principles
of interrupts
Thanks to
Dr Muhamad Fauzi
A/P Yar Kar Peo


## Slide 3
SINGAPORE
INSTITUTE OF
TECHNOLOGY
What we will cover in this segment
● Types of interrupt
● Interrupt handling/vectors/servicing
● Advantages and disadvantages of interrupts
● Interrupts and polling
● Efficiency
● Interrupt configuration


## Slide 4
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Types of interrupt
● Something that interrupts the normal flow of program execution
● A signal that immediate action is needed
● For example:
● a computer reset button
● over-pressure sensor in nuclear reactor
● touch the screen on your smartphone
● a memory error, a floating point error
● Interrupts are good!


## Slide 5
SINGAPORE
INSTITUTE OF
TECHNOLOGY
The reset button
● When you press RESET, the processor stops what it is doing and restarts
from the beginning.
● You remember how a CPU runs a program, right?
1. Read instruction from program counter (PC)
2. Execute instruction
3. Increment PC
● So RESET sets the PC to a new value -
the reset interrupt vector


## Slide 6
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Interrupt vector table (IVT)
● Code 'jumps' to a fixed location in the IVT when any interrupt occurs
(for some kinds of reset other things also happen – see later).
● The programmer or operating system puts instructions at each
fixed vector location to handle the interrupt.
● Usually the code says “branch to an interrupt service routine”.
● There is one interrupt service routine (ISR)
for each kind of reset you want to handle.
● ISRs can be located anywhere in memory.


## Slide 7
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● This is the standard ARM Cortex-M4 IVT
● By default the “offset” is 0, so the bottom
of the table starts at 0x0000 0000
● Some interrupts happen because the
processor has detected an error, but
many are signals from things attached to
the CPU.


## Slide 8
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● Read about interrupts in my
Computer Systems book, section 6.5 (page 341):
Interrupts and interrupt handling
● As an example, let's learn how the
interrupt process happens typically...


## Slide 9
SINGAPORE
INSTITUTE OF
TECHNOLOGY
(Extracted from my book with small changes)
(1) Code is running normally (orange colour), until an IRQ occurs.
(2) The PC is saved, then set to the IRQ int. vect. address, so the
next instruction is the IVT (3).
(3) The IRQ interrupt vector says “branch to the ISR1”.
(4) The PC is set to the ISR1 address, causing a branch to there.
(5) The ISR runs, then the CPU returns to where it left off (i.e. the PC
is set to the old saved value) and
(6) the original program
continues (purple colour).


## Slide 10
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Interrupt Response
● For most interrupts you will program, before the CPU jumps to the IVT, it
automatically stores its context, including the current program counter
(PC) and status register (SR), maybe some more things too!
● This is so, after the interrupted is serviced, it can restore context and
return to where it left off.
● In many processors, the place where PC,
SR and other items get stored to
is a block of memory called the stack.


## Slide 11
SINGAPORE
INSTITUTE OF
TECHNOLOGY
The stack
● An area in RAM to store miscellaneous
things for a while, then retrieve them.
● The CPU can push things onto the stack,
and then must pop them off later (why?)
● The stack pointer (SP) is a register that
indicates the address of the last item put
into the stack.
0x786b3
0x01203
0x00000
0x00000
0x00000
0x00000
0x00000
0x00000
SP 0x786b3
0x01203
0xFFFFF
0xF1F0F
0x00000
0x00000
0x00000
0x00000
SP
Push two things
to the stack


## Slide 12
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Recap
● Something interrupts the normal flow of program execution
● The CPU responds by pushing current context to the stack then
● Branching to the interrupt vector table (IVT) which
● Branches to an interrupt service routine (ISR) which services the interrupt
● Then restores context (pops it from the stack) and
● Returns - resumes program execution


## Slide 13
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Interrupt or poll?
Imagine you have a peripheral that receives data packets from a 5G network. You
task is to process each received packet within 1ms of it arriving.
How to you get the data from the peripheral
to your program?
5G
peripheral
Data, CPU
Address
& control
bus
Your program
to handle data
packets in
t
e
rf
a
c
e


## Slide 14
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Polling
How to you get the data from the peripheral to your program?
Using polling: ask the peripheral “is there any
packet yet”. If the answer is no, wait a bit and
then try again. If yes, then process.
Repeat forever.
Data, CPU
Address
& control
bus
Your program
to handle data
packets in
t
e
rf
a
c
e
5G
peripheral
write
read


## Slide 15
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Interrupt
How to you get the data from the peripheral to your program?
Using interrupts: setup the interrupt controller to
'listen' to the peripheral's int signal. When the
interrupt occurs, handle it in an ISR.
Then go to sleep.
You'll be woken up when needed.
Data, CPU
Address
& control
bus
Your ISR
to handle data
packets in
t
e
rf
a
c
e
5G
peripheral
Interrupt
controller
int signal
read
write
wake


## Slide 16
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● Polling (also called busy-wait) wastes precious CPU time
● The worst case latency (timing delay) depends on the polling cycle
● Interrupts are more energy-efficient
● Interrupts are faster
Note: you don't have to put all your code in an
ISR. You could use the same program/function
you used for polling, and just tell the ISR to wake
up and run that code whenever a packet arrives.
Interrupts vs. Polling


## Slide 17
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Utilisation upolling=c/p uint=(h+c)/T
Polling period p must be >c and <T, and takes
p+c time (worst case) to process an event so,
polling constraints are:
For interrupts it's different;
time
c
p
c
Polling
time
Interrupt
c
h
Int signal
If T is the fastest time between events occurring, D is a deadline. p is polling period.
c is CPU time taken to handle an event, h is the hardware response time.
2c≤c+P≤D≤T
h+c≤D≤T


## Slide 18
SINGAPORE
INSTITUTE OF
TECHNOLOGY
More about interrupts
● ISR code should be tiny, fast and efficient. It should affect the rest of the system
as little as possible
● Interrupts are asynchronous and unpredictable when they will occur.
They can happen at any time (re-entrant?)
● Turn off (mask) interrupts you don't need –
but some are non-maskable interrupts (NMI)
● A modern micro has many on-chip peripherals.
Each can have several interrupt signals...
there could be hundreds!


## Slide 19
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Writing an ISR
● On exit from an ISR, leave the CPU in the same state it was at entry (i.e. same
context). CPUs automatically do some of this, but probably not everything.
● Before you exit an ISR, you usually have to clear the interrupt flag (otherwise
once you exit, it will be triggered again immediately).
● ISRs use global variables – you can't pass parameters to them.
● Some processes allow nested interrupts. Most
use interrupt priorities for cases when they
coincide.
● Never put an infinite loop into an ISR!


## Slide 20
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Interrupt confguration in software
● Usually we need to (1) write an ISR, (2) setup the interrupt vector table with the
ISR address/name, (3) enable the correct interrupt in the interrupt controller, (4)
configure the peripheral's interrupt behaviour and then (5) unmask the interrupt.
● Interrupts can be edge-triggered or level-triggered. If edge-triggered, it can be
on falling or rising edge.
● Interrupts are really diffcult to debug
Falling
edge
Rising
edge


## Slide 21
SINGAPORE
INSTITUTE OF
TECHNOLOGY
What we have covered in this segment
● Types of interrupt
● Interrupt handling/vectors (IVT)/servicing (ISR)
● Advantages and disadvantages of interrupts
● Interrupts and polling
● Efficiency
● Interrupt configuration
(e.g. edge/level sensitivity, masking)


---

# Timer & PWM
*18 slides*

---

## Slide 1
Title: Timer principles
Lecturer: Professor Ian McLoughlin
Date: 2020-07


## Slide 2
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Professor Ian McLoughlin
ICT Cluster
Singapore Institute of Technology
General principles
of timers
Thanks to
Dr Muhamad Fauzi
A/P Yar Kar Peo
A/P Ryan Fraser Kirwan


## Slide 3
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Contents
● Clock/timer technology and uses
● Real-time clock
● Clocks & timers in a microcontroller
● Watchdog timer
● Pulse-width modulation


## Slide 4
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Clock/timer technology and uses
● Almost all digital circuits are synchronous – they run in step to a clock
● Most processors contain multiple clock signals
● Clocks have very precise timing


## Slide 5
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● Digital circuits (like CPUs) consume
more power when they are clocked
faster
● Some can switch to a fast system
clock for performance, or a slow
system clock to save power
● (but the best way to save power is to turn off
unused CPU modules)
From Oletic & Bilas, “System-Level Power Consumption Analysis of the Wearable
Asthmatic Wheeze Quantification”, Journal of Sensors, Vol. 2018, Article 6564158


## Slide 6
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● CPUs have a precise system clock, usually generated internally with
the help of an external crystal oscillator or ceramic resonator
Clock
module
System clock
Memory clock
Peripheral bus clock
1s clock pulse
Microprocessor
● Inside the processor, divider circuits
generate multiple internal clocks
● The oscillator frequencies should generally
be an integer multiple of the internal clock


## Slide 7
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● Usually there one oscillator is for the main system clock e.g. 48MHz
● Main internal clocks usually derived from this, e.g. 24MHz, 12MHz, 6MHz
● Usually there is a real time clock (RTC) signal from a 32.768kHz crystal
● Why such a strange number?
0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1
MCLK
MCLK/8
count


## Slide 8
SINGAPORE
INSTITUTE OF
TECHNOLOGY
`
● Real-time clock – 32.768kHz signal, divided by 32768 to give a 1Hz signal.
● The RTC maintains an internal count of minutes, hours, days etc..
● Provides an OS with time/date information
for use with high level languages
● Might have a battery back-up
Real-time clock
Count to 32,768 (2 `
15 32.768kHz ) 1Hz
Watch crystal 15 divide-bytwo units
RTC


## Slide 9
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● We saw the clock circuitry already
● Timers are internal peripherals that count clock cycles to either:
(a) Measure the duration of something or
(b) Control something with regular timing
● Most processors have several timers. Each can
raise its own interrupt.
● They can be used for many different things,
e.g. precise timing in software, controlling a
peripheral or measuring a duration.
● Clocks & timers in a microcontroller


## Slide 10
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Example 1
● With a 48MHz clock, you could set a timer to raise an interrupt every time it counts to
48,000.
● That is 48,000 / 48,000,000 Hz = 0.001 s = 1ms a one millisecond timer
● You can program it to be one-shot or continuous
● A typical OS would implement a regular time tick in this way


## Slide 11
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Example 2
● A peripheral is connected to a GPIO pin. You need to give it an output signal like this;
● How would you do that?
● NOT like this; loop forever {
set_gpio_output_high;
sleep(0.013);
set_gpio_output_low;
sleep(0.013);
}
13ms 13ms
What you get
What you want


## Slide 12
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● You configure a timer to take its input from one of several clock sources
● A timer is a counter that runs up or down
● Down - you load it with a start value, then it
counts down to 0, one step for each clock cycle
● Up – starts at 0, counts up until it hits a target value
● You configure what happens when it hits 0 or target
● Each timer has a width in bits which limits its
maximum count value;
e.g. a 12 bit timer can only count down
from/up to a maximum value of 2047
More about timers
Time
Max
Time
Max
Start value
Target value
0
0


## Slide 13
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● You can set each timer to raise an interrupt when it hits its end point
(either zero or the configured target value), and then either;
● Stop (one-shot mode);
● Wrap around to the maximum (free running);
● Re-load with the same start value (periodic)
More about timers


## Slide 14
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● Like other timers, the WDT is driven from a configurable clock source, and counts
up from 0 to a configured target value.
● The difference with other timers is that when it hits target, it RESETs the CPU.
● The idea is: your software is supposed to periodically clear the WDT counter, so
the CPU only resets when your software stops running
● i.e. it protects against crashes
● Can be disabled, but may be turned on by
default after reset... don't forget about this!
● Essential for unattended systems.
Watchdog timer


## Slide 15
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● Used for motor control, LED brightness control and high power audio amplifiers
● Acts a bit like a poor man's DAC (digital to analogue converter). e.g.
● The pulse width is changing, not the frequency.
The duty cycle changes
Pulse Width Modulation (PWM)
GPIO
output
pin
100% brightness
50% brightness
25% brightness
10% brightness
off


## Slide 16
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● The programmer configures (a) the clock source, (b) the duty-cycle, and
(c) polarity. Once running, it continues stand-alone.
● It's all done with counters!
● e.g. setting period=10, duty_cycle=4, polarity=low gives this;
Clock source
Counter 0 1 2 3 4 5 6 7 8 9 10 0 1 2 3 4 5 6 7 8 9 10 0 1 2
PWM output
Actual duty cycle (%) = (period – duty_cycle)/period * 100
For this example it is (11 - 5)/11 = approx 55%
The count starts at 0, not 1


## Slide 17
SINGAPORE
INSTITUTE OF
TECHNOLOGY
● Although we draw clocks as perfect square waves, they aren't really perfect!
● They have rise and fall times (also ringing and jitter)
One fnal point to note
Voh
Vol
Tclk
thigh tlow
trtf
Clock frequency fclk=1/Tclk
Duty cycle DC = thigh/Tclk


## Slide 18
SINGAPORE
INSTITUTE OF
TECHNOLOGY
Maybe we should have called this “counters and clocks” instead? We looked at:
● Clock/timer technology
● Real-time clock (RTC)
● Clocks & timers in a microcontroller
● Watchdog timer (WDT)
● Pulse-width modulation (PWM)
What we have covered in this segment


---

# W5.1: Embedded Operating System (RTOS)
*28 slides*

---

## Slide 1
Embedded Operating System


## Slide 2
Agenda
• Introduction to Embedded Operating System → RTOS
• Internal workings of an RTOS
• Context Switches
• A few examples of Scheduling


## Slide 3
What is an Operating Systems
• An organized collection of software extensions
(or libraries) that serve to:
• control common routines
• Printing to terminal
• Allocating memory
• Access rights to a peripheral
• a standard environment for execution of programs across various
platform or processors


## Slide 4
Operating System Hierarchy
APPLICATIONS
OS USER INTERFACE
FILE AND DISK SUPPORT
OS KERNEL
HARDWARE
more complex
simple
Kernel on an embedded
processor implements the most
basic of OS functionalities
Extends the basic kernel
functionalities, e.g. UI,
network stack, etc.
This is typically found in fullfeatured commercial OS.


## Slide 5
Microkernel vs Monolithic Kernel
The user services and kernel services
are kept in separate address space.
Both user services and kernel services
are kept in the same address space.


## Slide 6
Difference Between Microkernel and Monolithic Kernel
BASIS FOR COMPARISON MICROKERNEL MONOLITHIC KERNEL
Basic In microkernel user services and
kernel, services are kept in separate
address space.
In monolithic kernel, both user services
and kernel services are kept in the same
address space.
Size Microkernel are smaller in size. Monolithic kernel is larger than
microkernel.
Execution Slow execution. Fast execution.
Extendible The microkernel is easily extendible. The monolithic kernel is hard to extend.
Security If a service crashes, it does effect on
working of microkernel.
If a service crashes, the whole system
crashes in monolithic kernel.
Code To write a microkernel, more code is
required.
To write a monolithic kernel, less code is
required.


## Slide 7
Why the need for Embedded Operating System
• OS is just a “collection” of commonly used libraries
• Common for applications to re-use existing code or libraries
• These libraries are common across most/all applications
• Typically these libraries have been tested and verified
• Share limited resources (e.g. processor, memory, etc)
• Schedule the various request for a shared resource
• Kernels used in desktop OS are often:
• Not modular (not configurable)
• Not fault‐tolerant (Not designed for mission‐critical applications)
• Resource hungry
• Timing uncertainty makes designing a real-time system challenging.


## Slide 8
What is an Embedded Operating Systems
• Minimal Embedded OS → OS Kernel
• An embedded system is designed for a single purpose (we talked about this in Lecture 1)
• Does not need a user interface and file access (most of the time)
• Only contain libraries that are necessary (reduce overhead)
• Configurability is important feature
• Embedded OS gives you control over your resources
• Every process is scheduled (no accidental runs)
• The timing behavior of the OS must be predictable
• Number of tasks is known (bounded)
• Embedded OS allows control over timing by
• managing the timing and scheduling
• being aware of deadlines and have mechanism to take them into account during scheduling
• providing precise timing services with a high resolution.
An Embedded OS that supports the construction of real‐time
systems is called a Real‐time Operating System (RTOS)


## Slide 9
Basic Functions of RTOS Kernel
Inter‐task communication
(queuing of request)
Support of real‐time clocks, timers, delays, etc.
Task synchronization (critical sections,
semaphores, monitors, mutual exclusion) Execution of “parallel” tasks on a
processor by scheduling them to
ensure fairness in sharing the
resources
Critical component in RTOS to
ensure the device works indefinitely
without needing a reboot, e.g.
memory leaks, memory
fragmentation, etc.
An embedded system comprises
of various components other
then the CPU and memory that
needs to be managed by the OS
as a resource.
Managing and servicing
real-time events


## Slide 10
One Binary to rule them all
HARDWARE
APPLICATION LIBRARIES
HARDWARE
OPERATING SYSTEM LIBRARIES
APPLICATIONS
single binary image
bare-metal OS-based


## Slide 11
One Binary to rule them all
HARDWARE
APPLICATION LIBRARIES
HARDWARE
OPERATING SYSTEM LIBRARIES
APPLICATIONS
HARDWARE
OPERATING SYSTEM LIBRARIES
APPLICATION APPLICATION
single binary image
multiple binary files
bare-metal OS-based OS-based


## Slide 12
Compiling Application for EOS
LINKER
Executable
Image File
(.elf/.axf)
Linker Script (.ld)
C
Libraries (.a)
Object Files (.o)
Object Files (.o)
Assembly Files (.s)
Application
C Files (.c)
assembler
compiler
SYSCALL
Libraries (.a)
Startup Code
(startup.s)


## Slide 13
Compiling Application for EOS
LINKER
Executable
Image File
(.elf/.axf)
Linker Script (.ld)
C
Libraries (.a)
Object Files (.o)
Object Files (.o)
Assembly Files (.s)
Application
C Files (.c)
assembler
compiler
SYSCALL
Libraries (.a)
Startup Code
(startup.s)


## Slide 14
Libraries vs System Calls
Library Routines
System Calls
Kernel
Applications


## Slide 15
A task goes through several states
during its life in a multitasking
system.
Tasks are moved from one state to
another in response to the stimuli
marked on the arrows.
Task States
READY
BLOCKED
RUNNING
TERMINATED
startup
pre-emption
task is deleted
task is deleted
task is
blocked
task
exits
task is placed in queue


## Slide 16
Task State Diagram
A task enters this state when it starts executing on
the processor. Only one task can be in this state in
the system at any one time.
State of tasks that are ready to execute but cannot as
the processor is assigned to another task, i.e. another
task has the state “running”.
A task enters the blocked state when it executes a
synchronization primitive to wait for an event,
e.g. a wait primitive on a semaphore or timer.
A task will only be removed
when it is explicitly deleted.
ready queue
READY
BLOCKED
RUNNING
TERMINATED
startup
pre-emption
task is deleted
task is deleted
task is
blocked
task
exits
task is placed in queue
run
block queue


## Slide 17
ready queue
block queue
READY
BLOCKED
RUNNING
TERMINATED
startup
pre-emption
task is deleted
task is deleted
task is
blocked
task
exits
task is placed in queue
run
Task State Diagram
If the “running” task needs I/O or needs a
resource that is currently unavailable, it is
inserted in a “blocked” queue when its waiting on
a semaphore. When its resource becomes
available, it goes back to “ready” and inserted
into the “ready queue”.
When the scheduler decides the current task has
had enough time on the processor, either because
it finished, its time slice is up or its being preempted, the “running" task is moved to the “ready
queue”. Then the first task on the “ready queue” is
selected to run.
Any tasks that are ready to run sit on the ready
queue. The queue may be prioritized so the most
important task runs next.


## Slide 18
Tasks vs Functions
• A function is a set of program instruction,
then exits and may return a value, e.g.
“process data”
• A task is a process that repeats itself
• Essential software building block in a real
time systems
• Loop forever while waiting for a signal
• When a task is “blocked”, lower priority
tasks can run
• Another task can “post” a signal, to
“unblock” this task that would execute it
“process data” function
• Loops back and “block” again
“block”
signal
received
“loop”
process data
post
signal
TASK
FUNCTION


## Slide 19
Tasks advantages and characteristics
• Typically, an application will have a separate tasks for each
distinct activity.
• Tasks Control Block (TCB) stores information needed to
manage and schedule a task
A task is the smallest sequence of instructions that can
be managed independently by a scheduler; e.g., a task
is a basic unit of processor utilization.


## Slide 20
Task Control Block (TCB)
• The operating system maintains for each task a data structure that contains its current
status such as program counter, priority, state, scheduling information, task name.
• Typically, these TCBs are managed using linked lists (as shown below)
• Other implementation are double-link-list, array, etc.


## Slide 21
What is Multitasking?
• Separate tasks share one processor (or processors)
• Each task executes within its own context
• Owns processor
• Sees its own variables
• May be interrupted
• Tasks may interact to execute as a whole program
• OS needs to switch one context (task) to another context (task)
Context Switch


## Slide 22
Context Switch
• When the processor switches from one task to another task.
• Save the minimum information to restore the interrupted task
• stored in the stack
• contents of registers
• contents of the program counter
• contents of coprocessor registers (if applicable)
• memory page registers
• memory-mapped I/O
• special variables
• Interrupts are often disabled during a context switching
• Minimal times for context switches are required for Real-time Systems.


## Slide 23
Context Switch: An Example
TCB
TCB
TCB
TCB
Task T0 Task T1


## Slide 24
How do many tasks share the same processor?
• Different ways of scheduling a task in a multitasking
environment such as:
• Round Robin Systems
• Pre-emptive Priority Systems


## Slide 25
Round Robin
• Several processes execute sequentially to completion
• Each task is assigned a fixed time slice
• Fixed rate clock initiates an interrupt at a rate corresponding to the time slice
• Task executes until it completes, or its execution time expires
• Context saved if task does not complete
Round Robin Systems - Time Slicing of 3 Tasks
TASK 1 time
1 time slice
TASK 2 TASK 3
2 time slice
TASK 11 TASK 21 TASK 31
TASK
2
1
TASK 31 TASK 12 TASK 13 TASK 22 TASK 32
1 time slice 1.5 time slice
time
TASK Nm
which task, N
task iteration, m


## Slide 26
Pre-emptive Priority
• Higher priority task can pre-empt a lower priority task if it interrupts the lower-priority task
• Priorities assigned to each interrupt are typically based upon the urgency of the task
associated with the interrupt
• Priorities can be fixed or dynamic
Round Robin Systems – Pre-emptive Scheduling of 3 Tasks
TASK
1
1
TASK 21
TASK 31
time
priority
Low
High
TASK
2
1
TASK
1
1
TASK 1
time
TASK 2
TASK 3


## Slide 27
Other Priority Driven Scheduling Algorithm
• Fixed-Priority
• Rate Monotonic Scheduling (RMS)
• static priorities are assigned according to the cycle duration of the job
• a shorter cycle duration results in a higher job priority.
• Deadline Monotonic Scheduling (DMS)
• Dynamic-Priority
• Earliest Deadline First (EDF)
• place processes in a priority queue
• when a task finishes or a new task is started, this queue will be searched for the task closest to its
deadline
• this chosen task is next to be scheduled for execution
• Least Slack Time (LST)
• assigns priority based on the slack time of a task
• slack time is defined as the temporal difference between the deadline, the ready time and the run
time.


## Slide 28
Summary
• Overview of Embedded Operating System
• Briefly discussed the internal workings of an RTOS
• Task States
• Task Control Block
• Illustrate how OS manages multiple tasks via Context Switches
• Went through two examples of Scheduling
• Round Robin
• Pre-emptive Priority


---

# W5.2: Finite State Machine
*6 slides*

---

## Slide 1
Introduction – State Machine
• A model that describes a system’s state and how it
transitions between states based on inputs :
• States: A description of a system’s state
• Transitions: A set of actions that occur when a
condition is met or an event is received
• Inputs: A set of values that a state machine reads and
uses to change states


## Slide 2
Simplest Example


## Slide 3
Lets expand on this …
BTN 2 BTN 1 OFF OFF
OFF ON
ON OFF
ON ON
BTN 2 BTN 1
BTN 2 BTN 1
BTN 2 BTN 1
LED 2 LED 1


## Slide 4
00 01 10 11
BTN 1
BTN 2
BTN 1, BTN 2
BTN 1
BTN 1, BTN 2
BTN 2
STATE DIAGRAM


## Slide 5
00 01 10 11
BTN 1
BTN 2
BTN 1, BTN 2
BTN 1
BTN 1, BTN 2
BTN 2
STATE DIAGRAM


## Slide 6
Current State LED 2 LED 1 INPUT Next State LED 2 LED 1
00 0 0 BTN 1 01 0 1
00 0 0 BTN 2 00 0 0
01 0 1 BTN 1 10 1 0
01 0 1 BTN 2 10 1 0
10 1 0 BTN 1 10 1 0
10 1 0 BTN 2 11 1 1
11 1 1 BTN 1 00 0 0
11 1 1 BTN 2 00 0 0
STATE TABLE
NO CHANGE
NO CHANGE


---

# W6.1: Testing
*24 slides*

---

## Slide 2
TRACEABILITY
Common Anti-Patterns
• Tests not linked to requirements
• Requirements without tests
• Missing requirements or design
elements
• “Gold plating”: adding features
not required
What Traceability Ensures
• Every requirement maps to
design, code, and tests
• Verification: system is built as
specified
• Validation: system works as
intended
• Nothing left out, nothing extra
added


## Slide 3
TRACEABILITY
REQUIREMENT
ANALYSIS
SYSTEM
DESIGN
ARCHITECTUR
E DESIGN
MODULE
DESIGN
IMPLEMENTATION
ACCEPTANCE
TESTING
SYSTEM
TESTING
INTEGRATION
TESTING
UNIT TESTING UNIT TEST PLAN
& RESULTS
TRACEABILITY & VALIDATION
USER ACCEPTANCE TEST PLAN & RESULTS
SYSTEM TEST PLAN
& RESULTS
INTEGRATION TEST PLAN
& RESULTS
PRODUCT
REQUIREMENTS
SOFTWARE
REQUIREMENTS
HIGH LEVEL
DESIGN
DETAILED
DESIGN
‘TECHNICAL’
PRODUCT
INTEGRATION
TEST RESULT
UNIT TEST
RESULT
SOURCE
CODE
VERIFICATION
Test Plan & Test Results
VALIDATION


## Slide 4
TRACEABILITY EXAMPLES
Design
Ensures every req is covered by design & tested
Requirements → Design → Implementation
SQA
(Software Quality Assurance)
Confirms process compliance
Process step → Document/Artifact → Quality metric
Safety
Analysis
Confirms all hazards are mitigated
Hazard → Requirement → Mitigation →Validation
Defect
Ensures all bugs are fixed and verified
Bug report → Defect identified → Fix →
Code check-in → Regression test


## Slide 5
Req ID Requirement Design Ref Code Ref Test Ref
R1
System shall log
temperature every 5
mins
HLD Fig 2, Block
D1.2.1
logger.c:
log_temp_data() Test Case T1.3
Requirement → HLD Diagram → LLD Function → Code → Test Case.
Requirement (R1)
R1: The system shall log temperature data every 5
minutes to flash memory.
Low-Level Design (LLD)
• Design Element ID: D1.2.1
• Function: log_temp_data()
• Description:
• Reads temperature from read_temp_sensor()
• Compresses data to 4 bits
• Appends to flash memory buffer
• Runs every 300 seconds via system timer interrupt
High-Level Design (HLD) Diagram (Figure 2)
• Design Element ID: D1.2 (Logger Module)
• Description: Logger module receives
temperature data from Sensor Driver and
passes it to Flash Storage every 5 minutes.
Code Implementation
• File: logger.c
• Function:
• Triggered by: Timer ISR in timer.c
calling log_temp_data() every 300
seconds
Test Case
• Test ID: T1.3
• Description: Verify that system logs one
temperature value every 5 minutes.
• Method:
• Run device for 15 minutes.
• Read flash contents.
• Expect 3 valid entries.


## Slide 6
TRACEABILITY BEST PRACTICES
Good Practices
• Give every design item an ID for
traceability
• Link requirements design tests
(the “V-Model”)
• Check for gold plating (extra
features not tied to requirements)
• Trace changes to see their wider
impact
Pitfalls to Avoid
• IDs too coarse or too detailed
• hard to manage
• Re-numbering IDs can break
references (auto-gen)
• Using the wrong tool:
• Spreadsheets = don’t scale for big
projects
• Heavy tools = overkill for small
projects


## Slide 7
TESTING OVERVIEW
REQUIREMENT
ANALYSIS
SYSTEM
DESIGN
ARCHITECTUR
E DESIGN
MODULE
DESIGN
IMPLEMENTATION
ACCEPTANCE
TESTING
SYSTEM
TESTING
INTEGRATION
TESTING
UNIT TESTING UNIT TEST PLAN
& RESULTS
TRACEABILITY & VALIDATION
USER ACCEPTANCE TEST PLAN & RESULTS
SYSTEM TEST PLAN
& RESULTS
INTEGRATION TEST PLAN
& RESULTS
PRODUCT
REQUIREMENTS
SOFTWARE
REQUIREMENTS
HIGH LEVEL
DESIGN
DETAILED
DESIGN
‘TECHNICAL’
PRODUCT
INTEGRATION
TEST RESULT
UNIT TEST
RESULT
SOURCE
CODE
WE ARE HERE


## Slide 8
FORMAL TESTING WORKFLOW
Common Pitfalls
• Unstructured informal tests
• No defined pass/fail criteria
• No measurement of test coverage
Pass/fail by comparing
actual vs expected results
Define a workload
(input scenarios)
Run system under test
(SUT) with workload
Use an oracle to
determine the
expected output


## Slide 10
Product-level tests should never find a software bug
• If you find a bug, your process is broken
Always wondering:
How many bugs
are left?
Bugs prevented by
peer review, unit
tests, and
integration tests


## Slide 11
BEST PRACTICES
GOALS
• Aim for high coverage
• White box: covers most code paths
• Black box: covers all requirements
• Use exploratory testing to catch
unexpected behaviour
• Focus on common failure areas
("low-hanging fruit")
• Add other test types as needed
PITFALLS
• Impossible to test all inputs (too
many combinations)
• Test oracle challenge: knowing
correct results at scale
• 100% coverage ≠ fully tested
• All tests passing ≠ bug-free


## Slide 13
UNIT TESTING
REQUIREMENT
ANALYSIS
SYSTEM
DESIGN
ARCHITECTUR
E DESIGN
MODULE
DESIGN
IMPLEMENTATION
ACCEPTANCE
TESTING
SYSTEM
TESTING
INTEGRATION
TESTING
UNIT TESTING UNIT TEST PLAN
& RESULTS
TRACEABILITY & VALIDATION
USER ACCEPTANCE TEST PLAN & RESULTS
SYSTEM TEST PLAN
& RESULTS
INTEGRATION TEST PLAN
& RESULTS
PRODUCT
REQUIREMENTS
SOFTWARE
REQUIREMENTS
HIGH LEVEL
DESIGN
DETAILED
DESIGN
‘TECHNICAL’
PRODUCT
INTEGRATION
TEST RESULT
UNIT TEST
RESULT
SOURCE
CODE WE ARE
HERE


## Slide 14
UNIT TESTING
Good Practices
• Test one module/function at a
time
• Use low-level interfaces
• Combine white box (structure)
+ black box (functionality)
• Best place to catch boundary
bugs (cheaper here than in
system tests)
Common Mistakes
• Only doing system testing.
• Testing only “happy paths”
(everything works perfectly).
• Forgetting to test
missing/exception cases.


## Slide 15
Aspect White Box
Structural / Glass Box
Black Box
Functional / Behavioural
Knowledge Knows the code inside Ignores code, test behaviour
Approach Test internal
paths, branches, loops
Test inputs → output
(requirements)
Goal High code coverage Validate functionality
Advantages Finds hidden logic errors Finds missing or wrong features
Disadvantages Misses unimplemented cases Doesn’t cover code internals
Embedded Use Firmware, control loops,
safety checks
System I/O, sensors, user features
BLACK BOX VS WHITE BOX


## Slide 16
Getting to 100% coverage can be tricky
• Error handlers for errors that aren’t supposed to happen
• Dead (unused) code that should be removed from source
UNIT TESTING COVERAGE


## Slide 17
COVERAGE STRATEGIES
Boundary
Boundary Test
Min & Max values,
Counter Rollover
Time Crossings
Exceptional
NULL, NaN, Inf, null, …
Undefined, invalid inputs
Unusual events: leap
year, …
Justify
Trace to unit design
Get high code coverage
Define strategy for
boundary & exception
coverage


## Slide 18
INTEGRATION TESTING
REQUIREMENT
ANALYSIS
SYSTEM
DESIGN
ARCHITECTUR
E DESIGN
MODULE
DESIGN
IMPLEMENTATION
ACCEPTANCE
TESTING
SYSTEM
TESTING
INTEGRATION
TESTING
UNIT TESTING UNIT TEST PLAN
& RESULTS
TRACEABILITY & VALIDATION
USER ACCEPTANCE TEST PLAN & RESULTS
SYSTEM TEST PLAN
& RESULTS
INTEGRATION TEST PLAN
& RESULTS
PRODUCT
REQUIREMENTS
SOFTWARE
REQUIREMENTS
HIGH LEVEL
DESIGN
DETAILED
DESIGN
‘TECHNICAL’
PRODUCT
INTEGRATION
TEST RESULT
UNIT TEST
RESULT
SOURCE
CODE WE ARE
HERE


## Slide 19
INTEGRATION TESTING
Purpose: Validate interactions between modules, not just
individual functions.
• Focus: interfaces & message exchanges
• Use System Design (SDs) and High-Level Design (HLD) to
drive tests
• Assume components are vetted by unit tests
• Goal: ensure modules work together correctly under all
conditions


## Slide 20
ANTI-PATTERNS (WHAT NOT TO DO)
• Skipping straight to system test
• No traceability from integration test to High Level Design
• “Pass” based only on system function (ignores interfaces)
Result: Integration edge cases are missed, bugs slip through


## Slide 21
GOOD PRACTICES IN
INTEGRATION TESTING
• Exercise all component interfaces
• Test valid, invalid, and boundary values
• Cover timing & sequencing behaviors
• Trace integration tests back to HLD/SDs
• Check intermediate arcs and side effects (not just final output)


## Slide 22
SYSTEMS TESTING
REQUIREMENT
ANALYSIS
SYSTEM
DESIGN
ARCHITECTUR
E DESIGN
MODULE
DESIGN
IMPLEMENTATION
ACCEPTANCE
TESTING
SYSTEM
TESTING
INTEGRATION
TESTING
UNIT TESTING UNIT TEST PLAN
& RESULTS
TRACEABILITY & VALIDATION
USER ACCEPTANCE TEST PLAN & RESULTS
SYSTEM TEST PLAN
& RESULTS
INTEGRATION TEST PLAN
& RESULTS
PRODUCT
REQUIREMENTS
SOFTWARE
REQUIREMENTS
HIGH LEVEL
DESIGN
DETAILED
DESIGN
‘TECHNICAL’
PRODUCT
INTEGRATION
TEST RESULT
UNIT TEST
RESULT
SOURCE
CODE
WE ARE
HERE


## Slide 23
SYSTEM LEVEL TESTING
Common Mistakes
⚫ Excessive defect “escapes” to field testing
⚫ The majority of the testing effortis ad hoc exploratory testing
⚫ Acceptance testing is the only testing done on the system
https://www.techtarget.com/searchsoftwarequality/answer/User-acceptance-testing-vs-system-integration-testing


## Slide 24
SYSTEM TESTING
Purpose: Validate the entire system as a whole, in its intended
environment.
• Test with real hardware, sensors, actuators
• Driven by requirements & user scenarios
• Confirms the system meets end-to-end functionality
• Involves performance, usability, and safety checks
Focus: Does the system do what the HLD requires, under real
conditions?
Each bug found in the system test is a huge deal
• You should find few (<5%) bugs in system test
• Bug found in system test is a process failure


## Slide 25
ANTI-PATTERNS (WHAT NOT TO DO)
• Using only unit or integration tests → assuming system will
“just work”
• Testing only the “happy path” user flows
• Ignoring hardware-software interaction (timing, noise, power)
• Skipping environment tests (temperature, voltage, EMI, etc.)
Result: A system that passes in the lab but fails in the field


## Slide 26
GOOD PRACTICES IN SYSTEM TESTING
• Test end-to-end user scenarios with real inputs/outputs
• Include off-nominal conditions (faults, noise, invalid user
actions)
• Verify performance targets (response time, throughput, power
use)
• Run stress and soak tests (long duration, edge cases)
• Confirm safety/security requirements (e.g., “system shall not
overheat”)
• Trace back to requirements and acceptance criteria


## Slide 28
TOP 10 RISKS OF POOR
EMBEDDED SOFTWARE QUALITY
1. Fails Unit Test – Immediate rework, wasted development time
2. Bug Found in Peer Review – Fixable, but dents confidence in code quality
3. Fails Integration or System Testing – Delays project, adds cost in
debugging multiple modules
4. Fails Acceptance Testing – Customer loses trust; release delayed
5. Field Problem Report – Support costs increase; users frustrated
6. Customer Escalation – Critical downtime, angry stakeholders
7. Emergency Patch in Hostile Conditions – Risky updates in remote/unsafe
environments
8. Public Exposure – Negative press or social media backlash
9. Legal & Regulatory Trouble – Lawsuits, penalties, certification issues
10. Safety/Catastrophic Failure – Human injury, mission loss, or reputational
collapse
escalation from local embarrassment to disasters


---

# W6.2: Sensor Fusion
*41 slides*

---

## Slide 1
Sensors:
From Feeling the World to Understanding It


## Slide 2
Overview
• What are Sensors?
• Sensor Fundamentals
• Various types of Sensor
• Preprocessing of Sensor Data
• Sensor Fusion
• Actuators


## Slide 3
What are Sensors?
A sensor is a device that receives a stimulus and responds with an electrical signal.
trigger


## Slide 4
Computer Process Control System
Actuators
Computer
Controller
Transformation Process
Sensors
DAC ADC
Output Devices Input Devices
Continuous and Discrete
Variables
Continuous and Discrete
Parameters


## Slide 5
What is a Stimulus?
• Motion, position, displacement
• Velocity and acceleration
• Force, strain
• Pressure
• Flow
• Sound
• Moisture
• Light
• Radiation
• Temperature
• Chemical presence
Visual Sensor Ultrasound Sensor Infrared Sensor Button


## Slide 6
What is a Response?
• When we say electrical, we mean a signal which can be
channeled, amplified, and modified by electronic devices:
• Voltage
• Current
• Charge


## Slide 7
Sensor as Energy Translators
This conversion can be direct, or it may require transducers
Example:
• A chemical sensor may have a part which converts the energy of a chemical reaction into heat
(transducer) and another part, a thermopile, which converts heat into an electrical signal


## Slide 8
Physical Principles of Sensing
• Charges, fields, & potentials
• Capacitance
• Magnetism
• Induction
• Resistance
• Piezoelectric effect
• Seebeck and Peltier effects
• Thermal properties of materials
• Heat transfer
• Light


## Slide 9
Capacitance
Two isolated conductive objects of arbitrary shape, which can hold an
electric charge, are called a capacitor
• An electric field is developed between the two conductors
• Dielectric of thickness ‘d’ can be air or some other insulating material
d
A
V
q C
0 
= =
permittivity of free space,
ε0 = 8.85 × 10−12 F/m
A is the area of one
plate in square meters
d is the distance between
the plates in meters


## Slide 10
Dielectric Constant, κ
• The material between the plates of the capacitor can
also be used to sense changes in the environment.
• When vacuum (or air) is replaced by another material,
the capacitance increases by a factor of , known as
the dielectric constant of the material
• The increase in C is due to the polarization of the
molecules of the material used as an insulator
d
A
V
q C
 0
=  =
permittivity of free space,
ε0 = 8.85 × 10−12 F/m
A is the area of one
plate in square
meters
d is the distance
between the plates in
meters
Different dielectric constant
κ for various materials


## Slide 11
Dielectric Constant - Water Level Sensor
The total capacitance of the coaxial sensor shown below is the capacitance
of the water-free portion plus the capacitance of the water-filled portion; as
the level of the water changes, the total capacitance changes


## Slide 12
Analog to Digital Convertor (ADC)
ADC
(24 bits)
ANALOG SIGNAL DIGITAL
0 1 0 1 1 1 0 1 1 0
LPS25H Example:
• Operating range of the sensor: [260 hPa to 1260 hPa] where the sensor is relevant and reliable
• Conversion pressure to measure: measure = pressure × 4096
• Number of bits for coding the maximum value 1260 hPa → measure = 5 160 960
• Full scale : [ 0 hPa to 4096 hPa]
• Sensitivity : 4096 hPa / 2
24
-1 = 0.00024 hPa
2
8


## Slide 13
SenseHAT
Pressure / Temperature sensor
Humidity / Temperature sensor


## Slide 14
PRESSURE / TEMPERATURE SENSOR PROCESS
(LPS25H)
MULTIPLEXER


## Slide 15
HUMIDITY / TEMPERATURE SENSOR PROCESS
(HTS221)


## Slide 16
Signal Conditioning Steps
• Filter for expected frequency range → keep only useful signals, remove
unwanted noise.
• Remove DC offset (“zeroing”) → set the baseline to zero so readings stay
centred.
• Amplify or attenuate (“scaling”) → adjust the signal level to match the ADC
input range.
• Linearize the signal → convert nonlinear sensor output into a straight-line
relationship.
• Analog-to-Digital / Digital-to-Analog conversion → translate between realworld signals and digital values the microcontroller can process.


## Slide 17
Sensor Types: Hardware & Software
• Hardware-based sensors
• Physical components built into a device
• They derive their data by directly measuring specific environmental properties
• Software-based sensors
• Not physical devices, although they mimic hardware-based sensors
• They derive their data from one or more hardware-based sensors, e.g.
• Kalman filters for estimating the location
• Velocity estimators in electric motors
• Estimating process data using self-organizing neural networks
• Fuzzy computing in process control


## Slide 18
Preprocessing of Sensor Data


## Slide 19
Why do we need them?
• The resolution of a sensor is the smallest change in input that can be
reliably detected.
• The accuracy of a sensor is the average difference between measured
value and truth.
• Resolution and Accuracy are dominated by Noise, rather than the
precision of the ADC.
• ADC is sampled multiple times and averaged to improve the signal-tonoise ratio (SNR).


## Slide 20
Methods and Applications
Time focus Typical operation Example
Past → Smoothing Average or blend previous readings to reduce
noise, follow slow trend EMA, Moving Average
Present → Filtering Shape signal instantly or isolate parts of the signal
(low-pass, high-pass, notch)
Finite Impulse Response (FIR) and
Infinite Impulse Response (IIR) filters
Future → Prediction Estimate or forecast upcoming value or state Kalman filter, linear model


## Slide 21
Smoothing
• Averaging
• Moving average
• Exponential moving average
https://www.megunolink.com/articles/coding/3-methods-filter-noisy-arduino-measurements/
http://users.ece.utexas.edu/~valvano/Volume1/
IntroToEmbSys/Ch8_ADC.htm#8_5
Central Limit Theorem
Probability mass functions showing hardware averaging improves signal-to-noise ratio.


## Slide 22
Filtering
• Obtaining data of interest
by removing ‘noise’


## Slide 23
Prediction
• Kalman Filter = Predict → Measure → Correct → Repeat
https://youtu.be/LioOvUZ1MiM


## Slide 24
Sensor Fusion


## Slide 25
Why Filtering Alone Is Not Enough
• Filtering (like moving average, EMA, or low-pass) only cleans a single signal.
• It reduces noise, but cannot fix bias, drift, or missing information.
• Filtering can remove short-term noise, but it can’t correct long-term errors.
• If a sensor drifts slowly (like a gyro or encoder), filtering just makes the drift
smoother, not gone.
• Filtering only improves one sensor’s data it can’t know if that data is wrong.
• Some sensors react fast but unstable, others stable but slow, a single filter can’t
balance both behaviors.
• Filters are like “earplugs for noise,” not “truth detectors”, they make data quieter,
not necessarily more accurate.


## Slide 26
Complementary Filter
• The first part: 𝛼 𝑑fast
→ represents the fast ultrasonic sensor, which reacts quickly to changes in distance but tends
to be noisy and jumpy. It helps the system respond instantly when something moves.
• The second part: 1 − 𝛼 𝑑slow
→ represents the slow ultrasonic sensor, which updates less often but gives smoother, more
stable readings.
It corrects sudden spikes or noise from the fast sensor.
• Together, they form a balanced distance estimate
→ quick to react when something moves, yet steady and reliable when the readings fluctuate.


## Slide 27
Complementary Filter
• The first part: 𝛼(𝜃prev + gyro_rate x Δ𝑡)
→ predicts the angle using the gyro, which reacts fast but can drift.
• The second part: (1 - 𝛼) 𝜃acc
→ corrects that drift using the accelerometer, which is slower but stable.
• Together, they form a balanced estimate
→ quick to respond and steady over time.


## Slide 28
Sensor Fusion Classification
• Sensor Fusion is the process of fusing data coming from a set of
heterogeneous or homogeneous sensors.
• Three types of Sensor Fusion classification
• Abstraction level
• Centralization level
• Competition level


## Slide 29
Sensor Fusion by Abstraction Level
• Data-level
• Fused data collected by multiple
homogeneous sensors.
• Feature-level
• A feature vector that represents the monitored
object from data collected by the sensor. Fusing
information on the features of the monitored
object is called feature-level fusion.
• Decision-level
• Using the feature extracted, some
recognition, classification, and simple logical
operations are performed that lead to a
decision. Decision-level fusion is generally
application-oriented.
https://www.thinkautonomous.ai/blog/9-types-of-sensor-fusion-algorithms/
https://www.avnet.com/wps/portal/apac/resources/article/what-is-sensor-fusion/


## Slide 30
Sensor Fusion by Centralization Level
• Centralized - One central unit deals with the fusion (low-level)
• Distributed - Each sensor processes the data locally and send it to the next
unit (late fusion)
• Decentralized (Hybrid) - Each sensor fuses data and forwards it to the next
one.


## Slide 31
Sensor Fusion by Centralization Level
• Centralized
• The raw data collected by each
sensor is sent right to the main
processing hub for processing.
• Good accuracy and adaptable
algorithms
• The processing power of the
central processing unit is impacted
to process the massive amount of
raw data.
• The latency of data transmission
also needs to be taken into
account due to the volume of data
that needs to be processed.


## Slide 32
Sensor Fusion by Centralization Level
• Distributed
• Processing the raw data collected
by each sensor first in a place
closer to the sensor, sending the
processed data to the central
processing unit for information
fusion calculations, and then
obtaining the final findings.
• Low transmission bandwidth,
quick calculation times, and high
reliability are requirements for this
technology.
• The accuracy of the results
won't be as great as compared to
the centralized method, as some
information will be lost during the
processing of the original data.


## Slide 33
Sensor Fusion by Centralization Level
• Decentralized (Hybrid)
• This technique is a combination
of the first two techniques.
• Certain sensors employ a
distributed fusion approach, while
others employ a centralized
fusion approach.
• Provides high levels of
adaptability and stability since it
includes the benefits of both
centralized and distributed fusion
methods, but the total system
structure tends to be more
complex, and it will cost more to
process data and communicate it.


## Slide 34
Sensor Fusion by Competition Level
Competitive Fusion
• When sensors are meant for the same purpose,
e.g. use both a RADAR and a LiDAR to detect the
presence of a pedestrian. Here, the data fusion
process happening is called redundancy, thus
the "competitive" term.
Complementary Fusion
• Different sensors look at different scenes to get
something we couldn't have obtained
otherwise, e.g. building a panorama with
multiple cameras. Since these sensors complete
each other, we use the term "complementary".
Coordinated Fusion
• Two or more sensors to produce a new scene,
but this time looking at the same object, e.g.
stereo camera vision. Using the two of the same
cameras just a short distance apart gives you
depth.


## Slide 35
Advantages of Sensor Fusion
• Robustness and reliability
• Extended spatial and temporal coverage
• Increased confidence
• Reduced ambiguity and uncertainty
• Robustness against interference
• Improved resolution


## Slide 36
Actuators


## Slide 37
Actuators
• Hardware devices that convert a controller command signal into a change in a physical
parameter
• The change is usually mechanical (e.g., position or velocity)
• An actuator is also a transducer because it changes one type of physical quantity into some
alternative form
• An actuator is usually activated by a low-level command signal, so an amplifier may be
required to provide sufficient power to drive the actuator


## Slide 38
Types of Actuators
• Electrical actuators
• Electric motors
• DC servomotors
• AC motors
• Stepper motors
• Solenoids
• Hydraulic actuators
• Use hydraulic fluid to amplify the controller command signal
• Pneumatic actuators
• Use compressed air as the driving force
http://tbn2.google.com/images?q=tbn:7loeepr6ovfJLM:http://www.fwmurphy.co.uk/images/RP23xx_solenoid_medres.jpg


## Slide 39
Example: Servo motor
• "Servo Motor" employs negative
feedback to control motor speed
and/or position.
• Servo feedback senses the
difference between the actual and
desired speed or position so that
the controller can adjust the
output to correct the 'error’.
• Used in everything from highspeed CNC machines to
positioning motors for telescope
mirrors.
https://www.youtube.com/watch?v=J8atdmEqZsc


## Slide 40
Difference Between Sensors and Actuators
BASIS FOR COMPARISON SENSORS ACTUATORS
Basic Used to measure the continuous
and discrete process variables.
Impel continuous and discrete
processes parameters.
Placed at Input port Output port
Outcome Electrical signal Heat or motion
Example Magnetometer, Cameras,
Accelerometer, microphones.
LED, Laser, Loudspeaker, Solenoid,
motor controllers.
https://techdifferences.com/difference-between-sensors-and-actuators.html


## Slide 41
Summary
• What are Sensors?
• Stimulus → Transducer → Electrical
• Physical principles of sensing; capacitance, inductance, resistance…
• Preprocessing of Sensor Data
• Smoothing, filtering and prediction
• Sensor Fusion
• Abstraction, Centralization and Competition
• Actuators
• Electrical → Stimulus


---

# W8: Optimizations
*20 slides*

---

## Slide 1
Optimizing Embedded Software


## Slide 2
Agenda
• Optimizing Embedded Software
• Power
• Performance
• Memory


## Slide 3
What is Optimization?
• The action of making the most effective use of a resource.
• What are you trying to optimize?
• What are the constraints?
• What are the requirements?
• Example: Given bandwidth of 10 MHz, how to optimize given there are 10
users?
• Give each user 1Mhz?
• Time-slice for each user?


## Slide 4
Power


## Slide 5
Understanding power consumption
• Power (P) = Voltage (V) x Current (I)
• Higher (clock) frequency → higher Current → higher Power
• Ptotal = Pdynamic + Pstatic
• Static vs Dynamic power consumption
• Better control of dynamic consumption
• Power consumed by using the core subsystems, peripherals, memories, and clocks
• Factors: supply voltage
• Harder to control static consumption (static leakage)
• Power that a device consumes without any activity
• Factors: supply voltage, temperature and process technology (e.g. 28 nm).
• Determining power usage
• Maximum, average, worst-case (100% CPU), and typical (use case) power


## Slide 6
Measuring Power Consumption
• Measuring current using ammeter
• Measure the voltage drop across a (shunt)
resister
• Voltage Regulator Module
• splits a large input voltage into smaller ones to
supply individual sources (e.g. cpu, peripherals,
memory, etc)
• Static and Dynamic power measurement
• Profiling your application power consumption
(next slide)
Power
Supply
MCU
A
+ -
Power
Supply
MCU
SR
+ -
V
I = V / R
P = V x I


## Slide 7
EnergyTrace in Code Composer Studio
https://youtu.be/sjoY6h4wH2Y


## Slide 8
Minimizing Power Consumption
Clock Scaling
• This technique reduces the clock
frequency (fclk)
• This reduces the throughput, and power
by a proportional amount
• The energy consumption remains
unchanged
• When fclk is reduced the processor’s
circuits have a longer cycle time to
complete their computation
Voltage Scaling
• As voltage is lowered, frequency or
processor speed is sacrificed, so
generally voltage would be lowered when
the demand from a processor or a certain
peripheral is reduced.
• Typically managed by VRM energy/throughput
time
original
Clock or Voltage scaling


## Slide 9
Peripheral Utilization
• How the peripheral interacts with the core processors
• How does the core know that data is available?
• Polling
• least efficient (in terms of power)
• no context switches (good performance)
• Time-based processing
• data will always be available at a certain interval.
• “Wake up” to just get data then go back to “sleep”
• Interrupt processing
• Peripheral “wakes up” the MCU when data is available (no polling).


## Slide 10
Performance


## Slide 11
Compiler
• No optimization
• Debugging purpose.
• All variables are stored in the stack, enabling the programmer to modify the value of any
variable via the debugger when stopped.
• Inefficient code.
• Typically, four levels of optimization
• 0 = No optimization to 3 = Max optimization
• Varies from vendor to vendor
• Higher optimization level
lead to increase in compilation time
• Speed vs Size


## Slide 12
Basic C optimization techniques
• Choosing the right data types
• A processor only support a 16-bit multiplication
• Multiplying a 32-bit type will cause the compiler to generate a sequence of instructions
• If 32-bit precision is not needed, it would be better to use 16-bit.
• Functions calling conventions
• Stack-based vs Register-based
• Functions takes in more inputs than number of registers, then stack-based is preferred


## Slide 13
Basic C optimization techniques
• Hardware loops
• Mechanism that slows zero-overhead looping by keeping the loop body in a buffer or
prefetching.
• Faster then software loops that decrement counter and branch.
• Typically use loop registers that start with a count equal to the number of iterations of the loop,
decrease by 1 each iteration, and finish when the loop counter is zero.
• Assembly inlining
• Assembly language is used where performance is critical.
• Assembly language is most optimal (human readable code)


## Slide 14
Use vendor run-time libraries
• Vendors typically provide optimized library functions
• e.g. FFT, AES, etc.
• Typically written in assembly
• MSP432
• TI’s Driverlib (library)
• Firmware driverlib (embedded into the chip)


## Slide 15
Eliminating common sub-expressions
• Optimization compilers are able to perform quite well:
X = A * LOG(Y) + (LOG(Y) 2)
• Introduce an explicit temporary variable t:
t = LOG(Y)
X = A * t + (t2)
• Saves one 'heavy' function call, by an elimination of the common sub- expression
LOG(Y), the exponentiation now is:
X = (A + t) * t


## Slide 16
Loop Unrolling
• A technique where the loop body is
duplicated multiple times.
• How it works
• The loop exit checks cost CPU time.
• Loop unrolling tries to get rid of the checks
completely or to reduce the number of
checks.
• Enable other optimization
• Multisampling
• Partial summation
• Software pipelining
• Larger code size
// original version
for(int i=0; i<3; i++)
{
 color_map[n+i] = i;
}
// unrolled version
int i = 0;
colormap[n+i] = i; i++;
colormap[n+i] = i; i++;
colormap[n+i] = i;


## Slide 17
Memory


## Slide 18
Code size optimizations
• Compiler flags
• Speed vs Size
• Target ISA for size and performance trade-offs
• 32-bit arithmetic on a 16-bit platform
• More instructions → more code
• Functions calling conventions
• Stack-based vs Register-based vs Combination
• Data Types
• Select the appropriate data types
• If data can be stored within 16-bit, then use “short int” rather then “int” that is 32-bit.


## Slide 19
Data structures
Loop example 1: Loop example 2:


## Slide 20
Summary
• Power vs Performance vs Memory
• Sometimes it can co-exist, e.g. less code (less memory) → better performance
• Low-power efficient coding techniques:
• Use unsigned data types where possible
• Use pointers to access structures
• Use “static const” class to avoid run-time copying of structures, and arrays
• Avoid floating point operations
• Count down “for” loops
• Use short ISRs


---

# W10: Edge Computing
*21 slides*

---

## Slide 1
Edge Computing
INF2004 Embedded Systems Programming


## Slide 2
Introduction… to Cloud Computing
o Need for Scalable and Flexible Workload Management
o Organisations aim to shift from capital expenditures to operational expenses through pay-as-you-go models.
o Global access and faster deployment of services are in demand.
o Delivers computing services such as servers, storage, and software over the internet (“the cloud”).
o Infrastructure as a Service (IaaS)
o Platform as a Service (PaaS)
o Software as a Service (SaaS)
o Cloud Deployment Models
o Public, Private, Hybrid Clouds
o Key Characteristics
o On-demand self-service
o Broad network access
o Resource pooling and elasticity
o Measured service


## Slide 3
Inherent Challenges… of Cloud Computing
• Latency and Bandwidth Constraints
• Unsuitable for time-sensitive applications
• Potential increase in data transmission costs
• Privacy Concerns
• Off-premises data storage poses risks
• Regulatory challenges, e.g. Health data
• Dependence on Internet Connectivity
• Affects service availability
• Limited Control and Vendor Lock-in
• Difficult to customise
• Complicates migration between providers
Image Credit:
"Tips: Overcoming Individual & Interaction Challenges" by Numrah Khan, Agile Transformation Expert - CSM®, A-CSM℠, CSPO®, Certified SAFe® 5 Agilist & ICAgile Certified Professional Agile. Source: LinkedIn, URL:
https://media.licdn.com/dms/image/v2/D4D12AQHEgNTN3RcqOw/article-cover_image-shrink_720_1280/0/1677410626617?e=1733356800&v=beta&t=o-GzbxaRoClXcpGQqL2Ztkojj8yfhSNgkiISfjJOE10, Accessed 6 October 2024.


## Slide 4
A Changing World – Cotton Candy Cloud
More Devices Online
Devices Generating
more Data
Increased Demand for
Low Latency
Machine Leaning in IoT
Cheaper Sensors
Data Privacy
Regulations


## Slide 5
Evolution of Computing


## Slide 6
Edge-Fog-Cloud Architecture
Ref: Cao, Hung & Wachowicz, M. & Renso, Chiara & Carlini, Emanuele. (2019). Analytics Everywhere: Generating Insights From the Internet of Things. IEEE Access. 7. 71749-71769. 10.1109/ACCESS.2019.2919514.
Countless Billions Millions Thousands


## Slide 7
What is Edge Computing
o General Definition: Edge computing is a distributed computing paradigm that brings computation and data storage closer to
data sources such as sensors, devices, and end-users. This proximity reduces latency and bandwidth usage, enabling faster
processing and real-time responsiveness.
o National Institute of Standards and Technology (NIST) Perspective: Edge computing refers to the enabling technologies
allowing computation to be performed at the network edge, on downstream data for cloud services and upstream data for IoT
services.
o Industry Definition: Edge computing is processing data near the network’s edge, where the data is generated instead of in a
centralised data-processing warehouse. It allows for efficient data processing and analysis, reducing the need for data to
travel to distant servers.
o Cloud Computing Extension: Edge computing extends cloud capabilities by distributing processing power closer to data
sources. It complements cloud computing by handling time-sensitive data at the edge while leveraging the cloud for dataintensive and long-term analytics.
o Academic Definition: Edge computing is a model where data processing and storage are moved away from centralised points
to the logical extremes of a network, enabling data analytics and knowledge generation to occur at the source of the data.


## Slide 8
Mapping Between Characteristics and Benefits
CHARACTERISTIC Leads To BENEFIT
Local processing of data
Low Latency
(Enables real-time responses) Reduced latency for time-sensitive applications
Enhanced Privacy Measures
(Data doesn't leave the device) Improved data privacy and security
Autonomous decisions
(Immediate, context-aware actions) Increased responsiveness and relevance
Data filtering at the source Reduced Bandwidth Usage
(Less data transmitted over networks) Bandwidth optimization, cost savings
Resilience to Network Issues Continues functioning offline Improved reliability
Resource Constraints Requires optimized solutions Energy efficiency, cost efficiency
Heterogeneous Environments Devices work together seamlessly Scalability and flexibility


## Slide 9
Challenges – Post Deployment
COMPLEXITY ENVIRONMENT REMOTE LOCATION PRICE
vs
REDUNDANCY


## Slide 10
Challenges – Operational
SENSOR NETWORK
SECURITY


## Slide 11
Challenges – Manageability
Holistic tool monitor entire Edge Ecosystem Start Debugging from where?


## Slide 12
An Application: Illegal Parking Detection
12
Vehicle Localization &
Tracking Evidence Collection
Bus
Car
Classification
Pre-processing
Background Modeling &
Foreground Detection


## Slide 13
Edge Computing → AIoT → TinyML


## Slide 14
What is TinyML
• TinyML stands for Tiny Machine Learning.
• Deploying machine learning (ML) models on resource-constrained devices with limited
processing power, memory, and energy budget, such as microcontrollers and embedded
systems.
• Enables these small devices to perform data processing and inference tasks locally,
without the need for constant connectivity to cloud services.
• Supports a variety of ML algo, especially optimised for low computational requirements.
• Key Features:
• Low Power Consumption
• Small Model Size
• On-Device Processing
• Real-Time Inference


## Slide 15
TinyML Process Flow
ML
Development
ML Training
Continuous
Training
Convert Model
Model
Deployment
Inferencing
Continuous
Monitoring
Code & Config
Training Pipeline
Registered Model
Tensor Flow Lite
Model
Serving Package
Logs


## Slide 16
Optimizing ML Algorithms for TinyML
• Quantization
• Reducing the precision of numbers (e.g., from 32-bit floating-point to 8-bit integers) to decrease
model size and computation.
• Pruning
• Removing less significant weights or neurons from neural networks to reduce complexity.
• Knowledge Distillation
• Training smaller models (student models) to mimic larger, more complex models (teacher
models).
• Efficient Architectures
• Using architectures designed for low resource usage, such as MobileNet or SqueezeNet for
CNNs.


## Slide 17
Frameworks and Tools Supporting TinyML
• TensorFlow Lite for Microcontrollers
• A version of TensorFlow Lite optimized for microcontrollers.
• Supports a subset of TensorFlow operations suitable for embedded devices.
• uTensor
• A lightweight ML inference library for microcontrollers.
• CMSIS-NN
• Provides efficient neural network kernels optimized for Arm Cortex-M processors.
• Edge Impulse
• A platform for building and deploying TinyML applications, offering tools for data collection,
model training, and optimization.


## Slide 18
Considerations and Challenges
• Memory Constraints
• Models must fit within the limited RAM and flash storage of microcontrollers.
• Processing Power
• Algorithms should have low computational complexity to enable real-time inference.
• Energy Consumption
• Models need to be energy-efficient, especially for battery-powered devices.
• Data Types
• Use of integer-only arithmetic is common to reduce computational load.
• Model Size
• Target model sizes are often in the range of tens to hundreds of kilobytes.


## Slide 19
Demand for Intelligence at the Edge
Pico W Milk V Duo
The inbuilt Tensor Processing Unit (TPU) delivers 1.0 TOPS (Tera Operations
Per Second) of computing power for 8-bit integer operations, significantly
improving performance for efficient machine learning inference tasks.


## Slide 20
Summary - TinyML
• TinyML supports a range of machine learning algorithms tailored to operate within the
stringent resource limitations of edge devices. By optimizing models and selecting appropriate
algorithms, it's possible to implement intelligent features directly on microcontrollers and
embedded systems. This capability enables real-time, low-latency, and energy-efficient
applications across various domains, from consumer electronics to industrial automation.
• Example Applications
• Environmental Monitoring: Using linear regression to predict temperature or humidity trends.
• Anomaly Detection in Machinery: Applying decision trees or statistical methods to detect equipment
faults.
• Gesture Recognition: Utilizing small CNNs to interpret accelerometer data from wearable devices.
• Voice Activation: Implementing keyword spotting models for hands-free device control.
• Predictive Maintenance: Analyzing vibration patterns with RNNs to anticipate mechanical failures.


## Slide 21
Conclusion
• By bringing machine learning to the edge, TinyML empowers devices to make smart
decisions independently, improving efficiency, reducing latency, and ensuring data
privacy.
• It paves the way for innovative solutions in constrained environments, where real-time
insights and actions are critical.


---
