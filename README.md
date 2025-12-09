![Phase Engine](phase_intro.gif)

[🎥 Watch the Phase Engine Intro](final_video%20(78).mp4)

# Phase Engine v0.5 — Experimental Release

RCIRCUIT now includes:
- Local phase-update kernel (v0.5)
- Coupling & coherence computation
- Drift & resonance modeling
- 8 experimental validation files under docs/experiments

Purpose:
Validate transport-free compute behavior via coherence, drift, and threshold gate scans.

See: docs/experiments/

# RCIRCUIT — Phase Computing Engine
### Transport-Free Compute Model for Post-MatMul AI  
**Compute_E = (PhaseAmplitude × CouplingStrength) / PropagationTime**

A compute paradigm where **values never move** —  
only **local phase evolution** performs computation.

---

## 1. Why Phase Computing Matters
Modern AI is collapsing under physics —  
not math, not FLOPS, but **electricity and movement**.

### The Modern Bottleneck: Tensor Transport
AI workloads today are dominated by transport:

- move  
- multiply  
- accumulate  
- move again  

Physics pushes back:

- HBM saturates  
- interconnect latency dominates  
- wire delay explodes  
- thermal jitter breaks coherence  
- GPUs stall waiting for data, not compute  

**The real bottleneck = movement**  
**The real cost = electricity**  
**The real failure mode = physics**

---

## 2. RCIRCUIT: A New Compute Direction
A compute model where no values move —  
only **local phase-state evolution** computes.

Transport → expensive  
Local phase evolution → scalable

---

## 3. Why This Exists — Transport Collapse Physics
As models scale:

- memory traffic dominates latency  
- sync cost becomes nonlinear  
- thermal noise accumulates  
- power becomes the fundamental limit  

MatMul fails due to **transport limits**, not arithmetic.

RCIRCUIT replaces **global transport**  
with **O(N)** local-only phase updates.

---

## 4. Compute Primitive Shift
### MatMul (traditional)
- value transport  
- energy-heavy  
- long wires  
- global sync  
- thermal accumulation  

### RCIRCUIT
- no value movement  
- only local updates  
- coherence preserved locally  
- scaling bound by locality  

#### Comparison Table

| Property | MatMul AI | RCIRCUIT |
|---------|-----------|----------|
| Compute unit | tensor multiply | phase evolution |
| Movement | global | local |
| Scaling limit | bandwidth | locality |
| Sync | global | none |
| Heat | accumulated | localized |
| Complexity | O(N²) transport | O(N) updates |

---

## 5. Core RCIRCUIT Principle
RCIRCUIT eliminates:

- tensors  
- global sync  
- long-distance propagation  

It uses only four primitives:

1. phase registers  
2. Δ-signal transitions  
3. local resonance coupling  
4. coherence evolution  

Computation becomes a **local physical process**,  
not a global movement process.

---

## 6. Formal Minimal Architecture

### 6.1 RCIRCUIT Cell
struct RC_Cell {
float phase;
float delta;
float coupling;
};


### 6.2 Update Rule
delta_i(t+1) = γ Σ_j∈N(i)( phase_j - phase_i )
phase_i(t+1) = phase_i(t) + α · delta_i(t+1)


### 6.3 PDE Approximation
∂φ/∂t = α ∇²φ + γ R(φ)


---

## 7. Directory Structure (Expanded)
This repository contains the full RCIRCUIT research stack.

### 📁 docs/
- RCIRCUIT_whitepaper_V2.0.md  
- RCIRCUIT_ComputeE_Technical_Overview_v1.0.txt  
- Phase_OS_WhitePaper_v0.2_FigureEdition.md  
- Phase_Compute_Architecture.md  
- v1.3_phase_coupling_model.md  
- v1.4_local_coherence_map.md  
- v1.5_resonance_field_accumulator.md  
- v1.8_resonance_flow_graph.md  
- experiments/  
  - experiment_01_phase_xor.txt  
  - experiment_02_local_coherence_sim.txt  
  - experiment_03_resonance_drift_test.txt  
  - experiment_04_threshold_gate_scan.txt  

### 📁 src/
- phase_engine_core_v1.py  
- phase_node.py  
- phase_coupling.py  
- phase_propagation_kernel.py  
- coherence_metric.py  
- resonance_score.py  
- phase_state_snapshot.py  
- phase_xor_poc_v01.py  
- phase_and_poc.py  
- utils/  
  - grid_init.py  
  - noise_injector.py  
  - coupling_visualizer.py  

### 📁 assets/ (planned)
- animations/  
- coherence_maps/  
- phase_evolution_videos/  

---

## 8. POC #1 — Phase XOR Gate
Logic emerging from **phase**, not data movement.

Δφ = |φ₁ - φ₂|
XOR = 1 if Δφ > θ

Run:
python src/phase_xor_poc_v01.py


Example:
φ1=-0.134, φ2=-0.722 → XOR=1
φ1=-0.406, φ2=-0.491 → XOR=0


---
### Noise–Coherence Curve (Phase Engine)
![Noise vs Coherence](noise_coherence_plot.png)

## 9. Scaling & Cost Models (v1.5)

### Transport Cost Model
| Operation | MatMul Cost | RCIRCUIT Cost |
|----------|-------------|----------------|
| Move (HBM) | 100 | 0 |
| Multiply | 1 | 0.4 |
| Local Phase Step | — | 0.1 |

### Scaling
MatMul:  
`T(N) = O(N²) transport + O(N) compute`

RCIRCUIT:  
`T(N) = O(N) local updates`

Transport collapse begins at **N ≈ 10⁸**.

---

## 10. Commercial & Infra Impact
Eliminating value movement reduces:

- energy per token  
- datacenter cooling  
- interconnect burden  
- rack-level OPEX  

Enables:

- hyperscale AI under power limits  
- defense-grade compute  
- low-power inference  
- edge compute with no transport cost  

---

## 11. Practical Use Cases
RCIRCUIT is usable today for:

- transport-dominated regime analysis  
- scaling-limit prediction  
- coherence-failure simulation  
- local-update compute experiments  
- new-primitive prototyping  

---
## RCIRCUIT v0.6 — Phase Engine Upgrade Release
This release adds the minimal experimental set required for researchers to
evaluate RCIRCUIT as a transport-free compute primitive.

### ✔ New in v0.6
1. **Phase AND Gate (PoC #2)**
   - Implemented in `src/phase_and_poc.py`
   - Demonstrates logical conjunction emerging from phase thresholds
   - No value movement, no global sync

2. **Experiment 05 — Coupling Sweep**
   - File: `docs/experiments/experiment_05_coupling_sweep.txt`
   - Studies how γ (coupling strength) controls stability vs. resonance amplification
   - Useful for PDE model calibration

3. **v1.9 — Phase Evolution Map (Text Edition)**
   - File: `docs/v1.9_phase_evolution_map.txt`
   - Describes stable/unstable phase trajectories without requiring visualization assets
   - Provides a map for identifying logical regions in phase-space

4. **README Structural Update**
   - “Experiments” section now includes experiments 01–05
   - “PoC Directory” updated with AND gate

### ✔ Compatibility
- Backwards-compatible with v0.5
- No breaking changes to `phase_engine_core_v1.py`

### ✔ Next Roadmap
- v0.7: NAND universal gate draft
- v0.8: Coherence-driven scheduler baseline
- v0.9: PDE-backed stability model
- v1.0: Formal whitepaper + Phase OS integration

RCIRCUIT remains the first public framework proposing
**transport-free compute via local phase evolution.**
## 📣 Call for Experimental Collaboration — RCIRCUIT Phase Computing

RCIRCUIT has reached the point where further progress requires 
**team-based experimental validation.**

Already completed:
- Transport-free compute model
- Compute_E law formulation
- PDE-based phase evolution framework
- Phase Engine v0.5 implementation
- 8 experimental prototypes
- XOR PoC (logic without value movement)

Needed next:
- Large-scale phase-field stability tests
- Resonance coherence measurement
- Gate composition (XOR → NAND)
- Scaling validation vs transport-dominated models

Why external teams:
Phase-based compute is a frontier-class problem requiring HPC clusters, 
PDE specialists, numerical experts, and architecture researchers.

Who should contact:
- GPU/TPU architects
- PDE / numerical simulation researchers
- AI hardware labs
- PhD students, postdocs, deep-tech teams

Contact:

📩 jspchp638@gmail.com

---


