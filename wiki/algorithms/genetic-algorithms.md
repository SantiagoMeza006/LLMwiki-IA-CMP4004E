---
title: Genetic Algorithms (GA)
type: algorithm
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms, rn-ch04-complex-environments]
updated: 2026-09-30
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

## The textbook view (R&N §4.1.4)
R&N treat GAs as a **stochastic beam search with crossover** (see [local-search](../concepts/local-search.md)). Design choices of any evolutionary algorithm:
- **Population size**; **representation** — GA: strings over a finite alphabet; **evolution strategies**: real-valued vectors; **genetic programming**: programs.
- **Mixing number ρ** — parents per offspring (ρ = 2 usual; ρ = 1 = stochastic beam search, i.e. asexual).
- **Selection** — fitness-proportional, or tournament (pick n at random, keep the ρ fittest).
- **Recombination** — crossover point(s). **Mutation rate** — per-bit flip probability.
- **Next generation** — only offspring, or keep the best parents (**elitism**: fitness never decreases); **culling** (discard below a threshold) can speed things up.

**8-queens GA (R&N Fig 4.6):** a state is an 8-digit string (digit c = row of the queen in column c); fitness = number of **non-attacking pairs** (28 for a solution). Population 24748552 (24), 32752411 (23), 24415124 (20), 32543213 (11) → selection probabilities 31%, 29%, 26%, 14%; crossing `327|52411` with `247|48552` gives `32748552` (verified in code). Mutation = move a random queen within its column.
- R&N's schema example: `246*****` = first three queens in rows 2, 4, 6. If a schema's instances are above-average, its instance count grows — Holland's result in textbook form.
- **Crossover only helps if schemas correspond to meaningful components**; if the gene positions were randomly permuted, crossover would give no advantage → careful representation engineering.
- GA pseudocode (R&N Fig 4.8):
  ```
  function GENETIC-ALGORITHM(population, fitness) returns an individual
      repeat
          weights ← WEIGHTED-BY(population, fitness)
          population2 ← empty list
          for i = 1 to SIZE(population):
              parent1, parent2 ← WEIGHTED-RANDOM-CHOICES(population, weights, 2)
              child ← REPRODUCE(parent1, parent2)
              if (small random probability): child ← MUTATE(child)
              add child to population2
          population ← population2
      until some individual is fit enough, or enough time has elapsed
      return the best individual in population
  ```
- Early on, a diverse population makes crossover take **large steps** (like high-temperature [simulated annealing](simulated-annealing.md)); later steps get smaller.
- R&N's caveat: it's not clear how much of GAs' appeal comes from superior performance vs the appealing metaphor; they shine on complex structured problems (circuit layout, job-shop scheduling, neural architecture search).

## Properties
- Stochastic, population-based, no gradient needed; no optimality guarantee.
- Great at finding **promising regions** in huge, rugged landscapes; weak at fine-tuning → combine with local search (turbine example).
- Parameters: population size N, crossover rate p_c, mutation rate p_m, selection scheme, number of generations.

## Examples
- Prisoner's Dilemma strategies (64-bit strings) → rediscovered **tit-for-tat** (Axelrod & Forrest).
- Jet turbine design (>100 variables, 10^387 points), gas pipeline control, network design.

Worked generation: [ga-one-generation](../exercises/ga-one-generation.md). Compare: [bio-inspired-algorithms-comparison](../comparisons/bio-inspired-algorithms-comparison.md).
