# src/phase_propagation_kernel_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal propagation kernel (safe and dependency-free)

def propagate_phases(network, delta_rule):
    """
    Apply δ-signals across the whole network.
    delta_rule(node, neighbors) -> Δphase
    """

    deltas = []
    for idx, node in enumerate(network.nodes):
        neighbors = network.neighbors_of(idx)
        d = delta_rule(node, neighbors)
        deltas.append(d)

    # apply updates after computing all deltas
    for idx, node in enumerate(network.nodes):
        two_pi = 6.283185307179586
        node.phase = (node.phase + deltas[idx]) % two_pi

    return network


# internal safe test
if __name__ == "__main__":
    class _N:
        def __init__(self, p): self.phase = p

    from phase_network_v1 import PhaseNetworkV1

    net = PhaseNetworkV1()
    a = net.add_node(_N(0.1))
    b = net.add_node(_N(0.3))
    c = net.add_node(_N(0.2))

    net.add_edge(a, b)
    net.add_edge(b, c)

    # Simple static δ-rule (safe)
    def _rule(node, neighbors):
        if not neighbors: return 0.01
        return 0.1 * (sum(n.phase for n in neighbors)/len(neighbors) - node.phase)

    propagate_phases(net, _rule)
    print([n.phase for n in net.nodes])
