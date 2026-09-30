---
title: Inference in First-Order Logic (UI, EI, Generalized Modus Ponens)
type: concept
unit: logic
sources: [rn-ch09-fol-inference]
updated: 2026-09-30
---

# Inference in First-Order Logic

(R&N §9.1–9.2, [source](../sources/rn-ch09-fol-inference.md).)

## Instantiation rules
- **Universal Instantiation (UI):** from `∀v α` infer `SUBST({v/g}, α)` for **any ground term** g. From `∀x King(x) ∧ Greedy(x) ⇒ Evil(x)`: `King(John) ∧ Greedy(John) ⇒ Evil(John)`, `… Father(John) …`, etc. Can be applied many times.
- **Existential Instantiation (EI):** from `∃v α` infer `SUBST({v/k}, α)` with a **new** constant k — a **Skolem constant** (`∃x Crown(x) ∧ OnHead(x, John)` → `Crown(C1) ∧ OnHead(C1, John)`). Applied once, then the ∃ sentence can be dropped.

## Propositionalization
Instantiate every ∀ sentence with every ground term, replace ground atoms by proposition symbols, run a propositional algorithm. Problem: function symbols make the set of ground terms **infinite** (Father(Father(…))). **Herbrand's theorem**: if a sentence is entailed, a proof exists using a *finite* subset → generate terms by increasing depth. Complete, but:
> FOL entailment is **semidecidable** — an algorithm can say *yes* to every entailed sentence, but none can say *no* to every non-entailed one (Turing, Church 1936).

## Lifting: Generalized Modus Ponens (GMP) 🎯
For atomic sentences pᵢ, pᵢ′, q and a substitution θ with SUBST(θ, pᵢ′) = SUBST(θ, pᵢ) for all i:
```
p1′, p2′, …, pn′,   (p1 ∧ p2 ∧ … ∧ pn ⇒ q)
-------------------------------------------
              SUBST(θ, q)
```
Example: `King(John)`, `Greedy(y)` (everyone is greedy), `King(x) ∧ Greedy(x) ⇒ Evil(x)`, θ = {x/John, y/John} ⇒ `Evil(John)`.
Sound (by UI + Modus Ponens). It makes **only the substitutions needed** — the advantage of lifted inference over propositionalization. The substitutions are found by **[unification](unification.md)**.

## The three families of FOL inference
| Family | Works on | Page |
|---|---|---|
| **Forward chaining** (FOL-FC-ASK, Rete, Datalog) | definite clauses; sound & complete; Datalog in polynomial time | [forward-and-backward-chaining](forward-and-backward-chaining.md) |
| **Backward chaining** (FOL-BC-ASK, logic programming / Prolog) | definite clauses; DFS, linear space, can loop | same, [sld-resolution](../algorithms/sld-resolution.md) |
| **Resolution** (CNF + Skolem functions) | **any** FOL KB; refutation-complete | [resolution](../algorithms/resolution.md) |

## Storage and retrieval
STORE/FETCH underlie TELL/ASK. **Predicate indexing** (hash by predicate), multi-key indexing (e.g. Employs by 2nd argument), **subsumption lattice** of queries a fact can answer (O(2ⁿ) nodes for n arguments).

Related: [first-order-logic](first-order-logic.md) · [inference-methods-comparison](../comparisons/inference-methods-comparison.md)
