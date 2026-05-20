---
type: concept
title: "SOLID Principles and Design Patterns"
domain: software-engineering
course: ICT2112
complexity: high
tags: [solid, design-patterns, singleton, factory, abstract-factory, builder, prototype, adapter, decorator, facade, composite, proxy, observer, strategy, command, template-method, state, gof, creational, structural, behavioural]
updated: 2026-05-12
status: established
created: 2026-05-12
address: c-000009
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

### Builder Pattern

**Intent**: Separate the **construction of a complex object** from its representation so that the same construction process can produce different representations.

**Structure**:
- **Director** — Drives the construction sequence using the Builder interface
- **Builder** — Abstract interface for creating parts of the Product
- **ConcreteBuilder** — Assembles parts; tracks the representation being built
- **Product** — The complex object being constructed

```csharp
public class MealBuilder {
    private Meal _meal = new Meal();

    public MealBuilder AddBurger(string type) {
        _meal.Burger = type;
        return this;  // fluent API
    }

    public MealBuilder AddDrink(string type) {
        _meal.Drink = type;
        return this;
    }

    public Meal Build() => _meal;
}

// Usage — fluent chaining
var meal = new MealBuilder()
    .AddBurger("Chicken")
    .AddDrink("Coke")
    .Build();
```

**Use when**: Object construction is complex; you need different representations of the same product; you want a fluent, readable construction API.

**Relationship to Factory**: Factory creates in one step; Builder creates step-by-step.

### Prototype Pattern

**Intent**: Specify the kinds of objects to create using a **prototypical instance** and create new objects by **cloning** that prototype.

```csharp
public abstract class Shape {
    public abstract Shape Clone();
}

public class Circle : Shape {
    public int Radius { get; set; }

    public override Shape Clone() {
        return (Shape)this.MemberwiseClone();  // shallow clone
    }
}
```

**Use when**: Object creation is expensive (e.g., deep database reads); the types of objects to create are specified at runtime; instances differ only in their state.

**Shallow vs deep clone**: `MemberwiseClone()` copies value types and references (not referenced objects). Override `Clone()` for deep cloning when reference fields must also be copied.

---

## Structural Patterns (Deep Dives)

Structural patterns deal with **object composition** — how to assemble objects and classes into larger structures while keeping those structures flexible and efficient.

### Adapter Pattern

**Intent**: Convert the interface of a class into another interface that clients expect. Lets classes work together that otherwise could not due to incompatible interfaces.

**Also known as**: Wrapper.

**Two forms**:
- **Object Adapter** — Contains an instance of the Adaptee (composition — preferred)
- **Class Adapter** — Inherits from both Target and Adaptee (multiple inheritance — language-dependent)

```csharp
// Target interface (what the client expects)
public interface ITarget {
    void Request();
}

// Adaptee (existing class with incompatible interface)
public class Adaptee {
    public void SpecificRequest() { /* legacy behaviour */ }
}

// Object Adapter (composition)
public class Adapter : ITarget {
    private readonly Adaptee _adaptee = new Adaptee();

    public void Request() {
        _adaptee.SpecificRequest();  // delegate to adaptee
    }
}
```

**Use when**: You want to use an existing class but its interface does not match what you need; integrating legacy or third-party code into a new system.

### Decorator Pattern

**Intent**: Attach additional responsibilities to an object **dynamically** without subclassing. Decorators provide a flexible alternative to subclassing for extending functionality.

**Structure**:
- **Component** — Interface for objects that can have responsibilities added
- **ConcreteComponent** — The base object; responsibilities may be attached to it
- **Decorator** — Wraps a Component; forwards operations to the wrapped component
- **ConcreteDecorator** — Adds its specific responsibility before or after forwarding

```csharp
public interface ICoffee {
    string GetDescription();
    double GetCost();
}

public class SimpleCoffee : ICoffee {
    public string GetDescription() => "Simple coffee";
    public double GetCost() => 1.00;
}

public class MilkDecorator : ICoffee {
    private readonly ICoffee _coffee;
    public MilkDecorator(ICoffee coffee) { _coffee = coffee; }
    public string GetDescription() => _coffee.GetDescription() + ", milk";
    public double GetCost() => _coffee.GetCost() + 0.25;
}

// Usage — decorators can be stacked
ICoffee order = new MilkDecorator(new SimpleCoffee());
// → "Simple coffee, milk" at $1.25
```

**Use when**: You need to add responsibilities to individual objects (not the whole class); responsibilities can be combined and withdrawn at runtime; subclassing would cause a combinatorial explosion of classes.

### Facade Pattern

**Intent**: Provide a **unified, simplified interface** to a complex subsystem. The Facade does not add new behaviour — it reduces complexity for clients.

```csharp
public class HomeTheaterFacade {
    private readonly Amplifier _amp;
    private readonly DVDPlayer _dvd;
    private readonly Projector _projector;

    public HomeTheaterFacade(Amplifier amp, DVDPlayer dvd, Projector projector) {
        _amp = amp; _dvd = dvd; _projector = projector;
    }

    public void WatchMovie(string movie) {
        _amp.TurnOn();
        _projector.TurnOn();
        _dvd.Play(movie);
    }

    public void EndMovie() {
        _dvd.Stop();
        _projector.TurnOff();
        _amp.TurnOff();
    }
}
```

**Use when**: A complex subsystem has many interdependencies; you want to provide a clean API layer; you want to reduce coupling between clients and subsystem internals.

**Note**: In Android architecture, the **Repository** is effectively a Facade over Room (local DB) and Retrofit (network) — see [[android-architecture]].

### Composite Pattern

**Intent**: Compose objects into **tree structures** to represent part-whole hierarchies. Lets clients treat individual objects and compositions uniformly.

**Structure**:
- **Component** — Common interface for all objects in the composition
- **Leaf** — A basic element with no children; does the actual work
- **Composite** — A container that stores child Components; implements child-related operations; delegates work to children

**Use when**: You need to represent hierarchies (file systems, UI component trees, organisational charts); clients should be able to ignore the difference between individual items and groups.

### Proxy Pattern

**Intent**: Provide a **surrogate or placeholder** for another object to control access to it.

**Types**:

| Type | Purpose |
|------|---------|
| **Remote Proxy** | Local representative for an object in a different address space |
| **Virtual Proxy** | Creates expensive objects on demand (lazy loading) |
| **Protection Proxy** | Controls access based on permissions |
| **Caching Proxy** | Caches results of expensive operations |

**Use when**: You need to intercept access to an object — for lazy creation, access control, logging, or remote invocation.

### Bridge Pattern

**Intent**: Decouple an **abstraction** from its **implementation** so that the two can vary independently.

- Without Bridge: a `Shape` hierarchy multiplied by a `Colour` hierarchy creates N×M subclasses.
- With Bridge: `Shape` holds a reference to a `Colour` interface — any Shape can use any Colour.

**Use when**: Both the abstraction and its implementation should be extensible by subclassing; you want to avoid a permanent binding between abstraction and implementation.

### Flyweight Pattern

**Intent**: Use sharing to support large numbers of **fine-grained objects** efficiently.

- Separates **intrinsic state** (shared, immutable — e.g., glyph shape in a document editor) from **extrinsic state** (not shared, supplied by the client — e.g., glyph position)
- The Flyweight object stores only intrinsic state; extrinsic state is passed in at runtime

**Use when**: An application creates an enormous number of similar objects whose combined memory footprint is unacceptable.

---

## Behavioural Patterns (Deep Dives)

Behavioural patterns are concerned with algorithms and the **assignment of responsibilities** between objects. They describe both the patterns of objects and the communication patterns between them.

### Observer Pattern

**Intent**: Define a **one-to-many dependency** so that when one object changes state, all dependents are notified and updated automatically.

**Also known as**: Publish-Subscribe.

```csharp
public interface IObserver {
    void Update(string state);
}

public class NewsAgency {
    private readonly List<IObserver> _observers = new();
    private string _news;

    public void Attach(IObserver o) => _observers.Add(o);
    public void Detach(IObserver o) => _observers.Remove(o);

    public string News {
        set { _news = value; Notify(); }
    }

    private void Notify() {
        foreach (var o in _observers) o.Update(_news);
    }
}
```

**Use when**: A change in one object requires updating others, and you don't know how many objects need to change; you want loose coupling between the subject and its dependents.

**Examples**: Event systems, UI data binding, Android LiveData/StateFlow, RSS feeds.

### Strategy Pattern

**Intent**: Define a **family of algorithms**, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

```csharp
public interface ISortStrategy {
    void Sort(List<int> data);
}

public class BubbleSort : ISortStrategy {
    public void Sort(List<int> data) { /* O(n²) */ }
}

public class QuickSort : ISortStrategy {
    public void Sort(List<int> data) { /* O(n log n) avg */ }
}

public class Sorter {
    private ISortStrategy _strategy;
    public Sorter(ISortStrategy strategy) { _strategy = strategy; }
    public void SetStrategy(ISortStrategy s) { _strategy = s; }
    public void Sort(List<int> data) => _strategy.Sort(data);
}
```

**Use when**: Many related classes differ only in behaviour; you need interchangeable variants of an algorithm; you want to avoid large conditional statements choosing between behaviours.

**OCP alignment**: New sorting algorithm → new class; no changes to `Sorter`.

### Command Pattern

**Intent**: Encapsulate a **request as an object**, allowing you to parameterise clients with different requests, queue or log requests, and support undoable operations.

**Participants**:
- **Command** — Interface declaring `Execute()` (and optionally `Undo()`)
- **ConcreteCommand** — Implements `Execute()` by invoking Receiver operations; stores state for undo
- **Receiver** — Knows how to perform the actual work
- **Invoker** — Holds and fires Commands (without knowing their type)
- **Client** — Creates ConcreteCommands and sets their Receivers

**Use when**: You need undoable operations; you need to queue or log operations; you want to decouple the sender of a request from its receiver.

### Iterator Pattern

**Intent**: Provide a way to **sequentially access** elements of an aggregate object without exposing its underlying representation.

```csharp
// C# provides IEnumerable<T> / IEnumerator<T> natively
public class BookCollection : IEnumerable<Book> {
    private readonly List<Book> _books = new();

    public void Add(Book b) => _books.Add(b);
    public IEnumerator<Book> GetEnumerator() => _books.GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}

// Client iterates without knowing it's a List internally
foreach (var book in collection) { /* ... */ }
```

**Use when**: You want a uniform interface for traversing different collection types; you want to support multiple simultaneous traversals.

### Template Method Pattern

**Intent**: Define the **skeleton of an algorithm** in a base class, deferring certain steps to subclasses. Template Method lets subclasses redefine steps without changing the algorithm's overall structure.

```csharp
public abstract class DataMigration {
    // Template method — defines the algorithm skeleton
    public void Migrate() {
        ExtractData();
        TransformData();
        LoadData();
    }

    // Steps deferred to subclasses
    protected abstract void ExtractData();
    protected abstract void TransformData();
    protected abstract void LoadData();
}

public class CsvToDbMigration : DataMigration {
    protected override void ExtractData() { /* read CSV */ }
    protected override void TransformData() { /* map columns */ }
    protected override void LoadData() { /* insert into DB */ }
}
```

**Use when**: Multiple classes share the same algorithm structure but differ in specific steps; you want to enforce an invariant algorithm while allowing extensible steps.

**Relationship to Strategy**: Template Method uses **inheritance** (steps are overridden); Strategy uses **composition** (whole algorithm is swapped).

### State Pattern

**Intent**: Allow an object to **alter its behaviour when its internal state changes**. The object will appear to change its class.

**Structure**:
- **Context** — Maintains a reference to the current State; delegates state-dependent behaviour to it
- **State** — Interface for state-specific behaviour
- **ConcreteState** — Implements behaviour for one state; may transition the Context to another State

**Use when**: An object's behaviour depends on its state and must change at runtime; you have large multipart conditionals (`if/switch`) that depend on the object's state.

**Example states**: `TrafficLight` (Red → Green → Yellow → Red); `VendingMachine` (Idle, HasMoney, Dispensing).

### Chain of Responsibility Pattern

**Intent**: Avoid coupling the sender of a request to its receiver by giving **more than one object a chance to handle** the request. Chain the handlers and pass the request along until one handles it.

**Structure**: Each handler holds a reference to the next handler. If a handler cannot process the request, it passes it to its successor.

**Use when**: More than one object may handle a request and the handler is not known a priori; you want to issue a request to one of several objects without specifying the receiver explicitly.

**Examples**: HTTP middleware pipelines, logging level filters, helpdesk escalation chains.

### Mediator Pattern

**Intent**: Define an object that **encapsulates how a set of objects interact**. Mediator promotes loose coupling by keeping objects from referring to each other explicitly.

- Instead of N objects communicating directly (O(N²) connections), all objects communicate through the Mediator (O(N) connections)

**Use when**: A set of objects communicate in complex but well-defined ways; you want to customise how objects interact without subclassing them.

**Examples**: Chat room server (mediates messages between clients); air traffic control tower; UI form coordinator.

### Memento Pattern

**Intent**: Without violating encapsulation, **capture and externalise an object's internal state** so that the object can be restored to this state later.

**Participants**:
- **Originator** — The object whose state must be saved; creates and restores Mementos
- **Memento** — Stores the Originator's internal state; opaque to all other objects
- **Caretaker** — Holds Mementos; never inspects or modifies their contents

**Use when**: You need undo/redo; you need snapshots of an object's state; direct state access would violate encapsulation.

### Visitor Pattern

**Intent**: Represent an operation to be performed on elements of an object structure. Visitor lets you **define new operations without changing the classes** of the elements on which it operates.

**Structure**:
- **Visitor** — Interface with one `Visit()` method per ConcreteElement type
- **ConcreteVisitor** — Implements each `Visit()` method; accumulates results
- **Element** — Interface with `Accept(Visitor)` method
- **ConcreteElement** — Implements `Accept()` by calling `visitor.Visit(this)`

**Use when**: You need many distinct and unrelated operations on an object structure; you want to avoid polluting element classes with unrelated operations; element classes are stable but operations on them change frequently.

**Trade-off**: Adding a new Visitor is easy; adding a new ConcreteElement requires updating all Visitors.

---

## Pattern Selection Guide

| Scenario | Pattern | Category |
|----------|---------|----------|
| Exactly one instance of a class | Singleton | Creational |
| Defer object creation to subclasses | Factory Method | Creational |
| Create families of related objects | Abstract Factory | Creational |
| Build complex object step-by-step | Builder | Creational |
| Copy existing objects cheaply | Prototype | Creational |
| Incompatible interfaces must work together | Adapter | Structural |
| Add behaviour to objects dynamically | Decorator | Structural |
| Simplify a complex subsystem | Facade | Structural |
| Treat individual objects and groups uniformly | Composite | Structural |
| Control access to an object | Proxy | Structural |
| Decouple abstraction from implementation | Bridge | Structural |
| Share many fine-grained objects efficiently | Flyweight | Structural |
| Notify many objects of state change | Observer | Behavioural |
| Select algorithm at runtime | Strategy | Behavioural |
| Encapsulate a request as an object | Command | Behavioural |
| Traverse a collection without exposing it | Iterator | Behavioural |
| Define skeleton algorithm; defer steps | Template Method | Behavioural |
| Object changes behaviour with its state | State | Behavioural |
| Pass request along a chain of handlers | Chain of Responsibility | Behavioural |
| Centralise interaction between many objects | Mediator | Behavioural |
| Save and restore object state (undo) | Memento | Behavioural |
| Add operations to classes without modifying them | Visitor | Behavioural |

---

## See Also

- [[oop-four-pillars]] — the OOP foundation these patterns build on
- [[software-architecture-patterns]] — architectural-level patterns (Layered, MVC, SOA, Data Mapper …)
- [[software-design-process]] — design process, ATAM evaluation, and design smells
- [[kotlin-coroutines]] — Hilt implements DIP via constructor injection
- [[android-architecture]] — Repository (Facade), ViewModel (Observer), Hilt (DIP in practice)
- [[sources/ICT2112-software-design]] — primary source course for this page
- [[sources/INF1009-object-oriented-programming]] — original source (SOLID + three creational patterns)
