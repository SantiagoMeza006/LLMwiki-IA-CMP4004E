---
title: Swarm Intelligence
type: concept
unit: optimization
sources: [slides-04-optimization, dorigo-1996-ant-system]
updated: 2026-09-29
---

# Swarm Intelligence

Many **simple agents** following **local rules** and communicating (directly or through the environment) produce good **collective** solutions that no individual computes alone.

## Mechanisms
| Mechanism | Example |
|---|---|
| **Sharing the best-known position** | PSO particles are pulled toward the swarm's g_best. |
| **Stigmergy** (indirect communication by modifying the environment) | ants deposit **pheromone**; others read it (Dorigo 1996: "communicate by modifications of a global data structure"). |
| **Positive feedback / autocatalysis** | the more ants on a trail, the more attractive it gets. |
| **Negative feedback / forgetting** | pheromone **evaporation**; ABC scouts abandon exhausted food sources. |
| **Division of labour** | ABC: employed & onlooker bees exploit, scouts explore. |

## Algorithms in this course
- [Particle Swarm Optimization](../algorithms/particle-swarm-optimization.md) — Kennedy & Eberhart 1995.
- [Ant Colony Optimization / Ant System](../algorithms/ant-colony-optimization.md) — Dorigo 1996.
- [Artificial Bee Colony](../algorithms/artificial-bee-colony.md) — Karaboga 2007.

## Why it works (Dorigo's explanation)
Alone, an agent following a greedy rule converges quickly to a poor solution (good early steps, bad forced final steps). Together, many agents reinforce the *good parts* of many solutions; bad parts get little reinforcement. The shared information reshapes the problem representation and shrinks the region that is searched. Communication gives **synergy**: m ants communicating beat m ants alone.

Related: [exploration-vs-exploitation](exploration-vs-exploitation.md) · [agents-and-environments](agents-and-environments.md) (each ant/particle is a simple agent; the swarm is a multiagent, cooperative system)
