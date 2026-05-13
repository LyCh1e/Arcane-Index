---
type: concept
title: "File Systems (Interface and Implementation)"
domain: operating-systems
source: [[sources/ICT1012-operating-systems]]
complexity: high
updated: 2026-05-13
tags: [concept, operating-systems, file-systems, storage, allocation, directory]
---

# File Systems — Interface and Implementation

Covers the user-facing file system interface (file concept, access methods, directory structures, protection) and the internal implementation (layered FS, allocation methods, free-space management).

---

## Part A: File Systems Interface

### 1. File Concept

A file is a **contiguous logical address space** — the OS's abstraction for persistent storage.

**File attributes** (stored in the directory structure on disk):
| Attribute | Description |
|-----------|-------------|
| Name | Human-readable identifier |
| Identifier | Unique inode/file number |
| Type | OS-specific (extension or magic bytes) |
| Location | Pointer to device location |
| Size | Current file size |
| Protection | Who can read/write/execute |
| Timestamps & owner | For security and audit |

**File operations**: Create, Write (at write pointer), Read (at read pointer), Seek (reposition), Delete, Truncate, **Open** (load directory entry into memory), **Close** (flush memory entry back to disk).

**Open-file table** (per OS): tracks all open files; each process has its own file pointer and access rights within this table.

---

### 2. Access Methods

| Method | Description | When to Use |
|--------|-------------|------------|
| **Sequential** | Read/write one record at a time in order; `read_next`, `write_next`, `reset` | Tape, logs |
| **Direct** (random) | Read/write block n in any order; `read n`, `write n` | Databases |
| **Indexed** | Index in memory points to disk blocks; primary and secondary indices | Large files |

---

### 3. Directory Structures

A directory is a **symbol table** mapping file names to their File Control Blocks (FCBs/inodes).

| Structure | Description | Issue |
|-----------|-------------|-------|
| **Single-level** | One directory for all users | Naming conflicts |
| **Two-level** | Separate directory per user (UFD) under master (MFD) | Isolates users |
| **Tree-structured** | Multi-level hierarchy; current working directory | Standard UNIX/Windows |
| **Acyclic graph** | Allows shared files/subdirectories (via links) | Dangling pointers if delete without tracking; solved by reference count |
| **General graph** | Allows cycles | Traversal may not terminate; requires cycle detection |

**File reference count**: the file is deleted only when count reaches 0 (last link removed).

---

### 4. File Protection — Unix Model

Unix uses a three-class permission system: **owner (u)**, **group (g)**, **others (o)** — each with **read (r)**, **write (w)**, **execute (x)** bits.

```
  rwx   rwx   rwx
  7     6     1    = chmod 761
  │     │     └── others: execute only
  │     └──────── group: read+write
  └────────────── owner: all
```

Represented numerically: r=4, w=2, x=1 → sum per class (e.g., 7=rwx, 6=rw-, 5=r-x).

Commands: `chmod`, `chown`, `chgrp`.

---

## Part B: File System Implementation

### 5. Layered File System

```
Application (user)
     │
Logical file system  ← FCBs, directory management, file name → number
     │
File-organisation module  ← logical block# → physical block#, free space
     │
Basic file system  ← "read block 123" to device driver; buffer/cache management
     │
I/O control (device driver)  ← translate high-level to low-level hardware commands
     │
Hardware (disk)
```

Layering reduces complexity and redundancy but adds overhead.

**On-disk structures**:
| Structure | Location | Contents |
|-----------|---------|---------|
| Boot control block | First block of bootable volume | OS boot info |
| Volume control block (superblock) | Per volume | Block count, free blocks, block size |
| Directory structure | Per directory | File names + inode numbers |
| FCB / inode | Per file | Permissions, size, dates, data block pointers |

---

### 6. Directory Implementation

| Method | Search | Insert/Delete | Notes |
|--------|--------|---------------|-------|
| **Linear list** | O(n) | O(1) append | Simple; slow search |
| **Ordered linked list** | O(log n) binary search | O(n) to maintain order | Better search |
| **Hash table** | O(1) | O(1) | Best performance; collisions must be handled |

---

### 7. Disk Block Allocation Methods

| Method | How it works | Pros | Cons |
|--------|-------------|------|------|
| **Contiguous** | File occupies sequential blocks; directory stores (start, length) | Best read performance (sequential + direct access); simple | Must know file size at creation; external fragmentation |
| **Linked** | Each block contains pointer to next; directory stores first block | No external fragmentation; files grow freely | Inefficient random access (must traverse chain); wasted space for pointers; reliability (damaged pointer) |
| **Indexed** | Each file has an index block (inode) containing pointers to data blocks | Supports direct access; no external fragmentation | Index block overhead; large files need multi-level indices |

**FAT (File Allocation Table)**: a variant of linked allocation where all "next block" pointers are stored in a single table at the start of the volume — can be cached in memory for fast access.

**inode (Unix)**: a fixed-size index block holding metadata and block pointers (direct, single-indirect, double-indirect, triple-indirect) — allows files to scale from small to very large.

### Performance

| Access pattern | Best allocation |
|----------------|----------------|
| Sequential | Contiguous or linked |
| Random | Indexed (or contiguous) |
| Growing files | Linked or indexed |

---

### 8. Fragmentation in File Systems

| Type | Cause | Solution |
|------|-------|---------|
| **External fragmentation** | Enough total free space exists but not contiguous | Compaction (expensive) |
| **Internal fragmentation** | Allocated block slightly larger than needed | Smaller block sizes (but larger page table) |

50% rule: for every N allocated blocks, ~0.5N are lost to fragmentation on average.

---

### 9. Free-Space Management

| Method | Description | Pros | Cons |
|--------|-------------|------|------|
| **Bit vector (bitmap)** | One bit per block: 1=free, 0=used | Easy to find contiguous free blocks; fast with hardware bit-scan instructions | Requires extra space (32 MB for 1 TB disk with 4 KB blocks) |
| **Linked list** | Free blocks linked together | No extra space needed; first free block easy to find | Cannot easily find contiguous space |

---

### 10. File System Performance

- **Buffer cache**: a section of main memory holding recently used disk blocks
- **Synchronous write**: waits until data physically written — safe, slow
- **Asynchronous write**: returns to caller after writing to cache — fast, requires OS to ensure eventual consistency

---

## See Also

- [[concepts/os-processes-and-threads|OS Fundamentals, Processes, and Threads]] — OS structure that manages the FS
- [[concepts/memory-and-virtual-memory|Memory Management and Virtual Memory]] — memory where FS buffers and caches live
- [[sources/ICT1012-operating-systems|ICT1012 Source Page]]
