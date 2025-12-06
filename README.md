# RCIRCUIT — Phase Computing Engine
### A Post-MatMul / Post-FLOPS Compute Primitive

RCIRCUIT is not an accelerator.
RCIRCUIT is a new compute primitive.

Modern AI collapses at interconnect physics.
MatMul dies because transport dies.

RCIRCUIT computes by phase-state evolution, not tensor movement.
This removes the transport bottleneck and enables local-scaling compute.

---

# 1. Why This Exists — Transport Collapse Physics

MatMul scaling hits a hard wall due to transport, not arithmetic.

- HBM bandwidth saturates before FLOPS do.
- Interconnect latency (NVLink / PCIe / NoC) dominates execution time.
- Wire delay grows superlinearly with array size.
- Thermal jitter corrupts long-distance signal coherence.
- GPUs/TPUs stall waiting for data, not compute.

**AI scale = MatMul → FLOPS → bandwidth → heat → jitter → collapse.**

RCIRCUIT eliminates global data movement
and replaces it with purely local phase evolution.

---

# 2. Compute Primitive Shift

### MatMul = value transport
Data must move → energy cost ↑, wire delay ↑, synchronization ↑.

### RCIRCUIT = phase propagation
No values move.
Only state updates propagate through local coupling.

| Property       | MatMul           | RCIRCUIT          |
|----------------|------------------|--------------------|
| Compute unit   | tensor multiply  | phase evolution    |
| Data movement  | global           | local              |
| Scaling limit  | bandwidth        | locality           |
| Sync           | global           | none               |
| Heat           | accumulated      | localized          |
| Complexity     | O(N²) transport  | O(N) local updates |

**Value moves → expensive.  
Phase evolves → cheap.**

---

# 3. Core Principle

RCIRCUIT eliminates the three killers of modern AI scaling:

- No tensors  
- No global sync  
- No long-distance propagation  

Only four primitives exist:

- phase registers  
- Δ–signal transitions  
- local resonance coupling  
- coherence evolution  

This transforms compute into a purely local physical process.

---

# 4. Formal Minimal Architecture

## 4.1 RCIRCUIT Cell
struct RC_Cell {
float phase;
float delta;
float coupling;
};



## 4.2 Update Rule (Semi-Formal)

Let `phase_i` be the state of cell i  
and `N(i)` its neighbors under fixed locality radius r.

delta_i(t+1) = γ · Σ_j∈N(i) (phase_j(t) - phase_i(t))
phase_i(t+1) = phase_i(t) + α·delta_i(t+1)



- α = phase propagation coefficient  
- γ = local resonance strength  

This discrete rule approximates a phase-field PDE:

∂φ/∂t = α·∇²φ + γ·R(φ)


---

# 5. Directory Structure (Public)

rcircuit-phase-engine/
docs/
Phase_Compute_Architecture.md
v1.0_integration_skeleton.md
Phase_OS_Scheduler_v0.4.md

src/
phase_engine_core_v1.py
phase_node.py
phase_coupling.py
phase_propagation_kernel.py
resonance_score.py
coherence_metric.py
phase_state_snapshot.py


---

# 6. XOR Demo (Phase Logic)

Input states: φ1, φ2  
Compute Δφ  
Pass through resonance-gate  
Output: phase-aligned / misaligned state → logical XOR

No values transported.
Only phase differences.

---

# 7. Why GPUs, TPUs, Cerebras Fail to Scale Further

## 7.1 Global Transport = Hard Stop
All modern accelerators share a fatal constraint:

**Compute is cheap. Moving data is not.**

- GPU → SM stalls due to global memory dependency  
- TPU → systolic arrays choke on boundary conditions  
- Cerebras → wafer-scale fabric saturates  
- Groq → deterministic pipeline still depends on streaming bandwidth  

## 7.2 RCIRCUIT Avoids This Entire Category

Because:

- updates are local  
- no global barrier  
- constant fan-out radius  
- coherence maintained without large-scale wiring  

**RCIRCUIT decouples compute from transport.**

---

# 8. AI Impact (DeepTech Claim)

| Metric            | MatMul AI          | RCIRCUIT            |
|-------------------|---------------------|----------------------|
| Token latency      | transport-bound     | phase-local          |
| Energy/op          | high                | 30–100× reduced      |
| Throughput scaling | saturates           | linear               |
| Heat               | global accumulation | localized            |
| Failure mode       | jitter collapse     | local incoherence    |

Eventually this shifts AI from:

**Tensor-transport compute → Phase-evolution compute**

---

# 9. Repository
GitHub: https://github.com/jspchp63/rcircuit-phase-engine  
YouTube: @2EmotionCompute

---

# 10. Contact
**Chulhee Park**  
Email: jspchp638@gmail.com
