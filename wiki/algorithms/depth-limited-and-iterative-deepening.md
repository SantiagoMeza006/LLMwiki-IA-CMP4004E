---
title: Depth-Limited Search and Iterative Deepening (IDS)
type: algorithm
unit: search
sources: [rn-ch03-search]
updated: 2026-09-29
---

# Depth-Limited Search (DLS) and Iterative Deepening Search (IDS)

(R&N §3.4.4 — not on the slides, but the natural fix for DFS.)

## Depth-limited search
- DFS with a depth limit **ℓ**: nodes at depth ℓ are treated as having no successors.
- Time **O(b^ℓ)**, space **O(b·ℓ)**. Incomplete if ℓ < d; not optimal.
- Returns one of three results: a **solution**, **failure** (no solution at all), or **cutoff** (maybe a solution deeper than ℓ).
- Choosing ℓ from domain knowledge: Romania has 20 cities → ℓ = 19 is safe; the graph's **diameter** is 9 → ℓ = 9 is better.

```
function DEPTH-LIMITED-SEARCH(problem, ℓ) returns node | failure | cutoff
    frontier ← LIFO stack [NODE(problem.INITIAL)];  result ← failure
    while not IS-EMPTY(frontier):
        node ← POP(frontier)
        if problem.IS-GOAL(node.STATE): return node
        if DEPTH(node) > ℓ: result ← cutoff
        else if not IS-CYCLE(node):
            for each child in EXPAND(problem, node): add child to frontier
    return result
```

## Iterative deepening search 🎯 (preferred uninformed method for large spaces)
```
function ITERATIVE-DEEPENING-SEARCH(problem)
    for depth = 0 to ∞:
        result ← DEPTH-LIMITED-SEARCH(problem, depth)
        if result ≠ cutoff: return result
```
Combines DFS's memory with BFS's completeness/optimality:

| | |
|---|---|
| Complete | Yes (finite b; finite acyclic spaces or with full cycle checking) |
| Optimal | Yes if all action costs are equal |
| Time | **O(b^d)** (O(b^m) if no solution) |
| Space | **O(b·d)** |

**Isn't repeating the top levels wasteful?** No — most nodes are at the bottom level.
`N(IDS) = d·b + (d−1)·b² + ... + 1·b^d`. For b = 10, d = 5: N(IDS) = 50 + 400 + 3,000 + 20,000 + 100,000 = **123,450** vs N(BFS) = 10 + 100 + 1,000 + 10,000 + 100,000 = **111,110** (only ~11% more).

Use IDS when the state space doesn't fit in memory **and** the solution depth is unknown. Informed analogue: **IDA\*** (cutoff on f instead of depth) → [memory-bounded-and-weighted-search](memory-bounded-and-weighted-search.md).
