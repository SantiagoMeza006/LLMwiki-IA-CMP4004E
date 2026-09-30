---
title: Min-Conflicts (Local Search for CSPs)
type: algorithm
unit: games-csp
sources: [rn-ch05-csp]
updated: 2026-09-30
---

# Min-Conflicts

## Idea
[Local search](../concepts/local-search.md) on **complete assignments**: start with every variable assigned (usually violating constraints); repeatedly pick a **conflicted** variable at random and give it the value that **minimises the number of conflicts** with the other variables (ties broken randomly).

## Pseudocode (R&N Fig 5.9)
```
function MIN-CONFLICTS(csp, max_steps) returns a solution or failure
    current ← an initial complete assignment for csp
    for i = 1 to max_steps:
        if current is a solution for csp: return current
        var ← a randomly chosen conflicted variable from csp.VARIABLES
        value ← the value v for var that minimizes CONFLICTS(csp, var, v, current)
        set var = value in current
    return failure
```

## Properties & facts
- **n-queens:** run time (excluding the initial placement) roughly **independent of n** — the **million-queens** problem in ~**50 steps** on average. Solutions are dense, so the problem is easy for local search.
- **Hubble Space Telescope:** scheduling a week of observations went from **3 weeks to ~10 minutes**.
- Landscapes have **plateaus** (many assignments one conflict away) → allow sideways moves, **tabu search** (forbid recently visited states), simulated annealing, or **constraint weighting** (raise weights of constraints that keep being violated — adds topography and learning).
- Great for **online repair**: when a schedule breaks (bad weather), start from the current schedule and fix it with few changes.
- Incomplete: can't prove that no solution exists.

## Example (R&N Fig 5.8)
8-queens: choose conflicted Q8, move it to a row with only 1 conflict; then Q6 to row 8 with 0 conflicts → solution in 2 steps.

Related: [ac-3](ac-3.md) · [backtracking-search-csp](backtracking-search-csp.md) · [hill-climbing](hill-climbing.md) · WalkSAT is the same idea for SAT → [dpll-and-walksat](dpll-and-walksat.md)
