---
title: Uninformed Search — Comparison Table
type: comparison
unit: search
sources: [rn-ch03-search, slides-02-problem-solving]
updated: 2026-09-29
---

# Uninformed Search — Comparison 🎯

R&N Fig 3.15 (tree-like versions, no repeated-state checking):

| Criterion | [BFS](../algorithms/breadth-first-search.md) | [Uniform-cost](../algorithms/uniform-cost-search.md) | [DFS](../algorithms/depth-first-search.md) | [Depth-limited](../algorithms/depth-limited-and-iterative-deepening.md) | [Iterative deepening](../algorithms/depth-limited-and-iterative-deepening.md) | [Bidirectional](../algorithms/bidirectional-search.md) |
|---|---|---|---|---|---|---|
| Complete? | Yes¹ | Yes¹˒² | No | No | Yes¹ | Yes¹˒⁴ |
| Cost-optimal? | Yes³ | Yes | No | No | Yes³ | Yes³˒⁴ |
| Time | O(b^d) | O(b^(1+⌊C*/ε⌋)) | O(b^m) | O(b^ℓ) | O(b^d) | O(b^(d/2)) |
| Space | O(b^d) | O(b^(1+⌊C*/ε⌋)) | O(b·m) | O(b·ℓ) | O(b·d) | O(b^(d/2)) |
| Frontier | FIFO queue | priority queue on g | LIFO stack | stack + limit | stack, repeated | two frontiers |

Footnotes: ¹ complete if b is finite and the space has a solution or is finite · ² complete if all action costs ≥ ε > 0 · ³ cost-optimal if all action costs are identical · ⁴ if both directions are BFS or UCS.
b = branching factor · d = depth of shallowest solution · m = max depth · ℓ = depth limit · C* = optimal cost · ε = min action cost.

**Graph-search versions** (with `reached`): DFS becomes complete in **finite** spaces, and time/space are bounded by |V| + |E|.

## Slides-02 wording (what the exam will likely use)
- BFS: complete; optimal (fewest steps, uniform costs); O(b^d) time and space; frontier grows exponentially.
- DFS: complete only with repeated-state control and a finite space; not optimal; O(b^m) time; O(b·m) space; low memory vs BFS.

## Rules of thumb
- Uniform costs, enough memory → BFS. Varying costs → UCS.
- Large space, unknown depth → **iterative deepening** (the preferred uninformed method).
- Tiny memory, deep solutions, finite tree → DFS / backtracking.
- Can search backwards and goal is explicit → bidirectional.

See also: [informed-search-comparison](informed-search-comparison.md), [search-evaluation-criteria](../concepts/search-evaluation-criteria.md).
