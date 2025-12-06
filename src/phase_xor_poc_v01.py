import numpy as np

def phase_xor(phi1, phi2, threshold=0.5):
    """
    Simple XOR demo using phase difference.
    If |phi1 - phi2| is large → XOR = 1
    If |phi1 - phi2| is small → XOR = 0
    """
    diff = abs(phi1 - phi2)
    return 1 if diff > threshold else 0


def random_phase_pair():
    """Generate two random phases in [-1, 1]"""
    return np.random.uniform(-1, 1), np.random.uniform(-1, 1)


def run_demo(samples=10):
    print("=== RCIRCUIT XOR DEMO ===")
    for _ in range(samples):
        p1, p2 = random_phase_pair()
        out = phase_xor(p1, p2)
        print(f"φ1={p1:.3f}  φ2={p2:.3f}  |Δφ|={abs(p1-p2):.3f}  -> XOR={out}")


if __name__ == "__main__":
    run_demo()
