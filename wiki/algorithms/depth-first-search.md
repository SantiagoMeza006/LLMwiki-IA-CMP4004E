---
title: Depth-First Search (DFS) and Backtracking
type: algorithm
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# Depth-First Search (DFS) 🎯

## Idea
Always expand the **deepest** node in the frontier; follow one branch to the end, then **back up** to the next deepest node with unexpanded successors. Frontier = **LIFO stack**. Usually implemented as a **tree-like search** (no `reached` table), often recursively.

## Properties
| | slides-02 s.9 | R&N §3.4.3 nuance |
|---|---|---|
| Complete | only when repeated states are controlled **and** the space is finite | complete on finite trees; on finite graphs only with cycle checking; **incomplete** in infinite spaces (can dive down an infinite path) |
| Optimal | **No** — returns the first solution found | same |
| Time | **O(b^m)** | m = max depth (can be ≫ d, or ∞) |
| Space | **O(b·m)** | frontier is a "radius" of the search sphere (BFS's is the surface) |

## Why use it?
**Memory.** Problems needing exabytes with BFS fit in kilobytes with DFS. It's the workhorse of CSPs ([backtracking](backtracking-search-csp.md)), SAT, and **logic programming** (Prolog's [SLD resolution](sld-resolution.md) is DFS — and inherits its infinite-loop problem).

## Backtracking search (variant)
Generate **one successor at a time**, modify the current state in place and **undo** on backtrack → memory O(m) actions + one state (vs O(b·m) states). Cycle checks in O(1) with a set of states on the current path.

## Common mistakes
- Saying DFS is complete in general — only in finite spaces with cycle control.
- Confusing m (max depth) with d (solution depth).

Fixes for the depth problem: [depth-limited and iterative deepening](depth-limited-and-iterative-deepening.md). Traces: [uninformed-search-traces](../exercises/uninformed-search-traces.md).
