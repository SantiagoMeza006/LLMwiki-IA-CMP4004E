---
title: Expectiminimax (Games of Chance)
type: algorithm
unit: games-csp
sources: [rn-ch06-games]
updated: 2026-09-30
---

# Expectiminimax

(R&N §6.5.) **Stochastic games** (backgammon: dice decide which moves are legal) add **chance nodes** between MAX and MIN levels. Positions no longer have definite minimax values — only **expected** values.

## Definition
```
EXPECTIMINIMAX(s) = UTILITY(s, MAX)                                  if IS-TERMINAL(s)
                  = max_a EXPECTIMINIMAX(RESULT(s, a))              if TO-MOVE(s) = MAX
                  = min_a EXPECTIMINIMAX(RESULT(s, a))              if TO-MOVE(s) = MIN
                  = Σ_r P(r) · EXPECTIMINIMAX(RESULT(s, r))         if TO-MOVE(s) = CHANCE
```
Backgammon: 36 ordered rolls but **21 distinct**: 6 doubles with P = 1/36 each, 15 others with P = 1/18.

## Evaluation functions must be calibrated 🎯
R&N Fig 6.14: MAX chooses a1 or a2; each leads to a chance node with P = 0.9 / 0.1 over MIN results.
| Leaf values | a1 | a2 | Best |
|---|---|---|---|
| [2, 3] vs [1, 4] | 0.9·2 + 0.1·3 = **2.1** | 0.9·1 + 0.1·4 = 1.3 | a1 |
| [20, 30] vs [1, 400] (same order!) | 0.9·20 + 0.1·30 = 21 | 0.9·1 + 0.1·400 = **40.9** | a2 |

An **order-preserving** change of leaf values changed the decision. So EVAL must be a **positive linear transformation of the probability of winning** (or of expected utility) — unlike deterministic games, where only the order matters.

## Complexity
O(b^m · n^m) with n distinct chance outcomes (backgammon n = 21, b ≈ 20, sometimes up to 4000) → only ~3 ply is feasible. Alpha–beta-style pruning of chance nodes is possible if utilities are **bounded** (then an average can be bounded before seeing all children). Alternatives: sample chance outcomes, or use [MCTS](monte-carlo-tree-search.md) with random dice in playouts.

Worked: [games-traces](../exercises/games-traces.md). Related: [minimax](minimax.md) · [game-algorithms-comparison](../comparisons/game-algorithms-comparison.md)
