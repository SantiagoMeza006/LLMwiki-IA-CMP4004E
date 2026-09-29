---
title: Heuristic Functions (Admissibility, Consistency, Dominance)
type: concept
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# Heuristic Functions

## Definition 🎯
`h(n)` = **estimated** cost of the cheapest path from the state at node n to a goal (R&N §3.5).
Slides-02 s.11: h(n) = 0 if n is a goal; h(n) ≥ 0 always. A heuristic is an *estimate*, not a guarantee; a good one dramatically reduces nodes explored.
It encodes **domain knowledge** that is *not* derivable from ACTIONS/RESULT (e.g. straight-line distance h_SLD needs map coordinates).

## Properties 🎯 (slides-02 s.16)
| Property | Definition | Consequence |
|---|---|---|
| **Admissible** | never **overestimates**: h(n) ≤ h\*(n) (true cost to goal) for all n. "Optimistic." | [A*](../algorithms/a-star-search.md) (tree search, and graph search that re-opens nodes) is **cost-optimal**. |
| **Consistent** (monotone) | for every n and successor n' via action a: **h(n) ≤ c(n, a, n') + h(n')** — the triangle inequality. | Consistent ⇒ admissible (not vice-versa). f is non-decreasing along any path; the first time A* reaches a state it's via an optimal path, so no node is re-added. A* with consistent h is **optimally efficient**. |
| **Dominance** | h2 **dominates** h1 if h2(n) ≥ h1(n) for all n and both are admissible. | A* with h2 never expands more nodes than with h1 (it's more informed). Prefer the larger admissible heuristic (if it's not too costly to compute). |

- h_SLD (straight-line distance to Bucharest) is admissible **and** consistent.
- "Monotonic heuristic" = consistent (Pearl 1984 proved the two ideas equivalent).
- Inadmissible heuristics can still give optimal answers in special cases (overestimate by less than C₂ − C\*), and are used on purpose in **weighted A\*** → [memory-bounded-and-weighted-search](../algorithms/memory-bounded-and-weighted-search.md).

## h_SLD to Bucharest (R&N Fig 3.16)
| City | h | City | h | City | h | City | h |
|---|---|---|---|---|---|---|---|
| Arad | 366 | Eforie | 161 | Lugoj | 244 | Rimnicu Vilcea | 193 |
| Bucharest | 0 | Fagaras | 176 | Mehadia | 241 | Sibiu | 253 |
| Craiova | 160 | Giurgiu | 77 | Neamt | 234 | Timisoara | 329 |
| Drobeta | 242 | Hirsova | 151 | Oradea | 380 | Urziceni | 80 |
| Iasi | 226 | Pitesti | 100 | Vaslui | 199 | Zerind | 374 |

## 8-puzzle heuristics (R&N §3.6)
- **h1 = number of misplaced tiles** (blank excluded). Admissible: each misplaced tile needs ≥ 1 move.
- **h2 = sum of Manhattan (city-block) distances** of tiles to their goal squares. Admissible: each move moves one tile one step.
- h2 **dominates** h1. On R&N Fig 3.25: h1 = 8, h2 = 18, true cost = 26. Worked: [8-puzzle-heuristics](../exercises/8-puzzle-heuristics.md).

## Measuring heuristic quality
- **Effective branching factor b\***: if A* generates N nodes for a solution at depth d, b\* satisfies `N + 1 = 1 + b* + (b*)² + ... + (b*)^d`. Example: N = 52, d = 5 → b\* ≈ 1.92. Good heuristics have b\* close to 1.
- Korf & Reid: a heuristic reduces the **effective depth** by a constant k_h → cost O(b^(d−k_h)) instead of O(b^d).

Related: [a-star-search](../algorithms/a-star-search.md) · [greedy-best-first-search](../algorithms/greedy-best-first-search.md) · [informed-search-comparison](../comparisons/informed-search-comparison.md)
