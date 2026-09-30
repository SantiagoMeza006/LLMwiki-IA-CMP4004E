---
title: Logical Inference Methods — Comparison
type: comparison
unit: logic
sources: [rn-ch07-logical-agents, rn-ch09-fol-inference, slides-xx-prolog]
updated: 2026-09-30
---

# Logical Inference Methods — Comparison 🎯

| Method | Logic | KB form | Sound | Complete | Cost | Page |
|---|---|---|---|---|---|---|
| Truth-table model checking (TT-ENTAILS?) | propositional | any | ✅ | ✅ | O(2ⁿ) time, O(n) space | [propositional-logic](../concepts/propositional-logic.md) |
| DPLL | propositional | CNF | ✅ | ✅ | exponential worst case, fast in practice | [dpll-and-walksat](../algorithms/dpll-and-walksat.md) |
| WalkSAT | propositional | CNF | ✅ (a found model is real) | ❌ can't prove unsat | fast on satisfiable problems | same |
| Resolution | propositional | CNF | ✅ | ✅ refutation-complete | exponential worst case | [resolution](../algorithms/resolution.md) |
| Forward chaining (PL-FC-ENTAILS?) | propositional | **Horn / definite** | ✅ | ✅ (atoms) | **linear** | [forward-and-backward-chaining](../concepts/forward-and-backward-chaining.md) |
| Backward chaining | propositional | Horn / definite | ✅ | ✅ | linear, often less | same |
| Propositionalization + propositional prover | FOL | any | ✅ | ✅ but semidecidable | huge instantiation | [first-order-inference](../concepts/first-order-inference.md) |
| Forward chaining (FOL-FC-ASK, Rete) | FOL | definite clauses | ✅ | ✅ (Datalog: polynomial, terminates) | NP-hard matching per step in general | [forward-and-backward-chaining](../concepts/forward-and-backward-chaining.md) |
| Backward chaining (FOL-BC-ASK) | FOL | definite clauses | ✅ | ✅ in principle; **DFS implementation can loop** | linear space | same |
| **Prolog (SLD, depth-first, left-to-right)** | FOL fragment + database semantics | definite clauses + NAF | ✅ (❌ without occur check, rarely matters) | ❌ (left recursion) — ✅ for Datalog with tabling | fast | [sld-resolution](../algorithms/sld-resolution.md) |
| Resolution + Skolemization | FOL | CNF | ✅ | ✅ refutation-complete (semidecidable) | theorem provers | [resolution](../algorithms/resolution.md) |

## Key relationships
- **Entailment** is semantic; each method above is a syntactic procedure approximating it (sound = never wrong, complete = never misses).
- Backward chaining = resolution restricted to Horn clauses with a "spine" control strategy; Prolog = backward chaining with fixed DFS order.
- Forward chaining = data-driven (good for monitoring percepts); backward chaining = goal-driven (good for answering specific queries).
- DPLL/WalkSAT on SAT ≈ backtracking/min-conflicts on CSPs.

Related: [logic-to-horn-clauses](../concepts/logic-to-horn-clauses.md) · [logic-inference-traces](../exercises/logic-inference-traces.md)
