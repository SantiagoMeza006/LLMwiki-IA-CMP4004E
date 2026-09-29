---
title: Problem-Solving Agents and Problem Formulation
type: concept
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# Problem-Solving Agents and Problem Formulation

## Problem-solving agent 🎯
A **goal-based agent** that plans a *sequence* of actions before acting (slides-02 s.2). It uses **atomic** states ([state-representations](state-representations.md)). Assumes the environment is fully observable, deterministic, discrete, static (and known).

**Four phases** (R&N §3.1):
1. **Goal formulation** — adopt a goal (reach Bucharest); limits what to consider.
2. **Problem formulation** — decide which states and actions to model (abstraction).
3. **Search** — simulate action sequences in the model until one reaches the goal → a **solution**.
4. **Execution** — carry out the actions.

In a fully observable, deterministic, known environment the solution is a **fixed sequence**, so execution can ignore percepts — an **open-loop** system. If the model may be wrong or the world nondeterministic, use **closed-loop** execution (monitor percepts); in partially observable/nondeterministic worlds a solution becomes a *branching strategy* (contingency plan).

## Formal definition of a search problem 🎯
| Component | Meaning | Romania example |
|---|---|---|
| **States / state space** | set of possible environment states | 20 cities |
| **Initial state** | where the agent starts | `Arad` |
| **Goal states / IS-GOAL(s)** | one goal, a set, or a property | `Bucharest` |
| **ACTIONS(s)** | finite set of actions *applicable* in s | `{ToSibiu, ToTimisoara, ToZerind}` |
| **Transition model RESULT(s, a) → s'** | what each action does | `RESULT(Arad, ToZerind) = Zerind` |
| **ACTION-COST(s, a, s')** / `c(s,a,s')` | numeric cost; should reflect the performance measure | road distance in miles |

- **Path** = sequence of actions; **solution** = path from initial state to a goal; costs are **additive**; **optimal solution** = lowest path cost. Chapter 3 assumes all costs > 0 (negative cycles would make "optimal" undefined).
- The state space is a **graph**: vertices = states, directed edges = actions (each road = 2 actions).

## Abstraction
- Removing detail from a representation. A good formulation has the right **level of abstraction**.
- **Valid** if every abstract solution can be expanded into a detailed one; **useful** if each abstract action is easier than the original problem (driving Arad→Sibiu needs no further planning).
- "Move the right foot one centimetre" would be far too fine-grained.

Examples of formulations: [example-search-problems](example-search-problems.md). Next: [state-space-and-search-tree](state-space-and-search-tree.md).

Related: [agent-architectures](agent-architectures.md) · [practice-search](../practice/practice-search.md)
