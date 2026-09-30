---
title: "R&N Chapter 7 — Logical Agents"
type: source
unit: logic
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch07-logical-agents]
updated: 2026-09-30
---

# R&N Chapter 7 — Logical Agents (pp. 226–267)

Reading assigned by [slides-XX](slides-xx-prolog.md) (§7.5 for Horn clauses and chaining). Builds the propositional foundation under Prolog.

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 7.1 | **Knowledge-based agent**: KB of sentences, TELL/ASK, inference; knowledge level vs implementation level; declarative vs procedural. | [knowledge-based-agents](../concepts/knowledge-based-agents.md) |
| 7.2 | **Wumpus world** (PEAS, 4×4 cave, percepts Stench/Breeze/Glitter/Bump/Scream); informal reasoning example. | same |
| 7.3 | Syntax, semantics, **models**, **entailment** α ⊨ β ⇔ M(α) ⊆ M(β); model checking; **soundness**, **completeness**, grounding. | [propositional-logic](../concepts/propositional-logic.md) |
| 7.4 | Propositional syntax (BNF, precedence ¬ ∧ ∨ ⇒ ⇔), truth tables; wumpus KB R1–R5; **TT-ENTAILS?** (O(2ⁿ) time, O(n) space) — 3 of 128 models satisfy the KB. | same, [logic-inference-traces](../exercises/logic-inference-traces.md) |
| 7.5 | Logical equivalence, **validity**, **deduction theorem**, **satisfiability**, refutation; inference rules (Modus Ponens, And-Elimination); monotonicity; **resolution**, **CNF conversion**, PL-RESOLUTION, ground resolution theorem; **Horn/definite clauses**; **forward chaining (PL-FC-ENTAILS?)** and **backward chaining** — linear time. | [resolution](../algorithms/resolution.md), [logic-to-horn-clauses](../concepts/logic-to-horn-clauses.md), [forward-and-backward-chaining](../concepts/forward-and-backward-chaining.md) |
| 7.6 | Efficient model checking: **DPLL** (early termination, pure symbols, unit clauses/unit propagation, component analysis, clause learning...) and **WalkSAT**; random SAT phase transition at m/n ≈ 4.26 for 3-SAT. | [dpll-and-walksat](../algorithms/dpll-and-walksat.md) |
| 7.7 | Agents based on propositional logic: fluents, **frame problem**, successor-state axioms, logical state estimation, SATPLAN; propositional logic doesn't scale → motivates FOL. | [knowledge-based-agents](../concepts/knowledge-based-agents.md#limits-of-propositional-agents) |

## Takeaways 🎯
1. **Entailment** (semantic, "in every model") vs **inference** (syntactic, "derive"): sound = derives only entailed sentences; complete = derives all of them.
2. `KB ⊨ α` ⇔ `KB ⇒ α` is valid ⇔ `KB ∧ ¬α` is unsatisfiable — the basis of proof by refutation (resolution).
3. Resolution + CNF is **complete** for propositional logic; forward/backward chaining are complete **for Horn KBs** and run in **linear time**.
4. SAT is NP-complete; DPLL (complete) and WalkSAT (incomplete, fast) are the practical workhorses.
5. Propositional logic can't say "for all squares" concisely → first-order logic ([rn-ch08](rn-ch08-first-order-logic.md)).
