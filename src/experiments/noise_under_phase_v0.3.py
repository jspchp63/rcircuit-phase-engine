# RCIRCUIT — Experiment 03
# Noise-Under-Phase Stability Test v0.3
# Goal:
#   Observe how injected noise interacts with phase propagation,
#   and whether local coherence still forms.

import random
import math

class Node:
    def __init__(self, phase):
        self.phase = phase

    def update(self, neighbor_phase, noise_level=0.02, coupling=0.05):
        """
        Phase update rule with noise:
        phase_new = phase_old
                   + (neighbor - self) * coupling
                   + noise
        """
        noise = random.uniform(-noise_level, noise_level)
        delta = (neighbor_phase - self.phase) * coupling
        self.phase += delta + noise
        return self.phase

# ---- simulation ----

def simulate_noise_under_phase(steps=30):
    A = Node(phase=random.uniform(0.0, 1.0))
    B = Node(phase=random.uniform(0.0, 1.0))

    log = []
    for t in range(steps):
        A.update(B.phase)
        B.update(A.phase)
        log.append((t, round(A.phase, 4), round(B.phase, 4)))

    return log

if __name__ == "__main__":
    out = simulate_noise_under_phase()
    for t, a, b in out:
        print(f"t={t} | A={a} | B={b}")
