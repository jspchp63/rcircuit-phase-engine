# RCIRCUIT Stability Map (v0.4 Skeleton)

This document outlines the conceptual structure of the RCIRCUIT Stability Map.

The Stability Map describes:
1. Local Phase Consistency
2. ΔSignal Convergence Windows
3. Resonance Stability Thresholds
4. Noise-Isolation Boundaries
5. Global Synchronization Safety Limits

## 1. Local Phase Consistency (LPC)
- Measures how stable a node’s phase is before propagation.
- Key metric: phase_variance_local

## 2. ΔSignal Convergence Window (ΔSCW)
- Defines safe ranges of Δsignal magnitude.
- Prevents runaway amplification.

## 3. Resonance Stability Threshold (RST)
- Minimum coherence needed for propagation.
- RST <-> overall system stability function.

## 4. Noise Isolation Boundary (NIB)
- Separates meaningful Δsignal from noise.
- Future: NIB automatic tuning.

## 5. Global Synchronization Limit (GSL)
- System-level constraint.
- Prevents catastrophic dephasing events.

---
More details will be added in v0.5 when experiments mature.
This is a public-safe skeletal model.
