---
type: concept
title: "OOP Four Pillars"
domain: software-engineering
course: INF1009
complexity: medium
tags: [oop, encapsulation, inheritance, polymorphism, abstraction, java, uml, relationships]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000008
---

# OOP Four Pillars

Object-Oriented Programming organises software around **objects** — bundles of state (fields) and behaviour (methods) — rather than around functions and logic. The four pillars are the conceptual foundation: every OOP language feature exists to implement, enforce, or extend one or more of them.

## Pillar 1: Encapsulation

**Encapsulation** is the bundling of data with the methods that operate on it, combined with **access control** that hides internal state from external code.

### Access Modifiers (Java)

| Modifier | Class | Package | Subclass | World |
|----------|-------|---------|----------|-------|
| `private` | Yes | No | No | No |
| (default) | Yes | Yes | No | No |
| `protected` | Yes | Yes | Yes | No |
| `public` | Yes | Yes | Yes | Yes |

C++ equivalents: `private`, `protected`, `public` (no package-private; friendship mechanism instead).

### Getters and Setters

Fields are typically `private`; access is controlled via public `getX()` and `setX()` methods. This allows:
- **Validation** in setters (reject illegal values)
- **Lazy initialisation** in getters
- **Read-only** properties (getter with no setter)
- **Future change** of internal representation without breaking external code

Encapsulation enforces the **information hiding** principle: callers depend on interface, not implementation.

## Pillar 2: Inheritance

**Inheritance** allows a subclass to acquire all fields and methods of its superclass, enabling code reuse and expressing IS-A relationships.

```java
class Animal {
    protected String name;
    public void eat() { System.out.println(name + " eats"); }
}

class Dog extends Animal {
    public void bark() { System.out.println(name + " barks"); }
}
```

### Key Rules

- `extends` keyword in Java; `:` in C++
- `super.method()` calls the parent's version of an overridden method
- `super()` in a constructor calls the parent constructor (must be first statement)
- Java uses **single inheritance** for classes (multiple via interfaces); C++ allows multiple inheritance
- A subclass IS-A superclass — `Dog` IS-AN `Animal`

### Constructor Inheritance

Constructors are not inherited. If the superclass has no no-arg constructor, the subclass must explicitly call `super(args)`. The compiler inserts an implicit `super()` call if none is present — this will fail if no no-arg constructor exists in the parent.

### Visibility Changes in Overriding

A subclass can **widen** access of an overridden method (e.g., `protected` → `public`) but cannot **narrow** it. This preserves Liskov Substitutability.

## Pillar 3: Polymorphism

**Polymorphism** means "many forms" — one interface, multiple implementations.

### Overloading (Compile-Time / Static)

Multiple methods with the **same name but different parameter signatures** in the same class. The compiler selects the correct version at compile time based on argument types.

```java
int add(int a, int b)        // add(2, 3) → this one
double add(double a, double b) // add(2.0, 3.0) → this one
```

### Overriding (Runtime / Dynamic)

A subclass provides its own implementation of a method already defined in the superclass. The JVM selects the correct version at **runtime** based on the actual object type — this is **dynamic dispatch** / **dynamic binding**.

```java
Animal a = new Dog();  // static type: Animal; dynamic type: Dog
a.eat();               // calls Dog.eat() if Dog overrides it — NOT Animal.eat()
```

Java uses virtual dispatch by default; C++ requires explicit `virtual` keyword. `@Override` annotation in Java is optional but recommended (catches typos).

### Covariant Return Types

Java allows an overriding method to return a subtype of the declared return type. C++ also supports this.

## Pillar 4: Abstraction

**Abstraction** hides implementation complexity behind a simplified interface. It answers "what does this do?" not "how does it do it?"

### Abstract Classes

- Declared with `abstract` keyword
- Can have **abstract methods** (signature only, no body) and **concrete methods**
- Cannot be instantiated directly — must be subclassed
- Subclass must implement all abstract methods (or also be declared abstract)

```java
abstract class Shape {
    abstract double area();           // must implement
    void describe() { System.out.println("I am a shape"); }  // concrete
}
```

### Interfaces

- All methods implicitly `public abstract` (pre-Java 8); default/static methods added in Java 8+
- Fields implicitly `public static final`
- A class can **implement** multiple interfaces (solving the multiple-inheritance problem)
- Interfaces define a **contract**: any class implementing it guarantees those methods exist

```java
interface Drawable { void draw(); }
interface Resizable { void resize(double factor); }
class Circle extends Shape implements Drawable, Resizable { ... }
```

### Interface vs Abstract Class

| Feature | Interface | Abstract Class |
|---------|-----------|---------------|
| Instantiation | No | No |
| Multiple inheritance | Yes (multiple implements) | No (single extends) |
| Constructor | No | Yes |
| Fields | `public static final` only | Any |
| Method bodies | Default/static only (Java 8+) | Yes |
| Use when | Defining a contract across unrelated classes | Sharing code among closely related classes |

## OOP Relationships

### Association

A uses B, but neither owns nor controls B's lifecycle. Weakest relationship.

> A student **uses** a library (both exist independently)

UML: plain directed arrow.

### Aggregation (HAS-A, loose)

A whole-part relationship where the part **can exist independently** of the whole.

> A department **has** professors (professors exist without the department)

UML: open diamond at the "whole" end.

```java
class Department {
    List<Professor> professors;  // Professor lives on without Department
}
```

### Composition (HAS-A, strong)

A whole-part relationship where the part **cannot exist independently** — it lives and dies with the whole.

> A house **has** rooms (a room without a house is meaningless)

UML: filled diamond at the "whole" end.

```java
class House {
    Room room = new Room();  // Room created inside House, dies with House
}
```

### Summary Table

| Relationship | Coupling | Part survives whole? | UML |
|-------------|---------|----------------------|-----|
| Association | Weak | N/A | Arrow |
| Aggregation | Medium | Yes | Open diamond |
| Composition | Strong | No | Filled diamond |
| Inheritance | Strong | N/A | Open triangle arrow |

## See Also

- [[solid-and-design-patterns]] — applying OOP principles at architecture scale
- [[INF1009-object-oriented-programming]] — source course
- [[android-architecture]] — Android architecture is deeply OOP (ViewModel, Repository pattern)
- [[ICT2113-software-modelling]] — UML class diagrams use OOP relationship notation
