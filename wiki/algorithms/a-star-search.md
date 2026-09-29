---
title: A* Search
type: algorithm
unit: search
sources: [slides-02-problem-solving, rn-ch03-search, note-a-star-vs-dijkstra]
updated: 2026-09-29
---

# A* Search 🎯

## Idea
[Best-first search](best-first-search.md) with
```
f(n) = g(n) + h(n)
g(n) = actual cost from the start to n
h(n) = estimated cost of the cheapest path from n to a goal
f(n) = estimated cost of the best solution that goes through n
```
Intuition (slides-02 s.14): consider not only what *looks* close to the goal (h) but the best *estimated total* cost (g + h). Frontier = priority queue ordered by f. Goal tested when **popped**.

## Romania trace (R&N Fig 3.18) — optimal cost 418
| Step | Expanded (f = g + h) | New frontier entries |
|---|---|---|
| a | Arad 366 = 0 + 366 | Sibiu 393 = 140+253, Timisoara 447 = 118+329, Zerind 449 = 75+374 |
| b | Sibiu 393 | Arad 646, **Fagaras 415** = 239+176, Oradea 671, **Rimnicu Vilcea 413** = 220+193 |
| c | Rimnicu Vilcea 413 | Craiova 526 = 366+160, **Pitesti 417** = 317+100, Sibiu 553 |
| d | Fagaras 415 | Sibiu 591, **Bucharest 450** = 450+0 (on frontier, *not* selected) |
| e | Pitesti 417 | **Bucharest 418** = 418+0, Craiova 615, Rimnicu Vilcea 607 |
| f | Bucharest 418 → **goal** ✅ | |

Solution: **Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest = 418**. Bucharest via Fagaras (450) was on the frontier first but wasn't popped because Pitesti (417) might lead to something cheaper. **Timisoara (447) and Zerind (449) were never expanded** — pruned. Step-by-step: [romania-greedy-and-a-star-trace](../exercises/romania-greedy-and-a-star-trace.md).

## Properties
| | |
|---|---|
| Complete | **Yes** (action costs ≥ ε > 0; finite space or a solution exists). ⚠️ slides-02 tie it to admissibility — R&N doesn't. |
| Optimal | **Yes if h is admissible** (tree search); with **consistent** h also as graph search without re-opening nodes |
| Time | depends on the heuristic's quality; can still be exponential in the solution length |
| Space | **O(b^d)** — keeps every node in memory ← main weakness |
| Optimally efficient | with consistent h, no algorithm using the same h and extending paths from the start expands fewer nodes (ignoring ties at f = C*) |

## Optimality proof sketch (admissible h) 🎯
Suppose A* returns cost C > C*. Some node n on an optimal path is still unexpanded, so f(n) > C* ... but f(n) = g*(n) + h(n) ≤ g*(n) + h*(n) = C* by admissibility. Contradiction.

## Contours
A* expands **all** nodes with f(n) < C*, **some** with f(n) = C*, **none** with f(n) > C*. Contours of equal f stretch from the start toward the goal (UCS contours are circles). With consistent h, f is non-decreasing along paths.

## Special cases & relatives
- h = 0 → [UCS / Dijkstra](uniform-cost-search.md) (see [a-star-vs-dijkstra](../comparisons/a-star-vs-dijkstra.md)).
- f = h → [greedy](greedy-best-first-search.md).
- f = g + W·h (W > 1) → weighted A*; IDA*, RBFS, SMA*, beam → [memory-bounded-and-weighted-search](memory-bounded-and-weighted-search.md).

## Common mistakes
- Stopping when the goal is **generated** (would return 450 instead of 418).
- Forgetting to add g — that's greedy.
- Using an **overestimating** h and still claiming optimality.

Heuristic theory: [heuristics](../concepts/heuristics.md).
