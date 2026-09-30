---
title: Minimax
type: algorithm
unit: games-csp
sources: [slides-02-problem-solving, rn-ch06-games]
updated: 2026-09-30
---

# Minimax 🎯

## Idea
**MAX** tries to maximise the value of the final state, **MIN** tries to minimise it; **both play optimally**. The minimax value of a node is defined recursively (slides-02 s.18):

```
MINIMAX(s) = UTILITY(s, MAX)                         if IS-TERMINAL(s)
           = max_{a ∈ ACTIONS(s)} MINIMAX(RESULT(s,a))  if TO-MOVE(s) = MAX
           = min_{a ∈ ACTIONS(s)} MINIMAX(RESULT(s,a))  if TO-MOVE(s) = MIN
```
Values are **backed up** from the leaves to the root; MAX picks the move leading to the highest value.

## Pseudocode (R&N Fig 6.3, on slides-02 s.19)
```
function MINIMAX-SEARCH(game, state) returns an action
    player ← game.TO-MOVE(state)
    value, move ← MAX-VALUE(game, state)
    return move

function MAX-VALUE(game, state) returns (utility, move)
    if game.IS-TERMINAL(state): return game.UTILITY(state, player), null
    v ← −∞
    for each a in game.ACTIONS(state):
        v2, a2 ← MIN-VALUE(game, game.RESULT(state, a))
        if v2 > v: v, move ← v2, a
    return v, move

function MIN-VALUE(game, state) returns (utility, move)
    if game.IS-TERMINAL(state): return game.UTILITY(state, player), null
    v ← +∞
    for each a in game.ACTIONS(state):
        v2, a2 ← MAX-VALUE(game, game.RESULT(state, a))
        if v2 < v: v, move ← v2, a
    return v, move
```

## Example (R&N Fig 6.2) — two-ply tree
```
                 A (MAX) = 3
        a1 /        | a2       \ a3
   B (MIN)=3    C (MIN)=2     D (MIN)=2
   3  12  8     2   4   6     14   5   2
```
B = min(3,12,8) = 3; C = min(2,4,6) = 2; D = min(14,5,2) = 2; A = max(3,2,2) = **3** → MAX plays **a1**; MIN's best reply is **b1**.

## Properties
| | |
|---|---|
| Complete | Yes, if the tree is finite |
| Optimal | Yes, against an optimal opponent |
| Time | **O(b^m)** — explores the complete tree down to terminal nodes |
| Space | **O(b·m)** (depth-first; O(m) if generating one action at a time) |

Chess: b ≈ 35, m ≈ 80 ply → 35⁸⁰ ≈ 10¹²³ states (R&N §6.2.1) → infeasible. Tic-tac-toe has fewer than 9! = 362,880 terminal nodes; chess has over 10⁴⁰ nodes. Fixes: [alpha-beta pruning](alpha-beta-pruning.md); cut off at a depth and use a heuristic **evaluation function** ([heuristic-alpha-beta](heuristic-alpha-beta.md)); or sample with [MCTS](monte-carlo-tree-search.md).

## Multiplayer games
(R&N §6.2.2) Replace the single value by a **vector of utilities** ⟨vA, vB, vC⟩; each player picks the child whose vector is best **for itself**, and that vector is backed up. E.g. C choosing between ⟨1, 2, 6⟩ and ⟨4, 2, 3⟩ picks ⟨1, 2, 6⟩. Multiplayer games show **alliances** forming and breaking; in two-player zero-sum games the vector collapses to one number.

## Games of chance
Add chance nodes and average → [expectiminimax](expectiminimax.md).

Worked: [minimax-alpha-beta-trace](../exercises/minimax-alpha-beta-trace.md). Concept: [adversarial-search](../concepts/adversarial-search.md).
