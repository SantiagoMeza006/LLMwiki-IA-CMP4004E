---
title: "R&N Chapter 2 — Intelligent Agents"
type: source
unit: agents
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch02-intelligent-agents]
updated: 2026-09-29
---

# R&N Chapter 2 — Intelligent Agents (pp. 54–80)

The textbook behind [slides-03](slides-03-intelligent-agents.md). Read this for the precise definitions.

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 2.1 | Agent, sensors, actuators, percept, **percept sequence**, **agent function** vs **agent program**; vacuum world (Fig 2.2) and its tabulated agent function (Fig 2.3). | [agents-and-environments](../concepts/agents-and-environments.md) |
| 2.2 | Performance measure, consequentialism; rationality depends on 4 things; definition of rational agent; rationality ≠ omniscience ≠ perfection; information gathering; learning; autonomy (dung beetle, sphex wasp). | [rationality](../concepts/rationality.md) |
| 2.3 | Task environment, **PEAS** (taxi Fig 2.4; more in Fig 2.5); 7 properties + known/unknown; Fig 2.6 examples table. | [task-environment-properties](../concepts/task-environment-properties.md), [environment-examples](../comparisons/environment-examples.md) |
| 2.4.1 | agent = architecture + program; TABLE-DRIVEN-AGENT is doomed: Σ_{t=1..T} \|P\|^t entries (chess ≥ 10^150). | [agent-architectures](../concepts/agent-architectures.md) |
| 2.4.2–2.4.5 | Simple reflex, model-based reflex (transition model + sensor model), goal-based, utility-based (expected utility). | same, [agent-types-comparison](../comparisons/agent-types-comparison.md) |
| 2.4.6 | Learning agent: performance element, learning element, critic, problem generator. | same |
| 2.4.7 | Atomic / factored / structured representations; expressiveness; localist vs distributed. | [state-representations](../concepts/state-representations.md) |

## Most quotable lines (paraphrased)
- A rational agent selects, for each percept sequence, the action expected to maximise its performance measure given the percepts and built-in knowledge.
- "It is better to design performance measures according to what one actually wants... rather than according to how one thinks the agent should behave." (vacuum that dumps dirt to re-clean it)
- Rationality maximises **expected** performance; perfection maximises **actual** performance.
- Hardest environment: partially observable, multiagent, nondeterministic, sequential, dynamic, continuous, unknown.
