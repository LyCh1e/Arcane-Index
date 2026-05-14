---
type: synthesis
title: "Hardware Paging → OS Virtual Memory: The ICT1011 → ICT1012 Handover"
domain: computer-architecture × operating-systems
sources:
  - concepts/io-and-memory-systems
  - concepts/memory-and-virtual-memory
complexity: high
updated: 2026-05-14
tags: [synthesis, computer-architecture, operating-systems, paging, virtual-memory, TLB, page-replacement, thrashing, ICT1011, ICT1012]
---

# Hardware Paging → OS Virtual Memory: The ICT1011 → ICT1012 Handover

ICT1011 (Computer Organisation and Architecture) ends with a data structure: the page table, which maps logical pages to physical frames. ICT1012 (Operating Systems) begins exactly there and adds the policies that make the data structure useful. Without ICT1011's hardware foundation, the OS concepts in ICT1012 are floating abstractions. Without ICT1012's policy layer, the hardware mechanism has no purpose. This page documents the join precisely.

---

## 1. Where ICT1011 Ends

[[concepts/io-and-memory-systems|I/O Interfacing and Memory Systems]] (ICT1011) progresses through memory management in the following order:

### Fixed Partitioning
Memory is divided into fixed-size regions at system start. Each process occupies the smallest partition that fits. The problem: **internal fragmentation** — a process smaller than its partition wastes the leftover space.

### Dynamic Partitioning
Each process receives exactly the memory it needs. The problem shifts: over time, repeated allocation and deallocation creates **external fragmentation** — many small free holes scattered between processes, none large enough to be useful individually. Remedies (coalescing, compaction) are expensive.

### Paging — The ICT1011 Endpoint

Paging solves external fragmentation by abandoning the requirement for contiguous allocation. The key terms ICT1011 introduces:

| Term | Definition |
|---|---|
| **Page** | Fixed-size chunk of a process's logical address space |
| **Frame / Page frame** | Fixed-size chunk of physical memory of equal size |
| **Page table** | Per-process array mapping page number → frame number |

Address translation in ICT1011:

```
Logical address:   [ page number (p) | page offset (d) ]
                              ↓ index into page table
                         frame number (f)
                              ↓
Physical address:  [ frame number (f) | page offset (d) ]
```

Example from ICT1011: 16-bit logical address, 10-bit offset → 1024 bytes/page. Page 1, Offset 30 → Page table[1] = Frame 13 → Physical: Frame 13, Offset 30.

**ICT1011's contribution**: the static mechanism — what the data structure looks like and how one address translation works. It does not ask: where is the page table stored? How long does the translation take? What happens if the process needs more memory than is physically available?

---

## 2. The Exact Handover Point

[[concepts/memory-and-virtual-memory|Memory Management and Virtual Memory]] (ICT1012) opens with the same data structure and immediately extends it:

> The page table is stored in main memory, pointed to by the **Page Table Base Register (PTBR)**. Every memory access therefore requires two memory reads: one to fetch the page table entry, one to access the actual data.

This single observation — that the naive implementation doubles every memory access latency — is the motivation for everything that follows in ICT1012.

---

## 3. ICT1012's Extensions to the Paging Foundation

### 3.1 TLB — Translation Look-aside Buffer

The TLB is a small, fast hardware cache that holds recently used page-to-frame mappings. On a TLB hit, address translation is almost free. On a TLB miss, the full two-memory-read translation occurs and the result is added to the TLB.

**Effective Access Time (EAT)** formula from ICT1012:

```
EAT = hit_ratio × memory_access + (1 − hit_ratio) × 2 × memory_access

Example (99% hit ratio, 10 ns access time):
EAT = 0.99 × 10 + 0.01 × 20 = 10.1 ns
```

At a 99% hit ratio, TLBs reduce the penalty from doubling memory access time to a 1% overhead. **The TLB is invisible to the ICT1011 programmer** — it is a hardware optimisation of the page table mechanism ICT1011 defined.

TLBs store **Address Space IDs (ASIDs)** to avoid flushing all entries on a context switch. Without ASIDs, every process switch would cold-start the TLB, destroying the hit-ratio advantage.

### 3.2 Page Table Structures — Scaling the Mechanism

ICT1011 treats the page table as a flat array. ICT1012 notes the problem: a 32-bit address space with 4 KB pages requires 1 million page table entries — 4 MB per process just for the mapping. Three structures address this:

| Structure | Mechanism | Best For |
|---|---|---|
| **Hierarchical / Two-level** | Page table paged into outer + inner levels; unused regions have no inner table | 32-bit spaces with sparse usage |
| **Hashed page table** | VPN hashed; bucket is a linked list of (VPN, frame, next) entries | Address spaces >32-bit |
| **Inverted page table** | One global table indexed by physical frame number | Systems with limited physical memory |

The ICT1011 page table is the Level 1 / flat case of the hierarchical structure. ICT1012 generalises it.

### 3.3 Virtual Memory — Beyond Physical Capacity

ICT1011 assumes all pages of a running process are in physical memory. ICT1012 removes this restriction.

**Virtual memory**: the logical address space may be larger than physical memory. Only the pages currently needed reside in RAM; the rest remain on a backing store (disk). This is the mechanism that makes modern multi-tasking possible.

The valid-invalid bit — introduced in ICT1012 but logically extending the page table entry ICT1011 defined — distinguishes pages currently in memory (v) from pages on disk (i).

### 3.4 Demand Paging and Page Faults

When a process accesses a page marked invalid (not in memory), a **page fault** trap fires. The OS handles it in six steps:

1. Trap to OS; preserve process state
2. Verify: is this a legal address? (If not, terminate process.)
3. Find a free frame in the free frame list
4. Schedule disk read of the page into the free frame
5. Update page table entry (set valid bit to v; record frame number)
6. Restart the interrupted instruction

**Step 3 connects directly to ICT1011**: the "free frame list" is the OS's bookkeeping of which physical frames (as defined in ICT1011) are currently unoccupied. The frame concept from ICT1011 is the resource the OS allocates and reclaims.

The performance cost is severe:

```
EAT = (1 − p) × memory_access + p × (fault_overhead + swap_out + swap_in)

Typical values: memory_access = 200 ns, fault service = 8 ms
EAT = 200 + p × 7,999,800

For < 10% performance degradation: p < 1 in 400,000
```

---

## 4. Page Replacement Algorithms — OS Policy over Hardware Mechanism

When physical memory is full and a new page must be loaded, a victim page must be chosen for eviction. This is pure OS policy; the hardware only provides the dirty bit (whether the page has been modified) and the reference bit (whether it has been accessed recently).

| Algorithm | Strategy | Notes |
|---|---|---|
| **FIFO** | Evict oldest resident page | Simple; suffers Belady's anomaly (more frames → more faults possible) |
| **OPT** | Evict the page not needed for longest future time | Optimal but requires future knowledge; benchmark only |
| **LRU** | Evict least recently used | Approximates OPT; no Belady's anomaly; needs hardware support |
| **Second-chance (clock)** | FIFO with reference-bit reprieve | Practical LRU approximation; widely implemented |

**Why ICT1011 matters here**: LRU requires knowing when each frame was last accessed. The hardware mechanism that makes this possible — the reference bit in the page table entry — is an extension of the page table data structure ICT1011 defined. The OS sets and reads these bits; the hardware sets them on access. Without understanding what a page table entry contains (ICT1011), the LRU implementation in ICT1012 is mysterious.

---

## 5. Thrashing and the Working-Set Model

**Thrashing** occurs when the OS allocates too few frames to a process, causing it to page-fault continuously. The process spends more time waiting for pages to be loaded than executing instructions.

**Root cause**: the process's **working set** — the set of pages it actively uses in a given time window — does not fit in its allocated frames. Every eviction removes a page that will be needed momentarily.

The working-set model quantifies this:

$$D = \sum_i WSS_i \approx \text{total frames needed}$$

**Policy**: if D exceeds total available frames, the OS must suspend a process entirely and reclaim its frames. This is the highest-level OS memory policy decision — but it is only meaningful because ICT1011 established that a process's address space is divided into pages, that pages map to frames, and that the frame is the granular unit of physical allocation.

---

## 6. The Hardware View vs the OS View

| Aspect | ICT1011 (Hardware view) | ICT1012 (OS view) |
|---|---|---|
| What a page table is | An array: page number → frame number | A resource managed in main memory, accessed via PTBR |
| Address translation | A single worked example | A performance problem solved by TLB; formulated as EAT |
| Page table size | Fixed and flat | A scaling problem solved by hierarchical / hashed / inverted structures |
| All pages in memory | Assumed | Never assumed; managed via demand paging and page faults |
| Frame management | "Free frame list" mentioned abstractly | Actively managed: allocation policies, replacement algorithms, reapers |
| TLB | Not covered | Central to performance; EAT formula; ASIDs for multi-process correctness |

---

## 7. Dependency Chain

```
ICT1011: Fixed / Dynamic Partitioning
    ↓ problem: fragmentation
ICT1011: Paging (page, frame, page table, logical→physical address translation)
    ↓ picked up directly by ICT1012
ICT1012: PTBR — page table in main memory
    ↓ performance problem
ICT1012: TLB — EAT formula, ASID, hit ratio
    ↓ scaling problem for large address spaces
ICT1012: Hierarchical / Hashed / Inverted page tables
    ↓ exceeding physical memory
ICT1012: Virtual memory, valid-invalid bit, demand paging
    ↓ physical memory full
ICT1012: Page replacement (FIFO, OPT, LRU, second-chance)
    ↓ too many processes, too few frames
ICT1012: Thrashing, working-set model, page-fault frequency control
```

Every step in this chain depends on the previous one. Thrashing cannot be understood without page replacement; page replacement cannot be understood without demand paging; demand paging cannot be understood without the page table; the page table is ICT1011's terminal topic.

---

## See Also

- [[concepts/io-and-memory-systems|I/O Interfacing and Memory Systems]] (ICT1011) — paging data structure, address translation, SRAM/DRAM, partitioning
- [[concepts/memory-and-virtual-memory|Memory Management and Virtual Memory]] (ICT1012) — TLB, EAT, page table structures, demand paging, page replacement, thrashing
