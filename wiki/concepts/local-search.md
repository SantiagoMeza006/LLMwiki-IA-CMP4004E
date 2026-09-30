---
title: Local Search and Optimization Problems
type: concept
unit: optimization
sources: [rn-ch04-complex-environments, slides-04-optimization, holland-1992-genetic-algorithms]
updated: 2026-09-30
---

# Local Search 🎯

(R&N §4.1–4.2, [source](../sources/rn-ch04-complex-environments.md).) The bridge between the **search** unit and the **optimization** unit of the slides.

## Idea
- Sometimes only the **final state** matters, not the path (8-queens, IC layout, factory layout, job-shop scheduling, portfolio management).
- **Local search** moves from the current state to **neighbouring** states without remembering paths or reached states.
  - ✅ Very little memory (often constant); works in huge or infinite (continuous) spaces; solves pure **optimization problems** (find the best state by an **objective function**).
  - ❌ **Not systematic** → may never visit the region containing the solution (incomplete, not optimal in general).
- **Complete-state formulation:** every state is a full candidate (all 8 queens on the board), possibly with violations.

## The state-space landscape
Each state has an "elevation" = objective value. Maximise → **hill climbing**; minimise cost → **gradient descent**.

| Feature | What goes wrong |
|---|---|
| **Global maximum** | the goal |
| **Local maximum** | higher than all neighbours, lower than the global max — greedy methods stop here |
| **Ridge** | a sequence of local maxima not directly connected; every available move goes downhill |
| **Plateau** — flat local maximum | no uphill exit |
| **Plateau** — **shoulder** | flat, but progress is possible further on |

## The family
| Algorithm | Keeps | Moves | Page |
|---|---|---|---|
| Hill climbing (steepest ascent) | 1 state | best neighbour, stop at a peak | [hill-climbing](../algorithms/hill-climbing.md) |
| Stochastic / first-choice HC | 1 | random uphill / first better neighbour | same |
| Random-restart HC | 1 (+ best so far) | restart from random states | same |
| Simulated annealing | 1 | random move; accept downhill with prob e^(ΔE/T) | [simulated-annealing](../algorithms/simulated-annealing.md) |
| **Local beam search** | k states | all successors of all k, keep the k best — information is **shared** ("come over here, the grass is greener!") | below |
| **Stochastic beam search** | k | choose k successors with probability ∝ value (more diversity) | below |
| Evolutionary algorithms / GA | population | selection + **crossover** + mutation = stochastic beam search with sexual reproduction | [genetic-algorithms](../algorithms/genetic-algorithms.md) |
| Swarm methods (course extras) | population | PSO, ACO, ABC | [bio-inspired comparison](../comparisons/bio-inspired-algorithms-comparison.md) |
| Min-conflicts (for CSPs) | 1 | change a conflicted variable to its least-conflict value | [min-conflicts](../algorithms/min-conflicts.md) |

**Local beam ≠ k random restarts in parallel:** restarts run independently; beam search pools successors so effort moves to where progress is. Risk: the k states cluster together (lack of diversity) → stochastic beam search.

## Continuous spaces
(R&N §4.2) Example: place 3 airports in Romania minimising the sum of squared distances from each city to its nearest airport → 6-dimensional state (x1, y1, x2, y2, x3, y3).
- **Discretise** (move each variable by ±δ → 12 successors) or sample random directions — **empirical gradient**.
- **Gradient ascent:** `x ← x + α ∇f(x)` with **step size** α (too small = slow, too big = overshoot); **line search** doubles α until f decreases.
- **Newton–Raphson:** `x ← x − H_f⁻¹(x) ∇f(x)` (Hessian of second derivatives); for the airport problem one step moves each airport to the centroid of its cities.
- **Constrained optimization**; **linear programming** (polynomial time) ⊂ **convex optimization** (no local optima that aren't global).
- Same pitfalls (local maxima, ridges, plateaus) → random restarts, simulated annealing. [PSO](../algorithms/particle-swarm-optimization.md) and [ABC](../algorithms/artificial-bee-colony.md) are population methods for continuous spaces.

Related: [optimization-and-local-optima](optimization-and-local-optima.md) · [exploration-vs-exploitation](exploration-vs-exploitation.md) · [local-search-comparison](../comparisons/local-search-comparison.md) · [local-search-traces](../exercises/local-search-traces.md)
