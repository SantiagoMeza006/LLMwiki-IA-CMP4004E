---
title: "Slides 03 — Intelligent Agents"
type: source
unit: agents
raw: "raw/03_Intelligent Agents.pptx"
sources: [slides-03-intelligent-agents]
updated: 2026-09-29
---

# Slides 03 — Intelligent Agents

18 slides · Raw: `raw/03_Intelligent Agents.pptx` · Condensed version of [R&N Chapter 2](rn-ch02-intelligent-agents.md).

## What it covers

| Slide | Topic | Wiki page |
|---|---|---|
| 2 | What is an agent: sensors → processing → actuators (human, robot, software examples). ⚠️ slide text also contains a stray definition of *propositions* (copy-paste from the logic deck). | [agents-and-environments](../concepts/agents-and-environments.md) |
| 3 | 🎯 **Agent function** (abstract map percept history → action; could be a lookup table) vs **agent program** (concrete, runs on an architecture, approximates the function). "All AI design is the search for good programs that approximate the ideal function." | same |
| 4 | Vacuum world (rooms A, B; sensors: position + dirty/clean; actions Left, Right, Suck). Table of percept histories grows exponentially → intractable. | same |
| 5 | 🎯 **Rational agent**: maximises *expected* performance given percept history + built-in knowledge; explore, learn. Performance measure is external, set by the designer; "you get what you ask for". | [rationality](../concepts/rationality.md) |
| 6 | 🎯 **PEAS**: Performance, Environment, Actuators, Sensors. | [agents-and-environments](../concepts/agents-and-environments.md) |
| 8–12 | 🎯 Environment properties: fully/partially observable, deterministic/non-deterministic (stochastic), episodic/sequential, static/dynamic (semidynamic = chess with clock), discrete/continuous, single/multi-agent (competitive or cooperative). | [task-environment-properties](../concepts/task-environment-properties.md) |
| 14 | 🎯 Simple reflex agent: current percept only, condition–action rules; fails under partial observability. | [agent-architectures](../concepts/agent-architectures.md) |
| 15 | 🎯 Model-based reflex agent: internal state + "world model" (how the world evolves) + "transition model" (what my actions do). | same |
| 16 | 🎯 Goal-based agent: goals → planning/search; flexible; limitation: goals are binary. | same |
| 17 | 🎯 Utility-based agent: maximise expected utility; handles conflicting objectives (speed vs safety) and uncertainty. | same |
| 18 | 🎯 State representation: atomic / factored / structured; more expressive ⇒ more reasoning but more complexity. | [state-representations](../concepts/state-representations.md) |

## Where it fits
Unit **agents**. It is the conceptual frame for everything after: search agents are goal-based agents with atomic states; CSPs use factored states; logic/Prolog uses structured states.

> ⚠️ **Terminology (slide 15):** the slide calls the two models "world model" and "transition model". R&N (§2.4.3) calls them the **transition model** (covers *both* how the world evolves and what my actions do) and the **sensor model** (how world state shows up in percepts). See [discrepancies](../discrepancies.md).
>
> Note: the slides do not cover the **learning agent** (R&N §2.4.6); it is in the wiki from the textbook.
