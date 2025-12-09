import os
import json
import numpy as np
import matplotlib.pyplot as plt

EXPERIMENT_PREFIX = "Experiment_"
OUTPUT_DIR = "proof_output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_experiment_configs():
    configs = []
    for file in os.listdir("."):
        if file.startswith(EXPERIMENT_PREFIX) and file.endswith(".json"):
            with open(file, "r") as f:
                configs.append((file, json.load(f)))
    return configs

def simulate_phase_evolution(steps, noise_sigma, coupling=0.0):
    phase = np.zeros(steps)
    for i in range(1, steps):
        noise = np.random.normal(0, noise_sigma)
        phase[i] = phase[i-1] + noise - coupling * np.sin(phase[i-1])
    return phase

def compute_metrics(phase):
    drift = abs(phase[-1] - phase[0])
    max_drift = np.max(np.abs(phase - phase[0]))
    coherence = np.exp(-np.var(phase))
    return drift, max_drift, coherence

def save_plot(phase, name):
    plt.figure(figsize=(8, 3))
    plt.plot(phase, linewidth=1.0)
    plt.title(f"Phase Evolution — {name}")
    plt.xlabel("step")
    plt.ylabel("phase")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{name}.png"))
    plt.close()

def run_all():
    configs = load_experiment_configs()

    summary = []

    for filename, cfg in configs:
        name = cfg["experiment_id"]
        steps = cfg.get("steps", 1200)
        noise_sigma = cfg.get("noise_sigma", 0.05)
        coupling = cfg.get("coupling_strength", 0.0)

        print(f"Running {name} ({filename})...")

        phase = simulate_phase_evolution(
            steps=steps,
            noise_sigma=noise_sigma,
            coupling=coupling
        )

        drift, max_drift, coherence = compute_metrics(phase)
        save_plot(phase, name)

        summary.append({
            "experiment": name,
            "file": filename,
            "steps": steps,
            "noise_sigma": noise_sigma,
            "coupling": coupling,
            "drift": float(drift),
            "max_drift": float(max_drift),
            "coherence": float(coherence)
        })

    # Save summary
    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    # Save CSV version
    with open(os.path.join(OUTPUT_DIR, "summary.csv"), "w") as f:
        f.write("experiment,steps,noise_sigma,coupling,drift,max_drift,coherence\n")
        for s in summary:
            f.write(f"{s['experiment']},{s['steps']},{s['noise_sigma']},{s['coupling']},{s['drift']},{s['max_drift']},{s['coherence']}\n")

    print("\n=== Proof Complete ===")
    print(f"Outputs saved in: {OUTPUT_DIR}/")
    print("summary.json, summary.csv, and plots have been generated.")

if __name__ == "__main__":
    run_all()
