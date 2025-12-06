# RCIRCUIT — Phase Computing Engine
### Post-MatMul / Post-FLOPS Compute Primitive

RCIRCUIT is not an accelerator.  
RCIRCUIT is a new compute primitive.

Modern AI collapses at interconnect physics.  
MatMul dies because transport dies.

RCIRCUIT computes by **phase-state evolution**, not tensor movement.

---

## 1. Why This Exists
AI scale = MatMul → FLOPS → bandwidth → heat → jitter → collapse.  
Transport, not compute, is the real bottleneck.  
HBM burns. GPUs idle. NVLink saturates. TPU stalls.

---

## 2. Compute Primitive Shift
MatMul = value transport.  
RCIRCUIT = phase propagation.

Value moves → expensive.  
Phase evolves → cheap.

---

## 3. Core Principle
No tensors.  
No global sync.  
No long-distance propagation.

Only:
- phase registers  
- Δ-signal transitions  
- local resonance coupling  
- coherence evolution  

---

## 4. Minimal Architecture (Public)
docs/
- Phase_Compute_Architecture.md  
- v1.0_integration_skeleton.md  
- Phase_OS_Scheduler_v0.4.md  

src/
- phase_engine_core_v1.py  
- phase_node.py  
- phase_coupling.py  
- phase_propagation_kernel.py  
- resonance_score.py  
- coherence_metric.py  
- phase_state_snapshot.py  

---

## 5. RCIRCUIT Cell
struct RC_Cell {
float phase;
float delta;
float coupling;
};



Local update rule:
phase ← phase + f(delta, neighbors)
delta ← g(phase_diff)



---

## 6. XOR Demo (Phase)
φ1, φ2 → Δφ → resonance gate → output  
No values transported.

---

## 7. Why GPUs/TPUs/Cerebras Fail to Scale
Scaling MatMul = scaling transport.  
Transport scaling = dead.  
Phase scaling = local.

---

## 8. AI Impact
- Token latency ↓  
- Transport cost → ~0  
- Energy/op ↓ 30–100×  
- Thermal noise localized  
- Enters linear scaling regime  

---

## 9. Repository
GitHub: https://github.com/jspchp63/rcircuit-phase-engine  
YouTube: @2EmotionCompute  

---

## 10. Contact
**Chulhee Park**  
Email: jspchp638@gmail.com
