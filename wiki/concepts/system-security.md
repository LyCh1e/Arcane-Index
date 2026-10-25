---
type: concept
title: "System Security — Attacks Across the Stack"
domain: secure-software-development
status: established
created: 2026-10-25
updated: 2026-10-25
sources: [inf2005-csf-system-security]
tags: [system-security, hardware-attacks, spectre, vm-escape, hypervisor, privilege-escalation, rootkit, ransomware, wannacry, ld-preload, inf2005]
---

# System Security — Attacks Across the Stack

A computing system is an integrated combination of hardware, software and data. Vulnerabilities and exploits routinely **cross layer boundaries**, so defenders must understand the full stack from hardware up to application software.

**Von Neumann architecture** separates the CPU, I/O devices and main memory. The defining characteristic — memory holds both data *and* instructions — is what makes injection and control-flow attacks possible.

---

## Attack Layers

```
Applications
System Software  (package managers, dynamic linker)
Operating System (kernel, kernel modules)
Hypervisor       (Type-1, Type-2, OS-level)
Software         (user-space programmes)
Hardware         (CPU, DRAM, peripherals)
```

---

## 1. Hardware Attacks

| Attack | Description | Examples |
|---|---|---|
| **Counterfeit** | Malicious or tampered hardware components distributed in the supply chain | Hardware trojans with backdoors; compromise during manufacturing; a dropped USB that emulates keyboard input |
| **Fault injection** | Physically tampers with hardware to alter device operation | Voltage glitching; clock glitching; periodic electromagnetic pulses; changing CPU instructions |
| **Micro-architectural** | Targets the CPU implementation below the ISA | Speculative execution attacks (Spectre); DRAM rowhammer for privilege escalation |

### Case Study: Spectre

- A **speculative execution** timing side-channel attack that reads arbitrary memory across process boundaries.
- **Root cause:** modern CPUs speculatively execute instructions while waiting for memory fetches. If the guess is wrong the CPU rolls back, but the speculative work leaves microarchitectural traces (cache state) that can be measured via timing.
- **Why it matters:** Spectre is a *design flaw* in the CPU itself. There is no easy hardware fix; most mitigations are expensive software patches (e.g. KPTI/retpoline) that reduce performance.
- Hardening effort was significant in 2018 across virtually all OS and hypervisor vendors.

---

## 2. Software Attacks

### Control Flow Attacks

Divert a programme's intended control flow to execute malicious code.

| Technique | Mechanism |
|---|---|
| **Stack smashing** | Overwrite the return address on the call stack via a buffer overflow |
| **Return-oriented programming (ROP)** | Chain together existing code *gadgets* (sequences ending in `ret`) to construct malicious logic without injecting new code |

### Code Injection

Input passed to one programme (*generator*) produces executable code that a second programme (*executor*) runs.

### Command Injection

A subclass of code injection where attacker-supplied input reaches a **command interpreter** (shell), causing arbitrary commands to execute.

#### Example

```c
// Vulnerable: argv[i] is user-controlled
execve("/usr/bin/cat", {"/usr/bin/cat", argv[i], NULL}, envp);
```

If `argv[i]` is `/dev/null; reboot`, the shell executes both `cat /dev/null` and `reboot`.

**Defence:** never concatenate unsanitised user input into a command string; use parameterised APIs.

---

## 3. Hypervisor / Virtualisation Attacks

A **hypervisor** is the software layer that enables server virtualisation, forming an abstraction between hardware resources and the OS or containers.

| Type | Description |
|---|---|
| **Type-1 (bare-metal)** | Runs directly on hardware (e.g. VMware ESXi, Xen, Hyper-V) |
| **Type-2 (hosted)** | Runs on top of a host OS (e.g. VirtualBox, VMware Workstation) |
| **OS-level (container)** | Virtualises at the OS level (e.g. Docker, LXC) |

### Hypervisor Attack Types

| Attack | Description |
|---|---|
| **Hyperjacking** | Replaces the legitimate hypervisor with a malicious one (injected below, above, or in place of it). Extremely difficult to detect from the OS layer. |
| **VM escape** | Breaks the isolation provided by the hypervisor so a guest VM can interact with the hypervisor or host OS. Found in many popular hypervisors. |
| **VM rootkit** | A rootkit running *beneath* the OS — a special case of hyperjacking that can launch malware in separate, invisible VMs. |

### Notable VM Escape CVEs

| CVE | Product | Detail |
|---|---|---|
| **CVE-2015-3456 (VENOM)** | QEMU (Xen < 4.5.x, KVM) | Local guest users exploit the **virtual floppy disk controller** (`FD_CMD_READ_ID`) to cause an out-of-bounds write and potentially execute arbitrary code on the host |
| **CVE-2017-4907** | VMware Workstation | Flaw in the **3D acceleration** feature allows guest-to-host code execution |
| **CVE-2020-3960** | VMware | **Uninitialised stack memory** allows a guest to escape to the host |

---

## 4. Operating System Attacks

### Loadable Kernel Module Attack

Loadable kernel modules (drivers, network protocol stacks) can be used to inject malicious code into the kernel. On **monolithic kernels**, a malicious module has nearly unlimited access to all running programmes.

### Kernel Rootkit Attack

Installs a rootkit within the OS kernel, with or without prior privilege escalation. Kernel rootkits are very difficult to detect from within the running OS — a **complete reinstallation** is usually required.

### Privilege Escalation

Gains access to resources normally protected from unprivileged users.

| Type | Description |
|---|---|
| **Horizontal** | Gains access to **another user's account at the same privilege level** to reach their assets |
| **Vertical** | **Raises privileges** of a compromised account to administrator or root level — potentially giving complete system control |

Some operating systems confine processes in restricted environments called **jails** (e.g. FreeBSD jails, Linux namespaces). Privilege escalation can be used to escape these environments (**jailbreaking**).

#### Typical Attack Chain

1. Execute an initial exploit to gain **unprivileged access** to the system.
2. Execute a privilege escalation exploit to gain **root or kernel-level access**.
3. Install a **persistent rootkit** that provides backdoors and hides the attacker's presence.
4. Use the system to **exfiltrate data, block access, or launch further attacks**.

---

## 5. System Software Attacks

### Dynamic Linking Attack

Manipulates the dynamic linker to load malicious libraries at programme startup.

- On Linux, the **`LD_PRELOAD`** environment variable specifies libraries that are loaded *before* any other system libraries. An attacker who can set this variable can intercept any library call.

### Package Management Attack

Modifies a package manager to accept malicious packages.

Methods:
- Use malicious signing keys to validate packages.
- Create malicious packages signed with those keys.
- Exploit bugs in the package manager itself.

### Ransomware

A **crypto-virology** attack that permanently blocks access to the victim's data.

Characteristics:
- Encrypts files with a random key (the victim cannot decrypt without paying).
- **Also targets backups** to maximise pressure.
- Advanced variants **exfiltrate data before encrypting** and threaten to publish it (*double extortion*).

#### Case Study: WannaCry (2017)

| Fact | Detail |
|---|---|
| **Spread** | Over 200,000 computers in over 150 countries in under 2 days |
| **Payment** | Ransom demanded in Bitcoin (difficult to trace) |
| **Vulnerability** | EternalBlue (SMBv1 exploit) — Microsoft had issued patch MS17-010 in **March 2017** |
| **Victims** | Government hospitals, legacy enterprise systems running **unsupported Windows** |
| **Lesson** | A known, patched vulnerability became a global incident purely because organisations failed to apply patches |

---

## Defensive Principles

| Principle | Practice |
|---|---|
| Patch promptly | WannaCry exploited a patched vulnerability; delay = exposure |
| Defence in depth | No single layer is sufficient; secure every layer |
| Least privilege | Limit what each process and user can do to reduce the blast radius of a compromise |
| Input validation | Prevents command injection and many control-flow attacks |
| Integrity verification | Sign packages, verify firmware; detect counterfeit hardware |
| Assume breach | Plan detection and response, not just prevention |

---

## Related Pages

- [[concepts/malware]] — malware types that exploit system vulnerabilities (rootkits, ransomware, trojans)
- [[concepts/access-control]] — privilege rings, protection levels
- [[concepts/ethical-hacking]] — penetration testing at the system layer
- [[concepts/secure-input-validation]] — preventing injection attacks
- [[sources/inf2005-csf-system-security]] — source lecture notes
