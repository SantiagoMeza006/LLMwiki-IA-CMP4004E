---
title: Optimization, Local vs Global Optima, Metaheuristics
type: concept
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms, dorigo-1996-ant-system, rn-ch04-complex-environments]
updated: 2026-09-30
---

# Optimization and Local vs Global Optima

## Optimization vs path search
- [Path search](search-problem-formulation.md) (Ch 3) wants a *sequence of actions* to a goal.
- **Optimization** wants a *point* (a candidate solution) that maximises/minimises an **objective / fitness function**; the path to it doesn't matter. Examples: parameters of a function, a TSP tour, a turbine design, a schedule.

## Global vs local optima 🎯
- **Global maximum/minimum:** best value over the whole solution space.
- **Local maximum/minimum:** better than all its neighbours but not globally best.
- Optimization "seeks global maximum or minimum solution points and avoids confusing them with local points" (slides-04 s.3).
- **Hill climbing** (move to a better neighbour until none is better) gets stuck on local optima, plateaus and ridges; complex, high-dimensional landscapes have many peaks (Holland 1992). Textbook treatment: [local-search](local-search.md), [hill-climbing](../algorithms/hill-climbing.md), [simulated-annealing](../algorithms/simulated-annealing.md) (R&N §4.1).

## The evolutionary idea (slides-04 s.3)
Treat every point in the solution space as an **individual** of a species; evaluate its **fitness**; replicate evolution (adaptation, heredity, natural selection) so that only individuals converging to the global optimum survive.

## Population-based metaheuristics in this course
| Method | Inspiration | Search space | Page |
|---|---|---|---|
| Genetic algorithm | natural selection + sexual reproduction | discrete (bit strings) | [genetic-algorithms](../algorithms/genetic-algorithms.md) |
| Particle swarm optimization | bird flocks / fish schools | continuous | [particle-swarm-optimization](../algorithms/particle-swarm-optimization.md) |
| Ant colony optimization | ant pheromone trails | combinatorial (graphs: TSP, QAP, JSP) | [ant-colony-optimization](../algorithms/ant-colony-optimization.md) |
| Artificial bee colony | honeybee foraging | continuous | [artificial-bee-colony](../algorithms/artificial-bee-colony.md) |

Shared traits: **stochastic**; keep a **population** (samples many regions at once, resisting local optima); balance [exploration vs exploitation](exploration-vs-exploitation.md); no guarantee of global optimality ("good enough" / satisficing, like [weighted A*](../algorithms/memory-bounded-and-weighted-search.md)); often outperformed by specialised algorithms but very **versatile** (Dorigo 1996). Holland: best at locating promising regions; combine with local methods for fine-tuning.

Compare them: [bio-inspired-algorithms-comparison](../comparisons/bio-inspired-algorithms-comparison.md) and, including hill climbing / simulated annealing / beam search, [local-search-comparison](../comparisons/local-search-comparison.md).

Related: [evolutionary-computation](evolutionary-computation.md) · [swarm-intelligence](swarm-intelligence.md)
