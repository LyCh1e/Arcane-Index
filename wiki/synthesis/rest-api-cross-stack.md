---
type: synthesis
status: established
title: "REST API: Server Design (INF1005) ↔ Android Client (INF2007)"
domain: web-development × mobile-development
sources:
  - concepts/server-side-web-development
  - concepts/web-fundamentals
  - concepts/android-architecture
  - concepts/kotlin-coroutines
complexity: high
updated: 2026-05-14
tags: [synthesis, REST, express, retrofit, android, nodejs, http, json, MVVM, coroutines, INF1005, INF2007]
---

# REST API: Server Design (INF1005) ↔ Android Client (INF2007)

INF1005 teaches how to build a REST API server using Node.js and Express. INF2007 teaches how to call a REST API from an Android application using Retrofit. The two modules are taught in different semesters and with no explicit cross-reference, yet they are describing the two ends of a single HTTP conversation. This page documents the full request lifecycle, the shared contract both sides must honour, and the places where the two implementations diverge.

---

## 1. The REST Contract

A REST API is defined by a contract: an agreement between server and client on URL structure, HTTP verbs, request format, and response format. Both sides must implement the same contract, or communication fails. The contract is not enforced by any runtime — it is enforced by the discipline of both developers.

The elements of the contract:

| Element | Example | Where Defined |
|---|---|---|
| Base URL | `https://api.example.com/` | Server deployment; Retrofit `baseUrl()` |
| Resource path | `/items`, `/items/{id}` | Express route string; Retrofit `@GET("items/{id}")` |
| HTTP verb | GET, POST, PUT, DELETE | Express method name; Retrofit annotation |
| Request body format | `application/json` | `express.json()` middleware; Retrofit `GsonConverterFactory` |
| Response body format | JSON object / array | `res.json(data)`; Retrofit deserialises to data class |
| Status codes | 200, 201, 404, 500 | Express `res.status(n).json(…)`; Retrofit `Response<T>.code()` |

---

## 2. The Server Side (INF1005 — Express)

[[concepts/server-side-web-development|Server-Side Web Development]] covers REST API construction in Node.js with Express. The five CRUD routes follow a consistent pattern:

```javascript
const express = require('express');
const app = express();
app.use(express.json());   // Parse JSON request bodies

// READ all
app.get('/items', (req, res) => {
    res.json(items);                          // 200 OK with JSON array
});

// READ one
app.get('/items/:id', (req, res) => {
    const item = items.find(i => i.id === parseInt(req.params.id));
    if (!item) return res.status(404).json({ error: 'Not found' });
    res.json(item);
});

// CREATE
app.post('/items', (req, res) => {
    const newItem = { id: Date.now(), ...req.body };
    items.push(newItem);
    res.status(201).json(newItem);            // 201 Created
});

// UPDATE
app.put('/items/:id', (req, res) => {
    const idx = items.findIndex(i => i.id === parseInt(req.params.id));
    items[idx] = { ...items[idx], ...req.body };
    res.json(items[idx]);
});

// DELETE
app.delete('/items/:id', (req, res) => {
    items = items.filter(i => i.id !== parseInt(req.params.id));
    res.status(204).send();                   // 204 No Content
});

app.listen(3000);
```

Key points:
- `req.params.id` extracts path parameters (`:id` in the route string).
- `req.body` is the parsed JSON request body, available after `express.json()` middleware.
- `res.json(data)` serialises the JavaScript object to JSON and sets `Content-Type: application/json`.
- `res.status(n)` sets the HTTP response status code.

---

## 3. The Client Side (INF2007 — Retrofit)

[[concepts/kotlin-coroutines|Kotlin, Coroutines, and Android Async]] covers Retrofit as Android's REST client. The Retrofit interface mirrors the Express routes exactly, using annotations instead of method names:

```kotlin
interface ItemApiService {

    // READ all       ← mirrors app.get('/items')
    @GET("items")
    suspend fun getItems(): List<ItemDto>

    // READ one       ← mirrors app.get('/items/:id')
    @GET("items/{id}")
    suspend fun getItem(@Path("id") id: Int): ItemDto

    // CREATE         ← mirrors app.post('/items')
    @POST("items")
    suspend fun createItem(@Body item: ItemDto): ItemDto

    // UPDATE         ← mirrors app.put('/items/:id')
    @PUT("items/{id}")
    suspend fun updateItem(@Path("id") id: Int, @Body item: ItemDto): ItemDto

    // DELETE         ← mirrors app.delete('/items/:id')
    @DELETE("items/{id}")
    suspend fun deleteItem(@Path("id") id: Int): Response<Unit>
}
```

The Retrofit instance is built once (typically in a Hilt module, as shown in [[concepts/kotlin-coroutines|Kotlin, Coroutines, and Android Async]]) and injected wherever needed:

```kotlin
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val apiService = retrofit.create(ItemApiService::class.java)
```

`GsonConverterFactory` handles JSON serialisation and deserialisation automatically. The data class `ItemDto` must have fields matching the JSON keys the server sends:

```kotlin
data class ItemDto(
    val id: Int,
    val name: String,
    val price: Double
)
```

---

## 4. Express Route ↔ Retrofit Annotation Mapping

| CRUD Operation | Express Route | Retrofit Annotation | Path Param | Body |
|---|---|---|---|---|
| Read all | `app.get('/items', …)` | `@GET("items")` | — | — |
| Read one | `app.get('/items/:id', …)` | `@GET("items/{id}")` | `@Path("id")` | — |
| Create | `app.post('/items', …)` | `@POST("items")` | — | `@Body` |
| Update | `app.put('/items/:id', …)` | `@PUT("items/{id}")` | `@Path("id")` | `@Body` |
| Delete | `app.delete('/items/:id', …)` | `@DELETE("items/{id}")` | `@Path("id")` | — |

The symmetry is structural: the route string `/items/:id` in Express corresponds to the annotation string `"items/{id}"` in Retrofit; the `:id` placeholder and the `{id}` placeholder serve identical purposes in their respective frameworks. Both are resolved to the value provided at call time (`req.params.id` on the server; `@Path("id") id: Int` on the client).

---

## 5. The Full HTTP Request Lifecycle

A single `getItem(42)` call from the Android app to the Express server traverses the full stack:

```
Android App
  │
  │  ItemViewModel.loadItem(42)
  │       calls repository.getItem(42)
  │            calls apiService.getItem(42)
  │                 Retrofit builds HTTP request:
  │                   GET /items/42
  │                   Host: api.example.com
  │                   Accept: application/json
  │
  ▼ (OkHttp sends over TCP/IP)
  
Express Server
  │
  │  Router matches: app.get('/items/:id', handler)
  │  req.params.id === "42"
  │  Finds item with id 42
  │  res.json({ id: 42, name: "Widget", price: 9.99 })
  │    → HTTP/1.1 200 OK
  │    → Content-Type: application/json
  │    → {"id":42,"name":"Widget","price":9.99}
  │
  ▼ (response travels back over TCP/IP)
  
Android App
  │  Gson deserialises JSON → ItemDto(id=42, name="Widget", price=9.99)
  │  suspend function returns ItemDto
  │  Repository returns to ViewModel
  │  ViewModel updates StateFlow
  │  Composable recomposed with new data
  ▼
```

---

## 6. Coroutine Integration — The INF2007 Async Bridge

The `suspend` keyword on Retrofit interface functions is what makes the Android side work without callbacks or blocking threads. From [[concepts/kotlin-coroutines|Kotlin, Coroutines, and Android Async]]:

```kotlin
// In the Repository (runs on IO dispatcher)
suspend fun loadItem(id: Int): ItemDto {
    return withContext(Dispatchers.IO) {
        apiService.getItem(id)
    }
}

// In the ViewModel
fun fetchItem(id: Int) {
    viewModelScope.launch {
        val item = repository.loadItem(id)   // suspends, does not block UI thread
        _uiState.value = item
    }
}
```

The `viewModelScope` is tied to the ViewModel's lifecycle (from [[concepts/android-architecture|Android Architecture]]). If the user navigates away, the scope is cancelled and any in-flight Retrofit request is automatically cancelled. The Express server will process the request and return a response, but the Android app will ignore it — there is no listener any more.

The Repository pattern wraps Retrofit and is the architectural boundary between the MVVM ViewModel layer and the network layer. The ViewModel never calls Retrofit directly.

---

## 7. Error Handling: The Divergence

This is where the two sides differ most sharply.

**Express (server)**: returns HTTP status codes to signal outcomes. The developer sets them explicitly:
- `res.status(400).json({ error: 'Validation failed' })`
- `res.status(404).json({ error: 'Not found' })`
- `res.status(500).json({ error: 'Internal server error' })`

**Retrofit / OkHttp (client)**: distinguishes two failure modes:
1. **Network failure** (no connection, timeout, DNS failure) → Retrofit throws an exception (typically `IOException`). The `suspend` function throws; the coroutine's exception propagates up.
2. **HTTP error response** (4xx, 5xx) → Retrofit returns normally, but with `Response<T>.isSuccessful == false` and a non-null `errorBody()`. No exception is thrown for HTTP errors.

To handle both modes correctly in a Repository:

```kotlin
suspend fun loadItem(id: Int): Result<ItemDto> {
    return try {
        val response = apiService.getItemResponse(id)   // @GET returns Response<ItemDto>
        if (response.isSuccessful) {
            Result.Success(response.body()!!)
        } else {
            Result.Error("HTTP ${response.code()}: ${response.message()}")
        }
    } catch (e: IOException) {
        Result.Error("Network failure: ${e.message}")
    }
}
```

A sealed `Result` class (from [[concepts/kotlin-coroutines|Kotlin, Coroutines, and Android Async]]) is the idiomatic way to propagate both outcomes to the ViewModel without throwing.

---

## 8. Content-Type: The Shared Language

The `Content-Type: application/json` header is the explicit declaration of the shared data format. Neither side can omit it correctly:

- **Express server**: `res.json(data)` automatically sets `Content-Type: application/json`. The `express.json()` middleware parses incoming requests whose `Content-Type` is `application/json`.
- **Retrofit client**: `GsonConverterFactory` automatically sets `Content-Type: application/json` on POST/PUT requests with `@Body` and deserialises responses whose `Content-Type` is `application/json`.

If a developer sets `Content-Type: text/plain` on the server, Retrofit's Gson converter will receive plain text where it expects JSON and throw a `JsonSyntaxException`. The contract has been violated.

---

## 9. MVVM Layer Summary

The full call chain, mapped to MVVM layers from [[concepts/android-architecture|Android Architecture]]:

| MVVM Layer | Android Component | Responsibility |
|---|---|---|
| **UI Layer** | Jetpack Compose `@Composable` | Observes `StateFlow`, renders data, sends user events |
| **ViewModel Layer** | `ViewModel` + `viewModelScope` | Launches coroutines, holds and updates `StateFlow` |
| **Repository** | `ItemRepository` | Decides cache vs network; calls Retrofit; returns domain objects |
| **Remote Data Source** | Retrofit `ItemApiService` | Executes HTTP requests, deserialises JSON |
| *(Network)* | OkHttp | TCP connection, redirects, timeouts |
| *(Server)* | Express `app.get/post/put/delete` | Handles request, queries database, serialises response |

---

## See Also

- [[concepts/server-side-web-development|Server-Side Web Development]] — Express routes, CRUD pattern, `res.json()`, PDO prepared statements for the database layer
- [[concepts/web-fundamentals|Web Fundamentals]] — HTTP verbs, status codes, request/response structure, `Content-Type` header
- [[concepts/android-architecture|Android Architecture]] — MVVM pattern, Repository, ViewModel, Room for local persistence
- [[concepts/kotlin-coroutines|Kotlin, Coroutines, and Android Async]] — Retrofit interface annotations, `suspend` functions, `viewModelScope`, structured concurrency
