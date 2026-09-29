---
title: "Exercise — ACO Transition Probabilities and Pheromone Update"
type: exercise
unit: optimization
sources: [slides-04-optimization, dorigo-1996-ant-system]
updated: 2026-09-29
---

# ACO: One Decision and One Pheromone Update

An ant is at city **A**; unvisited cities B, C, D. (Numbers verified in code.)

| Edge | d | η = 1/d | τ (pheromone) |
|---|---|---|---|
| A–B | 2 | 0.5 | 1 |
| A–C | 4 | 0.25 | 3 |
| A–D | 5 | 0.2 | 1 |

## 1. Transition probabilities with α = 1, β = 2
`P(j|A) = τ_Aj^α · η_Aj^β / Σ_k τ_Ak^α · η_Ak^β`

| j | τ^1 · η^2 | P |
|---|---|---|
| B | 1 · 0.25 = 0.25 | 0.25 / 0.4775 = **0.524** |
| C | 3 · 0.0625 = 0.1875 | **0.393** |
| D | 1 · 0.04 = 0.04 | **0.084** |

## 2. Effect of α and β
| Setting | P(B) | P(C) | P(D) | Interpretation |
|---|---|---|---|---|
| α = 1, β = 2 | 0.524 | 0.393 | 0.084 | balance |
| α = 0, β = 2 | 0.709 | 0.177 | 0.113 | ignores pheromone → stochastic greedy (nearest city) |
| α = 1, β = 0 | 0.200 | 0.600 | 0.200 | ignores distance → follows the crowd only |
| α = 1, β = 5 (Dorigo's best) | 0.906 | 0.085 | 0.009 | strongly greedy early on |

## 3. Pheromone update (slide convention, ρ = evaporation = 0.5, Q = 10)
Two ants finished: ant 1's tour L₁ = 10 used A–B; ant 2's tour L₂ = 12 used A–C.
`τ_ij ← (1 − ρ)·τ_ij + Σ_k Δτ_ij^k`, `Δτ_ij^k = Q / L_k`

| Edge | (1−ρ)·τ | deposits | new τ |
|---|---|---|---|
| A–B | 0.5 · 1 = 0.5 | + 10/10 = 1.0 | **1.5** |
| A–C | 0.5 · 3 = 1.5 | + 10/12 = 0.833 | **2.333** |
| A–D | 0.5 · 1 = 0.5 | — | **0.5** |

New probabilities (α = 1, β = 2): B **0.693**, C **0.270**, D **0.037** — the short edge A–B, used by the better tour, gained; the unused edge A–D evaporated toward irrelevance.

> ⚠️ In Dorigo's paper the same update is written `τ ← ρ·τ + Δτ` with ρ = **persistence**. With ρ = 0.5 the numbers are identical; with ρ = 0.9 (paper) you'd keep 90% (slide convention: evaporate 90%!). Always check which convention a question uses.

## Try it
Same start, but ant 2 had the shorter tour (L₂ = 8) and ant 1 the longer (L₁ = 20). New τ? <details><summary>answer</summary>A–B: 0.5 + 10/20 = 1.0; A–C: 1.5 + 10/8 = 2.75; A–D: 0.5.</details>
