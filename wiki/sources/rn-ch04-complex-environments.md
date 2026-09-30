---
title: "R&N Chapter 4 — Search in Complex Environments"
type: source
unit: optimization
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch04-complex-environments]
updated: 2026-09-30
---

# R&N Chapter 4 — Search in Complex Environments (pp. 128–162)

Relaxes Ch 3's assumptions: we care about the **final state, not the path** (§4.1–4.2), the world is **nondeterministic** (§4.3), **partially observable** (§4.4) or **unknown** (§4.5). §4.1 is the textbook backbone of the course's optimization unit ([slides-04](slides-04-optimization.md)).

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 4.1 | Local search: state-space landscape, objective function, global/local maxima, plateaus, shoulders, ridges; complete-state formulation (8-queens, h = attacking pairs, 56 successors). | [local-search](../concepts/local-search.md) |
| 4.1.1 | **Hill climbing** (steepest ascent, "greedy local search"); 8-queens: solves 14%, 86% stuck; sideways moves (≤100) → 94%; stochastic, first-choice, **random-restart** (complete with probability 1; expected restarts 1/p). | [hill-climbing](../algorithms/hill-climbing.md) |
| 4.1.2 | **Simulated annealing**: random move, accept worse moves with probability e^(ΔE/T), T decreases by a schedule; finds global optimum with probability → 1 if cooled slowly enough. | [simulated-annealing](../algorithms/simulated-annealing.md) |
| 4.1.3 | **Local beam search** (k states, share information) and stochastic beam search. | [local-search](../concepts/local-search.md) |
| 4.1.4 | **Evolutionary algorithms**: population, mixing number ρ, selection, crossover, mutation rate, elitism, culling; GA on 8-queens digit strings (Fig 4.6); schemas; GA pseudocode (Fig 4.8); evolution strategies, genetic programming; Baldwin effect. | [genetic-algorithms](../algorithms/genetic-algorithms.md), [evolutionary-computation](../concepts/evolutionary-computation.md) |
| 4.2 | Continuous spaces: discretisation, empirical gradient, gradient ascent `x ← x + α∇f(x)`, step size, line search, Newton–Raphson (Hessian), constrained optimization, linear programming, convex optimization. | [local-search](../concepts/local-search.md#continuous-spaces) |
| 4.3 | Nondeterministic actions: erratic vacuum, RESULTS returns a set, **conditional plans**, **AND–OR search trees** (OR = agent's choice, AND = nature's outcome), cyclic plans ("try, try again"). | [nondeterministic-and-partially-observable-search](../concepts/nondeterministic-and-partially-observable-search.md) |
| 4.4 | Partial observability: **belief states**, sensorless (conformant) problems, coercion, prediction/observation/update, AND–OR search over belief states. | same |
| 4.5 | Online search in unknown environments: competitive ratio, safely explorable, dead ends, random walk, **LRTA\*** (optimism under uncertainty). | same |

## Most exam-relevant takeaways 🎯
1. Local search keeps **one (or k) current state(s)**, uses **very little memory**, is **not systematic** (may miss solutions) but works on huge or infinite spaces and pure optimization problems.
2. Hill climbing gets stuck on **local maxima, ridges and plateaus**; fixes: sideways moves, random restarts, randomness (stochastic/first-choice), simulated annealing.
3. Simulated annealing = hill climbing + **controlled random walk**; temperature controls exploration.
4. A GA is a **stochastic beam search with crossover**; crossover only helps if the encoding has meaningful **building blocks (schemas)**.
5. With nondeterminism/partial observability, a solution becomes a **conditional plan** (a tree), found by AND–OR search — the same AND–OR structure Prolog explores (see [sld-resolution](../algorithms/sld-resolution.md)).
