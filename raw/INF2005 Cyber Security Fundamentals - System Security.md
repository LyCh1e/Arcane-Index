# (Operating) System Security

*INF2005 Cyber Security Fundamentals, Week 8 — Dr Aris Cahyadi Risdianto*

## 0. Module Logistics (Weeks 8–13)

- **Instructor:** Dr Aris Cahyadi Risdianto
- **Announcements:** updates on submissions, project deadlines and exam information
- **Online lectures:** Zoom, Mondays, weeks 8–12 (SIT / student accounts only)
- **Discussion forum:** all project questions go in the **ACW3** forum under the correct topic; emailed queries are reposted there if they contain no private or sensitive information
- **Consultation:** optional tutorial/lab hours Tue 9 AM–1 PM and Thu 9 AM–6 PM; by appointment with 1 day's notice
- **Quiz:** a live Slido quiz closes the session

---

## 1. Introduction: What is a (Computing) System?

- A computer system is **hardware and system software working together to run application programs**. Implementations change over time, but the underlying concepts do not (Bryant & O'Hallaron, *Computer Systems: A Programmer's Perspective*).
- More broadly: an integrated combination of hardware, software and data that processes input, executes instructions, stores information and produces output, usually via an **operating system**. Systems range from PCs and phones to cloud infrastructure and embedded devices.

### System Layers and Von Neumann Architecture
- **Von Neumann architecture** separates the CPU, I/O devices and main memory. The key characteristic is that **memory holds both data and instructions**.
- Adversaries can attack a system without a full view of the layers, because **vulnerabilities and exploits often cross layer boundaries**. Security specialists therefore need to understand how complex software systems are executed.

---

## 2. Attacks on the Computer System

Attacks are grouped by the layer they target: hardware, software, hypervisor, operating system and system software.

### 2.1 Hardware Attacks

| Attack | Description | Examples |
|---|---|---|
| **Counterfeit** | Distribution of malicious or tampered hardware components | Hardware trojans with backdoors, compromise during manufacturing, a dropped USB that emulates keyboard keystrokes |
| **Fault injection** | Alters device operation by physically tampering with hardware | Voltage or clock glitches that change CPU instructions; periodic electromagnetic pulses |
| **Micro-architectural** | Targets the implementation of a system's microarchitecture | Speculative attacks that read arbitrary memory; exploiting DRAM vulnerabilities for privilege escalation |

#### Example: Spectre
- A **speculative execution attack** that reads arbitrary memory using a **timing side-channel** to pass information from the microarchitectural layer to the software layer.
- **Why it works:** CPU caches are not accessible from outside the CPU, but when an instruction needs data from slow main memory the CPU must wait. To avoid waiting, the CPU **guesses a value and continues speculatively**. It rolls back if the guess was wrong and commits if it was right.
- The leak comes from the speculative work leaving traces (such as cache timing) even after rollback.
- Spectre exploits a **design problem in modern CPUs**, so there is **no easy fix** for the hardware root cause. Much effort went into **hardening systems in 2018**.

### 2.2 Software Attacks

- **Control flow attack** — diverts a program's intended control flow to execute malicious code. Examples: **stack smashing** and **return-oriented programming (ROP)**, which builds malicious code out of function returns.
- **Code injection attack** — input passed to a program (the *generator*) produces executable code that another program (the *executor*) runs.
- **Command injection attack** — a code injection where attacker input modifies **commands passed to a command interpreter**, so the attacker's commands run.

#### Example: Command Injection
- A program builds a shell command from user-supplied `argv[i]`, such as `/usr/bin/cat <argv[i]>`.
- If `argv[i]` contains `/dev/null;reboot`, the shell runs `cat /dev/null` and then `reboot`, so the **system reboots**.
- The code is **not harmless**: user input must be validated or sanitised and never concatenated straight into a command string.

### 2.3 Hypervisor / Virtualization

A **hypervisor** is a small piece of software that makes **server virtualization** possible. It forms an **abstraction layer between the server's hardware resources and the operating system or containers**.

| Type | Description |
|---|---|
| **Type-1 (bare-metal)** | Runs directly on the hardware |
| **Type-2 (hosted)** | Runs on top of a host operating system |
| **OS-level (container)** | Virtualizes at the operating system level |

#### Hypervisor Attacks
- **Hyperjacking** — replaces the legitimate hypervisor with a **malicious one**, by injecting it below or above the real one or replacing it entirely. It is **hard to detect from the operating system**.
- **VM escape** — a program that breaks the **isolation** provided by the hypervisor, so the VM can interact with the hypervisor or host OS. Found in many popular hypervisors (Xen, KVM, VMware, Hyper-V, VirtualBox).
- **VM rootkit** — a rootkit running **underneath** the operating system (a special case of hyperjacking). It can launch malware in separate, invisible VMs.

#### VM Escape Examples
| CVE | Detail |
|---|---|
| **CVE-2015-3456 (VENOM)** | Affected several virtualization platforms; attackers break out of a VM and execute code via the **virtual floppy disk controller** |
| **CVE-2017-4907** | VMware Workstation flaw in the **3D acceleration** feature that lets a guest execute code on the host |
| **CVE-2020-3960** | VMware flaw involving **uninitialized stack memory** that allows escape from guest to host |

**VENOM detail:** the Floppy Disk Controller (FDC) in **QEMU** (Xen before 4.5.x and KVM) lets local guest users cause a **denial of service (out-of-bounds write)** or possibly execute arbitrary code via commands such as `FD_CMD_READ_ID` and `FD_CMD_DRIVE_SPECIFICATION_COMMAND`.

### 2.4 Operating System Attacks

- **Loadable kernel module attack** — uses loadable kernel modules (drivers, network protocols) to inject malicious code into the kernel. On **monolithic kernels**, malicious modules have almost unlimited access to programs.
- **Kernel rootkit attack** — installs a rootkit (persistently or volatilely) within the OS kernel, with or without privilege escalation. Kernel rootkits are **difficult to detect**, so a **complete re-installation** is usually required.
- **Kernel privilege escalation attack** — gains access to resources normally protected from users. Kernels run at higher privilege levels (see **protection rings**) and protect resources from less privileged processes. Some operating systems confine application processes in restricted environments called **jails**. Privilege escalation can be used to **escape the jail (jailbreaking)**.

#### Privilege Escalation Types
| Type | Description |
|---|---|
| **Horizontal** | The attacker gets access to **another user's account at the same privilege level** to reach valuable assets or information |
| **Vertical** | The attacker **raises the privileges of a compromised account** to administrative or root level. Especially dangerous because it may give complete control of the system |

#### Typical Kernel Privilege Escalation Attack Chain
1. Execute an attack to get **unprivileged access** to the system
2. Execute an attack to **escalate privileges** to root or kernel level
3. Install a **persistent rootkit** that provides backdoors and hides the attacker's presence
4. Use the system to **collect or steal data, block access, or attack other systems**

### 2.5 System Software Attacks

- **Dynamic linking attack** — manipulates the dynamic linker to load malicious libraries at program startup. On Linux, the **`LD_PRELOAD`** environment variable specifies libraries loaded before any other system libraries.
- **Package management attack** — modifies a package manager to accept malicious packages. Methods: use malicious keys to validate packages, create malicious packages signed with those keys, or exploit bugs in the package manager.
- **Ransomware attack** — a **crypto-virology** attack that permanently blocks access to the victim's data.
  - Encrypts files with a **random key**
  - Also targets **backups** to increase pressure to pay
  - Advanced attacks **steal data before encrypting** it, with a threat to publish it

#### Example: WannaCry
- Infected **over 200,000 computers in over 150 countries in 2 days**
- Ransom demanded in **Bitcoin**, which is not easily traceable
- Not a new weakness: **Microsoft had issued a patch in March 2017**
- Many organizations, including **government hospitals and older businesses**, were hit because they ran **older, unsupported Windows**

---

## Key Takeaways
- Vulnerabilities and exploits **cross layer boundaries**, so defenders must understand the whole stack from hardware up to applications.
- **Hardware:** counterfeit, fault injection and micro-architectural attacks (Spectre uses speculative execution plus a timing side-channel, with no easy fix).
- **Software:** control flow hijacking (stack smashing, ROP) and injection flaws. Command injection comes from unsanitised input reaching a shell.
- **Virtualization:** hyperjacking, VM escape (VENOM and others) and VM rootkits attack the isolation that virtualization provides.
- **OS:** malicious kernel modules, kernel rootkits (usually needing a full reinstall) and privilege escalation, either horizontal or vertical.
- **System software:** `LD_PRELOAD` hijacking, package-manager compromise and ransomware.
- WannaCry shows how **unpatched and unsupported systems** turn a known vulnerability into a global incident.
