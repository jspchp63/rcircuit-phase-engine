# src/delta_signal_engine_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal Δsignal engine (safe, no external dependencies)

def compute_delta_signal(node, neighbors=None):
    """
    Simple Δsignal rule for v1.0 prototype.
    - If neighbors exist: Δ = k * (mean_neighbor_phase - node.phase)
    - If no neighbors: Δ = constant minimal delta
    """

    # No neighbors → minimal constant delta
    if not neighbors:
        return 0.01

    neighbor_phase = sum(n.phase for n in neighbors) / len(neighbors)
    gain = 0.1  # Prototype gain coefficient (safe placeholder)

    return gain * (neighbor_phase - node.phase)


# Internal test (safe)
if __name__ == "__main__":
    class _Node:
        def __init__(self, p):
            self.phase = p

    a = _Node(0.10)
    b = _Node(0.20)
    c = _Node(0.15)

    print("Δsignal:", compute_delta_signal(a, [b, c]))
