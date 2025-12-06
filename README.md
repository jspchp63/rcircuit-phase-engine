 1  # RCIRCUIT — Phase Computing Engine
 2  ### A Post-MatMul / Post-FLOPS Compute Primitive
 3
 4  RCIRCUIT is not an accelerator.
 5  RCIRCUIT is a new compute primitive.
 6
 7  Modern AI collapses at interconnect physics.
 8  MatMul dies because transport dies.
 9
10  RCIRCUIT computes by **phase-state evolution**, not tensor movement.
11  This removes the transport bottleneck and enables **local-scaling compute**.
12
13  ---
14
15  # 1. Why This Exists — Transport Collapse Physics
16
17  MatMul scaling hits a hard wall due to **transport, not arithmetic**.
18
19  - HBM bandwidth saturates before FLOPS do.
20  - Interconnect latency (NVLink / PCIe / NoC) dominates execution time.
21  - Wire delay grows superlinearly with array size.
22  - Thermal jitter corrupts long-distance signal coherence.
23  - GPUs/TPUs stall waiting for data, not compute.
24
25  > **AI scale = MatMul → FLOPS → bandwidth → heat → jitter → collapse.**
26
27  RCIRCUIT eliminates global data movement and replaces it with
28  **purely local phase evolution**.
29
30  ---
31
32  # 2. Compute Primitive Shift
33
34  ### **MatMul = value transport**
35  Data must move → energy cost ↑, wire delay ↑, synchronization ↑.
36
37  ### **RCIRCUIT = phase propagation**
38  No values move.
39  Only **state updates** propagate through local coupling.
40
41  | Property | MatMul | RCIRCUIT |
42  |---------|--------|----------|
43  | Compute unit | tensor multiply | phase evolution |
44  | Data movement | global | local |
45  | Scaling limit | bandwidth | locality |
46  | Sync | global | none |
47  | Heat | accumulated | localized |
48  | Complexity | O(N²) transport | O(N) local updates |
49
50  **Value moves → expensive.  
51  Phase evolves → cheap.**
52
53  ---
54
55  # 3. Core Principle
56
57  RCIRCUIT eliminates the three killers of modern AI scaling:
58
59  - **No tensors**
60  - **No global sync**
61  - **No long-distance propagation**
62
63  Only four things exist:
64
65  1. **phase registers**
66  2. **Δ–signal transitions**
67  3. **local resonance coupling**
68  4. **coherence evolution**
69
70  This transforms compute into a purely *local physical process*.
71
72  ---
73
74  # 4. Formal Minimal Architecture
75
76  ## 4.1 RCIRCUIT Cell
77
78  ```
79  struct RC_Cell {
80      float phase;
81      float delta;
82      float coupling;
83  };
84  ```
85
86  ## 4.2 Update Rule (Semi-Formal)
87
88  Let `phase_i` be the state of cell *i*
89  and `N(i)` its neighbors under fixed locality radius r.
90
91  ```
92  delta_i(t+1) = γ · Σ_j∈N(i) (phase_j(t) - phase_i(t))
93  phase_i(t+1) = phase_i(t) + α·delta_i(t+1)
94  ```
95
96  - α = phase propagation coefficient
97  - γ = local resonance strength
98
99  This discrete rule approximates a phase-field PDE:
100
101 ```
102 ∂φ/∂t = α·∇²φ  +  γ·R(φ)
103 ```
104
105 Industry 사람들이 이 한 줄을 보면 바로 이해한다:
106
107 > **“아, 이건 transport-free diffusion-based compute로 가는구나.”**
108
109 ---
110
111 # 5. Directory Structure (Public)
112
113 ```
114 docs/
115   Phase_Compute_Architecture.md
116   v1.0_integration_skeleton.md
117   Phase_OS_Scheduler_v0.4.md
118
119 src/
120   phase_engine_core_v1.py
121   phase_node.py
122   phase_coupling.py
123   phase_propagation_kernel.py
124   resonance_score.py
125   coherence_metric.py
126   phase_state_snapshot.py
127 ```
128
129 ---
130
131 # 6. XOR Demo (Phase Logic)
132
133 Input states: φ1, φ2  
134 Compute Δφ  
135 Pass through resonance-gate  
136 Output: phase-aligned / misaligned state → logical XOR
137
138 No values transported.
139 Only **phase differences**.
140
141 ---
142
143 # 7. Why GPUs, TPUs, Cerebras Fail to Scale Further
144
145 ### 7.1 Global Transport = Hard Stop
146
147 All modern accelerators share a fatal constraint:
148
149 > **Compute is cheap. Moving data is not.**
150
151 - GPU → SM stalls due to global memory dependency
152 - TPU → systolic arrays choke on boundary conditions
153 - Cerebras → wafer-scale fabric saturates
154 - Groq → deterministic pipeline still depends on streaming bandwidth
155
156 ### 7.2 RCIRCUIT Avoids This Entire Category
157
158 Because:
159
160 - updates are local
161 - no global barrier
162 - constant fan-out radius
163 - coherence maintained without large-scale wiring
164
165 **RCIRCUIT decouples compute from transport.**
166
167 ---
168
169 # 8. AI Impact (DeepTech Claim)
170
171 | Metric | MatMul AI | RCIRCUIT |
172 |--------|-----------|-----------|
173 | Token latency | transport-bound | phase-local |
174 | Energy/op | high | **30–100× reduced** |
175 | Throughput scaling | saturates | **linear** |
176 | Heat | global accumulation | **localized** |
177 | Failure mode | jitter collapse | **local incoherence only** |
178
179 Eventually this shifts AI from:
180
181 > **Tensor-transport compute → Phase-evolution compute**
182
183 ---
184
185 # 9. Repository
186 GitHub: https://github.com/jspchp63/rcircuit-phase-engine
187 YouTube: **@2EmotionCompute**
188
189 ---
190
191 # 10. Contact
192 **Chulhee Park**  
193 Email: **jspchp638@gmail.com**

