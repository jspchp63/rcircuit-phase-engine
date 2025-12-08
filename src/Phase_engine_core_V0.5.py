# Phase Engine v0.5 — Local Update Compute Engine
# Author: Chulhee Park

import numpy as np

class PhaseEngine:
    def __init__(self, size=50, alpha=0.15, gamma=0.25, noise=0.0):
        self.size = size
        self.alpha = alpha
        self.gamma = gamma
        self.noise = noise

        # initialize phase field
        self.phase = np.random.uniform(-1, 1, (size, size))
        self.delta = np.zeros((size, size))

    def step(self):
        # compute Laplacian (local neighborhood interaction)
        laplacian = (
            np.roll(self.phase, 1, axis=0) +
            np.roll(self.phase, -1, axis=0) +
            np.roll(self.phase, 1, axis=1) +
            np.roll(self.phase, -1, axis=1) -
            4 * self.phase
        )

        # update delta
        self.delta = self.gamma * laplacian
        
        # noise injection
        if self.noise > 0:
            self.delta += np.random.normal(0, self.noise, self.phase.shape)

        # phase update
        self.phase += self.alpha * self.delta

        return self.phase
✅ (B) 실험 3–4개 tx
