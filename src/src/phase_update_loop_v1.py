# src/phase_update_loop_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal standalone phase update loop (safe, dependency-free)

class SimplePhaseNode:
    """Standalone node (safe version) with internal Δsignal rule."""
    def __init__(self, phase=0.0):
        self.phase = phase

    def compute_delta(self):
        """Minimal Δsignal placeholder."""
        return 0.01

    def update_phase(self, delta):
        """Apply Δsignal with 2π wrap."""
        two_pi = 6.283185307179586
        self.phase = (self.phase + delta) % two_pi


def run_phase_updates(nodes, steps=10):
    """
    Minimal multi-step phase update loop.
    Independent from other modules.
    """
    for _ in range(steps):
        deltas = [n.compute_delta() for n in nodes]
        for node, d in zip(nodes, deltas):
            node.update_phase(d)
    return nodes


if __name__ == "__main__":
    # Minimal internal test
    nodes = [SimplePhaseNode(0.1 * i) for i in range(5)]
    updated = run_phase_updates(nodes, steps=20)
    print([n.phase for n in updated])
