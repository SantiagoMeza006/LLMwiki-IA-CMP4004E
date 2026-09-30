---
title: Backtracking Search for CSPs
type: algorithm
unit: games-csp
sources: [slides-02-problem-solving, rn-ch05-csp]
updated: 2026-09-30
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

Why "fail-first" for variables but "fail-last" for values? Every variable must be assigned eventually, so picking the likely failure first prunes early; but we only need **one** solution, so try the most promising value first (if we wanted *all* solutions, value order wouldn't matter). (R&N §5.3.1)

## Why assign one variable per level (R&N §5.3)
A naive depth-limited search over partial assignments branches on any variable/value pair: n·d at the top, (n−1)·d next… → **n!·dⁿ leaves** although only dⁿ complete assignments exist. CSPs are **commutative** (order of assignments doesn't matter), so BACKTRACK picks one variable per node → dⁿ leaves.

## Forward checking in action (R&N Fig 5.7, verified in code)
| After | WA | NT | Q | NSW | V | SA | T |
|---|---|---|---|---|---|---|---|
| start | RGB | RGB | RGB | RGB | RGB | RGB | RGB |
| WA = red | **R** | GB | RGB | RGB | RGB | GB | RGB |
| Q = green | R | **B** | **G** | RB | RGB | **B** | RGB |
| V = blue | R | B | G | R | **B** | **∅** ⇒ backtrack | RGB |

Forward checking misses that NT and SA are both {B} but adjacent after Q = green; **MAC** would catch it one step earlier.

## Looking backward: smarter backtracking
- **Chronological backtracking**: undo the most recent decision — with order Q, NSW, V, T, SA… a dead end at SA makes us pointlessly recolour Tasmania.
- **Backjumping**: jump to the most recent variable in SA's **conflict set** ({Q, NSW, V}). Redundant if you already use forward checking/MAC.
- **Conflict-directed backjumping**: conflict sets propagate: `conf(Xi) ← conf(Xi) ∪ conf(Xj) − {Xi}` when Xj fails.
- **Constraint learning**: record a minimal conflicting assignment as a **no-good** so the same dead end is never re-explored (key in modern CSP/SAT solvers).

## Example — 4-Queens as a CSP
Variables Q1..Q4 (column of the queen in row i), domains {1,2,3,4}, constraints: different columns, not on a diagonal (|Qi − Qj| ≠ |i − j|). Backtracking finds `[2,4,1,3]`. Prolog version with "test as you go": [n-queens-prolog](../exercises/n-queens-prolog.md).

Properties: complete (finite domains), exponential worst case; memory linear in the number of variables (it's DFS — see [depth-first-search](depth-first-search.md#backtracking-search-variant)).

Concept: [constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md).
