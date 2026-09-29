---
title: Search Evaluation Criteria (Completeness, Optimality, Time, Space)
type: concept
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# Evaluating Search Algorithms 🎯

| Criterion | Question |
|---|---|
| **Completeness** | Guaranteed to find a solution when one exists, and to report failure when none does? |
| **Cost optimality** | Does it find the lowest-path-cost solution? (Some authors: "admissibility" or just "optimality".) |
| **Time complexity** | How long? (seconds, or number of states/actions considered) |
| **Space complexity** | How much memory? |

## Complexity parameters
- For explicit graphs: |V| + |E|.
- For implicit state spaces (usual in AI):
  - **b** — branching factor (max successors of a node),
  - **d** — depth of the **shallowest** / optimal solution,
  - **m** — **maximum** depth of any path (may be ∞),
  - **C\*** — cost of the optimal solution, **ε** — minimum action cost (ε > 0),
  - **ℓ** — depth limit (depth-limited search).

## Completeness subtleties
- Finite spaces: completeness just requires exploring every reachable state while cutting cycles.
- Infinite spaces need **systematic** exploration (e.g. spiral outwards on an infinite grid). Repeatedly applying factorial in Knuth's problem, or walking straight on an infinite grid, never repeats a state yet is incomplete.
- With no solution in an infinite space, a sound algorithm can never terminate.

## Useful numbers (R&N §3.4.1)
With b = 10, 1M nodes/s, 1 KB/node, BFS to d = 10 takes < 3 hours but **10 TB** of memory; d = 14 takes 3.5 years. → memory is usually the bigger problem; exponential search is hopeless for large instances without good heuristics.

See all algorithms scored on these criteria: [uninformed-search-comparison](../comparisons/uninformed-search-comparison.md), [informed-search-comparison](../comparisons/informed-search-comparison.md).
