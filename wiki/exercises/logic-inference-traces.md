---
title: "Exercise — Logic: model checking, CNF, resolution, forward chaining, FOL translation"
type: exercise
unit: logic
sources: [rn-ch07-logical-agents, rn-ch08-first-order-logic, rn-ch09-fol-inference]
updated: 2026-09-30
---

# Logic Inference Traces

Wumpus KB (R&N §7.4.3), after visiting [1,1] (no breeze) and [2,1] (breeze):
```
R1: ¬P1,1
R2: B1,1 ⇔ (P1,2 ∨ P2,1)
R3: B2,1 ⇔ (P1,1 ∨ P2,2 ∨ P3,1)
R4: ¬B1,1
R5: B2,1
```

## 1. Model checking (TT-ENTAILS?) — verified in code
7 symbols → 2⁷ = **128** models; KB is true in exactly **3**:
| Model | True symbols |
|---|---|
| 1 | B2,1, P3,1 |
| 2 | B2,1, P2,2 |
| 3 | B2,1, P2,2, P3,1 |
- **¬P1,2** holds in all 3 ⇒ KB ⊨ ¬P1,2 (no pit in [1,2]).
- P2,2 is true in 2 of 3 ⇒ KB entails neither P2,2 nor ¬P2,2.

## 2. Proof with inference rules (R&N §7.5.1)
1. Biconditional elimination on R2: R6 `(B1,1 ⇒ (P1,2 ∨ P2,1)) ∧ ((P1,2 ∨ P2,1) ⇒ B1,1)`
2. And-Elimination: R7 `(P1,2 ∨ P2,1) ⇒ B1,1`
3. Contraposition: R8 `¬B1,1 ⇒ ¬(P1,2 ∨ P2,1)`
4. Modus Ponens with R4: R9 `¬(P1,2 ∨ P2,1)`
5. De Morgan: R10 `¬P1,2 ∧ ¬P2,1` ∎
Notice it never touched B2,1, P2,2, P3,1 — proofs can ignore irrelevant symbols; model checking can't.

## 3. CNF conversion
Convert `B1,1 ⇔ (P1,2 ∨ P2,1)`. <details><summary>answer</summary>(¬B1,1 ∨ P1,2 ∨ P2,1) ∧ (¬P1,2 ∨ B1,1) ∧ (¬P2,1 ∨ B1,1) — steps in [resolution](../algorithms/resolution.md#converting-to-cnf-propositional-).</details>
Convert `(A ∧ B) ⇒ (C ∨ D)`. <details><summary>answer</summary>¬(A ∧ B) ∨ C ∨ D = ¬A ∨ ¬B ∨ C ∨ D (a single clause; not Horn — two positive literals).</details>
Convert `A ⇔ ¬B`. <details><summary>answer</summary>(A ⇒ ¬B) ∧ (¬B ⇒ A) → (¬A ∨ ¬B) ∧ (B ∨ A).</details>

## 4. Resolution refutation: KB = R2 ∧ R4, prove ¬P1,2
Clauses of KB ∧ ¬α: `¬B1,1 ∨ P1,2 ∨ P2,1`, `¬P1,2 ∨ B1,1`, `¬P2,1 ∨ B1,1`, `¬B1,1`, and the negated goal `P1,2`.
<details><summary>one refutation</summary>Resolve `¬P1,2 ∨ B1,1` with `¬B1,1` → `¬P1,2`. Resolve `¬P1,2` with `P1,2` → **empty clause** ⇒ KB ⊨ ¬P1,2.</details>

## 5. Unit resolution chain (R&N §7.5.2)
From R15 `P1,1 ∨ P2,2 ∨ P3,1`, R13 `¬P2,2`, R1 `¬P1,1`, derive where the pit is. <details><summary>answer</summary>R15 + R13 → `P1,1 ∨ P3,1`; + R1 → **P3,1** (pit in [3,1]).</details>

## 6. Forward chaining (R&N Fig 7.16) — verified in code
KB: `P ⇒ Q`, `L ∧ M ⇒ P`, `B ∧ L ⇒ M`, `A ∧ P ⇒ L`, `A ∧ B ⇒ L`, facts A, B. Query Q.
| Pop | Count reaching 0 | Add |
|---|---|---|
| A | — (A∧P⇒L needs P; A∧B⇒L needs B) | |
| B | A ∧ B ⇒ L | L |
| L | B ∧ L ⇒ M | M |
| M | L ∧ M ⇒ P | P |
| P | P ⇒ Q; A ∧ P ⇒ L (L already inferred) | Q |
| Q | = query → **true** | |

## 7. Translate to FOL
a. "Every student who takes AI likes Prolog." <details><summary>answer</summary>∀x Student(x) ∧ Takes(x, AI) ⇒ Likes(x, Prolog)</details>
b. "Some student failed the lab." <details><summary>answer</summary>∃x Student(x) ∧ Failed(x, Lab01) — ∃ with ∧, not ⇒.</details>
c. "Nobody is their own sibling." <details><summary>answer</summary>∀x ¬Sibling(x, x) (equivalently ¬∃x Sibling(x, x)).</details>
d. "Everyone has exactly one mother." <details><summary>answer</summary>∀x ∃m Mother(m, x) ∧ ∀y (Mother(y, x) ⇒ y = m) — or use a function: Mother(x).</details>
e. `∀x ∃y Loves(x, y)` vs `∃y ∀x Loves(x, y)` in English. <details><summary>answer</summary>Everybody loves somebody (maybe different people) vs there is one person whom everybody loves.</details>

## 8. Unification (FOL notation, lowercase = variable)
| Pair | MGU |
|---|---|
| P(x, F(y)), P(A, F(B)) | <details><summary>?</summary>{x/A, y/B}</details> |
| Q(x, x), Q(A, B) | <details><summary>?</summary>failure</details> |
| Older(Father(y), y), Older(Father(x), John) | <details><summary>?</summary>{y/John, x/John}</details> |
| Knows(Father(y), y), Knows(x, x) | <details><summary>?</summary>failure — x/Father(y) and x/y would need y = Father(y) (occur check)</details> |

## 9. Skolemization
`∀x ∃y Parent(y, x)` → ? `∃y ∀x Loves(x, y)` → ?
<details><summary>answer</summary>`Parent(F(x), x)` (Skolem **function**, since y is inside ∀x). `Loves(x, C)` (Skolem **constant**, since ∃y is outside every ∀).</details>

## 10. Generalized Modus Ponens
Facts `Missile(M1)`, `Owns(Nono, M1)`; rule `Missile(x) ∧ Owns(Nono, x) ⇒ Sells(West, x, Nono)`. θ and conclusion? <details><summary>answer</summary>θ = {x/M1} → `Sells(West, M1, Nono)`.</details>
