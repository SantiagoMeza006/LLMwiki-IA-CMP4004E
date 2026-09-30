---
title: Forward and Backward Chaining
type: concept
unit: logic
sources: [slides-xx-prolog, rn-ch07-logical-agents, rn-ch09-fol-inference]
updated: 2026-09-30
---

# Forward and Backward Chaining

Inference over definite clauses ([Horn clauses](logic-to-horn-clauses.md)).

| | Forward chaining | Backward chaining 🎯 |
|---|---|---|
| Direction | **data-driven**: from known facts, fire every rule whose premises hold, add conclusions, until the query appears (or nothing new) | **goal-driven**: start from the query, find a clause whose head matches, try to prove its body, recurse down to facts |
| Touches | possibly many irrelevant facts | **only facts relevant to the query** |
| Space | size of derived facts | **linear in the size of the proof** (depth-first) |
| Used by | production systems, Datalog | **Prolog** |

## Backward chaining example — `Criminal(West)` (R&N Fig 9.7, slides-XX s.6–7)
Knowledge base (Prolog syntax):
```prolog
criminal(X) :- american(X), weapon(Y), sells(X, Y, Z), hostile(Z).
weapon(X)   :- missile(X).
hostile(X)  :- enemy(X, america).
sells(west, X, nono) :- missile(X), owns(nono, X).
american(west).   missile(m1).
owns(nono, m1).   enemy(nono, america).
```
Proof tree (depth-first, left-to-right):
```
criminal(west)
├── american(west)                 ✔ fact
├── weapon(Y)      → missile(Y)    ✔ Y = m1
├── sells(west, m1, Z)             Z = nono
│     ├── missile(m1)              ✔
│     └── owns(nono, m1)           ✔
└── hostile(nono)  → enemy(nono, america) ✔
```
`?- criminal(west).` → `true.`

## Propositional forward chaining — PL-FC-ENTAILS? (R&N Fig 7.15)
```
function PL-FC-ENTAILS?(KB, q) returns true or false
    count ← table: count[c] = number of symbols in clause c's premise
    inferred ← table: inferred[s] = false for all symbols
    queue ← symbols known to be true in KB
    while queue is not empty:
        p ← POP(queue)
        if p = q: return true
        if inferred[p] = false:
            inferred[p] ← true
            for each clause c in KB where p is in c.PREMISE:
                decrement count[c]
                if count[c] = 0: add c.CONCLUSION to queue
    return false
```
- **Sound** (each step is Modus Ponens), **complete** for Horn KBs (the final `inferred` table is a model of the KB, so every entailed atom is in it), **linear time**.
- Example (R&N Fig 7.16): `P ⇒ Q`, `L ∧ M ⇒ P`, `B ∧ L ⇒ M`, `A ∧ P ⇒ L`, `A ∧ B ⇒ L`, facts A, B. Order: A, B → L (A∧B) → M (B∧L) → P (L∧M) → Q (P). Verified in code: [logic-inference-traces](../exercises/logic-inference-traces.md).
- Backward chaining on the same KB works down the AND–OR graph from Q to A and B — essentially AND-OR-GRAPH-SEARCH ([nondeterministic search](nondeterministic-and-partially-observable-search.md)); often **much less than linear** because it touches only relevant facts.

## First-order versions (R&N §9.3–9.4)
- **First-order definite clauses:** exactly one positive literal; no ∃ (Skolemize first); variables implicitly ∀. **Datalog** = definite clauses without function symbols (the crime KB is Datalog).
- **FOL-FC-ASK:** each iteration fires every rule whose premises unify with known facts (via [Generalized Modus Ponens](first-order-inference.md#lifting-generalized-modus-ponens-gmp-)). Crime KB: iteration 1 adds `Sells(West, M1, Nono)`, `Weapon(M1)`, `Hostile(Nono)`; iteration 2 adds `Criminal(West)`; then a **fixed point**. Sound and complete for definite clauses; for Datalog it terminates in polynomial time (≤ p·n^k facts). With function symbols it may run forever (NatNum(S(S(…)))) — semidecidable.
- Efficiency: **conjunct ordering** (like MRV), matching is NP-hard in general (a CSP is one big definite clause), **incremental** forward chaining, the **Rete** algorithm (production systems like XCON, cognitive architectures ACT, SOAR), **magic sets** for deductive databases.
- **FOL-BC-ASK:** a **generator** of substitutions; FOL-BC-OR (try every rule whose head unifies with the goal) and FOL-BC-AND (prove every conjunct, threading θ) — an AND/OR search, depth-first → linear space, but repeated states and incompleteness.

## Caveats
- Backward chaining is a **depth-first search** — inherits DFS's incompleteness in infinite/cyclic spaces (left recursion loops). See [sld-resolution](../algorithms/sld-resolution.md).
- First-order entailment remains **semi-decidable**; Horn form only makes the search much cheaper than full resolution.

Related: [unification](unification.md) · [prolog](prolog.md)
