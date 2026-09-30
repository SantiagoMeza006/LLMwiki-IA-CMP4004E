---
title: "Slides 04 — Optimization and Biology-Inspired Agents"
type: source
unit: optimization
raw: "raw/04_Optimization.pptx"
sources: [slides-04-optimization]
updated: 2026-09-29
---

# Slides 04 — Optimization and Biology-Inspired Agents

19 slides · Raw: `raw/04_Optimization.pptx` · Formulas on slides 9, 14, 18 are images (transcribed below).

## What it covers

| Slide | Topic | Wiki page |
|---|---|---|
| 2 | 🎯 Evolutionary computation history: **Fogel 1960** (evolving finite-state machines), **Rechenberg & Schwefel 1970** (evolution strategies, parameter optimisation), **Holland 1975** (genetic algorithms). | [evolutionary-computation](../concepts/evolutionary-computation.md) |
| 3 | 🎯 Global vs local maxima/minima; adaptation, heredity, natural selection; treat each point of the solution space as an individual with a fitness. | [optimization-and-local-optima](../concepts/optimization-and-local-optima.md) |
| 5–6 | 🎯 Genetic algorithms (Holland): variation, selection, heredity; individuals = bit strings (chromosome), fitness function, **crossover** (single/two/k-point), **mutation** (bit flip with probability). | [genetic-algorithms](../algorithms/genetic-algorithms.md) |
| 8–10 | 🎯 **PSO** (Kennedy & Eberhart 1995): particles with position x_t, velocity v_t, personal best p_best; swarm best g_best. `v_{t+1} = v_t + α1·φ1·(p_best − x_t) + α2·φ2·(g_best − x_t)`, `x_{t+1} = x_t + v_{t+1}`, φ1, φ2 ~ U[0,1]. Exploration vs exploitation. | [particle-swarm-optimization](../algorithms/particle-swarm-optimization.md) |
| 12–14 | 🎯 **ACO** (Dorigo 1996): pheromone trails, evaporation. `P(j|i) = τ_ij^α·η_ij^β / Σ_{k∉visited} τ_ik^α·η_ik^β`; `τ_ij ← (1−ρ)·τ_ij + Σ_k Δτ_ij^k`; `η_ij = 1/d_ij`; `Δτ_ij^k = Q/L_k` if ant k used edge (i,j), else 0. | [ant-colony-optimization](../algorithms/ant-colony-optimization.md) |
| 16–19 | 🎯 **Artificial Bee Colony** (Karaboga 2007): employed, onlooker, scout bees; employed + onlookers exploit, scouts explore; parameters: number of food sources (= employed = onlooker bees), `limit`, max cycles MCN; candidate `v_ij = x_ij + φ_ij·(x_ij − x_kj)`. Loop: initialise; repeat {employed → onlookers → scouts} until done. | [artificial-bee-colony](../algorithms/artificial-bee-colony.md) |

## Where it fits
Unit **optimization**. Primary readings: [Holland 1992](holland-1992-genetic-algorithms.md) and [Dorigo et al. 1996](dorigo-1996-ant-system.md). Textbook backbone: [R&N Ch 4 §4.1–4.2](rn-ch04-complex-environments.md) — [local search](../concepts/local-search.md), [hill climbing](../algorithms/hill-climbing.md), [simulated annealing](../algorithms/simulated-annealing.md), local beam search and R&N's view of [genetic algorithms](../algorithms/genetic-algorithms.md). PSO, ACO and ABC are not in R&N; the papers and slides are the only sources for them.

> ⚠️ **Two conventions for ρ (slide 14 vs Dorigo 1996):** the slide writes `τ ← (1−ρ)τ + ΣΔτ` with **ρ = evaporation rate**. The original paper writes `τ(t+n) = ρ·τ(t) + Δτ` with **ρ = trail persistence** (so 1−ρ is evaporation). Same algorithm, opposite meaning of ρ. See [discrepancies](../discrepancies.md).
>
> ⚠️ **GA date (slide 5):** "John Holland – 1992" is the date of the Scientific American article we read; GAs themselves date to the **mid-1960s** (Holland's own account) and his book *Adaptation in Natural and Artificial Systems* is **1975** (slide 2).
