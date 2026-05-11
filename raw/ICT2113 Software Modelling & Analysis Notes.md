---
type: source
folder: wiki/sources
title: "ICT2113 Software Modelling & Analysis"
course: ICT2113
status: active
updated: 2026-05-09
tags:
  - folder-source
  - requirements-engineering
  - software-modelling
  - uml
  - agile
  - user-stories
related:
  - "[[requirements-engineering]]"
  - "[[agile-requirements]]"
---

# ICT2113 Software Modelling & Analysis — Lecture Notes
**Singapore Institute of Technology | Prof Kevin**

---

## Table of Contents
1. [L01 — Requirements Philosophy, Process, Methodology & Modeling](#l01)
2. [L02 — Capturing 'Big Requirements Up Front' — Requirements Engineering (RE)](#l02)
3. [L03 — Eliciting Authentic & Right Requirements by Customer](#l03)
4. [L04 — Knowing the Right Requirements Models (UseCase, ERD, DD, et al.)](#l04)
5. [L05 — Analysing PS Requirements by Vendor Proficiently with BCIC](#l05)
6. [L06 — Specifying Requirements in SRS with Quality, RTM & Change Protocol](#l06)
7. [L08 — Validating & QC SRS by Customer/Vendor (QA for RE)](#l08)
8. [L10 — Overcoming Deficiencies of RE — User Story is the Answer](#l10)
9. [L11 — UseCase 2.0: Heavyweight RCM Updated to Lightweight](#l11)
10. [L12 — UML: Giant No More — Less Relevant in Lightweight](#l12)

---

## Key Abbreviations & Glossary

- **RCM** — Requirements Capture Methodology
- **SDM** — Software Development Methodology
- **SDLC** — Software Development Life Cycle
- **RE** — Requirements Engineering (heavyweight RCM)
- **PS** — Project Specification (customer's eliciting deliverable)
- **SRS** — Software Requirements Specification (vendor's specifying deliverable)
- **PL** — Project Lead
- **BA** — Business Analyst
- **QC** — Quality Control (targets workproduct)
- **QA** — Quality Assurance (targets process)
- **iRTM** — Inceptive Requirements Traceability Matrix
- **PB** — Product Backlog
- **UC** — UseCase
- **IRC** — Incongruous Requirements Checklist
- **BRUF** — Big Requirements Up Front
- **GPV / GPR** — Goal, Purpose, Value / Goal, Purpose, Result (UseCase)
- **BCIC** — Breakdown, Clarify, Interpret, Categorize (Analysing activities)

---

<a name="l01"></a>
## L01 — Requirements Philosophy, Process, Methodology & Modeling

### **Learning Outcomes**
- **Why requirements are NOT part of software** — Requirements are essentially a *model* of not-yet-existing software. All models are flawed due to not being real; requirements suffer the additional incongruity of describing something that does not yet exist.
- **Why customer–vendor relationship is "remote cooperating"** and where this happens in the SDLC.
- **Heavyweight vs. lightweight** software development methodologies (SDMs) and their significance for requirements capture methodology (RCM).
- **Correlation** of process, methodology, and model in software engineering.

---

### **Why Requirements are Not Software**
Requirements are a **model** of not-yet-existing software. We use a process of *reasonable manifestation*:
- Customer **models** their needs → vendor **analyses** the model → then **designs & builds** to its understanding → customer **verifies** the newly-built item.
- Since initial needs are inherently uncertain, any "working real" product could be the best semblance of actual need.

---

### **"Four Horsemen of the Requirements Apocalypse"**
In the real world, requirements capture is fraught with excessive demands and impossible expectations:

- **Originality & Drift** — Customers frequently do not understand their own needs before engaging a developer; expectations drift while development is underway.
- **Quality** — Quality can only be measured for a tangible entity; one can never establish requirements quality with any precision before the software exists.
- **TwoThirdsRule** — Industry demands faster, better, and cheaper — but experience dictates that only two out of three is ever achievable.
- **OverVsRight** — There are never enough resources to do it right, but always enough resources to do it over.

---

### **Cooperation is "Name of the Game"**
- Customer and vendor share the **common goal** of completing the sw dev project within time and budget, albeit with differing KPIs (ROI vs. profit).
- They mostly work **alone**, each with well-defined, unique responsibilities, applying specialised soft skills and resources at specific times.
- The relationship is **remote cooperation** — more than communicate or coordinate, but not collaborate (due to strict demarcation of resources, ownership, and responsibility).
- Only teams with **excellent soft skills** can sustain remote cooperation over long periods.

---

### **History: Software Splits from Hardware → RCM Splits from SDM**
- Mid-1940s: computers programmed externally by cables & switches.
- Mid-1950s: stored programs made software a **separate product** from hardware, needing its own SDM.
- 1960s sw crisis: requirements needed its own kind of RCM, separate from the rest of the SDLC → **Requirements Engineering (RE)** emerged.
- Up to 1990s: if SDM was standard heavyweight (BRUF), then RCM was nearly always RE.
- 1980–90s: lightweight SDMs emerged using **incremental, iterative, or evolutionary** RCMs.
- 1998: **Extreme Programming (XP)** was first lightweight SDM with a truly non-BRUF RCM, namely **User Stories**.

---

### **Two Types of SDM — RCM Adapts in Kind**

| **SDM Subtype** | **RCM Subtype** | **Example SDM** |
|---|---|---|
| Heavyweight | RE | SDLC |
| Lightweight | User Story | XP, RAD |
| Lightweight | UseCase 2.0 | Scrum |

- **Heavyweight SDM** — Methods carried out in *immutable linear sequence* (one start and finish), plan prescribed at beginning. Produces frequent checklists, milestones, progress reports, and detailed specifications. Bureaucracy & documentation make the project immune to obstructive occurrences.
- **Lightweight SDM** — Methods carried out in *frequent development cycles* of small increments, built iteratively with stakeholders' continuous feedback ("incremental reqs, iterative dev", a.k.a. *evolutionary*). Highly flexible; requires only simple statements of requirements.
- **Traditional & Agile** are informal synonyms for heavyweight & lightweight, respectively; avoided in this module to reduce confusion.

---

### **Correlation of Process, Methodology & Model in SWE**

| **Concept** | **Definition** | **Example** |
|---|---|---|
| **Process** (1D model) | High-level plan for developing new software from cradle to grave | SDLC — linear sequence of Reqrs, Analysis, Program Design, Coding, Testing, Deploy |
| **Methodology** (1D model) | Set of methods realising the process | "SDLC" — four methods (Analysis, Design, Coding, Testing) with activities, standards, proprietary approaches |
| **Model** (2D+) | Higher-dimension representation needed to truly describe methodology | UML Activity diagram of SDLC; company SDM per company policy |

---

<a name="l02"></a>
## L02 — Capturing 'Big Requirements Up Front' — Requirements Engineering (RE)

### **Learning Outcomes**
- **Where in SDLC** is RE RCM conducted.
- **What type of SDM** RE RCM is paired with and why.
- **Relationship** between customer and vendor in conduct of RE RCM.
- **Why two specifications** are written in RE RCM, yet there can only be a single source of truth for the paired SDM to follow.
- **Earliest origin** of likely requirements capture failure and what makes it possible.

---

### **RE: Description, Not Specification**
RE is a **heavyweight RCM** applied to the first method (Requirements) of the SDLC. It applies a prescribed plan with excessive bureaucracy & documentation to produce a prescribed product.

RE comprises **five methods** (per IEEE SWEBOK): Eliciting, Analysing, Specifying, Validating & Managing. In this module, only the **first four** are studied (Managing is omitted).

---

### **RE Model — Methods, Specifications & Datastore**
Two cooperating organisations, **four methods**, **two specifications**, and **one datastore (Repository)**:

- **Customer's PL team → Eliciting →** Project Specification (PS)
  - Drawing forth lingering ideas & expectations from stakeholders on requirements for new not-yet-existing sw, plus survey of pertinent historical record for presently-in-use sw, plus terms for new sw dev project, documented as clauses and models in **PS**.
- **Vendor's Reqrs Analysis team → Analysing →** Repository
  - Regulated-revision of PS into ready-content for SRS: checked, fixed for integrity & comprehensiveness, enhanced with vendor's best practice in domain & technology. Relies on customer–vendor cooperation to clear up uncertainties about requirements.
- **Vendor's Reqrs Analysis team → Specifying →** Draft/Complete/Release SRS
  - Writing sw requirements spec (SRS) comprising 'base' requirements per agreed standards with codified 'development provisions' best practices (latest technology, sw dev quality model, iRTM & change mitigation strategy), all needed by vendor in post-requirements stages of SDLC.
- **Vendor's Reqrs Analysis team → Validating →** (end)
  - Applying QC measures onto SRS, and conducting QA audit of vendor's conduct of Analysing, Specifying, and Validating against contractual and professional standards, to ensure that vendor has right SRS produced right.

---

### **Why Two Specifications — One Per Organisation**
Only one spec, the **SRS**, exits from RE, ensuring there is a **single source of truth** for new not-yet-existing sw. The other spec, the **PS**, is internal and only seen by participants of RE.

The approach is similar to "passing bills in government": one org writes the bill, another seconds it with amendments. In RE:
- Customer writes **core** requirements first.
- Vendor supplements that core … **without changing** its essence.

This ensures both parties retain **legal protection** and some control:
- Customer establishes their requirements from their business and operations perspective, independently.
- Vendor infuses **appropriate technology** into requirements, synchronising them with best-practice development processes.

**Key RE Standards:** IEEE 29148-2018, IEEE SWEBOK, FAA RE Management Handbook, International RE Board (IREB), IBM Rational Resource Library.

---

### **Tender Process — Customer's Undertaking**
The Tender process is the intercession necessary to determine if a vendor is willing and able to take on the sw dev project. It sits between Eliciting and Analysing and involves:
- Customer releases **RFP** for project.
- Vendors form tender analysing teams, submit 'solution' proposals.
- Risks: denial of weak capability, lowballing, pressure by senior management to win, incorrect info given, info denied due to security concerns.
- Customer decides **winning bid** → signing contract, exchanging project info → Analysing begins.

---

<a name="l03"></a>
## L03 — Eliciting Authentic & Right Requirements by Customer

### **Learning Outcomes**
- **Eliciting method**, story of it being awaited, and three priority tasks of the PL team.
- **Requirements clauses**, model usage, and effective writing.
- **Four subtypes** of Eliciting.
- **Stakeholder groupings** and their precedence indices.
- **Planning** conduct of 'Enterprise team' subtype Eliciting.
- Apply **Mag7 & R-Tree** to effectively write quality PS.

---

### **RE Conduct, RCM Type & Organisations' Relationship**
- RE applies to the **first method of SDLC** (Requirements).
- RE is **heavyweight RCM**, pairing with same-type SDMs.
- RE applies **prescribed plan** with excessive bureaucracy & documentation to produce a prescribed product with expectation of no deviations right up to the end.
- It starts with approved budget & schedule to replace ineffective presently-in-use sw, and ends with a complete set of requirements for starting design of new not-yet-existing sw.
- RE is **cooperation** between customer and vendor; this includes customer interceding RE with their **Tender process** (to select and contract sw developer), that stops RE in its tracks until intercession is concluded.

---

### **Brief Definitions of RE's Four Methods**

- **Eliciting** — Drawing forth lingering ideas & expectations from stakeholders on requirements for new not-yet-existing sw, along with survey of pertinent historical record for presently-in-use sw, plus terms for new sw dev project, and then documenting all that info as clauses and models in the **Project Spec (PS)**.
- **Analysing** — Regulated-revision of PS into ready-content for SRS that is checked, fixed for integrity and comprehensiveness, plus enhanced with vendor's best practice in domain & technology. Relies on customer–vendor cooperation to clear up any uncertainties about requirements.
- **Specifying** — Writing sw requirements spec (SRS) that comprises 'base' requirements per agreed **standards** with codified 'development provisions' best practices, i.e., latest technology, sw dev quality model, iRTM & change mitigation strategy, all needed by vendor in post-requirements stages of SDLC.
- **Validating** — Applying quality control measures onto SRS, and conducting quality assurance audit of vendor's conduct of Analysing, Specifying, and Validating against contractual and professional standards, to ensure that vendor has right SRS produced right.

---

### **Tender Meeting is Origin of Likely Requirements Capture Failure**
The tender meeting introduces: denial of weak capability, lowballing, pressure by senior management to win, incorrect info given due to security concerns. These all seed potential requirements failure from the outset.

---

### **Clauses, Modeling & Effective Writing**

- **Black-box clause** — States inputs, *what* the requirement does, and outputs it generates.
- **White-box clause** — States inputs, *how* they are used & how the requirement gets resulting outputs. (More to purpose of sw dev, not requirements.)

**Magnificent Seven (Mag7) — Seven Quality Features of Requirements Clauses:**
Verifiable & testable, Complete, Correct (accurate & consistent), Fully distinct (no overlap), Ranked/prioritized, Realistic/feasible, Unambiguous & clear.

**Requirements Tree (R-Tree)** — Mostly resolves *completeness* quality of requirements.

---

### **Four Subtypes of Eliciting Method**

| **Subtype** | **Intended For** | **Conducted By** | **Deliverable** |
|---|---|---|---|
| Consultant-driven | Specialty & complicated projects | External expert | High-quality PS |
| Enterprise team | Conventional & uncomplicated projects | Internal appointees | Final PS |
| Pre-sales demo | Customisation projects | Internal product owners or external reps | COTS-centric PS |
| Scoping review | Mega projects | Senior management | High-level plan or meta-plan + several PS |

In this module, focus is on **Enterprise team** subtype only.

---

### **Stakeholders**
- Person with **vested interest** in new sw.
- Typically internal, but some are external.
- **Qualify** according to project impact and perspective of sw needs.
- Types: Direct end users, Indirect end users, Beneficiaries, Authorities & decision makers, PL team.
- **Precedence index** (in order of priority): Essential, Desirable, Acceptable.

---

### **Enterprise Team Subtype — Priority Tasks for PL Team**
1. Conducting **Eliciting method**, and completing full version of PS.
2. Organising **Tender process**, including creating edited version of PS for release to bidders, drafting RFP, and planning evaluation of submitted bids.
3. Installing resources for **customer's project office**, including staffing, communications, infrastructure, and testing harnesses for proof-of-concept prototypes.

---

### **Basic Outline of Info Comprising PS**

| **Seq** | **Section** | **Details** |
|---|---|---|
| 1 | Describe your company | Name, mission, vision, core biz, industry sector, and key initiatives related to new sw |
| 2 | Describe your project | a) Appropriate descriptive title, b) Project "body of knowledge" for readers to understand issues, c) SMART goals |
| 3 | List your Biz Ops requirements | Main commercial purpose new sw expected to serve. Sub-outline grouping logical and consistent. Write levels 0&1 of supplied Reqrs tree |
| 4 | List your technical requirements | Sw configuration items such as code & desired documentation, plus current IT set-up |
| 5 | Set your financial requirements | Breakdown project cost structure, where funds will come from, and desired payment schedule |
| 6 | Set your delivery requirements | Graduated deliveries from kick-off through work & testing milestones to final soft launch |
| 7 | Addendum & attachment | Up to student; use as per descriptions in Glossary |

---

<a name="l04"></a>
## L04 — Knowing the Right Requirements Models (UseCase, ERD, DD, et al.)

### **Learning Outcomes**
- Select requirements capture models according to their appropriate **variant**, appropriate **ways to use**, and **eight effective writing** guidelines.
- Write and/or draw any **six** of these 11 requirements models: UseCase diagram & matrix, Context diagram, As-is & to-be Business Process model, ERD, Data dictionary, Dialog Map, Org chart, Gantt chart, Wireframe, and Mockup.

---

### **Four Variants of Engineering Models**
A **model** is a *stylized and portable representation* (physical or virtual) of **one** or a couple of aspects (either structural or behavioural) of some real, usually physical, entity. It has four variants according to dimensionality:

| **Variant** | **Examples** |
|---|---|
| 1D | Text & stream of tokens |
| 2D | Graph, chart, waveform, photo & drawing |
| 3D | Toy, display, figurine, mold & 3D computer-aided design |
| 4D | Tesseract, windtunnel, light refraction, hourglass, crash-dummy & 4D printed model |
| Mockup | Scale model, prototype & simulator (member of 3D or 4D) |

---

### **Why Models are Important in Requirements Capture**
Engineering models are employed in the following ways:

- **Manufacturing** — To aid or instruct in any/all stages of manufacturing of a manmade entity (planning, managing, designing, implementing, or testing).
- **Exploring existing/known entity** — To study operating (fit into environment), compatibility (fit into ecosystem), analysis of quality (reliability, availability, fault tolerance, load & stress levels), and to show useability in standard condition.
- **Discovering possibilities of new/unknown entity** — Research, feasibility study, observing useability first time or under duress, projecting limitation, reliability, tolerance & safety.
- **Education** — Be learning aid (propositional knowledge) or skills training (procedural knowledge), gather feedback on entity, display info for public awareness, show proofs of things for learning, demonstrations of phenomenon.

---

### **Effective Writing Guidelines (Dos & Don'ts)**

| **Do ✓** | **Don't ✗** |
|---|---|
| Apply to crucial, complex, or difficult to understand requirements | Make a work of art |
| Provide sufficient context to models | Cram full of elements |
| Codify for traceability | Make elements inconsistent with other models in same document |
| V&V for implementation neutrality | Change, rebrand, or hybridize |

---

### **Key Requirements Models Covered**

**1. As-is & To-be Business Process Model (BPMN)**
Elements:
- **FlowObjects** — Events (something that *happens*), Activities (something that *is done*), Gateways (forking and merging of paths depending on conditions expressed).
- **ConnectingObjects** — SequenceFlow (order activities are performed), MessageFlow (messages across org boundaries & between Pools; never used to connect Activities or Events within same Pool), Association.
- **Swim lanes** — Pool (major participants in process), Lane (organise & categorise Activities within Pool according to function or role).
- **Artifacts** — DataObject, Group, Annotation.

Business (Biz) Process Model provides graphical notation based on flowcharting very similar to UML's Activity diagram. Objective: provide standard notation readily understandable by all stakeholders.

---

**2. UseCase Diagram — Value of Biz Processes**
Elements:
- **UseCase** — Sequence of usage transactions yielding 'goal, purpose, value' (GPV) to Actors without declaring Subject's internal structure.
- **Actor** — Role played by external user or another system that interacts with Subject.
- **Association** — Connection that allows typed elements to interchange signals and/or data.
- **Subject** — Element that contains or shares UseCases (e.g., subsystem, component & class).
- **Extend** — *Conditionally* (how & when) inserts entire behavior from extending UseCase into behavior of extended UseCase.
- **Include** — *Auto-inserts* entire behavior from included UseCase into including UseCase.
- **Multiplicity** — Inclusive range of interchanges.

---

**3. Context DFD — External Exchange of Data**
Elements:
- **ExternalEntity** — External consumer or producer of DataFlows between it and new sw's Main Process (analogous to root node in hierarchy).
- **MainProcess** — New sw, designated "LevelZero", receiving and/or generating DataFlows from ExternalEntities.
- **DataFlow** — Electronic, written, or verbal movement of data between external entities and MainProcess.

---

<a name="l05"></a>
## L05 — Analysing PS Requirements by Vendor Proficiently with BCIC

### **Learning Outcomes**
- **Analysing method**, minimum analysing for Tender process, and **Repository**.
- How **regulated-revision** works in checking, correcting, keeping consistency with PS.
- **Account manager** and how he/she can help vendor's requirements analysis team.
- Apply **BCIC four activities** to PS (i.e., do regulated-revision of PS).
- Make personal **IRC**, use it to effectively write quality requirements, and upload them into Repository.

---

### **Regulated-Revision Requirements Loaded into Repository**
- **Eliciting output** → PS (Customer's PS contains all Eliciting requirements & project management, except budget. Effective writing per Mag7 & R-tree.)
- **Analysing output** → Repository (Vendor's Analysing contains both checked & revised requirements from PS, complying to previous effective writing plus effective writing from applying IRC.)
- Analysing does regulated-revision of input PS, and loads **Repository** with all requirements being placed into SRS.

---

### **Our Analysing Method Model (BCIC)**
Four activities (remember: **B**reakdown → **C**larify → **I**nterpret → **C**ategorize):

**1. Breakdown** — Separate all incongruent biz ops & technical requirements from cogent ones. By Business Analyst (BA) with aid of personal Incongruous Requirements Checklist (IRC). BA actions include:
- Check entire PS for incongruities according to IRC.
- Cross-check all known and industry-standard external systems for omissions in PS.
- Check for compound requirements that are better understood when separated into atomic ones.

**2. Clarify** — Determine authentic purpose and substance of priority incongruent requirements uncovered in preceding action via **cooperation** with originating stakeholder(s). BA actions include:
- Physically meet stakeholder face-to-face with pre-agreed agenda (web video conferencing and WhatsApp calling are possible alternatives; audio-only is often not enough).
- Explain specific difficulties with priority requirements via user-friendly and informative models.
- Ensure agreement reached, even if only to continue clarifying or be open issue in SRS.

**3. Interpret** — Correct & replace all incongruent requirements, per agreement from preceding actions, into cogent ones. Revise models (vendor's & customer's). Insert industry-standard codification.

**4. Categorize** — Organize all biz ops & technical requirements into standard categories & codification, then load them with their models into stock template set up in Repository. Team does sanity check.

---

### **Generic IRC — Becomes Effective Writing Guide**

| **Imperative** | **Continuance** | **Contextual** |
|---|---|---|
| Check appropriateness for degree of priority (highest to lowest: Shall, Must or must not, Is required to, Are applicable, Responsible for, Will, Should) | Verify that excessive use of continuance words does not make undue complexity (Below, As follows, Following, Listed, In particular, Supported by) | Inconsistent with another requirement |
| | | Not testable |
| | | Unseemly prioritized |
| | | Ambiguous |
| | | Unverifiable with customer policy |
| | | Substantively invalid |
| | | Suspected incompleteness |
| | | Not feasible or unrealistic |
| | | Unreadable due to typo(s) or missing word(s) |

Effective writing is personal to team member — it comes from applying corrections in your IRC; also, revisiting Mag7, plus creating own R-tree if not using PL team's one.

---

### **Risks for Customer & Vendor During Analysing**

**Legacy Risks for Customer:**
- Vendor doesn't know our industry to do regulated-revision of new sw requirements.
- Vendor will fight us on every change regardless of how important it is.
- Vendor too techie to communicate well enough to explain nature of new sw.
- Vendor will skimp on quality by using low-skilled outsourced junior analysts.

**Legacy Risks for Vendor:**
- Customer will change their requirements way too much, and expect it will be Free of Charge.
- Such changes will not be cross-checked by customer for obvious inconsistencies.
- Customer will fight us about deferring changes too significant for this round.
- Customer is not techie enough to understand innovation of new sw.
- Account Manager is suddenly and unavoidably replaced in middle of RE.

---

<a name="l06"></a>
## L06 — Specifying Requirements in SRS with Quality, RTM & Change Protocol

### **Learning Outcomes**
- **Specifying method**.
- Why a **better template** than stock in Repository is necessary for SRS.
- **Four development provisions** of vendor.
- **Three change mitigation strategies**.
- Draw **SRS profile model**.
- Apply **three perspectives** and **11 features** of McCall's sw quality model.
- Organise sample **iRTM**, with rows, columns & dummy values for PS & SRS.

---

### **Specifying is 3rd in RE — Vendor Goes Solo**
*Writing sw requirements spec (SRS) that comprises 'base' requirements per agreed standards with codified 'development provisions' best practices, i.e., latest technology, sw dev quality model, iRTM & change mitigation strategy, all needed by vendor in post-requirements stages of SDLC.*

By completion of Analysing, vendor likely discerned that:
a) Developing sw is **not** customer's core competency (otherwise external vendor not contracted).
b) Customer is **not settling** for run-of-the-mill sw that does not give it edge against its competitors.

With all requirements thought of by customer made as perfect as reasonably possible by vendor's regulated-revision, Specifying is the expedient stage of RE for vendor to finally apply that substantial expertise.

---

### **Repository's Stock Template is Insufficient for SRS**
The stock template in Repository holds only regulated-revision requirements, but does **not** cater clause-wise for **development provisions** because they can be determined only after Analysing. So, a **new expanded template** is needed. Four choices for expanded template:
1. Use template supported by your company's IT department.
2. Purchase template supported by major standards agencies (ISO, IEC, IEEE).
3. Co-opt template from thousands available on Internet.
4. Assemble own custom template from parts of various others ("Frankenstein template").

---

### **Four Development Provisions in SRS**
Once SRS is released, vendor cannot add items to dev process that are not in SRS (it's bad for profits, ROI, reputation, plus good for competition). So, essential to insert **development provisions** into SRS before release:

- **New technology** — Sw technology is manifested in a wide range of peripheral entities (platform, networks, maintenance, security, etc.). Only vendor knows how to "coax" most benefits out of new technology despite customer's IT constraints.
- **Quality of development** — Customer has own quality model but it would be ill-suited to sw development; only vendor's quality model is appropriate.
- **Trace requirements to testing** — Customer knows acceptance testing is crucial, but doesn't have access to development process to trace their requirements to testing; only vendor can design and maintain such tracing. Customer must be shown it so it can approve SRS.
- **Change mitigation** — Some change is inevitable, so vendor needs measures in SRS to mitigate disruption to product itself as well as project (schedule & budget). Such measures are not static; they evolve with experience and new ways of thinking.

---

### **McCall's Software Quality Model**
Originating from U.S. Airforce, the most frequently applied sw quality model is the **1977 McCall's** (a.k.a., General Electric model). It comprises **11 features** (originally called factors) grouped into **three perspectives**:

**Perspectives:**
- **Operation** — How well sw works in use
- **Revision** — How well sw tolerates internal change without degradation or failure
- **Transition** — How well sw adapts to external change without degradation or failure

**Eleven Features (factors):**

| **Perspective** | **Features** |
|---|---|
| Product Operation | Correctness, Efficiency, Integrity, Reliability, Usability |
| Product Revision | Flexibility, Maintainability, Testability |
| Product Transition | Interoperability, Portability, Reusability |

Definitions:
- **Correctness** — Extent to which sw performs its exact intended function.
- **Efficiency** — Extent to which sw makes optimal use of resources.
- **Integrity** — Extent to which access to sw and data can be controlled.
- **Reliability** — Extent that sw can be expected to perform its intended function with required precision.
- **Usability** — Extent to which users can learn to operate, prepare input for, and interpret output of sw.
- **Flexibility** — Extent that sw can adapt to unusual conditions or unpredicted variances in environment interface or internal processes.
- **Maintainability** — Extent that sw can be confidently and continuously monitored for specified operation, repaired, and upgraded to achieve maximum useful life.
- **Testability** — Extent that sw can be tested or do and record self-diagnostics.
- **Interoperability** — Extent that sw can exchange data via common set of exchange formats, read and write same file formats, and follow same protocols, as another.
- **Portability** — Inverse-extent of time and effort it takes to adapt new sw that operates under a particular compiler, OS, or hardware, to operate under another.
- **Reusability** — Extent that part(s) of one new sw can be directly installed into and used by another.

Features are often regrouped into **external** and **internal** conditions to associate quality with SDLC.

---

### **Codifying and Inceptive RTM (iRTM)**
**Requirements Traceability Matrix (RTM)** — First version is the 'inceptive RTM' or **iRTM**.
- **Umbrella** document — "Living" for entire SDLC, iterative with successive versions, and *linker* of requirements to all project's data through to user acceptance testing, ensuring all requirements are accounted for across SDLC.
- More than a checklist: a) "chain of custody" of requirements from PS to SRS to Design Spec to Coding Spec and so on, and b) dynamic adapter of any documents in project.
- Concept of 'requirements traceability' was first introduced in publication by Penedo & Stuckle in 1985.
- Integrity of RTM relies entirely upon goodness of codifying in SRS.

**Codifying:**
- Assigning unique identifier (numeric or alphanumeric string) for every requirement in SRS.
- Key factor: how far into requirements statements should team take it (single statements, compound statements, lists, elements in models — all are difficult codifying decisions).
- **Recommended NOT** to use unique outline numbering used for table of contents for codifying, as this may change often, and even minor changes to contents can break codification in RTM.

---

<a name="l08"></a>
## L08 — Validating & QC SRS by Customer/Vendor (QA for RE)

### **Learning Outcomes**
- **Validating method**, and how it incorporates QC & QA.
- Use of QC to "catch" three kinds of errors — **authorship indiscriminate**, **latent contradictions**, **omission of topics** — via minimum six investigation techniques.
- Use of QA to "catch" 'failure to strictly comply with RE(-) methods' error via minimum three investigation techniques.
- What's next in RCMs and what alternatives are there to RE.

---

### **Broad Terms for QC and QA Auditing**

**Quality Management (QM)** is the high-level process that specifies techniques and tools for establishing quality across all forms of manmade goods and services providers. **QC** and **QA** are its two methods; they differ in their targets and extent of actions.

- **QC (Quality Control)** — Target is the **workproduct** generated by process (defect detection, not prevention). Procedures include batch inspection, product sampling, statistical analysis, and level 1–3 testing. Elimination of defects is not normally done, especially with manufactured and specialty goods.
- **QA (Quality Assurance)** — Target is the **process** producing the workproduct. Broadly entails documentation, suppliers, engineer & manager training, and workproduct changes, to ensure compliance with standards such as ISO/IEC 25010. Categories of QA: defect prevention, continuous improvement, human resource management, and application of risk-based approaches. Procedures: investigative reporting, audits of internal auxiliary processes, planned system reviews, and spot checks.

---

### **Validating Method Basics — SRS**
1. Vendor's **Project Manager (PM)** in-charge of QC audit, directing requirements team to support QC auditor.
2. Before QC independent auditor arrives, vendor & customer cooperate to **review SRS** and correct any high-profile errors, such as: missing essential requirements, agreed edits per Analysing sessions (customer); change mitigation, codification coherence, quality model, iRTM & typos (vendor).
3. Auditor's **Execution plan** — including T&Cs of auditing SRS, access control, audit team size & roles, kinds of errors being pursued, and reporting — is provided to PM for approval.
4. Auditor ensures appropriate **security controls** of sensitive info and integrity of SRS is maintained throughout audit.
5. Following 'Post-op report', PM advises requirements team to make necessary enhancements.

---

### **What's Next After RE**
- RE is dominant RCM, but has well-known deficiencies that led to demand for lighter, faster, more flexible alternatives.
- Lightweight SDMs require non-BRUF RCMs — chiefly **User Stories** and **UseCase 2.0**.

---

<a name="l10"></a>
## L10 — Overcoming Deficiencies of RE — User Story is the Answer

### **Learning Outcomes**
- **Quiet revolution** of RCM from heavyweight to lightweight pre-Agile conclave.
- **User stories method & methodology**.
- **Origin** of User stories.
- **Importance of Agile conclave** on dominance of User stories.
- **Three conventions** for effectively writing User stories.
- Sketch (artistically as opposed to formally) **User story process model**.

---

### **Key SDM Innovations — Gallery**

| **Year** | **Innovation** | **Type** |
|---|---|---|
| 1956 | Kanban, by Taiichi Ōno in Toyota | Proj Mgmt |
| 1957 | Incremental, by Weinberg & Dimsdale in IBM | Proj Mgmt |
| 1977 | Joint Application Dev, by Chuck Morris & Tony Crawford in IBM | Proj Mgmt |
| 1986 | Spiral Model of SDLC, by Barry Boehm in TRW | Sw Develop |
| 1991 | Rapid Application Development (RAD), by James Martin | Sw Develop |
| 1994 | Dynamic Sys Dev Method (DSDM), by Consortium | Sw Develop |
| 1995 | Scrum, by Schwaber and Sutherland | Sw Develop |
| **1996** | **Extreme Programming (XP), by Kent Beck at Chrysler** | **Sw Develop** |
| 1997 | Feature-Driven Dev, by Jeff DeLuca at United Overseas Bank | Sw Develop |
| 2007 | Knbn Method, by Anderson in Corbis | Proj Mgmt |

---

### **User Story — Anchor Element of Lightweight RCM**

> *Informal description of new sw's capability/condition from perspectives of its user, imagined usage, and expected benefit, along with its production-grade code being realized (designed, coded & accepted by stakeholder) within hours to few days of specification.*

Key concepts:
- **Conversation** — User story is enough to initiate expansive conversation (verbal, docs, observing) between stakeholder & developer to specify requirement. Little saved after realization: source code & some design.
- **Epic & Feature** — Each sw dev proj has many user stories (100s, even 1,000s), because each applies to very small part of new sw. Often stories amalgamated into "Epics" to better manage numerous disparate tasks, or "Features" to optimally integrate code blocks into functions. These are broken apart to be realized as individual stories, only to be rejoined post-realization.
- **Product Backlog (PB)** — Stories held in repository 'Product Backlog' to await realization; **no SRS** per se.
- **Not saved** — Once chosen for realization, User story deleted from PB.
- **Coach** — Typically, first-time customers hire 'Agile coaches' to orient corporate expectations with Agile development norms. Biggest tension is with **fragmentation debt**: system context lost in a sea of disjointed PB items.

---

### **User Story's Origin in XP Practice**
User stories are super-tightly bound to XP SCM. Of original 13 XP practices, five directly drive User stories:
- **Customer conducts release planning** (difficulty, cost & scheduling of realizing User stories).
- **Real users are part of whole team** for requirements, priorities, and steering of project.
- **Customer defines acceptance tests** for realized User stories; added into regression testing regime.
- **Project co-opts Customer's simple evocative vision** of how new sw works, via use of **metaphor**.
- **Customer sets requirements small** yet with real business value, so they can be realized and shipped to customer frequently as "shrink-wrapped" sw features.

---

### **User Story Effective Writing — Three Conventions**

**1. Original No Name (Three-C's)**
Named by Ron Jeffries (Aug 2001 blog). Components:
- **Card** — Story is *unformatted first-hand outline*, by authentic user, who stays for all three-C's, of biz process with just enough info to evoke one unique proto-requirement. Story bound not by standard format, but by standard-size text box (original was 3"x5" index card). If too large to fit, must be revised to fit into smaller box.
- **Conversation** — Collaboration of user and developer akin to Eliciting Method in RE RCM, to specify full requirement from 'proto' one and to estimate realization effort. Uses "social" eliciting techniques, exchanges documents, and demos prototypes. Prior to specification, proto-requirement is validated. Priority and cost notes are appended.
- **Confirmation** — Realization of sw by developer, followed by acceptance testing of said sw by authentic user, akin to SDLC User Acceptance Testing (UAT) with two important differences: a) user already familiar with sw's capability and UX because pre-coding development work is done in full collaboration with developer, and b) only one requirement is being tested, to allow incremental release of accepted sw to customer.

**2. Connextra (Format-based)**
Brought in as coaching aid. Provides a structured template:
> "As a **[role]**, I want **[feature]** so that **[benefit]**."

**3. INVEST (Quality-based)**
Published by Bill Wake (Aug 2003 blog). Acronym highlights characteristics that good User stories will exhibit:
- **I**ndependent — Its content does not overlap with any others.
- **N**egotiable — Its exact representation of full requirement is completely open to being elaborated via conversation.
- **V**aluable — Its derived benefit to authentic user must be tangible & compelling.
- **E**stimable — It must have enough prioritization content to enable cost & effort derivation by orgs.
- **S**mall — It fits in given standard text box and its realization is achievable in minimum period of time.
- **T**estable — Its operability must be measurable, so definitive acceptance can be made of its suitability.

User story authors must accompany them with **scorecard** showing which quality features are met and which aren't. Poor scorecard doesn't mean story is discarded; developers use it to critique when and in what order such User stories are processed.

---

<a name="l11"></a>
## L11 — UseCase 2.0: Heavyweight RCM Updated to Lightweight

### **Learning Outcomes**
- **UseCase 2.0 methodology**.
- **Parent-UC** method including **Auxiliary details**.
- **UseCase Stories**.
- **UseCase Slices**.
- **Effectively writing** Auxiliary details, Stories, and Slices.
- Sketch (artistically as opposed to formally) **UseCase 2.0 process model**.

---

### **Timeline of Lightweight SDMs Evolution**

| **Year** | **SDM** | **RCM** |
|---|---|---|
| 1957 | Incremental (IBM) | RE |
| 1977 | Joint Application Dev (IBM) | RE |
| 1977 | V-chart (Sys Dev Corp) | RE |
| 1986 | Spiral Model (TRW) | Progressive in each spiral |
| 1991 | Rapid Application Development | Initial for MVP, progressive after each iteration |
| 1995 | Scrum (Easel Corp) | BRUF (not RE) |
| **1996** | **Extreme Programming (XP, Chrysler)** | **User story** |
| 1997 | Feature-Driven (UOB Singapore) | Initial for PM, progressive with UML models |

Since 1950, SDM-RCM pairing was heavyweight. In late 1970s, lightweight SDM-RCMs began emerging, though they retained vestiges of heavyweight. Finally, 1996 saw the **first truly lightweight RCM: User stories**.

---

### **Effective Writing Conventions: Three-C's**
*(See L10 — Three-C's section above)*

---

### **Effective Writing Conventions: INVEST**
*(See L10 — INVEST section above)*

---

### **History of UseCase Original Version**
UseCase method is the brain-child of Swedish computer scientist **Ivar Jacobson**. From **1967**, original modeling method coined "traffic cases" was used to specify functions and features for large telecommunication switching systems built and operated by Ericsson. Later, he enhanced traffic cases into what we now know as **"UseCases"**.

At second annual OOPSLA in **1987**, Ivar revealed the concept of UseCases in his article "Object-oriented development in an industrial environment", and how they were used at Ericsson to capture large system requirements.

In **1993**, he along with Christerson, Jonsson & Overgaard authored "Object-Oriented Software Engineering — A Use Case Driven Approach". Among other major ideas, it introduced UseCases in **graph & matrix representations** as cornerstones of software design. After book's publication, interest in applying UseCase method grew steadily.

---

### **UseCase 2.0 is a New Application of UseCase**
In **2011**, Jacobson collaborated with Ian Spence and Kurt Bittner to write eBook **"Use-Case 2.0: The Guide to Succeeding with Use Cases"**. It explained that UseCase 2.0 is a **new way** of applying UseCases that is:
- Lightweight, lean, scalable, versatile, easy-to-use.
- **Inspired by User stories**.

Structurally, UseCase 2.0 is still UseCase 1987–92,97 (a.k.a., **parent-UC**), its UML specification unchanged, and retains its original strengths, especially its coverage across SDM, SWE, and SDLC. Now, with UseCase as cornerstone, they supplemented parent-UC with two new methods: **Story** and **Slice**.

*Back in 1996, Kent Beck (XP lead-creator) says he was inspired by Jacobson's UseCases. With UC2.0, Jacobson says "inspiration has flown in opposite direction".*

---

### **UseCase 2.0 Process Model (8 Steps)**
1. Users draw **UseCase model** of new sw, and list **Auxiliary details**.
2. Users **prioritize** each UC for MVP.
3. Users write **Stories** for priority UC.
4. Store Stories in **PB** per UC & priority.
5. Developers join users to **specify** full requirements from Stories → **Slices**.
6. Write **Slices** to align select requirements in vertical orientation of Jacobson's BCE model (Boundary, Control, Entity).
7. Developers & users join in **realizing** each Slice IAW priority scheme.
8. Accepted realizations become sw increments uploaded into **shippable product**.

---

### **Alistair's Effective Writing of Stories**
Alistair Cockburn (co-signatory on 2001 Agile Manifesto) started his decades-long association with writing UseCases when he visited C3 project in 1998, expecting UseCases but getting User stories. In 2000/2001, he published "Writing Effective Use Cases".

UseCase templates in his book are elaborations of varying complexity of **matrix models**. The most useful to UC2.0 for effective writing of Stories is the **'Casual' & 'low-ceremony'** template. (As such, they are not appropriate for lightweight development, except for this one.)

---

<a name="l12"></a>
## L12 — UML: Giant No More — Less Relevant in Lightweight

### **Learning Outcomes**
- **Six phases** of sw dev project modeling.
- **Immediate benefits** of UML to heavyweight developers.
- **UML's semantic backplane**.
- **Four reasons** for UML's decline in usage.
- **Four selective & pragmatic uses** currently of UML by developers.
- Draw four each of **vertex & edge shapes** for structure & behaviour MEs (Modeling Elements) that represent notational self-consistency.

---

### **Sw Dev Proj Modeling Phases**
Since World War II, modeling has gone through **five major phases**, now on its sixth:

- **Phase 1 — Flowcharting (1947 to end-1960)** — Von Neumann & Goldstine proposed that mathematicians design and write algorithms for programs, recorded into flow diagrams (later flowcharts), then transformed by coders into machine instructions. Quickly became industry standard. But more complicated machines and operating systems proved to be flowcharts' undoing.
- **Phase 2 — Developer-centric flow models (1970 to 1980)** — Born inside heavyweight SDMs, proprietary to developer organizations. Some repurposed flowcharting to show what program does rather than how programmer should build it. At least 12 major sw dev project modeling conventions, including Structured Design by Yourdon & Constantine (1975) and System Analysis & Spec by Tom DeMarco (1978).
- **Phase 3 — SSADM (1980 to 1990)** — Conceived by UK government telecommunications agency. Massive methodology dominating development of heavyweight information systems. Combined methods from Checkland, Constantine, DeMarco, Jackson, and Yourdon; major models are data & control flow diagram, entity-relationship diagram, state transition diagram, structure chart, decision tree & table, and data dictionary.
- **Phase 4 — UML (1997 to present)** — Unified Modeling Language. See below.
- **Phase 5/6 — Lightweight (ongoing)** — UseCase 2.0, User stories, etc.

---

### **UML: Initial Reactions — Positive, Later Muted**

**By heavyweight project developers** — Approximately 71–85% of early practitioners reported using UML Class diagrams for functional and data structure modeling. **Immediate benefits:**
- **Code generation from model (Eclipse)** — Integration of UML with MOF standard supported use of CASE tools that could generate significant portions of code automatically from Class diagram, increasing productivity and ensuring consistency.
- **Improved communication** — With its open and pedantic standard, UML bridges communication gap among diverse stakeholders & developers.
- **Iteratively do designing** — UML's range of formedness of models allows developers to design big-picture, then design inside, and so on. Complex systems could be abstracted and then drilled-down.
- **Preserving archives** — Numerous large IT companies provide UML's CASE tool for diagram editing, allowing companies to preserve archived models.

**By Agile proponents** — While they didn't reject UML outright, they criticized its rigidity, time consumption, and overhead of creating detailed UML diagrams that became outdated as requirements evolved, and started looking for something better.

---

### **UML's Semantic Backplane — Notational Self-Consistency**
UML follows a strict regime of assigning **shape** and **outline** of Modeling Elements (ME) according to **type categorization** — namely structure and behaviour.

**Structure** is defined as a collection of ME for which:
- Composition defines uniqueness (of structure instance or type).
- Absence of any part disrupts integrity and operability of whole.
- Begin and end are definitely known and may even be definitive.

**Behaviour** is defined as a collection of ME for which:
- Repetition and/or duration defines uniqueness (of behaviour instance or type).
- Compositional integrity is not definitive.
- Begin and end may be unknown or unknowable.

**Structure diagrams use:** solid-outline shapes (rectangles, nodes, etc.) with **triangular** arrowheads.
**Behaviour diagrams use:** dashed or double-outline shapes with standard **arrowheads** (not triangles).

---

### **Overview of UseCase 2.0 Methodology (Revisited in L12)**
UC2.0 is **disruptive technology** to traditional Agile development that uses User stories. Such projects often suffer from **fragmentation debt** — where overall system context (big picture) is lost in a sea of disjointed PB items. UC2.0 is a beyond-worthy alternative by handling all scales of project, large to small scale.

It achieves this through its unique **three-method approach**:
1. **Preserves** reliable UseCase model to provide big-picture map of new sw.
2. **Reworks** "stories of usage" to ensure more robust specification that anticipates complexity before it hits development phase.
3. **Introduces Slices** to ensure that every realization delivers functional piece of new sw that is both architecturally sound and immediately valuable to user.

---

## Summary: RCM Types — Heavyweight vs. Lightweight

| **Feature** | **Heavyweight RE** | **Lightweight (User Story / UC2.0)** |
|---|---|---|
| SDM pairing | Heavyweight (SDLC) | Lightweight (XP, Scrum) |
| Approach | Big Requirements Up Front (BRUF) | Incremental/iterative/evolutionary |
| Specifications | PS (customer) + SRS (vendor) | Product Backlog (User Stories) / UseCase model + Slices |
| Documentation | Extensive | Minimal |
| Flexibility | Low | High |
| Key document | SRS | Product Backlog / UseCase model |
| Customer role | Elicits requirements, then largely done | Embedded in dev team throughout |
| Quality mechanism | QC (SRS audit) + QA (process audit) | Acceptance testing per story |
| Fragmentation risk | Low (single SRS) | High (PB fragmentation debt) |

---

*End of ICT2113 Software Modelling & Analysis Notes — compiled from all lecture materials.*
