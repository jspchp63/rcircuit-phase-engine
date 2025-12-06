import numpy as np

class RCircuitGrid:
    def __init__(self, size=32, alpha=0.15, gamma=0.12):
        self.size = size
        self.alpha = alpha
        self.gamma = gamma
        self.phase = np.random.uniform(-1, 1, (size, size))
        self.delta = np.zeros((size, size))

    def step(self):
        """One simulation step."""
        padded = np.pad(self.phase, 1, mode="wrap")
        new_delta = np.zeros_like(self.phase)

        for i in range(self.size):
            for j in range(self.size):
                neighbors = [
                    padded[i, j+1],
                    padded[i+2, j+1],
                    padded[i+1, j],
                    padded[i+1, j+2],
                ]
                local = padded[i+1, j+1]
                new_delta[i, j] = self.gamma * sum(n - local for n in neighbors)

        self.delta = new_delta
        self.phase = self.phase + self.alpha * self.delta
        return self.phase
