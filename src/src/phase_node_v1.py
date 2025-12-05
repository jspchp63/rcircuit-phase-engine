# src/phase_node_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal standalone PhaseNode implementation (safe version)

class PhaseNodeV1:
    """Independent node with simple phase + Δsignal update."""
    def __init__(self, phase=0.0):
        self.phase = phase

    def compute_delta(self):
        """
        Base Δsignal placeholder.
        No external dependency.
        """
        return 0.01  # constant delta for v1.0 skeleton

    def update_phase(self, delta):
        """Update phase with wrap-around at 2π."""
        two_pi = 6.283185307179586
        self.phase = (self.phase + delta) % two_pi

    def __repr__(self):
        return f"PhaseNodeV1(phase={self.phase:.4f})"
