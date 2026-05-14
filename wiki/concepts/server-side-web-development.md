---
type: concept
title: "Server-Side Web Development (PHP, Node.js, Databases)"
domain: web-development
source: [[sources/INF1005-web-systems-technologies]]
complexity: high
updated: 2026-05-14
tags: [concept, web-development, php, nodejs, express, mysql, pdo, rest-api, mongodb, lamp]
---

# Server-Side Web Development

Covers PHP basics (syntax, arrays, OOP, form processing), the LAMP stack, MySQL database operations via PDO, relational and NoSQL databases, Node.js/Express REST APIs, WebSockets, view engines, serverless, and modern frameworks.

---

## 1. Server-Side vs Client-Side

| | Client-Side (Browser) | Server-Side |
|-|-----------------------|-------------|
| Language | JavaScript | PHP, Node.js, Python, Ruby, C# |
| Execution | Browser | Web server |
| Access to | DOM, browser APIs | Databases, files, external services |
| Security | Cannot be trusted | Last line of defence |

**When to use server-side**: database access, authentication, session management, business logic that must not be exposed, sending email, calling external APIs.

---

## 2. PHP — Basics

PHP embeds inside HTML. Code inside `<?php … ?>` is executed; HTML outside is echoed directly.

```php
<?php
$user = "Randy";
?>
<!DOCTYPE html>
<html>
<body>
  <h1>Welcome <?php echo $user; ?></h1>
</body>
</html>
```

- Files use `.php` extension
- Comments: `//` (single-line), `/* … */` (multi-line)
- PHP 7+ supports type declarations: `function greet(string $name): string { … }`

### Variables and Types

```php
$name   = "Alice";   // String
$age    = 25;        // Integer
$price  = 9.99;      // Float
$active = true;      // Boolean
$nothing = null;     // Null
```

Variables are prefixed with `$`. Dynamically typed.

### Output

```php
echo "Hello " . $name;         // Concatenation with .
echo "<em>$name</em>";         // Variables expand in double-quoted strings
printf("Price: %.2f", $price); // Formatted output
```

### Control Flow

```php
if ($x > 0) { echo "positive"; }
elseif ($x === 0) { echo "zero"; }
else { echo "negative"; }

switch ($type) {
  case "A": echo "Alpha"; break;
  default:  echo "Other";
}

while ($i < 10) { $i++; }
for ($i = 0; $i < 10; $i++) { echo $i; }
foreach ($array as $value) { echo $value; }
foreach ($array as $key => $value) { echo "$key: $value"; }
```

### Include Files

```php
include "header.php";           // Warning if missing
require "config.php";           // Fatal error if missing
include_once "functions.php";   // Include at most once
require_once "db.php";          // Require at most once
```

### Functions

```php
function getNiceTime($showSeconds = true) {
  return $showSeconds ? date("H:i:s") : date("H:i");
}

// Pass by reference
function addTen(&$num) { $num += 10; }
```

---

## 3. PHP Arrays

```php
// Indexed
$days = ["Mon", "Tue", "Wed"];
$days[] = "Thu";           // Append
echo $days[0];             // "Mon"

// Associative (key-value)
$person = ["name" => "Alice", "age" => 30];
echo $person["name"];      // "Alice"

// Multidimensional
$cart = [
  ["id" => 37, "title" => "Widget A", "qty" => 2],
  ["id" => 38, "title" => "Widget B", "qty" => 1],
];

unset($cart[0]);           // Delete element
count($days);              // Length
isset($days[0]);           // Check existence
```

---

## 4. PHP OOP

```php
class Artist {
  public  $firstName;
  private $secret;

  function __construct($firstName) {
    $this->firstName = $firstName;
  }

  public function getName(): string {
    return $this->firstName;
  }
}

class Painter extends Artist {
  public $style;
  function __construct($first, $style) {
    parent::__construct($first);
    $this->style = $style;
  }
}

$artist = new Artist("Pablo");
echo $artist->getName();
```

**Visibility**: `public` — anywhere; `private` — within class only; `protected` — within class and subclasses.

---

## 5. PHP Superglobals

| Superglobal | Contents |
|-------------|----------|
| `$_GET` | URL query string parameters |
| `$_POST` | HTTP POST body data |
| `$_REQUEST` | Combined GET + POST + COOKIE |
| `$_SESSION` | Session data (persists across requests) |
| `$_COOKIE` | Cookie data |
| `$_FILES` | Uploaded file data |
| `$_SERVER` | Server and request metadata |
| `$_ENV` | Environment variables |

```php
$id = $_GET["id"];
$username = $_POST["username"];
if ($_SERVER["REQUEST_METHOD"] === "POST") { /* … */ }

// HTTP headers
header("Location: error.php");           // Redirect
header("Content-Type: application/json");
echo json_encode($data);                 // Return JSON
```

---

## 6. Form Processing and Input Security

### Validation Layers (in order of importance)

1. **HTML5** — `required`, `type`, `min/max` — UX hint only; easily bypassed
2. **JavaScript** — better UX; not reliable
3. **Server-side** — **only guaranteed layer; always required**

### Sanitising PHP Input

```php
// Escape HTML output to prevent XSS
$safe = htmlspecialchars($_POST["comment"]);

// Validate email
if (filter_var($email, FILTER_VALIDATE_EMAIL)) { /* valid */ }

// Sanitise string
$clean = filter_var($input, FILTER_SANITIZE_STRING);
```

**POST vs GET decision**: use GET for idempotent/read requests (search); use POST for state-changing requests (login, purchase).

---

## 7. The LAMP Stack

| Letter | Component |
|--------|-----------|
| **L** | Linux — operating system |
| **A** | Apache — web server |
| **M** | MySQL — relational database |
| **P** | PHP — server-side scripting language |

### LAMP Setup on Ubuntu

```bash
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install mysql-server
sudo apt-get install php libapache2-mod-php php-mysql
sudo systemctl restart apache2
# Deploy files to /var/www/html/
```

**Alternatives**: MAMP (macOS), WAMP (Windows), XAMPP (cross-platform).

---

## 8. MySQL and PDO

PHP Data Objects (PDO) is the recommended way to interact with databases — supports prepared statements which prevent SQL injection.

```php
// Connect
try {
  $pdo = new PDO("mysql:host=localhost;dbname=mydb", USER, PASS);
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
  die($e->getMessage());
}

// Create table
$pdo->exec("CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  email VARCHAR(100)
)");

// Insert (prepared statement — safe from SQL injection)
$stmt = $pdo->prepare("INSERT INTO users (username, email) VALUES (?, ?)");
$stmt->execute([$username, $email]);

// Select
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->bindValue(':id', $_GET['id']);
$stmt->execute();
while ($row = $stmt->fetch()) { echo $row['username']; }

// Close
$pdo = null;
```

---

## 9. Relational Database Concepts

- **Table** — 2D container (rows and columns)
- **Primary key** — uniquely identifies each record
- **Foreign key** — links to another table's primary key

### Relationships

| Type | Description |
|------|-------------|
| **One-to-many** | One record → many records in another table |
| **One-to-one** | One record → exactly one record |
| **Many-to-many** | Requires a junction (intermediate) table with a composite key |

### SQL CRUD

```sql
-- Read
SELECT Title, Artist FROM Paintings WHERE Year > 1900 ORDER BY Title;

-- Read with JOIN
SELECT Paintings.Title, Artists.LastName
FROM Paintings
INNER JOIN Artists ON Paintings.ArtistID = Artists.ArtistID;

-- Aggregate
SELECT Artist, COUNT(*) AS Count FROM Paintings GROUP BY Artist;

-- Create
INSERT INTO Artists (FirstName, LastName) VALUES ('Pablo', 'Picasso');

-- Update
UPDATE Artists SET City = 'Paris' WHERE ArtistID = 5;

-- Delete
DELETE FROM Artists WHERE ArtistID = 5;

-- Transaction
START TRANSACTION;
INSERT INTO orders …;
UPDATE inventory …;
COMMIT;  -- or ROLLBACK on error
```

---

## 10. NoSQL Databases

| Type | Description | Examples |
|------|-------------|---------|
| **Key-Value Store** | Unique key → value | Redis, DynamoDB |
| **Document Store** | Key → JSON/XML document | MongoDB, Firebase |
| **Column Store** | Stored by column, not row | Cassandra |
| **Graph Store** | Nodes and relationships | Neo4j |

**Use NoSQL when**: large datasets, high write volume, flexible schemas, distributed systems.
**Use SQL when**: ACID compliance, relational integrity, complex joins.

### MongoDB with Mongoose (Node.js)

```javascript
const mongoose = require('mongoose');
mongoose.connect(process.env.MONGO_URL);

const bookSchema = new mongoose.Schema({
  isbn: String,
  title: String,
  year: Number
});
const Book = mongoose.model('Book', bookSchema, 'books');

Book.find({}, (err, data) => res.json(data));
Book.find({ isbn: "12345" }, (err, data) => res.json(data));
```

---

## 11. Node.js

Server-side JavaScript runtime built on Chrome's V8 engine. **Asynchronous, event-driven, non-blocking** architecture.

### Blocking vs Non-Blocking

| PHP/Apache (Blocking) | Node.js (Non-Blocking) |
|-----------------------|------------------------|
| Each request → own thread | Single event-loop thread |
| I/O blocks the thread | I/O delegated; loop continues |
| Simpler model, less scalable | More complex, highly scalable |

**Advantages**: JavaScript everywhere (shared code), push architectures, rich npm ecosystem.
**Disadvantages**: not ideal for CPU-intensive tasks (video processing, heavy computation); more complex relational DB integration.

### Basic Node Server

```javascript
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, {"Content-Type": "text/plain"});
  res.write("Hello from Node.js!");
  res.end();
});
server.listen(8080);
```

---

## 12. Express Framework

```javascript
const express = require('express');
const app = express();

// Serve static files
app.use('/static', express.static('public'));

// Routes
app.get('/', (req, res) => res.send("Home page"));
app.get('/users/:id', (req, res) => {
  res.json({ id: req.params.id, name: "Alice" });
});

app.listen(8080);
```

### REST API with CRUD

```javascript
app.get('/items',     (req, res) => { /* READ all   */ });
app.get('/items/:id', (req, res) => { /* READ one   */ });
app.post('/items',    (req, res) => { /* CREATE      */ });
app.put('/items/:id', (req, res) => { /* UPDATE      */ });
app.delete('/items/:id', (req, res) => { /* DELETE   */ });
```

---

## 13. WebSockets (Socket.io)

Enables **two-way (full-duplex) communication** between browser and server — used for chat, live updates, multiplayer games.

```javascript
// Server side
const io = require('socket.io')(server);
io.on('connection', socket => {
  socket.on('chat message', msg => {
    io.emit('chat message', msg);   // Broadcast to all connected clients
  });
});
```

---

## 14. View Engines (EJS)

EJS (Embedded JavaScript) templates allow Node.js to render HTML server-side with dynamic data:

```html
<h1><%= title %></h1>
<% for (let p of paintings) { %>
  <div><%= p.artist %> — <%= p.title %></div>
<% } %>
```

---

## 15. Serverless Computing

Deploy functions without managing servers; cloud provider handles infrastructure.

| Type | Description |
|------|-------------|
| **DBaaS** | Database as a Service (e.g., Firebase, Atlas) |
| **PaaS** | Platform as a Service (e.g., Heroku, App Engine) |
| **FaaS** | Functions as a Service (e.g., AWS Lambda, Cloudflare Workers) |

Benefits: reduced complexity, pay-per-use, auto-scaling, higher reliability.

---

## 16. Modern Frameworks (Overview)

| Framework | Language | Approach |
|-----------|----------|---------|
| **React** | JavaScript (JSX) | Component-based UI library (Facebook, 2013) |
| **Next.js** | JavaScript | React + server-side rendering, routing, full-stack |
| **Remix** | JavaScript | Full-stack React; nested routing; server-loads data in parallel |
| **ASP.NET Core** | C# | Fast, cross-platform; Razor Pages syntax |
| **ASP.NET Blazor** | C# | Full-stack .NET; runs in browser via WebAssembly or server via SignalR |

---

## See Also

- [[concepts/web-fundamentals|Web Fundamentals]] — HTTP, DNS, the network layer
- [[concepts/javascript-fundamentals|JavaScript Fundamentals]] — client-side JS; Node.js shares the same language
- [[concepts/web-security-and-devops|Web Security and DevOps]] — SQL injection, XSS, prepared statements, HTTPS
- [[concepts/relational-database-fundamentals|Relational Database Fundamentals]] — deeper SQL and normalisation theory
- [[concepts/nosql-and-data-warehousing|NoSQL and Data Warehousing]] — MongoDB, Redis, Cassandra in detail
- [[sources/INF1005-web-systems-technologies|INF1005 Source Page]]
