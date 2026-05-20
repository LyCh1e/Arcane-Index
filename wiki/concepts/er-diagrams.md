---
type: concept
title: "Entity-Relationship Diagrams"
domain: database-systems
course: INF2003
complexity: medium
tags: [er-diagram, entity, relationship, cardinality, participation, weak-entity, isa, subclass, schema-conversion]
updated: 2026-05-12
status: established
created: 2026-05-12
---

# Entity-Relationship Diagrams

The **Entity-Relationship (ER) model**, proposed by Peter Chen in the 1970s, is a graphical, high-level tool for database conceptual design. It covers Stages S2 (Conceptual Design) and S3 (Logical Design) of the six-stage design process, bridging requirements and the relational schema.

> ER diagrams are pictures that speak a thousand words — they surface design errors before any code is written.

---

## ER Diagram Notation (Chen-style)

| Symbol | Meaning |
|--------|---------|
| Rectangle | **Entity set** |
| Diamond | **Relationship set** |
| Oval/ellipse | **Attribute** |
| Double oval | **Multivalued attribute** |
| Dashed oval | **Derived attribute** |
| Underlined attribute | **Key attribute** (primary key) |
| Double rectangle | **Weak entity set** |
| Double diamond | **Identifying relationship** (for weak entities) |
| Bold/double line | **Total participation** |
| Single line | **Partial participation** |
| Arrow (→) | "One" side of a cardinality constraint |
| No arrow (—) | "Many" side |

---

## Entities

An **entity** is a unique, distinguishable object in the real world.  
An **entity set** is a collection of entities sharing the same properties (same attributes, types, and key).

Entity ≈ object in OOP, but *static* — no methods.

**Example:**

```
Entity: Student (id=1001, name='John Doe')
Entity set: { (1001, 'John'), (1002, 'Arya'), … }
```

---

## Attribute Types

| Type | Description | Notation |
|------|-------------|---------|
| **Key attribute** | Uniquely identifies each entity | Underlined in the oval |
| **Simple attribute** | Single atomic value | Plain oval |
| **Composite attribute** | Made up of sub-attributes (e.g., Address = street + suburb + postcode) | Oval with child ovals |
| **Multivalued attribute** | Can hold multiple values (e.g., Phone — a person may have several) | Double oval |
| **Derived attribute** | Computed from another attribute (e.g., Age derived from DOB) | Dashed oval |

---

## Relationships

A **relationship** is an association between two or more entities. It is uniquely identified by the keys of its participating entities and may have its own attributes.

**Example:** `Lecturer (20221001) teaches Course (ICT2103) since 2022`  
The `since` attribute belongs to the *Teaches* relationship, not to either entity.

### Participation Constraints

Specify whether every entity in the set *must* participate in the relationship.

| Constraint | Notation | Meaning |
|------------|----------|---------|
| **Total participation** | Bold / double line | Every entity is involved in at least one relationship (≥ 1) |
| **Partial participation** | Single line | An entity may or may not participate (0 or more) |

**Example:** Every Booking must have a Customer (Booking: total). Not every Customer must have made a Booking (Customer: partial).

### Cardinality

The number of entities on each side of the relationship:

| Cardinality | Notation | Meaning |
|-------------|----------|---------|
| One-to-one (1:1) | Arrow on both sides | Each entity in A relates to at most one in B, and vice versa |
| Many-to-one (N:1) | Arrow on one side | Many A relate to one B |
| One-to-many (1:N) | Arrow on one side | One A relates to many B |
| Many-to-many (M:N) | No arrows | Many A relate to many B, and vice versa |

### Degree of Relationship

| Degree | Name | Example |
|--------|------|---------|
| 1 entity set | Unary (recursive) | Module is prerequisite for Module |
| 2 entity sets | Binary | Teacher teaches Module |
| 3 entity sets | Ternary | Teacher teaches Module in Programme |

> **Good practice**: avoid ternary relationships where possible — decompose into multiple binary relationships. Ternary relationships add complexity and make constraints harder to enforce.

---

## Weak Entities

A **weak entity** cannot be uniquely identified by its own attributes alone — it depends on a **strong (owner) entity** for identification.

- Identified by: **owner entity's key + weak entity's partial key** (discriminator)
- Participates with **total participation** in the identifying relationship
- If the owner is deleted, the weak entity must also be deleted (`ON DELETE CASCADE`)

**Example:** `Dependent` (of an airline booking) cannot exist without a `Booking`. The Dependent's name alone does not uniquely identify it — it needs the `BookingID` from the parent.

```
Notation: Double rectangle for weak entity, double diamond for identifying relationship
```

---

## Subclasses and ISA (Inheritance)

A **subclass** is a more specific type of an existing entity that inherits its attributes and relationships.

**Declare**: `A ISA B` — every A entity is also a B entity.

**Constraints:**

| Constraint | Description |
|------------|-------------|
| **Overlap** (on subclasses) | Can an entity be a member of multiple subclasses? E.g., can an employee be both `HourlyEmp` and `ContractEmp`? Usually: disallowed. |
| **Covering** (on superclass) | Must every entity in the superclass belong to at least one subclass? E.g., must every `Employee` be either `HourlyEmp` or `ContractEmp`? Usually: yes. |

**Example:**

```
Employees (name, ssn, lot)
    ISA
    ├── HourlyEmps (hourly_wages, hours_worked)
    └── ContractEmps (contractid)
```

---

## Converting ER Diagrams to Relational Schema

### Entity Sets → Tables

Each entity set becomes a table. Attributes become columns. The primary key is carried over.

```sql
-- Entity: Product(name, price, category)
CREATE TABLE Product (
    name     CHAR(50) PRIMARY KEY,
    price    DOUBLE,
    category VARCHAR(30)
);
```

### Composite Attributes → Flattened

Flatten composite attributes into their atomic components:

```
Address(street, suburb, postcode) → street, suburb, postcode as separate columns
```

### Multivalued Attributes → Separate Table

A multivalued attribute becomes a new table linking values to their entity:

```
Person has FavColour (multivalued)

→ Person(pid, name, dob)
→ FavColour(pid, colour)   -- FK: pid REFERENCES Person
```

### Relationship Sets → Tables

A relationship set becomes a table containing:
- Foreign keys for all participating entity sets
- Descriptive attributes of the relationship

```sql
CREATE TABLE Manages (
    ssn   CHAR(11),
    did   INTEGER,
    since DATE,
    PRIMARY KEY (ssn, did),
    FOREIGN KEY (ssn) REFERENCES Managers,
    FOREIGN KEY (did) REFERENCES Departments
);
```

**Many-to-many**: must become a separate table with a composite primary key.

**Optimisation for participation constraint (at-most-one)**:
If a constraint means each department has *at most one* manager, the relationship's key is just `did`. The `Manages` and `Departments` tables can even be merged:

```sql
CREATE TABLE DeptMgr (
    did    INTEGER PRIMARY KEY,
    dname  CHAR(20),
    budget REAL,
    ssn    CHAR(11),     -- manager's SSN (FK)
    since  DATE,
    FOREIGN KEY (ssn) REFERENCES Managers
);
```

### Weak Entity Sets → Combined Table

The weak entity set and its identifying relationship are merged into one table. The primary key is the combination of the owner's key and the weak entity's discriminator.

```sql
CREATE TABLE Transaction (
    TransNum  INTEGER,
    AccNum    INTEGER NOT NULL,
    Date      DATE,
    Amount    FLOAT,
    PRIMARY KEY (TransNum, AccNum),
    FOREIGN KEY (AccNum) REFERENCES Account ON DELETE CASCADE
);
```

### Subclasses → Three Strategies

| Strategy | Implementation | When to Use |
|----------|---------------|-------------|
| **ER style** | Superclass table + subclass tables with FK to superclass | When subclasses have many distinct attributes |
| **Object-oriented** | One table per subclass, each containing all inherited attributes | When queries typically access one subclass |
| **Single table with NULLs** | One table for the whole hierarchy; NULL for unused subclass columns | When queries frequently span the whole hierarchy |

---

## ER Design Decisions

**Entity vs attribute?**
An "object" should be an entity if it has its own properties of interest beyond what the host entity needs.

**Entity vs relationship?**
Use a relationship to describe an *action* or *association* between entities.

**Where to place relationship attributes?**
Relationship attributes belong on the relationship if they describe the *association*, not the entities themselves.

**N-ary vs multiple binary relationships?**
Prefer binary relationships — ternary relationships are harder to constrain and reason about.

---

## ER Design Process Summary

```
Requirements (S1)
    │ identify entities, attributes, and relationships
    ▼
ER Diagram (S2)
    │ translate to relational schemas
    ▼
Logical Schema (S3): tables with primary/foreign keys
    │ normalise
    ▼
Refined Schema (S4): BCNF-compliant tables
```

---

## See Also

- [[concepts/relational-database-fundamentals]] — Keys, integrity constraints, relational model
- [[concepts/database-normalisation]] — Stage S4: refining the logical schema produced by ER translation
- [[concepts/relational-algebra-and-sql]] — SQL that implements and queries the resulting schema
- [[sources/INF2003-database-systems]] — Source course
