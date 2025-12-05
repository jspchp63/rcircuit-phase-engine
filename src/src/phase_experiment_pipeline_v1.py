# src/phase_experiment_pipeline_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal full experiment pipeline (standalone / safe)

import random
import math

class PipelineNode:
    """Node with phase + minimal Δsignal logic."""
    def __init__(self, phase=0.0):
        self.phase = phase

    def compute_delta(self, neighbors):
        """Δsignal based on mean neighbor phase."""
        if not neighbors:
            return 0.01
        mean_p = sum(n.phase for n in neighbors) / len(neighbors)
        return 0.1 * (mean_p - self.phase)

    def update(self, delta):
        two_pi = 6.283185307179586
        self.phase = (self.phase + delta) % two_pi


class PipelineNetwork:
    """Simple adjacency-list network."""
    def __init__(self, num_nodes):
        self.nodes = [PipelineNode(phase=0.1 * i) for i in range(num_nodes)]
        self.edges = {i: [] for i in range(num_nodes)}

    def connect(self, a, b):
        self.edges[a].append(b)
        self.edges[b].append(a)

    def neighbors_of(self, idx):
        return [self.nodes[i] for i in self.edges[idx]]


def run_pipeline(num_nodes=5, steps=20):
    """Full pipeline: Δsignal → propagation → phase update."""
    net = PipelineNetwork(num_nodes)

    # simple linear chain
    for i in range(num_nodes - 1):
        net.connect(i, i + 1)

    for _ in range(steps):
        deltas = []
        for idx, node in enumerate(net.nodes):
            neighbors = net.neighbors_of(idx)
            d = node.compute_delta(neighbors)
            deltas.append(d)

        for node, d in zip(net.nodes, deltas):
            node.update(d)

    return [node.phase for node in net.nodes]


if __name__ == "__main__":
    print("Pipeline result:", run_pipeline())
