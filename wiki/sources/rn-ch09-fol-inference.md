---
title: "R&N Chapter 9 — Inference in First-Order Logic"
type: source
unit: logic
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch09-fol-inference]
updated: 2026-09-30
---

# R&N Chapter 9 — Inference in First-Order Logic (pp. 298–331)

Reading assigned by [slides-XX](slides-xx-prolog.md) (§9.4 backward chaining and logic programming). Many slide examples (Criminal(West), `path/2` loop, `append/3`) come from here.

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 9.1 | **Universal Instantiation** (substitute any ground term), **Existential Instantiation** (new **Skolem constant**); **propositionalization**; Herbrand's theorem; FOL entailment is **semidecidable**. | [first-order-inference](../concepts/first-order-inference.md) |
| 9.2 | **Generalized Modus Ponens** (lifted MP); **UNIFY** algorithm (Fig 9.1), **standardizing apart**, **most general unifier**, **occur check** (quadratic; omitted by Prolog); storage/retrieval, predicate indexing, subsumption lattice. | [unification](../concepts/unification.md), [first-order-inference](../concepts/first-order-inference.md) |
| 9.3 | **First-order definite clauses**, the crime KB (9.3–9.10), **Datalog**; FOL-FC-ASK (2 iterations to Criminal(West)); fixed point; sound and complete for definite clauses; conjunct ordering (≈ MRV), matching is NP-hard, incremental FC, **Rete**, production systems (XCON), magic sets. | [forward-and-backward-chaining](../concepts/forward-and-backward-chaining.md) |
| 9.4 | **FOL-BC-ASK** as generator (AND/OR search); **logic programming**, *Algorithm = Logic + Control*; Prolog's departures from logic (database semantics, built-in arithmetic `is`, side effects, no occur check, DFS with no loop check); redundant inference & infinite loops (`path/2`: 877 vs 62 inferences); **tabling**; database semantics & **completion**; **constraint logic programming** (`triangle(3,4,Z)` → 1 < Z < 7). | [prolog](../concepts/prolog.md), [sld-resolution](../algorithms/sld-resolution.md) |
| 9.5 | FOL **resolution**: CNF conversion with **Skolem functions**, binary resolution + factoring, crime and "Curiosity killed the cat" proofs, refutation completeness, equality (demodulation, paramodulation), strategies (unit preference, set of support, input resolution, subsumption), theorem provers. | [resolution](../algorithms/resolution.md) |

## Takeaways 🎯
1. Unification lets inference make **only the substitutions it needs** (lifting), instead of instantiating everything.
2. Forward chaining = data-driven, complete for definite clauses, reaches a **fixed point** (Datalog: polynomial). Backward chaining = goal-driven **DFS**, linear space, but repeated states and infinite loops.
3. **Backward chaining is resolution with a particular control strategy** (the resolution "spine" = the goal list).
4. Prolog trades logical purity for speed: database semantics, no occur check, depth-first left-to-right — hence the slide's "SLD resolution is complete; Prolog's search rule is not".
5. Resolution with Skolemization is refutation-complete for all of FOL (not only Horn clauses).
