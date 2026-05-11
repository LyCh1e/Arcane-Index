---
type: concept
title: "SOLID Principles and Design Patterns"
domain: software-engineering
course: INF1009
complexity: high
tags: [solid, design-patterns, singleton, factory, abstract-factory, gof, creational, structural, behavioural]
updated: 2026-05-11
---

# SOLID Principles and Design Patterns

SOLID is a set of five object-oriented design principles that, when followed together, produce code that is easy to maintain, extend, and test. The Gang-of-Four (GoF) design patterns are reusable solutions to recurring design problems — they are practical applications of SOLID and good OOP. Together, they form the professional vocabulary of software design.

## SOLID Principles

### S — Single Responsibility Principle (SRP)

> A class should have one, and only one, reason to change.

A "reason to change" corresponds to a **stakeholder or concern**. If a class handles both data persistence and email notification, two different teams can cause it to change — violating SRP.

**Violation example**: A `Report` class that generates report content AND formats it as PDF AND emails it.  
**Fix**: Split into `ReportGenerator`, `PdfFormatter`, `EmailSender`.

SRP reduces coupling — a change in email infrastructure doesn't risk breaking report generation logic.

### O — Open/Closed Principle (OCP)

> Software entities should be open for extension, but closed for modification.

Adding new functionality should not require modifying existing, tested code. Achieve this via **abstraction**: define an interface or abstract class; add new behaviour by implementing/extending, not by editing.

**Violation example**: A `DiscountCalculator` with a `switch` statement over customer types — adding a new type requires modifying the class.  
**Fix**: `Discount` interface with `calculate()` method; new discount types are new classes.

### L — Liskov Substitution Principle (LSP)

> Objects of a subclass should be substitutable for objects of its superclass without altering the correctness of the program.

If `S extends T`, then anywhere a `T` is expected, an `S` should work without surprises. Overriding methods must not:
- Strengthen preconditions (require more from the caller)
- Weaken postconditions (guarantee less to the caller)
- Throw new checked exceptions

**Classic violation**: `Square extends Rectangle`. Setting width of a Square also changes height (to maintain squareness) — but `Rectangle` callers don't expect this. Fix: don't inherit Square from Rectangle; make both implement a `Shape` interface.

### I — Interface Segregation Principle (ISP)

> No client should be forced to depend on methods it does not use.

Fat interfaces that cover unrelated operations force implementors to stub out irrelevant methods. Split fat interfaces into focused, client-specific ones.

**Violation**: `IWorker { work(); eat(); sleep(); }` — a Robot implements `IWorker` but must stub `eat()` and `sleep()`.  
**Fix**: `IWorkable { work(); }`, `IFeedable { eat(); }`, `IRestable { sleep(); }`.

### D — Dependency Inversion Principle (DIP)

> High-level modules should not depend on low-level modules. Both should depend on abstractions.

Depend on interfaces, not concrete implementations. This enables swapping implementations without changing the high-level policy.

**Violation**: `OrderService` directly instantiates `MySQLRepository`.  
**Fix**: `OrderService` depends on `IOrderRepository` interface; `MySQLRepository` and `MockRepository` both implement it.

DIP is the foundation of **Dependency Injection** — see [[kotlin-coroutines]] for Hilt's DI implementation.

## Design Patterns Overview

The Gang of Four (Gamma, Helm, Johnson, Vlissides) catalogued **23 patterns** across three categories:

| Category | Focus | Examples |
|----------|-------|---------|
| **Creational** | How objects are created | Singleton, Factory Method, Abstract Factory, Builder, Prototype |
| **Structural** | How objects are composed | Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy |
| **Behavioural** | How objects communicate | Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor |

## Creational Patterns (Deep Dives)

### Singleton Pattern

**Intent**: Ensure a class has exactly one instance and provide global access to it.

**Structure**:
- Private constructor (prevents external instantiation)
- Static field holding the single instance
- Static `getInstance()` method (creates on first call, returns existing on subsequent calls)

```java
public class ConfigManager {
    private static ConfigManager instance;

    private ConfigManager() {}  // prevent external instantiation

    public static ConfigManager getInstance() {
        if (instance == null) {
            instance = new ConfigManager();  // lazy initialisation
        }
        return instance;
    }
}
```

**Thread-safe Singleton** (double-checked locking):
```java
private static volatile ConfigManager instance;

public static ConfigManager getInstance() {
    if (instance == null) {
        synchronized (ConfigManager.class) {
            if (instance == null) {
                instance = new ConfigManager();
            }
        }
    }
    return instance;
}
```

**Use when**: Shared resource with exactly one logical instance (database connection pool, logger, application config, thread pool).

**Pitfalls**: Makes testing hard (global state); use DI frameworks to inject a singleton-scoped bean instead.

### Factory Method Pattern

**Intent**: Define an interface for creating objects, but let subclasses decide which class to instantiate. The Factory Method decouples object creation from usage.

**Structure**:
- `Creator` abstract class with `createProduct()` abstract factory method
- Concrete creators override `createProduct()` to return their specific product type
- `Product` interface implemented by all concrete products

```java
interface Notification { void send(String message); }
class EmailNotification implements Notification { ... }
class SMSNotification implements Notification { ... }

abstract class NotificationFactory {
    abstract Notification createNotification();
    void notify(String msg) { createNotification().send(msg); }
}

class EmailFactory extends NotificationFactory {
    Notification createNotification() { return new EmailNotification(); }
}
```

**Use when**: A class cannot anticipate the type of objects it needs to create; subclasses should control instantiation.

**OCP alignment**: New notification types → new factory subclass, no changes to existing code.

### Abstract Factory Pattern

**Intent**: Provide an interface for creating **families of related or dependent objects** without specifying concrete classes.

Where Factory Method creates one product, Abstract Factory creates a **suite of compatible products**.

```java
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

class WindowsFactory implements GUIFactory {
    Button createButton() { return new WindowsButton(); }
    Checkbox createCheckbox() { return new WindowsCheckbox(); }
}

class MacFactory implements GUIFactory {
    Button createButton() { return new MacButton(); }
    Checkbox createCheckbox() { return new MacCheckbox(); }
}
```

The client (`Application`) uses `GUIFactory` and never references `WindowsButton` or `MacButton` directly.

**Use when**: System must be independent of how its products are created; products must be used together as a family; you want to enforce consistency among related objects.

**Relationship**: Abstract Factory often uses Factory Methods internally to create individual products.

## Pattern Selection Guide

| Scenario | Pattern |
|----------|---------|
| Exactly one instance of a class | Singleton |
| Defer object creation to subclasses | Factory Method |
| Create families of related objects | Abstract Factory |
| Build complex object step-by-step | Builder |
| Copy existing objects | Prototype |
| Notify many objects of state change | Observer |
| Encapsulate a request as an object | Command |
| Define skeleton algorithm, defer steps | Template Method |
| Select algorithm at runtime | Strategy |

## See Also

- [[oop-four-pillars]] — the OOP foundation these patterns build on
- [[kotlin-coroutines]] — Hilt implements DIP via constructor injection
- [[android-architecture]] — Repository pattern is a form of Facade; ViewModel is an Observer
- [[INF1009-object-oriented-programming]] — source course
