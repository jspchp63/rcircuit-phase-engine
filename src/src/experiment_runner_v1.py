# src/experiment_runner_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal experiment runner (safe, dependency-free)

class SimpleNode:
    """Minimal node for experiments."""
    def __init__(self, phase=0.0):
        self.phase = phase

    def compute_delta(self):
        return 0.01

    def update_phase(self, delta):
        two_pi = 6.283185307179586
        self.phase = (self.phase + delta) % two_pi


def run_experiment(num_nodes=5, steps=20):
    """
    Run a small phase-update experiment.
    Independent from other modules.
    """
    nodes = [SimpleNode(phase=0.1 * i) for i in range(num_nodes)]

    for _ in range(steps):
        deltas = [n.compute_delta() for n in nodes]
        for node, d in zip(nodes, deltas):
            node.update_phase(d)

    return [n.phase for n in nodes]


if __name__ == "__main__":
    result = run_experiment(num_nodes=5, steps=20)
    print("Final phases:", result)
