---
title: Evolutionary Computation
type: concept
unit: optimization
sources: [slides-04-optimization, holland-1992-genetic-algorithms]
updated: 2026-09-29
---

# Evolutionary Computation

Arose from the need to solve (combinatorial) optimization problems with the principles of **biological evolution** (slides-04 s.2).

## Lineage 🎯
| Year | Who | Contribution |
|---|---|---|
| 1960 | **Lawrence J. Fogel** | "Creator" of the field (per slides): evolutionary programming — evolving **finite-state machines**. |
| 1970 | **Ingo Rechenberg & Hans-Paul Schwefel** | **Evolution strategies** for continuous parameter optimization. |
| mid-1960s / **1975** | **John H. Holland** | **Genetic algorithms**, a general adaptive model (book 1975; 1992 Sci. Am. article). Emphasised **crossover (mating)** over mutation. |
| late 50s/early 60s | Friedberg (machine evolution), Bremermann | Early mutation-only attempts did poorly (R&N §1.3.3; Holland 1992). |

## Biological vocabulary → algorithm
| Biology | Algorithm |
|---|---|
| Individual / organism | candidate solution |
| Chromosome / genotype | encoding (e.g. bit string) |
| Gene / allele | position / value in the encoding |
| Phenotype | what the solution actually does |
| Fitness | objective function value |
| Natural selection | fitter individuals reproduce more |
| Heredity | offspring inherit parents' traits (crossover) |
| Variation | mutation (+ recombination) |
| Adaptation | population improves over generations |

## Three principles (slides-04 s.5)
**Variation**, **selection**, **heredity**.

## Why recombination matters (Holland)
Sexual reproduction mixes genes so creatures evolve faster than by copying + occasional mutation. In GAs, crossover combines **building blocks** (schemata) from different parents; mutation is just insurance against losing diversity. See [genetic-algorithms](../algorithms/genetic-algorithms.md).

Related: [optimization-and-local-optima](optimization-and-local-optima.md) · [history-of-ai](history-of-ai.md)
