# RCIRCUIT Phase Compute Prototype v1.0 — Design Spec

Phase Computing · Δ-signal Engine · Local Coherence Simulation

---

## 0. Scope & Goal

This document defines the minimal executable prototype of the RCIRCUIT Phase Compute Engine (v1.0).

Goal of v1.0:

- Implement a small phase graph (8–64 nodes).
- Evolve phase states via Δ-signal propagation, not bulk value movement.
- Compute local & global coherence at each step.
- Demonstrate noise-under-phase behavior and propagation gating.

This is not a hardware spec.  
It is a simulation-level compute primitive for researchers who understand:

> Modern AI isn’t compute-bound. It’s interconnect-bound.

---

## 1. Core Concepts

### 1.1 Node

- Discrete compute element.
- Indexed by integer `node_id`.
- Holds a phase state and internal Δ-signal accumulator.

### 1.2 Phase State

- Continuous angle in `[0, 2π)` or `[-π, π)`.
- Denoted `φ_i(t)` for node `i` at time step `t`.
- Represents compute state as phase, not numeric value.

### 1.3 Δ-signal

- Small change term derived from neighbor phases.
- Denoted `Δ_i(t)` or `d_i(t)`.
- Represents meaningful change, not absolute value.

### 1.4 Edge / Coupling

- Weighted connection between nodes `i` and `j`.
- Weight `w_ij` encodes coupling strength.
- Optional: directed vs undirected.

### 1.5 Local Coherence

- Measures how aligned a node’s neighborhood is.
- High local coherence → stable phase band.
- Low local coherence → noisy or de-synchronized.

### 1.6 Global Coherence

- Aggregation of local coherence across the graph.
- Used as a propagation gate:
  - Below threshold → limited update.
  - Above threshold → full update.

---

## 2. Mathematical Model (v1.0 Minimal)

We use a Kuramoto-inspired but simplified phase update.

### 2.1 Neighborhood Phase Influence

For node `i` with neighbors `N(i)`:

\[
F_i(t) = \sum_{j \in N(i)} w_{ij} \cdot \sin(\phi_j(t) - \phi_i(t))
\]

Intuition:

- If neighbors are in similar phase, `F_i(t)` is large and coherent.
- If neighbors are random, `F_i(t)` tends to cancel out.

### 2.2 Δ-signal Definition

We define Δ-signal as a clipped version of the local field:

\[
\Delta_i(t) = \text{clip}(F_i(t), -D_{\max}, D_{\max})
\]

Where:

- `D_max` is a hyperparameter (max allowed Δ per step).
- `clip(x, a, b)` limits `x` into `[a, b]`.

### 2.3 Phase Update Rule

Phase evolves as:

\[
\phi_i(t+1) = \text{wrap}\big(\phi_i(t) + \alpha \cdot \Delta_i(t) + \eta_i(t)\big)
\]

Where:

- `α` : phase learning rate (0 < α ≤ 1).
- `η_i(t)` : noise term (e.g. Gaussian with small σ).
- `wrap(·)` : maps angle back to `[0, 2π)`.

### 2.4 Local Coherence Metric

For node `i`:

\[
C_i(t) = \left| \frac{1}{|N(i)|} \sum_{j \in N(i)} e^{j \phi_j(t)} \right|
\]

- `C_i(t) ∈ [0, 1]`
- `1` → perfectly aligned neighborhood.
- `0` → fully de-synchronized.

### 2.5 Global Coherence

\[
C_{\text{global}}(t) = \frac{1}{|V|} \sum_{i \in V} C_i(t)
\]

Used as a phase OS gate.

---

## 3. Propagation Gate (Non-Movement Compute)

We interpret global coherence as a gate on how aggressively the system can propagate phase.

Let:

- `C_min` : coherence threshold.
- `γ_low` : low update gain when coherence is poor.
- `γ_high` : full update gain when coherence is good.

Define effective update gain `G(t)`:

\[
G(t) = 
\begin{cases}
\gamma_{\text{low}}, & C_{\text{global}}(t) < C_{\min} \\
\gamma_{\text{high}}, & C_{\text{global}}(t) \geq C_{\min}
\end{cases}
\]

Then phase update becomes:

\[
\phi_i(t+1) = \text{wrap}\big(\phi_i(t) + G(t) \cdot \alpha \cdot \Delta_i(t) + \eta_i(t)\big)
\]

This implements non-movement compute:

- We never transport full state values.
- We propagate only Δ-signal and adjust phase locally.
- Global coherence controls how much phase is allowed to move.

---

## 4. Engine State Representation (v1.0)

### 4.1 Core Data Structures (Conceptual)

    num_nodes: int

    phase: float[num_nodes]          # φ_i(t)
    delta: float[num_nodes]          # Δ_i(t)
    noise: float[num_nodes]          # η_i(t)

    # Adjacency / coupling
    neighbors: list[list[int]]       # N(i) for each i
    weights: list[list[float]]       # w_ij for each neighbor j of i

    # Coherence
    local_coherence: float[num_nodes]   # C_i(t)
    global_coherence: float             # C_global(t)

### 4.2 Hyperparameters

- `alpha` : base update step for Δ-signal.
- `D_max` : max allowed Δ magnitude.
- `C_min` : global coherence threshold.
- `gamma_low`, `gamma_high` : low/high effective gains.
- `noise_std` : standard deviation for `η_i(t)`.
- `num_steps` : simulation length.

---

## 5. Update Cycle (Single Time Step)

Single-step pseudocode (conceptual):

    def step(state, params):
        """
        state: phase, delta, neighbors, weights, ...
        params: alpha, D_max, C_min, gamma_low, gamma_high, noise_std
        """

        # 1) Compute Δ-signal for each node
        for i in range(num_nodes):
            F_i = 0.0
            for k, j in enumerate(neighbors[i]):
                w_ij = weights[i][k]
                F_i += w_ij * math.sin(phase[j] - phase[i])
            delta[i] = clip(F_i, -D_max, D_max)

        # 2) Compute local coherence
        for i in range(num_nodes):
            if len(neighbors[i]) == 0:
                local_coherence[i] = 0.0
                continue
            real_sum = 0.0
            imag_sum = 0.0
            for j in neighbors[i]:
                real_sum += math.cos(phase[j])
                imag_sum += math.sin(phase[j])
            real_avg = real_sum / len(neighbors[i])
            imag_avg = imag_sum / len(neighbors[i])
            local_coherence[i] = math.sqrt(real_avg**2 + imag_avg**2)

        # 3) Global coherence
        global_coherence = sum(local_coherence) / num_nodes
        state.global_coherence = global_coherence

        # 4) Determine propagation gain
        if global_coherence < C_min:
            G = gamma_low
        else:
            G = gamma_high

        # 5) Phase update with noise
        for i in range(num_nodes):
            noise_i = random.gauss(0.0, noise_std)
            phase[i] = wrap_angle(
                phase[i] + G * params.alpha * delta[i] + noise_i
            )

        return state

This is the minimal v1.0 engine:

- Δ-signal,
- local coherence,
- global gating,
- non-movement phase update.

---

## 6. Simulation Loop (v1.0)

Minimal simulation runner:

    def run_simulation(state, params, num_steps):
        history = {
            "phase": [],
            "global_coherence": [],
        }

        for t in range(num_steps):
            # Record snapshot
            history["phase"].append(list(state.phase))
            history["global_coherence"].append(state.global_coherence)

            # Single-step update
            state = step(state, params)

        return history

This is enough for:

- resonance chain experiment
- noise-under-phase test
- local coherence map evolution
- phase update vs coherence visualization

---

## 7. File / Module Layout (Proposal)

In `rcircuit-phase-engine`:

    /src
      rcircuit_core_v1_0.py          # State, init, step()
      rcircuit_metrics.py            # Coherence, diagnostics
      rcircuit_experiments_v1_0.py   # Simple experiments
      rcircuit_viz.py                # (optional) plot phase/coherence over time

Suggested:

- `rcircuit_core_v1_0.py`
  - `init_graph(num_nodes, topology="ring"|"grid"|"random")`
  - `step(state, params)`
  - `run_simulation(...)`

- `rcircuit_metrics.py`
  - `compute_local_coherence(...)`
  - `compute_global_coherence(...)`

- `rcircuit_experiments_v1_0.py`
  - `experiment_resonance_chain()`
  - `experiment_noise_under_phase()`

---

## 8. Experiments to Include in v1.0

### 8.1 Resonance Chain

- Topology: ring (each node connected to 2 neighbors).
- Initial condition: random phases.
- Run 100–1000 steps.

Measure / plot:

- `C_global(t)`
- phase distribution at t = 0, mid, final.

Goal: show self-organization into coherent bands.

### 8.2 Noise-Under-Phase

- Same ring topology.
- Vary `noise_std` in {0.0, 0.05, 0.1, 0.2}.
- Measure steady-state global coherence vs noise level.

Goal: show phase robustness under noise and breakdown threshold.

---

## 9. Interpretation (What v1.0 Proves)

v1.0 is not a full compute system.  
It shows that:

1. Phase-only state evolution (no bulk value movement) is a coherent compute primitive.  
2. Δ-signal propagation can be defined purely from neighbor interactions.  
3. Local & global coherence provide a natural gating mechanism for phase updates.  
4. Noise interacts with phase in a structured way, not as pure destruction.

This is enough to justify deeper work on:

- Phase OS  
- Phase registers  
- RCIRCUIT → hardware mapping  
- Post-FLOPS architecture exploration.

---

## 10. Status

- v1.0 spec: this document.  
- Implementation: to be provided in `/src` as a minimal but runnable prototype.  
- Target audience: the ~3k people worldwide who understand why “phase > value” is not a slogan, but an architecture boundary.
