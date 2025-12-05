# src/phase_harmonization_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal harmonization (alignment) mechanism — standalone & safe

def harmonize_phase(node, target_phase, strength=0.05):
    """
    Pull the node's phase slightly toward a target phase.
    This models a basic 'alignment force' in phase computation.
    """
    delta = strength * (target_phase - node.phase)
    two_pi = 6.283185307179586
    node.phase = (node.phase + delta) % two_pi
    return node.phase


def harmonize_group(nodes, strength=0.05):
    """
    Move all nodes slightly toward the group mean phase.
    This is a simplified 'global harmonization' step.
    """
    if not nodes:
        return []

    mean_phase = sum(n.phase for n in nodes) / len(nodes)
    two_pi = 6.283185307179586

    new_phases = []
    for n in nodes:
        delta = strength * (mean_phase - n.phase)
        n.phase = (n.phase + delta) % two_pi
        new_phases.append(n.phase)

    return new_phases


# internal safe test
if __name__ == "__main__":
    class _N:
        def __init__(self, p): self.phase = p

    nodes = [_N(0.1), _N(0.5), _N(1.2)]
    print("Before:", [n.phase for n in nodes])
    harmonize_group(nodes, strength=0.1)
    print("After :", [n.phase for n in nodes])
