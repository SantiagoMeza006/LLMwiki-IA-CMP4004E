---
title: Alpha–Beta Pruning
type: algorithm
unit: games-csp
sources: [slides-02-problem-solving, rn-ch06-games]
updated: 2026-09-30
---

# Alpha–Beta Pruning 🎯

## Idea
[Minimax](minimax.md) explores the entire tree — too slow for real games. Alpha–beta **eliminates branches that cannot influence the final decision** and returns **exactly the same move/value as minimax** while exploring far fewer nodes (slides-02 s.20).

- **α** = best (highest) value found so far for **MAX** along the path → a **lower bound**.
- **β** = best (lowest) value found so far for **MIN** along the path → an **upper bound**.
- Every node carries an interval **[α, β]**; start with [−∞, +∞].

## Pruning rule 🎯
- At a **MIN** node, if its value drops to **≤ α** → prune (MAX above already has something at least as good, so MAX would never choose this path).
- At a **MAX** node, if its value rises to **≥ β** → prune (MIN above would never allow this path).

## Pseudocode (R&N Fig 6.7)
```
function ALPHA-BETA-SEARCH(game, state) returns an action
    player ← game.TO-MOVE(state)
    value, move ← MAX-VALUE(game, state, −∞, +∞)
    return move

function MAX-VALUE(game, state, α, β)
    if game.IS-TERMINAL(state): return game.UTILITY(state, player), null
    v ← −∞
    for each a in game.ACTIONS(state):
        v2, a2 ← MIN-VALUE(game, game.RESULT(state, a), α, β)
        if v2 > v: v, move ← v2, a;  α ← MAX(α, v)
        if v ≥ β: return v, move            # β cut-off
    return v, move

function MIN-VALUE(game, state, α, β)
    if game.IS-TERMINAL(state): return game.UTILITY(state, player), null
    v ← +∞
    for each a in game.ACTIONS(state):
        v2, a2 ← MAX-VALUE(game, game.RESULT(state, a), α, β)
        if v2 < v: v, move ← v2, a;  β ← MIN(β, v)
        if v ≤ α: return v, move            # α cut-off
    return v, move
```

## Example (R&N Fig 6.5, slides-02 s.21–22) on the Fig 6.2 tree
| Step | Event | Intervals |
|---|---|---|
| a | B's 1st leaf = 3 | B ∈ [−∞, 3] |
| b | B's 2nd leaf = 12 (MIN ignores) | B ∈ [−∞, 3] |
| c | B's 3rd leaf = 8 → B = 3 | B = [3,3]; A ∈ [3, +∞] |
| d | C's 1st leaf = 2 → C ≤ 2 < α = 3 | **prune C's other 2 leaves** (4 and 6) |
| e | D's 1st leaf = 14 | D ∈ [−∞, 14]; A ∈ [3, 14] |
| f | D's leaves 5, 2 → D = 2 | A = [3,3] → move **a1**, value 3 |

Full walkthrough: [minimax-alpha-beta-trace](../exercises/minimax-alpha-beta-trace.md).

## Properties
| | |
|---|---|
| Result | identical to minimax (pruning never changes the root value) |
| Time, perfect move ordering | **O(b^(m/2))** — effective branching √b; can search ~**twice as deep** as minimax in the same time |
| Time, random ordering | ≈ O(b^(3m/4)) |
| Time, worst ordering | O(b^m) (no pruning) |

**Move ordering matters** (R&N §6.2.4): with perfect ordering the effective branching factor is √b — for chess about **6 instead of 35**. How to get close:
- **Static ordering:** captures first, then threats, then forward moves, then backward moves → within ~2× of the best case.
- **Dynamic ordering / killer move heuristic:** try first the moves that were best before — from the previous move or from a shallower **iterative deepening** pass.
- **Transposition table:** cache values of positions reached by different move orders (transpositions), like the `reached` table in graph search — in chess it roughly **doubles** the reachable depth.

Even so, full-depth alpha–beta is impossible in chess → cut off with an evaluation function: [heuristic-alpha-beta](heuristic-alpha-beta.md).

## Common mistakes
- Thinking pruning can change the answer.
- Swapping the α and β roles (α belongs to MAX, β to MIN).
- Forgetting that the D subtree in Fig 6.5 is **not** pruned (its first leaf 14 > α).
