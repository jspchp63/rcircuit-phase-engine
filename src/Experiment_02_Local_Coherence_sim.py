# experiment_02_local_coherence_sim.py
# RCIRCUIT - Local Coherence Simulation (1D line)
#
# What this shows:
# - N phase nodes in a line
# - Each step, every node updates from its neighbors (local coupling)
# - We measure average |neighbor difference|
#   → this value tends to go down = coherence forming locally

import math
import random

N = 32          # number of phase nodes in a 1D line
STEPS = 50      # number of time steps
ALPHA = 0.2     # phase propagation coefficient
GAMMA = 0.5     # coupling strength


def init_line():
    """Initialize phases randomly between -pi and pi."""
    return [random.uniform(-math.pi, math.pi) for _ in range(N)]


def step(phase):
    """One local update step with nearest-neighbor coupling."""
    new_phase = phase[:]
    for i in range(N):
        left = phase[i - 1] if i > 0 else phase[i]
        right = phase[i + 1] if i < N - 1 else phase[i]
        delta = GAMMA * ((left - phase[i]) + (right - phase[i]))
        new_phase[i] = phase[i] + ALPHA * delta
    return new_phase


def avg_neighbor_diff(phase):
    """Average absolute difference between neighboring phases."""
    diffs = []
    for i in range(N - 1):
        diffs.append(abs(phase[i + 1] - phase[i]))
    return sum(diffs) / len(diffs)


def run():
    phase = init_line()
    print("step,avg_neighbor_diff")
    for t in range(STEPS + 1):
        c = avg_neighbor_diff(phase)
        print(f"{t},{c:.6f}")
        phase = step(phase)


if __name__ == "__main__":
    run()
