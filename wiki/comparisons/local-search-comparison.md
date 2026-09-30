---
title: Local Search & Metaheuristics — Comparison
type: comparison
unit: optimization
sources: [rn-ch04-complex-environments, rn-ch05-csp, slides-04-optimization, holland-1992-genetic-algorithms, dorigo-1996-ant-system]
updated: 2026-09-30
---

# Local Search & Metaheuristics — Comparison 🎯

| Algorithm | States kept | How it moves | Escapes local optima by | Complete? | Memory | Page |
|---|---|---|---|---|---|---|
| Hill climbing (steepest) | 1 | best neighbour | — (stops) | ❌ | O(1) | [hill-climbing](../algorithms/hill-climbing.md) |
| + sideways moves | 1 | best neighbour incl. equal | walking plateaus (bounded) | ❌ | O(1) | same |
| Stochastic / first-choice HC | 1 | random uphill / first better | randomness (a little) | ❌ | O(1) | same |
| Random-restart HC | 1 (+ best) | HC from random starts | restarting | ✅ with probability 1 | O(1) | same |
| Simulated annealing | 1 | random neighbour; downhill with P = e^(ΔE/T) | accepting bad moves early (high T) | ✅ w.p. → 1 with slow cooling | O(1) | [simulated-annealing](../algorithms/simulated-annealing.md) |
| Local beam search | k | best k of all successors | shared information across k | ❌ | O(k) | [local-search](../concepts/local-search.md) |
| Stochastic beam search | k | k successors sampled ∝ value | diversity | ❌ | O(k) | same |
| Genetic algorithm | population | selection + crossover + mutation | population diversity, recombining building blocks | ❌ | O(N) | [genetic-algorithms](../algorithms/genetic-algorithms.md) |
| PSO | swarm | velocity toward p_best & g_best | inertia, random φ | ❌ | O(N) | [particle-swarm-optimization](../algorithms/particle-swarm-optimization.md) |
| ACO | colony + pheromone matrix | probabilistic tour construction | evaporation, stochastic choice | ❌ | O(n²) pheromones | [ant-colony-optimization](../algorithms/ant-colony-optimization.md) |
| ABC | food sources | neighbour search; scouts reset | scout bees | ❌ | O(SN) | [artificial-bee-colony](../algorithms/artificial-bee-colony.md) |
| Min-conflicts (CSP) | 1 complete assignment | least-conflict value for a conflicted var | plateau moves, tabu, weights | ❌ | O(n) | [min-conflicts](../algorithms/min-conflicts.md) |
| WalkSAT (SAT) | 1 model | flip random or best symbol of a false clause | random-walk flips (prob p) | ❌ | O(n) | [dpll-and-walksat](../algorithms/dpll-and-walksat.md) |
| Gradient ascent / Newton | 1 point (continuous) | x ← x + α∇f / x ← x − H⁻¹∇f | restarts | ❌ (✅ for convex) | O(n) / O(n²) | [local-search](../concepts/local-search.md#continuous-spaces) |

## One-line intuitions
- Hill climbing = greedy. Simulated annealing = greedy + a cooling random walk. Beam = parallel greedy that shares. GA = beam + sex. PSO/ACO/ABC = beam + social signals (best positions, pheromones, dances).
- Everything here trades **guarantees** for **memory and speed** — the same trade as weighted A* vs A* ([informed-search-comparison](informed-search-comparison.md)).

See also: [bio-inspired-algorithms-comparison](bio-inspired-algorithms-comparison.md) · [exploration-vs-exploitation](../concepts/exploration-vs-exploitation.md)
