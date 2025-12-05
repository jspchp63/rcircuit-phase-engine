# src/phase_benchmark_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Minimal reproducible benchmark for phase-based computation

import time
from phase_compute_api_v1 import PhaseComputeAPI
from phase_config_v1 import PhaseConfig
from phase_analysis_v1 import phase_stability

def run_benchmark(steps=50, num_nodes=PhaseConfig.DEFAULT_NUM_NODES):
    """
    Benchmark RCIRCUIT phase engine by measuring:
    - runtime
    - final coherence
    - stability score
    """
    api = PhaseComputeAPI(num_nodes=num_nodes)

    start = time.time()
    api.run(steps)
    end = time.time()

    coherence = api.measure_coherence()
    stability = phase_stability(api.nodes)
    runtime_ms = (end - start) * 1000

    return {
        "nodes": num_nodes,
        "steps": steps,
        "runtime_ms": runtime_ms,
        "coherence": coherence,
        "stability": stability,
    }


if __name__ == "__main__":
    result = run_benchmark()
    
    print("\n=== RCIRCUIT Benchmark v1.0 ===")
    print(f"Nodes       : {result['nodes']}")
    print(f"Steps       : {result['steps']}")
    print(f"Runtime     : {result['runtime_ms']:.3f} ms")
    print(f"Coherence   : {result['coherence']:.6f}")
    print(f"Stability   : {result['stability']:.6f}")
    print("================================\n")
