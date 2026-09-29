---
title: Ant Colony Optimization (Ant System)
type: algorithm
unit: optimization
sources: [slides-04-optimization, dorigo-1996-ant-system]
updated: 2026-09-29
---

# Ant Colony Optimization (ACO) / Ant System 🎯

**Marco Dorigo (with Maniezzo & Colorni), 1996.** Metaheuristic originally for **combinatorial** problems (TSP, QAP, job-shop). Inspired by how ants find short paths to food.

## Biology → algorithm (slides-04 s.13)
Real ants wander randomly; when they find food they return to the colony leaving **pheromone**. Other ants tend to follow strong trails and reinforce them. **Evaporation** weakens unused trails. Goal: increase pheromone on good solutions, decrease it on poor ones.

## Ingredients (TSP)
| Symbol | Meaning |
|---|---|
| `τ_ij` | **pheromone** on edge (i,j): learned attraction, initialised uniformly (small constant c) |
| `η_ij = 1/d_ij` | **heuristic / visibility**: closer cities are intrinsically more attractive (greedy) |
| `α` | weight of pheromone (α = 0 ⇒ pure stochastic greedy) |
| `β` | weight of the heuristic |
| `ρ` | evaporation rate (slides) — see ⚠️ below |
| `Q` | deposit constant |
| `L_k` | length of ant k's tour |
| tabu list | cities already visited by ant k (guarantees a valid tour) |

## Rules 🎯 (slides-04 s.14)
**Transition probability** for ant at city i:
```
P(j | i) = τ_ij^α · η_ij^β  /  Σ_{k ∉ visited} τ_ik^α · η_ik^β      (j not visited; else 0)
```
**Pheromone update** after all ants complete their tours:
```
τ_ij ← (1 − ρ)·τ_ij + Σ_k Δτ_ij^k
Δτ_ij^k = Q / L_k   if ant k used edge (i,j) in its tour,  else 0
```
Shorter tours deposit **more** pheromone per edge.

> ⚠️ **ρ convention.** Slides: ρ = **evaporation** → `τ ← (1−ρ)τ + Δτ`. Dorigo 1996: ρ = **persistence** → `τ(t+n) = ρ·τ(t) + Δτ`, so evaporation is 1−ρ. With ρ = 0.5 the two agree; otherwise read the formula, not the letter. See [discrepancies](../discrepancies.md).

## Algorithm (ant-cycle)
```
initialise τ_ij = c on every edge; place m ants on cities (m ≈ n, spread out)
repeat for NC = 1..NC_MAX:
    each ant builds a full tour city by city using P(j|i), updating its tabu list
    compute each L_k; remember the best tour
    evaporate and deposit pheromone
    empty tabu lists
until NC_MAX or stagnation (all ants make the same tour)
```
Complexity O(NC · n² · m) = O(NC · n³) with m ≈ n.

## Dorigo's findings
- Best settings: **α = 1, β = 5, ρ = 0.5 (persistence), Q = 100**; m ≈ n ants.
- Too large α → fast **stagnation** on poor tours; α = 0 → no communication, poor results.
- **Ant-cycle** (deposit Q/L_k at tour end, global info) beats **ant-density** (Q per step) and **ant-quantity** (Q/d_ij per step).
- **Elitist ants**: extra e·Q/L* on best-so-far tour edges; helps up to an optimal e.
- Three pillars: **positive feedback**, **distributed computation**, **greedy constructive heuristic**.

Worked: [aco-transition-step](../exercises/aco-transition-step.md). See also [swarm-intelligence](../concepts/swarm-intelligence.md), [bio-inspired-algorithms-comparison](../comparisons/bio-inspired-algorithms-comparison.md).
