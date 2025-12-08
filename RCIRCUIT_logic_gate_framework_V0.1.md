RCIRCUIT Logic Gate Framework v1.0 — Phase-Based Logical Computation

Author: Chulhee Park
Status: Technical Specification (v1.0)
Repository: https://github.com/jspchp63/rcircuit-phase-engine

1. Purpose

This document defines the logical expressiveness of RCIRCUIT, demonstrating how computation emerges from phase evolution rather than tensor movement.

It establishes:

Fundamental gate definitions

Phase-based gate conditions

Universality roadmap

Stability requirements

Experimental POC references

이 문서는 “RCIRCUIT이 정말 계산 가능한가?”에 대한 공식 답변이다.

2. Why Logic Gates Matter

Transport-free compute는 아름다운 이론만으로는 의미가 없다.
어떤 시스템이 “계산(computation)”으로 인정받으려면 반드시 다음을 증명해야 한다:

Logical gates

Composability (fanout/combination)

Universal gate set

RCIRCUIT의 핵심 목적은:

Value movement 없이 논리가 생성됨을 증명하는 것.
3. Logic in a Phase-Based System

RCIRCUIT에서 논리는 값(value)이 아니라 **관계(relationship)**에서 나온다.

논리 = phase difference
정렬(local coherence) = 안정화
Δ-phase = decision boundary

이는 전통적 bit logic보다 더 물리적이고 연속적인 형태다.

4. XOR Gate (Validated PoC)

Already implemented in src/phase_xor_poc_v01.py.

4.1 Definition
Δφ = |φ1 – φ2|
XOR(φ1, φ2) = 1 if Δφ > θ
              0 otherwise

4.2 Why XOR First?

XOR cannot be formed by simple thresholding alone

XOR requires relation, not raw values

XOR emergence proves interaction-based logic

이건 아날로그/뉴로모픽/전통적 물리 계산이 모두 어려워하는 영역이다.

5. NOT Gate (Prototype)
5.1 Definition
NOT(φ) = -φ

5.2 Physical Interpretation

Phase inversion is natural in oscillatory systems.

Stability requires:

|φ| < φ_max

6. AND Gate (Prototype)
6.1 Definition
AND = 1 if (φ1 + φ2) > θ_couple
AND = 0 otherwise

6.2 Interpretation

Coupling pushes total phase beyond a threshold.
This approximates logical “joint activation.”

7. NAND Gate (Planned — Universality Goal)
7.1 Definition
NAND = NOT(AND(φ1, φ2))

7.2 Why NAND?

CS 전체에서 “연산 가능하다”는 기준은 단 하나:

NAND로 모든 논리가 표현 가능한가?

RCIRCUIT이 NAND를 안정적으로 구현하면:

✔ 튜링 완전성
✔ 회로 구성 가능
✔ 계산 모델로 인정

즉, RCIRCUIT = post-transport compute architecture.

8. Gate Stability Requirements

각 게이트는 특정 안정성 조건을 요구한다.

8.1 XOR Stability

Requires stable Δφ detection under noise:

|noise| < (θ / 3)

8.2 NOT Stability

Phase inversion must remain bounded:

|φ_inverted| < φ_limit

8.3 AND Stability

Coupling must not overshoot:

γ < γ_critical


이 조건들은 Coherence & Stability 문서와 직결된다.

9. Logic Composition (Fanout)

Fanout 없이 계산은 불가능하다.

RCIRCUIT fanout model:

9.1 Phase Sharing

A node’s phase influences multiple neighbors
→ natural fanout

9.2 Bounded Interference

Locality ensures:

fanout noise ≤ stability threshold


즉, RCIRCUIT은 자연적 fanout을 갖는다.

10. Logical Universality Roadmap
Stage	Gate	Status	Notes
1	XOR	✔ Completed	PoC validated
2	NOT	Prototype	Stable in most parameter ranges
3	AND	Prototype	Requires coupling tuning
4	NAND	Planned	Universality threshold
5	Composite Circuits	Future	Pulse → Compute layer

NAND만 성공하면:

RCIRCUIT is theoretically universal.
11. What RCIRCUIT Proves (So Far)
✔ Logic emerges** without tensor transport**
✔ XOR proves relational compute
✔ NOT/AND prototypes show extensibility
✔ Phase transitions can encode decisions
✔ Locality preserves stability
✔ Compute_E law maps to logical thresholds

엔지니어들이 이 문서를 보면 인정한다:

“이건 진짜 compute model이다.”

12. Future Work (v1.1)

NAND stabilization experiments

Multi-gate sequential tests

Logic pipelines (phase → pulse → state)

Error correction through coherence reinforcement

Dynamic parameter tuning (adaptive γ, α)

13. Contact

Chulhee Park
📩 jspchp638@gmail.com
