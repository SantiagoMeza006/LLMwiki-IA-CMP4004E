---
title: "Exercise — One Generation of a Genetic Algorithm"
type: exercise
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms]
updated: 2026-09-29
---

# One Generation of a GA — maximise f(x) = x², x ∈ [0, 31]

Classic textbook setup: 5-bit chromosomes, population 4, roulette-wheel (fitness-proportional) selection, single-point crossover, bit-flip mutation. All numbers verified in code.

## 1. Evaluate
| # | Chromosome | x | f(x) = x² | P(select) = f / Σf | Cumulative |
|---|---|---|---|---|---|
| 1 | 01101 | 13 | 169 | 0.144 | 0.144 |
| 2 | 11000 | 24 | 576 | 0.492 | 0.637 |
| 3 | 01000 | 8 | 64 | 0.055 | 0.691 |
| 4 | 10011 | 19 | 361 | 0.309 | 1.000 |
| | | | Σ = 1170, avg 292.5, max 576 | | |

## 2. Select (roulette spins r = 0.10, 0.45, 0.70, 0.90)
r = 0.10 → #1 `01101` · r = 0.45 → #2 `11000` · r = 0.70 → #4 `10011` · r = 0.90 → #4 `10011`.
Individual #3 (the weakest) was not selected; #4 got two copies.

## 3. Crossover
- Pair (01101, 11000), cut after bit 4: `0110|1` × `1100|0` → **01100** (12), **11001** (25)
- Pair (10011, 10011), cut after bit 2: identical parents ⇒ offspring identical: **10011**, **10011**. (Crossover can't create novelty from identical parents — that's why mutation matters.)

## 4. Mutation
Flip bit 3 of the last offspring: `10011` → **10111** (23).

## 5. New generation
| Chromosome | x | f(x) |
|---|---|---|
| 01100 | 12 | 144 |
| 11001 | 25 | 625 |
| 10011 | 19 | 361 |
| 10111 | 23 | 529 |
| | | Σ = 1659, **avg 414.75** (was 292.5), **max 625** (was 576) |

## Observations
- Average and best fitness both improved after one generation.
- Schema `1****` (x ≥ 16) went from 2/4 to 3/4 of the population: above-average building blocks spread (Holland's schema idea).
- Without mutation, the population could never recover bit values that disappear from every string.

## Try it
Repeat step 3 with the first pair cut after bit 1. <details><summary>answer</summary>`0|1101` × `1|1000` → 01000 (8, f=64) and 11101 (29, f=841). One child is terrible, one is excellent — crossover is a gamble; selection keeps the good ones.</details>
