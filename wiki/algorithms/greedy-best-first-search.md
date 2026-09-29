---
title: Greedy Best-First Search
type: algorithm
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# Greedy Best-First Search 🎯

## Idea
Expand the node that **appears closest to the goal**: **f(n) = h(n)**. Frontier = priority queue ordered by h. "Greedy": the locally best-looking choice at each step, **ignoring accumulated cost g**.
> ⚠️ Slides-02 s.12 call this simply "Best-First Search".

## Romania trace with h_SLD (R&N Fig 3.17)
| Step | Expand | Frontier (h) |
|---|---|---|
| 0 | — | Arad 366 |
| 1 | Arad | **Sibiu 253**, Timisoara 329, Zerind 374 |
| 2 | Sibiu | **Fagaras 176**, Rimnicu Vilcea 193, Timisoara 329, Zerind 374, Arad 366, Oradea 380 |
| 3 | Fagaras | **Bucharest 0**, ... → goal |

Path **Arad → Sibiu → Fagaras → Bucharest**, cost 140 + 99 + 211 = **450**. It never expanded a node off the solution path — fast — but the optimal path (via Rimnicu Vilcea and Pitesti, **418**) is **32 miles shorter**. ⇒ **not optimal**.

## Properties
| | |
|---|---|
| Complete | Graph search: yes in **finite** spaces; not in infinite ones. Slides: "only when repeated states are controlled" (tree version can loop, e.g. Iasi → Neamt → Iasi ...) |
| Optimal | **No** |
| Time & space | worst case O(\|V\|) for graph search (O(b^m) tree-like); a good h can cut it drastically |

Can be trapped in suboptimal paths when the heuristic is misleading.

## Related variants
- **Speedy search:** greedy with h = estimated number of *actions* to the goal (ignores costs) — unbounded-cost search.
- Greedy = weighted A* with W → ∞.

See [a-star-search](a-star-search.md), [informed-search-comparison](../comparisons/informed-search-comparison.md), trace: [romania-greedy-and-a-star-trace](../exercises/romania-greedy-and-a-star-trace.md).
