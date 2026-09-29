---
title: Weighted A*, Beam Search, IDA*, RBFS, SMA*
type: algorithm
unit: search
sources: [rn-ch03-search]
updated: 2026-09-29
---

# Satisficing and Memory-Bounded Heuristic Search

(R&N §3.5.4–3.5.5 — beyond the slides; good for "why not always A*?" questions.)

## Weighted A* — trade optimality for speed
- `f(n) = g(n) + W·h(n)`, W > 1 → **inadmissible**-style but focused search. Finds a cost between C* and W·C* (in practice close to C*). R&N Fig 3.21: W = 2 explored **7× fewer** states for a path **5%** costlier.
- Everything is weighted A*:

| Algorithm | f | W |
|---|---|---|
| Uniform-cost | g | 0 |
| A* | g + h | 1 |
| Weighted A* | g + W·h | 1 < W < ∞ |
| Greedy best-first | h | ∞ |

- **Satisficing** = "good enough". **Bounded suboptimal** (within factor W), **bounded-cost** (cost < C), **unbounded-cost** (any cost, fast — e.g. *speedy search*).
- *Detour index*: road distance ≈ 1.2–1.6 × straight-line distance.

## Beam search
Keep only the **k best** nodes on the frontier (or all within δ of the best). Fast, memory-bounded, **incomplete and suboptimal**.

## IDA* (iterative-deepening A*)
Like IDS but the cutoff is **f = g + h**; each iteration's new cutoff = smallest f that exceeded the previous one. Linear memory; great when f-values are integers (8-puzzle: ≤ 31 iterations); poor when every node has a distinct f.

## RBFS (recursive best-first search)
Recursive DFS that tracks `f_limit` = best alternative from any ancestor; unwinds when exceeded and stores the **backed-up value** (best f of the forgotten subtree). Linear space; optimal with admissible h; "changes its mind" often → re-expansions.

## SMA* (simplified memory-bounded A*)
Runs A* until memory is full, then **drops the worst leaf** (highest f) and backs its value up to the parent. Complete if the shallowest goal fits in memory; optimal if an optimal solution is reachable. Can **thrash** on hard problems.

Related: [a-star-search](a-star-search.md) · [informed-search-comparison](../comparisons/informed-search-comparison.md)
