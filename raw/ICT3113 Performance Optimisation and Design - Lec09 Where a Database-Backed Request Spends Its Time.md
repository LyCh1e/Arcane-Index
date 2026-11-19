# Lecture 09: Where a Database-Backed Request Spends Its Time

**Three contributors to connection hold time**

Presented by A/Prof Donny Soh
Programme Leader, Applied Artificial Intelligence
Programme Leader, SITxNVIDIA (SNAIC) AI Training
InfoComm Technology (ICT) Cluster
Singapore Institute of Technology

*Note: slides are numbered by PDF page order below. The printed footer numbers ("x / 21") are given in brackets where they differ from the page order; the PDF has 17 slides.*

---

## Slide 1: Title

LECTURE 09: WHERE A DATABASE-BACKED REQUEST SPENDS ITS TIME
Three contributors to connection hold time

---

## Slide 2: Where this sits, and the one question this lecture asks

- Lecture 07 tested a service whose data lived in process memory. The soak test showed why that cannot last. The usual answer is a database.
- Once a service talks to a database, the stress test usually finds the knee there. This lecture is about what to do next.
- One question: where does a database-backed request spend its time and capacity?
- The unit we will use is hold time: the time a request keeps a database connection, from borrowing it to giving it back. There are three places that time can go. Each has its own symptom, its own instrument, and its own fixes.
- Response time at the database tier = wait time + hold time. Wait time is how long a request queues for a free connection. Hold time is the time with the connection. Hold time is what we can shorten; wait time is what grows when we do not.
- You will not write SQL in this lecture. The AI does that. You will read the evidence and say what to change.

**Three causes of pressure**

1. Too many queries per request
2. Too much time per query
3. Other work while holding the connection

Numbers on the slides are illustrative unless a slide says they were measured.

*(Footer: 2 / 21)*

---

## Slide 3: Reminder from Lecture 07: the web tier scales out, the database does not

*[Diagram, labelled PRODUCTION: a Load balancer feeds Web server 1, Web server 2 and Web server 3. All three web servers connect to a single Database server.]*

Three web servers behind a load balancer, one database. Expected load: L requests per second.

- When the web tier is the bottleneck, you add a fourth server. The load balancer spreads the work and the knee moves.
- There is one database. Every request touches it, usually several times. Adding web servers does not move its knee. It sends it more work.
- So in most services, when the stress test finds the knee, the database is the resource at its limit.
- That is why this lecture exists. Not to make you a database administrator, but because the knee is usually here.

*(Footer: 3 / 21)*

---

## Slide 4: The pool turns hold time into waiting: a queue with c servers

From the last slide: one database, and a request can only use it while holding a connection. There is a fixed number of connections.

- Opening a database connection is slow, so a service keeps a pool of open ones. A request borrows a connection, does its database work, gives it back. Pool size is c.
- That is the queue from Lecture 04. c servers, arrival rate λ, and S is the hold time: how long a request keeps the connection.
- Utilisation = λ × S / c. Ceiling = c / S.
- Pool of 10, hold time 400 ms: ceiling 25 requests per second.
- Close to the ceiling, requests wait for a connection before the database sees them. Response time climbs while database CPU stays low, because the database is idle while requests queue outside it.

### What it looks like when the pool is the problem

What you see is wait time. What causes it is hold time.

| Where you see it | What it tells you |
|---|---|
| Users: response time rises, but database CPU stays low | Requests are waiting for a connection, not for the database. The database is idle while they queue outside it. |
| Pool metrics: wait time climbing, then "could not get connection" errors | The pool is the queue. Wait time is its length in time. The errors mean the queue has a limit and it was reached. |
| After adding web servers: response time gets worse, not better | More pools, same database. Its connection limit is hit. |

The reflex is a bigger pool. That lets more requests into the database at once, which helps until the database itself is the limit, and then makes every query slower. The durable fix is a shorter hold time. The slide after next says what hold time is made of, and that is where the fixes are.

*(Footer: 4 / 21)*

---

## Slide 5: Little's Law on the pool, with illustrative numbers

From the last slide: ceiling = connections ÷ hold time. Here is what that does to throughput.

| Pool size c | Hold time S | Ceiling c / S | At 20 req/s, utilisation | What happens |
|---|---|---|---|---|
| 10 | 400 ms | 25 /s | 0.80 | Close to the ceiling. Response time several times S. |
| 10 | 100 ms | 100 /s | 0.20 | Comfortable. Same pool, query made 4x faster. |
| 40 | 400 ms | 100 /s | 0.20 | Comfortable at the pool. But 40 queries at once on the database: is each still 400 ms? |
| 10 | 40 ms | 250 /s | 0.08 | Comfortable. 200 queries collapsed into 1. |

- From slide 2: response time = wait time + hold time. The table shows hold time and the ceiling it sets. Wait time appears when you get near that ceiling (row 1).
- Rows 2 and 3 reach the same ceiling. Row 2 did it by making the query cheaper; row 3 by letting four times as many queries run at once. Row 3 only works if the database has the headroom, and the stress test is how you find out.
- Row 4 is cause 1. Fewer queries cut hold time more than any index can.
- Little's Law on that queue: requests waiting = λ × wait time. So if the pool reports 5 requests waiting at 20 per second, each waits 5 ÷ 20 = 250 ms before its first query runs.

**The thing to remember.** S is the time a request holds the connection, not the time the database works. Shortening S is what moves the ceiling. The pool size is the last knob, not the first.

*(Footer: 5 / 21)*

---

## Slide 6: Connection hold time, and its three contributors

From the last slides: hold time sets the ceiling. So what is hold time made of?

- A service keeps a pool of open database connections. A request borrows one, uses it, returns it. Pool libraries call borrowing "checking out", like a library book. Hold time is the time between borrowing and returning.
- For one request: hold time = sum of database-call elapsed times + other time while the connection is still borrowed. A call to the database is a query, so from here on: queries.
- If the N queries take roughly the same time:
- **hold time ≈ N × average time per query + other time while borrowed**
- That is the rest of the lecture. Three contributors to hold time, each with its own instrument and its own fixes.

| # | Contributor | Detail |
|---|---|---|
| 1 | Too many queries per request | N is large. Instrument: the query log. |
| 2 | Too much time per query | The average per query is large. Instrument: the plan. |
| 3 | Other work while holding the connection | Waiting on a payment API between queries, for example. Instrument: pool metrics, hold time against query time. |

Query count and time per query combine by multiplying, not adding; the other time adds on top. A later slide covers what changes when the data is huge; that is not a fourth contributor, it is a different scale for the second.

*(Footer: 6 / 21)*

---

## Slide 7: 1. Too many queries per request

```python
# generated code, and it works
orders = db.query('SELECT ... FROM orders WHERE customer_id = ?', cid)
for o in orders:
    o.items = db.query('SELECT ... FROM order_items WHERE order_id = ?', o.id)
# 1 query for the list, then 1 per order. People call this N+1.
```

```sql
-- the fix: one query
SELECT o.order_id, i.product_id, i.qty
FROM orders o LEFT JOIN order_items i ON i.order_id = o.order_id
WHERE o.customer_id = ?
```

1. **The task**
   - Show one customer's orders and what was in each one.
2. **What the code does**
   - One query fetches the 200 orders. Then, for each order, another query fetches its items. 1 query becomes 201. An ORM (a library that writes SQL for you, such as Django ORM, SQLAlchemy or Hibernate) does this by default when code touches order.items inside a loop.
3. **Why it is hard to spot**
   - EXPLAIN on any one of the 201 queries looks fully optimised: index lookup, one row. Plan reading will not catch it. The query log will: it shows 201 queries for one request.
4. **The fix**
   - One query with a JOIN. The database matches orders to items itself and returns everything at once. LEFT JOIN, so that an order with no items still appears, as it did in the loop. In ORM terms this is called eager loading.

**Why it matters**

- Each database round trip adds overhead and latency, however small the query. The database has to receive it, parse it, choose a plan, run it and send the result back. For a one-row lookup that overhead is more than the lookup. Then there is the travel: on the same machine almost nothing, so 201 queries take about 25 ms; on machines 1 ms apart, 200 ms of travel alone; with the database in another region, 20 ms away, 4 seconds. And the connection is held for the whole loop. In the equation, N went from 2 to 201. Making each query faster does not help.

*(Footer: 8 / 21)*

---

## Slide 8: 2. Too much time per query. First: which queries matter?

- A service runs many different queries. A few of them cause most of the database's work.
- Lecture 03 gave you the list: each query, how often it runs, how long each run takes. Multiply runs per second by elapsed time per run. That is the query's total elapsed time per second. It is not CPU time: queries overlap, and elapsed time includes waiting.
- Sort by that number. The top three or four usually add up to more than half of all the database's time. Those are the queries you work on. Leave the rest alone.
- A query that runs once a night and takes 10 seconds is not a problem. A query that takes 5 ms and runs 500 times a second adds up to 2.5 seconds of query time every second. That one is.

### Illustrative numbers

| Query | Runs per second | Elapsed time per run | Total query elapsed time per second |
|---|---|---|---|
| Get order by id | 500 | 5 ms | 500 × 5 ms = 2.5 s |
| List orders for a customer | 50 | 40 ms | 50 × 40 ms = 2.0 s |
| Monthly revenue report | 0.01 | 3 s | 0.01 × 3 s = 0.03 s |
| Search products | 20 | 15 ms | 20 × 15 ms = 0.3 s |

The report looks like the slow one. It is not the problem. The two at the top are. Fixing "get order by id" from 5 ms to 1 ms saves more than fixing the report from 3 s to 0.3 s.

*(Footer: 9 / 21)*

---

## Slide 9: 2. Before the three causes: how the database runs a query

*[Diagram, three stages left to right:]*

| Parse | Optimise | Execute |
|---|---|---|
| SQL becomes a tree. Names checked. | The database considers the ways it could get the answer, estimates the cost of each from statistics about the data, and picks the cheapest estimate. | The chosen plan runs. This is where the time goes. |

The SQL says what you want, not how to get it. The database picks the how from statistics it keeps: how many rows, how many distinct values in each column, and where available how the values are spread. When the available statistics do not capture the skew, the row estimate can be wrong.

A slow query has one of three causes.

- 2.1 Missing index: the database had no cheaper option.
- 2.2 Wrong estimate: it had a cheaper option but its row count guess led it to the wrong plan.
- 2.3 Query written so the index cannot be used.

The plan tells you which. The next slide is how to read one.

*(Footer: 10 / 21)*

---

## Slide 10: 2. Before the three causes: reading a plan (MySQL 8)

Type EXPLAIN ANALYZE in front of a query and run it. This is MySQL 8.0.18 or later; PostgreSQL has the same command with different output, and SQL Server calls it the actual execution plan. The database runs the query and prints one line per step.

```
EXPLAIN ANALYZE SELECT order_date, total_amount FROM orders WHERE customer_id = 7 AND order_date >= '2025-07-01'
-> Filter: order_date >= '2025-07-01'               (rows=50000)   (actual time=4..95   rows=17000   loops=1)
    -> Index lookup on orders (customer_id = 7)     (rows=150000)  (actual time=4..90   rows=70000   loops=1)
```

Reading one line: the first `rows=` is what the database expected. `actual time=a..b`: first row out at a ms, last row out at b ms. The `rows=` after actual is what it really got. `loops=` is how many times the step ran.

### Where the numbers come from

- The plan is a tree. An indented line is a child of the line above it and runs first, handing its rows up. Read from the most indented line outward.
- Expected: orders has 1,500,000 rows and 10 distinct customer ids, so the database assumes 1,500,000 ÷ 10 = 150,000 per customer. The date range covers a third of the dates, so 150,000 ÷ 3 = 50,000 after the filter.
- Actual: this customer has 70,000 orders, and 17,000 of them are in the date range.
- Time: the index lookup finished at 90 ms. The Filter finished at 95 ms. MySQL's times for a step include the steps under it, so subtracting gives roughly the Filter's own added time: about 5 ms. Approximate, and only this simple for a plain parent and child.

### Three things to ask of any plan

1. **Which step took the time?**
   A step's time includes the steps under it, so its own added time is roughly its finish time minus the finish time of the step below. Index lookup: 90 ms. Filter: 95 − 90 ≈ 5 ms. The index lookup took the time.
2. **Why is that step slow?**
   Did it read the whole table or use an index? How many rows did it touch? How many times did it run (loops)? Here: an index, but it read 70,000 rows to keep 17,000. The Filter on order_date is throwing away rows the index could have skipped. That is where to index. Next slide.
3. **Did the database expect that?**
   Compare the two `rows=` numbers. The database chose this plan because it expected 150,000. It got 70,000. Would it have chosen differently if it had known? Here, no: an index lookup is right for either number, so the wrong guess did no harm. Slide 2.2 is a case where it did.

Plain EXPLAIN gives the expected numbers without running the query. Use it when the query takes an hour. Otherwise use EXPLAIN ANALYZE.

*(Footer: 11 / 21)*

---

## Slide 11: 2.1 Missing index

- An index is an ordered structure over one or more columns, with a pointer from each entry back to its row. Finding a value in an ordered structure is fast, like finding a name in a phone book. Without one, the only way to find a customer's orders is to read every row.
- Same query as the last slide, same table: 1,500,000 orders, this customer has 70,000, and 17,000 of those are in the date range.
- Without an index on customer_id: read all 1,500,000 rows, keep 17,000. With an index on customer_id: jump to this customer's 70,000 rows, keep 17,000. With an index on (customer_id, order_date): jump straight to the 17,000.
- Which column: the ones the query filters or joins on. Here customer_id first, because it cuts the most. Then run EXPLAIN ANALYZE again. If the plan still shows a table scan, the optimiser estimated the scan was cheaper; find out why before deciding whether to keep the index.
- The cost: every new order must also be written into every index on the table, so each index makes writes slower. Index for the few queries that matter, and no more.

### Same query, three plans, rows read

**No index: table scan**

```
-> Filter: customer_id = ? AND order_date >= ?
    -> Table scan on orders     (actual rows=1500000)
```

**Index on (customer_id)**

```
-> Filter: order_date >= ?
    -> Index lookup on orders      (actual rows=70000)
```

**Index on (customer_id, order_date)**

```
-> Index range scan on orders (actual rows=17000)
   (no filter step needed)
```

| Plan | Rows read | Rows kept |
|---|---|---|
| Table scan | 1,500,000 | 17,000 |
| Index on customer_id | 70,000 | 17,000 |
| Index on (customer_id, order_date) | 17,000 | 17,000 |

*(Footer: 12 / 21)*

---

## Slide 12: 2.2 Wrong estimate, wrong plan

- Without better statistics, the database estimates row counts from averages, as the plan-reading slide showed: rows ÷ distinct values. That is fine when the values are spread evenly, and wrong when a few values dominate.
- Same table: 1,500,000 orders. The status column has 5 values, so the database expects 1,500,000 ÷ 5 = 300,000 rows for any status. In fact 1,200,000 orders are 'delivered' and 'cancelled' is 30,000.
- Ask for the delivered orders. Expecting 300,000, the database picks an index lookup on status, which is right for 300,000: jump to the rows, fetch each one. It gets 1,200,000, and fetches each one. Reading the whole table in order would have been faster.
- Why this guess mattered and the one on the plan-reading slide did not. The database had two plans to choose from: the index lookup, which fetches matching rows one at a time, and a table scan, which reads all 1,500,000 rows in order. Fetching one row at a time costs more per row. Suppose benchmarking shows a scan is cheaper above about 750,000 matching rows, half the table. The index lookup is right for 300,000. Had the database known it was 1,200,000, it would have chosen the scan. On the plan-reading slide, 150,000 and 70,000 are both well under 750,000, so it would have chosen the index lookup either way.

**Expected 300,000, got 1,200,000**

```
-> Index lookup on orders using ix_status (status = 'delivered')
       (rows=300000)   (actual rows=1200000 loops=1)
```

- **How you see it.**
  - On the step that took the time, the expected rows and the actual rows are far apart: rows=300000 against actual rows=1200000.
- **The fix.**
  - Tell the database how the values are really spread: a histogram on status (`ANALYZE TABLE orders UPDATE HISTOGRAM ON status`). Now it expects 1,200,000 for delivered and 30,000 for cancelled, and picks a scan for one and a lookup for the other. Check the plan after.
- **Why this matters for testing.**
  - Test data with every status equally common never shows this. The plan that is right for the test data is wrong for production. Test data must have the real skew in it.

*(Footer: 13 / 21)*

---

## Slide 13: 2.3 Query written so the index cannot be used

The index exists in all three. The query is written so the database cannot use it, or can only use it the hard way. The plan tells you which: a Scan where you expected an index lookup, or a huge `rows=` on an index step.

| What the code wrote | What the plan shows | Why | The fix | Rows read |
|---|---|---|---|---|
| `WHERE DATE(order_date) = '2025-10-15'` | Scan on orders, rows=1,500,000 | The index stores order_date. DATE(order_date) is a different value, so the database computes it for every row. | `WHERE order_date >= '2025-10-15' AND order_date < '2025-10-16'`. The column on its own; the index finds the range. | 1,500,000 → 2,000 |
| `WHERE legacy_code = 4242` (legacy_code is VARCHAR) | Scan on products, rows=5,000 | Number against text. Every stored string is converted to a number first, so the index order no longer applies. No error, right rows back. | `WHERE legacy_code = '4242'`. Same type on both sides. | 5,000 → 1 |
| `ORDER BY order_date LIMIT 20 OFFSET 400000` | Index scan, rows=400,020 | The index is used, but OFFSET means produce 400,020 rows and throw away 400,000. There is no way to jump to row 400,000. | `WHERE order_date > :last_seen ORDER BY order_date LIMIT 20`. Start where the last page ended. | 400,020 → 20 |

Tables: orders (1,500,000 rows, index on order_date) and products (5,000 rows, index on legacy_code).

All three are what generated code writes by default, because that is what the tutorials show. All three pass the tests on a table of 200 rows.

*(Footer: 14 / 21)*

---

## Slide 14: 3. Other work while holding the connection

```python
# generated code, and it works
with db.transaction() as tx:                      # borrow a connection
    order = tx.query(SELECT..FOR UPDATE)          # 2 ms, locks row
    receipt = payment_api.charge(...)             # 300 ms, external call
    tx.execute(UPDATE orders ...)                 # 3 ms
# return it. Held 305 ms
```

```python
# the fix: three short steps
with db.transaction() as tx:                      # 1. reserve, 5 ms
    tx.execute(UPDATE orders SET status='PROCESSING'
               WHERE id=? AND status='UNPAID')    # stops a 2nd attempt
receipt = payment_api.charge(..., key=order_id)
                                                  # 2. 300 ms, nothing held
with db.transaction() as tx:                      # 3. finalise, 3 ms
    tx.execute(UPDATE orders SET status='PAID' ...)
# Held 8 ms in total
```

| | Hold time | Of which database | Pool of 10: ceiling |
|---|---|---|---|
| Before | 305 ms | 5 ms | 10 ÷ 0.305 ≈ 33 /s |
| After | 8 ms | 8 ms | 10 ÷ 0.008 ≈ 1,250 /s |

- **What the code does**
  - A transaction borrows a connection when it opens and returns it when it closes. Everything inside runs while the connection is held, including a 300 ms call to a payment service. The pool counts the whole 305 ms: ten connections, 33 requests per second. The database did 5 ms of work. EXPLAIN ANALYZE says both queries are fine, and they are.
- **What the original gets right**
  - SELECT ... FOR UPDATE locks the order row until the transaction closes, so two requests cannot both charge the same order. Just moving the charge outside the transaction would lose that. Step 1 keeps it: only the request that changed UNPAID to PROCESSING goes on to charge.
- **What no transaction can do**
  - Undo an external charge. In either version, if the charge succeeds and the database write fails, the customer has paid. With the fix, the order is left at PROCESSING. A background job finds those and asks the provider, using the same idempotency key, so a retry cannot charge twice.
- **What the ceiling means**
  - 1,250 per second is the pool's ceiling, not the system's. The payment provider at 300 ms a call is the next bottleneck. The stress test finds it.

*(Footer: 15 / 21)*

---

## Slide 15: The pattern behind the fix: a saga

From the last slide: one transaction became three short steps plus a recovery job. That shape has a name.

- A saga is a series of small transactions T1, T2, ... Tn, each committed on its own.
- Each one has a compensating transaction C1, C2, ... Cn that undoes it.
- Two possible outcomes: T1, T2, ... Tn all succeed, or T1, ... Tj fail at step j and the saga runs Cj-1, ... C1 to back out.
- Nothing holds a lock or a connection across steps. That is why hold time stays short.
- The cost: between steps the system is in an intermediate state (hotel booked, no car yet), and the code must handle it.

### The standard example: book a trip

*[Diagram: three transactions in sequence, each with a dashed arrow to its compensating transaction.]*

| Transaction | Compensating transaction |
|---|---|
| T1 Book hotel | C1 Cancel hotel |
| T2 Book car | C2 Cancel car |
| T3 Book flight | C3 Cancel flight |

Flight fails at T3: run C2 then C1. The trip is gone, nothing is half-booked. If every T succeeds, no C runs.

### Back to the payment on the last slide

- T1 reserve the order (UNPAID to PROCESSING). T2 charge the card. T3 record PAID.
- T2 fails: C1 sets the order back to UNPAID. T3 fails after T2 succeeded: the recovery job either finishes T3, or runs C2, a refund. The idempotency key is what makes retrying T2 safe.
- The original single transaction looked simpler. It was a saga with the compensations missing.

*(Footer: 16 / 21)*

---

## Slide 16: The method: spot the pressure, find the cause, fix it, check again

From the last slide: three terms, three instruments. Here is the order you use them in.

| Step | Instrument | What it tells you |
|---|---|---|
| Spot the pressure | Stress test | The knee, from Lecture 07. Then which resource ran out: web CPU has headroom; database CPU or disk is at its limit (cause 1 or 2), or the database is idle but the pool is full and requests wait for a connection (cause 3). |
| Find its cause | Query log | How many queries one request sends. Cause 1. |
| | Plan (EXPLAIN ANALYZE) | How much work one query does. Cause 2. |
| | Pool metrics | Hold time against query time. Cause 3. |
| Choose the fix | The cause decides it | Fewer queries, less time per query, or less other work while holding the connection. |
| Check the knee moved | Stress test again | If it did not, the database was not the bottleneck, or you fixed the wrong cause. |

Three instruments for three causes. The mistake to avoid is going straight to the plan when the problem is in the query log or the pool. The plan cannot see those two.

*(Footer: 7 / 21)*

---

## Slide 17: Summary

**One number: hold time**

- The time a request keeps a database connection.
- A pool of c connections serves at most c ÷ hold time requests per second.
- Shorten hold time and the ceiling rises. A bigger pool only pushes the limit into the database.

**Three contributors**

- hold time ≈ number of queries × time per query + other work while borrowed.

**Three places to look**

- Too many queries? Count them in the query log.
- One query slow? Run EXPLAIN ANALYZE on it.
- Connection held longer than the queries take? Compare hold time with query time in the pool's metrics.

**Three fixes**

- Too many queries: one query that joins, instead of a loop.
- Slow query, three causes: missing index, add one on the column the plan filters on. Wrong estimate, give it a histogram. Query written so the index cannot be used, rewrite it.
- Held too long: split into short transactions around the slow work, and keep the guarantee the long one gave you (a saga).

**How you go about it**

- Stress test. Find the knee.
- Check the database is the resource at its limit.
- Look in the three places. See which contributor is large.
- Fix that one. Stress test again.
- Knee did not move? Not the database, or not that contributor.

**Next**

- The model has a ceiling of its own. LLM inference performance, and what the code around the model controls.

*(Footer: 17 / 21)*
