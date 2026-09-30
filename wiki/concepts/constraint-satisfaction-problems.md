---
title: Constraint Satisfaction Problems (CSPs)
type: concept
unit: games-csp
sources: [slides-02-problem-solving, rn-ch05-csp]
updated: 2026-09-30
---

# Constraint Satisfaction Problems

Sources: [slides-02](../sources/slides-02-problem-solving.md) s.23–25 and [R&N Ch 5](../sources/rn-ch05-csp.md).

## Idea 🎯
- In standard search, states are **black boxes** (atomic); only reaching the goal matters.
- In a CSP, states have **internal structure** — a [factored representation](state-representations.md): **variables** with **values** that must satisfy **constraints**. This lets us use **general-purpose, domain-independent** heuristics and prune a partial assignment the moment it violates a constraint.
- Solved when we find a **complete** and **consistent** assignment. Solving CSPs is **NP-complete** in general.

## Components 🎯
| Symbol | Meaning |
|---|---|
| `X = {X1, ..., Xn}` | variables |
| `D = {D1, ..., Dn}` | domains (allowed values per variable) |
| `C` | constraints; each is ⟨scope, rel⟩, e.g. ⟨(X1, X2), X1 > X2⟩ or an explicit set of allowed tuples |

- **Consistent (legal)** assignment: violates no constraint. **Complete**: every variable assigned. **Solution** = consistent + complete. **Partial solution** = consistent partial assignment.
- **Constraint graph**: nodes = variables, edges = binary constraints (hypergraph for n-ary).

## Classic examples
| Problem | Variables | Domains | Constraints |
|---|---|---|---|
| 🎯 **Map colouring (Australia)** | WA, NT, Q, NSW, V, SA, T | {red, green, blue} | 9 "≠" constraints between neighbours (SA borders 5 regions; T borders none) |
| 🎯 **Sudoku** | 81 cells A1..I9 | {1..9} (givens: singleton) | 27 **Alldiff** (9 rows, 9 columns, 9 boxes) |
| 🎯 **School timetable** (slides) | classes | time slots | e.g. "sports cannot be after lunch" |
| 8-queens | Q1..Q8 (column) | rows {1..8} | no two in same row/diagonal |
| Job-shop scheduling (car assembly) | 15 task start times | {0..30} minutes | precedence `T1 + d1 ≤ T2`; disjunctive (`AxleF + 10 ≤ AxleB` or vice versa) |
| Cryptarithmetic TWO + TWO = FOUR | F,T,U,W,R,O + carries C1..C3 | digits | Alldiff + column sums |

## Kinds of variables and constraints
- **Domains:** discrete finite (map colouring), discrete infinite (integers — needs implicit constraints; nonlinear integer constraints are undecidable), continuous (linear programming — polynomial).
- **Constraints:** **unary** (SA ≠ green), **binary** (SA ≠ NSW), higher-order (Between(X,Y,Z)), **global** (Alldiff, Atmost — any number of variables). Any finite n-ary CSP can be turned binary (auxiliary variables or the **dual graph**).
- **Absolute** vs **preference** constraints (costs) → **constrained optimization problem (COP)**.

## Solving
1. **Constraint propagation** (inference): shrink domains using constraints — before or during search 🎯:
   - **Node consistency** (unary constraints), **arc consistency** (binary; algorithm [AC-3](../algorithms/ac-3.md)), **path consistency** (triples), **k-consistency**; special algorithms for **global constraints** (Alldiff: m variables but fewer than m values ⇒ fail; Atmost; **bounds propagation** e.g. F1 + F2 = 420 with F1 ∈ [0,165], F2 ∈ [0,385] ⇒ F1 ∈ [35,165], F2 ∈ [255,385]).
   - **Forward checking**: after assigning X, remove inconsistent values from X's unassigned neighbours; empty domain ⇒ backtrack now.
   - **MAC** (maintaining arc consistency): after assigning X, run AC-3 starting from the arcs into X — strictly stronger than forward checking.
2. **[Backtracking search](../algorithms/backtracking-search-csp.md)** with heuristics 🎯:
   - **MRV** (minimum remaining values, "most constrained variable", **fail-first**): choose the variable with the fewest legal values.
   - **Degree heuristic**: tie-break by the most constraints on other unassigned variables (SA has degree 5).
   - **Least-constraining value** (**fail-last**): try first the value that rules out fewest neighbour values.
   - Smarter backtracking: **backjumping** (conflict sets), **conflict-directed backjumping**, **constraint learning** (no-goods).
3. **Local search**: **[min-conflicts](../algorithms/min-conflicts.md)** on complete assignments.

> ⚠️ Slides-02 s.24 list "Forward Checking, Arc Consistency, Minimum Remaining Values" under *constraint propagation*. MRV is a **variable-ordering heuristic**, not propagation (R&N §5.3.1) — though forward checking computes exactly the information MRV needs.

## Structure of problems
(R&N §5.5)
- **Independent subproblems** (Tasmania): solve separately; n variables split into n/c groups turns d^n into (n/c)·d^c.
- **Tree-structured** constraint graph ⇒ solvable in **O(n·d²)**: topologically sort, make each parent→child arc consistent from the leaves up, then assign top-down with no backtracking. (General CSPs: O(dⁿ).)
- **Cutset conditioning**: assign a **cycle cutset** S (removing it leaves a tree), solve the tree for each assignment → O(d^c · (n − c)·d²) with c = |S|. Australia: cutset {SA}.
- **Tree decomposition**: solve a tree of overlapping subproblems; cost O(n·d^(w+1)) for tree width w.
- **Value symmetry**: permuting colours gives equivalent solutions → add **symmetry-breaking** constraints (e.g. NT < SA < WA alphabetically).

## Links
- CSPs are special cases of **SAT** and vice versa ([dpll-and-walksat](../algorithms/dpll-and-walksat.md)); a whole CSP can be written as one Prolog/Datalog definite clause (R&N Fig 9.5), and **constraint logic programming** extends Prolog with constraint solvers ([prolog](prolog.md)).
- [N-Queens in Prolog](../exercises/n-queens-prolog.md): "test as you go" = backtracking; up to 77× fewer inferences than generate-and-test.
- Worked: [csp-traces](../exercises/csp-traces.md). Practice: [practice-games-and-csp](../practice/practice-games-and-csp.md).
