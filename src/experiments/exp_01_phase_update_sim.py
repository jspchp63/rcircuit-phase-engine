# exp_01_phase_update_sim.py
# RCIRCUIT Experimental Prototype (v0.1)
# Demonstrates a minimal phase-update primitive using local coherence.

import numpy as np

def phase_update(theta, k=0.05, noise=0.01):
    """
    theta : array of phases (radians)
    k     : coupling strength
    noise : random perturbation simulating physical jitter
    """
    # pairwise phase differences
    diff = theta[:, None] - theta[None, :]
    
    # local coherence term (Kuramoto-like but not identical)
    coupling = np.sum(np.sin(diff), axis=1)
    
    # update rule: base phase + resonance influence + jitter
    return theta + k * coupling + noise * np.random.randn(len(theta))

if __name__ == "__main__":
    # initialize a small field of random phases
    phases = np.random.rand(8) * 2 * np.pi

    print("Initial phases:", phases)

    # iterate 5 steps
    for step in range(5):
        phases = phase_update(phases)
        print(f"Step {step+1}:", phases)
