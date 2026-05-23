# INF1002 Programming Fundamentals — Complete Notes

> Singapore Institute of Technology · INF1002 Programming Fundamentals  
> This document consolidates all lecture slides and code examples from the module.

---

## Table of Contents

### Python (Weeks 1–6)
1. [Module Introduction](#1-module-introduction)
2. [Python Basic I — Variables, Types, I/O](#2-python-basic-i)
3. [Python Basic II — Control Flow](#3-python-basic-ii)
4. [Advanced Data Structures — String, List, Tuple, Dict](#4-advanced-data-structures)
5. [Functions, File I/O, Scope, Modules](#5-functions-file-io-scope-modules)
6. [Recursion and Docstrings](#6-recursion-and-docstrings)
7. [Lambda Expressions](#7-lambda-expressions)

### C Programming (Weeks 8–12)
8. [Introduction to C](#8-introduction-to-c)
9. [Functions, Arrays, and Strings in C](#9-functions-arrays-and-strings-in-c)
10. [Pointers](#10-pointers)
11. [Dynamic Memory Allocation and Linked Lists](#11-dynamic-memory-allocation-and-linked-lists)
12. [File I/O in C](#12-file-io-in-c)

### Code Examples
13. [All C Code Examples](#13-all-c-code-examples)

---

---

# Part 1: Python Programming

## 1. Module Introduction

### Slide 2: Outline

• Module introduction
• Python introduction
• Some concept of software engineering
• Python basic I
• Some concept of programming

### Slide 3: Survey

• To know your background
• https://xsite.singaporetech.edu.sg/d2l/home/144699
• Assessments  Surveys Student Programming Experience

### Slide 4: Assessments

• Quiz
• Close book
• Online MCQ
• Understanding of the labs/lectures
Python 
Group 
Project 25%
Python Lab 
5%
Python Quiz 
(Week 6) 
20%
C Group 
Project 25%
C Lab 5%
C Quiz 
(Week 13) 
20%

### Slide 5: Labs

• Programming exercises
• Warmup questions
• No need to submit
• Three questions per Lab
• Auto-graded

### Slide 6: Labs

• Groups and instructors
• You can find in xsite
• Class Activities  Classlist  View By Sections
• Friday

### Slide 7: Projects

• Group Project – 5 people per group
• Form groups freely inside your Lab groups
• If you are in LAB-P1, find your friends inside LAB-P1
• Class Activities  Groups
• If you haven't found a group by 7 Sep, the system will randomly allocate one for you
• If you find that your group does not have enough people, please let me know
• Example project ideas and rubrics are ready
• Timeline

### Slide 8: Projects

• A complex programming exercise
• To demonstrate your ability to write Python programs by solving a small 
practical problem
• Data Processing, Data Analysis, Data Visualization
• Able to write well-designed, modular, and efficient code that is easy to maintain and 
optimized for performance
• Application of Development Framework, modules
• To understand and to overcome the challenges you encounter in a project
• Differences between the initial plan and actual progress
• Effective communication, conflict resolution, and collaborative problem-solving

### Slide 9: Projects

• A complex programming exercise
• To practice academic writing
• Title, Abstract, Introduction, Related work, Method, Experiments, Results, 
Conclusion, References
• Present findings objectively
• Innovation
• You must use advanced tools like ChatGPT, co-polite etc.
• You create something new. (bonus)

### Slide 10: Projects

• About ChatGPT
• ChatGPT does not have a soul; you should have one
• To learn 1+1, do not use a calculator
• To finish your lab assignment, please do not use it
• To solve word problems, it's an efficient tool
• To finish your project, please use it to enhance your 
efficiency and the project quality
• Check the generated code line by line

### Slide 11: Equipment

• For class
• Have a Google account
• https://colab.research.google.com/
• Laptop is preferred
• iPad is also fine 
• For project / lab
• Laptop is strongly recommended

### Slide 12: Course Aims

• Fundamental skills in programming (Python & C)
• Improved problem-solving ability
• Don't worry even you have never been exposed to programming before
• I hope you learn and contribute something even you are already an expert
• Required a lot of effort of self-learning

### Slide 13: Classroom Expectations

• It is a disciplinary offence to copy another student’s work or to 
allow another student to copy your work.
• Do not lie to yourself.
• You must use ChatGPT, but please use it appropriately.

### Slide 14: Best Wishes

• Focus on improving your skills rather than worrying about one or 
two points.
• You can try to tell your interviewer that you could have scored two more 
points in programming basic module.
• Focus on your main problem
• Make you life easier

### Slide 15: Review

• Survey
• Labs, a project, a quiz
• https://colab.research.google.com with a google account

### Slide 16: Schedule 1st Half

Week Topics Labs
1 Module Introduction & Python Basic I No lab
2 Python Basic II Lab1: Python Basic
3 Advanced data structures: list, tuples, 
dictionary & iteration (for, while)& Files I/O
Lab2: Loops and Advanced Data 
Structures
4 Functional abstraction Lab3: Functions
5 Introduction to recursion Lab4: Recursion
6 Python Test
Explain the test questions
High-order functions
Lab5: High-order functions
Python Project Submission
7 Recess Week

### Slide 17: Schedule 2nd Half

Week Topics Labs
8 Introduction to C
User defined data types
Lab W8: Introducing VSE, Tic-Tac-Toe 
Template
9 Functions
Introduction to Arrays and Pointers
Lab W9: Using Arrays
10 More on Arrays and Pointers
Lab W10&W11: Arrays &
User defined data type
11 Strings & Files
12 Introduction to Data Structures
Submit Assignment 2
Lab W12: Using Files and
advanced data structures
13 Lecture Test 2

### Slide 18: Module Road Map

Real World Problems / Project Management Problems/ Innovation / Self-study
Variables & 
Types & 
Operators
Control 
Flow
Advanced 
Data 
Structures 
& I/O
Functional
abstraction
Recursion
Higher 
order 
function

### Slide 19: • Learn the basics

• Practice more
• Think more about the logic, 
instead of repeating
• Read books
• Read codes
• Fast is slow
• Slow is fast
https://www.rocketacademy.co/software-engineering/software-engineering-career-path

### Slide 20: How to success in programming

Practice!
Practice!!! Practice!!!!
Practice!!

### Slide 21: Suggestions from industry experts

• Data Structure and Algorithms
• https://leetcode.com/
• Real world projects, Internship
• Find a good piece of open-source software in a specific direction 
and develop a deep understanding of it.
• APP Development
• Web Server
• Database
• Middleware
• Cloud Computing
• …

### Slide 22: Suggestions from industry experts

• Data Structure and Algorithms
• https://leetcode.com/
• Real world projects, Internship
• Find a good piece of open-source software in a specific direction 
and develop a deep understanding of it.
• APP Development
• Web Server
• Database
• Middleware
• Cloud Computing
• …

### Slide 23: Story of Exemptions

• 7 out of 101 applications are approved
Using C, we were told to develop a product that can tackle 
an everyday problem. We made a medicine dispenser 
which reminds and dispenses medicine when the set time 
is met. This project was made by programming a PIC18 
microcontroller using concepts of C programming, OOP 
and solid programming knowledge. My project can be 
found here: 
https://github.com/WolfverusWasTaken/PIC18-MedDispenser/tree/main/CDIO_PIC_Project
Using python and tensorflow, we developed an image 
classification model for our final project. We were 
taught on the various python programming techniques 
on how to make AI models with python. Here is my 
code in my github repo: 
https://github.com/WolfverusWasTaken/Simple-FoodImage-Classifier

### Slide 24: Story of Exemptions

• 7 out of 101 applications are approved
Using C, we were told to develop a product that can tackle 
an everyday problem. We made a medicine dispenser 
which reminds and dispenses medicine when the set time 
is met. This project was made by programming a PIC18 
microcontroller using concepts of C programming, OOP 
and solid programming knowledge. My project can be 
found here: 
https://github.com/WolfverusWasTaken/PIC18-MedDispenser/tree/main/CDIO_PIC_Project
Using python and tensorflow, we developed an image 
classification model for our final project. We were 
taught on the various python programming techniques 
on how to make AI models with python. Here is my 
code in my github repo: 
https://github.com/WolfverusWasTaken/Simple-FoodImage-Classifier

### Slide 25: Story of Exemptions

• 7 out of 101 applications are approved
Using C, we were told to develop a product that can tackle 
an everyday problem. We made a medicine dispenser 
which reminds and dispenses medicine when the set time 
is met. This project was made by programming a PIC18 
microcontroller using concepts of C programming, OOP 
and solid programming knowledge. My project can be 
found here: 
https://github.com/WolfverusWasTaken/PIC18-MedDispenser/tree/main/CDIO_PIC_Project
Using python and tensorflow, we developed an image 
classification model for our final project. We were 
taught on the various python programming techniques 
on how to make AI models with python. Here is my 
code in my github repo: 
https://github.com/WolfverusWasTaken/Simple-FoodImage-Classifier
Some friends just throw a transcript with C 
grade in my face

### Slide 26: Story of Exemptions

• Read the instructions carefully
• Thinking from the other person's perspective
• If you have some basic programming knowledge, the lecture 
should be easy for you.
• Contribute more to the team project
• It does not mean you do all the work.

### Slide 27: Lecturers

• Associate Professor
• InfoComm Technology
• Email: zhengchen.zhang@singaporetech.edu.sg
• Workstation: E1-L7-7 
• Consultation hour: by appointment
• Research interest
• Text-to-Speech
• Natural Language Processing
Dr. ZHANG Zhengchen

### Slide 28: Lecturers

• Associate Professor
• InfoComm Technology
• Email: Frank.Guan@singaporetech.edu.sg
• Workstation: E1-L7-76
• Consultation hour: by appointment
• Research interest
• Augmented Reality
• Virtual Reality
• Artificial Intelligence
• Computational Imaging
• 3D Visualization
• Computer Graphics
Dr. Frank GUAN Yunqing

### Slide 29: • We are here to help you

• Feel free to email me
• zhengchen.zhang@singaporet
ech.edu.sg 
• Wish you have a good start 
• Programming
• Your university life

### Slide 30: Review

• Assessment
• Quiz
• Lab
• Project
• Module Road Map
• Variables & Types
• Control Flow
• Advance Data Types: List, Dictionary etc.
• Recursion
• High Order Functions

### Slide 31: Review

• Think about your future
• Software Engineering
• Operating System
• Internet of Things
• …
• Do not lie to yourself.
• Exemption Story
• Read the instructions carefully
• Thinking from the other person's perspective
• Self-study is very important
• We are here to help you

### Slide 32: Reference

• https://www.tutorialspoint.com/python/index.htm

---

## 2. Python Basic I

*Topics: Why Python, first programs, variables, data types, arithmetic operators, type casting.*

### Slide 2: Outline

• Module introduction
• Python introduction
• Some concept of software engineering
• Python basic I
• Some concept of programming

### Slide 3: Python

First Steps in Python

### Slide 4: Why Python?

• Simple
• Powerful
• Community
• Ecosystem
• Application in Machine Learning

### Slide 5: TIOBE Programming Community Index: an index of evaluating language popularity

https://www.tiobe.com/tiobe-index/

### Slide 6: Why is Python So Popular?

• Simple
• Powerful
• Ecosystem
• Community
• Cross-platform
• Application in Machine Learning
• Beautiful is better than ugly. 
• Explicit is better than implicit. 
• Simple is better than complex. 
• Complex is better than complicated. 
• Flat is better than nested. 
• Sparse is better than dense. 
• Readability counts. 
• Special cases aren't special enough to break the rules. 
• Although practicality beats purity. 
• Errors should never pass silently. 
• Unless explicitly silenced. 
• In the face of ambiguity, refuse the temptation to guess. 
• There should be one-- and preferably only one --obvious way to do it. 
• Although that way may not be obvious at first unless you're Dutch. 
• Now is better than never. 
• Although never is often better than *right* now.
• If the implementation is hard to explain, it's a bad idea. 
• If the implementation is easy to explain, it may be a good idea. 
• Namespaces are one honking great idea -- let's do more of those!
The Zen of Python

### Slide 7: Your First Python Program

• https://colab.research.google.com/
• File  New notebook in Drive 
• Rename, Save, …

### Slide 8: Your First Python Program

• Write one program to print "Hello World!" in Python
• print ("Hello World!")
• Or
• print ('Hello World!')
• print()
• to print something to the screen
• Using either " " or ' ' around what you want to print
• Further Reading
• The arguments of print() function

### Slide 9: Knowing Python

• Single Quote and Double Quote can generally be used 
interchangeably.
• print('Hello, World! ')
• print("Hello, World! ")
• print('He said, "Python is awesome! "')
• print("It's a beautiful day! ")

### Slide 10: Knowing Python

• What if I want to print
• It's a "beautiful" day.
\n Newline
\t Tab
\\ backslash
• Use a backslash ('\') to escape quotes inside the string
print('It\'s a "beautiful" day! ')
print("It's a \"beautiful\" day! ")
• Escape characters

### Slide 11: Knowing Python

• Raw strings
• Prefixing a string with r or R makes it a raw string, where backslashes are 
not treated as escape characters
• print(r'it\n1\t2')
• print('it\n1\t2')
• Print(r"C:\Users\Name")
• Print("C:\Users\Name")

### Slide 12: Knowing Python

• The language is case sensitive
• print ≠ Print ≠ PRINT
• Indention matters
• Some development tools would make automatic indention
• Be careful about indention
• In nested if, for, while

### Slide 13: Write comments

• Comments 
• People may read your code
• Guide your thinking
• In a single line
• Using the symbol #
• For multiple lines
• Using three quotation marks ''' '''
• Docstring

### Slide 14: Write comments

• Comments
• People may read your code
• Guide your thinking
• In a single line
• Using the symbol #
• For multiple lines
• Using three quotation marks ''' '''
• Docstring

### Slide 15: Python 2 and Python 3

• We use Python 3 in this module
• Print statement
• Python 2: print "abc ", print 'abc'
• Python 3: print("abc")
• Libraries
• Some libraries only work on P2 e.g. PyImage
• P3 is increasing the third party module support (especially those machine/deep learning libraries)
• Others
• Unicode and Strings
• Division with integers
• Input() is now safe to use
• More difference can be found at: 
https://www.interviewbit.com/blog/difference-between-python-2-and-3/

### Slide 16: Review

• Hello World in python
• Quotation marks
• Escape Characters
• Backslash
• Comments
• Versions of Python

### Slide 17: Outline

• Module introduction
• Python Introduction
• Some concept of software engineering
• Python basic I
• Some concept of programming

### Slide 18: Programming and Problem Solving

• A problem is defined by its inputs and the desired property of the 
output.
Evans D. Introduction to computing: explorations in language, logic, and machines[M]. CreateSpace Independent Publishing Platform, 2011.

### Slide 19: How to solve a problem

Pólya G. How to solve it: A new aspect of mathematical method[M]. Princeton university press, 2014, first published in 1945.

### Slide 20: How to solve a problem

### Slide 21: Software Engineering

• Software Development Methodologies
Agile Development in Software Engineering
https://www.geeksforgeeks.org/what-is-agile-methodology/

### Slide 22: Know the problem first

• Requirement Analysis
• Let's store files into a database
• What kind of files
• File size, numbers
• Will modify or not
• Will read them frequently
• …

### Slide 23: Design

• Design Pattern
• Reusable solutions in software 
development that addresses 
common design problems, 
promoting code 
maintainability, scalability, 
and reusability.

### Slide 24: Implementing - Debug

• Logic Error
• When the code is executed, it produces incorrect results
• Known as a bug
• Visual Studio Code
• Run: F5
• Breakpoint: pause the execution of a program at a specific line of code
• Step over: F10
• Step into: F11

### Slide 25: Testing

• The act of checking whether software satisfies expectations.
• Automated testing
• Levels
• Unit testing
• Integration testing
• System testing
• Test Cases

### Slide 26: Deployment

• Take a website as an example
• Develop on Local Machine
• You create the website and test it on your laptop.
• Test on Staging Server 
• You upload it to a staging server to simulate the production environment and catch 
any bugs.
• Deploy to Production Server 
• Once everything works perfectly, you upload it to a production server. 
• Now, anyone can visit your website using its URL.
• Monitor 
• After deployment, you regularly check the website to ensure it’s running smoothly 
and fix any issues visitors report.

### Slide 27: Deployment

• Key Concepts:
• Continuous Integration/Continuous Deployment (CI/CD) 
• A set of practices that involve automatically testing and deploying code changes to 
ensure rapid and reliable updates.
• Version Control 
• Tools like Git help manage changes to the code and keep track of different versions.
• Rollback 
• The ability to revert to a previous version if the new deployment causes issues.
• Large scale and complex real world problems

### Slide 28: Looking back

• Monitor your products
• Get feedback
• Evaluate your methods/solutions
• With numbers
• Evaluation
• A formal end of this step
• A guide to your next step

### Slide 29: Review

• Programming and problem solving
• Understand the problem
• Plan
• Execute the plan
• Lookback
• Programming and software engineering
• Plan
• Requirement Analysis
• Design
• Implementation
• Testing
• Deployment
• Maintenance
• Iteration…

### Slide 30: Outline

• Module introduction
• Python Introduction
• Some concept of software engineering
• Python basic I
• Some concept of programming

### Slide 31: Variables and Assignment

Statements

### Slide 32: Module Road Map

Real World Problems / Project Management Problems/ Innovation / Self-study
Variables & 
Types & 
Operators
Selection &
Iteration
Advanced 
Data 
Structures
Functional
abstraction
Recursion
Higher 
order 
function

### Slide 33: Variables and Assignment Statements

• Variables
• <variable name > = expression
• print('Hello, World! ')
• print("Hello, World! ")
• print('He said, "Python is awesome! "')
• print("It's a beautiful day! ")
• print('Taylor')
• firstName = 'Taylor'
• print(firstName)

### Slide 34: Variables and Assignment Statements

• Variables
• <variable name > = expression
• A variable is a reserved memory location used to store values

### Slide 35: Variables and Assignment Statements

• Variables
• <variable name > = expression
• A name
• We can use the name in following expressions
• Variable references
• Values can be reset to new ones
• Assignment statement
Assignment 
statements
Variable references
Reset a variable

### Slide 36: Variable Naming Rules

• Variables must start with a letter or an underscore _
• Subsequent characters can be letters, numbers, or underscores
• Variable names are case-sensitive
• Keywords cannot be used as variable names:
• Examples of keywords: if, else, for, while, class, def, return, try, except, etc.
• Which one is valid?
• _myvar, Var1, 1var, -var, return, good

### Slide 37: Variable Naming Rules

• Variables must start with a letter or an underscore _
• Subsequent characters can be letters, numbers, or underscores
• Variable names are case-sensitive
• Keywords cannot be used as variable names:
• Examples of keywords: if, else, for, while, class, def, return, try, except, etc.
• Which one is valid?
• _myvar, Var1, 1var, -var, return, good

### Slide 38: Variable Naming Rules

• Use lowercase letters and underscores for variable names (snake_case):
• Example: my_variable, user_name, total_sum
• Constants (values that do not change) are usually written in all uppercase 
with underscores (UPPERCASE_WITH_UNDERSCORES):
• Example: PI = 3.14159, MAX_LIMIT = 100
• Use meaningful variable names:
• Choose names that clearly describe the variable’s purpose, e.g., total_sum instead of ts.
• Avoid single-character variable names, unless in loops (e.g., i, j, k):

### Slide 39: Variable Naming Rules

• Follow the PEP 8 style guide:
• PEP 8 is the Python community's style guide, recommending consistent and readable 
naming practices.
• https://peps.python.org/pep-0008/
• Python 3 supports Unicode characters, allowing variable names in non-Latin 
scripts like Chinese or Japanese, but it's best to maintain consistency and 
readability.

### Slide 40: Variables and Assignment Statements

• Variables
• <variable name > = expression
• A variable is a reserved memory location used to store values
• How can I know the memory address of a variable?
• id()

### Slide 41: Multiple Assignment

### Slide 42: Multiple Assignment

• Practice
• How can we swap the values of two variables?

### Slide 43: Multiple Assignment

Elegant 
• Practice
• How can we swap the values of two variables?

### Slide 44: Variable types

• Variables
• Name
• Id
• Type
• How to know a variable's type?
• type()

### Slide 45: Variable types

Type Samples
int 8,12,1024
float 2.3, 3.1415926
bool True, False
str 'Hello, World! ', '3.1415926'
None None
List
Tuple
Set
Dictionary
byte

### Slide 46: Type Casting and Dynamic Typing

• Type casting • Dynamic Typing

### Slide 47: Type Casting

• Numbers to string
• String to numbers
• Numeric precision adjustment

### Slide 48: Type Casting

• Numbers to string
• String to numbers
• Numeric precision adjustment

### Slide 49: Type Casting

• Numbers to string
• String to numbers
• Numeric precision adjustment
• Int and float
Why -100, not -101?
Round vs Truncation 
Why 70, not 71?

### Slide 50: Type Casting

### Slide 51: Arithmetic Operators

Operator Name Example
+ Addition
- Subtraction
* Multiplication
/ Division 10/0 ZeroDivisionError
4/2 integer or float?
// Floor Division 13.9//2 = 6.0
% Modulus 11%3 = 2; 11.0%3.0 = 2.0
** Exponent 2**4 = 16
+= Augmented Addition Operator a+=1 equals to a = a+1
-=
*=
…

### Slide 52: Review

• Variables
• Id
• Name
• Type
• Type Casting
• Arithmetic operators

### Slide 53: Outline

• Module introduction
• Python Introduction
• Some concept of software engineering
• Python basic 1
• Some concept of programming

### Slide 54: Command Line and IDE

• Command line - Python Shell
• Interactive programming Python shell
• Show the results immediately after the statements
• Cons: 
• Difficult to manage in large projects
• Difficult to refactor

### Slide 55: Command Line and IDE

• Integrated Development Environments
• A programming environment
• A code editor
• A compiler
• A debugger
• A graphical user interface (GUI) builder

### Slide 56: Command Line and IDE

• https://www.w3schools.com/python/
• https://colab.research.google.com/
• We will use this one in class
• Save your results easily
• Use the auto-complete function properly

### Slide 57: Jupyter Notebook

• https://jupyter.org/
• https://jupyter.org/try-jupyter/lab/

### Slide 58: What is programming?

• Computer programming or coding is the composition of 
sequences of instructions, called programs, that computers can 
follow to perform tasks. 
https://en.wikipedia.org/wiki/Computer_programming
High Level Language
0s and 1s
?

### Slide 59: From high level code to 0 and 1 (Compiled Language)

High Level Programming Languages
Compiler
Assembly Language
Assembler
Machine Code

### Slide 60: Bytecode

• https://godbolt.org/
• Further Reading
• Interpreted Languages
• Compiled Languages

### Slide 61: Bytecode

### Slide 62: Compiler and Interpreter

• Compiler
• Translates the entire source code of a program into machine code before execution.
• Generates an executable file that can be run independently of the source code.
• Usually faster execution after compilation because the translation is done once.
• Error detection happens at compile-time, making debugging easier before running the 
program.
• Examples: GCC (GNU Compiler Collection), MSVC (Microsoft Visual C++), Clang.
• Interpreter
• Translates and executes the source code line by line at runtime.
• Does not produce an independent executable file; the source code must be present 
during execution.
• Slower execution because translation happens every time the program is run.
• Immediate execution allows for easier testing and debugging of small code snippets.
• Examples: Python interpreter, Ruby interpreter, JavaScript engines (like V8).

### Slide 63: CPython

• CPython is an interpreter responsible for reading, parsing, and 
executing Python code. 
• Translate high level code to bytecode
• Execute the bytecode

### Slide 64: Review

• Command Line and IDE
• High Level Code
• Bytecode / Assembly Language
• Machine Code

### Slide 65: Assignment

• Assignment
• Install the Python 3
• Try pip install
• Conda / Miniconda
• Install Conda
• Create an environment
• Install the IDE that you like to use (i.e., Pycharm , Visual Studio Code)
• Create a simple program
• Try run, debug, breakpoint, check the variant value
• First lab from week 2

### Slide 66: Good Programming Practices

Martin R C. Clean code: a handbook of agile software craftsmanship[M]. Pearson Education, 2009.

---

## 3. Python Basic II

*Topics: Control flow — if/elif/else, while, for loops, input/output, f-strings.*

### Slide 2: Review

• Variables
• Id
• Name
• Type and Type Casting
• Arithmetic operators

### Slide 3: Assignment

• Assignment
• Install the Python 3
• Try pip install
• Conda / Miniconda
• Install Conda
• Create an environment
• Install the IDE that you like to use (i.e., Pycharm , Visual Studio Code)
• Create a simple program
• Try run, debug, breakpoint, check the variant value
• First lab from week 2

### Slide 4: Outline

• Control Flow
• Conditional Control
• if statement
• Loop Control
• while
• for
• Input/Output from console
• String format
• Project
https://www.researchgate.net/figure/Flow-chart-diagram-Online-e-commerce-shopping-web-app_fig1_347169962

### Slide 5: Definition of Control Flow

• In computer science, control flow (or flow of control) is the order 
in which individual statements, instructions or function calls of an 
imperative program are executed or evaluated. 
• Imperative programming
• https://en.wikipedia.org/wiki/Imperative_programming
• Declarative programming
• https://en.wikipedia.org/wiki/Declarative_programming
https://en.wikipedia.org/wiki/Computer_programming

### Slide 6: Main Control Flow Structures

• Sequential Control
• Conditional Control
• Loop Control
• Function Call
• Exception Handling

### Slide 7: Sequential Control

• The program executes instructions in the order they are written, 
from top to bottom.

### Slide 8: Conditional Control

• We would like the program to perform different steps depending 
on different conditions
• Decision-making ability
• My Five "No-Do's" at Work
• If I know how to do it, I won't do it, because I won't learn anything new.
• If I don't know how to do it, I won't do it, because I don't know how.
• If it's urgent, I won't do it, because rushing can lead to mistakes.
• If it's not urgent, I won't do it, because if it's not urgent, why should I do it now?
• If I don't want to do it, I won't do it, because if I don't want to, how can I do it?
• Otherwise, I will do it.

### Slide 9: Conditional Control

• The program makes decisions based on the truth value of 
conditions, determining which path to take.
• Structures: if, if-else, if-elif-else
• Boolean variable type
• True or False
• Boolean expression
• An expression that evaluates to either True or False.

### Slide 10: Boolean Expression

• Logical Operator
• and 
• or
• not
• Identity Operator
• is
• is not
a b a and b
True True True
True False False
False True False
False False False
a b a or b
True True True
True False True
False True True
False False False

### Slide 11: Boolean Expression

• Logical Operator
• and 
• or
• not
• Identity Operator
• is
• a is b
• id(a)==id(b)
• a is None
• is not
a not a
True False
False True
mark = 90
print(f'{mark} mark>85: {mark>85}')
print(f'{mark} mark<100: {mark<100}')
print(f'{mark} mark>85 and mark<100: 
{mark>85 and mark<100}')
print('==='*10)
print(f'{mark} mark<85: {mark<85}')
print(f'{mark} mark<100: {mark<100}')
print(f'{mark} mark<85 or mark<100: 
{mark<85 or mark<100}')
print('==='*10)
print(f'{mark} mark>85: {mark>85}')
print(f'{mark} not mark>85: {not mark>85}')

### Slide 12: if

if expr:
 statement(s)

### Slide 13: if-else

if expr:
 statement(s)
else:
 statement(s)

### Slide 14: if-elif-else

if expr1:
 statement(s)
elif expr2:
 statement(s)
else:
 statement(s)

### Slide 15: if-elif-…-else

if expr1:
 statement(s)
elif expr2:
 statement(s)
elif expr3:
 statement(s)
else:
 statement(s)
drink = "Latte"
price = 0.0
if drink == "Americano":
print("You chose Americano.")
print("That will be $3.50.")
price = 3.50
elif drink == "Latte":
print("You chose Latte.")
print("That will be $4.00.")
price = 4.00
elif drink == "Tea":
print("You chose Tea.")
print("That will be $2.50.")
price = 2.50
elif drink == "Hot Chocolate":
print("You chose Hot Chocolate.")
print("That will be $3.00.")
price = 3.00
else:
print("Sorry, we don't have that option.")

### Slide 16: Details of if Statement

• The Colon (:)
• The colon is required at the end of the if and else lines.
• It indicates that a block of code will follow.
• Indentation:
• Python uses indentation to define the scope of the code block.
• Consistent indentation is crucial for the correct execution of the program.
• Typically, four spaces or one tab is used for indentation.

### Slide 17: Nested if Statement

• Be careful of indentations
drink = "Latte"
size = "Large"
if drink == "Latte":
if size == "Large":
print("You chose a Large Latte.")
print("That will be $5.00.")
else:
print("You chose a Small Latte.")
print("That will be $4.00.")
else:
print("Sorry, we only have Latte available.")

### Slide 18: match-case Statement

match variable_name:
 case 'pattern 1' : 
 statement1
 case 'pattern 2' : 
 statement2
 ...
 case 'pattern n' : 
 statementn
drink = "Latte"
price = 0.0
if drink == "Americano":
print("You chose Americano.")
print("That will be $3.50.")
price = 3.50
elif drink == "Latte":
print("You chose Latte.")
print("That will be $4.00.")
price = 4.00
elif drink == "Tea":
print("You chose Tea.")
print("That will be $2.50.")
price = 2.50
elif drink == "Hot Chocolate":
print("You chose Hot Chocolate.")
print("That will be $3.00.")
price = 3.00
else:
print("Sorry, we don't have that option.")

### Slide 19: Review

• Logical Operators
• and
• or
• not
• Identity Operators
• is
• is not
• if elif elif elif else
• match-case

### Slide 20: Outline

• Control Flow
• Conditional Control
• if statement
• Loop Control
• while
• for
• Input/Output from console
• String format
https://www.researchgate.net/figure/Flow-chart-diagram-Online-e-commerce-shopping-web-app_fig1_347169962

### Slide 21: Loop Control

• The program repeatedly executes a block of code as long as a 
specified condition is met.
• Structures: for, while
• A person does 20 push-ups every day, 
• He stops once he has completed all 20 push-ups.

### Slide 22: while Loop

• Sequential Control
• Start
• Push-up 1 
• Push-up 2
• ... 
• Push-up 20 
• End
• loop
• Pseudocode:
• pushup_count = 0
• IF pushup_count < 20
• Push-up
• INCREMENT pushup_count by 1
• ELSE
• Stop
• IF pushup_count < 20
• Push-up
• INCREMENT pushup_count by 1
• ELSE
• Stop
• …

### Slide 23: while Loop

The program repeatedly executes a block of code as long as a specified condition is met.
• loop
• Pseudocode:
• pushup_count = 0
• IF pushup_count < 20
• Push-up
• INCREMENT pushup_count by 1
• ELSE
• Stop
• IF pushup_count < 20
• Push-up
• INCREMENT pushup_count by 1
• ELSE
• Stop
• …

### Slide 24: while Loop

while expression:
 statement1
 statement2
• Expression
• Boolean Expression
• Whether to stay within the loop
• Statements
• Do something
• Will change the result of the Expression

### Slide 25: Infinite Loops

• What happens if you forget pushup_coutnt += 1?
• Dead Loop
• The most common reason for a program ‘hanging’
• To quit program execution: restart, Ctrl + C
• When Infinite Loop is useful?
while True:
…

### Slide 26: The loop may not be executed

• If the condition is False to begin with

### Slide 27: Review

• Loop
• The program 
• repeatedly executes a block of code 
• as long as a specified condition is met.
while expression:
 statement1
 statement2
• Infinite Loops

### Slide 28: for Loop

for iterating_var in sequence:
 statements
• Define pushup_count inside for
• Sequence
• range(20)

### Slide 29: for Loop

• The for loop in Python provides the ability to loop over the items of 
any sequence, such as a list, tuple or a string. 
• It performs the same action on each item of the sequence.
• range() function
• Generate a list of numbers
• Generally used to iterate over with for loops
• range(stop)
• Stop: number of integers to generate starting from 0
• 0,1,2,3,…,19
https://www.tutorialspoint.com/python/python_for_loops.htm

### Slide 30: for Loop

• The for loop in Python provides the ability to loop over the items of 
any sequence, such as a list, tuple or a string. 
• String as a sequence

### Slide 31: Compare for and while

while boolean_expression:
Statements
• Condition met or not
for iterating_var in sequence:
Statements
• Go through the sequence
• List, tuple, string, range
• Iterable:
• Whenever we say an iterable in 
Python, it means a sequence data 
type (for example, a list).

### Slide 32: for Loop

• range(stop)
• range(start, stop)
• range(start, stop, step)
• Start: starting num of the sequence
• Stop: generate num up to, but not including this num
• Step: difference between each num in the sequence

### Slide 33: for Loop

for iterating_var in sequence:
 statements
• You may use the iterating_var in the statements
• Scenario:
• John starts walking from his house.
• He walks for a total of 1 hour (60 minutes).
• His speed increases with each minute
• In the 1st minute, he walks at 1 meter per minute, 
• In the 2nd minute, he walks at 2 meters per minute, and so on.
• Calculate the total distance he walks.
• Ans: 1830 meters

### Slide 34: for Loop

• Scenario 2:
• John starts walking from his house.
• He walks for a total of 1 hour (60 minutes).
• His speed increases with every 2 minute
• In the 1st minute, he walks at 1 meter per minute, 
• In the 2nd minute, he walks at 1 meters per minute, 
• In the 3rd minute, he walks at 3 meter per minute, 
• In the 4th minute, he walks at 3 meters per minute, 
• and so on.
• Calculate the total distance he walks.
• Ans: 1800 meters

### Slide 35: Dead loop

• loop over the items of a 
sequence
• How can we write a dead loop 
in 'for'?

### Slide 36: Dead loop

### Slide 37: Break Statement

• Stop the loop when some condition 
is satisfied
• Can be used in both Python while 
and for loops

### Slide 38: Continue Statement

• Skips the remaining statements 
in the current loop and starts 
the next iteration.
• Can be used in both Python 
while and for loops
• Example:
• I don't do exercise on Sunday

### Slide 39: Review

• Loop over the items of a sequence
for iterating_var in sequence:
Statements
• Break statement
• Continue statement

### Slide 40: Learning a programming language

• Understand the basic vocabulary
• Keywords
• Words built into language
• Also called reserved words
• Syntax
• Rules of language
• Includes:
• Spelling
• Punctuation
• Grammar
• Each programming language has own unique syntax and structure

### Slide 41: Syntax Examples

Python VisualBasic

### Slide 42: Syntax Examples

C

### Slide 43: Syntax Error

• A mistake in a program
• Violates the language rules
• Compiler checks for syntax errors
• Code cannot run unless fixed

### Slide 44: Logic Error

• The syntax is correct
• However, when the code is executed, it produces incorrect results
• Also known as a bug

### Slide 45: Review

• Some basic concept
• Syntax Error
• Logic Error

### Slide 46: Input and Output

• Program needs users to provide some data
• Two main different input manners
• Input from the Keyboard
• Input from files

### Slide 47: Input from the keyboard

https://ubuntu.com/tutorials/command-line-for-beginners#4-creating-folders-and-files

### Slide 48: input()

• input ()
• Read one line from standard input
• Return it as a string
• We can give a prompt text
• which will appear before the cursor when you run the code.

### Slide 49: Type casting

• input ()
• Read one line from 
standard input
• Return it as a string
• You need to convert the 
data type if necessary

### Slide 50: Python2

• raw_input()
• input()

### Slide 51: Output to the screen

• Print one variable’s value
• print (“something or null” + variable_name)
• Print one string variable ( e.g. name)
• print (“this is one string” + name)
• Print one int variable ( e.g. age)
• print (age)
• print (“Your age is: ” + str(age))
• Print one float variable (e.g. salary)
• print (salary)
• print (“Your age is: ” + str(salary))

### Slide 52: Neat and organized print format

### Slide 53: Looks better?

Alignment problem
How to align them?

### Slide 54: Data Formatting: f-string

• Print variables

### Slide 55: f-string

• Print expression

### Slide 56: f-string

• Self-debugging

### Slide 57: f-string

• Alignment
• {variable:>width}
• > right-aligned
• Width: the total number of 
characters

### Slide 58: f-string

• Alignment
• {variable:>width}
• {variable:<width}
• {variable:^width}
• > right-aligned
• < left-aligned
• ^ center-aligned
• Width: the total number of characters

### Slide 59: f-string

• Precision handling of floats
• {variable:>[width].[precision]f}
• Width: total number of digits
• Precision: decimal digits
• Do not forget f
• What will happen if we lose f?

### Slide 60: Data Formatting

• Format strings
• %<width>s
• Format integers
• %<width>d

### Slide 61: Data Formatting

• Format a floating point number
• %<width>.<precision>f
• Width: total length of the number, including the decimal point
• Precision: number of decimal places
• If width < real_length, Print real_length

### Slide 62: Review

• Input from screen
• Output to screen
• f-string
• Alignment
• String width control
• Decimal precision control

### Slide 63: Git

• Git and GitHub are different
• Version Control
• Forget what has been changed two weeks ago
• How to combine many people's work
• Go to https://git-scm.com/downloads

### Slide 64: Git

1. Go to the command line
• Windows + R, input cmd
2. git config --global user.name "Mona Lisa"
• If your name has a whitespace, then the double quotes are necessary
3. git config --global user.email "your.email@example.com"
• Not for logging into any website
• To record who submit the codes

### Slide 65: Git

1. Go to a folder
• cd d:\
• cd ~
2. git init project1
• Will create a folder named project1
3. cd project1
4. Make a txt file: file1.txt
• Write something and save and close
5. git add file1.txt
6. git commit –m "my first commit"

### Slide 66: Git

• Create a public repository on GitHub
• git clone <repository_url>
• https://github.com/ZhengchenZhang/python-lecture2.git
• git branch
• git checkout –b main
• Modify the files
• git add *.py
• git commit –m "my homework"
• git remote add origin <repository_url>
• git push origin main

### Slide 67: Secure Shell Protocol (SSH)

1. ssh-keygen -t rsa -b 4096 -C your_email@example.com
2. Type enter many times
3. C:\users\<user_name>\.ssh\id_rsa.pub
4. Open it using a text editor, copy the content
5. Go to https://github.com/settings/keys
6. Click New SSH key
7. Give any name, and paste the content
8. Get the ssh address of your repository
9. Repeat the comments in the last page

---

## 4. Advanced Data Structures

*Topics: Strings, Lists, Tuples, Dictionaries, Sets, Files I/O in Python.*

### Slide 2: Review

• if elif elif else
• Boolean expression
• while loop
• for loop
• f-string
• Alignment
• Width of a string
• Precision of a float number

### Slide 3: Outline

• Advanced Data Types
• String
• List
• Tuple
• Dictionary
• Files I/O
Type Samples
int 8,12,1024
float 2.3, 3.1415926
bool True, False
str 'Hello, World! ',
'3.1415926'
None None
List
Tuple
Set
Dictionary
byte

### Slide 4: string

• An immutable sequence of Unicode characters.
• Immutable
• Sequence
• Unicode
• Immutable vs mutable
• Mutable: The value of the object can be changed, such as lists, 
dictionaries, and sets.
• Immutable: The value of the object cannot be changed once it is created, 
such as strings, tuples, and integers.

### Slide 5: string

• An immutable sequence of Unicode characters.
• Immutable
• Sequence
• Unicode
• Further Reading : Unicode • Unicode, formally The Unicode Standard is a text encoding standard maintained by the Unicode 
Consortium designed to support the use of text in all of the world's writing systems that can be 
digitized. 1
1. https://en.wikipedia.org/wiki/Unicode
2. https://home.unicode.org/

### Slide 6: string concatenation and repetition

• Strings are identified by single or double quotation marks:
• 'Mike'
• "Something interesting"
• '73'
• The operator + is used for string concatenation:
• 'Taylor' + 'Swift' evaluates to 'TaylorSwift'
• 'Taylor' + ' '+ 'Swift' evaluates to 'Taylor Swift'
• Operator *

### Slide 7: string comparation

• What is the ASCII code of 'a' and 'b'
• Which is larger?
• 'a' > 'b' or 'a' < 'b' ?
• 'aa' > 'ab' or 'aa' < 'ab' ?
• 'aba' > 'ab' or 'aba' < 'ab' ?
• 'a0' > 'a9' or 'a0' < 'a9' ?

### Slide 8: ASCII Table

### Slide 9: string - a sequence of characters

• Sequence
• Membership Operator
• in
• not in

### Slide 10: string slicing

• Index of characters in a string
• First character is indexed with 0.
• Last character is indexed with len(s)-1
• A character is a string with length 1
• s[index]
• s[-1]
• s[start : end]
• end: exclusive

### Slide 11: string slicing

• Index of characters in a string
• s[start : end : step]

### Slide 12: string built-in methods

Function Description
find(str, beg=0, end=len(string)) Determine if str occurs in string or in a substring of string if 
starting index beg and ending index end are given returns index 
if found and -1 otherwise.
isdigit() Returns true if string contains only digits and false otherwise.
lower() Converts all uppercase letters in string to lowercase.
upper() Converts lowercase letters in string to uppercase.
split(str="", num=string.count(str)) Splits string according to delimiter str (space if not provided) 
and returns list of substrings; split into at most num substrings 
if given.
endswith(suffix, beg=0, end=len(string)) Determines if string or a substring of string (if starting index beg 
and ending index end are given) ends with suffix; returns true if 
so and false otherwise.
…

### Slide 13: String built-in functions

Name Description
len(string) Gives the total length of the string.
max(string) Returns character from the string with max value.
min(string) Returns character from the string with min value.
https://www.tutorialspoint.com/python/python_strings.htm

### Slide 14: Function and Method

• Function
• len(string)
• Method
• string.lower()
• Further reading
• Ask ChatGPT
• Concept of function in python (we will learn this in next lecture)
• Concept of Class/Object in Object-Oriented Programming

### Slide 15: Review

• string
• immutable and mutable
• Concatenation and repetition
• Comparison
• String as a sequence
• Membership operator
• Slicing
• Bulit-in functions and methods

### Slide 16: List

• A Python list is a sequence of comma separated items, enclosed 
in square brackets [ ]. 
• Name1 = 'Saul'
• Name2 = 'David'
• Name3 = 'Solomon'
• Name4 = 'Rehoboam'
• Names = ['Saul', 'David', 'Solomon', 'Rehoboam']
• The items in a Python list need not be of the same data type.

### Slide 17: List - Index in a sequence

• my_list[0]
• my_list[-1]
• Membership operator
• 'abc' in my_list
• Slicing
• my_list[start : end : step]

### Slide 18: List

• Update:
• my_list[1] = 'efg'
• Can string do this?
• Add
• my_list.append('hij') 
• my_list.insert(0,'klmn')
• Delete
• del my_list[-2]
• my_list.remove('abc')
• Length
• len(my_list)

### Slide 19: List

• Built-in functions
Name Description
cmp(list1, list2) Compares elements of both lists.
len(list) Gives the total length of the list.
max(list) Returns item from the list with max value.
min(list) Returns item from the list with min value.
list(seq) Converts a tuple into list.
https://www.tutorialspoint.com/python/python_lists.htm

### Slide 20: List – Concatenation and Repetition

• Concatenation +
• [1, 2, 3]+[4, 5, 6]
• Repetition *
• [1, 2, 3]*4
• ['a', 'b', 'c']*3

### Slide 21: List

• Practice
• Copy one list to a new list
• Set the first item of the new list to be something else
• Print the old and new lists

### Slide 22: Deep Copy

• A deep copy creates a new object and recursively adds copies of 
nested objects found in the original.
• Changes to the copied object do not affect the original object.

### Slide 23: Immutable vs Mutable

• Mutable: The value of the object can be changed, such as lists, dictionaries, and sets.
• Immutable: The value of the object cannot be changed once it is created, such as strings, tuples, and integers.
• The python id() function is used to return a unique identification value of the object stored in the memory. 1
1. https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/python-id/

### Slide 24: Shallow Copy

• A shallow copy creates a new object but inserts references into it 
to the objects found in the original.
• Changes to the copied object can affect the original object if the 
copied object contains references to mutable objects.
• A reference is a variable that points to or "references" a location in 
memory where an object is stored.
• Zhengchen (list2) and Prof. Zhang (list1)

### Slide 25: Shallow Copy

[1] [2] 3 4
Pointer1 Pointer2 Pointer3 Pointer4 … List1
An array of pointers
Pointer1 Pointer2 Pointer3 Pointer4 … List3
A new array of pointers
A shallow copy creates a new object but inserts references into it to the objects found in the original.

### Slide 26: Shallow Copy

Changes to the copied object can affect the original object if 
the copied object contains references to mutable objects.
list3[0][0] = 100
print('new values')
print(list1)
print(list3)
print('id of the first item')
print(id(list1[0]))
print(id(list3[0]))
Print('\n')
#==============================
list3[0] = [200]
print('new values')
print(list1)
print(list3)
print('id of the first item')
print(id(list1[0]))
print(id(list3[0]))

### Slide 27: Review

• Operations on a sequence
• Assignment, Deep Copy and Shallow Copy
• Sometimes you change the values of a list unexpectedly
• Immutable and Mutable

### Slide 28: Tuples

• A sequence of immutable Python objects
• Difference between tuple and list
• Tuples use parentheses () and lists use square brackets []
• The tuples can not be changed

### Slide 29: Dictionary

• A word and its explanation
• In Python, a dictionary is a built-in data 
type that stores data in key-value pairs.2
• Each key in a dictionary is unique and 
maps to a value. 
• Example:
1. https://www.wikihow.com/Use-a-Dictionary
2. https://tutorialspoint.com/python/python_dictionary.htm
ID Name Score
001 John 100+
002 John 80
…

### Slide 30: Dictionary

• Each key is separated from its value by a colon (:)
• The items are separated by commas
• The whole thing is enclosed in curly braces
• An empty dictionary is {}

### Slide 31: Dictionary

• Keys are unique within a dictionary
• Values may not be unique
• Values can be of any type
• Strings, numbers, tuples, lists, dictionaries etc.
• Keys must be of an immutable data type
• Strings, numbers, or tuples

### Slide 32: Dictionary

• Access
• value = students[key]
• Update and Add
• students[key] = value
• If a key already exists, the old value will 
be overwritten by the new value.
• If it is a new key, the key and value pair 
will be added to the dictionary
• Delete
• del students[key]
• students.clear()

### Slide 33: Built-in Functions with Dictionaries

Name Description
len(dict) Give the length of the dictionary, which is the number of items in the 
dictionary
str(dict) Produce a printable string representation of a dictionary

### Slide 34: Python Dictionary Methods

Name Description
dictionary.keys() Returns list of dictionary keys
dictionary.values() Returns list of dictionary values
dictionary.items() Returns list of dictionary items: (key, value) tuple pairs
dictionary.update(dictionary2) Adds dictionary2's key-values pairs to the first dictionary

### Slide 35: For loop

• Practice
• Create a dictionary, which contains student scores
• Key is the student number
• Value is the score
• Print the sorted scores

### Slide 36: Review

• Key-value pairs
• Keys are unique
• Add, update, delete
• for key, value in my_dict.items():
• keys(), values()

### Slide 37: List Comprehension

• Generate a new list by applying an expression to each item in an 
existing iterable (like a list or range) in a single line of code. 
• Create a list containing the first ten perfect squares

### Slide 38: List Comprehension

• new_list = [expression for member in iterable]
• expression: the list member itself or any valid expression returns a value
• i**2
• member: the object or value in the list or iterable
• i
• iterable: a list, set, sequence, generator or any other object that can 
return its elements one at a time
• list(range(10)) : [0,1,2,3,4,5,6,7,8,9]

### Slide 39: List Comprehension

• Using conditional logic
• new_list= [expression for member in iterable (if conditional)]
Readability

### Slide 40: Integrated application

### Slide 41: Review

• new_list= [expression for member in iterable (if conditional)]
• Efficiency sometimes comes at the cost of readability

### Slide 42: Files I/O

• Why do we need a file?
• Data used in the program is stored in the memory
• Still can find the data after reboot the computer/restart the program
• Keep the data permanent
• File operations
Open a file Process the 
data/file Save the file
Load data from 
disk to 
memory
Process the 
data
Write data to 
disk

### Slide 43: Open a file

• Python’s built-in open() function
• Create one file object that can be utilized
• Syntax:
• file_object= open(file_name[, access_mode] [, encoding])

### Slide 44: Object Oriented Programming

• Class
• A blueprint for creating objects
• Defines a set of attributes and methods
• Groups data and behavior together in a reusable and organized way
• Object
• An instance of a class
• Key Characteristics
• Attributes (or Properties): Variables that store data specific to the object
• Name, Age
• Methods (or Functions): Functions that define the behavior of the object
• Walk, Speak

### Slide 45: open()

• File_name
• a string value that contains the name of the file that you want to access
• Access_mode
• the mode in which the file to be opened, i.e., read, write, append, etc.
• Optional, the default model is read(r)
• Encoding
• Default value depends on your operating system
• utf-8
• Remember the Unicode thing?

### Slide 46: mode

• Open('student_info.txt', mode='r')
Mode Description
r Opens a file for reading only. This is the default mode.
r+ Opens a file for both reading and writing. 
w Opens a file for writing only. Overwrites the file if the file exists. If the file 
does not exist, creates a new file for writing.
w+ Opens a file for both writing and reading. Overwrites the existing file if the 
file exists. If the file does not exist, creates a new file for reading and 
writing.
a Opens a file for appending. If the file does not exist, it creates a new file for 
writing.
b rb, wb, ab, etc. Opens the file in binary mode.
…

### Slide 47: Practice

• Create a new file on Google Colab
• Double click 'student.txt' and edit it, and save it (Ctrl + S)

### Slide 48: File pointer

• Indicate the current focused 
position of the file
• Description of mode 'r'
• Opens a file for reading only. 
• The file pointer is placed at the 
beginning of the file.

### Slide 49: Read a file

• read(size)
• returns the specified number of bytes from the 
file. 
• size
• Indicates the number of bytes to read from the 
file. 
• Optional, default is -1 which means the whole file
• If omitted or set to a negative value, the method 
reads until the end of the file.
• readline(size) • returns one line from the file
• If size < len(aline)
• If size > len(aline)
• readlines(hint) • returns a list containing each line in the file as 
a list item.
• If returned number of bytes > hint, then stop

### Slide 50: Update data

• Take note of the \n at 
the end of the line
• Try to make the lines 
aligned using f-string

### Slide 51: Write data to a file

• write(str)
• This is the String to be written in the file.
• writelines(sequence)
• This is the Sequence of the strings.
Open a file Process the 
data/file Save the file
Load data from 
disk to 
memory
Process the 
data
Write data to 
disk

### Slide 52: With open() as file:

• The with statement is a context manager
• Automatically handles file opening and closing
• Ensures the file is properly closed even if an exception occurs
• Restricts the variable scope to the with block

### Slide 53: The 'with' statement

• Advantages of the with statement:
• More concise
• Automatic resource management, avoiding resource leaks
• Safer, more readable code
• Restricts the variable scope, reducing potential bugs
• Disadvantages of the traditional method:
• Requires explicit file closing
• Error-prone, can lead to resource leaks
• Variable remains in scope, which may cause unexpected issues

### Slide 54: Review

• Read data from a file
• Operations on the data
• Write to a file
• File Pointer
• 'with' statement

### Slide 55: Topics to Carry Over to Lectures 4 and 5

• Return value of a function
• Returns one line of the file 
• Bytes Data Type
• ASCII, Byte, bit, Unicode
• Beyond txt file: image, audio, video, npy

### Slide 56: Review

• String, List
• sequence
• Immutable and mutable
• Tuple
• Shallow Copy and Deep Copy
• Dictionary
• File I/O

---

## 5. Functions, File I/O, Scope, Modules

*Topics: Defining functions, default args, *args/**kwargs, scope, modules, higher-order functions.*

### Slide 2: Early Learning Insight Survey (ELIS)

• To find out how you have been coping with 
your modules since the start of the trimester
• From 16 Sep 2024 to 29 Sep 2024, 9 PM
• To collect your learning needs early
• Access the survey via
1. Individualized link in the email sent to all
2. xSiTe
3. URL Link -
https://singaporetech.bluera.com/singaporetech
4. QR Code

### Slide 3: Review

• String, List
• WADIOOO
• Sequence
• Insert, delete, update, query
• in, not in
• index, slicing
• Concatenation and repetition
• Immutable and mutable
• Tuple
• Shallow Copy and Deep Copy
• Dictionary
• Key-value pair
• List Comprehension

### Slide 4: Outline

• File I/O
• read
• write
• Function
• Default arguments
• Positional and keyword arguments
• Will a Variable's Value Change After a Function Call?
• Variable scope
• Modules
• Higher-order functions

### Slide 5: Files I/O

• Why do we need a file?
• Data used in the program is stored in the memory
• Still can find the data after reboot the computer/restart the program
• Keep the data permanent
• File operations
Open a file Process the 
data/file Save the file
Load data from 
disk to 
memory
Process the 
data
Write data to 
disk

### Slide 6: Practice

• Create a new file on Google Colab
• Double click 'student.txt' and edit it, and save it (Ctrl + S)
%cd /content/drive/MyDrive

### Slide 7: Sample file

000 John 100
001 Josh 101
002 James 89
003 Jane 95

### Slide 8: Practice

1. Append a new student: Jack 99
2. The id of the new student is maximum_id + 1: 004
3. Save data to the file
# read file
# get max id
# generate new id
# append one student
# write to file

### Slide 9: Practice

# read file
students = []
file = open('student.txt', 'r')
for line in file:
line = line.strip()
if line:
students.append(line)
print(students)
file.close()

### Slide 10: Open a file

• Python’s built-in open() function
• Create one file object that can be utilized
• Syntax:
• file = open('student.txt', 'r')
• file_object= open(file_name[, access_mode] [, encoding])

### Slide 11: open()

• open('student.txt', 'r')
• File_name
• a string value that contains the name of the file that you want to access
• Access_mode
• the mode in which the file to be opened, i.e., read, write, append, etc.
• Optional, the default model is read(r)
• Encoding
• Default value depends on your operating system
• utf-8
• Remember the Unicode thing?

### Slide 12: mode

• Open('student_info.txt', mode='r')
Mode Description
r Opens a file for reading only. This is the default mode.
r+ Opens a file for both reading and writing. 
w Opens a file for writing only. Overwrites the file if the file exists. If the file 
does not exist, creates a new file for writing.
w+ Opens a file for both writing and reading. Overwrites the existing file if the 
file exists. If the file does not exist, creates a new file for reading and 
writing.
a Opens a file for appending. If the file does not exist, it creates a new file for 
writing.
b rb, wb, ab, etc. Opens the file in binary mode.
…

### Slide 13: readline() vs for line in file

while True:
line = file.readline() # Read one line
if not line: # If an empty string is returned, end of file is reached
break
if line.strip():
students.append(line.strip()) # Store the line after removing the newline character
#==============================================
for line in file:
line = line.strip()
if line:
students.append(line)

### Slide 14: Practice

#students = file.readlines()
students = [line.strip() for line in file.readlines() if line.strip()]

### Slide 15: Read a file

• readline(size)
• the size parameter specifies the maximum number of characters to read from the line, strictly 
limiting the read to that number or until the end of the line is reached. 
• readlines(hint)
• returns a list containing each line in the file as a list item.
• the hint parameter suggests the approximate number of characters to read, but it doesn't strictly 
limit the total number, ensuring complete lines are still returned. 
• read(size)
students = []
file = open('student.txt', 'r')
students = file.readlines(3)
print(students)
file.close()
students = []
file = open('student.txt', 'r')
line = file.readline(3)
students.append(line)
print(students)
file.close()
exit()

### Slide 16: # get max id

max_id = 0
for student in students:
id = int(student.split(' ')[0])
if id > max_id:
max_id = id
print(max_id)

### Slide 17: # generate new id

new_id = max_id + 1
print(new_id)
# append a student 004
new_id = str(new_id).zfill(3)
students.append(f'{new_id} Jack 99')
print(students)

### Slide 18: # write to file

with open('student.txt', 'w', encoding='utf-8') as file:
for student in students:
file.write(student + '\n')

### Slide 19: Write data to a file

• write(str)
• writelines(sequence)
• Whether the lines include newline characters.
Open a file Process the 
data/file Save the file
Load data from 
disk to 
memory
Process the 
data
Write data to 
disk

### Slide 20: Append mode

• Open('student_info.txt', mode='r')
Mode Description
r Opens a file for reading only. This is the default mode.
r+ Opens a file for both reading and writing. 
w Opens a file for writing only. Overwrites the file if the file exists. If the file 
does not exist, creates a new file for writing.
w+ Opens a file for both writing and reading. Overwrites the existing file if the 
file exists. If the file does not exist, creates a new file for reading and 
writing.
a Opens a file for appending. If the file does not exist, it creates a new 
file for writing.
b rb, wb, ab, etc. Opens the file in binary mode.
…

### Slide 21: File pointer

• Indicate the current focused position of the file
• open(xxx, mode='r')
• The file pointer is placed at the beginning of the file.
# read file
file = open('student.txt', 'r')
seg1 = file.read(4)
print(f'{seg1=}')
seg2 = file.read(4)
print(f'{seg2=}')
file.close()

### Slide 22: With open() as file:

• The with statement is a context manager
• Automatically handles file opening and closing
• Ensures the file is properly closed even if an exception occurs
• Restricts the variable scope to the with block
file = open('student.txt', 'r')
file.close()
with open('student.txt', 'r') as file:
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:

### Slide 23: The 'with' statement

• Advantages of the with statement:
• More concise
• Automatic resource management, avoiding resource leaks
• Safer, more readable code
• Restricts the variable scope, reducing potential bugs
• Disadvantages of the traditional method:
• Requires explicit file closing
• Error-prone, can lead to resource leaks
• Variable remains in scope, which may cause unexpected issues

### Slide 24: Review

• Read data from a file
• Operations on the data
• Write to a file
• File Pointer
• 'with' statement

### Slide 25: Open a file

• Python’s built-in open() function
• Create one file object that can be utilized
• Syntax:
• file = open('student.txt', 'r')
• file_object= open(file_name[, access_mode] [, encoding])

### Slide 26: Object Oriented Programming

• Class
• A blueprint for creating objects
• Defines a set of attributes and methods
• Groups data and behavior together in a reusable and organized way
• Instance
• Attributes (or Properties): Variables that store data specific to the object • Name, Age
• Methods (or Functions): Functions that define the behavior of the object • Walk, Speak
• Abstraction
• Encapsulation, Inheritance, Polymorphism, …

### Slide 27: Outline

• File I/O
• read
• write
• Function
• Default arguments
• Positional and keyword arguments
• Will a Variable's Value Change After a Function Call?
• Variable scope
• Modules
• Higher-order functions

### Slide 28: Function

• A Python function is a block of organized, reusable code that is 
used to perform a single, related action.
• Functions of a smartphone
• Make a phone call
• Calculator
• Play games
https://www.tutorialspoint.com/python/python_functions.htm
https://hub.jhu.edu/2016/03/07/lego-blocks-build-better-thinkers/

### Slide 29: function definition

def function_name( arguments ):
 '''function_docstring'''
 function_suite
 return [expression]
• Function_name
• The identifier of the function
• Arguents
• Input
• Formal Arguments
• Actual Arguments
• Function_docstring
• Comment your codes
• Optional
• Function_suite
• Block of code
• indented
• Return value
• Optional
• Exits a function
• Passing back an expression to the caller
• Output
import sys
def is_number(s):
try:
float(s)
return True
except ValueError:
#print('float s error')
return False
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def AverageCalculator():
input1 = sys.argv[1]
input2 = sys.argv[2]
input3 = sys.argv[3]
#print(input1,input2,input3)
if not is_number(input1) or not is_number(input2) or not
is_number(input3):
print('Your input is invalid!')
return
average = (float(input1)+float(input2)+float(input3))/3
#print(average)
print(f'Average:{average:.2f}')

### Slide 30: Arguments

• A function can have 0 or multiple 
arguments
• Formal Arguments
• A place to get input value
• A name used inside a function
• Actual Arguments
• True value
• When you call one function, it 
must have the same number of 
arguments as defined
Formal Argument
Actual Argument

### Slide 31: Positional and Keyword Arguments

• Positional Arguments
• Passed to the function in the order in which they are defined.
• Order matters, arguments are matched by position.
• Keyword Arguments
• Passed to the function by explicitly naming each parameter.
• Order doesn't matter, parameters are matched by name.
• Keyword-Only Arguments
• To enhance the robustness and readability of the program
• Especially when there are many parameters
file = open('student.txt', 'r','utf-8')
file = open('student.txt', 'r', encoding='utf-8')

### Slide 32: Positional and Keyword Arguments

• Further Reading
• *args
• Allows a function to accept any number of positional arguments.
• Pack positional arguments into a tuple.
• **kwargs
• Allows a function to accept any number of keyword arguments.
• Pack keyword arguments into a dictionary.
https://www.tutorialspoint.com/python/python_arbitrary_arguments.htm
def sum_numbers(*args):
total = 0
for number in args:
total += number
return total
# Call the function and pass two positional arguments
result = sum_numbers(10, 20)
print(result) # Output: 30
result = sum_numbers(1, 2, 3, 4, 5)
print(result) # Output: 15

### Slide 33: Will a Variable's Value Change After a

Function Call?
• Immutable variables
• str, int, float, tuple
• Immutable variables are not changed after a function call
def AverageModifier(average):
print(f'==inside the function {average}, id {id(average)}')
average += 10
print(f'==inside the function {average}, id {id(average)}')
average = 0.0
print(f'before {average}, id {id(average)}')
AverageModifier(average)
print(f'after {average}, id {id(average)}')
before 0.0, id 2197420871600
==inside the function 0.0, id 2197420871600
==inside the function 10.0, id 2197420578224
after 0.0, id 2197420871600

### Slide 34: Will a Variable's Value Change After a

Function Call?
• Mutable variables
• list, dictionary
• Mutable variables can be changed as a result of one function call
def AddAScore(scores):
print(f'==inside the function {scores}, id {id(scores)}')
scores.append(10)
print(f'==inside the function {scores}, id {id(scores)}')
scores = [0.0]
print(f'before {scores}, id {id(scores)}')
AddAScore(scores)
print(f'after {scores}, id {id(scores)}')
before [0.0], id 2197429867136
==inside the function [0.0], id 2197429867136
==inside the function [0.0, 10], id 2197429867136
after [0.0, 10], id 2197429867136

### Slide 35: The scope of the variable

• Local Variable
• Variables defined within a function can only be accessed and used inside that function.
• They "come to life" when the function is called and "die" (or go out of scope) when the 
function execution is completed.

### Slide 36: The scope of the variable

• Global Variable
• Nonlocal Variables
https://www.tutorialspoint.com/python/python_variables_scope.htm
#global variables
name = 'TutorialsPoint'
marks = 50
def myfunction():
# accessing inside the function
print("name:", name)
print("marks:", marks)
# function call 
myfunction()
# this is a global variable
marks = 50
def myfunction():
 # global marks
 print (marks)
marks = marks + 20
print (marks)
myfunction()
UnboundLocalError: local variable 'marks' referenced before 
assignment

### Slide 37: Review

def function_name( arguments ):
 statements
• Arguments
• Default arguments
• Positional and Keyword Arguments
• Immutable variables' value cannot be changed
• Scope of variables
• Local Variable
• Global Variable

### Slide 38: Outline

• File I/O
• read
• write
• Function
• Default arguments
• Positional and keyword arguments
• Will a Variable's Value Change After a Function Call?
• Variable scope
• Modules
• Higher-order functions

### Slide 39: Modules

• Function is a container of bit of codes
• Module
• Put related functions together.
• A module is a file containing definition of functions, classes, variables, 
constants or any other Python object.
• Python has the import keyword to load a module.

### Slide 40: Create your own module

• A module is a simple python 
file
• Like your regular scripts
• Create one module
• Write one or more functions in a 
text file
• Save it with a .py extension
• Save in the same directory as 
other scripts
• Give one descriptive name
'''
A module that processing text files
'''
def load_data(file_name):
'''
load txt lines from a file
'''
with open(file_name,'r') as file:
data = file.readlines()
return data
def process_data(data):
'''
data is a list of string
for each string, there is a \\n at the end
'''
data = [i.strip()+': processed\n' for i in data]
return data
#for i in range(len(data)):
# data[i] = data[i].strip()+': processed\n'

### Slide 41: Use a module

• import module_name [as 
simple_name]
• Without .py extension
• Use a function
• module_name.fun_name()
import txt_processor
help(txt_processor)
#from txt_processor import load_data, process_data
file_name = 'student.txt'
data = txt_processor.load_data(file_name)
#data = load_data(file_name)
print(data)
processed_data = txt_processor.process_data(data)
#processed_data = process_data(data)
print(processed_data)
print(dir(txt_processor))
Help on module txt_processor:
NAME
 txt_processor- A module that processing text files
FUNCTIONS
 load_data(file_name)
 load txt lines from a file
 process_data(data)
 data is a list of string
 for each string, there is a \n at the end
FILE
 ---\txt_processor.py
['John\n', 'Josh\n', 'James\n', 'Jane']
['John: processed\n', 'Josh: processed\n', 'James: processed\n', 'Jane: processed\n']
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'load_data', 'process_data']

### Slide 42: Use a module

• from module_name import (* or function_names)
• from txt_processor import load_data, process_data
• Allow you to select specific functions from the module
• When to use from keyword
• For a module that hundreds of functions
• It saves loading time
• In your program, can directly use the function name
#import txt_processor
#help(txt_processor)
from txt_processor import load_data, process_data
file_name = 'student.txt'
#data = txt_processor.load_data(file_name)
data = load_data(file_name)
print(data)
#processed_data = txt_processor.process_data(data)
processed_data = process_data(data)
print(processed_data)
#print(dir(txt_processor))

### Slide 43: #import txt_processor

#help(txt_processor)
from txt_processor import load_data, process_data
file_name = 'student.txt'
#data = txt_processor.load_data(file_name)
data = load_data(file_name)
print(data)
#processed_data = txt_processor.process_data(data)
processed_data = process_data(data)
print(processed_data)
#print(dir(txt_processor))
Use a module
• from module_name import (* or function_names)
• Allow you to select specific functions from the module
• When to use from keyword
• For a module that hundreds of functions
• It saves loading time
• In your program, can directly use the function name

### Slide 44: Python built-in modules

• Plenty of built in modules – Python really excels
• Popular modules
• math
• datetime
• random
• os
• urllib2

### Slide 45: File Path

• os.path.join()
• os.path.split()
• os.path.splitext()
• os.path.exists()
• os.mkdir()

### Slide 46: Library, Package, Module

Library
│
└─── Package
 ├─── Module (module1.py)
 ├─── Module (module2.py)
 └─── Subpackage
 ├─── Module (module3.py)
 └─── Module (module4.py)

### Slide 47: Popular Python Libraries for Data Science

Data Mining
• Scrapy
• Help to build crawling programs that can retrieve structured data from web
• A great tool for scraping data used in like ML models
• BeautifulSoup
• Another library for web crawling and data scraping 
• If you want to collect data that’s available on some website but not via a proper CSV or API, this library 
helps you scrape it and arrange it into the format you need 
• NumPy
• A perfect tool for scientific computing and performing basic and advanced array operations
• Handy features performing operations on n-arrays and matrics
• Performs math operations on array
• SciPy
• Include modules for linear algebra, integration, optimization and statistics
• Its main functionality was built upon NumPy
• Works great for all kinds of scientific programming projects (science, mathematics and engineering)

### Slide 48: Popular Python Libraries for Data Science

Data Mining
• Pandas
• Help work with “labeled” and “relational” data intuitively
• Based on two main data structures
• Series : one-dimensional like a list of items
• Data frames: two-dimensional like a table with multiple columns
• A Must-have for data wrangling, manipulation and visualization
• Matplotlib
• Standard library for visualization like two-dimensional diagrams and graphs (histograms, scatterplots, non-cartesion coordates graphs)
• Provides an object-oriented API for embedding plots into applications
• Seaborn
• Based on Matplotlib as useful ML tool for visualizing statistical models –heatmaps and 
other types of visualizations that summarize data and depict the overall distributions
• Get to benefit from an extensive gallery of visualization including complex ones like time 
series, joint plots and violin diagrams

### Slide 49: Popular Python Libraries for Data Science

Data Mining
• PyTorch
• Developed by Facebook's AI Research lab (FAIR)
• Deep Neural Networks: Built on a tape-based autograd system
• Flexibility: Suitable for research and prototyping
• Performance: High performance with easy integration into existing workflows
• Community: Strong support and extensive documentation
• Transformers
• Developed by: Hugging Face
• Pre-trained Models: Access to hundreds of models in over 100 languages (e.g., BERT, GPT-2, T5, RoBERTa)
• Easy Integration: Compatible with PyTorch and TensorFlow
• Pipeline API: Simplifies application of models to tasks like text classification, named 
entity recognition, question answering, and text generation
• Makes advanced NLP models accessible and easy to deploy

### Slide 50: Popular Python Libraries for Data Science

Data Mining
• SciKit-Learn
• An industry-standard for data science project
• A group of packages in the SciPy stack that were created for specific 
functionalities like image processing
• Uses math operations of SciPy to explosea concise interface to ML algorithms
• HanldesML and data mining tasks such as Clustering, regression, model 
selection, dimensionality reduction and classification
• TensorFlow
• A framework for ML and DL developed at Good Brain
• Best tool for tasks like object identification, speech recognition and many others
• Works with artificial neural networks to handle multiple datasets

### Slide 51: Popular Python Libraries for Data Science

Data Mining
• You are free to ask ChatGPT
• You are encouraged to read more documents
• Know what you are going to do
• Focus on your task

### Slide 52: Review

• import a_module as module
• Benefits of Modules
• Code organization: Group related functionality together for better structure.
• Code reuse: Write once, use in multiple programs.
• Namespace isolation: Prevent naming conflicts across different parts of the project.
• Maintainability: Easier to update and modify specific parts of the code.
• Further Reading
• __init__.py

### Slide 53: Outline

• File I/O
• read
• write
• Function
• Default arguments
• Positional and keyword arguments
• Will a Variable's Value Change After a Function Call?
• Variable scope
• Modules
• Higher-order functions

### Slide 54: Higher Order Functions

• Functions that take a function as an argument or return a function
• A function can be assigned as the value of a variable
• Can also be passed and returned just like any other reference variables
• A high order functions can be stored in the form of lists, hash tables, etc.

### Slide 55: Functions can be returned

def operation_factory(operation):
def add(a, b):
return a + b
def subtract(a, b):
return a - b
if operation == 'add':
return add
elif operation == 'subtract':
return subtract
add_fn = operation_factory('add')
subtract_fn = operation_factory('subtract')
print(add_fn(10, 5)) 
print(subtract_fn(10, 5))

### Slide 56: Built-in higher order functions

• sorted()
• Sorting items such as numbers or strings
• Sorting algorithms

### Slide 57: sorted – 'higher order'

• Sort a list of numbers by absolute value 
instead by their nature value
• Customize how sorting works
• The sorted function takes a parameter named 
'key'
• The key needs to be a simple function that 
takes a single value and tells python the value 
to use in sorting it
• Built-in function abs() can be used to get the 
absolute value
• We can specify the abs() as the key argument

### Slide 58: sorted – 'higher order'

• Specify your own function to sort the 
list
• Example:
• Given a list of strings, sort based on their last 
character
• Write one function to get the last character of the 
one string
• Specify this function as the key of the sorted 
function
• Bonus: built-ins max and min can be 
used in the same way as sorted

### Slide 59: Built-in higher order functions – map

• map(func, sequence)
• One of the arguments is a function
• The function is applied to each item in the sequence
• Return a sequence with different values
• Same order, same length, mapped via a function
map

### Slide 60: map

• Example
• Given a list of numbers, calculate the squares of each item
• Define one function square(x) to calculate the square number
• Use the map function to calculate the squares of the list

### Slide 61: map

• map can also use built-in functions like abs
• Practice
• Suppose you have a list of student names and scores
• ['John\t100', 'Josh\t90','Jane\t101','James\t92']
• Get the scores only

### Slide 62: map

• Practice
• Suppose you have a list of student names and scores
• ['John\t100', 'Jane\t101', 'Josh\t98', 'James\t120']
• Get the scores only

### Slide 63: Built-in higher order functions - filter

• filter (func, sequence)
• func: the filtering function
• seq: a sequence of the values
• Output: a sequence of values for which the function func returns true
• Function applies to each item to decide whether the item shall be kept or not
• If function returns True, the item is kept
• Otherwise, it is removed
filter

### Slide 64: filter

• Given a list of strings, filter those are start with 't'
• Define a function names is_startwitht(string) as the filter function
• Do the filter
• Implement the same function using for loop

### Slide 65: Map, Filter, and List Comprehension

def double(x):
return x * 2
numbers = [1, 2, 3]
result = map(double, numbers)
print(list(result)) # Output: [2, 4, 6]
result = [double(x) for x in numbers]
print(result) # Output: [2, 4, 6]
def is_even(x):
return x % 2 == 0
numbers = [1, 2, 3, 4]
result = filter(is_even, numbers)
print(list(result)) # Output: [2, 4]
result = [x for x in numbers if is_even(x)]
print(result) # Output: [2, 4]

### Slide 66: Map, Filter, and List Comprehension

• Lazy evaluation
• map() and filter() return iterators that delay computation until results are 
requested (e.g., with list(), for loop, or next()).
• Strategy: Expressions are evaluated only when needed.
• Benefits
• Saves memory by not storing all elements at once.
• Reduces unnecessary computations when only a portion of the data is needed.
• Efficient when working with large datasets or infinite sequences.
• List comprehension immediately calculates and returns a complete 
list.

### Slide 67: reduce

• reduce (func, seq)
• Takes a sequence of data and return a single value
• Func: Takes two values and returns one value
1. Consume the first two values from the sequence
2. Return a value
3. Consume the next value and the returned value
4. Repeat 3, until all values in the sequence have been consumed
5. Return the final value
• In python3, it is not a built-in function any longer. It is moved to 
'functools' module
• from functools import reduce

### Slide 68: reduce

• Calculate the summation of all the numbers in one list using 
reduce
• Define a function that adds two numbers
• reduce (func, seq)

### Slide 69: Notes

• All these functions does not change the original sequence
• A new sequence is created to hold the output

### Slide 70: Review

• Sorted
• Map
• Filter
• Lazy evaluation
• Reduce

---

## 6. Recursion and Docstrings

*Topics: Recursion concepts, factorial, Fibonacci, docstrings.*

### Slide 2: Review

• File I/O
• read, readline, readlines
• write, writelines
• with open() as file:
for line in file
• Function
• Default arguments
• Positional and keyword arguments
• *args, **kwargs
• Will a Variable's Value Change After a Function Call?
• Variable scope
• Modules
• Higher-order functions
• Function can be the value of a variable
• Can also be passed and returned just like any other reference variables

### Slide 3: Outline

• Recursion
• Docstring

### Slide 4: Recursion

• In computer science, recursion is a method of solving a 
computational problem where the solution depends on solutions 
to smaller instances of the same problem.1
• Recursion occurs when the definition of a concept or process 
depends on a simpler or previous version of itself.2
1. https://en.wikipedia.org/wiki/Recursion_(computer_science)
2. https://en.wikipedia.org/wiki/Recursion 
3. https://medium.com/analytics-vidhya/recursion-the-nesting-doll-of-programming-404ae61708a0

### Slide 5: Factorial

• 𝑛𝑛! = � 1, 𝑛𝑛 = 0
𝑛𝑛 ∗ 𝑛𝑛 − 1 !, 𝑛𝑛 > 0
• n=3
𝑛𝑛! = 3 ∗ 3 − 1 ! = 3 ∗ 2! = 3 ∗ 2 ∗ 2 − 1 ! = 3 ∗ 2 ∗ 1! = 3 ∗
2 ∗ (1 ∗ 1 − 1 !) = 3 ∗ 2 ∗ (1 ∗ 0!) = 6
How to we write a program to solve this problem?

### Slide 6: Factorial

• decomposition
• We turn this problem into a smaller 
problem of same kind. 
• base case
• Finally, we know the answer without 
calling the function itself
• composition
• We use the result of smaller problems 
to find the result of a larger problem.
3
2
1
0
1
2
3
3 ∗ 2!
2 ∗ 1!
1 ∗ 0!
1
1 ∗ 1 = 1
2 ∗ 1 = 2
3 ∗ 2 = 6
decomposition
base case
composition
𝑛𝑛! = � 1, 𝑛𝑛 = 0
𝑛𝑛 ∗ 𝑛𝑛 − 1 !, 𝑛𝑛 > 0

### Slide 7: Factorial

• https://pythontutor.com/render.html
#mode=display
• Further Reading:
• Stack
• Last in first out
• Push and pop
• Frame
• To represent the execution state of a 
function or code block
def factorial(n): 
 # Base case: If n is 0, return 1 
 if n == 0: 
 return 1 
 # Recursive case: n! = n * (n-1)! 
 else: 
 return n * factorial(n - 1)
# Example usage
number = int(input("Please enter an integer: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")

### Slide 8: Key points

• Figure out the formula about how a big problem can be solved by a 
similar smaller problem
• Assume you know how to solve the problem for n-1. How to use this 
information to solve the problem for n?
• Figure out what is the base case that the problem can get a solution.

### Slide 9: Fibonacci numbers

• Leonardo Pisano Fibonacci (12thcentury) is credited for the 
sequence:
• f(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, …
• n: 0, 1, 2, 3, 4, 5, 6, 7, 8, …
• Starting from the third number, each number in the sequence is
the sum of the previous two.
• Calculate f(n) to calculate the number on the position n

### Slide 10: Fibonacci numbers

• Figure out the formula about how a big problem can be solved by a 
similar smaller problem
• Assume you know how to solve the problem for n-1. How to use this 
information to solve the problem for n? Derive the recursive formula.
• Figure out what is the base case that the problem can get a solution.
•
𝐹𝐹0 = 0
𝐹𝐹1 = 1
𝐹𝐹𝑛𝑛 = 𝐹𝐹𝑛𝑛−1 + 𝐹𝐹𝑛𝑛−2
• Practice
Base case
Recursive formula

### Slide 11: From analyse to program

def func(big_problem):
 if base_case:
 return value
 else:
 # recursive formula
 tmp = func(smaller_problem)
 return recursive_formula(tmp)

### Slide 12: Fibonacci numbers

• Anything can be improved?

### Slide 13: Fibonacci numbers 5 4

3
21
2
3
21

### Slide 14: Fibonacci numbers 5 4

3
21
2
3
21

### Slide 15: Fibonacci numbers

### Slide 16: Practice

• Reverse a list
• scores = [70,63,98,85,22]
• Figure out the formula about how a big problem can be solved by a similar 
smaller problem
• Assume you know how to solve the problem for n-1. How to use this information to 
solve the problem for n?
• Figure out what is the base case that the problem can get a solution.
• What is the base case?
• What is the recursive formula?
https://leetcode.com/problems/reverse-linked-list/

### Slide 17: Practice

### Slide 18: Practice

• Implement Factorial function without recursion
• Recursion problems can be written in an iterative manner, and 
vice versa
• In actual programming, the choice between recursion and 
iteration often depends on the nature and context of the specific 
problem, as well as considerations of performance and 
readability.
𝑛𝑛! = � 1, 𝑛𝑛 = 0
𝑛𝑛 ∗ 𝑛𝑛 − 1 !, 𝑛𝑛 > 0

### Slide 19: Practice

### Slide 20: Review

• Recursion
• Figure out the formula about how a big problem can be solved by a similar 
smaller problem
• Base case
• Further Reading
• Dynamic Programming
• Stack
• Frame

### Slide 21: Docstring

• A Docstring is a comment 
that appears as the first line 
in a new part of the code
• Used for help functions

### Slide 22: Write your own module

• In the beginning of the module, 
write the module description 
surrounded by ''' or """
• In each function, write your 
comment in the first line with ''' 
or """

### Slide 23: Write your own module

### Slide 24: Review

• A comment that appears as the first line in a new part of the code
• Surrounded by ''' or """

### Slide 25: Byte Data Type

• ASCII, Byte, bit, Unicode
• Beyond txt file: image, audio, video, npy

### Slide 26: Byte Data Type

• The byte is a unit of digital information that most commonly 
consists of eight bits.
• A bit is 0 and 1.
• The bit is the most basic unit of information in computing and 
digital communication. 
• The name bit is a portmanteau of binary digit. 
• The bit represents a logical state with one of two possible values. These 
values are most commonly represented as either "1" or "0", but other 
representations such as true/false, yes/no, on/off, or +/− are also widely 
used.
• What is the value range of a byte?

### Slide 27: Memory usage of int and float in Python

• Not fixed
• A surprise from Python
• import sys 
• print(sys.getsizeof(1.0)) # 24
• print(sys.getsizeof(1)) # 28
• reference count, type information, extra padding or management 
overhead, etc.

### Slide 28: Byte and ASCII code

• One byte represents 8 bits
• In python, a char type is one byte
• The original ASCII table is a 7-bit encoding scheme that defines 
128 characters, numbered from 0 to 127. 
• These characters include English uppercase and lowercase 
letters, digits, punctuation marks, and control characters.
• The extended ASCII table (characters numbered 128 to 255) varies 
across different platforms and systems, lacking a single standard 
version.

### Slide 29: ASCII Table

• ASCII stands for American Standard Code for Information Interchange.

### Slide 30: ASCII Table

• Extended ASCII Codes
• Has not been widely or consistently adopted

### Slide 31: Unicode

• The original ASCII table is a 7-bit encoding scheme 
that defines 128 characters, numbered from 0 to 
127. 
• These characters include English uppercase and 
lowercase letters, digits, punctuation marks, and 
control characters.
• How to handle other languages? Chinese, Tamil, 
etc.
• Too many characters
• A-65
• 龙-40857

### Slide 32: Unicode and UTF-8

• A – 65 – 1000001 – 0100 0001
• 龙 – 40857 – 1001 1111 1001 1001 – (1001 1111) (1001 1001) 
• UTF-8 
• Variable-Length Encoding
• Uses 1 to 4 bytes to encode characters. 
• ASCII characters use 1 byte, while other characters use 2 to 4 bytes.
• Full compatible with ASCII
• Any valid ASCII text is also valid UTF-8 text.

### Slide 33: Byte and UTF-8

• The character "龙" (U+9F99) is encoded in UTF-8 as E9 BE 99.
• 龙 – 40857 – 1001 1111 1001 1001 - 1001 111110 011001
• UTF-8 uses 3 bytes to represent "龙"
• Format: 1110xxxx 10xxxxxx 10xxxxxx
• First byte 1110xxxx
• Fill in the first four bits: 1110 1001, which is E9.
• Second byte 10xxxxxx
• Fill in the next six bits: 1011 1110, which is BE.
• Third byte 10xxxxxx: 
• Fill in the remaining six bits: 1001 1001, which is 99.
https://www.rapidtables.com/convert/number/binary-to-decimal.html

### Slide 34: SIT Internal

### Slide 35: UTF-8

Type Description Unicode range Format
1 Byte Encode 7-bit ASCII 
characters
U+0000 to U+007F 0xxxxxxx
2 Bytes Encode 8 to 11-bit 
characters 
U+0080 to U+07FF 110xxxxx 10xxxxxx
3 Bytes Encode 12- to 16-bit 
characters
U+0800 to U+FFFF 1110xxxx 10xxxxxx 10xxxxxx
4 Bytes Encode 17- to 21-bit 
characters
U+10000 to 
U+10FFFF
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

### Slide 36: Understanding binary files

• Structure of a PNG File
• Signature
• First 8 bytes of the file
• Specific byte values (hexadecimal)
• 89 50 4E 47 0D 0A 1A 0A 
• Indicates that the file is a PNG
• Chunks
• Critical chunks (must appear in the file)
• IHDR: Image header
• Width,Height, Bit depth, Color type, …
• IDAT: Image data
• IEND: Image end 
• Ancillary chunks (optional metadata) 
Notepad++
Install HexViewer plugin

### Slide 37: Bits, Bytes, and Character Encoding

• Bit:
• 1 bit represents the most basic unit of data in computing, either 0 or 1.
• Byte:
• A byte is the standard unit for storing data in computers, comprising 8 bits.
• A byte can represent 256 possible values (from 0 to 255 in decimal).
• ASCII (American Standard Code for Information Interchange):
• ASCII uses 7 bits to encode printable characters, including English letters, digits, and control characters.
• Typically, ASCII is represented using 8 bits (1 byte), where the highest bit is often set to 0.
• UTF-8 (Unicode Transformation Format - 8 bits):
• UTF-8 is a variable-length encoding scheme that uses 1 to 4 bytes to represent characters from all languages.
• It is backward compatible with ASCII: ASCII characters use 1 byte, while more complex characters (e.g., from other 
languages) can use up to 4 bytes.
• Binary Files:
• A binary file is any file that contains a sequence of bytes.
• Not all binary files are human-readable. Text files, such as those using ASCII or UTF-8 encoding, can be read by 
humans. However, binary files like images, audio, or executables often need to be decoded by specific programs to be 
interpreted in a human-readable form.

### Slide 38: Professional

### Slide 39: UTF-8 won't be on the exam.

---

## 7. Lambda Expressions

*Topics: Anonymous functions, lambda syntax, use with map/filter/reduce.*

### Slide 2: Review

• Recursion
• Figure out the formula about how a big problem can be solved by a similar 
smaller problem
• Base case
• Docstring
• A comment that appears as the first line in a new part of the code
• Surrounded by ''' or """

### Slide 3: Outline

• Lambda Expression
• Reflect on Your Project

### Slide 4: Lambda Expression

• Anonymous Functions
• To create functions without a name
• Concise Syntax
• Contains only one statement
• Automatically returns the value of that 
statement
• Written in one line
• Ideal for small, simple operations.

### Slide 5: def vs lambda

def func_name(arg1, arg2, …, argn):
function body
return expression
• Has a name
• Arguments are in brackets
• Can have complex function body
• Optional keyword return
lambda arg1, arg2, …, argn: expression
• No name
• Arguments after lambda keyword
• No return keyword
• Cannot contain multiple statements 
or complex logic

### Slide 6: Practice

• Lambda in reduce function
• Can have multiple arguments

### Slide 7: Review

• Lambda Expression
• Anonymous Functions
• lambda arg1, arg2, …, argn: expression
• Can have multiple arguments.
• Only contains one statement.
• Returns the value of the statement automatically

### Slide 8: Project

• Can you include this project on your CV? How?
• How would you introduce your project in an interview if you only 
had 1-2 minutes?
• Could your project be published on GitHub?
• If given the opportunity, how would you improve your project in the 
future?

---

# Part 2: C Programming

## 8. Introduction to C

*Topics: C vs Python, compilation, data types, printf/scanf, operators, control flow, #define, enums.*

### Slide 2: ABOUT ME

2
– Dr Frank Guan, PhD
 Associate Professor, SIT
– Research interests:
– Virtual Reality (VR)
– Augmented Reality (AR)
– Artificial Intelligence (AI)
– Entrepreneurship & innovation
– If any module related matter, please email me at: 
Frank.Guan@singaporetech.edu.sg

### Slide 3: HOUSEKEEPING

– Lecture online (Zoom)
– Recorded
– Be focused and limit distractions
– Questions:
– Voice up
– Type in chat window 
– Other matters
– Respect
– Integrity
4

### Slide 4: INTRODUCTION TO C

DR FRANK GUAN
INF1002 – PROGRAMMING FUNDAMENTALS
WEEK 8

### Slide 5: Agenda

1. History of C
2. From Python to C
3. A simple C program
4. Basic data types
5. C formatted I/O
6. Control structures
6

### Slide 6: RECOMMENDED READING

7
Paul Deitel and Harvey Deitel
C: How to Program
9th Edition
Pearson, 2021

### Slide 7: HISTORY OF C

### Slide 8: QUESTION

– Type in the Zoom Chat window of 
the result of adding 37 to 45
9

### Slide 9: HOW ABOUT ASKING A COMPUTER

– Define two integer variables
– Assign values (35 and 47) for each 
variable
– Calculate the sum value of 35 and 47
– Print out the result (82) on the screen
• HOW TO DO
10

### Slide 10: WHY PROGRAMMING LANGUAGE

11
https://usemynotes.com/assembly-language-and-machine-language/

### Slide 11: HISTORY OF C

Martin Richard created the 
Basic Combined Programming Language 
in 1966 and 1967.
B
BCPL
C
13
Ken Thompson developed 
B – based on BCPL
in 1969 at Bell Lab. 
An early version of UNIX was written in B.
J. Presper Eckert and John Mauchly
Electronic Numerical Integrator and Computer 
1943 - 1946

### Slide 12: HISTORY OF C

1970s Traditional C
1989 – C89/ANSI C/Standard C
1990 – ANSI/ISO C
1999 – C99: an attempt to 
standardise many variations of C
C was created by Dennis Ritchie at 
Bell Lab between 1972 - 1973.
14
Dennis Ritchie (left) and Ken Thompson 
were the lead developers of UNIX.
UNIX was re-written in C in 1973.

### Slide 13: C VS. RELATED LANGUAGES

More recent derivatives: 
Influenced:
C lacks: 
Low-level language - faster code (usually) 
C++, Objective C, C# 
Java, Perl, Python 
(quite different) 
Exceptions
Range-checking
Garbage collection
Object-oriented programming
15

### Slide 14: FROM PYTHON TO C

### Slide 15: 1. COMPILERS VS. INTERPRETERS

Python uses an interpreter
to execute a program.
In C, the compiler converts 
a program into machine code.
The machine code can be 
executed directly by the CPU.
17

### Slide 16: 1. COMPILERS VS. INTERPRETERS

program.c a.out
Compiler
Source code Machine code
1
0001
1
 12
123
1234
12345
Interpreter
18

### Slide 17: 1. COMPILERS VS. INTERPRETERS

C programs can lead to faster runtimes.
C is designed so the compiler can tell 
everything it needs to know to translate the 
program into machine code.
19

### Slide 18: 2. VARIABLE DECLARATIONS

C requires variable declarations
These tell the compiler about the variable before it is 
used.
Once declared, you cannot change its type.
if you happen to misspell a 
variable’s name
20
Good

### Slide 19: 2. VARIABLE DECLARATIONS

In Python: no declaration required
You are responsible for checking your own code!
More convenient.
21

### Slide 20: 3. WHITESPACE

In Python, 
whitespace characters 
are important.
C does not use 
whitespace except for 
separating words.
Identify blocks
Identify new 
statements
22
Use braces {} to 
delimit blocks
Use a semi-colon to 
terminate statements

### Slide 21: 4. FUNCTIONS

– All C code must be put within 
functions.
– The main() function is the 
“starting point” for a C program.
23

### Slide 22: 4. FUNCTIONS

24
#include <stdio.h>
int gcd(int a, int b) {
 if (b == 0)
 return a;
 else
 return gcd(b, a % b);
}
int main() {
 printf("GCD: %d\n", gcd(24, 40));
 return 0;
}
C Program
def gcd(a, b):
 if b == 0:
 return a
 else:
 return gcd(b, a % b)
print("GCD: " + str(gcd(24, 40)))
Python Program
From http://www.cs.toronto.edu/~patitsas/cs190/c_for_python.html

### Slide 23: GOOD CODING PRACTICE IN C

– Indent blocks of code as in Python
– Format braces and whitespace consistently
– Use comments to explain your code to 
other programmers
– Use meaningful variable names
25
int i;main(){for(;i["]<i;++i){--i;}"];read('-'-'-',i+++"hell\
o, world!\n",'/'/'/'));}read(j,i,p){write(j/p+p,i---j,i/i);}
(from http://www.ioccc.org)

### Slide 24: GOOD CODING PRACTICE IN C

– Pay attention to compiler warnings
– these indicate code that is synactically correct 
but is likely to lead to run-time errors
– Avoid system-specific features
– all programs in this module should compile and 
run using any modern compiler
– code that works on many systems without 
modification is called portable
26

### Slide 25: A SIMPLE C PROGRAM

### Slide 26: TYPICAL C PROGRAM DEVELOPMENT

ENVIRONMENT
28
Editor The programmer creates a 
program.
Preprocessor The pre-processor processes 
the code.
Compiler The compiler creates object 
code.
Linker
The linker links the object 
code with the libraries and 
creates an executable file.
Loader
The loader puts the program 
in memory.
Disk
Memory
CPU takes each instruction 
and executes it.

### Slide 27: C PROGRAMS

Userdefined
C standard 
library
Other 
existing 
functions
A “C” Program
C programs consist of modules called functions
Provides a rich collection of 
existing common functions
Promote software reusability
29

### Slide 28: A SIMPLE C PROGRAM

Comments: any 
text between /*
and */ is ignored 
by the compiler.
30
/*
* Hello World program in C.
*/
#include <stdio.h>
int main() {
printf("Hello world!\n");
return 0;
}

### Slide 29: A SIMPLE C PROGRAM

C pre-processor: 
this line tells the 
preprocessor to 
include the 
content of the 
standard 
input/output 
header 
<stdio.h>
31
/*
* Hello World program in C.
*/
#include <stdio.h>
int main() {
printf("Hello world!\n");
return 0;
}

### Slide 30: A SIMPLE C PROGRAM

C programs 
contain one or 
more functions, 
one of which 
MUST be main. 
Every program in 
C begins 
execution in 
main.
32
/*
* Hello World program in C.
*/
#include <stdio.h>
int main() {
printf("Hello world!\n");
return 0;
}

### Slide 31: A SIMPLE C PROGRAM

One printf
can print several 
lines by using 
additional 
newline 
characters ‘\n’
33
/*
* Hello World program in C.
*/
#include <stdio.h>
int main() {
printf("Hello world!\n");
return 0;
}

### Slide 32: A SIMPLE C PROGRAM

Returning 0 tells 
the operating 
system that the 
program ended 
with no errors.
34
/*
* Hello World program in C.
*/
#include <stdio.h>
int main() {
printf("Hello world!\n");
return 0;
}
Code: “hello.c”

### Slide 33: C PRE-PROCESSOR

The C pre-processor executes before a 
program is compiled. 
Some actions it performs are: – definition of symbolic constants 
– the inclusion of other files in the file 
being compiled
Pre-processor directives begin with #
35

### Slide 34: #DEFINE PRE-PROCESSOR DIRECTIVE

36
The #define 
directive creates 
symbolic constants.
All subsequent 
occurrences of 
NUM_STUDENTS will be 
replaced with 140.
#define NUM_STUDENTS 140
int main() {
 int scores[NUM_STUDENTS];
 for (int i = 0; i < NUM_STUDENTS; i++) {
 scores[i] = 0;
 }
 return 0;
}

### Slide 35: #INCLUDE PRE-PROCESSOR DIRECTIVE

The #include directive causes a 
copy of a specified file to be included in 
place of the directive.
37

### Slide 36: #INCLUDE PRE-PROCESSOR DIRECTIVE

The two forms of the #include 
directive are:
#include <filename>
#include "filename"
"": used for user-defined files. 
The pre-processor starts searches 
in the same directory as the file 
being compiled
<>: is normally used for standard library
headers, the search is performed normally 
through pre-designated compiler and system 
directories.
38

### Slide 37: HEADER FILES

A C program might have header 
files containing:
Function prototypes
(declaration with no 
implementation)
Definitions of 
various data 
types
Definitions of 
constants
39

### Slide 38: 40

#include <stdio.h>
#include “chat1002.h"
int main() {
 int done = 0;
 do {
 ...
 } while (!done);
 return 0;
}
#define MAX_INTENT 32
#define MAX_ENTITY 64
void chatbot_do_load(int inc, char **inv);
void chatbot_do_smalltalk(int inc, char **inv);
#include "chat1002.h"
void chatbot_do_load(int inc, char **inv) {
 ...
}
void chatbot_do_smalltalk(int inc, char **inv) 
{
 ...
}
main.c
chat1002.h
chatbot.c
Constants
Function prototypes

### Slide 39: ANOTHER SIMPLE C PROGRAM

The names 
integer1, 
integer2
and sum are 
the names 
of 
variables. 
41
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}
Code: “sum.c”

### Slide 40: ANOTHER SIMPLE C PROGRAM A variable is a location in memory

where a value can be stored for use by a 
program.
42
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}
Code: “sum.c”

### Slide 41: ANOTHER SIMPLE C PROGRAM These definitions specify that the

variables integer1, integer2 and sum
are of type int.
43
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}
Code: “sum.c”

### Slide 42: The

scanf()
function 
reads from 
the standard 
input, which 
is usually 
the 
keyboard.
44
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}
ANOTHER SIMPLE C PROGRAM

### Slide 43: This scanf

has three 
arguments, 
"%d%d" and 
&integer1
and 
&integer2.
45
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}
ANOTHER SIMPLE C PROGRAM

### Slide 44: scanf(): The first argument, the format control string, indicates

the type of data that should be input by the user. The %d 
conversion specifier indicates that the data should be a (decimal) 
integer.
46
ANOTHER SIMPLE C PROGRAM
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}

### Slide 45: scanf(): The second and third arguments of scanf begin with

an ampersand (&)—called the address operator in C—followed by 
the variable name. 
47
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}
ANOTHER SIMPLE C PROGRAM

### Slide 46: scanf(): The ampersand tells scanf the locations (or addresses)

in memory at which the variables integer1 and integer2 are 
stored. 
48
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}
ANOTHER SIMPLE C PROGRAM
Code: “sum.c”

### Slide 47: 49

5 Minutes Break

### Slide 48: BASIC DATA TYPES

### Slide 49: MEMORY CONCEPTS

Every variable 
has a name, a 
type and a 
value.
51
int integer1, inteter2, sum;

### Slide 50: MEMORY CONCEPTS Variable

names such as 
integer1, 
integer2 and 
sum actually 
correspond to 
locations in 
the computer’s 
memory. 
integer1
integer2
sum
52
int integer1, inteter2, sum;
0x0060FF03
0x0060FF05
0x0060FF07
Memory Address

### Slide 51: MEMORY CONCEPTS The value typed

by the user is 
placed into a 
memory 
location to 
which the name 
integer1 or 
integer2 has 
been assigned.
53
scanf("%d%d", &integer1, &integer2);
45
37
integer1
integer2
sum
0x0060FF03
0x0060FF05
0x0060FF07
Memory Address
Assume we key in “45” for integer1 and “37” for integer2

### Slide 52: MEMORY CONCEPTS

Whenever a 
value is placed 
in a memory 
location, the 
value replaces
the previous 
value in that 
location.
54
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
Assume we key in “45” for integer1 and “37” for integer2
45
37
integer1
integer2
82 sum
0x0060FF03
0x0060FF05
0x0060FF07
Memory Address

### Slide 53: BASIC DATA TYPES

55

### Slide 54: EXAMPLE – C DATA TYPES

What is the %.10f for?
Try to change it to some other number and observe the output
https://alvinalexander.com/programming/printf-format-cheat-sheet56
#include <stdio.h>
int main() {
int a = 3000; /* integer data type */
float b = 4.5345; /* floating point data type */
char c = 'A'; /* character data type */
long d = 31456; /* long integer data type */
double e = 5.1234567890; /* double-precision floating point data type */
printf("Here is the list of the basic data types\n");
printf("\n1. This an integer (int): %d", a);
printf("\n2. This is a floating point number (float): %f", b);
printf("\n3. This is a character (char): %c", c);
printf("\n4. This is a long integer (long): %ld", d);
printf("\n5. This is a double-precision float (double): %.10f", e);
printf("\n6. This is a sequence of characters: %s",
"Hello INF1002 students");
return 0;
}
Code: “datatypes.c”

### Slide 55: C EXPRESSIONS

Arithmetic can be performed using the 
usual operators:
57
+ Addition
- Subtraction
* Multiplication
/ Division
% Remainder upon division (modulo)
() Parentheses

### Slide 56: C EXPRESSIONS

The result of an arithmetic operation depends 
on the type of its operands:
You can explicitly change the type of an 
expression using a cast:
58
int op int int
int op float float
float op float float
double op float double
char op int char
(int)4.5 round down
(float)4 “promote”

### Slide 57: C FORMATTED I/O

### Slide 58: C FORMATTED I/O

Standard input/output: 
#include <stdio.h>
– Input data from the standard input 
stream
– Output data to the standard output 
steam
– printf, scanf, puts, 
getchar, putchar
60

### Slide 59: STREAMS

All input and output is performed with streams.
Stream: A sequence of bytes.
C 
Programs
Memory
Keyboard, disk Input Stream
drive, network 
connections
Output Stream Screen, disk 
drive, printer, 
network 
connections
Error Stream
Screen
61

### Slide 60: FORMATTING OUTPUT WITH PRINTF

– format-control-string: describes the output 
format
– other-arguments (optional): correspond to each 
conversion specification within format-controlstring
printf(format-control-string, other-arguments);
printf("%s", "Hello World!");
62

### Slide 61: COMMON CONVERSION SPECIFIERS

Specifier Output
Characters
%c Character
%s A string of characters
Integers
%d Decimal integer
%x Hexadecimal integer
%ld Long decimal integer
Floating point numbers
%f Single-precision
%lf Double-precision
63
See Deitel & Deitel Ch. 9 for other specifiers.

### Slide 62: MORE ON CONVERSION SPECIFIERS

conversion-specifier = <flags><field width><precision><literal character>
printf( "%-10s%-10d%-10c%-10.3f\n", 
"hello", 7, 'a', 1.23 );
flag field width literal character
precision
64

### Slide 63: PRINTF FLAGS

Flag Description
- (minus sign)
Left-justify the output within the 
field.
+ (plus sign)
Insert a plus sign before positive 
numbers and a minus sign before 
negative numbers.
space
Insert a space before positive
numbers.
0 Zero-pad the number to the width of 
the field.
65
See Deitel & Deitel Ch. 9 for other flags.

### Slide 64: 66

/*
* Printing field width example adopted from Deitel & Deitel
*/
#include <stdio.h>
int main() {
printf("%4d\n", 1);
printf("%04d\n", 1);
printf("%-4d\n", 1);
printf("%4d\n", 12);
printf("%4d\n", 123);
printf("%4d\n", 1234);
printf("%4d\n", 12345);
return 0;
}
1
0001
1
 12
123
1234
12345
Output:
PRINTF FLAGS - EXAMPLE
Code: “fieldwidth.c”

### Slide 65: ESCAPE SEQUENCES

Characters with special meaning to the 
compiler need to be “escaped”:
67
Escape Sequence Output
\n New line
\t Tab
\' Single quote
\" Double quote
\\ Backslash
See Deitel & Deitel Ch. 9 for other escape sequences.

### Slide 66: SCANF – READING FORMATTED INPUT

scanf(format-control-string, other-arguments);
Output
68
printf("Enter seven integers: ");
scanf("%d%i%i%i%o%u%x", &a, &b, &c, &d, &e, &f, &g);
printf("The input displayed as decimal integers is:\n");
printf("%d %d %d %d %d %d %d", a, b, c, d, e, f, g);
Enter seven integers: -70 -70 070 0x70 70 70 70
The input displayed as decimal integers is:
-70 -70 56 112 56 70 112

### Slide 67: NOW TAKE A LOOK BACK AT THE PREVIOUS SAMPLE

69
/*
* Another simple C program.
*/
#include <stdio.h>
int main() {
int integer1, integer2, sum;
printf("Enter two numbers to add\n");
scanf("%d%d", &integer1, &integer2);
sum = integer1 + integer2;
printf("Sum of entered numbers = %d\n", sum);
return 0;
}

### Slide 68: CONTROL STRUCTURES

### Slide 69: C CONTROL STRUCTURES

C has the same control structures as 
other programming languages:
– if-else
– switch (not available in Python)
– for
– while
– do-while (not available in Python)

### Slide 70: DECISIONS

if-else
if (x > 1) {
 printf("More than one.");
} else {
 printf("Not more than one.");
}
switch
switch (x) {
 case 1:
 printf("x is 1.");
 break;
 case 2:
 printf("x is 2.");
 break;
 …
}
72

### Slide 71: LOOPS

for
int i;
for (i = 0; i < 10; i++) {
 printf("i = %d\n", i);
}
while & do-while
int i = 0;
while (i < 10) {
 printf("i = %d\n", i);
 i++;
}
i = 0;
do {
 printf("i = %d\n", i);
 i++;
} while (i <= 10);
73

### Slide 72: END-OF-WEEK CHECKLIST

74
C development environment
Pre-processor directives
#include
#define
printf()
scanf() Format control strings
Coding conventions
Basic data types
Variables & memory
Streams
If/else
Switch/case
for/while/do..while
Comments
Basic C program structure

### Slide 73: ADMINISTRATIVE ITEMS

– Group project
– Project description will be uploaded to LMS in Week 9. 
– Grouping
– Test (week 13)
– Online
75
Item %
Lab Assignments 5%
Group Project 25%
Test (Week 13) 20%
Sub-total 50%

### Slide 74: ABOUT USAGE OF AI TOOLS

– For Labs
• AI tools (e.g. ChatGPT, Copilot, etc.) are allowed for reference purpose
• However, strongly recommend hands-on learning
– For Group Project
• AI tools are NOT allowed
• A declaration is needed from each team
– For Test
• AI tools are NOT allowed
76

### Slide 75: ABOUT LAB

– Conducted in classroom
– Follow the instructions on the lab sheet
– A few exercises to be completed in lab class
– Strongly recommend to complete these exercises in the 
lab and you may consult the instructor if any help is 
needed
– Assignment
77

---

## 9. Functions, Arrays, and Strings in C

*Topics: Function prototypes, call-by-value, scope, arrays, 2D arrays, strings, string functions.*

### Slide 2: RECAP OF LAST WEEK

– C programs consist of modules called functions
– The main() function is the “starting point” fora C program
– The pre-processor (begins with #) executes before a program is compiled
– definition of symbolic constants 
– the inclusion of other files in the file being compiled
– A variable is a location in memory where a value can be stored for use by a 
program
– printf(): the first argument, the format control string, describe the output format
– scanf(): The first argument, the format control string, indicates the type of data 
that should be input by the user
– control structures
– if – else
– switch
– for
– while
– do - while
2

### Slide 3: EXPERIENCE SHARING

– “Practice makes perfect”
– Truly common if you spend one week 
time on:
– Debugging
– Troubleshooting
– Reference reading
– Discussion
– Self-learning
– …
3

### Slide 4: Agenda

1. Functions
2. Arrays
3. Characters and Strings
4

### Slide 5: FUNCTIONS IN C

### Slide 6: FUNCTIONS – C’S BUILDING BLOCK

Functions 
promote 
reusability.
Each 
function is 
written once.
6
print
student 
information
Lecturer
Exam 
department
Student 
management 
department

### Slide 7: FUNCTIONS – C’S BUILDING BLOCK

The 
function can 
be used 
repeatedly 
by many 
other 
functions
7
print
student 
information
Lecturer
Exam 
department
Student 
management 
department

### Slide 8: C FUNCTION CALLS

8
main(){
function_1(...);
...
function_2(...);
...
function_n(...);
}
function_1(...){
...
function_1_1(...);
...
}
function_2(...){
...
}
function_n(...){
...
}
function_1_1(...)
{
...
}
1
2
3
4
5
6
7
8
Functions are invoked by specifying their name and 
parameters (or arguments) without knowing the actual 
implementation of the function.

### Slide 9: FUNCTION DEFINITIONS

9
The above function calculates the square of 
an integer y

### Slide 10: FUNCTION DEFINITIONS

10
return_value_type
function_name(<parameter_list>)
{
/*definitions*/
/*statements*/
}
• A comma-separated list of parameters received by the 
function when it is called.
• A type must be listed explicitly for each parameter. 
• E.g int number, char grade

### Slide 11: FUNCTION PROTOTYPES

– A function prototype is a function 
definition without a body, e.g.
int square(int);
– Function prototypes are optional, but are 
used by the compiler to validate function 
calls
– This prevents errors
– Prototypes are usually declared at the 
top of a source file, or in a header file
11

### Slide 12: FUNCTION DEFINITION - EXAMPLE

The function 
prototype 
informs the 
compiler that 
addition() 
expects to receive 
two integer
values and 
returns an 
integer result.
/* http://www.programmingsimplified.com */
#include <stdio.h>
/* function prototype */
int addition(int, int);
int main() {
int first, second, sum;
/* read input */
scanf("%d%d", &first, &second);
/* invoke the addition function */
sum = addition(first, second);
printf("%d\n", sum);
return 0;
}
/* function implementation */
int addition(int a, int b) {
int result;
result = a + b;
return result;
}

### Slide 13: FUNCTION DEFINITION - EXAMPLE

Whenever 
there’s a 
function call, 
the compiler 
will check 
that call 
against the 
function 
prototype.
/* http://www.programmingsimplified.com */
#include <stdio.h>
/* function prototype */
int addition(int, int);
int main() {
int first, second, sum;
/* read input */
scanf("%d%d", &first, &second);
/* invoke the addition function */
sum = addition(first, second);
printf("%d\n", sum);
return 0;
}
/* function implementation */
int addition(int a, int b) {
int result;
result = a + b;
return result;
}

### Slide 14: 14

The function 
stops executing as 
soon as one 
return
statement is 
executed.
MULTIPLE RETURN STATEMENTS
int get_sign(int n) {
 if (n < 0)
 return NEGATIVE;
 if (n > 0)
 return POSITIVE;
 return ZERO;
}
#include <stdio.h>
#define POSITIVE 1
#define NEGATIVE -1
#define ZERO 0
int get_sign(int n);
int main() {
 int n;
 int sign;
 printf("Type an integer: ");
 scanf("%d", &n);
 sign = get_sign(n);
 if (sign == POSITIVE)
 printf("That is a positive number.\n");
 else if (sign == NEGATIVE)
 printf("That is a negative number.\n");
 else
 printf("That is zero.\n");
 return 0;
}

### Slide 15: CALLING FUNCTIONS BY VALUE

– Call-by-value
– A copy of the argument’s value is made and passed to the called function
– Changes to the copy do not affect the original variable’s value in the caller
– By default, all calls in C are by value
15

### Slide 16: CALL-BY-VALUE – EXAMPLE

17
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
Output

### Slide 17: CALL-BY-VALUE – EXAMPLE

18
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
a 0x0060FF03 10
Memory Address

### Slide 18: CALL-BY-VALUE – EXAMPLE

19
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
a 0x0060FF03 10
Memory Address

### Slide 19: CALL-BY-VALUE – EXAMPLE

20
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
a 0x0060FF03 10
Memory Address
x 0x0060FF05 10
Pass 
by 
value

### Slide 20: CALL-BY-VALUE – EXAMPLE

21
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
a 0x0060FF03 10
Memory Address
x 0x0060FF05 20

### Slide 21: CALL-BY-VALUE – EXAMPLE

22
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
a 0x0060FF03 10
Memory Address
x 0x0060FF05 20

### Slide 22: CALL-BY-VALUE – EXAMPLE

23
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
a 0x0060FF03 10
Memory Address
x 0x0060FF05 20
Value of “a” is 
not updated!

### Slide 23: CALL-BY-VALUE – EXAMPLE

24
#include <stdio.h>
void call_by_value(int);
int main() {
int a = 10;
printf(“\nBefore call_by_value, a = %d.\n\n", a);
call_by_value(a);
printf("After call_by_value, a = %d.\n \n ", a);
return 0;
}
/* this function will make a copy of a */
void call_by_value(int x) {
printf("Inside call_by_value, x = %d.\n \n ", x);
x += 10;
printf("After adding ten, x = %d.\n \n ", x);
}
Output

### Slide 24: CALLING FUNCTIONS BY REFERENCE

– Call-by-reference
– The caller allows the called function to modify the 
original value
– Call-by-reference can be simulated by using the address operator (&)
– More will be covered later…
25

### Slide 25: FUNCTIONS FROM THE STANDARD C LIBRARY

The Standard C Library provides many 
commonly-used functions, e.g.
26
Header Functions
<ctype.h> Character functions:
isalpha(), isdigit(), etc.
<math.h> Mathematical functions:
sqrt(), exp(), log(), sin(), cos(), tan(), etc.
<stdlib.h> Miscellaneous functions:
malloc(), free(), rand(), atoi(), etc.
<stdio.h> Input/output:
printf(), scanf(), fopen(), fread(), fwrite(), etc.
<string.h> String functions:
strcpy(), strcmp(), etc.

### Slide 26: FUNCTIONS FROM THE STANDARD C LIBRARY

Visit cplusplus.com for a complete list:
– http://www.cplusplus.com/reference/clibrary/
27

### Slide 27: SCOPE RULES

28

### Slide 28: SCOPE RULES

The scope of an identifier is the 
portion of the program in which the 
identifier can be referenced.
– The same identifier can be re-used in 
different scopes.
– Tip: the scope of an identifier should 
be as small as possible. 
– Why?
29

### Slide 29: SCOPE RULES – FILE SCOPE

– An identifier declared outside any 
function has file scope.
– A file-scope identifier is accessible 
from its declaration until the end 
of the file.
– Variables with file scope are often 
called global variables.
30

### Slide 30: FILE SCOPE - EXAMPLE

31
i is declared 
outside any 
function so i has 
file scope
#include <stdio.h>
int i = 1;
int main() {
 int x = 4;
 printf("add_i outputs %d\n", add_i(x));
 printf("i is %d\n", i);
 printf("x is %d\n", x);
 return 0;
}
int add_i(int n) {
 int x = n + i;
 i++;
 return x;
}
This statement 
updates the global 
variable i

### Slide 31: SCOPE RULES – BLOCK SCOPE

– Identifiers defined inside a block 
delimited by braces {…} have 
block scope.
– Any block may contain variable definitions.
– Variables with block scope are 
often called local variables.
32

### Slide 32: BLOCK SCOPE - EXAMPLE

33
#include <stdio.h>
int i = 1;
int main() {
 int x = 4;
 printf("add_i outputs %d\n", add_i(x));
 printf("i is %d\n", i);
 printf("x is %d\n", x);
 return 0;
}
int add_i(int n) {
 int x = n + i;
 i++;
 return x;
}
This x has block 
scope within 
main()
This x has block 
scope within 
add_i()
add_i outputs 5
i is 2
x is 4
Output:

### Slide 33: 34

### Slide 34: ARRAYS

### Slide 35: ARRAYS

An array is a group of memory locations 
that all have
 the same name
 the same type
36

### Slide 36: The position

number contained 
within square 
brackets is called 
a subscript
or index.
37

### Slide 37: The index starts at

zero.
38
The index ends at the 
number of array 
elements, minus 1
The index can be any 
integer expression, e.g.
int a = 1;
c[a+2] += 2;

### Slide 38: HOW TO USE

39
Define
Initialize
Use
#include <stdio.h>
#define MAX_STUDENTS 10
int main() {
int studentId[MAX_STUDENTS];
for (int i = 0; i < MAX_STUDENTS; i++)
studentId[i] = i + 1;
printf("%7s%13s\n", "Element", "Value");
for (int i = 0; i < MAX_STUDENTS; i++)
printf("%7d%13d\n", i, studentId[i]);
return 0;
}

### Slide 39: DEFINING ARRAYS

To define an array we need 
to specify:
the type of the elements
the name of the array
the number of elements
40
int b[100], x[27];
Type Name Number
int a, y;
VS

### Slide 40: ARRAY INITIALISATION

We can use a loop to initialise array 
elements:
41
#include <stdio.h>
#define MAX_STUDENTS 10
int main() {
int studentId[MAX_STUDENTS];
for (int i = 0; i < MAX_STUDENTS; i++)
studentId[i] = i + 1;
printf("%7s%13s\n", "Element", "Value");
for (int i = 0; i < MAX_STUDENTS; i++)
printf("%7d%13d\n", i, studentId[i]);
return 0;
}
Define an array
Initialize the array
Use the array

### Slide 41: ARRAY INITIALISATION

We can also use an initialiser list:
42
#include <stdio.h>
#define MAX_STUDENTS 10
int main() {
int studentId[MAX_STUDENTS] =
{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
printf("%7s%13s\n", "Element", "Value");
for (int i = 0; i < MAX_STUDENTS; i++)
printf("%7d%13d\n", i, studentId[i]);
return 0;
}

### Slide 42: MULTI-DIMENSIONAL ARRAYS

– The most commonly used are two dimensional arrays 
or double-subscripted arrays.
– In general, an array with m rows and n columns is 
called an m-by-n array.
43

### Slide 43: DECLARING MULTIDIMENSIONAL ARRAYS

44
int b[ 2 ][ 2 ] = { { 1, 2 }, { 3, 4 } };
Declare and initialise a two-dimensional array of integers.
The values in the initialiser list are grouped by row.
1 2
3 4 b

### Slide 44: STRINGS

### Slide 45: FUNDAMENTALS OF CHARACTERS

A program may contain character constants
– A character constant is denoted by single 
quotes and has an integer value according 
to the character set
– E.g. in ASCII: 
– 'z' has an integer value of 122
– '\n' has an integer value of 10
– Some mathematical operators can be applied 
to characters
– + and – move up and down the character set
– <, >, ==, != compare according to the 
character set
46

### Slide 46: CHARACTER HANDLING LIBRARY

47
<ctype.h>

### Slide 47: FUNDAMENTALS OF STRINGS

A string in C is an array of
characters ending in the null
character ('\0').
String literals (constants) are written in 
double quotation marks: – "SIT-DNA"
– "Thinking Tinkerers"
– "Able to Learn, Unlearn and Relearn"
– "Catalyst for Transformation"
– "Grounded in Community"
48

### Slide 48: STRING INITIALISATION

This is how you can initialise a string:
49
This creates an array of 
5 elements as follows:
b l u e \0
When defining a character 
array to contain a string, 
the array must be large 
enough to store the string 
and its terminating null 
character. 
If no size is specified, the size will be 
determined based on the number of 
initialisers in the list. E.g.: 5 in this case
char colour[] = "blue";

### Slide 49: STRING INITIALISATION

50
Variable word is an array, which is a 
memory address, so the address operator 
& is not needed with argument word.
A string can be stored in an array using scanf:
char word[10];
scanf("%9s\n", word);

### Slide 50: STRING INITIALISATION

51
Note that scanf will read characters until a 
space, tab, newline or end-of-file 
indicator is encountered. So it is possible 
that the user could exceed 9 characters and 
your program might crash. 
char word[10];
scanf("%9s\n", word);
A string can be stored in an array using scanf:

### Slide 51: STRING INITIALISATION

52
It is good practice to use the conversion 
specifier %9s so that scanf reads up 
to 9 characters and saves the last one for 
the null character.
char word[10];
scanf("%9s\n", word);
A string can be stored in an array using scanf:

### Slide 52: STANDARD I/O FUNCTIONS

FOR STRINGS & CHARACTERS
53
<stdio.h>

### Slide 53: STANDARD I/O FUNCTIONS

FOR STRINGS & CHARACTERS
54
#include <stdio.h>
#include <string.h>
#define MAX_LENGTH 80
/* print the characters of a string in reverse order */
void print_reverse(const char[]);
int main() {
char sentence[MAX_LENGTH];
printf("Enter a line of text:\n");
fgets(sentence, MAX_LENGTH, stdin);
printf("The input line written backwards:\n");
print_reverse(sentence);
return 0;
}
fgets() reads characters into an 
array of chars until a newline or the 
end-of-file indicator is encountered, 
or until the maximum number of 
characters is read.

### Slide 54: #include <stdio.h>

#define MAX_LENGTH 80
int main() {
 char sentence[MAX_LENGTH];
 char c;
 int index = 0;
 puts("Enter a line of text: ");
 while ((c = getchar()) != '\n' && index < MAX_LENGTH - 1)
 sentence[index++] = c;
 sentence[index] = '\0';
 puts("The input line was: ");
 puts(sentence);
 return 0;
}
STANDARD I/O FUNCTIONS 
PUTS() AND GETCHAR()
55
getchar() reads a character from the 
standard input and returns the character as 
an integer.
puts() takes a string as an argument and 
prints the string followed by a
newline character.

### Slide 55: #include <stdio.h>

#define MAX_LENGTH 80
int main() {
 char s[MAX_LENGTH];
 int x;
 double y;
 printf("Enter an integer and a double: ");
 scanf("%d%lf", &x, &y);
 sprintf(s, "integer: %d, double: %f\n", x, y);
 printf("The formatted string stored in the array is: %s", s);
 return 0;
}
STANDARD I/O FUNCTIONS 
FORMATTED DATA TO A STRING WITH SPRINTF()
56
sprintf() prints formatted data into an 
array of characters. The function uses the same 
conversion specifiers as printf

### Slide 56: STRING MANIPULATION FUNCTIONS

57
<string.h>

### Slide 57: #include <stdio.h>

#include <stdlib.h>
#include <string.h>
#include <time.h>
#define MAX_FULLNAME 80
#define MAX_USERNAME 9
#define RANDOM_DIGITS 3
int main() {
 char name[MAX_FULLNAME];
 char userID[MAX_USERNAME];
 int n, i;
 printf("Enter your name: ");
 scanf("%79s", name);
 strncpy(userID, name, MAX_USERNAME - RANDOM_DIGITS - 1);
 userID[MAX_USERNAME - RANDOM_DIGITS - 1] = '\0';
 n = strlen(userID);
 for (i = 0; i < RANDOM_DIGITS; i++)
 userID[n + i] = '0' + rand() % 10;
 userID[n + RANDOM_DIGITS] = '\0';
 printf("Your username is: %s\n", userID);
 return 0;
}
STRING MANIPULATION LIBRARY
EXAMPLE – WHAT DOES THIS PROGRAM DO?
58
Ensure the string is 
terminated by ‘\0’.
srand() and rand() 
generate random 
numbers.

### Slide 58: STRING MANIPULATION LIBRARY

EXAMPLE – OUTPUT
59
Enter your full name: Cristal Ngo Minh Ngoc
Your username is: Crist610
Enter your full name: Rachel Green
Your username is: Rache822

### Slide 59: STRING COMPARISON FUNCTIONS

60
<string.h>
Note:
strcmp() and strncmp() are both 
case-sensitive.

### Slide 60: STRING COMPARISON FUNCTIONS

EXAMPLE
61
#include <stdio.h>
#include <string.h>
int main() {
char word1[20], word2[20];
printf("Enter two words, separated by a space: ");
scanf("%19s%19s", word1, word2);
int c = strcmp(word1, word2);
if (c < 0)
printf("\"%s\" comes first.\n", word1);
else if (c > 0)
printf("\"%s\" comes first.\n", word2);
else
printf("Those two words are the same.\n");
return 0;
}

### Slide 61: STRING CONVERSION FUNCTIONS

62
<stdlib.h>

### Slide 62: STRING CONVERSION FUNCTIONS

EXAMPLES
63
convert the string "123456789" to the 
long integer 123456789
long l;
l = atol("123456789");

### Slide 63: END-OF-WEEK CHECKLIST

64
Function prototypes
Function definitions
Call by value
Scope rules
Array declarations
Array initialiser lists
Multi-dimensional arrays
Characters
Strings
String manipulation functions
String comparison functions
String I/O functions

### Slide 64: GROUP PROJECT

– Group Project
– Grouping
– Each team is formed with members from the same lab session
– Each team will have 5 members (adjustments will be made 
wherever needed)
– The final grouping will be announced on LMS
– Project specs will be uploaded to LMS soonest. 
– Plagiarism is strictly NOT allowed
– The group project is designed to help you to learn better.
– Do not copy from peers or from seniors or from other places
– Do not share your code with others or onto other platforms (e.g. 
GitHub)
65

### Slide 65: ABOUT USAGE OF AI TOOLS

– For Group Project
• AI tools are NOT allowed
• A declaration is needed from each team
– For Test
• AI tools are NOT allowed
66

---

## 10. Pointers

*Topics: Memory addresses, pointer variables, dereferencing, pointer arithmetic, arrays and pointers, call-by-reference.*

### Slide 2: RECAP FROM LAST WEEK

– Function
– A function prototype is a function 
definition without a body, e.g.
– int square(int);
2
return value type
function name
parameter list
int square(int y)
{
 return y * y;
}
return value

### Slide 3: CALL BY VALUE VS CALL BY REFERENCE

3
Call by Reference Call by Value

### Slide 4: SCOPE

– The scope of an identifier is the 
portion of the program in which the 
identifier can be referenced.
– Global VS Local variable
4

### Slide 5: ARRAY

An array is a group of memory locations 
that all have – the same name
– the same type
5

### Slide 6: STRING

A string in C is an array of characters ending 
in the null character ('\0').
6

### Slide 7: BEFORE WE START

– Project related matters
• Specs uploaded
• Grouping uploaded
– Double check your name, ID and Email
– Start discussing with your teammates
• Alert
– Be focused in this lecture
7

### Slide 8: Agenda

1. Pointers
2. Arrays and pointers
3. Call-by-reference
8

### Slide 9: For ALL variables:

– name, type, value
– How to use:
– Declare
– Initialize
– Use (assign new value/retrieve value)
– Two steps happened for the above code:
– Step 1 – declare : – int numberOfStudents_INF1002;
– A random value will be assigned to numberOfStudents_INF1002
– Step 2 – initialize (assign an initial value): – numberOfStudents_INF1002 = 300;
MORE ABOUT VARIABLES
9
int numberOfStudents_INF1002 = 300;

### Slide 10: MORE ABOUT VARIABLES

10
int numberOfStudents_INF1002 = 300;
printf(“Memory starting address: %p”, &numberOfStudents_INF1002);
printf(“Memory length: %d”, sizeof(numberOfStudents_INF1002);
Result:
Memory starting address: 0x0060FF05
Memory length: 4
0x0060FF05
0x0060FF06
0x0060FF07
0x0060FF08
0x0060FF09
– When a variable is declared:
– Memory space is automatically allocated for the variable
– When a variable is initialized/assigned with a value:
– The data in the allocated memory space will be updated 300
numberOfStudents_INF1002: integer
0x0060FF04
Memory Address Value

### Slide 11: MORE ABOUT VARIABLES

11
int numberOfStudents_INF1002 = 300;
int numberOfStudents_ICT2107 = 100;
0x0060FF05
0x0060FF06
0x0060FF07
0x0060FF08
0x0060FF09
300
numberOfStudents_INF1002: integer
0x0060FF0A
0x0060FF0B
0x0060FF0C
numberOfStudents_ICT2107: integer
100
Memory Address Value

### Slide 12: MORE ABOUT VARIABLES

12
numberOfStudents_ICT2107 = numberOfStudents_INF1002;
0x0060FF05
0x0060FF06
0x0060FF07
0x0060FF08
0x0060FF09
300
0x0060FF0A
0x0060FF0B
0x0060FF0C
300
0x0060FF05
0x0060FF06
0x0060FF07
0x0060FF08
0x0060FF09
300
0x0060FF0A
0x0060FF0B
0x0060FF0C
100
Memory Address Value Memory Address Value

### Slide 13: HOW TO OBTAIN MEMORY ADDRESS ALLOCATED FOR A

VARIABLE
– The addressof & operator returns the 
address of its operand.
13
0x0060FF05
0x0060FF06
0x0060FF07
0x0060FF08
0x0060FF09
300
0x0060FF0A
0x0060FF0B
0x0060FF0C
Starting memory address: &numberOfStudents_INF1002
Memory Address Value
int numberOfStudents_INF1002 = 300;

### Slide 14: POINTERS

### Slide 15: POINTER VARIABLES

Pointers are variables whose values are 
memory addresses.
100
0xF200 ptr: int*
0xF200
0xF300
count: int
int count = 100;
int* ptr = &count;
Type
Memory Address Value

### Slide 16: HOW TO USE?

– Declare
– int count;
– int *ptr;
– Initialize (initial value assignment)
– int count = 100;
– ptr = &count;
– Use: dereference (retrieve/update the 
value in the memory space it points to)
– int a = *ptr;
– *ptr = 200;
16
100
0xF200 ptr
0xF200
0xF300
count
0xF400 100 a
0xF200 200 count
Memory Address Value

### Slide 17: POINTER VARIABLE

DEFINITION
int *ptr;
* indicates that 
the variable 
being defined 
is a pointer:
“ptr is a 
pointer to an 
int”

### Slide 18: POINTER VARIABLE DEFINITION

int *ptr1, *ptr2;
int a, b;
Note: The asterisk (*) does not distribute to all 
variable names in a declaration. 
Each pointer must be declared with the * 
prefixed to the name.

### Slide 19: POINTER INITIALIZATION

7
count
0xF200 7
countPtr
0xF200
count directly references a variable 
that contain the value 7
countPtr indirectly references a 
variable that contains the value 7
A pointer contains an address of a 
variable that contains a specific value
int count = 7;
int *countPtr = &count;
0xF300
0xF200

### Slide 20: POINTER INITIALIZATION

The addressof &
operator returns the 
address of its 
operand.
Assign the address 
of y to yPtr
#include <stdio.h>
int main() {
 int y = 5;
 int *yPtr;
 yPtr = &y;
 printf("Address of y: %p\n", &y);
 printf("Value of yPtr: %p\n", yPtr);
 printf("Address of yPtr: %p\n", &yPtr);
 printf("Value to which yPtr points: %d\n",
 *yPtr);
 return 0;
}

### Slide 21: QUESTION

– Why not initialize a pointer variable 
with a direct value?
– i.e. 
– int *yPtr;
– yPtr = 0060FF0C;
21

### Slide 22: POINTER OPERATORS

The de-referencing operator returns the 
value of the object to which its operand points.
int main() {
 int y = 5;
 int *yPtr;
 yPtr = &y;
 printf("Address of y: %p\n", &y);
 printf("Value of yPtr: %p\n", yPtr);
 printf("Value to which yPtr points: %d\n", *yPtr);
 *yPtr = 10;
 
 printf("Value to which yPtr points: %d\n", *yPtr);
 printf("Value of y:%d\n", y);
 return 0;
}
The de-referencing 
operator is used to 
update the value of the 
object to which its 
operand points.

### Slide 23: POINTER OPERATORS

Dereferencing a pointer which has not been properly initialised or 
that has not been assigned to point to a specific location in memory 
is an error. 
This could cause a fatal run time error, or it could accidentally modify 
important data and allow the program to run to completion with 
incorrect results.
Memory Address Value

### Slide 24: EXERCISE

What are the values of a and b after 
each line of the following program?
24
int a = 5, b = 2;
int *p = &a, *q = &b;
(*p) *= 2; //a = ?, (*p) = (*p) * 2
*q = *p – 1;
p = &b;
b = *p + 3; //b = ?

### Slide 25: EXERCISE

What are the values of a and b after 
each line of the following program?
25
int a = 5, b = 2;
int *p = &a, *q = &b;
(*p) *= 2; //a = ?, (*p) = (*p) * 2
*q = *p – 1;
p = &b;
b = *p + 3; //b = ?

### Slide 26: POINTERS & ARRAYS

### Slide 27: POINTERS & ARRAYS

Pointers and arrays are intimately related in C.
– An array name can be thought of as a constant 
pointer to the start of the array.
– Array subscripts can be applied to pointers.
– Pointer arithmetic can be used to navigate 
arrays.
27

### Slide 28: int main() {

char charArray[] = {'a', 'b', 'c', 'd', 'e' };;
printf("charArray: \t%p\n", charArray);
printf("&chararray[0]: \t%p\n", &(charArray[0]));
printf(“&charArray: \t%p\n", &charArray);
return 0;
}
POINTERS & ARRAYS
28
The name of the array evaluates to the address of 
the first element of the array.
Output

### Slide 29: int main() {

char b[] = {'a', 'b', 'c', 'd', 'e' };
 char *bPtr = b;
 printf("*(bPtr + 3): \t%c\n", *(bPtr + 3));
 printf("*(b + 3): \t%c\n", *(b + 3));
 printf("bPtr[3]: \t%c\n", bPtr[3]);
return 0;
}
POINTERS & ARRAYS
29
*(bPtr + 3): d
*(b + 3): d
bPtr[3]: d
Subscripting and pointer arithmetic can be used 
interchangeably.
Output

### Slide 30: POINTERS & ARRAYS

The fourth element of b can be referenced 
using any of the following statements:
30
*(bPtr + 3) 
*(b+3)
3 is the offset to the pointer indicates which 
element of the array should be referenced
The array itself can be treated as a pointer to the 
first element of the array.
bPtr[3] pointers can be subscripted exactly as arrays can.

### Slide 31: EXERCISE

What are the contents of the array a
after each line of the following program?
31
int a[] = { 1, -1, 4, 5, 4, -3 };
int *p = a + 5;
*p = -(*p);
p -= 2;
*p = *p + 1;
*(p + 1) = *p * 2;

### Slide 32: EXERCISE

What are the contents of the array a
after each line of the following program?
32
int a[] = { 1, -1, 4, 5, 4, -3 };
int *p = a + 5;
*p = -(*p);
p -= 2;
*p = *p + 1;
*(p + 1) = *p * 2;

### Slide 33: POINTER EXPRESSIONS & ARITHMETIC

### Slide 34: THE SIZEOF OPERATOR

The sizeof operator returns the number of 
bytes required to hold a type.
• E.g.
– sizeof(char) evaluates to 1
– sizeof(int) evaluates to 2, 4 or 8 depending on the 
word size of the compiler
34

### Slide 35: THE SIZEOF OPERATOR

35
int size = sizeof(int) * 4;
printf("size of 4 integers is: 
%d bytes\n", size);
This gives the size 
of an integer.

### Slide 36: THE SIZEOF OPERATOR

36
int size = sizeof(int) * 4;
printf("size of 4 integers is:
%d bytes\n", size);
This gives the size 
of 4 integers.
Output:
size of 4 integers is: 16 bytes

### Slide 37: POINTER EXPRESSIONS & ARITHMETIC

In general, pointers are valid 
operands in 
– assignment expressions
– arithmetic expressions
– comparison expressions
37
However, not all the operators 
normally used in these expressions 
are valid in conjunction with 
pointer variables.

### Slide 38: POINTER ASSIGNMENT

A pointer can be assigned to another pointer if 
they have the same type.
38
anotherPtr will point to 
whatever memory location that 
ptr is pointing to
n 5
0x3000
0x3000 ptr
0x3434
0x3000 anotherPtr
0x4000

### Slide 39: POINTER EXPRESSIONS & ARITHMETIC

39
int v[5] = {0};
int *vPtr = v;
What is the 
result of
vPtr += 2;
v[0]
0x3000
v[1]
0x3004
v[2]
0x3008
v[3]
0x3012
v[4]
0x3016
0x3000
v
vPtr

### Slide 40: POINTER EXPRESSIONS & ARITHMETIC

40
int v[5] = {0};
int *vPtr = v;
What is the 
result of
vPtr += 2;
v[0]
0x3000
v[1]
0x3004
v[2]
0x3008
v[3]
0x3012
v[4]
0x3016
0x3000
v
vPtr
In conventional arithmetic, 3000+2 = 
3002. However, this is not the case 
with pointer arithmetic.
0x3002

### Slide 41: POINTER EXPRESSIONS & ARITHMETIC

41
v[0]
0x3000
v[1]
0x3004
v[2]
0x3008
v[3]
0x3012
v[4]
0x3016
0x3008
v
vPtr
0x3008 = 0x3000 + 2*sizeof(int)
When an integer is added or subtracted from a pointer, the pointer is 
incremented or decremented by that integer times the size of the object 
to which the pointer refers.
vPtr += 2;

### Slide 42: POINTER EXPRESSIONS & ARITHMETIC

42
v[0]
0x3000
v[1]
0x3004
v[2]
0x3008
v[3]
0x3012
v[4]
0x3016
0x3016
v
vPtr
if vPtr has been incremented 
to 0x3016, the statement
vPtr -=4;
would set vPtr to 0x3000.

### Slide 43: POINTER EXPRESSIONS & ARITHMETIC

43
v[0]
0x3000
v[1]
0x3004
v[2]
0x3008
v[3]
0x3012
v[4]
0x3016
0x3004
v
vPtr If vPtr has been reset to 
0x3000, the statement
vPtr++;
would set vPtr to 0x3004.

### Slide 44: POINTERS TO POINTERS

### Slide 45: POINTERS TO POINTERS

(int *): pointer to an integer
(int *)*: pointer to a pointer which points to 
an integer
Many uses in C:
– Arrays of pointers
– Arrays of strings
5
n
Address 
of n
ptr
Address 
of ptr
ptrToPtr
int n = 5;
int *ptr = &n;
int **ptrToPtr = &ptr;

### Slide 46: POINTERS TO POINTERS

#include <stdio.h>
int main() {
int n = 5;
int *ptr = &n;
int **ptrToPtr = &ptr;
printf("&n = %p\n", &n);
printf("ptr = %p\n", ptr);
printf("&ptr = %p\n", &ptr);
printf("ptrToPtr = %p\n", ptrToPtr);
/* illustrating the dereferencing operator * */
printf("*ptr = %d\n", *ptr);
printf("*ptrToPtr = %p\n", *ptrToPtr);
printf("ptr = %p\n", ptr);
printf("**ptrToPtr = %d\n", **ptrToPtr);
return 0;
}
Output

### Slide 47: POINTERS TO POINTERS

EXAMPLE – WHAT IS THE OUTPUT OF THIS PROGRAM?
int main() {
int a = 5;
int b = 6;
int *ptrA = &a;
int *ptrB = &b;
printf("At the start:\n");
printf("a = %d, b = %d\n", a, b);
printf("ptrA = %p, ptrB = %p\n\n", ptrA, ptrB);
/* test swapPointer() */
ptrA = &a;
ptrB = &b;
swapPointer(&ptrA, &ptrB);
printf("After swapPointer():\n");
printf("a = %d, b = %d\n", a, b);
printf("ptrA = %p, ptrB = %p\n\n", ptrA, ptrB);
/* test swapValue() */
ptrA = &a;
ptrB = &b;
swapValue(ptrA, ptrB);
printf("After swapValue():\n");
printf("a = %d, b = %d\n", a, b);
printf("ptrA = %p, ptrB = %p\n\n", ptrA, ptrB);
return 0;
}

### Slide 48: ARRAYS OF POINTERS

Arrays may contain pointers.
*illustration from Deitel & Deitel 48
char * suit[ 4 ] = { "Hearts", "Diamonds", "Clubs", "Spades" };
“an array of 
4 elements”
each element 
is of type 
“pointer to 
char”

### Slide 49: ARRAYS OF POINTERS - EXAMPLE

#include <stdio.h>
int main() {
 char *suit[4] = { "Hearts", "Diamonds", "Clubs", "Spades" };
 char *face[13] = {
 "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
 "Jack", "Queen", "King"
 };
 for (int i = 0; i < 4; i++) {
 char *card_suit = suit[i];
 for (int j = 0; j < 13; j++) {
 printf("%s of %s\n", face[j], card_suit);
 }
 }
 return 0;
}
49

### Slide 50: CALL-BY-REFERENCE

### Slide 51: CALLING FUNCTIONS BY VALUE

Recall call-by-value:
– A copy of the argument’s value is made 
and passed to the called function.
– Changes to the copy do not affect the 
original variable’s value in the caller.
– By default, all calls in C are by value.
53

### Slide 52: CALLING FUNCTIONS BY REFERENCE

In call-by-reference:
– The caller allows the called function to 
modify the original value.
– Call-by-reference can be simulated using 
a pointer in C.
54

### Slide 53: FUNCTIONS – CALL-BY-REFERENCE

55
Simulating callby-reference
When calling a 
function with 
arguments that 
should be modified, 
the addresses 
for the 
arguments are 
passed.
#include <stdio.h>
/* cube a number in-place */
void cubeByReference(int *);
int main() {
int number = 5;
cubeByReference(&number);
printf("number = %d\n", number);
return 0;
}
void cubeByReference(int *ptr) {
*ptr = (*ptr) * (*ptr) * (*ptr);
}
Output

### Slide 54: PASSING ARRAYS TO FUNCTIONS

int a[5] = { 0, 1, 2, 3, 4 };
To pass an array argument to a function, specify the 
name of the array without any brackets:
modifyArray(a, 5);
Suppose we have this array:
This function call passes array a and its size to function 
modifyArray.
56

### Slide 55: PASSING ARRAYS TO FUNCTIONS

void modifyArray(int b[], int size)
The square brackets tell 
the compiler that the 
function expects an array.
The size of the array is not 
required between the array 
brackets [].
57

### Slide 56: PASSING

ARRAYS TO 
FUNCTIONS
This function doubles the value of each element 
in the array. Will the contents of array a in 
main change after this function returns?
58
/* the first argument of this function is an array of integers */
void modifyArray(int [], int);
int main() {
int a[5] = {0, 1, 2, 3, 4};
modifyArray(a, 5);
return 0;
}
/* double every element of an array */
void modifyArray(int b[], int size) {
int j;
for (j = 0; j < size; j++)
b[j] *= 2;
}

### Slide 57: 59

C automatically passes arrays to 
functions by reference.
The called function can 
modify the element values in 
the callers’ original arrays.

### Slide 58: 60

This function 
prints the 
contents of 
the array
Output:
[Array] = 0 1 2 3 4
[Array] = 0 2 4 6 8
int main() {
int a[5] = {0, 1, 2, 3, 4};
printArray(a, 5);
modifyArray(a, 5);
printArray(a, 5);
return 0;
}
/* double every element of an array */
void modifyArray(int b[], int size) {
int j;
for (j = 0; j < size; j++)
b[j] *= 2;
}
void printArray(int b[], int size) {
int j;
printf("[Array] = ");
for (j = 0; j < size; j++)
printf("%d ", b[j]);
printf("\n");
}
This function 
doubles every 
element of an arry

### Slide 59: 61

Many times, you do not want 
a function to change the 
contents of the original array, 
so what do you do in this 
case?

### Slide 60: 62

Use const to 
prevent modification of 
values in an array in a 
functions.

### Slide 61: 63

When an array 
parameter is 
preceded by the 
const qualifier, 
the array elements 
become constant in 
the function body, 
and any attempt to 
modify an element 
of the array in the 
function body 
results in a compiletime error.
void tryToModifyArray(const int b[], int size) {
int j;
for (j = 0; j < size; j++)
b[j] *= 2;
}
const_array.c
const_array.c(28): error C2166: l-value specifies const object
Compiler Output

### Slide 62: END-OF-WEEK 10 CHECKLIST

64
Arrays & pointers
Pointer arithmetic
Passing arrays to functions
Call by reference
Arrays of pointers
Pointers to pointers
Pointer assignment
Void pointers
Pointer declarations
Address operator
Pointer dereferencing
Using const

---

## 11. Dynamic Memory Allocation and Linked Lists

*Topics: malloc, calloc, realloc, free, memory leaks, structs, linked lists.*

### Slide 2: RECAP OF LAST WEEK

2
Pointers are variables whose values are 
memory addresses.
100
0xF200 ptr: int*
0xF200
0xF300
count: int
int count = 100;
int* ptr = &count;

### Slide 3: HOW TO USE POINTER

3
– D: Declaration/definition
– int variable;
– int *ptr;
– I: Initialization (value assignment)
– int variable = 10;
– ptr = &variable;
– D: Dereference
– *ptr = 20; (update the value stored in the pointed memory space)
– int a = *ptr; (retrieve the value stored in the pointed memory space)

### Slide 4: POINTERS AND ARRAY

4
Pointers and arrays are intimately related in C.
– An array name can be thought of as a constant pointer to 
the start of the array.
– Array subscripts can be applied to pointers.
– Pointer arithmetic can be used to navigate arrays.
int main() {
 char b[] = {'a', 'b', 'c', 'd', 'e' };
 char *bPtr = b;
 printf("*(bPtr + 3): \t%c\n", *(bPtr + 3));
 printf("*(b + 3): \t%c\n", *(b + 3));
 printf("bPtr[3]: \t%c\n", bPtr[3]);
return 0;
}
*(bPtr + 3): d
*(b + 3): d
bPtr[3]: d
Output

### Slide 5: POINTER TO POINTER

5
(int *): pointer to an integer
(int *)*: pointer to a pointer which points to 
an integer
Many uses in C:
– Arrays of pointers
– Arrays of strings
5
n
Address 
of n
ptr
Address 
of ptr
ptrToPtr
int n = 5;
int *ptr = &n;
int **ptrToPtr = &ptr;

### Slide 6: Agenda

1. Void pointer
2. Dynamic memory allocation
3. User-defined data types
4. Linked lists
6

### Slide 7: VOID POINTER

7

### Slide 8: VOID POINTERS

8
All pointers can be 
assigned to a 
pointer to void.
A pointer to void
can point to a 
variable of any type.
int x;
void *xPtr = &x;
printf("xPtr: %p\n", xPtr);
float f;
void *fPtr = &f;
printf("fPtr: %p\n", fPtr);

### Slide 9: VOID POINTERS

9
A pointer to void cannot be dereferenced. 
Void pointers should always be cast before 
dereferencing.
float f = 123.45;
/* incorrect */
void *fPtr = &f;
printf("*fPtr: %f\n", *fPtr);
/* correct */
float *fPtr2 = (float *)fPtr;
printf("*fPtr2: %0.2f\n", *fPtr2);
void_pointers.c
void_pointers.c(16): error C2100: 
illegal indirection
The compiler says:

### Slide 10: DYNAMIC MEMORY ALLOCATION

10

### Slide 11: include <stdio.h>

#define NUM_STUDENTS 10
int main() {
int grades[NUM_STUDENTS];
int i;
for (i = 0; i < NUM_STUDENTS; i++) {
printf("Grade for student %d: ", i + 1);
scanf("%d", &grades[i]);
}
return 0;
}
WHY DYNAMIC MEMORY ALLOCATION?
11
NUM_STUDENTS has to 
be defined at compile 
time
This loop reads the 
grades for students
What happens if we do not know how many students 
we have in advance?

### Slide 12: 12

We need DYNAMIC
memory allocation

### Slide 13: DYNAMIC MEMORY ALLOCATION

Three steps to dynamic memory allocation:
13
1. include #include <stdlib.h>
2. malloc
int *ptr = (int *)malloc(sizeof(int)*N);
Use malloc or calloc to request memory. 
3. free free(ptr);
Free up the memory when no longer 
needed.

### Slide 14: MALLOC AND CALLOC

malloc allocates a block of memory with a given number of bytes
int *ptr = (int *)malloc(sizeof(int) * N);
calloc allocates a block of memory with space for a given number of elements, and 
sets them to zero
int *ptr = (int *)calloc(N, sizeof(int));
14
https://stackoverflow.com/questions/1538420/difference-between-malloc-and-calloc
malloc VS calloc

### Slide 15: MALLOC AND CALLOC

malloc and calloc return a void pointer to the start of the allocated memory
• it MUST be explicitly cast to the appropriate type before use
• it is often used like an array
• if not enough memory is available, the pointer 
has the special value NULL
15
int *grades = (int *)malloc(num_students * sizeof(int));
for (i = 0; i < num_students; i++)
grades[i] = …;

### Slide 16: THE SIZEOF OPERATOR

To be able to allocate memory dynamically, we 
need to tell the compiler the size of memory 
we need at runtime.
The sizeof operator returns the number of 
bytes required to hold a type.
• E.g.
– sizeof(char) evaluates to 1
– sizeof(int) evaluates to 2, 4 or 8 depending on the 
word size of the compiler
16

### Slide 17: THE SIZEOF OPERATOR

17
int size = sizeof(int) * 4;
printf("size of 4 integers is: 
%d bytes\n", size);
This gives the size 
of an integer.

### Slide 18: THE SIZEOF OPERATOR

18
int size = sizeof(int) * 4;
printf("size of 4 integers is:
%d bytes\n", size);
This gives the size 
of 4 integers.
Output:
size of 4 integers is: 16 bytes

### Slide 19: FREE

free de-allocates memory previously allocated by malloc or calloc
• all memory allocated by malloc or calloc
should eventually be free’d
• this allows the memory to be re-used
• failure to de-allocate memory is called a memory leak
• a leaking program will use up more and more 
memory over time, and eventually crash
19

### Slide 20: EXAMPLE

20
#include <stdio.h>
#include <stdlib.h>
int main() {
 int *grades;
 int num_students;
 /* ask how many grades need to be stored */
 printf("How many students are in your class? ");
 scanf("%d", &num_students);
 /* allocate enough space to hold num_students integers */
 grades = (int *)malloc(num_students * sizeof(int));
 if (grades == NULL) {
 printf("Out of memory.");
 return 1;
 }
 /* read the grades */
 for (int i = 0; i < num_students; i++) {
 printf("Grade for student %d: ", i + 1);
 scanf("%d", &grades[i]);
 }
 /* de-allocate memory */
 free(grades);
 return 0;
}
With dynamic memory 
allocation, we can set the 
number of students at run 
time.
If there is not enough 
memory, malloc returns 
NULL.
Use free to de-allocate memory 
when it is no longer required.

### Slide 21: DYNAMIC MEMORY ALLOCATION

STRINGS
21
/* allocate enough space to hold num_students strings */
 char **names = (char **)malloc(num_students * sizeof(char *));
 if (names == NULL) {
 printf("Out of memory.");
 return 1;
 }
 for (i = 0; i < num_students; i++) {
 /* read the name */
 printf("Name of student %d: ", i + 1);
 fgets(buf, MAX_NAME, stdin);
 /* copy the name into the array */
 int length = strchr(buf, '\n') - buf;
 names[i] = (char *)calloc(length + 1, sizeof(char));
 if (names[i] == NULL) {
 printf("Out of memory.");
 return 1;
 }
 strncpy(names[i], buf, length);
 }
 /* de-allocate memory */
 for (i = 0; i < num_students; i++)
 free(names[i]);
 free(names);
names is an array of pointers 
to characters.
Allocate space for each string 
according to its length.
Invoke free for each allocated 
block of memory.
Self-exercise: names_dynamic.c

### Slide 22: USER-DEFINED DATA TYPES

### Slide 23: STRUCTURES

Name Sachin Kumar
Roll 101
Age 16
Class INF1002
Suppose you want to 
represent this 
information about a 
student.
23

### Slide 24: STRUCTURES

struct <name> {
member 1;
member 2;
:
member n;
};
24
C allows structured collections of 
information to be defined using the 
struct keyword.
struct student {
char name[20];
int roll;
int age;
char class[12];
};

### Slide 25: DECLARE STRUCTURES VARIABLE

Option #2:
struct student {
char name[20];
int roll;
int age;
char class[12];
} student_2, student_3;
The code above declares 3 variables of type struct 
student, called student_1, student_2, and 
student_3
25
Option #1:
struct student {
char name[20];
int roll;
int age;
char class[12];
};
struct student student_1;

### Slide 26: USE STRUCTURE VARIABLE

26
/*
* struct example from Sharma
*/
#include <stdio.h>
struct student {
char name[20];
int roll;
int age;
char class[12];
};
int main() {
/* initialise a variable of type student */
struct student stud1 = { "Sachin Kumar", 101, 16, "INF1002" };
/* display contents of stud1 */
printf("\n Name : %s", stud1.name);
printf("\n Roll : %d", stud1.roll);
printf("\n Age : %d", stud1.age);
printf("\n Class: %s", stud1.class);
return 0;
}
Name : Sachin Kumar
Roll : 101
Age : 16
Class: INF1002
Output
Use the dot
operator to refer 
to members of a 
structure.
Structures 
can be 
initialised 
similar to
arrays.

### Slide 27: PASSING STRUCTURES TO FUNCTIONS BY REFERENCE

27
/*
* struct example with functions
*/
#include <stdio.h>
void print_student(Student *s);
int main() {
/* initialise a variable of type Student */
Student stud1 = { "Sachin Kumar", 101, 16, "INF1002" };
/* display contents of stud1 */
print_student(&stud1);
return 0;
}
void print_student(Student *s) {
printf("\n Name : %s", s->name);
printf("\n Roll : %d", s->roll);
printf("\n Age : %d", s->age);
printf("\n Class: %s", s->class);
}
Use the “->” 
arrow operator to 
de-reference a 
pointer to a 
structure.
Structures 
can be 
passed by 
reference.

### Slide 28: HOW TO MAKE IT SHORT?

– struct student stud1 = { “Bill 
Gates", 101, 16, "INF1002" };
– struct student stud2 = { “Elon 
Musk", 102, 16, “INF1003" };
– …
28

### Slide 29: LIFE EXAMPLE

– Singapore Institute of Technology is Singapore’s University 
of Applied Learning. Singapore Institute of Technology’s 
vision is to be a leader in innovative learning by integrating 
learning, industry and community. Singapore Institute of 
Technology’s mission is to nurture and develop individuals 
who build on their interests and talents to impact society in 
meaningful ways.
– Singapore Institute of Technology (from now on referred 
as “SIT”) is Singapore’s University of Applied Learning. 
SIT’s vision is to be a leader in innovative learning by 
integrating learning, industry and community. SIT’s 
mission is to nurture and develop individuals who build 
on their interests and talents to impact society in 
meaningful ways.
29

### Slide 30: USER-DEFINED DATA TYPES - TYPEDEF

User-defined data types can be declared using typedef:
<type> can be a basic data type or struct
<new_type> is the user-defined data type
typedef <type> <new_type>
30

### Slide 31: USER-DEFINED DATA TYPES - TYPEDEF

struct student {
char name[20];
int roll;
int age;
char class[12];
};
typedef (struct student) Student;
/* initialise a variable of type Student */
Student student_1 = { "Sachin Kumar", 101, 16, "INF1002" };
32

### Slide 32: USER-DEFINED DATA TYPES - TYPEDEF

typedef struct {
char name[20];
int roll;
int age;
char class[12];
} Student;
/* initialise a variable of type student */
Student student_1 = { "Sachin Kumar", 101, 16, "INF1002" };
33
We can make it even more concise!!!

### Slide 33: USER-DEFINED DATA TYPES - TYPEDEF

typedef float salary; 
salary wages_of_month;
In this example wages_of_month is of type 
salary which is a float by itself.
This enhances the readability of the program.
34

### Slide 34: THE SIZEOF OPERATOR

35
typedef struct {
int id;
char name[25];
} Student;
The sizeof operator can also be used with 
user-defined types: 
printf("The size of a Student record is:
%d bytes\n", sizeof(Student));

### Slide 35: LINKED LISTS

### Slide 36: 37

Why are you teaching 
us Linked Lists? We 
are happy with arrays!
Arrays need contiguous 
memory slots. With a 
linked list, you can 
optimise memory by 
linking data at different
memory locations.
Array
Linked list

### Slide 37: LIFE EXAMPLE

38
– The professor (me) left his water bottle in 
the classroom and one student found it and 
kept it for the professor
– There are 5 students: A, B, C, D, E
– A knows the address of B, B knows the 
address of C, and so forth
– I only know the address of A.
– Q: how can I get my bottle back?

### Slide 38: LINKED LISTS

39
link
12 13 5 7 X
A linked list is a linear collection of 
self-referential structures, called 
nodes, connected by pointers, called 
links.
node node node node

### Slide 39: typedef struct node_struct {

int data;
 struct node_struct *next;
} Node;
SELF-REFERENTIAL 
STRUCTURES A selfreferential 
structure 
contains a 
pointer 
member that 
points to a 
structure of the 
same type
40

### Slide 40: SELF-REFERENTIAL

STRUCTURES Self-referential 
structures can 
be linked
together to 
form useful 
data structures 
such as linked 
lists, queues, 
stacks and 
trees.
41
typedef struct node_struct {
 int data;
 struct node_struct *next;
} Node;

### Slide 41: node1 node2 42

How do you create two nodes and 
link node1 to node2?
int main() {
Node node1 = { 15, NULL };
Node node2 = { 10, NULL };
node1.next = &node2;
}

### Slide 42: int main() {

Node node1 = { 15, NULL };
Node node2 = { 10, NULL };
node1.next = &node2;
printf("node1.data = %d\n", node1.data);
printf("node1.next = %p\n", node1.next);
}
ACCESSING DATA IN A LINKED LIST
Use the dot “.”
notation for non- pointer variables
43

### Slide 43: int main() {

Node node1 = { 15, NULL };
Node node2 = { 10, NULL };
node1.next = &node2;
Node *node_ptr = &node1;
printf("node1.data = %d\n", node_ptr->data);
node_ptr = node_ptr->next;
printf("node2.data = %d\n", node_ptr->data);
}
ACCESSING DATA IN A LINKED LIST
44
Use the arrow 
“->” operator for 
pointer variables

### Slide 44: ACCESSING DATA IN A LINKED LIST

45
head
12 13 5 7 X
A linked list is accessed 
via a pointer to the first 
node (head).
Subsequent nodes are 
accessed via the link in 
each node.
By convention: the 
link pointer in the 
last node points to 
NULL.

### Slide 45: LINKED LIST OPERATIONS

46
Search/update
Insert
Delete

### Slide 46: 47

head
12 13 5 7 X
temp
temp is a pointer to the first node of 
the list.
How do we move temp to the node 
containing 5?
LINKED LIST OPERATIONS Search

### Slide 47: 48

Using the next pointer
head
12 13 5 7 X
temp
LINKED LIST OPERATIONS Search
temp = temp->next;

### Slide 48: 49

Using the next pointer
head
12 13 5 7 X
temp
LINKED LIST OPERATIONS Search
temp = temp->next;
temp = temp->next;

### Slide 49: LINKED LIST OPERATIONS

50
head
100 X 12 13 5 7 X
new_node
Node *new_node = (Node *)malloc(sizeof(Node));
new_node->data = 100;
new_node->next = NULL;
How do we insert new_node at the 
beginning of the list?
Insert

### Slide 50: LINKED LIST OPERATIONS

51
head
100 12 13 5 7 X
new_node->next = head;
1. Link the new node to the old head.
Insert
new_node

### Slide 51: LINKED LIST OPERATIONS

52
100 12 13 5 7 X
head
new_node->next = head;
head = new_node;
2. Move the head to the new node.
Insert

### Slide 52: How do we delete the node pointed to

by node_ptr?
LINKED LIST OPERATIONS
53
head
12 13 5 7 X
node_ptr
Delete

### Slide 53: 54

head
12 13 5 7 X
prev_ptr
prev_ptr->next = node_ptr->next;
free(node_ptr);
How do we get prev_ptr?
Delete LINKED LIST OPERATIONS
node_ptr
Don’t 
forget to 
free the 
node if it 
was created 
by malloc.

### Slide 54: 55

head
12 13 5 7 X
temp
Node* Find_Pre_Node()
{
Node *temp = head;
while (temp->next != NULL)
{
if (temp->next == node_ptr){
return temp;
}
temp = temp->next;
}
}
LINKED LIST OPERATIONS Delete
node_ptr

### Slide 55: END-OF-WEEK CHECKLIST

56
Dynamic memory allocation
malloc() and free()
The sizeof operator
Self-referential structures
Linked lists
Linked lists vs arrays
Searching & updating lists
Inserting into linked lists
Deleting from linked lists
User-defined data types
Dot operators

---

## 12. File I/O in C

*Topics: fopen, fclose, fprintf, fscanf, fread, fwrite, fseek, sequential vs random access.*

### Slide 2: Agenda

1. Files (sample code uploaded to LMS)
2. Recap of all past lectures
2

### Slide 3: FILES

3

### Slide 4: INTRODUCTION

4
Storage of data 
in variables and 
arrays is 
temporary—such 
data is lost when 
a program 
terminates.
Files are used for 
permanent 
retention of data. 
Computers store 
files on secondary
storage devices 
such as hard disks 
and flash memory.

### Slide 5: FILES & STREAMS

C views each file as a sequential stream
of bytes. Each file ends at the end-of-file 
(EOF) marker.
5

### Slide 6: STREAMS

6
Files Programs
Streams
When a file is opened, a stream is 
associated with the file

### Slide 7: BASIC FILE OPERATIONS

– Create a new file and write content into it 
– Open an existing file and read content from it
– Basic functions:
– fopen
– fprintf
– fscanf
– feof
– fclose
– fseek
– fread
– fwrite
– …
7

### Slide 8: CREATING AND WRITING INTO A TEXT FILE

8

### Slide 9: SAMPLE: CREATING AND WRITING A TEXT FILE

9
#include <stdio.h>
int main() {
/* declare a pointer to a FILE structure */
FILE *f;
/* open the file with fopen() */
f = fopen(“create_file.txt", "w");
if (f == NULL) {
printf("Could not open data.txt.\n");
return 1;
}
/* write to the file with fprintf() */
fprintf(f, "Hello! This is a new file.\n");
/* close the file with fclose() */
fclose(f);
return 0;
}
Step 2: Write to the file using
fprintf()
Step 1: Open the file
using fopen()
Step 0: declare a 
pointer to a FILE 
structure
Step 3: Close the file using 
fclose()
create_file.c

### Slide 10: “FILE” STRUCTURE

– A structure data type
– Contains info to control a stream
– The content info is not meant to be 
accessed from outside the functions of 
the <stdio.h> and <cwchar.h>
10
From stdio.h in MinGW32 5.1.4
Only for your reference:

### Slide 11: STEP 1: OPEN (AND CREATE) A TEXT FILE

File opening modes for text files:
11
FILE *fopen(const char *filename, const char *mode);
f = fopen("data.txt", "w");
Opens the file whose name is specified in the parameter filename and 
associates it with a stream. The operations that are allowed on the stream and 
how these are performed are defined by the mode parameter.

### Slide 12: STEP 2: WRITE TO A TEXT FILE

12
fprintf(f, "Hello! This is a new file.\n");
Writes the C string pointed by format to the stream. If format includes format 
specifiers (subsequences beginning with %), the additional arguments following 
format are formatted and inserted in the resulting string replacing their respective 
specifiers.
int fprintf ( FILE * stream, const char * format, ... );

### Slide 13: STEP 3: CLOSE A TEXT FILE

Closes the file associated with the stream and disassociates it.
13
fclose(f);
int fclose ( FILE * stream );

### Slide 14: READING FROM A TEXT FILE

14
How do you take out an elephant from the refrigerator?

### Slide 15: READ DATA FROM A TEXT FILE

Reads data from the stream and stores them according to the 
parameter format into the locations pointed by the additional 
arguments.
15
fscanf (f, "%d%19s%lf", &account, name, &balance);
int fscanf ( FILE * stream, const char * format, ... );

### Slide 16: READING FROM A TEXT FILE - EXAMPLE

16
#include <stdio.h>
int main() {
FILE *f;
int account;
char name[20];
double balance;
/* open the file */
f = fopen(“read_from_file.txt", "r");
if (f == NULL) {
printf("Could not open credit.txt.\n");
return 1;
}
/* read until the end of the file */
printf("%10s\t%20s\t%10s\n", "Account", "Name", "Balance");
while (!feof(f)) {
/* read one record */
fscanf(f, "%d%19s%lf", &account, name, &balance);
/* display it to the screen */
printf("%10d\t%20s\t%10.2lf\n", account, name, balance);
}
/* clean up */
fclose(f);
return 0;
}
Step 0: declare a 
pointer to a FILE 
structure
Step 1: Open the file using fopen()
Step 2: Read data from the file using fscanf()
Step 3: Close the file using fclose()
read_from_file.c
feof() returns a true value if
the file pointer is at the end
of the file.

### Slide 17: 17

The above code will go through all content from the beginning until reaching the EOF. 
What if we want to read/write data at a random location inside a file?
QUESTION
#include <stdio.h>
int main() {
FILE *f;
int account;
char name[20];
double balance;
/* open the file */
f = fopen(“read_from_file.txt", "r");
if (f == NULL) {
printf("Could not open credit.txt.\n");
return 1;
}
/* read until the end of the file */
printf("%10s\t%20s\t%10s\n", "Account", "Name", "Balance");
while (!feof(f)) {
/* read one record */
fscanf(f, "%d%19s%lf", &account, name, &balance);
/* display it to the screen */
printf("%10d\t%20s\t%10.2lf\n", account, name, balance);
}
/* clean up */
fclose(f);
return 0;
}
read_from_file.c

### Slide 18: TWO STREAM OPENING MODES

Streams may be opened 
in one of two modes:
– text mode is used for 
reading and writing text 
files
– files are divided into 
lines by new line 
characters
– e.g. plain text, source 
code, HTML, XML, 
etc.
– binary mode is used 
for reading and writing 
all other files
– files are made up of raw 
bytes
– e.g. images, videos, 
databases, etc.
18

### Slide 19: 19

There are two elephants in the refrigerator now. How can I 
insert a new elephant between the two elephants???

### Slide 20: RANDOM ACCESS FILES

A random access file can be read or 
written in any order.
Writing to one part of the file does not 
change another part of the file.
20

### Slide 21: RANDOM ACCESS FILES

The simplest kind of random access file 
consists of a series of records of fixed 
length:
21

### Slide 22: RANDOM ACCESS FILES

22
Every record in a 
random access file has 
the same length
The exact location of a 
record can be calculated 
from the record key and 
length.

### Slide 23: RANDOM ACCESS FILES

23
Fixed-length records enable data to be 
inserted/updated/deleted in a random access file 
without destroying other data

### Slide 24: STEP 1: OPENING A RANDOM ACCESS FILE

f = fopen(filename, "wb+");
24
rb Opens an existing binary file for reading.
wb Opens a binary file for writing. If it does not exist, a new file is created. 
If it exists, it will be overwritten.
ab Opens a binary file for appending. If it does not exist, a new file is 
created.
rb+ Opens a binary file for reading and writing both.
wb+ Opens a binary file for reading and writing both. 
ab+ Opens a binary file for reading and writing both. 
Binary file opening modes:
f = fopen(filename, “wb+");

### Slide 25: STEP 2: USE FSEEK TO MOVE TO A SPECIFIC

POSITION IN THE FILE
Sets the position indicator associated with the stream to a new position. 
For streams open in binary mode, the new position is defined by 
adding offset to a reference position specified by origin.
25
fseek(f, (client.acc_num - 1) * sizeof(Client), SEEK_SET);
int fseek ( FILE * stream, long int offset, int origin );
origin

### Slide 26: STEP 3: USE FWRITE/FREAD TO WRITE/READ

Writes an array of count elements, each one with a size of size bytes, from the block of memory pointed by ptr to the current position in the stream.
26
fwrite(&client, sizeof(Client), 1, f);
size_t fwrite ( const void * ptr, size_t size, size_t count, FILE * stream );
fread(&client, sizeof(Client), 1, f);
size_t fread ( void * ptr, size_t size, size_t count, FILE * stream );
Reads an array of count elements, each one with a size of size bytes, from 
the stream and stores them in the block of memory specified by ptr.

### Slide 27: SAMPLE: READ FROM RANDOM ACCESS FILE

27
/*
* Random access file example.
*/
#include <stdio.h>
/* this structure holds the data for one client */
typedef struct client_struct {
 int acc_num;
 char last_name[15];
 char first_name[10];
 double balance;
} Client;
int main() {
const char *filename = "random_access_write.dat";
FILE *f;
Client client;
/* open the data file */
f = fopen(filename, "rb");
if (f == NULL) {
printf("Could not open %s.\n", filename);
return;
}
/* print title */
printf("%-6s%-16s%-11s%10s\n", "Acct", "Last Name", "First Name", "Balance");
/* read one record at a time until we reach EOF */
fread(&client, sizeof(Client), 1, f);
while (!feof(f)) {
if (client.acc_num != 0)
printf("%-6d%-16s%-11s%10.2lf\n", client.acc_num, client.last_name, 
client.first_name, client.balance);
fread(&client, sizeof(Client), 1, f);
}
fclose(f);
}
Step 2: Read the data from the
present position in the file
Step 1: Open the file using
fopen() in binary mode
Step 0: declare a pointer 
to a FILE structure
Step 3: Close the file using fclose()

### Slide 28: SAMPLE: READ FROM RANDOM ACCESS FILE

– random_access_read.c
28

### Slide 29: SAMPLE: WRITE TO RANDOM ACCESS FILE

29
#include <stdio.h>
/* this structure holds the data for one client */
typedef struct client_struct {
 int acc_num;
 char last_name[15];
 char first_name[10];
 double balance;
} Client;
int main() {
const char *filename = "random_access_write.dat";
FILE *f;
Client client;
/* open the data file */
f = fopen(filename, "wb+");
if (f == NULL) {
printf("Could not open %s.\n", filename);
return;
}
/* read account data from the user */
printf("Enter account number (1-100, 0 to end)\n? ");
scanf("%d", &client.acc_num);
while (client.acc_num != 0) {
/* read the data for this record */
printf("Enter last name, first name and balance\n? ");
scanf("%14s%9s%lf", client.last_name, client.first_name, &client.balance);
/* go to this record's position in the file */
fseek(f, (client.acc_num - 1) * sizeof(Client), SEEK_SET);
/* write the client data structure */
fwrite(&client, sizeof(Client), 1, f);
/* ask for another record */
printf("Enter account number (1-100, 0 to end)\n? ");
scanf("%d", &client.acc_num);
}
fclose(f);
return 0;
}
random_access_write.c
Step 2: Move to a certain position
of the file
Step 1: Open the file using
fopen() in binary mode
Step 0: declare a pointer 
to a FILE structure
Step 3: Write to the file using 
fwrite() Step 4: Close the file using 
fclose()

### Slide 30: SAMPLE: WRITE TO RANDOM ACCESS FILE

– “random_access_write.c
30

### Slide 31: END-OF-WEEK CHECKLIST

31
Files
Streams
Opening a file
Writing to a file
Reading from a file
Sequential access files
Random access files

### Slide 32: TAKE A LOOK BACK

### Slide 33: A SIMPLE C PROGRAM

33
/*
* Hello World program in C.
*/
#include <stdio.h>
int main() {
printf("Hello world!\n");
return 0;
}

### Slide 34: 34

C programs 
contain one or 
more functions, 
one of which 
MUST be main. 
Every program in 
C begins 
execution in 
main.
/*
* Hello World program in C.
*/
#include <stdio.h>
int main() {
printf("Hello world!\n");
return 0;
}

### Slide 35: 35

#DEFINE/#INCLUDE PRE-PROCESSOR DIRECTIVE
The #define 
directive creates 
symbolic constants.
All subsequent 
occurrences of 
NUM_STUDENTS will be 
replaced with 140.
#include <stdio.h>
#define NUM_STUDENTS 140
int main() {
 int scores[NUM_STUDENTS];
 for (int i = 0; i < NUM_STUDENTS; i++) {
 scores[i] = 0;
 }
 return 0;
}
#include <stdio.h>
#define NUM_STUDENTS 140
int main() {
 int scores[NUM_STUDENTS];
 for (int i = 0; i < NUM_STUDENTS; i++) {
 scores[i] = 0;
 }
 return 0;
}
The #include 
directive causes a copy 
of a specified file to be 
included in place of 
the directive.

### Slide 36: 36

PRINTF
conversion-specifier = <flags><field width><precision><literal character>
printf( "%-10s%-10d%-10c%-10.3f\n", 
"hello", 7, 'a', 1.23 );
flag field width literal character
precision

### Slide 37: 37

SCANF – READING FORMATTED INPUT
scanf(format-control-string, other-arguments);
Output
printf("Enter seven integers: ");
scanf("%d%i%i%i%o%u%x", &a, &b, &c, &d, &e, &f, &g);
printf("The input displayed as decimal integers is:\n");
printf("%d %d %d %d %d %d %d", a, b, c, d, e, f, g);
Enter seven integers: -70 -70 070 0x70 70 70 70
The input displayed as decimal integers is:
-70 -70 56 112 56 70 112

### Slide 38: 38

C CONTROL STRUCTURES
C has the same control structures as 
other programming languages:
– if-else
– switch
– for
– while
– do-while

### Slide 39: FUNCTION

39
– Function
– A function prototype is a function 
definition without a body, e.g.
– int square(int);
return value type
function name
parameter list
int square(int y)
{
 return y * y;
}
return value

### Slide 40: SCOPE

– The scope of an identifier is the 
portion of the program in which the 
identifier can be referenced.
– Global VS Local variable
40

### Slide 41: ARRAY

An array is a group of memory locations 
that all have – the same name
– the same type
41

### Slide 42: STRING

A string in C is an array of characters ending 
in the null character ('\0').
42

### Slide 43: POINTER

43
Pointers are variables whose values are 
memory addresses.
100
0xF200 ptr: int*
0xF200
0xF300
count: int
int count = 100;
int* ptr = &count;

### Slide 44: HOW TO USE POINTER

44
– D: Declaration/definition
– int variable;
– int *ptr;
– I: Initialization (value assignment)
– int variable = 10;
– ptr = &variable;
– D: Dereference
– *ptr = 20; (update the value stored in the pointed memory space)
– int a = *ptr; (retrieve the value stored in the pointed memory space)

### Slide 45: POINTERS AND ARRAY

45
Pointers and arrays are intimately related in C.
– An array name can be thought of as a constant pointer to 
the start of the array.
– Array subscripts can be applied to pointers.
– Pointer arithmetic can be used to navigate arrays.
int main() {
 char b[] = {'a', 'b', 'c', 'd', 'e' };
 char *bPtr = b;
 printf("*(bPtr + 3): \t%c\n", *(bPtr + 3));
 printf("*(b + 3): \t%c\n", *(b + 3));
 printf("bPtr[3]: \t%c\n", bPtr[3]);
return 0;
}
*(bPtr + 3): d
*(b + 3): d
bPtr[3]: d
Output

### Slide 46: POINTER TO POINTER

46
(int *): pointer to an integer
(int *)*: pointer to a pointer which points to 
an integer
Many uses in C:
– Arrays of pointers
– Arrays of strings
5
n
Address 
of n
ptr
Address 
of ptr
ptrToPtr
int n = 5;
int *ptr = &n;
int **ptrToPtr = &ptr;

### Slide 47: 47

CALL BY VALUE VS CALL BY REFERENCE
Call by Reference Call by Value

### Slide 48: STRUCTURES

48
struct <name> {
member 1;
member 2;
:
member n;
};
C allows structured collections of 
information to be defined using the 
struct keyword.

### Slide 49: DYNAMIC MEMORY ALLOCATION

– Three steps to dynamic memory allocation:
49
1. include #include <stdlib.h>
2. malloc
int *ptr = (int *)malloc(sizeof(int)*N);
Use malloc or calloc to request memory. 
3. free free(ptr);
Free up the memory when no longer 
needed.

### Slide 50: FREE ALLOCATED MEMORY

50
free de-allocates memory previously allocated by malloc or calloc
• all memory allocated by malloc or calloc
MUST be free’d
• this allows the memory to be re-used
• failure to de-allocate memory is called a memory leak
• a leaking program will use up more and more 
memory over time, and eventually crash

### Slide 51: LINKED LIST

51
link
12 13 5 7 X
A linked list is a linear collection of 
self-referential structures, called 
nodes, connected by pointers, called 
links.
node node node node

### Slide 52: node1 node2 52

How do you create two nodes and 
link node1 to node2?
int main() {
Node node1 = { 15, NULL };
Node node2 = { 10, NULL };
node1.next = &node2;
}

### Slide 53: 53

LINKED LIST OPERATIONS
Search/update
Insert
Delete

---

# Part 3: C Code Examples

## 13. All C Code Examples

All `.c` files from the module, organized by topic.

### Basics

#### `hello.c`

```c
/*
 * A simple C program.
 */
#include <stdio.h>

int main() {

	printf("Hello world! abcdefg\n");

    printf("Hello world!     \n");

	return 0;

}
```

#### `sum.c`

```c
/*
 * Another simple C program.
 */
#include <stdio.h>

int main() {

	int integer1, integer2, sum;
	
	printf("Enter two numbers to add\n");
	scanf("%d%d", &integer1, &integer2);
	
	sum = integer1 + integer2;
	
	printf("Sum of entered numbers = %d\n", sum);
	
	return 0;
	
}
```

#### `datatypes.c`

```c
/*
 * Data types program example.
 */
#include <stdio.h>

int main() {

	int	a = 3000;			/* integer data type */
	float	b = 4.5345;			/* floating point data type */
	char	c = 'A';			/* character data type */
	long	d = 31456;			/* long integer data type */
	double	e = 5.1234567890;	/* double-precision floating point data type */
	
	printf("Here the list of the basic data types\n");
	printf("\n1. This an integer (int): %d", a);
	printf("\n2. This is a floating point number (float): %f", b);
	printf("\n3. This is a character (char): %c", c);
	printf("\n4. This is a long integer (long): %ld", d);
	printf("\n5. This is a double-precision float (double): %.10f", e);
	printf("\n6. This is a sequence of characters: %s", "Hello ICT1002 students");
	
	return 0;
	
}
```

#### `fieldwidth.c`

```c
/*
 * Printing field width example adapted from Deitel & Deitel [2]
 */
#include <stdio.h>

int main() {

	printf("%4d\n", 1);
	printf("%04d\n", 1);
	printf("%-4d\n", 1);
	printf("%4d\n", 12);
	printf("%4d\n", 123);
	printf("%4d\n", 1234);
	printf("%4d\n", 12345);
	
	return 0;
}
```

#### `scanf.c`

```c
/*
 * Reading formatting input with scanf.
 */
#include <stdio.h>

int main() {

	int a, b, c, d, e, f, g;

	printf("Enter seven integers: ");
	scanf("%d%i%i%i%o%u%x", &a, &b, &c, &d, &e, &f, &g);
	
	printf("The input displayed as decimal integers is:\n");
	printf("%d %d %d %d %d %d %d", a, b, c, d, e, f, g);
	
	return 0;
	
}
```

#### `define.c`

```c
#define NUM_STUDENTS 140

int main() {

    int scores[NUM_STUDENTS];

    for (int i = 0; i <= NUM_STUDENTS; i++) {
        scores[i] = 0;
    }

    return 0;

}
```

#### `enum.c`

```c
/*
 * Enumerated data type example.
 */
#include <stdio.h>

enum colour {
	Blue,
	Yellow,
	White,
	Black
};

int main() {

	enum colour colourIndex;
	
	for (colourIndex = Blue; colourIndex <= Black; colourIndex++) {
	
		switch (colourIndex) {
			case Blue:
				printf("Blue's index is: \t%d\n", Blue);
				break;
			case Yellow:
				printf("Yellow's index is: \t%d\n", Yellow);
				break;
			case White:
				printf("White's index is: \t%d\n", White);
				break;
			case Black:
				printf("Black's index is: \t%d\n", Black);
				break;
		}
	}
}
```

### Functions

#### `addition.c`

```c
/*
 * Function definition example.
 * From http://www.programmingsimplified.com
 */
#include <stdio.h>

/* function prototype */
int addition(int, int);

int main() {

	int first, second, sum;
	
	/* read input */
	scanf("%d%d", &first, &second);
	
	/* invoke the addition function */
	sum = addition(first, second);
	printf("%d\n", sum);
	
	return 0;
}


/* function implementation */
int addition(int a, int b) {

	int result;
	result = a + b;
	
	return result;
}
```

#### `absolute_value.c`

```c
#include <stdio.h>

int iabs(int);

int main()
{
    int x;

    printf("Enter a number: ");
    scanf("%d", &x);
    printf("%d\n", iabs(x));

    return 0;
}

int iabs(int n)
{
    /* to be implemented */

    return 0;
}
```

#### `multiple_return.c`

```c
#include <stdio.h>

#define POSITIVE 1
#define NEGATIVE -1
#define ZERO     0

int get_sign(int n);

int main() {

    int n;
    int sign;

    printf("Type an integer: ");
    scanf("%d", &n);

    sign = get_sign(n);
    if (sign == POSITIVE)
        printf("That is a positive number.\n");
    else if (sign == NEGATIVE)
        printf("That is a negative number.\n");
    else
        printf("That is zero.\n");

    return 0;
}

int get_sign(int n) {

    if (n < 0)
        return NEGATIVE;
    if (n > 0)
        return POSITIVE;

    return ZERO;
}
```

#### `call_by_value.c`

```c
/*
 * Call-by-value example.
 */
#include <stdio.h>

void call_by_value(int);

int main() {

	int a = 10;
	
	printf("Before call_by_value, a = %d.\n", a);
	call_by_value(a);
	printf("After call_by_value, a = %d.\n", a);
	
	return 0;
}

/* this function will make a copy of a */
void call_by_value(int x) {

	printf("Inside call_by_value, x = %d.\n", x);
	x += 10;
	printf("After adding ten, x = %d.\n", x);
}
```

#### `call_by_reference.c`

```c
/*
 * Passing arrays to functions, use of const.
 */
#include <stdio.h>

/* cube a number in-place */
void cubeByReference(int *);

int main() {

	int number = 5;
	cubeByReference(&number);
	printf("number = %d\n", number);

	return 0;
}

void cubeByReference(int *ptr) {

	*ptr = (*ptr) * (*ptr) * (*ptr);

}
```

#### `scope.c`

```c
#include <stdio.h>

int i = 1;

int main() {

    int x = 4;
    printf("add_i outputs %d\n", add_i(x));
    printf("i is %d\n", i);
    printf("x is %d\n", x);
    return 0;
}

int add_i(int n) {

    int x = n + i;
    i++;

    return x;
}
```

#### `gcd.c`

```c
/*
 * GCD program from [5]
 */
#include <stdio.h>

int gcd(int a, int b) {
 
	if (b == 0)
		return a;
	else
		return gcd(b, a % b);
		
}

int main() {

	printf("GCD: %d\n", gcd(24, 40));
	
	return 0;
	
}
```

### Arrays

#### `array.c`

```c
/*
 * Array example.
 */
#include <stdio.h>

#define MAX_STUDENTS 10

int main() {

	int studentId[MAX_STUDENTS];
	for (int i = 0; i < MAX_STUDENTS; i++)
		studentId[i] = i + 1;
	
	printf("%7s%13s\n", "Element", "Value");
	for (int i = 0; i < MAX_STUDENTS; i++)
		printf("%7d%13d\n", i, studentId[i]);
	
	return 0;	
}
```

#### `array_init.c`

```c
/*
 * Array initialiser example.
 */
#include <stdio.h>

#define MAX_STUDENTS 10

int main() {

    int studentId[MAX_STUDENTS] =
        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    printf("%7s%13s\n", "Element", "Value");
    for (int i = 0; i < MAX_STUDENTS; i++)
        printf("%7d%13d\n", i, studentId[i]);
	
    return 0;	
}
```

#### `array_addresses.c`

```c
/*
 * The name of the array evaluates to the address of the first element
 * of the array.
 */
 #include <stdio.h>
 
 int main() {
 
	char charArray[5];

	printf("charArray: \t%p\n", charArray);
	printf("&chararray[0]: \t%p\n", &charArray[0]);
	printf("&charArray: \t%p\n", &charArray);
	
	return 0;
}
```

#### `two_dimensional_array.c`

```c
/*
 * Two dimensional arrays example.
 */
#include <stdio.h>
 
/* array dimensions */
#define STUDENTS 3
#define EXAMS 4

/* each of these functions takes a two-dimensional array as its first parameter */
int findLowest(int[][EXAMS], int);
int findHighest(int[][EXAMS], int);
void printGrades(const int[][EXAMS], int);

int main() {
 
	int studentGrades[STUDENTS][EXAMS] = {
		{77, 68, 86, 72},
		{96, 87, 89, 78},
		{70, 90, 86, 81}
	};
	
	printGrades(studentGrades, STUDENTS);
	printf("The lowest grade is %d.\n", findLowest(studentGrades, STUDENTS));
	printf("The highest grade is %d.\n", findHighest(studentGrades, STUDENTS));
	
	return 0;
	
}

/* find the lowest grade for all students on all exams */
int findLowest(int grades[][EXAMS], int numberOfStudents) {
	
	int lowest = 101;
	int i, j;
	
	for (i = 0; i < numberOfStudents; i++)
		for (j = 0; j < EXAMS; j++)
			if (grades[i][j] < lowest)
				lowest = grades[i][j];
			
	return lowest;
	
}

/* find the highest grade for all students on all exams */
int findHighest(int grades[][EXAMS], int numberOfStudents) {
	
	int highest = 0;
	int i, j;
	
	for (i = 0; i < numberOfStudents; i++)
		for (j = 0; j < EXAMS; j++)
			if (grades[i][j] > highest)
				highest = grades[i][j];
			
	return highest;
	
}

/* print an array of students grads */
void printGrades(const int grades[][EXAMS], int numberOfStudents) {
	
	int i, j;
	
	printf("Name\t\t[0]\t[1]\t[2]\t[3]\n");
	for (i = 0; i < numberOfStudents; i++) {
		printf("Student[%d]", i);
		for (j = 0; j < EXAMS; j++)
			printf("\t%d", grades[i][j]);
		printf("\n");
	}
	
	return;
}
```

#### `grades_static.c`

```c
/*
 * Read a list of grades with static memory allocation.
 */
#include <stdio.h>

#define NUM_STUDENTS 10

int main() {

	int grades[NUM_STUDENTS];
	int i;

	for (i = 0; i < NUM_STUDENTS; i++) {
		printf("Grade for student %d: \n", i + 1);
		scanf("%d", &grades[i]);
		printf("Entered grade: %d\n", grades[i]);
	}

	return 0;

}
```

### Strings

#### `puts_and_getchar.c`

```c
/*
 * puts() and getchar() example.
 */
#include <stdio.h>

#define MAX_LENGTH 80

int main() {

	char sentence[MAX_LENGTH];
	char c;
	int index = 0;
	puts("Enter a line of text: ");
	while ((c = getchar()) != '\n' && index < MAX_LENGTH - 1)
		sentence[index++] = c;
	sentence[index] = '\0';
	puts("The input line was: ");
	puts(sentence);
	
	return 0;
	
}
```

#### `print_reverse.c`

```c
/*
 * String reversal exercise.
 */
#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 80

/* print the characters of a string in reverse order */
void print_reverse(const char[]);

int main() {

	char sentence[MAX_LENGTH];
	printf("Enter a line of text:\n");
	fgets(sentence, MAX_LENGTH, stdin);
	printf("The input line written backwards:\n");
	print_reverse(sentence);
	
	return 0;
	
}


/* this function is to be implemented */
void print_reverse(const char str[]) {

	int i;
	for (i = strlen(str) - 1; i >= 0; i--)
		putchar(str[i]);

}
```

#### `string_manipulation.c`

```c
/*
 * String manipulation example.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_FULLNAME  80
#define MAX_USERNAME  9
#define RANDOM_DIGITS 3

int main() {

	char name[MAX_FULLNAME];
	char userID[MAX_USERNAME];
	int  n, i;
	
	printf("Enter your name: ");
	scanf("%79s", name);
	strncpy(userID, name, MAX_USERNAME - RANDOM_DIGITS - 1);
	userID[MAX_USERNAME - RANDOM_DIGITS - 1] = '\0';
	
	srand(time(NULL));
	n = strlen(userID);
	for (i = 0; i < RANDOM_DIGITS; i++)
		userID[n + i] = '0' + rand() % 10;
	userID[n + RANDOM_DIGITS] = '\0';
	printf("Your username is: %s\n", userID);
	
	return 0;
	
}
```

#### `string_comparison.c`

```c
#include <stdio.h>
#include <string.h>

int main() {

	char word1[20], word2[20];

	printf("Enter two words, separated by a space: ");
	scanf("%19s%19s", word1, word2);

	int c = strcmp(word1, word2);
	if (c < 0)
		printf("\"%s\" comes first.\n", word1);
	else if (c > 0)
		printf("\"%s\" comes first.\n", word2);
	else
		printf("Those two words are the same.\n");

	return 0;
}
```

#### `string_conversion.c`

```c
/*
 * String conversion examples.
 */
#include <stdio.h>
#include <stdlib.h>

int main() {

	/* convert the string "123456789" to the long integer 123456789 */
	long l;
	l = atol("123456789");
	printf("%ld\n", l);
	
	/* convert the number part of the string "52.1-String" to a double */
	const char *inputStr = "52.1-String";
	double d;
	char *endStr;
	d = strtod(inputStr, &endStr);
	printf("%.2f\n%s\n", d, endStr);
	
	return 0;
}
```

#### `sprintf.c`

```c
/*
 * sprintf() example from [1].
 */
#include <stdio.h>

#define MAX_LENGTH 80

int main() {

	char s[MAX_LENGTH];
	int x;
	double y;
	
	printf("Enter an integer and a double: ");
	scanf("%d%lf", &x, &y);
	
	sprintf(s, "integer: %d, double: %f\n", x, y);
	printf("The formatted string stored in the array is: %s", s);
	
	return 0;
	
}
```

### Pointers

#### `pointer.c`

```c
/*
 * Pointer example.
 */
#include <stdio.h>

int main() {
	int y = 5;
	int *yPtr;
	
	yPtr = &y;
	printf("Address of y: %d\n", &y);
	printf("Value of yPtr: %d\n", yPtr);
	printf("Address of yPtr: %d\n", &yPtr);
	printf("Value to which yPtr points: %d\n", *yPtr);
	
	return 0;
}
```

#### `pointer_-_Exercise.c`

```c
/*
 * Pointer example.
 */
#include <stdio.h>

int main() {
	int a = 5, b = 2;
    int *p = &a, *q = &b;

    *p *= 2;        //a = 10;
    *q  = *p - 1;   //b = 9;
    p  = &b;        //*p = 9;
    b  = *p + 3;    //b = 12;

    printf("the value of a is: %d\n", a);
    printf("the value of b is: %d\n", b);

	return 0;
}
```

#### `pointer_to_pointer.c`

```c
/*
 * Pointers to pointers example.
 */
#include <stdio.h>

int main() {

	int n = 5;
	int *ptr = &n;
	int **ptrToPtr = &ptr;

	/* illustrating the address operator & */
	printf("&n = %d\n", &n);
	printf("ptr = %d\n", ptr);
	printf("&ptr = %d\n", &ptr);
	printf("ptrToPtr = %d\n\n", ptrToPtr);

	/* illustrating the dereferencing operator * */
	printf("*ptr = %d\n", *ptr);
	printf("*ptrToPtr = %d\n", *ptrToPtr);
	printf("ptr = %d\n", ptr);
	printf("**ptrToPtr = %d\n", **ptrToPtr);

	return 0;

}
```

#### `pointers_and_subscripts.c`

```c
/*
 * Subscripting and pointer arithmetic can be used interchangeably.
 */
#include <stdio.h>

int main() {
 
    char b[] = {'a', 'b', 'c', 'd', 'e' };
    char *bPtr = b;

    printf("*(bPtr + 3): \t%c\n", *(bPtr + 3));
    printf("*(b + 3): \t%c\n", *(b + 3));
    printf("bPtr[3]: \t%c\n", bPtr[3]);
	
	return 0;
}
```

#### `pointers_and_arrays_exercise.c`

```c
/*
 * Pointers and arrays example.
 */
#include <stdio.h>

int main() {

	int a[] = { 1, -1, 4, 5, 4, -3 };

    int *p = a + 5;
    printf("content in array a:\t\t%d  %d  %d  %d  %d  %d\n", a[0], a[1], a[2], a[3], a[4], a[5]);
    printf("*P after *p = a + 5:\t\t%18d\n\n", *p);

    *p = -(*p);
    printf("content in array a:\t\t%d  %d  %d  %d  %d  %d\n", a[0], a[1], a[2], a[3], a[4], a[5]);
    printf("*P after *p = -(*p):\t\t%17d\n\n", *p);

    p -= 2;
    printf("content in array a:\t\t%d  %d  %d  %d  %d  %d\n", a[0], a[1], a[2], a[3], a[4], a[5]);
    printf("*P after p -= 2:\t\t%11d\n\n", *p);

    *p = *p + 1;
    printf("content in array a:\t\t%d  %d  %d  %d  %d  %d\n", a[0], a[1], a[2], a[3], a[4], a[5]);
    printf("*P after *p = *p + 1:\t\t%11d\n\n", *p);

    *(p + 1) = *p * 2;
    printf("content in array a:\t\t%d  %d  %d  %d  %d  %d\n", a[0], a[1], a[2], a[3], a[4], a[5]);
    printf("*P after *(p + 1) = *p * 2:\t%11d\n", *p);

	return 0;

}
```

#### `array_of_pointers.c`

```c
/*
 * The name of the array evaluates to the address of the first element
 * of the array.
 */
 #include <stdio.h>

 int main() {

	char *suit[4] = { "Hearts", "Diamonds", "Clubs", "Spades" };
    char *face[13] = {
        "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King"
    };

    for (int i = 0; i < 4; i++) {
        char *card_suit = suit[i];
        for (int j = 0; j < 13; j++) {
            printf("%s of %s\n", face[j], card_suit);
        }
    }

	return 0;
}
```

#### `swap_pointer.c`

```c
/*
 * Swapping example
 */

#include <stdio.h>
 
/* swap pointers */
void swapPointer(int **a, int **b) {

	int *temp = *a;
	*a = *b;
	*b = temp;
	
}

/* swap values */
void swapValue(int *a, int *b) {

	int temp = *a;
	*a = *b;
	*b = temp;
	
}

int main() {

	int a = 5;
	int b = 6;
	int *ptrA = &a;
	int *ptrB = &b;
	
	printf("At the start:\n");
	printf("a = %d, b = %d\n", a, b);
	printf("ptrA = %p, ptrB = %p\n\n", ptrA, ptrB);
	
	/* test swapPointer() */
	ptrA = &a;
	ptrB = &b;
	swapPointer(&ptrA, &ptrB);
	printf("After swapPointer():\n");
	printf("a = %d, b = %d\n", a, b);
	printf("ptrA = %p, ptrB = %p\n\n", ptrA, ptrB);
	
	/* test swapValue() */
	ptrA = &a;
	ptrB = &b;
	swapValue(ptrA, ptrB);
	printf("After swapValue():\n");
	printf("a = %d, b = %d\n", a, b);
	printf("ptrA = %p, ptrB = %p\n\n", ptrA, ptrB);
	
	return 0;
	
}
```

### Structs and Dynamic Memory

#### `struct_with_function.c`

```c
/*
 * struct example with function calls
 */
#include <stdio.h>

typedef struct student {
	char name[20];
	int roll;
	int age;
	char class[12];
} Student;

void print_student(Student *s);

int main() {

	/* initialise a variable of type Student */
	Student stud1 = { "Sachin Kumar", 101, 16, "INF1002" };

	/* display contents of stud1 */
	print_student(&stud1);

	return 0;

}

void print_student(Student *s) {

	printf("\n Name : %s", s->name);
	printf("\n Roll : %d", s->roll);
	printf("\n Age  : %d", s->age);
	printf("\n Class: %s", s->class);

}
```

#### `grades_dynamic.c`

```c
/*
 * Read a list of grades with dynamic memory allocation.
 */
#include <stdio.h>
#include <stdlib.h>

int main() {

	int *grades;
	int num_students;
	int i;
	
	/* ask how many grades need to be stored */
	printf("How many students are in your class? ");
	scanf("%d", &num_students);
	
	/* allocate enough space to hold num_students integers */
	grades = (int *)malloc(num_students * sizeof(int));
	if (grades == NULL) {
		printf("Out of memory.");
		return 1;
	}
	
	/* read the grades */
	for (i = 0; i < num_students; i++) {
		printf("Grade for student %d: ", i + 1);
		scanf("%d", &grades[i]);
	}
	
	/* de-allocate memory */
	free(grades);
	
	return 0;
	
}
```

#### `names_dynamic.c`

```c
/*
 * Read a list of names with dynamic memory allocation.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME 256

int main() {

	char buf[MAX_NAME];
	char **names;
	int num_students;
	int length;
	int i;
	
	/* ask how many names need to be stored */
	printf("How many students are in your class? ");
	scanf("%d", &num_students);
	
	/* read to the end of the line */
	fgets(buf, MAX_NAME, stdin);
	
	/* allocate enough space to hold num_students strings */
	names = (char **)malloc(num_students * sizeof(char *));
	if (names == NULL) {
		printf("Out of memory.");
		return 1;
	}
	
	for (i = 0; i < num_students; i++) {
		/* read the name */
		printf("Name of student %d: ", i + 1);
		fgets(buf, MAX_NAME, stdin);
		
		/* copy the name into the array */
		length = strchr(buf, '\n') - buf;
		names[i] = (char *)calloc(length + 1, sizeof(char));
		if (names[i] == NULL) {
			printf("Out of memory.");
			return 1;
		}
		strncpy(names[i], buf, length);
	}
	
	/* print allof the names */
	printf("Here is the class list:\n");
	for (i = 0; i < num_students; i++)
		printf("  %s\n", names[i]);
	
	/* de-allocate memory */
	for (i = 0; i < num_students; i++)
		free(names[i]);
	free(names);
	
	return 0;
	
}
```

### Linked Lists

#### `linked_list.c`

```c
/*
 * Linked list example.
 */
#include <stdio.h>

/* the structure of a node */
typedef struct node_struct {
	int data;
	struct node_struct *next;
} Node;


int main() {
	/* declare two nodes and link them */
	Node node1 = { 15, NULL };
	Node node2 = { 10, NULL };
	node1.next = &node2;

	/* printing out the data of a node */
	printf("node1.data = %d\n", node1.data);
	printf("node1.next = \t\t%p\n", node1.next);
	printf("memory address of node2:%p\n", &node2);

	/* using a pointer to traverse the list */
	Node *node_ptr = &node1;
	printf("node1.data = %d\n", node_ptr->data);
	node_ptr = node_ptr->next;
	printf("node2.data = %d\n", node_ptr->data);

}
```

### File I/O

#### `create_file.c`

```c
/*
 * Creating a file.
 */
#include <stdio.h>

int main() {

	/* declare a pointer to a FILE structure */
	FILE *f;

	/* open the file with fopen() */
	f = fopen("create_file.txt", "w");
	if (f == NULL) {
		printf("Could not open data.txt.\n");
		return 1;
	}

	/* write to the file with fprintf() */
	fprintf(f, "Hi, this is INF1002.\n");

	/* close the file with fclose() */
	fclose(f);
    printf("The file is successfully created.\n");


	return 0;

}
```

#### `read_from_file.c`

```c
#include <stdio.h>
int main() {
	FILE *f;
	int account;
	char name[20];
	double balance;
	/* open the file */
	f = fopen("read_from_file.txt", "r");
	if (f == NULL) {
		printf("Could not open credit.txt.\n");
		return 1;
	}
	/* read until the end of the file */
	printf("%10s\t%20s\t%10s\n", "Account", "Name", "Balance");
	while (!feof(f)) {
		/* read one record */
		fscanf(f, "%d%19s%lf", &account, name, &balance);
		/* display it to the screen */
		printf("%10d\t%20s\t%10.2lf\n", account, name, balance);
	}
	/* clean up */
	fclose(f);
	return 0;
}
```

#### `random_access_write.c`

```c
#include <stdio.h>
/* this structure holds the data for one client */
typedef struct client_struct {
    int acc_num;
    char last_name[15];
    char first_name[10];
    double balance;
} Client;

int main() {
	const char *filename = "random_access_write.dat";
	FILE *f;
	Client client;
	/* open the data file */
	f = fopen(filename, "wb+");
	if (f == NULL) {
		printf("Could not open %s.\n", filename);
		return;
	}
	/* read account data from the user */
	printf("Enter account number (1-100, 0 to end)\n? ");
	scanf("%d", &client.acc_num);
	while (client.acc_num != 0) {
		/* read the data for this record */
		printf("Enter last_name first_name balance\n? ");
		scanf("%14s%9s%lf", client.last_name, client.first_name, &client.balance);
		/* go to this record's position in the file */
		fseek(f, (client.acc_num - 1) * sizeof(Client), SEEK_SET);
		/* write the client data structure */
		fwrite(&client, sizeof(Client), 1, f);
		/* ask for another record */
		printf("Enter account number (1-100, 0 to end)\n? ");
		scanf("%d", &client.acc_num);
	}
	fclose(f);
	return 0;
}
```

#### `random_access_read.c`

```c
/*
 * Random access file example.
 */
#include <stdio.h>

/* this structure holds the data for one client */
typedef struct client_struct {
    int acc_num;
    char last_name[15];
    char first_name[10];
    double balance;
} Client;

int main() {

	const char *filename = "random_access_write.dat";
	FILE *f;
	Client client;

	/* open the data file */
	f = fopen(filename, "rb");
	if (f == NULL) {
		printf("Could not open %s.\n", filename);
		return;
	}
	/* print title */
	printf("%-6s%-16s%-11s%10s\n", "Acct", "Last Name", "First Name", "Balance");
	/* read one record at a time until we reach EOF */
	fread(&client, sizeof(Client), 1, f);
	while (!feof(f)) {
		if (client.acc_num != 0)
			printf("%-6d%-16s%-11s%10.2lf\n", client.acc_num, client.last_name, client.first_name, client.balance);
		fread(&client, sizeof(Client), 1, f);
	}
	fclose(f);
}
```
