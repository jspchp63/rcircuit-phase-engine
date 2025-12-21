# RCIRCUIT — Architecture Specification

This document defines the **structural architecture** of RCIRCUIT.

It does **not** describe:
- an implementation
- an optimization strategy
- a performance claim
- a task-level system

It defines **what must remain invariant** for the architecture to exist.

---

## Architectural Boundary

RCIRCUIT is defined by a single constraint:

> **Computation must occur without value transport.**

Any system that:
- moves values between compute units
- aggregates state globally
- synchronizes via centralized control

is **outside** the RCIRCUIT architecture,
regardless of performance or scale.

---

## Core Assumptions

RCIRCUIT assumes:

1. **Local phase evolution constitutes computation**
2. **Coherence is a structural invariant, not an emergent byproduct**
3. **Synchronization is a failure mode, not a solution**
4. **Transport introduces irreducible instability at scale**

These assumptions are architectural.
They are not tunable parameters.

---

## What RCIRCUIT Is Not

RCIRCUIT is **not**:
- a neural network architecture
- a faster accelerator
- a training framework
- a scheduling optimization
- a replacement for FLOPs-based scaling

Any interpretation that treats RCIRCUIT
as a performance improvement is incorrect.

---

## Structural Components

At the architectural level, RCIRCUIT consists of:

- **Phase Nodes**  
  Local state units evolving without external coordination

- **Local Coupling Rules**  
  Interaction limited to immediate neighbors

- **Coherence Constraints**  
  Conditions under which phase alignment is preserved or lost

No component requires:
- global clocks
- shared memory
- broadcast signals
- centralized control paths

---

## Failure-First Design Principle

RCIRCUIT is designed to be **falsifiable**.

The architecture is considered invalid if:

- coherence survives arbitrary value transport
- global synchronization improves stability
- scale alone resolves phase divergence

Experiments are constructed to **break** the architecture,
not to showcase success cases.

---

## Scope of This Document

This document specifies:
- architectural invariants
- allowed structural transformations
- disallowed operations

It does **not** specify:
- code structure
- APIs
- hardware layouts
- performance targets

Those belong to implementation layers
*outside* this specification.

---

## Relationship to Experiments

All experiments in this repository exist to test
whether this architecture **fails under constraint**.

If experimental results contradict this document,
the architecture must be revised or discarded.

---

## Canonical Reference

The formal definition of the compute primitive is given in:

**Phase Computing Engine (R CIRCUIT):  
A Transport-Free Compute Architecture**

DOI: https://doi.org/10.5281/zenodo.17925222

---

## Final Constraint

If RCIRCUIT works,
it must work **without transport**.

If it requires transport,
it is not RCIRCUIT.

No exceptions.
## Structural Notice

RCIRCUIT is not a system design, algorithm, or optimization technique.

This document specifies a **compute architecture defined by phase dynamics**,  
not by dataflow, instruction sequences, or state transition graphs.

No assumptions are made about hardware, programming models, or execution environments.  
Only structural invariants related to **local phase evolution and coherence survival** are defined.

Any attempt to interpret this architecture as a model, framework, or product  
indicates a category error.

This document exists solely to describe **what must not move**.

## Fixed Definition — RCIRCUIT / Phase Computing

1. Phase Computing is a transport-free compute paradigm where local phase evolution constitutes computation itself.
2. No values are moved, synchronized, or globally aggregated; coherence emerges solely from local coupling.
3. The architecture targets scalability limits caused by bandwidth, synchronization, and coherence collapse in conventional systems.

# RCIRCUIT Architecture Specification (v2)

This document describes the **structural architecture** of RCIRCUIT
as a phase-based, transport-free compute system.

It intentionally excludes motivation, philosophy, and narrative context.
Those are documented in README.md.

---

## Scope

This specification focuses on:

- Computational primitives
- Local phase evolution rules
- Coupling and coherence mechanisms
- Execution boundaries and non-goals

It does **not** claim completeness or production readiness.

---

## Architectural Premise

RCIRCUIT replaces value-transport-based computation with
**local phase evolution as the primary compute primitive**.

No global synchronization.
No value movement.
No centralized state.

Computation emerges from:
- Local phase drift
- Neighbor coupling
- Coherence preservation constraints

---

## Status

This architecture is **experimental and evolving**.

Interfaces, boundaries, and operators may change
as empirical validation continues.
