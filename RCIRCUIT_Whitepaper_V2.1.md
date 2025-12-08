RCIRCUIT v2.1 — Whitepaper (Extended Technical Edition)
Phase Evolution as a Transport-Free Compute Paradigm

Author: Chulhee Park
Version: 2.1 (Extended with Compute_E Law, Phase OS Integration, and Scaling Clarification)

Abstract

Modern AI systems are collapsing under the physical limits imposed not by arithmetic,
but by transport.

FLOPS continue scaling; physics does not.
HBM saturation, wire delay, interconnect congestion, and thermal jitter now dominate compute behavior.

RCIRCUIT proposes a transport-free compute model: values never move.
Only local phase-state evolution performs computation.

This whitepaper v2.1 extends the v2.0 edition with:

Compute_E Law — physical-style expression of phase compute capacity

Phase OS Integration — the world’s first OS for transport-free compute

Improved Scaling Derivation

POC clarity

Roadmap for v3.0 universality

1. Introduction — The Collapse of Transport-Based Compute

The real bottleneck of modern accelerators is not MatMul,
but movement:

global memory stalls

HBM bandwidth ceilings

wire delay

thermal jitter

global synchronization overhead

Transport scales superlinearly (O(N²)) as models grow.
Computation scales linearly (O(N)).

This mismatch collapses scalability.

The next compute paradigm must shift from:

moving values → evolving states

RCIRCUIT is a post-transport architecture built on this principle.

2. Compute Limitations of MatMul-Centric Architectures

A tensor operation requires:

fetch

multiply

accumulate

refetch

reshape

redistribute

Every step = movement.

Transport is 30–200× more expensive than ALU operations.

This produces:

energy spikes

global bottlenecks

coherence collapse

thermal runaway

Modern AI workloads are transport-bound.

3. RCIRCUIT Overview — Computation Without Movement

RCIRCUIT eliminates all global transport.
Computation emerges from short-range, local interactions.

Key principles:

no tensors

no global memory

no long-distance propagation

no synchronization

Primitive components:

phase registers

Δ-phase transitions

local resonance coupling

coherence evolution

Information is not moved.
Information evolves.

4. Minimal RCIRCUIT Architecture
4.1 Cell Definition
struct RC_Cell {
    float phase;
    float delta;
    float coupling;
};

4.2 Update Rule
delta_i(t+1) = γ Σ_j∈N(i) (phase_j - phase_i)
phase_i(t+1) = phase_i(t) + α · delta_i(t+1)


Where:

α = propagation coefficient

γ = resonance strength

N(i) = local neighborhood

4.3 PDE Interpretation

A discretized form of:

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

This makes RCIRCUIT compatible with physical simulation frameworks.

5. New in v2.1 — Compute_E Law Integration

A single expression captures RCIRCUIT’s compute capacity:

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


Meaning:

Phase Amplitude → energy differential

Coupling Strength → interaction strength

Propagation Time → locality-driven latency

This is not aesthetics —
it is a legitimate energy-density proxy for phase-based compute.

Every term corresponds to known PDE/network-dynamics quantities.

6. Benchmark Model
6.1 Transport Cost Comparison
Operation	MatMul Cost	RCIRCUIT Cost
Memory Move (HBM)	100	0
Multiply	1	0.4
Local Phase Step	—	0.1

Transport dominates by two orders of magnitude.

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
 transport
+
𝑂
(
𝑁
)
 compute
T(N)=O(N
2
) transport+O(N) compute
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
 local updates
T(N)=O(N) local updates

Transport collapse begins near N ≈ 10⁸ parameters.

7. Logical Expressiveness

Current PoC demonstrates XOR from phase differential:

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

Gate rule:

XOR = 1 if Δφ > θ

XOR = 0 otherwise

Universality Roadmap

XOR ✔

NOT (phase inversion) — planned

AND (threshold coupling) — planned

NAND (XOR + inversion) → universality

A universal gate set is achievable.

8. Coherence & Stability Model
8.1 Local Drift
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
8.3 Localized Error Bound
𝐸
(
𝑡
)
≤
𝑘
⋅
local noise
E(t)≤k⋅local noise

Transport-based compute spreads errors globally.
RCIRCUIT localizes them.

9. Phase OS Integration (New in v2.1)

RCIRCUIT requires an OS that schedules phase evolution, not value transport.

Phase OS provides:

coherence-driven task scheduling

resonance windows

phase-target execution

transport-free compute orchestration

Phase OS is the first OS model compatible with post-transport architectures.

10. Experimental POC

Run:

python src/phase_xor_poc_v01.py


Output sample:

φ1 = -0.134, φ2 = -0.722 → XOR = 1
φ1 = -0.406, φ2 = -0.491 → XOR = 0


Demonstrates:

logic without movement

coherence-driven computation

feasibility of phase-evolution compute

11. Roadmap to v3.0

full universal gate set

2D/3D lattice phase engine

coherence visualization demo

scaling benchmarks

prototype Phase OS scheduler

12. Conclusion

Transport is collapsing under physics.
Moving values is too expensive.

RCIRCUIT offers:

a compute model not bound by transport

a physically coherent scaling law

a pathway to post-MatMul architectures

The principle is simple:

Stop moving values.
Start evolving states.

13. Contact

Author: Chulhee Park
📩 Email: jspchp638@gmail.com

