# src/phase_compute_api_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Unified API layer for interacting with phase engine components

from phase_engine_core_v1 import PhaseEngineCore
from phase_node_v1 import PhaseNode
from coherence_metric_v1 import compute_local_coherence
from phase_visualizer_v1 import visualize_phase_states

class PhaseComputeAPI:
    """
    Unified API for initializing, running, and evaluating
    RCIRCUIT phase computations.
    """

    def __init__(self, num_nodes=5):
        self.nodes = [PhaseNode(initial_phase=0.0) for _ in range(num_nodes)]
        self.engine = PhaseEngineCore()

    def step(self):
        """Perform one propagation step across nodes."""
        self.nodes = self.engine.propagate(self.nodes)

    def run(self, steps=10):
        """Run multiple update cycles."""
        for _ in range(steps):
            self.step()

    def measure_coherence(self):
        """Return coherence score across nodes."""
        return compute_local_coherence(self.nodes)

    def visualize(self, title="Phase State"):
        """Show text-based visualization."""
        phases = [n.phase for n in self.nodes]
        visualize_phase_states(phases, title)


if __name__ == "__main__":
    api = PhaseComputeAPI(num_nodes=5)
    api.run(steps=20)
    print("Coherence:", api.measure_coherence())
    api.visualize("Final Phase Distribution")
