---
title: Bio-Inspired Algorithms — Comparison (GA, PSO, ACO, ABC)
type: comparison
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms, dorigo-1996-ant-system]
updated: 2026-09-29
---

# Bio-Inspired Algorithms — Comparison 🎯

| | [GA](../algorithms/genetic-algorithms.md) | [PSO](../algorithms/particle-swarm-optimization.md) | [ACO / Ant System](../algorithms/ant-colony-optimization.md) | [ABC](../algorithms/artificial-bee-colony.md) |
|---|---|---|---|---|
| Author, year | Holland (1960s; book 1975; article 1992) | Kennedy & Eberhart 1995 | Dorigo (+ Maniezzo, Colorni) 1996 | Karaboga 2007 |
| Inspiration | natural selection, sexual reproduction | bird flocks, fish schools | ant foraging, pheromone trails | honeybee foraging |
| Family | evolutionary computation | swarm intelligence | swarm intelligence | swarm intelligence |
| Candidate solution | chromosome (bit string) | particle position x | tour built by one ant | food source position |
| Typical space | discrete / binary encoded | continuous | combinatorial graph (TSP, QAP, JSP) | continuous |
| Memory / shared info | population itself (genes) | p_best per particle, g_best shared | pheromone matrix τ (stigmergy) | food sources in memory + fitness "dances" |
| Main operators | selection, crossover, mutation | velocity update toward p_best & g_best | probabilistic construction (τ^α·η^β), evaporation, deposit Q/L_k | employed/onlooker neighbour search `v = x + φ(x − x_k)`, scout reset after `limit` |
| Exploration by | mutation, crossover in new contexts | inertia, random φ | stochastic choice, evaporation | scout bees |
| Exploitation by | selection of fittest | pull to p_best/g_best | pheromone reinforcement, β greedy term, elitist ants | employed + onlooker bees |
| Key parameters | N, p_c, p_m, selection | α1, α2 (+ inertia w) | α, β, ρ, Q, m (≈ n) | SN/BN, limit, MCN |
| Failure mode | uniform population / premature convergence | premature convergence to g_best | stagnation (all ants same tour) | slow convergence |

## One-sentence summaries
- **GA:** breed better bit strings by keeping the fittest, recombining their building blocks, and occasionally mutating.
- **PSO:** particles fly through space, each pulled toward its own best and the swarm's best.
- **ACO:** ants build solutions probabilistically, favouring short and heavily-trodden edges; good tours leave more pheromone, all trails evaporate.
- **ABC:** employed and onlooker bees refine good food sources; scouts abandon exhausted ones and explore randomly.

Background: [optimization-and-local-optima](../concepts/optimization-and-local-optima.md) · [evolutionary-computation](../concepts/evolutionary-computation.md) · [swarm-intelligence](../concepts/swarm-intelligence.md) · [exploration-vs-exploitation](../concepts/exploration-vs-exploitation.md)
