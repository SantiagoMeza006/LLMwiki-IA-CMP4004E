---
title: Propositional Logic — Syntax, Semantics, Entailment, Inference
type: concept
unit: logic
sources: [rn-ch07-logical-agents, slides-xx-prolog]
updated: 2026-09-30
---

# Propositional Logic 🎯

(R&N §7.3–7.5; slides-XX s.2–3 put it at the bottom of the ladder: "decidable, but it cannot say *every*".)

## Syntax
- **Atomic sentences:** proposition symbols (P, W₁,₃, FacingEast), plus True and False.
- **Connectives:** ¬ (negation), ∧ (conjunction), ∨ (disjunction), ⇒ (implication: premise/antecedent ⇒ conclusion/consequent), ⇔ (biconditional).
- **Literal:** atom or negated atom. **Precedence** (high → low): ¬, ∧, ∨, ⇒, ⇔.

## Semantics
A **model** assigns true/false to every symbol (n symbols → 2ⁿ models). Truth of complex sentences is computed recursively:

| P | Q | ¬P | P ∧ Q | P ∨ Q | P ⇒ Q | P ⇔ Q |
|---|---|---|---|---|---|---|
| F | F | T | F | F | **T** | T |
| F | T | T | F | T | **T** | F |
| T | F | F | F | T | **F** | F |
| T | T | F | T | T | T | T |

- P ⇒ Q is false **only** when P is true and Q false ("5 is even ⇒ Sam is smart" is true). No causation implied.
- ∨ is inclusive (xor is different).
- Wumpus rules need ⇔: `B₁,₁ ⇔ (P₁,₂ ∨ P₂,₁)`.

## Core definitions 🎯
| Term | Definition |
|---|---|
| m **satisfies** α (m is a model of α) | α true in m; M(α) = set of models of α |
| **Entailment** α ⊨ β | β true in **every** model where α is true ⇔ M(α) ⊆ M(β) |
| **Logical equivalence** α ≡ β | true in the same models ⇔ α ⊨ β and β ⊨ α |
| **Valid** (tautology) | true in all models (P ∨ ¬P) |
| **Satisfiable** | true in some model |
| **Deduction theorem** | α ⊨ β ⇔ (α ⇒ β) is valid |
| **Refutation** | α ⊨ β ⇔ (α ∧ ¬β) is **unsatisfiable** (reductio ad absurdum) |
| α valid ⇔ ¬α unsatisfiable | |
| **Inference** KB ⊢_i α | algorithm i derives α from KB |
| **Sound** | derives only entailed sentences ("doesn't make things up") |
| **Complete** | derives every entailed sentence |
| **Monotonicity** | if KB ⊨ α then KB ∧ β ⊨ α |

Haystack analogy: entailment = the needle is in the haystack; inference = finding it.
**SAT** (is a sentence satisfiable?) was the first NP-complete problem; propositional entailment is co-NP-complete.

## Standard equivalences (R&N Fig 7.11)
Commutativity and associativity of ∧, ∨ · double negation ¬¬α ≡ α · **contraposition** (α ⇒ β) ≡ (¬β ⇒ ¬α) · **implication elimination** (α ⇒ β) ≡ (¬α ∨ β) · **biconditional elimination** (α ⇔ β) ≡ (α ⇒ β) ∧ (β ⇒ α) · **De Morgan** ¬(α ∧ β) ≡ ¬α ∨ ¬β, ¬(α ∨ β) ≡ ¬α ∧ ¬β · **distributivity** of ∧ over ∨ and ∨ over ∧.

## Inference methods
| Method | Idea | Complete? | Page |
|---|---|---|---|
| **Model checking (TT-ENTAILS?)** | enumerate all 2ⁿ models; check α wherever KB is true. O(2ⁿ) time, O(n) space (depth-first) | ✅ | [logic-inference-traces](../exercises/logic-inference-traces.md) |
| **Inference rules + search** | Modus Ponens (α ⇒ β, α ⊢ β), And-Elimination (α ∧ β ⊢ α), equivalences; proof search can ignore irrelevant symbols | depends on the rules | same |
| **Resolution** (CNF) | one rule, refutation-complete | ✅ | [resolution](../algorithms/resolution.md) |
| **Forward / backward chaining** | Modus Ponens on **Horn** clauses, linear time | ✅ for Horn KBs | [forward-and-backward-chaining](forward-and-backward-chaining.md) |
| **DPLL** | smart backtracking model checking | ✅ | [dpll-and-walksat](../algorithms/dpll-and-walksat.md) |
| **WalkSAT** | local search for a model | ❌ (can't prove unsatisfiability) | same |

Compare: [inference-methods-comparison](../comparisons/inference-methods-comparison.md). Next level up: [first-order-logic](first-order-logic.md); restricted fragment: [logic-to-horn-clauses](logic-to-horn-clauses.md).
