import numpy as np

def phase_and(phi1, phi2, threshold=0.4):
    """
    Phase-based AND gate.
    Condition:
        If both phases are 'close to alignment' (Δφ small for both),
        AND = 1
    Otherwise:
        AND = 0
    """
    diff = abs(phi1 - phi2)
    return 1 if diff < threshold else 0


def random_phase_pair():
    """Generate two random phases in [-1, 1]"""
    return np.random.uniform(-1, 1), np.random.uniform(-1, 1)


def run_demo(samples=10):
    print("=== RCIRCUIT AND DEMO ===")
    for _ in range(samples):
        p1, p2 = random_phase_pair()
        out = phase_and(p1, p2)
        print(f"φ1={p1:.3f}  φ2={p2:.3f}  |Δφ|={abs(p1-p2):.3f}  -> AND={out}")


if __name__ == "__main__":
    run_demo()
