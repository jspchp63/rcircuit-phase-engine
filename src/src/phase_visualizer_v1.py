# src/phase_visualizer_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal visualizer (text-based, safe for all environments)

def visualize_phase_states(phases, title="Phase State Visualization"):
    """
    Very simple visualizer: prints bar-length per phase value.
    No external libraries required.
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    two_pi = 6.283185307179586

    for i, p in enumerate(phases):
        normalized = p / two_pi
        bars = int(normalized * 40)
        print(f"Node {i:02d} | phase={p:.4f} | " + ("█" * bars))


def visualize_experiment_results(results):
    """
    Accepts list of phase arrays (multiple trials).
    Produces text-based visual summary.
    """
    for idx, phases in enumerate(results):
        title = f"Trial {idx+1} — Final Phase Distribution"
        visualize_phase_states(phases, title=title)


if __name__ == "__main__":
    example = [
        [0.1, 1.2, 2.5, 3.8, 5.0],
        [0.2, 1.4, 2.7, 4.0, 5.2]
    ]
    visualize_experiment_results(example)
