# src/phase_config_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Global configuration values for phase computation experiments

class PhaseConfig:
    """
    Centralized configuration for RCIRCUIT components.
    All phase engines, experiments, and schedulers refer to this.
    """

    # Phase update sensitivity
    COUPLING_STRENGTH = 0.12     # how strongly nodes influence each other
    PROPAGATION_GAIN = 0.85      # damping factor for stability

    # Noise model parameters
    NOISE_STD = 0.005            # standard deviation of random noise
    NOISE_ENABLED = True

    # Phase bounds (for clipping or wrap-around)
    PHASE_MIN = 0.0
    PHASE_MAX = 1.0

    # Coherence scoring
    COHERENCE_DECAY = 0.98       # stabilizer constant

    # Simulation defaults
    DEFAULT_NUM_NODES = 5
    DEFAULT_STEPS = 20


if __name__ == "__main__":
    print("PhaseConfig loaded.")
    print("COUPLING_STRENGTH =", PhaseConfig.COUPLING_STRENGTH)
    print("PROPAGATION_GAIN =", PhaseConfig.PROPAGATION_GAIN)
