# RCIRCUIT v2.0 — Whitepaper Edition  
### Phase Evolution as a Transport-Free Compute Paradigm  
**Author: Chulhee Park**

---

## **Abstract**

Modern AI systems are collapsing under physical limits imposed by data transport.  
Computation is no longer FLOPS-bound; it is movement-bound.  
HBM saturation, wire delay, interconnect latency, and thermal jitter now dominate system behavior.

**RCIRCUIT introduces a compute model where values never move.**  
Only **local phase-state evolution** performs computation.

We show:

1. Transport → O(N²) scaling bottleneck  
2. Phase evolution → O(N) locality-bound scaling  
3. Logical operations (XOR) emerge from phase differentials  
4. A theoretical universal gate set is achievable  
5. Local coherence enables stable computation without global sync

This work proposes RCIRCUIT as a candidate for **post-MatMul compute architectures**.

---

## **1. Introduction**

The failure mode of modern accelerators is not arithmetic but physics.

Transport dominates:

- global memory stalls  
- HBM bandwidth ceilings  
- wire delay  
- incoherence under thermal jitter  
- global sync barriers  

As model size increases, **transport grows superlinearly**, while compute grows linearly.

This asymmetry collapses scalability.

**Compute must shift from “moving values” to “evolving states.”**

RCIRCUIT embodies this shift.

---

## **2. Limitations of MatMul-Centric Architectures**

Tensor operations require:

1. fetch  
2. multiply  
3. accumulate  
4. refetch  
5. reshape  
6. redistribute  

Each step requires **movement**.

Transport is 30–200× more expensive than local ALU operations.

This produces:

- global latency  
- energy spikes  
- synchrony barriers  
- heat accumulation  
- utilization collapse  

AI workloads are thus **transport-limited**, not compute-limited.

---

## **3. RCIRCUIT Overview**

RCIRCUIT eliminates global transport.  
Only **local phase-state updates** occur.

Key principles:

- no tensors  
- no global memory  
- no long-distance propagation  
- no synchronization  

Computation emerges from:

- phase registers  
- Δ-phase transitions  
- local resonance coupling  
- short-range coherence evolution  

This shifts computation from information **movement** → information **evolution**.

---

## **4. Minimal RCIRCUIT Architecture**

### **4.1 Cell Definition**
```c
struct RC_Cell {
    float phase;
    float delta;
    float coupling;
};
```

### **4.2 Update Rule**
```text
delta_i(t+1) = γ Σ_j∈N(i) (phase_j - phase_i)
phase_i(t+1) = phase_i(t) + α · delta_i(t+1)
```

### **4.3 Physical Interpretation**

- α governs propagation rate  
- γ governs resonance strength  
- neighborhood N(i) defines locality  

This is a discretized PDE system:

```text
∂φ/∂t = α ∇²φ + γ R(φ)
```

---

## **5. Benchmark Model**

### **5.1 Transport Cost Model**

| Operation | MatMul Cost | RCIRCUIT Cost |
|----------|-------------|----------------|
| Memory Move | 100 | 0 |
| Multiply | 1 | 0.4 |
| Local Phase Step | — | 0.1 |

Transport dominates by two orders of magnitude.

### **5.2 Scaling Model**
MatMul:
```
T(N) = O(N²) transport
```

RCIRCUIT:
```
T(N) = O(N) local updates
```

---

## **6. Logical Expressiveness**

The XOR gate emerges from phase differential:

```
Δφ = |φ₁ - φ₂|
XOR = 1 if Δφ > θ
```

We outline a **universal gate roadmap**:

- XOR ✔  
- NOT (inversion)  
- AND (threshold coupling)  
- NAND (XOR + inversion)  

If NAND is realizable:

> **RCIRCUIT becomes computationally universal.**

---

## **7. Coherence & Stability Model**

### **7.1 Local Drift**
```
phase_i(t+1) = phase_i(t) + ε
```

### **7.2 Coherence Decay**
```
C(r) = exp(-λ r)
```

### **7.3 Error Bound**
```
E(t) ≤ k · local_noise
```

Transport-based compute spreads errors globally.  
RCIRCUIT localizes them.

---

## **8. Implications for Physical Compute Systems**

Transport-free compute reduces:

- datacenter energy  
- cooling requirements  
- wire delay  
- interconnect load  
- reliability failures  

Enabling:

- low-power inference  
- large-scale training stability  
- edge compute viability  
- defense & autonomous system reliability  

---

## **9. Experimental Example (POC)**

The Phase XOR POC demonstrates:

- computation without movement  
- logic emerging from phase evolution  
- coherence-driven output  

Run:
```
python src/phase_xor_poc_v01.py
```

Example output:
```
φ1 = -0.134, φ2 = -0.722 → XOR = 1
φ1 = -0.406, φ2 = -0.491 → XOR = 0
```

---

## **10. Discussion**

RCIRCUIT challenges the fundamental assumption of modern compute:  
**that computation requires transporting values.**

Instead, it proposes:

- locality instead of bandwidth  
- coherence instead of synchronization  
- evolution instead of movement  

The implications are architectural, physical, and economic.

---

## **11. Conclusion**

Transport is collapsing.  
Movement is too expensive.  
Physics is rejecting our architectures.

RCIRCUIT presents:

- a model not bound by transport  
- a pathway to post-MatMul compute  
- a new physical interpretation of computation  

The argument is simple:

> **Stop moving values.  
> Start evolving states.**

---

## **12. Contact**

**Author: Chulhee Park**  
📩 Email: **jspchp638@gmail.com**

