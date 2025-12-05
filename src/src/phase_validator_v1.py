# src/phase_validator_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Internal consistency checks for phase-based computation

from phase_node_v1 import PhaseNode
from phase_config_v1 import PhaseConfig

def validate_node_structure(nodes):
    """Ensure all nodes expose required attributes."""
    for n in nodes:
        if not hasattr(n, "phase"):
            return False
        if not isinstance(n.phase, (int, float)):
            return False
    return True


def validate_phase_bounds(nodes):
    """Ensure phase values remain within configured bounds."""
    for n in nodes:
        if not (PhaseConfig.PHASE_MIN <= n.phase <= PhaseConfig.PHASE_MAX):
            return False
    return True


def validate_coherence_value(value):
    """Coherence must be between 0 and 1."""
    return 0 <= value <= 1


def run_all_validations(nodes, coherence_score):
    return {
        "node_structure_ok": validate_node_structure(nodes),
        "phase_bounds_ok": validate_phase_bounds(nodes),
        "coherence_valid": validate_coherence_value(coherence_score),
    }


if __name__ == "__main__":
    # minimal self-test
    test_nodes = [PhaseNode(initial_phase=0.2), PhaseNode(initial_phase=0.7)]
    result = run_all_validations(test_nodes, coherence_score=0.85)
    print("Validation results:", result)
