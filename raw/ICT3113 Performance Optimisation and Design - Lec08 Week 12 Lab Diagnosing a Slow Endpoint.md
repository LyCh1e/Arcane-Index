# Week 12 Lab: Diagnosing a Slow Endpoint (accompanies Lecture 08)

Presented by A/Prof Donny Soh
ICT3113 Performance Optimisation and Design
InfoComm Technology (ICT) Cluster, Singapore Institute of Technology

*(Slide 1 of 8)*

---

## Lab: Diagnosing a slow endpoint

1. Read the case on the next slide first. All four questions use it.
2. Answer using the Lecture 08 content. The formulas and notation you need are on the reference slide at the end of this deck.
3. State the unit of measurement in every answer and in every step of your working. An answer without units is incomplete.
4. Say which piece of evidence each conclusion rests on. The method matters more than the final number.

The four questions are the four steps of the Lecture 08 method. Each one narrows down where the time goes.

| Question 1: Spot the pressure | Question 2: Find its cause | Question 3: Choose the fix | Question 4: Check the knee moved |
|---|---|---|---|
| Which resource is at its limit: the database or the pool? | Use the query log, the plan and the pool metrics. Which of the three causes is dominant? | The cause decides the fix. Why not a bigger pool? | Predict the pool metrics after the fix, then stress test again. |

*(Slide 2 of 8)*

---

## The case: an AI-generated endpoint is slow

`GET /customers/{id}/summary` returns a customer's recent orders with a payment check. The stress test put the knee at **18 requests per second**, below the target of **40**. Database CPU at the knee: **22%**.

### Query log, one request

```
12:04:11.002  SELECT ... FROM customers WHERE id=?
12:04:11.004  SELECT ... FROM orders WHERE customer_id=?
              ORDER BY order_date DESC LIMIT 20
12:04:11.009  SELECT ... FROM order_items WHERE
              order_id IN (?,?,...)
12:04:11.012  UPDATE customers SET last_seen=?
              WHERE id=?

4 queries, 10 ms of database time
```

### Pool metrics, at the knee

| Metric | Value |
|---|---|
| pool size | 10 |
| avg hold time | 480 ms |
| avg wait for conn | 310 ms |
| avg query time/req | 10 ms |
| connections in use | 10 / 10 |

### Plan of the biggest query

```
-> Limit: 20 row(s)
    -> Index lookup on orders using
       ix_cust_date (customer_id=?)
       (rows=20) (actual rows=20 loops=1)

expected 20, actual 20, 3 ms
```

- **Query log:** every query one request sent, with the time it was sent.
- **Pool metrics:** averages over the stress test at 18 requests per second. Pool size is *c*. Hold time is *S*.
- **Plan:** EXPLAIN ANALYZE on the orders query, the slowest of the four.

*(Slide 3 of 8)*

---

## Question 1: Spot the pressure

The knee is at 18 requests per second, below the target of 40. Before looking for a cause, find which resource ran out.

### Pool metrics, at the knee

| Metric | Value |
|---|---|
| pool size | 10 |
| avg hold time | 480 ms |
| avg wait for conn | 310 ms |
| avg query time/req | 10 ms |
| connections in use | 10 / 10 |

Hold 480 ms, queries 10 ms.

From the stress test: database CPU at the knee is 22%.

From the pool metrics, calculate:

1. the ceiling of the pool
2. the utilisation of the pool at the knee
3. the average number of requests waiting for a connection
4. the average time from asking for a connection to giving it back
5. Which resource is at its limit: the database or the pool? Which of the three causes does that point to?

*(Slide 4 of 8. Step tracker: 1. Spot the pressure, 2. Find its cause, 3. Choose the fix, 4. Check the knee moved. Step 1 highlighted.)*

---

## Question 2: Find its cause

From Question 1: the pool is at its limit, the database is not. Now check each cause with its own instrument.

### Query log, one request

```
12:04:11.002  SELECT ... FROM customers WHERE id=?
12:04:11.004  SELECT ... FROM orders WHERE customer_id=?
              ORDER BY order_date DESC LIMIT 20
12:04:11.009  SELECT ... FROM order_items WHERE
              order_id IN (?,?,...)
12:04:11.012  UPDATE customers SET last_seen=?
              WHERE id=?

4 queries, 10 ms of database time
```

### Plan of the biggest query

```
-> Limit: 20 row(s)
    -> Index lookup on orders using
       ix_cust_date (customer_id=?)
       (rows=20) (actual rows=20 loops=1)

expected 20, actual 20, 3 ms
```

Formula: hold time ≈ N × average time per query + other time while borrowed

1. **Query log:** how many queries does one request send, and how long do they take in total? Is it cause 1, too many queries per request?
2. **Plan:** is the biggest query slow, or does it read more rows than it returns? Is it cause 2, too much time per query?
3. **Pool metrics:** hold time is 480 ms. How much of it is other time while borrowed? Is it cause 3?
4. Which cause is dominant?

*(Slide 5 of 8. Step 2 highlighted.)*

---

## Question 3: Choose the fix

From Question 2: the cause is other work while holding the connection, about 470 ms of the 480 ms hold time. The cause decides the fix.

1. What would you ask the AI to change? Which business rules must still hold, and how would you check that the transaction can safely end before the payment check?
2. A teammate proposes a pool of 30 instead, with no code change. Calculate the ceiling of the pool, and its utilisation at 40 requests per second.
3. Does the pool of 30 reach the target of 40 requests per second? Give two things it does not fix.

*(Slide 6 of 8. Step 3 highlighted.)*

---

## Question 4: Check the knee moved

From Question 3: assume the other work can safely run before the connection is borrowed, so other time while borrowed goes from 470 ms to 0 ms. Pool size stays at 10.

**Predict, after the fix:**

1. the average hold time, using hold time ≈ N × average time per query + other time while borrowed
2. the ceiling of the pool
3. the utilisation of the pool at 40 requests per second
4. the average wait for a connection

**Then answer:**

5. Does one request now finish in about 10 ms? Explain.
6. Where do you expect the knee to go, and how do you check?

*(Slide 7 of 8. Step 4 highlighted.)*

---

## Reference: formulas and notation

Use these where needed. Each is covered in Lecture 08.

### The pool as a queue

| Quantity | Formula |
|---|---|
| Utilisation | λ × S / c |
| Ceiling | c / S |
| Little's Law | requests waiting = λ × wait time |

### Hold time

For one request:

hold time = sum of query elapsed times + other time while borrowed

If the N queries take roughly the same time:

hold time ≈ N × average time per query + other time while borrowed

### Notation

| Symbol | Meaning |
|---|---|
| c | pool size (connections) |
| S | hold time: borrowing a connection to giving it back |
| λ | arrival rate (requests per second) |
| N | queries per request |

### Three causes, three instruments

| Cause | Instrument |
|---|---|
| 1. Too many queries per request | Query log |
| 2. Too much time per query | Plan (EXPLAIN ANALYZE) |
| 3. Other work while holding the connection | Pool metrics |

*(Slide 8 of 8)*
