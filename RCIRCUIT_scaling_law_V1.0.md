RCIRCUIT Scaling Law Model v1.0 — Transport-Free Compute Scaling

Author: Chulhee Park
Status: Technical Model (v1.0)
Repository: https://github.com/jspchp63/rcircuit-phase-engine

1. Purpose

This document formalizes RCIRCUIT’s scalability advantage by deriving transport-cost behavior and comparing it to MatMul-based compute systems.

Scaling Law Model v1.0 answers:

Why does MatMul scale as O(N²)?

Why does RCIRCUIT scale as O(N)?

When does transport collapse begin?

What physical terms govern scaling behavior?



2. Background: Why Scaling Laws Matter

AI scaling is no longer math-bound.

Scaling laws today depend on:

HBM movement

Interconnect bandwidth

Wire delay

Memory hierarchy depth

Synchronization load

These are all movement-driven costs.

MatMul architectures are fundamentally transport-dominated, not compute-dominated.

3. MatMul Scaling Behavior

Modern accelerators perform:

Load → Multiply → Accumulate → Sync → Redistribute


Each step requires moving values across system boundaries.

3.1 Transport-Dominated Cost

Transport cost per parameter:

Cost_transport ≈ O(N)


For N parameters:

Total ≈ N × O(N) = O(N²)

Why O(N²)?

Because:

Each parameter must be moved many times

Movement scales with model dimension

Bandwidth and wire delay grow superlinearly

Transport dominates compute by 30–200×.

4. RCIRCUIT Scaling Behavior

RCIRCUIT eliminates transport:

No memory fetch
No global sync
No long propagation paths

Only local updates:

phase_i ← phase_i + α Σ_j∈N(i)(phase_j – phase_i)

4.1 Local Update Cost

Each node updates from its neighbors:

Cost_local ≈ constant × k   // k = neighborhood size


k is bounded (e.g., 4, 8, 12).
k does not grow with N.

Thus:

Total ≈ N × constant = O(N)

5. Scaling Threshold Analysis

Transport collapse begins when:

Transport_cost > Compute_cost


Substituting O(N²) vs O(N):

N² dominates when N > 10⁸


This matches real-world behavior:

GPT-3 scale (~175B params) → transport bottleneck already extreme

Llama/GPT-4 scale → wire delay & HBM saturation fully dominate

Thus:

**AI scaling collapsed not because math is hard,

but because transport does not scale.**

6. Compute_E and Scaling

RCIRCUIT uses the Compute_E expression:

Compute_E = (PhaseAmplitude × CouplingStrength) / PropagationTime


PropagationTime is strictly local, not global.

Thus Compute_E does not degrade with N.

Contrast:

Transport_Time ∝ model_size
Propagation_Time_local ∝ constant


This is the key physical reason RCIRCUIT remains linear-scale.

7. Comparison Table
Property	MatMul AI	RCIRCUIT
Movement	Global	Local
Complexity	O(N²)	O(N)
Sync	Required	None
Heat	Accumulates	Localized
Failure	Transport collapse	Local incoherence only
Scaling	Bandwidth-bound	Locality-bound
8. Visual Interpretation
MatMul (O(N²))

Think of N workers passing boxes across a warehouse:
Every worker touches almost every box → cost explodes.

RCIRCUIT (O(N))

Think of N workers updating only their own table:
Local only → scales linearly.

9. Experimental Requirements for Validation

To validate the scaling law experimentally (Phase Engine roadmap):

Large-scale lattice simulation

Measurement of per-update cost (constant vs size-dependent)

Fast-coherence decay profiling

Transport-free logic gate scaling

Propagation-time distribution analysis

이 실험은 Phase Engine v0.7 이후에서 가능해진다.

10. Conclusion

MatMul architectures face unavoidable collapse because:

Transport grows faster than compute.


RCIRCUIT avoids this entirely:

Transport removed → only local updates remain.


Thus:

MatMul scaling = O(N²)
RCIRCUIT scaling = O(N)

Transport-free compute is the most physically scalable compute model currently known.

11. Contact

Chulhee Park
📩 jspchp638@gmail.com
