# src/phase_coupling_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal coupling function (safe, no external dependencies)

def phase_coupling_strength(node_a, node_b, k=0.1):
    """
    Compute basic phase coupling strength between two nodes.
    Higher difference → higher coupling force.
    """
    return k * (node_b.phase - node_a.phase)


def apply_coupling(node, neighbors):
    """
    Apply coupling influence from all neighbors.
    Δ = sum( coupling_strength(neighbor → node) )
    """

    if not neighbors:
        return 0.0  # no coupling influence

    delta = 0.0
    for nb in neighbors:
        delta += phase_coupling_strength(node, nb)
    return delta


# Internal safe test
if __name__ == "__main__":
    class _N:
        def __init__(self, p): self.phase = p

    a = _N(0.10)
    b = _N(0.25)
    c = _N(0.05)

    print("Coupling influence:", apply_coupling(a, [b, c]))
