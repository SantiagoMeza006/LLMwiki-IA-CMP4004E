---
title: Task Environment Examples (R&N Fig 2.6)
type: comparison
unit: agents
sources: [rn-ch02-intelligent-agents]
updated: 2026-09-29
---

# Task Environment Examples 🎯

| Task environment | Observable | Agents | Deterministic | Episodic | Static | Discrete |
|---|---|---|---|---|---|---|
| Crossword puzzle | Fully | Single | Deterministic | Sequential | Static | Discrete |
| Chess with a clock | Fully | Multi | Deterministic | Sequential | **Semi** | Discrete |
| Poker | Partially | Multi | Stochastic | Sequential | Static | Discrete |
| Backgammon | Fully | Multi | Stochastic | Sequential | Static | Discrete |
| Taxi driving | Partially | Multi | Stochastic | Sequential | Dynamic | Continuous |
| Medical diagnosis | Partially | Single | Stochastic | Sequential | Dynamic | Continuous |
| Image analysis | Fully | Single | Deterministic | **Episodic** | Semi | Continuous |
| Part-picking robot | Partially | Single | Stochastic | **Episodic** | Dynamic | Continuous |
| Refinery controller | Partially | Single | Stochastic | Sequential | Dynamic | Continuous |
| English tutor | Partially | Multi | Stochastic | Sequential | Dynamic | Discrete |

Notes:
- No "known/unknown" column — it describes the agent's knowledge, not the environment.
- Properties are not always clear-cut: medical diagnosis is episodic if it's "pick a diagnosis from symptoms", sequential if it involves tests and treatment over time; multiagent if you model difficult patients/staff.

## More to classify (my additions for practice — answers are arguable, justify them)
| Task | Suggested answer |
|---|---|
| 8-puzzle solver | Fully, single, deterministic, sequential, static, discrete |
| Sudoku (CSP) | Fully, single, deterministic, sequential, static, discrete |
| Vacuum world (R&N basic) | Partially (local dirt sensor) or fully (2 squares with location sensor), single, deterministic, sequential, static, discrete |
| Spam filter | Partially, single (or multi: spammers adapt), stochastic, episodic, static, discrete |
| Ant colony solving TSP | Fully (graph known), multi (cooperative), stochastic, sequential, static, discrete |

Concepts: [task-environment-properties](../concepts/task-environment-properties.md).
