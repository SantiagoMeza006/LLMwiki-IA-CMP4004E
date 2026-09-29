---
title: Example Search Problems
type: concept
unit: search
sources: [rn-ch03-search]
updated: 2026-09-29
---

# Example Search Problems (R&N §3.2)

**Standardized problems** are concise benchmarks; **real-world problems** are idiosyncratic.

## Vacuum world as a grid world
- States: agent location × dirt in each cell → 2 × 2 × 2 = **8** states for 2 cells; **n · 2^n** for n cells.
- Actions: Suck, Left, Right (in 2-D: Up/Down or egocentric Forward/Backward/TurnLeft/TurnRight).
- Goal: all cells clean. Cost: 1 per action.

## Sokoban
Push boxes to storage cells; can't push into a box or wall. n non-obstacle cells, b boxes → n · n!/(b!(n−b)!) states (8×8 with a dozen boxes > 200 trillion).

## 8-puzzle (sliding tiles) 🎯
- States: position of each tile. Actions: move the **blank** Left/Right/Up/Down. Cost 1 each.
- A parity property splits the space: any goal is reachable from exactly **half** the initial states → 9!/2 = **181,440** reachable states. 15-puzzle: 16!/2 > 10 trillion.
- Used for [heuristics](heuristics.md) h1/h2 — see [8-puzzle-heuristics](../exercises/8-puzzle-heuristics.md).

## Knuth's "4" problem — infinite state space
Start at 4; operators √, floor, factorial; Knuth conjectured any positive integer is reachable. ⌊√√√√√(4!)!⌋ = 5; the path passes through (4!)! ≈ 6.2 × 10^23. Infinite spaces arise with expressions, circuits, proofs, programs.

## Route finding — Romania 🎯
20 cities, roads with distances in **miles** (R&N Fig 3.1). Arad → Bucharest; the classic test bed for [UCS](../algorithms/uniform-cost-search.md), [greedy](../algorithms/greedy-best-first-search.md) and [A*](../algorithms/a-star-search.md). Diameter of the graph = 9 (any city reachable from any other in ≤ 9 actions).

Key edges used in traces: Arad–Sibiu 140, Arad–Timisoara 118, Arad–Zerind 75, Sibiu–Fagaras 99, Sibiu–Rimnicu Vilcea 80, Sibiu–Oradea 151, Fagaras–Bucharest 211, Rimnicu Vilcea–Pitesti 97, Rimnicu Vilcea–Craiova 146, Pitesti–Bucharest 101, Pitesti–Craiova 138, Zerind–Oradea 71.

## Real-world
- **Airline travel:** state = airport + time + fare history; costs combine price, waiting, flight time, etc.
- **Touring problems / TSP:** visit every city; NP-hard; also the benchmark for [ACO](../algorithms/ant-colony-optimization.md). (Boston school buses: $5M saved.)
- **VLSI layout** (cell layout + channel routing), **robot navigation** (continuous, many-dimensional), **automatic assembly sequencing**, **protein design**.

Related: [search-problem-formulation](search-problem-formulation.md)
