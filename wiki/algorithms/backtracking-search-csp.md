---
title: Backtracking Search for CSPs
type: algorithm
unit: games-csp
sources: [slides-02-problem-solving]
updated: 2026-09-29
---

# Backtracking Search for CSPs 🎯

## Idea
A **depth-first** search that assigns **one variable at a time**, checks constraints immediately, and **backtracks** (undoes the last assignment) when a variable has no legal value. Commutativity: the order of assignments doesn't change the final assignment, so we only branch on the values of one variable per level (no n!·dⁿ blow-up).

## Pseudocode (R&N Fig 5.5, slides-02 s.25)
```
function BACKTRACKING-SEARCH(csp) returns a solution or failure
    return BACKTRACK(csp, {})

function BACKTRACK(csp, assignment) returns a solution or failure
    if assignment is complete: return assignment
    var ← SELECT-UNASSIGNED-VARIABLE(csp, assignment)          # e.g. MRV, degree
    for each value in ORDER-DOMAIN-VALUES(csp, var, assignment):  # e.g. least-constraining value
        if value is consistent with assignment:
            add {var = value} to assignment
            inferences ← INFERENCE(csp, var, assignment)        # forward checking / arc consistency
            if inferences ≠ failure:
                add inferences to csp
                result ← BACKTRACK(csp, assignment)
                if result ≠ failure: return result
                remove inferences from csp
            remove {var = value} from assignment
    return failure
```

## Plug-in heuristics
| Hook | Heuristic | Rule |
|---|---|---|
| SELECT-UNASSIGNED-VARIABLE | **MRV** (minimum remaining values, "fail-first") | pick the variable with the fewest legal values |
| | Degree heuristic | tie-break: variable involved in most constraints with unassigned variables |
| ORDER-DOMAIN-VALUES | Least-constraining value | try first the value that rules out fewest options for neighbours |
| INFERENCE | **Forward checking** | remove inconsistent values from neighbours' domains; empty domain ⇒ fail now |
| | **Arc consistency (AC-3)** / MAC | propagate until every arc X→Y has support |

## Example — 4-Queens as a CSP
Variables Q1..Q4 (column of the queen in row i), domains {1,2,3,4}, constraints: different columns, not on a diagonal (|Qi − Qj| ≠ |i − j|). Backtracking finds `[2,4,1,3]`. Prolog version with "test as you go": [n-queens-prolog](../exercises/n-queens-prolog.md).

Properties: complete (finite domains), exponential worst case; memory linear in the number of variables (it's DFS — see [depth-first-search](depth-first-search.md#backtracking-search-variant)).

Concept: [constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md).
