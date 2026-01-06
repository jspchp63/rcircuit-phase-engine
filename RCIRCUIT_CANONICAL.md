# RCIRCUIT_CANONICAL.md
## Phase Computing Engine — Canonical Specification

Status: **Canonical / Locked**  
Author: **Chulhee Park**  
Last Update: 2026-01  
Scope: **Research Evidence / Pre-Product**

---

## 0. Canonical Declaration

This file is the **single source of truth** for RCIRCUIT.

- READMEs summarize.
- Experiments may expand.
- Implementations may change.

**This file does not.**

If any document, post, or repository conflicts with this file,  
**this file overrides all others.**

---

## 1. Exact Definition

**RCIRCUIT** is a **phase-based computation experiment** designed to test a single structural claim:

> **Large-scale computation fails primarily due to state transport and synchronization,
> not due to insufficient computation (FLOPs).**

RCIRCUIT removes value transport from computation and evaluates **coherence stability**
under identical dynamics.

RCIRCUIT is **not** a model, **not** a product, and **not** an optimization.

---

## 2. Core Hypothesis (Falsifiable)

> **Transport-based state updates destroy long-horizon coherence.
> Local phase-only evolution preserves coherence longer.**

This hypothesis must be **falsified** if any of the following holds:

1. Coherence remains stable as transport pressure increases  
2. Global synchronization outperforms local-only coupling in long-horizon stability  
3. Noise degrades transport-free systems more than transport-based systems  

If falsified, **RCIRCUIT is invalid**.

---

## 3. What Is Proven (Evidence Summary)

Across controlled simulations with identical dynamics:

- **Transport-based updates**
  - Accumulate noise
  - Amplify drift
  - Collapse coherence earlier

- **Local phase-only evolution**
  - Maintains coherence longer
  - Degrades more slowly under identical noise

These failures occur **before**:
- compute limits
- numerical precision limits
- learning or optimization effects

**Conclusion:** the dominant failure mode is **movement**, not computation.

---

## 4. Executable Evidence (Minimum Set)

RCIRCUIT provides **executable, reproducible evidence**.

- Repository:
  - `rcircuit-phase-engine`
- Demo:
  - `demo/demo_coherence_vs_transport.py`
- Output:
  - Coherence decay curves
  - Identical initial conditions
  - Increasing perturbation
  - Direct comparison: transport vs local-phase

This demo is **not a benchmark** and **not a learning task**.  
It is a **structural failure probe**.

---

## 5. Experimental Coverage (Completed)

The following experiment classes have been executed and documented
(independent probes, consistent outcome):

- Phase Diffusion
- Coupling Strength Sweep
- Coherence Decay Curves
- Resonance Threshold Scan
- Local Stability Region Mapping
- Phase Jump Settling Dynamics
- Noise Band Resonance Suppression
- Multi-node Coherence Propagation
- Long-Horizon Stability (10K steps)
- Global Phase Field Stability Mapping

Total: **20+ experiments**  
Data and configs are stored in:
- `rcircuit-phase-engine`
- `HROS-RCIRCUIT-LAB`

---

## 6. Metrics (Diagnostic Only)

RCIRCUIT uses diagnostic metrics **only to compare failure modes**:

- Coherence (phase alignment over time)
- Drift rate under noise
- Stability region boundaries

No performance, throughput, or efficiency claims are permitted.

---

## 7. Scope Boundary (Hard Limits)

RCIRCUIT explicitly does **not** do the following:

- ❌ Product implementation
- ❌ Performance optimization
- ❌ Learning / inference modeling
- ❌ AGI claims
- ❌ Hardware tapeout
- ❌ SDK delivery

Any description claiming otherwise is incorrect.

---

## 8. Relationship to Other Repositories

| Repository | Role |
|---|---|
| **rcircuit-phase-engine** | Executable evidence (this engine) |
| **HROS-RCIRCUIT-LAB** | Architecture, physics, documentation |
| **RFC-DRE_CANONICAL.md** | Downstream coherence evaluation |
| **RFC-DRE Lite** | Non-executable preparation space |

**Authority order:**
RCIRCUIT → RFC-DRE → HROS  
If RCIRCUIT is falsified, all downstream work is void.

---

## 9. Current Status (Truth)

- Hypothesis: **Defined**
- Evidence: **Executable**
- Experiments: **Completed (20+)**
- Productization: **None**
- Commercial readiness: **No**

RCIRCUIT is a **research evidence engine**, nothing else.

---

## 10. Canonical Closing Statement

> **If computation fails, first ask where state moves.
> If coherence collapses, movement is already the cause.**

---

## Signature

Author: **Chulhee Park**  
Canonical Authority: This file  
Contact: jspchp638@gmail.com
