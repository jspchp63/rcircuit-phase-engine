# src/noise_model_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal noise model (safe, dependency-free)

import random

def gaussian_noise(std=0.01):
    """
    Return a single Gaussian noise value.
    Prototype version: uses Python's random module only.
    """
    return random.gauss(0, std)


def apply_noise_to_phase(phase, std=0.01):
    """
    Add noise to a phase value, modulo 2π.
    """
    two_pi = 6.283185307179586
    noisy = (phase + gaussian_noise(std)) % two_pi
    return noisy


if __name__ == "__main__":
    # Simple quick test
    base_phase = 0.5
    for _ in range(5):
        print("noisy:", apply_noise_to_phase(base_phase))
