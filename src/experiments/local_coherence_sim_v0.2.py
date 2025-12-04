# RCIRCUIT — Experiment 02
# Local Coherence Simulation v0.2
# Goal: observe how neighboring phases converge or diverge under Δsignal coupling.

import random
import math

class Node:
    def __init__(self, phase):
        self.phase = phase

    def update(self, neighbor_phase, coupling=0.05):
        """
        phase_new = phase_old + (neighbor - self) * coupling
        (minimal local coherence rule)
        """
        delta = (neighbor_phase - self.phase) * coupling
        self.phase += delta
        return self.phase

# ---- simulation ----

def simulate_local_coherence(steps=20):
    A = Node(phase=random.uniform(0.0, 1.0))
    B = Node(phase=random.uniform(0.0, 1.0))

    log = []
    for t in range(steps):
        A.update(B.phase)
        B.update(A.phase)
        log.append((t, round(A.phase, 4), round(B.phase, 4)))

    return log

if __name__ == "__main__":
    out = simulate_local_coherence()
    for step in out:
        print(f"t={step[0]} | A={step[1]} | B={step[2]}")
