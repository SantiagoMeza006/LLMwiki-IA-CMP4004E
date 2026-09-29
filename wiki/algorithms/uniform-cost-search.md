---
title: Uniform-Cost Search (Dijkstra's Algorithm)
type: algorithm
unit: search
sources: [rn-ch03-search, note-a-star-vs-dijkstra]
updated: 2026-09-29
---

# Uniform-Cost Search (UCS) = Dijkstra's Algorithm

## Idea
[Best-first search](best-first-search.md) with **f(n) = g(n)** (path cost from the root). AI calls it *uniform-cost search*; theoretical CS calls it *Dijkstra's algorithm*. BFS spreads in waves of uniform **depth**; UCS spreads in waves of uniform **path cost**.
`UNIFORM-COST-SEARCH(problem) = BEST-FIRST-SEARCH(problem, PATH-COST)`.

## Why the goal test must be late (R&N Fig 3.10) 🎯
Sibiu → Bucharest:
1. Expand Sibiu → Rimnicu Vilcea (80), Fagaras (99).
2. Expand RV (80) → Pitesti (80+97 = **177**).
3. Expand Fagaras (99) → Bucharest (99+211 = **310**) — generated, but **not yet tested**.
4. Expand Pitesti (177) → Bucharest (177+101 = **278**) — cheaper, replaces 310 in `reached`.
5. Pop Bucharest (278) → goal ✅.

Testing on generation would have returned the 310 path via Fagaras. Full trace: [romania-ucs-trace](../exercises/romania-ucs-trace.md).

## Properties
| | |
|---|---|
| Complete | **Yes**, if every action cost ≥ ε > 0 (and b finite) |
| Optimal | **Yes** — the first solution popped costs no more than anything on the frontier |
| Time & space | **O(b^(1 + ⌊C*/ε⌋))** — can be much worse than b^d when there are many cheap actions; = O(b^(d+1)) if all costs equal |

## Relation to A*
UCS is [A*](a-star-search.md) with **h(n) = 0** (weighted A* with W = 0). It has "circular" contours around the start; A* stretches them toward the goal. See [a-star-vs-dijkstra](../comparisons/a-star-vs-dijkstra.md).
