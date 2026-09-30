---
title: "Slides 02 — Problem Solving"
type: source
unit: search
raw: "raw/02_Problem Solving.pptx"
sources: [slides-02-problem-solving]
updated: 2026-09-29
---

# Slides 02 — Problem Solving

25 slides · Raw: `raw/02_Problem Solving.pptx` · Many slides are figures copied from R&N (Romania map, search trees, minimax/alpha-beta trees, pseudocode).

## What it covers (slide by slide)

| Slide | Topic | Wiki page |
|---|---|---|
| 2 | 🎯 Problem-solving agent = goal-based agent that plans a *sequence* of actions; formulate → search → execute; assumes observable, deterministic, discrete, static env. | [search-problem-formulation](../concepts/search-problem-formulation.md) |
| 3 | 🎯 Problem formulation: initial state, actions, transition model `Result(s,a) → s'`, goal test, cost function → define the **state space**. | same |
| 4 | State space as a graph (nodes = states, edges = actions with cost); never built explicitly. | [state-space-and-search-tree](../concepts/state-space-and-search-tree.md) |
| 5 | 🎯 Repeated states: state graph vs search tree; **frontier** + **explored set**; without repeated-state control the search may not terminate. | same |
| 6 | 🎯 Uninformed search + the 4 evaluation criteria (completeness, optimality, time, space). | [search-evaluation-criteria](../concepts/search-evaluation-criteria.md) |
| 7–8 | 🎯 BFS: FIFO queue, complete, optimal with uniform costs, O(b^d) time and space. | [breadth-first-search](../algorithms/breadth-first-search.md) |
| 9–10 | 🎯 DFS: LIFO stack, complete only with repeated-state control in finite spaces, not optimal, O(b^m) time, O(b·m) space. | [depth-first-search](../algorithms/depth-first-search.md) |
| 11 | 🎯 Informed search, heuristic h(n): estimate to goal, h(goal)=0, h ≥ 0. | [heuristics](../concepts/heuristics.md) |
| 12–13 | "Best-First Search" = greedy: priority queue by h(n), not optimal. ⚠️ naming | [greedy-best-first-search](../algorithms/greedy-best-first-search.md) |
| 14–15 | 🎯 A*: priority queue by f(n)=g(n)+h(n); optimal if h admissible/consistent; O(b^d) space. Figures: A* on Romania. | [a-star-search](../algorithms/a-star-search.md) |
| 16 | 🎯 Properties of heuristics: **admissibility**, **dominance** (h2(n) ≥ h1(n) ∀n, both admissible), **consistency** h(n) ≤ c(n,a,n') + h(n') (triangle inequality figure). | [heuristics](../concepts/heuristics.md) |
| 17 | Adversarial search: MAX vs MIN, zero-sum, perfect information, deterministic. | [adversarial-search](../concepts/adversarial-search.md) |
| 18–19 | 🎯 Minimax: recursive definition, O(b^m) time, O(b·m) space; R&N Fig 6.2 tree and Fig 6.3 pseudocode. | [minimax](../algorithms/minimax.md) |
| 20–22 | 🎯 Alpha–beta: α = best for MAX (lower bound), β = best for MIN (upper bound); same answer as minimax; best case O(b^(m/2)). R&N Fig 6.5 step-by-step. | [alpha-beta-pruning](../algorithms/alpha-beta-pruning.md) |
| 23–24 | 🎯 CSPs: variables X, domains D, constraints C; consistent + complete assignment; constraint propagation (forward checking, arc consistency, MRV). Examples: Sudoku, school timetable. | [constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md) |
| 25 | BACKTRACKING-SEARCH pseudocode (R&N Fig 5.5). | [backtracking-search-csp](../algorithms/backtracking-search-csp.md) |

## Where it fits
Units **search** and **games-csp**. Textbook companions: [R&N Ch 3](rn-ch03-search.md) (search), [R&N Ch 5](rn-ch05-csp.md) (CSPs), [R&N Ch 6](rn-ch06-games.md) (games) — the slide figures (Figs 5.5, 6.2, 6.3, 6.5) come from these chapters.

> ⚠️ **Naming (slide 12):** the slide titles greedy search "Best-First Search". In R&N, *best-first search* is the **generic family** (expand the node with minimum f(n)); *greedy best-first* is the member with f(n)=h(n). Know both usages.
>
> ⚠️ **A\* completeness (slide 14):** the slide says A* is complete "if h is admissible". In R&N, A* is complete regardless of admissibility (given positive action costs and a finite space or an existing solution); admissibility is what gives **optimality**.
