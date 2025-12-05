# src/coherence_metric_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal coherence metric (independent, safe)

def compute_local_coherence(nodes):
    """
    Compute simple coherence = 1 / (1 + variance of phases)
    Independent function — no external dependencies.
    """
    phases = [n.phase for n in nodes]
    mean_p = sum(phases) / len(phases)
    variance = sum((p - mean_p)**2 for p in phases) / len(phases)
    return 1.0 / (1.0 + variance)


if __name__ == "__main__":
    # Minimal self-test (safe)
    class _Node: 
        def __init__(self, p): self.phase = p

    test_nodes = [_Node(0.1), _Node(0.12), _Node(0.11)]
    print("Coherence:", compute_local_coherence(test_nodes))
