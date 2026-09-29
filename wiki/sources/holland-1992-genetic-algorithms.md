---
title: "Holland (1992) — Genetic Algorithms, Scientific American"
type: source
unit: optimization
raw: "raw/Holland-GeneticAlgorithms-1992.pdf"
sources: [holland-1992-genetic-algorithms]
updated: 2026-09-29
---

# John H. Holland, "Genetic Algorithms", *Scientific American* 267(1), July 1992, pp. 66–73

Popular-science article by the inventor of GAs. Raw: `raw/Holland-GeneticAlgorithms-1992.pdf`.

## Key ideas
1. **Why evolution?** Natural selection avoids having to specify in advance every feature of a problem; we can "breed" programs no one fully understands.
2. **History (Holland's account):** late-1950s/early-60s attempts relied on *mutation* only and did poorly; Bremermann (early 60s) added a limited mating (summing genes); Holland developed the **genetic algorithm in the mid-1960s**, with **mating (crossover) + mutation**; then extended it to **classifier systems**.
3. **Representation:** candidate solutions are **bit strings**; the key difficulty is designing a "genetic code" where changes in genotype give meaningful changes in phenotype (mutating FORTRAN text gives no program at all).
4. **The loop:** evaluate every string's fitness → higher-ranking strings **mate** (single-point crossover: swap the tails after a random point) → offspring **replace low-fitness strings** (population size constant) → **mutation** flips ~1 in 10,000 bits (insurance against a uniform population, not the main driver).
5. **Search landscape:** hill climbing gets stuck on landscapes with many peaks; a GA population samples many regions at once.
6. **Schemata / building blocks & implicit parallelism** 🎯: a string such as `11011001` belongs to many regions (`11******`, `1******1`, `**0**00*`, ...). Sampling a few thousand strings implicitly samples a vastly larger number of regions; regions receive samples at a rate proportional to their estimated average fitness.
7. **Compact building blocks** survive crossover (a block spanning few adjacent positions is rarely cut); *inversion* can make blocks more compact.
8. **Nonlinearity:** fitness of two blocks together ≠ sum of their parts; GAs still exploit useful multi-bit blocks.
9. **Exploration vs exploitation** 🎯: crossover tests building blocks in new contexts — GAs balance mortgaging the present for the future.
10. **Prisoner's Dilemma example** (Axelrod & Forrest): strategies encoded by the last 3 plays (4³ = 64 histories → 64-bit strings, 2^64 strategies); the GA rediscovered **tit-for-tat** and then a refinement that exploits "bluffable" opponents. Payoffs: both cooperate 3/3; defect vs cooperate 5/0; both defect minimal.
11. **Classifier systems:** condition–action rules as strings with "don't care" symbols; rules compete, winners strengthened (credit assignment); evolve **default hierarchies** (general default rules + specific exception rules).
12. **Applications:** gas-pipeline control (Goldberg), communication networks (Davis), jet-engine turbine design at GE/RPI (>100 variables, >10^387 points; GA seeded by an expert system → 3× the manual improvements in 2 days).
13. **Limitation:** GAs excel at locating promising regions of complex landscapes; for fine-tuning a few variables, combine with standard local methods.

> OCR note: the PDF text shows "54 possibilities" and "2^54"; the arithmetic (4 outcomes per play, 3 plays) gives **4³ = 64**, so strings are 64 bits and there are 2^64 ≈ 1.8×10^19 strategies.

Feeds: [genetic-algorithms](../algorithms/genetic-algorithms.md), [evolutionary-computation](../concepts/evolutionary-computation.md), [exploration-vs-exploitation](../concepts/exploration-vs-exploitation.md).
