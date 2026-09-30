---
title: From Propositional Logic to Horn Clauses
type: concept
unit: logic
sources: [slides-xx-prolog, rn-ch07-logical-agents]
updated: 2026-09-30
---

# From Propositional Logic to Horn Clauses

(Slides-XX s.2–5; [R&N §7.5](../sources/rn-ch07-logical-agents.md). Foundations: [propositional-logic](propositional-logic.md), [first-order-logic](first-order-logic.md).)

## The ladder 🎯
| Level | Can express | Cost of inference |
|---|---|---|
| 1. **Propositional calculus** | facts, connectives, truth tables; **no objects**, can't say "every" | decidable |
| 2. **First-order calculus** | constants, variables, predicates, **quantifiers** (∀, ∃) | **undecidable** (semi-decidable) |
| 3. **Horn clauses** | the fragment with **at most one positive literal** | cheap: propositional definite-clause entailment is **linear** in KB size |
| 4. **Prolog** | Horn clauses + **backward chaining** + **unification** | depth-first search; can loop |

> **Algorithm = Logic + Control** (Kowalski 1979): your clauses are the logic; Prolog supplies the control.

## Clause form (CNF)
- **Literal:** a symbol or its negation. **Clause:** disjunction of literals. **CNF:** conjunction of clauses.
- Every propositional sentence has an equivalent CNF (nothing is lost).
- Why: **resolution** — one inference rule, refutation-complete for propositional logic — needs clause form.

## Horn clauses 🎯
A **Horn clause** has **at most one positive literal**.

| Kind | Clause form | Implication form | Role |
|---|---|---|---|
| **Definite clause** | ¬A ∨ ¬B ∨ C (exactly one positive) | A ∧ B ⇒ C | a **rule** |
| **Fact** | C | True ⇒ C | definite clause with empty body |
| **Goal clause** | ¬A ∨ ¬B (no positive) | A ∧ B ⇒ False | a **query** |

What the restriction buys:
1. clauses read as **implications**;
2. inference by **chaining** (forward: facts → query; backward: query → facts) — see [forward-and-backward-chaining](forward-and-backward-chaining.md);
3. **cheap entailment**.

What it costs: `P ∨ Q` (two positive literals) has **no Horn form** — Prolog cannot say "one of these, but I don't know which".

Extra facts from R&N §7.5.3:
- In implication form the premise is the **body** and the conclusion the **head** (Prolog: `head :- body.`).
- Horn clauses are **closed under resolution** (resolving two Horn clauses gives a Horn clause).
- **k-CNF**: CNF where every clause has at most k literals (3-CNF is the standard hard SAT form).
- Example definite clause: `¬L1,1 ∨ ¬Breeze ∨ B1,1` ≡ `(L1,1 ∧ Breeze) ⇒ B1,1`; `¬B1,1 ∨ P1,2 ∨ P2,1` is **not** Horn (two positive literals).
- R&N Fig 7.12 grammar: `CNFSentence → Clause1 ∧ … ∧ Clausen`, `Clause → Literal1 ∨ … ∨ Literalm`, `DefiniteClauseForm → Fact | (Symbol1 ∧ … ∧ Symboll) ⇒ Symbol`, `GoalClauseForm → (Symbol1 ∧ … ∧ Symboll) ⇒ False`.

Full proof procedure for *any* CNF (not only Horn): [resolution](../algorithms/resolution.md).

## AND–OR graph
A definite-clause KB can be drawn as an AND–OR graph: links joined by an arc are a **conjunction** (all premises needed), separate links are **alternatives**. Prolog explores exactly this graph **depth-first, left to right**.

Related: [prolog](prolog.md) · [unification](unification.md) · [sld-resolution](../algorithms/sld-resolution.md)
