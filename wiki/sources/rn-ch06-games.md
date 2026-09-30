---
title: "R&N Chapter 6 — Adversarial Search and Games"
type: source
unit: games-csp
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch06-games]
updated: 2026-09-30
---

# R&N Chapter 6 — Adversarial Search and Games (pp. 192–225)

Textbook behind [slides-02](slides-02-problem-solving.md) s.17–22.

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 6.1 | Game theory setting; deterministic, two-player, turn-taking, **perfect information, zero-sum** ("constant-sum" would be more accurate). Formal game: S0, TO-MOVE, ACTIONS, RESULT, IS-TERMINAL, UTILITY. Ply; tic-tac-toe < 9! = 362,880 terminal nodes; chess > 10^40 nodes. | [adversarial-search](../concepts/adversarial-search.md) |
| 6.2.1 | **Minimax** value and algorithm (Figs 6.2, 6.3): O(b^m) time, O(bm) space. Chess b ≈ 35, m ≈ 80 → 35^80 ≈ 10^123. | [minimax](../algorithms/minimax.md) |
| 6.2.2 | Multiplayer games: vector of utilities; alliances emerge. | [minimax](../algorithms/minimax.md#multiplayer-games) |
| 6.2.3–6.2.4 | **Alpha–beta** (Figs 6.5, 6.7), **move ordering**: perfect O(b^(m/2)) (chess b ≈ 6 instead of 35), random ≈ O(b^(3m/4)); killer moves, iterative deepening, **transposition tables**; Shannon's Type A (wide/shallow) vs Type B (deep/narrow). | [alpha-beta-pruning](../algorithms/alpha-beta-pruning.md) |
| 6.3 | **Heuristic alpha–beta**: H-MINIMAX with EVAL and IS-CUTOFF; weighted linear evaluation functions (material: pawn 1, knight/bishop 3, rook 5, queen 9); quiescence search, **horizon effect**, singular extensions; forward pruning (beam, PROBCUT, late move reduction); opening books and retrograde endgame tables. | [heuristic-alpha-beta](../algorithms/heuristic-alpha-beta.md) |
| 6.4 | **Monte Carlo tree search**: playouts, playout policy, selection policy; 4 steps (selection, expansion, simulation, back-propagation); **UCT / UCB1**; return most-played move. | [monte-carlo-tree-search](../algorithms/monte-carlo-tree-search.md) |
| 6.5 | **Stochastic games** (backgammon, 21 distinct rolls): chance nodes, **expectiminimax**; evaluation must be a positive linear transform of win probability (Fig 6.14); O(b^m n^m). | [expectiminimax](../algorithms/expectiminimax.md) |
| 6.6 | Partially observable games (Kriegspiel, card games): belief states, averaging over clairvoyance and its pitfalls. | [adversarial-search](../concepts/adversarial-search.md#beyond-the-basic-setting) |
| 6.7 | Limitations: evaluation errors, one move at a time, metareasoning. | same |

## Takeaways 🎯
1. Minimax is exact but exponential; alpha–beta computes the same answer with far less work, **how much less depends on move ordering**.
2. Real programs cut off search and use an **evaluation function** — which introduces the horizon effect and needs quiescence search.
3. **MCTS** replaces the evaluation function with averaged playouts; great for huge b (Go) or when no good evaluation function exists.
4. Chance nodes → **expectiminimax**: averages, not min/max; evaluation-function *scale* now matters.
