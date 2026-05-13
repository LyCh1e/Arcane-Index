# ICT1012 Operating Systems Notes

*Comprehensive lecture notes compiled from all lecture slides.*  
*Course: ICT1012 Operating Systems — Singapore Institute of Technology*

---

## Table of Contents

1. [Chapter 1: Introduction to Operating Systems](#chapter-1-introduction-to-operating-systems)
2. [Chapter 2: System Calls](#chapter-2-system-calls)
3. [Chapter 3: Processes](#chapter-3-processes)
4. [Chapter 4: Threads and Concurrency](#chapter-4-threads-and-concurrency)
5. [Chapter 5: CPU Scheduling](#chapter-5-cpu-scheduling)
6. [Chapter 6: Synchronization](#chapter-6-synchronization)
7. [Chapter 7: File Systems Interface](#chapter-7-file-systems-interface)
8. [Chapter 7b: File System Implementation](#chapter-7b-file-system-implementation)
9. [Chapter 8: Main Memory](#chapter-8-main-memory)
10. [Chapter 9: Virtual Memory](#chapter-9-virtual-memory)
11. [Chapter 10: Deadlocks](#chapter-10-deadlocks)

---


# Chapter 1: Introduction to Operating Systems

## Slide 1

ICT1012
Operating Systems
1. Introduction
Dr. David Sanan

## Slide 2

Who are we?
• Shang-wei Lin
• Lecture + Tutorial/Lab
• Tel : 6592 1497
• shangwei.lin@singaporetech.edu.sg
• David Miguel Sanan Baena
• Lecture + Tutorial/Lab
• Tel : 6592 3043
• david.sanan@singaporetech.edu.sg
• Mr. Eric Lam Tutorial/Lab
• IF_Eric.Lam@singaporetech.edu.sg

## Slide 3

• Teaching Activities
• Lectures – 2 hours per week
• Tuesday, 11 am – 13 noon (online)
• Tutorials and Laboratory - 2 hours alternate week (starting with Week 2)
DAY Start Time End Time Venue Group Faculty
Thursday 9:00 AM 11:00 AM E2-06-02 P5/T5
HAW JU ERIC LAM, SAHAYA 
FRANCIS
Thusrday 11:00 AM 1:00 PM E2-06-02 P6/T6 HAW JU ERIC LAM
Thursday 2:00 PM 4:00 PM E2-06-02 P7/T7 DAVID SANAN
Thursday 4:00 PM 6:00 PM E2-06-02 P8/T8 SHANG-WEI LIN
Friday 9:00 AM 11:00 AM E2-06-02 P1/T1 HAW JU ERIC LAM
Friday 12:00 PM 2:00 PM E2-06-02 P2/T2 HAW JU ERIC LAM
Friday 2:00 PM 4:00 PM E2-06-02 P3/T3 HAW JU ERIC LAM
Friday 4:00 PM 6:00 PM E2-06-02 P4/T4 HAW JU ERIC LAM
Who are we?

## Slide 4

Text Material (always recommended first)
• Referencing resources
• A. Silberschatz, P. Galvin, and G. Gagne, Operating System Concepts (Ninth 
Edition) , John Wiley & Sons, Inc., 2019.
• Recommended Resources
• Brian W. Kernighan , Dennis M. Ritchie, C Programming Language, 2nd 
Edition
Resources
Video Materials
OS Course from University of California Berkeley
OS Course from University of Wisconsin-Madison
OS Course from University of Massachusetts Amherst
Mitch Davis Course on OS

## Slide 5

• Lab Sessions(30% - graded by POs)
• Test your practical skills 
• Lab 1 is ungraded
• For Lab 2 to Lab 5 (7.5% each)
• Lab Quiz 
• Submission of Lab work 
• Individually assessed
• Assignment(35% - graded by respective faculty)
• Test your ability to implement certain aspects of an Operating System.
• Group assessment based on demonstration and sourcecode
• Team of 5 or 6
• Exam (35% - graded by both lecturers)
• Test your overall understanding of the subject.
• Mainly focus on the lecturematerials.
Grading

## Slide 6

• Introduction to the 
Operating Systems
• their structure
• what they do
• how they are
designed and
constructed
• Memory
Management
• Memory Hierarchy
and Memory 
Management Unit
• Linking and
Memory 
Allocation
• Fragmentation
• Paging
• Segmentation
• Virtual
Memory 
Management
• Demand Paging
• Page Replacement
• Thrashing
• File System 
Management 
and Storage
Management
• FileAttributes
• Directory
Structure
• File System
Structure
• Mass Storage
Structure
• I/O Systems
Module Overview
• Process Management
• Process concept
• Process Scheduling
• Threads
• Multithreaded Programming
• Synchronisation
• Mutex Locks and Semaphores
• Deadlocks

## Slide 7

• To describe what Operating Systems are, and how they are designed.
• To describe and explain Process Management (e.g. scheduling, 
synchronisation, etc)
• To describe and explain Memory Management
(Memory Hierarchy, the Memory Management Unit, Paging and Fragmentation)
• To describe and explain Virtual Memory Management (Demand 
Paging and Page Replacement Algorithms)
• To describe and explain File System Structure & Mass Storage Structure.
• To describe and explain I/O System.
Learning Outcomes

## Slide 8

1. What is an Operating System?
▪ Which is/are operating system(s)?
▪ Windows 11 and its software
▪ Ubuntu Kernel and the drivers
▪ Graphical User Interface
▪ The software on a DJI drone
▪ Microsoft
▪ The software on a new Samsung phone
▪ Raspberry Pi
▪ The C library, LibC
https://app.sli.do/event/nCBrEY9JskYD8zZACDSt2T

## Slide 9

What is an Operating System?
▪ How do you think an operating system should be defined?
▪ I don’t know
▪ Nobody Knows
▪ The text book claims to know
▪ They are programs, BIG PROGRAMS
▪ They are programs that make writing other programs easier –
The raw hardware is an unforgiving place to execute..
https://app.sli.do/event/nCBrEY9JskYD8zZACDSt2T

## Slide 10

What is an Operating System?
▪ A program that acts as an intermediary
between a user of a computer and the 
computer hardware
▪ Operating system goals:
▪ Provide users with an interface to 
hardware.
▪ Give a friendly environment for 
users
▪ Execute user programs and make 
solving user problems easier
▪ Resource Management: Use the 
computer hardware in an efficient 
manner

## Slide 11

What is an Operating System?
▪ A program that acts as an intermediary
between a user of a computer and the 
computer hardware

## Slide 12

What is an Operating System?
▪ A program that acts as an intermediary
between a user of a computer and the 
computer hardware

## Slide 13

Computer System Structure
▪ Computer system can be divided into four 
components:
▪ Hardware – provides basic computing 
resources
▪ CPU, memory, I/O devices
▪ Operating system
▪ Controls and coordinates use of 
hardware among various applications 
and users
▪ Application programs – define the ways in 
which the system resources are used to solve 
the computing problems of the users
▪ Word processors, compilers, web 
browsers, database systems, video 
games
▪ Users
▪ People, machines, other computers

## Slide 14

Computer System Structure
▪ Applications cannot directly 
manipulate (many of) the hardware 
components. They have to ask the 
OS to do it on their behalf
▪ It is a security basis
▪ Various apps/hardware – content 
and extensions are constantly 
changing

## Slide 15

What Operating Systems Do
Provide a HW abstraction for applications:
CPU
Memory
I/O Devices
Manage HW and build ecosystem for Apps

## Slide 16

What Operating Systems Do
Manage HW and build ecosystem for Apps
OS is a resource allocator
Manages resources:
CPU
Memory
I/O Devices
Decides between 
conflicting requests for 
efficient and fair 
resource use (e.g., 2 
processes need to use 
CPU, which to assign?)

## Slide 17

What Operating Systems Do
Manage HW and build ecosystem for Apps
Provides Synchronization for processes
The OS provides efficient synchronization 
among applications

## Slide 18

What Operating Systems Do
Manage HW and build ecosystem for Apps
Provides Communication for applications
Applications can use the network for interprocess communication (loop-back devices)
The OS provides local communication:
Pipes
Shared Memory
Passing Messages

## Slide 19

What Operating Systems Do
Operating System Concepts – 10
th Edition 1.15 Silberschatz, Galvin and Gagne ©2018
Manage HW and build ecosystem for Apps
Manage HW and build ecosystem for Apps
√
√
√
√
√
√

## Slide 20

What Operating Systems Do
Operating System Concepts – 10
th Edition 1.15 Silberschatz, Galvin and Gagne ©2018
Manage HW and build ecosystem for Apps
Manage HW and build ecosystem for Apps
√
√
√
√
√
√
Is it enough?

## Slide 21

What Operating Systems Do
Is it enough? Not Always
These operating systems are
very specialized. It is enough for
them to do their tasks as
required.

## Slide 22

What Operating Systems Do
Is it enough? Not Always

## Slide 23

What Operating Systems Do
Is it enough? Not Always
Nokia and Blackberry dominated the market in 2006.
They were very secure devices with as many functionalities, if no 
more, as iOS/Android when they were released in 2007.

## Slide 24

What Operating Systems Do
Is it enough? Not Always
Nokia and Blackberry dominated the market in 2006.
They were very secure devices with as many functionalities, if no 
more, as iOS/Android when they were released in 2007.

## Slide 25

What Operating Systems Do
Is it enough? Not Always
What was the actual innovation of the new systems?

## Slide 26

What Operating Systems Do
Is it enough? Not Always
APPLICATIONS…

## Slide 27

What Operating Systems Do
Is it enough? Not Always
APPLICATIONS…

## Slide 28

What Operating Systems Do
Is it enough? Not Always
APPLICATIONS…
Developers could only use complex APIs not documented to access the phone features.

## Slide 29

What Operating Systems Do
Is it enough? Not Always
APPLICATIONS…
Apple and Google focused their systems on DEVELOPERS.
They created a set of well documented APIs that ease 
implementing applications using the device features

## Slide 30

Operating System Definition
▪ No universally accepted definition
▪“Everything a vendor ships when you order an operating system” is 
good approximation
▪ But varies wildly
▪“The one program running at all times on the computer” is the kernel. 
Everything else is either a system program (ships with the operating 
system) or an application program.

## Slide 31

2. Computer-System Organization
▪ Computer-system operation
▪ One or more CPUs, device controllers connect through common bus providing 
access to shared memory
▪ Concurrent execution of CPUs and devices competing for memory cycles

## Slide 32

Computer-System Operation
RAM → Local Buffer → Device → Local Buffer → RAM
▪ I/O devices and the CPU can execute 
concurrently 
▪ Each device controller is in charge of a 
particular device type
▪ Each device controller has a local buffer 
(storage). CPU moves data from/to main 
memory to/from buffers
▪ I/O is from the device to local buffer of controller
▪ Device controller informs CPU that it has 
finished its operation by causing an interrupt
▪ Device drivers provide the operating system with 
a uniform interface to access the device

## Slide 33

Processor (Top-Level Components)
OS Data
Interrupt table i
i+1
i+m
k0
kj
k+p
k1
km
Interrupt 
handler j

## Slide 34

Computer Startup
▪ bootstrap program is loaded at power-up or reboot
▪ Typically stored in ROM or EPROM, generally known as firmware
▪ Initializes all aspects of system
▪ Loads operating system kernel and starts execution
RAM
Bootstrap Program
Operating System
Operating System
Devices
Read OS
Load OS
Start 
Device
Drivers
ROM
Main Memory

## Slide 35

I/O Structure
I/O An important functionality of an 
Operating System is to handle 
Input/Output operations.
The OS must efficiently handle access 
to devices to allow concurrent access 
and preserve data consistency
Device Drivers
Use of Buffers
Use of Caches
drivers
Buffers Cache

## Slide 36

Direct Memory Access Structure
Used for high-speed I/O devices able to 
transmit information at close to memory 
speeds
Device controller transfers blocks of data 
from buffer storage directly to main 
memory without CPU intervention
Only one interrupt is generated per block, 
rather than the one interrupt per byte

## Slide 37

Program Control Flow Without Interrupts
User Program I/O Routine
Write
Write
I/O Processing
1
2
3
4
5
User program performs a series of Write calls
Code Segments 1, 2, and 3 refer to sequences 
of instructions (no I/O)
Write call will transfer to I/O routine and the 
User Program waits.
Segment 4: prepare for I/O operation 
(copy data, prepare parameters)
Actual I/O execution: must wait for I/O 
device to perform the requested function
Segment 5: complete I/O operation

## Slide 38

Program Control Flow Without Interrupts
User Program I/O Routine
Write
Write
I/O Processing
1
2
3
4
5
Actual I/O execution: must wait for I/O device 
to perform the requested function
What happens when the device is busy?
Polling: The user program will keep checking 
the device status until the device is not busy 
(active waiting).
As a consequence, the operational flow will be as it follows:
• User program executes Segment 1.
• The Write operation will trigger the handler to process the I/O 
request:
• Executes Segment 4
• The I/O operation is carried out
• Executes Segment 5
• Returns to the user space
• User Program executes Segment 2

## Slide 39

Program Control Flow Without Interrupts
User Program I/O Routine
Write
Write
I/O Processing
1
2
3
4
5
As a consequence, the operational flow will be as it follows:
• User program executes Segment 1.
• The Write operation will trigger the handler to process the 
first I/O request:
• Executes Segment 4
• The I/O operation is carried out
• Executes Segment 5
• Returns to the user space
• User Program executes Segment 2 after completing the first 
write
• The Write operation will trigger the handler to process the 
second I/O request:
• Executes Segment 4
• The I/O operation is carried out
• Executes Segment 5
• Returns to the user space
• User Program executes Segment 3 after completing the 
second write

## Slide 40

Program Control Flow Without Interrupts
Save
100% Usage

## Slide 41

Interrupt Cycle
Start Fetch
Instruction
Execute
Instruction
IE
Saver context; Initiate 
interrupt handler
Interrupts
Enabled
Yes
No
PI
Pending 
Interrupts
No
Yes
1
2
3
1. Processor checks for interrupts
2. If interrupts are enabled and there is any 
pending, save context of the current 
program and execute the interrupt-handler
3. If interrupts are disabled or no pending 
interrupts, fetch the next instruction for 
the current program and execute it.

## Slide 42

Program Control Flow With Interrupts
User Program I/O Routine
Write
I/O Processing
1
2A
4
5
After segment 4 (actual I/O command started), 
control return to user program and continue 
its own execution in segment 2 (no waiting)
External device performs its own operation 
concurrently
Once the external device is done, it will send 
an interrupt request to the processor 
(between 2a&2b)
The processor halts user’s program execution, 
branchs off to segment 5 and complete the 
operation
Interrupt 
Handler
2B

## Slide 43

Program Control Flow With Interrupts
User Program I/O Routine
Write
I/O Processing
1
2A
4
5
Interrupt 
Handler
2B
• User program executes Segment 1.
• The Write operation will trigger the handler to process the 
I/O request:
• Executes Segment 4
• Starts the I/O operation
• Returns to user space while the I/O operation is still 
being carried out
• User Program executes Segment 2 while the data is being 
written:
• At time T, the writing operation finishes, until the time 
one part of Segment 2 has been executed (called 2A) 
but not necessary the whole segment.
• The OS interrupts the user program to execute the 
interrupt handler represented by Segment 5
• After the interrupt handler has finished, Segment 2 
continues its execution to finish the rest of the 
segment (segment 2B).
T

## Slide 44

Program Control Flow With Interrupts
Save
~0% Usage

## Slide 45

Changes in Memory and Registers for an interrupt
Start
N + 1
Y + L
N
Y
Y
T
Return
User's
Program
Main
Memory
Processor
General
Registers
Program
Counter
Stack
Pointer
N + 1
T – M
T – M
T
Control
Stack
Interrupt
Service
Routine
User's
Program
Interrupt
Service
Routine
(a) Interrupt occurs after instruction
Start
N + 1
Y + L
N
Y
T
Return
Main
Memory
Processor
General
Registers
Program
Counter
Stack
Pointer
Y + L
T – M
T – M
T
Control
Stack
N + 1
1
2
3
4
1. After the execution of instruction at 
location N, an interrupt occurs (PC = N+1)
2. Save context (all registers + PC) onto the 
stack (M words)
3. Update stack pointer to position (T-M). For 
example, if Stack Pointer is 0x09 and the 
context size is 8 bytes the new stack will be 
0x09 – 8 = 0x01
4. Program Counter update to the interrupt 
handler address

## Slide 46

Changes in Memory and Registers for an interrupt
Y
am
Processor
General
Registers
Program
Counter
Stack
Pointer
N + 1
T – M
T
upt
e
ne
User's
Program
Interrupt
Service
Routine
Start
N + 1
Y + L
N
Y
T
Return
Main
Memory
Processor
General
Registers
Program
Counter
Stack
Pointer
Y + L
T – M
T – M
T
Control
Stack
N + 1
1
2.1
2.2
1. At the end of interrupt
2. Retrieve context back to registers 
(registers + PC)
2.1 The PC register is updated with the 
previous value N+1 that was store in the 
stack.
2.1 The Stack pointer is restored to the 
previous value T, also stored in the stack.
3. The execution of the user program 
continues in N+1

## Slide 47

Questions ?
david.sanan@singaporetech.edu.sg


---

# Chapter 2: System Calls

## Slide 1

ICT1012
Operating Systems
2. System Calls
Dr. David Sanan

## Slide 2

Functionality Mechanisms
Multiprogramming and Multitasking Concept of Process
Process Scheduling
Process Swapping
Virtual Memory
Interrupt Processing Interrupt Table
Interrupt Handlers
System Protection Execution Modes (User and Kernel)
System Calls (Execute controlled 
privileged instructions)
System and Process Clocks Timers
Multi-Mode Operations Virtual Machine Support
1. OS Functionality, Mechanisms, and Implementation

## Slide 3

Operating System Services 
process 
management

## Slide 4

Operating System Services 
process 
management
https://app.sli.do/event/ebCXVcFwZEZyVYpTHMgQxS
Enumerate services that you think the OS should provide through system 
calls. You can use system-call group / service name. For example, file 
system / open file.
https://app.sli.do/event/ebCXVcFwZEZyVYpTHMgQxS
Enumerate services that you think the OS should provide through system 
calls. You can use system-call group / service name. For example, file 
system / open file.

## Slide 5

▪ One set of operating-system 
services provides functions that are 
helpful to the user:
▪ User interface - Almost all 
operating systems have a user 
interface (UI).
▪ Varies between 
Command-Line (CLI), 
Graphics User Interface 
(GUI), Batch
▪ Program execution - The 
system must be able to load a 
program into memory and to 
run that program, end 
execution, either normally or 
abnormally (indicating error)
Operating System Services

## Slide 6

▪ One set of operating-system 
services provides functions that are 
helpful to the user:
▪ User interface - Almost all 
operating systems have a user 
interface (UI).
▪ Varies between 
Command-Line (CLI), 
Graphics User Interface 
(GUI), Batch
▪ Program execution - The 
system must be able to load a 
program into memory and to 
run that program, end 
execution, either normally or 
abnormally (indicating error)
Operating System Services

## Slide 7

▪ One set of operating-system 
services provides functions that are 
helpful to the user:
▪ I/O operations - A running 
program may require I/O, 
which may involve a file or an 
I/O device
▪ File-system manipulation - 
The file system is of particular 
interest. Programs need to 
read and write files and 
directories, create and delete 
them, search them, list file 
Information, permission 
management.
Operating System Services

## Slide 8

▪ One set of operating-system 
services provides functions that are 
helpful to the user:
▪ I/O operations - A running 
program may require I/O, 
which may involve a file or an 
I/O device
▪ File-system manipulation - 
The file system is of particular 
interest. Programs need to 
read and write files and 
directories, create and delete 
them, search them, list file 
Information, permission 
management.
Operating System Services

## Slide 9

▪ Communications – Processes may 
exchange information, on the same 
computer or between computers 
over a network
▪ Communications may be via 
shared memory or through 
message passing (packets 
moved by the OS)
▪ Error detection – OS needs to be 
constantly aware of possible errors
▪ May occur in the CPU and 
memory hardware, in I/O 
devices, in user program
▪ For each type of error, OS 
should take the appropriate 
action to ensure correct and 
consistent computing
▪ Debugging facilities can greatly 
enhance the user’s and 
programmer’s abilities to 
efficiently use the system
Operating System Services

## Slide 10

▪ Communications – Processes may 
exchange information, on the same 
computer or between computers 
over a network
▪ Communications may be via 
shared memory or through 
message passing (packets 
moved by the OS)
▪ Error detection – OS needs to be 
constantly aware of possible errors
▪ May occur in the CPU and 
memory hardware, in I/O 
devices, in user program
▪ For each type of error, OS 
should take the appropriate 
action to ensure correct and 
consistent computing
▪ Debugging facilities can greatly 
enhance the user’s and 
programmer’s abilities to 
efficiently use the system
Operating System Services

## Slide 11

▪ Another set of OS functions exists 
for ensuring the efficient 
operation of the system itself via 
resource sharing
▪ Resource allocation -
When multiple users or 
multiple jobs running 
concurrently, resources must 
be allocated to each of them
▪ Many types of 
resources - Some 
(such as CPU cycles, 
main memory, and file 
storage) may have 
special allocation code, 
others (such as I/O 
devices) may have 
general request and 
release code
▪ Accounting - To keep track 
of which users use how 
much and what kinds of 
computer resources
Operating System Services

## Slide 12

▪ Another set of OS functions exists 
for ensuring the efficient 
operation of the system itself via 
resource sharing
▪ Resource allocation -
When multiple users or 
multiple jobs running 
concurrently, resources must 
be allocated to each of them
▪ Many types of 
resources - Some 
(such as CPU cycles, 
main memory, and file 
storage) may have 
special allocation code, 
others (such as I/O 
devices) may have 
general request and 
release code
▪ Accounting - To keep track 
of which users use how 
much and what kinds of 
computer resources
Operating System Services

## Slide 13

▪ Another set of OS functions exists for 
ensuring the efficient operation of the 
system itself via resource sharing
▪ Protection and security - The 
owners of information stored in a 
multiuser or networked computer 
system may want to control use of 
that information, concurrent 
processes should not interfere with 
each other
▪ Protection involves ensuring 
that all access to system 
resources is controlled
▪ Security of the system from 
outsiders requires user 
authentication, extends to 
defending external I/O devices 
from invalid access attempts
▪ If a system is to be protected 
and secure, precautions must 
be instituted throughout it. A 
chain is only as strong as its 
weakest link.
Operating System Services

## Slide 14

▪ Programming interface to the 
services provided by the OS
▪ Typically written in a high-level 
language (C or C++)
▪ System calls are invoked by 
triggering specific interruptions 
that the CPU Instruction Set 
Architecture (ISA) reserves for 
OS purposes.
2. System calls Olden x86
0x80 linux
0x2E Windows
Interrupt table
0x2E_handler:
Check register eax
for specific call
Arguments to the 
call are placed in 
other registers like 
ebx, ecx, etc.
Introduces overhead when looking for the specific call
int ISA call
int 0x2E

## Slide 15

▪ Programming interface to the 
services provided by the OS
▪ Typically written in a high-level 
language (C or C++)
▪ System calls are invoked by 
triggering specific interruptions 
that the CPU Instruction Set 
Architecture (ISA) reserves for 
OS purposes.
Current approach reducing overhead
Reduces overhead by directly jumping to a specific call
RAX Contains the system call number
RCX, RDX, R8, R9, R10, R11 contains 
arguments to the call
syscall
System Calls

## Slide 16

▪ Programming interface to the 
services provided by the OS
▪ Typically written in a high-level 
language (C or C++)
▪ Mostly accessed by programs 
via a high-level Application 
Program Interface (API) rather 
than direct system call use; API 
specifies a set of functions that 
are available to an application 
programmer, including the 
parameters that are passed and 
expected return values
System Calls

## Slide 17

System Calls
▪ Three most common APIs are 
Win32 API for Windows, POSIX 
API for POSIX-based systems 
(including virtually all versions 
of UNIX, Linux, and Mac OS X), 
and Java API for the Java 
virtual machine (JVM)
▪ Why use APIs rather than 
system calls?

## Slide 18

System Calls
▪ Three most common APIs are 
Win32 API for Windows, POSIX 
API for POSIX-based systems 
(including virtually all versions 
of UNIX, Linux, and Mac OS X), 
and Java API for the Java 
virtual machine (JVM)
▪ Why use APIs rather than 
system calls? 
https://app.sli.do/event/ebCXVcFwZEZyVYpTHMgQxS
What benefits do we get by accessing system calls through an API?

## Slide 19

System Calls
▪ Three most common APIs are 
Win32 API for Windows, POSIX 
API for POSIX-based systems 
(including virtually all versions of 
UNIX, Linux, and Mac OS X), and 
Java API for the Java virtual 
machine (JVM)
▪ Why use APIs rather than system 
calls? 
▪ Provide an abstraction of the 
function call behaviour
▪ Provide interoperability among 
different OS/HW versions
▪ Usually implement efficient 
access to the System Call
(Note that the system-call names 
used throughout this text are 
generic)

## Slide 20

System Call Implementation
▪ Typically, a number associated with each 
system call
▪ System-call interface maintains a 
table indexed according to these 
numbers
▪ The system call interface invokes intended 
system call in OS kernel and returns 
status of the system call and any return 
values
▪ The caller need know nothing about how 
the system call is implemented
▪ Just needs to obey API and 
understand what OS will do as a 
result call
▪ Most details of OS interface hidden 
from programmer by API 
▪ Managed by run-time support 
library (set of functions built into 
libraries included with compiler)

## Slide 21

System Call Parameter Passing 
▪ Often, more information is required than 
simply identity of desired system call
▪ Exact type and amount of information 
vary according to OS and call
▪ Three general methods used to pass 
parameters to the OS
▪ Simplest: pass the parameters in 
registers
▪ In some cases, may be more 
parameters than registers
1
2
3
mov 1 r1
mov 2 r2
mov 3 r3
call func
func(1,2,3)

## Slide 22

System Call Parameter Passing
▪ Often, more information is required than 
simply identity of desired system call
▪ Exact type and amount of information 
vary according to OS and call
▪ Three general methods used to pass 
parameters to the OS
▪ Parameters stored in a block, or 
table, in memory, and address of 
block passed as a parameter in a 
register 
▪ This approach taken by Linux and 
Solaris

## Slide 23

System Call Parameter Passing
▪ Often, more information is required than 
simply identity of desired system call
▪ Exact type and amount of information 
vary according to OS and call
▪ Three general methods used to pass 
parameters to the OS
▪ Parameters placed, or pushed, onto 
the stack by the program and popped
off the stack by the operating system
Parameters passed in a block, or by storing them in the stack do no limit the number of arguments
push 1
push 2
push 3
call func
func(1,2,3)
3
2
1
SP

## Slide 24

System Call Security
▪ HW Security System calls can execute 
privilege ISA instructions. These are 
instructions that user applications cannot 
invoke:

## Slide 25

System Call Security
▪ HW Security System calls can execute 
privilege ISA instructions. These are 
instructions that user applications cannot 
invoke:
https://app.sli.do/event/ebCXVcFwZEZyVYpTHMgQxS
What kind CPU instructions might be privileged? Give some examples

## Slide 26

System Call Security
▪ Security System calls can execute privilege ISA 
instructions. These are instructions that user 
applications cannot invoke:
▪ Access/modifications of registers
▪ LGDT / SGDT: Load/Store Global Descriptor Table 
register.
▪ MOV CRx: Move values to/from control registers (CR0, 
CR2, CR3, CR4, etc.).
▪ HLT: Halt the processor (requires the system to be in a 
privileged state).
▪ Certain (Virtual) memory-related 
operations
▪ LGDT / LIDT: Manipulate descriptor tables for memory 
management.
▪ Interrupt handling
▪ INT n: Software interrupt (some interrupts may require 
privilege depending on the vector).
▪ IRET / IRETD: Return from an interrupt (restoring 
processor state).
▪ System Management
▪ RDPMC: Read Performance Monitoring Counters (may 
require privilege based on configuration).
▪ Virtualisation
▪ VMRUN: Launch a virtual machine

## Slide 27

System Call Security
▪ By forbidding these instructions, prevent 
user-mode applications from:

## Slide 28

System Call Security
▪ By forbidding these instructions, prevent 
user-mode applications from:
https://app.sli.do/event/ebCXVcFwZEZyVYpTHMgQxS
How having a privileged mode of operation can benefit security?

## Slide 29

System Call Security
▪ By forbidding these instructions, prevent 
user-mode applications from:
▪ Obtaining unauthorized access to 
critical resources
▪ Disabling or interfering with essential 
system functions like interrupts or 
memory management
▪ Tamper kernel structures

## Slide 30

System Call Security
▪ How it works: When the CPU executes a 
instruction that goes to kernel model, it 
automatically modifies a bit indicating 
privilege mode in a system register (CPL 
for Intel architectures). And set it back to 
original value when the control goes back 
to the user.
CS Register
Current Privilege Level (CPL)
0 1
1 1
System Call

## Slide 31

System Call Security
▪ How it works: When the CPU executes a 
instruction that goes to kernel model, it 
automatically modifies a bit indicating 
privilege mode in a system register (CPL 
for Intel architectures). And set it back to 
original value when the control goes back 
to the user.
CS Register
Current Privilege Level (CPL)
0 1
0 0
System Call
The system call will be able to execute privilege instructions

## Slide 32

System Call Security
▪ How it works: When the CPU executes a 
instruction that goes to kernel model, it 
automatically modifies a bit indicating 
privilege mode in a system register (CPL 
for Intel architectures). And set it back to 
original value when the control goes back 
to the user.
CS Register
Current Privilege Level (CPL)
0 1
1 1
System Call
return
After returning to the user space, the user 
app cannot execute privilege instructions

## Slide 33

Design Approaches
The design of an OS can follow different approaches
Layer 0 (HW)
Layer N (User Interface)
Layered approach Modular Approach

## Slide 34

Design Approaches
The design of an OS can follow different approaches
Layer 0 (HW)
Layer N (User Interface)
Layered approach Modular Approach
https://app.sli.do/event/ebCXVcFwZEZyVYpTHMgQxS
Give benefits and disadvantages of the layered and modular approaches

## Slide 35

Layered Approach
▪ The operating system is 
divided into a number of 
layers (levels), each built 
on top of lower layers. 
The bottom layer (layer 
0), is the hardware; the 
highest (layer N) is the 
user interface.
▪ With modularity, layers 
are selected such that 
each uses functions 
(operations) and services 
of only lower-level layers
▪ Implemented in: Linux, 
MacOS, Windows

## Slide 36

Modules
▪ Most modern operating systems implement loadable
kernel modules
▪ Uses object-oriented approach
▪ Each core component is separate
▪ Each talks to the others over known interfaces
▪ Each is loadable as needed within the kernel
▪ Overall, similar to layers but with more flexible
▪ Linux, Solaris, Windows

## Slide 37

3. Design Approaches
The design of an OS can follow different approaches
Application ProgramFile SystemDevice Driver
Interprocess Communication memory managment CPU
scheduling messages messages microkernel hardware
user mode
kernel mode
Micro-Kernel
Signal 
Handling
File 
System
Memory
Management
Virtual 
Memory Drivers
Monolithic
Authentication
Libraries
User 
Interface
Applications Services
Kernel Space
User Space

## Slide 38

3. Design Approaches
The design of an OS can follow different approaches
Application ProgramFile SystemDevice Driver
Interprocess Communication memory managment CPU
scheduling messages messages microkernel hardware
user mode
kernel mode
Micro-Kernel
Signal 
Handling
File 
System
Memory
Management
Virtual 
Memory Drivers
Monolithic
Authentication
Libraries
User 
Interface
Applications Services
Kernel Space
User Space
https://app.sli.do/event/ebCXVcFwZEZyVYpTHMgQxS
Give benefits and disadvantages of the Micro-Kernel and Monolithic 
approaches

## Slide 39

Microkernel System Structure 
▪ Moves as much from the kernel into user space
▪ Mach example of microkernel
▪ Mac OS X kernel (Darwin) partly based on Mach
▪ HarmonyOS NEXT (Huawei) Separation microkernel extended with independent services layers.
▪ Communication takes place between user modules using 
message passing
▪ Benefits:
▪ Easier to extend a microkernel
▪ Easier to port the operating system to new 
architectures
▪ More reliable (less code is running in kernel mode)
▪ More secure
▪ Detriments:
▪ Performance overhead of user space to kernel space 
communication Application Program
File SystemDevice Driver
Interprocess Communication memory managment CPU
scheduling
messages messages
microkernel
hardware
user mode
kernel mode

## Slide 40

UNIX/Linux/Windows until NT – Monolithic
Beyond simple but not fully layered
▪ UNIX – limited by hardware functionality, 
the original UNIX operating system had 
limited structuring. The UNIX OS 
consists of two separable parts
▪ Systems programs
▪ The kernel
▪ Consists of everything below the systemcall interface and above the physical 
hardware
▪ Provides the file system, CPU 
scheduling, memory management, and 
other operating-system functions; a large 
number of functions for one level

## Slide 41

Hybrid Kernels
▪ Combine a micro-kernel with extended functionality to enhance performance
Windows NT Mac OS X Kernel (Darwin)
Mach
I/O
Drivers
File System Network Memory 
Management
BSD

## Slide 42

4. Computing Environments - Traditional
▪ Stand-alone general purpose machines
▪ But blurred as most systems interconnect with 
others (i.e. the Internet)
▪ Portals provide web access to internal 
systems
▪ Network computers (thin clients) are like 
Web terminals
▪ Mobile computers interconnect via wireless 
networks
▪ Networking becoming ubiquitous – even home 
systems use firewalls to protect home 
computers from Internet attacks

## Slide 43

Mobile Operating Systems
▪ Handheld smartphones, tablets, etc.
▪ What is the functional difference between them 
and a “traditional” laptop?
▪ Extra feature – more OS features (GPS, 
gyroscope)
▪ Allows new types of apps like augmented 
reality
▪ Use IEEE 802.11 wireless, or cellular data 
networks for connectivity
▪ Leaders are Apple iOS and Google Android

## Slide 44

Virtualization
▪ Allows operating systems to run applications 
within other OSes
▪ Vast and growing industry
▪ Emulation used when source CPU type 
different from target type (i.e. ARM to Intel 
x86)
▪ Generally slowest method
▪ When computer language not compiled to 
native code – Interpretation
▪ Virtualization – OS natively compiled for 
CPU, running guest OSes also natively 
compiled 
▪ Consider VMware running WinXP guests, 
each running applications, all on native WinXP
host OS
▪ VMM (virtual machine manager) provides 
virtualization services

## Slide 45

Real-Time Embedded Systems
▪ Real-time embedded systems most prevalent form of computers
▪ Vary considerable, special purpose, limited purpose OS, real-time OS
▪ Use expanding
▪ Many other special computing environments as well
▪ Some have OSes, some perform tasks without an OS
▪ Real-time OS has well-defined fixed time constraints
▪ Processing must be done within constraint
▪ Correct operation only if constraints met

## Slide 46

Questions ?
david.miguel@singaporetech.edu.sg


---

# Chapter 3: Processes

## Slide 1

ICT1012
Operating Systems
3. Processes
Dr. David Sanan

## Slide 2

Chapter 3: Process Concept
§ Process Concept
§ Process Scheduling
§ Operations on Processes
§ Interprocess Communication
§ Communication in Client-Server Systems

## Slide 3

Objectives
§ To introduce the notion of a process -- a program in execution, which forms the basis of 
all computation
§ To describe the various features of processes, including scheduling, creation and 
termination, and communication
§ To explore interprocess communication using shared memory and message passing
§ To describe communication in client-server systems

## Slide 4

Process Concept
§ An operating system executes a variety of 
programs:
§ Batch system – jobs
§ Time-shared systems – user programs or 
tasks
§ Process – a program in execution; process 
execution must progress in sequential fashion
§ Program is passive entity stored on disk 
(executable file), process is active 
§ Program becomes process when executable 
file loaded into memory
§ Execution of program started via GUI mouse 
clicks, command line entry of its name, etc
§ One program can be several processes
§ Consider multiple users executing the same 
program

## Slide 5

Process State
§ As a process executes, it changes state
§ new: The process is being created
§ running: Instructions are being executed
§ waiting: The process is waiting for some event to occur
§ ready: The process is waiting to be assigned to a processor
§ terminated: The process has finished execution

## Slide 6

Process State
§ As a process executes, it changes 
state
§ new: The process is being created
§ running: Instructions are being 
executed
§ waiting: The process is waiting for 
some event to occur
§ ready: The process is waiting to be assigned to a processor
§ terminated: The process has finished execution
§ Waiting swapped: The process 
was swapped while waiting for an 
I/O or an event.

## Slide 7

CPU Switch From Process to Process
Overhead!
Overhead!

## Slide 8

Process Control Block (PCB)
Information associated with each process (also called task 
control block)
§ Process state – running, waiting, etc
§ Process Identifier – Unique identifier of the process
§ Program counter – location of instruction to next execute
§ CPU registers – contents of all process-centric registers
§ CPU scheduling information- priorities, scheduling queue 
pointers
§ Memory-management information – memory allocated to 
the process
§ Accounting information – CPU used, clock time elapsed 
since start, time limits
§ I/O status information – I/O devices allocated to process, list 
of open files
§ Inter-process Communication – Communication structures 
between process (shared memory areas, message queues).

## Slide 9

Memory Structure of a Process
 Text section comprises the compiled program code (from nonvolatile storage) when launched [other sections (.init, .rodata)] 
 Stack containing temporary data such as function parameters, 
return addresses, local variables 
 Data section containing global and static variables, allocated 
and initialized prior to executing main 
 BSS (Block Stated by Symbol) is similar to Data section but 
have uninitialized global and static variables 
 Heap containing memory dynamically allocated during run time 
and is managed via calls such as malloc, free, etc 
 When processes are swapped out of memory and later 
restored, additional information must be stored and restored. 
 program counter and the value of all program registers. 
 Note that the stack and the heap start at opposite ends and 
grow towards each other. Should they ever meet: 
 stack overflow error will occur 
 a call to new or malloc will fail due to insufficient memory 
available

## Slide 10

Linux Processor Descriptor

## Slide 11

Fields in a process-descriptor (Linux)
https://github.com/torvalds/linux/blob/master/include/linux/sched.h

## Slide 12

Ready Queue And Various I/O Device Queues
 Maintains scheduling queues of 
processes
 Job Queue – Set of all the 
system tasks
 Ready Queue – Set of all 
processes residing in main 
memory, ready and waiting 
to execute 
 Device queues – Set of 
processes waiting for an I/O 
device
 Processes migrate among the 
various queues

## Slide 13

Process Scheduling
§ Maximize CPU use, quickly switch processes onto CPU for time sharing, to deliver
“acceptable” response times for all programs, particularly for real time execution.
§ Process scheduler selects among available processes for next execution on CPU. The
process scheduler must meet these objectives by implementing suitable policies for
swapping processes in and out of the CPU. Process scheduler selects among available
processes for next execution on CPU
§ Note that these objectives can be conflicting as every time the system steps in to swap
processes (context switch) it takes up CPU time, which is thereby “lost” from doing any
productive work.
0 100
50
60
90 150
160
190
210

## Slide 14

Schedulers
§ Long-term scheduler (or job scheduler) –
selects which processes should be brought into 
the ready queue
§ Short-term scheduler (or CPU scheduler) –
selects which process should be executed next 
and allocates CPU
§ Sometimes the only scheduler in a system
§ Short-term scheduler is invoked very frequently 
(milliseconds) Þ (must be fast)
§ Long-term scheduler is invoked very infrequently 
(seconds, minutes) Þ (may be slow)
§ The long-term scheduler controls the degree of 
multiprogramming
§ Long-term scheduler strives for good process 
mix
Processes can be described as either:
I/O-bound process – spends more time doing I/O than 
computations, many short CPU bursts
CPU-bound process – spends more time doing 
computations; few very long CPU bursts

## Slide 15

 Medium-term can be used when a system loads get high, the scheduler will swap one or more 
processes out of the ready queue system for a few seconds, in order to allow smaller faster jobs to 
finish up quickly and clear the system. 
 Remove process from memory, store on disk, bring back in from disk to continue execution: 
swapping
 An efficient scheduling system will select a good process mix of CPU-bound processes and I/O 
bound processes
Addition of Medium Term Scheduling

## Slide 16

CPU Switch From Process to Process
Overhead!
Overhead!

## Slide 17

§ UNIX examples
§ fork() system call creates new process
§ exec() system call used after a fork() to replace 
the processʼ memory space with a new program
§ wait() system call used after a fork() in the 
parent to sync with the created children.
§ exit() system call used by a process to notify the 
parent that has finalized.
§ getpid()/getppid() system call used by a 
process to obtain its pid and parent pid.
§ Abort() system call used by a parent to kill a child.
Process Creation

## Slide 18

Process Creation (Cont)
§ Parent process create children processes, 
which, in turn create other processes, forming 
a tree of processes
§ Generally, process identified and managed via 
a process identifier (pid)
§ Execution options
§ Parent and children execute concurrently
§ fork is not blocking, the parent continues 
the execution
§ Parent waits until children terminate. Child 
termination is registered with exit.
§ On typical Linux systems the process 
scheduler is termed sched and is given PID 0.
§ At system start up the scheduler launches 
init systemd, with PID 1.
§ systemd launches system daemons and 
logins and is the parent of all processes.

## Slide 19

Process Creation (Cont)
§ Resource sharing options
§ Parent and children share all resources
§ Children share subset of parentʼs resources
§ Parent and child share no resources
§ By default fork in Linux share all resources.
§ Address space (2 options)
§ Child duplicate of parent
§ Child has a program loaded into it
Parent Child

## Slide 20

C Program Forking Separate Process (Linux)
#include <sys/types.h> 
#include <stdio.h> 
#include <unistd.h> 
int main() 
{ 
 pid_t pid;
 /* fork a child process */ 
 pid = fork(); 
 if (pid < 0) { /* error occurred */
 fprintf(stderr, "Fork Failed"); 
 return 1; 
 }
 else if (pid == 0) { /* child process */ 
 printf(”I am the child %d",getpid()); 
 } 
 else { /* parent process */
 /* parent won’t wait for the child to complete */ 
 printf(”I am the parent with pid %, and my dear son has pid %”, \
 getpid(),pid);
 } 
 return 0; 
}

## Slide 21

C Program Forking Separate Process (Linux)
#include <sys/types.h> 
#include <stdio.h> 
#include <unistd.h> 
int main() 
{ 
 pid_t pid;
 /* fork a child process */ 
 pid = fork(); 
 if (pid < 0) { /* error occurred */
 fprintf(stderr, "Fork Failed"); 
 return 1; 
 }
 else if (pid == 0) { /* child process */ 
 printf(”I am the child %d",getpid()); 
 } 
 else { /* parent process */
 /* parent will wait for the child to complete */ 
 wait(NULL);
 printf(”I am the parent with pid %, and my dear son has pid %”, \
 getpid(),pid);
 } 
 return 0; 
}

## Slide 22

C Program Forking Separate Process (Linux)
#include <sys/types.h> 
#include <stdio.h> 
#include <unistd.h> 
int main() 
{ 
 pid_t pid1, pid2, pid3;
 pid1 = fork();
 pid2 = fork();
 pid3 = fork();
 
 printf("pid1: %i. pid2: %i. pid3: %i\n", pid1, pid2, pid3);
 return 0; 
}

## Slide 23

C Program Forking Separate Process (Linux)
#include <sys/types.h> 
#include <stdio.h> 
#include <unistd.h> 
int main() 
{ 
 pid_t pid;
 /* fork a child process */ 
 pid = fork(); 
 if (pid < 0) { /* error occurred */
 fprintf(stderr, "Fork Failed"); 
 return 1; 
 }
 else if (pid == 0) { /* child process */ 
 execlp("/bin/ls","ls",NULL); 
 } 
 else { /* parent process */
 /* parent will wait for the child to complete */ 
 wait(NULL);
 printf("Child Complete"); 
 } 
 return 0; 
}

## Slide 24

Process Termination
§ Process executes last statement and asks the operating system to delete it (exit())
§ Output data from child to parent (via wait())
§ Processʼ resources are deallocated by operating system
§ Parent may terminate execution of children processes (abort())
§ Child has exceeded allocated resources
§ Task assigned to child is no longer required
§ If parent is exiting
§ Some operating systems do not allow child to continue if its parent terminates
• All children terminated - cascading termination
§ If no parent waiting, then terminated process is a zombie
§ If parent terminated, processes are orphans

## Slide 25

Interprocess Communication (IPC)
§ Processes within a system may be independent or 
cooperating
§ Cooperating process can affect or be affected by other 
processes, including sharing data
 Reasons for cooperating processes:
 Information sharing
 Computation speedup
 Modularity
Shared Memory Message Passing

## Slide 26

Shared Memory System Calls
§ mmap(): maps a region of a file or device into memory. It can be used for memory-mapped file 
access or for creating a shared memory region. When used with the MAP_SHARED flag, it allows 
multiple processes to access the same physical memory.
§ shm_open() and shm_unlink():
§ shm_open() is used to create or open a POSIX shared memory object. It's similar to open(), 
but the file is created in a virtual filesystem, typically /dev/shm, and is used for shared 
memory.
§ shm_unlink() is used to delete a shared memory object.
§ ftruncate(): Although primarily a file operation, ftruncate() is often used in conjunction with 
shm_open() to set the size of the shared memory object.
§ munmap(): This system call is used to unmap a previously mapped memory region. It's essential 
for cleaning up and ensuring that resources are not leaked after the shared memory is no longer 
needed.

## Slide 27

Shared Memory System Calls

## Slide 28

Interprocess Communication – Message Passing
§ Mechanism for processes to communicate and to synchronize their actions
§ Message system – processes communicate with each other without resorting to shared variables
§ IPC facility provides two operations:
§ send(message) – message size fixed or variable 
§ receive(message)
§ If P and Q wish to communicate, they need to:
§ establish a communication link (channel) between them
§ exchange messages via send/receive
P0 Channel P1
ch.send ch.receive
 Channel Implementation:
 physical (e.g., shared memory, 
hardware bus)
 logical (e.g., direct or indirect, 
synchronous or asynchronous, 
automatic or explicit buffering)

## Slide 29

Interprocess Communication – Message Passing
P0 Channel P1
ch.send ch.receive
§ mq_open() Creates a message queue
§ mq_send() sends a message to the message queue.
§ mq_receive() receives a message from the message queue.
§ mq_close() closes a message queue descriptor.
§ mq_unlink() removes a message queue from the system

## Slide 30

Synchronization
§ Message passing may be either blocking or nonblocking
§ Non-blocking is considered asynchronous
§ Non-blocking send has the sender send the 
message and continue
§ Non-blocking receive has the receiver 
receive a valid message or null
P1
Send
Channel
Receive
Receive
P2
Communication 
Execution time

## Slide 31

Synchronization
§ Message passing may be either blocking or nonblocking
§ Blocking is considered synchronous 
(rendezvouz)
§ Blocking send has the sender blocked until 
the message is received
§ Blocking receive has the receiver blocked 
until a message is available
P1
Send
Channel
Receive
P2
Communication 
Execution time

## Slide 32

Buffering
§ Queue of messages attached to the link; implemented in one of three ways
1. Zero capacity – 0 messages
Sender and receiver wait for each other (rendezvous)
2.Bounded capacity – finite length of n messages
A. Not Loosing Messages: Sender and receiver must wait if buffer full when sending or empty 
when receiving.
B. Loosing Messages: Sender and receiver don’t wait, but messages can be lost
3. Unbounded capacity – infinite length 
Sender never waits

## Slide 33

Buffering (Zero Capacity)
§ Queue of messages attached to the link; implemented in one of three ways
Zero capacity – 0 messages
Sender and receiver wait for each other (rendezvous)
No buffer

## Slide 34

Buffering (Bounded Capacity)
§ Queue of messages attached to the link; implemented in one of three ways
Bounded capacity – finite length of n messages
A. Not Loosing Messages
B. Loosing Messages
Empty
Under any configuration, if the queue is empty, 
the receiver will wait until there is any element 
in the queue

## Slide 35

Buffering (Bounded Capacity)
§ Queue of messages attached to the link; implemented in one of three ways
Bounded capacity – finite length of n messages
A. Not Loosing Messages: Sender and receiver must wait if buffer full when sending 
or empty when receiving.
B. Loosing Messages
Full

## Slide 36

Buffering (Bounded Capacity)
§ Queue of messages attached to the link; implemented in one of three ways
Bounded capacity – finite length of n messages
A. Not Loosing Messages: Sender and receiver must wait if buffer full when sending or 
empty when receiving.
B. Loosing Messages: Sender and receiver don’t wait, but messages can be lost.
Full

## Slide 37

Buffering (Unbounded Capacity)
§ Queue of messages attached to the link; implemented in one of three ways
Unbounded capacity – infinite length 
Sender never waits
Never Full

## Slide 38

Producer-Consumer Problem
§ Paradigm for cooperating processes, producer process produces information that is 
consumed by a consumer process
§ unbounded-buffer places no practical limit on the size of the buffer
§ bounded-buffer assumes that there is a fixed buffer size

## Slide 39

Bounded-Buffer – Shared-Memory Solution
§ Solution is correct, but can only use BUFFER_SIZE-1 elements
#define BUFFER_SIZE 10
typedef struct {
. . .
} item;
Item 
buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
item next consumed; 
while (true) {
while (in == out) 
; /* do 
nothing */
next consumed = 
buffer[out]; 
out = (out + 1) % 
BUFFER_SIZE;
/* consume the item 
in next consumed */ 
} 
item next produced; 
while (true) { 
/* produce an item in 
next produced */ 
while (((in + 1) % 
BUFFER_SIZE) == out) 
; /* do nothing */ 
buffer[in] = next 
produced; 
in = (in + 1) % 
BUFFER_SIZE; 
} 
Why???

## Slide 40

Bounded-Buffer – Shared-Memory Solution
§ Solution is correct, but can only use BUFFER_SIZE-1 elements
#define BUFFER_SIZE 10
typedef struct {
. . .
} item;
Item 
buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
item next consumed; 
while (true) {
while (in == out) 
; /* do 
nothing */
next consumed = 
buffer[out]; 
out = (out + 1) % 
BUFFER_SIZE;
/* consume the item 
in next consumed */ 
} 
item next produced; 
while (true) { 
/* produce an item in 
next produced */ 
while (((in + 1) % 
BUFFER_SIZE) == out) 
; /* do nothing */ 
buffer[in] = next 
produced; 
in = (in + 1) % 
BUFFER_SIZE; 
} 
Why???

## Slide 41

Questions ?
david.miguel@singaporetech.edu.sg


---

# Chapter 4: Threads and Concurrency

## Slide 1

ICT1012
Operating Systems
4. Multithreaded 
Programming
Dr. David Sanan

## Slide 2

Chapter 4: Multithreaded Programming
§ Overview
§ Multicore Programming
§ Multithreading Models
§ Thread Libraries
§ Threading Issues
§ Operating System Examples

## Slide 3

Objectives
§ To introduce the notion of a thread—a fundamental unit of CPU 
utilization that forms the basis of multithreaded computer systems
§ To discuss the APIs for the Pthreads libraries
§ To examine issues related to multithreaded programming
§ To cover operating system support for threads in Linux

## Slide 4

Motivation
§ Most modern applications follow a 
multithreaded design
§ Threads run within application
§ Multiple tasks with the application can be 
implemented by separate threads
§ Update display
§ Fetch data
§ Spell checking
§ Answer a network request
§ Process creation is heavy-weight while thread 
creation is light-weight
§ Can simplify code, increase efficiency
§ Kernels are generally multithreaded
client
(1) request
(2) create new
thread to service
the request
(3) resume listening
for additional
client requests
server thread

## Slide 5

Single and Multithreaded Processes
registers
code data files
stack registers registers registers
code data files
stack stack stack
thread thread
single-threaded process multithreaded process

## Slide 6

Benefits
§ Economy 
§ Resource Sharing
§ Scalability/Responsivenes. 
registers
code data files
stack registers registers registers
code data files
stack stack stack
thread thread
single-threaded process multithreaded process

## Slide 7

Benefits
§ Economy – cheaper than process creation, thread switching lower 
overhead than context switching. In general, it is significantly more 
time consuming to create and manage processes than threads.
code data files code data files
Process creation

## Slide 8

Benefits
code data files
Thread creation
 Economy – cheaper than process creation, thread switching lower 
overhead than context switching. In general, it is significantly more time 
consuming to create and manage processes than threads.

## Slide 9

Benefits
§ Resource Sharing – threads share memory and the resources of the 
process to which they belong to, easier than shared memory or 
message passing. The benefit of sharing code and data is that it 
allows an application to have several different threads of activity 
within the same address space.
code data files code data files code data files
communication

## Slide 10

Benefits
§ Scalability – process can take advantage of multiprocessor architectures where threads could 
be running in parallel on different processing cores. A single-threaded process can run on only 
one processor.
§ Responsiveness – may allow continued execution if part of process is blocked, especially 
important for user interfaces. A single-threaded application would be unresponsive to the user until 
the operation had completed. However, if the time-consuming operation is performed in a 
separate thread, the application remains responsive to the user.
code data files

## Slide 11

 As # of threads grows, so does architectural support for threading
 CPUs have cores as well as hardware threads
 Consider Oracle SPARC T4 with 8 cores, and 8 hardware threads per 
core
 New intel and AMD CPUS 24 cores/ 32 threads.
Concurrency vs. Parallelism
 Concurrent execution on single-core system: more than one task making progress. 
Scheduler providing concurrency
 Parallelism on a multi-core system: a system can perform more than one task 
simultaneously
single core T1 T2 T3 T4 T1 T2 T3 T4 T1
time
…
core 1 T1 T3 T1 T3 T1
core 2 T2 T4 T2 T4 T2
time
…
…

## Slide 12

Multicore Programming
§ Multicore or multiprocessor systems putting pressure on 
programmers, challenges include:
§ Dividing activities : examining applications to find areas that 
can be divided into separate, concurrent tasks.
§ Balance : with tasks identified that can run in parallel, one still 
need to ensure that the tasks perform equal work of equal 
value. 
§ Data splitting : the data accessed and worked on by the tasks 
must be divided to run on separate cores.
§ Data dependency : programmers must ensure that the 
execution of the tasks is synchronized to accommodate the 
data dependency.
§ Testing and debugging : as many different execution paths 
are possible, testing and debugging such concurrent programs 
is inherently more difficult.

## Slide 13

Multicore Programming (Cont.)
Data parallelism – distributes subsets of the same data across multiple 
cores, same operation on each
To calculate
Each core k process
With n = elements in the data structure
 c = total number of cores ! k = core processing computation !"#
$
∗&
#
$
∗&'
#
$()
����[�]

## Slide 14

Multicore Programming (Cont.)
Task parallelism – distributing threads across cores, each thread 
performing unique operation
For Example: Core 0 process 
For Example: Core 1 process 
Core 2 process 
Core 3 process 
����(����)
�������(����)

## Slide 15

User Threads and Kernel Threads
§ User threads - management done by user-level threads library
§ Three primary thread libraries:
§ POSIX Pthreads
§ Win32 threads
§ Java threads
§ Kernel threads - Supported by the Kernel
§ Examples – virtually all general purpose operating systems, including:
§ Windows 
§ Solaris
§ Linux
§ Tru64 UNIX
§ Mac OS X

## Slide 16

Threads Models
One to many
user thread
k kernel thread
user thread
k k k k kernel thread
Many to many 2-Level Mode
One to One
user thread
k k k kernel thread
user thread
k k k k kernel thread

## Slide 17

Many-to-One
§ Many user-level threads mapped to single 
kernel thread
§ One thread blocking causes all to block
§ As only one thread can access the kernel 
at a time, multiple threads may not run in 
parallel on muticore system
§ Does not result in true concurrency as kernel 
can schedule only one thread at a time
§ Few systems currently use this model
§ Examples:
§ Solaris Green Threads
§ GNU Portable Threads
user thread
k kernel thread

## Slide 18

One-to-One
§ Each user-level thread maps to kernel thread
§ Creating a user-level thread creates a kernel thread
§ More concurrency than many-to-one. Also allows multiple threads to run in parallel
on multiprocessors
§ Number of threads per process sometimes restricted. Why ? Due to the overhead of 
creating kernel threads can burden the performance of an application 
§ Examples
§ Windows NT/XP/2000
§ Linux
§ Solaris 9 and later
user thread
k k k k kernel thread

## Slide 19

Many-to-Many Model
Allows many user level threads to be 
mapped to many kernel threads
Allows the operating system to 
create a sufficient number of kernel 
threads
When a thread performs a blocking 
system call, the kernel can schedule 
another thread for execution
Solaris prior to version 9
Windows NT/2000 with the 
ThreadFiber package
user thread
k k k kernel thread

## Slide 20

Two-level Model
§ Similar to M:M, except that it allows a user thread to be bound
to kernel thread
§ Examples
§ IRIX
§ HP-UX
§ Tru64 UNIX
§ Solaris 8 and earlier
user thread
k k k k kernel thread

## Slide 21

Thread Libraries
§ Thread library provides programmer with API for creating and managing 
threads
§ Two primary ways of implementing
§ Library entirely in user space with no kernel support. All code and data 
structures for the library exist in user space and invoking a function in the 
library results in a local function call in user space and not a system call. 
E.g., Posix Pthreads.
§ Kernel-level library supported by the OS. Code and data structures for 
the library exist in kernel space. Invoking a function in the API for the library 
typically results in a system call to the kernel. E.g., Windows Threads or 
Linux System V.

## Slide 22

Pthreads
§ May be provided either as user-level or kernel-level
§ A POSIX standard (IEEE 1003.1c) API for thread creation and 
synchronization
§ Specification, not implementation
§ API specifies behavior of the thread library, implementation is up to 
development of the library
§ Common in UNIX operating systems (Solaris, Linux, Mac OS X)

## Slide 23

Pthreads
§ pthread_create(): Creates a new thread
§ pthread_attr_init(): Initialize thread attributes like stack size, scheduling size and priority.
§ pthread_exit() Terminates the calling thread.
§ pthread_join(): Waits for a thread to finish. It is equivalent to wait in processes
§ pthread_detach() detaches a thread releasing the resources after termination. It used to manage 
resources.
§ pthread_cancel() Requests cancellation of a thread.

## Slide 24

Pthreads Example
#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h>
/* this data is shared 
 by the thread(s) */
int sum; 
/* threads call this function */
void *runner(void *param); 
int main(int argc, char *argv[]) {
 /* the thread identifier */ 
 pthread_t tid; 
 /* set of thread attributes */
 pthread_attr_t attr; 
 /* set the default attributes 
 of the thread */
 pthread_attr_init(&attr);
 /* create the thread */
 pthread_create(&tid, &attr, runner, argv[1]); 
 /* wait for the thread to exit */
 pthread_join(tid,NULL); 
 printf("sum = %d∖n",sum); 
} 
/* The thread will 
 execute in this function */ 
void *runner(void *param)
{ 
 int i, upper = atoi(param); 
 sum = 0; 
 for (i = 1; i <= upper; i++)
 sum += i; 
 pthread_exit(0); 
}

## Slide 25

Pthreads Code for Joining 10 Threads
#define NUM THREADS 10 
/* an array of threads to be joined upon */ 
pthread_t workers[NUM_THREADS]; 
for (int i = 0; i < NUM_THREADS; i++)
 pthread_join(workers[i], NULL);

## Slide 26

Threading Issues
§ Semantics of fork() and exec() system calls
§ Signal handling
§ Synchronous and asynchronous
§ Thread cancellation of target thread
§ Asynchronous or deferred
§ Thread-local storage
§ Thread Safety

## Slide 27

Semantics of fork() and exec()
 If one thread in a program calls fork(), does fork()duplicate only the calling thread or all 
threads?
 Some UNIXes have two versions of fork
 Exec() usually works as normal – replace the running process including all threads
 If exec() is called immediately after forking, then duplicating all threads is not productive as the 
program specified in the parameters to exec() will replace the process; duplicating only the calling 
thread is appropriate
 If the separate process does not call exec() after forking, the separate process should duplicate 
all threads

## Slide 28

Signal Handling
§ Signals are used in UNIX systems to notify a process that a particular event has occurred.
§ A signal handler is used to process signals
1. Signal is generated by particular event
2. Signal is delivered to a process
3. Signal is handled by one of two signal handlers:
1. default
2. user-defined
§ Every signal has default handler that kernel runs when handling signal
§ User-defined signal handler can override default
§ For single-threaded, signal delivered to process
§ Where should a signal be delivered for multi-threaded? 
§ Deliver the signal to the thread to which the signal applies
§ Deliver the signal to every thread in the process
§ Deliver the signal to certain threads in the process
§ Assign a specific thread to receive all signals for the process

## Slide 29

Signal Handling (Cont.)
§ The standard UNIX function for delivering a signal is 
kill (pid_t pid, int signal)
§ This function specifies the process (pid) to which a particular signal 
(signal) is to be delivered. Most multithreaded versions of UNIX allow a 
thread to specify which signals it will accept and which it will block. A 
signal is typically delivered only to the first thread found that is not 
blocking it.
§ POSIX Pthreads provides the following function, which allows a signal to be 
delivered to a specified thread (tid) 
pthread_kill(pthread_t tid, int signal)

## Slide 30

Thread Cancellation
§ Terminating a thread before it has finished
§ Thread to be canceled is target thread
§ Two general approaches:
§ Asynchronous cancellation terminates the target thread immediately
§ Deferred cancellation allows the target thread to periodically check if it 
should be cancelled
§ Pthread code to create and cancel a thread:

## Slide 31

Thread Cancellation (Cont.)
§ Invoking thread cancellation requests cancellation, but actual cancellation 
depends on thread state
§ If thread has cancellation disabled, cancellation remains pending until thread 
enables it
§ Default type is deferred
§ Cancellation only occurs when thread reaches cancellation point
§ I.e. pthread_testcancel()
§ Then cleanup handler is invoked
§ On Linux systems, thread cancellation is handled through signals

## Slide 32

Thread-Local Storage
§ Thread-local storage (TLS) allows each thread to have its own copy of data
§ Useful when you do not have control over the thread creation process (i.e., when 
using a thread pool)
§ Different from local variables
§ Local variables visible only during single function invocation
§ TLS visible across function invocations
§ Similar to static data
§ TLS is unique to each thread

## Slide 33

Thread Safety
§ Three Levels:
§ Thread Safe
§ Conditionally safe
§ Unsafe
§ Two approaches to avoid race conditions:
Avoid Share State
• Support for Re-Entrancy: Code that can be 
partially executed by threads simultaneously 
and correctly complete the original execution. 
Requires local variables to the thread or using 
atomic operations
• Thread-Local Storage
• Immutable objects.
Synchronization
• Mutual Exclusion: Access to shared variables is 
serialized so all the threads are reading from a 
shared resource; or only one thread writes on 
the shared resource, without any other thread 
accessing it for either reading or writing
• Atomic operations: updates to shared variables 
cannot be interrupted by other threads.

## Slide 34

Thread Safety
§ Three Levels:
§ Thread Safe
§ Conditionally safe
§ Unsafe

## Slide 35

Linux Threads
§ Linux refers to them as tasks rather than threads
§ Thread creation is done through clone() system call
§ clone() allows a child task to share the address space of the parent task 
(process)
§ Flags control behavior
§ struct task_struct points to process data structures (shared or unique)
flag meaning
CLONE_FS
CLONE_VM
CLONE_SIGHAND
CLONE_FILES
File-system information is shared.
The same memory space is shared.
Signal handlers are shared.
The set of open files is shared.

## Slide 36

Linux Threads
2 Processes, 1 Thread each process

## Slide 37

Linux Threads
1 Processes, 2 Threads
stack P1
P0

## Slide 38

Questions ?


---

# Chapter 5: CPU Scheduling

## Slide 1

ICT1012
Operating Systems
5. CPU Scheduling
Dr. David Sanan

## Slide 2

Chapter 5: CPU Scheduling
§ Basic Concepts
§ Scheduling Criteria 
§ Scheduling Algorithms
§ Multiple-Processor Scheduling
§ Thread Scheduling
§ Real-Time CPU Scheduling
§ Linux Example

## Slide 3

Scheduling
§ To introduce CPU scheduling, which is the basis for 
multi-programmed operating systems
§ To describe various CPU-scheduling algorithms
§ To examine the scheduling algorithms of Linux 
operating systems

## Slide 4

Basic Concepts
§ Maximum CPU utilization obtained with multiprogramming
§ CPU–I/O Burst Cycle – Process execution consists of a 
cycle of CPU execution and I/O wait
§ CPU burst followed by I/O burst
§ CPU burst distribution is of main concern
§ Characterised with a large number of short CPU bursts 
and a small number of long CPU bursts
§ I/O bound program typically has many short CPU 
bursts
§ CPU bound program might have a few long CPU 
bursts
CPU burst
load store
add store
read from file
store increment
index
write to file
load store
add store
read from file
wait for I/O
wait for I/O
wait for I/O
I/O burst
I/O burst
I/O burst
CPU burst
CPU burst
•
•
•
•
•
•

## Slide 5

Histogram of CPU-burst Times
CPU burst
load store
add store
read from file
store increment
index
write to file
load store
add store
read from file
wait for I/O
wait for I/O
wait for I/O
I/O burst
I/O burst
I/O burst
CPU burst
CPU burst
•
•
•
•
•
•
Processes can be described as:
 IO-Bound processes – spend more time doing I/O than 
computations, many short CPU bursts
 CPU-Bound Processes – spend more time doing 
computations; few very long CPU bursts.

## Slide 6

Scheduling
Long-Term scheduling 
• Determines which programs are 
admitted to the system for 
processing 
• When to create a new process 
• Controls the degree of 
multiprogramming 
• More processes, smaller % of 
time for each process 
• Invoke very infrequently
• Strive for good process mix

## Slide 7

Scheduling
Medium-Term scheduling 
• Part of the swapping 
function (make swapping 
decisions)
• Based on the need to 
manage the degree of 
multiprogramming (memory 
requirement)
• Remove processes from 
memory, store on disk, bring 
back in from disk to 
continue execution

## Slide 8

Scheduling
Short-Term scheduling 
• Is invoked very frequently 
(milliseconds) and must be 
very fast 
• Responsible for context 
switching
• Aims to maximise CPU 
utilisation and throughput 
• Load balancing for multicore architectures
• Adaptability

## Slide 9

CPU Scheduler
 Short-term scheduler selects from among the processes in ready queue, 
and allocates the CPU to one of them
 Queue may be ordered in various ways
 CPU scheduling decisions may take place when a process:
1. Switches from running to waiting state
2. Terminates
3. Switches from running to ready state
4. Switches from waiting to ready
 Scheduling under 1 and 2 is non-preemptive (or cooperative; once the 
CPU has been allocated to a progress, the process keeps the CPU until it 
releases the CPU either by terminating or by switching to the waiting state)
 Scheduling under 3 and 4 is preemptive
New Process must be 
selected (NonPreemptive)
New Process must be 
selected (Preemptive)

## Slide 10

Dispatcher
§ Dispatcher module gives control of the CPU to 
the process selected by the short-term 
scheduler; this involves:
§ switching context
§ switching to user mode
§ jumping to the proper location in the user 
program to restart that program
§ Dispatch latency – time it takes for the 
dispatcher to stop one process and start 
another running
§ Scheduler and Dispatcher are used in the 
process scheduling of an OS.
§ The Scheduler selects a process out of 
several processes to be executed
§ The dispatcher allocates the CPU for the 
selected process by the scheduler

## Slide 11

Scheduling Criteria
§ CPU utilization – keep the CPU as busy as possible
§ Throughput – # of processes that complete their execution per time unit
§ Turnaround time – amount of time to execute a particular process (i.e. time of submission
to the time of completion; sum of the periods spend waiting to get into memory, waiting in
the ready queue, executing on the CPU, and I/O; In an interactive system, turnaround time
may not be the best criterion; turnaround time is limited by the speed of the output device)
§ Waiting time – amount of time a process has been waiting in the ready queue (CPU
scheduling algorithm does not affect the amount of time during which a process executes or
does I/O)
§ Response time – amount of time it takes from when a request was submitted until the first
response is produced, not output (for time-sharing environment) (time from the submission
of a request until the first response is produced)

## Slide 12

Scheduling Criteria
§ CPU utilization – keep the CPU as busy as possible (maximize)
§ Throughput – # of processes that complete their execution per time unit (maximize)
§ Turnaround time – amount of time to execute a particular process (i.e. time of submission to the
time of completion; sum of the periods spend waiting to get into memory, waiting in the ready
queue, executing on the CPU, and I/O; In an interactive system, turnaround time may not be the
best criterion; turnaround time is limited by the speed of the output device) (Minimize)
§ Waiting time – amount of time a process has been waiting in the ready queue (CPU scheduling
algorithm does not affect the amount of time during which a process executes or does I/O)
(Minimize)
§ Response time – amount of time it takes from when a request was submitted until the first
response is produced, not output (for time-sharing environment) (time from the submission of a
request until the first response is produced) (Minimize)

## Slide 13

Scheduling Algorithms
§ First-Come, First-Served Scheduling (FCFS)
§ Simplest CPU-scheduling algorithm
§ The process that requests the CPU first is allocated the CPU first
§ The implementation is easily managed with a FIFO queue
§ When a process enters the ready queue, 
§ its PCB is linked onto the tail of the queue
§ When the CPU is free, 
§ it is allocated to the process at the head of the queue
§ the running process is then removed from the queue
§ Average waiting time under the FCFS policy is often quite long

## Slide 14

First-Come, First-Served (FCFS) Scheduling
Process Burst Time
P1 3
P2 3
P3 24
§ Suppose that the processes arrive in the order: P1 , P2 , P3 
The Gantt Chart for the schedule is:
§ Waiting time for P1 = 0; P2 = 3; P3 = 6
§ Average waiting time: (0 + 3 + 6)/3 = 3
P1 P2 P3
0 3 6 30

## Slide 15

FCFS Scheduling (Cont.)
Suppose that the processes arrive in the order:
P3 , P2 , P1
§ The Gantt chart for the schedule is:
§ Waiting time for P3 = 0; P2 = 24; P1 = 27
§ Average waiting time: (0 + 24 + 27)/3 = 17
§ Much worse than previous case
§ Convoy effect - short process behind long process
§ Consider one CPU-bound and many I/O-bound processes
P3 P2 P1
0 24 27 30

## Slide 16

Shortest-Job-First (SJF) Scheduling
§ Associate with each process the length of its next CPU burst
§ Use these lengths to schedule the process with the shortest time
§ Two schemes: 
§ nonpreemptive – once CPU given to the process it cannot be preempted until
completes its CPU burst
§ preemptive – if a new process arrives with CPU burst length less than
remaining time of current executing process, preempt. This scheme is know as
the Shortest-Remaining-Time-First (SRTF)
§ SJF is optimal – gives minimum average waiting time for a given set of 
processes
§ The difficulty is knowing the length of the next CPU request
§ Could ask the user

## Slide 17

Example of SJF (non-preemptive)
ProcessArriva l Time Burst Time
P1 0.0 6
P2 2.0 8
P3 4.0 7
P4 5.0 3
§ SJF scheduling chart
§ Average waiting time = (3 + 16 + 9 + 0) / 4 = 7
P4 P P3 1
0 3 9 16
P2
24

## Slide 18

Determining Length of Next CPU Burst
§ Can only estimate the length – should be similar to the previous one
§ Then pick process with shortest predicted next CPU burst
§ Can be done by using the length of previous CPU bursts, using 
exponential averaging:
1. �! = actual length of �"# CPU burst
2. �!$% = Predicted value for the next CPU burst
3. �, 0 ≤ � ≤ 1
4. Define �!$%= � ⋅ �! + 1 − � �!
§ Commonly, � set to 1/2

## Slide 19

Prediction of the Length of the Next CPU Burst
6 4 6 4 13 13 13 …
10 6 6 5 9 11 12 8 …
CPU burst (ti)
"guess" (τi
)
ti
τi
2
time
4
6
8
10
12

## Slide 20

Examples of Exponential Averaging
§ a =0
§ tn+1 = tn
§ Recent history does not count
§ a =1
§ tn+1 = a tn
§ Only the actual last CPU burst counts
§ If we expand the formula, we get:
tn+1 = a tn+(1 - a)a tn-1 + …
+(1 - a )j a tn -j + …
+(1 - a )n +1 t0
§ Since both a and (1 - a) are less than or equal to 1, each successive term has 
less weight than its predecessor

## Slide 21

Example of Shortest-remaining-time-first
§ Now we add the concepts of varying arrival times and preemption to the 
analysis
ProcessAarri Arrival TimeTBurst Time
P1 0 8
P2 1 4
P3 2 9
P4 3 5
§ Preemptive SJF Gantt Chart
§ Average waiting time = [(10-1)+(1-1)+(17-2)+5-3)]/4 = 26/4 = 6.5 msec
P1 P2 P1
0 1 10 17
P3
5 26
P4

## Slide 22

Priority Scheduling
§ A priority number (integer) is associated with each process
§ The CPU is allocated to the process with the highest priority (smallest integer º
highest priority)
§ Pre-emptive : will preempt the CPU if the priority of the newly arrived process is 
higher than the priority of the currently running process
§ Non-preemptive : will simply put the new process at the head of the ready queue
§ SJF is a special case of priority scheduling algorithm where priority is the inverse of 
predicted next CPU burst time
§ the larger the CPU burst, the lower the priority, and vice versa

## Slide 23

Example of Priority Scheduling
ProcessA arri Burst TimeT Priority
P1 10 3
P2 1 1
P3 2 4
P4 1 5
P5 5 2
§ Priority scheduling Gantt Chart
§ Average waiting time = 8.2 ms
P2 P5 P3
0 1 16 18
P4
6 19
P1

## Slide 24

Priority Scheduling -- Issues
P1
Priority 5
P2
Priority 4 
P3
Priority 1

## Slide 25

P1
Priority 5
Execution
Priority Scheduling -- Issues
P2
Priority 4 
P3
Priority 1

## Slide 26

Priority Scheduling -- Issues
P1
Priority 5
P2
Priority 4 
P3
Priority 1

## Slide 27

P1
Priority 5
Execution
Priority Scheduling -- Issues
P2
Priority 4 
P3
Priority 1

## Slide 28

Priority Scheduling -- Issues
P1
Priority 5
P2
Priority 4 
P3
Priority 1 
§ Problem º Starvation – low priority processes may never execute
§ indefinite blocking – can leave some low priority processes waiting indefinitely

## Slide 29

Priority Scheduling -- Issues
P1
Priority 5
P2
Priority 4 
P3
Priority 1 
§ Problem º Starvation – low priority processes may never execute
§ indefinite blocking – can leave some low priority processes waiting indefinitely
§ Solution º Aging – as time progresses, increase the priority of the process

## Slide 30

Priority Scheduling -- Issues
§ Problem º Starvation – low priority processes may never execute
§ indefinite blocking – can leave some low priority processes waiting indefinitely
§ Solution º Aging – as time progresses, increase the priority of the process
P1
Priority 5
Execution
P2
Priority 4 
P3
Priority 1

## Slide 31

Priority Scheduling -- Issues
P1
Priority 5
P2
Priority 4 
P3
Priority 2 
§ Problem º Starvation – low priority processes may never execute
§ indefinite blocking – can leave some low priority processes waiting indefinitely
§ Solution º Aging – as time progresses, increase the priority of the process

## Slide 32

Priority Scheduling -- Issues
§ Problem º Starvation – low priority processes may never execute
§ indefinite blocking – can leave some low priority processes waiting indefinitely
§ Solution º Aging – as time progresses, increase the priority of the process
P1
Priority 5
Execution
P2
Priority 4 
P3
Priority 2

## Slide 33

Priority Scheduling -- Issues
P1
Priority 5
P2
Priority 5 
P3
Priority 3 
§ Problem º Starvation – low priority processes may never execute
§ indefinite blocking – can leave some low priority processes waiting indefinitely
§ Solution º Aging – as time progresses, increase the priority of the process

## Slide 34

Round Robin (RR)
§ Each process gets a small unit of CPU time (time
quantum q), usually 10-100 milliseconds. After this
time has elapsed, the process is preempted and
added to the end of the ready queue.
§ Designed especially for time-sharing systems
§ If there are n processes in the ready queue and the
time quantum is q, then each process gets 1/n of the
CPU time in chunks of at most q time units at once. No
process waits more than (n-1)q time units.
§ Timer interrupts every quantum to schedule next
process
§ Performance
§ q large Þ FIFO
§ q small Þ q must be large with respect to context
switch, otherwise overhead is too high
P1 P2 P3 P1 P1 P1 P1 P1
0 ≤
q
≤
3*q
≤
4*q
≤
5 ∗
q
≤
6*q
≤
7*q
≤
8*q
≤
2*q

## Slide 35

Example of RR with Time Quantum = 4
Process Burst Time
P1 24
P2 3
P3 3
§ Typically, higher average turnaround than SJF, but better response
§ Average turnaround time for RR = (30 + 7 + 10)/3 = 15.6
§ Average turnaround time for SJF = (30+3+6) / 3 = 13.0
§ q should be large compared to context switch time
§ q usually 10ms to 100ms, context switch < 10 usec
P1 P2 P3 P1 P1 P1 P1 P1
0 4 7 10 14 18 22 26 30

## Slide 36

Time Quantum and Context Switch Time

## Slide 37

Turnaround Time Varies With 
The Time Quantum
80% of CPU bursts should be shorter than q

## Slide 38

Turnaround Time Varies With The Time Quantum
80% of CPU bursts should be shorter than q
How does the quantum affect the waiting time?

## Slide 39

Multilevel Queue
§ Ready queue is partitioned into separate queues, eg:
§ foreground (interactive)
§ background (batch)
§ Process permanently in a given queue
§ Each queue has its own scheduling algorithm:
§ foreground – RR
§ background – FCFS
§ Scheduling must be done between the queues:
§ Fixed priority scheduling; (i.e., serve all from 
foreground then from background). 
§ Possibility of starvation for background processes
§ Time slice – each queue gets a certain amount of 
CPU time which it can schedule amongst its 
processes; i.e., 
§ 80% to foreground in RR
§ 20% to background in FCFS

## Slide 40

Multilevel Feedback Queue
 A process can move between the various queues; 
aging can be implemented this way
 Multilevel-feedback-queue scheduler defined by the 
following parameters:
 number of queues
 scheduling algorithms for each queue
 method used to determine when to upgrade a 
process
 method used to determine when to demote a 
process
 method used to determine which queue a 
process will enter when that process needs 
service

## Slide 41

Example of Multilevel Feedback Queue
§ Three queues: 
§ Q0 – RR with time quantum 8 milliseconds
§ Q1 – RR time quantum 16 milliseconds
§ Q2 – FCFS
§ Scheduling
§ A new job enters queue Q0 which is served RR
§ When it gains CPU, job receives 8 milliseconds
§ If it does not finish in 8 milliseconds, job is moved 
to queue Q1
§ At Q1 job is again served RR and receives 16 
additional milliseconds
§ If it still does not complete, it is preempted and 
moved to queue Q2
§ If a FCFS job gains the CPU, it will be pre-empted if a 
job in either Q0 or Q1 becomes ready

## Slide 42

Scheduling Policies and Starvation
Selection 
Function
Decision 
Mode
Throughput Response 
time
Overhead Effect on Processes Starvation
FCFS Max[w] NonPreemptiveNot 
emphasized
May be high Minimum Bad for short 
processes and I/O 
Bound processes
No
Round Robin constant Preemptive 
at time 
quantum
May be low 
for small 
quantum
Good 
response time
Minimum Fair Treatment No
SJF Min[s] NonPreemptiveHigh Good for short 
processes
Can be 
high
Penalizes long 
processes
Possible
SRT Min[s-e] Preemptive 
at arrival
High Good for short 
processes
Can be 
high
Penalizes long 
processes
Possible
Priority Priority Preemptive 
at arrival if 
preemptive
Not 
Emphasized
Good for high 
priority 
processes
Can be 
high
Penalizes low 
priority processes
Possible
Multilevel Priority and 
secondary 
policy
Preemptive –
at arrival and 
time 
quantum
Not 
Emphasized
Good for high 
priority 
processes
Can be 
high
Penalizes low 
priority processes
Possible
Multilevel 
Feedback
Priority and 
secondary 
policy
and aging
Preemptive –
at arrival and 
time 
quantum
Not 
Emphasized
Good for high 
priority 
processes
Can be 
high
Penalizes low 
priority processes
Possible

## Slide 43

Real-Time CPU Scheduling
§ Can present obvious challenges
§ Soft real-time systems – no 
guarantee as to when critical realtime process will be scheduled
§ Hard real-time systems – task 
must be serviced by its deadline
§ Two types of latencies affect 
performance
1.Interrupt latency – time from 
arrival of interrupt to start of 
routine that services interrupt
2.Dispatch latency – time for 
schedule to take current 
process off CPU and switch to 
another

## Slide 44

Real-Time CPU Scheduling (Cont.)
§ Conflict phase of 
dispatch latency:
1.Preemption of any 
process running in 
kernel mode
2. Release by lowpriority process of 
resources needed 
by high-priority 
processes
response to event
real-time 
process 
execution
event
conflicts
time
dispatch 
response interval
dispatch latency
process made 
interrupt available
processing

## Slide 45

Priority-based Scheduling
§ For real-time scheduling, scheduler must support preemptive, prioritybased scheduling
§ But only guarantees soft real-time
§ For hard real-time must also provide ability to meet deadlines
§ Processes have new characteristics: periodic ones require CPU at 
constant intervals
§ Has processing time t, deadline d, period p
§ 0 ≤ t ≤ d ≤ p
§ Rate of periodic task is 1/p

## Slide 46

Rate Montonic Scheduling
§ A priority is assigned based on the inverse of its period
§ Shorter periods = higher priority;
§ Longer periods = lower priority
§ CPU utilization: t!/�"
P1 Period 50
P1 Burst 20
CPU 1 20/50
P2 Period 100
P2 Burst 35
CPU 2 35/80
P1 is assigned a higher priority than P2.
Total CPU = 20/50 + 35/100 = 0.4 + 0.35 = 0.75

## Slide 47

Rate Montonic Scheduling
§ It is an optimal algorithm: if a set of processes cannot be scheduled 
by this algorithm, no other algorithm assigning static priorities can do 
it.
§ Limitation: CPU utilization is bounded by the following:
§ �(2
!
" − 1)
§ When the number of processes is very large, worst case utilization rate 
goes to a 69%
§ For 1 process CPU Utilization = 1
§ For 2 Processes CPU Utilization = 0.82

## Slide 48

Missed Deadlines with 
Rate Monotonic Scheduling
P1 Period 50
P1 Burst 25
CPU 1 25/50
P2 Period 80
P2 Burst 35
CPU 2 35/80 Total CPU = 25/50 + 35/80 = 0.5 + 0.43 = 0.93

## Slide 49

Linux Scheduling
§ Two algorithms: time-sharing and real-time
§ Time-sharing
§ Prioritized credit-based – process with most credits is 
scheduled next
§ Credit subtracted when timer interrupt occurs
§ When credit = 0, another process chosen
§ When all processes have credit = 0, recrediting occurs
§ Based on factors including priority and history
§ Real-time
§ Soft real-time
§ Posix.1b compliant – two classes
§ FCFS and RR
§ Highest priority process always runs first

## Slide 50

Linux Scheduling in Version 2.6.23 +
§ Completely Fair Scheduler (CFS)
§ Scheduling classes
§ Each has specific priority
§ Scheduler picks highest priority task in highest scheduling class
§ Rather than quantum based on fixed time allotments, based on proportion of CPU time
§ 2 scheduling classes included, others can be added
1. default
2. real-time
§ Quantum calculated based on nice value from -20 to +19
§ Lower value is higher priority
§ Calculates target latency – interval of time during which task should run at least once
§ Target latency can increase if say number of active tasks increases
§ CFS scheduler maintains per task virtual run time in variable vruntime
§ Associated with decay factor based on priority of task – lower priority is higher decay rate
§ Normal default priority yields virtual run time = actual run time. E.g. a task with default priority 
runs for 200ms, its vruntime is 200ms, a task with lower priority run will have vruntime higher than 200ms, a task with higher priority will have vruntime less than 200ms
§ To decide next task to run, scheduler picks task with lowest virtual run time

## Slide 51

Linux Scheduling (Cont.)
§ Real-time scheduling according to POSIX.1b
§ Real-time tasks have static priorities
§ Real-time plus normal map into global priority scheme
§ Nice value of -20 maps to global priority 100
§ Nice value of +19 maps to priority 139

## Slide 52

Questions ?

## Slide 53

Turnaround Time Varies With 
The Time Quantum
P1 P2 P3 P4 P1 P2 P4 P1 P2 P4 P1 P4 P1 P4 P1 P4 P4
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
P1 P2 P3 P4 P1 P2 P4 P1 P4 P4
0 2 4 5 7 9 10 12 14 16 17
P1 P2 P3 P4 P1 P4 P4
0 3 6 7 10 13 16 17

## Slide 54

Turnaround Time Varies With 
The Time Quantum
P1 P2 P3 P4 P1 P4
0 4 7 8 12 14 17
P1 P2 P3 P4 P1 P4
0 5 8 9 14 15 17
P1 P2 P3 P4 P4
0 6 9 10 16 17

## Slide 55

Turnaround Time Varies With 
The Time Quantum
P4 P1 P2 P3 P4 P1 P2 P4 P1 P2 P4 P1 P4 P1 P4 P1 P4
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
P4 P1 P2 P3 P4 P1 P2 P4 P1 P4
0 2 4 6 7 9 11 12 14 16 17
P4 P1 P2 P3 P4 P1 P4
0 3 6 9 10 13 16 17
P4: 7 ms P1: 6 ms P2: 3 ms P3: 1 ms

## Slide 56

Turnaround Time Varies With 
The Time Quantum
P4 P1 P2 P3 P4 P1
0 4 8 11 12 15 17
P4 P1 P2 P3 P4 P1
0 5 10 13 14 16 17
P4 P1 P2 P3 P4
0 6 12 15 16 17
P4 P1 P2 P3
0 7 13 16 17


---

# Chapter 6: Synchronization

## Slide 1

ICT1012
Operating Systems
5. Process Synchronization
Dr. David Sanan

## Slide 2

Chapter 5: Synchronisation
§ Background
§ The Critical-Section Problem
§ Synchronization Hardware
§ Mutex Locks
§ Semaphores
§ Classic Problems of Synchronization
§ Synchronization Examples

## Slide 3

Objectives
§ To introduce the critical-section problem, whose solutions can be used to 
ensure the consistency of shared data
§ To present both software and hardware solutions of the critical-section 
problem
§ To explore several tools that are used to solve process synchronization 
problems
§ To examine several classical process-synchronization problems

## Slide 4

Background
§ Processes and thread can execute concurrently
§ May be interrupted at any time, partially completing execution
§ Concurrent access to shared data may result in data inconsistency
§ Maintaining data consistency requires mechanisms to ensure the orderly 
execution of cooperating processes

## Slide 5

Illustration Producer-Consumer Problem
while (true) {
 /* produce an item in next produced */ 
 while (counter == BUFFER_SIZE); /* do 
nothing */ 
 buffer[in] = next produced; 
 in = (in + 1) % BUFFER_SIZE; 
 counter++; 
} 
while (true) {
 while (counter == 0); /* do nothing */ 
 next_consumed = buffer[out]; 
 out = (out + 1) % BUFFER_SIZE;
 counter--; 
 /* consume the item in next consumed */ 
} 
Producer Consumer
Suppose that we wanted to provide a solution to the consumer-producer problem that fills all the buffers. We 
can do so by having an integer counter that keeps track of the number of full buffers. Initially, counter is set 
to 0. It is incremented by the producer after it produces a new buffer and is decremented by the consumer after 
it consumes a buffer.

## Slide 6

Illustration Producer-Consumer Problem
while (true) {
 /* produce an item in next produced */ 
 while (counter == BUFFER_SIZE); /* do 
nothing */ 
 buffer[in] = next produced; 
 in = (in + 1) % BUFFER_SIZE; 
 counter++; 
} 
while (true) {
 while (counter == 0); /* do nothing */ 
 next_consumed = buffer[out]; 
 out = (out + 1) % BUFFER_SIZE;
 counter--; 
 /* consume the item in next consumed */ 
} 
Producer Consumer
Suppose that we wanted to provide a solution to the consumer-producer problem that fills all the buffers. We 
can do so by having an integer counter that keeps track of the number of full buffers. Initially, counter is set 
to 0. It is incremented by the producer after it produces a new buffer and is decremented by the consumer after 
it consumes a buffer.
https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
What can go wrong with the code?

## Slide 7

Race Condition
§ counter++ could be implemented as
 register1 = counter
 register1 = register1 + 1
 counter = register1
§ counter-- could be implemented as
 register2 = counter
 register2 = register2 - 1
 counter = register2
§ Consider this execution interleaving with “count = 5” initially:
S0: producer execute register1 = counter {register1 = 5}
S1: producer execute register1 = register1 + 1 {register1 = 6} 
S2: consumer execute register2 = counter {register2 = 5} 
S3: consumer execute register2 = register2 – 1 {register2 = 4} 
S4: producer execute counter = register1 {counter = 6 } 
S5: consumer execute counter = register2 {counter = 4}

## Slide 8

Race Condition
while (true) {
 /* produce an item in next produced */ 
 while (counter == BUFFER_SIZE); /* do 
nothing */ 
 buffer[in] = next produced; 
 in = (in + 1) % BUFFER_SIZE; 
 counter++; 
} 
while (true) {
 while (counter == 0); /* do nothing */ 
 next_consumed = buffer[out]; 
 out = (out + 1) % BUFFER_SIZE;
 counter--; 
 /* consume the item in next consumed */ 
} 
Producer Consumer
Protects well the access to the buffer in the case of one 
producer and one consumer (what happens if there are more 
than one producer or consumer?)
Modification of counter variable is not protected

## Slide 9

Critical Section Problem
§ Consider system of n processes {p0, p1, … pn-1}
§ Each process has critical section segments of code
§ Process may be changing common variables, updating table, writing file, 
etc
§ When one process in critical section, no other may be in its critical section 
to ensure data consistency and integrity
§ Critical section problem consists on designing a protocol to solve the above
§ Each process must ask permission to enter critical section in entry section, 
may follow critical section with exit section, then remainder section

## Slide 10

Critical Section
§ General structure of process pi is as below:
§ Each process must ask permission to enter critical section in entry 
section, may follow critical section with exit section, then remainder 
section

## Slide 11

Solution to Critical-Section Problem
1. Mutual Exclusion - If process Pi is executing
in its critical section with respect to a particular
resource, then no other processes can be
executing in their critical sections.
Can be optimized by differentiating between
writers and readers over a share variable v:
Only one process Pi is executing in its critical
section writing on a shared variable v, then no other
processes can be executing in their critical sections.
n processes P0 … Pn are executing in its critical
section as far as none of them is writing over the
shared variable v.

## Slide 12

Solution to Critical-Section Problem
2. Progress - If no process is executing
in its critical section and there exist
some processes that wish to enter
their critical section, then the
selection of the processes that will
enter the critical section next cannot
be postponed indefinitely

## Slide 13

Solution to Critical-Section Problem
3. Bounded Waiting - A bound must exist on the number of 
times that other processes are allowed to enter their critical 
sections after a process has made a request to enter its 
critical section and before that request is granted
 Assume that each process executes at a nonzero 
speed 
 No assumption concerning relative speed of the n
processes

## Slide 14

1
Solution to Critical-Section Problem
3. Bounded Waiting - A bound must exist on the number of 
times that other processes are allowed to enter their critical 
sections after a process has made a request to enter its 
critical section and before that request is granted
 Assume that each process executes at a nonzero 
speed 
 No assumption concerning relative speed of the n
processes

## Slide 15

2
Solution to Critical-Section Problem
3. Bounded Waiting - A bound must exist on the number of 
times that other processes are allowed to enter their critical 
sections after a process has made a request to enter its 
critical section and before that request is granted
 Assume that each process executes at a nonzero 
speed 
 No assumption concerning relative speed of the n
processes

## Slide 16

N
Solution to Critical-Section Problem
3. Bounded Waiting - A bound must exist on the number of 
times that other processes are allowed to enter their critical 
sections after a process has made a request to enter its 
critical section and before that request is granted
 Assume that each process executes at a nonzero 
speed 
 No assumption concerning relative speed of the n
processes

## Slide 17

N+1
Solution to Critical-Section Problem
3. Bounded Waiting - A bound must exist on the number of 
times that other processes are allowed to enter their critical 
sections after a process has made a request to enter its 
critical section and before that request is granted
 Assume that each process executes at a nonzero 
speed 
 No assumption concerning relative speed of the n
processes

## Slide 18

Solution to Critical-Section Problem
§ Two approaches depending on if kernel is preemptive or non-preemptive 
§ Preemptive – allows preemption of process when running in kernel mode. 
§ Needs synchronization mechanisms to control mutual exclusion.
§ Non-preemptive – runs until exits kernel mode, blocks, or voluntarily yields CPU
§ Essentially free of race conditions in kernel mode but can have problems with progress and 
bounded waiting.

## Slide 19

Synchronization Hardware
§ Many systems provide hardware support for critical section code
§ All solutions below based on idea of locking
§ Protecting critical regions via locks
§ Uniprocessors – could disable interrupts
§ Currently running code would execute without preemption
§ Generally too inefficient on multiprocessor systems
§ Operating systems using this not broadly scalable
§ Modern machines provide special atomic hardware instructions
§ Atomic = non-interruptible
§ Either test memory word and set value in one atomic operation test_and_set
§ Or swap contents of two memory words in one atomic operation compare_and_swap
do { 
acquire lock 
critical section 
release lock 
remainder section 
} while (TRUE);

## Slide 20

test_and_set Instruction 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
do {
 while (test_and_set(&lock)); 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
If target == 0 (false) executing test_and_set sets target to 1 (true) and the function returns 0
If target == 1 (True) executing test_and_set sets target to 1 (true) and the function returns 1
The test-and-set instruction atomically:
1. Reads the value of a control variable (e.g., lock).
2. Sets it to True.
3. Returns the old value.

## Slide 21

test_and_set Instruction 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 22

test_and_set Instruction (when lock is false) 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is false
0. target == false
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 23

test_and_set Instruction (when lock is false) 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is false
1. Keeps in local value rv the value of target
before invoking the function (rv == false)
1. rv == false
0. target == false
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 24

test_and_set Instruction (when lock is false) 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is false
1. Keeps in local value rv the value of target
before invoking the function (rv == false)
2. Update the value of target to true
1. rv == false
0. target == false
2. target == true
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 25

test_and_set Instruction (when lock is false) 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
1. rv == false
0. target == false
2. target == true
3. Return false
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
0. Assume value of target is false
1. Keeps in local value rv the value of target
before invoking the function (rv == false)
2. Update the value of target to true
3. Returns rv that is equal to false

## Slide 26

test_and_set Instruction (when lock is false) 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
1. rv == false
0. target == false
2. target == true
3. Return false
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
4. Test_and_set returns false exiting the 
loop and progressing into the critical 
section.
0. Assume value of target is false
1. Keeps in local value rv the value of target
before invoking the function (rv == false)
2. Update the value of target to true
3. Returns rv that is equal to false

## Slide 27

test_and_set Instruction (when lock is true) 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is true
0. target == true
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 28

test_and_set Instruction 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is true
1. Keeps in local value rv the value of target
before invoking the function (rv == true)
1. rv == true
0. target == true
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 29

test_and_set Instruction 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is true
1. Keeps in local value rv the value of target
before invoking the function (rv == true)
2. Update the value of target to true (target 
does not change)
1. rv == true
0. target == true
2. target == true
do {
 while (test_and_set(&lock)) 
 ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 30

test_and_set Instruction 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is true
1. Keeps in local value rv the value of target
before invoking the function (rv == true)
2. Update the value of target to true
3. Return rv (which by 1 it is true)
1. rv == true
0. target == true
2. target == true
3. Return True
do {
 while (test_and_set(&lock)); 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true);

## Slide 31

test_and_set Instruction 
§ Definition:
boolean test_and_set (boolean *target) {
 boolean rv = *target;
 *target = true;
 return rv:
}
Atomically updates target value and returning 
its value before the execution of the function. It 
is used to check the value of a Boolean variable, 
while updating it to a new value
0. Assume value of target is true
1. Keeps in local value rv the value of target
before invoking the function (rv == true)
2. Update the value of target to true
3. Return rv (which by 1 it is true)
1. rv == true
0. target == true
2. target == true
3. Return true
do {
 while (test_and_set(&lock));
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
4. test_and_set returns true, so it doesn’t 
progress to the critical section

## Slide 32

Solution using test_and_set()
§ Shared boolean variable lock, initialized to false. We can go into the critical section when lock == 
false. We need to change it to true, to prevent other processes/threads to access the critical 
section.
§ Solution:
do {
while (test_and_set(&lock)) ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
 
test_and_set(&lock) == false
The lock was False (no one had the lock) before 
TESTING test_and_set(&lock)
And we SET it to true (we get the lock)
boolean test_and_set (boolean *target){ boolean rv = *target;
 *target = TRUE; return rv:
}
1
1
2
We set the lock to false (other 
processes can enter in the critical 
section)
2

## Slide 33

Solution using test_and_set()
§ Shared boolean variable lock, initialized to false. We can go into the critical section when lock == 
false. We need to change it to true, to prevent other processes/threads to access the critical 
section.
§ Solution:
do {
while (test_and_set(&lock)) ; /* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
 
test_and_set(&lock) == false
The lock was False (no one had the lock) before 
TESTING test_and_set(&lock)
And we SET it to true (we get the lock)
boolean test_and_set (boolean *target){ boolean rv = *target;
 *target = TRUE; return rv:
}
1
1
2
We set the lock to false (other 
processes can enter in the critical 
section)
2
https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
Assume lock is initialized to True. What would happen 
in this case?

## Slide 34

Solution using test_and_set()
 
do {
while (test_and_set(&lock)) ; 
/* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
do {
while (test_and_set(&lock)) ; 
/* do nothing */ 
 /* critical section */ 
 lock = false; 
 /* remainder section */ 
} while (true); 
Assume lock is initialized to True. What would happen in this case?
P1 P2
P1 and P2 go into the loop with lock == True. test_and_set returns the initial value of lock and sets it to true.
P1 and P2 will be stuck in the loop forever (deadlock)
If target == 1 (True) executing test_and_set sets target to 1 (true) and the function returns 1

## Slide 35

compare_and_swap Instruction
§ Definition:
int compare and swap(int *value, int expected, int new value) { 
 int temp = *value; 
 if (*value == expected) 
 *value = new_value; 
 return temp; 
} 
1. We copy the current value of the lock
2. We check that the current value is what we 
expect it to be (we check that it is the value 
indicating no one has the lock)
3. We set the value of the control to a value 
indicating that we have the lock
4. We return the current value of the control
compare_and_swap is more efficient than test_and_set.
It allows the implementation of non-binary semaphores without blocking

## Slide 36

compare_and_swap Instruction
§ Definition:
int compare and swap(int *value, int expected, int new value) { 
 int temp = *value; 
 if (*value == expected) 
 *value = new_value; 
 return temp; 
} 
1. We copy the current value of the lock
2. We check that the current value is what we 
expect it to be (we check that it is the value 
indicating no one has the lock)
3. We set the value of the control to a value 
indicating that we have the lock
4. We return the current value of the control
compare_and_swap is more efficient than test_and_set.
It allows the implementation of non-binary semaphores without blocking
https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
Why is test_and_set inefficient?

## Slide 37

compare_and_swap Instruction
§ Definition:
int compare and swap(int *value, int expected, int new value) { 
 int temp = *value; 
 if (*value == expected) 
 *value = new_value; 
 return temp; 
} 
1. We copy the current value of the lock
2. We check that the current value is what we 
expect it to be (we check that it is the value 
indicating no one has the lock)
3. We set the value of the control to a value 
indicating that we have the lock
4. We return the current value of the control
compare_and_swap is more efficient than test_and_set.
It allows the implementation of non-binary semaphores without blocking
https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
Why is test_and_set inefficient?
Always writes in memory causing cache 
invalidation and other problems.

## Slide 38

Solution using compare_and_swap
§ Shared Boolean variable lock initialized to false (0); Each process has a local Boolean 
variable key.
§ Solution:
do {
 while (compare and swap(&lock, 0, 1) != 0); /* do nothing */ 
 /* critical section */ 
 lock = 0; 
 /* remainder section */ 
} while (true); 
 
compare_and_swap is more efficient than test_and_set.
It allows the implementation of non-binary semaphores without blocking

## Slide 39

Mutex Locks
§ Previous solutions are complicated and generally inaccessible to application programmers
§ OS designers build software tools to solve critical section problem
§ Simplest is mutex lock
§ Protect critical regions with it by first acquire() a lock then release() it
§ Boolean variable indicating if lock is available or not
§ Calls to acquire() and release() must be atomic
§ Usually implemented via hardware atomic instructions
§ But this solution requires busy waiting
 This lock therefore called a spinlock
 Can use sleep to avoid the spinlock (slower)

## Slide 40

Mutex Locks
§ Previous solutions are complicated and generally inaccessible to application programmers
§ OS designers build software tools to solve critical section problem
§ Simplest is mutex lock
§ Protect critical regions with it by first acquire() a lock then release() it
§ Boolean variable indicating if lock is available or not
§ Calls to acquire() and release() must be atomic
§ Usually implemented via hardware atomic instructions
§ But this solution requires busy waiting
 This lock therefore called a spinlock
 Can use sleep to avoid the spinlock (slower)
do {
 acquire(&lock);
 /* critical section */ 
 release(&lock); 
 /* remainder section */ 
} while (true); 
How to use it

## Slide 41

Mutex Locks
§ Previous solutions are complicated and generally inaccessible to application programmers
§ OS designers build software tools to solve critical section problem
§ Simplest is mutex lock
§ Protect critical regions with it by first acquire() a lock then release() it
§ Boolean variable indicating if lock is available or not
§ Calls to acquire() and release() must be atomic
§ Usually implemented via hardware atomic instructions
§ But this solution requires busy waiting
 This lock therefore called a spinlock
 Can use sleep to avoid the spinlock (slower)
void acquire(int *lock){
 while(test_and_set(lock)); 
}
void release(int *lock){
 *lock = false;
}
Implementation

## Slide 42

Mutex Locks
§ Previous solutions are complicated and generally inaccessible to application programmers
§ OS designers build software tools to solve critical section problem
§ Simplest is mutex lock
§ Protect critical regions with it by first acquire() a lock then release() it
§ Boolean variable indicating if lock is available or not
§ Calls to acquire() and release() must be atomic
§ Usually implemented via hardware atomic instructions
§ But this solution requires busy waiting
 This lock therefore called a spinlock
 Can use sleep to avoid the spinlock (slower)
void acquire(int *lock){
 while(test_and_set(lock)); 
}
void release(int *lock){
 *lock = false;
}
Implementation
https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
How would you use sleep to avoid spinlock?

## Slide 43

Mutex Locks
§ Previous solutions are complicated and generally inaccessible to application programmers
§ OS designers build software tools to solve critical section problem
§ Simplest is mutex lock
§ Protect critical regions with it by first acquire() a lock then release() it
§ Boolean variable indicating if lock is available or not
§ Calls to acquire() and release() must be atomic
§ Usually implemented via hardware atomic instructions
§ But this solution requires busy waiting
 This lock therefore called a spinlock
 Can use sleep to avoid the spinlock (slower)
void acquire(int *lock){
 while(test_and_set(lock)); 
}
void release(int *lock){
 *lock = false;
}
Implementation
https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
How would you use sleep to avoid spinlock?
void acquire(int *lock){
 while(test_and_set(lock)){
 sleep(1);
 } 
}

## Slide 44

Semaphore
§ Synchronization tool that does not require busy waiting 
§ Semaphore S – integer variable. It representing how many threads/processes can 
access the shared resource. 
§ Two standard operations modify S: wait() and signal()
§ Originally called P() and V()
§ Less complicated than using TestAndSet and Swap
§ Can only be accessed via two indivisible (atomic) operations
wait (S) { 
 while (S == 0); // busy wait.
 S--;
}
signal (S) { 
 S++;
}
In practice the process goes to sleep/is blocked not 
having to do busy waiting

## Slide 45

Semaphore Usage
Critical Section
§ Binary semaphore – integer value can range only between 0 and 1
§ Then a mutex lock (without spinlock)
§ Counting semaphore – integer value can range over an unrestricted domain
Synchronisation. Consider P1 and P2 that require S1 to happen 
before S2
P1:
 S1;
 signal(synch);
P2:
 wait(synch);
 S2;

## Slide 46

Semaphore Usage
Critical Section
§ Binary semaphore – integer value can range only between 0 and 1
§ Then a mutex lock (without spinlock)
§ Counting semaphore – integer value can range over an unrestricted domain
Synchronisation. Consider P1 and P2 that require S1 to happen 
before S2
P1:
 S1;
 signal(synch);
P2:
 wait(synch);
 S2;
https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
How do you initialize the semaphore to enable synchronization?

## Slide 47

Semaphore Usage
Critical Section
§ Binary semaphore – integer value can range only between 0 and 1
§ Then a mutex lock (without spinlock)
§ Counting semaphore – integer value can range over an unrestricted domain
Synchronisation. Consider P1 and P2 that require S1 to happen 
before S2
P1:
 S1;
 signal(synch);
P2:
 wait(synch);
 S2; https://app.sli.do/event/wbtQdNqMpoQXxsRnyBcnjx
How do you initialize the semaphore to enable synchronization?
P1:
 S1;
 signal(synch);
P2:
 wait(synch);
 S2;
synch = 0

## Slide 48

Semaphore Implementation with no Busy waiting 
§ With each semaphore there is an associated waiting queue
§ The block operation places a process into a waiting queue associated 
with the semaphore, and the state is switched to the waiting state
§ A process that is blocked (waiting on Semaphore S) will restart when 
some other process executes a signal() operation
§ Each entry in a waiting queue has two data items:
§ value (of type integer) / process control block for the waiting process
§ pointer to next record in the list
§ Two operations:
§ block – place the process invoking the operation on the appropriate 
waiting queue
§ wakeup – remove one of processes in the waiting queue and place it in 
the ready queue

## Slide 49

Problems with Semaphores
§ Incorrect use of semaphore operations:
§ signal (mutex) …. wait (mutex) 
§ wait (mutex) … wait (mutex)
§ Omitting of wait (mutex) or signal (mutex) (or both)
§ Deadlock and starvation

## Slide 50

Problems with Semaphores
§ Incorrect use of semaphore operations:
§ signal (mutex) …. wait (mutex) 
§ wait (mutex) … wait (mutex)
§ Omitting of wait (mutex) or signal (mutex) (or both)
§ Deadlock and starvation
Signal to enter in the critical section!! 
Everybody can come in!!

## Slide 51

Problems with Semaphores
§ Incorrect use of semaphore operations:
§ signal (mutex) …. wait (mutex) 
§ wait (mutex) … wait (mutex)
§ Omitting of wait (mutex) or signal (mutex) (or both)
§ Deadlock and starvation
Signal to enter in the critical section!! 
Everybody can come in!!
Wait instead of signal when exiting the critical section!
Eventually the process will block and no one can go 
in.

## Slide 52

Deadlock and Starvation
§ Deadlock – two or more processes are waiting indefinitely for an event that can be caused by only one 
of the waiting processes
§ Let S and Q be two semaphores initialized to 1
 P0 P1
 wait(S); wait(Q);
 wait(Q); wait(S);
 . .
 signal(S); signal(Q);
 signal(Q); signal(S);
§ Starvation – indefinite blocking 
§ A process may never be removed from the semaphore queue in which it is suspended
§ Priority Inversion – Scheduling problem when lower-priority process holds a lock needed by higherpriority process
 Solved via priority-inheritance protocol (processes accessing resources needed by a higherpriority process inherit the higher priority until they are finished and priority revert to original value)

## Slide 53

Classical Problems of Synchronization
§ Classical problems used to test newly-proposed synchronization schemes
§ Bounded-Buffer Problem
§ Readers and Writers Problem (refer to textbook)
§ Dining-Philosophers Problem (refer to textbook)

## Slide 54

Bounded-Buffer – Shared-Memory Solution
§ Solution is correct, but can only use 
BUFFER_SIZE-1 elements
#define BUFFER_SIZE 
10
typedef struct {
. . .
} item;
item 
buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
Int count = 0; item next_consumed; 
while (true) {
 while (count ==0); /* do nothing */
 next_consumed = buffer[out]; 
 out = (out + 1) % BUFFER_SIZE;
/* consume the item in next_consumed */ 
 count--;
} 
item next_produced; 
while (true) { 
/* produce an item in next_produced */ 
 while (count == BUFFER_SIZE); 
 /* do nothing */ 
 buffer[in] = next_produced; 
 in = (in + 1) % BUFFER_SIZE; 
 count++;
}

## Slide 55

Bounded-Buffer Problem
§ n buffers, each can hold one item
§ Semaphore mutex initialized to the value 1
§ Semaphore not_empty initialized to the value 0
§ Semaphore not_full initialized to the value n
Access Mutual Exclussion Section
Tells the consumer whether the buffer is 
empty or not, and how elements it has. 
Initially buffer is empty and there is nothing 
to read (semaphore = 0)
Tells the producer whether there are 
positions in which it can write (empties or the 
reader already consumed it).
Initially buffer is empty and the producer can 
write as many times as the capacity of the 
buffer (semaphore = n)

## Slide 56

Bounded Buffer Problem (Cont.)
§ The structure of the producer process
do { 
 ...
 /* produce an item in next_produced */ 
 ... 
 wait(not_full);
 wait(mutex); 
 ... /* add next produced to the buffer */ 
 ... 
 signal(mutex); 
 signal(not_empty); 
} while (true);
Initially the buffer is empty and can produce as many elements as buffer size
The producer waits in the semaphore while is full (semaphore = 0). 
It will be active again after a consumer signals it indicating that there is space available in the buffer
Wait to adquire for the lock to the critical section
release the lock to the critical section
Indicate the consumer that there are elements in the buffer

## Slide 57

Bounded Buffer Problem (Cont.)
§ The structure of the consumer process
do { 
 wait(not_empty); 
 wait(mutex); 
 ...
 /* remove an item from buffer to next_consumed */ 
 ... 
 signal(mutex); 
 signal(not_full); 
 ...
 /* consume the item in next consumed */ 
 ...
} while (true); 
Initially the buffer is empty. The consumer waits in the semaphore while is empty (semaphore = 0)
The semaphore will be active once a producer signal this semaphore after producing elements.
Wait to adquire for the lock to the critical section
release the lock to the critical section
Indicate the producer that there are free positions in the buffer

## Slide 58

Linux Synchronization
§ Linux:
§ Prior to kernel Version 2.6, disables interrupts to implement short critical 
sections
§ Version 2.6 and later, fully preemptive
§ Linux provides:
§ semaphores
§ spinlocks
§ reader-writer versions of both
§ On single-cpu system, spinlocks replaced by enabling and disabling kernel 
preemption

## Slide 59

Questions ?


---

# Chapter 7: File Systems Interface

## Slide 1

Operating System Concepts Silberschatz, Galvin and Gagne
ICT1012 － Operating Systems
Topic 7(a): File System Interface
Instructor: Assoc. Prof. Shang-Wei LIN (林尚威)
InfoComm Technology (ICT) Cluster,
Singapore Institute of Technology (SIT)
shangwei.lin@singaporetech.edu.sg

## Slide 2

Operating System Concepts 2 Silberschatz, Galvin and Gagne
Outline
▪ File Concept
▪ Access Methods
▪ Disk and Directory Structure
▪ Protection

## Slide 3

Operating System Concepts 3 Silberschatz, Galvin and Gagne
Objectives
▪ To explain the function of file systems
▪ To describe the interfaces to file systems
▪ To discuss file-system design tradeoffs, including 
• access methods
• file sharing
• directory structures
▪ To explore file-system protection

## Slide 4

Operating System Concepts 4 Silberschatz, Galvin and Gagne
Outline
▪ File Concept
▪ Access Methods
▪ Disk and Directory Structure
▪ Protection

## Slide 5

Operating System Concepts 5 Silberschatz, Galvin and Gagne
File Concept
▪ Contiguous logical address space
▪ Types: 
• Data
 Numeric
 Character
 Binary
• Program
▪ Contents defined by file’s creator
• Many types
 text file
 source file
 executable file

## Slide 6

Operating System Concepts 6 Silberschatz, Galvin and Gagne
File Attributes
▪ Name – only information kept in human-readable form
▪ Identifier – unique tag (number) identifies file within file system
▪ Type – needed for systems that support different types
▪ Location – pointer to file location on device
▪ Size – current file size
▪ Protection – controls who can do reading, writing, executing
▪ Time, date, and user identification – data for protection, security, and 
usage monitoring
▪ Information about files are kept in the directory structure, which is 
maintained on the disk
▪ Many variations, including extended file attributes such as file checksum

## Slide 7

Operating System Concepts 7 Silberschatz, Galvin and Gagne
File info Window on Mac OS X

## Slide 8

Operating System Concepts 8 Silberschatz, Galvin and Gagne
File Operations
▪ Create
▪ Write – at write pointer location
▪ Read – at read pointer location
▪ Reposition within file – seek
▪ Delete
▪ Truncate
▪ Open (Fi) – search the directory structure on disk for entry Fi, and 
move the content of entry to memory
▪ Close (Fi) – move the content of entry Fiin memory to directory 
structure on disk

## Slide 9

Operating System Concepts 9 Silberschatz, Galvin and Gagne
Open Files
▪ Several pieces of data are needed to manage open files:
• Open-file table: to track open files (only one maintained by OS)
• File pointer: pointer to last read/write location (per process)
• File-open count: counter of number of times a file is open
 to allow removal of data from open-file table when last 
processes closes it
• Disk location of the file: cache of data access information
• Access rights: access mode information (per process)

## Slide 10

Operating System Concepts 10 Silberschatz, Galvin and Gagne
File Types – Name, Extension

## Slide 11

Operating System Concepts 11 Silberschatz, Galvin and Gagne
File Structure
▪ How to interpret the content of a file?
• No structure - sequence of words or bytes (maximum flexibility)
• Simple record structure
 Lines 
 Fixed length
 Variable length
• Complex Structures
 Formatted document
 Relocatable load file
▪ Can simulate last two with first method by inserting appropriate control characters
▪ Who decides the structure?
• Operating system
• Program (programmer)

## Slide 12

Operating System Concepts 12 Silberschatz, Galvin and Gagne
Outline
▪ File Concept
▪ Access Methods
▪ Disk and Directory Structure
▪ Protection

## Slide 13

Operating System Concepts 13 Silberschatz, Galvin and Gagne
Access Methods
▪ A file is fixed length logical records
▪ How to access files?
• Sequential Access
• Direct Access
• Other Access Methods

## Slide 14

Operating System Concepts 14 Silberschatz, Galvin and Gagne
Sequential Access
▪ The simplest access method
• information in the file is processed in order, one record after the other
▪ Operations (based on blocks/records and current position)
• read_next
• write_next
• reset
• no read after last write (rewrite)

## Slide 15

Operating System Concepts 15 Silberschatz, Galvin and Gagne
Direct Access
▪ Read and write records rapidly in no particular order
▪ Operations (based on blocks/records number)
• read n
• write n
• To be compatible with sequential access
 position to n
 read_next
 write_next
▪ Relative block numbers allow OS to decide where file should be placed
n: relative block number
(relative to the beginning of the file)

## Slide 16

Operating System Concepts 16 Silberschatz, Galvin and Gagne
Simulation of Sequential Access on Direct-access File
cp: current position

## Slide 17

Operating System Concepts 17 Silberschatz, Galvin and Gagne
Other Access Methods
▪ Other access methods are usually built on top of base methods
▪ General involve creation of an index for the file
▪ Keep index in memory for fast determination of location of data
▪ What if the index is too large to be kept in memory?
• Create an index for the index file
• The primary index file (in memory) contains pointers to secondary index 
files (in disk), which point to the actual data items.

## Slide 18

Operating System Concepts 18 Silberschatz, Galvin and Gagne
Other Access Methods - Example
▪ IBM indexed sequential-access method (ISAM)
• Small master index, points to disk blocks of secondary index
• File kept sorted on a defined key
• All done by the OS
▪ VMS operating system provides index and relative files

## Slide 19

Operating System Concepts 19 Silberschatz, Galvin and Gagne
Outline
▪ File Concept
▪ Access Methods
▪ Disk and Directory Structure
▪ Protection

## Slide 20

Operating System Concepts 20 Silberschatz, Galvin and Gagne
Disk Structure
▪ Disk can be subdivided into partitions
▪ Disks or partitions can be RAID protected against failure
▪ Disk or partition can be used 
• raw – without a file system
• formatted – with a file system
▪ Entity containing file system is known as a volume
• Each volume can be thought of as a virtual disk
• Each volume stores the file system’s info in 
 device directory (we call it directory for short)
 volume table of contents

## Slide 21

Operating System Concepts 21 Silberschatz, Galvin and Gagne
A Typical File-system Organization
A partition or volume could be 
• a subset of a device
• a whole device
• multiple devices linked together into a RAID set.

## Slide 22

Operating System Concepts 22 Silberschatz, Galvin and Gagne
Types of File Systems
▪ We mostly talk of general-purpose file systems
• Some OS may have more than one file system
 some are general-purpose
 some are special-purpose
▪ Consider Solaris has
• tmpfs – memory-based volatile FS for fast, temporary I/O
• objfs – interface into kernel memory to get kernel symbols for debugging
• ctfs – contract file system for managing daemons 
• lofs – loopback file system allows one FS to be accessed in place of another
• procfs – kernel interface to process structures
• ufs, zfs – general purpose file systems

## Slide 23

Operating System Concepts 23 Silberschatz, Galvin and Gagne
Directory Structure
▪ The directory can be viewed as a symbol table that translates file names 
into their file control blocks.
▪ A collection of nodes containing information about all files
▪ Both the directory structure and the files reside on disk

## Slide 24

Operating System Concepts 24 Silberschatz, Galvin and Gagne
Operations Performed on Directory
▪ Search for a file
▪ Create a file
▪ Delete a file
▪ List a directory
▪ Rename a file
▪ Traverse the file system

## Slide 25

Operating System Concepts 25 Silberschatz, Galvin and Gagne
Directory Organization
▪ Efficiency – locating a file quickly
▪ Naming – convenient to users
• Two users can have same name for different files
• The same file can have several different names
▪ Grouping – logical grouping of files by properties
• e.g., all Java programs, all games, …
The directory is organized logically to obtain

## Slide 26

Operating System Concepts 26 Silberschatz, Galvin and Gagne
Single-Level Directory
▪ A single directory for all users
▪ Naming problem
• Each file must have a unique name 
▪ Difficult to remember all file names, when the number of files increases

## Slide 27

Operating System Concepts 27 Silberschatz, Galvin and Gagne
Two-Level Directory
▪ Separate directory for each user
▪ A username and a file name define a path name
▪ user1/cat/file
▪ Different users may have files with the same name
▪ as long as all the file names within each UFD are unique
▪ Efficient searching
▪ When a user refers to a particular file, only his own UFD is searched
MFD:
UFD:

## Slide 28

Operating System Concepts 28 Silberschatz, Galvin and Gagne
Tree-Structured Directories
▪ Extended to multi-levels

## Slide 29

Operating System Concepts 29 Silberschatz, Galvin and Gagne
Acyclic-Graph Directories
▪ Shared subdirectories and files

## Slide 30

Operating System Concepts 30 Silberschatz, Galvin and Gagne
Acyclic-Graph Directories (Cont.)
▪ Two different names (aliasing)
▪ If dict deletes w/list  dangling pointer
Solutions:
• Backpointers, so we can delete all pointers.
 Variable size records a problem
• File reference count
 The file will be deleted, if the count is 0 
▪ Possible implementation: New directory entry type
• Link – another name (pointer) to an existing file
• Resolve the link – follow pointer to locate the file

## Slide 31

Operating System Concepts 31 Silberschatz, Galvin and Gagne
Acyclic-Graph Directories (Cont.)
▪ How do we guarantee no cycles?
• Allow only links to files not subdirectories
• Every time a new link is added use a cycle detection algorithm to 
determine whether it is OK

## Slide 32

Operating System Concepts 32 Silberschatz, Galvin and Gagne
General Graph Directory
▪ The most flexible directory structure, which allows cycles

## Slide 33

Operating System Concepts 33 Silberschatz, Galvin and Gagne
General Graph Directory (Cont.)
▪ Traversing a graph with cycles may not terminate
• A poorly designed algorithm might result in an infinite loop continually 
searching through the cycle and never terminating
• Performance issue
▪ Solutions:
• Bypass links
• Limit the number of directories that will be accessed during a search
• Run cycle-detection algorithms (graph theory) to detect cycles
 computationally expensive

## Slide 34

Operating System Concepts 34 Silberschatz, Galvin and Gagne
Current Directory
▪ Designate one of the directories as the current (working) directory
• cd /spell/mail/prog
• type list
▪ Creating and deleting a file is done in current directory
▪ Example of creating a new file
• If in current directory is /mail
• The command 
 mkdir <dir-name>
• Results in:
• Deleting “mail”  deleting the entire subtree rooted by “mail”

## Slide 35

Operating System Concepts 35 Silberschatz, Galvin and Gagne
Outline
▪ File Concept
▪ Access Methods
▪ Disk and Directory Structure
▪ Protection

## Slide 36

Operating System Concepts 36 Silberschatz, Galvin and Gagne
Protection
▪ File owner/creator should be able to control:
• What can be done
• By whom
▪ Types of access
• Read
• Write
• Execute
• Append
• Delete
• List

## Slide 37

Operating System Concepts 37 Silberschatz, Galvin and Gagne
Access Lists and Groups in Unix
▪ Mode of access: read (R), write (W), execute (X)
▪ Three classes of users on Unix / Linux
RWX
a) owner access 7  1 1 1
RWX
b) group access 6  1 1 0
RWX
c) public access 1  0 0 1
▪ Ask manager to create a group (unique name), say G, and add some 
users to the group.
▪ For a file (say game) or subdirectory, define an appropriate access.
▪ Attach a group to a file
 chgrp G game

## Slide 38

Operating System Concepts 38 Silberschatz, Galvin and Gagne
A Sample UNIX Directory Listing
d: directory

## Slide 39

Operating System Concepts 39 Silberschatz, Galvin and Gagne
Windows 7 Access-Control List Management

## Slide 40

Operating System Concepts Silberschatz, Galvin and Gagne
End of Topic


---

# Chapter 7b: File System Implementation

## Slide 1

Operating System Concepts Silberschatz, Galvin and Gagne
ICT1012 － Operating Systems
Topic 7(b): File System Implementation
Instructor: Assoc. Prof. Shang-Wei LIN (林尚威)
InfoComm Technology (ICT) Cluster,
Singapore Institute of Technology (SIT)
shangwei.lin@singaporetech.edu.sg

## Slide 2

Operating System Concepts 2 Silberschatz, Galvin and Gagne
Outline 
▪ File-System Structure
▪ File-System Operations
▪ Directory Implementation
▪ Allocation Methods
▪ Free-Space Management 
▪ Efficiency and Performance

## Slide 3

Operating System Concepts 3 Silberschatz, Galvin and Gagne
Objectives
▪ Describe the details of implementing local file systems and directory structures
▪ Discuss block allocation and free-block algorithms and trade-offs
▪ Explore file system efficiency and performance issues

## Slide 4

Operating System Concepts 4 Silberschatz, Galvin and Gagne
Outline 
▪ File-System Structure
▪ File-System Operations
▪ Directory Implementation
▪ Allocation Methods
▪ Free-Space Management 
▪ Efficiency and Performance

## Slide 5

Operating System Concepts 5 Silberschatz, Galvin and Gagne
File-System Structure
▪ File system resides on secondary storage (disks)
• Provides user interface to storage
 mapping logical space to physical space
• Provides efficient and convenient access to disk 
 allowing data to be stored, located, and retrieved easily
▪ Disk provides in-place rewrite and random access
• I/O transfers performed in blocks of sectors (usually 512 bytes)
▪ File control block (FCB) – storage structure consisting of information about a file

## Slide 6

Operating System Concepts 6 Silberschatz, Galvin and Gagne
Layered File System
▪ Layered Architecture
▪ Advantage:
• reduces complexity
• reduces redundancy
• modularity
▪ Disadvantage:
• adds overhead 
• decreases performance

## Slide 7

Operating System Concepts 7 Silberschatz, Galvin and Gagne
File System Layers (Cont.)
▪ Logical file system
• Manages file control blocks (FCB)
 metadata information
• Translates the file name into file 
number, file handle, location
• Directory management
• Protection

## Slide 8

Operating System Concepts 8 Silberschatz, Galvin and Gagne
File System Layers
▪ File-organization module
• understands files, logical address, and 
physical blocks
• translates logical block # to physical block #
• manages free space, disk allocation

## Slide 9

Operating System Concepts 9 Silberschatz, Galvin and Gagne
File System Layers
▪ Basic file system
• issues basic commands to device driver
• Reads and writes block on disk
 e.g., “read block 123”
• manages memory buffers to hold data block
 Buffers hold data in transit
 Caches hold frequently used data

## Slide 10

Operating System Concepts 10 Silberschatz, Galvin and Gagne
▪ I/O control layer
• Device drivers transfer info between memory 
and disk
• High level instruction is translated to low-level 
hardware-specific instructions to control the 
device
 e.g., read drive1, cylinder 72, track 2, sector 
10, into memory location 1060
File System Layers

## Slide 11

Operating System Concepts 11 Silberschatz, Galvin and Gagne
Outline 
▪ File-System Structure
▪ File-System Operations
▪ Directory Implementation
▪ Allocation Methods
▪ Free-Space Management 
▪ Efficiency and Performance

## Slide 12

Operating System Concepts 12 Silberschatz, Galvin and Gagne
File-System Operations
▪ Several on-disk and in-memory structures are used to implement a file system
• These structures vary in different OS, but some general principles apply
▪ Boot control block contains info needed by system to boot OS from that volume
• Needed if volume contains OS, usually first block of volume
▪ Volume control block (superblock, master file table) contains volume details
• Total # of blocks, # of free blocks, block size, free block pointers or array
▪ Directory structure organizes the files
• Names and inode numbers, master file table

## Slide 13

Operating System Concepts 13 Silberschatz, Galvin and Gagne
File Control Block (FCB)
▪ OS maintains file control block (FCB) per file
• Containing many details about the file
 Typically, permissions, size, dates, inode number, etc.

## Slide 14

Operating System Concepts 14 Silberschatz, Galvin and Gagne
Outline 
▪ File-System Structure
▪ File-System Operations
▪ Directory Implementation
▪ Allocation Methods
▪ Free-Space Management 
▪ Efficiency and Performance

## Slide 15

Operating System Concepts 15 Silberschatz, Galvin and Gagne
Directory Implementation
▪ Linear list of file names with pointer to the data blocks
• Simple to program
• Time-consuming to execute
 Linear search time, O(n), when creating or deleting files
 Improvement:
– alphabetically ordered linked list (binary search, O(log 𝑛))
▪ Hash Table – linear list with hash data structure
• Decreases directory search time
• Collisions – situations where two file names hash to the same location
• Only good if entries are fixed size, or collisions can be resolved easily

## Slide 16

Operating System Concepts 16 Silberschatz, Galvin and Gagne
Outline 
▪ File-System Structure
▪ File-System Operations
▪ Directory Implementation
▪ Allocation Methods
▪ Free-Space Management 
▪ Efficiency and Performance

## Slide 17

Operating System Concepts 17 Silberschatz, Galvin and Gagne
Allocation Method 
▪ An allocation method refers to how disk blocks are allocated for files:
• Contiguous Allocation
• Linked Allocation
 File Allocation Table (FAT)
• Indexed Allocation

## Slide 18

Operating System Concepts 18 Silberschatz, Galvin and Gagne
Contiguous Allocation
▪ Each file occupies set of contiguous blocks
• The size of the file must be decided (known), when it is created
 How many blocks are needed?
• Best performance in most cases
• Simple – only two info are required
 starting block number
 length (number of blocks)
• Problems include:
 Finding space on the disk for a file 
 Knowing file size in advance
 External fragmentation (to be introduced in a moment)
– need for compaction off-line (downtime) or on-line

## Slide 19

Operating System Concepts 19 Silberschatz, Galvin and Gagne
Fragmentation
▪ External Fragmentation
• There is enough total space to 
satisfy a request but the available 
spaces are not contiguous
• Compaction
 Move occupied spaces to make 
them contiguous
▪ Internal Fragmentation
• The allocated space is larger than 
requested
Figure Source: https://takeuforward.org/operating-system/memory-management-techniques

## Slide 20

Operating System Concepts 20 Silberschatz, Galvin and Gagne
Contiguous Allocation (Cont.)
▪ Mapping from logical address (LA) to physical (block size =512 bytes)
▪ Block to be accessed = starting address + Q
▪ Displacement into block = R
LA/512
Q
R

## Slide 21

Operating System Concepts 21 Silberschatz, Galvin and Gagne
Extent-Based Systems
▪ Many newer file systems (i.e., Veritas File System) use a modified
contiguous allocation scheme
▪ Extent-based file systems allocate disk blocks in extents
▪ An extent is a contiguous block of disks
• Extents are allocated, when a file grows and needs more space
• A file consists of one or more extents

## Slide 22

Operating System Concepts 22 Silberschatz, Galvin and Gagne
Linked Allocation
▪ Each file is a linked list of blocks
• Each block contains the pointer to the next block
• File ends at nil pointer
• A new block request is managed by free space management
▪ Advantage:
• No external fragmentation (no need of compaction)
• Files can continue to grow (no need to know the file size in advance)
▪ Disadvantage:
• Inefficient for direct/random access
 Locating the i-th block can take many I/Os and disk seeks
• Space wastage (overhead on the pointer to the next block)
• Reliability can be a problem (lost/damaged pointer)

## Slide 23

Operating System Concepts 23 Silberschatz, Galvin and Gagne
Linked Allocation Example
▪ Each file is a linked list of disk blocks
• blocks may be scattered anywhere on the disk
▪ Scheme

## Slide 24

Operating System Concepts 24 Silberschatz, Galvin and Gagne
File-Allocation Table (FAT)
▪ Beginning of the volume has a table, indexed by block number
• Each entry records the next block number
• Fast, when the table can be cached (in memory)
-1

## Slide 25

Operating System Concepts 25 Silberschatz, Galvin and Gagne
Indexed Allocation
▪ Each file has its own index block(s) of pointers to its data blocks
• an array of storage-block addresses
• the i-th entry in the index block points to the i-th block of the file
▪ Logical view
index table

## Slide 26

Operating System Concepts 26 Silberschatz, Galvin and Gagne
Example of Indexed Allocation

## Slide 27

Operating System Concepts 27 Silberschatz, Galvin and Gagne
Indexed Allocation Method (cont.)
▪ Advantage:
• Support random access
• No external fragmentation
▪ Disadvantage:
• How to decide the size of index block?
• Overhead of index block
 Wastage of space
– All the pointers in the index block have to be allocated, even if they 
point to null
• How to extend for large files?
 linked indexed files
 multilevel indexed files

## Slide 28

Operating System Concepts 28 Silberschatz, Galvin and Gagne
Performance
▪ Best method depends on file access type
• Contiguous allocation
 great for sequential and random (direct) access
 But file size needs to be declared (not easily grow)
• Linked allocation
 good for sequential, but not random (direct) access
• Indexed allocation (more complex)
 Single block access could require 2 reads (index block read then 
data block read)
▪ Some file systems require to declare access type at creation
• Select either contiguous or linked
▪ Some systems combine contiguous (for small file) with indexed 
allocation (if the file grows large)

## Slide 29

Operating System Concepts 29 Silberschatz, Galvin and Gagne
Outline 
▪ File-System Structure
▪ File-System Operations
▪ Directory Implementation
▪ Allocation Methods
▪ Free-Space Management
▪ Efficiency and Performance

## Slide 30

Operating System Concepts 30 Silberschatz, Galvin and Gagne
Free-Space Management
▪ File system maintains a free-space list to track available blocks
▪ Different design/implementation of the free-space list
• Bit Vector or Bitmap
• Linked List

## Slide 31

Operating System Concepts 31 Silberschatz, Galvin and Gagne
Bit Vector
▪ Bit vector or bit map (n blocks) …
0 1 2 n -1
bit[i] =
1  block[i] free
0  block[i] occupied
0: allocated
1: free

## Slide 32

Operating System Concepts 32 Silberschatz, Galvin and Gagne
Bit Vector (cont.)
Block number calculation of the first free block
(number of bits per word) * (number of 0-value words) + offset of first 1 bit
CPUs have instructions to return the offset within the word of the first “1” bit

## Slide 33

Operating System Concepts 33 Silberschatz, Galvin and Gagne
Bit Vector (cont.)
▪ Advantage:
• Easy to get contiguous files
▪ Disadvantage:
• requires extra space
• Example:
block size = 4KB = 212 bytes
disk size = 240 bytes (1 terabyte)
n = 240/212 = 228 bits (or 32MB)
if clusters of 4 blocks -> 8MB of memory

## Slide 34

Operating System Concepts 34 Silberschatz, Galvin and Gagne
Linked List
▪ The free-space list is implemented as a linked list
▪ Advantage:
• No extra space required 
• No need to traverse the entire list 
• The first free block will do
• Disadvantage:
• Cannot get contiguous space easily

## Slide 35

Operating System Concepts 35 Silberschatz, Galvin and Gagne
Outline 
▪ File-System Structure
▪ File-System Operations
▪ Directory Implementation
▪ Allocation Methods
▪ Free-Space Management 
▪ Efficiency and Performance

## Slide 36

Operating System Concepts 36 Silberschatz, Galvin and Gagne
Efficiency
▪ Efficiency here means efficient use of storage device space
▪ Efficiency depends on:
• Disk allocation and directory algorithms
• Types of data kept in file’s directory entry
• Pre-allocation or as-needed allocation of metadata structures
• Fixed-size or varying-size data structures

## Slide 37

Operating System Concepts 37 Silberschatz, Galvin and Gagne
Performance
▪ Performance here means how fast the read/write operations can be finished
▪ Performance depends on:
• Keeping data and metadata close together
• Buffer cache – separate section of main memory for frequently used blocks
 Synchronous writes
– No buffering / caching – the caller must wait until the data has been 
written back to disk successfully
– Slow, but does not require OS to take care of data consistency
 Asynchronous writes 
– Control returns to the caller once the data has been written in cache
– Fast, but requires OS to take care of data consistency

## Slide 38

Operating System Concepts Silberschatz, Galvin and Gagne
End of Topic


---

# Chapter 8: Main Memory

## Slide 1

Operating System Concepts Silberschatz, Galvin and Gagne
ICT1012 － Operating Systems
Topic 8: Memory Management
Instructor: Assoc. Prof. Shang-Wei LIN (林尚威)
InfoComm Technology (ICT) Cluster,
Singapore Institute of Technology (SIT)
shangwei.lin@singaporetech.edu.sg

## Slide 2

Operating System Concepts 2 Silberschatz, Galvin and Gagne
Outline
▪ Background
▪ Contiguous Memory Allocation
▪ Paging
▪ Structure of the Page Table
▪ Swapping

## Slide 3

Operating System Concepts 3 Silberschatz, Galvin and Gagne
Learning Objectives
▪ To provide a detailed description of various ways of organizing memory
▪ To discuss various memory-management techniques

## Slide 4

Operating System Concepts 4 Silberschatz, Galvin and Gagne
Outline
▪ Background
▪ Contiguous Memory Allocation
▪ Paging
▪ Structure of the Page Table
▪ Swapping

## Slide 5

Operating System Concepts 5 Silberschatz, Galvin and Gagne
Background
▪ CPU can only access registers and main memory directly
• Program must be brought (from disk) into memory before execution
▪ Memory unit only sees a stream of the following operations:
• address read requests, or 
• address write requests
▪ Register access is done in one CPU clock (or less)
▪ Main memory can take many cycles, causing a stall
• Cache sits between main memory and CPU registers
▪ Protection of memory required to ensure correct operation
• memory used by OS kernel cannot be accessed by user programs

## Slide 6

Operating System Concepts 6 Silberschatz, Galvin and Gagne
Protection
▪ A process should access only those addresses in its address space
• How to ensure this?
▪ A pair of base and limit registers to define its logical address space
base: 300040
limit: 120900
legal address: 
300040 ~ 420940 (inclusive)

## Slide 7

Operating System Concepts 7 Silberschatz, Galvin and Gagne
Hardware Address Protection
▪ CPU must check every memory access generated in user mode to 
be sure it is between base and limit for that user
▪ The base and limit registers can only be loaded by OS
• by special privileged instructions (only in kernel mode)

## Slide 8

Operating System Concepts 8 Silberschatz, Galvin and Gagne
Multistep Processing of a User Program

## Slide 9

Operating System Concepts 9 Silberschatz, Galvin and Gagne
Address Binding
▪ Programs must be brought into memory before execution
• But WHERE (which addresses) in the memory?
▪ Deciding where to load the program is called address binding
▪ Addresses can be represented in different ways at different stages
• Source code addresses are usually symbolic
• Compiled code addresses bind to relocatable addresses
 i.e., “14 bytes from beginning of this module”
• Linker or loader will bind relocatable addresses to absolute addresses
 i.e., 74014
• Each binding maps one address space to another

## Slide 10

Operating System Concepts 10 Silberschatz, Galvin and Gagne
▪ Address binding can happen at 
three different stages
• Compile time
• Load time
• Execution time
Address Binding (cont.)

## Slide 11

Operating System Concepts 11 Silberschatz, Galvin and Gagne
▪ Compile time
• If memory location known a priori, 
absolute code can be generated
• must recompile code if starting 
location changes
Address Binding (cont.)

## Slide 12

Operating System Concepts 12 Silberschatz, Galvin and Gagne
▪ Load time
• If memory location is not known at 
compile time, must generate 
relocatable code
• If starting address changes, only 
need to reload code
Address Binding (cont.)

## Slide 13

Operating System Concepts 13 Silberschatz, Galvin and Gagne
▪ Execution time
• if the process can be moved during its 
execution from one memory segment 
to another, address binding has to be 
delayed until run time
• Need hardware support for address 
maps (e.g., base and limit registers)
Address Binding (cont.)

## Slide 14

Operating System Concepts 14 Silberschatz, Galvin and Gagne
Logical vs. Physical Address Space
▪ The concept of a logical address space that is bound to a separate 
physical address space is central to proper memory management
• Logical address – generated by the CPU; a.k.a. virtual address
• Physical address – address seen by the memory unit
▪ Logical and physical addresses are the same in compile-time and 
load-time address-binding schemes
▪ logical (virtual) and physical addresses differ in execution-time 
address-binding scheme
▪ Logical address space is the set of all logical addresses generated 
by a program
▪ Physical address space is the set of all physical addresses 
generated by a program

## Slide 15

Operating System Concepts 15 Silberschatz, Galvin and Gagne
Memory Management Unit (MMU)
▪ Hardware device that at run time maps virtual to physical address
• MMU: Memory Management Unit
▪ Many methods possible (will be introduced in a moment)

## Slide 16

Operating System Concepts 16 Silberschatz, Galvin and Gagne
Memory Management Unit (Cont.)
▪ Consider a simple scheme: a generalization of the base register scheme
▪ The base register now called relocation register
▪ The value in the relocation register is added to every address generated 
by a user process at the time it is sent to memory
▪ The user program deals with logical addresses
• it never sees the real physical addresses

## Slide 17

Operating System Concepts 17 Silberschatz, Galvin and Gagne
Dynamic Loading
▪ The entire program does need to be in memory to execute
▪ Routine is not loaded until it is called
▪ Better memory-space utilization
▪ unused routine is never loaded
▪ All routines kept on disk in relocatable load format
▪ Useful when large amounts of code are needed to handle infrequently 
occurring cases
▪ No special support from the operating system is required
• Implemented through program design
• OS can help by providing libraries to implement dynamic loading

## Slide 18

Operating System Concepts 18 Silberschatz, Galvin and Gagne
Dynamic Linking
▪ Static linking – system libraries and program code combined by the loader 
into the binary program image
▪ Dynamic linking –linking postponed until execution time
• Small piece of code, stub, used to locate the memory-resident routine
• Stub replaces itself with the address of the routine to be executed
• OS checks if the routine is in processes’ memory address
 If not, add it to the address space
▪ Dynamic linking is particularly useful for libraries
• also known as shared libraries
• Consider applicability to patching system libraries
 Versioning may be needed

## Slide 19

Operating System Concepts 19 Silberschatz, Galvin and Gagne
Outline
▪ Background
▪ Contiguous Memory Allocation
▪ Paging
▪ Structure of the Page Table
▪ Swapping

## Slide 20

Operating System Concepts 20 Silberschatz, Galvin and Gagne
Contiguous Allocation
▪ Main memory must support both OS and user processes
▪ Limited resource, must allocate efficiently
▪ Contiguous allocation is one early method
▪ Main memory usually into two partitions:
• Resident operating system
 usually held in low memory with interrupt vector
• User processes then held in high memory
 Each process contained in single contiguous section of memory

## Slide 21

Operating System Concepts 21 Silberschatz, Galvin and Gagne
Contiguous Allocation (Cont.)
▪ Relocation registers used to protect user processes from each other, 
and from changing operating-system code and data
• Base register contains value of smallest physical address
• Limit register contains range of logical addresses
 Each logical address must be less than the limit register
– WHY? Think about it!
• MMU maps logical addresses to physical addresses dynamically
• This allows actions such as kernel code being transient and kernel 
changing size

## Slide 22

Operating System Concepts 22 Silberschatz, Galvin and Gagne
Hardware Support for Relocation and Limit Registers

## Slide 23

Operating System Concepts 23 Silberschatz, Galvin and Gagne
Variable Partition
▪ Multiple-partition allocation
• Degree of multiprogramming limited by number of partitions
• Variable size for each partition for efficiency (sized to a given process’ needs)
• Hole – block of available memory
 holes of various size are scattered throughout memory
• When a process arrives, it is allocated memory from a hole large enough to accommodate it
• Process exiting frees its partition, adjacent free partitions combined
• Operating system maintains information about:
 allocated partitions 
 free partitions (hole)

## Slide 24

Operating System Concepts 24 Silberschatz, Galvin and Gagne
Dynamic Storage-Allocation Problem
▪ First-fit: Allocate the first hole that is big enough
▪ Best-fit: Allocate the smallest hole that is big enough
• Must search entire list, unless ordered by size 
• Produces the smallest leftover hole
▪ Worst-fit: Allocate the largest hole
• Must search entire list 
• Produces the largest leftover hole
How to satisfy a request of size n from a list of free holes?
First-fit and best-fit better than worst-fit in terms of speed and storage utilization

## Slide 25

Operating System Concepts 25 Silberschatz, Galvin and Gagne
Fragmentation
▪ External Fragmentation
• Total memory space exists to satisfy a request, but it is not contiguous
▪ Internal Fragmentation
• Allocated memory may be slightly larger than requested memory
• This size difference is internal to a partition, but not being used
▪ First fit analysis reveals that the 50-percent rule
• Given N blocks allocated, another 0.5N blocks are lost in fragmentation
▪ Reduce external fragmentation by compaction
• Shuffle memory contents to place all free memory contiguous
• Possible only if relocation is dynamic at execution time
• Expensive

## Slide 26

Operating System Concepts 26 Silberschatz, Galvin and Gagne
Outline
▪ Background
▪ Contiguous Memory Allocation
▪ Paging
▪ Structure of the Page Table
▪ Swapping

## Slide 27

Operating System Concepts 27 Silberschatz, Galvin and Gagne
Paging
▪ Physical address space of a process can be noncontiguous
• Avoids external fragmentation
• Avoids problem of varying sized memory chunks
▪ Divide physical memory into fixed-sized blocks called frames
• Size is power of 2, between 512 bytes and 16 Mbytes
• Keep track of all free frames
▪ Divide logical memory into blocks of same size called pages
▪ A program of size N pages requires N free frames to be loaded into memory
▪ A page table (per process) is used to translate logical to physical addresses
▪ Paging still has internal fragmentation

## Slide 28

Operating System Concepts 28 Silberschatz, Galvin and Gagne
Address Translation Scheme
▪ Address generated by CPU is divided into:
• Page number (p) – used as an index into a page table
 contains base address of each page in physical memory
• Page offset (d) – combined with base address to define the physical 
memory address that is sent to the memory unit
• For given logical address space 2m and page size 2
n

## Slide 29

Operating System Concepts 29 Silberschatz, Galvin and Gagne
Paging Hardware

## Slide 30

Operating System Concepts 30 Silberschatz, Galvin and Gagne
Paging Model of Logical and Physical Memory

## Slide 31

Operating System Concepts 31 Silberschatz, Galvin and Gagne
Paging Example 
▪ Logical address: n = 2 and m = 4. Using a page size of 4 bytes and 
a physical memory of 32 bytes (8 pages)

## Slide 32

Operating System Concepts 32 Silberschatz, Galvin and Gagne
Paging -- Calculating internal fragmentation
▪ Page size = 2,048 bytes
▪ Process size = 72,766 bytes
▪ 35 pages + 1,086 bytes are required
▪ Internal fragmentation of 2,048 - 1,086 = 962 bytes
▪ Worst case (internal) fragmentation (in bytes) = S – 1
▪ On average fragmentation = 1/2 S
▪ So small frame sizes desirable?
• But each page table entry takes memory to track
▪ Page sizes growing over time
• Solaris supports two page sizes – 8 KB and 4 MB
S: page size

## Slide 33

Operating System Concepts 33 Silberschatz, Galvin and Gagne
Free Frames
Before allocation After allocation

## Slide 34

Operating System Concepts 34 Silberschatz, Galvin and Gagne
Implementation of Page Table
▪ Page table can be kept in high-speed hardware registers
• Fast, but expensive
 only feasible for small page tables
• Increases overhead when performing a context switch
▪ Page table is kept in main memory
• Page-table base register (PTBR) points to the page table (in memory)
• Page-table length register (PTLR) indicates size of the page table
• Every data/instruction access requires two memory accesses
 One for the page table and one for the data/instruction
 Solution: translation look-aside buffers (TLBs)
– A special, small, fast-lookup, hardware cache
– (also called associative memory).

## Slide 35

Operating System Concepts 35 Silberschatz, Galvin and Gagne
Translation Look-Aside Buffer
parallel search
Add the 
missed frame 
number to TLB

## Slide 36

Operating System Concepts 36 Silberschatz, Galvin and Gagne
Translation Look-Aside Buffer (cont.) 
▪ Some TLBs store address-space identifiers (ASIDs) in each TLB entry
• Uniquely identifies each process to provide address-space protection
• Otherwise need to flush at every context switch
▪ TLBs typically small (64 to 1,024 entries)
▪ On a TLB miss, value is loaded into the TLB for faster access next time
• Replacement policies must be considered
• Some entries can be wired down for permanent fast access

## Slide 37

Operating System Concepts 37 Silberschatz, Galvin and Gagne
Effective Access Time (EAT)
▪ Hit ratio – percentage of times that a page number is found in the TLB
▪ An 80% hit ratio
 the desired page number is found in the TLB 80% of the time
▪ Suppose that 10 nanoseconds are required to access memory 
• If the desired page is found in TLB, a mapped-memory access take 10 ns
• Otherwise, we need two memory access so it is 20 ns
▪ Effective Access Time (EAT) of an 80% hit ratio
 EAT = 0.80 x 10 + 0.20 x 20 = 12 nanoseconds
 implying 20% slowdown in access time
▪ Consider a more realistic hit ratio of 99%, 
 EAT = 0.99 x 10 + 0.01 x 20 = 10.1ns
 implying only 1% slowdown in access time.

## Slide 38

Operating System Concepts 38 Silberschatz, Galvin and Gagne
Memory Protection
▪ Additional protection bits (per frame) can be used in page table
• To indicate access rights, e.g., read-only, read-write, etc
▪ Valid-invalid bit attached to each entry in the page table:
•“valid” indicates that the associated page is in the process’
logical address space, and is thus a legal page
•“invalid” indicates that the page is not in the process’ logical 
address space
▪ Any violations result in a trap to the kernel

## Slide 39

Operating System Concepts 39 Silberschatz, Galvin and Gagne
Valid (v) or Invalid (i) Bit in A Page Table
Consider a system with 14-bit address space (0 to 16,383), page size of 2KB 
A program that should use only addresses 0 to 10,468
Page 5 in valid, but bytes 10,469 ~ 12,287 are invalid
Internal fragmentation

## Slide 40

Operating System Concepts 40 Silberschatz, Galvin and Gagne
Shared Pages
▪ The same computation but on different data
▪ Shared code
• One copy of read-only (reentrant) code shared among processes
 e.g., text editors, compilers, window systems
• Similar to multiple threads sharing the same process space
• Also useful for interprocess communication if sharing of read-write 
pages is allowed
▪ Private data
• Each process keeps a separate copy of data for computation

## Slide 41

Operating System Concepts 41 Silberschatz, Galvin and Gagne
Shared Pages Example

## Slide 42

Operating System Concepts 42 Silberschatz, Galvin and Gagne
Outline
▪ Background
▪ Contiguous Memory Allocation
▪ Paging
▪ Structure of the Page Table
▪ Swapping

## Slide 43

Operating System Concepts 43 Silberschatz, Galvin and Gagne
Structure of the Page Table
▪ Memory structures for paging can get huge using straight-forward methods
• Consider a 32-bit logical address space as on modern computers
• Page size of 4 KB (i.e., 212 bytes)
• Page table would have 1 million entries (232 / 212)
• If each entry is 4 bytes ➔ each process requires 4 MB of physical 
address space for the page table alone
 Don’t want to allocate that contiguously in main memory
▪ One simple solution is to divide the page table into smaller units
• Hierarchical Paging
• Hashed Page Tables
• Inverted Page Tables

## Slide 44

Operating System Concepts 44 Silberschatz, Galvin and Gagne
Hierarchical Page Tables
▪ Break up the logical address space into multiple page tables
▪ A simple technique is a two-level page table
▪ We then page the page table

## Slide 45

Operating System Concepts 45 Silberschatz, Galvin and Gagne
Two-Level Paging Example
▪ A logical address (on 32-bit machine with 4K page size) is divided into:
• a page number consisting of 20 bits
• a page offset consisting of 12 bits
▪ Since the page table is paged, the page number is further divided into:
• a 10-bit page number 
• a 10-bit page offset
▪ Thus, a logical address is as follows:
▪ where p1is an index into the outer page table, and p2is the 
displacement within the page of the inner page table
▪ Known as forward-mapped page table

## Slide 46

Operating System Concepts 46 Silberschatz, Galvin and Gagne
Address-Translation Scheme

## Slide 47

Operating System Concepts 47 Silberschatz, Galvin and Gagne
64-bit Logical Address Space
▪ Even two-level paging scheme is not sufficient
▪ If page size is 4 KB (212)
• Then page table has 252 entries
• If two level scheme, inner page tables could be 210 entries
• Address would look like
• Outer page table has 242 entries
• One solution is to add a 2nd outer page table
• But in the following example the 2nd outer page table still has 232 entries
 And possibly 4 memory access to get to one physical memory location

## Slide 48

Operating System Concepts 48 Silberschatz, Galvin and Gagne
Three-level Paging Scheme

## Slide 49

Operating System Concepts 49 Silberschatz, Galvin and Gagne
Hashed Page Tables
▪ Commonly used in address spaces bigger than 32-bit 
▪ The virtual page number is hashed into a page table
• a linked list of elements hashing to the same location
 To handle collisions
▪ Virtual page numbers are compared in the linked list searching for a match
• If a match is found, the corresponding physical frame is extracted
▪ Variation for 64-bit addresses is clustered page tables
• Similar to hashed but each entry refers to several pages (such as 16) 
rather than 1
• Especially useful for sparse address spaces (where memory references 
are non-contiguous and scattered)

## Slide 50

Operating System Concepts 50 Silberschatz, Galvin and Gagne
Hashed Page Table (cont.)
▪ Each element contains
• (1) the virtual page number 
• (2) the value of the mapped page frame
• (3) a pointer to the next element

## Slide 51

Operating System Concepts 51 Silberschatz, Galvin and Gagne
Inverted Page Table
▪ Only ONE page table (for all processes) in the system!
▪ One entry for each real page (frame) of memory, indicating
• the virtual address of the page stored in that real memory location
• the process owning that page
▪ Advantage:
• Decreases memory needed to store each page table
▪ Disadvantage:
• Increases time needed to search the table when a page reference occurs

## Slide 52

Operating System Concepts 52 Silberschatz, Galvin and Gagne
Inverted Page Table Architecture

## Slide 53

Operating System Concepts 53 Silberschatz, Galvin and Gagne
Outline
▪ Background
▪ Contiguous Memory Allocation
▪ Paging
▪ Structure of the Page Table
▪ Swapping

## Slide 54

Operating System Concepts 54 Silberschatz, Galvin and Gagne
Swapping
▪ A process can be temporarily swapped out of memory to a backing store, and then 
swapped in back to memory for continued execution
• Total physical memory space of processes can exceed physical memory
 Increase degree of multiprogramming in a system

## Slide 55

Operating System Concepts 55 Silberschatz, Galvin and Gagne
Swapping (cont.)
▪ Backing store – fast disk large enough to 
• accommodate copies of all memory images for all users
• provide direct access to these memory images
▪ Roll out, roll in – swapping variant used for priority-based scheduling 
• lower-priority process is swapped out so higher-priority process can be 
loaded and executed
▪ Major part of swap time is transfer time
• total transfer time is directly proportional to the amount of memory 
swapped
▪ System maintains a ready queue of ready-to-run processes which have 
memory images on disk

## Slide 56

Operating System Concepts 56 Silberschatz, Galvin and Gagne
Swapping (Cont.)
▪ Does the swapped out process need to be swapped back into the same
physical addresses?
• This depends on
 address binding method
 any (asynchronous) pending I/O
▪ Modified versions of swapping are found on many systems (i.e., UNIX, Linux, 
and Windows)
• Swapping normally disabled
• Started if the amount of free memory falls below a threshold
• Disabled again once the amount of free memory goes above the threshold

## Slide 57

Operating System Concepts 57 Silberschatz, Galvin and Gagne
Context Switch Time Including Swapping
▪ What if the next process to be put on CPU is not in memory, and memory is 
not sufficient to swap in any process?
• need to swap out a process first and then swap in the target process
▪ Context switch time can then be very high
• 100MB process swapping to hard disk with transfer rate of 50MB/sec
 Swap out time of 2 secs
 Plus swap in time of the same sized process
 Total context switch swapping component time of 4 secs
▪ Standard swapping is not used in modern operating systems
• Context switch time is too long
• How to reduce context switch time (swap time) ?

## Slide 58

Operating System Concepts 58 Silberschatz, Galvin and Gagne
Swapping with Paging
▪ To reduce the swap time, swap a portion of a process, not the whole process

## Slide 59

Operating System Concepts Silberschatz, Galvin and Gagne
End of Topic


---

# Chapter 9: Virtual Memory

## Slide 1

Operating System Concepts – 10th Edition Silberschatz, Galvin and Gagne ©2018
ICT1012 － Operating Systems
Topic 9: Virtual Memory
Instructor: Assoc. Prof. Shang-Wei LIN (林尚威)
InfoComm Technology (ICT) Cluster,
Singapore Institute of Technology (SIT)
shangwei.lin@singaporetech.edu.sg

## Slide 2

Operating System Concepts – 10th Edition 2 Silberschatz, Galvin and Gagne ©2018
Outline
▪ Background
▪ Demand Paging
▪ Page Replacement
▪ Allocation of Frames
▪ Thrashing
▪ Other Considerations

## Slide 3

Operating System Concepts – 10th Edition 3 Silberschatz, Galvin and Gagne ©2018
Learning Objectives
▪ Define virtual memory and describe its benefits.
▪ Illustrate how pages are loaded into memory using demand paging.
▪ Apply the FIFO, optimal, and LRU page-replacement algorithms.
▪ Describe the working set of a process, and explain how it is related to 
program locality.

## Slide 4

Operating System Concepts – 10th Edition 4 Silberschatz, Galvin and Gagne ©2018
Outline
▪ Background
▪ Demand Paging
▪ Page Replacement
▪ Allocation of Frames
▪ Thrashing
▪ Other Considerations

## Slide 5

Operating System Concepts – 10th Edition 5 Silberschatz, Galvin and Gagne ©2018
Background
▪ Code needs to be in memory to execute, but the entire program is rarely used
• Error code, unusual routines, large data structures
▪ The entire program is not needed at the same time, in many cases
▪ Consider ability to execute partially-loaded programs
• Programs no longer constrained by limits of physical memory
• Each program takes less memory while running
 more programs run at the same time
 Increased CPU utilization and throughput
• Less I/O needed to load or swap programs into memory

## Slide 6

Operating System Concepts – 10th Edition 6 Silberschatz, Galvin and Gagne ©2018
Virtual Memory 
▪ Virtual memory – separation of user logical memory from physical memory
• Only part of the program needs to be in memory for execution
• Logical address space can be much larger than physical address space
• Allows address spaces to be shared by several processes
• Allows for more efficient process creation
• More programs running concurrently
• Less I/O needed to load or swap processes

## Slide 7

Operating System Concepts – 10th Edition 7 Silberschatz, Galvin and Gagne ©2018
Virtual Memory (Cont.)
▪ Virtual address space – logical view of how process is stored in memory
• Usually start at address 0, contiguous addresses until end of space
• Meanwhile, physical memory organized in page frames
• MMU must map logical to physical
▪ Virtual memory can be implemented via:
• Demand paging
• Demand segmentation

## Slide 8

Operating System Concepts – 10th Edition 8 Silberschatz, Galvin and Gagne ©2018
Virtual Memory Larger Than Physical Memory

## Slide 9

Operating System Concepts – 10th Edition 9 Silberschatz, Galvin and Gagne ©2018
Virtual-address Space
▪ Stack: from Max logical address and grows “down”
▪ Heap: grows “up”
▪ Maximizes address space use
▪ Unused address space between the two is hole
 No physical memory needed until heap or 
stack grows to a given new page
▪ Enables sparse address spaces with holes left for 
growth, dynamically linked libraries, etc.

## Slide 10

Operating System Concepts – 10th Edition 10 Silberschatz, Galvin and Gagne ©2018
Shared Library Using Virtual Memory

## Slide 11

Operating System Concepts – 10th Edition 11 Silberschatz, Galvin and Gagne ©2018
Outline
▪ Background
▪ Demand Paging
▪ Page Replacement
▪ Allocation of Frames
▪ Thrashing
▪ Other Considerations

## Slide 12

Operating System Concepts – 10th Edition 12 Silberschatz, Galvin and Gagne ©2018
Demand Paging
▪ A page is brought into memory only when it is needed
• No unnecessary I/O
• Less memory needed 
▪ We call it pager in a demand paging system
• Faster response
• More users

## Slide 13

Operating System Concepts – 10th Edition 13 Silberschatz, Galvin and Gagne ©2018
Basic Concepts
▪ When a process is to be swapped in, pager guesses which pages will 
be used before the process is swapped out again
▪ Pager brings in only those pages into memory
▪ How to determine that set of pages?
• Need new MMU functionality to implement demand paging
▪ If pages needed are already memory resident
• No difference from non demand paging system
▪ If page needed and not memory resident
• Need to detect and load the page into memory from storage
 Without changing program behavior
 Without programmer needing to change code

## Slide 14

Operating System Concepts – 10th Edition 14 Silberschatz, Galvin and Gagne ©2018
Implementation of Demand Paging
▪ Implementation of Demand Paging includes:
• Frame-allocation algorithm
 How many frames to give each process
• Page-replacement algorithm
 Which frames to replace
 With the lowest page-fault rate

## Slide 15

Operating System Concepts – 10th Edition 15 Silberschatz, Galvin and Gagne ©2018
Valid-Invalid Bit and Page Fault
▪ Each entry of the page table is associated with a valid–invalid bit
• v: in-memory – memory resident
• i: invalid
 Not a valid page
 The page is valid, but not in memory
▪ Initially valid–invalid bit is set to i on all entries
▪ Access to a page marked invalid causes a page fault
• The paging hardware will notice that the invalid bit 
is set, causing a trap to the operating system

## Slide 16

Operating System Concepts – 10th Edition 16 Silberschatz, Galvin and Gagne ©2018
Steps in Handling Page Fault
1. If a page not in memory is referenced, it will trap to operating system 
• Page fault
2. Operating system checks an internal table to decide:
• Invalid reference  terminate the process
• Just not in memory  need to bring in the page
3. Find a free frame (from the free frame list)
4. Swap the page into a (memory) frame via scheduled disk operation
5. Modify the page table to indicate that the page is now in memory
• Set validation bit = v
6. Restart the instruction interrupted by the page fault

## Slide 17

Operating System Concepts – 10th Edition 17 Silberschatz, Galvin and Gagne ©2018
Steps in Handling a Page Fault (Cont.)

## Slide 18

Operating System Concepts – 10th Edition 18 Silberschatz, Galvin and Gagne ©2018
Aspects of Demand Paging
▪ Extreme case – processes start with NO pages allocated in memory
• Pure demand paging – never bring a page into memory until required
 Every page encounters a page fault on its first access
▪ One instruction could access multiple pages, causing multiple page faults
• Consider fetch and decode of instruction which adds 2 numbers from 
memory and stores result back to memory
• Exceedingly unlikely, because of locality of reference
▪ Hardware support required for demand paging
• Page table with valid/invalid bit
• Secondary memory (swap device with swap space)
• Instruction restart

## Slide 19

Operating System Concepts – 10th Edition 19 Silberschatz, Galvin and Gagne ©2018
Instruction Restart
▪ After a page fault, we must be able to restart the process 
• in exactly the same place, and
• In exactly the same state, 
• except that the desired page is now in memory and is accessible.
▪ ADD O1, O2, R
1. Fetch and decode the instruction (ADD)
2. Fetch operand O1
3. Fetch operand O2
4. Compute O1 + O2
5. Store the result in R
▪ Page fault in any of the above steps, the instruction needs to restart
// R ← (O1 + O2)
1
2
3
5
Page faults 
could occur here

## Slide 20

Operating System Concepts – 10th Edition 20 Silberschatz, Galvin and Gagne ©2018
Free-Frame List
▪ When a page fault occurs, the operating system must bring the 
desired page from secondary storage into main memory.
▪ Most operating systems maintain a free-frame list
• a pool of free frames for satisfying such requests
▪ Operating system typically allocate free frames using a technique 
known as zero-fill-on-demand
• the content of the frames is zeroed-out before being allocated
▪ When a system starts up, all available memory is placed on the freeframe list.

## Slide 21

Operating System Concepts – 10th Edition 21 Silberschatz, Galvin and Gagne ©2018
Stages in Demand Paging
1. Trap to the operating system
2. Save the user registers and process state
3. Determine that the interrupt was a page fault
4. Check that the page reference was legal and determine the location of 
the page on the disk
5. Issue a read from the disk to a free frame:
a) Wait in a queue for this device until the read request is serviced
b) Wait for the device seek and/or latency time
c) Begin the transfer of the page to a free frame
Worst Case

## Slide 22

Operating System Concepts – 10th Edition 22 Silberschatz, Galvin and Gagne ©2018
Stages in Demand Paging (Cont.)
6. While waiting, allocate the CPU to some other user
7. Receive an interrupt from the disk I/O subsystem (I/O completed)
8. Save the registers and process state for the other user
9. Determine that the interrupt was from the disk
10. Correct the page table and other tables to show page is now in memory
11. Wait for the CPU to be allocated to this process again
12. Restore the user registers, process state, and new page table, and then 
 resume the interrupted instruction
Worst Case

## Slide 23

Operating System Concepts – 10th Edition 23 Silberschatz, Galvin and Gagne ©2018
Performance of Demand Paging
▪ Three major activities required for a page fault
• Service the interrupt – careful coding could reduce the service time
• Read the page – lots of time
• Restart the process – again just a small amount of time
▪ Page Fault Rate 0  p  1
• if p = 0 no page faults 
• if p = 1, every reference is a fault
▪ Effective Access Time (EAT)
 EAT = (1 – p ) x memory access time + 
 p x ( page fault overhead + swap page out + swap page in )

## Slide 24

Operating System Concepts – 10th Edition 24 Silberschatz, Galvin and Gagne ©2018
Demand Paging Example
▪ Memory access time = 200 nanoseconds
▪ Average page-fault service time = 8 milliseconds
▪ EAT = (1 – p) x 200 + p (8 milliseconds) 
 = (1 – p) x 200 + p x 8,000,000 
 = 200 + p x 7,999,800
▪ If one access out of 1,000 causes a page fault, then
 EAT = 8.2 microseconds. 
 This is a slowdown by a factor of 40!!
▪ If we want the performance degradation < 10 percent
• 220 > 200 + 7,999,800 x p
20 > 7,999,800 x p
• p < .0000025
• < one page fault in every 400,000 memory accesses

## Slide 25

Operating System Concepts – 10th Edition 25 Silberschatz, Galvin and Gagne ©2018
Outline
▪ Background
▪ Demand Paging
▪ Page Replacement
▪ Allocation of Frames
▪ Thrashing
▪ Other Considerations

## Slide 26

Operating System Concepts – 10th Edition 26 Silberschatz, Galvin and Gagne ©2018
What If There Is No Free Frame?
▪ A system usually tries to increase the degree of multiprogramming
• To fully utilize the power of CPU
▪ All the memory could be used up by process pages
• over-allocation of memory
▪ Page replacement
• Find some page in memory, which is not really in use
• Page it out
• Swap the desired page into memory

## Slide 27

Operating System Concepts – 10th Edition 27 Silberschatz, Galvin and Gagne ©2018
Page Replacement
▪ Which page to be swapped out?
• We want a strategy causing the minimum number of page faults
• If the selection is bad, the swapped-out page may be required soon
 The same page may be brought into memory several times
▪ Use modify (dirty) bit to reduce overhead of page transfers
• If a page is modified in memory, its dirty bit will be set (to true)
• only modified pages need to be written back to disk

## Slide 28

Operating System Concepts – 10th Edition 28 Silberschatz, Galvin and Gagne ©2018
Need For Page Replacement

## Slide 29

Operating System Concepts – 10th Edition 29 Silberschatz, Galvin and Gagne ©2018
Basic Page Replacement
1. Find the location of the desired page on disk
2. Find a free frame:
• If there is a free frame, use it
• If there is no free frame
 use a page replacement algorithm to select a victim frame
• Write victim frame to disk if dirty
3. Bring the desired page into the (newly) free frame
• update the page and frame tables
4. Continue the process by restarting the instruction causing the trap
Potentially TWO page transfers for page fault – increasing EAT

## Slide 30

Operating System Concepts – 10th Edition 30 Silberschatz, Galvin and Gagne ©2018
Page Replacement

## Slide 31

Operating System Concepts – 10th Edition 31 Silberschatz, Galvin and Gagne ©2018
Evaluation of Page Replacement Algorithms
▪ Many page replacement algorithms were developed
▪ How to evaluate which algorithm is better?
• Reference string: a string of memory references
 Run page replacement algorithms on a reference string
 Compute the number of page faults on the string for each algorithm
 Compare the page fault numbers
• A reference string is a sequence of page numbers, not full addresses
 Repeated access to the same page does not cause a page fault
• Results depend on the number of frames available
▪ In all our examples, the reference string of referenced page numbers is 
 7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1

## Slide 32

Operating System Concepts – 10th Edition 32 Silberschatz, Galvin and Gagne ©2018
Page Faults vs. Number of Frames
In general, we expect a curve like this:

## Slide 33

Operating System Concepts – 10th Edition 33 Silberschatz, Galvin and Gagne ©2018
▪ Always replace the oldest page
• Reference string: 7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1
▪ The result can vary by different reference strings
• Consider another reference string: 1,2,3,4,1,2,5,1,2,3,4,5
• Adding more frames may cause more page faults!
 Belady’s Anomaly
▪ How to track ages of pages? 
• Just use a FIFO queue
First-In-First-Out (FIFO) Algorithm
15 page faults
3 frames 
available

## Slide 34

Operating System Concepts – 10th Edition 34 Silberschatz, Galvin and Gagne ©2018
FIFO Illustrating Belady’s Anomaly
reference string: 1,2,3,4,1,2,5,1,2,3,4,5

## Slide 35

Operating System Concepts – 10th Edition 35 Silberschatz, Galvin and Gagne ©2018
Optimal Algorithm
▪ Replace the page that will not be used for the longest period of time
• 9 is optimal for the same reference string
▪ How do you know the pages to be referenced in advance?
• Cannot read the future
▪ Used for measuring how well your algorithm performs

## Slide 36

Operating System Concepts – 10th Edition 36 Silberschatz, Galvin and Gagne ©2018
Least Recently Used (LRU) Algorithm
▪ Use past knowledge rather than future
▪ Replace page that has not been used in the most amount of time
▪ Associate time of last use with each page
▪ 12 page faults – better than FIFO but worse than OPT
▪ Generally good algorithm and frequently used
▪ But how to implement?

## Slide 37

Operating System Concepts – 10th Edition 37 Silberschatz, Galvin and Gagne ©2018
LRU Algorithm (Cont.)
▪ Counter implementation
• Every page entry has a counter
• Every time a page is referenced, copy the clock into the counter
• When a page to be replaced, look at the counters with the smallest value
 Need to search through all the pages
▪ LRU and OPT do not have Belady’s Anomaly

## Slide 38

Operating System Concepts – 10th Edition 38 Silberschatz, Galvin and Gagne ©2018
LRU Approximation Algorithms
▪ LRU needs special hardware and is still slow
▪ Reference bit
• Each page is associated a reference bit (initially set to 0)
• When page is referenced, its reference bit set to 1
• Replace any page with reference bit = 0 (if one exists)
 We do not know the order, however

## Slide 39

Operating System Concepts – 10th Edition 39 Silberschatz, Galvin and Gagne ©2018
LRU Approximation Algorithms (cont.)
▪ The FIFO algorithm, plus hardware-provided reference bit
• Clock replacement
▪ Second-chance algorithm
• When searching for a victim page
 If the reference bit of the page is 0
– replace it
 If the reference bit of the page is 1
– Set the reference bit to 0 and leave the page in memory
– Continue for the next page, subject to same rules

## Slide 40

Operating System Concepts – 10th Edition 40 Silberschatz, Galvin and Gagne ©2018
Second-chance Algorithm

## Slide 41

Operating System Concepts – 10th Edition 41 Silberschatz, Galvin and Gagne ©2018
Enhanced Second-Chance Algorithm
▪ Improve algorithm by using reference bit and modify bit (if available) 
in concert
▪ Take ordered pair (reference, modify):
• (0, 0) neither recently used not modified – best page to replace
• (0, 1) not recently used but modified – not quite as good, must 
write out before replacement
• (1, 0) recently used but clean – probably will be used again soon
• (1, 1) recently used and modified – probably will be used again 
soon and need to write out before replacement
▪ When page replacement called for, use the clock scheme but use the 
four classes replace page in lowest non-empty class
• Might need to search circular queue several times

## Slide 42

Operating System Concepts – 10th Edition 42 Silberschatz, Galvin and Gagne ©2018
Counting Algorithms
▪ Not common
▪ Maintain a counter recording the number of references so far for each page
▪ Lease Frequently Used (LFU) Algorithm:
• Replaces page with smallest count
▪ Most Frequently Used (MFU) Algorithm: 
• Based on the argument that the page with the smallest count was 
probably just brought in and has yet to be used

## Slide 43

Operating System Concepts – 10th Edition 43 Silberschatz, Galvin and Gagne ©2018
Page-Buffering Algorithms
▪ Keep a pool of free frames
• When a page fault occurs, a victim frame is selected
• The desired page is read into a free frame from the pool 
before the victim is written out
• When the victim is later written out, its frame is added to the 
free-frame pool

## Slide 44

Operating System Concepts – 10th Edition 44 Silberschatz, Galvin and Gagne ©2018
Applications and Page Replacement
▪ All of these algorithms have OS guessing about future page access
▪ Some applications have better knowledge, e.g., databases
▪ Memory intensive applications can cause double buffering
• OS keeps copy of page in memory as I/O buffer
• Application keeps page in memory for its own work
▪ Operating system can given direct access to the disk, getting out of 
the way of the applications
• Raw disk mode
▪ Bypasses buffering, locking, etc.

## Slide 45

Operating System Concepts – 10th Edition 45 Silberschatz, Galvin and Gagne ©2018
Outline
▪ Background
▪ Demand Paging
▪ Page Replacement
▪ Allocation of Frames
▪ Thrashing
▪ Other Considerations

## Slide 46

Operating System Concepts – 10th Edition 46 Silberschatz, Galvin and Gagne ©2018
Allocation of Frames
▪ Each process needs minimum number of frames
▪ Example: IBM 370 – 6 pages to handle SS MOVE instruction:
• instruction is 6 bytes, might span 2 pages
• 2 pages to handle from
• 2 pages to handle to
▪ Maximum of course is total frames in the system
▪ Two major allocation schemes
• fixed allocation
• priority allocation
▪ Many variations

## Slide 47

Operating System Concepts – 10th Edition 47 Silberschatz, Galvin and Gagne ©2018
Fixed Allocation
▪ Equal allocation – For example, if there are 100 frames (after 
allocating frames for the OS) and 5 processes, give each process 20 
frames
• Keep some as free frame buffer pool
▪ Proportional allocation – Allocate according to the size of process
• Dynamic as degree of multiprogramming, process sizes change
m
S
s
a p
m
S s
s p
i
i i
i
i i
= = 
=
= 
=
allocation for
total number of frames
size of process m = 64
s1 =10
s2=127
a1=
10
137
´ 62 » 4
a2=
127
137
´ 62 » 57

## Slide 48

Operating System Concepts – 10th Edition 48 Silberschatz, Galvin and Gagne ©2018
Global vs. Local Allocation
▪ Global replacement – process selects a replacement frame from the 
set of all frames; one process can take a frame from another
• But then process execution time can vary greatly
• But greater throughput so more common
▪ Local replacement – each process selects from only its own set of 
allocated frames
• More consistent per-process performance
• But possibly underutilized memory

## Slide 49

Operating System Concepts – 10th Edition 49 Silberschatz, Galvin and Gagne ©2018
▪ A strategy to implement global page-replacement policy 
▪ All memory requests are satisfied from the free-frame list, rather 
than waiting for the list to drop to zero before we begin selecting 
pages for replacement, 
▪ Page replacement is triggered by OS kernels, when the list falls 
below a certain threshold.
• Such kernel routines are often known as reapers
▪ This strategy attempts to ensure there is always sufficient free 
memory to satisfy new requests.
Reclaiming Pages

## Slide 50

Operating System Concepts – 10th Edition 50 Silberschatz, Galvin and Gagne ©2018
Reclaiming Pages Example

## Slide 51

Operating System Concepts – 10th Edition 51 Silberschatz, Galvin and Gagne ©2018
Outline
▪ Background
▪ Demand Paging
▪ Page Replacement
▪ Allocation of Frames
▪ Thrashing
▪ Other Considerations

## Slide 52

Operating System Concepts – 10th Edition 52 Silberschatz, Galvin and Gagne ©2018
Thrashing
▪ If a process does not have “enough” pages, the page-fault rate is very high
• Page fault occurs to a get page
• Replace existing frame
• But quickly need replaced frame back
• This leads to:
 Low CPU utilization
 Operating system thinking that it needs to increase the degree of 
multiprogramming
 Another process added to the system

## Slide 53

Operating System Concepts – 10th Edition 53 Silberschatz, Galvin and Gagne ©2018
Thrashing (Cont.)
▪ Thrashing. A process is busy swapping pages in and out

## Slide 54

Operating System Concepts – 10th Edition 54 Silberschatz, Galvin and Gagne ©2018
Demand Paging and Thrashing 
▪ Why does demand paging work?
 Locality model
• Process migrates from one locality to another
• Localities may overlap
▪ Why does thrashing occur?
  size of locality > total memory size
▪ Limit effects by using local or priority page replacement

## Slide 55

Operating System Concepts – 10th Edition 55 Silberschatz, Galvin and Gagne ©2018
Locality In A Memory-Reference Pattern

## Slide 56

Operating System Concepts – 10th Edition 56 Silberschatz, Galvin and Gagne ©2018
Working-Set Model
▪   working-set window  a fixed number of page references 
Example: 10,000 instructions
▪ WSSi(working set of Process Pi) = total number of pages referenced 
in the most recent  (varies in time)
• if  too small will not encompass entire locality
• if  too large will encompass several localities
• if  =   will encompass entire program
▪ D =  WSSi  total demand frames 
• Approximation of locality

## Slide 57

Operating System Concepts – 10th Edition 57 Silberschatz, Galvin and Gagne ©2018
Working-Set Model (Cont.)
▪ if D > m  Thrashing
▪ Policy if D > m, then suspend or swap out one of the 
processes

## Slide 58

Operating System Concepts – 10th Edition 58 Silberschatz, Galvin and Gagne ©2018
Keeping Track of the Working Set
▪ Approximate with interval timer + a reference bit
▪ Example:  = 10,000
• Timer interrupts after every 5000 time units
• Keep in memory 2 bits for each page
• Whenever a timer interrupts copy and sets the values of all 
reference bits to 0
• If one of the bits in memory = 1  page in working set
▪ Why is this not completely accurate?
▪ Improvement = 10 bits and interrupt every 1000 time units

## Slide 59

Operating System Concepts – 10th Edition 59 Silberschatz, Galvin and Gagne ©2018
Page-Fault Frequency
▪ More direct approach than WSS
▪ Establish “acceptable”page-fault frequency (PFF) rate and use 
local replacement policy
• If actual rate too low, process loses frame
• If actual rate too high, process gains frame

## Slide 60

Operating System Concepts – 10th Edition 60 Silberschatz, Galvin and Gagne ©2018
Working Sets and Page Fault Rates
▪ Direct relationship between working set of a process and its 
page-fault rate
▪ Working set changes over time
▪ Peaks and valleys over time

## Slide 61

Operating System Concepts – 10th Edition 61 Silberschatz, Galvin and Gagne ©2018
Outline
▪ Background
▪ Demand Paging
▪ Page Replacement
▪ Allocation of Frames
▪ Thrashing
▪ Other Considerations

## Slide 62

Operating System Concepts – 10th Edition 62 Silberschatz, Galvin and Gagne ©2018
Other Considerations
▪ Prepaging
▪ Page size
▪ TLB reach
▪ Inverted page table
▪ Program structure
▪ I/O interlock and page locking

## Slide 63

Operating System Concepts – 10th Edition 63 Silberschatz, Galvin and Gagne ©2018
Prepaging
▪ To reduce the large number of page faults that occurs at process startup
▪ Prepage all or some of the pages a process will need, before they are 
referenced
▪ But if prepaged pages are unused, I/O and memory was wasted
▪ Assume s pages are prepaged and α of the pages is used
• Is cost of s * α save pages faults > or < than the cost of prepaging
s * (1- α) unnecessary pages? 
• α near zero  prepaging loses

## Slide 64

Operating System Concepts – 10th Edition 64 Silberschatz, Galvin and Gagne ©2018
Page Size
▪ Sometimes OS designers have a choice
• Especially if running on custom-built CPU
▪ Page size selection must take into consideration:
• Fragmentation
• Page table size 
• Resolution
• I/O overhead
• Number of page faults
• Locality
• TLB size and effectiveness
▪ Always power of 2, usually in the range 212 (4,096 bytes) to 222
(4,194,304 bytes)
▪ On average, growing over time

## Slide 65

Operating System Concepts – 10th Edition 65 Silberschatz, Galvin and Gagne ©2018
TLB Reach 
▪ TLB Reach - The amount of memory accessible from the TLB
▪ TLB Reach = (TLB Size) X (Page Size)
▪ Ideally, the working set of each process is stored in the TLB
• Otherwise there is a high degree of page faults
▪ Increase the Page Size
• This may lead to an increase in fragmentation as not all 
applications require a large page size
▪ Provide Multiple Page Sizes
• This allows applications that require larger page sizes the 
opportunity to use them without an increase in fragmentation

## Slide 66

Operating System Concepts – 10th Edition 66 Silberschatz, Galvin and Gagne ©2018
Program Structure
▪ Program structure
• int[128,128] data;
• Each row is stored in one page 
• Program 1 
 for (j = 0; j <128; j++)
 for (i = 0; i < 128; i++)
 data[i,j] = 0;
 128 x 128 = 16,384 page faults 
• Program 2 
 for (i = 0; i < 128; i++)
 for (j = 0; j < 128; j++)
 data[i,j] = 0;
128 page faults

## Slide 67

Operating System Concepts – 10th Edition 67 Silberschatz, Galvin and Gagne ©2018
I/O interlock
▪ I/O Interlock – Pages must 
sometimes be locked into 
memory
▪ Consider I/O - Pages that are 
used for copying a file from a 
device must be locked from 
being selected for eviction by a 
page replacement algorithm
▪ Pinning of pages to lock into 
memory

## Slide 68

Operating System Concepts – 10th Edition Silberschatz, Galvin and Gagne ©2018
End of Topic


---

# Chapter 10: Deadlocks

## Slide 1

Operating System Concepts Silberschatz, Galvin and Gagne ©2018
ICT1012 － Operating Systems
Topic 10: Deadlocks
Instructor: Assoc. Prof. Shang-Wei LIN (林尚威)
InfoComm Technology (ICT) Cluster,
Singapore Institute of Technology (SIT)
shangwei.lin@singaporetech.edu.sg

## Slide 2

Operating System Concepts 2 Silberschatz, Galvin and Gagne ©2018
Deadlock in A Nutshell
Figure source: link

## Slide 3

Operating System Concepts 3 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 4

Operating System Concepts 4 Silberschatz, Galvin and Gagne ©2018
Learning Objectives
▪ Illustrate how deadlock can occur when mutex locks are used
▪ Define the four necessary conditions that characterize deadlock
▪ Identify a deadlock situation in a resource allocation graph
▪ Evaluate the four different approaches for preventing deadlocks
▪ Apply the banker’s algorithm for deadlock avoidance
▪ Apply the deadlock detection algorithm
▪ Evaluate approaches for recovering from deadlock

## Slide 5

Operating System Concepts 5 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 6

Operating System Concepts 6 Silberschatz, Galvin and Gagne ©2018
System Model
▪ System consists of resources
▪ Resource types R1, R2, . . ., Rm
• CPU cycles, memory space, I/O devices
▪ Each resource type Ri has Wiinstances.
▪ Each process utilizes a resource as follows:
• request 
• use 
• release

## Slide 7

Operating System Concepts 7 Silberschatz, Galvin and Gagne ©2018
Deadlock with Semaphores
▪ Data:
• A semaphore S1initialized to 1
• A semaphore S2initialized to 1
▪ Two threads T1 and T2
▪ T1: 
 wait(s1)
 wait(s2)
▪ T2: 
 wait(s2)
 wait(s1)

## Slide 8

Operating System Concepts 8 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 9

Operating System Concepts 9 Silberschatz, Galvin and Gagne ©2018
Deadlock Characterization
▪ Mutual exclusion
• only one thread at a time can use a resource
▪ Hold and wait
• a thread holding at least one resource is waiting to acquire 
additional resources held by other threads
▪ No preemption
• a resource can be released only voluntarily by the thread holding it, 
after that thread has completed its task
▪ Circular wait among a set {T0, T1, …, Tn } of waiting threads 
• T0 is waiting for a resource that is held by T1
• T1is waiting for a resource that is held by T2, 
• …
• Tn–1is waiting for a resource that is held by Tn
• Tnis waiting for a resource that is held by T0
Deadlock can arise, if four conditions hold simultaneously

## Slide 10

Operating System Concepts 10 Silberschatz, Galvin and Gagne ©2018
Resource-Allocation Graph
▪ V is partitioned into two types:
• T = {T1, T2, …, Tn }
 the set consisting of all the threads in the system
 Each thread Ti is denoted by a circle
• R = {R1, R2, …, Rm }
 the set consisting of all resource types in the system
 Each type Rjis denoted by a rectangle
▪ E is partitioned into two types:
• request edge – directed edge Ti → Rj
• assignment edge – directed edge Rj → Ti
A set of vertices V and a set of edges E.

## Slide 11

Operating System Concepts 11 Silberschatz, Galvin and Gagne ©2018
Resource Allocation Graph Example
▪ One instance of R1
▪ Two instances of R2
▪ One instance of R3
▪ Three instance of R4
▪ T1 holds one instance of R2 and is 
waiting for an instance of R1
▪ T2 holds one instance of R1, one 
instance of R2, and is waiting for an 
instance of R3
▪ T3is holds one instance of R3

## Slide 12

Operating System Concepts 12 Silberschatz, Galvin and Gagne ©2018
Resource Allocation Graph with a Deadlock

## Slide 13

Operating System Concepts 13 Silberschatz, Galvin and Gagne ©2018
Graph with a Cycle But no Deadlock

## Slide 14

Operating System Concepts 14 Silberschatz, Galvin and Gagne ©2018
Basic Facts
▪ If graph contains no cycles  no deadlock
▪ If graph contains a cycle 
• if only one instance per resource type, then deadlock
• if several instances per resource type, possibility of deadlock

## Slide 15

Operating System Concepts 15 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 16

Operating System Concepts 16 Silberschatz, Galvin and Gagne ©2018
Methods for Handling Deadlocks
▪ Proactive approach
• Ensure that the system will never enter a deadlock state
 Deadlock prevention
 Deadlock avoidance
▪ Passive approach
• Allow the system to enter a deadlock state and then recover
• Ignore the problem and pretend that deadlocks never occur

## Slide 17

Operating System Concepts 17 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 18

Operating System Concepts 18 Silberschatz, Galvin and Gagne ©2018
Deadlock Prevention
▪ Mutual Exclusion
• sharable resources (e.g., read-only files) are not mutual exclusive
• Using sharable resources can prevent deadlocks
 However, some resources are intrinsically non-sharable, e.g., mutex
▪ Hold and Wait
• When a thread requests a resource, it does not hold any other resources
• Low resource utilization
• starvation possible
Invalidate one of the four necessary conditions for deadlock:

## Slide 19

Operating System Concepts 19 Silberschatz, Galvin and Gagne ©2018
Deadlock Prevention (Cont.)
▪ No Preemption
• If a process, holding some resources, requests another resource that 
cannot be immediately allocated to it, then all resources currently being 
held are released (preempted)
• Preempted resources are added to the list of resources for which the 
thread is waiting
• Thread will be restarted only when it can regain its old resources, as 
well as the new ones that it is requesting
▪ Circular Wait
• Impose a total ordering of all resource types
• Each thread requests resources in an increasing order
Invalidate one of the four necessary conditions for deadlock:

## Slide 20

Operating System Concepts 20 Silberschatz, Galvin and Gagne ©2018
Circular Wait
▪ Invalidating the circular wait condition is most common
▪ Simply assign each resource (i.e., mutex locks) a unique number
▪ Resources must be acquired in order
▪ If:
first_mutex = 1
second_mutex = 5
code for thread_two could not be 
written like this:

## Slide 21

Operating System Concepts 21 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 22

Operating System Concepts 22 Silberschatz, Galvin and Gagne ©2018
Deadlock Avoidance
▪ Each thread declares the maximum number of resources of each type 
that it may need
▪ The deadlock-avoidance algorithm dynamically examines the resourceallocation state to ensure that there can never be a circular-wait
condition
▪ Resource-allocation state is defined by the number of available and 
allocated resources, and the maximum demands of the processes
Require that the system has some additional a priori information available

## Slide 23

Operating System Concepts 23 Silberschatz, Galvin and Gagne ©2018
Safe State
▪ When a thread requests an available resource, system must decide 
if immediate allocation leaves the system in a safe state
▪ System is in safe state if there exists a sequence <T1 , T2 , …, Tn > 
of ALL the threads in the systems such that for each Ti , the 
resources that Ti can still request can be satisfied by currently 
available resources plus resources held by all the Tj, with j < i
▪ That is:
• If Tiresource needs are not immediately available, then Ti can 
wait until all Tj have finished
• When Tjis finished, Ti can obtain needed resources, execute, 
return allocated resources, and terminate
• When Titerminates, Ti +1 can obtain its needed resources, and 
so on

## Slide 24

Operating System Concepts 24 Silberschatz, Galvin and Gagne ©2018
Safe State (cont.)
The system has 12 magnetic tape drives.
There are 3 processes (P0, P1 and P2) in the system.
SAFE!! Safe sequence: < P1 , P0 , P2 >

## Slide 25

Operating System Concepts 25 Silberschatz, Galvin and Gagne ©2018
Unsafe State
The system has 12 magnetic tape drives.
There are 3 processes (P0, P1 and P2) in the system.
UNSAFE!! No safe sequence exists!
3

## Slide 26

Operating System Concepts 26 Silberschatz, Galvin and Gagne ©2018
Basic Facts
▪ If a system is in safe state  no deadlocks
▪ If a system is in unsafe state  possibility of deadlock
▪ Avoidance  ensure that a system will never enter an unsafe state.

## Slide 27

Operating System Concepts 27 Silberschatz, Galvin and Gagne ©2018
Safe, Unsafe, Deadlock State

## Slide 28

Operating System Concepts 28 Silberschatz, Galvin and Gagne ©2018
Avoidance Algorithms
▪ Single instance of a resource type
• Use a resource-allocation graph
▪ Multiple instances of a resource type
• Use the Banker’s Algorithm

## Slide 29

Operating System Concepts 29 Silberschatz, Galvin and Gagne ©2018
Resource-Allocation Graph Scheme
▪ Claim edge Ti → Rj indicates that process Ti may request resource Rj
• represented by a dashed line
▪ Claim edge converts to request edge when a thread requests a resource
▪ Request edge converted to an assignment edge when the resource is 
allocated to the thread
▪ When a resource is released by a thread, assignment edge reconverts to a 
claim edge
▪ Resources must be claimed a priori in the system

## Slide 30

Operating System Concepts 30 Silberschatz, Galvin and Gagne ©2018
Resource-Allocation Graph

## Slide 31

Operating System Concepts 31 Silberschatz, Galvin and Gagne ©2018
Unsafe State In Resource-Allocation Graph

## Slide 32

Operating System Concepts 32 Silberschatz, Galvin and Gagne ©2018
Resource-Allocation Graph Algorithm
▪ Suppose that thread Ti requests a resource Rj
▪ The request can be granted only if 
• converting the request edge to an assignment edge does NOT
result in the formation of a cycle in the resource allocation graph

## Slide 33

Operating System Concepts 33 Silberschatz, Galvin and Gagne ©2018
Banker’s Algorithm
▪ Multiple instances of resources
▪ Each thread must a priori claim maximum use
▪ When a thread requests a resource, it may have to wait 
▪ When a thread gets all its resources it must return them in a finite 
amount of time

## Slide 34

Operating System Concepts 34 Silberschatz, Galvin and Gagne ©2018
Data Structures for the Banker’s Algorithm 
▪ Available: A vector of length m. 
• If Available[j] = k, there are k instances of resource type Rj available
▪ Max: A (n x m) matrix. 
• If Max[i,j] = k, then process Ti may request at most k instances of resource type Rj
▪ Allocation: A (n x m) matrix. 
• If Allocation[i,j] = k, then Tiis currently allocated k instances of Rj
▪ Need: A (n x m) matrix. 
• If Need[i,j] = k, then Ti may need k more instances of Rj to complete its task
Need[i,j] = Max[i,j] – Allocation[i,j]
n: number of processes
m: number of resources types

## Slide 35

Operating System Concepts 35 Silberschatz, Galvin and Gagne ©2018
Safety Algorithm
1. Let Work and Finish be vectors of length m and n, respectively. 
Initialize:
Work = Available
Finish[i] = false for i = 0, 1, …, n- 1
2. Find an i such that both: 
 (a) Finish[i] = false
 (b) Needi  Work
 If no such i exists, go to step 4
3. Work = Work + Allocationi
Finish[i] = true
 go to step 2
4. If Finish[i] == true for all i, then the system is in a safe state

## Slide 36

Operating System Concepts 36 Silberschatz, Galvin and Gagne ©2018
Resource-Request Algorithm for Process Pi
Requesti = request vector for process Ti. If Requesti[j] = k then 
process Ti wants k instances of resource type Rj
1. If Requesti  Needi go to step 2. Otherwise, raise error 
condition, since process has exceeded its maximum claim
2. If Requesti  Available, go to step 3. Otherwise Ti must wait, 
since resources are not available
3. Pretend to allocate requested resources to Ti by modifying the 
state as follows:
Available = Available – Requesti;
Allocationi = Allocationi + Requesti;
Needi = Needi – Requesti;
• If safe  the resources are allocated to Ti
• If unsafe  Ti must wait, and the old resource-allocation state 
is restored

## Slide 37

Operating System Concepts 37 Silberschatz, Galvin and Gagne ©2018
Example of Banker’s Algorithm
▪ 5 threads T0 through T4; 
 3 resource types:
 A (10 instances), B (5instances), and C (7 instances)
▪ Snapshot at time T0:
Allocation Max Available
A B C A B C A B C
T0 0 1 0 7 5 3 3 3 2
T1 2 0 0 3 2 2 
T2 3 0 2 9 0 2
T3 2 1 1 2 2 2
T4 0 0 2 4 3 3

## Slide 38

Operating System Concepts 38 Silberschatz, Galvin and Gagne ©2018
Example (Cont.)
▪ The content of the matrix Need is defined to be Max – Allocation
Need
A B C
T0 7 4 3 
T1 1 2 2 
T2 6 0 0 
T3 0 1 1
T4 4 3 1 
▪ The system is in a safe state since the sequence < T1, T3, T4, T2, T0> 
satisfies safety criteria

## Slide 39

Operating System Concepts 39 Silberschatz, Galvin and Gagne ©2018
Example: P1 Request (1,0,2)
▪ Check that Request  Available (that is, (1,0,2)  (3,3,2)  true
Allocation Need Available
A B C A B C A B C 
T0 0 1 0 7 4 3 2 3 0
T1 3 0 2 0 2 0 
T2 3 0 2 6 0 0 
T3 2 1 1 0 1 1
T4 0 0 2 4 3 1 
▪ Executing safety algorithm shows that sequence < T1, T3, T4, T0, T2> 
satisfies safety requirement
▪ Can request for (3,3,0) by T4 be granted?
▪ Can request for (0,2,0) by T0 be granted?

## Slide 40

Operating System Concepts 40 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 41

Operating System Concepts 41 Silberschatz, Galvin and Gagne ©2018
Deadlock Detection
▪ Allow system to enter deadlock state 
▪ Detection algorithm
▪ Recovery scheme

## Slide 42

Operating System Concepts 42 Silberschatz, Galvin and Gagne ©2018
Single Instance of Each Resource Type
▪ Maintain wait-for graph
• Nodes are threads
• Ti → Tj if Tiis waiting for Tj
▪ Periodically invoke an algorithm that searches for a cycle in the graph. 
If there is a cycle, there exists a deadlock
▪ An algorithm to detect a cycle in a graph requires an order of n2
operations, where n is the number of vertices in the graph

## Slide 43

Operating System Concepts 43 Silberschatz, Galvin and Gagne ©2018
Resource-Allocation Graph and Wait-for Graph
Resource-Allocation Graph Corresponding wait-for graph

## Slide 44

Operating System Concepts 44 Silberschatz, Galvin and Gagne ©2018
Several Instances of a Resource Type
▪ Available: A vector of length m indicates the number of available 
resources of each type
▪ Allocation: An n x m matrix defines the number of resources of each 
type currently allocated to each thread.
▪ Request: An n x m matrix indicates the current request of each 
thread. If Request [i][j] = k, then thread Tiis requesting k more 
instances of resource type Rj.

## Slide 45

Operating System Concepts 45 Silberschatz, Galvin and Gagne ©2018
Detection Algorithm
1. Let Work and Finish be vectors of length m and n, respectively 
Initialize:
a) Work = Available
b) For i = 1,2, …, n, if Allocationi  0, then 
Finish[i] = false; otherwise, Finish[i] = true
2. Find an index i such that both:
a) Finish[i] == false
b) Requesti  Work
If no such i exists, go to step 4

## Slide 46

Operating System Concepts 46 Silberschatz, Galvin and Gagne ©2018
Detection Algorithm (Cont.)
3. Work = Work + Allocationi
 Finish[i] = true
 go to step 2
4. If Finish[i] == false, for some i, 1  i  n, then the system is in 
deadlock state. Moreover, if Finish[i] == false, then Tiis 
deadlocked
Algorithm requires an order of O(m x n2) operations to detect 
whether the system is in deadlocked state

## Slide 47

Operating System Concepts 47 Silberschatz, Galvin and Gagne ©2018
Example of Detection Algorithm
▪ Five threads T0through T4; three resource types 
A (7 instances), B (2 instances), and C (6 instances)
▪ Snapshot at time T0:
Allocation Request Available
A B C A B C A B C
 T0 0 1 0 0 0 0 0 0 0
 T1 2 0 0 2 0 2
 T2 3 0 3 0 0 0 
 T3 2 1 1 1 0 0 
 T4 0 0 2 0 0 2
▪ Sequence <T0, T2, T3, T1, T4> will result in Finish[i] = true for all i

## Slide 48

Operating System Concepts 48 Silberschatz, Galvin and Gagne ©2018
Example (Cont.)
▪ T2requests an additional instance of type C
Request
A B C
T0 0 0 0
T1 2 0 2
T2 0 0 1
T3 1 0 0 
T4 0 0 2
▪ State of system?
• Can reclaim resources held by thread T0, but insufficient resources 
to fulfill other processes; requests
• Deadlock exists, consisting of processes T1, T2, T3, and T4

## Slide 49

Operating System Concepts 49 Silberschatz, Galvin and Gagne ©2018
Detection-Algorithm Usage
▪ When, and how often, to invoke depends on:
• How often a deadlock is likely to occur?
• How many processes will need to be rolled back?
 one for each disjoint cycle
▪ If detection algorithm is invoked arbitrarily, there may be many cycles in 
the resource graph and so we would not be able to tell which of the 
many deadlocked threads “caused” the deadlock.

## Slide 50

Operating System Concepts 50 Silberschatz, Galvin and Gagne ©2018
Outline
▪ System Model
▪ Deadlock Characterization
▪ Methods for Handling Deadlocks
▪ Deadlock Prevention
▪ Deadlock Avoidance
▪ Deadlock Detection 
▪ Recovery from Deadlock

## Slide 51

Operating System Concepts 51 Silberschatz, Galvin and Gagne ©2018
Recovery from Deadlock: Process Termination
▪ Abort all deadlocked threads
▪ Abort one process at a time until the deadlock cycle is eliminated
▪ In which order should we choose to abort?
1. Priority of the thread
2. How long has the thread computed, and how much longer to 
completion
3. Resources that the thread has used
4. Resources that the thread needs to complete
5. How many threads will need to be terminated
6. Is the thread interactive or batch?

## Slide 52

Operating System Concepts 52 Silberschatz, Galvin and Gagne ©2018
Recovery from Deadlock: Resource Preemption
▪ Selecting a victim – minimize cost
▪ Rollback – return to some safe state, restart the thread for 
that state
▪ Starvation – same thread may always be picked as victim, 
include number of rollback in cost factor

## Slide 53

Operating System Concepts 53 Silberschatz, Galvin and Gagne ©2018
Module and Teaching Feedback
1. Complete both module and teaching feedback.
2. Please share constructive feedback in the free 
text sections.
3. Academic Staff will not be able to identify the 
student. All feedback received are anonymous.
4. Students’ grades will not be affected as the 
feedback results will only be shared with the 
academic staff after the release of exam results.

## Slide 54

Operating System Concepts Silberschatz, Galvin and Gagne ©2018
End of Topic
