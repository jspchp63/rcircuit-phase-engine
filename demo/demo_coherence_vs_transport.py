"""
Demo: Coherence vs Transport
RCIRCUIT minimal demonstration

This script compares:
1) Transport-based synchronization (global averaging)
2) Transport-free local phase evolution (local coupling)

Metric: global coherence over time
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# parameters
# -----------------------------
N = 50            # number of oscillators
T = 300           # time steps
noise = 0.02
coupling = 0.05

# -----------------------------
# helpers
# -----------------------------
def coherence(phases):
    return np.abs(np.mean(np.exp(1j * phases)))

# -----------------------------
# CASE 1: transport-based sync
# -----------------------------
phases_transport = np.random.uniform(0, 2*np.pi, N)
coh_transport = []

for _ in range(T):
    global_mean = np.mean(phases_transport)          # transport
    phases_transport += coupling * (global_mean - phases_transport)
    phases_transport += noise * np.random.randn(N)
    coh_transport.append(coherence(phases_transport))

# -----------------------------
# CASE 2: transport-free local coupling
# -----------------------------
phases_local = np.random.uniform(0, 2*np.pi, N)
coh_local = []

for _ in range(T):
    neighbor_mean = np.roll(phases_local, 1)         # local only
    phases_local += coupling * (neighbor_mean - phases_local)
    phases_local += noise * np.random.randn(N)
    coh_local.append(coherence(phases_local))

# -----------------------------
# plot
# -----------------------------
plt.figure(figsize=(8,4))
plt.plot(coh_transport, label="Transport-based")
plt.plot(coh_local, label="Transport-free (local)")
plt.xlabel("time")
plt.ylabel("coherence")
plt.title("Coherence collapse: transport vs local phase evolution")
plt.legend()
plt.tight_layout()
plt.show()





plt.savefig("coherence_demo.png")
