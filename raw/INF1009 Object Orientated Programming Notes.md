---
type: source
folder: wiki/sources
title: INF1009 Object Orientated Programming Notes
course: INF1009
status: ingested
updated: 2026-05-09
tags:
  - source
  - oop
  - java
  - inf1009
related:
  - oop-fundamentals
  - oop-encapsulation
  - oop-inheritance
  - oop-polymorphism
  - oop-abstraction-interfaces
  - oop-relationships
  - solid-principles
  - uml-class-diagrams
  - oop-design-patterns
  - oop-generics
  - oop-error-handling
---

# INF1009 Object-Oriented Programming Notes

> Singapore Institute of Technology (SIT)
> **Lecturers:** Dr. Nisha Jain (Weeks 1–6) | Dr. Oran Zane Devilly (Weeks 8–13)
> **Language:** Java (primary), C++ (introduced in Week 10)

### Course Learning Outcomes

1. Develop a clear *understanding* of OOP concepts: classes, objects, abstraction, inheritance, encapsulation, polymorphism
2. *Apply* good programming practices when developing OOP applications
3. *Develop* basic OOP applications in industry standard languages such as Java and C++
4. *Apply* appropriate APIs in industry standard languages in OOP application development
5. *Apply* basic test-first programming

### Assessment (Tentative)

| Component | Weight |
|-----------|--------|
| Labs | 10% |
| Quiz 1 | 20% |
| Quiz 2 | 20% |
| Project (Prototype 20% + Final 30%) | 50% |

> **No exam!**

### Course Schedule

| Week | Topic |
|------|-------|
| 1 | OOP Fundamentals |
| 2 | Class, Object and Encapsulation |
| 3 | Inheritance and Polymorphism |
| 4 | Generics / Templates / Cloning |
| 5 | Testing and Exception Handling |
| 8 | Project / Code Organisation (Game Engine) |
| 9 | Software Design Patterns (Game Engine) |
| 10 | Problem Solving for Context (Develop Actual Game) |
| 11 | Transferable Skills — C, C++, Java and beyond |
| 12 | Consultation (Project Part 2 due) |

---

## Table of Contents

1. [Building Blocks of OOP](#1-building-blocks-of-oop)
2. [UML and SOLID Principles](#2-uml-and-solid-principles)
3. [Implementing Encapsulation](#3-implementing-encapsulation)
4. [Polymorphism](#4-polymorphism)
5. [Encapsulation (Deep Dive)](#5-encapsulation-deep-dive)
6. [Inheritance](#6-inheritance)
7. [Abstraction](#7-abstraction)
8. [Interfaces](#8-interfaces)
9. [Relationships in OOP](#9-relationships-in-oop)
10. [Assignment and Cloning](#10-assignment-and-cloning)
11. [Error Handling](#11-error-handling)
12. [Generic Programming](#12-generic-programming)
13. [Inheritance: Additional Concepts](#13-inheritance-additional-concepts-lec-3-extended)
14. [Static Keyword and `this`](#14-static-keyword-and-this-lec-2-extended)
15. [Code Organisation and Packages](#15-code-organisation-and-packages-lec-8--dr-oran-devilly)
16. [Design Patterns: Singleton, Factory, Abstract Factory](#16-design-patterns-singleton-factory-abstract-factory-lec-9)
17. [C, C++, Java and Beyond](#17-c-c-java-and-beyond-lec-10)

---

## 1. Building Blocks of OOP

### Recap: Why OOP?

Procedural programming focuses more on **procedure than data**, leading to:
- Top-down approach
- Lack of modularity and reusability of code
- Data security issues

OOP uses **simple concepts** to represent **complex problems**.

### What is a Class?

A **Class** is a template definition of the methods and properties of one particular kind of object in the real world.

- A class groups together **Properties** (data/attributes) and **Methods** (functions/behaviours)
- Think of it as a **blueprint**

**Example — Car class:**

```
Car
├── Properties: make, model, color, year, price
└── Methods:    start(), stop(), move()
```

**Example — Cat class:**

```
Cat
├── Properties: color, eyeColor, height, weight
└── Methods:    sit(), laydown()
```

**Java code:**

```java
class Cat {
    // class properties
    String color;
    String eyeColor;
    int height;
    int weight;

    // class methods
    void sit() {
        // implementation
    }
    void laydown() {
        // implementation
    }
}
```

### What is an Object?

- An object is **created from the class**
- It is a **specific instance** of a class
- It contains **real values** instead of variables
- One class can have **multiple objects** (multiple instances)

**Example — Cat Object "Bella":**

```
Cat Object Bella
├── color: Yellow
├── eyeColor: Black
├── height: 12
├── weight: 15
├── sit()
└── laydown()
```

**Java code:**

```java
class Cat { /* ... */ }

public class TestCat {
    public static void main(String args[]) {
        Cat Bella = new Cat("Yellow", "Black", 12, 15);
        Bella.sit();
    }
}
```

### The 4 Pillars of OOP

| Pillar | Description |
|--------|-------------|
| **Encapsulation** | Bundling data and methods, hiding internal state |
| **Inheritance** | Deriving new classes from existing ones |
| **Polymorphism** | Many forms — same name, different behaviour |
| **Abstraction** | Hiding complexity, showing only essentials |

### Summary

- **Class**: A template definition of the methods and properties of one particular kind of object in the real world.
- **Object**: Created from the class; contains real values instead of variables.
- One class can have **multiple objects**.
- Encapsulation, Inheritance, Polymorphism, and Abstraction are the **4 pillars** of OOP.

---

## 2. UML and SOLID Principles

### UML: Unified Modeling Language

- UML is **not textual** — it is a **graphical notation**
- Provides a **set of diagrams** to model software systems
- Key diagram types:
  - Use Case Diagram
  - **Class Diagram** ← most commonly used in OOP
  - Sequence Diagram
  - Activity Diagram
  - State Machine Diagram
  - Component Diagram
  - Deployment Diagram

### Class Diagram Structure

A UML class box has three sections:

```
┌────────────────────┐
│      ClassName     │  ← Name
├────────────────────┤
│  - attribute: Type │  ← Attribute(s)  (- = private)
├────────────────────┤
│  + method(): Type  │  ← Operation(s)  (+ = public)
└────────────────────┘
```

**Without signatures:**
```
Circle
- radius
+ getArea()
+ getPerimeter()
+ setRadius(double)
```

**With signatures:**
```
Circle
- radius : double
+ getArea() : double
+ getPerimeter() : double
+ setRadius(double) : void
```

**Example — Cat class UML:**
```
Cat
- color : String
- eyeColor : String
- height : double
- weight : double
+ Sit() : void
+ LayDown() : void
```

### Relationships in UML

- **Association** — general relationship between classes
- **Aggregation** — "has-a" relationship (weak ownership)
- **Composition** — "has-a" with strong ownership (lifecycle dependency)
- **Inheritance** — "is-a" relationship
- **Dependency** — one class uses another
- **Interface** — contract implementation

### SOLID Principles

SOLID is a set of 5 design principles to write maintainable, scalable software:

| Letter | Principle | Meaning |
|--------|-----------|---------|
| **S** | Single Responsibility Principle | A class has only one responsibility; only one reason to change |
| **O** | Open-Closed Principle | Open for extension, closed for modification |
| **L** | Liskov Substitution Principle | Subtypes must be substitutable for their base types |
| **I** | Interface Segregation Principle | No client should be forced to depend on methods it does not use |
| **D** | Dependency Inversion Principle | Depend on abstractions, not concretions |

#### Single Responsibility Principle (SRP)

> A class has **a single responsibility** and only **one reason to change**.

**Bad example:** A `BankAccount` class with `deposit()`, `withdraw()`, AND `sendNotifications()` — this has multiple responsibilities and violates SRP.

**Fix:** Separate the notification logic into its own class (e.g., `NotificationService`).

#### Open-Closed Principle (OCP)

> Software entities should be **open for extension** but **closed for modification**. Classes should be easily extendable.

**Example:** An eCommerce system supporting PayPal, Stripe, and Braintree. New payment gateways can be added by implementing the payment interface, without modifying existing payment-handling code.

### Summary

- **UML**: Graphical modeling language with a range of diagrams and notations for relationships between classes.
- **SOLID**: 5 design principles — SRP and OCP introduced here; LSP, ISP, DIP to follow.

---

## 3. Implementing Encapsulation

### Encapsulation = Data Hiding

Encapsulation means bundling data (attributes) and methods within a class, and controlling access through a public interface.

```
Object
├── Public Methods      ←→   Interaction Interface (outside world)
└── Private Data
    Private Methods
```

> *"Don't ask how I do it, but this is what I can do"* — The encapsulated object
>
> *"I don't care how, just do your job, and I'll do mine"* — One encapsulated object to another

### Implementing Encapsulation: Three Tools

1. **Access Modifiers**
2. **Getters and Setters**
3. **Constructors**

### Access Modifiers

| Modifier | Access Scope |
|----------|-------------|
| `private` | Only within the class itself |
| `protected` | Within the package and all subclasses |
| `public` | All classes can access |

### Setters

**Setters** are methods that **only alter** the state of an object by changing values of the class's attributes.

```java
class Time {
    private int hour;

    public void setHour(int h) {
        hour = h;
    }
}
```

### Getters

**Getters** are methods that **only return** the state of an object by returning the values of the class's attributes.

```java
class Time {
    private int hour;

    public int getHour() {
        return hour;
    }
}
```

### Constructors

- **Special functions** used to **initialize objects**
- Constructor name **must match class name**
- Constructors have **no return type** (no `void`, no `static`)
- Called when an object of a class is created using the `new` keyword
- Useful for setting **initial values** of attributes

#### Types of Constructors

```
Constructors
├── Default Constructor      — no parameters; initializes to default values
└── Parameterized Constructor — requires arguments; initializes to given values
```

```java
// Default constructor
Time() {
    hour = 5;
    minutes = 15;
}

// Parameterized constructor (1 param)
Time(int h) {
    hour = h;
}

// Parameterized constructor (2 params)
Time(int h, int m) {
    hour = h;
    minutes = m;
}
```

#### Multiple Constructors (Constructor Overloading)

- Provides different ways to initialize objects based on varying scenarios
- Each constructor has a **unique set of parameters**
- Shares the same name but differs in parameter list
- Provides **flexibility**

```java
// Using constructors:
Time t1 = new Time();       // default
Time t2 = new Time(5);      // parameterized (1 arg)
Time t3 = new Time(5, 15);  // parameterized (2 args)
```

### Summary

- **Encapsulation**: Bundles data and methods together within a class.
- **Control access to data**: via public getter and setter methods.
- **Constructors**: Customise the initialization process using default and parameterized forms.
- Good programming practice: enforce encapsulated classes.

---

## 4. Polymorphism

### What is Polymorphism?

**Poly** = many, **morphism** = form

> Polymorphism is the **ability of objects to take on different forms or exhibit different behaviours** based on the context.

> More concisely: **a way of allowing similar operations to be grouped together under the same name**.

**Example:** The `speak()` method produces different results depending on which animal calls it:
- Dog → "Woof"
- Cat → "Meow"
- Cow → "Moo"

### Two Types of Polymorphism

```
Polymorphism
├── Method Overloading  — same name, different parameters (same class)
└── Method Overriding   — subclass provides its own implementation of a parent method
```

### Method Overloading

Allows a class to have **more than one method with the same name**, provided their **argument lists are different**.

```java
class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }
}

// Usage:
Calculator calculator = new Calculator();
int sum1 = calculator.add(5, 10);    // calls 2-param version
int sum2 = calculator.add(1, 2, 3); // calls 3-param version
```

### Method Overriding

Allows a **subclass to provide its own implementation** of a method defined in its **superclass**.

**UML example:**
```
           Animal
    - color: String
    - age: int
    - name: String
    + speak(): void
        ↑         ↑      ↑       ↑
      Dog       Cat    Duck    Pig
  +speak():void  etc.
```

Each subclass (Dog, Cat, Duck, Pig) overrides `speak()` with its own implementation.

### Summary

- **Polymorphism**: the actual type of an object can be different from the type it is declared as.
- **Method overloading**: multiple methods with the **same name** in the **same class**, but with **different signatures** (compile-time polymorphism).
- **Method overriding**: two methods — one in a **parent** class and one in a **child** class — with the **same signature** (runtime polymorphism).

---

## 5. Encapsulation (Deep Dive)

### What is Encapsulation?

Encapsulation is the mechanism of wrapping data (attributes) and code acting on the data (methods) together as a single unit. It restricts direct access to some components.

Key ideas:
- **Data hiding**: internal state is hidden from the outside
- External code interacts only through **public methods**
- Protects data **integrity**

### Benefits

- Improved **data security**
- Better **maintainability** — internal implementation can change without affecting users
- **Modularity** — each class is self-contained
- Easier **debugging**

### Access Modifiers (Revisited)

```
private    → only within the class
(default)  → within the same package
protected  → within the package + subclasses
public     → everywhere
```

---

## 6. Inheritance

### What is Inheritance?

> Inheritance is when a class **reuses the properties and behaviours** of another class or specifies new implementation.

- **Derive** a new class from an existing one
- Allows classes to **use** properties and behaviours from other classes
- Enables the creation of a **hierarchy of classes**

**Example — Clothing Store:**
```
       ClothingItem
      (brand, size, color)
         ↑         ↑
       Shirt      Pants
  (sleeveLength, (waistSize,
   collarType)   inSeamLength)
```

Both `Shirt` and `Pants` **inherit** `brand`, `size`, and `color` from `ClothingItem`.

### Syntax: `extends` Keyword

```java
class Vehicle {
    private int wheels;

    Vehicle() {
        wheels = 4;
    }

    Vehicle(int wheels) {
        this.wheels = wheels;
    }

    public int getWheels() { return wheels; }
    public void setWheels(int wheels) { this.wheels = wheels; }
    public void print() {
        System.out.println("Wheels: " + wheels);
    }
}

class Car extends Vehicle {
    public String color;

    Car() {
        super();       // calls parent constructor
        color = "red";
    }

    Car(String color) {
        this.color = color;
    }

    Car(String color, int wheels) {
        super(wheels);          // calls Vehicle(int wheels)
        this.color = color;
    }

    public void displayParentInfo() {
        super.print();                  // calls parent method
        int a = super.getWheels();
    }
}
```

### Inheritance and Constructors

- Constructors are **not inherited**, even if they have public visibility
- **Parent's constructor** is used to set up the "parent's part" of the object
- The **first line** of a child's constructor should use `super()` to call the parent's constructor

### Inheritance and Visibility

| Modifier | Inherited? | Accessible in subclass? |
|----------|-----------|------------------------|
| `public` | Yes | Yes |
| `protected` | Yes | Yes |
| `private` | No (not inherited directly) | No (must use getters/setters) |

### Summary

- Derive a new class from an existing one, allowing classes to inherit properties and behaviours.
- Can extend the base class functionality by adding new methods or fields.
- Enables a **hierarchy of classes**.
- Constructors are **not inherited** but are implicitly called.
- Use access modifiers to control the level of visibility.

---

## 7. Abstraction

### What is Abstraction?

> Abstraction is the process of **hiding complex, low-level details** with a simpler, high-level layer — showing only essential information to the user.

- Lets you use objects in a way that hides the details you don't need to know
- Makes it easier to work with complex systems
- Allows you to focus on the **important aspects** of your code

### Abstract Classes

- A class whose **object cannot be created** (cannot be instantiated)
- It can **only be inherited**
- Serves as a **blueprint or template** for creating concrete (non-abstract) subclasses

```java
abstract class Shape {
    abstract void draw();  // abstract method — no body
    void display() {
        System.out.println("Displaying shape");
    }
}
```

### Abstract Methods

- Methods whose **signature has been provided, but no implementation** is given
- A method without a meaningful or complete implementation

```java
abstract void setInfo();
```

- Subclasses **must provide implementations** for all abstract methods.

### Example

```java
abstract class Animal {
    abstract void sound();
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Woof");
    }
}
```

### Summary

- **Abstraction**: hides details, exposes only essentials.
- **Abstract Classes**: cannot be instantiated directly; serve as blueprints.
- **Abstract Methods**: declared without a method body; subclasses must implement them.

---

## 8. Interfaces

### Recap: Abstraction

- Hiding complex details with a simpler high-level layer.
- Showing only essential information to the user.

### The Problem: Multiple Inheritance

Java does not support multiple class inheritance. An interface solves the "multiple roles" problem.

**Example:** A `TeachingAssistant` is both a `Teacher` AND a `Student` — it cannot extend both classes simultaneously. Instead, both `Teacher` and `Student` become **interfaces**.

### What is an Interface?

> An interface is a way through which **unrelated objects interact** with one another.

- A **blueprint for a group of related methods** that a class must implement
- Allows unrelated classes to work together by providing a **common set of methods**
- Achieves **abstraction and polymorphism**
- Uses the `implements` keyword

### Interface Syntax

```java
// Teacher interface
public interface Teacher {
    void teach();
}

// Student interface
public interface Student {
    void study();
}

// TeachingAssistant implements both
public class TeachingAssistant implements Teacher, Student {
    String name;
    String subject;

    @Override
    public void teach() {
        System.out.println(name + " (Teaching Assistant) is assisting in teaching " + subject);
    }

    @Override
    public void study() {
        System.out.println(name + " (Teaching Assistant) is also studying.");
    }
}
```

### Interface vs Abstract Class

| Feature | Abstract Class | Interface |
|---------|----------------|-----------|
| Instantiation | Cannot be instantiated | Cannot be instantiated |
| Methods | Can have concrete + abstract methods | All methods abstract (by default) |
| Variables | Can have instance variables | Only `public static final` constants |
| Inheritance | `extends` (single) | `implements` (multiple allowed) |
| Use case | "is-a" relationship | "can-do" / contract |

### Summary

- An interface is a **blueprint** for a group of related methods that a class must implement.
- Interfaces allow unrelated classes to work together via a **common set of methods**.
- Allows achieving **abstraction and polymorphism**.
- A class can implement **multiple interfaces** (unlike class inheritance in Java).

---

## 9. Relationships in OOP

### Types of Relationships

| Relationship | Symbol (UML) | Meaning |
|-------------|-------------|---------|
| **Association** | → | General relationship; "uses" |
| **Aggregation** | ◇→ | "Has-a" (weak); parts can exist independently |
| **Composition** | ◆→ | "Has-a" (strong); parts cannot exist independently |
| **Inheritance** | ▷ | "Is-a" relationship |
| **Dependency** | - - → | One class depends on another temporarily |
| **Interface** | - - ▷ | Implementation of an interface |

### Association

A general relationship between classes where one class uses another.

```java
class Student {
    private Course course;  // association: Student uses Course
}
```

### Aggregation (Weak "Has-a")

A "whole-part" relationship where the part can exist independently of the whole.

```
Department ◇——— Employee
```
An Employee can exist without a Department.

### Composition (Strong "Has-a")

A "whole-part" relationship where the part **cannot exist** independently.

```
House ◆——— Room
```
A Room cannot exist without a House.

### Key Distinctions

- **Aggregation**: weak ownership — *"has a"* but the child can live on its own.
- **Composition**: strong ownership — *"owns a"* and the child dies with the parent.

---

## 10. Assignment and Cloning

### Assignment of Variables

Variables in Java are assigned in two ways:

```
Assignment of Variables
├── Primitive / Value types   (int, double, char, boolean, etc.)
└── Reference / Object types  (objects, arrays)
```

**Primitive assignment** — copies the actual value:
```java
int a = 5;
int b = a;  // b gets a COPY of 5; changing b does not affect a
b = 10;     // a is still 5
```

**Reference assignment** — copies the reference (pointer), NOT the object:
```java
Cat c1 = new Cat("Yellow", "Black", 12, 15);
Cat c2 = c1;  // c2 points to the SAME object as c1
c2.color = "Red";  // c1.color is now also "Red"!
```

### Cloning

Cloning creates a **new object** that is a copy of an existing object.

- Initialises all its fields with **exactly the contents** of the corresponding fields of the original object.
- The class must implement the `Cloneable` interface and provide a `clone()` method.

```java
class Employee implements Cloneable {
    private int employeeId;
    private String employeeName;
    Department department;

    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}

// Usage:
Employee original = new Employee(1, "Admin", dept);
Employee cloned = (Employee) original.clone();
```

### Shallow vs Deep Copy

**Shallow Copy** — copies primitive fields by value, but reference fields point to the **same object**:
```java
// If cloned.department changes, original.department also changes
cloned.department.departmentName = "Finance";
// Both original and cloned now show Department: Finance
```

**Deep Copy** — creates new copies of **all** referenced objects as well, so changes to the clone don't affect the original.

| | Shallow Copy | Deep Copy |
|-|-------------|-----------|
| Primitive fields | Copied by value ✓ | Copied by value ✓ |
| Reference fields | Same reference (shared) | New objects created (independent) |

---

## 11. Error Handling

### What is Testing?

> Testing is a systematic process of evaluating a software application to **identify defects, bugs, or discrepancies** between expected and actual outcomes.

### Types of Errors

- **Syntax errors** — caught at compile time (e.g., missing semicolons)
- **Logic errors** — program runs but gives wrong output
- **Runtime errors** — program crashes during execution (e.g., dividing by zero, null pointer)

### What is an Exception?

An **exception** is an **unexpected event** that occurs during execution of a program that disrupts the normal flow.

### What is Exception Handling?

> Exception handling is a **mechanism in programming** that allows developers to handle and manage errors or exceptional situations that may occur during the execution of a program.

- Instead of allowing exceptions to **crash the program**, it provides a **structured approach** to deal with such situations.
- Need something to **detect** and **handle** exceptions.

### Design of an Exception Handler: try-catch-finally

```java
try {
    // Code that is suspect — might throw an exception
    // Put in try block
} catch (ExceptionType1 e1) {
    // Code to handle the exception
    // What to do after the exception occurs
} finally {
    // Optional block
    // Always executes — whether or not an exception was thrown
}
```

**Key points:**
- Code that might throw → put in `try` block
- Code to handle the exception → put in `catch` block
- `finally` block always runs regardless of try/catch result

### Common Exception Types

| Exception | Cause |
|-----------|-------|
| `ArithmeticException` | Division by zero |
| `NullPointerException` | Accessing a null object |
| `ArrayIndexOutOfBoundsException` | Invalid array index |
| `NumberFormatException` | Invalid string-to-number conversion |
| `ClassCastException` | Invalid type casting |

### Throwing Custom Exceptions

```java
class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

class BankAccount {
    private double balance;

    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException("Not enough funds!");
        }
        balance -= amount;
    }
}
```

---

## 12. Generic Programming

### What is Generic Programming?

> Generic programming is a **programming paradigm** that allows developers to create **flexible and reusable algorithms and data structures** by using **placeholders for types**.

**Why do we need it?** Without generics, you'd need separate `addInt()` and `addFloat()` methods for every type. With generics, one method/class handles all types.

### Components of Generic Programming

- **Type Parameter** — placeholder for a specific data type (`<T>` or `<E>`)
- **Generic Class** — a single class that can handle multiple data types
- **Generic Methods** — methods that work with any type
- **Wild Cards** — `<?>` for unknown types

### Generic Class Syntax

```java
public class MyClass<T> {
    // Class implementation with type parameter T
    private T data;

    public void setData(T data) {
        this.data = data;
    }

    public T getData() {
        return data;
    }
}

// Usage:
MyClass<Integer> intObj = new MyClass<>();
intObj.setData(42);

MyClass<String> strObj = new MyClass<>();
strObj.setData("Hello");
```

### Generic Methods

```java
public <T> void printArray(T[] array) {
    for (T element : array) {
        System.out.print(element + " ");
    }
}
```

### Wild Cards

- `<?>` — unknown type (read-only)
- `<? extends T>` — upper bounded wildcard (T or subtype)
- `<? super T>` — lower bounded wildcard (T or supertype)

### Benefits of Generic Programming

- **Type safety** — errors caught at compile time
- **Code reusability** — one implementation works for any type
- **Eliminates casting** — no need for explicit type casts
- **Cleaner code** — fewer method duplications

---

## 13. Inheritance: Additional Concepts (Lec 3 Extended)

### Overriding Methods — Rules

- `private`, `static`, and `final` methods **cannot** be overridden (they are local to the class)
- Static methods can be **re-declared** in the subclass (not the same as overriding)
- Binding of overridden methods happens at **runtime** — known as **dynamic binding**
- The `super` keyword is used for calling the parent class method or constructor

### Dynamic Binding

Dynamic binding (runtime polymorphism) means the JVM decides at runtime which overridden method to call, based on the **actual type** of the object, not the declared type.

```java
Animal a = new Dog();  // declared as Animal, actual type is Dog
a.speak();             // calls Dog's speak(), not Animal's speak()
```

### Type Assignment and Polymorphism

A parent class reference can point to a child class object:

```java
Person p = new Student();  // valid — Student IS-A Person
```

But a child class reference **cannot** point to a parent object:

```java
Student s = new Person();  // INVALID — compile error
```

The reference only knows what the declared type knows — a `Person` reference can only access `Person` fields/methods, even if the object is a `Student`.

### The `instanceof` Operator

Used to check if an object is an instance of a specific class:

```java
if (a instanceof Dog) {
    Dog d = (Dog) a;  // safe to cast
    d.fetch();
}
```

---

## 14. Static Keyword and `this` (Lec 2 Extended)

### `static` Keyword

`static` means there is **one copy for the class and all instances** (applies to both fields and methods).

| Type | Instance | Static |
|------|---------|--------|
| Belongs to | Each object | The class itself |
| Access | `objectName.field` | `ClassName.field` |
| Memory | Per object | Shared, single copy |

```java
class Counter {
    private static int count = 0;   // shared across ALL objects

    public Counter() {
        count++;                    // increments for every new object
    }

    public static int getCount() {
        return count;
    }
}

// Usage:
Counter c1 = new Counter();
Counter c2 = new Counter();
System.out.println(Counter.getCount()); // 2
```

### `this` Keyword

`this` refers to the **current object instance**. Common uses:

**1. Disambiguate field from parameter:**

```java
class Person {
    private String name;

    public Person(String name) {
        this.name = name;  // this.name = field; name = constructor parameter
    }
}
```

**2. Call another constructor in the same class:**

```java
class Time {
    private int hour, minute;

    Time() {
        this(0, 0);         // calls Time(int, int)
    }

    Time(int hour, int minute) {
        this.hour = hour;
        this.minute = minute;
    }
}
```

### Why Need Encapsulation?

- Combines data and how it's manipulated **in one place**
- Achieved through the **state** (private fields) and **behaviours** (public methods) of an object
- Only allows the state to be accessed and modified through behaviours
- Values within an object's state can then be **strictly controlled**

---

## 15. Code Organisation and Packages (Lec 8 — Dr. Oran Devilly)

### Game vs Game Engine

The course project applies OOP in a **game development context**:

- **Game Engine** = abstract, reusable framework (engine is abstract!)
- **Game** = concrete implementation that uses the engine (game is concrete!)
- The game engine hides core code, provides scripting for interaction, and abstracts functionality to usable controls

### Java Packages

A **package** is a grouping mechanism for organising related classes — think of it as a folder/directory for your code.

**Why use packages?**
- Organise code into logical **components**
- Avoid naming conflicts (namespace management)
- Control access between classes

**Creating a package in Java:**

```java
package myGame.entities;  // declares this file belongs to the package

import myGame.engine.Renderer;  // import from another package
```

**Creating packages in Eclipse:** Right-click project → New → Package

- Classes dragged into a package automatically get the package name assigned
- Classes using a packaged class automatically get the import added

### Software Engineering Terminology

**Patterns** — reusable solutions to commonly occurring problems in software development. Two key categories:

- **Software Design Patterns** — solve recurring code-level design problems
- **Software Architecture Patterns** — solve system-level structural problems

These are tried-and-tested approaches which tend to work best for given scenarios.

### The 23 Design Patterns (GoF)

Design patterns can be broken into **3 types**:

```
Design Patterns
├── Creational (1–5)
│   1. Singleton
│   2. Factory
│   3. Abstract Factory
│   4. Builder
│   5. Prototype
├── Structural (6–12)
│   6. Adapter
│   7. Composite
│   8. Proxy
│   9. Fly Weight
│   10. Facade
│   11. Bridge
│   12. Decorator
└── Behavioural (13–23)
    13. Template Method
    14. Mediator
    15. Chain of Responsibility
    16. Observer
    17. Strategy
    18. Command
    19. State
    20. Visitor
    21. Iterator
    22. Interpreter
    23. Memento
```

---

## 16. Design Patterns: Singleton, Factory, Abstract Factory (Lec 9)

### Good Coding Expectations

Code should be: **SOLID, Readable, Reusable, Scalable, Extensible, Graceful, Testable**

### Singleton Pattern (Creational)

> Ensures that **only one instance** of an object is created, and provides a **global access point** to that object.

Use when multiple instances of said object would lead to unstable code (e.g., a game manager, audio system, config loader).

**UML:**
```
SingletonPatternDemo
+ main(): void
       ↓ asks
   SingleObject
   - instance: SingleObject
   - SingleObject()
   + getInstance(): SingleObject
   + showMessage(): void
```

**Java implementation:**

```java
class SingleObject {
    // private static instance — only one ever exists
    private static SingleObject instance;

    // private constructor — cannot be called from outside
    private SingleObject() {}

    // public accessor
    public static SingleObject getInstance() {
        if (instance == null) {
            instance = new SingleObject();
        }
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello from Singleton!");
    }
}

// Usage:
SingleObject obj = SingleObject.getInstance();
obj.showMessage();
```

### Factory Pattern (Creational)

> Creates objects without specifying the exact class. Delegates the instantiation to subclasses.

**Why use Factory?** Without a factory, your main `Game` class would need to know about and directly create every type of entity (Player, Enemy, Bullet, Wall, Tree). This creates tight coupling. A factory decouples creation from usage.

Benefits:
- **Single Responsibility Principle** is met
- **Open/Closed Principle** is met (add new types without modifying existing code)

```java
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    @Override
    void draw() { System.out.println("Drawing Circle"); }
}

class Rectangle extends Shape {
    @Override
    void draw() { System.out.println("Drawing Rectangle"); }
}

// Factory class
class ShapeFactory {
    public Shape getShape(String type) {
        if (type.equals("CIRCLE")) return new Circle();
        if (type.equals("RECTANGLE")) return new Rectangle();
        return null;
    }
}

// Usage — the caller doesn't know which class it's getting:
ShapeFactory factory = new ShapeFactory();
Shape s = factory.getShape("CIRCLE");
s.draw();
```

### Abstract Factory Pattern (Creational)

> A factory **of factories** — creates families of related objects.

Helps code become more **loosely coupled**. Imagine a game that supports multiple themes (sci-fi, fantasy) — the Abstract Factory creates all entities in a consistent theme without the caller knowing which theme is active.

```java
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

class WindowsFactory implements GUIFactory {
    public Button createButton() { return new WindowsButton(); }
    public Checkbox createCheckbox() { return new WindowsCheckbox(); }
}

class MacFactory implements GUIFactory {
    public Button createButton() { return new MacButton(); }
    public Checkbox createCheckbox() { return new MacCheckbox(); }
}
```

### Components and Layers

One common approach to **software architecture** is **layering** based on functionality:

- A **layer** groups related functionality at the same level of abstraction
- A layer can have **many components**
- Components are grouped based on **shared functionality** (like entities)

**Typical game engine layers:**
```
Game Specific Subsystems (top)
├── Front-end / Animation / Human Interface Devices
├── Visual Effects / Scene Graph / Audio / Networking
├── Renderer / Collision and Physics
├── Resource Management and Game Assets
├── Core Support and Utility Systems
├── Platform Independence Layer
├── SDKs / Drivers / OS
└── Hardware (bottom)
```

### Object (Entity) Management

In a game, you need to **keep track of many entities all at once** — hundreds of enemies, thousands of bullets, UI elements, and multiplayer objects.

**Solution: Use `ArrayList` to manage collections of objects**

```java
import java.util.ArrayList;

ArrayList<Enemy> enemies = new ArrayList<>();

// Add entities
enemies.add(new Enemy("Goblin", 50));
enemies.add(new Enemy("Orc", 120));

// Update all
for (Enemy e : enemies) {
    e.update();
}

// Remove dead enemies
enemies.removeIf(e -> e.isDead());

// Get count
System.out.println("Enemies remaining: " + enemies.size());
```

**Using an iterator to safely remove during iteration:**

```java
Iterator<Enemy> it = enemies.iterator();
while (it.hasNext()) {
    Enemy e = it.next();
    if (e.isOffScreen()) {
        it.remove();  // safe removal during iteration
    }
}
```

---

## 17. C, C++, Java and Beyond (Lec 10)

### Transferable Programming Concepts

Good code in any language should be: **SOLID, Readable, Reusable, Scalable, Extensible, Graceful, Testable**

**Tips for transitioning between programming languages:**
- "Hello World" is always a great place to start — start simple, get the basics right, build confidence
- Focus on what you **DO** know first
- Then figure out what you **don't** know — mainly just syntax differences
- Choose languages based on **fit for purpose**, not just familiarity
- You'll never know every programming language forever — being able to switch is really important, because they're all the same at heart

### History of C++

| Year | Event |
|------|-------|
| 1972 | C created by Dennis Ritchie at Bell Labs for Unix development |
| 1979 | Bjarne Stroustrup began work on "C with Classes" (predecessor to C++) |
| 1982 | Stroustrup developed "C++" (++ being the increment operator in C) |
| 1985 | First edition of *The C++ Programming Language* released |
| 1998 | C++98 released — standardised the language |
| 2011 | C++11 released — added numerous new features |

**C++ is described as "a better C"** — it adds OOP capabilities while maintaining C's performance and system-level control.

### Java vs C++ Comparison

| Feature | Java | C++ |
|---------|------|-----|
| Memory management | Automatic (Garbage Collector) | Manual (`new`/`delete`) |
| Platform | JVM — write once run anywhere | Platform-specific compilation |
| Pointers | No explicit pointers | Explicit pointer support |
| Multiple inheritance | Via interfaces only | Full multiple inheritance |
| Header files | Not used | `.h` header files required |
| Output | `System.out.println()` | `cout << ` |
| Input | `Scanner` | `cin >> ` |
| String | `String` class | `#include <string>` |

### C++ Basics — Hello World

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    return 0;
}
```

### C++ Strings

```cpp
#include <iostream>
#include <string>  // Required for string class
using namespace std;

int main() {
    string firstName, lastName;
    firstName = "George";
    lastName  = "Washington";
    cout << firstName << " " << lastName << endl;

    // getline reads full line including spaces (cin stops at whitespace)
    string name;
    getline(cin, name);
    return 0;
}
```

### C++ I/O Stream Manipulators

```cpp
#include <iostream>
#include <iomanip>  // Required for setw
using namespace std;

int main() {
    int num1 = 2897, num2 = 5, num3 = 837;
    cout << setw(6) << num1 << setw(6) << num2 << setw(6) << num3 << endl;
    // Output:  2897     5   837
    return 0;
}
```
`setw(x)` prints in a field at least x spaces wide.

### Problem Solving in Context

**General Problem Solving process:**
1. Requirements Gathering (be clear about the requirements)
2. Know your audience (always think about "who am I building this for?")
3. Research your audience (don't make assumptions)
4. Design first:
   - Software Design
   - Problem Design
   - Problem Definition and Solution
   - Task Development
   - Task Assignment
   - Operationalization

---

## Quick Reference: Key Java Keywords

| Keyword | Purpose |
|---------|---------|
| `class` | Declares a class |
| `interface` | Declares an interface |
| `abstract` | Declares abstract class or method |
| `extends` | Inheritance (class extends another) |
| `implements` | Class implements an interface |
| `new` | Creates a new object |
| `this` | References current object |
| `super` | References parent class |
| `public` | Accessible everywhere |
| `private` | Accessible only within class |
| `protected` | Accessible within package + subclasses |
| `static` | Belongs to the class, not an instance |
| `final` | Cannot be changed / overridden |
| `void` | Method returns nothing |
| `return` | Returns a value from a method |
| `try` | Block of code to monitor for exceptions |
| `catch` | Handles exceptions |
| `finally` | Always runs after try-catch |
| `throw` | Throws an exception |
| `throws` | Declares possible exceptions in method signature |

---

## Access Modifiers Summary

| Modifier | Class | Package | Subclass | World |
|----------|-------|---------|----------|-------|
| `public` | ✓ | ✓ | ✓ | ✓ |
| `protected` | ✓ | ✓ | ✓ | ✗ |
| (default) | ✓ | ✓ | ✗ | ✗ |
| `private` | ✓ | ✗ | ✗ | ✗ |

---

## The 4 Pillars — One-Line Summaries

| Pillar | One-liner |
|--------|-----------|
| **Encapsulation** | Bundle data + methods; hide internals; control access via getters/setters |
| **Inheritance** | Child class reuses parent's properties/methods via `extends` |
| **Polymorphism** | Same method name, different behaviour (overloading = compile-time; overriding = runtime) |
| **Abstraction** | Hide complexity; expose only essentials via abstract classes and interfaces |

---

*Notes compiled from INF1009 lecture slides — SIT Internal*
