"""
Phase Engine v0.5 — 2D Local Phase Field Simulator
RCIRCUIT Phase Computing Engine
Author: Chulhee Park

Purpose
-------
This is a minimal transport-free phase evolution engine for RCIRCUIT.

- 2D grid of phase nodes
- Local coupling via Laplacian
- No global transport
- O(N) local update cost
- Simple coherence metric

This file is intentionally simple:
- Easy to read
- Easy to extend
- Safe to share as a research prototype

It is NOT an HPC implementation.
It is the reference engine for the RCIRCUIT whitepaper.
"""

import numpy as np

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


class PhaseEngine2D:
    """
    Minimal 2D phase evolution engine.

    State:
        phase[i, j]   : local phase value
        delta[i, j]   : local update value (Δ-phase)
    Parameters:
        alpha         : phase propagation coefficient
        gamma         : coupling strength
        lambda_c      : locality / coherence decay constant
    """

    def __init__(
        self,
        nx: int = 64,
        ny: int = 64,
        alpha: float = 0.2,
        gamma: float = 0.1,
        lambda_c: float = 0.02,
        seed: int | None = 42,
    ) -> None:
        if seed is not None:
            np.random.seed(seed)

        self.nx = nx
        self.ny = ny
        self.alpha = alpha
        self.gamma = gamma
        self.lambda_c = lambda_c

        # Initialize phase field with small random noise around 0
        self.phase = 0.1 * np.random.randn(nx, ny)
        self.delta = np.zeros_like(self.phase)

    # ---- Core Local Operator -------------------------------------------------

    @staticmethod
    def laplacian_periodic(field: np.ndarray) -> np.ndarray:
        """
        2D Laplacian with periodic boundary conditions.

        This represents local coupling:
            Σ_j∈N(i) (phase_j - phase_i)
        up to a constant factor.
        """
        up = np.roll(field, -1, axis=0)
        down = np.roll(field, 1, axis=0)
        left = np.roll(field, -1, axis=1)
        right = np.roll(field, 1, axis=1)

        return (up + down + left + right - 4.0 * field)

    # ---- Update Step ---------------------------------------------------------

    def step(self) -> None:
        """
        Single phase evolution step.

        The update rule corresponds to:

            delta_i(t+1) = γ * Σ_j∈N(i)( phase_j - phase_i )
            phase_i(t+1) = phase_i(t) + α * delta_i(t+1)

        In PDE form (continuous limit):

            ∂φ/∂t = α ∇²φ + γ R(φ)

        Here we implement the ∇²φ (diffusion-like) part directly.
        """
        lap = self.laplacian_periodic(self.phase)
        self.delta = self.gamma * lap
        self.phase = self.phase + self.alpha * self.delta

    # ---- Metrics -------------------------------------------------------------

    def global_coherence(self) -> float:
        """
        Simple global coherence metric in [-1, 1].

        If all phases are aligned, coherence ~ 1.
        If phases are random, coherence ~ 0.
        """
        mean_phase = np.mean(self.phase)
        return float(np.mean(np.cos(self.phase - mean_phase)))

    def compute_E_scalar(self) -> float:
        """
        A scalar proxy for the Compute_E law:

            Compute_E = (PhaseAmplitude × CouplingStrength) / PropagationTime

        Here we approximate:
            PhaseAmplitude  ~ RMS of phase
            CouplingStrength ~ gamma
            PropagationTime  ~ 1 (single step)

        This is NOT a full physical energy.
        It is a diagnostic indicator connecting the law to the engine.
        """
        phase_amplitude = float(np.sqrt(np.mean(self.phase ** 2)))
        return (phase_amplitude * self.gamma) / 1.0


# ---- Optional Visualization Helpers -----------------------------------------


def plot_phase_field(phase: np.ndarray, step_idx: int | None = None) -> None:
    """
    Simple 2D phase field plot.

    This is only for local testing / demo.
    """
    if not HAS_MPL:
        print("[PhaseEngine2D] matplotlib not available, skipping plot.")
        return

    plt.figure(figsize=(5, 5))
    plt.imshow(phase, cmap="twilight", interpolation="nearest")
    plt.colorbar(label="phase")
    title = "Phase field"
    if step_idx is not None:
        title += f" (step {step_idx})"
    plt.title(title)
    plt.tight_layout()
    plt.show()


# ---- Main Demo --------------------------------------------------------------


def run_demo(
    steps: int = 200,
    print_interval: int = 20,
    preview_plot: bool = False,
) -> None:
    """
    Simple 2D demo run.

    - Evolves the phase field for a number of steps.
    - Prints coherence and Compute_E every print_interval.
    - Optionally shows a plot at the end.

    This is the official "Phase Engine v0.5" reference run.
    """
    engine = PhaseEngine2D(nx=64, ny=64, alpha=0.22, gamma=0.12, lambda_c=0.02)

    print("=== RCIRCUIT Phase Engine v0.5 — 2D Demo ===")
    print(f"Grid        : {engine.nx} x {engine.ny}")
    print(f"alpha       : {engine.alpha}")
    print(f"gamma       : {engine.gamma}")
    print(f"lambda_c    : {engine.lambda_c}")
    print("--------------------------------------------")

    for t in range(steps):
        engine.step()

        if (t + 1) % print_interval == 0:
            coh = engine.global_coherence()
            compute_e = engine.compute_E_scalar()
            print(
                f"step {t+1:4d} | "
                f"coherence = {coh: .4f} | "
                f"Compute_E ≈ {compute_e: .4f}"
            )

    if preview_plot:
        plot_phase_field(engine.phase, step_idx=steps)


if __name__ == "__main__":
    # Default demo run.
    #
    # From the repository root:
    #   python src/phase_engine_v0_5_sim2d.py
    #
    # If matplotlib is installed, set preview_plot=True
    # to see a zebra-like phase pattern at the end.
    run_demo(
        steps=200,
        print_interval=20,
        preview_plot=False,  # change to True if you want to see the plot
