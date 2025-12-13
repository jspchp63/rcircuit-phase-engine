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
