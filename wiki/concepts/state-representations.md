---
title: State Representations (Atomic, Factored, Structured)
type: concept
unit: agents
sources: [rn-ch02-intelligent-agents, slides-03-intelligent-agents, rn-ch03-search]
updated: 2026-09-29
---

# State Representations 🎯

Axis of **increasing expressiveness** (R&N §2.4.7; slides-03 s.18):

| Representation | A state is... | Example (driving) | Used by |
|---|---|---|---|
| **Atomic** | an indivisible black box; can only be compared equal/different | "in Arad" | search & games (Ch 3, 4, 6), HMMs, MDPs |
| **Factored** | a fixed set of **variables/attributes** with values (Boolean, real, symbol) | fuel level, GPS coords, oil light, money for tolls, radio station | **CSPs** (Ch 5), propositional logic (Ch 7), planning, Bayesian networks, many ML algorithms |
| **Structured** | **objects** with attributes and **relationships** among them | "truck reversing into dairy-farm driveway, blocked by loose cow" | relational DBs, **first-order logic** (Ch 8–9) → **Prolog**, NLP |

- Two factored states can share some attributes — easier to reason about turning one into another; two atomic states share nothing.
- More expressive ⇒ more **concise** (chess rules: 1–2 pages in FOL, thousands of pages in propositional logic, ~10^38 pages as a finite automaton) **but** reasoning and learning get more **complex**. Real systems may use all levels at once.
- Second axis: **localist** (one concept ↔ one memory location) vs **distributed** (concept spread over many locations; robust to noise — flipping a few bits lands on a similar meaning).

## Where each appears in this course
- Atomic → [search-problem-formulation](search-problem-formulation.md): problem-solving agents treat states as wholes.
- Factored → [constraint-satisfaction-problems](constraint-satisfaction-problems.md): "in a CSP, states have internal structure" (slides-02 s.23).
- Structured → [prolog](prolog.md): terms like `parent(hector, ana)` describe objects and relations.

Related: [agent-architectures](agent-architectures.md)
