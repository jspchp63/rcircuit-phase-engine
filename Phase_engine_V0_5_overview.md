# Phase Engine v0.5 — 2D Local Phase Simulator
**RCIRCUIT Transport-Free Compute Engine — Reference Implementation**

Author: *Chulhee Park*  
Status: Research Prototype

---

## 1. Purpose

Phase Engine v0.5 is the **first working engine** for the RCIRCUIT compute model.

- No tensors
- No global transport
- Only local phase evolution on a 2D grid
- O(N) local update cost

This file is the **reference implementation** used by the RCIRCUIT whitepaper and Compute_E law.

---

## 2. Core Idea

Each cell holds:

- `phase`  : local phase value  
- `delta`  : local update (Δ-phase)  
- `coupling` : effective interaction strength (through γ)

Update rule:

- local Laplacian → neighbor interaction  
- phase update → `phase = phase + α * delta`

This corresponds to the RCIRCUIT PDE form:

\[
\frac{\partial \phi}{\partial t} = \alpha \nabla^2 \phi + \gamma R(\phi)
\]

---

## 3. File Location

Engine code:

```text
src/phase_engine_v0_5_sim2d.py
Main entry point:

bash
코드 복사
python src/phase_engine_v0_5_sim2d.py
4. What It Demonstrates
Phase Engine v0.5 shows:

Transport-free compute loop

No global memory movement

Only local neighbor interactions (Laplacian)

Coherence metric

global_coherence() measures how aligned the field is

Values near 1.0 → strong global alignment

Values near 0.0 → random / disordered state

Compute_E connection

compute_E_scalar() gives a scalar proxy for:

Compute_E
=
Phase Amplitude
×
Coupling Strength
Propagation Time
Compute_E= 
Propagation Time
Phase Amplitude×Coupling Strength
​
 
This connects the law to a running engine

5. How to Run (Demo)
From the repo root:

bash
코드 복사
python src/phase_engine_v0_5_sim2d.py
You will see logs like:

text
코드 복사
=== RCIRCUIT Phase Engine v0.5 — 2D Demo ===
Grid        : 64 x 64
alpha       : 0.22
gamma       : 0.12
lambda_c    : 0.02
--------------------------------------------
step   20 | coherence =  0.1234 | Compute_E ≈  0.0567
step   40 | coherence =  0.2389 | Compute_E ≈  0.0812
...
If matplotlib is installed, you can enable plotting by editing the bottom of the file:

python
코드 복사
run_demo(
    steps=200,
    print_interval=20,
    preview_plot=True,  # set to True to see the final phase field
)
This will display a 2D phase field (often with stripe / wave-like patterns).

6. Next Steps (v0.6+ Roadmap)
Planned extensions:

Save phase field frames → animation (MP4/GIF)

Add basic phase gates (XOR/AND) on top of the field

Noise injection + recovery demo (coherence vs. time)

Phase Engine v0.5 is the baseline engine.
All future RCIRCUIT experiments will build on this file.
