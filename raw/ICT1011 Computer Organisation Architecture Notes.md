# ICT1011 Computer Organisation & Architecture Notes

> Compiled from lecture slides via OCR. Some formatting may vary due to image-based source PDFs.

---

## Table of Contents

1. [Chapter 0: ICT1011 Module Overview](#chapter-0-ict1011-module-overview)
2. [Chapter 1: Fundamentals of Computer Architecture](#chapter-1-fundamentals-of-computer-architecture)
3. [Chapter 3: Instruction Set Architecture](#chapter-3-instruction-set-architecture)
4. [Chapter 4: Introduction to Assembly Language Programming](#chapter-4-introduction-to-assembly-language-programming)
5. [Chapter 5: Executable Assembly Instructions](#chapter-5-executable-assembly-instructions)
6. [Chapter 6: Modular Programming](#chapter-6-modular-programming)
7. [Chapter 7: I/O Interfacing Techniques](#chapter-7-io-interfacing-techniques)
8. [Chapter 8: Secondary Memory Subsystems](#chapter-8-secondary-memory-subsystems)
9. [Chapter 9: Primary Memory Subsystems](#chapter-9-primary-memory-subsystems)
10. [Chapter 10: Memory Management](#chapter-10-memory-management)

---

# Chapter 0: ICT1011 Module Overview



---
### Slide 1

1CT1011: Computer Organisation and Architecture

Steven Wong

=
:

ICT1011
Computer Organisation
and Architecture

Chapter 0

Module Overview

Prof Steven Wong
Steven.Wong@Singaporetech.edu.sg

©2024
Chapter 0: ICT1011 Module Overview


---
### Slide 2

How | conduct lectures???

Lectures will start on time

Lectures will last about 2 hours with a 5-10 minutes break
in between (if time permits)

Please mute your microphones during the lecture

Be mindful of what you type using the chat function. No
vulgarities, swearing or any disrespectful languages are
allowed.

A Slido page will be enabled during the break for you to
post your questions.

Chapter 0: ICT1011 Module Overview


---
### Slide 3

Rationale

Why this module is taught?

This is a foundational course whose main focus is on the
characteristics and development of computational building
blocks, how they are wired together, and how they work to
perform tasks.

You are going to be an ICT professional... so you need
to know exactly how a computer operates!!!

3? A computer works by Logic,
Sx not by Magic!!!

Chapter 0: 1CT1011 Module Overview


---
### Slide 4

Your PC ran into a problem and needs to restart. We're just
collecting some error info, and then we'll restart for you. (0%
complete)

If you'd like to know more, you can search online later for this error: HAL INITIALIZATION FAILED

This happens ror a reason!



---
### Slide 5

Computer Architecture

What is Computer Architecture?

Just like an architect designs buildings, a computer architect
designs computers. So computer architecture is the study of
how computers are designed, why they are designed that
way and what are the effect of different designs on their
performance.

Computer architecture is what's happening inside the
“brain” of a computer

Taught in the 15‘ Part of this module

Chapter 0: ICT1011 Module Overview


---
### Slide 6

Computer Organisation

What is Computer Organisation?

A brain, by itself, is not useful unless if there are some ways
for it to interact with the real world.

Computer organisation is how a CPU
interacts with the things around it, and how
you use it in a real-world application.

Taught in the 2nd Part of this module

Chapter 0: ICT1011 Module Overview


---
### Slide 7

Learning Outcomes

Appreciate the basic building blocks of a computer

Understand the how data and instructions are represented,
stored and retrieved on a computer

Understand how instructions are executed on a computer

Ability to write basic assembly language micro-controller based
platforms

Appreciate the different memory subsystems
Understand and evaluate the various means of interfacing the

Central Processing Unit (CPU) to different Input / Output (I/O)
devices

Chapter 0: ICT1011 Module Overview


---
### Slide 8

Why is this module interesting?

Self-Reflection???

A human system and computer system is similar
in many aspects.

Billions of
Transistors

Internal World

Billions of
Neurons

ai
ae

t Interface

iO

@
Siben Peripherals

oO

External World

ws

Chapter 0: ICT1011 Module Overview



---
### Slide 9

Module Overview
Teaching activities

Lectures (2 hours weekly) (Remote via Zoom)

Tutorials (1 hour weekly) Starts on Week 3 (Remote via MS
Teams)

Labs (5 sessions, 2 hours each) Starts on Week 3 (on campus)

Assessments

Lab quizzes = (30%) - Lab 2 (5%), Lab 3(5%) & Final Lab Quiz (20%)
Team project (20%) - Week 7 to Week 12

Quizzes (20%) — 10% Computer Architecture (1st half)

Sa, MAAs 10% Computer Organisation (2"¢ half)
we A//h C/T ceo% =;
j 3 f Hl 7) ' ' f K : oF

Chapter 0: ICT1011 Module Overview


---
### Slide 10

sv Relationship with other modules

Digital Logic / Data Representation C Programming
Overlap
| 1CT1011 /.
INFi001 \ Computer y INF1002
Introduction to Organisation Programming
Computing and Fundamentals

Architecture

Prerequisite for
1CT2215 a INF2004

Mobile and Embedded Security Embedded Systems
Programming

1CT1011: Computer Organisation and Architecture

ICT3125X 1CT3213
Digital Forensics Malware Analysis and Defence

10

©2024

Steven Wong Chapter 0: ICT1011 Module Overview


---
### Slide 11

Topics covered in this module

Computer Architecture
Fundamentals of Computer Architecture (Chpt 1)

» The CPU (Chpt 2)
Instruction Set Architecture (Chpt 3)
Low-level programming (Chpt 4-6)

Computer Organisation
» Input / Output Techniques (Chpt 7)

» Primary Memory Subsystems (Chpt 8)
Secondary Memory Subsystems (Chpt 9)

(Topics and their sequence are subjected to changes)

Chapter 0: ICT1011 Module Overview


---
### Slide 12

Laboratory Exercises

There will be 5 lab sessions for this course
— 2 hours each, every alternate week
— Lab 1 (Week 3/4): Introduction of MSP430 development tools
— Lab 2 (Week 5/6): Address modes and data storage*
— Lab 3 (Week 8/9): Assembly Instructions*
_ — Lab 4 (Week 10/11): Project Familiarisation
— Week 13: Team presentations for project

* Labs with online submissions (5% each)

DO NOTE THE DATES FOR THE LABS ON
YOUR TIMETABLES!!!

You should have one lab session every 2
weeks

Chapter 0: ICT1011 Module Overview



---
### Slide 13

Laboratory

The MSP430 Launchpad and the Tiny-screen device will be
given out during your 1st Lab session

Lab sessions are optional as you can do the labs at home too
once you have collected the devices. However, do use the lab
sessions as opportunities to clarify your doubts.

You will have to submit the results of Lab 2 and 3 through an
online lab quiz (5% each). The quizzes will be made available
on xSITe by Week 3.

You have to submit your answers by Week 7 and Week 10 for
Lab 2 and 3 respectively

There will be a final lab quiz (20%) that will be conducted in
Week 13 during the 1CT1011 lecture time.

You will need to return the Launchpad during the start of the
next Trimester.

You are responsible for your own learning!!!

Chapter 0: ICT1011 Module Overview


---
### Slide 14

ST Team Exploration Project

a

A Tiny Screen Smart Watch kit will be GIVEN TO YOU for this module.
YOUR RESPONSIBILTY... NO REPLACEMENTS/WARRANTY!!!

A team of 6 students will work on their watches to develop new applications.
The team may leveraging on open-source codes. They will need to then create
a you-tube demonstration.

1CT1011: Computer Organisation and Architecture

For those who are eager to read more in advance, please go to:
https://tinycircuits.com/
You may start working individually on this as soon as you get it.

14 Teams will be formed (members must be from same lab groups) by week 5.
a wis Chapter 0: 1CT1011 Module Overview


---
### Slide 15

References

C@MPUTER

ARCHITECTURE

Computer Architecture: An Embedded Approach
Author: lan McLoughlin

ISBN: 978-0071311182

i Beel gc Structured Computer Organization
cu oa Author: Andrew S. Tanenbaum

(kar rs ISBN: 978-0131485211
CAPA |

on

———a

Chapter 0: ICT1011 Module Overview


---
### Slide 16

References

Computer Organization and Architecture:
Designing for Performance

Author: William Stallings

ISBN: 978-0135064177

COMPUTER

Structured Computer Organization
Author: John L. Hennessy and David A. Patterson
ISBN: 978-0123838728

Chapter 0: ICT1011 Module Overview


---
### Slide 17

References

ih MSP430 Microcontroller Basics
MSP430 Author: John H. Davies
== ISBN: 978-0750682763



---
### Slide 18

Summary of Schedules

i Week Lecture Date Lecture Assessments Lab/Project Assessments Lab Groups Tutorials
i 7 1 6-Sep Lecture 1
“ 4 | 2 13-Sep Lecture 2
“ ' , 3 20-Sep Lecture 3 lab1 Tutorial 1
. - 2 4 27-Sep Lecture 4 1% lab 1 P1 Tutorial 2
x 5 4-Oct Lecture 5 1% Lab 2 and Quiz P2,P3 Tutorial 3
f the 6 11-Oct Lecture 6 E-Learning 6% Lab 2 and Quiz 5% P1 Tutorial 4
@
; ? bs | 8 25-Oct Lecture 7 1% Lab 3 and Quiz 5% P1 Tutorial 5
: 9 1-Nov Lecture 8 1% Lab 3 and Quiz P2, P3 Tutorial 6
v “ss 10 8-Nov Lecture 9 1% Lab 4 Tutorial 7
¥ 11 15-Nov Lecture 10 1% Lab 4 Tutorial 8
: ‘2 12 22-Nov Lecture 11 6% Project
ol > 29-Nov Finca ons aia 20% Project 20% (Project Demo) All access
. i 13 Consultation

Computer Organisation and Architecture

or

-rerson1:

iol

Bis Chapter 0: ICT1011 Module Overview



---

# Chapter 1: Fundamentals of Computer Architecture



---
### Slide 1

=)
a

1CT1011: Computer Organisation and Architecture

ICT1011
Computer Organisation
and Architecture

Chapter 1

Fundamentals of
Computer
Architecture

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 2

Chapter Contents

History and Evolution of Computers
Computer Hardware Decomposition
Classes of Computers

Basic operations and requirements

Components inside a Computer

Example-Register to Register data
transfer

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 3

Chapter Contents

History and Evolution of Computers

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 4

History and Evolution of Computers
Early days of the computer

1834, Cambridge, UK

Charles Babbage built the Difference
Engine, and then the Analytical
Difference Engine.

This was a fully programmable digital
computer, but was mechanical rather
than electronics. This was an
incredibly ambitious, advanced design

1940, Germany

Konrad Zuse used a_= similar

mechanical approach, but controlled i US: a

by electrical relays. The Difference Engine, as drawn in
Harper's new monthly magazine.
Vol. 30, Issue 175, p.34, 1864.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 5

SiTE eg History and Evolution of Computers
Early days of the computer

@ Major progress made during World War II (1940's)
@ Computer research funded mainly by the War Dept.
@  Tosolve problems related to ballistics or cryptography

1CT1011: Computer Organisation and Architecture

©2024
Steven Wong Chpt 1: Fundamentals of Computer Architecture



---
### Slide 6

History and Evolution of Computers

Early days of the computer
r+) 1943, Bletchley Park, UK

Tommy Flowers, working with Alan
Turing, built Colossus as a code-
breaking machine.

=)
:

There were 10 separate machines
built, all were electronic and
programmable. However these
remained a secret until the year

2000.
@ 1944, USA +
mi SSE else 5 P
ENIAC had a_ similar design to A Colossus computer in use ding WWilL courtesy of
Colossus, and although it was only the Bletchley Park Trust

operational after Colossus, ENAIC i eee meee

wasn't secret - so was incorrectly
hailed for many years as the world's
first electronic computer.

These were still very much purpose-built
6 computers!!!

©2024
Steven Wong Chpt 1: Fundamentals of Computer Architecture

1CT1011: Computer Organisation and Architecture



---
### Slide 7

History and Evolution of Computers

John Von Neumann

@ John Von Neumann proposed
the stored program concept
at Princeton University.

]
B

1CT1011: Computer Organisation and Architecture

John von Neumann

©2024

Steven Wong Chpt 1: Fundamentals of Computer Architecture



---
### Slide 8

SiTpsia History and Evolution of Computers
General Purpose Computers

@ 1948, Manchester
The SSEM (Baby) was the first
stored program computer (i.e. an
architecture like a modern machine).

@ 1953, Manchester
The transistor computer was (as the
name suggests) the worlds first
transistor computer. Manchester was
also the home of the world’s first
commercial computer, in 1951

i

IBM System/360 photograph, courtesy of Ben Franske, Wikipedia.

By the mid 1950s, the focus of computer development was shifting
from the UK to the USA:

1CT1011: Computer Organisation and Architecture

@ 1951, USA
MIT (Massachusetts Institute of Technology) built the worlds first real-time
computer
@ 1964, USA
aa /BM enters the picture with the revolutionary System/360.

Steven Wong Chpt 1: Fundamentals of Computer Architecture



---
### Slide 9

SiTpsia

1CT1011: Computer Organisation and Architecture

©2024
Steven Wong

History and Evolution of Computers
Dawn of the Modern Computer

1971, California, USA
Intel releases the Intel 4004 mass-market single
chip CPU. Consider some of its descendants:

8008, 8080, 8080, 8085, 8086, 8088, 80186,
80286, 80386, 80486, Pentium, Pentium II,

Pentium III ,Pentium IV, Celeron, Core, Atom...

1977, Massachusetts, USA

Digital Equipment Corporation release the
VAX11/780; a pioneering computer for one of the
greatest American computing companies of all
time.

VAX mainframe
http://williambader.com/museum/vax/vax.html

By the late 1970s, computers were becoming small and
cheap enough that small companies could own one!

Then came home computers...

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 10

7]
8

1CT1011: Computer Organisation and Architecture

10

©2024
Steven Wong

History and Evolution of Computers
Early “portable” computers

http://en.wikipedia.org/wiki/File:|BM_PC_5150.jpg

Sinclair ZX Spectrum (photo Bill Bertram) Apple Lisa

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 11

T1011: Computer Organisation and Architecture
Pp g

i

11

©2024
Steven Wong

Miniaturisation of the computer

With the advancements in micro-electronics, more
transistors can be fabricated into a micro-chip leading
to creation of powerful micro-processors and micro-

controllers.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 12

7]
8

Year
1941
1945
1949
1951
1961
1964
1968
1975
1987
1992
1993
1997
2000
2007
2009

1CT1011: Computer Organisation and Architecture

12

©2024
Steven Wong

History and Evolution of Computers
Evolution in a nut-shell

Floating point operations per second, FLOPS
1

100

1,000 (1 KiloFLOPS, kKFLOPS)

10,000

100,000
1,000,000 (1 MegaFLOPS, MFLOPS)
10,000,000

100,000,000

1,000,000,000 (1 GigaFLOPS, GFLOPS)
10,000,000,000

100,000,000,000
1,000,000,000,000 (1 TeraFLOPS, TFLOPS)
10,000,000,000,000
478,000,000,000,000 (478 TFLOPS)
1,100,000,000,000,000 (1.1 PetaFLOPS)

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 13

Chapter Contents

Computer Hardware Decomposition

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 14

Computer Hardware Decomposition

PRE-EXERCISE

There are certain things that a “computer” probably needs, in
order to be called a “computer”.

Consider which one of the following are really necessary:
\ a shiny white box with a logo of a half-eaten apple on it

Oa display

0 a hard disc drive

O DVD/Blu-Ray

O wireless

Oa unit that processes numbers

O memory

0 an input device (like a keyboard)

OC a mains power supply or battery
Chpt 1: Fundamentals of Computer Architecture



---
### Slide 15

Computer Hardware Decomposition

y

Do you know what is in the Apple iPad Air?

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 16

Computer Hardware Decomposition
iPad Air Teardown

Source: IHS

WHERE IS THE “BRAINS”???

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 17

<U® Computer Hardware Decomposition

The brains of the iPad

_ e J
* . e
bad s .

/O Controllers 4 * .

And Peripheral : AT .

ICs

Power management processor Flash
memory

Integrated Circuit
(IC)

1CT1011: Computer Organisation and Architecture

The main mother board is the brains of the system. It
contains the file store (flash memory), I/O controller, and the
A7 system-on-chip (SoC) processor.

17

©2024

Steven Wong Chpt 1: Fundamentals of Computer Architecture



---
### Slide 18

SiTpsia

1CT1011: Computer Organisation and Architecture

18

©2024
Steven Wong

Computer Hardware Decomposition

Y \s the iPad hardware decomposition
Y similar to a notebook?

Display Module

Value Line Item #50

Memory Module
#208

Motherboard

Audio 1/0 PCB

Enclosure, Main,
Top #174

= What is common?

Unpl fl. Funuaiienmais OF COMpuler AICMleciure

Source: IHS



---
### Slide 19

Computer Hardware Decomposition

Let’s Revisit this exercise

There are certain things that a “computer” probably needs, in
order to be called a “computer”.

Consider which one of the following are really necessary:
0 a shiny white box with a logo of a half-eaten apple on it

Oa display

0 a hard disc drive

O DVD/Blu-Ray

O wireless

Oa unit that processes numbers

O memory

0 an input device (like a keyboard)

OC a mains power supply or battery
Chpt 1: Fundamentals of Computer Architecture



---
### Slide 20

Chapter Contents

Classes of Computers

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 21

Classes of Computers

From supercomputer — personal computer

— personal digital assistant —> digital watch.

All these devices contain some form of computational
element(s).

There is no clear cut way to classify all these computers.
But we review three broad categories:

- Supercomputers, microcomputers (multi-chip) and
embedded computer (single-chip).

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 22

Classes of computers
Embedded microcomputers

Compact computers that use a single-chip
(microcontroller) that contains the processing
unit, memory and required peripheral support.
They are called embedded microcomputers as the

presence of the microprocessor is non-obvious.
Embedded systems are all around us.

Examples of embedded microcomputer applications

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 23

Classes of computers

Systems-on-Chip (SoC)

A microcontroller that has been integrated with other

interface systems on a single chip is Known as Systems-
on-Chip (SoC).

C430 low-power RF + ultra-low-power MCU

MSP430 microcontroller
© Industry's lowest-power MCU
© 16-bit RISC architecture
© 27- ashe essor log
© Hi ince anal
. Seaecr interface

CC1101 RF transceiver SoC

; * High sensitivity

Ultra-tow power © Low current consum

MPA) * Excellent blocking <a

© Flexible data rate and modulation format

Low-power RF

niegrated chip ae “ erals

Bik carte ADC offering
© 96- ert ctcler

© 128- or AES security encryption/decryption
processor

64-pin QFN
ob i- ene

The highly integrated Texas Instruments CC430 contains an MCU, a transceiver, and intelligent
peripherals, all within a 9.1- by 9.1-mm, 64-pin, QFN package. These parameters suit it for the design
of home portable healthcare equipment.



---
### Slide 24

Chapter Contents

Basic operations and requirements

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 25

Basic Operations and Requirements

Actually, at it's heart, a computer is simply a device that
does 3 things repetitively:

1. Stores and retrieves (loads) values (data)

2. Transforms those values al

3. Transfers those values from one place to another

Every computer program ever written is just a sequence of
these three operations.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 26

Basic Operations and Requirements

The things that differ between computers are really:

1. Where the values can be stored
(and whether different numbers convey different
meanings)

2. What type of processing can be done

3. Where can the data be transferred from or to

Of course there are some other things to consider like:

Speed, accuracy, data size, cost, power consumption,

physical size, programmability, ease of debugging,
memory size, input output capabilities.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 27

Basic Operations and Requirements

Example 1

An MP3 player during audio playback - loads data from flash
memory into RAM in MP3 format. The CPU decompresses the
MP3 data into audio samples. The audio samples are
transferred to a digital-to-analogue converter output.

MP3
decompression
(CPU, RAM etc...)

flash
memory

LOAD>PROCESS> OUTPUT

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 28

Basic Operations and Requirements

Example 2

A games console, displaying an icon on an LCD screen...

Transform image \
—_ pixels —> o>
(resize, rotate etc...)

OxFFFFFF OxFFFFFF OxFFFFFF
OxFFFFFF 0x99CCFF OxFFFFFF
OxFFFFFF 0x99CCFF OxFFFFFF
OxFFFFFF 0x99CCFF OxFFFFFF
OxFFFFFF 0x99CCFF OxFFFFFF
OxFFFFFF OxFFFFFF 0xFFFFFF
OxFFFFFF OxFFFFFF OxFFFFFF

Content of display memory Display memory
Chpt 1: Fundamentals of Computer Architecture



---
### Slide 29

Chapter Contents

‘i fo i}

wa
vv
A
i

Components inside a Computer

Ke

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 30

cies Components inside a Computer

1CT1011: Computer Organisation and Architecture

30

©2024
ven Wong

Peripherals

AT91SAM9261

Pu |
[Jes
| er |

32KH:

POR pacalne

RIT
SHWDC
GPBREG

CPU

USB thost |

i

EB!
CF
NAND
ECC
SDRAM

Diagram from EETimes

Chpt 1: Fundamentals of Computer Architecture

External
Memory
bus

Internal
host
bus

Internal
peripheral
bus

Peripherals

Here is another system-on-chip device... All this is inside one IC
chip We are starting to see clustering of devices inside the chip.



---
### Slide 31

SiTa Components inside a Computer
Using a Micro-controller as reference

I/O pins

I/O pins

CH) O} O
power clock reset

By contrast, this is a diagram of a simple PIC microcontroller IC.
Notice how few things are inside compared to the ARM SoC in the

previous slide!

1CT1011: Computer Organisation and Architecture

However, this still supports the basic functionality of a computer:
* Read only memory (ROM) to hold a program.
* Random access memory (RAM) to hold variables and data.
* An arithmetic logic unit (ALU) to process them.
31 ¢ Two ports for input/output

©2024
Steven Wong



---
### Slide 32

7]
B

1CT1011: Computer Organisation and Architecture

32

©2024
Steven Wong

Components inside a Computer
Using a Micro-controller as reference

I/O pins

I/O pins

Apart from the CPU itself, the most important considerations are
probably Power, Clock, Reset and Memory...

Just an overview here as more details will
be discussed in the following chapters!!!

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 33

Components inside a Computer

The Clock

Almost all modern computers are synchronous - which means that
all their internal signals are triggered on clock edges... it is a very
fundamental technique in making digital logic reliable. This is also
one of the challenges making faster processors.

Complex modern CPUs have one master clock, but use dividers
and multipliers to derive several different speed clocks from this.

Generally, things closer to the core of the CPU(registers and ALU)
will be clocked faster. Things further away will clock slower.

External memory will be a bit slower again, and most peripherals
will be the slowest.

For similar processors, the higher the clock speed,
the faster the processing. Is this true when
comparing different processors?

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 34

Components inside a Computer
Reset

Logic bits are stored as voltage in flip-flops, latches and as
electronic charge in a capacitive cell.

When you start up a logic device (by turning on the power), you
might guess that all the voltages and charges start at zero. But
it's often not true!

So a reset signal is very important to give a CPU a clean start.

One of the things that will get reset to zero when most CPUs
start up is the program counter (PC).

It causes a CPU to boot from address zero: we will see this
later.

This is a hardware reset. How about a software
reset?

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 35

Components inside a Computer

Memory

Non-volatile memory

that retains its contents when the power is turned off. This
can be programmable (like flash, EEPROM, EPROM), or
fixed (like ROM and mask-programmed ROM).

Volatile memory

that gets wiped whenever the power goes off. This
includes SRAM and DRAM (including SDRAM, DDR
etc...).

Note: technically, hard disc, CD-ROM and DVD-ROM are
non-volatile memory (either read-only or read-write).

What about write-only memory?

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 36

Components inside a Computer
Memory

Memories are generally organized in levels of decreasing

speed and cost/bit.

Secondary
Memory

|i Qe increasing cost/bit and speed

© Registers Very fast access but limited numbers within CPU.
Operates at CPU clock rate (size: 2-128 registers)

© Cache Fast access static RAM close to CPU. Typical access
Memory __ time 8-35nS (size: 1kB - 512 kB)
© Main Usually dynamic RAM or ROM (for program storage).

memory _ [ypical access time 20-100nS. (size: 1kB — 1GB)

Not always random access but non-volatile. Maybe be based
on magnetic or flash technology.
Typical access time 5-20mS. (size: 1MB - 80GB)

Chpt 1: Fundamentals of Computer Architecture

© Secondary
Memory



---
### Slide 37

Chapter Contents

Example-Register to Register data
transfer

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 38

Example
Register-to-Register Data Transfer

To highlight the use of the clock and show an example of memory
load/store using register-to-register data transfer.

We start by defining a register that can hold 8 bits of data:

We'll call this register RO, and then put some data inside it:

| | Hi fi

Positive Voltage = Logic 1, No voltage = Logic 0

If red represents a positive voltage, what is the

value stored in the register???
It contains the binary value 00110101

We need to know a little bit about how the register operates now...

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 39

Example
Register-to-Register Data Transfer

The register actually has some contro! wires, and some data
connections. Let's look at a single bit from the register.

ro| | i

The way this works is that
when the “Latch Input” signa Latch Input
is triggered, whatever data is
currently on the input pin

(i.e. high or low), will be latched

into the cell. Memory Cell

When the “Enable Output” signal is
triggered, whatever is stored inside
the cell will appear at the output.

Y
\ Enable Output
Output |

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 40

Example
Register-to-Register Data Transfer

So let's see how we can transfer data from RO to a new
register, we will call R1.

First let's run wires from each cell in RO to the corresponding
cell in R1:

pat | | a LJ Sot onal

Input enable

RI Output enable

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 41

Example
Register-to-Register Data Transfer

Next is a sequence of operations.

1. We enable the output of RO:

Input enable
ios Output enable
R4 Input enable

Output enable

This causes whatever voltage is held in each bit position of RO
to flow through the wires connected to the RO output pins.
But it can't enter R71 yet...

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 42

Example
Register-to-Register Data Transfer

2. Once the voltage on those wires has stabilised, we momentarily
trigger the R1 input enable (keeping RO output turned on):

Input enable
Be Output enable
R1 Input enable [|
Output enable

So now, the data gets into R1, and is latched there.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 43

Example
Register-to-Register Data Transfer

3. Now we can safely turn off the RO output enable:

Ro | i eres

R1 ae [- H puueneae

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 44

Example
Register-to-Register Data Transfer

Before we explore further. Just a reminder:

All data is just 1's and 0's. It doesn't matter if the data is a single
bit, a byte, word, character, string, program, or your entire set of
MP3s and BluRay movies... they are just 1's and 0's to a
computer.

What matters is:

Where is the data stored?

How is the data stored?

Where does it need to be transferred to?
How does it need to be processed?

How much data is there?

How quickly does it need to be processed?
How important is the data and it's timeliness?

How the programmer/user interprets the data?

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 45

Example
Register-to-Register Data Transfer

Going back to our example. | don't want to have to draw so much
every time | discuss register operation... So we simplify:

Input enable
RO Output enable

It's a lot easier to draw it in this way (note the bus is now a single

thick line):
7 ri
Out
a En.

Normally we would indicate the data bus “width” (i.e. 8 bits in this
case), as follows:

Out
— En.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 46

Example
Register-to-Register Data Transfer

Such buses are used extensively to transfer data to and from
registers, memory, input/output ports and so on.

Tristate buffers (>>) arbitrate between these (we had some of
these inside our register’), all timed by a CPU clock, and all
controlled by a CPU control unit.

AH?
«fos se
| BH}

*Tristate buffers mean the output wire can be HIGH, LOW or OFF.
They are very important in allowing different units to share the

same bus to convey data.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 47

Example
Register-to-Register Data Transfer

Here is an example showing how data in one register (A) can
be transferred over a shared bus to another register (B) using
the clock.

Darker lines indicates that the particular bus or signal is active at that time.

fj] See) ee

1

All off Enable Enable Disables Disables
Output Input Input of Output of All off
a mies Data of A oe B read ‘a A
> is data
LW available from
bus

In this example, 5 separate clock cycles are used to enable and
disable buses, tristates and latch inputs at the rising clock edges in
the correct sequence to transfer data from register A to register B.

Chpt 1: Fundamentals of Computer Architecture



---
### Slide 48

Summary

i= | EARNING OUTCOMES OF CHAPTER:
| Knowledge about the evolution of computing

Ability to identify essential components of a
computer

v Ability to determine the class of a computer
Sv Understand the basic operations of a computer

NEXT UP: Details of the CPU

Chpt 1: Fundamentals of Computer Architecture



---

# Chapter 3: Instruction Set Architecture



---
### Slide 1

1CT1011: Computer Organisation and Architecture

Steven Wong

a

ICT1011
Computer Organisation
and Architecture

Chapter 3

Instruction Set
Architecture

- Example of a computer system using
the MSP430-

©2024
Chpt 3: Instruction Set Architecture



---
### Slide 2

Chapter Contents

Examples of Computers

> Micro-processor based and Micro-controller
based systems

> The MSP430 MCU Overview

MSP430 CPU ISA

> CPU Organisation

Registers

Memory Organisation

Machine Code & Assembly Instructions
Addressing Modes

VV VV

Chpt 3: Instruction Set Architecture



---
### Slide 3

Chapter Contents

Examples of Computers

> Micro-processor based and Micro-controller
based systems

Chpt 3: Instruction Set Architecture



---
### Slide 4

SITs Microprocessor vs. Microcontroller

an eerie re ieraitaer System

@ A microprocessor (or uP) forms the core of the system
with external memory and I/O support added to provide
operational capabilities.

rie

ik \

g
:
2
:
5

1CT1011: Computer Organisation and Architecture

4 A Basic Motorola 68000 Microprocessor System

©2023
Steven Wong

Chpt 3: Instruction Set Architecture



---
### Slide 5

SiT psy Microprocessor vs. Microcontroller

Microprocessor-based System

@ Many of the modern day desktop computers are
microprocessor-based systems.

Durable Black™ Solid Capacitors — v= | All New Heat Sink Design 30y Gold Plated LGA2011-3 CPU Socket
. OC Brace f .

Audio Noise Guard with
Trace Path Lighting and
Blink to Music LEC

8-pin CPU Power Connecto
POSCAP™ Capacitors

High End Audio Capacitors ,- Cooper Bussmann Server Level Chokes

IR soe CPU Power De:
(IR Digital Controller+ IR P< MiRstag

115dB HD Audio
with Custom Metal Shielding

4 Channel DDR4

30y Gold Plated PCle Siots a6
mory Slots

Supports GIGABYTE add-in card Ultra Protection

Screw Mounting Hole

4-Way Graphics specail SLI-
! CrossFire™ (Up to 320Gb.

OC Buttons

OG: PEG Extra Power _

Turbo M.2 eee :
onnector for Enhanced PCle Stability

Up to 20Gb/
Front USB 3.0 —
GIGABYTE Pantented DualBIOS™

with LED Indicators se 4
F age
10 SATA 3 Connectors (Up to 6Gb/s : | | ty

SATA EXPRESS Connector (Up to 10Gb/s)

Mop Sensor ron

The Gigabyte GA-X99-SOC Force supporting the
5 Intel Core i7 microprocessors

©2023
Steven Wong

1CT1011: Computer Organisation and Architecture

Chpt 3: Instruction Set Architecture



---
### Slide 6

7]
B

Microprocessor vs. Microcontroller

Microcontroller-based System

@ Amicrocontroller (MCU or pC) has built-in memory and
I/O support, giving rise to a compact operational system.

Revi.t
MSP-EXP4 \@F 552SLP

A single chip
has all the
equivalent

components of

a 68000 uP

system

1CT1011: Computer Organisation and Architecture

: A MSP430F5529 microcontroller based computer

©2023

Steven Wong Chpt 3: Instruction Set Architecture



---
### Slide 7

1CT1011: Computer Organisation and Architecture

7

©2023
Steven Wong

7]
B

Microprocessor vs. Microcontroller

Example of a MCU

MSP430F59xx
Ultra Low Power
16-bit MCU

16MHz

i% Texas
INSTRUMENTS

Accelerators

° 32x32 Multiplier

* DMA (3 Ch)

* CRC16

* AES256 Encryption (FR59xx)

Serial Interfaces

* 3 Serial Interfaces (eUSCI)
¢ 2 UART + IrDA or SPI

°2 12C or SPI

Analog

* 12-bit SAR ADC (up to 16 ch)

o Differential inputs
o Window comparators

* Comparator (Comp_E)
* Vref (REF_A)

Memory
* RAM
°* MPU

Debug

* Real Time JTAG

* Embedded emulation
¢ Bootstrap Loader

Timers

* Watch Dog Timer (WDT_A)

* Real Time Clock (RTC_B)

* Two 16-bit w/3 CCR (TAO, TA1)
* Two 16-bit w/2 CCR (TA2, TA3)
* One 16-bit w/7 CCR (TBO)

Connectivity
* Up to 40 GPIO (Interrupt/Wake)
* Cap touch IO

Power & Clocking

- Brownout Reset
Supply Voltage Supervisor (SVS)
Low Power Vreg (1.5V LDO)
External Oscillators: LFXT, HFXT
Internal Oscillators: VLO, DCO (+2%)

Chpt 3: Instruction Set Architecture



---
### Slide 8

Microprocessor vs. Microcontroller
Microcontroller-based System

Properties of a typical microcontroller (uC)
system:

Integration: Able to implement a whole design onto a single chip.
Cost: Are usually low-cost devices (a few $ each);

Clock frequency: Compared with other devices (microprocessors
_ and DSPs), MCUs use a low clock frequency:

— MCuUs today run up to 100 MHz/100 MIPS (Million Instructions Per Second).
Power consumption: Low power (battery operation);
Bits: 4 bits (older devices) to 32 bits devices;
Memory: Limited available memory, usually less than 1 MByte;

Input/Output (I/O): Low to high (8 to 150) pin-out count.

Chpt 3: Instruction Set Architecture



---
### Slide 9

SiTp se

1CT1011: Computer Organisation and Architecture

©2023
Steven Wong

Viicrooprocessor vs. Microco ntre ») ier
MSP430 — An example of a microcontroller
Low power consumption:
— 0.1 yA for RAM data retention;

— 0.8 PA for real-time clock mode operation;
— 250 yA/MIPS during active operation.

a _——>——

Chpt 3: Instruction Set Architecture



---
### Slide 10

SiTpssg Microprocessor vs. Microcontroller
Microcontroller-based System

@ Why are we using a microcontroller-based systems for this
course???

Applications

Firmware /
Drivers

a1eMyOoS

Compiler

: Instruction Set Architecture

Input / CPU

Transistors / Gates

eempiey

1CT1011: Computer Organisation and Architecture
COMPUTER SYSTEM

It is still a computer and representative of generic
computers. It is also less complex and is cheap!!!

WHY Note: ICT1011 uses the MSP430 to demonstrate principals of Computer Architecture and
MSP430? Organisation. Thus, not everything on MSP430 is covered in this module. More about the
10 MSP430 and other processors will be covered in other modules!!!

©2023

Steven Wong Chpt 3: Instruction Set Architecture



---
### Slide 11

Chapter Contents

Examples of Computers

> The MSP430 MCU Overview

Chpt 3: Instruction Set Architecture



---
### Slide 12

eH

a

+

<2

ca oy
i.

wives

*

5-5

Laie
saeule i

re an

LMF

CP habe

’

ven eed

Sia:

___ 1CT1011: Computer Organisation and Architecture _

otf
tithagey

r
i

¥

MSP430 MCU Overview

MSP430 2000 TivaC Hercules _ Sitara DSP Multicore
16-bit 32-bit 32-bit 16/32-bit 32-bit
Ultra Low A Safety Linux All-around Massive
Power & Cost MCU Android DSP Performance

; * C66 + C66
MSP430 |;@@aattime ARM ARM + A15 + C66
ULP RISC NI Cortex-M3 | Cortex-A8 * A8 + C64
MCU NM M3+C28 m="! Cortex-R4 | Cortex-A9 * ARM9 +
C674
* Low Pwr Mode : P ;
i 0 1 pA * Motor Control * 92-bit Float. | ao, step * $5 Linux CPU C5000 Low °F x oF Float

= 0.5 pA + Digital Power * Nested Vector Dual-coreR4 » 3D Graphics Power DSP _* Up to 12 cores

(RTC) IntCtr (NVIC) . EGG Memory PRUCSS « 32-bit fixifloat oe
* Analog I/F + SIL3Certified industria C6000 DSP * St
* USB and RF subsys 352,000

3" Party Linux, Android, C5x: DSP/BIOS Linux
(only) TI-RTOS Kernel C6x: TI-RTOS (k) TI-RTOS (k)

256K to3M L1:32Kx2 L1:32Kx2 L1:32Kx2
Flash L2: 256K L2: 256K L2: 1M+4M

220 MHz 1.35 GHz 800 MHz 1.4 GHz

-RTOS

TLRTOS —‘TI-RTOS (

k)

Flash: 512K
FRAM: 64K

25 MHz

$0.25 to $1.85 to $1.00 to $5.00 to $5.00 to $2.00 to $30.00 to
$9.00 $20.00 $8.00 $30.00 $25.00 $25.00 $225.00

Chpt 3: Instruction Set Architecture



---
### Slide 13

MSP430 Overview

Internal and External Buses

The MSP430 has a 16-bit internal architecture, a

16-bit external data bus.
16-bit

CPU Internal Bus
16-bit

Control Data Address
Bus Bus Bus

External CPU Buses

Chpt 3: Instruction Set Architecture



---
### Slide 14

SiT psy MSP430 Overview

XIN XOUT RSTINMI DVCC DVSS VCORE AVCC AVSS PA
Pix), P2.x), P3.x ol P5.x ‘ia P7.x pf

HY

om

uscio,1 |} ADC1Z.A

1CT1011: Computer Organisation and Architecture

JTAGI TAO TA TBO USCI_Ax: ]]  12Bit
UART, |] 200KSPS

Reon MPY32 1} Timer_A || Timer_A Timer_B |} RTCA |] CRCI6 |) ion spy
5cC 3cc 7c¢ 16 Channel:
Registers |] Registers | | Registers |] Registers USCI_Bx: | |{14 exti2 int)

SPI,I2c |] Autoscan

DP.DM.PUR

wrt 4
saldaty A MN AY AY AY AY RAY

Regist
(L: 8+2)

REF

MSP430 Detailed Block Diagram

COMP_B
12 Channels}

This is all inside one single MSP430 chip!!!
14

©2023
Steven Wong

Chpt 3: Instruction Set Architecture

OMA

3 Channel



---
### Slide 15

MSP430 Overview

Simplified Block Diagram

Clock
Generation

RISC CPU
16-bit

Digital
Peripherial

Peripherial

1,

This is all inside one single MSP430 chip!!!

Chpt 3: Instruction Set Architecture

Von-Neumenn
architecture —
common bus to all
memory and
peripherals

MAB — Memory
Address Bus

MDB — Memory Data
Bus

Size of MAB (e.g.
16-bits) depends on
the device model



---
### Slide 16

Chapter Contents

MSP430 CPU ISA
> CPU Organisation

Chpt 3: Instruction Set Architecture



---
### Slide 17

MSP430 CPU ISA
The MSP430 Micro-Architecture
Address Bus
{ Memory Address Register | | He le Counter | =
as EE eee . = 7 ADDRESS BUS \\
1
MAR: [0000 ]}/" MAR pc =| mehr MEMORY Port P1
MSP430 a a
: SP a
[WR @=| {_SourceOperand |_| 52] cnco:! | tose) set
| Instruction Register a ot oe | — ee
[ Destination Operand |! |Site) os2s
= Yah 72) eet] | im oes
\ RB: 1 || 800e] 0022
(000 _00t is 104 - F) — oe —
Csis: LY D: \- D i ' soe Sa
044 42 : ses, 1 || qi6] s31e
Ria ! 18| £03e
| | R13: } bia| ooof y
src dst z: 4: 1
: = /16-bit ALU & | lee
= SE T RWE ;
A [” MSEL-
[Arithmetic Logic Unit. | Condition Codes |-|_ Memory
Chpt 3: Instruction Set Architecture



---
### Slide 18

MSP430 CPU ISA
Main Characteristics

16-bit RISC CPU

— Compact core design reduces power consumption and cost

— 27 core instructions (8 Jump, 7 single and 12 double-operand
instructions)

— 7 addressing modes
— 8/16-bit instruction addressing format

Memory architecture
— 16 16-bit registers (4 dedicated-use and 12 general registers)
— 16-bit Arithmetic Logic Unit (ALU)
— 16-bit data bus (8-bit addressability)
— Supports 8/16-bit peripherals
— Address bus size is dependent on model

Chpt 3: Instruction Set Architecture



---
### Slide 19

MSP430 CPU ISA
Organisation of the CPU

Organization of the MSP430 CPU:

— 16-bit data bus (MDB). In this example, a
16-bit address bus (MAB) is shown.

Both registers and memory can be accessed
either in word format or in byte format.

Allows the direct transfer of data between
memory, without passing through the
registers.

through the instructions, some of which run
in a single clock cycle.

Some of the constants most used in
programming can be obtained from the
constant generator.

The 16-bit registers can be accessed directly

MDB - Memory Data Bus
~ 15 0

i —_— RO/PC Program Counter |0
| RWUSP Stack Pointer [0

R2/SRICG1 Status
R3/CG2 Constant Generator

<——— J R10 General Purpose

<——— R11 General Purpose
< R12 General Purpose
<—_} R13 General Purpose

< R14 General Purpose
< R15 General Purpose

Za
Zero,Z —\ dst sre

Carry, C
Overflow, V
Negative, N

16-bit ALU

NUUUU UU

Memory Address Bus - MAB

a“



---
### Slide 20

MSP430 CPU ISA
Organisation of the CPU

Organization of the MSP430 CPU (continued):

— The architecture has a 16 bit Arithmetic
Logic Unit (ALU).

— Carrying out operations affects the state of
the following flags:

¢ Zero (Z);

* Carry (C);

* Overflow (V);
¢ Negative (N).

- eens (Master) clock signal drives the

MDB - Memory Data Bus Memory Address Bus - MAB

16-bit ALU

~ 15 0 4»
i —_— RO/PC Program Counter |of——>
c—— RI/SP Stack Pointer Ol —>

R2/SRICG1 Status —s
R3/CG2 Constant Generator —}
<————) R4 General Purpose —>
<——)]R5 General Purpose =>
—
—
—
—
-—
=,
-—>
}—
—
>

root

dst src 7

1€



---
### Slide 21

Chapter Contents

MSP430 CPU ISA

> Registers

Chpt 3: Instruction Set Architecture



---
### Slide 22

MSP430 CPU ISA

Registers

MDB — Memory Data Bus Memory Address Bus — MAB

»

LL

RO/PC Program Counter |0

RO = Program Counter (PC)

R1 = Stack Pointer (SP)

R2 = Status Register (SR)

R3 / R2 = Constant Generator (CG)

\

it

R1/SP Stack Pointer

i=)

R2/SR/CG1 Status

R3/CG2 Constant Generator

I

R4 General Purpose

R5 General Purpose

R6 General Purpose

R7 General Purpose

RB General Purpose

R9 General Purpose

R10 General Purpose

General Purpose Registers (also
known as Working Registers)

R11 General Purpo

> R4 to R15

General Purpo:

General Purpo:

R4 to R15 are single-cycle, general
purpose and identical in all aspects —
# ) used for math, storage and
LU addressing modes.

Example:
add.w R11,R12 ;R12=R11+R12

MIT

Zero, Z
Carry, C
Overflow, V
Negative, N

Chpt 3: Instruction Set Architecture



---
### Slide 23

MSP430 CPU ISA - Registers
RO — Program Counter (PC)
Pc}x|x|x|x|x|]x|x}x]x|x]x}x]x|x]}x]o
X can be 1 or 0

The 16-bit program counter (PC/RO) points to the next
instruction to be executed

8 7 6 5 4 3

Each instruction uses an even number of bytes (two,
four, or six), and the PC is incremented accordingly.

Instruction accesses in the address space are performed
on word boundaries, and the PC is aligned to even
addresses

PC can be addressed by all instructions and _ all
addressing modes

—- MOV #LABEL,PC ; Branch to address LABEL
—- MOV LABEL,PC ; Branch to address contained in LABEL
—- MOV @R14,PC ; Branch indirect to address in R14

Chpt 3: Instruction Set Architecture



---
### Slide 24

1CT1011: Computer Organisation and Architecture

24

©2023
Steven Wong

]
B

MSP430 CPU ISA - Registers
R1 — Stack Pointer (SP)

Bit 15 1

SP Stack Pointer Bits 15 to 1 0

The stack pointer (SP/R1) is used by the CPU to store the return
addresses of subroutine calls and interrupts. It also can be used to
store local data.

It uses a pre-decrement, post-increment scheme. SP always point to
a RAM location and is always even

Examples
- PUSH #0123h ; Put 0123h onto Top of (Stack TOS)
- POP R8 ; R8 = 0123h

Addr Content Addr Content Addr Content
1008h 1008h 1008h
1006h 1006h 1006h
1004h SP 1004h 1004h = SP
1002h 1002h| 9123h |=SP i002h| 0123h
1000h 1000h 1000h
PUSH #0123h POP R8

R8 = 0123h
Chpt 3: Instruction Set Architecture



---
### Slide 25

SR |

The status register (SR/R2),
used as a source or
destination register, can be
used in the register mode only
addressed with word
instructions.

The remaining combinations of
addressing modes are used to
support the constant
generator.

MSP430 CPU ISA - Registers
R2 — Status Register

Reserved Vv | SCG1 | SCGO

oFF|orr | SIE] N |Z

‘OSC]cPU =

SCG1
SCGO

OSCOFF

CPUOFF
GIE

Overfiow bit. This bit is set when the result of an arithmetic operation
overflows the signed-variable range.

ADD(.B) ,ADDC(.B)

Set when:
Positive + Positive = Negative

Negative + Negative = Positive,
otherwise reset

Set when:

Positive — Negative = Negative
Negative - Positive = Positive,
otherwise reset

System clock generator 1. This bit, when set, turns off the SMCLK.

System clock generator 0. This bit, when set, tums off the DCO dc
generator, if DCOCLK is not used for MCLK or SMCLK.

Oscillator Off. This bit, when set, turns off the LFXT1 crystal oscillator,
when LFXT1CLK is not use for MCLK or SMCLK

CPU off. This bit, when set, turns off the CPU.

General interrupt enable. This bit, when set, enables maskable
interrupts. When reset, all maskable interrupts are disabled.

Negative bit. This bit is set when the result of a byte or word operation
is negative and cleared when the result is not negative.

Word operation: N is set to the value of bit 15 of the
result

N is set to the value of bit 7 of the

SUB(.B) ,SUBC(.B) ,CMP(.B)

Byte operation:

result

Zero bit. This bit is set when the result of a byte or word operation is 0
and cleared when the result is not 0.

Carry bit. This bit is set when the result of a byte or word operation
produced a carry and cleared when no carry occurred.

Chpt 3: Instruction Set Architecture



---
### Slide 26

1CT1011: Computer Organisation and Architecture

26

©2023
Steven Wong

MSP430 CPU ISA - Registers
R2/R3 — Constant Generators

R2/R3: Constant Generator Registers (CG1/CG2):

— Depending of the source-register addressing modes (As) value, six
constants can be generated without code word or code memory
access to retrieve them.

— This is a very powerful feature which allows the implementation of
emulated instructions, for example, instead of implement a core
instruction for an increment the constant generator is used.

Register As Constant Remarks

R2 00 5 Register mode
R2 01 (0) Absolute mode
R2 10 00004h +4, bit processing
R2 alg 00008h +8, bit processing
R3 00 00000h 0, word processing
R3 01 0000ih +1

R3 10 00002h +2, bit processing
R3 oi OFFFFh -1, word processing

Remember that memory access is slow. It is better to use the registers to
store commonly used constants.

Chpt 3: Instruction Set Architecture



---
### Slide 27

MSP430 CPU ISA - Registers

General Purpose Registers

R4-R15: General-purpose registers:

— The general purpose registers R4 to
R15 can be used as data registers, data
pointers and indices. They can be
accessed either as a byte or as a word;

— These registers support operations on
words or bytes;

— In the example to the right, the contents
of the least significant byte of register
R5 (0x8F) is added to the contents of
the memory address pointed to by the
register R6 (0x12h);

Register-Byte Operation

High Byte Low Byte

Byte Memory

Example Register-Byte Operation
R5 = 0OA28Fh

R6 = 0203h

Mem(0203h) = 012h

ADD.B R5,0(R6)
O8Fh

+012h
OAih

Mem (0203h) = OAth
C=0,Z=0,N=1



---
### Slide 28

MSP430 CPU ISA - Registers

General Purpose Registers

R4-R15: General-purpose registers:

— The contents of the memory address is
updated with the result of the operation
(OxA1);

— The status flags of the CPU in the SR are
updated after the execution of the
instruction.

Register-Byte Operation

High Byte Low Byte

Maron

Example Register-Byte Operation

R5 = OA28Fh

R6 = 0203h

Mem(0203h) = 012h

ADD.B R5,0(R6)
O8Fh

+012h
OAth

Mem (0203h) = OAth
C=0,Z=0,N=1



---
### Slide 29

R4-R15: General-purpose registers:

MSP430 CPU ISA - Registers
General Purpose Registers

Byte-Register Operation

High Bi Low B
The contents of the memory address eS ia

pointed to by R6 (0x5F) is added to the Memony
contents of the least significant byte of
register R5 (0x02); Oh Register

i ; E le Byte-Register O; ti
The result of the operation (0x61) is stored json

in the least significant byte of register R5; 6 = 022s
Mem(0223h) = O5Fh

Meanwhile, the most significant byteof ~~
register R5 is set to zero; O5Fh

+ 002h

00061h
The system flags in SR are updated in RS = 00061h

accordance with the result. CFR NAS



---
### Slide 30

Chapter Contents

MSP430 CPU ISA

> Memory Organisation

Chpt 3: Instruction Set Architecture



---
### Slide 31

OFFFEh

MSP430 CPU ISA
Example of the Main Memory

Interrupt Vectors

Word/Byte

SRAM
0200h

16-Bit

Peripherals Word only

0100h

8-Bit
Peripherals
& SFR

Byte only

000h

Word3

Word2

Word1

Low Byte
15/141. . Bits. .| 9] ®
716]. . Bits. | 1] °

High Byte2
Low Byte2

High Byte1

Low Byte1

Example of a memory map

Chpt 3: Instruction Set Architecture

020Ah
0209h
0208h
0207h
0206h
0205h
0204h



---
### Slide 32

MSP430 CPU ISA
Memory Organisation

Word alignment
— Bytes are located at even or odd

addresses

— Words are only located at even

addresses Low Byte

020Ah

Endianess (little-endian)

8 | 0209h

vie) Bites:
— When using word instructions, Words { ee
only even addresses may be i

0 | 0208h

¥
used. The low byte of a word is org High Byte2 o2o7h
always an even address. Low Byte2 0206h

— The high byte is at the next odd

address. Word

— For example, if a data word is

located at address xxx4h, then
the low byte of that data word is

located at address xxx4h, and
the high byte of that word is

located at address xxx5h.

Chpt 3: Instruction Set Architecture

Low Byte1 0204h



---
### Slide 33

7]
B

MSP430 CPU ISA
Memory Organisation

An Example
Assume value of R8 and R9 is initialised to 0

Retrieving a byte from memory Address Content
e.g. MOV.B &3000h, R8

l H’ 9A
Register R8 will have a value of 0x3004
H'12. 0x3003| H’78

0x3002| H’56
0x3001|] y’34

Retrieving a word from memory
e.g. MOV.W &3000h, RY
Register RQ will have a value of
H’3412. (MOV.W &3001h, R9 will

1CT1011: Computer Organisation and Architecture

0x3000 H'12

produce the same result) | There is many correct notations to
represent hexadecimal numbers:
33 e.g. H’12AF, 0x12AF, 12AFh, 12AF,,

©2023
Steven Wong Chpt 3: Instruction Set Architecture



---
### Slide 34

MSP430 CPU ISA

Example of the M Main Memory

MSP430F5522 MSP430F 5523
MSP430F5521 Msp as0rss24 msPas0rssz6 MSP430F5528
MSP430F5513 SP430F5514 MSP430F5517 MSP430F 5513
Memory (flash) Total Size 32 KB 64 KB 96 KB 128 KB
Main: interrupt vector OOFFFFh—OOFFSOh OOF FFFh—OOFFSOn
NIA N/A NA 32 KB
eee 0243FFh-01C400h
c NIA NA 32 KB 32 KB
; Sark 01C3FFh-014400h 01C3FFh-014400h
a DOS END Bark 8 15KB 32 KB 22 KB 32 KB
OOF FFFh-00C400h 0143FFh—00C400h 0143FFh-00C400h 0143FFh—00C400h
Bars 17 KB 32 KB 32 KB 32 KB
Al _:0c3FFh-008000h 00C3FFh-004400h 00C3FFh-004400h 00C3FFh-004400h
Sector 3 2KB> NIA NIA 2KB
0043FFh—003C00h 0043FFh—003C00h
Sector 2 2KB”? NIA 2kB 2B
0038FFh-003400h 0038FFh-003400h 0028FFh-003400h
RAM
Sector 1 2B 2kB 28 2kB
003:
Sector 0 2KB 2kKB 2KB 2KB
0028FFh-002400h 0028FFh—002400h 0028FFh-002400h 0028FFh-002400h
USB RAM“ Sector 7 2kB 2kB 2KB 2kB
: 0023FFh-001C00h 0023FFh-001C00h 0023FFh—001C00h 0023FFh—001C00h
Info A 1288 1288 1288 1288
0019FFh—001980h 0019FFh—001980h 0019FFh—001980h 0019FFh—001980h
Info 8 1288 1288 1288 1288
memory 00197Fh-001900h 00197Fh-001900h 00197Fh-001900h 00197Fh-001900h
(asn) Info C 1288 1288 1288 1288
0018FFh—001880h 0018FFh-001880h 0018FFh-001880h 0018FFh—001820h
Info D 1288 1288 1288 1288
00187Fh-001800h 00187Fh-001800h 00187Fh-001800h 00187Fh-001800h
BSL 3 5128 5128 5128 5128
0017FFh—001600h 0017FFh-001600h 0017FFh—001600h 0017FFh—001600h
BSL 2 5128 5128 5128 5128
Bootstrap loader (BSL) 0015Fh-001400h 0015FFh—001400h 0015FFh—001400h 0015FFh—001400h
memory (flash) BSL 1 5128 5128 5128 5128
0013Fh—001200h 0013FFh—001200h 0013FFh—001200h 0013FFh—001200h
BSLO 5128 5128 5128 5128

0011FFh—001000h

0011FFh—001000h

0011FFh—001000h

0011FFh—001000h

Detailed memory map depends on the device model.

Chpt 3: Instruction Set Architecture



---
### Slide 35

MSP430 CPU ISA
Example of the Main Memory

‘F5529 Memory Map
Bytes
Main Flash
* 512 byte segments — 128K
+ Start address moves according Flash
to RAM
OxFFFF
Info Memory get) INT Vectors 80
+ Use for your own
calibration data, etc. 0x4400
+ 4segments (A-D) ad
+ 128 byte segments 0x2400 RAM | 8K
USB RAM 2K
Boot Loader (BSL) 0x01C0
. Poon casa with serial Info Memory
(slau319 |—_———__
« Password protected Boot Loader
+ 512 byte segments Peripherals

0x0000

Chpt 3: Instruction Set Architecture

MSP430 Memory

+ Unified memory map
(program or data)

+ Absolutely no paging

RAM

+ Always a contig. block

+ If enabled, USB port uses
first 2K

+ RAM segments can be
powered down



---
### Slide 36

Chapter Contents

MSP430 CPU ISA

> Machine Code & Assembly Instructions

Chpt 3: Instruction Set Architecture



---
### Slide 37

MSP430 CPU ISA

MSP430 Instructions Overview

Instruction Register

15 14 13 12 11 10 9 8 7 6 &§ 4 3

1\/0

1\0

0/0/0)\0

0000
0001
0010
0011

Memory
0/1/0)/0)/0/1/0)1/0)/0)/0/0)0;1/0
0/0/0);1/0/0/0)/0/0)/0;0/0)0|1/0
0)/0/1;0)1/1/1/1/1/1/1/0)/0)1)/0
0/1/0);0)/0/0/0)0/0)0)1/1)0;0/0
0/0/0)/0)/0/1/1;/0/0)/0;/0/0;/0;0/0

JNE, JEQ, JNC, JC

0100

JN, JGE, JL, JMP

Mnemonics
mov.w r5,r4 — PC
rrc.w r5
jc main
mov.w #0x0600,r1

0101

MOV

ADD

0110
0111

ADDC

1000

SUBC

1001

SUB

CMP

DADD

BIT

BIC

Chpt 3: Instruction Set Architecture



---
### Slide 38

MSP430 CPU ISA
MSP430 Instructions Data Types

. @ The MSP430 instruction set supports 3 data types:

_@ Bytes (8 bits) Basic data types

3 @ Words (16 bits)

a

Example from Lab 1:

XOR.B #01h, &P10UT ; (i) This XOR the contents at the address
; P10UT with the BYTE value 01,,
; (ii) The results are stored back at address
; P1OUT

MOV.W #60000, R15 _ ; This stores a WORD value of 60000,, into
; Register R15

Chpt 3: Instruction Set Architecture



---
### Slide 39

| 39 word data by default

MSP430 CPU ISA
MSP430 Instructions

27 core instructions

. There are three formats used to encode
instructions for processing by the CPU core

— Double operand
— Single operand
_ — Jumps

The instructions for double and single operands,
depend on the suffix used, (.w) word or (.b)

byte
These suffixes allow word or byte data access
If the suffix is ignored, the instruction processes

Chpt 3: Instruction Set Architecture



---
### Slide 40

MSP430 CPU ISA
MSP430 Instruction Formats

Format |: Instructions with two operands:
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

Op-code S-reg Ad | b/w As D-reg

- Format Il: Instruction with one operand:
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

Op-code b/w Ad D/S-reg

- Format III: Jump instructions:
15 14 13 12 11 10 9 8 7 6 5 4 3 2 14 0

Op-code Condition 10-bit, 2’s complement PC offset

Chpt 3: Instruction Set Architecture



---
### Slide 41

MSP430 CPU ISA - Instructions
Format |: Double Operand Instructions

12 double operand instructions:

Mnemonic Operation Description

Arithmetic instructions

ADD(.B or .W) src,dst srctdstdst Add source to destination

ADDC(.B or .W) src,dst  srctdst+C—>dst Add source and carry to destination

DADD(.B or .W) src,dst srctdst+C— dst (dec) Decimal add source and carry to destination
SUB(.B or .W) srce,dst dst+.not.src+1—dst Subtract source from destination

SUBC(.B or .W) src,dst dst+.not.src+C—dst Subtract source and not carry from destination

Logical and register control instructions

AND(.B or .W) src,dst src.and.dstdst AND source with destination
BIC(.B or .W) src,dst -not.src.and.dstdst Clear bits in destination
BIS(.B or .W) src,dst src.or.dstdst Set bits in destination
BIT(.B or .W) src,dst src.and.dst Test bits in destination
XOR(.B or .W) src,dst src.xor.dstdst XOR source with destination

Data instructions

CMP(.B or .W) src,dst dst-src Compare source to destination

MOV(.B or .W) src,dst srcdst Move source to destination

Chpt 3: Instruction Set Architecture



---
### Slide 42

15 14 13

12

MSP430 CPU ISA - Instructions
Format |: Double Operand Instructions

11

10 9

8

7

6

5

4

3

2 1

0

Op-code

S-reg

Ad

b/w

As

D-reg

The source and destination of the data operated by an instruction are
defined by the following fields:

— src: source operand address, as defined in As and S-reg;

— dst: destination operand address, as defined in Ad and D-reg;

— As: addressing bits used to define the addressing mode used by
the source operand;

— §-reg: register used by the source operand;
— Ad: Addressing bits used to define the addressing mode used by

the destination operand;
— D-reg: register used by the destination operand;
— B/W: word or byte access definition bit. (0:16-bits, 1: 8-bits)

Chpt 3: Instruction Set Architecture



---
### Slide 43

MSP430 CPU ISA - Instructions
Example: Double Operand

Copy the contents of a register to another register

— Assembly: mov.w r5,r4
— Instruction code: 0x4504
Op-code Ad b/w As D-re
mov Register 16-bits Register 14
0100 0101 0 0 00 0100

One word instruction

The instruction instructs the CPU to copy the 16-bit 2’s
complement number in register r5 to register r4

Chpt 3: Instruction Set Architecture



---
### Slide 44

MSP430 CPU ISA - Instructions
Format Il: Single Operand Instructions

7 single operand instructions:

Mnemonic Operation

Description

Logical and register control instructions

RRA(.B or .W) dst MSB->MSB-...

LSB>C
RRC(.B or .W) dst C>MSB-...LSB>C
SWPB( or .W) dst Swap bytes
SXT dst bit 7>bit 8...bit 15

PUSH(.B or .W) src S$P-2—SP, src>@SP

Roll destination right

Roll destination right through carry
Swap bytes in destination

Sign extend destination

Push source on stack

Program flow control instructions

CALL(.B or .W) dst SP-2>SP,
PC+2—@SP
dst>PC

RETI @SP+-—SR, @SP+—SP

Subroutine call to destination

Return from interrupt

Chpt 3: Instruction Set Architecture



---
### Slide 45

MSP430 CPU ISA - Instructions
Example: Single Operand

Logically shift the contents of register r5 to the right
through the status register carry

— Assembly: rrc.w rs

— Instruction code: 0x1005

Op-code b/w Ad D-reg
rrc 16-bits Register 5
000100000 0 00 0101

> One word instruction

* The CPU shifts the 16-bit register r5 one bit to the right
(divide by 2) — the carry bit prior to the instruction
becomes the MSB of the result while the LSB shifted out
replaces the carry bit in the status register

Chpt 3: Instruction Set Architecture



---
### Slide 46

These 8 jump instructions are used to direct program flow to

MSP430 CPU ISA - Instructions
Format Ill: Jump Instructions

another part of the program.

Mnemonic

Description

Program flow control instructions

JEQ/JZ label
JNE/JNZ label
JC label

JNC label

JN label

JGE label

JL label

JMP label

Jump to label if zero flag is set

Jump to label if zero flag is reset
Jump to label if carry flag is set
Jump to label if carry flag is reset
Jump to label if negative flag is set
Jump to label if greater than or equal
Jump to label if less than

Jump to label unconditionally

“label” is where the program will jump to if the conditions are

met.



---
### Slide 47

15 14

13

12 11 10

9

MSP430 CPU ISA - Instructions
Format Ill: Jump Instructions Format

8 7 6 5 4 3 2 1 #0

Op-code

Condition

10-bit, 2’s complement PC offset

Jump instructions are used to direct program flow to

another part of the program.

The condition on which a jump occurs depends on the
Condition field consisting of 3 bits:

— 000: jump if not equal (Z = 0)

— 001: jump if equal (Z=1)
— 010: jump if carry flag equal to zero (C = 0)
— 011: jump if carry flag equal to one (C = 1)
— 100: jump if negative (N = 1)
— 101: jump if greater than or equal (N = V)
— 110: jump if lower (N # V)
— 111: unconditional jump

Chpt 3: Instruction Set Architecture



---
### Slide 48

MSP430 CPU ISA - Instructions
Format Ill: Jump Instructions Format

» Jump instructions are executed based on the current PC
_and the status register

Conditional jumps are controlled by the status bits
Status bits are not changed by a jump instruction

The jump off-set is represented by the 10-bit, 2’s
complement value:
x2

PC, = PCy, + 2 + PC

PC. is the address of the Jump instruction

offset

- Thus, the range of the jump is -511 to +512 words, (-1022
to 1024 bytes ) from the current instruction

Chpt 3: Instruction Set Architecture



---
### Slide 49

MSP430 CPU ISA - Instructions
Example: Jump Instruction

Continue execution at the label Delay if the Zero bit (Z-
flag) is not set

— Assembly: jnz Delay
— Instruction code: 0x23FE

Op-code Condition 10-Bit, 2’s complement PC offset
wine Not Zero -

001 000 1111111110
0 | 0 | 1 | condition 10-bit signed offset ss
o;}O0;1};0;{0]0 10-bit signed offset JNE/JNZ Jump if not equal/zero

> One word instruction

- The CPU will add to the incremented PC (RO) the value
-2 x 2 if the zero flag is not set (i.e, Z=0)

Chpt 3: Instruction Set Architecture



---
### Slide 50

Chapter Contents

MSP430 CPU ISA

> Addressing Modes

Chpt 3: Instruction Set Architecture



---
### Slide 51

MSP430 CPU ISA
Addressing Modes Overview

Op-code S- Ad b/w As D-
mov Register 16-bits Register -
0100 0101 0 0 00 0100

» Opcodes tells the ALU what operations to perform, but
the addressing modes specifies the source and
destination of the parameters (or operands).

_ There are seven addressing modes that take a source
operand and four of these addressing modes also take a
_ destination operand;

- The operands can be located in any memory space
address, but the user needs to be aware of the effects
that their accesses may have;

_¢ The addressing modes are selected by the As and Ad

fields that make up the instruction



---
### Slide 52

MSP430 CPU ISA

Addressing Modes Overview

Op-code Ad b/w As
Spc Scatter «= tes «Regier «=a
0101 | 0001 0 0 00 | 1010

Operands (single-operand instructions)
Source operands (double-operand

instructions)

Destination operands (double-operand
instructions)

Addressing As S-reg Addressing Ad D-reg
mode mode
Register mode | 00 0000to1ii1 Register mode 0 0000to1i11i1
Indexed mode |01/]0001,0011to11 | Indexed mode 1 0001,001itoiiil
11
Symbolic mode | 01 0000 Symbolic 1 0000
mode
Absolute mode | 01 0010 Absolute mode| 1 0010
Indirect register | 10 0000to1111
mode
Indirect auto ik ii Oo00ito1iil
increment mode
Immediate mode} 1 1 0000



---
### Slide 53

MSP430 CPU ISA — Addressing Modes

Source Operand Mnemonics

> The MSP430 has four modes for the source
address:
- Rs - Register ADD.W R4, R10
- x(Rs) - Indexed Register ADD.W 6(R4), R10
- @Rs_~— - Register Indirect ADD.W@R4, R10
—- @Rs+_ - Indirect Auto-increment ADD.W @R4+, R10

In combination with registers RO/R2, three
additional source addressing modes are
available:

- label - PC Relative, x(PC) ADD.W cnt, R10

- &label - Absolute, x(SR) ADD.W &cnt, R10

— #n - Immediate, @PC+ ADD.W #100, R10

Chpt 3: Instruction Set Architecture



---
### Slide 54

MSP430 CPU ISA — Addressing Modes
Destination Operand Mnemonics

There are two modes for the destination
address:

— 0=Rd - Register ADD.W R4, R10

— 1=x(Rd) - Indexed Register ADD.W R4, 6(R10)

In combination with registers RO/R2, two
additional destination addressing modes are
available:

- label - PC Relative, x(PC) ADD.W R4, cnt

— &label — Absolute, x(SR) ADD.W R4, &cnt

Chpt 3: Instruction Set Architecture



---
### Slide 55

MSP430 CPU ISA — Addressing Mode 1
Register Mode — Example 1

add.w r4,r10 ;r10 = r4 + 4r10
a eee
yN ase ae 1
a oa Bus (+1 cycle) | ss x540a] mm i
= _ iis

Chpt 3: Instruction Set Architecture



---
### Slide 56

MSP430 CPU ISA — Addressing Mode 1
Register Mode

In Register addressing mode, the contents of a register is
used as the operand;

This type of addressing mode can be used both with
source and destination operands.

Add the contents of register R4 to register R10:
ADD R4, R10

— Instruction code: 0x540a

Op-code S-reg Ad B/W As D-reg
0101 0100 0 0 00 1010
ADD R4 Register 16-bit Register R10



---
### Slide 57

MSP430 CPU ISA — Addressing Mode 1
Register Mode — Example 2

Move the contents of register R5 to register R4:

MOV R5,R4

— Instruction code: 0x4504

Op-code S-reg Ad B/W As D-reg

0100 0101 0 0 00 0100
MOV R5 Register 16-bit Register R4
CPU Registers Address Space
Code
Before After Reus Mier
R5 | OxAOFD R5_ | OxAOFD
R4 [OxxXXX] 4 foxdorD] | 0x8112 0x3112 RG
0x3110 | 0x4504 | PC 0x3110 | 0x4504

PC | 0x3110 PC | 0x3112



---
### Slide 58

MSP430 CPU ISA - Addressing Mode 2
Indexed Mode — Example 1
add.w 6(r4) ,r10 ;r10 = M(r4+6) + 1r10

fo ee 1
Memory pares oan ==
: o

~

“s.__ Registers

PC>

Chpt 3: Instruction Set Architecture



---
### Slide 59

MSP430 CPU ISA —- Addressing Mode 2
Indexed Mode

» In indexed mode, whether used to indicate the source
address or the destination address, the sum of the
register contents and the signed offset point to the
location in memory;

The offset value is stored in the word following the
| instruction;

» After the execution of the instruction, the contents of
registers are not affected and the PC is incremented to
point to the next instruction to be executed;

» This addressing mode is useful to access data stored in
tables. Apart from the registers PC and SR, all other
registers can be used as an index in indexed mode.



---
### Slide 60

MSP430 CPU ISA - Addressing Mode 2
Indexed Mode — Example 2

Move the byte pointed to by (R5 + 4) to the byte pointed
to by (R4 + 1):
MOV.B 4(R5),1(R4)

— Instruction code: 0x45D4

Op-code S-reg Ad B/W As D-reg
0100 0101 1 1 O01 0100
MOV R5 Indexed 8-bit Indexed R4

— The instruction coding specifies that the byte (B/w =
1) pointed to by the sum of the contents of register R5
(S-reg = 0101) and the word x1 should be moved
to the memory address pointed to by the sum of
register R4 (D-reg = 0100) and the contents of the

word x2:



---
### Slide 61

MSP430 CPU ISA - Addressing Mode 2
Indexed Mode — Example 2

Move the byte pointed to by (R5 + 4) to the byte pointed
to by (R4 + 1) (continued):

MOV.B 4(R5),1(R4)

— Instruction code: 0x45D4 0x0004 0x0001

Op-code S-reg Ad B/W As D-reg
0100 0101 1 1 O01 0100
MOV R5 Indexed 8-bit Indexed R4

— The words X1 and x2 are located in the memory
addresses following the instruction;
— The addressing mode used for the source and

destination operands is controlled by the bits Ad = 1
(Indexed mode) and As = 01 (Indexed mode).



---
### Slide 62

MSP430 CPU ISA — Addressing Mode 2

Indexed Mode — Example 2

Move the byte pointed to by (R5 + 4) to the byte pointed to
by (R4 + 1) (continued):

MOV.B 4(R5),1(R4)

CPU Registers Address Space
Code

Before After Before After

R5_ [ 0x0200 R5 [ 0x0200 0x3116 0x3116 PC
0x3114 | Ox000T | x2 0x3114 | Ox000T | x2

0x3112 | Ox0004 | X1 0x3112 | 0x0004 | X1

R4 —|_0x0200 R4 [0x0200 0x3110 | 0x45D4| PC  — 0x3110 [| 0x45D4
PC 0x3110 PC 0x3116
Data
Destination Address 0x0206 0x0206
0x0200 = (R4) 0x0204 | 0x9ABC 0x0204 [ 0x9ABC
+0x0001__-(X2) 0x0202 | _0x5678 0x0202 | 0x5678
0x0201 0x0200 | 0x1234 ]14(R4)  0x0200 1(R4)
Source Address 0x0206 0x0206
0x0200 in) 0x0204 |Ox9ABC | 4(R5) 0x0204 |_Ox9ABC | 4(R5)
+0x0004 X1 0x0202 | 0x5678 0x0202 | 0x5678
0x0204 0x0200 |_0x1234 0x0200



---
### Slide 63

MSP430 CPU ISA — Addressing Mode 3
Indirect Register Mode — Example 1

add.w @r4,r10 ;rx10 = M(r4) + 4r10

5 BUS ee ea rr a
Memory padres cn = =. - CPU
=

Chpt 3: Instruction Set Architecture



---
### Slide 64

MSP430 CPU ISA — Addressing Mode 3
Indirect Register Mode

In Indirect register mode, any of the 13 CPU registers can
be used (RO, R2 and R3 are not to be used).

A restriction arises from the fact that this addressing mode
can only be used to specify the source operand
_address in dual-operand instructions;

An alternative way to avoid this restriction is to use
indexed mode to specify the destination operand address,
with a zero offset.



---
### Slide 65

MSP430 CPU ISA — Addressing Mode 3

Indirect Register Mode — Example 2

» Move the word pointed to by R5 to the word pointed to by

R4:

MOV @R5,0 (R4)
— Instruction code: 0x45A4 0x0000

Op-code S-reg Ad B/W As D-reg
0100 0101 1 0 10 0100
MOV R5 Indexed 16-bit Indirect R4

— The instruction coding specifies that register R5

(S-reg = 0101) uses the source address (As

= 10);

— The destination address is pointed to in Indexed mode
(Ad = 1) by R4 (D-reg = 0100), using a Zero value

offset.



---
### Slide 66

MSP430 CPU ISA — Addressing Mode 3

Indirect Register Mode — Example 2

Move the word pointed to by Rd to the word pointed to by

R4 (continued):
MOV @R5,0(R4)

CPU Registers

Address Space

Code
Before After Before After
R5 0x0200 R5 0x0200
0x3114 0x3114 PC
R4 0x0202 R4 [0x0202 0x3112 | Ox0000 | X1 0x3112 | Ox0000 | X1
0x3110 | 0x45A4 | PC 0x3110 | 0x45A4
PC 0x3110 PC 0x3114
Data
Destination Address 0x0206 0x0206
0x0204 | Ox9ABC 0x0204 | Ox9ABC
0x0202 ad 0x0202 | 0x5678 | O(R4)  0x0202 | 0xi234 | O(R4)
+0x0000 (X14 0x0200 [0x1234 0x0200 [| 0x1234
0x0202
Source Address 0x0206 0x0206
0x0204 | Ox9ABC 0x0204 |_Ox9ABC
0x0202 | 0x5678 0x0202 | 0x1234
0x0200 |_0x1234 | @R5 0x0200 |_0x1234 | @R5



---
### Slide 67

MSP430 CPU ISA — Addressing Mode 4
Indirect Auto-inc Mode — Example 1

add.w @r4+,r10 ;r10 = M(r4+) + 110

Chpt 3: Instruction Set Architecture



---
### Slide 68

MSP430 CPU ISA - Addressing Mode 4
Indirect Auto-increment Mode

» This addressing mode is similar to the previous one;

» The contents of source register is incremented according
to the data type processed;

- If the data value is byte, the source register is
incremented by 1;

If the data value is a word, the source register is
incremented by 2;

Note that this addressing mode can only be used to
specify the source operand in dual-operand instructions.



---
### Slide 69

MSP430 CPU ISA — Addressing Mode 4

Indirect Auto-inc Mode — Example 2

Move the word pointed to by R65 to the word pointed to by

R4, and increment the source pointer:
MOV @R5+,0 (R4)

— Instruction code: 0x45B4 O0x0000

Op-code S-reg Ad B/W As D-reg
0100 0101 1 0 11 0100
MOV R5 Indexed 16-bit Ind. aut. R4

inc.

— The instruction coding specifies that the register R5

(S-reg = 0101) contains the source address (As

= 11);

— The destination address is pointed to in indexed mode by
R4 (D-reg = 0100), using a zero value offset;

— The execution of the instruction increments the contents
of register R5 by 2.



---
### Slide 70

RS

R4

PC

MSP430 CPU ISA - Addressing Mode 4
Indirect Auto-inc Mode — Example 2

Move the word pointed to by Rd to the word pointed to by
R4, and increment the source pointer (continued):

MOV @R5+,0(R4)

CPU Registers Address Space
Code
Before After Before After
0x0200 R5— [ 0x0202
0x3114 0x3114 PC
0x0202 R4 [Ox0202 0x3112 | 0x0000] x1 0x3112 [_0x0000 | x1
0x3110 | 0x45A4 | PC 0x3110 | 0x45A4
0x3110 PC [| 0x3114
Data
Destination Address 0x0206 0x0206
0x0204 | Ox9ABC 0x0204 | 0x9ABC
0x0202 Re 0x0202 [ 0x5678 | O(R4)  0x0202 | 0xi234 | O(R4)
+0x0000_— (X11 0x0200 [ 0x1234 0x0200 | 0x1234
0x0202
Source Address 0x0206 0x0206
0x0204 | Ox9ABC 0x0204 | 0x9ABC
Ox0202 |_0x5678 0x0202 |_0xi234
0x0200 | 0x1234 | @R5 0x0200 | _0x1234 | @R5



---
### Slide 71

MSP430 CPU ISA — Addressing Mode 5
Symbolic Mode (PC-relative) — Example 1

add.w cnt,r10 ;r10 = M(cnt) + £10

y N “SC s.r 1
2 SS ns So
Memory pa'S= ss6 CPU
f Z: 1
Pi =

PC>

cnt

Chpt 3: Instruction Set Architecture



---
### Slide 72

MSP430 CPU ISA — Addressing Mode 5
Symbolic Mode (PC-relative)

In symbolic addressing mode, for either the source or
destination operands, the memory address is determined
_by adding an offset to the program counter (PC) register;

The offset value is obtained by determining the code
position in the memory, then calculating the difference
between the code position and the memory position that

_ should be achieved;

The assembler determines the offset value and puts it in
the word following to the instruction;

After the execution of the instruction, the program counter
(PC) register is incremented in order to point to the next

instruction.



---
### Slide 73

MSP430 CPU ISA — Addressing Mode 5
Symbolic Mode (PC-relative) — Example 2

» Move the word pointed to by EDEN to the word pointed to
by TONI:

MOV EDEN, TONI

— Instruction code: 0x4090 Ox---- Ox----

Op-code S-reg Ad B/W As D-reg
0100 0000 1 0 01 0000
MOV PC Symbolic 16-bit Symbolic PC

_ — The instruction coding specifies that the value pointed
to by the sum of the PC register contents (s-reg = 0)
and the word x1 should be moved to the memory

address pointed to by the sum of register PC contents
(D-reg = 0) and the word x2;

— The words xX1 and xX2 are stored in the memory
addresses following the instruction.



---
### Slide 74

MSP430 CPU ISA — Addressing Mode 5
Symbolic Mode (PC-relative) — Example 2

Move the word pointed to by EDEN to the word pointed to
by TONI (continued) :

MOV EDEN, TONI

— Instruction code: 0x4090

Op-code S-reg Ad B/W As D-reg
0100 0000 1 0 01 0000
MOV PC Symbolic 16-bit Symbolic PC

— The addressing mode used for the source and
destination operands is controlled by the bits Ad = 1
(Symbolic mode) and As = 01 (Symbolic mode).



---
### Slide 75

MSP430 CPU ISA — Addressing Mode 5
Symbolic Mode (PC-relative) — Example 2

Move the word pointed to by EDEN to the word pointed
to by TONI:

MOV EDEN, TONI

CPU Registers Address Space
Code
Before After Before After
0x3116 0x3116 PC
0x3110 PG [loners 0x3114 [OxDOEE| X2 0x3114_[ OxDOEE| x2

0x3112 [OxDOEE | X1 0x3112 | OxDOEE | X1
0x3110 | 0x4090 | PC 0x3110 | 0x4090

Data
Destination Address 0x0206 0x0206
0x0204 | 0x9ABC 0x0204 | 0x9ABC

0x3114 Gs 0x0202 | 0x5678 | TONI 0x0202 | 0x1234 | TONI
+0xDOEE_ = (X2 0x0200 | 0x1234 0x0200 | 0x1234
0x0202

Source Address 0x0206 0x0206
0x3112 0x0204 | 9x9ABC 0x0204 | Ox9ABC
40xDOEE 6S 0x0202 | 0x5678 0x0202 | 0x1234
“anooo 0x0200 |_0x1234 | EDEN  —9x0200 |_0x1234 | EDEN



---
### Slide 76

MSP430 CPU ISA — Addressing Mode 6
Absolute Addressing Mode — Example 1

add.w &cnt,r10 ;r10 = M(cnt) + 1r10

yN i CS SS
ess =e ay
Memory pase = | “Eig, CPU
J ™ .

PC>

cnt :

Chpt 3: Instruction Set Architecture



---
### Slide 77

MSP430 CPU ISA — Addressing Mode 6
Absolute Addressing Mode

In Absolute mode, the data memory address is placed
after the instruction;

The difference between this addressing mode and
Indexed mode is that the register R2 is now used as an
index, using the constants generator to generate the
value zero;

This addressing mode can be used to define either the
source address or the destination address.



---
### Slide 78

MSP430 CPU ISA — Addressing Mode 6

Absolute Addressing Mode — Example 2
Move the word pointed to by EDEN to the word pointed to

by TONI:
MOV &EDEN, &TONI

_— Instruction code: 0x4292 Ox---- Ox----

Op-code S-reg Ad B/W As D-reg
0100 0010 1 0 01 0010
MOV R2/CG1 Absolute 16-bit Absolute R2/CG1

_ — It can be seen that the register R2 has (Ss-reg = 0010)
and (D-reg = 0010). Register R2 is used as an addresses

index, in which the constant generator loads the value zero;
— When the contents of this register is added to the offset
value X1 or X2, the source and destination addresses are
obtained;
— The words x1 and xX2 are stored in the memory addresses
following the instruction.



---
### Slide 79

MSP430 CPU ISA — Addressing Mode 6

Absolute Addressing Mode — Example 2

Move the word pointed to by EDEN to the word pointed to

by TONI (continued):
MOV &EDEN, &TONI

— Instruction code: 0x4292

Op-code S-reg Ad B/W As D-reg
0100 0010 1 0 01 0010
MOV R2/CG1 Absolute 16-bit Absolute R2/CG1

— The addressing mode used for the source and
destination operands is specified by the bits Ad = 1
(Absolute mode) and As = 01 (Absolute mode).



---
### Slide 80

MSP430 CPU ISA — Addressing Mode 6

Absolute Addressing Mode — Example 2

Move the word pointed to by EDEN to the word pointed
to by TONI (continued):

MOV &EDEN, &TONI

CPU Registers Address Space
Code

Before After Before After

0x3116 0x3116 PC
Po | bse PC Leste 0x3114 [Ox0202 | x2 —0x3114_ | Ox0202 | x2

0x3112 | 0x0200 | X1 0x3112 | 0x0200 | X1
0x3110 | 0x4292 | PC 0x3110 | 0x4292

Data
Destination Address 0x0206 0x0206
0x0204 | 0x9ABC 0x0204 | 0x9ABC

0x0000 ia 0x0202 [| 0x5678 | TONI 0x0202 [ 0x1234 | TONI
+0x0202 = (X2 0x0200 | 0x1234 0x0200 | 0x1234
0x0202

Source Address 0x0206 0x0206
0x0000 0x0204 | 0x9ABC 0x0204 |_Ox9ABC
+ (R2) 0x0202 |_0x5678 0x0202 |_Ox1254
ee (X1) oxo200 | 0x1234 | EDEN 0x0200 | 0x1234 |EDEN



---
### Slide 81

MSP430 CPU ISA — Addressing Mode 7
Immediate Mode — Example 1

add.w #100,r10 ;r10 = #100 + r10
Gadd weston FID

PC>

Chpt 3: Instruction Set Architecture



---
### Slide 82

MSP430 CPU ISA - Addressing Mode 7
Immediate Mode

- The Immediate addressing mode allows values to be
loaded directly into registers or memory addresses. It
can only be used with source operands.

- Move the value 0x0200 to R5:
MOV #0x0200,R5

— Instruction code: 0x4035 0x0200

Op-code S-reg Ad B/W As D-reg
0100 0000 0 0 A, if 0101
MOV PC Register 16-bit Immediate R5

— The instruction coding specifies that the register PC
(S-reg = 0000) is used to define the address of the
word in memory that loads the register R5 (D-reg =
0101) with (As = 11).



---
### Slide 83

MSP430 CPU ISA — Addressing Mode 7
Immediate Mode — Example 3

Move the value 0x0200 to R5 (continued):
MOV #0x0200,R5

CPU Registers Address Space
Code

Before After Before After
R5 | OxXXXX R5 | 0x0200

0x3114 0x3114 PC
PC [oxi pc [oats 0x3112 | 0x0200) x1  0x3112 | 0x0200 | x1
0x3110 | 0x4035 | PC —0x3140 | 0x4035



---
### Slide 84

» | The Constant Generator is automatically used by the assembler

MSP430 CPU ISA - Addressing Mode 7
Immediate Mode — Example 2

add.w #1,r10 ;r10 = #1 + 1r10
Op-code S-reg Ad B/W As D-reg
0101 ooii 0 0 O01 1010

ADD R3 Register 16-bit Register R10

y N ese ae CPU

-
| prsael“ Data Bus 12 100 fxs] 1a a Registers
| 0000

0001
0002
0004
0008

Chpt 3: Instruction Set Architecture



---
### Slide 85

and Architecture

1CT1011: Computer Organisation

age
A

DON’T WORRY!!! ey

(still not the time for that yet)
Try out some of the stuff in
this lecture on your
Lauchpad!!!



---
### Slide 86

LEARNING OUTCOMES OF CHAPTER:

Summary

Understand the ISA of the MSP430
~Understand how machine code instructions are

constructed

Understand and be able to use the various
_ addressing modes available in the MSP430

sieMyoS

COMPUTER SYSTEM

NEXT UP:

The fun of coding
in Assembly
continues!!!

Chpt 3: Instruction Set Architecture

auempieH



---

# Chapter 4: Introduction to Assembly Language Programming



---
### Slide 1

=)
a

and Architecture

1CT1011: Computer Organisation

ICT1011
Computer Organisation
and Architecture

Chapter 4

Introduction to
Assembly Language
Programming

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 2

Introduction to Assembly Language

Introduction Programming

- What is assembly programming
- Why and when to use assembly programming

| Assembly Program Basics

- Stages in assembly program development
- Assembly Language Syntax

Assembler Directives

- Select assembler sections (.sect,.text, .bss, .usect).

- Define values for memory locations (.byte, .word, .string).
- Create symbol table entries (.equ, .set).

- Define library references and definitions (.global, .ref, .def)
- Specify the end of program (.end)

- Assembly Process

Information on Executable Instructions

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 3

Introduction to Assembly Language

H Obes]
Introduction Program ming peat rhe
- What is assembly programming Bib

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 4

What is Assembly Language?

High-level Languages
» E.g. C, C++, Java, Basic
» if (x>10)
y = 20.2;
Easy to write and understand
» Performs data type casting/checking

Limited or no knowledge needed about the
processor

» No details about how fast it would run or how
many bytes of memory is needed to store the
instructions

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 5

What is Assembly Language?

High-level Languages

‘

Assembly Language

» Written in mnemonics of basic instructions
supported by the processor

|e MOVB R85, R6
| MOV.B- R6, &temp
-@ Not as simple to understand program

» Programmer know exactly what operations the
processor is going to perform

e Can calculate the memory needed to store the
code and the time needed to execute the code

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 6

What is Assembly Language?

High-level Languages

‘

Assembly Language

,

Machine Code

@ The exact binary bits that are stored in the

memory to instruct the processor to carry out
certain operations

'¢ 494442162400,

@ MOV.B R9,R10
| 6 MOV.W &2400h, R6

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 7

Introduction to Assembly Hanguage

Introduction Programming

- Why and when to use assembly programming

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 8

Why Use Assembly Language?

Very efficient codes can be created:

@ Reduce unnecessary programming overheads

e.g. high-level language may perform data type checking,

but this improvement in code robustness comes at the
expense of efficiency.

@ More compact program size

e.g. embedded devices may not have much built-in
memory but require more and more functionalities.

4 Codes with faster execution speed

e.g. algorithms for processing signals in mobile phone can

be computationally demanding and need to operate in real-
time.

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 9

When to Use Assembly Language?

Critical parts of the operating system’s software
e.g. kernel of system that is constantly being executed.

Input/Output intensive codes

e.g. device drivers and “loopy” segments of code that
processes streaming data (e.g. audio signal enhancement).

Time-critical or time-dependent codes

e.g. code that detects incoming sensor signals and has to
respond quickly (e.g. car braking system).

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 10

Programming

Assembly Program Basics
- Stages in assembly program development

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 11

Assembly Program Development

Stages in developing an assembly program

Main.asm Prog.obj Prog.abs | | j
—

Linking — | Address Info Download

~ tl

Object file Load module : Memory of
Host PC (for software development) Target MCU.

Assembly Program Development Tools
e Text editor — edit the text-based mnemonics in source file (*.asm).

oe] 2r — converts mnemonics in source file into machine code
and produces an object file (*.0b/).

° ani combines several object files (e.g. from libraries) into a load
module that contains machine code and address information (*.abs).

— uses load module’s address info. to download instructions

and data constants into appropriate memory areas for execution.
: Chpt 4: Introduction to Assembly Language Programming



---
### Slide 12

Characteristics of Assembly Programs

An assembly language program is made up of
basically two types of statements.

Executable instructions
— these are valid instructions of the processor

-— executed when the program runs

. Assembler directives

— they tell the assembler about the desired characteristics
of the program

— they are processed during program assembly and
influence the way the program is loaded into memory.

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 13

MSP430 Assembly Program Example

: Executable instructions Assembler Directives

RESET
StopWDT

Mainloop

Delay

.text
global
retain

.retainrefs

mMoOvV.W
moOvV.W

bis.b
xor.b
mov.w
dec.w
jnz

jmp

.global
-sect
sect
-short

; Assemble into program memory

RESET
; Override ELF conditional linking
; and retain current section
; Additionally retain any sections
; that have references to current
; section
#_ STACK_END,SP ; Initialize stackpointer
#WDTPW|WDTHOLD,&WDTCTL ; Stop watchdog timer
#001h, &P1DIR ; Set P1.0 as output
#001h, &P1OUT ; Toggle value of P1.0 (i.e toggle the LED)
#60000, R15 ; Counter for Delay loop
R15 ; The Delay Loop
Delay ; While R15 is not zero
; keep looping back to label Delay
Mainloop ; Jump back to label Mainloop
__STACK_END
stack
"reset" ; MSP430 RESET Vector
RESET

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 14

Introduction to Assembly panguage
Programming a

Assembly Program Basics

- Assembly Language Syntax

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 15

Assembly Language Syntax

_The typical assembly language program format
divides into four columns.

R15 ; The Delay Loop

jnz Delay ; While R15 is not zero
; keep looping back to label Delay
jmp | Mainloop ; Jump back to label Mainloop

global '__STACK_END
sect | .Stack

.sect ; reset”
-short | RESET

> MSP430 RESET Vector



---
### Slide 16

Assembly Language Syntax

ts The MSP430 assembler reads up to 200 characters per
___ line. Any characters beyond 200 are truncated.

* Follow these guidelines:

— All statements must begin with a label, a blank, an asterisk, or a
semicolon

— Labels are optional; if used, they must begin in column 1

_ — One or more blanks must separate each field. Tab and space
characters are blanks.

~~ Comments are optional. Comments that begin in column 1 can
: begin with an asterisk or a semicolon (* or ;), but comments that
begin in any other column must begin with a semicolon.

~ — Amnemonic cannot begin in column 1 or it will be interpreted as
a label

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 17

Assembly Language Syntax

Label Field

— Labels are optional for all assembly language instructions and
for most (but not all) assembler directives

— When used, a label must begin in column 1
— A label can contain up to 128 alphanumeric characters (A-Z, a-

z, 0-9, _, and $)
— Labels are case sensitive and the first character cannot be a
number

— A label can be followed by a colon (:)
— A label on a line by itself is a valid statement

— If you do not use a label, the first character position must
contain a blank, a semicolon, or an asterisk

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 18

Assembly Language Syntax

Address and Value Labels

It is used as a reference to the address of an instruction or
data (address label).

However, when used with the . equ directive, it takes on
the value of the equated constant (value label).

Example
.equ 5 ;Value label “Fri” has the value of 5
. byte 7 Address labels “Week” and “Main” are
: assigned the addresses of the memory
mov .b R5,R6 ‘locations where the word-sized data 7
mov .w &Week,R7_ ;and the mov .b instruction are stored

;respectively.

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 19

Assembly Language Syntax

Mnemonic Field
— The mnemonic field follows the label field.

— The mnemonic field cannot start in column 1; if it does, it is
interpreted as a label.

— The mnemonic field can begin with one of the following items:
* Machine-instruction mnemonic (such as ADD, MOV, JMP)
« Assembler directive (such as .data, .list, .equ)
¢ Macro directive (such as .macro, .var, .mexit)
* Macro call
(We will not cover this in this module)

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 20

Assembly Language Syntax

Contains mnemonic of executable instructions
or assembler directives.

» Many opcode mnemonics require a suffix to
indicate size of the data being handled.

e.g. — the 2 valid size suffixes of the move mnemonic are

mov.b,mov.w

» Some examples of assembler directives :

Fri ‘initialize byte-sized memory to Fri
12 ‘allocate 12 bytes of memory

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 21

Operand Field

— The operand field follows the mnemonic field and
contains one or more operands.

— The operand field is not required for all instructions or
directives.

— An operand consists of the following items:

* Symbols
* Constants
¢ Expressions (combination of constants and symbols)

— You must separate operands with commas

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 22

“i Assembly Language Syntax

Label Mnemonic Operand Comments

¢ Number of operands in this column depends on the
instruction (may be 0, 1 or 2).

Two-operand example:
mov.b R5,R6 ‘move byte in register R6 to R6

One-operand example:
dec.w R15 ‘decrement the value in R15

1CT1011: Computer Organisation and Architecture

No operand example:
ret ‘return from subroutine.

22

©2024
Steven Wong

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 23

Assembly Language Syntax

aka Le LAL ~*#*#€=™L—_—=....:.=~=~SC*C“‘Ci‘SsSsSsSSS:S:STSTC(
Lave f

Constants

— Constants are treated as unsigned (FFh is equal to
OOFF,, or 255,,)

— Types of constants:

* Decimal: string of decimal digits ranging from (-2147483648
to 4294967295 (ie, 1000, -32768)

* Hexadecimal: string of up to 8 hexadecimal digits followed
by suffix ‘H’ (or ‘h’) or preceded by ‘Ox’ (ie, 78h, 0x78)

— Note: for hex numbers beginning with ‘A’ — ‘F, always precede the
number with a ‘0’ else the assembler will treat it as a label.

— For example: 0A123H is a hex number, A123H is a Label

* Octal: string of up to 8 hexadecimal digits followed by suffix
‘Q’ (or ‘q’) or preceded by ‘0’ (ie, 078, 0x78, 78Q)

* Binary: string of up to 32 binary digits followed by suffix B
(or b) (ie. OO00b, 11110000B)

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 24

Assembly Language Syntax

Expressions

— An expression is a constant, a symbol, or a series of constants
and symbols separated by arithmetic operators.

— Three main factors influence the order of expression evaluation:

* Parentheses Expressions enclosed in parentheses are always
evaluated first.

— 8/(4/2)=4

* Precedence groups Operators: when parentheses do not determine
the order of expression evaluation, the highest precedence operation

is evaluated first.
— 8+4/2=10 (4/2 is evaluated first)

* Left-to-right evaluation: when parentheses and precedence groups
do not determine the order of expression evaluation, the expressions
are evaluated from left to right

—- 8/4/2=1

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 25

Operators can be used in expressions and are evaluated
according to precedence group

Group Operator

1

oOo Wh

oO ON OD

t, “; ~;
* 1
+,-
<<, >>
tee
=[=], I=
&

Description
Unary plus, minus, 1’s complement,

Logical NOT

Multiplication, Division, Modulo

Addition, Subtraction

Shift left, Shift right

Less than, Less than or equal to, Greater
than, Greater than or equal to

Equal to, Not equal to

Bitwise AND

Bitwise exclusive OR (XOR)

Bitwise OR

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 26

“i Assembly Language Syntax

Label Mnemonic Operand Comments

@ Comments are ignored by the assembler but are
essential for good program documentation.

e Use a“;” character before starting comments.

1CT1011: Computer Organisation and Architecture

Main: mov.b R5, R6 ;move byte in register R6 to R6
mov.W &Week, R7 ;move word at memory variable Week to R7
mov.W R12, &Mth ;move word in ER12 to memory var. Mth

26

©2024
Steven Wong

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 27

Introduction to Assembly Language
Programming

Assembler Directives

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 28

Assembler Directives

- Assembler directives supply data to the program

and control the assembly process

» Assembler directives enable you to:

— Assemble code and data into specified sections

— Reserve space in memory for uninitialized variables
— Control the appearance of listings

— Initialize memory

— Define global variables

— Specify libraries from which the assembler can obtain
macros

— many more...

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 29

Assembly Directives

Symbols

> Symbols are used as labels, constants, and
_ substitution symbols

A symbol name is a string of up to 200
alphanumeric characters (A-Z, a-z, 0-9, $, and _ )

A symbol cannot contain embedded blanks and
_ the first character cannot be a number

Symbols are case sensitive

Symbols used as labels become symbolic
addresses that are associated with locations in
the program

Labels used locally within a file must be unique.

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 30

Assembly Directives

Commonly Used Directives
Assembly directives are used to:

— Select assembler sections (.sect,.text, .bss, .usect).

— Define values for memory locations (.byte, .word,
string, .space).

— Create symbol table entries (.equ, .set).

— Define library references and definitions (.global, .ref,
.def)

— Specify the end of program (.end).

FI III KKK RII KIKI KKH IK KIKI TH HK KKK KFT IKK KKH IK HHI IIH KKK IKI IK EKER
Example Code
FRI KI II IKK KIKI RK I KIKI I RK HII IK KK IKI HK RHI II IIH HII KEKE EKER KK

.cdecls C,"msp430x22x4.h" ; include C header

-equ 2000

.bss ent,2 ; ISR counter

Directives - text ; Program reset

mov.w #0x0400,SP ; Initialize stack pointer

mov.w #WDT_MDLY 0 5, &WDTCTL ; Set Watchdog interval to ~0.5ms
bis.w #LPMO+GIE,SR ; Enter LPMO w/ interrupt

jmp $ ; Loop forever; interrupts do all
-sect -reset" i MSP430 RESET Vector
-word start Power Up ISR

Chipt™ F: Introduction to Assembly Language Guarrent Location Counter



---
### Slide 31

Introduction to Assembly panguage
Programming

Assembler Directives
- Select assembler sections (.sect,.text, .bss, .usect).

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 32

Assembly Directives
Select Assembler Sections

A section is a block of code or data that occupies
contiguous space in the memory map.

Each section has its own Location Counter.
The assembler assembles into the current section.

There are two types of sections:

» Initialized sections containing
data or code (modal)

=» .sect Object File Target Memory
s .t -b: 2
ext SS Var, — shi)
=» .data .usect "mySection”
» Uninitialized sections reserving
space in the memory map for
uninitialized data (temporary) ROM (Flash)
=» .bss
» .usect

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 33

Assembly Directives
Select Assembler Sections

Assembler directives that define sections:

Mnemonic and Syntax Description

.bss symbol, size in bytes|, alignment] Reserves size bytes in the .bss (uninitialized data) section
data Assembles into the .data (initialized data) section

sect " section name" Assembles into a named (initialized) section

text Assembles into the .text (executable code) section

symbol .usect "section name", size in bytes Reserves size bytes in a named (uninitialized) section
[, alignment]

.text identifies portions of code in the .text section. The .text section usually contains
executable code.

.data identifies portions of code in the .data section. The .data section usually contains
initialized data.

-Sect defines initialized named sections and associates subsequent code or data with
that section. A section defined with .sect can contain code or data.

.bss reserves space in the .bss section for uninitialized variables.

-usect reserves space in an uninitialized named section. The .usect directive is similar
to the .bss directive, but it allows you to reserve space separately from the .bss

section.
Chpt 4: Introduction to Assembly Language Programming



---
### Slide 34

Select Assembler Sections
Location Counter

The Location Counter holds the relative memory position
of an instruction within the current section.

_— Each section has a location counter used to assign storage
addresses to your program's statements.

— As the instructions of a source module are being assembled, the
location counter keeps track of the current location in storage.

— A $ (dollar sign) can be used as an operand to an instruction to
refer to the current value of the location counter.

The assembler assembles into the current section.

— An initialized section directive (.data, .sect, .text) instructs the
assembler to stop assembling in the current section and begin
assembling in the indicated section.

— An uninitialized section directive does not end the current
section, but simply escape from the current section temporarily.

(Thus uninitialized directives .bss and .usect can appear
anywhere in an initialized section without affecting its contents.)

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 35

Introduction to Assembly Language
Programming

Assembler Directives

- Define values for memory locations (.byte, .word, .string).

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 36

Assembly Directives

Directives that Initialises Memory

Mnemonic and Syntax Description

byte value; [, ... , valuep] nitialize one or more successive bytes in
the current section

.double floating point value nitialize a 48-bit MSP430 floating-point

; constant ;

float floating point value nitialize a 32-bit, MSP430 floating-point
constant

Space size in bytes Reserve size bytes in the current section;
note that a label points to the beginning of
the reserved space

String ‘string,"|, ..., ‘stringn') Initialize one or more text strings

word valuey [, ... , Valuep] Initialize one or more 16-bit integers

Some Examples

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 37

Assembly Directives
Directives that Initialises Memory

.byte places one or more 8-bit values into consecutive bytes of the current section.

-word places one or more 16-bit values into consecutive bytes in the current section.

.String places 8—bit characters from one or more character strings into the current
section. This directive is identical to .byte.

float calculates a (32-bit) MSP430 floating-point representation of a single precision
floating-point value and stores it in four consecutive bytes in the current section.

-double calculates a (48 bit) MSP430 floating-point representation of a double precision
floating-point value and stores it in six consecutive bytes in the current section.

Addr
1 0000
0001
2 0002
3 0004
0005
0006
0007
4 0008
5 000C

Contents AN EXAMPLE
Oxaa .byte OAAh, OBBh
Oxbb

0x1234 .word 01234h

0x68 .String "help"

Ox65

Ox6c

0x70

0x81490fdb float 3.141592654

0x81490fdaa292 | .double 3.141592654

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 38

Directives that Ini

Assembly Directives

tialises Memory

The .space directive reserves a specified number of
bytes in the current section. The assembler fills these

reserved bytes with Os.

When you use a label with .space, it points to the first

byte of the reserved block.

Addr _— Contents AN
1 0x0000 0x100
0x0002 0x200

EXAMPLE
.word 100h,200h

2 0x0004 Res_1: .space 17

3 0x0016 Ox000f

.word 15

j—— Res_1 = 04h

17 bytes
reserved

Chpt 4: Introduction to Assembly;

Language Programming



---
### Slide 39

Assembly Directives
rocation counters’ Worked Example

1 Cc t t GSE A AAA REAAAAARAAREW ERA RARER EARS
2 beichias ;* Start assembling into .text *
3 £ ERE RAEREAAEKAEEREAEREREHRRREREREERE
4 0000 - text
5 0000 01 «byte 1,2

0001 02
6 0002 03 -byte 3,4

0003 04
7
8 FEAR AAKEAHAHREREKARAREREKERHREKKRRRERE
9 ;* Start assembling into .data *
10 g RARER HAHRARAAREARHERRHEEKNRRENRERRRHRE
11 0000 -data
12 0000 09 -byte 9,10

0001 0a
13 0002 Ob byte 11,12

0003 Oc
14
15 AAR AERAAHEKERRAAERRRERKENHEERHREAEHREEE
16 ;* Start assembling into named ¥
17 ;* section, var_defs =
18 DORI III III IOI OI III TOTO TOTTI Ik
19 0000 -sect "var _defs"
20 0000 a4. -byte 17,18

0001 12
21

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 40

22
23
24
25
26

27
28

29
30
31
32
33
34

35
36

0004
0004
0005
0000
0006
0007

0004
0004
0005
0000
0006

0007

0d
0e

of
10

05
06

07
08

Assembly Directives

Worked Example

ERE RAERAAEEREEERERERRERRKEEEREREEE

;* Resume assembling into .data *
g SERRE CARRAHRAEEHRREAEEREEHERRREREREEERE

-data

-byte 13,14

-bss sym,19 ; reserve space in .bss
-byte 15,16 ; still in .data

gp FERRE RAERAERAKKRRERRERERRRRRREREEREE

;* Resume assembling into .text *
FERRARA AARHEARERERERRRARKKEERERERE

. text
-byte 5,6

usym .usect "xy",20 ; reserve space in xy
-byte 7,8 ; still in .text

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 41

_ Introduction to Assembly paniguage
Programming ef

Assembler Directives

- Create symbol table entries (.equ, .set).

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 42

Assembly Directives
Create Symbol Table Entries

Syntax symbol .set value
symbol .equ value
Description

The .set and .equ directives equate a constant value to a symbol.
The symbol can then be used in place of a value in assembly
source. This allows you to equate meaningful names with constants
and other values. The .set and .equ directives are identical and can
be used interchangeably.

a gERAERRARAAKEERAKKKREEURERKREEREKEREREEEERER
2 ;* Equate symbol FP to register R11 *
3 7* and use it instead of R11 ¥
4 FEATHER AEAEHHREREEREN HERRERA HKREREEKRE
5 Ob FP -set R11

6 0000 4b24 MOV @FP, R4

-

8 g RRA AARRARAHLERARERRRKERRRRRERRERREREURE
9 ;* Set symbol count to an integer *
10 ;* expression and use it as an *
a2 ;* immediate operand *
12 FEAR EREAHEHEREAEKEERHHAEHEERENHRERHEEKE
13 35 count -equ 100/2+3
14 0002 40340035 MOV #count, R4

~* It is like,a text-replacement tool!!!

Chpt 4: a tex to Assembly Language Programming



---
### Slide 43

Assembler Directives

- Define library references and definitions (.global, .ref, .def)

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 44

Assembly Directives
Library Reference and Definition

» Library
— Aset of routines for a specific domain application.
— Example: math, graphics, GUI, etc.

— Use the .ref directive to reference symbols defined outside a
program.

» Library routine invocation
— Labels for the routines are defined as .def
— Each library routine contains its own symbol table.

—A linker resolves the external addresses before creating the
executable image.

— Reports and unresolved symbols.

' The .global directive declares a symbol to be external so that it is
available to other modules at link time. This directive does double
duty, acting as a .def for defined symbols and as a .ref for undefined
symbols.

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 45

Assembly Directives
Library Reference and Definition

Module A
Source Module A Object
ref myFunc Executable
.ref sqrt Image
.text
Module A
call #myFunc Object
call #sqrt
” Module B
Object Module B
and Object
Source Module B
.def myFunc Math
.text Library

myFunc:

ret

.end

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 46

_ Introduction to Assembly vanguage
Programming i

Assembler Directives

- Specify the end of program (.end)

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 47

Assembly Directives

Specify End of Program

Syntax .end

Description

The .end directive is an optional directive that terminates assembly.
It should be the last source statement of a program. The assembler
ignores any source statements that follow an .end directive.

This directive has the same effect as an end—of-file. You can also
use .end when you're debugging code and you'd like to stop
assembling at a specific point in your code.

Text start: .text
.-byte Oah
-word Oaaaah

.string "aaa"

.end

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 48

Assembler Directives

- Assembly Process

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 49

Assembly Directives

Assembly Process

The assembler translates assembly language programs
(.asm) into the machine language of the ISA (.obj).

There is a 1-to-1 correspondence between assembly
language instructions and instructions in the final machine
language.

First Pass:

— find all labels  and_ their corresponding addresses
this information is stored in the symbol table

Second Pass:

— convert instructions to machine language, using information from
symbol table

—>| 1st Pass +») 2nd Pass Executable
Image

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 50

Programming

Information on Executable Instructions

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 51

Executable Instruction Information
Executable Instructions

Executable instructions are assembly mnemonic
instructions that are assembled into machine codes and

executed by the MSP430.

Information for the assembly instructions can be obtained

from:
— MSP430 Quick Reference
— MSP430 Instruction Set Summary

Information includes:

— Machine code translation

— Instruction operation and description
— Impact on the status bits

— Length and clock-cycle information

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 52

Executable Instruction Information
Machine Code Translation
Using the MSP430 Quick Reference

opcode source Ad | BAW] As | destination Two-operand arithmetic
0 | VOL A |__source__| Ad | BW | As | destination | ADD Add source to destination
B/W: 0 = 16-bits, 1 = 8-bits
As | Ad | d/s| Register | Syntax Description
oo | 0 | as nz3 Register direct. The operand is the contents of Rn. Ag=0
01 1 | ds|nz0,2,3 Indexed. The operand is in memory at address Rn+x.
10 | - | s | 7=0,2,3| @Rn_| Register indirect. The operand is in memory at the address held in Rn.
11 | - | s [n=0,2,3| @Rn+ | Indirect auto-increment. As above, then the register is incremented by 1 or 2.
Addressing modes using RO (PC)
01 1 | ds 0 (PC) [LABEL | Symbolic. x(PC) The operand is in memory at address PC+x.
11 - s 0 (PC) #x Immediate. @PC+ The operand is the next word in the instruction stream.
Addressing modes using R2 (SR) and R3 (CG), special-case decoding
01 | 1 [ds] 2(SR) [RLABEL] Absolute. The operand is in memory at address x.
10 -|-s 2 (SR) #4 Constant. The operand is the constant 4.
11 - s 2 (SR) #8 Constant. The operand is the constant 8.
00 < s 3 (CG) #0 Constant. The operand is the constant 0.
01 - s 3 (CG) #1 Constant. The operand is the constant 1. There is no index word.
10 : s 3 (CG) #2 Constant. The operand is the constant 2.
ie | s 3 (CG) #-1__| Constant. The operand is the constant -1.

ADD.W
Binary: 0101 0101 0000 0110
Hex: 0x5506

R5,

R6

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 53

Executable Instruction Information

Instruction Operation and Description
Using the MSP430 Quick Reference or Instruction Set

Summa

ADC(.B)
ADD(.B)

ADDC(.B)
AND(.B)
BIC(.B)
BIS(.B)
BIT(.B)

dst

src,dst
src,dst
src,dst
src,dst
src,dst
src,dst

Status Bits

dst + C > dst

src + dst > dst

src + dst + C > dst

src .and. dst > dst
-not.src .and. dst — dst
src .or. dst > dst

src .and. dst

BIS.W #0100h, R6 ;assume initial R6=0x0001
0000 0001 0000 0000

OR_0000 0000 0000 0001

R6=0000 0001 0000 0001 = 0x0101

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 54

Executable Instruction Information

Impact on status flags

Using the MSP430 Quick Reference or Instruction Set

Summa

ADC(.B)
ADD(.B)

ADDC(.B)
AND(.B
BIC(.B)
BIS(.B)
BIT(.B)

dst

src,dst
src,dst
src,dst
src,dst
src,dst
src,dst

Status Bits

dst + C > dst

src + dst > dst

src + dst + C > dst

src .and. dst > dst
-not.src .and. dst — dst
src .or. dst > dst

src .and. dst

ADD.W #8123h, R6 ‘assume initial R6=0x9001
1000 0001 0010 0011

+ 1001 0000 0000 0001

R6=0001 0001 0010 0100 = 0x1124

N=0, V=1, C=1, Z=0

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 55

Executable Instruction Information

Length and Clock Cycle
Using the Instruction Set Summary
Address Mode #of cycles Length of
As Ad instruction
00, Rn 0,Rm 1 1
0,PC 2 1
00, Rn 1, x(Rm) 4 2
1, EBE 2
1, &EDE 2
01, x(Rn) 0,Rm 3 2
01, EDE 2
01, &EDE
01, x(Rn) 1, x(Rm) 6 3
01, EDE 1, TONI 3
01, &EDE 1, &TONI 3

ADD 3(R4),6(R9)
Length = 3 Words, Cycle = 6
WHY 3-WORDS and 6-CYCLES???

Chpt 4: Introduction to Assembly Language Programming



---
### Slide 56

LEARNING OUTCOMES OF CHAPTER:

f Understand the usage of assembly

_ programming

Understand the structure of an assembly
language program

tie Develop simple programs using the Assembler

7 Directives and Executable Instructions

NEXT UP:
More on
Executable
Instructions!!!

Chpt 4: Introduction to Assembly Language Programming

COMPUTER SYSTEM



---

# Chapter 5: Executable Assembly Instructions



---
### Slide 1

janisation and Architecture

1CT1011: Computer Org

a

ICT1011
Computer Organisation
and Architecture

Chapter 5

Executable Assembly
Instructions

Chpt 5: Executable Assembly Instructions



---
### Slide 2

Executable Assembly Instructions

MSP430 Instruction Set and Emulated Instructions

Executable Instructions

- Data Movement

- Arithmetic

- Logical and Bit Manipulation
- Rotation

- Program Control

Chpt 5: Executable Assembly Instructions



---
### Slide 3

_ Introduction to Assembly Language
Programming

MSP430 Instruction Set and Emulated Instructions

Chpt 5: Executable Assembly Instructions



---
### Slide 4

Instructions and Emulated

Instructions
The MSP430 has 27 Core Instructions

> Opcodes of these instructions can be converted to machine code

In addition, the MSP430 supports another 24 Emulated
Instructions

_» These opcodes are emulated by one of the Core Instruction

> Emulated Instruction does not add any new functionality, but makes
coding easier.

Mnemonic Operation Emulation Description
Arithmetic Instructions

DEC(.B or .W) dst dst-1— dst SUB(.B or .W) #1,dst Decrement destination
DECD(.B or .W) dst dst-2- dst SUB(.B or .W) #2,dst Decrement destination twice
INC(.B or .W) dst dst+1— dst ADD(.B or .W) #1,dst Increment destination
INCD(.B or .W) dst dst+2— dst ADD(.B or .W) #2,dst Increment destination twice

Chpt 5: Executable Assembly Instructions



---
### Slide 5

Introduction to Assembly Language
Programming

Executable Instructions
- Data Movement

Chpt 5: Executable Assembly Instructions



---
### Slide 6

Data Movement Instructions

MOV

The mov instruction provides data movement
between a source and a destination.

The mnemonic is given by mov.x src,dst.
. The suffix .x can be byte (.b) or word (.w).

e Source operand is not modified by the execution.
Status Bits are not affected:

Status Bits

VN ZC
MOV(.B) — src,dst src — dst - « & #

This information can be obtained from the Instruction Set
Summary or the Instruction Set Description documents

Chpt 5: Executable Assembly Instructions



---
### Slide 7

Data Movement Instructions

MOV - "Example

Before execution

deanization andiarchitoctira..
nisa nd Archit /

ili ki aemintr}
=!

oC Thar

ray.

 0x6000
~ 0x6002
 0x6004
(0x6006

R13

Memory map
Before execution

R11 0x6789 ~

R10 0x1234 |
R11 0x0034 |

After execution
MSB is set to 0x00

_ Example: mov.w R13, &0x6000

0x6000

0x6002| Ox!
0x6004
0x6006

Memory map.
After execution

Chpt 5: Executable Assembly Instructions



---
### Slide 8

Introduction to Assembly Language
Programming

Executable Instructions

- Arithmetic

Chpt 5: Executable Assembly Instructions



---
### Slide 9

Arithmetic Instructions

SXT

SxXT sign-extends the sign bit of the lower-order byte in a

register to the remaining higher-order bits (copies bit 7 into
bits 8-15).

/ The mnemonic is given by sxt reg

@ eg. sxt R10 : copies bit 7 in R10 into upper bits 8 to 15 of R10

R10|  0x1284 | R10|

Before execution After’ execution

Chpt 5: Executable Assembly Instructions



---
### Slide 10

SiTpsia Arithmetic Instructions

ADD

@ Adds source operand to the destination operand.

@ The mnemonic is given by add.x src,dst.
e The suffix .x can be a byte (.b) or word (.w)
¢ Result is stored in the destination.

Status Bits : Set if result is negative, reset if positive
: Set if result is zero, reset otherwise

: Set if there is a carry from the result, cleared if not.
: Set if an arithmetic overflow occurs, otherwise reset

1CT1011: Computer Organisation and Architecture

@ €.g. add.b R10,R11 ; add byte contents in R10 and R11
; MSB of R11 is cleared to 0x00
@ eg. add.w #2,R13 ; add 2 to the contents of R13
10

©2024

Steven Wong Chpt 5: Executable Assembly Instructions



---
### Slide 11

Program Statement - Addition

Write an assembly language program to :

e Add the contents of two 16-bit variables stored in
consecutive memory locations.

e Store the result in the third memory location
immediately following the two values.

° Getting started:

e Determine the data and code areas in memory, e.g. .data
section for the variable, .text section for the code

» Determine the label names to give to the two numbers and
result, e.g. N1 and N2 for numbers and A1 for answer.

Chpt 5: Executable Assembly Instructions



---
### Slide 12

SiT isis

Program Solution - Addition

@ Asimple program to illustrate the addition of two
memory variables and the storing of its result to

©2024
Steven Wong

2 P

3 another memory variable.

z .data

§ N1 . space 2 ‘allocate 1 word for variable N1

2 N2 .space 2 allocate 1 word for variable N2

& Al .space 2 allocate 1 word for variable A‘

g

5S . text

. mov .w &N1,R10 move word at N1 to register R10

= mov .w &N2,R11 ;move word at N2 to register R11

2 add.w R11,R10 ;add R10 with R11
mov .W R10, &Al ;save word result in R10 to variable A1
.end

12 Can you find a quicker way to do this???

Chpt 5: Executable Assembly Instructions



---
### Slide 13

2
3
s °@
—
g
5 !lCUO
5
S
-
é
3
=
Q
5
.
5
=
S)
e
®
13

©2024
Steven Wong

Arithmetic Instructions

ADDC

Adds source operand and carry flag (C) to the
content destination operand.

The mnemonic is given by addc.x src,dst.
The suffix .x can be a byte (.b) or word (.w)
Result is stored in the destination.

Status Bits N: Set if result is negative, reset if positive
: Set if result is zero, reset otherwise

C: Set if there is a carry from the MSB of the result, reset if not
: Set if an arithmetic overflow occurs, otherwise reset

€.g. addc.w R10,R11 ;R11=R10+ R11+C
€.g. addc.w #2,R13 ;R13=R13+2+C

Chpt 5: Executable Assembly Instructions



---
### Slide 14

Arithmetic Instructions

Use of ADDC

2 ADDC is often used to support higher-order

_addition

@ For example, write an assembly program to help you add

_two 32-bit numbers;
H’77778888 + H’55556666

_and store the result in two registers, R11 storing bits 0-15
_ of the results and R12 storing bits 16-31 of the results?

#0x7777, R12 ;store the higher 16-bits for 1st num
#0x8888, R11 :store the lower 16-bits for 1* num

#0x6666, R11 ;adds the lower 16-bits

#0x5555, R12 ;add the upper 16-bits as well as the
C-flag from the previous operation

Chpt 5: Executable Assembly Instructions



---
### Slide 15

Arithmetic Instructions

DADD

The source operand and the destination operand are
treated as four binary coded decimals (BCD) with
positive signs.

The source operand and the carry C are added decimally

to the destination operand.
The mnemonic is given by dadd.x src,dst.

e The suffix .x can be a byte (.b) or word (.w)

Result is stored in the destination.

Status Bits : Set if the MSB is 1, reset otherwise
: Set if result is zero, reset otherwise

: Set if the result is greater than 9999.
Set if the result is greater than 99.

: Undefined

Chpt 5: Executable Assembly Instructions



---
### Slide 16

Arithmetic Instructions

ADD vs DADD (An Example)

Example: add.w R10,R11

-R10| 0x1234 R10| 0x1234
R11 0x6789 R11 | 0x7 9BD
Before execution After execution

Example: dadd.w R10,R11

R10|  0x1234 | R10| 0x1234
R11|  0x6789 R11/  0x8023
Before execution After execution

DADD.W treats the contents as decimal numbers.
ADD.W treats the contents as binary numbers.

Chpt 5: Executable Assembly Instructions



---
### Slide 17

SiT psy

§
3 @
=
£
<=
co]
5
§
2
3
‘
3
5
S
5
S @
°
ry

17

©2024
Steven Wong

Arithmetic Instructions

SUB

@ The source operand is_ subtracted from the

destination operand.

This is made by adding the 2's complement of the source
operand to the destination operand. The status bits are
set/cleared based on this addition operation

dst + (- (src)) > dst

Status Bits : Set if result is negative, reset if positive
: Set if result is zero, reset otherwise

: Set if there is a carry from the result, cleared if not.
: Setif an arithmetic overflow occurs, otherwise reset

The mnemonic is given by sub.x src,dst.

The suffix .x can be a byte (.b) or word (.w)

e.g. sub.b R10,R11 ;substract byte contents in R10 and R11
; MSB of R11 will be cleared to 0x00

Chpt 5: Executable Assembly Instructions



---
### Slide 18

Arithmetic Instructions

SUBC

Subtracts source operand and carry flag (C) from
content of the destination operand.

Similar to addc, subc is used to support subtraction of
numbers that are >16-bits.

CCR flags are affected as in the sub .b instruction

Chpt 5: Executable Assembly Instructions



---
### Slide 19

Arithmetic Instructions

Use of SUBC

@ Like ADDC, SUBC is often used to support

higher-order addition

@ For example, write an assembly program to help you

= subtract two 32-bit numbers;
H’77778888 - H’55556666

_and store the result in two registers, R11 storing bits 0-15
_ of the results and R12 storing bits 16-31 of the results?

#0x7777, R12 ;store the higher 16-bits for 1st num
#0x8888, R11 :store the lower 16-bits for 1* num

#0x6666, R11 ;subtract the lower 16-bits

#0x5555, R12 subtract the upper 16-bits as well as
the C-flag from the previous operation

Chpt 5: Executable Assembly Instructions



---
### Slide 20

Arithmetic Instructions

Emulated Arithmetic Instructions
7 additional arithmetic instructions

can be emulated using the core arithmetic
instructions.

Mnemonic Operation Emulation Description
Arithmetic Instructions
ADC(Bor.W) dst dst+C-rdst ADDC(B or W) #0,dst Add carry to destination
DADC(Bor.W) dst  dst+C-rdst (decimally) DADD(B or .W) #0,dst Decimal add carry to destination
| DEC(Bor.W) dst —dst-1rdst SUB(B o.W) #1,dst Decrement destination
‘| peco(e or W)dst — dst-2->dst SUB(.B or .W) #2,dst Decrement destination twice
INC(Bor.W) dst dst+1->dst ADD(B or.W) #1,dst nerement destination
INCD(Bor.W) dst  dst+2-rdst ADD(.B or W) #2,dst nerement destination twice
SBC(.B or.W) dst dst+OFFFFh+C->dst SUBC(.B or .W) #0,dst Subtract source and borrow /.NOT. carry
dst+0FFh dst rom dest.

Chpt 5: Executable Assembly Instructions



---
### Slide 21

Introduction to Assembly Language
Programming

Executable Instructions

- Logical and Bit Manipulation

Chpt 5: Executable Assembly Instructions



---
### Slide 22

Logical and Bit Manipulation
Logical Operations

Like most CPUs, logical operation between the
source and destination operands can _ be
computed and the result stored into the
destination.

» 3 logical operations are supported by the MSP430 core
instructions: and, bis (same as logical OR) and xor.

» The way that the status bits are affect varies with the
logical operation used.

» The source operand can either be a register or an
immediate value.

Chpt 5: Executable Assembly Instructions



---
### Slide 23

SiT es Logical and Bit Manipulation
and, bis and xor

@ Logical instructions are used for the following purpose:
¢ and - Clear specific bits in the destination register.

@ bis — set specific bits in the destination register (it’s aOR
operation).

e xor-—complement specific bits in the destination register.

1CT1011: Computer Organisation and Architecture

AND truth table OR truth table XOR truth table
0 0 0 0 O 0 0 0 0
0 il 0 Gi a it QO 1 1
: wv 0 ~ © 1 1 0 1
oe 1 a 1 = 0
A logical 0 is used A logical 1 is used A logical 1 is used

of clear to set to complement

©2024
Steven Wong

Chpt 5: Executable Assembly Instructions



---
### Slide 24

Instruction examples — and, bis, xor

Bits 76543210

Initial conditions of byte-sized register R10 and CCR flags

N: Set if MSB of result is set, reset if not set
Set if result is zero, reset otherwise

and.b # Litt (@) (@) @) Ob r R1 (@) c Set if result is not zero, reset otherwise ( = .NOT. Zero)

Reset

Bit 0 to 3 cleared
after execution

bis.b #11110000b R10 Bis do not change the status bits
° ’

Bit 4 to 7 set
after execution

R10|B’ 01¢

: Set if MSB of result is set, reset if not set

: Set if result is zero, reset otherwise

: Set if result is not zero, reset otherwise ( = .NOT. Zero)
: Set if both operands are negative

Bit 4 to 7 inverted
after execution

%

fe)

5

oy
Sk
a
ay
pany
a
fo)
(>)
fo)
(2)
oy
aw
Se
(oe)

<SONZ

Chpt 5: Executable Assembly Instructions



---
### Slide 25

SiTpcey Logical and Bit Manipulation

BIC

@ Other than the bit-set instruction bis, there is also
a bit-clear instruction bic

e The inverted source operand and the destination operand
are logically AND'ed. The result is placed into the
destination.

.NOT.srce .AND. dst -> dst

@ The mnemonic is given by bic.x src,dst.
e The suffix .x can be a byte (.b) or word (.w)

e The status flags are no affected.
¢ €g. bic.b #11101100b,R11

R11] 01010000b |——p R11}/00010000b

Before execution After execution

1CT1011: Computer Organisation and Architecture

25

©2024
Steven Wong

Chpt 5: Executable Assembly Instructions



---
### Slide 26

Logical and Bit Manipulation

Emulated Bit Manipulation Instructions
Other than the core instruction, the programmer

can also modify certain bits (e.g. the status bits)
using the emulated instructions.

Mnemonic
Data Instructions

- | CLR(B or.W) dst
| CIRC
| CURN
| cLRZ
INV(.B or W) dst

SETC
SETN

SETZ

Operation Emulation

(dst

ae

QN

2
NOT.dst>dst
19(

1>N

17

MOV(.B or.W) #0,dst
BIC #1,5R
BIC #4,5R
BIC #2,5R
XOR(.B or .W) #0(FF)FFh dst

BIS #1,5R
BIS #4,5R

BIS #2,5R

Chpt 5: Executable Assembly Instructions

Description

Clear destination

Clear carry flag

Clear negative flag
Clear zero flag

Invert bits in destination
Set carry flag

Set negative flag

Set zero flag



---
### Slide 27

Introduction to Assembly Language
Programming

Executable Instructions

- Rotation

Chpt 5: Executable Assembly Instructions



---
### Slide 28

Rotation Instructions
Summary of Rotation Instructions

Rotation instructions are use to rotate bits within
the destination operand

2 types of rotations: Arithmetic or “Through Carry”

A visual summary of the operation for all the shift
and rotate instructions:

word 15 word 15 0

0
RRA Cc >
a :

RLA bye 7

word 15 0 word 15 0

ae AH IRE

RLC) byte 7 0 a ;

Left Right

Chpt 5: Executable Assembly Instructions



---
### Slide 29

SiTp Rotate Right through Carry

RRC

@ The destination operand is shifted right one position. The
carry C is shifted into the MSB, the LSB is shifted into the

carryC. word 15 0
byte 7 0

@ The mnemonic is given by rrc.b dst / rre.w dst

N: Set if result is negative (MSB = 1), reset otherwise (MSB = 0)
Set if result is zero, reset otherwise

Loaded from the LSB

Reset

= 2

1CT1011: Computer Organisation and Architecture

mm ©€.g. rre.b Ril
R11/01010000b |————» R11/10101000b

29

©2024

Steven Wong Chpt 5: Executable Assembly Instructions



---
### Slide 30

SiT isis Rotate Left through Carry

RLC (emulated instruction using ADDC)
@ The destination operand is shifted left one position. The

carry C is shifted into the LSB, the MSB is shifted into the
carry C. word 15 0

@ The mnemonic is given by rlc.b dst / rlc.w dst

Status Bits N: Set if result is negative, reset if positive

Set when Z: Set if result is zero, reset otherwise

change of C: Loaded from the MSB
sign V: Set if arithmetic overflow occurs otherwise reset

1CT1011: Computer Organisation and Architecture

m= ©€.g. rlie.b Ril
R11]/01010000b |————» R11/10100001b

N=0, Z=0, V=0, C=1_ N=1, Z=0, V=1, C=O

30

©2024
Steven Wong

Chpt 5: Executable Assembly Instructions



---
### Slide 31

SiTp Rotate Right Arithmetically

RRA

@ The destination operand is shifted right one position. The
MSB is shifted into the MSB, the MSB is shifted into the
MSB-1, the LSB+1 is shifted into the LSB.

word 15 0

Cc] pL >
byte 15 ie)

e The mnemonic is given by rra.b dst / rra.w dst

Status Bits N: Set if result is negative, reset if positive
Z: Set if result is zero, reset otherwise

C: Loaded from the LSB

1CT1011: Computer Organisation and Architecture

@ eg. rra.b R11
R11/01010000b |————» R11/00101000b

31

©2024

Steven Wong Chpt 5: Executable Assembly Instructions



---
### Slide 32

SiT isis

1CT1011: Computer Organisation and Architecture

32

©2024
Steven Wong

Rotate Left Arithmetically

RLA (emulated instruction using ADD)

word

15 0

oye = -- =~ --------| 0

byte

e The mnemonic is
Status Bits

Set when
change of

7 0

C: Loaded from the MSB
V: Set if an arithmetic overflow occurs -

m €.g. rla.b Ril

@ The destination operand is shifted left one position. The
MSB is shifted into the carry C, the LSB is filled with 0.

given by rla.b dst / rla.w dst

N: Set if result is negative, reset if positive
Z: Set if result is zero, reset otherwise

R11

01010000b |————» R11/10100000b

Chpt 5: Executable Assembly Instructions

N=1, Z=0, V=1, C=0



---
### Slide 33

= e.g. B’ 00000100 (4) —

Rotation Instructions

Rotate to Multiple or Divide

Arithmetic rotation performs multiply (shift left) or

divide (shift right) by a factor of 2", where Nis the no.
_of bits shifted.

shift left 2 bits (x4) 5, 99910000 (16)

hift right 1 bit (2 ,
SIREN AGREE BIR A) es 00000010 (2)

2 RRA ® Supports Division (+2) by rotating bits

one bit right

RLA =» Supports Multiplication (x2) by rotating
bits one bit left

Chpt 5: Executable Assembly Instructions



---
### Slide 34

SiT isis

exchanged.

affected

1CT1011: Computer Organisation and Architecture

15

Swap Bytes

SWPB

@ The mnemonic is given by swpb dst

8 7

@ The high and the low bytes of the destination operand are

e Only supports word-sized operations, no status bits

0

@ e.g. swpb R11

R11

OxAABB

34

©2024
Steven Wong

Chpt 5: Executable Assembly Instructions

OxBBAA



---
### Slide 35

Introduction to Assembly Language
Programming

Executable Instructions

- Program Control

Chpt 5: Executable Assembly Instructions



---
### Slide 36

Program Control Instructions

These instructions facilitate the disruption of a
program’s normal sequential flow.

e The disruption of sequential flow is implemented using a
jump or a conditional jump instruction.

» Ajump can be obtained by modifying the contents of the
_ Program Counter (PC).

» Ajump can be executed based on a given condition (e.g. if
result of previous execution is negative) and this is called a
conditional jump.

e@ Conditional jump is useful for implementing:
- conditional constructs (e.g. if or if-else)
- loop constructs (e.g. for or while loops)

Chpt 5: Executable Assembly Instructions



---
### Slide 37

These 8 jump instructions are used to direct program flow to

Program Control Instructions
Jump Instructions (recap)

another part of the program.

Mnemonic

Description

Program flow control instructions

JEQ/JZ label
JNE/JNZ label
JC label

JNC label

JN label

JGE label

JL label

JMP label

Jump to label if zero flag is set

Jump to label if zero flag is reset
Jump to label if carry flag is set
Jump to label if carry flag is reset
Jump to label if negative flag is set
Jump to label if greater than or equal
Jump to label if less than

Jump to label unconditionally

“label” is where the program will jump to if the conditions are

met.



---
### Slide 38

15 14

13

Program Control Instructions
Jump Instructions (recap)

12 11 10 9

8 7 6 5 4 3 2 1

0

Op-code

Condition

10-bit, 2’s complement PC offset

Jump instructions are used to direct program flow to

another part of the program.

The condition on which a jump occurs depends on the

Condition field consisting of 3 bits:
— 000: jump if not equal (Z = 0)
— 001: jump if equal (Z=1)

— 010: jump if carry flag equal to zero (C = 0)
— 011: jump if carry flag equal to one(C = 1)
— 100: jump if negative (N = 1)
— 101: jump if greater than or equal (N = V)
— 110: jump if lower (N # V)
— 111: unconditional jump

Chpt 5: Executable Assembly Instructions



---
### Slide 39

Program Control Instructions
Jump Instructions (recap)

» Jump instructions are executed based on the current PC
and the status register

Conditional jumps are controlled by the status bits
Status bits are not changed by a jump instruction

The jump off-set is represented by the 10-bit, 2’s
complement value:
x2

PC... = PC,, +2 +PC

PC. is the address of the Jump instruction

offset

Chpt 5: Executable Assembly Instructions



---
### Slide 40

Program Control Instructions
Conditional jump example

E.g. loop: SETZ
jz loop

Note: This is an example of
a disastrous infinite loop

* jz and jeq are the same instruction

H’ 001000
H’ 001001
H’ 001002
H’ 001003
PC—> H’001004

Before executing
jz loop

Memory map
(Code area)

After jz loop instruction is fetched After execution

from code memory, PC points to next
instruction at 0x1004.

Chpt 5: Executable Assembly Instructions



---
### Slide 41

SiT es Program Example
Implementing a simple count loop

@ Consider the task of writing 0’s to 10 bytes of
memory starting at address 0x2400:

mov.w #10,R12 sload 10 into counter register
mov.b #0,R10
» Loop mov.b R10,0x2400-1 (R12)

sub.w #1,R12 ;subtract 1 from counter register
| __ jne loop ;skeep looping back 10 times

j—

1CT1011: Computer Organisation and Architecture

loop back Continue sequential execution if result is zero
if result is (i.e. exit count loop)
not zero

Implementation using register indirect with
aa pre-decrement and the jne conditional test

©2024
Steven Wong Chpt 5: Executable Assembly Instructions



---
### Slide 42

SiT es

2

3

= °

£

=

2 @

o

s

2

:

3

3

Q

§

oO

= «6

S

‘

g @
e

42

©2024
Steven Wong

Program Control Instructions

Testing Unsigned and Signed Values

@ Appropriate conditional test must be selected

based on the number representation used.

For testing signed values, use JGE, JL, JN

e.g.

test

cmp.w R12,R11
jge test ;jump to test if R12 is greater

For testing unsigned values, use JLO, JHS

e.g.

R1>R2

cmp.w R2,R1
JLo test ;branch to R1>R2

Chpt 5: Executable Assembly Instructions



---
### Slide 43

Program Control Instructions

Bit Testing

. Bit testing can be used to control program flow;

. Hence, the CPU provides an instruction to test

the state of individual or multiple bits;

. The operation performs a logical & (AND)

operation between the source and destination
operands;

» The result is ignored and none of the operands

are changed.

Chpt 5: Executable Assembly Instructions



---
### Slide 44

Program Control Instructions

BIT

@ The source operand and the destination operand are
logically AND'ed. The result affects only the Status Bits.
The source and destination operands are not affected.

@ Usually used to check if certain bits of the destination are
set/cleared before a conditional jump instruction.

=]
a

e The mnemonic is given by bit.x src,dst

: Set if MSB of result is set, reset if not set
Set if result is zero, reset otherwise

C: Set if result is not zero, reset otherwise (.NOT. Zero)
V: Reset

1CT1011: Computer Organisation and Architecture

@ eg. bit.w #0x0080,R11
R11 0x00CC ——P> R11 0x00CC

44

©2024

Steven Wong Chpt 5: Executable Assembly Instructions



---
### Slide 45

1CT1011: Computer Organisation and Architecture

45

©2024
Steven Wong

Program Control Instructions

CMP

The source operand is subtracted from the destination
operand. The two operands are not affected and, the
result is not stored; only the status bits are affected.

Usually used to compare two values before a conditional
jump instruction.

The mnemonic is given by cmp.x src,dst

Status Bits

N: Set if result is negative, reset if positive (src >= dst)
Z: Set if result is zero, reset otherwise (src = dst)
C:

Set if there is a carry from the MSB of the result, reset if not
V: Setif an arithmetic overflow occurs, otherwise reset

0x0012 + (— 0x0014) = 0x0012 + OxFFEC = OxFFFE
e.g. cmp.w #0x0014,R11
R11 0x0012 ——> R11 0x0012

Chpt 5: Executable Assembly Instructions



---
### Slide 46

Program Control Instructions

]
B

TST (emulated instruction using cmp)

Mnemonic Emulation Description
TST(.B or .W) dst CMP(.B or .W) #0,dst Test destination

@ Used to test if a value is Neg or Zero. The destination
Operand is compared to zero. The status bits are set
according to the result. The destination is not affected.

@ The mnemonic is given by tst.x dst

Set if destination is negative, reset if positive
: Set if destination contains zero, reset otherwise
Set

Reset.

SONS]

1CT1011: Computer Organisation and Architecture

e@ eg. tst.w R11
R11 0x80CC ——»> R11 0x80CC

46

©2024

Steven Wong Chpt 5: Executable Assembly Instructions



---
### Slide 47

Program Control Instructions
BR (emulated instruction) / JMP

» The BR instruction allows branch without any
constraint to be performed

» The mnemonic is given by br dst

» Actual instruction is mov dst,RO

» In addition to the BR instruction, it is possible to
jump to a destination using the unconditional
jump instruction:

jmp dst

Chpt 5: Executable Assembly Instructions



---
### Slide 48

Program Control Instructions

Conditional Jump Examples
Conditional jump - Jump if equal (Z = 1):

JEQ destination or JZ destination

labell:
MOV 0x0100,R5
MOV 0x0100,R4
CMP R4,R5
JEQ labell

. The above example compares the contents of registers R4
and Rd;

» As they are equal, the flag Z is set, and therefore, the jump
to address label1 is executed.

Chpt 5: Executable Assembly Instructions



---
### Slide 49

Program Control Instructions

Conditional Jump Examples
Conditional jump - Jump if different (Z = 0):

JNE destination or JNZ destination

label2:
MOV #0x0100,R5

MOV #0x0100,R4
CMP R4,R5
JINZ label2

. The above example compares the contents of registers R4
and Rd;

» As they are equal, the flag Z is set, and therefore, the jump
to address label2 is not executed.

Chpt 5: Executable Assembly Instructions



---
### Slide 50

Summary

LEARNING OUTCOMES OF CHAPTER:

e¥ Understand and be able to use the core

-~MSP430 executable instructions which can be
grouped into the following categories: Data
Movement, Arithmetic, Logical and _ Bit
Manipulation, Rotation and Program Control
_ instructions

NEXT UP:

The Stack and
modular
programming

COMPUTER SYSTEM

Chpt 5: Executable Assembly Instructions



---

# Chapter 6: Modular Programming



---
### Slide 1

ICT1011
Computer Organisation

and Architecture
Part Il

Dr. Xin Lou



---
### Slide 2

SIT Internal

Acknowledgments

| would like to thank Prof. Wong
for sharing his slides for the
second half of 1CT1011



---
### Slide 3

SIT Internal

ICT1011
Computer Organisation
: and Architecture
g
3 Chapter 6
: Modular Programming
: ORC
Ta
ous
3 J Join at
slido.com

©2024
Steven Wong & ¥
Ta Chapter 6: Modular Programming #1CT101 1 Pt2


---
### Slide 4

SIT Internal

What We Have Learned So Far?
1. The Fundamental of Computer
| 2. The Central Processing Unit
| 3. Instruction Set Architecture

is 4. Assembly Language Programming

n
= re}
Ww +
oD = 5
> Firmware / =

)
” Drivers
ol: ; :
wi! : Instruction Set Architecture :
a) +x
s Input / CPU| 2
ro) Output Memory Fa
O Transistors / Gates 5


---
### Slide 5

SIT Internal

What Will We Learn Today?

Subroutines and the Stack
CALL (call a subroutine)

RET (return from a subroutine)
Parameter Passing Methods

Subroutine Local Variables

Chapter 6: Modular Programming


---
### Slide 6

Ree SIT Internal P
ai Modular Program Design

@ Large, complex software should be decomposed
into several less complex modules
e Modules can be designed and tested independently

¢ Modules that are general can be re-used in other projects

@ Modules can reduce overall program size as the same
code segments may be required in several places

1CT1011: Computer Organisation and Architecture

©2024
Steven Wong &
Xin Lou



---
### Slide 7

SIT Internal

Modular Program Design

Characteristics of a good software module

» Loose coupling — data within module is entirely
independent of other modules

» Strong modularity — should perform a single logically
coherent task

Chapter 6: Modular Programming


---
### Slide 8

SIT Internal

Subroutines

2 Modules are implemented as subroutines

. The same subroutine (or function in C) can be called from
various parts of the program

' On completion, it returns control to the place immediately
after where the subroutine was called

- Acombination of call and ret allow subroutine calls to be
implemented

Calling program

g

}

Calling and returning from a subroutine

Chapter 6: Modular Programming

Subroutine



---
### Slide 9

SIT Internal

Subroutines

How to return to the calling program?

_ In order to return to the calling program, a return address
is saved on the system stack before jumping to the
subroutine

Calling program

1»

©
Calling and returning from a subroutine

Chapter 6: Modular Programming

Subroutine



---
### Slide 10

Fite Revision bf Stack Pointer

R1 — Stack Pointer (SP)

Bit 15 1

SP Stack Pointer Bits 15 to 1 0

¢ The stack pointer (SP/R1) is used by the CPU to store the return
addresses of subroutine calls and interrupts. It also can be used to
store local data and pass parameters

* It uses a pre-decrement, post-increment scheme. SP always point to
a RAM location and is always even

* Examples
—- PUSH #0123h ; Put 0123h onto Top of (Stack TOS)
- POP R8 ; R8 = 0123h

1CT1011: Computer Organisation and Architecture

Addr Content Addr Content Addr Content
1008h 1008h 1008h
1006h 1006h 1006h
1004h SP 1004n 1004h [SP
1002h 1002h| 9123h /€"SP 1002h} 0123h

49 %.1000h 1000h 1000h

©2024 PUSH #0123h POP R8

art hors & Chapter 6: Modular Programming R8 = 0123h


---
### Slide 11

SIT Internal

System Stack in the MSP430

| The system stack is very important in all
_ microprocessor systems

Besides subroutine calls, the system
stack is also used in exception
_handling, and as a temporary storage Flash
area for local variables and
subroutine parameters

» Since a stack grows towards lower OXEFEF
zi, Ys , F : : gee] INT Vectors
memory, it is maintained in high RAM

area, starting from anevenaddress ™“”
0x4400

0x2400 ~

oxoico. USB RAM
J Info Memory
grows towards | Boot Loader

—_ } Peripherals
Peripherals
Chapter 6: Modular Programming 0x0000

‘F5529 Memory Map

128K

80

8K

2K
512
2K

4K


---
### Slide 12

| Start address
of instructions

Subrout

Calling program

=r ey Tr 4
CTIR1
nal #SUB

Next instruction

a

SIT Internal

ines and the System Stack

» In order to return to the calling program, a return
address is saved on the system stack before

jumping to the subroutine

| The return address is the current PC contents, which

points to the start address of the instruction immediately
after call

Push PC to stack before jump

Subroutine

Pop stack into PC to return
Chapter 6: Modular Programming


---
### Slide 13

SiTp a SIT Internal
INSTITUTE OF
TECHNOLOGY

Assume the SP is initialized to 0x3400. The following two
16-bit values are pushed to the stack: 0x1122 and
0x3344. What value will be held in SP?

A.0x3404
B.0x3402
C.0x33FE
D.0x33FD
E. Ox33FC

1CT1011: Computer Organisation and Architecture

13

©2024

Steven Wong & 5 A
Xin Lou Chapter 6: Modular Programming


---
### Slide 14

omnaroie: SIT Internal
INSTITUTE OF
TECHNOLOGY

Assume the SP is initialized to 0x3400. The following two
16-bit values are pushed to the stack: 0x1122 and
0x3344. What value will be held in SP?

A.0x3404
B.0x3402
C.0x33FE
D.0x33FD
E. 0x33FC

1CT1011: Computer Organisation and Architecture

14

©2024

Steven Wong & 5 A
Xin Lou Chapter 6: Modular Programming


---
### Slide 15

SIT Internal

Modular Programming

CALL (call a subroutine)

Chapter 6: Modular Programming


---
### Slide 16

SIT Internal

CALL

. | call pushes a return address onto the system
_ stack before jumping to the effective address

« Return address (i.e., current PC content) occupies 2
_ bytes on the stack

¢ SP or R1 is decremented by 2 since the stack grows
towards lower memory

System stack grows after every execution of call

« Care must be taken when implementing many nested
subroutine calls as risk of stack overflow may occur

@ IMPORTANT: Make sure that R1 is initialised to a
valid address in RAM

Chapter 6: Modular Programming


---
### Slide 17

SH SIT Internal
a Instruction Example - call

®@ E.g., call #0x5000

] Return
; address
° 0x4004
=
g : 0x4003
£ 0x4002
& 0x4001
5 ;
3 PC 0x4000 Return address (i.e., current PC sP
8 ; Memory map content) occupies 2 bytes on the
spe ee cal 0x3402
a 1 push
5 0x3402
= 0x3401
5 SP—> 0x3400
- / 0x33FF 0x3400 =
: emory map
0x33FE SP (stack area)
Memory map * SPis decremented by 2 since the stack grows
(stack area) towards lower memory :
e Fetched but before execution After execution
coer goraraee Chapter 6: Modular Programming


---
### Slide 18

SIT Internal

Modular Programming

RET (return from a subroutine)

Chapter 6: Modular Programming


---
### Slide 19

SIT Internal

RET

y ret returns from a subroutine by popping the
return address from the stack into the PC

« Return address currently on the top of the stack is
popped off as a word and placed in the PC

@ This increments contents in SP by 2
Note: Any PUSH operations to the stack done within the

subroutine must be accompanied by the appropriate pops
before ret is executed. This ensures the return address is

currently at the top of the stack at the point of executing
ret. ,

Chapter 6: Modular Programming



---
### Slide 20

Sit] BY SIT Internal

s
PC—> 0x4004
Fr 0x4003
0x4002
0x4001
0x4000

hor 4
{

re

ents

_ 1CT1011: Computer Organisation and Architecture

* Return address is popped off as a

F. Instruction Example - ret
@ E.g., call #0x5000 (return from subroutine)

PC
0x3400
SP

Memory map F
: word and placed in the PC
a (Code area) 0x3402
rh 0x3401
¢
5 SP—> 0x3400
. 0x33FF
5-1 18. SP 0x33FE
=, Memory map
sP> (stack area)
tie 2054 Memory map * SPs incremented by 2
20 (stack area)
ex Run the subroutine until ret After ret
‘Steven Wong & Chapter 6: Modular Programming

Xin Lou


---
### Slide 21

SIT Internal

Modular Programming

Parameter Passing Methods

Chapter 6: Modular Programming


---
### Slide 22

SIT Internal

Parameter Passing

_ Calling programs often need to pass parameters to
_ influence a subroutine’s execution

» Parameters must be setup properly before the subroutine
_ Is called, and appropriately removed after returning to the
_ Calling program

Subroutine

Parameter passing
Chapter 6: Modular Programming


---
### Slide 23

SIT Internal

aye NS

isiT) a
SITE
a Reser

_How can we pass parameters

5 i,
Tails

?

i tern aps er tse oh sat tend ag BT aS AN porte:
SU Piette | te sh ge Bh as He Bae
+a ea ti Reet = ef i

Beit shite eal tity tate Bien

=!
‘Ta
reat)

Chapter 6: Modular Programming



---
### Slide 24

SIT Internal

Parameter Passing

@ There are three basic methods to pass parameters,
via registers, memory block or the system stack

Subroutine

Parameter passing

Chapter 6: Modular Programming


---
### Slide 25

SIT Internal

Modular Programming

Parameter Passing Methods
- Registers

Chapter 6: Modular Programming


---
### Slide 26

SIT Internal

Parameter Passing using Registers

Parameters are placed into the registers before

Calling the subroutine
@ Pros

— Very efficient as parameters are already in register within the
_ subroutine and can be used immediately

-— Useful when number of parameters are small

e@ Cons

— Reduces the number of available registers within subroutine
— Lacks generality due to the limited number of registers

Analogy:
Messenger for quick hand-delivery

Subroutine

Chapter 6: Modular Programming


---
### Slide 27

SIT Internal

Parameter Passing using Registers Example

Bit Counting Subroutine

~(JWrite a subroutine to:
e@ Count the number of “1” bits in a word

» Return the result as a byte in register R10
LJ Design considerations:

How do we transfer the word into the subroutine?
- Put the word into a word-sized register, which can then
be accessed within the subroutine, e.g., register R11.

How do we check if each individual bit is a “1” or a “0”?

-- Rotate R11 left 16 times and after each rotation we test
the carry bit to decide if the bit counter (i.e., R10) should

be incremented. nr

bit R11
LJ—LLTITTTITtTitittit ttt ty

Chapter 6: Modular Programming


---
### Slide 28

SIT Internal

~ Quick Recap on Program Control
3 Instructions

Conditional jump; PC = PC + 2xoffset

JNE/JNZ Jump if not equal/zero
JEQ/JZ Jump if equal/zero

JNC/JLO Jump if no carry/lower
JC/JHS Jump if carry/higher or same

JN Jump if negative
JGE Jump if greater or equal

JL Jump if less
JMP Jump (unconditional

Chapter 6: Modular Programming


---
### Slide 29

SIT tin

Bit Counting Subroutine
Possible Solution

. text

,|BitCnt push.w R12 ;save register used within subroutine to stack
3 rons
8 mov.b #16,R12 sinitialize loop counter with 16
8 mov.b #0,R10 ;Clear bit counter register to zero
E Loop rlc.w R11 ;rotate word in R11, so MSB goes into C-flag
$ jnc Skip ;skip increment if C-flag is cleared
: inc.b R10 increment bit counter by 1 if C-flag is set
S Skip dec.b R12 ;decrement 1 from loop counter register
5 jne Loop ‘branch back to Loop if not zero
5 pop.w R12 ‘restored saved register before returning
5 ret ‘return from subroutine
i
iS) .end

R10 = register to pass out result. R11 = register to pass parameter R12 =Loop counter

Note: The subroutine uses R12 but returns its content to its original
29 form on returning to the calling program as R12 may be used by

steven Weng the Calling program

Xin Lou

Chapter 6: Modular Programming



---
### Slide 30

SIT Internal

Bit Counting Subroutine
Alternative Solution

BitCnt
Loop

Done

. text

mov.b #0,R10
rla.w Ril

jeq Done
addc.b #0,R10
jmp Loop
addc.b #0,R10
ret

.end

‘Clear bit counter register to zero

;shift word in R11, so MSB goes into C-flag
‘branch to Done if no more 1’s in R11

;add C-flag to contents in R10

‘loop back

;add C-flag to contents in R10

‘return from subroutine

1CT1011: Computer Organisation and Architecture

R10 = register to pass out result

Note:

1. Unlike the solution #1, the parameter passed in is destroyed
2. This example shows one of the uses of the addc instruction

30

©2024
Steven Wong &
Xin Lou

R11 = register for passing parameter

Chapter 6: Modular Programming



---
### Slide 31

SIT Internal

Modular Programming

Parameter Passing Methods

- Memory

Chapter 6: Modular Programming


---
### Slide 32

SIT Internal

Parameter Passing using Memory

@ A region in memory is treated like a mailbox and is

used by both the calling program and subroutine

» Parameters to be passed are gathered into a block ata
_ predefined memory location

¢ The start address of the memory block is passed to the

subroutine via an address register
Useful for passing large number of parameters

» Itis also called “passing by reference”

Analogy:
Share folder/mailbox

Subroutine

Chapter 6: Modular Programming


---
### Slide 33

omnaroie: SIT Internal
INSTITUTE OF

wake Parameter Passing using Memory Example

Lower to Upper Case Subroutine
LWrite a subroutine to convert an ASCII string from

lower to upper case
¢ The string is terminated by a NULL character (H’ 00)

¢ The start address of the string is passed via R11

LY Asegment of the calling program showing how the
parameter is setup and the subroutine is called:

String trang ‘a’; p' ;'p ;"1/ ,7Se" 00h

1CT1011: Computer Organisation and Architecture

mov .W #String,R11 ;move start addr. of string to R11
call #Lo2Up ‘branch to Lo2Up subroutine

33

©2024

Steven Wong & ¥
Xin Lou Chapter 6: Modular Programming


---
### Slide 34

SIT Internal

Lower to Upper Case Subroutine

Algorithm Design
How to convert an ASCII character from lower to

upper case?
Check that the character’s value is between ‘a’ and ‘2’.
If so, subtract its value by 32 to make it upper case.

subtract 32
MS
Ls 0 1 2 4 6
@

NUL | DLE SP

SOH | DC1 !
STX | DC2
ETX | DC3
EOT | DC4
ENQ | NAK
ACK | SYN
BEL | ETB
BS CAN
HT | EM

LF | SUB
vt | ESC
FF | FS

cR | GS -
so | RS F
SI US i

ASCIl Character
Set (7-Bit Code)

-@ WH 5
ODAIHDUABWNHE OC] W

a

---_ i)

> A en
OoOnBDBrRPwWUHEFTQAMHOAAAAD -

YHHONWPODIDUARWNHHRO

UV I Awe oe

2 _ DEL
Chapter 6: Modular Programming



---
### Slide 35

rO:
push.w R10

push.w R11
Next mov.b @R11,R10 ;get current char from string in memory
cmp #00h,R10 ‘compare with NULL char
§ jeq Done ‘if NULL char, branch to Done
: cmp.b #’a’,R10 ‘compare with lower limit “a”
2 jn Update if smaller than “a”, do not convert
5 cmp.b #/’z’+1,R10 ;compare with upper limit beyond “z”
8 jge Update ‘if out of range beyond “z”, do not convert
8, add.b #-32,R10 convert to upper case by subtracting 32
3|Update mov.b R10,0(R11) write char back to string in memory
3 inc.w R11 increment pointer to next char in string
6 jmp Next -branch back to Loop
5|Done pop.w Ril ‘restore saved registers betore returning
8 pop.w R10
ret sreturn from subroutine

Note:
Soe VC

©2024
Steven Wong &
Xin Lou


---
### Slide 36

SIT Internal

Modular Programming

Parameter Passing Methods

- Stack

Chapter 6: Modular Programming


---
### Slide 37

“= Parameter Passing using Stack
@ Parameters are pushed onto the stack before
calling the subroutine and retrieved from the stack

within the subroutine
¢ Most general method of parameter passing — no registers
needed, support recursive programming

¢ Number of parameters passed can be quite large, as long as
stack overflow does not occur

() Parameters pushed onto the stack must be removed by the
calling program immediately after returning from subroutine

) If not, repeated pushing of parameters to the stack will lead to a

Analogy:
stack overflow A oile of files

Subroutine
— SUB1

Setup parameters —
4 ] —==~ | :
= ret

1CT1011: Computer Organisation and Architecture

Remove parameters
(depending on passing method)

37

©2024
Steven Wong &

Mis Ta Chapter 6: Modular Programming


---
### Slide 38

SIT Internal

Parameter Passing using Stack Example
Square of Integer Subroutine (X?)

JWrite a subroutine to compute the square of an
unsigned 8-bit byte 'X’
e Value of the 8-bit byte is passed to subroutine

» The word result is stored in a memory location (whose
_ address is also passed in)

_ @ All available registers are required by the calling program
and cannot be used to pass the required parameters

| ] Solution:

e Use the stack to pass byte-sized integer value and word-
_ sized address of result (memory variable) to subroutine

e Use indexed addressing to update memory variable
3 _- within the subroutine

Chapter 6: Modular Programming


---
### Slide 39

a: Square of llitéger Subroutine

Calling the Subroutine

Result .word 1 ;word-sized memory variable

bitecture.

_% mov .b #5,R11 ;put value of x= 5 into R11 (to find square of 5)
22} push.w R11 ‘push integer value onto stack
2£) mov.w  #Result,R11__ ;copy address of Result into R11
B s push.w R11 ;push address of memory variable onto stack
call #Square ‘call subroutine square
add.w #4,R1 ;add 4 to pop the 2-word parameters from
: C ‘the stack
8 Parameters removal

Note: The parameters that were set up before calling the subroutine are
removed immediately after returning from subroutine. This is done by
simply returning the contents of SP to its original value before

39 parameters were pushed to the stack (just prior to the subroutine call)

©2024
Steven Wong &
Xin Lou

Chapter 6: Modular Programming


---
### Slide 40

Subroutine

Solution
Square push.w R10 ;save registers used within subroutine
push.w R11

mov .b 8 (SP) ,R10 _ ;retrieve byte value from the stack
mov .w 6(SP),R11 _ ;retrieve variable’s address from stack

etrieve stack
parameters

mov .w #0, O(R11)_ ;setresult to 0 first
add.w 8(SP), 0O(R11) ; add the byte, x, into result

dec.b R10 ; repeat for x-1 times,
jne sqr ; where x is the value of the byte

:
8
3
:
$
o
g
S
=
S
s
a
§
xs
bad
2
~
cS)

Done pop.w- Ril ;restore saved registers before returning
pop.w R10

40 ret ‘return from subroutine

©2024
Steven Wong &
Xin Lou



---
### Slide 41

eas Square of llitéger Subroutine
Accessing Stack Parameters

Calling program = After) SP _—ox33F6[

mov .b #5,R11
nad After) SP>

push.w
mov .W #Result,R11

O)
@)|push.w R11 After) SP>
©)

call #Square

After(2) SP>

7 Subroutine Square After@) SP>

orn R10
(5)|push.w R11
mov .w 8(SP) ,R10 ae Before (4) sP->

mov.w 6(SP),R11 =~

1CT1011: Computer Organisation and Architecture

0x3400 Memory map
(stack area)

Displacements for stack parameters

Note: Indexed addressing can be used to access parameters on the stack but
41 knowledge of all items on the stack is needed to compute the correct

©2024 iti
Steven Wong & offsets from the current SP POSIOR iar —


---
### Slide 42

SIT Internal

res Square of Integer Subroutine
Returning from the Subroutine

e Parameters pushed onto the stack must be removed/released by the
calling program immediately after returning from subroutine

e If not, repeated pushing of parameters to the stack will lead to a stack

2
3

£ overflow

: Calling program Before(1) SP 0x33F6

: mov .b #5,R11 0x33F7

3 push.w R11 0x33F8

; mov.w #Result,R11 0x33F9

3 push.w R11

: 0x33FA |

3 call #Square ;

: cin His 0x33FB}] Ad

: S ‘ 0x33FC}| Address
8

Subroutine Square

0x33FE

pop.w R11 0x33FF
pop.w R10 0x3400 Memory map

4
3 eet (stack area)
Steven Wong & Chapter 6: Modular Programming

Xin Lou



---
### Slide 43

ai SIT Internal

— s }

n the next slide

sen Pore: Chapter 6: Modular Programming


---
### Slide 44

omnaroie: SIT Internal

res Square of Integer Subroutine
Returning from the Subroutine

e Parameters pushed onto the stack must be removed by the calling
program immediately after returning from subroutine.

e If not, repeated pushing of parameters to the stack will lead to a stack

g
2
£ overflow.
$ scan aa Before) SP 0x33F6
3 nor BR 0x33F7
—a"-* a te Rt After(@) SP 0x33F8
& mov .w Result,R1 pa
3 push.w R11 fetes |
3 call #Square After (2) SsP—> x :
2 @ladd.w #4,R1 Ox33F5 i
= : After (3) SP-> 0x33FC Address
Oo
S m4
Subroutine Square 0x33ED | of Result
: 0x33FE
B pop.w R11 0x33FF
oe |P OP - ¥ R10 After (4) SP—> 0x3400 Memory map
2 ret (stack area)

Steven Wong & : ‘
Xin Lou Chapter 6: Modular Programming


---
### Slide 45

omnaroie: SIT Internal
INSTITUTE OF
TECHNOLOGY

Passing by Value and by Reference

@ Parameters are passed to subroutines in 2 ways:

e Pass by value — the value

Calling program

of the data (or variable) is i. —

passed to the subroutine { push.w
¢ Pass by reference — the { MOV .W

address of the variable is #—“ __ | |Push-w

passed to the subroutine call

#5,R11

R11
#Result,R11
R11

#Square

@ hen is passing by reference used?

1CT1011: Computer Organisation and Architecture

subroutine

« When the parameter passed is to be modified by the

¢ Large quantity of data (e.g., array) have to be passed

45 between subroutine and calling program

©2024

somes one & Chapter 6: Modular Programming



---
### Slide 46

SIT Internal

Modular Programming

Subroutine Local Variables

Chapter 6: Modular Programming


---
### Slide 47

SIT Internal

Program Development Process

C = A higher Level Languages

| Prog.asm Prog.c
.

=|mov.b #0x12,R10
z=] dec.b #1,R10
jne loop

for (x=0;x<12;x++}
continue;

Prog.obj Prog.abs

. . 0x6000
Linking Address Info 0x6002
i 0x6004 ;
01010 "
11011 L | ) 0x600A
: 5/7 —«ox600

Object file Load module
Host PC (for software development)

Assembly

Chapter 6: Modular Programming


---
### Slide 48

SIT Internal

C Function Example

@ C function to compute the mean value of N elements in an
integer Array

Passing by reference Passing by value

int avg, i; - -
ane: aan. = 62 Local variables used only by the function

for (i=0; i<N; i++)

sum = sum + Array[i];
avg = sum / N;
return avg; <———)A function returns a single output

{
}

£

3

g

Mean (int *Array, int N)

Note: Observe that local variables are required by the function
48 Mean to compute the result

©2024
somes one & Chapter 6: Modular Programming


---
### Slide 49

SIT Internal

Local Variables in Subroutines

> Subroutines often use local variables whose
scope and life span exist only during the execution
_ of the subroutine---Short-lived

e Memory storage for these variables is created on
entry into the subroutine and released on exit

from subroutine

e The system stack is the ideal place to create
_memory space for temporary variables

z « This temporary memory space is called the stack
frame, i.e., a block of memory allocated by a
, subroutine to be used for local variables

Chapter 6: Modular Programming


---
### Slide 50

omnaroie: SIT Internal

a Stack Frame

@ A stack frame of N bytes can be created on the
system stack immediately on entry into subroutine

Lower address

int Mean ()

{
SP-> | int avg int avg, i;
int sum = 0;

int i

int sum

function Mean

1CT1011: Computer Organisation and Architecture

SP |Return Address

Stack frame of N=6
bytes created for

Stack after stack three word-sized
Stack on entry f iI éj local variables in
50 into subroutine rame allocation function Mean

©2024

Steven Wong & ¥
Xin Lou Chapter 6: Modular Programming


---
### Slide 51

SIT Internal

_ Accessing Stack Frame Variables
@ The stack frame can be assessed using stack
__ pointer (SP)

Stack Pointer SP>

» Astack frame is created by | sp+02
adding frame size N to SP acaiha

¢ e SPis used as a reference to
access all local variables

_ Appropriate positive displacements Accessing the
_ from SP is used to access any of the cae ISS
_ stack frame variables

Chapter 6: Modular Programming


---
### Slide 52

SIT Internal

Summary — Modular Programming

@ call and ret are the basic instructions for
implementing subroutines

_@ The stack is the most favored method for
parameter passing but a combination of methods
3 may be used (e.g., pass in via stack and pass out via
register)

9 Saving and restoring used registers within a
subroutine is necessary to make it transparent to
the calling program

-@ Local variables within a subroutine are usually

maintained on the system stack

Chapter 6: Modular Programming


---
### Slide 53

SIT Internal

Thank you!

lou.xin@singaporetech.edu.sg

Chapter 6: Modular Programming


---

# Chapter 7: I/O Interfacing Techniques



---
### Slide 1

omnaroie: SIT Internal

ICT1011
Computer Organisation

and Architecture
Chapter 7

and Architecture
—)

Input / Output
Interfacing
Techniques an

Ope

1CT1011: Computer Organisation

1 L J Join at
©2024 slido.com
Si Wong & ; 1 i
age § om Chapter 7: Input / Output Interfacing Techniques #ICT1 011 Pt2


---
### Slide 2

SIT Internal

~ What We Have Learned So Far?

1. The Fundamental of Computer

: 2. The Central Processing Unit
E
: 3. Instruction Set Architecture
| 4. Assembly Language Programming
°
3 = Applications o
S Lu +
io ~ =
5 S Compiler Firmware / 3
S = J i: Drivers °
= Instruction Set Architecture
= [input / CPU a
= Output Memory ¢
ss, oO Transistors / Gates =

sal vont a Chapter 7: Input / Output Interfacing Techniques


---
### Slide 3

SIT Internal

What Will We Learn Today?

1. Basic I/O Interfacing Concepts
Digital Communications
Memory Mapped I/O and Isolated I/O

Polled and Interrupt-driven I/O Technique

7 PF YY Bb

Bluetooth

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 4

Chapter 7:TInput / Output
Interfacing Techniques

. Basic I/O Interfacing Concepts

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 5

SIT Inte

Introduction
The MSP430F5529 Pin Layout

Q
x
5 4 5
zea Fs] 5
Sassexohoess
BS RRs Se 580RR. zs
eVSSSeEEEEE SS an
Soeepissceecs 2 ses538
oooo X77 FMW H HS KF DOADIDDY
aaaa Qaanoagraadtc>>oraaas
aie iatalaiatataiatatatatatatetatalaiata!
SBRRERREKRARKCRGSSSEBSISIS
Pe.aiceaias 1 O 60 [9 P7.7/TBOCLK/MCLK
P6.S/CBS/AS C2 so [1 P7.6/TB04
P6.6/CBE/AS C3 88 1D P7.5/TB0.3
P6.7/CB7/A7 C44 57 FD P7.4/TBO2
P7.O/CB8/A12 [5 $6 [0 P5.7/TB0.1
P7.1/CBY/A13 []6 55 1 P5.6/TBO.0
P7.2ICB10/A14 (7 54 [D P4.7/PM_NONE
P7.3/CB11/A15 C8 53 1 P4.6/PM_NONE
P5.0/A8/VREF+/VeREF+ [Ig §2 [0 P4.5/PM_UCA1RXD/PM_UCA1SOMI
P5.1/AQVREF-VeREF- C] 10 meftipet sinc 51 [0 P4.4/PM_UCA1TXD/PM_UCA1SIMO
AVCC1 C11 MSP430F55251PN so Pp DVCC2
PS.4/XIN (12 MSP430F55211PN 49 [0 Dvss2
P5.5/XOUT C13 48 [0 P4.3/PM_UCB1CLK/PM_UCA1STE
AVSS1 14 47 [D P4.2/PM_UCB1SOMI/PM_UCB1SCL
P8.0 C415 46 [0 P4.1/PM_UCB1SIMO/PM_UCB1SDA
P8.10116 45 [0 P4.0/PM_UCB1STE/PM_UCAICLK
P8.2 C17 44 1D P3.7/TBOOUTH/SVMOUT
OVCC1 C18 43 2 P3.6/TB0.6
DVSS1 []19 42 1D P3.5/TB0.5
s VCORE [20 41 [0 P3.4/UCAORXD/UCAOSOMI
ust by itse es
5 NNNANNNNNNMMMNMMMNMMNMH S
DODDCCCOOTOOOUoOooOooIo
hi ip i EPP EPEEEEEEEP PETS
3 x22 022240 90H
this chip is Sef2ee REE SEZ2S922 25
eee ease e5 8853
Qraasa Sasa shes §$25229
not useful at * 2 § B52832
E x 3°
6 € E ES5a86
a : i 88803
all!!! ° aEEEE
Qaoks
aa a

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 6

SIT Internal

Introduction

In this chapter, we are interested in the interfacing
of the CPU with the memory and the peripherals.

External Waa

o

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 7

SIT Internal

Definitions???

_What are peripherals?
— Oxford English Dictionary states:

“able to be attached to and used with a
computer, though not an integral part of it.”

— Steven’s ICT1011 Dictionary (to be ready by
year 3010) states:

“a unit or device providing peripheral functions
that is connected to the CPU either on the
same chip or different chips”

—ChatGPT says:

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 8

SIT Internal

Definitions???

What is interface?

— Oxford English Dictionary states:

“a device or program enabling a user to communicate
with a computer, or for connecting two items of
hardware or software”

— Steven’s ICT1011 Dictionary states:
“Please refer to the Oxford English Dictionary!!!”

— ChatGPT says:

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 9

SINGAPORE
INSTITUTE OF
SiTpaa

SIT Internal

@ Asystem with CPU and
memory alone is useless

0/1} 2]3 ==
aster] SG
*[8/9/# -_ =
Main nput Output
Pr r
ee Memory Interface Interface

1CT1011: Computer Organisation and Architecture

peripherals

e What types peripherals are

present this watch?
9

©2024

Steven Wong & Chapter 7: Input / Output Interfacing Techniques

Xin Lou

« Evena simple computer, like the
MSP430 Chronos, requires its
processor to be interfaced with

Peripherals and I/O Interfaces

Address
Control


---
### Slide 10

SIT Internal

Peripherals and I/O Interfaces

2 Peripherals connect to a processor in 2 ways:

« Loosely coupled
e via an external bus — USB, SCSI, |?C, Firewire

e via a network — Ethernet, ATM, airport (wireless)
e via a port — serial (RS232), parallel, PS2

« Tightly coupled

e via fast internal bus — graphics & hard-disk controllers

2 Peripherals generally communicate with the CPU
through I/O interfaces

CPU , Peripheral
side 1 side
Address bus ———_______—

Network / Bus

Chapter 7: inl Z Anter Ese facing Techniques


---
### Slide 11

SIT Internal

Introduction to Interfacing

Interfacing is the process of connecting two
devices together so that they can exchange
information

Interface includes

— physical connections (hardware interface)

— the hardware

— a set of rules/ procedures (software, protocols)
— follow some Standards

L) For example, connecting a keyboard to a
computer needs an interface. Similarly, external

memory, hard disk, serial data communication, etc.,
need proper interfaces.

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 12

SIT Internal

Introduction to Interfacing

Digital and Analogue |/O

— An analogue signal is a signal with continuous
voltage levels, i.e., can take any number of values,

— A digital signal has only two values: High or Low

ADC and DAC

— The analogue output of a pressure or temperature
sensor is to be converted into digital form by Analog-
to-Digital Converter (ADC)

— Digital output of processor is to be converted into
analogue form (using a Digital-to-Analog Converter
(DAC)) to control a valve or to regulate speed of a
motor or to produce a sound on a speaker

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 13

SIT Internal

Introduction to Interfacing

Most computers have different types of I/O
subsystems (peripheral modules) and thus
different types of interfacing requirements

_}] For example,

— a set of switches (input device) or a set of LEDs or
-~anLCD display (output device) or a printer can be
connected to an I/O parallel port

-—a keyboard (input device) can be interfaced with
processor through a serial interface
)

Ee)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 14

Chapter 7:TInput / Output
Interfacing Techniques

Digital Communications

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 15

Sie Parallel Data Transfer

« Parallel data communications: more than
one bit of information to be transferred
between the computer and external device

simultaneously
* Faster data transfers: usually done between

the processor and devices those are located

nearby
Example: Computer to transfer the byte H’AA (10101010b) to the device

Computer

1CT1011: Computer Organisation and Architecture

Steven vont & Chapter 7: Input / Output Interfacing Techniques


---
### Slide 16

SIT Internal

Parallel Data Transfer

¢ Microcontrollers (MCU) will usually have
several ports that allow data to be transferred
in parallel between the MCU and the external
devices

SINGAPORE
INSTITUTE OF
TECHNOLOGY

¢ However, to communicate with peripherals
located at a remote places, it is uneconomical
to use parallel mode as it needs too many
wires

1CT1011: Computer Organisation and Architecture

16
©2024

sal vont & Chapter 7: Input / Output Interfacing Techniques



---
### Slide 17

SIT Internal

Serial Data Transfer

* Serial communications allow one-bit of data
to be transferred at a time through two/three
wires

— Data is converted from parallel to serial form
and sent over a single wire or a pair of wires

—lIt is called as serial interface in which data
transfer takes place from point-to-point one bit
at a time
Computer to transfer the byte H’AA (10101010b) to the device

Computer Device

INSTITUTE OF

1CT1011: Computer Organisation and Architecture

10101010

TxD RxD
GND GND
17

©2024 Least Significant Bit (LSB) is transmitted first.

Steven Wong &
Xin Lou

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 18

SIT Internal

What is the data transfer mode for USB flash
drive?

ff tee eee een er oe, ae i
Universal Serial Bus

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 19

SIT Internal

Pros and Cons

¢ Serial data transfers, when compared
with parallel data transfers are:

— Less expensive:
¢ Fewer wires and connections are required

— Slower than parallel:

* In general, slow. But latest serial interfaces, such
as USB 4, can support speeds up to 40Gbits/s or
higher, so it is fast for most common applications.

— More robust.

¢ No cross talk

* No limitations at high frequencies and long range
transmission

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 20

Sth: Usage and Application Examples

¢ Serial communications can be used for:

— Communications between the computer and
devices that are located far away (several
meters to few hundred meters)

— Keyboard and mouse cables and ports
— The cables that carry digital video

MALE 9-PIN

SERIAL PORT

1CT1011: Computer Organisation and Architecture

20

©2024

sal vont & Chapter 7: Input / Output Interfacing Techniques


---
### Slide 21

Th Usage and Application Examples

¢ Internal communications in small devices (e.g.,
between processor and peripheral chips) as less
connections are required

Initialize alnitialize

Camera
Module

10101011

00:14:33 18 Sep 08
KW =

1CT1011: Computer Organisation and Architecture

PillCam™ Si

oes 11001100

sal vont & Chapter 7: Input / Output Interfacing Techniques


---
### Slide 22

SIT Internal

Mode of Transfers

Serial data transfer can be

— Simplex mode: Transmission is in one direction
only

— Example - a temperature sensor sending data
to a monitoring station

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 23

aie Mode of Transfers

¢ Serial data transfer can be

— Half-duplex mode: Transmission takes place
in both directions, but can only occur in one
direction at a time

—Example - a single channel 2-way radio

Computer Asynchronous Half Duplex Device

1CT1011: Computer Organisation and Architecture

23

©2024
Steven Wong &
Xin Lou



---
### Slide 24

SIT Internal

Mode of Transfers

Serial data transfer can be

— Full-duplex mode: Transmission in both
directions simultaneously

— Example - a normal telephone line

— Normally asynchronous transmission refers to
full duplex

Asynchronous Full Duplex

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 25

SiT pass SIT Internal .
How does the receiver know

when the transmission starts?

1CT1011: Computer Organisation and Architecture

We will discuss this in the next a few slides

Steven Won & Chapter 7: Input / Output Interfacing Techniques


---
### Slide 26

omnaroie: SIT Internal
INSTITUTE OF

Synchronous and Asynchronous

¢ Serial data links use the serial interface. Serial
data can be transmitted either in synchronous or
in asynchronous modes

¢ Synchronous transmission:

— A common clock is used between transmitter and
the receiver to synchronize the bit transfers

Synchronous Full Duplex

Clock Source
Computer

1CT1011: Computer Organisation and Architecture

26

©2024

sal vont & Chapter 7: Input / Output Interfacing Techniques


---
### Slide 27

SIT Internal

Synchronous and Asynchronous

¢« Asynchronous character-based transmission:

—No common clock is required between the
transmitter and the receiver

— Information is transmitted, one bit at a time, as
characters comprising of:

° 1 start bit

¢ 7-bit or 8-bits of information
° 1 parity bit (optional)

¢°1, 1.5 or 2 stop bit(s)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 28

SIT Internal

Asynchronous Serial Data Format

- Text information (including alpha-numeric and
control characters) are usually encoded in the
American Standard Code for Information Interchange
(ASCII)

fon)

ee ODIDUBAWNEO] WwW
D4 K~ONKKSECGCHOADONM HN
WH r-AONKEX ECE tHORQUTIN

OZEBYPRGHTOAHAAUVAWDPe!sA
OnpBBRPWUHFPTQMAAATDM =

Oo
1
2
3
4
5
6
7
8
9
A
B
Cc
D
E
F

7-bit ASCII Table

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 29

SIT Internal

Ls Asynchronous Serial Data Format

. The parameters for the serial ports that must be
specified before data communications can occur

are:

_ e the baud rate of the transmission
_e the number of data bits

_ e the sense of the optional parity bit
e the number of stop bits

. Both transmitter and receiver should be
configured with the same parameters

° Each bit is represented by Mark (logic 1) or
_ Space (logic 0)

_ @ When the serial line is idle (no data), it remains in
sw _ the Mark (logic 1) state

Chanter 7: Innit / O1stnist Interfacing Technic iec



---
### Slide 30

SIT Internal

Asynchronous Serial Data

Transmission
Example

Draw the waveform of a 7-bit ASCII character ‘C’

(B’1000011) transmitted on a serial port with 7-bit data,
Even parity ou 1 stop bit and a baud rate of 2400

Start bit

How does the transmitter tell the receiver that it
is going to begin the transmission of the

character?
This is done using the Start bit. As the serial line is Mark (1) when idle, the

transmitter begins transmission by sending a Space (0) bit. This bit is

known as the start bit.
Chapter 7: Input / Output Interfacing Techniques


---
### Slide 31

SIT Internal

Asynchronous Serial Data
Transmission

Example
Draw the waveform of a 7-bit ASCII character ‘C’

(B’1000011) transmitted on a serial port with 7-bit data,

Even parity bit, 1 ae bit and a baud rate of 2400
Data bits ;

How is the data character ‘C’ transmitted?

The character ‘C’ is sent one bit at a time starting from the least significant
bit (so the right most bit is transmitted first). From the ASCII table, ‘C’ is

represented by H’43 or B’100 0011.

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 32

SIT Internal

Asynchronous Serial Data

Transmission
Example

Draw the waveform of a 7-bit ASCII character ‘C’
(B’1000011) transmitted on a serial port with 7-bit data,
Even parity bit, 1 stop bit and a baud rate of 2400

1:14] 0f0:0:0]1] 1:

Pope abe- | —— SUED

Start bit ‘Parity bit

How can error detection be achieved?

If enabled, using the Parity Bit. Even parity means that the total number of
1’s in the transmitted frame, including the parity bit, must be an even
number. In this case, to make the number of 1’s even, parity bit = 1.

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 33

SIT Internal

Asynchronous Serial Data

Transmission
Example
Draw the waveform of a 7-bit ASCII character ‘C’
(B’1000011) transmitted on a serial port with 7-bit data,

Even parity bit, 1 top bit and a baud rate of 2400
i, ; Stop | bit

1i1]0!0!0!0]1 1!

How is the transmission completed?
The transmitter will transmit 1 or 2 Stop Bits. Stop bits are MARK (1)

signals.
After the stop bit(s), the transmitter will set the serial line to MARK (1) to
indicate that the line is idle.

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 34

SIT Internal

Asynchronous Serial Data

Transmission
Example

Draw the waveform of a 7-bit ASCII character ‘C’ (H’43)
transmitted on a serial port with 7-bit data, Even parity bit, 1

stop bit and a baud rate of 2400
| ee Stop bit

1114] 0f0:0:0]1] 1:

ee

Start bit ‘Parity bit

How fast is the data transferred?

This is determined by the Baud Rate. The baud rate is the maximum
number of bits (including the start, parity & stop bit) that can be transmitted
per second. For a 2400 baud rate, T = 1/2400 seconds.

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 35

SIT Internal

ard Asynchronous Serial Data Reception

Receiving end:
— The Receiver continuously monitors the line
looking for the start bit

When detected, it waits till the end of start bit,
then samples the next N bits at their center. Nis
the number of data bits.

If parity is enabled, the receiver will then sample
the parity bit and check for parity error (e.g., if
even parity was used and there is an odd
number of 1’s in the frame, a parity error has
occurred.)

The receiver then samples the stop bit(s) for
framing error (e.g., error when Stop Bit = 0)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 36

SIT Internal

Baud Rates and Overheads

: The term baud rate is used for the data transfer
rate of the serial communication link

* It is given by 1/T, where T is the duration of each
bit

Common Baud rates are 300, 600, 1200, 2400,
4800, 9600 and 19200

Considering 10 bits per character, a baud rate of
1200 means that 120 characters are being
transmitted per second

OAn obvious disadvantage of this mode _ of
_ transmission is that to transmit a 7-bit (ASCII)
a information, 10-bits are needed to be transmitted

Chapter 7: Input / Output Interfacing Techniques



---
### Slide 37

ae The RS-232 Standard

¢ Serial interface standard

¢ Defines signals connecting between a DIE (data
terminal equipment) e.g., a computer, and a DCE
(data communication equipment), e.g., a modem

* Specifies electrical and mechanical interface, e.g.,
voltage levels used, maximum bit rate and maximum
distance of operation, etc

12 3 4 §

[ i —s

_ EL [ ]
( MALE 9-PIN i
\ SERIAL PORT
ry) \ @e000 | =
Th ag” Pr
@ 4 °

}.J  \ eno / LT |

>)

1CT1011: Computer Organisation and Architecture

Data Carrier Detect 6. Data Set Ready 7 ee ee
Receive Data 7. Request to Send
Transmit Data 8. Clear to Send RS-232 port

37

©2024
Steven Wong &
Xin Lou

Data Terminal Ready 9. Ring Indicator (DE-9)

Signal Ground Chapter 7: Input / Output Interfacing Techniques

oc he


---
### Slide 38

Chapter 7:TInput / Output
Interfacing Techniques

}. Memory Mapped I/O and Isolated I/O

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 39

SIT Internal

Memory Mapped I/O

From the earlier slides, we have seen that computers
can be interfaced to external devices using Parallel
Ports and Serial Communications Port

These interfaces are provided by the computer using
I/O Ports and Peripheral Modules

Microcontroller Unit (MCU)

CPU

1/O data Registers

CPU Registe

/O Ports
USB
Serial USB

1/O and peripheral
function Control and
Status Registers

Peripheral
Modules

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 40

_ — The peripheral can be used (e.g., to output the value of H

SIT Internal

Memory Mapped I/O

A set of Peripheral Registers are provided by the
I/O ports and the peripheral modules so that:

— The peripheral can be configured (e.g., the asynchronous
data format used for serial communications, UCSI)

to a I/O port)

CPU

Internal Bus

Microcontroller Unit (MCU)

Peripheral
registers are

not the same

as CPU
_ registers

Vss

Aa |

1/O data Regist

CPU Registers

1/O and peripheral
function Control and
Status Registers

Chapter 7: Input / Output Interfacing Techniques

—
sp

1/O Ports

mp snroex

2one< ag


---
### Slide 41

spe Memory Mapped I/O
Memory Mapped I/O

¢ The peripheral registers are interfaced onto the same bus as
the memory (Thus, they share the same address space)

* Each peripheral register is given an address

* These peripheral registers are accessed in exactly the same
way as any other location in the memory (RAM/ROM)

BUS ‘F5529 Memory Map

CPU RAM ROM Peripheral
Registers

Flash 128K

OxFFFF

OxFF80 INT Vectors 80

1CT1011: Computer Organisation and Architecture
ie
i z

li
geae

8K

2K
512
2K

41

©2024
Steven Wong &
Xin Lou

Peripherals 4k

Output Interfacing Techniques


---
### Slide 42

SiTp ; SIT Internal
Example Using a MSP430 Microcontroller

-* The MSP430 microcontroller uses memory-mapped I/O
_ for its peripherals and I/O Ports

’ Example of the peripheral registers for Port 1 of the
~_ MSP430 microcontroller (remember Lab 1???)

3
:
-

ages

= ra Name of Port 1 Registers Description
‘
| Direction Register (P1 DIR) The individual bits of P1DIR specify input or output for the pins of port 1.
q Setting a bit to 1 makes the corresponding port 1 pin an output pin, while
‘ clearing this bit to 0 makes the pin an input pin.
he Data Out (PIOUT) PIOUT stores output data for the port 1 (For pins configured as output).
Fi: Data In (PIIN) PI1IN shows port | pin states. (i.e. allows reading of input pins)

. These peripheral registers are placed in specific
_ addresses in the memory (this information is available in

i the datasheet_of the processor

_ 1CT1011: Computer Organisation and Architecture.

+]

?
ro

25
~ ©2024
tages ote Chapter 7: Input / Output Interfacing Techniques


---
### Slide 43

SIT Internal

_Example Using a MSP430 Microcontroller

Name of Port 1 Registers Description
Direction Register (P1 DIR) The individual bits of P1DIR specify input or output for the pins of port 1.
Setting a bit to 1 makes the corresponding port 1 pin an output pin, while PORT ‘I
clearing this bit to 0 makes the pin an input pin. i
Data Out (PIOUT) P1OUT stores output data for the port 1 (For pins configured as output). H 1
Data In (P1IN) P1IN shows port | pin states. (i.e. allows reading of input pins) P14 6 —> (6)
F —
OxFFFF CPU Registers P14— 0
Cie INT Vectors EY
0
0x2400 Gee 8K Fe 1
0x01C0 USB RAM 2K v
| Info Memory 51 ican Goud & 0
| Boot Loader Status Registers e
Peripherals 4k

Pe: 0x0000
Address

P1IDIR - EQU 0x0204
P10UT . EQU 0x0202
P1IN -EQU 0x0200

0x0202

0x0200 =pmov.b #0F0h,&P1DIR

bis.b #080h,&P10UT
Port 1 Registers Chapter 7: Input / Output Interfacing Techniques



---
### Slide 44

si BES teed SIT Internal

P1IDIR' .EQU 0x0204

ORF Sue: ; ; 1 ‘ 0x0202
___ Add an XOR operation in PLN’ “EQU  0x0200
____ the previous code. What
ee ie

_ ___ values will be present in Savi SOPUH, SEEDER

omy bis.b #080h,&PlouT
| PAIN?

xor.b #01Fh, &P1OUT

nina | Chapter 7: Input / Output Interfacing Techniques


---
### Slide 45

si BES teed SIT Internal

ah: E PIDIR .EQU 0x0204

__ Add an XOR operation in — =e Se

____ the previous code. What

values will be present in wov:b gor, cuoin
~ P1IN? xorb  #01Fh, &P10UT

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 46

SIT Internal

Isolated I/O

+ Two separate address spaces are used - one for
memory and other for I/O devices (dedicated address
space)

* Two separate control lines for memory and I/O
transfer: I/O read and write; memory read and write

-* Separate instructions for data transfer, e.g., IN and
OUT for I/O, MOV for memory

¢ E.g., Intel 8086 MSP430
_OxFFFFF _—

Memory

address OxFFFF

space

0x0000 0x0000

-0x00000

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 47

Chapter 7:TInput / Output
Interfacing Techniques

4. Polled and Interrupt-driven I/O Technique

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 48

SIT Internal

Polled and Interrupt-driven I/O

Interfacing involves handling of I/O Data transfer

That is, either
— writing (transmitting) data to an output device or
— reading data (receiving) data from an input device

There are mainly two techniques of data transfer:
— Polled I/O (Program controlled)

CPU Initiates, controls and terminates data transfer by
executing a set of instructions.

— Interrupt Driven

Device initiates but CPU controls and terminates data
transfer.

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 49

SIT Internal

| Polled I/O Technique

¢ Polling is continuously testing a port to
see if data is available. That is, the CPU
polls (asks or checks) the port if it has
data available or if it is capable of
-accepting data

» For example, CPU continuously polls
(checks) the port to see if the printer is
ready to accept data (prt_ready signal)

If ready, then writes a data byte to the
sa printer port, otherwise the CPU waits

Chapter 7: Input / Output Interfacing Techniques



---
### Slide 50

SIT Inter

Polled I/O Technique

Polled I/O is inherently inefficient

->When the CPU issues a command to the I/O
module, it must wait until the I/O operation is
complete

> |f the CPU is faster than the I/O module, this
is waste of processor time

>E.g., a printer takes few milliseconds to
accept a byte of data - the CPU spins in a
loop doing nothing (other than testing the
printer status port) for this time duration

=:
Chapter 7: Input / Output Interfacing Techniques +3]



---
### Slide 51

orla Polled I/O Flow Chart

¢ Before data transfer, the initialige the Control

1CT1011: Computer Organisation and Architecture

CPU must check whether Registers for data
Status Register of the
checking the status of inl

51 by CPU

the I/O device is READY transfer
peripheral)

| _ DEVICE
the peripheral device. cea

or not (by checking the >
Test Status of
I/O Device
¢ CPU waits in a loop
When device is ready, =o
data transfer is initiated Transfer Data
Steven vont & Chapter 7: Input / Output Interfacing Techniques


---
### Slide 52

SIT Internal

Sequence of Events

Computer
CPU Polls
CHECK
CPU _. Status of the
EXECUTE TRANSFER} aeviee

Peripheral Subsystem mma fod VICE READY
ONTROL REGISTER LT status bit

STATUS REGISTER

V/O

DATA REGISTER

Data
Device

READY |
Dev_Rdy Signal

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 53

SIT Internal

Example Using the Polled I/O
Technique

An example ——
Receiving a byte from the W/

keyboard

Vee

; RS232
aga RD Interface <> Key Board
Module TxD bs

SCI_RDR: .EQU ree ; Assume this is the serial data register
SC11_SSR: .EQU ee ; Assume this stores the serial status register
RDRF: -EQU ee ; Assume this a bit to show if there is data
WAIT: Zz BIT RDRF ; Is there data in the receiver buffer?
JEQ WAIT ; If no data, branch back to WAIT
MOV.B &SCII_RDR,R10 sreceive data and store to R10
BIC RDRF ; Reset the status bit
MP WAIT ; Jump back to WAIT

Look at the comments instead of the codes.
Chapter 7: Input / Output Interfacing Techniques



---
### Slide 54

SIT Internal

_ Interrupt-driven I/O Technique
- Data transfer initiated by the external device

> An interrupt is an external hardware event (such
as the printer becoming ready to accept another

byte)

» This event causes the CPU to interrupt the current
_ instruction sequence (Suspend temporarily)

» And execute a special routine written by the
programmer called interrupt service routine (ISR)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 55

SIT Internal

Interrupt-driven I/O Technique

» When the device is READY for data
transfer, it sends an interrupt request to
the CPU

> CPU executes an interrupt service routine
(ISR) (meant for the device)

» The ISR transfers data to/from the device

» As the ISR is executed in very short time,
the main program is suspended for a very
_ brief time only

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 56

SIT Internal

Sequence of Events

Computer

CPU executes an
ISR to transfer
data

Normal Program Execution

CPU
Interrupt Processing en
J if

Peripheral Subsystem
CONTROL REGISTER

STATUS REGISTER

DATA REGISTER

Port2 Device

Device sends|an
Interrupt signal

IRQ4

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 57

SIT Internal

a Disruption to the Main Program

Main Program

Device1 sends an
= 3S INTERRUPT
Request

mov.b R12,R11

add.b R10,R11 ;
Execute INTERRUPT

SERVICE ROUTINE (ISR)
of Device1

1CT1011: Computer Organisation and Architecture

Return to main
Program

57

©2024

sal vont & Chapter 7: Input / Output Interfacing Techniques



---
### Slide 58

SIT Internal

eg i V/O Flow Chart

INTERRUPT
INITIALIZATION

Main Program ENABLE INTERRUPT

MOV.B R10,R11;

SUB.B R12,R12 }

MOV.B R12/,&Dest ;

SEND AN INTERRUPT
REQUEST
T

COMPLETE EXECUTION OF
CURRENT INSTRUCTION

EXECUTE INTERRUPT
SERVICE ROUTINE

RETURN TO MAIN PROGRAM

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 59

SIT Internal

Interrupt-driven I/O Technique
An Example

Vee

(1) The processor executes the main
ce! program which blinks the LED
connected to I/O port pin, P20, at
a certain frequency

pc

P20
“ge

Serial | RxD fe} RS232 Key | (2)When a key is pressed from the

Module | tx 4, Interfae [**} Board keyboard, this will cause an
interrupt request via the RS232
Interface

_ (3) The CPU temporarily suspends the main program
(4) Then CPU executes the ISR
(5) The ISR transfers data received to a memory location in RAM

(6) After this CPU returns to the main program where it stopped and
continues

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 60

SIT Internal

Pros and Cons

Polled I/O:
* Advantages:

— minimum hardware interface circuitry
between I/O device and processor

— programmer has complete control over the
entire process

— easiest method to test and debug

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 61

SIT Internal

Pros and Cons

Polled I/O:
> Disadvantages: since CPU waits in a loop, it
cannot perform any other task until data
transfer is completed

— inefficient use of CPU resources

— program execution of CPU held up while waiting
for I/O device to get ready

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 62

SIT Internal

Pros and Cons

_Interrupt-driven:

¢ Advantages:

— efficient use of CPU; promptly provides
service to at the request of the peripheral.

— CPU can continue with other tasks between
interrupts.

* Disadvantages:

— more hardware interface circuitry required
between I/O device and processor

— program is slightly more complex and difficult
to debug

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 63

SIT Internal

When to Use What???

Polled I/O

— useful when the data transfer must be
completed before the program can continue

— For example:

* waiting for user input from a mouse ora
keyboard

* writing into the control registers of peripheral chips
during initialization

* waiting for a switch to be pressed before program
execution can continue

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 64

SIT Internal

When to Use What???

Interrupt-driven I/O

— useful when the timing of the data transfer
cannot be known beforehand or occurs
infrequently.

— Examples: getting data from a switch; sending
data to a printer; getting data from a
temperature sensor

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 65

SIT Internal

Summary

Understand the need for peripherals and interfaces

— Input / Output, Digital / Analogue, Microprocessors,
Microcontrollers, Parallel / Serial Data Transfers

Configuring and using the interfaces and peripherals

— Peripheral registers are provided by the peripheral I/O
modules

— These registers can be interfaced to the CPU using
memory-mapped I/O

How data can be transferred between CPU and the
peripheral I/O modules

— Polled I/O, Interrupt Driven I/O

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 66

SIT Internal

Chapter 7: Input / Output
Interfacing Techniques

5. Bluetooth

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 67

SIT Internal

What Will We Learn Today?

Bluetooth History/Versions
Bluetooth Specifications
Bluetooth Operation Status and Protocol Stack

Bluetooth LE (brief introduction)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 68

SIT Internal

What is Bluetooth?

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 69

SIT Internal

Bluetooth

¢ What is Bluetooth?

— A short-range radio
connection technology

— A low power and low cost
wireless standard for many
devices

— Not limited to “line of sight’
— Examples:

* Robots

* Smart watches

¢ Smart phones

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 70

SIT Internal

BT - Brief History

Began with Ericsson's (Sweden) Bluetooth
Project in 1994 for radio communication
between cell phones over short distances

» BT was named after Danish king Harald
Blaatand (AD 940-981) who was fond of
blueberries and had a blue tooth

»
»~ “td yy a S
f Silden

Chapter 7: Input / Output Interfacing Techniques



---
### Slide 71

SIT Internal

BT - Brief History

Tech giants like Intel, IBM, Nokia, Toshiba,
and Ericsson formed Bluetooth SIG
(special interest group) in May 1998

- Version 1.0A of the specification came out
in late 1999

IEEE standardized BT as 802.15.1 in
2002 and 2005

da Later versions handled by Bluetooth SIG
directly

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 72

SIT Internal

Bluetooth Versions

1.0 and 1.0B (late 1999): too many problems

1.1: IEEE 802.15.1-2002. (WPAN (wireless personal
area network))

1.2: IEEE 802.15.1 -2005, 720kbps

2.0 + Enhanced Data Rate (EDR) 2.1 + EDR: Secure
Simple Pairing to speed up pairing, 2007

3.0+: High Speed (HS), 2009

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 73

SIT Internal

Bluetooth Versions

4.0: (includes Bluetooth Smart or Bluetooth Low
Energy(BLE)): Low energy, smaller devices, longer
battery life

4.1: 4.0 + Core Specification Amendments (CSA) 1, 2,
3, 4, 2013

4.2: 4.1 + flexible internet connectivity, 2014
5.0 and later, since 2016

Latest version 5.4, 2023 (Bluetooth 6.0
announced in September 2024)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 74

SIT Internal

Bluetooth Specifications

Operating frequency: 2402 to 2480 MHz
(79 1-MHz physical channels)

Data Rate: 1 Mbps using 1 MHz
(720kbps/user)

Radio Frequency hopping: 1600 times/s -
0.625 ms/hop

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 75

SIT Internal

Bluetooth Transmit Power

TX Output Power:

— Class 1: 20 dBm (0.1W) — 100m
— Class 2: 4 dBm (2.5 mW) — 10m
— Class 3: 0 dBm (1mW) — 1m

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 76

SIT Internal

Piconets & Scatternets

How do multiple BT devices communicate?

Piconet: a type of BT network consists of a set of

BT devices sharing a common channel
one master and maximum of 7 active slave nodes
slaves can transmit only when a master requests

Scatternet: interconnecting multiple (~10) piconets



---
### Slide 77

SIT Internal

Frequency Hopping (FH)

What is FH or Frequency-hopping spread
spectrum (FHSS) ?

— amethod of transmitting radio signals by rapidly
changing the carrier frequency among many distinct
frequencies occupying a large spectral band

— makes jamming and interception more difficult

Frequency

‘+

SPA HS Am D

5

fi to Sis ta ts So Sr Sy Frequency Time
(a) Channel assignment (b) Channel use

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 78

SIT Internal

Frequency Hopping (FH)

FH in Bluetooth:

— Total BW (79 MHz) is divided into 79 physical
channels of 1 MHz bandwidth each

— At any time 1 MHz is shared among 8 devices
— FH follows a pseudo random sequence

— All devices in a piconet share the same
sequence

— Hop rate is 1600 hops/s — each physical
channel is occupied for 0.625 ms (slot)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 79

SIT Internal

Frequency Hopping

Master transmits during even numbered
slots

* Slaves transmit during odd numbered slots
Packets can be 1, 3 or 5 slots long

: Hopping is deferred during data
fransmsson

requency |

PT ected rrequency 3

Frequency 3

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 80

SIT Internal

Frequency Hopping TDD - TDMA

BT implements Time Division Duplexing (TDD)

— Data transmission alternates between two
directions (T & R)

* More than two devices share the piconet, access
technique is called Time Division Multiple Access
(TDMA)

Since FH is combined with TDMA, piconet access is
called FH-TDD-TDMA

Chapter 7: Inp


---
### Slide 81

SIT Internal

Frequency Hopping TDD - TDMA

Figure illustrates TDD — TDMA (k denotes
slot number, and f(k) denotes physical
channel selected during slot period k)

Stk+\) S(k+2)

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 82

SIT Internal

=u Frequency Hopping TDD - TDMA

FH sequence is determined by the master
in the piconet

* It is a function of the master’s BT address
Masters in different piconets in the same

area use different hop frequencies (hence
different physical channels)

= * Collision is possible if two piconets use the

same physical channel

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 83

SIT Internal

Packet Format

Packet Format

Access | Baseband/Link | Data
Code | Control Header | Payload
72b 54b 0-2745b

Access Code: timing synchronization, offset
compensation, paging and inquiry

> Header: identify packet type, carry protocol
control information

_* Payload: user voice or data and payload
e« header, if present

Chapter 7: Input / Output Interfacing Techniques



---
### Slide 84

SIT Internal

BT Operational Status

Standby: Initial state (default)

Connected: The device is connected to a
piconet as a master or slave

Active

Low Power

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 85

SIT Internal

BT Operational Status

Inquiry:
— Master sends an inquiry packet

— Slaves scan inquiries and respond with their
address and clock after a random delay

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 86

SIT Internal

| BT Operational Status
Page:
Master invites devices to join the piconet

Page message is sent in three consecutive
slots (3 frequencies)

Slave enters page response state & sends
response including its device access code

Master informs slave about its clock and
address to let slave participate in piconet

Disconnected

Transmit

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 87

SIT Internal

Power Down Modes
¢ There are three inactive states (low power)

— Hold: Low power mode; Places the link between a
master and slave in hold mode for a specified time

— Sniff: Low power mode; Slave listens after fixed sniff
intervals

— Park: Very low power mode; Given the 8-bit parking
member address and loses its 3-bit active member
address; Wakes up periodically & listens to beacons
from master

SINGAPORE
INSTITUTE OF
TECHNOLOGY

1CT1011: Computer Organisation and Architecture

Sniff Park

87
©2024

Steven Wong &
Xin Lou



---
### Slide 88

SiT pass

e There a> thran inanntnin atatac [I

— Hold: |
2
3 master
E — Sniff: L
: interva
: — Park: \
3 membe
: addres
: from m
iS)

88

©2024
Steven Wong &
Xin Lou

SIT Internal

Power Down Modes

Park

Park
Address
10 sec

Give Up
Active

ae
e

Ow power)

link between a
specified time

3 after fixed sniff

1e 8-bit parking
ctive member
2ns to beacons



---
### Slide 89

SIT Internal

BT Protocol Stack

Applications (Profiles)

Application

Middleware|Audio

Link Manager
Transport | Baseband

RF

Soil Horizons

+O - Organic Layer
_| Humus

|-A - Topsoil
Minerals with humus
+E - Eluviation Layer
Leached minerals & organic matter

-B - Subsoil
Deposited minerals & metal salts

-C - Parent Rock
Partly weathered rock

+R - Bedrock
Unweathered parent rock

fo oe


---
### Slide 90

SIT Internal

Bluetooth LE
€) Bluetooth T.Ct‘(‘(‘(sUC<SOaahS==/

APP ‘-F
| | Profiles and Services

Bluetooth® Low Energy a ||

¢ Lower energy, longer battery life

SMP Host

¢ Used for applications that do not
need to exchange large

amounts of data, and can HCl:

therefore run on battery power 7

for years at a cheaper cost | controter
BLE PHY

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 91

SIT Internal

Bluetooth Applications

» Bluetooth Classic

-wireless headsets/speakers
-wireless keyboards and printers
-file transfers between devices

¢ Bluetooth Low Energy
-proximity detectors
-location

-health devices

-sensors

-various loT applications

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 92

SIT Internal

Summary of Chapter 7

1. Basic I/O Interfacing Concepts

Parallel and Serial Communications
Memory Mapped I/O and Isolated I/O
Polled and Interrupt-driven I/O Technique

Bluetooth

af bP RN

Chapter 7: Input / Output Interfacing Techniques


---
### Slide 93

SIT Internal

Thank you!

lou.xin@singaporetech.edu.sg

Chapter 7: Input / Output Interfacing Techniques


---

# Chapter 8: Secondary Memory Subsystems



---
### Slide 1

omnaroie: SIT Internal

ICT1011
Computer Organisation
and Architecture

and Architecture
—)

Chapter 8

Secondary Memory
Subsystems

1CT1011: Computer Organisation

Seven Noes Chapter 8: Secondary Memory Subsystems


---
### Slide 2

SIT Internal

Where Are We Now?

| 1. The Fundamental of Computer
The Central Processing Unit
Instruction Set Architecture
Assembly Language Programming

Input/output

Pf & NS

aJEMYOS

Firmware /
Drivers

Instruction Set Architecture

Input / CPU
Output Memory

COMPUTER SYSTEM

auempseH

Transistors / Gates


---
### Slide 3

SIT Internal

What We Will Learn Today?

. Memory Hierarchy
The Magnetic Hard Disk
, Redundancy and Surety (Use of RAID)

Chapter 8: Secondary Memory Subsystems


---
### Slide 4

SIT Internal

Chapter 8: Secondary Memory
Subsystems

Memory Hierarchy

Chapter 8: Secondary Memory Subsystems


---
### Slide 5

oe SIT Internal

j =

za "Illustrate the memory types in terms
of the memory hierarchy.

pe ekeaees amare oar aaa oF
{

Xin Lou us Chapter 8: Secondary Memory Subsystems


---
### Slide 6

SIT Internal

Memory Hierarchy

Illustrate the memory types in terms of the
memory hierarchy?

reasing capacity and access time ——

Processor

Secondary
Memory

oo Increasing cost/bit, frequency of access

and speed

Chapter 8: Secondary Memory Subsystems


---
### Slide 7

SIT Internal

Memory Hierarchy

_Memories are generally organized in levels of decreasing
speed and cost/bit.
ncreasing capacity and access time ——>

Processor

Secondary
Memory

== Increasing cost/bit and frequency of access

© Registers Very fast access but limited numbers within CPU.
Operates at CPU clock rate (size: 2-128 registers)

_© Cache Fast access static RAM close to CPU. Typical access
memory _ time 8-35nS (size: 1KB — 16MB)
© Main Usually dynamic RAM or ROM (for program storage).

memory _ [ypical access time 20-100nS. (size: 1KB — 32GB)
. ‘ou will learn more about this in the next chapter!
© Secondary Not always random access but non-volatile. Maybe be

memory based on magnetic, optical or flash technology.
Typical access time 5-20mS. (size: 1MB — 4TB)

Chapter 8: Secondary Memory Subsystems



---
### Slide 8

SIT Internal

Secondary Memory

: Secondary Memory is usually external (thus, external
-memory) to the microprocessor and provides the largest

storage space for data and program

* External Memory consists of peripheral storage devices
_that are accessible to the processor via I/O controllers

SYSTEM BUS

Chapter 8: Secondary Memory Subsystems



---
### Slide 9

SIT Internal

Types of External Memory

Due to cost as well as space constraints, the
capacity of the main memory is very limited, thus
external/secondary memory has to be used

Types of external secondary memory include:

— Magnetic: e.g., mechanical hard-disk, floppy disk, etc.
— Optical: CD-ROM, CD-RW, DVD, BLU-RAY, etc.

— Semiconductor: Memory cards, Solid-State Drives,

i etc.
— Anything that can store discrete values

| Processor

Chapter 8: Secondary Memory Subsystems


---
### Slide 10

SIT Internal

Chapter 8: Secondary Memory
Subsystems

_ The Magnetic Hard Disk

Chapter 8: Secondary Memory Subsystems


---
### Slide 11

SIT Internal

Introduction to Magnetic Hard Disk

Computers often use magnetic hard disks for
large secondary storage

One or more platters on a common spindle
Platters are covered with thin magnetic film
Platters rotate on spindle at constant rate

Read/Write
Rotary head
drive shaft

7S - Read/write heads in close
| ——— proximity to the surface
> can access data arranged
l —__———— . .
y | in concentric tracks
Disk f<—

Access
mechanism Chapter 8: Secondary Memory Subsystems


---
### Slide 12

SiTpg | ; SIT Internal ; _
Introduction to Magnetic Hard Disk

Hard Disk Drives (HDDs) use spinning disks (platters)
to magnetically store information.

1CT1011: Computer Organisation and Architecture

12

©2024

w
a Lou” : Chapter 8: Secondary Memory Subsystems


---
### Slide 13

SIT Internal

Read and Write Mechanisms

Recording & retrieval are performed via a conductive coil
called a Head

May be single read/write head or separate ones
During read/write, head is stationary, platter rotates

QO Write
" Current through coil produces magnetic field
» Pulses sent to head

» Magnetic pattern recorded on surface below

current

Inductive Write/
~~ Magneto Resistive Read
“| Head


---
### Slide 14

SIT Internal

Read and Write Mechanisms

URead
= Can be a separate read head, close to write head
= Partially shielded magneto resistive (MR) sensor

" Electrical resistance depends on direction of magnetic
field

Direction of
magnetization

Chapter 8: Secondary Memory Subsystems


---
### Slide 15

ios
Steven Wong &
Xin Lou

SIT Internal

Read and Write Mechanisms

Chapter 8: Secondary Memory Subsystems


---
### Slide 16

SIT Internal

Jata is stored on the surface of
Ne platter in concentric rings

co lled Tracks track t a. spindle
[he set of all the tracks in the i
same relative position on the © sectors |
platter is referred to asa a
Cylinder wfindere-= | ae
Use
Each track has same width as patter”
the head = ™

~ Gaps between tracks to
minimise interferences from
adjacent tracks

rotation

Chapter 8: Secondary Memory Subsystems

Data Organization and Formatting

+— arm assembly



---
### Slide 17

SIT Internal

Data Organization and Formatting

Tracks are divided into Sectors

Sectors may be separated by a small gap to reduce
precision requirement

Minimum Data Block Size is one sector

Sectors Tracks

Inter-sector gap

oo *. Inter-track gap

Chapter 8: Secondary Memory Subsystems


---
### Slide 18

SIT Internal

Characteristics of Common
Modern Hard Disk

Movable head en ee
— One read/write head per side _ \

— Mounted on a movable arm <b
Multiple double-sided platters ==" i——_

drive shaft

\

sais Surface 4 +
5 Surface 3
——
Surface 2
—— sidan t+
_———
Surface 0 '
—
J, _———— Spina Boum
. ae ' <=>
Disk
Access
mechanism

Chapter 8: Secondary Memory Subsystems


---
### Slide 19

SIT Internal

Multiple Platter Hard Disks

Most hard disks you have in your computer today have
multiple platters per disk

Each platter surface will have one read/write head that
are joined and aligned so that the heads are in the same
position for each platter

- A data is striped by cylinder
— reduces head movement
— Increases speed (transfer rate)

An example of data striping by cylinder
A 4MBytes data block can be striped into
8 x 512Kbytes tracks. If a disk has 4
double sided platters, these 8 tracks can
_be stored in the same location across the
8 surfaces.

Chapter 8: Secondary Memory Subsystems


---
### Slide 20

SINGAPORE SIT Internal

A magnetic hard disk comprises 3 platters, and each platter
has 2 recording surfaces, where each surface is composed
of 6000 tracks. How many cylinders does this disk have,
and how many tracks are there in one cylinder?

1CT1011: Computer Organisation and Architecture

20

©2024
Steven Wong &

Xin Lou Chapter 8: Secondary Memory Subsystems


---
### Slide 21

SIT Internal

=
2

A magnetic hard disk comprises 3 platters, and each platter
has 2 recording surfaces, where each surface is composed
of 6000 tracks. How many cylinders does this disk have,
and how many tracks are there in one cylinder?

track t — spindle

K?] 5
, | arm assembly
|

sector s

1CT1011: Computer Organisation and Architecture
>

head

Cylinders: 6000 pata

Tracks in one cylinder: 6 am

rotation

21

©2024
Steven Wong &

Xin Lou Chapter 8: Secondary Memory Subsystems


---
### Slide 22

SIT Internal

Speed (Transfer Rate) of Hard Disk

Seek Time (T;)
— Time it takes for the head to move to the correct track

. Rotational Delay (T,)

— Time it takes for the disk to rotate until the read/write head
reaches the starting position of the target sector

Access Time (T,)

— Time from request to the time the head is in position (T, + Tp)

Transfer Time (T+)

— Time required to transfer the required data after the head is
positioned =

Chapter 8: Secondary Memory Subsystems


---
### Slide 23

SIT Internal

Speed (Transfer Rate) of Hard Disk

The Rotational Delay, Tp, is dependent on the rotational
speed of the disk (commonly denominated in
Revolutions Per Minute, RPM)

For calculations, RPM is’ usually converted to
Revolutions Per Second, RPS where:
RPS = RPM/60

For a random section,

Avg. Rotational delay, T, = 0.5 /RPS seconds
(0.5 for half a revolution)

Chapter 8: Secondary Memory Subsystems


---
### Slide 24

SIT Internal

Speed (Transfer Rate) of Hard Disk

[he Transfer Time, 7;, is also dependent on the rotational

speed of the disk, as well as the Track Density, D; (number of

sectors per track), Sector Density, D, (number of bytes per
ector) and the number of bytes for the transfer N

Transfer Time:

T; =N/(RPS x DT x DS)=

N 1
xX —i
DrxDs ©’ RPS

where D; X Dgis the number of bytes on the track.

The total average data block read/write time:

Tota = Ta + Tr = Ts + Tp+ Ty
T

T,



---
### Slide 25

SIT Internal

Example

A 15,000 RPM disk has the following parameters:
— Avg. Seek Time, T; = 4 ms

— Track Density, D; = 500 sectors per track

— Sector Density, D, = 512 bytes per sector

— Revolutions per Second, RPS = 15,000/60 = 250 RPS

Calculate the total time, T;,;4), it takes to read a 3Kbytes
file that is stored in consecutive sectors on the same
track?

Access Time, T, = T5 + Tp = 4ms + (0.5/250) = 6 ms
mnAAe 3072 1

Transfer Time, T;= 3072 / (250*500*512) = sopxead 250

= 48 us

Total Time, 7;,:4;= T, + T; = 6.048 ms

This example shows that the Access Time can be the
bottleneck when accessing random files on the disk!!!

Chapter 8: Secondary Memory Subsystems



---
### Slide 26

SIT Internal

The Magnetic Hard Disk

Track to track access time: Time taken to
move from one track to successive track

If data is stored in successive tracks, inter
track access time is to considered

Unapter &: seconaary Memory Subsystems


---
### Slide 27

SIT Internal

Chapter 8: Secondary Memory
Subsystems

. Redundancy and Surety (Use of RAID)

Chapter 8: Secondary Memory Subsystems


---
### Slide 28

Redundant Ariay of Independent
Disks (RAID)

_A single magnetic hard disk suffers from the following:

— The access times for moving the head to the correct position
significantly lowers the transfer rate of the disk

_ — Magnetic hard disk are mechanical devices that suffers “easily”
from crashes

The use of multiple physical disks as a single logical
drive may help with the above issues

One possible method is the use of a Redundant Array
_of Independent Disks (RAID)

— There are many different RAID configurations (usually 7 levels, 0
to 6)

_-— Some of these configurations use data distributed across

physical drives (known as striping) to improve access times
(e.g., RAID 0)

— Some configurations can also use redundant capacity to mirror a
drive (e.g., RAID 1) Chapter 8: Secondary Memory Subsystems



---
### Slide 29

SIT Internal

An Example - RAID 0

No redundancy
- Needs a minimum of 2 disks

Data striped as blocks across
all disks

Round Robin striping

Adv: increased speed

_— Multiple data requests probably not
on same disk

— Disks seek in parallel Disk 0 Disk 1

— A set of data is likely to be striped
across multiple disks

RAID 0

Chapter 8: Secondary Memory Subsystems


---
### Slide 30

SIT Internal

An Example - RAID 1

Mirrored Disks
Data is written identically to two or more disks

2 copies of each stripe on separate disks

A minimum of 2 disk is required
RAID 1

Disk 0 Disk 1

Chapter 8: Secondary Memory Subsystems



---
### Slide 31

SIT Internal

An Example - RAID 1

Adv: faster read operations
— Read from either disk that contains the requested data

— But write is same as single disk (on both corresponding
strips) RAID 1

Adv: recovery is simple
— Swap faulty disk & re-mirror
— No down time

Disadvantage: higher cost

Disk 0 Disk 1

Chapter 8: Secondary Memory Subsystems


---
### Slide 32

SIT Internal

Nested RAID-Example: RAID 10

Mirroring and stripping RAID +0
(stripe of mirrors) | |
8 . RAID 1

A minimum of 4 a —
Only half of the capacity eal
is for data storage a
Fast read/write operation

a

Disk O Disk 1 Disk 2 Disk 3

Chapter 8: Secondary Memory Subsystems


---
### Slide 33

SIT Internal

Applications

Network-attached storage (NAS)
Data streaming
Gaming system

Chapter 8: Secondary Memory Subsystems


---
### Slide 34

SIT Internal

Summary

. The Memory Hierarchy: Primary Memory
(Internal) and Secondary Memory (External)

. The Magnetic Hard Disk: Mechanisms and
Performance Metrics

. Redundancy and Surety: Basic Ideas of
RAID

Chapter 8: Secondary Memory Subsystems


---
### Slide 35

SIT Internal

Thank you!

lou.xin@singaporetech.edu.sg

Chapter 8: Secondary Memory Subsystems


---

# Chapter 9: Primary Memory Subsystems



---
### Slide 1

omnaroie: SIT Internal

ICT1011
Computer Organisation

and Architecture
Chapter 9

and Architecture
—)

Primary Memory
Subsystems

1CT1011: Computer Organisation

(a) [sl
omg
[als
1 J Join at
©2024 slido.com

Steven Wong & - Dri
Xi Lou 9 Chapter 9: Primary Memory Subsystems #1CT101 1 Pt2


---
### Slide 2

oa fF WON

SIT Internal

Where Are We Now?

. The Fundamental of Computer

The Central Processing Unit
Instruction Set Architecture
Assembly Language Programming
Input/output

Secondary Memory Subsystems

aleMYOS

Input /

Output Memory

COMPUTER SYSTEM

aseMpieHy


---
### Slide 3

SIT Internal

What Will We Learn Today?

if Memory Hierarchy (Register and Cache)
2. CPU-Memory Interfacing

3. Introduction to the Main Memory

4. RAM Technologies

5. ROM and FLASH Technologies

Chapter 9: Primary Memory Subsystems


---
### Slide 4

SIT Internal

Chapter 9: Primary Memory

Subsystems
. Memory Hierarchy (Register and Cache)

Chapter 9: Primary Memory Subsystems


---
### Slide 5

SIT Internal

Memory Hierarchy

_Memories are generally organized in levels of decreasing
speed and cost/bit.

Processor

© Registers

Increasing capacity and access time L==>

Secondary
Memory

Increasing cost/bit and access
frequency, and speed

Very fast access but limited numbers within CPU.
Operates at CPU clock rate (size: 2-128 registers)

_© Cache
Memory

Fast access static RAM close to CPU. Typical access
time 8-35nS (size: 1KB — 16MB)

© Main
memory

Usually dynamic RAM or ROM (for program storage).
Typical access time 20-100nS. (size: 1KB — 32GB)

© Secondary
Memory

Not always random access but non-volatile. Maybe be
based on magnetic, optical or flash technology.
Typical access time 5-20mS. (size: 1MB — 4TB)

Chapter 9: Primary Memory Subsystems


---
### Slide 6

SIT Internal

Registers

Very fast flip/flop-based storage elements within
the CPU

Data In
ee
— =
DO D1 D2 D3
Le Q | D DQ Ls Q
f= = f= CLK
Clock Co 6 b 3
—
Data Out

An example of a 4-bit register

Chapter 9: Primary Memory Subsystems



---
### Slide 7

SIT Internal

Overview of Cache Operations

* Cache Memory is “small” and “optional” amount

of fast memory that sits between the main
memory and the CPU

Cache may be single-level or multi-level

Main Memory

Fastest Fast

3-Level Cache
Chapter 9: Primary Memory Subsystems



---
### Slide 8

SIT Internal

Overview of Cache Operations

Cache operations are usually handled by
the cache controller

|. CPU requests contents of a main memory location

2. Checks if data is available in the cache

3. If present, CPU reads from cache (fast)

|. If not present, the cache controller will fetch the required
block from main memory and store it in the cache

5. The CPU will then read from the cache

Main Memory

Chapter 9: Primary Memory Subsystems


---
### Slide 9

cies Which of the following memory types is

the fastest but also the most expensive
(cost per bit)?

A.L2 Cache
B. Main Memory

C. Flash Memory

1CT1011: Computer Organisation and Architecture

D. Magnetic Hard Disk

©2024
pr Wong & Chapter 9: Primary Memory Subsystems


---
### Slide 10

cies Which of the following memory types is

the fastest but also the most expensive
(cost per bit)?

A.L2 Cache
B. Main Memory

C. Flash Memory

1CT1011: Computer Organisation and Architecture

D. Magnetic Hard Disk

10

©2024
ee Wong & Chapter 9: Primary Memory Subsystems


---
### Slide 11

SIT Internal

Chapter 9: Primary Memory
Subsystems

CPU-Memory Interfacing

Chapter 9: Primary Memory Subsystems


---
### Slide 12

SIT Internal

_A Bus is a communication pathway between two
or more devices, including the CPU, Memory,
etc.

*- A bus is made up. of a number of

lines/wires/connections that can be classified into 3
functional groups: Data, Address, Control lines

pauses Lines Bus
Data Lines |

Chapter 9: Primary Memory Subsystems



---
### Slide 13

SIT Internal

= The Bus Interconnection (Recap)

Data Bus is a set of data lines that collectively
provides a path to move data between devices

As each data line can only carry 1-bit at a time, the
number of data lines in a bus determines the number of
bits that can be transferred at one time

~The number of data lines is also known as the width of
_the data bus

Chapter 9: Primary Memory Subsystems


---
### Slide 14

SIT Internal

_ The Bus Interconnection (Recap)

* Address Bus is a set of address lines that is
used to designate the source (reading) or
destination (writing) of the data on the data bus

° The number of address lines on the address bus is
known as the width of the address bus. This width
determines the MAXIMUM possible memory capacit

of the system
Cc
Bus
im
Data Lines

Chapter 9: Primary Memory Subsystems



---
### Slide 15

SIT Internal

The Bus Interconnection

Control Bus is the contro! lines used to control
the access and the use of the data and address
lines

Control signals on the control bus can support
one or both of these data transfer timings:

— Asynchronous Timing: the occurrence of one event
on the bus follows and depends on the occurrence of a
previous event

— Synchronous Timing: the occurrence of events on the
bus is determined by a clock

Chapter 9: Primary Memory Subsystems


---
### Slide 16

SIT Internal

The Bus Interconnection

Typical control lines include:

— Memory Write, Memory Read (Memory Operations)
— I/O Write, I/O Read (I/O Operations)

— Interrupt Request, Interrupt ACK (Interrupts)

— Clock (for Synchronous data transfers)

— Reset (initializes all modules)

Chapter 9: Primary Memory Subsystems


---
### Slide 17

SIT Internal

The Bus Interconnection:
An Example

Microprocessor

A0-A23

Mem_RD
Mem_WR
/O_RD
/(O_WR

The above shows the pins available on a microprocessor. Based on
these pins, several attributes can be determined:

— DO-D7 forms the Data Bus with a width of 8-bits. Thus, this
processor can fetch 8-bits at one time.

— AO-A23 forms the Address Bus with width of 24-bits. Thus, the
total memory capacity will be 24 bytes.

— From the Control Bus, it can be seen that this microprocessor
supports isolated I/O as it has separate control lines for I/O
devices

Chapter 9: Primary Memory Subsystems


---
### Slide 18

SIT Internal

Synchronous Bus Transfers- Read

During T,: (1) The address of the source is placed on the
Address Bus and (2) latched by the memory module

During T,: (3) The Read Signal is activated on the Control
Bus

During T;: (4) Data stored at the indicated address will be
placed on the Data Bus and is read by the CPU

, Bus cycles , - ;
>

2
f
°
+
:

1
1 1 1
Clock (1) ‘ ‘ ;
ress '
aah Stable address
lines

! 1
1
' 1 1
Data ' 1 - -
Read lines 11 Valid data in>-— Valid data in> data in
' 1
reaa__i __Y@ :+@® W—
’

Subsystems *

Chapter 9: Primary Mem


---
### Slide 19

SIT Internal

Synchronous Bus Transfers- Write

During T,: (1) The destination address is placed on the
Address Bus and (2) latched by the memory module

During T,: (3) Data to be stored is placed onto the Data
Bus and a Write Signal is activated on the Control Bus
by the CPU

During T,: (4) Memory stores the data at the specified

destination address

<P eT eT
Clock

aces

'
Address (2) 1 1
enable ——_L—___ 4 ; ee

'
Data ' 1
Write lines : < Valid data out >—
'
U
'
'

i. or Oe

'
Chapter 9: Primary Herory Subsystems 4 1



---
### Slide 20

SIT Internal

" Asynchronous Bus Transfers- Read

1. The address of the source is placed on the Address Bus
2. The Read Signal is activated on the Control Bus

3. After a short delay (the access time), data stored at the

indicated address will be placed on the Data Bus
CPU reads data and resets the Address and Control Bus

Address 4)
lines —< Stable address >
Read (2)

CPU | = ---| ss | | vo | ++ | vo |

[ |
Control Lines

[| iy f = i LT ‘
Address Lines Bus

J I J I im J |
Data Lines
Chapter 9: Primary Memory Subsystems



---
### Slide 21

SIT Internal

: Asynchronous Bus Transfers- Write

1. The destination address is placed on the Address Bus
Data to be stored is placed on the Data Bus
3. The Write Signal is activated on the Control Bus

4. CPU resets the Address and Control Bus after some time
(Memory should store the data into the correct location by then)

Address (4)
ves
Data @)
inves
Write 3) (4)
CPU | Memory | *-°*] Memory | vo | coe | vo |
| | 2 LI

Control Lines
i LI 1 LT I LT
Address Lines Bus
J I } | im T]
Data Lines
Chapter 9: Primary Memory Subsystems



---
### Slide 22

SIT Internal

Synchronous and
Asynchronous Timing

Synchronous Timing
— Simpler to implement and test

— Less flexible as all devices on the bus are tied to a
fixed clock rate

. Asynchronous Timing

_— Very flexible as a mixture of slow and fast devices,
using older and newer technology, can share a bus

— Operations of the bus is more complex as different
devices may operate at different soeeds

— A slow device may hold up the entire bus

Chapter 9: Primary Memory Subsystems


---
### Slide 23

SIT Internal

Memory Performance Attributes

Access Time (latency)

_ — Time from the instant that a control request is sent to the memory

to the instant that the data have been stored or made available for
use

— For mechanical storage devices, the access time is the time it

takes to position the read-write mechanism at the desired location
Access Time

I : ; I
Address

aes
;
Read ee as or
1
Data
lines
; <>
Memory cycle time Time for Data bus to clear

— Access time plus any additional time required before another
memory access can commence

— Mainly for RAM

Chapter 9: Primary Memory Subsystems


---
### Slide 24

SIT Internal

Memory Performance Attributes

Transfer Rate

— This is the rate at which data can be transferred into or out of a
memory unit

— This is usually (1 / Memory Cycle Time) for RAM

— For non-random-access memory (e.g., magnetic storage devices),
the total transfer time:

TN = TA + (N/R),
Where

TN = Average time to read or write N bits
TA = Average Access time

N = Number of bits

R = Transfer rate, in bits per second (bps)

Chapter 9: Primary Memory Subsystems


---
### Slide 25

cies Which of the following signals is NOT

transmitted at the control bus?

A. 1/O Read
B. Characters from Keyboard
C. Clock »

D. Interrupt request

1CT1011: Computer Organisation and Architecture

25

©2024
pr Wong & Chapter 9: Primary Memory Subsystems


---
### Slide 26

SU Which of the following signals is NOT

transmitted at the control bus?

A. 1/O Read
B. Characters from Keyboard
C. Clock »

D. Interrupt request

1CT1011: Computer Organisation and Architecture

26

©2024

Seven woes Chapter 9: Primary Memory Subsystems


---
### Slide 27

SIT Internal

Chapter 9: Primary Memory
Subsystems

_ Introduction to the Main Memory

Chapter 9: Primary Memory Subsystems


---
### Slide 28

SIT Internal

Memory Overview

» Memory in a computer system is an entity
that allows a collection of bits to be stored
and retrieved

« Main Memory (semiconductor) is
required for the basic operation of a CPU
(Fetch-Decode-Execute cycle)

Two groups of memory types are usually
available in the main memory:

— RAM: Random Access Memory

2®. — ROM: Read Only Memory

Chapter 9: Primary Memory Subsystems



---
### Slide 29

SIT Internal

Random Access Memory (RAM)

Its contents can be read from and written to at any
time

Contents are normally volatile (Data is retained only
when power is on)

Two major types of RAM

- SRAM: Static RAM

- DRAM: Dynamic RAM

Computer systems require RAM so that it can store
its working variables, store temporary data, maintain
a system stack, etc.

Chapter 9: Primary Memory Subsystems


---
### Slide 30

SIT Internal

Read Only Memory

# Read Only Memory (ROM)
e¢ Contents are non-volatile (retained after power-off)

-@ Contents are not easily changed, but once changed,
contents can be read but normally not written to (from
the CPU’s perspective)

e Different types of commonly-used ROM includes:
— PROM: Programmable ROM
— EPROM: Erasable Programmable ROM
— EEPROM: Electrically Erasable Programmable ROM
— FLASH

-@ Computer systems require ROM to store system
programs (e.g., BIOS — Basic Input/Output System),
configuration settings, etc.

Chapter 9: Primary Memory Subsystems



---
### Slide 31

SIT Internal

The Basic Memory Cell

~The main memory is constructed using memory cells
that support two basic operations: Read and Write

A basic memory cell has 3 terminals:

_ — Select: Activates/Selects a cell for reading/writing

— Control: Indicate if a read or write operation is
required

— Data: Indicate the logic to be stored (Write operation)
or the logic that has been stored (Read operation)

Control

Select >a" oes Data

Example of a Basic 1-bit Memory Cell
Chapter 9: Primary Memory Subsystems



---
### Slide 32

SIT Internal

The Basic Memory Cell: Write

To write to a cell asynchronously, the following
operations are performed:
_ — The control signal for writing is activated

— The logic to be stored is indicated on the Data
terminal

— The cell is selected for writing

Control _ 1 __ ,-—
: 1 0 CSo
10 4 —t -
es i
Select Data R/Wo
Do Valid Data

The Write operation

The Timing Diagram
This is just an example.

Not all memory cells uses the same sequence.
Chapter 9: Primary Memory Subsystems



---
### Slide 33

SIT Internal

The Basic Memory Cell: Read

To read the contents of a cell asynchronously,
the following operations are performed:

_ — The control signal for reading is activated

— The cell is selected for reading

_— The logic stored in the cell is sent to the Data terminal

Control _ ~ -—
| i} 1 CS 0
| 10 1 _-———_.|.
Select Data R/Wo
Bia ---- 4 Valid Data P-------

The Read operation

The Timing Diagram

This is just an example.
Not all memory cells uses the same sequence.

apter 9: Primary Memory Subsystems



---
### Slide 34

SIT Internal

Chapter 9: Primary Memory
Subsystems

RAM Technologies

Chapter 9: Primary Memory Subsystems


---
### Slide 35

SIT Internal

How RAM Can Be Built?

-Acommon building block for most digital
devices, including RAM, are Transistors

' For this course, you can view transistors as a
simple digital switch with 3 different pins:
Source (S), Gate (G) and Drain (D)

|
LL (6-0 > ste current
SJL 1

Ss °° fem> sf db
——> current

3 | Only when the Gate is closed (i.e., G = Logic 1),
35 current is allowed to flow from Source to Drain

Chapter 9: Primary Memory Subsystems



---
### Slide 36

SIT Internal

Static RAM (SRAM)

» Needs power to retain state; usually has short
access time (few nanosecs)

* A SRAM cell in a memory chip consists of
| two cross-connected inverters to form a latch

* Chip implementation typically uses CMOS
_ (Complementary Metal-Oxide Semiconductor) cell
_ whose advantage is low power consumption

. Two transistors controlled by Word Line act as

_ switches between the cell and the Bit Lines

_* To Write, the desired bit value is applied to Bit line
= * TO Read, the bit value is read from Bit line

Chapter 9: Primary Memory Subsystems



---
### Slide 37

SIT Internal

Static RAM (SRAM)

b b’

Word line

= Bit lines

A single SRAM Cell
A logical view of the cell

Chapter 9: Primary Memory Subsystems


---
### Slide 38

SIT Internal

Static RAM (SRAM)

2 Vsupply e
n] b —d [ T,X
. 0 Example if
r T; Il hold
1+ 1 I + + 1 I ce olds
— *x Y_— value of 1
1 1
xr; | | © od 1 IL T¢
= |
Word line
- _-

Bit lines

A single SRAM Cell

Actual Implementation using transistors

Chapter 9: Primary Memory Subsystems


---
### Slide 39

SIT Internal

Static RAM (SRAM)

Memory cells are organised in an_ array
consisting of Word Lines and Bit Lines

Bit Line
& ‘Lh’
Word Line
oO Ao
Aj
ae oad
a in cells
©
A
~~ 3
7)
|
5
4-bit address — R/W
Sense/Wri Sense/Wri Sense/Wri
24 Words gli “o [

rr 8-bit data

Data input/output lines: 7 by by
Chapter 9: Primary Memory Subsystems



---
### Slide 40

SIT Internal

Dynamic RAM (DRAM)

-* SRAMs have short access time, but need
several transistors per cell, so density is
lower (/.e., fewer cells per unit)

* DRAM has higher density and lower cost,
but access time is longer

Useful when density/cost advantages
outweigh slowness

DRAM is widely used in computers as the
main memory

Chapter 9: Primary Memory Subsystems


---
### Slide 41

SIT Internal

Dynamic RAM (DRAM)

Cell consists of a transistor and a capacitor
State is presence/absence of capacitor charge
Charge leaks away and must be refreshed

bitline bitline
wordline + wordline
J lL J J l
'1' bit pi 'O' bit [
stored T- stored T

A single DRAM Cell

Chapter 9: Primary Memory Subsystems



---
### Slide 42

SIT Internal

Dynamic RAM: Operations

« For Write, access the row and drive bit lines
to alter amount of charge in subset of cells

Refresh rows periodically to maintain charge

For Read, charge from cells in selected row
is checked by sense amplifiers on bit lines

1 or O if charge is above or below threshold

Action of sensing the bit lines also causes refresh of
charge in all cells of selected row

bitline bitline

wordline wordline

rt — ‘obit —lLe
stored ===-—— stored ——>—



---
### Slide 43

SIT Internal

DRAM vs SRAM

Both volatile
— Power needed to preserve data

Chapter 9: Primary Memory Subsystems


---
### Slide 44

=

ie ee He
a is
Ss

ietiah Bo)
' f 1}

SIT Internal

i] What's the difference between DRAM
23 and SRAM?

|

Chapter 9: Primary Memory Subsystems


---
### Slide 45

SIT Internal

DRAM vs SRAM

Both volatile
-— Power needed to preserve data

» DRAM
— Simpler to build (less components)
— More dense

— Less expensive

— Needs refresh

_— Higher Capacity, Larger memory units, suitable for main
memory

SRAM

— Faster access
— Suitable to be used as Cache

What’s the
difference
between

DRAM and
SRAM?

Chapter 9: Primary Memory Subsystems


---
### Slide 46

SIT Internal

Chapter 9: Primary Memory
Subsystems

>. ROM and FLASH Technologies

Chapter 9: Primary Memory Subsystems


---
### Slide 47

SIT Internal

ROM and FLASH Technologies

A read-only memory (ROM) has its contents
_written only once, at the time of manufacture

The basic ROM cell in such a memory contains
a single transistor switch for the bit line

The other end of the bit line is connected to the
power supply through a resistor

Bit line

Power. surely
_RES | Word line

& J L
ic
Connected to store a 0
P =

Not connected to store a |

A single ROM Cell

Chapter 9: Primary Memory Subsystems


---
### Slide 48

SIT Internal

ROM and FLASH Technologies

If the transistor is connected to ground,
bit line voltage is near zero, so cell stores a 0

Otherwise, bit line voltage is high for a 1

Bit line

Power supply
RES | Word line

[
Connected to store a 0
P =

Not connected to store a |

A single ROM Cell

Chapter 9: Primary Memory Subsystems


---
### Slide 49

SIT Internal

PROM, EPROM and EEPROM

Cells of a Programmable ROM (PROM) chip
may be written after the time of manufacture

— A fuse is burned out with a high current pulse

An Erasable Programmable ROM (EPROM)
uses a Special transistor instead of a fuse

— Injecting charge allows transistor to turn on (Logic 0)
— Erasure requires UV light to remove all charge

An Electrically Erasable Programmable ROM
(EEPROM) can have individual cells erased
electrically; More expensive than EPROM

Chapter 9: Primary Memory Subsystems


---
### Slide 50

SIT Internal

PROM, EPROM and EEPROM
« Flash memory is based on EEPROM cells

* For higher density, Flash cells are designed
to be erased in larger blocks, not individually

* Writing individual cells requires reading a block,
erasing the block, then writing the block with
changes

Greater density & lower cost of Flash memory
outweighs the inconvenience of block writes

_ + Widely used in cell phones, digital cameras, and
Solid-state drives (e.g., USB memory keys)

Chapter 9: Primary Memory Subsystems


---
### Slide 51

SIT Internal

Summary

Memory Hierarchy

— From fast to slow: Registers, Cache, Main Memory,
Secondary Memory

CPU-Memory Interface
— Data, Address and Control Bus

The Main Memory
— Memory can be classified as RAM or ROM

— RAM can be Static RAM (SRAM) or Dynamic RAM
(DRAM)

— Types of ROM include PROM, EPROM, EEPROM,
Flash

Chapter 9: Primary Memory Subsystems


---
### Slide 52

SIT Internal

Thank you!

lou.xin@singaporetech.edu.sg

Chapter 9: Primary Memory Subsystems


---

# Chapter 10: Memory Management



---
### Slide 1

omnaroie: SIT Internal

ICT1011
Computer Organisation

and Architecture
Chapter 10

and Architecture
—)

Memory Management

1CT1011: Computer Organisation

Oba O
omg
[als
4 L J) Join at
©2024 slido.com

Steven Wong & ,
ee aL oe Chapter 10: Memory Management #1CT101 1 Pt2


---
### Slide 2

SIT Internal

Agenda for Today
Lecture on memory management
Quick review of part Il

. Miscellaneous (Quiz, Consultation, Project,
Exam)

Chapter 10: Memory Management


---
### Slide 3

SIT Internal

: What We Have Learned So Far?

The Fundamental of Computer
The Central Processing Unit
Instruction Set Architecture
Assembly Language Programming
input/output

Primary and Secondary Memory Subsystems

aiemyos

Instruction Set Architecture

Input / CPU

Output Memory
Transistors / Gates

COMPUTER SYSTEM

e1eMpseH


---
### Slide 4

SIT Internal

What Will We Learn Today?

. Uni and Multi-Program Systems
Swapping and Partitioning

. Paging

Chapter 10: Memory Management


---
### Slide 5

SIT Internal

Chapter 10: Memory

Management
. Uni and Multi-Program Systems

Chapter 10: Memory Management


---
### Slide 6

SIT Internal

Uni and Multi-Program Systems

_A typical computer system has many programs
that can be stored in the memory and executed

Uni-program System

_ — Uni-program means that the computer, at any one
time, can only be in the process of executing one
program (no concurrency)

— The computer must complete the execution of the
current program before execution of another program
can begin

— Memory split into two
¢ One for Operating System (monitor)
¢ One for currently executing program (“user”

Chapter 10: Memory Management


---
### Slide 7

SIT Internal

~ Uni and Multi-Program Systems

Problem:

I/O operations required by a program can be
very slow compared with CPU execution making
uni-program systems very inefficient

Multi-program Systems

_- More than one program can be executed
concurrently (but need not be simultaneously)

- The “user” memory is sub-divided and shared
among active processes

Chapter 10: Memory Management


---
### Slide 8

SIT Internal

Uni and Multi-Program Systems

roblem:
WO 7 oo 'G
very Program A Run Wait Run Wait aking
4 Time >
unl -f (a) Uniprogramming
Mult Program A Run Wait Run Wait
- Mc |
Program B Wait} Run Wait Run Wait
Col duSly)
- Th Combines a — Wait = rs Wait Jared
air Time >

(b) Multiprogramming with two programs

Chapter 10: Memory Management


---
### Slide 9

SIT Internal

Uni and Multi-Program Systems

Question:

But for multi-program systems, how can these
programs be stored and executed?

Memory Management

Chapter 10: Memory Management


---
### Slide 10

SIT Internal

Chapter 10: Memory
Management

Swapping and Partitioning

Chapter 10: Memory Management


---
### Slide 11

SIT Internal

Main Memory for Program Execution

Recall that Main Memory (e.g., DRAM) is much faster than
Secondary Memory (e.g., Hard Disk)

CPU executes programs directly from the secondary memory
is extremely inefficient and thus, modern computers only
execute programs loaded into main memor

* Problem: The capacity of the main memory is limited

Solution: Fetch the program to be executed from the
secondary memory to the main memory, then execute it.
A method of doing this is called Swapping

re
Processor mt) Cache (eed Main /4.....:

Secondary
L = Memory

Chapter 10: Memory Management


---
### Slide 12

Swapping

Process: A program in execution

Long-term queue: a queue of process requests, typically
stored on disk

Intermediate queue: a queue of existing processes that
have been temporarily kicked out of memory, typically
stored on disk

Processes “swapped” in as space becomes available

Disk storage

intermediate

queue Operating

Completed jobs
and user sessions

Long-term
queue

Chapter 10: Memory Management


---
### Slide 13

Swapping

As a process completes, it is moved out of main memory

If none of the processes in memory is ready (i.e., all I/O
blocked)

— Swap out a blocked process to intermediate queue
— Swap in a ready process or a new process

Swapping is an I/O operation

Disk storage

Main
intermediate ROSHOLY,
queue Operating
system
L t Completed jobs
ong-term i—— 3nd user sessions
queue Al-=— |

Chapter 10: Memory Management


---
### Slide 14

SIT Internal

Partitioning

* Partitioning: splitting memory into sections to
allocate to processes (including Operating
System)
Two Methods:

1. Fixed partition

2. Dynamic partition

Chapter 10: Memory Management


---
### Slide 15

SIT Internal

Partitioning — Fixed
_ Fixed-sized partition

* Size of each partition is fixed

we Operating System Operating System
¢ Partitions may or may not be of | _™ ™
equal size s im

¢ Process is fitted into smallest
partition that will take it (best fit) |  *

& 2M

Any problem with om

, this partitioning? om

16M

(a) Equal-size partitions (b) Unequal-size partitions
Chapter 10: Memory Management



---
### Slide 16

assem 2, aed
| SIT SIT Internal

=f



---
### Slide 17

SIT Internal

Partitioning — Fixed
_ Fixed-sized partition

* Size of each partition is fixed

we Operating System Operating System
¢ Partitions may or may not be of | _™ ™
equal size s im

* Process is fitted into smallest
partition that will take it (best fit) |  *

«/\* Any problem with on ha
, this partitioning? om
Some wasted memory! ™

(a) Equal-size partitions (b) Unequal-size partitions
Chapter 10: Memory Management



---
### Slide 18

SIT Internal

Partitioning — Dynamic

Dynamic Partitioning

When a process is placed into the main memory, the

exact required memory is allocated to the process
a &

p Any problem with this partitioning?

Chapter 10: Memory Management


---
### Slide 19

SIT Internal

Partitioning — Dynamic

Dynamic Partitioning

When a process is placed into the main memory, the
exact required memory is allocated to the process

Any problem with this partitioning?

The hole in the memory!

1. Ahole at the end of memory, too small to use (but only
one small hole - less waste)
2. When a process is swapped out, the new process
swapped in may be smaller than the swapped-out
process, thus, another hole is created

Chapter 10: Memory Management


---
### Slide 20

SiTpc SIT Internal
Effects of Dynamic Partitioning

Assume minimum process is 8MB.

8M

20M

14M

18M

1CT1011: Computer Organisation and Architecture

20

Steven Wore & Even though 16MByte left, only process<=6MByte can be loaded

Xin Lou



---
### Slide 21

SIT Internal

Effects of Dynamic Partitioning

Eventually there will be a lot of holes (this
phenomenon is known as_ external

fragmentation)

Solutions: @

Chapter 10: Memory Management


---
### Slide 22

SIT Internal

How to deal with fragmentation?



---
### Slide 23

SIT Internal

' Effects of Dynamic Partitioning
‘ Eventually there will be a lot of holes (this
- phenomenon is known as_ external

fragmentation)

ae i 8M 8M

5 . 4M 8M

$ meat (3 4M

2 18M 18M
_—Coalesce 30M 30M

Solutions: 2

¢ Join adjacent holes into one large hole

Chapter 10: Memory Management


---
### Slide 24

SIT Internal

_ Effects of Dynamic Partitioning
- Eventually there will be a lot of holes (this

phenomenon is known as_ external
fragmentation)

Solutions:

_—Coalesce

| ¢ Join adjacent holes into one large hole

_— Compaction
, * From time to time go through_ memory and_m
all holes into one free block gm

14M 14M

6M
8M
6M

8M

18M

18M
16M

Chapter 10: Memory Management 4M



---
### Slide 25

SIT Internal

Chapter 10: Memory
Management

Chapter 10: Memory Management


---
### Slide 26

SIT Internal
Paging
To overcome the problem of “holes” in basic partitioning,
Paging is used

Programs/processes are divided into equal sized small
chunks known as Pages

The main memory is divided into small chunks of equal
sizes. These chunks are known as Frames/ Page Frames

Size of Page Frame = Size of Page

The required number page frames are allocated to a
process

Operating System maintains the list of free frames

A process does not require contiguous page frames, thus
will need a Page Table to keep track of the memories
allocated

Chapter 10: Memory Management


---
### Slide 27

SIT Internal

Allocation of Free Space in
win Memory -

memory memory

Process A 13 Process A
0
14 Page 1
2
3

15

16

Free frame list Free frame list

13 17 20
14
My . Process A
1 age table
20 P —
14
20 15

Chapter 10: Memory Management


---
### Slide 28

SIT Internal

Relocation of Codes

There is no guarantee that a process will be loaded into the
same place in the main memory during swapping
But instructions could contain absolute addresses
— Locations of data

— Addresses for instructions (branching)
Solution: the user codes using Logical Addresses whilst
the CPU executes from the actual Physical Addresses

_-— Logical address (Virtual): a location relative to the
beginning of the program

— Physical address: actual location in memory

Translation between these addresses is the job of the
_ Memory Management Unit of the operating system

Chapter 10: Memory Management


---
### Slide 29

SIT Internal

Address Translation Scheme

- The Logical address is divided into:
_ QO) Page number (p): used as an index into a page table

_ O) Page offset/offset (d): relative address within a page, which can
be combined with physical base address (Frame number) to
define the physical memory address

Page number Page offset
n-m m

a Logical address space 2” and page size 2”

- e.g., N=16 bits and m=10 bits, then each page contains 1024 items
and totally 64 pages

Chapter 10: Memory Management


---
### Slide 30

Paging Hardware

SIT Internal

logical physical
address address 0000... 0000

7 0 eed

TETAT eee T4911

Page offset

Page frame

number
Chapter 10: Memory Management

physical
memory



---
### Slide 31

SIT Internal

Logical/Physical Address
Translation

ain
Logical Physical memory |
Address ; Address themey
age Page 1
13
Page No. Offset Frame No. Offset f ? of A —
Page 2 13 ah
1 30 13 30 oe 5
| a | 1 14 Page 2
15 Page 3 2 ofA
of A 3 —-
Page Frame rT, | 15[ soe
No. No. a) :
I ” use
0 18 17 use Free frame list rt
Pp. use
2 |" 16}P2929) | procera
page table 18 274
2 | 14 Ps 8
use 13 19 In
3 15 14 ani
20 1 »0
Process A
Page Table

Chapter 10: Memory Management


---
### Slide 32

SIT Internal

The logical address space contains 128Kbytes. The
physical address space contains 64Kbytes. The page
size is 2Kbytes. How many frames are there in this
system?

cote a Chapter 10: Memory Management


---
### Slide 33

SIT Internal

The logical address space contains 128Kbytes. The
physical address space contains 64Kbytes. The page
size is 2Kbytes. How many frames are there in this
system?

Chapter 10: Memory Management


---
### Slide 34

SIT Internal

Summary of Memory Management

— Uni-program and Multi-program

— Swapping: |/O operation between the hard disk and
main memory

— Partitioning: split memory into sections to allocate the
process; can cause fragmentations/holes

— Paging: divide process and memory into page and
frames; overcome the problem of holes

Chapter 10: Memory Management


---
### Slide 35

SIT Internal

Sit
___ Overall Summary Chapters 1-10

3 ICT1007: Operating System

§
a.
3
Ed
5
5 5
3 Computer
+ Reet _ System
>, aid} — n
po a oo oO
$ = Main Memory
y be

a 5 (Chpt 9)
= 5 = :
ea.
=
S

a+

3512

~ ©2024
Steven Wong &

Xin Lou”


---
### Slide 36

SIT Internal

Modular Programming

1. The stack operation
2. CALL and RET

3. Parameter Passing Methods
LRegisters

Li Memory

LI Stack



---
### Slide 37

SIT Internal

Input / Output Interfacing
Techniques

1. Basic I/O Interfacing Concepts

2. Digital Communications

_ OParallel and Serial data transfer

_U Duplex and Simplex data transfer

| USynchronous and Asynchronous data transfer

3. Memory Mapped I/O and Isolated I/O
4. Polled and Interrupt-driven I/O Technique

37 5. Bluetooth


---
### Slide 38

SIT Internal

b= Memory Subsystems (Primary

| and Secondary)
4. Memory Hierarchy

_ 2. Magnetic Hard Disk
-_ Q Structure and Read/Write mechanism
3 L) Data organization and formatting
~ O Performance

; 3. Redundancy and Surety (RAID 0, RAID 1 and
» RAID 10)

= 4, CPU-Memory Interfacing

* 5. Main Memory

6. RAM, ROM and Flash Technologies

: Memory Management (swapping, partitioning
and paging)



---
### Slide 39

SIT Internal

Module Assessment

Assessments

Lab quizzes = (30%) - Lab 2 (5%), Lab 3(5%) & Final Lab Quiz (20%)
Team project (20%) - Week 7 to Week 12

Quizzes (20%) — 10% Computer Architecture (15 half)

Ay) 10% Computer Organisation (2"¢ half)
“Ht sai © Hh (30%)
{J /f 1! Tf )

Chapter 0: |CT1011 Module Overview



---
### Slide 40

SIT Internal

Miscellaneous

Part Il review quiz (6% of the module marks)
Previous quizzes of part II for revision

Final Lab Quiz and Consultation: 29" November
(WK 13)

ULab quiz: 4:00 PM to 4:35 PM (Starts at 4:10PM)
Part |: Prof. Wong (4:40 PM to 5:10 PM)
UPart Il: Xin Lou (5:10 PM to 5:40 PM)

Project

UiDemonstration: 9 AM to 1 PM, 26 November
LIAIl documents submission: 2359hrs, 25th
November (Mon)

Exam: 4° December 2024


---
### Slide 41

SIT Internal

Module and Teaching Feedback

Module and Teaching
Feedback AY24/25, Tri1

_ 1. Complete both module and teaching feedback

2. Do not be rude and make personal attacks in the free text sections

3. Academic Staff will not be able to identify the student. All feedback received are anonymous
4.Their grades will not be affected as the feedback results will only be shared with the academic staff

after the release of exam results



---
### Slide 42

Thank you for the support! &

All the best in your final
assessments!

lou.xin@singaporetech.edu.sq



---

