---
type: concept
title: "JavaScript Fundamentals"
domain: web-development
source: [[sources/INF1005-web-systems-technologies]]
complexity: high
updated: 2026-05-14
tags: [concept, web-development, javascript, dom, events, async, es6, fetch-api]
status: established
created: 2026-05-14
---

# JavaScript Fundamentals

Covers JavaScript language fundamentals (types, operators, arrays, objects, functions, scope, closures, classes), DOM manipulation, event handling, asynchronous programming (Promises, async/await, Fetch API), ES6 modules, and browser APIs.

---

## 1. Language Overview

- **Object-oriented, dynamically typed** scripting language.
- Primarily client-side (browser), also server-side (Node.js).
- Variables, functions, and arrays are all objects.
- **Weakly/dynamically typed** — variables can hold any type.

**History**: Netscape 1996 → ECMAScript 1997. **ES6 (2015)**: major — classes, arrow functions, Promises, `let`/`const`, iterators, destructuring. Continues evolving (ES2020+).

**Placement**:
- Inline `onclick="..."` — discouraged
- Embedded `<script>` — mixes concerns
- External `<script src="file.js">` — **recommended**

---

## 2. Variables and Data Types

```javascript
var x = 5;    // function-scoped, hoisted (avoid in modern JS)
let y = 10;   // block-scoped
const z = 15; // block-scoped, immutable binding
```

### Primitive Types

| Type | Description |
|------|-------------|
| `Boolean` | `true` or `false` |
| `Number` | 64-bit float (integers and decimals) |
| `String` | Text, single or double or backtick quotes |
| `Null` | Intentional absence of value |
| `Undefined` | Declared but not assigned |
| `Symbol` | Unique key (ES2015) |

### Truthy and Falsy

- **Falsy**: `false`, `null`, `""`, `''`, `0`, `NaN`, `undefined`
- **Truthy**: everything else (including `"0"`, `[]`, `{}`)

---

## 3. Operators and Control Flow

### Equality

- `==` — loose equality with type coercion (avoid)
- `===` — strict equality, no coercion — **always prefer this**

### Conditionals

```javascript
if (x > 0) { … }
else if (x === 0) { … }
else { … }

switch (value) {
  case "A": result = "Alpha"; break;
  default: result = "Other";
}

// Ternary
let label = x > 0 ? "positive" : "non-positive";
```

### Loops

```javascript
while (count < 10) { count++; }
do { count++; } while (count < 10);
for (let i = 0; i < 10; i++) { /* … */ }
for (let item of array) { /* … */ }   // ES6 — iterates values
```

---

## 4. Arrays

```javascript
const countries = ["Canada", "France", "Germany"];

countries[0];           // "Canada"
countries.push("Spain");// Add to end
countries.pop();        // Remove from end
countries.length;       // Length

// Destructuring
let [first, second] = countries;
```

### Functional Array Methods (ES6+)

```javascript
// forEach — iterate (no return)
paintings.forEach(p => console.log(p.title));

// find — first match
const courbet = paintings.find(p => p.artist === "Courbet");

// filter — all matches
const vangoghs = paintings.filter(p => p.artist === "Van Gogh");

// map — transform into new array
const titles = paintings.map(p => p.title);

// reduce — single accumulated value
const total = paintings.reduce((acc, p) => acc + p.value, 0);

// sort — sort in place (provide compare function for objects)
const sorted = paintings.sort((a, b) => a.year - b.year);
```

---

## 5. Objects

```javascript
const photo = {
  id: 1,
  title: "Central Library",
  location: { country: "Canada", city: "Calgary" }
};

// Property access
photo.title;
photo["title"];

// Destructuring
let { id, title } = photo;
let { country, city } = photo.location;

// Spread
const copy = { ...photo, extra: "value" };
```

### JSON

```javascript
const jsonStr = '{"name": "Alice", "age": 30}';
const obj = JSON.parse(jsonStr);   // string → object
const str = JSON.stringify(obj);   // object → string
```

Property names in JSON must use **double quotes**.

---

## 6. Functions

```javascript
// Declaration (hoisted)
function subtotal(price, quantity) { return price * quantity; }

// Expression (not hoisted)
const calc = function(p, q) { return p * q; };

// Arrow function (ES6) — concise syntax
const tax = () => 0.05;
const add = (a, b) => a + b;

// Default parameters
function greet(name = "World") { return "Hello " + name; }

// Rest parameters
function sum(...args) { return args.reduce((a, b) => a + b, 0); }
```

---

## 7. Scope and Closures

| Scope | Keyword | Accessible |
|-------|---------|------------|
| Global | `var` (outside functions) | Everywhere |
| Function | `var`, `let`, `const` | Within function |
| Block | `let`, `const` | Within `{}` block |

**Hoisting**: function declarations are moved to the top of their scope. `var` declarations (not assignments) are also hoisted. `let`/`const` are not hoisted in the same way.

**Closure**: a function that retains access to its enclosing scope after that scope has finished executing.

```javascript
function makeCounter() {
  let count = 0;
  return function() { return ++count; };
}
const counter = makeCounter();
counter(); // 1
counter(); // 2
```

---

## 8. Classes (ES6)

JavaScript is **prototype-based**: objects inherit from other objects. ES6 classes are syntactic sugar over prototypes.

```javascript
class Customer {
  constructor(name, address) {
    this.name = name;
    this.address = address;
  }
  output() { return `${this.name}, ${this.address}`; }
}

class PremiumCustomer extends Customer {
  constructor(name, address, discount) {
    super(name, address);
    this.discount = discount;
  }
}
```

---

## 9. The Document Object Model (DOM)

The DOM is the browser's internal **tree** representation of an HTML page.

- `document` — root object representing the entire document
- **Nodes** — each element, attribute, or text piece
- **NodeList** — a collection of nodes

### Selecting Elements

```javascript
document.getElementById("myId");
document.getElementsByClassName("myClass");
document.getElementsByTagName("p");
document.querySelector("#main .highlight");    // first match
document.querySelectorAll("ul li");            // all matches (NodeList)
```

### Key Properties

| Property | Description |
|----------|-------------|
| `innerHTML` | All content (text + tags) — XSS risk if from user input |
| `textContent` | Text only (no tags) — safer |
| `classList` | Methods: `add()`, `remove()`, `toggle()` |
| `style` | Inline CSS properties |
| `value` | Form input value |

### Modifying the DOM

```javascript
// Style and classes
el.style.backgroundColor = "#ff0000";
el.classList.add("highlight");
el.classList.toggle("active");

// Content
element.textContent = "New text";
element.innerHTML = "<strong>Bold</strong>";

// Create and insert
const div = document.createElement("div");
parent.appendChild(div);
parent.insertBefore(newChild, referenceChild);

// Remove
parent.removeChild(child);
```

---

## 10. Event Handling

```javascript
// Modern approach
element.addEventListener("click", function(e) {
  e.preventDefault();     // Prevent default action (e.g., form submit, link navigation)
  e.stopPropagation();    // Stop bubbling
  console.log(e.target);  // Element that triggered the event
});

// Wait for DOM to be ready
document.addEventListener("DOMContentLoaded", function() { /* … */ });
```

### Event Categories

| Category | Events |
|----------|--------|
| **Mouse** | `click`, `dblclick`, `mousedown`, `mouseup`, `mouseover`, `mouseout`, `mousemove` |
| **Keyboard** | `keydown`, `keyup` |
| **Form** | `blur`, `focus`, `change`, `submit`, `reset` |
| **Window** | `load`, `DOMContentLoaded`, `resize`, `scroll` |

### Event Propagation

1. **Capturing phase** — event travels from root down to the target
2. **Bubbling phase** — event travels from target back up to root

### Event Delegation

Add one listener to a parent instead of many listeners on children:

```javascript
document.querySelector("#list").addEventListener("click", function(e) {
  if (e.target && e.target.nodeName === "LI") {
    handleItem(e.target);
  }
});
```

---

## 11. Regular Expressions

```javascript
let emailPattern = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
if (emailPattern.test(email)) { /* valid */ }
```

- Contained in forward slashes `/pattern/`
- Case-sensitive by default; add `i` flag for case-insensitive
- Metacharacters: `. [ ] \ ( ) ^ $ | * ? { } +`

---

## 12. Asynchronous JavaScript

### Fetch API

```javascript
fetch("/api/data")
  .then(response => response.json())
  .then(data => { /* use data */ })
  .catch(error => console.error(error));
```

### Promises

```javascript
const p = new Promise((resolve, reject) => {
  if (success) resolve(data);
  else reject(new Error("Failed"));
});
p.then(data => { /* success */ })
 .catch(err => { /* error */ });
```

### Async/Await (ES7)

```javascript
async function loadData() {
  try {
    const response = await fetch("/api/data");
    const data = await response.json();
    return data;
  } catch (err) {
    console.error(err);
  }
}
```

### CORS

Browsers restrict cross-origin requests by default. The server must respond with:
```
Access-Control-Allow-Origin: *
```

---

## 13. ES6 Modules

```javascript
// art.js — exporting
export function getAll() { /* … */ }
export const data = [];

// main.js — importing
import { getAll, data } from "./art.js";
```

In HTML:
```html
<script src="main.js" type="module"></script>
```

---

## 14. Browser APIs

### Web Storage

```javascript
// localStorage — persists until manually cleared
localStorage.setItem("key", JSON.stringify(value));
const val = JSON.parse(localStorage.getItem("key"));

// sessionStorage — cleared when tab closes
sessionStorage.setItem("key", "value");
```

### Geolocation API

```javascript
navigator.geolocation.getCurrentPosition(
  pos => console.log(pos.coords.latitude, pos.coords.longitude),
  err => console.error(err)
);
```

---

## See Also

- [[concepts/html-and-css|HTML and CSS]] — the DOM that JavaScript manipulates
- [[concepts/server-side-web-development|Server-Side Web Development]] — Node.js, REST APIs, server-side JS
- [[concepts/web-security-and-devops|Web Security and DevOps]] — XSS and CSRF risks from `innerHTML`/unsanitised input
- [[sources/INF1005-web-systems-technologies|INF1005 Source Page]]
