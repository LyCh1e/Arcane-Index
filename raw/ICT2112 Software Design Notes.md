# ICT2112 / ICT2106 – Software Design Notes
### Singapore Institute of Technology (SIT) | AY2025/26

---

## Table of Contents

1. [Module Overview](#module-overview)
2. [Topic 1 – Introduction to Software Design](#topic-1--introduction-to-software-design)
3. [Topic 2 – Software Design Principles](#topic-2--software-design-principles)
4. [Topic 3 – Software Architecture Patterns & Styles](#topic-3--software-architecture-patterns--styles)
5. [Topic 4 – Data Source & Presentation Layer Patterns](#topic-4--data-source--presentation-layer-patterns)
6. [Topic 5 – SOA Patterns & Putting It Together](#topic-5--soa-patterns--putting-it-together)
7. [Topic 6 – Principles of Detailed Design](#topic-6--principles-of-detailed-design)
8. [Topic 7 – Creational Design Patterns](#topic-7--creational-design-patterns)
9. [Structural Design Patterns](#structural-design-patterns)
10. [Behavioral Design Patterns](#behavioral-design-patterns)
11. [Design Evaluation](#design-evaluation)
12. [Construction Design](#construction-design)
13. [Week 8 Admin & Week 12 Revision](#week-8-admin--week-12-revision)

---

## Module Overview

**Module:** ICT2112 / ICT2106 – Software Design  
**Academic Year:** AY2025/26  
**Module Lead:** Asst. Prof. Alex Q. Chen (alex.q.chen@singaporetech.edu.sg, +65 6592 1401)  
**Module Co-Lead:** A/P Indriyati Atmosukarto (indriyati@singaporetech.edu.sg, +65 6592 2157)  
**Instructors:** Ms Serena Goh Hui Lin, Mr Sahaya Francis Mahendran Jeganatham

### Module Learning Outcomes

After completing this module, students should be able to:

1. Comprehend commonly used software architecture designs and their impacts on software performance.
2. Apply the appropriate software architecture styles and design patterns to design a moderately complex software system.
3. Translate a software architecture design into appropriate patterns, reusable software components, and classes.
4. Implement the detailed design for components of a software system and specify the internal interfaces between components.
5. Evaluate designs against non-functional requirements of a software system.
6. Analyse and use appropriate tools to support the software design process.

### Module Format

| Mode | Activities | Time |
|---|---|---|
| Lectorial | Content delivery, worked exercises, tutorials, announcements | 2 hours/week |
| Lab | Labs, project work | 2 hours/week |
| Self-Study | Including project and assignments | 10 hours/week |

### Assessment

| Item | Description | Due | Weight |
|---|---|---|---|
| In-class activities | Blended learning activities, tutorial & studio presentations & Q&As, lab exercises | Week 1–13 | 5% |
| Project (Team) | Design and implement a portion of a complex software, documentation, integration | D1 (20%), D2 (20%) | 40% |
| Quizzes (Individual) | Written tests of applied knowledge of software design | Week 6 (12.5%) & Week 12 (12.5%) | 25% |
| Final Exam (Individual) | Written examination covering all materials from Weeks 1–13 | Exam Period | 30% |

### Main Textbooks

- Martin Fowler, *Patterns of Enterprise Application Architecture*, Addison-Wesley, Boston, 2003.
- Carlos E. Otero, *Software Engineering Design: Theory and Practice*, CRC Press, 2012.

### Recommended Reading Resources

- Ian Sommerville, *Software Engineer*, 9th Edition, Pearson, 2010
- Adam Freeman, *Pro ASP.NET Core MVC 3*, 8th Edition, Apress, 2020
- Erich Gamma et al., *Design Patterns: Elements of Reusable Object-Oriented Software*, Addison-Wesley, 1994
- Scott Millet, *Professional ASP.NET Design Patterns*, Wiley, 2010
- Juval Lowy, *Righting Software: A Method for System and Project Design*, 1st Edition, Pearson Education, 2020

### Tools

- **Programming Language:** C# (similar to C++ and Java; students are expected to pick up C# quickly and independently)
- **Project Stack:** .NET Core, ASP.NET Core, Git

### Prior Knowledge Required

- Introduction to Software Engineering (INF2001)
- Object-Oriented Programming (INF1009) — classes/objects, aggregation/composition, inheritance, abstraction, interfaces, polymorphism
- Web Systems and Technologies (INF1005)
- UML — class diagrams, object diagrams, sequence diagrams, communication diagrams

### What is Complexity?

**Complexity** is anything related to the structure of a software system that makes it hard to understand and modify the system.

Complexity can take many forms. It might:
- Be hard to understand how a piece of code works
- Take a lot of effort to implement a small improvement
- Not be clear which parts of the system must be modified to make an improvement
- Be difficult to fix one bug without introducing another

> If a software system is hard to understand and modify, then it is **complicated**.  
> If a software system is easy to understand and modify, then it is **simple**.

---

## Topic 1 – Introduction to Software Design

### Key Points

1. Design your software for a purpose
2. Follow the design process flow
3. Seven key considerations when designing your software

### Agenda

1. Motivation for Software Engineering
2. Importance of Software Design
3. Software Design Process
4. Software Design & Quality Attributes
5. Key Issues in Software Design

---

### 1.1 Motivation for Software Engineering

**Software Engineering** is the application of a **systematic**, **disciplined**, and **quantifiable** approach to the development, operation, and maintenance of software; that is, the application of engineering to software.

Not all software systems are equal. Some are more **complex** than others and software failure may result in **catastrophic events**, including loss of human life.

**Engineering Software = Requirement → Design → Construction → Test → Maintenance**

Of importance to this course is the **design phase**, where requirements are used to create a **blueprint** of the software to be constructed.

---

### 1.2 Importance of Software Design

**Software Design is:**

- The **process** of identifying, evaluating, validating, and specifying the architectural, detailed, and construction models required to build software that meets its intended functional and non-functional requirements; **and**
- The **product** of such process.

**Why Software Design?**

- Improve the **economical aspect** of software development
- Improve **software quality**
- **Increase** the chance of meeting **user's requirements**
- Create **foundation** for system **understanding** and discussion
- Because **change is the only constant**!
- Produce a sense of **accomplishment** when producing a good design
- Deliver software **as a service**

---

### 1.3 Software Design Process

A **software design process** is a set of **activities** and **controls** that specify how resources work together for the production of software design artefacts.

**Design Process Components:**
1. **Objective & Constraints** — Description of what is to be achieved by the design process and the constraints
2. **Description of the product** — What the product is
3. **Plan of production** — Description of how the product is to be produced
4. **Rationale of the design** — Statements that justify why the designed product and its associated production plan can achieve the objectives and satisfy the constraints
5. **Condition of usage** — The condition under which the product should be used

**Software Design Process = Architecture Design → Detailed Design → Construction Design** *(iteration occurs between activities)*

- Architectural designs are elaborated through detailed design, which are further elaborated through construction design.
- In practice, design activities are not carried out in such orderly and controlled fashion; quite a bit of **iteration** occurs between these activities.

---

### 1.4 Software Architecture (Part 1)

Software architecture serves four purposes:

| Role | Description |
|---|---|
| **Structural** | Provides the major structural components and interfaces of the system |
| **Communication** | Serves as an important communication, reasoning, and analysis tool that supports the development and growth of the system |
| **Quality** | Focuses on the quality aspects of the system before detailed design or construction can begin |
| **Foundation** | Lays the foundation for all subsequent work in the software engineering lifecycle |

---

### 1.5 Detailed Design (Part 2)

- **Internal design** — Focuses mostly on the internals of components and interfaces
- **White-box** — Builds on the software architecture to provide a white-box approach to design the structure and behaviour of the system
- **Functional** — Focuses on functional requirements, whereas the architecture focuses mostly on non-functional (quality) requirements
- **Follows architecture** — Refines the architecture to reach a point where the software design, including architecture and detailed design, is deemed sufficiently complete for the construction phase to begin

**Detailed Design = Interface Design + Component Design**

**Interface (Not GUI) Design:**
- Specification of interfaces between components
- Provides a standardised way of accessing software components
- Allows multiple development efforts to occur in parallel as long as interfaces are obeyed

**Component Design:**
- Internal design (**structure** & **behaviour**) of components is created
- In OO design, components are designed by using class diagrams and sequence diagrams

---

### 1.6 Software Design & Quality Attributes

**Functional vs. Quality Attributes:**

Given: *"When the user presses the green button, the Options dialog appears"*
- How quickly will the dialog appear? → **Performance**
- How often will this function fail? → **Reliability / Availability**
- How quickly will it be repaired? → **Availability**

**Microsoft Quality Attributes:**

**User-facing:**
- **Usability** — How well the application meets the requirements of the user and consumer, resulting in a good overall experience

**Run-time:**
- **Availability** — Defines the proportion of time that the system is functional and working
- **Performance** — Indication of the responsiveness of the system
- **Reliability** — The ability of the system to remain operational over time
- **Scalability** — Ability of a system to handle increasing load or to be readily enlarged
- **Security** — Capability of a system to prevent malicious or accidental actions

**Design:**
- **Conceptual Integrity** — Defines the consistency and coherence of the overall design
- **Maintainability** — Ability of the system to undergo changes with a degree of ease
- **Reusability** — The capability for components and subsystem to be suitable for use in other applications and scenarios
- **Testability** — How easy it is to test the application

---

### 1.7 Design Tactics for Quality Attributes

**Tactics for Security:**
- Resisting Attacks: Authenticating users, Limit exposure, Limit access on need-to-know basis, etc.
- Detecting Attacks: Intrusion detection

**Tactics for Testability:**
- Event logging: Log data and operations throughout the system. Allow testers to enable/disable this feature so events are displayed in the console to give insight into the system's operations and data.

**Tactics for Maintainability:**
- Localize changes: Modularisation, abstraction, encapsulation
- Prevention of ripple effects: Encapsulation, reduce coupling

**Tactics for Availability:**
- Redundancy, Task monitor, Watchdog timer, etc.

**Tactics for Performance:**
- Increase computation efficiency, reduce computational overhead, introduce concurrency, etc.

---

### 1.8 Key Issues in Software Design

**Process-Oriented Quality Attributes (Feasibility, Productivity, Time to Market, Integration with legacy system, Risk, Cost)**

**Process Facet of Design Quality** includes:
- Project Schedule & Milestones
- Development team organisation
- Test plan, etc.

**Levels of Software Design:**
1. The Software system
2. Is first organised into subsystems
3. The subsystems are further divided into classes
4. The classes are divided into routines and data
5. The inside of each routine is also designed

---

## Topic 2 – Software Design Principles

### 2.1 Software Architecture Drivers

**The Software Architecture Drivers** define the *what* and *why* about the architecture. They include:
1. **Primary functionality** — Core use cases the system must support
2. **Design purpose** — Why the system is being built and what it aims to achieve
3. **Quality attributes** — Non-functional requirements (performance, security, maintainability, etc.)
4. **Architectural concerns** — Cross-cutting concerns (logging, error handling, etc.)
5. **Architectural constraints** — Technology mandates, budget, time, team skill

> Software architecture requirements are **not the only** functional requirements.

---

### 2.2 General Design Principles

#### Principle #1: Modularisation

**Modularisation** is the process of continuous decomposition of the software system until fine-grained components are created.

> When you modularise a design, you are also modularising the requirements, programming, and test cases.

**Decomposition Strategies:**
- **Information hiding** — Make anticipation of areas in your code that change. Areas that change frequently in an implementation is best dealt with in isolation. This technique allows the semantics of a module to remain unchanged when implementations are replaced.
- **Layering** — Focusing on information hiding modules is not enough. Consider the concepts of abstract machines.

---

#### Principle #2: Abstraction

Abstraction is the process of identifying the essential aspects of an entity while ignoring the non-essential details.

- Abstractions simplify thinking about a complex system
- Allows you to focus on *what* something does, rather than *how* it does it

---

#### Principle #3: Encapsulation

**Encapsulation** deals with providing access to services of abstracted entities by exposing only the information that is essential to carry out such services while **hiding details** of how the services are carried out.

**Information hiding:** Internal details (state, structure, behaviour) become the object's secret.

*Example:* A simple `fillUp()` and `depleteOzone()` interface fully encapsulates and hides the `tank` attribute. No other object can use or know the state of the gas tank.

---

#### Principle #4: Coupling

**Coupling** is a measure of the strength of interconnection between modules/components.

- **Goal:** Low coupling (loosely coupled)
- **Scale (Tight → Loose):** Content → Common → Control → Stamp → Data

| Type | Description |
|---|---|
| **Content Coupling** | A module directly references the content of another module (e.g., module p modifies a statement of module q, refers to local data of q, or branches to a local label of q) |
| **Common Coupling** | Modules share a common data area (global variables) |
| **Control Coupling** | One module controls the logic of another by passing control information |
| **Stamp Coupling** | Modules share a composite data structure but may only use part of it |
| **Data Coupling** | Modules share data through parameter passing only (best form) |

**How to Decouple Your Design?**
- Divide and Conquer strategy
- Use what you have learned in OO Programming (Inheritance, Polymorphism)
- Other techniques introduced in this module

---

#### Principle #5: Cohesion

**Cohesion** is a measure of how closely related and focused the responsibilities of a single module are.

- **Goal:** High cohesion
- **Scale (High → Low):**

| Level | Type | Description |
|---|---|---|
| Highest | **Informational** | Module performs multiple operations on a shared data structure |
| | **Functional** | Module performs a single, well-defined function |
| | **Communicational** | Module's elements operate on the same data |
| | **Procedural** | Module's elements are related by order of execution |
| | **Temporal** | Module's elements are related by time of execution |
| | **Logical** | Module's elements are related by logic category |
| Lowest | **Coincidental** | Module's elements have no meaningful relationship |

---

### 2.3 Software Architecture Design Process & Evaluation

**Architecture Design involves:**
1. Identify the architectural drivers
2. Choose an architectural pattern / style
3. Apply the pattern to the system
4. Elaborate the architecture
5. Evaluate the architecture

**Architecture Evaluation:**
- Does the architecture meet the functional requirements?
- Does the architecture satisfy the quality attributes?
- Are the architectural constraints satisfied?

---

## Topic 3 – Software Architecture Patterns & Styles

### 3.1 Why Use Software Architecture Patterns?

> "The only constant is changes when engineering software."

**Software projects can be complex.** One of the major reasons for software projects to be complex is the constant change of requirements:
- As people understand the problem better, requirements may change.
- As people have a better understanding of the project solution, requirements may change.
- Well-designed software can be modified or extended easily.

**Architecture patterns** allow designers to:
- Quickly design and systematically **identify structural characteristics** of systems
- Provide means for **examining interactions**
- Examine proposed **quality** of the system

> It is much harder to come up with structural architecture from scratch — just like it is harder for a caveman to come up with the structural architecture of a house from scratch!

---

### 3.2 Introducing Software Architecture Patterns / Styles

A **software architecture pattern** is a proven, generalised solution to a recurring design problem. It describes the major structural components of a system, the relationships between them, and the interactions that occur.

**Common Architectural Patterns:**
- **Layered Architecture** (N-Tier)
- **Model-View-Controller (MVC)**
- **Service-Oriented Architecture (SOA) / Microservices**
- **Repository / Data Mapper**
- **Event-Driven Architecture**

---

### 3.3 The Layering Technique

**Layering** is one of the most common techniques for breaking down the complexity of software systems.

**Benefits of Layering:**
- You can understand a single layer as a coherent whole **without knowing** much about the other layers
- You can **substitute** layers with alternative implementations of the same basic services
- **Minimise dependencies** between layers
- Layers make good places for **standardisation**
- Once you have a layer built, you can use it for many **higher-level services**

**Common Layered Architecture (3-Tier):**

```
┌──────────────────────┐
│  Presentation Layer  │  ← UI / Web controllers
├──────────────────────┤
│    Domain Layer      │  ← Business logic
├──────────────────────┤
│  Data Source Layer   │  ← Data access / persistence
└──────────────────────┘
```

**Rules of Layering:**
- Upper layers can call lower layers
- Lower layers should **not** call upper layers (avoid circular dependencies)
- Layers communicate through defined interfaces

---

### 3.4 Patterns for Organising the Domain Layer

The domain layer contains the **business logic** of the application. Key patterns for organising this layer:

#### Transaction Script
- Organises business logic as a series of procedures
- Each procedure handles a single request from the presentation layer
- Simple to understand; becomes complex as logic grows

#### Domain Model
- An object model of the domain that incorporates both behaviour and data
- Classes represent real-world entities (e.g., Order, Customer, Product)
- Preferred for complex business logic

#### Table Module
- A single instance that handles the business logic for all rows in a database table or view
- Sits between Transaction Script and Domain Model

---

## Topic 4 – Data Source & Presentation Layer Patterns

### 4.1 Data Source Layer Architecture Patterns

The **data source layer** handles the communication between the application and its data stores (databases, external services, etc.).

#### Table Data Gateway
- An object that acts as a gateway to a database table
- One instance handles all the rows in the table
- Contains methods like `find()`, `insert()`, `update()`, `delete()`

**Example:**
```csharp
public class BookGateway {
    public DataTable FindAll() { ... }
    public DataRow FindById(int id) { ... }
    public int Insert(string title, string author) { ... }
    public void Update(int id, string title) { ... }
    public void Delete(int id) { ... }
}
```

#### Row Data Gateway
- An object that acts as a gateway to a single row in a database table
- One instance per row
- Contains instance variables for each column

#### Active Record
- An object that wraps a row in a database table or view
- Encapsulates the database access and adds domain logic on that data
- The object carries both data and behaviour
- Used in simple domain logic scenarios

#### Data Mapper
- A layer of Mappers that moves data between objects and the database while keeping them independent of each other
- The domain objects don't know anything about the database
- The database schema doesn't need to match the object structure
- Best for complex domain models

---

### 4.2 Patterns for Presentation Layer

The **presentation layer** handles the display of information and the management of user interaction.

#### Model-View-Controller (MVC)

The **MVC** pattern splits user interface interaction into three components:

| Component | Responsibility |
|---|---|
| **Model** | Contains business/domain data and logic; notifies views of changes |
| **View** | Displays the model; sends user gestures to the controller |
| **Controller** | Interprets user gestures and invokes changes on the model |

**MVC Flow:**
1. User interacts with the **View**
2. View forwards input to **Controller**
3. Controller updates the **Model**
4. Model notifies **View** (or controller retrieves updated model)
5. View re-renders from Model

#### Model-View-Presenter (MVP)

- The **Presenter** acts as the middleman between Model and View
- The View is passive — it only renders data
- The Presenter contains all UI logic

#### Model-View-ViewModel (MVVM)

- Used heavily in WPF, Xamarin, Angular, Vue
- The **ViewModel** exposes data streams and commands to the View
- Two-way data binding between View and ViewModel
- View has no reference to the Model

---

## Topic 5 – SOA Patterns & Putting It Together

### 5.1 Service-Oriented Architecture (SOA) Patterns

**Service-Oriented Architecture (SOA)** is an approach to designing software in which application components provide services to other components via a communications protocol (typically over a network).

**Key Characteristics of SOA:**
- **Loose coupling** — Services are independent of each other
- **Interoperability** — Services can communicate regardless of platform/language
- **Reusability** — Services can be reused by multiple consumers
- **Discoverability** — Services can be found and invoked dynamically
- **Composability** — Services can be combined to create composite applications

#### Common SOA / Microservices Patterns

**Gateway Pattern:**
- A single entry point for all client requests
- Handles routing, load balancing, authentication, rate limiting
- Example: API Gateway

**Service Registry / Service Discovery:**
- A database of services and their locations
- Services register themselves and clients look up services
- Examples: Consul, Eureka

**Circuit Breaker:**
- Prevents an application from repeatedly trying to call a remote service that is failing
- Detects failures and "trips" the circuit to prevent cascading failures
- States: Closed → Open → Half-Open

**Adapter Pattern (in SOA):**
- Bridges differences between service interfaces
- Enables incompatible services to work together

---

### 5.2 Putting It Together

**The complete software design landscape:**

```
Software Requirements
        │
        ▼
Software Architecture
  ├── Architectural Views
  └── Architectural Patterns
        │
        ▼
Detailed Design
  ├── Interface Design
  └── Component Design
        │
        ▼
Construction Design
  ├── Flow-based design
  └── Table-based design
        │
        ▼
Software Construction
```

**When applying patterns together:**
1. Choose the overall **architectural style** (e.g., Layered / SOA / MVC)
2. Identify the **layers** (Presentation, Domain, Data Source)
3. Apply appropriate **patterns** to each layer
4. Design **interfaces** between layers and components
5. Apply **design patterns** within components
6. Evaluate against **quality attributes**

---

## Topic 6 – Principles of Detailed Design

### 6.1 Overview

Detailed design focuses on the **internals of components** and the **interfaces between them**. It is the white-box view of the system.

**Detailed design produces:**
- Class diagrams (structure)
- Sequence diagrams (behaviour)
- Interface specifications
- Component specifications

---

### 6.2 SOLID Principles

The **SOLID** principles are five object-oriented design principles intended to make designs more understandable, flexible, and maintainable.

#### S – Single Responsibility Principle (SRP)
- A class should have **one, and only one, reason to change**
- Each class should encapsulate a single responsibility or functionality
- Violation: A class that handles both data access AND business logic AND UI rendering

#### O – Open/Closed Principle (OCP)
- Software entities (classes, modules, functions) should be **open for extension but closed for modification**
- Extend behaviour by adding new code, not changing existing code
- Use inheritance and polymorphism to achieve this

#### L – Liskov Substitution Principle (LSP)
- Objects of a superclass should be **replaceable with objects of subclasses** without affecting correctness
- Subclasses must honour the contract of the parent class
- Violation: A `Square` class that extends `Rectangle` but breaks `setWidth()` / `setHeight()` expectations

#### I – Interface Segregation Principle (ISP)
- A client should not be forced to implement interfaces it does not use
- **Many client-specific interfaces are better than one general-purpose interface**
- Split large interfaces into smaller, more specific ones

#### D – Dependency Inversion Principle (DIP)
- High-level modules should not depend on low-level modules. Both should depend on **abstractions**
- Abstractions should not depend on details. Details should depend on abstractions
- Use dependency injection and interfaces to invert dependencies

---

### 6.3 Interface Design Principles

**Interface design** (not GUI — this refers to API/component interfaces) involves specifying how components communicate.

**Good Interface Design:**
- **Minimal** — Expose only what clients need
- **Consistent** — Use consistent naming conventions and patterns
- **Complete** — Provide all operations the client needs
- **Convenient** — Easy to use correctly
- **Robust** — Hard to use incorrectly

---

### 6.4 Component Design

**Component design** specifies the internal structure and behaviour of individual components.

**Steps in component design:**
1. Identify the component's responsibilities
2. Define the interface (methods, parameters, return types)
3. Design the internal data structures
4. Specify the algorithms / logic
5. Identify collaborators

**UML tools for component design:**
- **Class diagrams** — Structure (attributes, methods, relationships)
- **Sequence diagrams** — Behaviour (message flows, interaction)
- **State diagrams** — Lifecycle of objects
- **Activity diagrams** — Flow of control

---

## Topic 7 – Creational Design Patterns

### 7.1 Introduction to Design Patterns

**Design patterns** are general, reusable solutions to commonly occurring problems in software design. They are *templates* — not finished code — that can be adapted to solve a design problem in many different situations.

**Origin:** "Gang of Four" (GoF) — Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides — *Design Patterns: Elements of Reusable Object-Oriented Software*, 1994.

**Benefits of Design Patterns:**
- Provide proven solutions to common problems
- Facilitate communication between developers (shared vocabulary)
- Improve code reusability, flexibility, and maintainability
- Support the principles of good OO design

**Three Categories of Design Patterns:**

| Category | Purpose |
|---|---|
| **Creational** | How objects are created |
| **Structural** | How objects are composed/structured |
| **Behavioral** | How objects communicate/interact |

---

### 7.2 Creational Patterns

Creational patterns deal with **object creation mechanisms**, aiming to create objects in a manner suitable to the situation.

#### Factory Method Pattern

**Intent:** Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

**Structure:**
- **Creator** — Declares the factory method; may provide a default implementation
- **ConcreteCreator** — Overrides the factory method to return a ConcreteProduct
- **Product** — Interface for objects the factory method creates
- **ConcreteProduct** — Implements the Product interface

**When to use:**
- When a class cannot anticipate the class of objects it must create
- When a class wants its subclasses to specify the objects it creates

**Example:**
```csharp
public abstract class Logger {
    public abstract ILog CreateLog(); // Factory method
    
    public void LogMessage(string msg) {
        ILog log = CreateLog();
        log.Write(msg);
    }
}

public class FileLogger : Logger {
    public override ILog CreateLog() {
        return new FileLog();
    }
}

public class DatabaseLogger : Logger {
    public override ILog CreateLog() {
        return new DatabaseLog();
    }
}
```

---

#### Abstract Factory Pattern

**Intent:** Provide an interface for creating **families of related or dependent objects** without specifying their concrete classes.

**Structure:**
- **AbstractFactory** — Interface for creating abstract products
- **ConcreteFactory** — Implements operations to create concrete products
- **AbstractProduct** — Interface for a type of product object
- **ConcreteProduct** — Defines a product to be created by corresponding ConcreteFactory
- **Client** — Uses only interfaces declared by AbstractFactory and AbstractProduct

**When to use:**
- When a system should be independent of how its products are created
- When a system should be configured with one of multiple families of products
- When you want to provide a class library of products and want to reveal only their interfaces

**Example:**
```csharp
public interface IUIFactory {
    IButton CreateButton();
    ITextBox CreateTextBox();
}

public class WindowsUIFactory : IUIFactory {
    public IButton CreateButton() => new WindowsButton();
    public ITextBox CreateTextBox() => new WindowsTextBox();
}

public class MacUIFactory : IUIFactory {
    public IButton CreateButton() => new MacButton();
    public ITextBox CreateTextBox() => new MacTextBox();
}
```

---

#### Singleton Pattern

**Intent:** Ensure a class has **only one instance** and provide a global point of access to it.

**When to use:**
- When exactly one object is needed to coordinate actions across the system
- Examples: logging service, configuration manager, thread pool

**Implementation (C#):**
```csharp
public class Singleton {
    private static Singleton _instance;
    private static readonly object _lock = new object();
    
    private Singleton() { }
    
    public static Singleton Instance {
        get {
            lock (_lock) {
                if (_instance == null) {
                    _instance = new Singleton();
                }
                return _instance;
            }
        }
    }
}
```

**Concerns:**
- Can make unit testing harder (global state)
- Can introduce hidden dependencies
- Thread safety must be carefully handled

---

#### Builder Pattern

**Intent:** Separate the **construction of a complex object** from its representation, so the same construction process can create different representations.

**When to use:**
- When the algorithm for creating a complex object should be independent of the parts that make up the object
- When you need to create different representations of the same product

**Structure:**
- **Director** — Constructs an object using the Builder interface
- **Builder** — Specifies an abstract interface for creating parts of a Product
- **ConcreteBuilder** — Constructs and assembles parts; defines and keeps track of the representation
- **Product** — The complex object being built

**Example:**
```csharp
public class MealBuilder {
    private Meal _meal = new Meal();
    
    public MealBuilder AddBurger(string type) {
        _meal.Burger = type;
        return this;
    }
    
    public MealBuilder AddDrink(string type) {
        _meal.Drink = type;
        return this;
    }
    
    public Meal Build() => _meal;
}

// Usage
var meal = new MealBuilder()
    .AddBurger("Chicken")
    .AddDrink("Coke")
    .Build();
```

---

#### Prototype Pattern

**Intent:** Specify the kinds of objects to create using a **prototypical instance**, and create new objects by **copying** (cloning) this prototype.

**When to use:**
- When a system should be independent of how its products are created, composed, and represented
- When the classes to instantiate are specified at runtime
- When instances of a class can have one of only a few different combinations of state

**Implementation:**
```csharp
public abstract class Shape {
    public abstract Shape Clone();
}

public class Circle : Shape {
    public int Radius { get; set; }
    
    public override Shape Clone() {
        return (Shape)this.MemberwiseClone();
    }
}
```

---

## Structural Design Patterns

### Introduction

**Structural patterns** deal with **object composition** — creating relationships between objects to form larger structures.

**Purpose:** Describe how to compose objects and classes to form larger structures while keeping these structures flexible and efficient.

---

### Adapter Pattern

**Intent:** Convert the interface of a class into another interface that clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

**Also known as:** Wrapper

**Two forms:**
- **Object Adapter** — Uses composition (contains an instance of the adaptee)
- **Class Adapter** — Uses multiple inheritance (inherits from both target and adaptee)

**When to use:**
- When you want to use an existing class but its interface doesn't match what you need
- When you want to create a reusable class that cooperates with unrelated or unforeseen classes

**Example:**
```csharp
// Target interface
public interface ITarget {
    void Request();
}

// Adaptee (existing class with incompatible interface)
public class Adaptee {
    public void SpecificRequest() { ... }
}

// Adapter
public class Adapter : ITarget {
    private Adaptee _adaptee = new Adaptee();
    
    public void Request() {
        _adaptee.SpecificRequest();
    }
}
```

---

### Decorator Pattern

**Intent:** Attach additional responsibilities to an object **dynamically**. Decorators provide a flexible alternative to subclassing for extending functionality.

**When to use:**
- When you want to add responsibilities to individual objects without affecting others
- When you want to add responsibilities that can be withdrawn
- When extension by subclassing is impractical

**Structure:**
- **Component** — Interface for objects that can have responsibilities added
- **ConcreteComponent** — The object to which responsibilities can be attached
- **Decorator** — Maintains a reference to a Component and defines an interface conforming to Component's
- **ConcreteDecorator** — Adds responsibilities to the component

**Example:**
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
    private ICoffee _coffee;
    public MilkDecorator(ICoffee coffee) { _coffee = coffee; }
    public string GetDescription() => _coffee.GetDescription() + ", milk";
    public double GetCost() => _coffee.GetCost() + 0.25;
}
```

---

### Facade Pattern

**Intent:** Provide a **unified, simplified interface** to a set of interfaces in a subsystem.

**When to use:**
- When you want to provide a simple interface to a complex subsystem
- When there are many dependencies between clients and the implementation classes

**Example:**
```csharp
public class HomeTheaterFacade {
    private Amplifier _amp;
    private DVDPlayer _dvd;
    private Projector _projector;
    
    public void WatchMovie(string movie) {
        _amp.TurnOn();
        _projector.TurnOn();
        _dvd.Play(movie);
    }
}
```

---

### Composite Pattern

**Intent:** Compose objects into **tree structures** to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

**When to use:**
- When you want to represent part-whole hierarchies of objects
- When you want clients to be able to ignore the difference between compositions and individual objects

**Structure:**
- **Component** — Interface for all objects in the composition
- **Leaf** — Basic element; has no children
- **Composite** — Has children; stores child components; implements child-related operations

---

### Proxy Pattern

**Intent:** Provide a **surrogate or placeholder** for another object to control access to it.

**Types of Proxy:**
- **Remote Proxy** — Provides a local representative for an object in a different address space
- **Virtual Proxy** — Creates expensive objects on demand (lazy loading)
- **Protection Proxy** — Controls access to the original object; useful when objects should have different access rights

---

### Bridge Pattern

**Intent:** Decouple an abstraction from its implementation so that the two can **vary independently**.

**When to use:**
- When you want to avoid a permanent binding between an abstraction and its implementation
- When both the abstractions and their implementations should be extensible by subclassing

---

### Flyweight Pattern

**Intent:** Use sharing to support large numbers of **fine-grained objects** efficiently.

- Used when an application uses a large number of objects that are costly to create
- Separates intrinsic state (shared) from extrinsic state (not shared)

---

## Behavioral Design Patterns

### Introduction

**Behavioral patterns** concern algorithms and the **assignment of responsibilities** between objects. They describe patterns of objects and classes and the communication patterns between them.

---

### Observer Pattern

**Intent:** Define a **one-to-many dependency** between objects so that when one object changes state, all its dependents are notified and updated automatically.

**Also known as:** Publish-Subscribe

**Participants:**
- **Subject (Observable)** — Knows its observers; provides interface to attach/detach Observer objects
- **Observer** — Interface for objects that should be notified of changes in a Subject
- **ConcreteSubject** — Stores state of interest to ConcreteObserver; sends notification when state changes
- **ConcreteObserver** — Maintains a reference to ConcreteSubject; stores state to stay consistent with Subject

**Example:**
```csharp
public interface IObserver {
    void Update(string state);
}

public class NewsAgency {
    private List<IObserver> _observers = new List<IObserver>();
    private string _news;
    
    public void Attach(IObserver observer) { _observers.Add(observer); }
    
    public string News {
        set {
            _news = value;
            NotifyAll();
        }
    }
    
    private void NotifyAll() {
        foreach (var o in _observers) o.Update(_news);
    }
}
```

---

### Strategy Pattern

**Intent:** Define a **family of algorithms**, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

**When to use:**
- When many related classes differ only in their behaviour
- When you need different variants of an algorithm
- When you want to avoid exposing complex algorithm-specific data structures

**Example:**
```csharp
public interface ISortStrategy {
    void Sort(List<int> data);
}

public class BubbleSort : ISortStrategy {
    public void Sort(List<int> data) { /* bubble sort */ }
}

public class QuickSort : ISortStrategy {
    public void Sort(List<int> data) { /* quick sort */ }
}

public class Sorter {
    private ISortStrategy _strategy;
    public Sorter(ISortStrategy strategy) { _strategy = strategy; }
    public void Sort(List<int> data) { _strategy.Sort(data); }
}
```

---

### Command Pattern

**Intent:** Encapsulate a **request as an object**, thereby allowing you to parameterise clients with different requests, queue or log requests, and support undoable operations.

**Participants:**
- **Command** — Interface for executing an operation
- **ConcreteCommand** — Implements execute by invoking corresponding operations on Receiver
- **Client** — Creates a ConcreteCommand and sets its Receiver
- **Invoker** — Asks the command to carry out the request
- **Receiver** — Knows how to perform the operations associated with carrying out a request

---

### Iterator Pattern

**Intent:** Provide a way to **sequentially access** the elements of an aggregate object without exposing its underlying representation.

**Example:**
```csharp
// C# already has IEnumerable<T> and IEnumerator<T>
// Custom iterator:
public class BookCollection : IEnumerable<Book> {
    private List<Book> _books = new List<Book>();
    public IEnumerator<Book> GetEnumerator() => _books.GetEnumerator();
}
```

---

### Template Method Pattern

**Intent:** Define the **skeleton of an algorithm** in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

**Example:**
```csharp
public abstract class DataMigration {
    // Template method
    public void Migrate() {
        ExtractData();
        TransformData();
        LoadData();
    }
    
    protected abstract void ExtractData();
    protected abstract void TransformData();
    protected abstract void LoadData();
}
```

---

### State Pattern

**Intent:** Allow an object to **alter its behaviour when its internal state changes**. The object will appear to change its class.

**When to use:**
- When an object's behaviour depends on its state and it must change behaviour at runtime depending on that state
- When operations have large multipart conditional statements that depend on the object's state

---

### Chain of Responsibility Pattern

**Intent:** Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

---

### Mediator Pattern

**Intent:** Define an object that **encapsulates how a set of objects interact**. Mediator promotes loose coupling by keeping objects from referring to each other explicitly.

---

### Memento Pattern

**Intent:** Without violating encapsulation, **capture and externalise an object's internal state** so that the object can be restored to this state later.

**Useful for:** Undo/redo operations

---

### Visitor Pattern

**Intent:** Represent an operation to be performed on the elements of an object structure. Visitor lets you **define a new operation without changing the classes** of the elements on which it operates.

---

## Design Evaluation

### How to Evaluate a Software Design

Design evaluation checks whether the architecture and detailed design adequately address the system's requirements and quality attributes.

**Key Evaluation Questions:**
1. Does the design satisfy **functional requirements**?
2. Does the design satisfy **quality attribute requirements**?
3. Are **architectural constraints** satisfied?
4. Is the design **internally consistent**?
5. Is the design **feasible** to implement?

### Architecture Evaluation Methods

**Architecture Tradeoff Analysis Method (ATAM):**
- Evaluates architectural decisions with respect to quality attribute requirements
- Identifies tradeoffs, sensitivity points, and risks
- Identifies non-risk decisions

**Key Steps in ATAM:**
1. Present the ATAM
2. Present business drivers
3. Present the architecture
4. Identify architectural approaches
5. Generate quality attribute utility tree
6. Analyse the architectural approaches
7. Brainstorm and prioritise scenarios
8. Analyse the architectural approaches (again)
9. Present results

### Design Smells

**Design smells** are symptoms of poor design that may indicate deeper problems:

- **Rigidity** — Design is hard to change; every change causes a cascade of other changes
- **Fragility** — Software breaks in many places when a single change is made
- **Immobility** — Design contains parts that could be useful in other systems but cannot be extracted
- **Viscosity** — Easier to do the wrong thing than the right thing
- **Needless complexity** — Over-engineering; design contains unnecessary elements
- **Needless repetition** — Similar code appears in many places (violates DRY)
- **Opacity** — Code is difficult to understand

---

## Construction Design

### Overview

**Construction design** is the final stage before implementation. It bridges the gap between the detailed design and the actual code.

**Construction design produces:**
- **Flow-based design** — Pseudocode, flowcharts, activity diagrams
- **Table-based design** — State tables, decision tables

### Flow-Based Design

**Pseudocode** — An informal high-level description of the algorithm/logic of a component.

**Example:**
```
PROCEDURE ProcessOrder(order):
    IF order is valid THEN
        Calculate total
        Apply discount IF eligible
        Process payment
        Update inventory
        Send confirmation
    ELSE
        Return error
    END IF
END PROCEDURE
```

**Activity Diagrams** — UML diagrams that show the flow of control from activity to activity.

### Table-Based Design

**Decision Tables** — Tabular representation of conditions and actions.

| Condition | Rule 1 | Rule 2 | Rule 3 |
|---|---|---|---|
| Member? | Yes | Yes | No |
| Purchase > $100? | Yes | No | - |
| **Action: Apply 20% discount** | X | | |
| **Action: Apply 10% discount** | | X | |
| **Action: No discount** | | | X |

**State Transition Tables** — Describe how a system transitions between states given events.

| Current State | Event | Next State | Action |
|---|---|---|---|
| Idle | Start | Processing | Begin operation |
| Processing | Complete | Idle | Log result |
| Processing | Error | Error | Log error |
| Error | Reset | Idle | Clear error |

---

## Week 8 Admin & Week 12 Revision

### Week 8 Admin Notes

- Midpoint of the module — Quiz 1 feedback and project progress check
- Integration of sub-modules begins (Weeks 8–13)
- Teams are expected to have completed their module scope and be working on deliverable D1

### Week 12 Revision – Part 2

**Key topics to revise for the final exam:**

#### Architecture Recap

| Topic | Key Concepts |
|---|---|
| Software Design Process | Architecture → Detailed → Construction |
| Quality Attributes | Usability, Availability, Performance, Reliability, Scalability, Security, Conceptual Integrity, Maintainability, Reusability, Testability |
| Architecture Drivers | Primary functionality, Design purpose, Quality attributes, Architectural concerns, Architectural constraints |
| Layering | Presentation, Domain, Data Source layers; benefits; rules |

#### Design Principles Recap

| Principle | Summary |
|---|---|
| Modularisation | Decompose into fine-grained components |
| Abstraction | Focus on what, not how |
| Encapsulation | Hide internal details |
| Coupling | Low coupling = loosely coupled; Content < Common < Control < Stamp < Data |
| Cohesion | High cohesion; Informational > Functional > Communicational > Procedural > Temporal > Logical > Coincidental |
| SOLID | SRP, OCP, LSP, ISP, DIP |

#### Patterns Recap

**Architectural / Layer Patterns:**
| Pattern | Layer | Key Idea |
|---|---|---|
| MVC / MVP / MVVM | Presentation | Separation of concerns for UI |
| Transaction Script | Domain | Procedure per use case |
| Domain Model | Domain | Rich OO model with behaviour |
| Table Module | Domain | One instance per table |
| Table Data Gateway | Data Source | One gateway object per table |
| Row Data Gateway | Data Source | One object per row |
| Active Record | Data Source | Object with data + DB access |
| Data Mapper | Data Source | Separate mapping layer |

**GoF Design Patterns:**

| Pattern | Category | Key Idea |
|---|---|---|
| Factory Method | Creational | Subclass decides which class to instantiate |
| Abstract Factory | Creational | Creates families of related objects |
| Singleton | Creational | Only one instance |
| Builder | Creational | Step-by-step construction |
| Prototype | Creational | Clone existing objects |
| Adapter | Structural | Convert interface to another interface |
| Decorator | Structural | Add behaviour dynamically |
| Facade | Structural | Simplified interface to subsystem |
| Composite | Structural | Part-whole tree structure |
| Proxy | Structural | Surrogate / placeholder |
| Bridge | Structural | Decouple abstraction from implementation |
| Flyweight | Structural | Share fine-grained objects |
| Observer | Behavioral | One-to-many state change notification |
| Strategy | Behavioral | Interchangeable algorithms |
| Command | Behavioral | Encapsulate request as object |
| Iterator | Behavioral | Sequential access without exposing structure |
| Template Method | Behavioral | Skeleton algorithm; subclass fills in steps |
| State | Behavioral | Object changes behaviour with state |
| Chain of Responsibility | Behavioral | Pass request along a chain |
| Mediator | Behavioral | Centralise object interaction |
| Memento | Behavioral | Save and restore object state |
| Visitor | Behavioral | Add operations without changing classes |

---

## Case Study – ElectronicDeals / Library Books Management System

Throughout the module, the **ElectronicDeals** system and the **Library Books Management System** are used as running case studies to illustrate the application of software design concepts.

**Library Books Management System features:**
- Books details: abstract, reviews (via Google Books API)
- Weather information (via Tomorrow.io weather API)
- Borrowing and return management
- User management and authentication

**Design of the system applies:**
- **Layered Architecture** — Presentation → Domain → Data Source
- **MVC** — For the web presentation layer
- **Data Mapper** — For isolating domain objects from database
- **Repository Pattern** — For data access abstraction
- **SOA** — For external API integrations (Google Books, Weather API)
- **Factory Method** — For creating different types of services
- **Observer** — For notifications on book availability

---

## Supplementary References

1. Carlos E. Otero. *Software Engineering Design*. CRC Press, Boca Raton FL, 2012 – Chapter 1
2. Software Engineering Book of Knowledge – SWEBOK: Software Design Chapter
3. UML – Information from the OMG portal: http://www.uml.org
4. Giddings, R. V. (1984). Accommodating uncertainty in software design. *Communications of the ACM*, 27(5), 428-434. DOI: https://doi.org/10.1145/358189.358066
5. McConnell, S., & Mcconnell, S. (2004). *Code Complete*. Microsoft Press.

---

*End of ICT2112 Software Design Notes – AY2025/26*
