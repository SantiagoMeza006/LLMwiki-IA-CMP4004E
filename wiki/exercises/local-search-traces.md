---
title: "Exercise — Hill climbing on 8-queens, simulated annealing, random restarts, GA fitness"
type: exercise
unit: optimization
sources: [rn-ch04-complex-environments]
updated: 2026-09-30
---

# Local Search Traces

8-queens encoding (R&N): an 8-digit string, digit c = row (1 = bottom) of the queen in column c. h = number of attacking pairs (same row or diagonal; column clashes impossible). Non-attacking pairs = 28 − h. All numbers verified in code.

## 1. Evaluate states
| State | h (attacking) | fitness (non-attacking) |
|---|---|---|
| 24748552 | 4 | 24 |
| 32752411 | 5 | 23 |
| 24415124 | 8 | 20 |
| 32543213 | 17 | 11 |

(These are R&N Fig 4.6's population; fitness-proportional selection probabilities 31%, 29%, 26%, 14%.)

## 2. Steepest-descent hill climbing from 32543213
56 successors (move one queen within its column); the best has h = 11 (a unique best here). One run, ties broken by lowest column then lowest row:
| Step | State | h |
|---|---|---|
| 0 | 32543213 | 17 |
| 1 | 32548213 | 11 |
| 2 | 32748213 | 7 |
| 3 | 32758213 | 4 |
| 4 | 62758213 | 2 |
| 5 | 64758213 | **1** — no successor improves → **stuck in a local minimum** |

Exactly R&N's story: rapid progress from a bad state, then stuck one conflict short. Fixes: sideways moves, random restart, simulated annealing.

## 3. Random restarts — expected cost
Each hill-climbing run succeeds with p = 0.14, taking 4 steps on success and 3 on failure. Expected runs and steps?
<details><summary>answer</summary>Runs = 1/p ≈ 7 (6 failures + 1 success). Steps ≈ 4 + (1 − p)/p · 3 = 4 + 6.14·3 ≈ 22. With sideways moves: p = 0.94, 21 steps success, 64 failure → 1/0.94 ≈ 1.06 runs, 21 + (0.06/0.94)·64 ≈ 25 steps.</details>

## 4. Simulated annealing acceptance
Current cost 10, proposed neighbour cost 12 (ΔE = −2 in the cost-minimisation form). Probability of accepting at T = 10, T = 1? What if the neighbour has cost 9?
<details><summary>answer</summary>e^(−2/10) = 0.819; e^(−2/1) = 0.135. A better neighbour (cost 9) is **always** accepted.</details>

At T = 5, compare ΔE = −1 and ΔE = −5. <details><summary>answer</summary>0.819 vs 0.368 — worse moves are less likely, and all bad moves get rarer as T falls.</details>

## 5. Local beam vs random restarts
k = 4 beams vs 4 independent restarts on 8-queens — what's different? <details><summary>answer</summary>Beam search pools all successors of the 4 states and keeps the best 4 overall, so effort concentrates where progress is (information sharing); restarts never interact. Beam search risks losing diversity (all 4 in one region) — stochastic beam search picks successors with probability ∝ value.</details>

## 6. Gradient step
f(x) = −(x − 3)², x = 0, α = 0.25. One gradient-ascent step? Newton step?
<details><summary>answer</summary>f′(x) = −2(x − 3) = 6 at x = 0 → x ← 0 + 0.25·6 = 1.5. Newton: f″ = −2 → x ← x − f′/f″ = 0 − 6/(−2) = 3 (the maximum in one step, since f is quadratic).</details>
