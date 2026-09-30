---
title: Hill Climbing (and its variants)
type: algorithm
unit: optimization
sources: [rn-ch04-complex-environments, holland-1992-genetic-algorithms]
updated: 2026-09-30
---

# Hill Climbing 🎯

## Idea
Keep **one current state**; repeatedly move to the **best neighbour** (steepest ascent); stop when no neighbour is better. "Like climbing Everest in thick fog with amnesia" (R&N §4.1.1). Also called **greedy local search**. With a cost h (to minimise), climb on −h.

## Pseudocode (R&N Fig 4.2)
```
function HILL-CLIMBING(problem) returns a state that is a local maximum
    current ← problem.INITIAL
    while true:
        neighbor ← a highest-valued successor state of current
        if VALUE(neighbor) ≤ VALUE(current): return current
        current ← neighbor
```

## 8-queens example (R&N)
- Complete-state formulation: one queen per column; successors = move one queen within its column → 8 × 7 = **56 successors**.
- Cost **h = number of attacking pairs** (0 = solution); 8⁸ ≈ 17 million states.
- From random starts, steepest ascent **solves 14%** (≈ 4 steps) and **gets stuck 86%** (≈ 3 steps).
- Allow up to 100 consecutive **sideways moves** → **94%** solved (≈ 21 steps success, 64 failure).

## Why it gets stuck
**Local maxima**, **ridges**, **plateaus** (flat maxima or shoulders) — see [local-search](../concepts/local-search.md#the-state-space-landscape).

## Variants
| Variant | Rule | Note |
|---|---|---|
| Steepest ascent | best neighbour | basic version |
| **Sideways moves** | allow equal-value moves (limited count) | escapes shoulders |
| **Stochastic HC** | random uphill move, probability ∝ steepness | slower, sometimes better optima |
| **First-choice HC** | generate random successors until one is better | good when there are thousands of successors |
| **Random-restart HC** | run HC from random initial states until a goal is found | **complete with probability 1**; expected restarts = **1/p**. 8-queens: p ≈ 0.14 → ~7 runs, ~22 steps; with sideways moves ~1.06 runs, ~25 steps. Solves 3 million queens in seconds. |

## Properties
| | |
|---|---|
| Complete | No (random-restart: with probability 1) |
| Optimal | No — returns a local optimum |
| Time | fast on easy landscapes; NP-hard problems have exponentially many local maxima |
| Space | O(1) — one state |

## Common mistakes
- Confusing hill climbing with greedy best-first search: greedy *path* search keeps a frontier; hill climbing keeps **only the current state** and no path.
- Thinking a restart "remembers" previous runs — it doesn't (except the best result so far).

Trace: [local-search-traces](../exercises/local-search-traces.md). Holland (1992) contrasts GAs with hill climbing on many-peaked landscapes → [genetic-algorithms](genetic-algorithms.md).
Related: [simulated-annealing](simulated-annealing.md) · [local-search-comparison](../comparisons/local-search-comparison.md)
