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
