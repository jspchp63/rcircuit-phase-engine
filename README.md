# RCIRCUIT — Phase Computing Engine

> **Transport-free compute research framework**  
> Falsifying the assumption that scale fixes coherence.

---

## 🔴 ONE QUESTION  || READ THIS FIRST ||

This repository asks **one falsifiable question**:

**Does large-scale computation fail primarily because of insufficient compute,  
or because coherence collapses when state is transported and synchronized?**

**Claim (to be falsified):**  
Transport-based state reconstruction fails to preserve long-term coherence.  
Local phase evolution without transport preserves coherence longer.

This claim should be falsified if **any** of the following holds:

1. Coherence remains stable as transport pressure increases  
2. Global synchronization outperforms local-only coupling in long-horizon stability  
3. Noise degrades transport-free systems more than transport-based systems  

All documents, cases, and experiments in this repository exist **solely**  
to test this question.

If you believe this question is already answered,  
point to the **exact mechanism or metric** that disproves it.

---

## ⚠️ WHO THIS REPOSITORY IS FOR 

This repository is **not** for:
- students
- beginners
- prompt engineers
- product demo seekers

It is written **exclusively** for:
- system architects
- compute / interconnect researchers
- AI hardware designers
- researchers investigating **coherence, transport, and physical limits of computation**

If the problem statement feels obvious,  
you are expected to **disprove it**, not agree with it.

---

## 🧠 CORE PREMISE

Modern AI systems do not fail because of mathematics.  
They fail because **computation still moves**.

At scale:
- activations move  
- gradients move  
- weights move  
- memory moves  
- synchronization moves  

This movement dominates:
- latency
- energy
- coherence loss
- system instability

**RCIRCUIT removes movement from computation.**  
Local phase evolution **is** the compute.

---

## 🧪 DEMO — Coherence vs Transport (NEW)

Run:
python demo/demo_coherence_vs_transport.py

This repository includes a **minimal executable demo**  
that visualizes the core failure mode.

### What the demo shows

- Two systems with identical dynamics:
  - **Transport-based update**
  - **Local-only phase evolution**
- Increasing noise / perturbation
- Measured coherence over time

**Result:**  
Transport-based systems lose coherence significantly faster,  
even under minimal transport pressure.

📂 **Location:**  
`/demo/demo_coherence_vs_transport.py`

📸 **Output:**  
Local plot comparing coherence decay curves

> This is **not a product demo**.  
> It is a **falsification-oriented evidence demo**.

---

## 🧩 HOW THIS DEMO FITS THE RESEARCH STACK

The demo is **not RFC-DRE Lite**.  
It is the **foundational evidence layer** that RFC-DRE depends on.

Positioning:

- RCIRCUIT → explains **why transport fails**
- Demo → shows **coherence collapse is structural**
- RFC-DRE Lite (future) → exploits this to recover continuity

---

## 📁 HOW TO READ THIS REPOSITORY 

### STEP 1 — Problem Framing
- `README.md`

### STEP 2 — Structural Assumptions
- `ARCHITECTURE.md`

Check for internal consistency:
- transport-free local phase evolution
- no global synchronization
- coherence as a stability property

### STEP 3 — Minimal Failure Baseline
- `CASE_01.md`

Establishes coherence decay caused by **transport alone**.

### STEP 4 — Real-System Analogy
- `docs/CASE02_GPT_COHERENCE_FAILURE_LIVE.md`

Documents live conversational coherence failure  
under forced context transport.

### STEP 5 — Experiments (Structural Probes)
- `Experiment_*`
- `src/`

These are **not benchmarks**.  
Each asks one question only:

> Does coherence survive under this condition?

---

## ❗ WHAT THIS REPOSITORY IS NOT

- not a finished system  
- not a performance benchmark  
- not an SDK  
- not a product pitch  
- not an AGI proposal  

If you are searching for SOTA numbers, stop here.

---

## 🧱 CURRENT STATUS 

- ✅ Structural theory defined
- ✅ Multiple coherence experiments completed
- ✅ Executable coherence-vs-transport demo added
- ❌ RFC-DRE Lite not yet implemented
- ❌ No persistent state or session reconstruction
- ❌ No commercial product

This repository is **research-grade**, not market-ready.

---

## 🛣️ INTENDED NEXT STEPS

1. Extend demo → resonance / DRE score
2. Add minimal persistent state vector
3. Demonstrate cross-session coherence reconstruction
4. Split RFC-DRE Lite into a separate repository

---

## 🔗 Related Work — RFC-DRE Lite  || Executable Demo ||

A separate repository, **RFC-DRE Lite**, is under development.

Purpose:
- Provide a minimal executable demo
- Explore coherence reconstruction and continuity
- Operate strictly at the software / session level

Important:
- RFC-DRE Lite does NOT implement RCIRCUIT
- It does NOT validate Phase Computing
- It depends on the same coherence-failure premise demonstrated here

Relationship:
- RCIRCUIT → explains why transport fails (structural)
- This demo → shows coherence collapse experimentally
- RFC-DRE Lite → tests recovery strategies under the same constraint

RFC-DRE Lite is intentionally separated
to preserve the falsification integrity of this repository.

## 📜 LICENSE

**Phase OS Proprietary License**

Inspection and evaluation only.  
No redistribution.  
No modification.  
No commercial use.

---

## ✍️ AUTHOR

**Chulhee Park**  
Inventor — Transport-Free Compute Architecture  
RCIRCUIT / Phase Computing Engine

Falsification guide:  
`docs/HOW_TO_DISPROVE_RCIRCUIT.md`

---

## FINAL NOTE

This repository is intentionally dense.  
Intentionally selective.  
Intentionally uncomfortable.

If coherence matters to you, continue.  
If not, this repository is already working as intended.

---


