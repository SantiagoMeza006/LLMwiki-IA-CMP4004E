---
title: Heuristic Alpha–Beta (Evaluation Functions, Cutoff, Quiescence, Horizon Effect)
type: algorithm
unit: games-csp
sources: [rn-ch06-games]
updated: 2026-09-30
---

# Heuristic Alpha–Beta Tree Search

(R&N §6.3.) Even [alpha–beta](alpha-beta-pruning.md) can't reach terminal states in chess (35⁸⁰ ≈ 10¹²³ states). **Cut off** the search early and **estimate** the value of non-terminal states — Shannon's **Type A** strategy (wide but shallow). Type B (deep but narrow, forward pruning) is the other option; MCTS is its modern form.

## H-MINIMAX
Replace UTILITY by **EVAL** and IS-TERMINAL by **IS-CUTOFF**:
```
H-MINIMAX(s, d) = EVAL(s, MAX)                                     if IS-CUTOFF(s, d)
                = max_a H-MINIMAX(RESULT(s, a), d + 1)            if TO-MOVE(s) = MAX
                = min_a H-MINIMAX(RESULT(s, a), d + 1)            if TO-MOVE(s) = MIN
```
In ALPHA-BETA-SEARCH replace the IS-TERMINAL line with
`if game.IS-CUTOFF(state, depth) then return game.EVAL(state, player), null`.

## Evaluation functions
- Must equal UTILITY on terminal states, lie between loss and win otherwise, be **fast**, and be **strongly correlated with the chances of winning**.
- Conceptually: expected value over a category of states — e.g. two-pawns-vs-one-pawn endgames win 82%, lose 2%, draw 16% → 0.82·1 + 0.02·0 + 0.16·½ = **0.90**.
- In practice a **weighted linear function** `EVAL(s) = w1·f1(s) + w2·f2(s) + … + wn·fn(s)`. Chess material values: **pawn 1, knight/bishop 3, rook 5, queen 9**; features like pawn structure or king safety ≈ ½ pawn.
- Linearity assumes features are independent — real programs use nonlinear combinations (a bishop pair is worth more than 2 bishops; bishops are worth more in the endgame). Weights can be **learned** (ML confirmed a bishop ≈ 3 pawns).
- Only the **order** of values matters for deterministic games (not for games of chance → [expectiminimax](expectiminimax.md)).

## Cutting off search
- Fixed depth limit, or better **iterative deepening** until time runs out (and reuse the transposition table / move ordering from previous iterations).
- **Quiescence search:** only apply EVAL to **quiescent** positions (no pending capture that would swing the value); otherwise keep searching (often only captures).
- **Horizon effect** 🎯: an unavoidable loss is pushed beyond the search depth by delaying moves (e.g. sacrificing pawns to postpone the capture of a doomed bishop), so the program thinks it avoided it. Mitigation: **singular extensions** (keep searching a move that is clearly better than all others).

## Forward pruning (Type B)
Prune moves that *look* bad (risk of error): beam search over moves, **PROBCUT** (prune nodes *probably* outside [α, β], using statistics — beat plain alpha–beta 64% of the time with half the time), **late move reduction** (search late-ordered moves less deeply).

## Search vs lookup
- **Opening books** (from human expertise and game databases) for the first ~10–15 moves.
- **Endgame tables** by **retrograde minimax** (work backwards from checkmates): all endings with ≤ 7 pieces are solved (400 trillion positions).

## What it buys (R&N numbers)
~1 million nodes/s: minimax ≈ 5 ply (novice level) → alpha–beta + big transposition table ≈ 14 ply (expert) → STOCKFISH-class programs reach depth 30+.

Related: [minimax](minimax.md) · [heuristics](../concepts/heuristics.md) (h in search ↔ EVAL in games) · [game-algorithms-comparison](../comparisons/game-algorithms-comparison.md)
