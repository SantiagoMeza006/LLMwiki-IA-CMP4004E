---
title: State Space vs Search Tree, Frontier, Reached, Redundant Paths
type: concept
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# State Space vs Search Tree 🎯

| | State space (graph) | Search tree |
|---|---|---|
| Represents | the **problem**: all states and the actions linking them | the **search process**: paths explored from the initial state |
| Each state appears | **once** | possibly **many times** (reached via different paths) |
| Size | may be infinite; never built explicitly — explored progressively | may be infinite even for a finite graph (cycles) |

- **Node** (search tree) = `(STATE, PARENT, ACTION, PATH-COST)`; `g(n)` = PATH-COST. Following PARENT pointers from a goal node recovers the solution.
- **Expand** a node: apply ACTIONS, use RESULT to **generate** child (successor) nodes.
- **Frontier** 🎯: nodes generated but not yet expanded. (Some authors: *open list*.)
- **Reached**: states for which some node has been generated (frontier ∪ expanded). The **explored/closed set** = reached minus frontier.
- **Separation property:** the frontier separates the interior (expanded) from the exterior (unreached) — every path from the initial state to an unreached state passes through the frontier.

## Repeated states and redundant paths 🎯
- **Repeated state**: same state generated again. A **cycle** (loopy path, Arad→Sibiu→Arad) is a special case of a **redundant path** (a worse way to reach an already-reached state: Arad–Zerind–Oradea–Sibiu = 297 vs Arad–Sibiu = 140).
- In a 10×10 grid with 8 moves, cells are reachable in ≤ 9 moves but there are ~8^9 > 100M paths of length 9 — eliminating redundancy can speed search ~1,000,000×. "Algorithms that cannot remember the past are doomed to repeat it."
- Slides-02 s.5: **without repeated-state control the algorithm may not terminate even when a solution exists; with control each state is explored at most once.**

Three options (R&N §3.3.3):
1. **Graph search** — remember all reached states; detect every redundant path (best-first search does this). Use when the reached table fits in memory.
2. **Tree-like search** — don't check at all; saves memory; fine when paths rarely reconverge (e.g. assembly problems).
3. **Cycle checking only** — follow parent pointers to see if the state already occurs on the *current path* (no extra memory); may check only a few ancestors.

## Queues for the frontier
| Queue | Pops | Used by |
|---|---|---|
| Priority queue | minimum f(n) | [best-first search](../algorithms/best-first-search.md), UCS, greedy, A* |
| FIFO queue | oldest | [BFS](../algorithms/breadth-first-search.md) |
| LIFO queue (stack) | newest | [DFS](../algorithms/depth-first-search.md) |

Related: [search-evaluation-criteria](search-evaluation-criteria.md) · [uninformed-search-comparison](../comparisons/uninformed-search-comparison.md)
