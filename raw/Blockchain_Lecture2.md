# Blockchain Lecture 2

## Slide 1

Connect With Me On Twitter | @HendrikEbbers
Lecture 2

## Slide 2

Connect With Me On Twitter | @HendrikEbbers
Lecture table of contents
•Learn about Blockchain 
•Learn about hashing 
•Learn about or coding standards

## Slide 3

Connect With Me On Twitter | @HendrikEbbers
Blockchain 
Basics

## Slide 4

Connect With Me On Twitter | @HendrikEbbers
Let’s start with a block
data: my_transaction 
timestamp: 639246289246

## Slide 5

Connect With Me On Twitter | @HendrikEbbers
Let’s start with a block
data: my_transaction 
timestamp: 639246289246
This is our cool data entry

## Slide 6

Connect With Me On Twitter | @HendrikEbbers
Let’s start with a block
data: my_transaction
timestamp: 639246289246
This is our cool data entry
It is A common use case for blocks in a blockchain to store transactions

## Slide 7

Connect With Me On Twitter | @HendrikEbbers
Let’s start with a block
data: my_transaction 
timestamp: 639246289246
This is our cool data entry
It is A common use case for blocks in a blockchain to store transactions
WAIT

## Slide 8

Connect With Me On Twitter | @HendrikEbbers
Let’s start with a block
data: my_transaction 
timestamp: 639246289246
This is our cool data entry
It is A common use case for blocks in a blockchain to store transactions
WAIT
• a SQL DB 
• Java Objects 
• Java Records 
• JSON 
• a simple text file 
• JPA 
• Hibernate 
• MongoDB 
• the Cloud 
• Redis
I can store the exact same information by simply using

## Slide 9

Connect With Me On Twitter | @HendrikEbbers
Let’s start with a block
data: my_transaction 
timestamp: 639246289246
I want to mutate the 
transaction and add 
1,000,000 € to my 
account We want to secure the data and 
make it impossible to change 
any transaction information

## Slide 10

Connect With Me On Twitter | @HendrikEbbers
... the chain comes into play
on 
 
data
time
prev
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00f7d329a3091…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00a67e826ac79…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 005df89a5284d…

## Slide 11

Connect With Me On Twitter | @HendrikEbbers
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00f7d329a3091…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00a67e826ac79…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 005df89a5284d…
The Blockchain
on 
 
data
time
prev
The hash of the previous block

## Slide 12

Connect With Me On Twitter | @HendrikEbbers
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00f7d329a3091…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00a67e826ac79…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 005df89a5284d…
The Blockchain
on 
 
data
time
prev
Each blocks defines the validity 
of all previous blocks

## Slide 13

Connect With Me On Twitter | @HendrikEbbers
Hash Functions

## Slide 14

Connect With Me On Twitter | @HendrikEbbers
Hash Functions
•Map data to a hash 
•Input is normally (large) data of any size and 
type 
•Output is normally fixed-size data
#5f43d, #861a3, …

## Slide 15

Connect With Me On Twitter | @HendrikEbbers
Specification of Hash Functions
•Uniformity: map the inputs as evenly as possible over its output 
range 
•Efficiency: Calculation must be fast without using much memory 
•Deterministic: for a given input value it must always generate the 
same hash value. 
•Surjection: Every value of the hash range should be a reachable 
result 
•One-way-function: Not possible to reverse the computation

## Slide 16

Connect With Me On Twitter | @HendrikEbbers
Secure Hash Functions
•Data Integrity: Ensures data integrity by generating a unique hash 
output for a given input, making any alteration in data easily 
detectable. 
•One-Way Function: Functions that are easy to compute in one 
direction but computationally infeasible to reverse. 
•Collision Resistance: Designed to minimize the probability of two 
different inputs producing the same hash output. 
•Fixed Output Length: Produces a fixed-length output, regardless of 
the length of the input, aiding in data uniformity and consistency.

## Slide 17

Connect With Me On Twitter | @HendrikEbbers
Example of Hashing
Fox
The red fox jumps over 
the blue dog
The red fox jumps 
ouver the blue dog
The red fox jumps oer 
the blue dog
DECD 3454 BBED 7884 7517 
696C 24D9 7009 CA99 2D17
0086 46BB FB7D CBE2 823C 
ACC7 6CD1 90B1 EE6E 3ABC
8FD8 7558 7851 4F32 DICE 
76B1 7949 0DA4 AEFE 4819
8ACA D682 D588 4C75 4BF 
1799 7D88 BCF8 92B9 6A60
Input Hash Function Hash Value

## Slide 18

Connect With Me On Twitter | @HendrikEbbers
Usecases of Hashing
•Checksum: check a large download by comparing the 
checksum over the bytes of the file 
•Passwort storage: Store the hash of a password instead of 
storing the real password 
•Hashtable: Store large data collections in hash based 
tables / buckets

## Slide 19

Connect With Me On Twitter | @HendrikEbbers
Digit Sum
•The most simple hash function

## Slide 20

Connect With Me On Twitter | @HendrikEbbers
Digit Sum
•The most simple hash function

## Slide 21

Connect With Me On Twitter | @HendrikEbbers
Digit Sum
•The most simple hash function
F(84001)=8+4+0+0+1=13

## Slide 22

Connect With Me On Twitter | @HendrikEbbers
Digit Sum
•The most simple hash function
F(84001)=8+4+0+0+1=13
Input Value
HASH Value

## Slide 23

Connect With Me On Twitter | @HendrikEbbers
Digit Sum
•The most simple hash function
F(84001)=8+4+0+0+1=13
Only computable in 
one direction

## Slide 24

Connect With Me On Twitter | @HendrikEbbers
Digit Sum
•The most simple hash function
F(84001)=8+4+0+0+1=13
Calculation is 
really fast!

## Slide 25

Connect With Me On Twitter | @HendrikEbbers
Digit Sum
•The most simple hash function
F(84001)=8+4+0+0+1=13
Uniformity & Surjection 
are not really good...

## Slide 26

Connect With Me On Twitter | @HendrikEbbers
Hands on lesson
•Create a small program that calculates a digit sum 
•Digit sum must be printed as string 
•Digit sum must always be 8 digits long

## Slide 27

Connect With Me On Twitter | @HendrikEbbers
MD5 Hash Function
•Message Digest Algorithm 5 
•Widely used cryptographic hash function that produces a 
128-bit (16-byte) hash value 
•Previously used in SSL certificates, password hashing, and 
other cryptographic applications

## Slide 28

Connect With Me On Twitter | @HendrikEbbers
MD5 Hash Function
•Message Digest Algorithm 5 
•Widely used cryptographic hash function that produces a 
128-bit (16-byte) hash value 
•Previously used in SSL certificates, password hashing, and 
other cryptographic applications

## Slide 29

Connect With Me On Twitter | @HendrikEbbers
•At Chaos Communication Congress 2008 researchers 
shown how they hacked MD5 
•A cluster of 200 Playstation 3 has been used 
•SSL certificate has been hacked 
•VeriSign and others stopped using MD5
MD5 Collision Vulnerabilities

## Slide 30

Connect With Me On Twitter | @HendrikEbbers
Secure Hash Algorithm (SHA)
•Family of cryptographic hash functions 
•Designed by the National Security Agency 
(NSA) 
•Published by the National Institute of 
Standards and Technology (NIST) 
•Widely used in cryptography

## Slide 31

Connect With Me On Twitter | @HendrikEbbers
Secure Hash Algorithm (SHA)
•SHA-0: 
•Not widely used. 
•Was quickly replaced by SHA-1 due to vulnerabilities. 
•SHA-1: 
•Initially considered secure but later found vulnerable to collision 
attacks. 
•Currently, its use is deprecated in favor of more secure versions.

## Slide 32

Connect With Me On Twitter | @HendrikEbbers
Secure Hash Algorithm (SHA)
•SHA-2: 
•Enhanced version with multiple hash sizes: SHA-224, SHA-256, 
SHA-384, SHA-512, SHA-512/224, and SHA-512/256. 
•Most popular version is SHA-256, used often in blockchain 
technologies. 
•SHA-3: 
•Result of a public competition to create a new hash function. 
•Structurally different from SHA-2 but offers similar levels of security.

## Slide 33

Connect With Me On Twitter | @HendrikEbbers
Secure Hash Algorithm (SHA)
•Fixed-size Output: Regardless of the input size, the SHA algorithm 
will produce a hash of fixed size specific to its version (e.g., 256 bits for 
SHA-256).
•Fast Computation: Can process data quickly, which is vital for various 
applications.
•Small Changes, Big Impact: A tiny change in input data (even one bit) 
should produce a significantly different hash.
•Collision Resistant: It should be computationally infeasible to find 
two different inputs that produce the same hash.

## Slide 34

Connect With Me On Twitter | @HendrikEbbers
Hashing in Java
•The OpenJDK uses hashing at several places 
•The OpenJDK provides different API for hash calculation
Object.hashCode()
Hashtable
HashMap
HashSet
MessageDigest

## Slide 35

Connect With Me On Twitter | @HendrikEbbers
Hashing in Java
•The OpenJDK uses hashing at several places 
•The OpenJDK provides different API for hash calculation
Object.hashCode()
Hashtable
HashMap
HashSet
MessageDigest

## Slide 36

Connect With Me On Twitter | @HendrikEbbers
MessageDigest Class
•A class that provides applications the functionality of a 
message digest algorithm for creating hash representations 
of data. 
•The following algorithms are supported by 
MessageDigest

## Slide 37

Connect With Me On Twitter | @HendrikEbbers
MessageDigest Class
•MD2 
•MD5 
•SHA-224 
•SHA-256 
•SHA-384 
•SHA-512 
•SHA-512/224 
•SHA-512/256 
•SHA3-224 
•SHA3-256 
•SHA3-384 
•SHA3-512

## Slide 38

Connect With Me On Twitter | @HendrikEbbers
MessageDigest Class
public byte[] calculateHash(final Block block) { 
final String value = block.data() + block.previousHash(); 
final byte[] message = value.getBytes(StandardCharsets.UTF_8); 
final MessageDigest md = MessageDigest.getInstance("SHA-256"); 
final byte[] hash = md.digest(message); 
return hash; 
}

## Slide 39

Connect With Me On Twitter | @HendrikEbbers
Lecture 3

## Slide 40

Connect With Me On Twitter | @HendrikEbbers
Creating A 
Blockchain

## Slide 41

Connect With Me On Twitter | @HendrikEbbers
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00f7d329a3091…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00a67e826ac79…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 005df89a5284d…
The Blockchain
on 
 
data
time
prev
Each blocks defines the validity 
of all previous blocks

## Slide 42

Connect With Me On Twitter | @HendrikEbbers
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00f7d329a3091…
The Blockchain Code
blocks: sequence 
- valid check 
- add block 
Block class Chain class
Has no idea about the chain
Simple Data 
object
Immutable
Chain knows about 
blocks
The logic
Defines the Block Chain
Many to One Relation

## Slide 43

Connect With Me On Twitter | @HendrikEbbers
Let’s start with a block
public class Block { 
private final long timestamp 
private final String data 
private final String previousHash 
public Block(final String data, final Block previousBlock) { 
this.timestamp = System.currentTimeMillis(); 
this.data = data; 
this.previousHash = HashUtils.calculateHash(previousBlock); 
} 
};

## Slide 44

Connect With Me On Twitter | @HendrikEbbers
A simple block chain
ArrayList<Block> blockchain = new ArrayList<Block>(); 
Block block1 = new Block("Hi im the first block"); 
Block block2 = new Block("Hi im the second block“, block1); 
Block block3 = new Block("Hi im the third block“, block2); 
blockchain.add(block1); 
blockchain.add(block2); 
blockchain.add(block3);

## Slide 45

Connect With Me On Twitter | @HendrikEbbers
A simple block chain
boolean isChainValid() { 
for(int i=1; i < blockchain.size(); i++) { 
Block currentBlock = blockchain.get(i); 
Block previousBlock = blockchain.get(i-1); 
String hash = HashUtils.calculateHash(previousBlock); 
if(!Objects.equals(previousBlock.hash(), hash)) { 
return false; 
} 
} 
return true; 
}

## Slide 46

Connect With Me On Twitter | @HendrikEbbers
Is that enough?
on 
 
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00f7d329a3091…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 00a67e826ac79…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 005df89a5284d…
data
time
prev

## Slide 47

Connect With Me On Twitter | @HendrikEbbers
Is that enough?No!
on 
 
data: my_hacked_data
timestamp: 639246289246 
prev_hash: 00f7d329a3091…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 997cffe950d46…
data: my_transaction 
timestamp: 639246289246 
prev_hash: 3af5f8a85ab46…
data
time
prev

## Slide 48

Connect With Me On Twitter | @HendrikEbbers
We need the same data
Independent chain A
Independent chain B
Independent chain C
If all have the 
same state we 
should be fine

## Slide 49

Connect With Me On Twitter | @HendrikEbbers
We need consensus
Independent chain A
Independent chain B
Independent chain C
