# RCIRCUIT — Phase Computing Engine

## What this repository is

This repository does **not** propose a faster model.

It tests a single question:

**Does computation fail because of insufficient FLOPs,  
or because of transport and synchronization?**

RCIRCUIT is a phase-based computing engine designed to  
*falsify* architectures that assume scale fixes coherence.

All experiments here are minimal, failure-first,  
and intentionally run before optimization.

---

# ⚠️ READ BEFORE PROCEEDING

This repository is **not** written for general AI users, students,  
or content consumers.

It is written **exclusively** for:
- system architects
- compute researchers
- hardware / accelerator designers
- researchers investigating **transport, coherence, and physical limits of computation**

If you are not actively working on these problems,  
**this repository is not for you.**

---

## Fixed Definition — RCIRCUIT / Phase Computing

- **Phase Computing** is a *transport-free compute paradigm* where  
  **local phase evolution constitutes computation itself**.
- **No values are moved, synchronized, or globally aggregated**;  
  coherence emerges solely from **local coupling**.
- The architecture targets scalability limits caused by  
  **bandwidth**, **synchronization**, and **coherence collapse**  
  in conventional compute systems.

> This document describes **structure**, not **implementation**.

---

## Repository Scope

This repository documents an **evolving compute architecture**.

It is **not**:
- a finished system
- a benchmark suite
- a performance claim
- an SDK or product demo
- a paper supplement

Formal structural specifications are defined in **`ARCHITECTURE.md`**.

---

## Core Premise

Modern AI systems do not fail because of mathematics.  
They fail because **computation still moves**.

- Activations move  
- Gradients move  
- Weights move  
- Memory moves  
- Synchronization moves  

At scale, this movement dominates:
- latency
- energy
- coherence loss
- system instability

RCIRCUIT removes **movement** from computation.

**Local phase evolution is the compute.**

---

## What Phase Computing Changes

Traditional compute assumes:  
> computation = moving values + operating on them

Phase Computing assumes:  
> computation = **local state evolution**

This is **not** an optimization.  
It is a **redefinition of compute**.

---

## Canonical Whitepaper (DOI)

**Phase Computing Engine (R CIRCUIT):  
A Transport-Free Compute Architecture**

DOI (latest):  
https://doi.org/10.5281/zenodo.17925222

This document defines the **compute primitive**.  
This repository explores its **failure behavior**.

---

## Experimental Record

Experiments here are **structural probes**, not benchmarks.

Each experiment asks one question only:

> **Does coherence survive under this condition?**

If you are searching for SOTA numbers, stop here.  
If you are searching for **failure modes**, continue.

---

## License

**Phase OS Proprietary License**

Published for **inspection and evaluation only**.

- No redistribution  
- No modification  
- No derivative works  
- No commercial use  

All rights reserved.

---

## Credits

Created by **Chulhee Park**  
Inventor of the Transport-Free Compute Architecture  
and the RCIRCUIT Phase Computing Engine

For a concrete falsification path, see:  
`docs/HOW_TO_DISPROVE_RCIRCUIT.md`

If this architecture fails,  
it will fail here.

If you think it already does,  
**show me.**




