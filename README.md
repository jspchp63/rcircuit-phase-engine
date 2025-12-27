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

## Case Studies — Coherence Failure by Transport

RCIRCUIT investigates coherence failure not only in compute systems,  
but also in **conversational and cognitive architectures** where meaning,
state, and continuity are reconstructed via transport.

### CASE 01 — Coherence Failure Under Minimal Transport

**CASE_01** establishes the baseline failure mode:

- Even minimal value transport introduces
  - phase misalignment
  - synchronization pressure
  - coherence decay
- Failure occurs **before** scale, FLOPs, or numerical precision become relevant

This case formalizes the hypothesis:

> **Coherence does not scale by moving information.  
> It scales by local resonance.**

See:  
`CASE_01.md`

---

### CASE 02 — GPT Context Coherence Failure (Live System)

**CASE_02** extends the same failure mode into a real-world system:

- GPT-style conversational AI
- Session boundaries
- Context windows
- Memory summarization
- Retrieval-based reconstruction

Observed effects:
- loss of conversational continuity
- emotional and philosophical discontinuity
- forced re-explanation
- user anxiety caused by apparent “memory resets”

This is **not** attributed to:
- insufficient intelligence
- lack of parameters
- poor training

It is attributed to the same root cause:

> **Meaning is forced to move.  
> Coherence collapses under transport.**

CASE_02 documents this failure **as it occurs live**,  
without proposing a solution or alternative architecture.

See:  
`docs/CASE02_GPT_COHERENCE_FAILURE_LIVE.md`

---

## Related Conceptual Whitepaper (Conversational AI)

A separate conceptual whitepaper isolates this failure mode formally:

- **GPT Context Failure — Transport vs Coherence**  
  *Failure analysis of conversational AI memory collapse under value transport.*

This document:
- proposes no solution
- introduces no new model
- offers no benchmark

It places only the question—precisely.

See:  
`docs/GPT_CONTEXT_FAILURE_Transport_vs_Coherence.md`  
DOI (Zenodo): https://doi.org/10.5281/zenodo.17925222

---

## Related Experimental Evidence (Phase-Based Systems)

The same coherence failure is observable in minimal phase simulations
when transport or global synchronization is introduced.

- **Experiment 06 — Coherence Decay Curve**  
  Measures coherence collapse as a function of transport pressure alone,  
  independent of scale or FLOPs.

See:  
`Experiment_06_Coherence_Decay.Curve.txt`

This experiment does **not** benchmark performance.  
It isolates **movement as the failure variable**.

---

## What Phase Computing Changes

Traditional compute assumes:  
> computation = moving values + operating on them

Phase Computing assumes:  
> computation = **local state evolution**

This is **not** an optimization.  
It is a **redefinition of compute**.

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
 
