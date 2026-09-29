---
title: "Exercise — 8-Puzzle Heuristics h1 and h2, Effective Branching Factor"
type: exercise
unit: search
sources: [rn-ch03-search, slides-02-problem-solving]
updated: 2026-09-29
---

# 8-Puzzle Heuristics (R&N Fig 3.25)

```
Start          Goal
7 2 4          _ 1 2
5 _ 6          3 4 5
8 3 1          6 7 8
```

## h1 — misplaced tiles
Every tile 1–8 is out of place ⇒ **h1 = 8**.

## h2 — sum of Manhattan distances
| Tile | Start (row,col) | Goal (row,col) | Distance |
|---|---|---|---|
| 1 | (2,2) | (0,1) | 2 + 1 = **3** |
| 2 | (0,1) | (0,2) | 0 + 1 = **1** |
| 3 | (2,1) | (1,0) | 1 + 1 = **2** |
| 4 | (0,2) | (1,1) | 1 + 1 = **2** |
| 5 | (1,0) | (1,2) | 0 + 2 = **2** |
| 6 | (1,2) | (2,0) | 1 + 2 = **3** |
| 7 | (0,0) | (2,1) | 2 + 1 = **3** |
| 8 | (2,0) | (2,2) | 0 + 2 = **2** |
| | | | **h2 = 18** |

True optimal cost = **26**. Both 8 ≤ 26 and 18 ≤ 26 ✅ admissible; h2 ≥ h1 everywhere ⇒ **h2 dominates h1** (verified in code).

## Why both are admissible
- h1: each misplaced tile needs at least one move.
- h2: each move slides one tile one square, so it reduces the total Manhattan distance by at most 1.
- Both are exact costs of **relaxed problems** (h1: a tile can jump anywhere; h2: a tile can move to any adjacent square, even if occupied) — a standard way to invent admissible heuristics (R&N §3.6.2).

## Effective branching factor
A* finds a depth-5 solution after generating N = 52 nodes. Solve `53 = 1 + b* + b*² + b*³ + b*⁴ + b*⁵` ⇒ **b\* ≈ 1.92**. (Closer to 1 = better heuristic.)

## Self-test
Compute h1 and h2 for
```
1 4 2
3 _ 5
6 7 8
```
against the same goal. <details><summary>answer</summary>Misplaced: 1 (at (0,0), goal (0,1)) and 4 (at (0,1), goal (1,1)) → h1 = 2. Manhattan: tile 1 = 1, tile 4 = 1 → h2 = 2. Optimal solution: blank Up, then blank Left (2 moves), so both heuristics are exact here.</details>
