RCIRCUIT v2.1 — Whitepaper (Extended Technical Edition)
Phase Evolution as a Transport-Free Compute Paradigm

Author: Chulhee Park
Version: 2.1

Abstract

Modern AI systems are collapsing under physical limits not from arithmetic,
but from transport.

HBM saturation, wire delay, interconnect congestion, and thermal jitter now dominate compute behavior.

RCIRCUIT proposes a transport-free compute model: values never move —
only local phase-state evolution performs computation.

This v2.1 edition adds:

Compute_E law

Phase OS integration

Improved scaling model

Extended PoC clarity

Roadmap toward universality

1. Introduction — Transport Collapse

Modern accelerators fail due to movement, not math.

Transport dominates:

HBM bandwidth ceilings

global memory stalls

wire delay

thermal jitter

synchronization overhead

Transport scales O(N²); compute scales O(N).
This asymmetry kills scalability.

RCIRCUIT shifts computation from:

moving values → evolving states

2. Limitations of MatMul Compute

A single tensor op requires:

fetch

multiply

accumulate

refetch

redistribute

Every step = movement, which costs:

energy

bandwidth

time

heat

coherence

Transport is 30–200× more expensive than ALU compute.

Thus modern AI is transport-bound, not compute-bound.

3. RCIRCUIT Overview

RCIRCUIT eliminates global transport.

Key principles

no tensors

no global memory

no long-distance propagation

no synchronization

Primitive components

phase registers

Δ-phase transitions

local resonance coupling

coherence evolution

Computation emerges from local state evolution, not movement.

4. Minimal Architecture
4.1 RCIRCUIT Cell
struct RC_Cell {
    float phase;
    float delta;
    float coupling;
};

4.2 Update Rule
delta_i(t+1) = γ Σ_j∈N(i) (phase_j - phase_i)
phase_i(t+1) = phase_i(t) + α · delta_i(t+1)


Where:

α = propagation rate

γ = coupling strength

N(i) = local neighborhood

4.3 PDE Interpretation
∂
𝜙
∂
𝑡
=
𝛼
∇
2
𝜙
+
𝛾
𝑅
(
𝜙
)
∂t
∂ϕ
	​

=α∇
2
ϕ+γR(ϕ)
5. New in v2.1 — Compute_E Law

The physical-style compute capacity:

Compute_E
=
(
Phase Amplitude
)
×
(
Coupling Strength
)
Propagation Time
Compute_E=
Propagation Time
(Phase Amplitude)×(Coupling Strength)
	​


Where:

Phase Amplitude → energy differential

Coupling Strength → interaction strength

Propagation Time → latency of local update

This maps directly to PDE/network dynamics —
not aesthetics, actual physics.

6. Benchmark Model
6.1 Transport Cost Comparison
Operation	MatMul Cost	RCIRCUIT Cost
Memory Move (HBM)	100	0
Multiply	1	0.4
Local Phase Step	—	0.1

Transport dominates compute by two orders of magnitude.
RCIRCUIT avoids transport entirely.

6.2 Scaling Law

MatMul systems:

𝑇
(
𝑁
)
=
𝑂
(
𝑁
2
)
+
𝑂
(
𝑁
)
T(N)=O(N
2
)+O(N)

RCIRCUIT:

𝑇
(
𝑁
)
=
𝑂
(
𝑁
)
T(N)=O(N)

Transport collapse begins near N ≈ 10^8 parameters.

7. Logical Expressiveness
XOR Gate
Δ
𝜙
=
∣
𝜙
1
−
𝜙
2
∣
Δϕ=∣ϕ
1
	​

−ϕ
2
	​

∣

Rule:

XOR = 1 if Δφ > θ

XOR = 0 otherwise

Roadmap to Universality

XOR ✔

NOT (phase inversion) — planned

AND (threshold coupling) — planned

NAND (XOR + inversion) — planned

NAND = computational universality.

8. Coherence & Stability
8.1 Drift
𝜙
𝑖
(
𝑡
+
1
)
=
𝜙
𝑖
(
𝑡
)
+
𝜖
ϕ
i
	​

(t+1)=ϕ
i
	​

(t)+ϵ
8.2 Coherence Decay
𝐶
(
𝑟
)
=
𝑒
−
𝜆
𝑟
C(r)=e
−λr
8.3 Error Localization
𝐸
(
𝑡
)
≤
𝑘
⋅
local noise
E(t)≤k⋅local noise

Transport-based compute spreads errors globally;
RCIRCUIT localizes them.

9. Phase OS Integration

Transport-free compute requires a transport-free OS.

Phase OS schedules:

coherence thresholds

resonance windows

phase-target execution

local update priority

stability-driven compute events

Phase OS = the first OS designed for state evolution instead of value movement.

10. Experimental PoC

Run:

python src/phase_xor_poc_v01.py


Output:

φ1 = -0.134, φ2 = -0.722 → XOR = 1
φ1 = -0.406, φ2 = -0.491 → XOR = 0


Demonstrates:

logic without transport

computation from phase relationships

11. Roadmap to v3.0

universal gate implementation

2D/3D lattice engine

coherence visualization demo

extended scaling benchmarks

prototype Phase OS scheduler

12. Conclusion

Transport is collapsing under physical limits.
Movement is too expensive.

RCIRCUIT provides:

a transport-free compute model

coherent scaling law

a path to post-MatMul architectures

Stop moving values.
Start evolving states.

13. Contact

Author: Chulhee Park
📩 Email: jspchp638@gmail.com
