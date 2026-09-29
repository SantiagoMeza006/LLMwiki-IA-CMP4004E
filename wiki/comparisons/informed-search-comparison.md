---
title: Informed Search — Comparison Table
type: comparison
unit: search
sources: [rn-ch03-search, slides-02-problem-solving]
updated: 2026-09-29
---

# Informed (and cost-based) Search — Comparison 🎯

| Algorithm | f(n) | Complete? | Optimal? | Space | Notes |
|---|---|---|---|---|---|
| [Uniform-cost (Dijkstra)](../algorithms/uniform-cost-search.md) | g | Yes (costs ≥ ε) | **Yes** | O(b^(1+⌊C*/ε⌋)) | no heuristic; circular contours |
| [Greedy best-first](../algorithms/greedy-best-first-search.md) | h | finite spaces (graph search) | **No** (Romania: 450 vs 418) | O(b^m) worst | fast when h is good; misled by bad h |
| [A*](../algorithms/a-star-search.md) | g + h | Yes | **Yes if h admissible** | O(b^d) — all nodes | optimally efficient with consistent h |
| [Weighted A*](../algorithms/memory-bounded-and-weighted-search.md) | g + W·h | Yes | within W·C* | less than A* | satisficing |
| [IDA*](../algorithms/memory-bounded-and-weighted-search.md) | g + h (cutoff) | Yes | Yes (admissible h) | linear | re-expands nodes |
| [RBFS](../algorithms/memory-bounded-and-weighted-search.md) | g + h | Yes | Yes (admissible h) | linear | "changes its mind" |
| [SMA*](../algorithms/memory-bounded-and-weighted-search.md) | g + h | if goal fits in memory | if optimal reachable | all available memory | may thrash |
| [Beam](../algorithms/memory-bounded-and-weighted-search.md) | best k by f | No | No | O(k) | fast, approximate |

## The one-line summary
`f = g + W·h`: **W = 0 → UCS, W = 1 → A\*, 1 < W < ∞ → weighted A\*, W = ∞ → greedy.**

## Same Romania problem, three algorithms
| Algorithm | Path found | Cost | Nodes expanded (excluding the goal) |
|---|---|---|---|
| Greedy (h_SLD) | Arad–Sibiu–Fagaras–Bucharest | 450 | 3 (Arad, Sibiu, Fagaras) |
| A* (h_SLD) | Arad–Sibiu–RV–Pitesti–Bucharest | **418** | 5 (Arad, Sibiu, RV, Fagaras, Pitesti) |
| UCS | Arad–Sibiu–RV–Pitesti–Bucharest | **418** | more: every city with g < 418, including Zerind, Timisoara, Oradea, Lugoj, Craiova, Mehadia... |

Traces: [romania-greedy-and-a-star-trace](../exercises/romania-greedy-and-a-star-trace.md), [romania-ucs-trace](../exercises/romania-ucs-trace.md). Theory: [heuristics](../concepts/heuristics.md). Also: [a-star-vs-dijkstra](a-star-vs-dijkstra.md).
