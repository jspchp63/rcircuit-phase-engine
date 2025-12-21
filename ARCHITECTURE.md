## RCIRCUIT — Architecture Specification

This document defines the **structural architecture** of RCIRCUIT.

It does **not** describe:
- an implementation
- an optimization strategy
- a performance claim
- a task-level system
- a product or framework

It defines **what must remain invariant** for the architecture to exist.

This document is **normative**.
If experimental results contradict it, the architecture must be revised or discarded.

---

## Architectural Boundary

RCIRCUIT is defined by a single non-negotiable constraint:

> **Computation must occur without value transport.**

Any system that:
- moves values between compute units
- aggregates state globally
- relies on centralized synchronization
- introduces global control paths

is **outside** the RCIRCUIT architecture,
regardless of scale, performance, or implementation medium.

---

## Fixed Definition — Phase Computing (RCIRCUIT)

RCIRCUIT is a **phase computing architecture** in which:

1. **Local phase evolution constitutes computation**
2. **No values are moved, synchronized, or globally aggregated**
3. **Coherence emerges solely from local coupling**
4. **Synchronization is treated as a failure mode, not a solution**
5. **Transport introduces irreducible instability at scale**

These properties are **architectural invariants**.
They are not tunable parameters or design choices.

---

## Core Assumptions

RCIRCUIT assumes:

- Computation is a property of **local state evolution**, not dataflow
- Coherence must be preserved structurally, not recovered statistically
- Scale does not repair architectural instability
- Failure modes are more informative than success cases

---

## Structural Components

At the architectural level, RCIRCUIT consists of:

- **Phase Nodes**  
  Local state units evolving without external coordination

- **Local Coupling Rules**  
  Interactions restricted to immediate neighbors

- **Coherence Constraints**  
  Conditions under which phase alignment is preserved or lost

No component requires:
- global clocks
- shared memory
- broadcast mechanisms
- centralized schedulers

---

## What RCIRCUIT Is Not

RCIRCUIT is **not**:
- a neural network architecture
- a training or inference framework
- an accelerator optimization
- a scheduling technique
- a FLOPs-scaling strategy
- a product specification

Any interpretation of RCIRCUIT as a performance improvement
constitutes a category error.

---

## Failure-First Principle

RCIRCUIT is designed to be **falsifiable**.

The architecture is invalid if:

- coherence survives arbitrary value transport
- global synchronization improves stability
- increased scale alone resolves phase divergence

Experiments must attempt to **break** these assumptions.
Survival without violation does not constitute proof.

---

## Relationship to Experiments

All experiments in this repository exist solely to test
whether this architecture **fails under constraint**.

Experimental results do not refine the architecture;
they either **support** or **invalidate** it.

---

## Canonical Reference

The formal definition of the compute primitive is given in:

**Phase Computing Engine (R CIRCUIT):  
A Transport-Free Compute Architecture**

DOI: https://doi.org/10.5281/zenodo.17925222

---

## Final Fence

If RCIRCUIT works,
it must work **without transport**.

If transport is required,
it is **not RCIRCUIT**.

No exceptions.
