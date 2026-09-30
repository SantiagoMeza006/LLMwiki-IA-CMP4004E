---
title: AC-3 (Arc Consistency)
type: algorithm
unit: games-csp
sources: [rn-ch05-csp, slides-02-problem-solving]
updated: 2026-09-30
---

# AC-3 — Arc Consistency 🎯

## Idea
Variable Xi is **arc-consistent** with respect to Xj if **for every value in Di there is some value in Dj** that satisfies the binary constraint on (Xi, Xj). AC-3 removes values that have no such **support**, and whenever a domain shrinks it re-checks the arcs pointing into that variable. Mackworth (1977) — "3" because it was the third version in the paper.

## Pseudocode (R&N Fig 5.3)
```
function AC-3(csp) returns false if an inconsistency is found and true otherwise
    queue ← all the arcs in csp          # each binary constraint gives 2 arcs
    while queue is not empty:
        (Xi, Xj) ← POP(queue)
        if REVISE(csp, Xi, Xj):
            if size of Di = 0: return false
            for each Xk in Xi.NEIGHBORS − {Xj}:
                add (Xk, Xi) to queue
    return true

function REVISE(csp, Xi, Xj) returns true iff we revise the domain of Xi
    revised ← false
    for each x in Di:
        if no value y in Dj allows (x, y) to satisfy the constraint between Xi and Xj:
            delete x from Di;  revised ← true
    return revised
```

## Properties
| | |
|---|---|
| Result | an **equivalent** CSP (same solutions) with smaller domains; may solve it (all singletons) or prove no solution (an empty domain) |
| Time | **O(c·d³)** — c arcs, domain size ≤ d: each arc re-queued ≤ d times, each check O(d²) |
| Limits | can't see inconsistencies that need 3+ variables: 2-colouring the Australian triangle WA–NT–SA is arc-consistent but unsolvable (needs **path consistency**) |

## Examples
- `Y = X²`, both over digits 0–9 → X ∈ {0,1,2,3}, Y ∈ {0,1,4,9}.
- Australia with 3 colours and no assignment: AC-3 removes **nothing** (every colour of SA has a different colour available for WA).
- Sudoku: AC-3 alone solves the easy puzzle in R&N Fig 5.4 (E6 → {4}, then I6 → {7}, then A6 → 1, ...); harder puzzles need path consistency or cleverer reasoning ("naked triples").
- **MAC** = run AC-3 inside backtracking after each assignment, starting only from arcs (Xj, Xi) into the just-assigned Xi.

## Common mistakes
- Checking only (Xi, Xj) and forgetting the reverse arc (Xj, Xi).
- Not re-queuing neighbours after a revision.
- Thinking arc consistency guarantees a solution exists — it doesn't.

Worked: [csp-traces](../exercises/csp-traces.md). Concept: [constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md).
