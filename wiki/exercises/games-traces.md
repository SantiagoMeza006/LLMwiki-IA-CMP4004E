---
title: "Exercise — Evaluation functions, expectiminimax, MCTS/UCB1, multiplayer"
type: exercise
unit: games-csp
sources: [rn-ch06-games]
updated: 2026-09-30
---

# Games Traces (beyond minimax/alpha–beta)

For minimax and alpha–beta on R&N Fig 6.2 see [minimax-alpha-beta-trace](minimax-alpha-beta-trace.md).

## 1. Material evaluation
White: queen, 2 rooks, 5 pawns. Black: 2 rooks, bishop, knight, 6 pawns. EVAL = material(White) − material(Black) with P = 1, N = B = 3, R = 5, Q = 9?
<details><summary>answer</summary>White 9 + 10 + 5 = 24. Black 10 + 3 + 3 + 6 = 22. EVAL = +2 (White up two pawns' worth) — but only trust it in a **quiescent** position.</details>

## 2. Expected value of a category
A category of positions: 60% win (1), 10% loss (0), 30% draw (½). Expected value?
<details><summary>answer</summary>0.6 + 0 + 0.15 = 0.75.</details>

## 3. Expectiminimax (R&N Fig 6.14)
MAX: a1 → chance(0.9: MIN value 2, 0.1: MIN value 3); a2 → chance(0.9: 1, 0.1: 4).
<details><summary>answer</summary>a1 = 2.1, a2 = 1.3 → a1. Rescale leaves to 20, 30, 1, 400 (same order): a1 = 21, a2 = 40.9 → a2. Lesson: with chance nodes the evaluation must be a positive linear transform of win probability.</details>

## 4. Your own chance tree
MAX chooses L or R. L → coin flip: heads (½) → MIN chooses min(3, 9); tails (½) → MIN chooses min(8, 5). R → die event: P = ⅓ → 4, P = ⅔ → 6 (terminal). Value and move?
<details><summary>answer</summary>L: ½·3 + ½·5 = 4. R: ⅓·4 + ⅔·6 = 16/3 ≈ 5.33. MAX plays **R**.</details>

## 5. UCB1 (R&N Fig 6.10, parent has 100 playouts)
Children 60/79, 1/10, 2/11. Which is selected with C = 1.4? With C = 1.5?
<details><summary>answer</summary>C = 1.4: 1.098, 1.050, 1.088 → 60/79 (exploitation). C = 1.5: 1.122, 1.118, 1.152 → 2/11 (exploration). Verified in code.</details>

## 6. MCTS back-propagation
Path root(white just moved, 37/100) → black node 60/79 → white node 16/53 → black leaf 27/35 → new child 0/0. The playout is a **black** win. New counts?
<details><summary>answer</summary>Black nodes gain a win and a playout: 27/35 → 28/36, 60/79 → 61/80. White nodes gain only a playout: 16/53 → 16/54, root 37/100 → 37/101, and the new child (a white node, since levels alternate) 0/0 → **0/1** — exactly R&N Fig 6.10(c). Each node counts wins for the player who moved into it.</details>

## 7. Which move does MCTS return?
Root children after the time budget: A = 65/100, B = 2/3, C = 30/50.
<details><summary>answer</summary>A — the **most played** move (65/100 = 0.65). B's 0.67 is based on 3 playouts only.</details>

## 8. Horizon effect — spot it
Your program, searching 6 ply, keeps playing checks that sacrifice pawns whenever its knight is trapped. What's happening and what helps?
<details><summary>answer</summary>Horizon effect: the delaying checks push the unavoidable knight capture beyond ply 6, so the search thinks it's saved. Mitigations: singular extensions, quiescence search, deeper search.</details>

## 9. Multiplayer
Player B chooses between ⟨vA, vB, vC⟩ = ⟨4, 2, 3⟩ and ⟨1, 5, 2⟩. Which vector is backed up?
<details><summary>answer</summary>⟨1, 5, 2⟩ — B maximises its own component (5 > 2).</details>
