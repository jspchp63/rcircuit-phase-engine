# src/experiment_autorun_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal automated experiment runner (standalone & safe)

import random

class AutoNode:
    """Node with minimal Δsignal logic for automated tests."""
    def __init__(self, phase=0.0):
        self.phase = phase

    def step(self):
        """Simple Δsignal update."""
        delta = 0.01
        two_pi = 6.283185307179586
        self.phase = (self.phase + delta) % two_pi


def auto_run_experiment(
    num_nodes=5,
    steps=20,
    trials=5
):
    """
    Run the same experiment multiple times.
    No dependencies — safe prototype version.
    Returns list of results for each trial.
    """
    all_results = []

    for _ in range(trials):
        nodes = [AutoNode(phase=0.1 * i) for i in range(num_nodes)]

        for _ in range(steps):
            for n in nodes:
                n.step()

        all_results.append([n.phase for n in nodes])

    return all_results


if __name__ == "__main__":
    results = auto_run_experiment(num_nodes=5, steps=20, trials=3)
    print("Auto-run results:", results)
