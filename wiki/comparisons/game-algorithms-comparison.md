---
title: Game-Playing Algorithms — Comparison
type: comparison
unit: games-csp
sources: [rn-ch06-games, slides-02-problem-solving]
updated: 2026-09-30
---

# Game-Playing Algorithms — Comparison 🎯

| Algorithm | Evaluates leaves with | Exact? | Time | Best for | Page |
|---|---|---|---|---|---|
| Minimax | true UTILITY at terminals | ✅ optimal vs optimal opponent | O(b^m) | tiny games (tic-tac-toe) | [minimax](../algorithms/minimax.md) |
| Alpha–beta | UTILITY | ✅ same result as minimax | O(b^(m/2)) best, ≈ O(b^(3m/4)) random order | same, ~2× deeper | [alpha-beta-pruning](../algorithms/alpha-beta-pruning.md) |
| Heuristic alpha–beta (H-MINIMAX) | EVAL at a cutoff depth (+ quiescence) | ❌ approximate | O(b^(d/2))–O(b^d) to depth d | chess-like games with good evaluation functions (Type A) | [heuristic-alpha-beta](../algorithms/heuristic-alpha-beta.md) |
| Monte Carlo tree search | average result of playouts | ❌ converges with more playouts | linear per playout | Go (b = 361), new games, no evaluation function (Type B) | [monte-carlo-tree-search](../algorithms/monte-carlo-tree-search.md) |
| Expectiminimax | expected value at chance nodes | ✅ (full depth) | O(b^m · n^m) | dice games (backgammon) | [expectiminimax](../algorithms/expectiminimax.md) |
| Multiplayer minimax | vector of utilities | ✅ | O(b^m) | >2 players | [minimax](../algorithms/minimax.md#multiplayer-games) |
| Lookup (opening books, retrograde endgame tables) | precomputed | ✅ in the table | O(1) | openings, ≤ 7-piece endgames | [heuristic-alpha-beta](../algorithms/heuristic-alpha-beta.md#search-vs-lookup) |

## Parallels with single-agent search
| Single-agent search | Games |
|---|---|
| heuristic h(n) | evaluation function EVAL(s) |
| DFS / IDS | minimax / iterative-deepening alpha–beta |
| `reached` table (graph search) | transposition table |
| pruning with f > C* | alpha–beta pruning |
| beam search | forward pruning (Type B) |
| exploration vs exploitation | UCB1 in MCTS |

Related: [adversarial-search](../concepts/adversarial-search.md) · [games-traces](../exercises/games-traces.md)
