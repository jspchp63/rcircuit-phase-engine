# src/phase_engine_core_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal Core Engine — Safe Single-File Version

class PhaseNode:
    """Single compute node with a phase value."""
    def __init__(self, phase=0.0):
        self.phase = phase

    def compute_delta(self):
        """
        Placeholder Δsignal rule.
        Safe minimal version — does not rely on neighbors.
        """
        return 0.01  # constant delta for v1.0 skeleton

    def update_phase(self, delta):
        """
        Update the phase value with wrap-around at 2π.
        """
        two_pi = 6.283185307179586
        self.phase = (self.phase + delta) % two_pi


class PhaseEngine:
    """Minimal phase-update loop for RCIRCUIT prototype."""
    def __init__(self, nodes):
        self.nodes = nodes

    def step(self):
        """Perform one phase-update cycle across all nodes."""
        deltas = [node.compute_delta() for node in self.nodes]
        for node, d in zip(self.nodes, deltas):
            node.update_phase(d)

    def run(self, steps=10):
        """Run multiple update cycles."""
        for _ in range(steps):
            self.step()
        return self.nodes


# Example minimal usage (optional):
if __name__ == "__main__":
    nodes = [PhaseNode(phase=0.1 * i) for i in range(5)]
    engine = PhaseEngine(nodes)
    engine.run(steps=20)
    print([n.phase for n in nodes])
