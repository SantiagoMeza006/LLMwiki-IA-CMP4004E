---
title: "Dorigo, Maniezzo & Colorni (1996) — Ant System"
type: source
unit: optimization
raw: "raw/3 - dorigo1996.pdf"
sources: [dorigo-1996-ant-system]
updated: 2026-09-29
---

# Dorigo, Maniezzo & Colorni, "Ant System: Optimization by a Colony of Cooperating Agents", *IEEE Trans. SMC-B* 26(1), 1996, pp. 29–41

Raw: `raw/3 - dorigo1996.pdf`. The founding paper of ant colony optimisation.

## Key ideas
- **Three ingredients** 🎯: **positive feedback** (rapid discovery of good solutions), **distributed computation** (avoids premature convergence), **constructive greedy heuristic** (finds acceptable solutions early).
- **Real ants:** almost blind; communicate through **pheromone** trails; more ants on a trail → more attractive (autocatalytic process). Double-bridge/obstacle example: the shorter branch gets reinforced faster, so all ants converge to it.
- **Artificial ants differ:** they have memory (tabu list), are not completely blind (see distances), and live in discrete time.
- **Worked toy example (Fig 2):** 30 ants per time unit from each side; at t=1 the short side has trail 30 vs 15 on the long side ⇒ expected 20 vs 10 ants choose short vs long.

## The algorithm (applied to TSP)
- Visibility `η_ij = 1/d_ij` (fixed). Trail `τ_ij(t)` (changes).
- **Transition rule** (eq. 4): `p_ij^k(t) = [τ_ij]^α [η_ij]^β / Σ_{l ∈ allowed_k} [τ_il]^α [η_il]^β` for j ∈ allowed_k (not in ant k's tabu list), else 0.
- **Trail update** after every ant finishes a tour (n steps): `τ_ij(t+n) = ρ·τ_ij(t) + Δτ_ij`, with `Δτ_ij = Σ_k Δτ_ij^k`, and **ρ = persistence** (1−ρ = evaporation; ρ < 1 avoids unlimited accumulation).
- **Ant-cycle** deposit: `Δτ_ij^k = Q / L_k` if ant k used (i,j) in its tour, else 0 (global information: better tours deposit more).
- Variants: **ant-density** (deposit Q per step) and **ant-quantity** (deposit Q/d_ij per step) — both use only local info and performed worse than ant-cycle.
- **Tabu list** enforces legal tours (not tabu search — different idea).
- **Complexity:** O(NC · n² · m); with m ≈ n ants, O(NC · n³).
- **Stopping:** max cycles NC_MAX, or **stagnation** (all ants make the same tour).

## Experimental findings 🎯
- Best parameters (ant-cycle, Oliver30): **α = 1, β = 5, ρ = 0.5, Q = 100** (Q barely matters).
- α = 0 ⇒ stochastic multi-start greedy algorithm (no trail); too high α ⇒ quick **stagnation** on poor tours.
- **Synergy:** communicating ants (α > 0) beat non-communicating ones; optimal number of ants **m ≈ n** (number of cities).
- Spreading ants over different starting towns works better than starting all in one town.
- **Elitist strategy:** extra `e·Q/L*` on edges of the best-so-far tour; there is an optimal number of elitist ants (too many → premature focus on suboptimal tours).
- Found the best known Oliver30 tour (423.741) in 342 cycles; comparable to tabu search, better than simulated annealing on the same time budget; slower than TSP-specific heuristics.
- Versatile/robust: asymmetric TSP (no changes needed), **QAP**, **job-shop scheduling** (needs a graph representation, autocatalytic feedback, a greedy force, and a constraint-satisfaction method).

Feeds: [ant-colony-optimization](../algorithms/ant-colony-optimization.md), [swarm-intelligence](../concepts/swarm-intelligence.md), [aco-transition-step](../exercises/aco-transition-step.md).
