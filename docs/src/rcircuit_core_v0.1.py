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
        return self.phase

def propagate(nodes, delta_signal):
    """
    Minimal local propagation:
    each node updates independently.
    No global sync.
    """
    return [node.update(delta_signal) for node in nodes]

if __name__ == "__main__":
    nodes = [PhaseNode(0.0), PhaseNode(1.2), PhaseNode(-0.5)]
    result = propagate(nodes, delta_signal=0.3)
    print("Updated phases:", result)
