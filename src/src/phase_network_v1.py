# src/phase_network_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal network structure (safe and standalone)

class PhaseNetworkV1:
    """Simple undirected graph for phase compute experiments."""
    def __init__(self):
        self.nodes = []
        self.edges = {}  # adjacency list: node_index -> list of neighbor indices

    def add_node(self, node):
        idx = len(self.nodes)
        self.nodes.append(node)
        self.edges[idx] = []
        return idx

    def add_edge(self, a, b):
        """Undirected link between nodes a and b."""
        if a in self.edges and b in self.edges:
            self.edges[a].append(b)
            self.edges[b].append(a)

    def neighbors_of(self, index):
        """Return neighbor node objects."""
        return [self.nodes[i] for i in self.edges[index]]

    def __repr__(self):
        return f"PhaseNetworkV1(nodes={len(self.nodes)}, edges={sum(len(v) for v in self.edges.values())})"


# Safe internal test
if __name__ == "__main__":
    class _Node:
        def __init__(self, p): self.phase = p

    net = PhaseNetworkV1()
    a = net.add_node(_Node(0.1))
    b = net.add_node(_Node(0.2))
    net.add_edge(a, b)

    print(net)
    print("Neighbors of a:", net.neighbors_of(a))
