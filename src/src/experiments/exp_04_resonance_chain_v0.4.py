# RCIRCUIT Experiment 04 — Multi-Node Resonance Chain (v0.4)

# 목적:
# 단일 Δsignal이 여러 노드를 연쇄적으로 통과할 때
# 위상(phase)이 어떻게 누적·감쇠·공명하는지 관찰하는 실험.

import math
import random

class PhaseNode:
    def __init__(self, phase=0.0):
        self.phase = phase

    def update(self, delta_signal, modulation=0.1, damping=0.98):
        """
        기본 규칙:
        phase_new = (phase_old + Δsignal * modulation) * damping
        damping은 에너지 손실을 모델링.
        """
        self.phase = (self.phase + delta_signal * modulation) * damping
        return self.phase


def run_resonance_chain(num_nodes=5, steps=10, base_delta=0.1):
    """
    5개 노드가 1→2→3→4→5 순서로 Δsignal을 전달받는 구조.
    각 노드는 전달 과정에서 phase를 약간 변형해 다음 노드로 전달.
    """
    nodes = [PhaseNode(phase=random.uniform(-0.2, 0.2)) for _ in range(num_nodes)]

    print("Initial phases:")
    for i, node in enumerate(nodes):
        print(f" Node {i}: {node.phase:.4f}")
    print("\nRunning chain…\n")

    delta = base_delta

    for step in range(steps):
        print(f"[Step {step+1}] Δsignal_in = {delta:.4f}")
        for i, node in enumerate(nodes):
            new_phase = node.update(delta)
            print(f" Node {i} → phase={new_phase:.4f}")
            # Δsignal 변형: sign 유지, magnitude만 축소/확대
            delta = new_phase * 0.05
        print()

    return nodes


if __name__ == "__main__":
    final_nodes = run_resonance_chain()
    print("Final phases:")
    for i, node in enumerate(final_nodes):
        print(f" Node {i}: {node.phase:.4f}")
