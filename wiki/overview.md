---
title: Course Overview — Artificial Intelligence (USFQ)
type: overview
unit: all
sources: [slides-01-intro-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-prolog, rn-ch01-introduction, rn-ch02-intelligent-agents, rn-ch03-search, holland-1992-genetic-algorithms, dorigo-1996-ant-system, rn-ch04-complex-environments, rn-ch05-csp, rn-ch06-games, rn-ch07-logical-agents, rn-ch08-first-order-logic, rn-ch09-fol-inference]
updated: 2026-09-30
---

# Course Overview

Instructor: Daniel Riofrío. Textbook: Russell & Norvig, *AIMA* 4th ed. — full book in `raw/`; **Ch 1–9 ingested** (everything the slides cover so far).

## The big picture — one idea ties everything together
**AI = designing rational agents** ([what-is-ai](concepts/what-is-ai.md)). Every later unit is a way to build the agent's decision procedure for a particular kind of [task environment](concepts/task-environment-properties.md) and [state representation](concepts/state-representations.md):

```
                          Rational agent (maximise expected performance)
                                         │
   ┌──────────────┬──────────────────────┼──────────────────────┬──────────────────────────┐
 atomic states   atomic, 2+ players     factored states        structured states         solution = a state,
 1 agent, known  (adversarial)          (variables)            (objects, relations)      not a path
   │               │                      │                       │                         │
 SEARCH          GAMES                  CSPs                   LOGIC / PROLOG            LOCAL SEARCH & OPTIMIZATION
 BFS DFS UCS     minimax, alpha-beta    backtracking, MRV      propositional & FOL       hill climbing, SA, beam
 IDS A* greedy   eval functions, MCTS   forward checking, AC-3 resolution, chaining      GA, PSO, ACO, ABC
 (R&N Ch 3)      expectiminimax (Ch 6)  min-conflicts (Ch 5)   unification, SLD (Ch 7–9) (R&N Ch 4 + papers)
```

## Units, sources and key pages

| # | Unit | Slides | Readings | Start here | Practice |
|---|---|---|---|---|---|
| 1 | Introduction & history | [01](sources/slides-01-intro-to-ai.md) | [R&N Ch 1](sources/rn-ch01-introduction.md) | [what-is-ai](concepts/what-is-ai.md), [history-of-ai](concepts/history-of-ai.md) | [practice-intro](practice/practice-intro.md) |
| 2 | Intelligent agents | [03](sources/slides-03-intelligent-agents.md) | [R&N Ch 2](sources/rn-ch02-intelligent-agents.md) | [agents-and-environments](concepts/agents-and-environments.md), [agent-architectures](concepts/agent-architectures.md) | [practice-agents](practice/practice-agents.md) |
| 3 | Problem solving & search | [02](sources/slides-02-problem-solving.md) s.1–16 | [R&N Ch 3](sources/rn-ch03-search.md), [my A* note](sources/note-a-star-vs-dijkstra.md); optional [Ch 4 §4.3–4.5](sources/rn-ch04-complex-environments.md) | [search-problem-formulation](concepts/search-problem-formulation.md), [a-star-search](algorithms/a-star-search.md), [heuristics](concepts/heuristics.md) | [practice-search](practice/practice-search.md) |
| 4 | Games & CSPs | [02](sources/slides-02-problem-solving.md) s.17–25 | [R&N Ch 5](sources/rn-ch05-csp.md), [R&N Ch 6](sources/rn-ch06-games.md) | [adversarial-search](concepts/adversarial-search.md), [constraint-satisfaction-problems](concepts/constraint-satisfaction-problems.md), [game-algorithms-comparison](comparisons/game-algorithms-comparison.md) | [practice-games-and-csp](practice/practice-games-and-csp.md) |
| 5 | Optimization & bio-inspired agents | [04](sources/slides-04-optimization.md) | [R&N Ch 4 §4.1–4.2](sources/rn-ch04-complex-environments.md), [Holland 1992](sources/holland-1992-genetic-algorithms.md), [Dorigo 1996](sources/dorigo-1996-ant-system.md) | [local-search](concepts/local-search.md), [optimization-and-local-optima](concepts/optimization-and-local-optima.md), [local-search-comparison](comparisons/local-search-comparison.md) | [practice-optimization](practice/practice-optimization.md) |
| 6 | Logic & logic programming (Prolog) | [XX](sources/slides-xx-prolog.md) | [R&N Ch 7](sources/rn-ch07-logical-agents.md) (§7.5), [Ch 8](sources/rn-ch08-first-order-logic.md), [Ch 9](sources/rn-ch09-fol-inference.md) (§9.4) | [propositional-logic](concepts/propositional-logic.md), [first-order-logic](concepts/first-order-logic.md), [logic-to-horn-clauses](concepts/logic-to-horn-clauses.md), [prolog](concepts/prolog.md), [inference-methods-comparison](comparisons/inference-methods-comparison.md) | [practice-logic-prolog](practice/practice-logic-prolog.md) |

Note: deck numbering puts "Problem Solving" (02) before "Intelligent Agents" (03), but conceptually agents come first — search agents are one kind of goal-based agent. The slides skip R&N Ch 4 as a chapter, but its §4.1 (local search) is the textbook foundation of slides-04.

## Threads that cross units (good essay/exam material)
- **Search everywhere.** Prolog's execution is DFS ([sld-resolution](algorithms/sld-resolution.md)); CSP backtracking is DFS; minimax is DFS over a game tree; DPLL is backtracking over models; local search and bio-inspired methods are stochastic *local/population* search.
- **AND–OR structure.** Nondeterministic planning (R&N §4.3), game trees (MAX/MIN), and backward-chaining proofs all alternate "choose one" and "handle all" nodes.
- **Heuristics = domain knowledge.** h(n) in A* (relaxed problems, pattern databases), EVAL in games, η = 1/d in ACO, MRV/LCV in CSPs, move ordering in alpha–beta, unit-clause/pure-symbol in DPLL.
- **Exploration vs exploitation** — learning agents, simulated annealing, GA, PSO, ACO, ABC, MCTS/UCB1, LRTA* ([page](concepts/exploration-vs-exploitation.md)).
- **Optimality vs cost.** A* (optimal, memory-hungry) vs weighted A*/greedy/beam/local search/metaheuristics (fast, "good enough"); complete DPLL vs incomplete WalkSAT; exact minimax vs heuristic alpha–beta/MCTS.
- **Remembering the past.** `reached` set in graph search ↔ transposition tables in games ↔ tabling in Prolog ↔ no-goods in CSPs/SAT.
- **Same logic, different control** — clause order in Prolog, generate-and-test vs test-as-you-go, move ordering in alpha–beta, successor order in DFS.
- **Representation matters** — atomic → factored → structured; GA encoding design (Holland, R&N schemas); ACO graph representation (Dorigo); propositional vs first-order logic.

## Before an exam
1. Read [discrepancies](discrepancies.md) — where slides and textbook disagree.
2. Skim 🎯 markers on each unit's pages.
3. Redo the [exercises](index.md#exercises) by hand, then say "quiz me on <unit>".
