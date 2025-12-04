# RCIRCUIT — Phase Computing Research Engine

RCIRCUIT is an experimental phase-based compute model that replaces value movement (FLOPS) with phase propagation and Δsignal coherence.  
This repository provides the minimal public engine, experiments, and architectural briefs for Phase Computing.

---

## 1. What RCIRCUIT Solves
Modern GPUs hit four physical limits:
• Heat (thermal saturation)  
• Power density (the energy wall)  
• Distance (propagation delay)  
• Timing jitter (synchronization instability)

AI is no longer compute-bound.  
AI is **interconnect-bound**.

RCIRCUIT shifts the paradigm:
• Moves **phase**, not raw values  
• Transmits only **Δsignal** (meaningful change)  
• Achieves **local coherence** before global propagation  
• Reduces physical data movement cost  

---

## 2. Minimal Public Architecture (v0.3–v0.4)
Layer 0 — Physical Limits  
Layer 1 — RCIRCUIT Core (phase register · Δsignal engine · local propagation)  
Layer 2 — Phase Compute Layer (coherence map · stability metric · noise isolation)

Full architecture will be released after safety, IP, and partner verification.

---

## 3. Repository Contents
📂 **src/**  
• rcircuit_core_v0.1.py — minimal Δsignal engine  
• rcircuit_core_v0.2_skeleton.py — extended hooks for experiments

📂 **experiments/**  
• v0.2 — resonance scoring demo  
• v0.3 — noise-under-phase experiment  
  (iteration · node_id · phase · delta_signal · resonance_score)

📂 **docs/**  
• Interconnect Crisis Brief  
• Phase Compute OS Notes  
• Architecture Guide v1

---

## 4. Who This Repo Is For
GPU / TPU / HPC engineers  
Compute-physics & interconnect researchers  
DeepTech founders  
Anyone exploring post-FLOPS architectures

If “phase > value” makes instant sense to you,  
you are the target audience.

---

## 5. Contact
Founder: **Chulhee Park**  
Email: **jspchp638@gmail.com**

For collaboration, technical review, or research discussion, feel free to reach out.

---

## 6. Status
This repository is a **public-safe subset** of the ongoing Phase Computing project.  
Full implementation will be released after safety, legal, and partner verification.

Physics is the bottleneck.  
Phase is the next architecture.

---

## 7. System Context
RCIRCUIT is the core engine of the Phase Computing architecture, developed as part of the HROS framework.
📌 Active RCIRCUIT development has moved to → rcircuit-phase-engine/
