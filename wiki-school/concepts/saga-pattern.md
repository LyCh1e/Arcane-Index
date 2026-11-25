---
type: concept
title: "Saga Pattern (Short Transactions with Compensation)"
address: c-000139
aliases: ["saga", "compensating transaction", "idempotency key", "split transaction around slow external call"]
domain: performance-engineering
complexity: medium
status: established
created: 2026-11-19
updated: 2026-11-19
tags: [ict3113, saga, compensating-transaction, idempotency, transactions, hold-time, database, distributed-systems]
---

# Saga Pattern

**Cause 3 of connection hold time** is other work done while a connection is borrowed. The fix splits one long transaction into short ones, and the shape of that fix is a **saga**. Source: [[ict3113-pod-l9-database-request-time]] (slides 14 and 15).

## The problem: a slow call inside a transaction

```python
with db.transaction() as tx:                  # borrow a connection
    order = tx.query(SELECT..FOR UPDATE)      # 2 ms, locks the row
    receipt = payment_api.charge(...)         # 300 ms, external call
    tx.execute(UPDATE orders ...)             # 3 ms
# return it. Held 305 ms
```

The connection is held for the whole 305 ms although the database did 5 ms of work. `EXPLAIN ANALYZE` says both queries are fine, and they are. The instrument is the **pool metrics** (hold time against query time).

## The fix: three short steps

```python
with db.transaction() as tx:                  # 1. reserve, 5 ms
    tx.execute(UPDATE orders SET status='PROCESSING'
               WHERE id=? AND status='UNPAID')   # stops a second attempt
receipt = payment_api.charge(..., key=order_id)  # 2. 300 ms, nothing held
with db.transaction() as tx:                  # 3. finalise, 3 ms
    tx.execute(UPDATE orders SET status='PAID' ...)
# Held 8 ms in total
```

| | Hold time | Of which database | Pool of 10: ceiling |
|---|---|---|---|
| Before | 305 ms | 5 ms | 10 ÷ 0.305 ≈ 33 req/s |
| After | 8 ms | 8 ms | 10 ÷ 0.008 ≈ 1,250 req/s |

## What the original gets right, and what no transaction can do

- `SELECT … FOR UPDATE` locks the order row until the transaction closes, so two requests cannot both charge the same order. **Simply moving the charge outside the transaction would lose that.** Step 1 keeps it: only the request that changed `UNPAID` to `PROCESSING` goes on to charge.
- No transaction can undo an external charge. In either version, if the charge succeeds and the database write fails, the customer has paid. In the fix, the order is left at `PROCESSING`; a background **recovery job** finds those and asks the provider, using the same **idempotency key**, so a retry cannot charge twice.
- 1,250 req/s is the **pool's** ceiling, not the system's. The payment provider at 300 ms a call is the next bottleneck; the stress test finds it.

## The saga

A **saga** is a series of small transactions T1, T2, … Tn, each committed on its own, each with a **compensating transaction** C1, C2, … Cn that undoes it. Two outcomes: all of T1…Tn succeed, or T1…Tj fail at step j and the saga runs the compensations in reverse (Cj-1 … C1).

| Transaction | Compensating transaction |
|---|---|
| T1 Book hotel | C1 Cancel hotel |
| T2 Book car | C2 Cancel car |
| T3 Book flight | C3 Cancel flight |

If the flight fails at T3, run C2 then C1; nothing is half-booked. If every T succeeds, no C runs.

**Applied to the payment:** T1 reserve (UNPAID → PROCESSING), T2 charge the card, T3 record PAID.

- T2 fails: C1 sets the order back to UNPAID.
- T3 fails after T2 succeeded: the recovery job finishes T3, or runs C2 (a refund). The idempotency key makes retrying T2 safe.
- "The original single transaction looked simpler. It was a saga with the compensations missing."

## Trade-off

Nothing holds a lock or a connection across steps, which keeps hold time short. The cost is that the system passes through **intermediate states** (hotel booked, no car yet; order PROCESSING), and the code must handle them, including crashes between steps.

## Related

- [[connection-pool-diagnosis]] — the diagnosis that leads here
- [[database-indexing-transactions]] — ACID transactions and locking (INF2003)
- [[ict3113-lab-wk12-slow-endpoint-worked]] — the lab's "other work while holding the connection" case
