# Experiment Zero: Minimal Falsification Test

## Claim
Compute failure is not caused by insufficient FLOPs,
but by transport and synchronization.

## Setup (Thought Experiment)
Case A: Local phase-only interaction (no value transport)
Case B: Identical system with minimal value transport (1-bit)

## Observation
Case A maintains coherence.
Case B collapses coherence even at minimal transport.

## Interpretation
The failure appears before scale, FLOPs, or numerical precision limits.

## Falsification Path
If coherence survives arbitrary value transport,
this architecture is wrong.
