# ⚡ RCIRCUIT — Phase Computing Engine (Minimal Public Release)
**Post-FLOPS Compute Architecture Based on Phase Propagation**  
**“If MatMul Is the Limit, GPU Is the End.”**

---

## **1. Executive Summary**
AI scaling is no longer constrained by compute; it is constrained by **interconnect physics**:  
**Heat, Power, Distance, Timing Jitter.**  
GPUs move values.  
**RCIRCUIT moves phase.**

This repository provides the minimal public-safe version of a compute model that uses  
**Δ-signal propagation + coherence evolution**, instead of tensor transport.

---

## **2. Start Here (VC / DeepTech Engineers)**
Review this architecture using the 3-key files:

```
/docs/Phase_Compute_Architecture.md
/src/phase_engine_core_v1.py
/docs/v1.0_integration_skeleton.md
```

These explain why **Phase > FLOPS**.

---

## **3. Why MatMul Dies (Physics Argument)**  
Dense MatMul = FLOPS expansion = **data movement expansion**.  
This fails because the physical walls fail first:

- Heat saturation  
- Power density wall  
- Propagation delay  
- Timing jitter collapse  
- HBM bandwidth exhaustion  

AI is no longer compute-bound.  
**AI is interconnect-bound.**

---

## **4. Why Phase > FLOPS**
Value-transport compute wastes most energy on moving tensors.  
Phase compute does not.

RCIRCUIT replaces tensor movement with:

- **Δ-signal transitions**  
- **Local coherence formation**  
- **Phase alignment dynamics**  
- **Zero bulk data movement**

📌 No FLOPS scaling  
📌 Only **phase-state evolution**

---

## **5. Minimal Example (Pseudo-Python)**

```python
from rcircuit import PhaseEngine

engine = PhaseEngine(size=128)
engine.inject_signal(node=7, delta=0.12)

for _ in range(10):
    engine.step()
    engine.measure()
```

---

## **6. Minimal Public Architecture (v0.3–v0.4)**

**Layer 0 — Physical Limits**  
Propagation delay • thermal ceiling • jitter instability  

**Layer 1 — RCIRCUIT Core**  
Phase register • Δ-signal engine • local propagation loop  

**Layer 2 — Phase Compute Layer**  
Coherence map • resonance score • noise isolation  

⚠ Full architecture released after safety/IP verification.

---

## **7. Repository Structure**
```
/docs
  Architecture_Guide_v1.md
  Interconnect_Crisis_Brief.md
  Phase_Compute_Architecture.md
  Phase_OS_Scheduler_v0.4_pseudocode.md
  Phase_Stability_Map_v0.3.md
  v1.0_integration_skeleton.md
  v1.2_resonance_score_function.md
  v1.4_local_coherence_map.md
  v1.9_resonant_compute_pulse.md

/src
  phase_engine_core_v1.py
  phase_compute_api_v1.py
  phase_propagation_kernel_v1.py
  phase_coupling_v1.py
  phase_harmonization_v1.py
  resonance_score_v1.py
  noise_model_v1.py
  experiment_runner_v1.py
  placeholder.md

/experiments
  (public-safe experiment scripts)
```

---

## **8. Intended Audience**
- GPU / TPU / HPC engineers  
- Interconnect & compute-physics researchers  
- AI infra VCs (post-FLOPS narrative)  
- DeepTech founders exploring new compute primitives

---

## **9. Research Status**
This repo includes:

- Conceptual architecture  
- Δ-signal propagation experiments  
- Coherence / resonance metrics  
- Early simulation tools  
- Minimal phase-engine prototype  

RCIRCUIT = **research proposal**, not hardware.

---

## **10. Limitations**
- Not fabrication-ready  
- No silicon feasibility claims  
- No performance model  
- Abstractions subject to revision  
- Requires partner & IP validation

---

## **11. System Context**
RCIRCUIT is the compute engine of:

**HROS — Human Resonance Operating System**

Active development continues at:  
👉 https://github.com/jspchp63/rcircuit-phase-engine

---

## **12. Roadmap**
- v0.3 — Phase OS Scheduler  
- v0.5 — Coherence Kernel  
- v0.7 — Phase Simulation Layer  
- v1.0 — Integration Prototype  
- v1.2 — Interconnect Physics Appendix  

---

## **13. Contact**
For collaboration or technical review:  
📧 **jspchp638@gmail.com**


