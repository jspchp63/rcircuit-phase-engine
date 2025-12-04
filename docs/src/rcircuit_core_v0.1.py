# RCIRCUIT Core Engine v0.1 (Minimal Public Release)
# This file provides the simplest possible Δsignal → phase update loop.

import math

class PhaseNode:
    def __init__(self, phase=0.0):
        self.phase = phase

    def update(self, delta_signal):
        """
        Core rule:
        phase_new = phase_old + Δsignal * modulation
        """
        modulation = 0.1
        self.phase += delta_signal * modulation

    def coherence(self, other_phase):
        """
        Simple coherence metric:
        returns how close two phases are (1.0 = perfect sync)
        """
        return 1.0 - abs(self.phase - other_phase)

# Demo function (optional)
def run_demo():
    node = PhaseNode(phase=0.5)
    inputs = [0.1, -0.05, 0.2, -0.1]

    print("Initial phase:", node.phase)
    for d in inputs:
        node.update(d)
        print(f"Δsignal={d: .3f} → phase={node.phase: .3f}")

if __name__ == "__main__":
    run_demo()
