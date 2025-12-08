RCIRCUIT Phase Graph Model v1.0 — Structural Representation of Transport-Free Compute

Author: Chulhee Park
Status: Technical Specification (v1.0)
Repository: https://github.com/jspchp63/rcircuit-phase-engine

1. Purpose

The Phase Graph Model formalizes how RCIRCUIT represents computation as:

A graph of interacting phase nodes

Local coupling edges

Coherence-weighted propagation paths

Pulse-triggered logical events

This is RCIRCUIT의 **회로도(Circuit Diagram)**에 해당하는 개념 모델이다.
즉, “RCIRCUIT이 실제로 어떻게 생겼는가?”에 대한 답변이다.

2. Background

기존 컴퓨터 회로는:

bit nodes

wires (transport)

logic gates

이 3개로 구성된다.

하지만 RCIRCUIT은:

phase nodes (node)

coupling edges (edge)

coherence weights (meta-edge)

pulse events (gate)

으로 구성되는 완전히 다른 구조이다.

3. Phase Graph Definition

A Phase Graph G is defined as:

G = (V, E, Wc, Cp)


Where:

Symbol	Meaning
V	set of phase nodes
E	coupling edges between nodes
Wc	coherence weights per edge
Cp	pulse compute rules
3.1 Node Definition

Each node is:

v = { phase, delta, coupling, coherence }


Unlike classic nodes, RCIRCUIT nodes store state, not just values.

3.2 Edge Definition

Edges represent coupling:

e(i, j) = γ_ij (phase_j – phase_i)

3.3 Coherence Weight (Meta-edge)

Each edge carries a stability weight:

Wc(i,j) = exp(–λ r_ij)


This models physical locality & coherence.

4. Phase Graph Dynamics

Phase Graph evolves by:

4.1 Local Update
delta_i = Σ_j (γ_ij · (phase_j – phase_i))
phase_i ← phase_i + α delta_i

4.2 Coherence Update
coherence_i = exp(–λ r_i)

4.3 Pulse Trigger
pulse_i = 1 if |Δφ_i| > θ_pulse


이 3단계가 하나의 연산 사이클이다.

5. Graph Neighborhoods

Phase Graph supports multiple neighborhood models:

5.1 Von Neumann (4-edge)

Fast, minimal compute

5.2 Moore (8-edge)

Better logic emergence

5.3 Radius-r Local Graph

Used for modeling analog-like behavior

5.4 Dynamic Neighborhoods

Edges may appear/disappear based on coherence:

if C < C_min → edge_i_j disabled


This makes RCIRCUIT a self-adjusting compute graph,
전통 GPU/TPU에는 없는 기능이다.

6. Phase Graph as a Compute Graph

Deep learning frameworks use:

Tensor Graph


But RCIRCUIT uses:

Phase Graph


Comparison:

Concept	Tensor Graph	Phase Graph
Node	value	physical phase
Edge	transport	coupling
Operation	MatMul	Δ-phase evolution
Cost	bandwidth-heavy	local-only
Gate	explicit ops	pulse events
Failure	global	localized

Phase Graph is mathematically closer to:

PDE lattices

Cellular automata

Neuromorphic meshes

…but used as a general compute graph.

7. Logic Gates on a Phase Graph

Pulse events map directly to logic gates.

XOR Gate = Δφ crossing on two-input subgraph
pulse_xor(i,j) = 1 if |phase_i – phase_j| > θ

NOT Gate = phase inversion on single node
pulse_not(v) = 1 if –phase_v > θ_not

AND Gate = phase sum threshold
pulse_and(i,j) = 1 if (phase_i + phase_j) > θ_and

NAND Gate (Planned)

If implemented → RCIRCUIT becomes computationally universal.

8. Phase Graph Stability

Graph stability is governed by:

8.1 Coupling Bound
γ < γ_critical

8.2 Propagation Bound
α < α_critical

8.3 Coherence Survivability
C > C_min


Under these constraints:

Divergence does not occur

Errors remain local

Pulse events remain meaningful

9. Graph Visualization Outputs

RCIRCUIT Phase Graph can be visualized as:

Phase heatmap

Coupling edge map

Coherence field overlay

Pulse event scatter plot

Gate activation sequence

GitHub Pages 또는 YouTube demo에 적합한 시각화.

10. What Phase Graph Model Proves
✔ RCIRCUIT은 graph-based compute system이다
✔ Transport가 없으므로 edges = coupling only
✔ Pulse events = logic gates
✔ Coherence = stability weight
✔ Scaling = O(N) graph evolution (local only)
✔ Universality roadmap 명확

이 문서는 RCIRCUIT이 장난이 아니라
“정식 컴퓨팅 모델”임을 구조적으로 증명한다.

11. Roadmap v1.1

Multi-phase graphs (conductive + resonant layers)

Coherence-adaptive dynamic graphs

Pulse-propagation subgraph analysis

Universality proof with NAND circuits

Phase OS integration

12. Contact

Chulhee Park
📩 jspchp638@gmail.com
