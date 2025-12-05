# src/phase_state_snapshot_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal state snapshot utility (safe and standalone)

def snapshot_phases(nodes):
    """
    Return a simple list of current phases.
    Useful for logging, experiments, or debugging.
    """
    return [n.phase for n in nodes]


def snapshot_network(network):
    """
    Return phase list from network object (PhaseNetworkV1).
    """
    return [node.phase for node in network.nodes]


# internal safe test
if __name__ == "__main__":
    class _Node:
        def __init__(self, p): self.phase = p

    nodes = [_Node(0.1), _Node(0.2), _Node(0.3)]
    print("Snapshot:", snapshot_phases(nodes))
