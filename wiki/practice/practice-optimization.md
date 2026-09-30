---
title: Practice — Optimization & Bio-Inspired Algorithms
type: practice
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms, dorigo-1996-ant-system, rn-ch04-complex-environments]
updated: 2026-09-30
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

## Local search (R&N Ch 4)
19. What does local search give up, and what does it gain, compared with the systematic search of Ch 3?
    <details><summary>answer</summary>Gives up systematicity (may miss solutions; no path kept). Gains tiny memory (often O(1)) and the ability to handle huge/infinite state spaces and pure optimization problems.</details>
20. Name three landscape features that stop hill climbing and explain the difference between a flat local maximum and a shoulder.
    <details><summary>answer</summary>Local maxima, ridges, plateaus. A flat local maximum has no uphill exit; a shoulder is flat but leads upward later (sideways moves can cross it).</details>
21. 8-queens with steepest-ascent hill climbing: success rate, and with ≤ 100 sideways moves?
    <details><summary>answer</summary>14% (stuck 86%); 94% with sideways moves.</details>
22. Why is random-restart hill climbing "complete with probability 1"? Expected restarts if one run succeeds with probability p?
    <details><summary>answer</summary>Eventually a random initial state is itself a goal (or leads to one); expected runs = 1/p.</details>
23. In simulated annealing, a move worsens the objective by 3 at T = 3. Acceptance probability? What happens as T → 0?
    <details><summary>answer</summary>e^(−3/3) = e^(−1) ≈ 0.368. As T → 0, bad moves are essentially never accepted → hill climbing.</details>
24. Local beam search with k states vs k random restarts?
    <details><summary>answer</summary>Beam search pools successors and keeps the k best overall (information sharing); restarts are independent. Beam can lose diversity → stochastic beam search.</details>
25. According to R&N, what is a GA in terms of other local search methods? What is the mixing number?
    <details><summary>answer</summary>A stochastic beam search with crossover (recombination). Mixing number ρ = number of parents per offspring (ρ = 1 is stochastic beam search).</details>
26. When does crossover give *no* advantage?
    <details><summary>answer</summary>When the encoding has no meaningful building blocks/schemas — e.g. if gene positions were randomly permuted.</details>
27. In the 8-queens GA, what is the fitness function and its maximum?
    <details><summary>answer</summary>Number of non-attacking pairs of queens; 8·7/2 = 28 for a solution.</details>
28. What is elitism and what does it guarantee?
    <details><summary>answer</summary>Copying the best parents into the next generation; the best fitness never decreases.</details>
29. Gradient ascent update and the role of α? What does Newton–Raphson add?
    <details><summary>answer</summary>x ← x + α∇f(x); α = step size (too small = slow, too big = overshoot). Newton uses the Hessian: x ← x − H⁻¹∇f(x), jumping to the optimum of a local quadratic fit.</details>
30. What's special about convex optimization / linear programming?
    <details><summary>answer</summary>No local optima other than the global one; LP is solvable in polynomial time.</details>
