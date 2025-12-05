# src/phase_analysis_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal analysis utilities (safe, standalone)

import math

def phase_variance(nodes):
    """Return simple variance of phases."""
    phases = [n.phase for n in nodes]
    mean_p = sum(phases) / len(phases)
    return sum((p - mean_p) ** 2 for p in phases) / len(phases)


def phase_spread(nodes):
    """Return max-min spread of phases."""
    phases = [n.phase for n in nodes]
    return max(phases) - min(phases)


def phase_stability(nodes):
    """
    Stability = 1 / (1 + spread)
    Quick proxy for how 'tight' the phase cluster is.
    """
    spread = phase_spread(nodes)
    return 1.0 / (1.0 + spread)


# internal safe test
if __name__ == "__main__":
    class _N:
        def __init__(self, p):
            self.phase = p

    test_nodes = [_N(0.1), _N(0.12), _N(0.15)]
    
    print("Variance:", phase_variance(test_nodes))
    print("Spread  :", phase_spread(test_nodes))
    print("Stability:", phase_stability(test_nodes))
