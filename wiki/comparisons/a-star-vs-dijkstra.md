---
title: A* vs Dijkstra (Uniform-Cost Search)
type: comparison
unit: search
sources: [note-a-star-vs-dijkstra, rn-ch03-search]
updated: 2026-09-29
---

# A* vs Dijkstra

Filed from my homework note ([source](../sources/note-a-star-vs-dijkstra.md)) and checked against R&N.

| | Dijkstra / UCS | A* |
|---|---|---|
| Evaluation | f(n) = g(n) | f(n) = g(n) + h(n) |
| Knowledge of the goal | none (h = 0) | heuristic estimate (h_SLD) |
| Contours | circles of equal g around the start | ellipses of equal g+h stretched toward the goal |
| Optimal? | yes (costs > 0) | yes if h admissible |
| Romania Arad→Bucharest | 418 via Sibiu, RV, Pitesti | 418 via the same path |
| Work | expands every node with g < 418 (incl. Zerind, Timisoara, Oradea, Lugoj...) | expands only nodes with f < 418 (Arad, Sibiu, RV, Fagaras, Pitesti); **never** expands Timisoara (447) or Zerind (449) |
| Relationship | special case of A* with h(n) = 0 | generalisation |

## Conclusion
For this problem A* is better: **same optimal solution, fewer node expansions**, because h_SLD is informative and admissible/consistent. With h = 0, A* degenerates into Dijkstra; with a *better* admissible h (one that dominates h_SLD), A* would expand even fewer nodes.

> ⚠️ Units: R&N's Romania distances are in **miles**, not km (my note said 418 km).

Related: [a-star-search](../algorithms/a-star-search.md) · [uniform-cost-search](../algorithms/uniform-cost-search.md) · [informed-search-comparison](informed-search-comparison.md)
