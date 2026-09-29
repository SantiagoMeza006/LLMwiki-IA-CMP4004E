---
title: Constraint Satisfaction Problems (CSPs)
type: concept
unit: games-csp
sources: [slides-02-problem-solving]
updated: 2026-09-29
---

# Constraint Satisfaction Problems

(Source: slides-02 s.23–25, based on R&N Ch 5 — not in our PDF excerpt.)

## Idea 🎯
- In standard search, states are **black boxes** (atomic); only reaching the goal matters.
- In a CSP, states have **internal structure** — a [factored representation](state-representations.md): **variables** with **values** that must satisfy **constraints**.
- Solved when we find a **complete** and **consistent** assignment.

## Components 🎯
| Symbol | Meaning |
|---|---|
| `X = {X1, ..., Xn}` | variables (what must be assigned) |
| `D = {D1, ..., Dn}` | domains (allowed values of each variable) |
| `C` | constraints (conditions the assignment must satisfy) |

- **Consistent** assignment: violates no constraint.
- **Complete** assignment: every variable has a value.
- Examples in class: **Sudoku** (no repeats in rows/columns/boxes); **school timetable** (e.g. "sports cannot be after lunch"). Classic textbook example: map colouring of Australia (WA, NT, SA, Q, NSW, V, T with {red, green, blue}, adjacent regions differ).

## Solving
1. [Backtracking search](../algorithms/backtracking-search-csp.md): depth-first, assign one variable at a time, undo on conflict.
2. **Constraint propagation** — shrink domains *before/while* assigning 🎯:
   - **Forward checking:** after assigning X, delete from each unassigned neighbour's domain the values inconsistent with X. If some domain becomes empty → backtrack immediately.
   - **Arc consistency (AC-3):** arc X→Y is consistent if for every value of X there is *some* allowed value of Y; repeatedly remove unsupported values until all arcs are consistent.
   - **Minimum Remaining Values (MRV):** choose next the variable with the fewest legal values left ("fail-first"). (Strictly, MRV is a *variable-ordering heuristic*, listed on the slide together with propagation techniques.) Companion heuristics: **degree heuristic** (tie-break: most constraints on unassigned variables) and **least-constraining value** (order values to leave most options for neighbours).

## Link to Prolog
[N-Queens in Prolog](../exercises/n-queens-prolog.md) is a CSP: "test as you go" (check constraints while placing) beats "generate and test" by up to 77× in inferences — the same idea as forward checking/backtracking vs brute force.

Related: [practice-games-and-csp](../practice/practice-games-and-csp.md)
