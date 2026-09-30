---
title: DPLL and WalkSAT (SAT solving)
type: algorithm
unit: logic
sources: [rn-ch07-logical-agents]
updated: 2026-09-30
---

# DPLL and WalkSAT — Efficient Propositional Model Checking

(R&N §7.6.) Both decide **satisfiability** of a CNF sentence (entailment via KB ∧ ¬α unsatisfiable).

## DPLL (Davis–Putnam–Logemann–Loveland) — complete backtracking
Depth-first enumeration of models (like TT-ENTAILS?) with three improvements:
1. **Early termination:** a clause is true as soon as one literal is true; the sentence is false as soon as one clause is false — decide on **partial** models.
2. **Pure symbol heuristic:** a symbol with the same sign in all (remaining) clauses — set it to make those literals true.
3. **Unit clause heuristic:** a clause with a single unassigned literal forces its value; the cascade is **unit propagation** (≈ forward chaining for Horn clauses).

Modern tricks (the CSP ideas again): **component analysis** (independent subproblems, like Tasmania), variable/value ordering (degree heuristic), **intelligent backtracking** with **conflict clause learning**, **random restarts**, clever indexing. Solvers handle millions of variables.

## WalkSAT — local search
```
function WALKSAT(clauses, p, max_flips) returns a satisfying model or failure
    model ← a random assignment of true/false to the symbols in clauses
    for i = 1 to max_flips:
        if model satisfies clauses: return model
        clause ← a randomly selected clause from clauses that is false in model
        if RANDOM(0, 1) ≤ p:  flip the value in model of a randomly selected symbol from clause
        else: flip whichever symbol in clause maximizes the number of satisfied clauses
    return failure
```
- p ≈ 0.5: mix of **random walk** and **min-conflicts** moves (see [min-conflicts](min-conflicts.md)).
- Returns a model ⇒ satisfiable. Returns failure ⇒ **unknown** (unsatisfiable or not enough flips) → **can't prove entailment** (e.g. can't prove a wumpus square is safe). Sound but incomplete; best when a solution is expected.

## Hard vs easy SAT problems
- **Underconstrained** (few clauses per variable): many solutions, easy (like n-queens). **Overconstrained**: likely unsatisfiable, also easy to refute.
- Random 3-CNF: the probability of satisfiability drops sharply around a **clause/symbol ratio m/n ≈ 4.26**; solver run time **peaks** there (satisfiability threshold conjecture).

| | DPLL | WalkSAT |
|---|---|---|
| Type | systematic (backtracking) | local search |
| Complete | ✅ (can prove unsat) | ❌ |
| Typical use | proving entailment | finding models quickly |

Related: [propositional-logic](../concepts/propositional-logic.md) · [constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md) · [inference-methods-comparison](../comparisons/inference-methods-comparison.md)
