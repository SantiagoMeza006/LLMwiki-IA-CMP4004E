---
title: Best-First Search (the generic family)
type: algorithm
unit: search
sources: [rn-ch03-search, slides-02-problem-solving]
updated: 2026-09-29
---

# Best-First Search (generic)

## Idea
Repeatedly expand the frontier node with the **minimum value of an evaluation function f(n)**. Changing f gives different algorithms (R&N §3.3.1):

| f(n) | Algorithm |
|---|---|
| depth(n) | [BFS](breadth-first-search.md) (though BFS uses a cheaper FIFO queue) |
| g(n) (path cost) | [Uniform-cost / Dijkstra](uniform-cost-search.md) |
| −depth(n) | [DFS](depth-first-search.md) (usually implemented differently) |
| h(n) | [Greedy best-first](greedy-best-first-search.md) |
| g(n) + h(n) | [A*](a-star-search.md) |
| g(n) + W·h(n), W > 1 | [Weighted A*](memory-bounded-and-weighted-search.md) |

> ⚠️ Slides-02 s.12 use "Best-First Search" to mean **greedy** best-first specifically. See [discrepancies](../discrepancies.md).

## Pseudocode (R&N Fig 3.7)
```
function BEST-FIRST-SEARCH(problem, f) returns a solution node or failure
    node ← NODE(STATE = problem.INITIAL)
    frontier ← priority queue ordered by f, containing node
    reached ← lookup table {problem.INITIAL: node}
    while not IS-EMPTY(frontier):
        node ← POP(frontier)
        if problem.IS-GOAL(node.STATE): return node          # late goal test
        for each child in EXPAND(problem, node):
            s ← child.STATE
            if s not in reached or child.PATH-COST < reached[s].PATH-COST:
                reached[s] ← child
                add child to frontier
    return failure

function EXPAND(problem, node) yields nodes
    s ← node.STATE
    for each action in problem.ACTIONS(s):
        s' ← problem.RESULT(s, action)
        cost ← node.PATH-COST + problem.ACTION-COST(s, action, s')
        yield NODE(STATE=s', PARENT=node, ACTION=action, PATH-COST=cost)
```

## Key details
- It is a **graph search**: `reached` detects redundant paths and keeps only the cheapest path to each state (re-adding a state if a cheaper path is found).
- Remove `reached` → **tree-like search** (less memory, repeats work).
- **Late goal test**: the goal is checked when a node is **popped**, not when generated — essential for optimality in UCS/A* (see [uniform-cost-search](uniform-cost-search.md)).

Related: [state-space-and-search-tree](../concepts/state-space-and-search-tree.md)
