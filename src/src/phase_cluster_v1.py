# src/phase_cluster_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Multi-engine phase cluster model (early research version)

from phase_compute_api_v1 import PhaseComputeAPI
from phase_config_v1 import PhaseConfig

class PhaseCluster:
    """
    A PhaseCluster consists of multiple PhaseComputeAPI engines.
    It models how independent phase engines influence each other,
    forming the basis for a scalable phase-computing architecture.
    """

    def __init__(self, engine_count=3, nodes_per_engine=5):
        self.engines = [
            PhaseComputeAPI(num_nodes=nodes_per_engine)
            for _ in range(engine_count)
        ]

    def step(self):
        """Run one update step for all engines."""
        for eng in self.engines:
            eng.step()

        self._inter_engine_coupling()

    def run(self, steps=10):
        for _ in range(steps):
            self.step()

    def _inter_engine_coupling(self):
        """
        Basic inter-engine coupling model.
        Each engine slightly adjusts its average phase
        toward the global cluster mean.
        """

        # compute global mean phase
        all_phases = []
        for eng in self.engines:
            for n in eng.nodes:
                all_phases.append(n.phase)

        global_mean = sum(all_phases) / len(all_phases)

        # adjust phases toward cluster mean
        strength = PhaseConfig.COUPLING_STRENGTH * 0.25
        for eng in self.engines:
            for n in eng.nodes:
                n.phase += (global_mean - n.phase) * strength

    def measure_cluster_coherence(self):
        """Return coherence across the entire cluster."""
        all_phases = []
        for eng in self.engines:
            for n in eng.nodes:
                all_phases.append(n.phase)

        if not all_phases:
            return 0.0

        spread = max(all_phases) - min(all_phases)
        return 1.0 / (1.0 + spread)


if __name__ == "__main__":
    cluster = PhaseCluster(engine_count=3, nodes_per_engine=4)
    cluster.run(steps=30)

    print("Cluster Coherence:", cluster.measure_cluster_coherence())
