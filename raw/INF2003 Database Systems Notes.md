# INF2003 Database Systems

AY2025/26 Trimester 1
Dr. Tong Rong

---


---

# Lecture 1

*Source: INF2003_AY2425_T1_Lec01*


## Slide 1

INF2003
Database Systems
AY2025/26 Trimester 1
Dr. Tong Rong


## Slide 2

Database Intro


## Slide 3

Motivations to Learn DB
• Data is everywhere, explosively increasing.
• Organizations: bank, university, airlines, telecom etc
• Social networks, applications, personal devices
• Managing data is the key and foundation to almost any application in the world.
• DB technology encompasses broad areas in CS :OS, languages, AI, multimedia, logic, …
• Four people have won Turing Awards in this area
• Ground LLMs to specific domain/knowledge
3 source


## Slide 4

Database
• Database (DB)
• An organized collection of information.
• Database Management System (DBMS)
• A software package designed to store and 
manage databases. 
• Provides data processing environment that is 
both convenient and efficient to use. 
• Address all complications in data 
management
https://s7280.pcdn.co/wp-content/uploads/2018/08/database-management-system-810x898.png
4


## Slide 5

Why DBMS: advantages over flat file
• Data independence and efficient access
• DB independent to the application: logical design, physical storage
• Efficient access: easy retrieval, large file index, query optimization
• Reduced application development time
• DB system provide query facilities
• Data integrity and security
• Integrity constraints: validate data update request
• DBMS provides access control
• Uniform data administration
• Maintenance and data admin: 
 fine tuning data presentation, backups etc
• Concurrent access and crash recovery
5


## Slide 6

DBMS – Advantages 
Scenarios:
# 1: Given a student ID, how do I find the student, and the courses he/she is 
taking?
• We need: efficient data access.
# 2: I have multiple people making changes to the data, how do I ensure that the 
data is in a consistent state? How to solve the problem of concurrent access?
• We need: data integrity and concurrent access.
# 3: How do we enforce different users to perform different operations on 
subsets of data?
• We need: security / access control.
Do we need DBMS everywhere?
6


## Slide 7

Check
What is one common issue with storing data 
in flat files instead of a DBMS? 
• A) Too much security 
• B) Difficult concurrent access 
management 
• C) Excess data normalization 
• D) Automatic backups
7


## Slide 8

DBMS – Data Abstraction
View level (external) user, developer
user performs queries and operations, often in a 
software. 
Logical level (conceptual) developer, DB admin
communication protocol, define the abstracted 
structure: how the data pieces relate to one another. 
Physical level (internal) DB admin
how data stored in the disk, memory, cache, etc. 
https://binaryterms.com/view-of-data.html
Data is relatively isolated in different levels 
 
Data independence.
8


## Slide 9

DBMS – Data Independence
Change the physical characteristics without affecting the 
conceptual level
• Modify the physical schema
• Data is stored on disk or magnetic Tapes
• Changes to compression techniques or hashing algorithms.
Physical 
independence 
Change the logic structure of the data without affecting the 
other layers of the database
• Add/modify/delete a new attribute, entity or relationship is 
possible without a rewrite of existing application programs
• Merging two records into one
• Breaking an existing record into two or more records
Logical 
independence
Which one is more difficult? 
9


## Slide 10

Data Independence example - A simple university database
Id: 4 bytes Name:30 bytes …
Data on disk
View level
class student {
char name[30];
int id;
…
};
Logical level
• Students(Sid, Name, Age, Gpa)
• Module(Mid, Mname, Credit)
• Enroll (Sid, Mid, Grade)
Physical 
level
• Relations stored as 
unordered files
• Index on student ID
10


## Slide 11

Check
If you change the schema (e.g., add an 
attribute) but leave the applications 
unchanged, this demonstrates: 
A) Physical data independence 
B) Logical data independence 
C) Data abstraction 
D) Data inconsistency
11


## Slide 12

DBMS architecture
https://www.scaler.com/topics/dbms/dbms-architecture/
1-tier
2-tier
3-tier
12


## Slide 13

Types of DBMS
https://ptgmedia.pearsoncmg.com/images/chap4_9780135853290/elementLinks/04fig04_alt.jpg
• Structured data, 
explicit relationship
• Commonly used in 
enterprises
• Unstructured data
• Used in big data and 
real-time web 
applications
13


## Slide 14

Popular database
14
https://db-engines.com/en/ranking


## Slide 15

Relational Database –brief history
15


## Slide 16

Relational DB standard in transaction: ACID
• The entire transaction takes place at once or 
not at all.
Atomicity
• Database must be consistent before and 
after transaction
Consistency
• Multiple transactions occur independently 
without interference
Isolation
• Once a transaction is committed, considered 
permanent, even when a system failure
Durability
https://en.wikipedia.org/wiki/ACID By Jim Gray 16


## Slide 17

Database design


## Slide 18

Stages of Database Design
S1 • Requirement Analysis
S2 • Conceptual Database Design
S3 • Logical Database Design
S4 • Refine the Schemas
S5 • Physical Database Design
S6 • Application and Security Design
18


## Slide 19

Database Design stage 1 - requirement analysis 
• Bidirectional: 
• Our clients tell what they want. Normally not, or even far from complete. 
• We developers shall ask and clarify: what are the needs of our customers?
• What data to be stored? Numerical or text?
• What kind of applications to use the data? Online shopping or banking? 
• What operation needs to be performed? Read intensive? On many tables?
19


## Slide 20

Database Design stage 2 – conceptual design
• Given user requirements, what tools to model the requirements before creating 
the relevant tables in a DBMS?
• Create one relation for all modules and students? Or create multiple?
• Popular option: Entity Relationship (ER) Diagram.
• Requirement analysis information -> develop a high-level description of the 
data.
• Understand what are the constraints that need to be modeled.
Modules Enroll Students
20


## Slide 21

Database Design stage 3 – logical design
• ER -> relational database schemas.
• i.e., what are the columns and what are the rows.
• Database schema: blueprint or architecture of data 
• All important or relevant data
• Consistent formatting for all data entries
• Unique keys for all entries and database objects
• Each column in a table has a name and data type
• ER model is most relevant to the first three stages.
21


## Slide 22

Database Design stage 4 – schema refinement
• Analyze the relations -> identify potential problem -> refine it.
• Schema refinement (normalization): the process to reduce data redundancy and 
improve data integrity.
• Redundancy: repetition of same data or duplicate copies of same data
• Anomalies: the problems occurred after poorly planned
• Most popular technique: decomposition
• decomposing tables to eliminate data redundancy
22


## Slide 23

Database Design stage 5 – physical design
• The process of transforming a logical data model into a physical model 
• Physical design is optimized for data-access, performance 
requirements and other constraints of the target environment, i.e. 
hardware and software.
• Consider typical workloads
• Build indexes on tables and cluster some tables.
https://www.javatpoint.com/types-of-databases
23


## Slide 24

Database Design stage 6 – application & security design
Security design protecting a database from
• unauthorized access 
• malicious destruction 
• any accidental loss or misuse.
• Authorization: identify what is accessible or inaccessible.
• Access control: enforce access rules, i.e., guest and admin.
• Backup and recovery: recover the database from failure or damage
• Encryption: protect highly sensitive data
https://www.netsolutions.com/insights/the-ultimate-guide-to-database-security/
24


## Slide 25

Check
Which task is typically performed during 
the requirement analysis stage of 
database design?
A) Creating tables and assigning data 
types to columns 
B) Modeling data using Entity-Relationship 
diagrams 
C) Gathering user needs and identifying 
what data should be stored 
D) Breaking down tables to remove 
redundancy and anomalies
25


## Slide 26

Relational data model


## Slide 27

Relational Data Model 
• Relational database, a collection of relations, each has a unique name
• Relation, a table with rows and columns
• Each row in the table specifies a relationship between the values in that row
• Simple data representation.
• Easy query, expressing what you want, i.e., which column which row.
• Relations are unordered: 
• Allows optimized storage
Can we say: relational data model = SQL ? 
27


## Slide 28

Relational Data Model (cont.)
• Relation STUDENT
• Table STUDENT has 3 rows, or tuples. 
• Each row has 3 columns, or attributes.
• Each tuple specifies the relationship of the attributes
• Fixed size, with the same number of elements.
• Each attribute has a domain
• Specifies the set of valid values for the attribute
• Attribute values are (normally) required to be atomic; 
that is, indivisible, e.g.,
• sid is the set of 1 char + 7 digits 
sid sname saddress
S2022001 John Snow Blk 123 Ang Mo Kio
S2022002 Arya Stark Blk 45 Sengkang
S2022003 Sansa Stark Blk 108 Bukit Batok
STUDENT
28


## Slide 29

Relational Schema
• Relation schema: every relation has a schema
• Specifies the type information for relations, i.e., attribute name and domain.
• Different relations can share the same schema, i.e., year 1 year 2 students.
• A relation schema includes:
• a set of attributes
• the domain of each attribute
• Notation: r(R) - the schema of r is R.
• STUDENT(sid, sname, saddress)
• r: STUDENT
• R: (sid, sname, saddress)
• Domains are not stated explicitly in this notation!
sid sname saddress
S2022001 John Snow Blk 123 Ang Mo Kio
S2022002 Arya Stark Blk 45 Sengkang
S2022003 Sansa Stark Blk 108 Bukit Batok
STUDENT
29


## Slide 30

Domain - NULL
• The special value NULL is a member of every domain. Indicated that the value 
is unknown or unspecified
• A placeholder to denote values that are missing or do not know
• The null value causes complications in the definition of many operations
• Operations with NULLs are quite troublesome 
• NULL>100? NULL *100 =?
• avoid using NULL if possible.
• In DBMS, we can specify default values, i.e., 
• if not specified, record 0.
https://blog.sqlauthority.com/wp-content/uploads/2007/06/null-500x259.png
30


## Slide 31

Avoid Duplications – Keys
• A database contains many records, how to fetch a particular one?
• Keys are used to distinguish individual tuples 
• Definition: a certain minimal subset of relation attributes uniquely identifies a tuple.
• Keys define the meaning of the relation.
• All relations have a key, some may have multiple keys
• Unique: two distinct tuples cannot have same values in all key attributes.
31


## Slide 32

Avoid Duplications – Keys (cont.)
• Superkey: a set of attributes within a table that can uniquely identify each record
 sid / sid, sname /sphone/sid, address/ … How about saddress?
• Not all superkeys are equally useful…
• Candidate key: the minimal set of fields which can uniquely identify each record
• There can be more than one candidate key. sid / sphone
• Primary key: a candidate key that is most appropriate to become the main key: sid
• How to indicate Primary key? -> underline it.
 STUDENT (sid, sname, saddress, sphone)
sid sname saddress sphone
S2022001 John Snow Blk 123 Ang Mo Kio 91234567
S2022002 Arya Stark Blk 45 Sengkang 91234568
S2022003 Sansa Stark Blk 108 Bukit Batok 91234569
Primary key
Candidate key
Superkey
32


## Slide 33

Foreign Keys 
• To link the data among relations/tables
• Foreign key is the primary key of the other relations.
• Referencing relation and referenced relation, Like a logical pointer.
• Example: 
• sid is a foreign key referring to STUDENT:
sid cid grade
S2022001 ICT1002 C
S2022001 ICT1009 B
S2022003 ICT2103 A
S2022001 ICT2103 B
Enrolled: Referencing relation STUDENT (Referenced relation) 
sid sname saddress
S2022001 John Snow Blk 123 Ang Mo Kio
S2022002 Arya Stark Blk 45 Sengkang
S2022003 Sansa Stark Blk 108 Bukit Batok
33


## Slide 34

Check
Which of the following best describes a 
primary key in a relational database?
A) A field used mainly for sorting records in 
a table 
B) A field that allows duplicate values in all 
records 
C) A field chosen from candidate keys to 
uniquely identify each record 
D) A field that can be left empty or contain 
NULL values
34


## Slide 35

Recap • Introduction • General information • DBMS basics • Stages of Database Design • Six stages • Often many rounds • Relational data model • Concepts • Keys
35


## Slide 36

About Project
• an application of interests
Identify an application
• Real-world data: download, crawl etc. Or generate synthesized data if required
• Dataset good for relational database and non relational database
Identify datasets
• Functionalities
• Data models and ER diagram
Application and DB design
• Basic : CRUD, NoSQL data model
• Any complex DB related functions
Implementation
• Performance analysis
• limitations and potential improvements
Analysis and Reflection
36


## Slide 37

About Project
• Group project, 6 students/group (396 students)
• Self enrolment, by week 2, Sep 14, 11:30PM
Auto allocate unenrolled users after self enrollment expiry date
Deliverable Due and Submission 
Project proposal (2 pages)
Brief description of the application
Data, system architecture, software 
requirements, implementation plan, team 
member task assignment
Week 5 Oct 5 11:30 PM
XSite group Dropbox: 
Single file within 2 pages 
Project final report (template provided) Week 13 Nov 30, 11:30 PM ?
XSite group dropbox, a .zip file contains:
final report: *.pdf
Presentation slides: *.ppt
Presentation video: *.mp4
Source code: zip file 
Project presentation slides 
Video presentation (<10 mins)
Source code with user manual
Peer review (team mates)
37


## Slide 38

Lab 1
• Google colab: tutorial uploaded in Xsite
• Python-based Database with Object Relational Mapper (ORM)
• Objectives: to learn the basic database operations via Python and 
SQLAlchemy.
• SQLAlchemy allows us to bypass the SQL statements and perform 
the database operations in Python
• Colab/Jupyter notebook
38


---

# Lecture 2

*Source: INF2003_AY2425_T1_Lec02*


## Slide 1

INF2003 
Database systems
Relational Algebra and SQL
AY2025/26 Trimester 1
Dr. Tong Rong


## Slide 2

From last week
• DB
• We are motivated to study DB and DBMS
• Data abstraction and independence
• DBMS architecture
• Relational database basics: 
• History, ACID
• 6 Stages of Database Design
• Keys are used to distinguish individual tuples


## Slide 3

Outline – this week
Relational database:
• Relational algebra
• Allow manipulation and retrieval of data from a database.
• Fundamental operators and examples
• Extended operators and examples
• Integrity Constraints
• SQL
• Overview
• Part 1


## Slide 4

Communication with DBMS
• What to communicate
• Define the structure of database
• CREATE / ALTER / DROP / TRUNCATE / COMMENT / RENAME 
• Manipulate data
• SELECT / INSERT / UPDATE / DELETE etc
• How to communicate
• Relational algebra. Mathematical-driven
• Structured Query Language (SQL). Programming-driven.
• Relational calculus (a declarative language, describe what we want, not 
covered in this module)


## Slide 5

Relational Algebra


## Slide 6

Relational Algebra
• A procedural language, while SQL is declarative 
• Relational algebra ops are like the machine code for DBMSs
• Relational algebra forms the basis for DBMS implementation
• Many relational databases use relational algebra operations 
for representing execution plans 
• Simple, clean, effective abstraction for representing how 
results will be generated 
• Relatively easy to manipulate for query optimization
Procedure language
Specify what to get and how 
to get
E.g.
do while(isspace(*s)) s++; 
while(*d++ = *s++);
Declarative language
Specify what to get
E.g.
out_str = re.sub (r’^\s+', ' ', 
input_string)


## Slide 7

Relational algebra - operators
https://www.gatevidyalay.com/relational-algebra-relational-algebra-in-dbms
Natural Join (⋈)
Left, Right, Full outer join 
(⟕, ⟖, ⟗)
https://miro.medium.com/max/4230/1*mo7B0h9PHYGmwaJ1ouUl8g.png


## Slide 8

Fundamental Operator – Select 
• Representation: 𝜎𝑃(𝑟)
• r: one relation
• P: one or many attributes of relation r
• People also refer it as predicates, so it is P
• Logical operators: ‘and’ ∧, ‘or’ ∨, ‘not’ ¬.
• Comparison operators feasible: >=, >, =, !=, <, <=.
• Return: All the tuples in r that P condition is met.
• Schema is the same as r, or with same column names and 
data types.
SQL:
SELECT *
FROM r
WHERE P


## Slide 9

Fundamental Operator – Select Example 
1. Find all people from Winterfell.
• 𝜎{location=“Winterfell”} (GOT)
• Return tuple 1 – 3. 
2. Find all people from Winterfell and born 
after year 285.
𝜎 location=“Winterfell” ∧
YOB>285 (GOT)
For simplicity, we can write in Latex style:
𝜎_{location=“Winterfell” ∧ YOB>285} (GOT)
ID Name Location YOB
1 Sansa Stark Winterfell 285
2 Jon Snow Winterfell 281
3 Arya Stark Winterfell 287
4 Tywin Lannister Casterly Rock 234
5 Tyrion Lannister Casterly Rock 266
6 Daenerys Targaryen Dragonstone 282
GOT


## Slide 10

Fundamental Operator – Project 
• Notation: ∏𝑎,𝑏,…(𝑟)
• Selection is tuple-wise. Project is column-wise.
• Returned columns are from relation r.
• Values from the same domain.
• Possible to return fewer tuples than the original 
relation r. (why?)
SQL:
SELECT a,b …
FROM r
set operation


## Slide 11

Fundamental Operator – Project example 
• Find all the locations.
• π_{Location}(GOT).
• How many tuples can we get?
• No duplicate result, relations are sets
• What if partial relation input:
• π_{Location}(𝜎_{YOB>280}(GOT)).
• Do we still have ‘Casterly Rock’?
ID Name Location YOB
1 Sansa Stark Winterfell 285
2 Jon Snow Winterfell 281
3 Arya Stark Winterfell 287
4 Tywin Lannister Casterly Rock 234
5 Tyrion Lannister Casterly Rock 266
6 Daenerys Targaryen Dragonstone 282
GOT
Location
Winterfell
Casterly Rock
Dragonstone


## Slide 12

Fundamental Operator – Set Union 
• Combine, or union, the tuples of two relations r and s: r ∪ s.
• All the tuples, but not the duplicated ones.
• Requirement: same relation schema. 
• Exactly the same, i.e., name, type, and order.
Name Location YOB
Sansa Stark Winterfell 285
Jon Snow Winterfell 281
Arya Stark Winterfell 287
Name Location YOB
Arya Stark Winterfell 287
Tywin Lannister Casterly Rock 234
Tyrion Lannister Casterly Rock 266
Name Location YOB
Sansa Stark Winterfell 285
Jon Snow Winterfell 281
Arya Stark Winterfell 287
Tywin Lannister Casterly Rock 234
Tyrion Lannister Casterly Rock 266
r
s
r ∪ s


## Slide 13

Fundamental Operator – Set Union example 
• What if the schema of the relations are not same?
• Relation t and s, schemas not the same
• Cut part of the columns, which are the same, i.e.
project
• People who is either a Stark or a Targaryen.
• π_{Name}(t). Everyone who’s a Targaryen.
• π_{Name}(s). Everyone who’s a Stark.
• π_{Name}(t) ∪ π _{Name}(s). 
• How many tuple do we have?
• 4 instead of 5. Jon duplicated.
SID Name YOB
1 Sansa Stark 285
2 Jon Snow 281
3 Arya Stark 287
TID Name HasDragon
1 Jon Snow False
2 Daenerys Targaryen True
Name
Sansa Stark
Jon Snow
Arya Stark
Daenerys Targaryen
s
t


## Slide 14

Fundamental Operator – Set Difference 
• r – s: fulfill in relation r but not in relation s
• Requirement:
• Similar as set union, relations have exactly the same schema.
• A - B != B - A
Name Location YOB
Sansa Stark Winterfell 285
Jon Snow Winterfell 281
Arya Stark Winterfell 287
Name Location YOB
Arya Stark Winterfell 287
Tywin Lannister Casterly Rock 234
Tyrion Lannister Casterly Rock 266
r
s
Name Location YOB
Sansa Stark Winterfell 285
Jon Snow Winterfell 281
s - r
Name Location YOB
Tywin Lannister Casterly Rock 234
Tyrion Lannister Casterly Rock 266
r - s


## Slide 15

Fundamental Operator – Set Difference example 
• What if relation schemas not the same? 
• Use Project
• People who is a Stark but not a Targaryen.
• π_{Name}(s). Is a Stark.
• {Sansa Stark, Jon Snow, Arya Stark}
• π_{Name}(t). Is a Targaryen.
• {Jon Snow, Daenerys Targaryen}
• π_{Name}(s) −π_{Name}(t).
• Result?
• {Sansa Stark, Arya Stark}
• Jon is a Stark and a Targaryen as well.
SID Name YOB
1 Sansa Stark 285
2 Jon Snow 281
3 Arya Stark 287
TID Name HasDragon
1 Jon Snow False
2 Daenerys Targaryen True
Name
Sansa Stark
Arya Stark
s
t


## Slide 16

Fundamental Operator – Cartesian/cross Product
• Also called Cross product: s × t
• concatenate the tuples in s and t.
• Keep all attributes in s and in t. No abandon.
• If same attribute name, how?
• Like C++, add a scope, i.e., s.id and t.id for the same 
attribute name id.
• Keep all the tuples, i.e., nstuples for s and ntfor t, -> 
ns∗ nttuples.
• Unlike union/difference, no constraint for cross.
https://commons.wikimedia.org/wiki/File:Relational_Algebra_Cartesian_Product.svg


## Slide 17

Fundamental Operator – Cartesian/cross Product example
• Example: Relation s for name and relation t for location.
• Result: all concatenated.
ID Name YOB
1 Jon Snow 281
2 Arya Stark 287
ID Location
1 Winterfell
2 Dragonstone
s.ID Name YOB t.ID Location
1 Jon Snow 281 1 Winterfell
1 Jon Snow 281 2 Dragonstone
2 Arya Stark 287 1 Winterfell
2 Arya Stark 287 2 Dragonstone
s t
s x t


## Slide 18

Fundamental Operator – Rename
• Rename operation: 𝜌𝑥(𝐸).
• 𝜌: rename operator.
• x: new name. User specified.
• E: expression, or the resulting relation after certain relational operations.
• Or, if you want more: 𝜌𝑥(𝑎1,𝑎2,… )(𝐸).
• a1, a2, …: attribute names can also be renamed, if we have the attribute.
• Usage: 
• We have a name to refer to, if later working on the result.
• Resolve ambiguities.
• Use in Cartesian Product, i.e., r × 𝜌_s(r). Can we do r × r?
• Scope: (recall Python, C, C++).
• Name only valid in the local scope, i.e., the expression.


## Slide 19

Fundamental Operator – Rename example
• Relation 𝑟:
𝜌𝑥 𝑟 , Relation 𝑥:
𝜌𝑦(𝐶,𝐷,𝐸) 𝑟 , Relation 𝑦:
ID Name YOB
1 Jon Snow 281
2 Arya Stark 287
ID Name YOB
1 Jon Snow 281
2 Arya Stark 287
C D E
1 Jon Snow 281
2 Arya Stark 287


## Slide 20

Fundamental Operators example
• Who is the youngest? If we can only use the 6 operators introduced.
• Idea 1: use cross to inspect every possible combination.
• i.e., Sansa is younger than Jon.
• Problem: can we say Sansa is the youngest if Sansa is younger than Jon?
• We need to check all other people and compare with Sansa -> complicated.
SID Name YOB
1 Sansa Stark 285
2 Jon Snow 281
3 Arya Stark 287
s.ID s.Name s.YOB t.ID t.Name t.YOB
1 Sansa Stark 285 1 Sansa Stark 285
1 Sansa Stark 285 2 Jon Snow 281
1 Sansa Stark 285 3 Arya Stark 287
2 Jon Snow 281 1 Sansa Stark 285
2 Jon Snow 281 2 Jon Snow 281
2 Jon Snow 281 3 Arya Stark 287
3 Arya Stark 287 1 Sansa Stark 285
3 Arya Stark 287 2 Jon Snow 281
3 Arya Stark 287 3 Arya Stark 287


## Slide 21

Fundamental Operators example – cont.
Idea 2: use the contrary proof. Check who is older than anyone. 
If so, it cannot be the youngest. Can be removed.
• s × 𝜌_t(s): cross to get all combinations.
• 𝜎_{s.YOB < t.YOB}(s × 𝜌_t(s)): pick tuples that s.YOB is older
• π_{s.Name}(𝜎_{s.YOB < t.YOB}(s × 𝜌_t(s))): get names of above.
• π_{s.Name}(s) -π_{s.Name}(𝜎_{s.YOB < t.YOB}(s × 𝜌_t(s)))
 ALL names – older names. 
SID Name YOB
1 Sansa Stark 285
2 Jon Snow 281
3 Arya Stark 287
s.ID s.Name s.YOB t.ID t.Name t.YOB
1 Sansa Stark 285 1 Sansa Stark 285
1 Sansa Stark 285 2 Jon Snow 281
1 Sansa Stark 285 3 Arya Stark 287
2 Jon Snow 281 1 Sansa Stark 285
2 Jon Snow 281 2 Jon Snow 281
2 Jon Snow 281 3 Arya Stark 287
3 Arya Stark 287 1 Sansa Stark 285
3 Arya Stark 287 2 Jon Snow 281
3 Arya Stark 287 3 Arya Stark 287


## Slide 22

More Operators
• Why fundamental operators specially discussed?
• They are able to do any query, but complicate expression
• To simplify some operations -> additional operators.
• ∩: set intersection. 
• Join:
• ⋈ natural join.
• outer join
• ÷ division


## Slide 23

More Operators - Intersection
Intersection: s ∩ t 
• The relation schemas must be compatible.
• Use union and difference to realize intersection.
• (s ∪ t) – (s – t) – (t – s)
• Can be better?
• s – (s – t) 
• Who is both Stark and Targaryen? 
π_{Name}(s) ∩ π_{Name}(t)
SID Name YOB
1 Sansa Stark 285
2 Jon Snow 281
3 Arya Stark 287
TID Name HasDragon
1 Jon Snow False
2 Daenerys Targaryen True
Name
Jon Snow
s t


## Slide 24

More Operators - Natural Join
• s ⋈ t for relation s and relation t
• a special product
• contain all the attributes of both tables but only one copy of common column
• Requirement:
• Must share some columns, as the reference
• The name and type of the columns must be same.
• Can we use fundamental operators to do join?
• Schema s(S),t(T), their common columns:
• S ∩ T = {A1, A2, …, Am}
• s ⋈ t = π _{S∪ T}(𝜎_{s.A1=t.A1∧ ⋯ ∧ s.Am=t.Am}(s × t))
• Who is both Stark and Targaryen?
• π_{Name}(s ⋈ t) with join.
• Or Π_{Name}(𝜎_{s.Name=t.Name}(s × t)).
Name YOB House
Sansa Stark 285 Stark
Jon Snow 281 Stark
Arya Stark 287 Stark
Name HasDragon
Jon Snow False
Daenerys Targaryen True
Name YOB House HasDragon
Jon Snow 281 Stark False


## Slide 25

More Operators - Outer Join
• Natural join require the perfect match, if retain some 
imperfect ones -> outer join.
• If imperfect ones allowed, what to do with missing values? 
• use NULL. means unknown.
• Similar to set difference, direction matters.
• Left outer join: r s
• For tuples in left relation r, if not match, keep as NULLs
• For tuples in right relation s not match perfectly, delete
• Right outer join: r s. Reverse, keep s not r.
• Full outer join: r s, Keep both.
https://www.ionos.com/digitalguide/hosting/technicalmatters/sql-outer-join/


## Slide 26

Outer Join example
ID Name Dept.
10101 David ICT
10121 Raphael HSS
10151 Frank BCD
ID Module_id
10101 ICT101
10121 HSS201
10681 FCB302
r s
r s
Left out join 
ID Name Dept. Module_id
10101 David ICT ICT101
10121 Raphael HSS HSS201
10151 Frank BCD null
r s
Right out join 
ID Name Dept. Module_id
10101 David ICT ICT101
10121 Raphael HSS HSS201
10681 null null FCB302
r s
Full outer join 
ID Name Dept. Module_id
10101 David ICT ICT101
10121 Raphael HSS HSS201
10151 Frank BCD null
10681 null null FCB302


## Slide 27

More Operators - division
• It is defined on two relations r(U1) and s(U2) , denote as: r s or r/s
• U2 is a subset of U1 
• s is not an empty relation:
• Division is often used when express queries with ‘all’
• Example: Find out the module that taught in all programs
Module Program
Systems IS
Database IS
Database SE
Algebra SE
Program
IS
SE
÷ Module
Database
÷


## Slide 28

More Operator – Assignment
• Denoted by: t ← [expression].
• Where [expression] is a relational algebra expression
• t is a relation
• The assignment stores in t the output of [expression]
• Assignments provides a convenient way to express complex queries by cutting 
it into multiple steps:
• Long query as a sequential program
• Each step can be described by a short line
• Assignment must always be made to a temporary relation variable


## Slide 29

Assignment example
Given new tuple(s) E and relation s:
• Suppose the constraint can be met, i.e., same relation schema.
• E potentially can be quite complicated, i.e., a long operation expression.
• Insert: s ← s ∪ E.
• Specify actual items, also feasible. 
• Delete: s ← s – E.
• Delete Casterly Rock.
• s ← s – E, where 
• E = 𝜎_{Loc=‘Casterly Rock’}(s).
• Or, can also be written as:
• s ← 𝜎_{Loc≠‘Casterly Rock’}(s).
• Update: s ← Π(s)
• s ← Π_{ID+5, Name, Location, YOB}(s).Specify the schema clearly.
ID Name Location YOB
1 Sansa Stark Winterfell 285
2 Jon Snow Winterfell 281
3 Arya Stark Winterfell 287
4 Tywin Lannister Casterly Rock 234
5 Tyrion Lannister Casterly Rock 266
6 Daenerys Targaryen Dragonstone 282


## Slide 30

Query efficiency for good performance
Good performance involves any/all of:
• making applications run faster
• lowering response time of queries/transactions
• improving overall transaction throughput
Find the names of all instructors in the ICT, along with the titles of courses they teach:
• instructor(ID, name, dept_name, salary)
• teaches(ID, course_id, sec_id, semester, year)
• course(course_id, title, dept_name, credits)
Query 1:πname,title ( dept_name=`ICT`( instructor ⋈ (teaches ⋈ πcourse_id,title course)) )
Query 2:πname,title ( ( dept_name=`ICT` instructor ) ⋈ ( teaches ⋈ πcourse_id,title course ) )
• The two queries are not identical but equivalent: obtain same result.
• Query 2 perform an early selection: fewer number of tuples, saves time.


## Slide 31

Check
Please state the output of the following queries:
• r1 ← 𝜎_{color=’red’}(Parts)
• r2 ← 𝜎_{cost<100}(Catalog)
• π_{sname}(π_{sid}(r1 ⋈ r2) ⋈ Suppliers)


## Slide 32

Integrity Constraints


## Slide 33

Relational database: Integrity Constraints (ICs)
Integrity constraints (IC) are pre-defined set of rules that are applied on the relations
• ICs come from real-world requirements. 
• ICs are specified when schema is defined/created.
• ICs are checked when relations are modified.
• We can check a database instance to see if certain IC is violated.
• A database is legal if all ICs hold for all data.
• DBMS does not allow illegal relations. 
• Stored data is more faithful to real-world meaning.
• Wrongly input two students with the same matric number -> cannot pass.
• Types of Integrity Constraints
• Domain constraints
• Key constraints
• Referential constraints
https://www.rapidmicrobiology.com/rmbdata/userfiles/suppliers/biomerieux_industry/news/1
802_bioMeriuex_DateIntegrityWhitePaper.png


## Slide 34

Relational integrity constraints – Domain constraints
• Domain constraint restrict the kind of attributes or values a column can hold in 
the database table
• specified as data types, some standard data types: integers, real numbers, 
characters, Booleans, variable length strings, etc.
• Every attribute is bound to have a specific range of values. E.g., 
• age cannot be less than zero 
• telephone numbers cannot contain a digit outside 0-9.
sid sname saddress
S2022001 John Snow Blk 123 Ang Mo Kio
S2022002 Arya Stark Blk 45 Sengkang
S2022003 Sansa Stark Blk 108 Bukit Batok
S2022004 12345.678 123 East coast road


## Slide 35

Relational integrity constraints – key constraints
• Only one primary key
• Unique: no two tuples can have identical values for key attributes.
• Not NULL: key attribute can not have NULL values.
sid sname saddress
S2022001 John Snow Blk 123 Ang Mo Kio
S2022002 Arya Stark Blk 45 Sengkang
S2022003 Sansa Stark Blk 108 Bukit Batok
S2022003 John Doe 123 East coast road
NULL Whatever 234 West coast road


## Slide 36

Relational integrity constraints – referential constraints
The reference from one table to another table must be valid
• A foreign key must have a matching primary key
• The reference key element must exist in the table
sid mid grade
S2022001 ICT1002 C
S2022001 ICT1009 B
S2022003 ICT2103 A
S2022004 ICT2103 B
Enrolled: Referencing relation STUDENT (Referenced relation) 
sid sname saddress
S2022001 John Snow Blk 123 Ang Mo Kio
S2022002 Arya Stark Blk 45 Sengkang
S2022003 Sansa Stark Blk 108 Bukit Batok


## Slide 37

How to preserve ICs
• How to ensure the ICs
• Model those constraints with high-level database design, i.e., ER diagram.
• Evaluate ICs every time an insert, update, delete, or alter operation is 
performed on the table 
• SQL supports Ics, 
• e.g NOT NULL, Check, UNIQUE. PRIMARY KEY, FOREIGN KEY REFERENCES
• Can we infer that an IC is true by looking at one instance?


## Slide 38

Check
Which of the following best describes a 
referential integrity constraint in a relational 
database?
A) Every value in a field must be within a specific 
domain 
B) Every primary key value must be unique and 
not NULL 
C) Every foreign key value must match an existing 
primary key value in another table 
D) Every attribute in a relation must be unique


## Slide 39

SQL basics


## Slide 40

SQL Overview
• SQL: Structured Query Language.
• Developed at IBM in the mid-1970's (System-R)
• Original language was “SEQUEL”
• Was called Structured English Query Language.
• Same motivation as Python: let us code like speaking English.
• Rapid growth
• Standardized in 1986, and then in 1989, 1992, 1999, 2003, ... 2019
• Now it is a standardized (even ISO) way for database queries.
• Advantages: simple and declarative
• Users do not need to think much
• software can do the operation optimization.
https://www.dsdinc.com/wp-content/uploads/2020/02/SQL_mirror.png


## Slide 41

SQL Overview (cont.)
• Data Definition Language (DDL)
• Specify relation schemas (attributes, domains) 
• Specify a variety of integrity constraints 
• Access constraints on data 
• Indexes and other storage “hints” for performance 
• Data Manipulation Language (DML) 
• Generally based on relational algebra 
• Supports CRUD 
• Very sophisticated features for multi-table queries 
• Other useful tools 
• Defining views, transactions, etc


## Slide 42

SQL Basics
• Remember to add a ; after the SQL statement.
• Allows comments, which can be either single line or a block.
• -- This is a comment for SQL2008.
• /* line 1 line 2 … line n */
• One application often works with one database.
• Many app – one DB more common than one app – many DBs.
• One database often has many tables.
• Relational data model prefers ‘relation’.
• SQL prefers ‘table’. 
• Reserved words: e.g. CREATE, SELECT, TABLE, ..., 
• reserved words cannot be used identifiers unless quoted e.g "table“
• Operators: =, <>, <, <=, >, >=, AND, OR, NOT, ...
• SQL tutorial: many online material
• E.g., https://www.w3schools.com/sql/default.asp https://xsolutions.com/wp-content/uploads/2019/06/imgo-3.jpg


## Slide 43

Names
• Name your databases and tables properly.
• Analyze the application requirements, i.e., StudentICT and Student2019. 
• First character shall be a letter.
• Uppercase and lowercase for different letters in one name.
• Use underscore to connect different words.
• Consistent: follow the same naming schemes for a whole project.


## Slide 44

Data types
• char(n). Fixed length character string, with user-specified length n.
• varchar(n). Variable length character strings, with user-specified maximum 
length n.
• int. Integer (a finite subset of the integers that is machine-dependent).
• smallint. Small integer (a machine-dependent subset of the integer domain 
type).
• numeric(p,d). Fixed point number, with user-specified precision of p digits, with 
d digits to the right of decimal point. (ex., numeric(3,1), allows 44.5 to be stores 
exactly, but not 444.5 or 0.32)
• real, double precision. Floating point and double-precision floating point 
numbers, with machine-dependent precision.
• float(n). Floating point number, with user-specified precision of at least n digits.
• date, time, timestamp. For values contains date and time


## Slide 45

Check
Which SQL data type is best for storing a 
variable-length string like a user’s email 
address?
A) int 
B) char(10) 
C) varchar(50) 
D) float


## Slide 46

SQL operators
• Comparison operators: =,<>,<, >, <=, and >=
• E.g., Value = 50; Value <> 50
• String comparison (e.g. str1 < str2) uses dictionary order
• Boolean operators: AND, OR, NOT 
• E.g., A AND B
• Arithmetic operators: + - * / abs ceil floor power sqrt sin etc.
• E.g., Amount < Credit - Balance


## Slide 47

String value
• Strings are enclosed within single quotes: SELECT * FROM Customer WHERE name = ‘John Doe’
• String values can be compared: =, <,>,<=,>=
• Lexicographic comparisons, ‘alice’ <‘walter’
• Many system case insensitive, need to be evaluated for specific implementation: 'HELLO' = 'hello’ 
• Pattern matching with LIKE operator
• _ (underscore) matches a single character: name LIKE '_i%’
• % matches anything: name LIKE 'Ja%’
• Can escape % or _ with a backslash \: name LIKE ‘Ja\_%’ 
• Other operations:
• String concatenation: name = ‘John’ || ‘Doe’
• String conversion: upper(name), lower(name)
• String-matching tends to be expensive, especially patterns with a leading wildcard, e.g. '%abc’ 
• Try to avoid heavy usage of pattern-matching


## Slide 48

NULL value
• Have different meanings: unknown/ inapplicable/withheld
• NULL is not a constant, expressions containing NULL generally yield NULL.
• E.g., if x = NULL, the condition x > 3 evaluates to NULL
• Can only check if value is NULL use a special expression
• IS NULL, 
• IS NOT NULL
SELECT * 
FROM Person 
WHERE age < 25 OR age >= 25
SELECT * 
FROM Person
WHERE age < 25 OR age >= 25 OR age IS NULL


## Slide 49

DDL:CREATE and DROP TABLE
Create a new table in a database
CREATE TABLE Students ( 
sid serial, 
name varchar(40), 
dob date , 
gender char(1) CHECK (gender in ('M','F')), 
degree integer
); 
• check: checks whether an assertion is true, limit the value range
• Tables are removed via: DROP TABLE table_name
https://tfwiki.net/mediawiki/images2/thumb/6/68/TLK_Quintessa_fac
e.jpg/400px-TLK_Quintessa_face.jpg
Creator
CREATE TABLE TableName (
attribute1 type1 constraints1, 
attribute2 type2 constraints2, 
 .. 
table-level constraints, ... )


## Slide 50

More DDLs
• CREATE DATABASE db_name;
• DROP DATABASE db_name;
• ALTER TABLE table_name ADD column_name datatype;
• ALTER TABLE table_name DROP COLUMN column_name;
• ALTER TABLE table_name MODIFY COLUMN column_name datatype;
• GRANT, REVOKE, etc.
• Some people also use DCL (data control language)
https://en.wikipedia.org/wiki/Column#/media/File:Schema_Saeulenordnungen.jpg


## Slide 51

Integrity constraints in DDL 
• SQL integrity constraints
• primary key (A1, ..., An )
• foreign key (Am, ..., An ) references r
• not null
• SQL prevents any update to the database that violates an integrity constraint.
• Example:
 create table instructor (
 ID char(5),
 name varchar(20) not null,
 dept_name varchar(20),
 salary numeric(8,2),
 primary key (ID),
 foreign key (dept_name) references department);


## Slide 52

Data Manipulation Language (DML) : INSERT
Adding new rows to the existing table, order sensitive.
INSERT INTO table_name (col3, col5, ...)
VALUES (val3, val5, ...);
 
INSERT INTO table_name
VALUES (val1, val2, ...);
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
INSERT INTO sailors 
VALUES(74, ‘Rusty’, 7.5,35)
INSERT INTO RelationName
VALUES Tuple1, Tuple2, Tuple3, ...


## Slide 53

DML: UPDATE
• UPDATE modify the existing records in a table
UPDATE table_name
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE [condition];
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
sid name rating age
22 Dustin 9.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
UPDATE sailors 
SET rating=9.5 
WHERE sid=22


## Slide 54

DML: DELETE
• Delete the existing records from a table
DELETE FROM table_name
WHERE [condition];
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
sid name rating age
22 Dustin 9.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
DELETE FROM sailors 
WHERE sid=74


## Slide 55

DML: SELECT
• The #1 popular SQL keyword.
• Indicate the cols to return, not necessarily for all.
• If all, just use SELECT *.
• Corresponds to which fundamental operator?
• Indicate the table with the cols specified.
• Can be multiple tables, i.e., join them.
• Indicate the selection condition.
• Refer to the selection operator for relational algebra.
• Algebra form:π_{A1, A2, …}(𝜎_P(r1⋈ r2 …).
• Slight difference:
• Relational algebra quite rigorous, assuming set. 
• SQL for performance concern, assuming multi-set: no removing duplication.
• If really want to remove duplications, SQL also can do. 
• SELECT DISTINCT A1, A2, … 
• Just time consuming.
SELECT col1, col2, ...
FROM table_name
WHERE condition
SELECT A1, A2, ...
FROM r1, r2, …
WHERE P


## Slide 56

Check
Which SQL clause is used to check 
whether an attribute value is NULL?
A) WHERE value = NULL 
B) WHERE value <> NULL 
C) WHERE value IS NULL 
D) WHERE value != NULL


## Slide 57

SQL resources
There are many online resources for SQL, please search and pick ones that good for 
you. Some examples:
• W3Schools SQL tutorial: https://www.w3schools.com/sql/
• Khan Academy: https://www.khanacademy.org/computing/computerprogramming/sql
• SQLZoo: https://sqlzoo.net/wiki/SQL_Tutorial
• FreeCodeCamp: 4 hours video on youtube
https://www.freecodecamp.org/news/sql-and-databases-full-course/


## Slide 58

Recap
• Relational algebra
• Why study relational algebra
• 6 fundamental operators and 3 derived ones
• Some examples
• Integrity constrains
• SQL
• Basic knowledge: history, name convention, data types
• SQL expression, special values: String, NULL
• DDL and basic DML query


## Slide 59

Lab 2
SQL Basics in MariaDB
• MariaDB is an open-source MySQL
• Practice database software
• Perform simple DB manipulation using SQL 
• You are encouraged to explore more on your own
Submission:
Use the template provided, for each question, please attach the screenshot 
(note: not taking photos) to capture both your queries and outputs.


---

# Lecture 3

*Source: INF2003_AY2425_T1_Lec03*


## Slide 1

INF2003:
Database system
SQL Part 2
AY2025/26 Trimester 1
Dr. Tong Rong


## Slide 2

SIT Internal
From last week
https://www.gatevidyalay.com/relational-algebra-relational-algebra-in-dbms
Natural Join (⋈)
Left, Right, Full outer 
join (⟕, ⟖, ⟗)
SQL basics
Name convention
Data types
SQL expression
DDL, DML


## Slide 3

SIT Internal
Outline – this week
• Update database: INSERT/UPDATE/DELETE
• Retrieve information: SELECT
• WHERE condition
• UNION, INTERSECT, EXCEPT
• Nested query
• Aggregation operators
• Grouping and Partition
• Set comparison
• Check
• Order by


## Slide 4

SIT Internal
INSERT
Adding new rows to the existing table, order sensitive.
INSERT INTO table_name (col3, col5, ...)
VALUES (val3, val5, ...);
 
INSERT INTO table_name
VALUES (val1, val2, ...);
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
INSERT INTO sailors 
VALUES(74, ‘Rusty’, 7.5,35)
INSERT INTO RelationName
VALUES Tuple1, Tuple2, Tuple3, ...


## Slide 5

SIT Internal
UPDATE
• UPDATE modify the existing records in a table
UPDATE table_name
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE [condition];
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
sid name rating age
22 Dustin 9.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
UPDATE sailors 
SET rating=9.5 
WHERE sid=22


## Slide 6

SIT Internal
DELETE
• Delete the existing records from a table
DELETE FROM table_name
WHERE [condition];
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
sid name rating age
22 Dustin 9.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
DELETE FROM sailors 
WHERE sid=74


## Slide 7

SIT Internal
SELECT
• The #1 popular SQL keyword.
• Indicate the cols to return, not necessarily for all.
• If all, just use SELECT *.
• Corresponds to which fundamental operator?
• Indicate the table with the cols specified.
• Can be multiple tables, i.e., join them.
• Indicate the selection condition.
• Refer to the selection operator for relational algebra.
• Algebra form:π_{A1, A2, …}(𝜎_P(r1⋈ r2 …).
• Slight difference:
• Relational algebra quite rigorous, assuming set. 
• SQL for performance concern, assuming multi-set: no removing duplication.
• If really want to remove duplications, SQL also can do. 
• SELECT DISTINCT A1, A2, … 
• Just time consuming.
SELECT col1, col2, ...
FROM table_name
WHERE condition
SELECT A1, A2, ...
FROM r1, r2, …
WHERE P


## Slide 8

SIT Internal
SELECT with arithmetic operations
Possible to use arithmetic operations: 
• Addition, subtraction, multiplication, division, 
modulo, etc
• Use aliases to generate a temporary name
• useful when involving a table more than once
• Keyword ‘AS’ is optional
SELECT sid, name,
 rating/2 AS new_rating, age
FROM Sailors;
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
Sailors
sid name new_rating age
22 Dustin 3.75 45
31 Lubber 4.0 55
58 Rusty 4.5 35
74 Rusty 3.75 35


## Slide 9

SIT Internal
Rename
• Can specify alternate names in FROM clause too
• Syntax: table AS name
• The AS is optional, but it’s clearer to leave it in.
• Useful for referencing long table name
• When a table is renamed in FROM , the new name can be used in both 
SELECT and WHERE clauses
SELECT c.cust_name, l.amount
FROM customer AS c, borrower AS b, loan AS l
WHERE c.cust_name = b.cust_name AND b.loan_id = l.loan_id;
• 37


## Slide 10

SIT Internal
WHERE with Multiple Tables
• Q1: Find the sid of the sailors who have reserved a red boat.
• Where to find sid? Where are colors? Can connect?
• Choose the option with less tables.
• Q2: Find the names of the sailors who have reserved a red boat.
• Where to find S.name? color? Can connect?
• Cannot directly, then we need a middleman.
Ans 1:
SELECT R.sid
FROM Reserves R, Boats B
WHERE R.bid=B.bid AND B.color=‘red’
Ans 2: 
SELECT S.name
FROM Sailors S, Reserves R, Boats B
WHERE S.sid=R.sid AND R.bid=B.bid AND B.color=‘red’
sid name rating age
Sailors
bid name color
Boats
Reserves
sid bid day


## Slide 11

SIT Internal
WHERE Advanced 
Q1: Add 0.5 to the ratings of the sailor who sailed different boats 
on the same day.
• Many condition components, overwrite the rating.
• Same cols comparison? Duplicate the tables.
SELECT S.name, S.rating + 0.5 AS rating
FROM Sailors S, Reserves R1, Reserves R2
WHERE S.sid=R1.sid AND S.sid = R2.sid AND R1.day=R2.day 
AND R1.bid <> R2.bid
SELECT S1.name AS name1, S2.name AS name2
FROM Sailors S1, Sailors S2
WHERE S1.rating = S2.rating + 1.0
Q2: Find the pair of sailors where the former has 1.0 
higher rating than the later.
Same. Duplicate for same table comparison.
Do math in WHERE.
sid name rating age
Sailors
bid name color
Boats
Reserves
sid bid day


## Slide 12

SIT Internal
UNION, INTERSECT, EXCEPT
• SQL set-manipulation constructs: UNION, INTERSECT, EXCEPT.
• Same relation schema. Same requirement as relational algebra. 
• Find sailor names who have reserved a red or a green boat.
SELECT S.name
FROM Sailors S, Boats B, Reserves R
WHERE S.sid=R.sid AND R.bid=B.bid AND 
(B.color=‘red’ OR B.color=‘green’)
Another Option:
SELECT S1.name
FROM Sailors S1, Boats B1, Reserves R1
WHERE S1.sid=R1.sid AND R1.bid=B1.bid 
 AND B1.color=‘red’
UNION
SELECT S2.name
FROM Sailors S2, Boats B2, Reserves R2
WHERE S2.sid=R2.sid AND R2.bid=B2.bid 
 AND B2.color=‘green’
Which one do you like? Challenge ourselves, or 
computer? Reuse?
sid name rating age
Sailors
bid name color
Boats
Reserves
sid bid day


## Slide 13

SIT Internal
UNION
Find the sid of the sailors who have a rating of 10 or 
reserved boat 104. 
• different from red/green example
• same columns
• different tables
SELECT S.sid
FROM Sailors S
WHERE S.rating = 10
UNION
SELECT R.sid
FROM Reserves R
WHERE R.bid = 104
sid name rating age
Sailors
bid name color
Boats
Reserves
sid bid day


## Slide 14

SIT Internal
INTERSECT
Find name of sailors who reserved a red and a green boat.
Option 1:
SELECT S.name
FROM Sailors S, 
Reserves R1, Boats B1, 
Reserves R2, Boats B2
WHERE S.sid=R1.sid AND R1.bid=B.bid
AND S.sid=R2.sid AND R2.bid=B2.bid 
AND (B1.color=‘red’ AND B2.color=‘green’)
Option 2:
SELECT S1.name 
FROM Sailors S1, Boats B1, Reserves R1
WHERE S1.sid=R1.sid AND R1.bid=B1.bid AND B1.color=‘red’
INTERSECT
SELECT S2.name 
FROM Sailors S2, Boats B2, Reserves R2
WHERE S2.sid=R2.sid AND R2.bid=B2.bid AND 
B2.color=‘green’
Which one do you like more?
sid name rating age
Sailors
bid name color
Boats
Reserves
sid bid day


## Slide 15

SIT Internal
EXCEPT (Set Difference)
Find the sid of sailors who’ve reserved red boat but 
not green ones.
Option 1 :
SELECT S.sid
FROM Sailors S1, Boats B1, Reserves R1
WHERE S1.sid=R1.sid AND R1.bid=B1.bid AND B1.color=‘red’
EXCEPT
SELECT S2.sid 
FROM Sailors S2, Boats B2, Reserves R2
WHERE S2.sid=R2.sid AND R2.bid=B2.bid AND 
B2.color=‘green’
Option 2 (less tables can do):
SELECT R.sid
FROM Boats B1, Reserves R1
WHERE R1.bid=B1.bid AND B1.color=‘red’
EXCEPT
SELECT R2.sid 
FROM Boats B2, Reserves R2
WHERE R2.bid=B2.bid AND B2.color=‘green’
sid name rating age
Sailors
bid name color
Boats
Reserves
sid bid day
can improve?


## Slide 16

SIT Internal
Set – UNION, INTERSECT, EXCEPT
• By default: no duplication for UNION in SQL, set operation
• To retain duplicates, use UNION ALL.
• Similarly, INTERSECT ALL and EXCEPT ALL.
• In terms of efficiency, with ALL is faster, as it doesn’t 
need to remove duplicated ones.
• Find Name of staff from all the departments.
ID Name
001 Tony Wong
002 Alice Neo
004 Pricilla 
ID Name
101 Brian Lim
102 Jackson Wong
104 Pricilla 
Finance
HR
SELECT Name 
FROM Finance
UNION ALL
SELECT Name 
FROM HR
Name
Tony Wong
Alice Neo
Pricilla 
Brian Lim
Jackson Wong
Pricilla


## Slide 17

SIT Internal
Nested Queries
• Nested query
• Subquery embedded. Refer to the nested loops in Python or C.
• Multiple levels. (Be mindful about the readability as well)
• Typically, in WHERE clause. Sometimes also in FROM and HAVING clauses.
• Find the names of the sailors who have reserved boat #103.
• The subquery gets the sid for sailors who have reserved boat 103.
• The top-level query retrieves the names by sid.
SELECT S.name
FROM Sailors S
WHERE S.sid IN
(SELECT R.sid
FROM Reserves R
WHERE R.bid=103)
sid name rating age
Sailors
bid name color
Boats
Reserves
sid bid day


## Slide 18

SIT Internal
Aggregate Operators
• Besides retrieving data, want to perform some statistics, e.g. computation and 
summarization.
• SQL supports five aggregate operations
• SUM(): Returns the sum or total of each group.
• COUNT(): Returns the number of rows of each group.
• AVG(): Returns the average and mean of each group.
• MIN(): Returns the minimum value of each group.
• MAX(): Returns the minimum value of each group.
• Use DISTINCT if for counting unique ones.
• Can be applied to any columns.


## Slide 19

SIT Internal
Aggregate Operators
• Q1: Count number of sailors.
• Q2: Find the average age of the sailors with rating higher than 8.5.
• Q3: Find the name and age of the oldest sailor.
sid name rating age
22 Dustin 7.5 45
31 Lubber 8.0 55
58 Rusty 9.0 35
74 Rusty 7.5 35
Sailors
Q2:
SELECT AVG (age)
FROM Sailors
WHERE rating>8.5
Q3:
SELECT S1.name, S1.age
FROM Sailors S1
WHERE S1.age = 
(SELECT MAX(S2.age) FROM Sailors S2)
Q1:
SELECT COUNT (*)
FROM Sailors S


## Slide 20

SIT Internal
Aggregate Operators (cont.)
• Aggregate functions compute a single value from a multiset of inputs 
• The condition cannot include the aggregate
• Doesn’t make sense to combine individual attributes and aggregate functions, 
which is correct?
SELECT name, MAX(age)
FROM Sailors
SELECT MIN(age), MAX(age)
FROM Sailors
SELECT name, n_visits
FROM guests 
WHERE n_visits > AVG(n_visits);
SELECT name, n_visits
FROM guests 
WHERE n_visits > 
(SELECT AVG(n_visits) 
FROM guests);
• If SELECT clause uses aggregate operation 
• must use only aggregate operations 
• or via GROUP BY
• which on the right is correct?


## Slide 21

SIT Internal
Grouping – Group by
• Split: partition result relation into groups (according to values of specified 
attribute)
• Apply: aggregate some aspects of each group
• Combine: output one tuple per group, with grouping attribute and aggregates
https://www.datacamp.com/tutorial/group-by-having-clause-sql


## Slide 22

SIT Internal
Filtering groups
HAVING is used to qualify a GROUP-BY clause:
SELECT attributes/aggregations
FROM relations
WHERE condition1 (on tuples)
GROUP BY attributes
HAVING condition2; (on group)
Semantics of HAVING:
• generate the groups as for GROUP-BY
• discard groups not satisfying HAVING condition
• apply aggregations to remaining groups
https://www.datacamp.com/tutorial/group-by-having-clause-sql


## Slide 23

SIT Internal
Grouping and NULL
• NULL is ignored in Aggregation
• COUNT returns 0 for an empty input multiset
• All others return NULL for an empty input (even SUM !)
• On the other hand, NULL is treated as an ordinary value in a grouped attribute
1008 Peter NULL 0
NULL 0


## Slide 24

SIT Internal
UNIQUE
• Some relations have multiple candidate keys: specify candidate keys 
with UNIQUE constraints 
• Can only specify multi-column candidate key after the column 
specifications 
• Unlike primary keys, UNIQUE constraints do not exclude NULL values! 
• This constraint considers NULL values to be unequal! 
• If some attributes in the UNIQUE constraint allow NULLs, DB will 
allow multiple rows with the same values
• Example:
• Employee’s ID is the primary key 
• Every employee needs an SSN, but no two have the same SSN 
• Don’t forget NOT NULL constraint too! 
• Every employee should have a name
• but multiple employees might have same name
CREATE TABLE employee ( 
 emp_id INT PRIMARY KEY, 
 emp_ssn CHAR(9) NOT NULL UNIQUE, 
 emp_name VARCHAR(40) NOT NULL, ... 
);


## Slide 25

SIT Internal
UNIQUE and NULL
• Example relation:
• Try :
INSERT INTO customer VALUES ('John Doe', '123 Spring Lane’); 
INSERT INTO customer VALUES ('John Doe', '123 Spring Lane’);
INSERT INTO customer VALUES ('Jane Doe', NULL); 
INSERT INTO customer VALUES ('Jane Doe', NULL); 
• Be careful using nullable columns in UNIQUE constraints!
• Usually, you really want to specify NOT NULL for all columns that 
appear in UNIQUE constraints
CREATE TABLE customer ( 
cust_name VARCHAR(30) NOT NULL, 
address VARCHAR(60), 
UNIQUE (cust_name, address) )


## Slide 26

SIT Internal
Empty set test
Test whether or not a subquery generates any results at all
• EXISTS (...)
• NOT EXISTS (...)
Example:
 Find customers with an account but not a loan
SELECT DISTINCT customer_name FROM depositor d
WHERE NOT EXISTS (
SELECT * FROM borrower b
WHERE b.customer_name = d.customer_name);


## Slide 27

SIT Internal
Set-Comparison Operators
• Also available: op ANY, op ALL, op IN, with
• Ops: ≥, ≤, ≠, <, >, =, ….
• IN tests whether a value is in a set, equivalent to = ANY.
• NOT IN is equivalent to <> ALL.
• Q1: Find sailors with rating greater than any sailor called guppy.
• Q2: Find sailors with rating greater than every sailor called Sheldon.
• Q3: Find sailors with the highest rating.
Ans1 1:
SELECT *
FROM Sailors S1
WHERE S1.rating > ANY (
 SELECT S2.rating
 FROM Sailors S2
 WHERE S2.name=‘guppy’)
Ans 2:
SELECT *
FROM Sailors S
WHERE S.rating > ALL (
 SELECT S2.rating
 FROM Sailors S2
 WHERE S2.sname=‘Sheldon’)
Ans 3: 
SELECT *
FROM Sailors S1
WHERE S1.rating >= ALL ( 
 SELECT S2.rating
 FROM Sailors S2


## Slide 28

SIT Internal
Set comparison test
• Compare a value to a set of values: Is a value larger/smaller etc. 
than some value in the set?
• Find all branches with assets greater than at least one 
branch in AMK.
• General form of test: attr compare_op SOME ( subquery ) 
• Can use any comparison operation 
SOME is same as IN
• ANY is a synonym for SOME
• Can also compare a value with all values in a set 
Use ALL instead of SOME
<> ALL is same as NOT IN
• Find branches with assets greater than all branches in AMK
SELECT branch_name
FROM branch 
WHERE assets > SOME ( 
SELECT assets 
FROM branch 
WHERE branch_name=‘AMK’)
SELECT branch_name
FROM branch 
WHERE assets > ALL (
 SELECT assets 
 FROM branch
 WHERE branch_name =‘AMK')
SELECT branch_name
FROM branch 
WHERE assets > (
 SELECT MAX(assets) 
 FROM branch 
WHERE branch_name=AMK')


## Slide 29

SIT Internal
CHECK for Constraints
• CHECK constraint is used to constraint values to satisfy some predicate
• Very effective for constraining columns’ domains, and eliminating obviously bad inputs
• It must appear after the column specification 
• Attribute-based: checked if a tuple gets new value via INSERT or UPDATE.
• Check new values only, and old values are unchecked.
• Tuple-based: checked every time a tuple is inserted or updated.
• Involves ≥ 1 attribute of the tuple, must be a tuple-based constraint.
• Will be checked more frequently than attribute-based
• Must consider efficiency issue in design.
• In theory, can specify any expression that generates a Boolean result 
• This includes nested subqueries! 
• In practice, DBMS support for CHECK constraints varies widely, and is often quite limited
https://i.dlpng.com/static/png/6785165_preview.png


## Slide 30

SIT Internal
CHECK for Constraints - example
CHECK constraint is used to constraint values to satisfy some predicate
Q1: The value stored in age should large than 0
Q2: For sailor, the rating must be an integer in the range 1 to 10.
Q3: Define a new domain with CREATE DOMAIN, using CHECK constraints.
CREATE TABLE Sailors (
 sid INTEGER, name CHAR(10), rating INTEGER, age INTEGER,
 PRIMARY KEY (sid),
 CHECK ( rating >= 1 AND rating <= 10 ) )
CHECK (age >0 )
CREATE DOMAIN rtval INTEGER DEFAULT 1
 CHECK (VALUE>=1 AND VALUE<=10)
-- define schema
Sailors(name char(10), rating rtval);
CREATE TABLE Sailors ( 
 sid INTEGER, sname CHAR(10), 
 rating INTEGER, age INTEGER,
 PRIMARY KEY (sid),
 CHECK ( 
 (SELECT COUNT(Sailors.sid) FROM Sailors) + 
 (SELECT COUNT(Boats.bid) FROM Boats) < 100)
Q4: Enforce constraint that the number of boats 
plus the number of sailors is less than 100.


## Slide 31

SIT Internal
ORDER BY
• SQL result is unsorted by default.
• Sort: based on the values of ≥ 1 attribute.
• if multiple attributes, must have an order of the attributes.
• ORDER BY < list of attributes >.
• By default: ascending. Equivalent to use ORDER BY ASC
• Descending: ORDER BY DESC < list of attributes >.
• Normally after WHERE, GROUP BY, and HAVING.
• For GROUP BY, performed in each group.
• The results are passed to SELECT for output.
• More advanced usage: ORDER BY A+B DESC.
• Order by the summation of the two components A and B. 
SELECT *
FROM Sailors
ORDER BY age;
sid name rating age
22 Dustin 7 45
31 Lubber 8 55
58 Rusty 8 35
74 Rusty 7 35
Sailors
SELECT *
FROM Sailors
ORDER BY age DESC;
SELECT *
FROM Sailors
ORDER BY rating ASC, age DESC;
https://i.pinimg.com/originals/a9/c7/45/a9c7453ffda1
34329bbbab86f467d0cb.jpg


## Slide 32

SIT Internal
JOIN
SELECT table1.column_name, table2.column_name 
FROM table1 [JOIN TYPE] table2
ON table1.linking_column = table2.linking_column;
Join type: inner join, left (outer) join, right (outer) join, full (outer) join
Example:
SELECT customers.customer_name, orders.order_date
FROM customers INNER JOIN orders
ON customers.customer_id = orders.customer_id;


## Slide 33

SIT Internal
SQL functions
• SQL queries can use sophisticated math operations and functions 
• compute simple functions, aggregates
• compute and filter results 
• Sometimes, apps require specialized computations 
• Would like to use these in SQL queries, too 
• SQL provides a mechanism for defining functions
• User-Defined Function (UDF)
• Can be defined in a procedural SQL language, or in an external language
• Different vendors provide their own languages 
• Oracle: PL/SQL
• Microsoft: Transact-SQL (T-SQL) 
• PostgreSQL: PL/pgSQL
• MySQL: stored procedure 
• Some also support external languages: Java, C, C#, etc


## Slide 34

SQL query optimization


## Slide 35

SIT Internal
Query optimization
The process of refining SQL queries to improve their efficiency and performance.
Factors Affecting Performance:
data volume, query complexity, and hardware capabilities.
Optimization Goals:
 reducing execution time, minimizing resource consumption, and improving scalability
Monitor
Execution plan: step-by-step strategy outlines how the database will process the query
https://mariadb.com/kb/en/explain/


## Slide 36

SIT Internal
SQL query optimization example 
Optimize Select (1)
• Use Select instead of Select *
SELECT customer_id, customer_name, email
FROM customers;
• Avoid removing duplication if it is not important
SELECT Distinct -> SELECT
UNION ALL -> UNION
• Keep Wild cards at the End of Phrases
SELECT name, salary From Employee Where name like ‘%Ram%’;
SELECT name, salary From Employee Where name like ‘Ram%’;


## Slide 37

SIT Internal
Optimize Select (2)
Use Exist() instead of Count()
Find all customers that placed at least one order
SELECT customer_id
FROM customers
WHERE (SELECT COUNT(*) FROM orders WHERE orders.customer_id = customers.customer_id) > 0;
SELECT customer_id
FROM customers
WHERE EXISTS (SELECT 1 FROM orders WHERE orders.customer_id = customers.customer_id);
Exist() will run till it finds the first matching entry whereas
Count() will keep on running and provide all the matching records


## Slide 38

SIT Internal
Optimize Select (3)
Optimize by using faster operation
SELECT * FROM users WHERE id IN ( SELECT DISTINCT user_id FROM sessions WHERE session_date =
'2024-02-01’); 
SELECT * FROM users WHERE EXISTS ( SELECT DISTINCT user_id FROM sessions WHERE session_date =
'2024-02-01’);
• replace ‘id IN’ by ‘EXISTS’ will be faster
• EXISTS lets the database stop looking the moment it finds a matching record,
• while IN may require going through the whole dataset to gather the smaller group for comparison.


## Slide 39

SIT Internal
Subquery optimization
Find the total order amount for each customer. 
SELECT customer_id, (SELECT SUM(order_amount) FROM orders WHERE orders.customer_id = 
customers.customer_id) AS total_sales
FROM customers;
iterates over each customer and executes a subquery to calculate their total sales: inefficient for large
datasets.
SELECT customers.customer_id, SUM(orders.order_amount) AS total_sales
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id;
Join->group->sum


## Slide 40

SIT Internal
Join optimization
Select the JOIN type that aligns with the data you want to retrieve.
 SELECT * FROM orders, customers; 
 not efficient, will join everything
 SELECT orders.order_id, customers.customer_name
 FROM orders INNER JOIN customers 
 ON orders.customer_id = customers.customer_id;


## Slide 41

SIT Internal
Other strategies
• Use Indexes
• Identify frequently used columns in WHERE clauses, JOIN conditions, and ORDER BY clauses, 
and create indexes on those columns.
• However, creating too many indexes can slow down adding and updating data, so use them 
strategically.
• Use query optimization tools
• Some popular query optimization tools include Microsoft SQL Server Query Optimizer, Oracle SQL 
Developer, and MySQL Query Optimizer.
https://dev.mysql.com/doc/workbench/en/wb-performance.html
https://www.postgresql.org/docs/current
/performance-tips.html
https://docs.oracle.com/en/cloud/paas/exadata-expresscloud/csdbp/use-sql-tuning-advisor-sql-developer-sqltuning.html


## Slide 42

SIT Internal
SQL Programming Good Practices
• Good coding style is critical for almost all programming languages.
• Names: e.g., for table and column, use lowercase and meaningful words.
• Comment: make sure people can pick up your idea in a short time.
• Do not expect people, even ourselves, to check the code with a magnifier.
• Length: like comment for readability, e.g., within 80 chars per line
• Some editors do not wrap automatically for us.
• Even they wrap, shall be concise and clear.
• Keyword: e.g., SELECT and WHERE, use uppercase.
• Indentation: be consistent.
• e.g., 4-space or 1-tab.
• e.g., indent for cols in a table.


## Slide 43

SIT Internal
Lab 3
• Complex SQL Queries
• Sample data: online book exchange
• Perform data manipulation using SQL 
• You are encouraged to explore more


---

# Lecture 4

*Source: INF2003_AY2425_T1_Lec04*


## Slide 1

INF2003:
Database system
Database Refinement
AY2025/26 Trimester 1
Dr. Tong Rong


## Slide 2

From last week
• DML
• Update database: INSERT/UPDATE/DELETE
• Retrieve information: SELECT
• UNION, INTERSECT, EXCEPT
• Nested query
• Aggregation operators
• Grouping 
• Set comparison
• Order by
• JOIN
• Query optimization


## Slide 3

Stages of Database Design
S1 • Requirement Analysis
S2 • Conceptual Database Design
S3 • Logical Database Design
S4 • Refine the Schemas
S5 • Physical Database Design
S6 • Application and Security Design


## Slide 4

Outline – this week
• Data Anomalies
• Functional dependency (FD)
• Attribute Closure
• Normalization
• Normal forms
• Decomposition


## Slide 5

Relational design and redundancy
A good relational database design:
• must capture all necessary attributes/associations
• do this with minimal amount of stored information
• Minimal stored information ⇒ less redundant
• Redundancy
• In database design, redundancy is generally a "bad thing"
• causes problems maintaining consistency after updates
• Redundant Rows: Unnecessary data, waste space
• Redundant Rows = Slow Updates or Inconsistent Data
• But certain redundancy may give performance improvements
• e.g. avoid a join to collect pieces of data together


## Slide 6

Database Refinement
• Given an application, the database design is not unique. 
• Capture all the information needed - entity relationship (ER) diagram
• Achieve the above with little redundancy - normalization
• With many choices, which is the best one?
• We might never know.
• But very often, our design is not the best. Space to improve.
• Refinement/ Normalization: from better or best
• No missing information.
• Easy for information management; easy to add constraints. 
• No unnecessary redundancy. 
• Redundancy: repetition of data or duplicate data stored in different locations.
• Some redundancy cannot be avoided.


## Slide 7

Anomalies
Anomalies refers to the problems occurred on poorly 
planned databases
• Insertion anomalies: not possible to store information 
unless some other information is stored.
Insert new module: python without SID
• Redundant anomalies : some information is stored 
repeatedly
ModuleName (c++) and Fee (500)
• Update anomalies : If one data is updated, inconsistency is 
created unless all data are updated.
When Fees changed, multiple tuples to be revised
• Deletion anomalies : not possible to delete information 
without losing some other information. 
Delete student S3 will cause deletion of module M2
SID Sname ModuleID ModuleName Fee
S1 A M1 C++ 500
S2 B M1 C++ 500
S3 C M2 JAVA 400
Solution: 
Decomposition


## Slide 8

Decomposition
• Process of decomposing a larger relation 
into smaller relations:
• replacing relation schema by ≥ 2 schemas
• each with a subset of the attributes
• these subsets together include all 
attributes.
• Example: 
• decompose into 2 relations.
• efficient, eliminate potential 
redundancy.
SID Sname ModuleID ModuleName Fee
S1 A M1 C++ 500
S2 B M1 C++ 500
S3 C M2 JAVA 400
SID Sname ModuleID
S1 A M1
S2 B M1
S3 C M2
ModuleID ModuleName Fee
M1 C++ 500
M2 JAVA 400


## Slide 9

Check
In the single table at right, it stores 
employee and the projects they are
involving.
Which of the following action may cause
anomaly? 
A) Add Bob to project Gamma
B) Remove Alice from project Beta
C) Increase budget of project P3 to 400
D) Remove Alice from project Alpha
EID Ename ProjectID ProjectName Budget
10 Alice P1 Alpha 500
10 Alice P2 Beta 400
8 Bob P1 Alpha 500
9 Carl P3 Gamma 300
Employee


## Slide 10

Functional dependency (FD)
FD: the association between any two attributes:
• the non-key attribute is functionally dependent on the primary key attribute
• denoted as: X->Y, attribute Y is functionally dependent on X (or X determines Y)
• for any two tuples t1 and t2 of the relation R:
if t1[X] = t2[X] 
then t1[Y] = t2[Y] 
Study FDs: potential refinement to the schema.


## Slide 11

Functional dependency (FD) example
• FD X → Y : X functionally determines Y or X determines Y.
• FDs allow us to express constraints that cannot be expressed using superkeys. 
 EmpID → Name, Phone, Position
EmpID Name Phone Position
E0045 Smith 1234 Clerk
E3542 Mike 9876 Salesrep
E1111 Smith 9876 Salesrep
E9999 Mary 1234 Lawyer
… Phone Position
… 1234 Clerk
… 9876 ← Salesrep
… 9876 ← Salesrep
… 1234 Lawyer
… Phone Position
… 1234 → Clerk
… 9876 Salesrep
… 9876 Salesrep
… 1234 → Lawyer
Position → Phone Phone → Position


## Slide 12

Functional dependency (cont.)
• A legal instance must satisfy ALL specified ICs, including FDs.
• FD is a statement about all possible legal instances of the relation.
• Looking at an instance, we may tell that a certain FD does not hold.
• But we cannot deduce that an FD does hold just by looking at one instance.
• FD: AB -> C. (check if the instances satisfy?)
• An FD is not the same as a key constraint. (See the 1st 2 tuples) 
• If two tuples differ in either the field A or B, they must differ in the C field without 
violating the FD. (See the 3rd and 4th tuples) 
• Can we add tuple: (a1, b1, c2, d1 )?
• Cannot! conflicts with 1st 2 tuples
• Any violation -> “bad” FD.
• Reality: do not know all FDs initially. How to find all?
• Inference rules allow us to derive dependencies
A B C D
a1 b1 c1 d1
a1 b1 c1 d2
a1 b2 c2 d1
a2 b1 c3 d1
a1 b1 c2 d1


## Slide 13

Armstrong’s Axioms
A set of inference rules to infer FD, applied repeatedly to infer all FDs.
Let X, Y, Z denote sets of attributes over relation R.
• Reflexivity: if X ⊆ Y, then Y -> X.
{Name} ⊆ {Name, Phone}, hence {Name, Phone} -> {Name}
• Augmentation: if X -> Y, then XZ -> YZ for any Z.
{ID} -> {Name}, hence {ID, Phone} ->{Name, Phone}
• Transitivity: if X -> Y and Y -> Z, then X -> Z.
{ID} ->{Name}, and {Name} ->{Phone}, hence {ID}->{Phone}
ID Name Phone Module
0001 John 12341234 ICT1001
0002 Mike 56785678 ICT1002
0003 Smith 98769876 ICT1001
0004 Mary 12345431 ICT1002


## Slide 14

Armstrong’s Axioms – additional rules
Rules inferred from Armstrong’s Axioms.
Name Rule Proof
Union if X -> Y and X -> Z, 
then X -> YZ
X->XZ (XX->XZ) augmentation
XZ->YZ augmentation
X->YZ transitivity
Decomposition if X -> YZ, 
then X -> Y and X -> Z
X->YZ
YZ->Y reflexivity
X->Y transitivity
Similarly, X->Z
PseudoTransitivityif X -> Y, and YZ -> U, 
then XZ -> U.
XZ->YZ augmentation
YZ-> U
so XZ->U, transitivity


## Slide 15

Inference example
• Given a set of FDs, we can infer from them to get additional FDs.
 Contracts(cid, sid, jid, did, pid, qty, value)
• cid: contract id; sid: supplier id; jid: job id; did: department id; pid: parts id; qty: quantity; value
• Contract C: supplier S will supply quantity Q of items of part P to job J associated with department 
D, V is the contract value.
• Given FDs (often not our job to think about, why?):
• C -> CSJDPQV C (capital letter of cid) is the primary key
• JP -> C A Job purchases each part using a contract
• SD -> P Department purchases at most one part from a supplier
• From Armstrong’s axioms
• Transitivity: JP -> C and C -> CSJDPQV imply JP -> CSJDPQV.
• Augmentation: SD -> P implies SDJ -> JP.
• Transitivity: SDJ -> JP and JP -> C imply SDJ -> C.
• Decomposition: C -> C, C -> S, C -> J, C -> D, …


## Slide 16

Closure
• Given a set of FDs, how many new FDs can we derive? How to find all FDs? 
• It is difficult to use inference rules in practice. Use closure. 
• Closure of X, denoted as X
+ , where X is a set of attributes
• X
+ is the complete set of all possible attributes that can be functionally derived from 
given functional dependency using the inference rules (Armstrong’s).
• Closure algorithm
Input: attributes X and a set of FDs F; Output: X
+ 
Split FDs, each FD has single attribute at the right hand side
Result := X
While (changes to result) do
for each B->Y in F do
if B ⊆ Result then Result := Result ∪ Y 
X
+ := Result


## Slide 17

Computing Closure – Example 
Input: {name, category} and FDs.
Output: what is {name, category}+?
• Split FD with single attribute on right hand side (already satisfied here)
• Initialize X = {name, category}.
• Look at FD name -> color AND name ∈ X, so add color to X.
• X = {name, category, color}
• Look at FD category -> department AND category ∈ X, so add department to X.
• X = {name, category, color, department}
• Look at FD color, category -> price AND {color, category} are all in X, so add price to X.
• X = {name, category, color, department, price}
• X = {name, category, color, department, price}. (no more changes if repeat)
So {name, category}+ = {name, category, color, department, price}.
Or, name, category -> color, department, price.
name -> color
category -> department
color, category -> price


## Slide 18

Why closure
• Why do we need closure?
• With closure we can find all FDs easily.
• Use closure to obtain all super keys.
• Start with a set X containing a single attribute.
• Stop as soon as closure contains all attributes in the relation schema.
• By varying the starting attribute, you can obtain all super keys.
• Closures allow us to answer two interesting questions:
• Is a particular dependency X → Y derivable from F?
• Check whether Y in the closure of X
• Are two sets of dependencies F and G equivalent?
• Compare their closures


## Slide 19

Closure – how to use it
Given a set of FDs F:
Q1: what are the keys of R implied by F?
• find subsets K ⊂ R such that K
+ = R
Q2: is X → Y derivable from F? 
• compute the closure X
+
, check whether Y ⊂ X
+
Q3: are F and G equivalent?
• for each dependency in G, check whether derivable from F
• for each dependency in F, check whether derivable from G
• if true for all, then F → G and G → F which implies F and G are equivalent


## Slide 20

Closure example
• Does D -> A hold according to the set of FDs at right?
 Solve: Compute D+ and check whether A is in D+.
• Split BC -> AD into BC -> A and BC -> D. (Decomposition)
• X = {D}.
• Look at D -> E and D is in X, add {E} to X.
• X = {D, E}.
• No more changes possible.
• {D}+ = {D, E}
• Since A is not in {D}+, then D -> A does not hold.
A, B -> C
B, C -> A, D
D -> E
C, F -> B


## Slide 21

Determine keys
Determine super keys for each of the following:
• FD = { A → B, C → D, E → FG }
1. Check A? A
+ = AB, not a super key
2. Check AB? AB + = AB, not a super key
3. Check ACE? ACE + = ABCDEFG, yes, super key
• FD = { A → B, B → C, C → D }
1. Check B? B
+ = BCD, not a super key
2. Check A? A
+ = ABCD, yes, super key
• FD = { A → B, B → C, C → A }
1. Check A? A
+ = ABC, yes, super key
2. Check B? B
+ = ABC, yes, super key


## Slide 22

Normalization/Refinement
• FD whose left hand side is not a super key, hint a redundancy
• Normalization: 
• process of designing a consistent database with minimum redundancy
• if a relation is in a normal form certain kinds of problems can be avoided/minimized. 
• normalization algorithms reduce the amount of redundancy by decomposition
• Normal forms
• 1NF: All rows must contain the same number of fields (table is flat).
• 2NF: No partial key dependency (old and obsolete).
• 3NF: No attributes dependent on non-key attributes, defined by E. F. Codd in 1971.
• BCNF: extension of 3NF, developed in 1975 by Raymond F. Boyce and Edgar F. Codd.
• 4NF and 5NF (not covered and mostly not popular as well).
For most practical purposes, BCNF is acceptable NFs.
most redundancy
least redundancy


## Slide 23

First Normal Form (1NF)
• A database schema is in 1NF if all tables are flat (no lists or sets).
Name GPA Course
Alice 3.8 Math; DB; OS
Bob 3.7 DB; OS
Carol 3.9 Math; OS
Name GPA
Alice 3.8
Bob 3.7
Carol 3.9
Course
Math
DB
OS
Name Course
Alice Math
Alice DB
Alice OS
Bob DB
Bob OS
Carol Math
Carol OS


## Slide 24

Boyce-Codd Normal Form (BCNF)
BCNF: a condition under which we can guarantee there is no anomalies.
• Definition: if and only if for every of its dependencies X → Y :
• X → Y is a trivial FD (trivial: Y is a subset of X ). 
• A → A is a trivial functional dependency 
• AB → A is also a trivial functional dependency
• Or X is a superkey
• Equivalently: 
• ∀X, either (X+ = X) 
• OR (X+ = all attributes)
• Overall, relation in BCNF will have no “bad” FDs.


## Slide 25

BCNF example
Product(name, price, category, color), F ={(name, category) -> price; category -> color}
• (name, category)+ = name, category, price, color. 
• It is a key. Good FD.
• (category)+ = category, color. 
• So, (category) is NOT a key. Bad FD.
• Relation Product is NOT in BCNF.
R = ABCD, F = { A -> B, A -> C, A -> D }
• key(R) = A, all FDs have key on left hand side (LHS)
• Relation R is in BCNF
R = ABCD, F = { A -> BCD, D -> B, BC -> AD }
• key(R) = A, key(R) = BC, 
• D -> B, D and B are nontrivial (B  D)
• Relation R is NOT in BCNF


## Slide 26

Check
Let R(A,B,C,D) with 
F = { A → BC, C → D }. 
Which is correct? 
A) R is in BCNF 
B) A is not a key 
C) C is a superkey
D) R violates BCNF


## Slide 27

BCNF Decomposition Algorithm
• Cannot just arbitrarily break a relation schema.
• Start with the FD that violates BCNF
• Attributes are broken into two overlapping relation schema.
• One is all the attributes in the violating FD.
• Normalize(R):
Given relation R and all FDs.
Assume C is the set of all attributes in R
Find FD X->A , where A not in X and X+ ≠ C (not in BCNF)
If not found, 
then “R is in BCNF”. Return.
else 
let Y= X+ -X and Z = C - X
+
.
decompose R into R1(X +) and R2(X, Z).
Normalize(R1) , Normalize(R2)
X
+
Y X Z
Violating FD
R


## Slide 28

BCNF Decomposition – Example 
• Given relation R(SID,Name, PhoneNo, Town), 
• FD: SID -> Name, Town
• Violating FD as: SID+ = {SID, Name, Town}
• Use (SID -> Name, Town) to split. 
• After decomposition.
• SID+ = {SID, Name, Town} for R1
• SID and the rest to R2
Name, Town SID PhoneNo
SID+
Name SID PhoneNo Town
Fred 12345678 65551234 Clementi
Fred 12345678 65556543 Clementi
Joe 98765432 65552121 Ang mo kio
Joe 98765432 65551234 Ang mo kio
Name SID Town
Fred 12345678 Clementi
Joe 98765432 Ang mo kio
SID PhoneNo
123-45-6789 65551234
123-45-6789 65556543
987-65-4321 65552121
987-65-4321 65551234
R1
R2


## Slide 29

BCNF Decomposition – Example 2
• Given relation Person(name, SSN, age, hairColor, phoneNo), FDs:
• Iteration 1: check relation Person.
• SSN+ = {SSN, name, age, hairColor}. Bad FD.
• Decompose: P(SSN, name, age, hairColor) and Phone(SSN, phoneNo).
• Iteration 2: check relation P.
• age+ = age, hairColor. Bad FD.
• Decompose: People(SSN, name, age), Hair(age, hairColor), Phone(SSN, phoneNo)
SSN -> name, age
age -> hairColor
name, SSN, age, hairColor, phoneNo
name, SSN, age, hairColor SSNv, phoneNo
name, SSN, age age, hairColor


## Slide 30

Property of decomposition
• How do we know if a decomposition is correct or good?
• Lossless join
• Possible to reconstruct the original by a natural join on the decomposed schema 
• If R is decomposed into S and T, ensure S ∩ T ≠ ∅ and R = S ⨝ T
• Can be achieved with BCNF
• Dependency preservation
• Whether all the given FDs are satisfied after decomposition
• May not be achieved with BCNF


## Slide 31

Lossless Decomposition
• Lossless decomposition: able to restore instance of original relation from 
instances of smaller relations.
• decompose relation R into S and T, S ∩ T ≠ ∅ and R = S ⨝ T
Name Power Category
Bat Man rich Justice
Flash fast Justice
Bat Man rich Hero
Name Power
Bat Man rich
Flash fast
Name Category
Bat Man Justice
Flash Justice
Bat Man Hero
Power Category
Rich Justice
Fast Justice
Rich Hero
Name Category
Bat Man Justice
Flash Justice
Bat Man Hero
Lossy decomposition
Lossless decomposition
generate conflict tuples/ cannot recover some info


## Slide 32

Dependency preservation
• BCNF decomposition is lossless, but not always dependency preserving
• it is not guaranteed to preserve all FDs in the original relation
• Example: 
• R(StaffID, Name, Address, Hobby)
• FD: StaffID → Name, Address
• Decomposed into
• R1 = {StaffID, Name,Address} 
• R2 = {StaffID, Hobby} 
• The decomposition is dependency preserving
StaffID Name Address Hobby
StaffID Name Address StaffID Hobby


## Slide 33

Dependency preservation (cont.)
• Example: R(C,P,S,J,D,Q)
 FDs: C → {P,S,J,D,Q}, JP → C, SD → P, J → S 
• Decomposition into the following: R1(CJDQ), R2(JS), R3(SDP)
• It is a lossless join decomposition. 
• CPSJDQ = (SDP) ⋈ ( (JS) ⋈ (CJDQ))
• But not dependency preserving :
• JPC is not in one table (JP → C is not preserved)
• In this case, adding JPC to the collection of relations gives us a dependency preserving 
decomposition.
• JPC tuples stored only for checking FD! (Redundancy!)
CPSJDQ
CSJDQ SDP
CJDQ JS JPC


## Slide 34

Check
Decompose R(A,B,C) with 
F = { A → B, B → C } into R1(A,B) and R2(A,C). 
Which property holds?
A) Lossless and dependency-preserving 
B) Lossy but dependency-preserving 
C) Lossless but not dependency-preserving 
D) Lossy and not dependency-preserving


## Slide 35

Database refinement
• Storyline: bad DB design may introduce anomalies 
• Imperfect design -> redundancy.
• Redundancy -> decomposition.
• Normal forms are guidelines for what makes a database design “good” 
• Can formally specify them 
• Can transform schemas into normal forms
• Functional dependencies specify constraints between attributes in a schema 
• A more general kind of constraint than key constraints 
• 1NF requires all attributes to be atomic 
• BCNF uses functional dependencies to eliminate redundant data


## Slide 36

Database refinement (cont.)
• Functional dependency and closure
• BCNF based on FD.
• Given some FDs, 
• Option 1: infer all (hard)
• Option 2: closure. 
• Closure -> decomposition -> better design.
• Decomposition: not perfect; sometimes create more problems.
• Lossless-join property (BCNF ✓): recover instance of decomposed relation from 
instances of smaller relations
• Dependency-preservation property (BCNF ✗): enforce constraint on original 
relation by enforcing constraints on smaller relations.


## Slide 37

Performance considerations
A database designer may decide to use "bad" relations in a database because bad relations are 
often more efficient
Method 1: 
Method 2, two tables: 
Find the department name of employee: 
John Smith
Method 1: query from one table
Method 2: join the two tables to query: slower
Trade-off: Must consider efficiency vs. 
redundancy. 
SSN Name Bdate Dnum Dname Budget
1111 John Smith 1991-01-25 1 Research 50000
2222 Jane Doe 1993-04-01 1 Research 50000
3333 Harry Potter 1821-01-01 5 Magic 10000
SSN Name Bdate Dnum
1111 John Smith 1991-01-25 1
2222 Jane Doe 1993-04-01 1
3333 Harry Potter 1821-01-01 5
Dnum Dname Budget
1 Research 50000
5 Magic 10000


## Slide 38

Lab 4
SQL in Python
• mix SQL and Python, learn how to code SQL directly in Python
• Sqlite3
• Colab/Jupyter notebook


## Slide 39

Tutorial
• Questions uploaded on xsite
• Please try out those questions on your own. 
• We will go through on how to answer those questions in Tutorial session scheduled at
next week, Tuesday lab time online (12pm).


---

# Lecture 5

*Source: INF2003_AY2425_T1_Lec05*


## Slide 1

INF2003:
Database systems
ER Diagram
AY2025/26 Trimester 1
Dr. Tong Rong


## Slide 2

From last week
• Storyline:
• Imperfect design -> redundancy.
• Redundancy -> decomposition.
• Decomposition depends on normal form: BCNF
• Check if comply BCNF based on FD.
• Given some FDs, 
• Option 1: infer all using Axioms(hard)
• Option 2: closure. 
• Closure, BCNF -> decomposition -> better design.
• Decomposition: not perfect, may not preserves all dependency


## Slide 3

ER diagram


## Slide 4

ER diagram: Outline
• Intro: the main characteristics of entity relationship components
• ER model:
• Basic notation
• Entity
• Attribute
• Relationship and constraints
• Weak entities, subclass
• Convert ER to Relational Schema
• Entities
• Attributes
• Relationship 
• Weak entities, subclass
• Examples


## Slide 5

Stages of Database Design
S1 • Requirement Analysis
S2 • Conceptual Database Design
S3 • Logical Database Design
S4 • Refine the Schemas
S5 • Physical Database Design
S6 • Application and Security Design
ER model is relevant to the first 
three stages of database 
design.


## Slide 6

ER Model
• Full name: entity-relationship model.
• Peter Chen proposed ER Diagram in 1970s
• ER diagram is a graphical notation for ER data model.
• Pictures speak a thousand words, so much easier to debug.
• Simple and intuitive, but also powerful.
• A top-down approach to database design
• Conveys knowledge at a high-level (conceptual level)
• Natively compatible with the relational data model.


## Slide 7

ER diagram
• An ER diagram consists of:
• a collection of entity set definitions
• a collection of relationship
set definitions
• attributes associated with entity and 
relationship sets
• connections between entity and 
relationship 
https://www.guru99.com/images/1/100518_0621_ERDiagramTu2.png


## Slide 8

ER diagram – notation variations
• There are many variations of ERD 
notations
• You can use any of them in project, 
just make sure they are consistent
• https://hevodata.com/learn/er-modeltools/
link


## Slide 9

ER diagram: symbols used in this lecture
Notation
• Entity: rectangle
• lines to its attributes and relationships
• underline the primary key
• Relationship: diamond
• Attribute: oval/ellipse
• Double ellipse: multivalued attribute
• Dashed ellipse: derived attribute


## Slide 10

ER Model – Entity (E) 
• Entity: a unique object in real-world.
• Each entity has a set of attributes: id, name
• Each attribute has a data type: id: 4 digits number
• A subset of the attributes can uniquely identify the entity. id: 1001
• Entity is similar to object in OOP: entity is static, no methods!
• Entity set: a collection of the entities, with the same properties.
• Same attributes, same data type, same order, same key attributes
• Values are different, at least for the key attributes.
• Possible to have several entity sets with the same properties. 
e.g., {
 (1001, ‘John Doe’)
 (1002, ‘Arya Stark’)
 }
Entity
Attribute
id Student name


## Slide 11

ER Model – Attribute
An attribute describes the property of an entity, four types:
• Key attribute: keys are indicated in ER diagrams by underlining
• ID
• Composite attribute: a combination of attributes
• Address
• Multivalued attribute: An attribute that can hold multiple values
• Phone (can have multiple phone numbers)
• Derived attribute: whose value is dynamic and derived from another attribute
• Age, it can be derived from DOB
Customer Address
Phone
DOB
Name
ID
State
Country
Age


## Slide 12

ER Model – Relationship (R) 
• Relationship: association among two or more entities.
• Uniquely identified by the keys of its entities.
• E.g., Lecture (20221001) teach Course (ICT2103)
• Relationships may have attributes as well.
• every tuple of entities connected by the relationship is 
associated with a value for each attribute.
• E.g., Lecture (20221001) teach Course (ICT2103) since 
2022
Relationship
Lecture
Teach
Course
Since


## Slide 13

Relationship: Participation Constraints
• Specify whether the participation of an entity in a relationship is compulsory
• Total Participation (indicated by bold/double line)
• Each entity in the entity set is involved in at least one relationship, i.e. the number of
relationship in every entity is involved is greater than 0.
• E.g., every booking is required to have a customer.
 Participation of Booking in this relation is total
• Partial participation (indicated by single line)
• Each entity in entity set may or may not occur in at least one relationship
• E.g., not every customer needs to have made a booking
 Participation of Customer is partial
Customer Makes Booking
Partial
0 or more
Total
1 or more


## Slide 14

Relationship cardinality
• Number of associated entities on each side of relationship
• Can be classified as one-to-one, many-to-one, one-to-many, many-to-many
• a directed line (→), signifying “one,” 
• or an undirected line (—), signifying “many,”


## Slide 15

Degree of relationship
Teacher teaches Module
Module Is prerequisite for
Program
Teacher teaches Module
unary relationship
One entity set
binary relationship
Relationship 
between two entity
ternary relationship: 
Relationship of three 
entity sets
Good practice:
Avoid Ternary Relationship, 
Complex logics
• Number of entities involved in relationship


## Slide 16

Avoid Ternary Relationship
Program
Teacher teaches Module
Program
Teacher teaches Module
Belongs


## Slide 17

Weak Entities
• Exist only because of association with strong entities
• If the adult cancels the booking, all dependents 
booking needs to be canceled.
• Dependents is an example of a weak entity set. 
• The attribute name does not identify a dependent 
uniquely.
Customer
BookingID
Time
Name DOB Gender
ID
Dependent
Travel
With
Name
Age
Travel 
with
Makes Booking


## Slide 18

Subclasses and Inheritance
• Subclasses represent a more specific type of an existing 
entity, inheriting its attributes and relationships, while 
also possessing unique characteristics.
• One entity type might be a subtype of another
• Declare A ISA B: every A entity is also considered to be a 
B entity. 
• Overlap constraint, more for derived class
• Joe can be both an HourlyEmps and a 
ContractEmps entity? 
• Disallowed. No overlap. 
• Covering constraint: more for parent class
• Every Employees be an HourlyEmps or a 
ContractEmps entity? 
• Yes
parent class
ContractEmps
name
ssn
Employees
lot
hourly_wages
ISA
HourlyEmps
contractid
hours_worked
derived class


## Slide 19

Design Issues 
• Use of entity sets vs. attributes 
• Should an "object" be represented by an attribute or entity? 
• Entity should be important in its own.
• Is an "object" a strong or weak entity? (usually strong)
• Are there subclasses/superclasses within the entities?
• Use of entity sets vs. relationship sets 
• Is a "concept" best expressed as an entity or relationship?
• Possible guideline: use a relationship to describe an action that occurs between entities 
• Placement of relationship attributes
• Binary versus n-ary relationship sets
• Use n-way relationship or several 2-way relationships?
• Non-binary (n-ary, for n > 2) relationship is complicated
• Sometimes a n-ary relationship set shows more clearly that several entities participate in a 
single relationship.


## Slide 20

Design Decision: example
• Concept is not hard, but it can be challenging for real applications. 
• Modeling as single relationship makes it unique; what if not appropriate?
• Problem: a person can only buy a specific product once (in one day)?
Product Purchased
name category
price Person
date name
• Better design: multiple relationships to capture the purchases per product & person pair.
Product
name category
price Person
date name
Purchase
PID# quantity
ProductOf BuyerOf


## Slide 21

From ER Diagrams to Relational Schema
• For ER diagram to be useful, need to convert it into an implementation schema
• Convert entity and relationship set into relations or tables
• correspondences between relational and ER data models:
• not every diamond becomes a table: some data can be "absorbed" into another table. 
• many-to-many relationships may result in an extra table.
attribute(ER) ≅ attribute(Rel), entity(ER) ≅ tuple(Rel)
entity set(ER) ≅ relation(Rel), relationship(ER) ≅ relation(Rel)
• Components of conversion process
• Specify schema of the relation itself 
• Specify primary key on the relation 
• Specify any foreign key references to other relations


## Slide 22

Entity set to tables
• Each tuple is one entity in the entity set.
• Each tuple is composed of the entity’s attributes.
• The same primary key for both entity set and table.
name price category
product category
price
name
CREATE TABLE product(
 name CHAR(50) PRIMARY KEY,
price DOUBLE,
category VARCHAR(30)
)
product


## Slide 23

Composite attribute
• Composite attributes are mapped by concatenation or flattening.
number, street, suburb, pcode


## Slide 24

Multivalued attribute
• Multivalued attributes are mapped by a new table linking values to their entity
Person(12345, John, 12-feb-1990, [red,blue])
Person(54321, Jane, 25-dec-1990, 
[green,purple])
Person(12345, John, 12-feb-1990)
Person(54321, Jane, 25-dec-1990)
FavColour(12345, red)
FavColour(12345, blue)
FavColour(54321, green)
FavColour(54321, purple)


## Slide 25

Relationship Set to Tables
In translating a relationship set to a table, attributes of the relation must include:
• Keys for all the participating entity sets, as foreign keys.
• All descriptive attributes.
name
lot
dname
did budget
since
Managers Manages Departments
ssn
CREATE TABLE Manages(
ssn CHAR(11),
 did INTEGER,
 since DATE,
 PRIMARY KEY (ssn, did),
 FOREIGN KEY (ssn) REFERENCES Managers,
 FOREIGN KEY (did) REFERENCES Departments)
ssn did since
did ssn since
1 1 05/09/2023
2 2 04/03/2025
3 2 02/06/2024
3 3 06/03/2025
Manages


## Slide 26

Relationship Set with Constraint 
• constraint on Manages: each department has at most 1 manager.
• Use only did as the key for Manages, instead of both did and ssn
dname
did budget
since
lot
name
ssn
Managers Manages Departments
ssn name lot
1 Jogn 2
2 Eric 2
3 Lydia 1
Managers
did dname budget
1 Finance 10k
2 HR 5k
3 Transport 20k
Departments
Manages
Only 1 entry per did.
CREATE TABLE Manages (
ssn CHAR(11),
did INTEGER,
since DATE,
PRIMARY KEY (did),
FOREIGN KEY (ssn) REFERENCES Managers,
FOREIGN KEY (did) REFERENCES Departments)
Can further improve?
did ssn since
1 1 05/09/2023
2 2 04/03/2025
3 2 02/06/2024
3 3 06/03/2025


## Slide 27

Relationship Set with Constraint (cont.)
• Merge the relationship with the constrained entity to form one relation/table.
• Since each department has a unique manager, we could instead combine Manages and 
Departments -> save space for key duplications.
dname
did budget
since
lot
name
ssn
Managers Manages Departments
did dname budget ssn since
1 Finance 10k 1 05/09/2013
2 HR 5k 2 04/03/2015
3 Transport 20k 2 02/06/2014
CREATE TABLE DeptMgr(
did INTEGER,
dname CHAR(20),
budget REAL,
ssn CHAR(11),
since DATE,
PRIMARY KEY (did),
FOREIGN KEY (ssn) REFERENCES Managers)


## Slide 28

Check
A many-to-many (M:N) relationship between two entities, C and D, is resolved in a relational database 
schema by which of the following? 
A) Using a single foreign key to link entity C and entity D.
B) Creating a table with composite primary keys of C and D.
C) Adding a foreign key from entity C to entity D.
D) Creating a single table that combines all attributes of C and D.


## Slide 29

Weak Entity Set 
• Weak entity set and owner entity set -> many-to-1 relationship.
• Week entity identified by 1) owner key + 2) entity key.
• Weak entity set: total participation in identifying relationship set.
• Weak entity set + identifying relationship set -> one table.
• Owner entity deleted -> what shall we do?
• Must delete all associated weak entities.
CREATE TABLE Transaction (
TransNum INTEGER,
AccNum INTEGER NOT NULL,
Date date,
Amount FLOAT,
PRIMARY KEY (TransNum, AccNum),
FOREIGN KEY (AccNum) REFERENCES Account,
ON DELETE CASCADE)
TransNum AccNum Date Amount


## Slide 30

Subclass
Three approaches to mapping subclasses to tables:
• ER style
• object-oriented
• each entity becomes a separate table,
• inheriting all attributes from all superclasses
• single table with nulls
• whole class hierarchy becomes one table,
• containing all attributes of all subclasses 
(NULL, if unused)
ContractEmps
name
ssn
Employees
lot
hourly_wages
ISA
HourlyEmps
contractid
hours_worked
derived class
parent class


## Slide 31

Subclass – ER style
• Each entity becomes a separate table
• Subclass table + foreign key to superclass table


## Slide 32

Subclass – object-oriented
• Each entity becomes a separate table
• Inheriting all attributes from super class


## Slide 33

Subclass – single table with NULLs
• Whole class hierarchy becomes one table,
• Containing all attributes of all subclasses (NULL, if unused)


## Slide 34

Example
In a university, there are professors (identified by NRIC) and courses (identified by courseid) , the following 
situations concerns the Teaches relationship. Draw ER and convert it to relation schemas.
• Q1: professors can teach the same course in several semesters, and each offering must be recorded.
Professor (NRIC: varchar(9))
Course (courseid: varchar(10))
Semester (semesterid: varchar(10))
Teaches (courseid: varchar(10), NRIC: varchar(9),
 semesterid: varchar(10));
• Q2: Professors can teach the same course in several semesters, and only the most recent such offering 
needs to be recorded. 
Professor (NRIC: varchar(9)); 
Course (courseid: varchar(10)); 
Teaches (courseid: varchar(10), NRIC: varchar(9), 
semesterid: varchar(10));


## Slide 35

ER Diagram Summary
• ER design:
• An important step before jumping in to develop the database schema.
• Different solutions to a problem. 
• Analyze the application to find a suitable or better one. 
• Most importantly, ask questions (clarify with customers).
• Very likely it won’t the 100% clear in the beginning.
• Hard to simulate the situations in our modules.
• May practice during your project work.
• One step closer towards a good database design.
• Requirements -> conceptual design (ER).
• ER -> logical design (relation schema).
• Logical design -> further refinement.
• Functional dependencies and database normalization
https://www.techradar247.com/


## Slide 36

Tutorial
• Questions uploaded on xsite
• Please try out those questions on your own. 
• We will go through on how to answer those questions in Tutorial session scheduled at: 
 12 noon Sep 30, 2025.
 No Labs in week 5 and 6.


## Slide 37

Quiz 1
Room Details Room Capacity Student ID
E2-05-05 132 2202097 – 2400737
E2-06-02 80 2400740 - 2400991
E2-06-18 118 2401005 - 2401464
E2-06-19 118 2401465 - 2401753
E2-07-05-SR263 70 2401755 - 2401995
E2-07-13 238 2401996 - 2402815
E2-07-14 144 2402817 - 2403480
• Time: Oct 8, (Wednesday), 6:10 PM-7:00 PM, 50-min quiz. Please be seated by 6:00PM.
• Format: Online quiz in LMS with lockdown browser; In-person 
• Questions: 21 MCQ (single or multiple choice), 1 fill in the blank, 2 short questions
• Special arrangement: for students with special needs, please email me before hand;
• Absence: Only RO approved leave request will be accepted
• Venue: please find your room in the table below


---

# Lecture 6

*Source: INF2003_AY2526_T1_Lec06*


## Slide 1

Zhang Wei
SIT
Oct. 21, 2025
INF2003: 
Database Systems
Indexing
AY25/26 Trimester 1


## Slide 2

About Me
▪ Email: wei.zhang@singaporetech.edu.sg
▪ Google Homepage: https://sites.google.com/view/sit-zhang-wei/
▪ PhD in Computer Science from NTU. 
▪ Research: applied AI + energy efficiency.
▪ Interested in applied learning in my projects, welcome (but after this tri).
▪ Teaching database since 2019.
▪ Partly because I was involved in database tasks in A*STAR during 2017-19.
▪ Content was customized to diff. programmes, e.g., more in-depth for CS / SE. 
▪ Now harmonized as INF2003; difficulty level lower. 
▪ Looked after our Computing Science programme (2022-25). 
▪ One of SIT’s most popular programmes.


## Slide 3

2
nd Half Topics
W8
• Indexing (mainly centralized)
W9
• Transactions and Concurrency 
W10
• NoSQL
W11
• Blockchain
W12
• Data Warehouse


## Slide 4

Files and File Organization
▪ 1 database, >= 1 tables.
▪ 1 table, >= 1 tuples, stored in data files.
▪ 1 file, >= data pages (a chunk of data file). 
▪ Given a query requesting for certain data, DBMS figures out how to 
enable efficient access to the desired pages that contain the data.
▪ File organizations:
▪ Heap files (random order): scanning all records.
▪ Sorted files: good for order-sensitive data retrieval and range search. 
▪ Indexes: additional data structures to optimize certain retrievals.
▪ Advantages (for a good file organization) – Fast.
▪ Speed up search.
▪ Fast updates.
Data Files
Page 
1
Page 
2
Page 
n
. . .


## Slide 5

Discussion
A. SELECT * FROM Students;
B. SELECT * FROM Students WHERE sid = 2001234;
C. SELECT * FROM Students WHERE year >= 2013 AND year <= 2015;
▪ Which of the above statement(s) can be faster with indexing? Why?
▪ Create many indexes?
CREATE INDEX index_name
ON table_name (col_name)


## Slide 6

Index Data Structure - Hash
▪ Index is a collection of buckets.
▪ Bucket: primary page plus zero or more overflow pages.
▪ Buckets contain data entries.
▪ Hashing function h (same for all records):
▪ h(r) = bucket in which (data entry for) record r belongs.
▪ h looks at the search key fields of r.
First Name Surname Origin
Arya Stark Winterfell
Sansa Stark Winterfell
Jaime Lannister Casterly Rock
Tyrion Lannister Casterly Rock
Robb Stark Winterfell
Bran Stark Winterfell
Aegon Targaryen Tower of Joy
Arya Stark Winterfell
Sansa Stark Winterfell
Jaime Lannister Casterly Rock
Tyrion Lannister Casterly Rock
h(r) = Surname;
Each house a bucket.
Each bucket ≥ 1 pages.
Aegon Targaryen Tower of Joy
Robb Stark Winterfell
Bran Stark Winterfell


## Slide 7

Index Data Structure - Hash
▪ Q1. Possible two records in the same bucket?
▪ Q2. Possible one record in different buckets?
▪ Q3. Suitable for equality search or range search?


## Slide 8

Index Data Structure – Tree
▪ Hash – equality search.
▪ Tree – both equality and range search.
▪ Hash – flat structure; Tree – hierarchy. 
▪ Both direct a search to a suitable page.
▪ Many types of trees. 
▪ B+ tree is the most popular one, widely supported.
Tree Index Entries
Data Entries
Weirwood Tree


## Slide 9

B+ Tree
▪ Basic elements: root, internal nodes (non-leaf), and leaves.
▪ High fanout, e.g., typically on the order of 100 or more.
▪ Fanout: number of pointers to child nodes in a node.
▪ Why high fanout?
▪ Different implementations exist.
▪ Minor implementation differences.
▪ But same philosophy. 
▪ Some important rules:
▪ All data is in the leaf nodes.
▪ Leaves all in the same level.
▪ Tree balance is important. Why?
▪ Leaves linked together.
▪ Each leaf node, k keys, and k+1 pointers.
▪ Minimum 50% occupancy. Root is an exception.


## Slide 10

B+ Tree: Search
▪ Search: just a series of comparison operations in O(log(n)) time.
▪ Example.
▪ Search 8.
▪ Search [8, 24].
root
2 3 5 7 8 14 16 20 24 27 29 33 34 38 39
5 14 27 33
20


## Slide 11

B+ Tree: Insert
▪ Insert: locate -> insert -> update.
▪ Insert the value into the leaf. Enough space?
▪ Ture: done.
▪ False: split the leaf into two new nodes.
• Redistribute evenly. 
• Add parent node new key, i.e., duplicate the min value of the 2nd new node.
▪ Recursive execution. Level by level until no split is needed.
▪ Tree can grow, wider, deeper. Do not violate the min occupancy.
▪ Example: insert 8.
▪ Locate: which node? Insert: enough space? 
2 3 5 7 14 16 20 24 27 29 33 34 38 39
14 20 27 33 root


## Slide 12

B+ Tree: Insert
14 16 20 24 27 29 33 34 38 39
14 20 27 33 root
2 3 5 7 8
1) Split leaf -> insert 5 to parent.
14 16 20 24 27 29 33 34 38 39
20 27 33
2 3 5 7 8
2) Split parent. Done? 5 14


## Slide 13

B+ Tree: Insert
14 16 20 24 27 29 33 34 38 39
27 33
2 3 5 7 8
3) New root. 
Tree grows.
Wider.
Deeper.
Be patient.
5 14
20 root


## Slide 14

B+ Tree: Delete
▪ Locate -> remove -> low occupancy? 
▪ True: done.
▪ False: try borrowing one from the nearest siblings; if cannot, merge.
▪ Recursive. Level by level (upwards) until no changes needed. Be 
patient.
▪ Tree can be smaller.
14 16 20 24 27 29 33 34 38 39
27 33
2 3 5 7 8
1) Delete 8. 
Will the tree be smaller?
5 14
20 root


## Slide 15

B+ Tree: Delete
14 16 20 24 27 29 33 34 38 39
27 33
2 3 5 7
2) Delete 29. 
Will the tree be smaller?
5 14
20 root
14 16 20 24 27 33 34 38 39
27 34
2 3 5 7
5 14
Try to borrow if possible. 20 root
Less structure changes.


## Slide 16

B+ Tree: Delete
14 16 20 24 27 33 34 38 39
27 34
2 3 5 7
5 14
3) Delete 7. 20 root
Will the tree be smaller?
2 3 5 14 16 20 24 27 33 34 38 39
Tree becomes smaller. 14 20 27 34 root
Be patient until root.
A dynamic data structure that adjusts efficiently under inserts and deletes.


---

# Lecture 7

*Source: INF2003_AY2526_T1_Lec07*


## Slide 1

Zhang Wei
SIT
Oct. 28, 2025
INF2003: 
Database Systems
Transaction
AY25/26 Trimester 1


## Slide 2

2
nd Half Topics
W8
• Indexing (mainly centralized)
W9
• Transactions and Concurrency 
W10
• NoSQL
W11
• Blockchain
W12
• Data Warehouse


## Slide 3

Transaction
• Definition: a program with some reads and writes (Abbreviation: TXN). 
• In the world of SQL, a TXN is a series of SELECT, UPDATE, and INSERT.
• Transaction example: transfer 100 dollars from me to Batman.
• Read balance of my account: bal_wei.
• Write new balance to my account: bal_wei := bal_wei – 100.
• Read balance of Batman’s account : bal_wayne.
• Write new balance to Batman: bal_wayne := bal_wayne + 100.
• Transaction so simple? What would be the problem?
• Key issue: concurrency. 
• One database used by several users or threads.
• Each user can start a transaction freely. 
• Different transactions access the same data. 
• Results depend on the execution order or the operations.
• Even system throughput varies.


## Slide 4

Concurrency Example
• TXN-1: transfer 100 dollars from me to Batman.
• TXN-2: pay 3% interest for accounts.
• Read balance of my account: bal_wei.
• Write to my account: bal_wei := bal_wei * 1.03.
• Read balance of Batman’s account: bal_wayne.
• Write to Batman’s account: bal_wayne := bal_wayne * 1.03.
• Suppose TXN-1 was executed first and then TXN-2.
• My account, e.g., initially with 200: 200 -> 100 -> 103.
• Batman, e.g., also with 200: 200 -> 300 -> 309.
• Reverse the order: TXN-2 -> TXN-1.
• My account: 200 -> 206 -> 106. (3 dollars more)
• Batman: 200 -> 206 -> 306. (3 dollars less)
• Not perfect, but quite lucky, as the total amounts are the same, 412.
• With interleaving, could be worse.


## Slide 5

Interleaving
• When we allow the operations to interleave arbitrarily. 
• Interleaving 1: (suppose again me 200 and Batman 200 initially)
• TNX-1: 1) W –= 100; 3) B += 100.
• TNX-2: 2) W *= 1.03; 4) B *= 1.03. 
• Results: me 103; Batman 309; sum 412. 
• Interleaving 2: 
• TNX-1: 1) W –= 100; 4) B += 100.
• TNX-2: 2) W *= 1.03; 3) B *= 1.03. 
• Results: me 103; Batman 306; sum 409.
• Interleaving can be bad, or wrong. 
• But also a key tool to improve the system performance.
• Group the same read from different threads together.
• The same read loads data once from disk to memory and reuses a lot.
Cache Matching Algorithm


## Slide 6

Scheduling Transactions
• Serial schedule: does not interleave the actions of transactions.
• Fact: highest level of safety, but sometimes poor efficiency.
• Equivalent schedule: two schedules with the same output.
• Serializable schedule: equivalent to some serial ones’ outputs.
(Serial) 200 200
Read(W, t)
t := t+100
Write(W, t) 300
Read(B, t)
t := t–100
Write(B, t) 100
Read(W, s)
s:= s*1.03
Write(W, s) 309
Read(B, s)
s := s*1.03
Write(B, s) 103
(Serializable) 200 200
Read(W, t)
t := t+100
Write(W, t) 300
Read(W, s)
s:= s*1.03
Write(W, s) 309
Read(B, t)
t := t-100
Write(B, t) 100
Read(B, s)
s := s*1.03
Write(B, s) 103


## Slide 7

Transaction: ACID
• Database becomes inconsistent when transactions are wrongly scheduled.
• 4 transaction properties - ACID. 
• A: atomicity. 
• C: consistency.
• I: isolation.
• D: durability.
• Atomicity: all updates must happen or 
not at all.
• Conceptually, one transaction, one unit.
• e.g., money transfer as 1 transaction.
• Op-1: withdrawal from the first account.
• Op-2: deposit on the second. 
• Op-2 failed, don’t commit Op-1. 
• Otherwise, that money would disappear!
• Do all or do nothing.


## Slide 8

ACID: Consistency and Isolation 
• Consistency before transaction -> consistency after transaction.
• Or, each transaction must preserve the consistency of the database.
• Programmer’s job to preserve.
• DBMS’s job to execute atomically.
• Possible to be inconsistent in the middle of one transaction.
• Consistency guarantees the correctness of transaction? 
• No. Responsibility of application-level code.
• You may mistakenly write 3% interest rate as 30%. Nothing to do with C.
• Isolation: concurrently executed as if isolated.
• No result changes due to concurrency.
• e.g., A teller looking up a balance.
• Must be isolated from a concurrent withdrawal trans. 
• Only when withdrawal commits,
• -> the teller can see the new balance.


## Slide 9

ACID: Durability
• Durability: once done, holds true even system crashes.
• Record where we are in the beginning.
• In case cannot compete, go back to the original state. 
• Transaction log: records the transaction details.
• Include any changes to the database.
• Include when transactions complete and how.
• Write before commit. If crashes, no opportunity to record.
• Chained together by trans id. Easy to restore to any point.
• Log stored on disk, not memory. Why?
• ACID in money transfer example.
• Atomicity: cannot deduct money from my account without giving it to Batman.
• Consistency: money comes from somewhere, isn’t lost or gained.
• Isolation: invisible to the public until fully complete.
• Durability: the money does not flow back to my account.
Stay down. Final warning.
I could do this all day!


## Slide 10

Transactions in SQL
• COMMIT: end the current trans and make pending changes permanently. 
• ROLLBACK: discard all pending changes.
• SAVEPOINT: a marker, which divides a transaction into pieces. 
• ROLLBACK TO SAVEPOINT: any errors, rollback to the specified SAVEPOINT.
• Keep the changes until the SAVEPOINT and discard the changes after it.
• We code line by line and find an error after the 2nd update.
• We execute rollback immediately. Then commit.
• What is the grade of student 200123?
• Do we have student 200999?
• Trans ends where? 
• Either COMMIT or ROLLBACK.
• Or DDL, or GRANT, or REVOKE.
• Naturally exit.
UPDATE Students SET grade=“B” WHERE sid=200123;
SAVEPOINT sp1234;
INSERT INTO Students VALUES(200999, “Jon”, “A”);
UPDATE Students SET grade=“A+”;
ROLLBACK TO SAVEPOINT sp1234;
COMMIT;


## Slide 11

Recovery
• Transaction offers one layer of protection but cannot protect all.
• Potential failures: system crash; power failure; disk crash; user
mistake, cyber-attack, earthquake, etc.
• Singapore becomes the datacenter hub in ASEAN w/ system, infra, and talent.
• Good practice: prevention is the best medicine. 
• Robust (Linux for server), security (local network), UPS, etc.
• Relatively easy case: physical media is still working.
• Create some checkpoints to restart, redo, etc.
• Details beyond the scope of this module.
• Physical media damage: more serious. 
• Data damaged. Transaction log damaged. 
• In practice, backup the database in a secondary device, e.g., a tape.
• Try to backup the transaction log as well, in a secondary device. 
• e.g., 1% failure rate for 1 device; 0.01% for 2 devices.


## Slide 12

Concurrency Control: Lock
• For atomicity, what are we afraid of?
• Not serial. Interleaving. 
• A brute-force solution: lock.
• When I am using the data, you cannot use, and vice verse.
• Prevent another transaction from reading inconsistent data.
• Force the system to be non-concurrent.
• Lock manager: responsible for assigning and policing the locks.
• Lock granularity.
• Database-level lock: lock the entire database.
• Table-level lock: lock the entire table.
• Page-level lock: lock the entire disk page.
• The first two unsuitable for multi-user. Page-level much more popular. 
• Row-level lock: each row accessed by one trans and locked to the others. 
• Field-level lock: can access the same row, as long as for different columns.
• The last two, often impractical with a lot of locks.


## Slide 13

Lock and Optimistic Methods
• Deadlock: you wait for me to release, and I wait for you. Forever.
• Prevent (double-check the code) and detect (timeout).
• Do we really need locks? Underdog for speed?
• All read operations without any writes -> no problem.
• If there are writes, many applications do not write the same data.
• Even write the same data, often not at the same time.
• Go ahead to execute, assuming/expecting bad things won’t happen.
• Anything bad happens, restore to the original state. 
• A popular optimistic method: 3-phase method (no lock).
• Read: trans keeps a private data copy -> update in a private and 
temporary file.
• Validate: don’t affect integrity and consistency -> if pass, write; 
cannot pass, restart.
• Write: everything okay, write (commit the changes) permanently.


## Slide 14

Summary
• Transaction is a core concept in database.
• More important for large-scale and multi-user database. 
• Transactions improperly executed -> errors and data inconsistency.
• Understand the examples.
• Interleaving can be troublesome. 
• 4 transaction properties: ACID. 
• Atomicity, consistency, isolation, and durability.
• Simple way to avoid troubles: lock. 
• Drawbacks: slow and overhead -> try first w/t lock (3-phase method).
• Transaction control language (TCL) in SQL: COMMIT, ROLLBACK, etc.
• Database can crash. Prevent (the best defense is a good offense). 
• Database issues is not limited to SQL. Be aware of the real-world.
• May have to scale up the database. Remain centralized? Go distributed?


---

# Lecture 8

*Source: INF2003_AY2526_T1_Lec08*


## Slide 1

SIT Restricted
Zhang Wei
SIT
Nov. 4, 2025
INF2003: 
Database Systems
NoSQL
AY25/26 Trimester 1


## Slide 2

SIT Restricted
Relational DB: Advantages and Gap
• Benefits of relational database.
• Consistency, concurrency, recovery.
• Mathematically background -> solid and rigorous.
• SQL for management and communication. 
• Mature ecosystem with tools and services.
• Fact: Centralized. You may have noticed MySQL database is in one disk.
• Good: fast local join, easy management, etc. 
• Bad: scalability/partition, robustness/replication, task dispatch, etc.
• Reality: big data, geo-distribution, diversity, etc.


## Slide 3

SIT Restricted
NoSQL
• Simplify data models to improve the generalizability. 
• Deal with diverse data, diverse locations, diverse systems, etc.
• Name: Non-SQL? Neo SQL? No SQL? Not Only SQL? 
• Main categories:
• Key-value database, e.g., Redis, Memcached, and SimpleDB.
• Document database, e.g., MongonDB, CouchDB, and OrientDB.
• Columnar database, e.g., Cassandra and Hbase.
• Graph database, e.g., Neo4j.
• Key-value database: simplest NoSQL.
• key-value store: a simple hash table.
• All the access to the database are via keys.
• Operations: e.g., get key’s value, put value to a key, and delete key.
• No complex query filters. Join outside the database, like in Python. 
• Efficient (for its simplicity). Distribute everywhere.


## Slide 4

SIT Restricted
Key-Value Database: Redis
• Redis: (possibly) the most popular key-value database. https://redis.io/
• C++ based (potentially fast). Open-source.
• Rich data structures.
• e.g., strings, hashes, lists, sets, sorted sets, bitmaps.
• In-memory operations: faster than disks.
• Able to be customized, e.g., for speed or for reliability. 
• Data persistency: save the updated database in a disk periodically.
• Bindings to many languages.
• e.g., Python, Java, C, C#, C++, MATLAB, R, VB, Erlang, Perl, and PHP.
• A wide range of operations:
• GET: get the value of a key in O(1).
• SET: set key to hold a value in O(1).
• DEL: delete a key in O(1).
• Many others: https://redis.io/commands
redis> SET key2003 “DBSys”
“OK”
redis> GET key2003 
“DBSys” 
redis> DEL key2003 key1234 
(integer) 1
redis> GET key2003
(nil)


## Slide 5

SIT Restricted
Document Database
• What documents? 
• Not really about the docs we are familiar with.
• More like the heterogenous metadata of some items.
• How to put different things together?
• Quite common, e.g., items in Lazada/Shopee. 
• Not suitable to store in relational database.
Calligraphy Calligrapher Year Chinese
Lanting Xu Wang Xizhi 353CE 兰亭集序
Name Brand Year Memory 
Jetson Nano Nvidia 2020 SDRAM


## Slide 6

SIT Restricted
Document Database
• No relation schema.
• Store data in JSON, BSON, or XML documents.
• Documents can be nested, can be indexed.
• Similar format to many applications. Name a few?
• Potentially much less translation and fast.
• For SQL, more data assembling and disassembling.
• Flexibility with changeable data structures.
• For SQL databases, would be tough to pass admin control. 
{
 ItmeType: “Book”,
 ItemName: “Lanting Xu”,
 Author: “Wang Xizhi”,
 Year: “335”,
 Chinese: “兰亭集序”
}
{
 ItmeType: “Computer”,
 ItemName: “Jetson Nano”,
 Brand: “Nvidia”,
 Year: “2020”,
 Memory: “SDRAM”
}


## Slide 7

SIT Restricted
SQL -> NoSQL Migration
• Do you really want to migrate?
• Possible reasons:
• Business scale-up. May not need SQL->NoSQL.
• Application change. Diff. philosophies. Be careful.
• Scheme 1: 1-1 mapping. (most popular)
• 1 table in SQL -> 1 collection in NoSQL (like MongoDB).
• Tools available, e.g., AWS DMS, Python w/ related libs, SQL Server export.
• Sample code available in Google/GitHub.
• Scheme 2: Denormalization.
• Reverse the decomposition process -> small to big. 
• Moderate modification, moderate benefit.
• Scheme 3: forget migration and design from the beginning. 
• Suitable for dramatic application changes.
• Significant workload, but good for future operation and maintenance.


## Slide 8

SIT Restricted
MongoDB
• Founded in 2007, A document-oriented, NoSQL database.
• Written in C++.
• Hash-based, schema-less database.
• Key is a basic data type but, stored as strings.
• Document identifiers (_id, system reserved) will be created for each doc. 
• Can insert the “same” data multiple times. Why?
• Supports APIs (drivers) in many languages.
• e.g., JS, Python, Ruby, Perl, Java, JavaScala, C#, C++, Haskell, and Erlang. 
• Functionality:
• Secondary indexes. Query language via an API. 
• Atomic writes and fully-consistent reads.
• Master-slave replication with automated failover (replica sets).
• Built-in horizontal scaling via automated range-based partitioning of data.
• We may not be aware of. 
• No joins (imagine ERD w/t links, shall write scripts to do so if needed).


## Slide 9

SIT Restricted
MongoDB
• Simple queries (you will see a few later).
• Applicable to most web applications.
• Easy and fast integration of data.
• But, not suitable for heavy and complex transactions systems.
Relational DBMS MongoDB
Database Database 
Table, View Collection 
Row Document (BSON) 
Column Field 
Index Index 
Join Embedded Document 
Foreign Key Reference 
Partition Shard (Distributing Data)


## Slide 10

SIT Restricted
MongoDB - CRUD
• Create: db.collection_name.insert(<document>).
• db.ppl.insert({{_id: 11, type: “Avengers”, name: “Spider Man” })
• db.ppl.insert({type: “Transformers”, cat: “Autobot”, name: “Optimus Prime”}) 
• Omit the _id field to have MongoDB generate a unique key.
• Read: db.collection_name.find( <query>, <projection> ) or findOne.
• Find all: db.ppl.find(), no criteria specified. 
• db.ppl.find({type: {“Avengers”, “Transformers”}).
• Update: db.collection_name.update( <query>, <update> )
• db.ppl.update({type: “Avengers”, {$set: {type: “The Avengers”}})
• Delete: db.collection_name.remove(<query>, <justone>) 
• Delete all records from a collection or matching a criterion.
• How to delete all?
• <justone> - specifies to delete only 1 record matching the criterion.
• Example: db.ppl.remove(type: /^s/ } ) - remove all starting with s.
• https://docs.mongodb.com/manual/reference/method/js-collection/


## Slide 11

SIT Restricted
Columnar Database 
• Database is a collection of key/value pairs. Sounds familiar?
• Key 3 parts: row key, column key, and time-stamp.
• Why include time-stamp?
• 3-part key may not be the key point, which shall be column-wise storage.
• MySQL: 22, Dustin, 1000, 45, 31, Lubber, 1001, 55, 58 …
• Columnar: 22, 31, 58, 74, Dustin, Lubber, Rusty, Rusty, 1000, 1001, 1001, …
• Flexible schema: column set flexible, may differ from row-to-row.
• Data compression. Self-indexing.
• Rows can be constructed from columns.
• Popular ones: HBase, Cassandra, Hypertable, 
 Amazon SimpleDB, Clouddata, Google bigtable, etc.
• Not always good, e.g., insert. Why? 
• Facebook MySQL -> Cassandra 50GB: W 300->0.12ms, R 350->15ms.
sid name pts age
22 Dustin 1000 45
31 Lubber 1001 55
58 Rusty 1001 35
74 Rusty 1000 35


## Slide 12

SIT Restricted
Graph Database 
• Remember why we use ERD for conceptual database design?
• Similar motivation, as many applications have native graph structure.
• Graph database: a database with an explicit graph structure.
• Each node knows its adjacent nodes.
• As long as community is more or less unchanged, do not care about how big 
the whole world is. (local steps based on the links)
• Apply graph algorithms easily. https://en.wikipedia.org/wiki/Category:Graph_algorithms


## Slide 13

SIT Restricted
Graph Database 
• Node: can contain properties.
• Relationship: connect two nodes.
• Can contain types, e.g., ACTED_IN, DIRECTED.
• Can contain properties, e.g., roles=[‘Forrest’].
• Property: are named values where the name is a string.
• e.g., ‘name, Tom Hanks’ 
• Label for each node, e.g., person, movie.
• Used to select the same type of nodes.
RDBMS Graph Database
Tables Graphs
Rows Nodes
Columns & data Properties & values
Constraints Relationships
Joins Traversal


## Slide 14

SIT Restricted
Discussion and Summary
• When do we use NoSQL?
• When you feel RDBMS is too restrictive without much flexibility. 
• When you do not care about ACID.
• When your data is too large to be centralized.
• When you have diverse data sources.
• When you have high requirement on data availability.
• No schema, no unused cell, no datatype (implicit), etc.
• Think carefully for database migration.
• NoSQL is not always good, e.g., banking and finance prefer RDBMS.


---

# Lecture 9

*Source: INF2003_AY2526_T1_Lec09*


## Slide 1

Zhang Wei
SIT
Nov. 11, 2025
INF2003: 
Database Systems
Blockchain
AY25/26 Trimester 1


## Slide 2

Module and Teaching Feedback AY25/26, Tri 1
Below are some pointers you may wish to share with 
students before inviting them to complete the 
feedback:
• Complete both module and teaching feedback.
• Please share constructive feedback in the free text 
sections
• Academic Staff will not be able to identify the student. All 
feedback received are anonymous.
• Their grades will not be affected as the feedback results 
will only be shared with the academic staff after the 
release of exam results.
From Wei: We have been improving this module 
continuously based on students’ feedback. Thank you 
for your contribution to our module and for helping 
your junior peers.


## Slide 3

What is Blockchain
• Originally for recording transactions, where:
• Transactions organized as blocks.
• Blocks are encryption-based and chained together from old to new.
• Blocks can be accessed everywhere.
• Traditional ledger: e.g., OCBC, centralized leger for clients.
• OCBC, the centralized entity, always has the truth.
• Any discrepancies, client shall reconcile with OCBC (has the say).
• Blockchain leger:
• All nodes can access. All nodes have the truth. All nodes have the say.
• What if people share different opinions? Consensus to be achieved.
• Consensus is kind of democracy, but not really one people one vote. 
SIT
SingTel
NTU
Koufu
SIT
SingTel
NTU
Koufu
王
侯
将
相
宁
有
种
乎


## Slide 4

Process
• A user initiate a transaction. 
• As confidential information inside, need to encrypt with digital signature.
• Like sign to pay in real world.
• How to let the other nodes know? 
• Broadcast.
• Are we sure all nodes know? 
• Distributed system. Theoretically, possible to wait forever. 
• Those nodes which get the message, can choose to process/record.
• Each transaction one block?
• If so, the chain will be too long.
• Normally, received a lot transactions, and include some of them in a block.
• How to motivate the nodes to include a transaction?
• Pay transaction fee.
• Pay more, higher chance to be processed; initially not the dominant one.


## Slide 5

Process
• Can I add my block to the chain?
• Where the big reward comes (details later).
• All nodes want to add one block to a chain.
• But a chain can only be extended by 1.
• Compete for the right to add block. Mining process.
• Initially, reward much larger than transaction fee.
• One node wins the competition and adds a new block.
• Need the other nodes to acknowledge the win.
• Consensus protocols. 
• New block reflects the “truth” accepted by all.
• Start another round in the new chain.
Agree
Starting Point
+ History
-> Current State


## Slide 6

Supporting Technology
• New concept, old technologies (building blocks).
• Each full node in Blockchain keeps one copy of the whole chain.
• Problem: would the chain be super large?
• Buy a data center to participate? Then it encourages centralization again.
• Main cryptography techniques: Keys and Hash, mainly for blocks.
• Hash: h(x).
• x is a long text, object, file, etc.
• h(s) is a short representation of x.
• Given x and h, only 1 h(x). Deterministic.
• Given x1 != x2, h(x1) = h(x2). Collision.
• Rare. Even there is, u cannot control.
• Various hash functions available.
• We mainly use SHA-256.
• No matter how is the input x.
• -> the hash value is always 256 0/1 digits.


## Slide 7

Hash
• Solution: each block mainly consists of hash values, not raw info.
• Same block -> 1 hash value (given the same hash function).
• Any changes in the block -> different hash -> validation.
• Fast operation.
• How?
• Start with the Genesis block, or block 0.
• Compute the hash of the whole block, with all info of index, payload, etc.
• Block 1 must include the hash of block 0, as shown in “prev”.
• Compute the hash of the whole block, with all info of index, payload, etc.
• Every block records where this block comes from -> hash chain.
• Question: is blockchain a singly or doubly linked list?
Genesis
0
N.A.
payload
hash
1
prev
payload
hash
2
prev
payload
hash
3
prev
payload
hash
4
prev
payload
hash
5
prev
payload
hash


## Slide 8

Why Blockchain Cannot Be Tempered?
• In block 2, I transferred 100 SGD to Tony Stark.
• Now the latest block is block 5. 
• I want to temper block 2, e.g., change the amount to -100. Can I?
• The payload of block 2 has been changed.
• -> the hash of block 2 changes.
• -> the hash of block 2 cannot match with the “prev’ of block 3 anymore.
• We know the chain has been tempered by some simple hash comparisons.
0
N.A.
payload
hash
1
prev
payload
hash
2
prev
payload
hash
3
prev
payload
hash
4
prev
payload
hash
5
prev
payload
hash
0
N.A.
payload
hash
1
prev
payload
hash
2
prev
payload’
hash’
3
prev
payload
hash
4
prev
payload
hash
5
prev
payload
hash
≠


## Slide 9

Motivation to Participate
• I only want to use the system. I do not want to contribute. Can?
• Some jobs to do, for the whole system.
• Keep a copy of the history and current state. 
• It is fine, as mostly small hashes instead of the large raw data.
• Package transactions.
• Add new blocks.
• Motivation: 1) transaction fee; 2) new block reward.
• In the beginning stage, new block reward is dominant.
• Transaction fee will be more important as the system matures.


## Slide 10

Motivation to Participate
• Finding a nonce: called mining.
• Possible > 1 miners get a valid nonce at the (approximately) same time?
• Payload can be different.
• Nonce can be different.
• Mining is a process of looking for luck.
• With a valid nonce and a valid block -> broadcast to all.
• Once become the most accepted block -> officially add the block.
• The miner, who add the block, received the transaction fee and block reward.
• This is why, your transaction may never be included if you put 0 trans fee.
• e.g., bitcoins rewarded decreasing in time (but can be increasing in value).
• Bitcoin: half for every 210,000 blocks.
• Since Feb. 2019, each new block gets 12.5 BTC ~= SGD 55,000.
• Since May 2020, each new block gets 6.25 BTC ~= SGD 400,000.
• 2024: 3.125 BTC ~= SGD 381,000.
• BTC 2010: 10,000 BTC 2 pizzas -> 2023 ~SGD 500 MILLION SGD! 
• BTW, the guy recently said he does not regret …
https://www.coindesk.com/price/bitcoin
Luck is not a superpower.


## Slide 11

Proof of Work
• Finding a valid nonce is more or less guessing again and again.
• Who shall get the mining reward? Luck is the only factor?
• If everyone can, raspberry Pi or MCU rules the world.
• System attack becomes cheap -> system not secure anymore. 
• Shall be sincere enough. Sincere ~ computing power in our story.
• Say, hash threshold 2^200 for SHA-256.
• The beginning 56 digits are all 0.
• Each digit 50% chance to be 0 -> try how many times can win?
• Expectation: 2^56 times -> expected 1 success.
• Expectation: hard to prove, easy to verify.
• Hard: intensive computation to find a valid nonce.
• Slower chain expansion. 
• Expensive to cheat, e.g., adding invalid blocks.
• Disagreement? -> computing power as the justice … 
• Easy: just one hash comparison.
• Operational friendly. Traceability and so on.
“It is not by speeches and 
majority resolutions that the 
great questions of the time are 
decided, but by iron and blood.”


## Slide 12

Disagreement?
• The world is not perfect -> ppl extend the chain with different views.
• Miner 1 got a valid nonce, propose to add his block, and mine the next.
• Miner 2 got a valid nonce, propose to add his block, and mine the next.
• What will happen?
• State fork.
• Longest-chain rule. No matter how many forks, only the longest one wins.
• Every miner, checks the latest chain. Any forks, choose the longest one.
• Suppose all miners are fair, best way: broadcast early w/ good network.
0
N.A.
payload
hash
1
prev
payload
hash
2
prev
payload
hash
3
prev
payload
hash
4
prev
payload
hash
5
prev
payload
hash
4’
prev
payload
hash


## Slide 13

Discussion
• Is blockchain a good database for storing data?
• Record-keeping system. Cannot even work efficiently or work for CRUD.
• BTC, 1MB per block, 250B per trans, 10 min per block -> 400 trans per min.
• Visa: ~1,700 per second -> 102,000 trans per min.
• Can blockchain offer physical world traceability? 
• Hardly any online system has real control in the offline physical world.
• Buy organic food in blockchain. Package can be swapped in physical world.
• New and hot technologies are not omnipotent.
• What are the suitable areas for blockchain?
• International and universal currency beyond the current financial system.
• No long-waiting remittance. No swift code. 
• Unfortunately, also the reason why BTC is widely used in black market.
• Anti-counterfeiting. Data in the chain cannot be changed. 
• Change, no matter how small, can be detected w/ hash comparison.
• Patent, Covid-19 cross-border documents, etc.


## Slide 14

Summary
• History -> now.
• We lack trust to each other, especially in a world-wide scenario. 
• We do not even trust 3
rd party. 
• History recorded in distributed system, managed by all participate.
• “Agree on history” eventually leads to “agree on present”.
• Chain and hash.
• Raw data is not stored, making each participant keeps a full copy possible.
• Chain is hash-based, where each block records the info of the last block.
• -> once the last block is tempered, there will be a hash mismatch.
• Proof-of-work.
• Mostly widely used. 
• Higher computing power -> more likely to add new block -> more likely get 
reward and fee.
• Fair and secure. Bad guys must pay a lot with steeply diminishing return. 
• Be realistic and do not be fooled.


---

# Lecture 10

*Source: INF2003_AY2526_T1_Lec10*


## Slide 1

Zhang Wei
SIT
Nov. 18, 2025
INF2003: 
Database Systems
Data Warehouse
AY25/26 Trimester 1


## Slide 2

Data Warehouse
• Definition: a central repository of integrated data.
• Orthogonal data dimensions:
• Application dimension: the data normally come from multiple data sources.
• Sales, salaries, operational data, human resources data.
• Time dimension: both historical data and current data are included. 
• Objective: reporting and data analysis.
• One of the key components of business intelligence.
• Focus on OLAP (w/ historical data) instead of OLTP. (more details later)
• Also known as enterprise data warehouse.
• Architecture (like computer system):
• Operational system.
• e.g., marketing or sales.
• Integration layer.
• ETL, ELT, data cleansing.
• Data warehouse.


## Slide 3

Data Loading - ETL
• ETL: extract, transform, load.
• Extract: extracting data from different sources, e.g., operation, external
• Transform: transforming/enriching the data, e.g., data type conversion, 
combining columns like first and last names, data cleansing, masking.
• Load: loading it into the data warehouse.
• Staging layer: store raw data extracted from different sources in 
operational data store. (some data may be deleted later)
• Integration layer: integrate the data from the stage layer and move the 
data to another database, e.g., data warehouse.
• Data is arranged into hierarchical groups, or dimensions. 
• Dimensions are arranged into facts and aggregated facts.
• Schema = fact + dimension.
• Access layer: help users retrieve data.
• Challenges: data volume (time, spike), dirty data, synchronization … 
• Tools: IBM InfoSphere DataStage, Informatica PowerCenter, and so on.
• ELT: no transformation before loading; far less popular.


## Slide 4

Conceptual Modeling - Schemas
• Two popular schemas:
• Star schema
• Snowflake schema
• Star schema.
• Simplest style of data warehouse schema; most popular.
• 1 fact table + n referencing dimension tables.
• Name from its physical model in a star shape.
• Fact table as center.
• Dimension tables as star’s points.
• Business process data → facts.
• Facts generally consist of numeric values and foreign keys.
• Transaction fact (sales events); snapshot fact (month end); accumulating snapshot 
(monthly total).
• Dimension data: measurable, quantitative, as the fact descriptive attri..
• Dimension should be wide or narrow? 
• Time dimension; geography dimension; product dimension; employee dimension; range 
dimension.


## Slide 5

Star Schema
• Benefits:
• Denormalized (relatively). 
• For dimensions.
• Simpler queries: simple join logic.
• Query performance: read intensive.
• Disadvantages:
• Data integrity not enforced. 
• Often, data loading is highly controlled for 
protection.
• Not flexible. 
• Not suitable for complex analytics. 
• More purpose-built. 
• Example: 
• How many TV sets have been sold, for each 
brand and country, in 1997.
• Simple join?
• Note the keys.


## Slide 6

Snowflake Schema
• ER diagram resembles a snowflake shape.
• Centralized fact tables.
• Connected to multiple dimensions.
• Like star schema, but different.
• Dimensions normalized into multiple related tables.
• May have multiple levels of relationships.
• Star schema: dimension represented by a single table.
• Benefits: storage saving.
• Does storage saving makes sense? 
• Disadvantage: complex query.
• Alleviated year by year, but still slow.
• There is no end to normalization, 1NF, 2NF, 3NF, and so on. 
• Technically, there is a more normalized solution. 
• More normalized, more joins, more complex …
• Check the example in the next slide.


## Slide 7

Star vs Snowflake


## Slide 8

OLAP: Online Analytical Processing 
• Relational DB: focus on OLTP (online transaction processing)
• Transaction: atomic change of state.
• e.g., banking, sales, trading …
• Process small, quick, interactive, large volume workloads.
• Optimized for INSERT, UPDATE operation. 
• Focus on read operations.
• Highly normalized.
• Goals: availability, speed, concurrency, recoverability.
• OLAP.
• Derived from OLTP but allows complex analytics queries.
• Deliberately de-normalized with high SELECT throughput. 
• Applications: 
• e.g., sales report, marketing report, budgeting and forecasting.
• API support not as good as SQL. (true for most less popular functions)
• Options include Microsoft MDX and XML for Analysis.
• Market (years ago): 
• Microsoft was ~30%, Oracle was ~20%, IBM was ~15%, SAP was ~15%, others ~20%.
• Core: OLAP cube.


## Slide 9

OLAP Cube
• Cube, a multi-dimensional array of data.
• Also called hyper-cube if the dimension is higher than 3.
• Similar concept: cross-tabbed report in 1980s.
• Pre-computation can support an efficient query processing.
• An easy way for visualization.
• Terminology.
• Slice: keep some dimensions as constant and show the change of a few dimensions.
• e.g., apple sales in 2018.
• Measure: derived from the fact table.
• Dimension: derived from the dimension table.
• Cell: holds a number to represent some measure.
• e.g., sales, profits, budget.
• Hierarchy: organization of the elements of a dimension.
• AY20/21 ∋ AY20/21 Trimester 2.
• Trimester 2 ∋ 2
nd half of Trimester 2.
• Operations: slice, dice, drill down/up, roll-up, pivot.
Before time began, 
there was the Cube


## Slide 10

OLAP Cube: Sample Queries
• You might think the concept is different. The queries are familiar.
• Data cube: ProductSales(product, region, sday, sales)
• 3 dimensions: product, region, and day.
• 1 measure: sales.
• Q1. Find the total sales for each product.
• A1. SELECT SUM(P.sales) FROM ProductSales AS P GROUP BY product;
• Q2. Find the total sales for each region.
• A2. SELECT SUM(P.sales) FROM ProductSales AS P GROUP BY region;
• Q3. Find the total sales for each product on each day.
• A3. SELECT SUM(P.sales) FROM ProductSales AS P GROUP BY product, sday;
• Q4. Find the total sales so far.
• A4. SELECT SUM(P.sales) FROM ProductSales AS P;


## Slide 11

Cube Operations
• Slice: picking a rectangular 
subset of a cube.
• Example:
• Fix location as Asia.
• Variables: product and time.
• Dice: sub-cube with specific 
values of multiple dimensions.
• Each dimension has a range.
• Is slice a dice?
• Example.
• Asia & Africa.
• 2001 – 2003.


## Slide 12

Cube Operations
• Drill Down: navigate among levels of data, from summarized to detailed.
• e.g., from the summary sales data to the sales for the individual products.
• Roll Up: navigate among levels of data, from detailed to summarized.
• The summarization rule could be an aggregate function.
• e.g., sum, profit = sales – expenses.
• Other aggregation functions: COUNT, MAX, MIN …
• Pivot: rotate the cube, to see different faces.
• Different perspectives.
• From one year to one location.


## Slide 13

Cube Operations: Exercise
• For the following questions, which OLAP operator shall we use?
• Q1. Find the sales of each city.
• A1. ?
• Q2. Given the sales of each city, get the sales for each state.
• Assume each state includes several cities.
• A2. ? 
• Q3. Find the top-5 products ranked by total sales.
• A3. ?
• Q4. Given the sales of each state, get the sales of each city.
• A4. ?


## Slide 14

OLTP vs. OLAP - Summary
OLTP OLAP
Basic Online transactional system and 
manages database modification.
Online data retrieving and data 
analysis system.
Focus Insert, update, delete information. Extract data and analyze for decision 
making.
Data Source OLTP and its transactions. Different OLTPs database.
Transaction OLTP has short transactions. OLAP has long transactions.
Time Comparatively less in OLTP. Comparatively more in OLAP.
Queries Simpler. Complex.
Normalization Normalized (3NF). Not normalized.
Integrity Must maintain data integrity 
constraint.
Does not get frequently modified. 
Hence, data integrity is not affected.
Method Uses traditional DBMS. Uses the data warehouse.
Users Clerk and IT professionals Knowledge workers
No. of users Thousands of users. Only hundreds of users.
Src: https://www.guru99.com/oltp-vs-olap.html, https://techdifferences.com/difference-between-oltp-and-olap.html


## Slide 15

DBMS vs. Data Warehouse
• More or less the same with the comparison between OLTP and OLAP.
• DBMS: tuned for OLTP.
• Access methods, indexing, concurrency control, recovery.
• Data Warehouse: tuned for OLAP.
• Complex queries, multidimensional view, consolidation.
• To summarize (may be not rigorous).
• DBMS is used to run a business.
• Data warehouse helps optimize the business.


---

# Tutorial 1

*Source: INF2003_AY2526T1_Tutorial1*


## Slide 1

INF2003 AY2526 T1 Page 1 of 2
SIT Internal
INF2003: Database systems
Tutorial 1
Please try out those questions on your own. We will go through how to answer those questions in our 
Tutorial session scheduled at week 5 lab time online.
1. Mr. Wong owns a company and wants to store information like payroll about the employees. The 
data volume compels him to buy a database system. He is stingy and wants to buy a system with 
the fewest possible features. He also plans to run it as a stand-alone application on his PC and will 
not share the information with anyone else. Please indicate which of the following DBMS features
Mr. Wong should (or should not) pay for and why.
a. Security.
b. Concurrency control.
c. Crash recovery. Yes
d. Query language.
2. Consider the instance of the Students relation shown in the table below. Which attribute (or a set 
of attributes) is suitable as candidate key? 
SID Name Login Age GPA
S200111 Alvin alvin@sit 19 3.5
S200112 Donny donny@sit 18 4.1
S200113 Eric rric@uog 20 2.9
S200114 Alvin alvin@uog 21 3.8
S200115 Lisa lisa@digipen 18 4.0
S200116 Kate kate@sit 19 3.6
3. Assume we have two relations: 
R(A,B): {(0,1), (2,3), (2,4), (3,4)} 
S(B,C): {(0,1), (2,4), (2,5), (3,4), (0,2)} 
Give the result of the following relational algebra operations:
a) πA+B, 2*A (R) 
b) R ⋈ S 
c) R S


## Slide 2

INF2003 AY2526 T1 Page 2 of 2
SIT Internal
4. Consider the following airline scenario where you need to store information of flights, aircraft, 
employee and their certifications.
FOUR (4) given relations:
Flights (flno: integer, from: string, to: string, distance: integer, departs: time, arrives: time) 
Aircraft (aid: integer, aname: string, cruisingrange: integer) 
Certified (eid: integer, aid: integer) 
Employees (eid: integer, ename: string, salary: integer)
Note that the Employees relation is used to store information for all employees. An employee is a 
pilot if he/she is certified to fly an aircraft. Please write the following queries in SQL.
a) Find the names of the pilots certified for some Boeing aircraft (aircraft name is ‘Boeing’).
b) Find the eids of the employees who are certified for the largest number of aircraft.
 
c) Find the eids of the employees who make the highest salary.
5. Given a relation S (A, B, C), the first four tuples are follows: (1, 2, 3), (4, 2, 3), (5, 3, 3), (5, 3, 4). Which 
of the following functional dependencies do not hold over relations S? Please explain your answer.
a. A -> B. 
b. BC -> A.
c. B -> C. 
6. Given a relation R (A,B,C,D,E), we have FDs: AB->CD, D->E, A->C, B->D. 
Find the BCNF decomposition of the above relation. Evaluate if the final decomposition is 
dependency preserving.


---

# Tutorial 2

*Source: INF2003_AY2526T1_Tutorial2*


## Slide 1

INF2003 Page 1 of 2
SIT Restricted
INF2003: Database System
Tutorial 2
Q1. Given the below B+ tree with up to 3 keys per node.
Based on the given B+ tree, draw the B+ tree after inserting 6; then 
draw the B+ tree after further inserting 12; then draw the B+ tree after 
further inserting 20.
Q2. Given the below B+ tree with up to 3 keys per node.
Based on the given B+ tree, please list the nodes to be visited in order 
for searching 8 and the nodes for searching all the keys between 8 and 
50. 
Then, please draw the B+ tree after deleting 12; then draw the B+ tree 
after further deleting 15. Given the nearest left sibling and the nearest 
right sibling have the same number of keys, we prioritize the left one 
for key borrowing and nodes merging operations.


## Slide 2

INF2003 Page 2 of 2
SIT Restricted
Q3. Given the following transaction scheduling. Which of the transaction 
property implies that the total account balance remains the same after 
the transactions? R() and W() indicate read and write operation, 
respectively, where the input is data.
Time Slot TXN-1 TXN-2
1 R(D1)
2 D1: = D1 - 100
3 R(D2)
4 D2: = D2 + 100
5 W(D1)
6 W(D2)
Q4. Given the below scheduling of three transactions, TXN-1, TXN-2, and 
TXN-3, please indicate an equivalent serial scheduling. R() and W() 
indicate read and write operation, respectively, where the input is data.
Time Slot TXN-1 TXN-2 TXN-3
1 R(D1)
2 R(D2)
3 R(D2)
4 W(D2)
5 W(D1)
6 W(D1)
7 R(D1)
8 W(D1)


---

# Tutorial 1 Answers

*Source: INF2003_AY2526T1_Tutorial_answer1*


## Slide 1

INF2003 AY2526 T1 Page 1 of 3
SIT Internal
INF2003: Database systems
Tutorial 1
Please try out those questions on your own. We will go through how to answer those questions in our 
Tutorial session scheduled at week 5 lab time online.
1. Mr. Wong owns a company and wants to store information like payroll about the employees. The 
data volume compels him to buy a database system. He is stingy and wants to buy a system with 
the fewest possible features. He also plans to run it as a stand-alone application on his PC and will 
not share the information with anyone else. Please indicate which of the following DBMS features
Mr. Wong should (or should not) pay for and why.
a. Security. Yes, this is important to any dbms.
b. Concurrency control. No, he is the only user.
c. Crash recovery. Yes, same as security.
d. Query language. Yes, this is an essential feature.
2. Consider the instance of the Students relation shown in the table below. Which attribute (or a set 
of attributes) is suitable as candidate key? 
SID Name Login Age GPA
S200111 Alvin alvin@sit 19 3.5
S200112 Donny donny@sit 18 4.1
S200113 Eric rric@uog 20 2.9
S200114 Alvin alvin@uog 21 3.8
S200115 Lisa lisa@digipen 18 4.0
S200116 Kate kate@sit 19 3.6
SID and Login.
3. Assume we have two relations: 
R(A,B): {(0,1), (2,3), (2,4), (3,4)} 
S(B,C): {(0,1), (2,4), (2,5), (3,4), (0,2)} 
Give the result of the following relational algebra operations:
a) πA+B, 2*A (R): {(1,0),(5,4),(6,4),(7,6)}
b) R ⋈ S : {(2,3,4)}
c) R S : this is left outer join. {(0,1,NULL),(2,3,4),(2,4,NULL),(3,4,NULL)}


## Slide 2

INF2003 AY2526 T1 Page 2 of 3
SIT Internal
4. Consider the following airline scenario where you need to store information of flights, aircraft, 
employee and their certifications.
FOUR (4) given relations:
Flights (flno: integer, from: string, to: string, distance: integer, departs: time, arrives: time) 
Aircraft (aid: integer, aname: string, cruisingrange: integer) 
Certified (eid: integer, aid: integer) 
Employees (eid: integer, ename: string, salary: integer)
Note that the Employees relation is used to store information for all employees. An employee is a 
pilot if he/she is certified to fly an aircraft. Please write the following queries in SQL.
a) Find the names of the pilots certified for some Boeing aircraft (aircraft name is ‘Boeing’).
SELECT e.ename
FROM Employees e, Certified c, Aircraft a
WHERE a.aname=’Boeing’ AND a.aid=c.aid AND c.eid=e.eid
alternatively, you can use join
SELECT e.ename
FROM Employees AS e
JOIN Certified AS c ON e.eid = c.eid
JOIN Aircraft AS a ON a.aid = c.aid
WHERE a.aname = 'Boeing'
b) Find the eids of the employees who are certified for the largest number of aircraft.
SELECT c.eid from Certified c
GROUP by c.eid
HAVING COUNT(c.aid) >= ALL (
SELECT COUNT(c1.aid) from Certified c1
Group by c1.eid
)
alternatively, you can use DESC
SELECT c.eid, COUNT(*) as ct from Certified c
GROUP by c.eid
ORDER by ct DESC
Limit 1;
c) Find the eids of the employees who make the highest salary.
SELECT e1.eid from Employees e1
WHERE e1.salary = (
 SELECT MAX(salary) from Employees e2)


## Slide 3

INF2003 AY2526 T1 Page 3 of 3
SIT Internal
5. Given a relation S (A, B, C), the first four tuples are follows: (1, 2, 3), (4, 2, 3), (5, 3, 3), (5, 3, 4). Which 
of the following functional dependencies do not hold over relations S? Please explain your answer.
a. A -> B. cannot tell, as we only have the first 4 tuples.
b. BC -> A. not hold, as the first two tuples already not hold
c. B -> C. not hold, as the third and fourth tuples not hold
6. Given a relation R (A,B,C,D,E), we have FDs: AB->CD, D->E, A->C, B->D. 
Find the BCNF decomposition of the above relation. Evaluate if the final decomposition is 
dependency preserving. 
 Step 1: we need to check every FD if they are in BCNF.
AB->CD: let’s find closure of AB: AB+,
 we start from AB+={AB}, because of AB->CD, we have AB+={AB CD} 
 using D->E, we have AB+={AB CD E}, it contains all attributes in R. So AB->CD is in BCNF.
D->E, check D+: at first, D+ ={D E}, this FD is not in BCNF
A->C, check A+: at first, A+ = {A C}, so this FD is not in BCNF
B->D, check B+: at first, B+={B D}, use D->E, we have B+={ B D E}, so this FD is not in BCNF as well
Step 2: decomposition
 start with the first no in BCNF FD: D->E, we can decompose the (ABCDE) into (DE) and (ABCD)
 use the second A->C, we decompose (ABCD) to: (AC) and (ABD)
 use the last one: B->D, we decompose (ABD) to (BD) and (AB)
so after all the decomposition, we have: (DE) (AC) (BD) (AB)
step 3: check dependency preserving
D->E is preserved in (DE)
A->C is preserved in (AC)
B->D is preserved in (BD)
let’s check AB->CD still preserved: 
from AB->AB, we can get AB->A and AB->B. using AB->A, as we have A->C, so we can use transitivity
rule, we can get AB->C
from AB->B, we have B->D, so we use transitivity rule again, we get AB->D
from AB->C and AB->D, we get AB->CD using union rule.
all the FDs are preserved after decomposition.


---

# Tutorial 1 Solutions

*Source: INF2003_Tutorial1_Solutions*


## Slide 1

INF2003 Database Systems
Tutorial 1 - Solutions
Question 1: DBMS Features for Mr. Wong
a. Security: NO
Since Mr. Wong runs this as a stand-alone application on his PC and won't
share with anyone else, he doesn't need multi-user security features.
b. Concurrency control: NO
Concurrency control manages simultaneous access by multiple users.
Since only Mr. Wong will use the system, this feature is unnecessary.
c. Crash recovery: YES
Even for single-user systems, crash recovery is essential to protect
against data loss from system failures, power outages, or software
crashes. Payroll data is critical and shouldn't be lost.
d. Query language: YES
A query language (like SQL) is needed to retrieve and manipulate payroll
data effectively. Without it, accessing and analyzing employee information
would be extremely difficult.
Question 2: Candidate Keys for Students Relation
Suitable candidate keys:
SID - Each student has a unique ID (all values are distinct)
Login - Each login is unique across all students
Not suitable:
Name - "Alvin" appears twice, so it's not unique
Age - Multiple students share the same age
GPA - Not unique
Best choice: SID is the most appropriate primary key as it's designed as
a unique identifier.
Question 3: Relational Algebra Operations
Given:
R(A,B): {(0,1), (2,3), (2,4), (3,4)}
S(B,C): {(0,1), (2,4), (2,5), (3,4), (0,2)}
a) π(A+B, 2*A)(R):
(0,1): A+B=1, 2*A=0 → (1,0)
(2,3): A+B=5, 2*A=4 → (5,4)
(2,4): A+B=6, 2*A=4 → (6,4)
(3,4): A+B=7, 2*A=6 → (7,6)
Result: {(1,0), (5,4), (6,4), (7,6)}
b) R ⋈ S (Natural Join on B):
(0,1) joins with (0,1), (0,2) → (0,1,1), (0,1,2)
(2,3) joins with nothing (no B=3 in S)
(2,4) joins with (2,4), (2,5) → (2,4,4), (2,4,5)
(3,4) joins with (3,4) → (3,4,4)
Result: {(0,1,1), (0,1,2), (2,4,4), (2,4,5), (3,4,4)}
c) R ∪ S (Union):
This operation is not valid because R and S have different schemas (R
has attributes A,B while S has attributes B,C). Union requires relations with
the same set of attributes.
Question 4: SQL Queries for Airline Scenario
a) Names of pilots certified for Boeing aircraft:
SELECT DISTINCT e.ename
FROM Employees e
JOIN Certified c ON e.eid = c.eid
JOIN Aircraft a ON c.aid = a.aid
WHERE a.aname = 'Boeing';
b) Employees certified for the largest number of aircraft:
SELECT eid
FROM Certified
GROUP BY eid
HAVING COUNT(aid) = (
SELECT MAX(cert_count)
FROM (
SELECT COUNT(aid) AS cert_count
FROM Certified
GROUP BY eid
) AS counts
);
c) Employees with the highest salary:
SELECT eid
FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees);
Question 5: Functional Dependencies
Given tuples: (1,2,3), (4,2,3), (5,3,3), (5,3,4)
a. A → B: HOLDS
Each A value consistently maps to the same B value (A=5→B=3,
A=1→B=2, A=4→B=2).
b. BC → A: Does NOT hold
BC=(2,3) appears in tuples 1 and 2 with different A values (1 and 4). This
violates the functional dependency.
c. B → C: Does NOT hold
B=3 appears with C=3 in tuple 3 and C=4 in tuple 4 (inconsistent). This
violates the functional dependency.
Answer: Functional dependencies b and c do not hold.
Question 6: BCNF Decomposition
Given: R(A,B,C,D,E) with FDs: AB→CD, D→E, A→C, B→D
Step 1: Find candidate keys
From the given functional dependencies:
• B→D and D→E implies B→DE
• A→C
• Combined with AB→CD, we get AB→ABCDE
Candidate key: AB
Step 2: Check for BCNF violations
A relation is in BCNF if for every FD X→Y, X is a superkey.
• AB→CD: AB is a superkey ✓
• D→E: D is NOT a superkey ✗
• A→C: A is NOT a superkey ✗
• B→D: B is NOT a superkey ✗
Step 3: Decomposition Process
1. Decompose using D→E:
• R1(D,E) with FD: D→E
• R2(A,B,C,D) with FDs: AB→CD, A→C, B→D
2. Decompose R2 using B→D:
• R3(B,D) with FD: B→D
• R4(A,B,C) with FD: A→C
3. Decompose R4 using A→C:
• R5(A,C) with FD: A→C
• R6(A,B)
Final BCNF Decomposition:
• R1(D,E) with D→E
• R3(B,D) with B→D
• R5(A,C) with A→C
• R6(A,B)
Dependency Preservation Check:
• D→E: preserved in R1 ✓
• B→D: preserved in R3 ✓
• A→C: preserved in R5 ✓
• AB→CD: NOT directly preserved (requires joining R3, R5, R6) ✗
Conclusion: The decomposition is NOT dependency preserving
because AB→CD cannot be verified without joining multiple relations.
