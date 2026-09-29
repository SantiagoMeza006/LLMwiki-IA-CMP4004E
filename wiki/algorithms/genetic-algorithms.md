---
title: Genetic Algorithms (GA)
type: algorithm
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms]
updated: 2026-09-29
---

# Genetic Algorithms 🎯

**John H. Holland** (developed mid-1960s; book 1975; Sci. Am. article 1992). Apply natural selection to computing: **variation, selection, heredity** (slides-04 s.5).

## Representation
- **Individual / chromosome:** a **bit string** — a point in the solution space, e.g. a decimal number encoded in binary (slides-04 s.6).
- **Fitness function:** evaluates each individual (seek higher or lower value).
- Hard part (Holland): design an encoding where changing bits (genotype) changes behaviour (phenotype) meaningfully.

## The loop
```
population ← N random bit strings
repeat for G generations (or until good enough):
    evaluate fitness of every individual
    select parents (fitter ⇒ more likely; e.g. roulette-wheel / tournament / rank)
    for each pair of parents:
        with prob p_c: crossover → two offspring   (else copy parents)
        mutate each bit of each offspring with small prob p_m
    new population ← offspring (optionally keep the best: elitism)
return best individual seen
```
In Holland's version the offspring **replace the lowest-fitness strings**, keeping population size constant; intermediate strings simply survive.

## Operators 🎯
- **Crossover** (recombination / "reproduction" on slides): parents exchange bit sections **at the same positions**. Single-point: cut both at a random point and swap the tails. Generalises to two-point and **k-point** crossover.
  ```
  h1 = 1 0 1 | 1 0        →  1 0 1 0 1
  h2 = 0 1 1 | 0 1        →  0 1 1 1 0
  ```
- **Mutation:** each bit flips with a small probability (Holland: ~1 in 10,000 symbols). Not the main driver — **insurance against a uniform population** that can't evolve further.
- **Selection:** fitter strings mate more; weak ones perish.

## Why it works — schemata / building blocks (Holland)
- A **schema** is a pattern with wildcards, e.g. `1**0*`. A string of length L belongs to 2^L schemata ⇒ evaluating a few thousand strings implicitly samples a vastly larger number of regions: **implicit parallelism**.
- Above-average regions receive exponentially more samples over generations.
- **Compact building blocks** (defining bits close together) survive crossover best → they propagate at a rate proportional to their average fitness.
- Crossover tests building blocks in **new contexts** → balances [exploration vs exploitation](../concepts/exploration-vs-exploitation.md); handles nonlinear interactions between bits.

## Properties
- Stochastic, population-based, no gradient needed; no optimality guarantee.
- Great at finding **promising regions** in huge, rugged landscapes; weak at fine-tuning → combine with local search (turbine example).
- Parameters: population size N, crossover rate p_c, mutation rate p_m, selection scheme, number of generations.

## Examples
- Prisoner's Dilemma strategies (64-bit strings) → rediscovered **tit-for-tat** (Axelrod & Forrest).
- Jet turbine design (>100 variables, 10^387 points), gas pipeline control, network design.

Worked generation: [ga-one-generation](../exercises/ga-one-generation.md). Compare: [bio-inspired-algorithms-comparison](../comparisons/bio-inspired-algorithms-comparison.md).
