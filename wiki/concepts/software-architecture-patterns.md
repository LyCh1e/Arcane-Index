---
type: concept
title: "Software Architecture Patterns"
domain: software-engineering
course: ICT2112
complexity: high
tags: [architecture, layered-architecture, mvc, mvvm, mvp, soa, microservices, data-mapper, active-record, circuit-breaker, patterns]
updated: 2026-05-12
status: established
created: 2026-05-12
---

# Software Architecture Patterns

An **architecture pattern** is a proven, generalised solution to a recurring structural problem. Patterns allow designers to quickly identify structural characteristics of a system, examine component interactions, and reason about quality attributes before any code is written.

> "It is much harder to design structural architecture from scratch — just like it is harder for a caveman to design the structural architecture of a house from scratch."

---

## The Layering Technique

**Layering** is the most common technique for breaking down the complexity of large software systems. Each layer exposes a well-defined interface to the layer above and is ignorant of the layers above it.

**Benefits:**
- Understand one layer without knowing the others
- Substitute layers with alternative implementations
- Minimise inter-layer dependencies
- Layers are natural boundaries for standardisation
- Reuse lower layers across multiple higher-level services

**Rules of Layering:**
- Upper layers may call lower layers
- Lower layers must **not** call upper layers (no circular dependencies)
- Layers communicate only through defined interfaces

### Standard 3-Tier Architecture

```
┌──────────────────────┐
│  Presentation Layer  │  ← UI, web controllers, API endpoints
├──────────────────────┤
│    Domain Layer      │  ← Business logic, domain entities
├──────────────────────┤
│  Data Source Layer   │  ← Data access, persistence, external services
└──────────────────────┘
```

---

## Domain Layer Patterns

The **domain layer** contains the business logic of the application. The right pattern depends on the complexity of that logic.

### Transaction Script

- Organises business logic as a series of procedures
- Each procedure handles one request from the presentation layer
- Simple, easy to understand for CRUD-heavy applications
- Becomes unwieldy as logic grows in complexity

**Use when:** Domain logic is simple and procedural.

### Domain Model

- An object model of the domain that incorporates **both behaviour and data**
- Classes represent real-world entities (Order, Customer, Product …)
- Each class encapsulates its own business rules
- Best for complex, interconnected business logic

**Use when:** Business logic is rich, complex, and evolves frequently.

### Table Module

- A single instance that handles business logic for all rows in a database table or view
- Sits between Transaction Script (too simple) and Domain Model (too complex)
- Common in systems built around datasets (e.g., DataTable in .NET)

---

## Data Source Layer Patterns

The **data source layer** manages communication between the application and its data stores.

### Table Data Gateway (TDG)

- An object that acts as a gateway to **one database table**
- One instance handles all rows in that table
- Contains CRUD methods: `FindAll()`, `FindById()`, `Insert()`, `Update()`, `Delete()`
- The domain layer works with raw data returned (DataTable, DataRow in .NET)

```csharp
public class BookGateway {
    public DataTable FindAll() { ... }
    public DataRow FindById(int id) { ... }
    public int Insert(string title, string author) { ... }
    public void Update(int id, string title) { ... }
    public void Delete(int id) { ... }
}
```

**Use when:** Domain logic is in Transaction Script style; domain objects are not needed.

### Row Data Gateway (RDG)

- An object that acts as a gateway to a **single row** in a database table
- One instance per row
- Contains instance variables for each column
- The domain layer manipulates individual gateway objects

**Use when:** Simple domain logic; one-to-one mapping between objects and rows.

### Active Record

- An object that **wraps a row** in a table and adds domain logic
- Carries both data (instance variables = columns) and behaviour (business methods)
- The object itself knows how to save, load, and delete itself from the database

**Use when:** Domain logic is simple; convenience outweighs the coupling between domain and database schema.

**Trade-off:** Domain object is coupled to the database schema — schema changes require domain changes.

### Data Mapper

- A separate **mapping layer** that moves data between domain objects and the database
- Domain objects know **nothing** about the database
- The database schema need not match the object structure
- Provides the cleanest separation of concerns

**Use when:** Domain model is complex; database schema differs from object structure; domain objects must be testable in isolation.

**Comparison:**

| Pattern | Coupling | Complexity | Best For |
|---------|----------|------------|---------|
| Table Data Gateway | Low (no domain objects) | Low | Transaction Script style |
| Row Data Gateway | Medium | Medium | Simple per-row logic |
| Active Record | High (object = row) | Low | Simple CRUD apps |
| Data Mapper | None | High | Complex domain models |

---

## Presentation Layer Patterns

The **presentation layer** manages the display of information and the handling of user input.

### Model-View-Controller (MVC)

The canonical pattern for separating UI concerns. Splits interaction into three roles:

| Component | Responsibility |
|-----------|---------------|
| **Model** | Holds domain data and business logic; notifies views of changes |
| **View** | Renders the model; forwards user input to the Controller |
| **Controller** | Interprets user gestures; updates the Model; selects the View |

**Request flow:**
1. User interacts with the **View**
2. View forwards input to the **Controller**
3. Controller updates the **Model**
4. Model notifies View (or Controller retrieves updated Model)
5. View re-renders from the Model

**Used in:** ASP.NET Core MVC, Spring MVC, Rails, Django.

### Model-View-Presenter (MVP)

- The **Presenter** acts as the middleman between Model and View
- The **View is passive** — it only renders what the Presenter tells it to
- The Presenter contains all UI logic (making it independently testable)
- View communicates with the Presenter via an interface

**Use when:** The View is difficult to test (e.g., Windows Forms, Android XML layouts). The Presenter can be unit-tested without the View.

### Model-View-ViewModel (MVVM)

- The **ViewModel** exposes data streams and commands to the View via data binding
- **Two-way data binding** keeps View and ViewModel in sync automatically
- The View has no reference to the Model
- The ViewModel has no reference to the View

**Used in:** WPF, Xamarin, Android Jetpack Compose, Angular, Vue.js.

See [[android-architecture]] for MVVM applied to Android (ViewModel + StateFlow + Compose).

**MV* Pattern Comparison:**

| Pattern | Who handles UI logic? | View coupling | Testability |
|---------|----------------------|---------------|------------|
| MVC | Controller | Moderate | Moderate |
| MVP | Presenter | Low (via interface) | High |
| MVVM | ViewModel | None | High |

---

## Service-Oriented Architecture (SOA) & Microservices Patterns

**SOA** designs software as a set of independent services that communicate over a network.

**Key SOA characteristics:**
- **Loose coupling** — Services are independent of each other
- **Interoperability** — Services communicate regardless of platform or language
- **Reusability** — Services can be consumed by multiple clients
- **Discoverability** — Services can be found and invoked dynamically
- **Composability** — Services can be combined into composite applications

### Gateway Pattern (API Gateway)

- A **single entry point** for all client requests
- Handles: routing, load balancing, authentication, rate limiting, SSL termination
- Shields clients from the internal structure of the service landscape

**Use when:** Multiple services need to be accessed by external clients; cross-cutting concerns should be centralised.

### Service Registry / Service Discovery

- A database of running services and their network locations
- Services **self-register** on startup and deregister on shutdown
- Clients **look up** the registry to find service endpoints dynamically
- Examples: Consul, Eureka, Kubernetes DNS

**Use when:** Services are distributed and their locations are not fixed (cloud, containerised deployments).

### Circuit Breaker

- Prevents an application from repeatedly calling a **failing remote service**
- Detects failures; "trips" the circuit to short-circuit calls during outages
- Allows the remote service time to recover

**Three states:**
```
Closed (normal)  →  [failures exceed threshold]  →  Open (calls fail fast)
                                                         ↓
Half-Open (probe)  ←  [timeout elapsed]  ←────────────────┘
     ↓ success → Closed
     ↓ failure → Open
```

**Use when:** Services depend on unreliable remote calls; cascading failures must be prevented.

### Adapter Pattern (in SOA)

- Bridges incompatible service interfaces
- Enables a client to use a service whose interface it does not understand
- Equivalent to the GoF Adapter at the architectural scale

---

## End-to-End Design Pipeline

When combining patterns into a complete design:

1. Choose the overall **architectural style** (Layered / SOA / Event-Driven …)
2. Identify the **layers** (Presentation, Domain, Data Source)
3. Apply appropriate **patterns** to each layer
4. Design **interfaces** between layers and components
5. Apply **GoF design patterns** within components
6. Evaluate against **quality attributes** (ATAM)

**Case study — Library Books Management System:**

| Layer / Concern | Pattern Applied |
|-----------------|----------------|
| Overall structure | Layered (Presentation → Domain → Data Source) |
| Web UI | MVC (ASP.NET Core MVC) |
| Data access | Data Mapper + Repository |
| External APIs | SOA (Google Books API, Tomorrow.io Weather API) |
| Service creation | Factory Method |
| Book availability alerts | Observer |

---

## See Also

- [[software-design-process]] — Design process, quality attributes, coupling, cohesion, and ATAM
- [[solid-and-design-patterns]] — SOLID principles and the full GoF design pattern catalogue
- [[android-architecture]] — MVVM applied to Android (ViewModel + Repository + Room/Retrofit)
- [[concepts/docker-compose]] — Deployment tool used alongside SOA/Microservices in ICT2216
