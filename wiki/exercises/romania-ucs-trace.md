---
title: "Exercise — Uniform-Cost Search on Romania (Arad → Bucharest)"
type: exercise
unit: search
sources: [rn-ch03-search]
updated: 2026-09-29
---

# Uniform-Cost Search (Dijkstra) — Arad → Bucharest

Graph search, f = g, **late goal test**. Edge costs from R&N Fig 3.1 (see [example-search-problems](../concepts/example-search-problems.md)). Verified by running the algorithm in code.

## Expansion order
| # | Pop (g) | New or improved frontier entries (g) |
|---|---|---|
| 1 | Arad 0 | Zerind 75, Timisoara 118, Sibiu 140 |
| 2 | Zerind 75 | Oradea 146 (75+71) |
| 3 | Timisoara 118 | Lugoj 229 (118+111) |
| 4 | Sibiu 140 | Fagaras 239, Rimnicu Vilcea 220 (Oradea via Sibiu = 291 > 146, ignored) |
| 5 | Oradea 146 | — (Sibiu already cheaper) |
| 6 | Rimnicu Vilcea 220 | Pitesti 317, Craiova 366 |
| 7 | Lugoj 229 | Mehadia 299 |
| 8 | Fagaras 239 | **Bucharest 450** (generated, not tested!) |
| 9 | Mehadia 299 | Drobeta 374 |
| 10 | Pitesti 317 | **Bucharest 418** replaces 450 (Craiova via Pitesti 455 > 366) |
| 11 | Craiova 366 | (Drobeta via Craiova 486 > 374) |
| 12 | Drobeta 374 | — |
| 13 | **Bucharest 418 → goal** ✅ | |

**Solution:** Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest, **cost 418**. 12 nodes expanded before the goal.

## Lessons
- With an **early** goal test at step 8 we'd return 450 (via Fagaras) — wrong.
- UCS expands everything with g < 418 in *every* direction (Zerind, Timisoara, Lugoj, Mehadia, Drobeta...) because it has no idea where Bucharest is. Compare [A*](romania-greedy-and-a-star-trace.md), which expands only 5.
