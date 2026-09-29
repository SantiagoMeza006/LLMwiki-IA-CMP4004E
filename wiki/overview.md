---
title: Course Overview — Artificial Intelligence (USFQ)
type: overview
unit: all
sources: [slides-01-intro-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-prolog, rn-ch01-introduction, rn-ch02-intelligent-agents, rn-ch03-search, holland-1992-genetic-algorithms, dorigo-1996-ant-system]
updated: 2026-09-29
---

# Course Overview

Instructor: Daniel Riofrío. Textbook: Russell & Norvig, *AIMA* 4th ed. (we have Ch 1–3).

## The big picture — one idea ties everything together
**AI = designing rational agents** ([what-is-ai](concepts/what-is-ai.md)). Every later unit is a way to build the agent's decision procedure for a particular kind of [task environment](concepts/task-environment-properties.md) and [state representation](concepts/state-representations.md):

```
                     Rational agent (maximise expected performance)
                                    │
   ┌──────────────┬─────────────────┼──────────────────┬──────────────────────┐
 atomic states   atomic, 2 players  factored states    structured states     solution = a point,
 1 agent, known  zero-sum           (variables)        (objects, relations)  not a path
   │               │                  │                   │                     │
 SEARCH          GAMES              CSPs               LOGIC / PROLOG        OPTIMIZATION
 BFS DFS UCS     minimax            backtracking       Horn clauses          GA  PSO
 IDS A* greedy   alpha-beta         forward checking   backward chaining     ACO ABC
                                    arc consistency    unification, SLD
```

## Units, sources and key pages

| # | Unit | Slides | Readings | Start here | Practice |
|---|---|---|---|---|---|
| 1 | Introduction & history | [01](sources/slides-01-intro-to-ai.md) | [R&N Ch 1](sources/rn-ch01-introduction.md) | [what-is-ai](concepts/what-is-ai.md), [history-of-ai](concepts/history-of-ai.md) | [practice-intro](practice/practice-intro.md) |
| 2 | Intelligent agents | [03](sources/slides-03-intelligent-agents.md) | [R&N Ch 2](sources/rn-ch02-intelligent-agents.md) | [agents-and-environments](concepts/agents-and-environments.md), [agent-architectures](concepts/agent-architectures.md) | [practice-agents](practice/practice-agents.md) |
| 3 | Problem solving & search | [02](sources/slides-02-problem-solving.md) s.1–16 | [R&N Ch 3](sources/rn-ch03-search.md), [my A* note](sources/note-a-star-vs-dijkstra.md) | [search-problem-formulation](concepts/search-problem-formulation.md), [a-star-search](algorithms/a-star-search.md) | [practice-search](practice/practice-search.md) |
| 4 | Games & CSPs | [02](sources/slides-02-problem-solving.md) s.17–25 | (R&N Ch 5–6, not in excerpt) | [adversarial-search](concepts/adversarial-search.md), [constraint-satisfaction-problems](concepts/constraint-satisfaction-problems.md) | [practice-games-and-csp](practice/practice-games-and-csp.md) |
| 5 | Optimization & bio-inspired agents | [04](sources/slides-04-optimization.md) | [Holland 1992](sources/holland-1992-genetic-algorithms.md), [Dorigo 1996](sources/dorigo-1996-ant-system.md) | [optimization-and-local-optima](concepts/optimization-and-local-optima.md), [bio-inspired comparison](comparisons/bio-inspired-algorithms-comparison.md) | [practice-optimization](practice/practice-optimization.md) |
| 6 | Logic programming (Prolog) | [XX](sources/slides-xx-prolog.md) | (R&N §7.5, §9.4, not in excerpt) | [logic-to-horn-clauses](concepts/logic-to-horn-clauses.md), [prolog](concepts/prolog.md) | [practice-logic-prolog](practice/practice-logic-prolog.md) |

Note: deck numbering puts "Problem Solving" (02) before "Intelligent Agents" (03), but conceptually agents come first — search agents are one kind of goal-based agent.

## Threads that cross units (good essay/exam material)
- **Search everywhere.** Prolog's execution is DFS ([sld-resolution](algorithms/sld-resolution.md)); CSP backtracking is DFS; minimax is DFS over a game tree; bio-inspired methods are stochastic *local/population* search.
- **Heuristics = domain knowledge.** h(n) in A*, η = 1/d in ACO, MRV in CSPs, move ordering in alpha–beta.
- **Exploration vs exploitation** — learning agents, GA, PSO, ACO, ABC ([page](concepts/exploration-vs-exploitation.md)).
- **Optimality vs cost.** A* (optimal, memory-hungry) vs weighted A*/greedy/beam/metaheuristics (fast, "good enough").
- **Same logic, different control** — clause order in Prolog, generate-and-test vs test-as-you-go, move ordering in alpha–beta, successor order in DFS.
- **Representation matters** — atomic → factored → structured; GA encoding design (Holland); ACO graph representation (Dorigo).

## Before an exam
1. Read [discrepancies](discrepancies.md) — where slides and textbook disagree.
2. Skim 🎯 markers on each unit's pages.
3. Redo the [exercises](index.md#exercises) by hand, then say "quiz me on <unit>".
