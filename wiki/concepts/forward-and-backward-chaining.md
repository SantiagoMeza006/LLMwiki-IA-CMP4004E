---
title: Forward and Backward Chaining
type: concept
unit: logic
sources: [slides-xx-prolog]
updated: 2026-09-29
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

## Caveats
- Backward chaining is a **depth-first search** — inherits DFS's incompleteness in infinite/cyclic spaces (left recursion loops). See [sld-resolution](../algorithms/sld-resolution.md).
- First-order entailment remains **semi-decidable**; Horn form only makes the search much cheaper than full resolution.

Related: [unification](unification.md) · [prolog](prolog.md)
