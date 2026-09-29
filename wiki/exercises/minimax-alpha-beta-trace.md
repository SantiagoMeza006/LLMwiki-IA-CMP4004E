---
title: "Exercise — Minimax and Alpha–Beta on R&N Fig 6.2"
type: exercise
unit: games-csp
sources: [slides-02-problem-solving]
updated: 2026-09-29
---

# Minimax and Alpha–Beta, Step by Step

Tree (R&N Fig 6.2, slides-02 s.19):
```
                   A (MAX)
        a1 /         | a2          \ a3
     B (MIN)       C (MIN)        D (MIN)
   b1 b2 b3      c1 c2 c3       d1 d2 d3
    3 12  8       2  4  6       14  5  2
```

## Minimax
- B = min(3, 12, 8) = **3**
- C = min(2, 4, 6) = **2**
- D = min(14, 5, 2) = **2**
- A = max(3, 2, 2) = **3** → MAX plays **a1**; MIN answers **b1**.
- Leaves evaluated: **9**.

## Alpha–beta (left-to-right)
| Step | Node | Event | α, β / interval | Prune? |
|---|---|---|---|---|
| 1 | A (MAX) | start | α = −∞, β = +∞ | |
| 2 | B (MIN) | leaf 3 | B ≤ 3 → [−∞, 3] | |
| 3 | B | leaf 12 | still ≤ 3 | |
| 4 | B | leaf 8 | B = 3 | |
| 5 | A | B returns 3 | α = 3 → A ∈ [3, +∞] | |
| 6 | C (MIN) | leaf 2 | C ≤ 2, and 2 ≤ α = 3 | ✂️ **prune c2, c3** (MAX already has 3; C can only be ≤ 2) |
| 7 | D (MIN) | leaf 14 | D ≤ 14 → A ∈ [3, 14] | no (14 > α) |
| 8 | D | leaf 5 | D ≤ 5 → A ∈ [3, 5] | no (5 > α) |
| 9 | D | leaf 2 | D = 2 → A = 3 | (no leaves left) |

Result: value **3**, move **a1** — identical to minimax. Leaves evaluated: **7** of 9 (4 and 6 pruned).

## What if D's leaves were ordered 2, 5, 14?
<details><summary>answer</summary>After leaf 2, D ≤ 2 ≤ α = 3 → prune 5 and 14 as well. Only 5 leaves evaluated. Good move ordering (best moves first) is what brings alpha–beta toward O(b^(m/2)).</details>

## Practice tree
MAX root with three MIN children: X = [5, 6, 7], Y = [4, 9, 1], Z = [8, 2, 10]. Minimax value? Which leaves are pruned by alpha–beta (left to right)?
<details><summary>answer</summary>X = 5, Y = 1, Z = 2 ⇒ root = 5 (move to X). Alpha–beta: after X, α = 5. Y's first leaf 4 ≤ 5 → prune 9 and 1. Z's first leaf 8 > 5 → continue; leaf 2 ≤ 5 → prune 10. Evaluated 6 leaves (5, 6, 7, 4, 8, 2); pruned 3 (9, 1, 10).</details>
