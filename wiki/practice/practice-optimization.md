---
title: Practice — Optimization & Bio-Inspired Algorithms
type: practice
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms, dorigo-1996-ant-system]
updated: 2026-09-29
---

# Practice — Optimization & Bio-Inspired Algorithms

1. Who are Fogel (1960), Rechenberg & Schwefel (1970), and Holland (1975) in evolutionary computation?
   <details><summary>answer</summary>Fogel: evolutionary programming, evolving finite-state machines. Rechenberg & Schwefel: evolution strategies for parameter optimisation. Holland: genetic algorithms as a general adaptive model.</details>
2. Local vs global optimum; why do population methods help?
   <details><summary>answer</summary>Local: best among neighbours only; global: best overall. A population samples many regions at once, so it's less likely to get trapped on one peak.</details>
3. The three principles of a GA (slides) and the three operators.
   <details><summary>answer</summary>Variation, selection, heredity. Operators: selection, crossover, mutation.</details>
4. Do single-point crossover of 11010 and 00111 after bit 2.
   <details><summary>answer</summary>11|010 × 00|111 → 11111 and 00010.</details>
5. What is the role of mutation according to Holland? Typical rate he quotes?
   <details><summary>answer</summary>Insurance against a uniform population unable to evolve; it rarely drives progress. About 1 in 10,000 bits.</details>
6. What is implicit parallelism? What is a compact building block?
   <details><summary>answer</summary>Each string belongs to many schemata, so evaluating a few thousand strings samples a vastly larger number of regions. A compact building block has its defining bits close together, so crossover rarely breaks it.</details>
7. Roulette selection: fitnesses 10, 30, 60. Selection probabilities?
   <details><summary>answer</summary>0.1, 0.3, 0.6.</details>
8. Write the PSO velocity and position updates and name each term.
   <details><summary>answer</summary>v ← v + α1φ1(p_best − x) + α2φ2(g_best − x); x ← x + v. Inertia, cognitive (own best), social (swarm best); φ ~ U[0,1].</details>
9. PSO: x = 2, v = 1, p_best = 1, g_best = 0, α1 = α2 = 1, φ1 = 0.5, φ2 = 1. New v and x?
   <details><summary>answer</summary>v = 1 + 0.5·(1−2) + 1·(0−2) = 1 − 0.5 − 2 = −1.5; x = 0.5.</details>
10. ACO transition rule: what do τ, η, α, β mean? What happens with α = 0?
    <details><summary>answer</summary>τ pheromone (learned desirability), η = 1/d visibility (greedy), α and β their weights. α = 0 → ignores pheromone → stochastic multi-start greedy.</details>
11. Why do shorter tours get more pheromone?
    <details><summary>answer</summary>Δτ = Q/L_k is inversely proportional to tour length.</details>
12. What is stagnation in ACO and which parameter causes it?
    <details><summary>answer</summary>All ants follow the same tour; no more exploration. Caused by too high α (and too many elitist ants).</details>
13. Dorigo's best parameter set for ant-cycle? Optimal number of ants?
    <details><summary>answer</summary>α = 1, β = 5, ρ = 0.5, Q = 100; m ≈ n (number of cities).</details>
14. The slide writes τ ← (1−ρ)τ + ΣΔτ; the paper writes τ ← ρτ + Δτ. Reconcile.
    <details><summary>answer</summary>Slide ρ = evaporation rate; paper ρ = persistence (evaporation = 1−ρ). Same update, different letter meaning.</details>
15. Name ABC's three bee types and which explore vs exploit.
    <details><summary>answer</summary>Employed and onlooker bees exploit; scout bees explore (replace abandoned sources after `limit` failed trials).</details>
16. ABC control parameters?
    <details><summary>answer</summary>Number of food sources (= employed = onlooker bees, BN/SN), limit, maximum cycle number (MCN).</details>
17. For which kind of problem would you pick ACO over PSO, and why?
    <details><summary>answer</summary>Combinatorial/graph problems like TSP, routing, scheduling: ants construct discrete solutions edge by edge. PSO naturally handles continuous spaces.</details>
18. Holland's turbine example: what's the lesson about GA limitations?
    <details><summary>answer</summary>GAs locate promising regions of huge landscapes well, but fine-tuning a few variables is better done with conventional local methods — combine them.</details>
