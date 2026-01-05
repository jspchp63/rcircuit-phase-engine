# RCIRCUIT — Phase Computing

> Transport-free coherence experiment  
> Testing whether computation collapses due to state transport.

---

## ONE EXPERIMENTAL QUESTION

Does coherence collapse because computation moves?

---

## HYPOTHESIS 

Transport-based state updates destroy long-horizon coherence.  
Local phase evolution without transport preserves coherence longer.

This repository exists only to falsify this hypothesis.

---

## WHAT IS TESTED

Two systems with identical dynamics:

1. Transport-based update
   - state movement
   - global synchronization

2. Transport-free phase evolution
   - no state movement
   - local phase coupling only

Measured variable:
- coherence decay over time under increasing noise

---

## EXECUTABLE DEMO

Run:

python demo/demo_coherence_vs_transport.py

Produces:
- coherence decay curves
- identical initial conditions
- increasing perturbation

Observed:
- transport-based updates lose coherence faster

This is not a benchmark.
This is not a learning task.
This is a structural failure probe.

---

## DATA OVER CLAIMS

If coherence remains stable under transport,
this repository is wrong.

---

## RELATION TO RFC-DRE LITE

RCIRCUIT:
- explains why coherence collapses

RFC-DRE Lite:
- explores partial recovery strategies

RFC-DRE Lite is not implemented here.

---

## WHAT THIS IS NOT

- not a product
- not an SDK
- not AGI theory
- not performance research

---

## CURRENT STATE

- hypothesis defined
- transport vs local-phase demo implemented
- coherence probes completed
- no persistence layer
- no session reconstruction

---

## LICENSE

Phase OS Research License  
inspection and evaluation only

---

## AUTHOR

Chulhee Park  
RCIRCUIT / Phase Computing

---

## FINAL FENCE

If transport does not destroy coherence,
discard this work.
