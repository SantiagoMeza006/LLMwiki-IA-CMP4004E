---
title: Breadth-First Search (BFS)
type: algorithm
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# Breadth-First Search (BFS) 🎯

## Idea
Expand the **shallowest** nodes first — level by level. Frontier = **FIFO queue**. Appropriate when all actions have the **same cost**.

## Pseudocode (R&N Fig 3.9)
```
function BREADTH-FIRST-SEARCH(problem)
    node ← NODE(problem.INITIAL)
    if problem.IS-GOAL(node.STATE): return node
    frontier ← FIFO queue [node];  reached ← {problem.INITIAL}
    while not IS-EMPTY(frontier):
        node ← POP(frontier)
        for each child in EXPAND(problem, node):
            s ← child.STATE
            if problem.IS-GOAL(s): return child            # EARLY goal test
            if s not in reached:
                add s to reached;  add child to frontier
    return failure
```
Two efficiency tricks vs generic best-first: FIFO queue instead of priority queue; `reached` is just a **set** (the first path to a state is always the shallowest) → allows an **early goal test** (on generation).

## Properties
| | |
|---|---|
| Complete | **Yes** (if b finite) — systematic, even in infinite spaces |
| Optimal | **Only if all action costs are equal** (finds fewest-steps solution) |
| Time | **O(b^d)** — 1 + b + b² + ... + b^d |
| Space | **O(b^d)** — every node stays in memory; the frontier grows exponentially |

**Memory is the killer:** b = 10, d = 10 → 10 TB (R&N). At d = 14, 3.5 years even with infinite memory.

## Common mistakes
- Claiming BFS is optimal with **varying** costs — it isn't; use [UCS](uniform-cost-search.md).
- Using the early goal test in UCS/A* (it breaks optimality there; it's only safe for BFS).

Traces: [uninformed-search-traces](../exercises/uninformed-search-traces.md). Compare: [uninformed-search-comparison](../comparisons/uninformed-search-comparison.md).
