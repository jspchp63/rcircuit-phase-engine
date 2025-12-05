# src/resonance_score_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal standalone resonance score function (safe version)

def resonance_score(nodes):
    """
    Resonance metric based on phase coherence.
    Independent function — safe for integration.
    
    Formula (simple prototype):
        resonance = 1 / (1 + variance(phase))  squared
    """

    phases = [n.phase for n in nodes]
    mean_p = sum(phases) / len(phases)

    variance = sum((p - mean_p)**2 for p in phases) / len(phases)
    coherence = 1.0 / (1.0 + variance)

    # Resonance as amplified coherence
    return coherence * coherence


if __name__ == "__main__":
    # Minimal internal self-check
    class _Node:
        def __init__(self, p):
            self.phase = p

    demo = [_Node(0.1), _Node(0.11), _Node(0.13)]
    print("Resonance Score:", resonance_score(demo))
