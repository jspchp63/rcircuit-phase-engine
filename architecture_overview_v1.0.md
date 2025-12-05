# RCIRCUIT Architecture Overview (v0.1)

This document provides a clean, minimal, public-safe explanation of the RCIRCUIT architecture:  
how Δsignal, phase propagation, and coherence form a new compute pathway beyond FLOPS.

---

## 1. Why RCIRCUIT Exists  
GPUs hit four physical limits: heat, power density, distance, and timing jitter.  
The bottleneck is no longer compute — it is interconnect.

RCIRCUIT replaces **value movement** with **phase propagation**:
- Move phase, not data  
- Propagate Δsignal, not full state  
- Achieve local coherence before global sync  

---

## 2. Minimal Architecture Stack (Public Extract)

**Layer 0 — Physical Limits**  
Defines constraints: thermal saturation, energy wall, propagation delay, jitter.

**Layer 1 — RCIRCUIT Core**  
- Phase register  
- Δsignal engine  
- Local propagation model  

**Layer 2 — Phase Compute Layer**  
- Coherence map  
- Stability metric  
- Noise isolation  

---

## 3. Current Public Status  
This file represents a stable, safe, minimal public snapshot.  
The full internal system remains under safety and IP review.

Phase is the architecture.  
Physics is the bottleneck.
Fix double extension: mdmd → md
