---
title: Bidirectional Search
type: algorithm
unit: search
sources: [rn-ch03-search]
updated: 2026-09-29
---

# Bidirectional Search

(R&N §3.4.5 and §3.5.6 — not on the slides.)

## Idea
Search **forward from the start** and **backward from the goal(s)** simultaneously; stop when the frontiers meet. Motivation: **b^(d/2) + b^(d/2) ≪ b^d** (50,000× fewer nodes when b = d = 10).

## Requirements
- Two frontiers and two `reached` tables.
- Ability to reason **backwards**: know the predecessors of a state (if s' is a successor of s forward, s must be a successor of s' backward).
- Joining two half-paths when a state is reached from both sides (`JOIN-NODES`); the first joined solution is not necessarily optimal, so keep the best and use a `TERMINATED` test.

## Versions
- **Bidirectional uniform-cost** (f = path cost): never expands a node with g > C*/2.
- **Bidirectional best-first** with f2(n) = **max(2g(n), g(n) + h(n))** (heuristic version): never expands a node with g > C*/2 ("meet in the middle"); **complete and optimal** with admissible h.
- **Front-to-end** heuristics estimate distance to the goal/start; **front-to-front** estimate distance to the other frontier.

## Properties (Fig 3.15)
Complete and optimal **if both directions are BFS or UCS**; time and space **O(b^(d/2))**.
With a very good heuristic, A* alone is already focused and bidirectional adds little; with an average heuristic, meet-in-the-middle tends to expand fewer nodes.

Related: [uninformed-search-comparison](../comparisons/uninformed-search-comparison.md)
