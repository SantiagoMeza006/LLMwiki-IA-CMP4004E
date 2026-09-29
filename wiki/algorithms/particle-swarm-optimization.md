---
title: Particle Swarm Optimization (PSO)
type: algorithm
unit: optimization
sources: [slides-04-optimization]
updated: 2026-09-29
---

# Particle Swarm Optimization 🎯

**James Kennedy & Russell Eberhart, 1995.** Stochastic optimisation inspired by simulations of social behaviour in **bird flocks and fish schools** + swarm theory. A swarm of particles moves **continuously** through the search space, sharing information about the best positions found (slides-04 s.8).

## State
Each particle i (a candidate solution) has:
- **position** `x_t`,
- **velocity** `v_t`,
- **personal best** `p_best` (best position this particle has ever visited).

The swarm keeps **`g_best`**, the best position found by *any* particle in *any* iteration.

## Update rules (slides-04 s.9) 🎯
```
v_{t+1} = v_t + α1·φ1·(p_best − x_t) + α2·φ2·(g_best − x_t)
x_{t+1} = x_t + v_{t+1}
```
- `φ1, φ2 ~ U[0, 1]` — fresh random numbers (per step, often per dimension).
- `α1` — **cognitive** coefficient (trust in own memory); `α2` — **social** coefficient (trust in the swarm).
- Three pulls: **inertia** (keep going: `v_t`), **cognitive** (back toward p_best), **social** (toward g_best).
- Common extension (not on slides): inertia weight `w·v_t` with w < 1 to damp velocity; velocity clamping.

## Algorithm
```
initialise particles with random x, v;  p_best ← x;  g_best ← best p_best
repeat:
    for each particle:
        update v, then x
        if f(x) better than f(p_best): p_best ← x
        if f(x) better than f(g_best): g_best ← x
until max iterations or convergence
return g_best
```

## Exploration vs exploitation (slides-04 s.10)
Large velocities / strong inertia / random φ → **exploration**; strong pull to p_best/g_best → **exploitation** (convergence, risk of premature convergence to a local optimum).

Worked update: [pso-update-step](../exercises/pso-update-step.md). Compare: [bio-inspired-algorithms-comparison](../comparisons/bio-inspired-algorithms-comparison.md).
