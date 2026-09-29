---
title: Agent Architectures (Reflex, Model-Based, Goal, Utility, Learning)
type: concept
unit: agents
sources: [rn-ch02-intelligent-agents, slides-03-intelligent-agents]
updated: 2026-09-29
---

# Agent Architectures (agent program types)

Five skeletons in order of sophistication (R&N §2.4.2–2.4.6). Quick side-by-side: [agent-types-comparison](../comparisons/agent-types-comparison.md).

## 1. Simple reflex agent 🎯
- Acts on the **current percept only**, ignoring history, through **condition–action rules** (`if car-in-front-is-braking then initiate-braking`).
- ```
  function SIMPLE-REFLEX-AGENT(percept):
      state  ← INTERPRET-INPUT(percept)
      rule   ← RULE-MATCH(state, rules)
      return rule.ACTION
  ```
- ✅ Simple, efficient (can be a Boolean circuit). ❌ Works only if the environment is **fully observable**; infinite loops under partial observability (vacuum without location sensor). **Randomising** (coin flip on [Clean]) can escape loops — reaches the other square in 2 steps on average.

## 2. Model-based reflex agent 🎯
- Keeps **internal state** tracking the unobserved part of the world, updated with:
  - **Transition model** — how the world evolves on its own *and* what the agent's actions do;
  - **Sensor model** — how world state shows up in percepts.
- ```
  state ← UPDATE-STATE(state, action, percept, transition_model, sensor_model)
  rule  ← RULE-MATCH(state, rules); action ← rule.ACTION
  ```
- The state is a **best guess**; uncertainty may remain, but the agent must still act.
- > ⚠️ Slides-03 s.15 name the two models "world model" (how the environment evolves) and "transition model" (how my actions affect it). R&N folds both into the *transition model* and adds the *sensor model*. See [discrepancies](../discrepancies.md).

## 3. Goal-based agent 🎯
- Adds **goals** (desirable states); considers the **future** ("what happens if I do A?"). Requires **search** and **planning**.
- More flexible: change the destination and behaviour changes, no rules rewritten.
- ❌ Goals are **binary** (happy/unhappy) — can't tell better from worse ways to reach the goal.

## 4. Utility-based agent 🎯
- **Utility function** = internalisation of the performance measure; ranks states by "how happy".
- Chooses the action maximising **expected utility** (average over outcomes weighted by probability).
- Handles (a) **conflicting goals** (speed vs safety) and (b) several goals none certain (weigh likelihood vs importance).
- Any rational agent must behave *as if* it maximises an expected utility (R&N Ch 15).

## 5. Learning agent (R&N only; not in slides)
Four components:
| Component | Role |
|---|---|
| **Performance element** | what we called "the agent" — picks actions |
| **Learning element** | improves the performance element using feedback |
| **Critic** | judges behaviour against a **fixed, external performance standard** (percepts alone don't say if you did well) |
| **Problem generator** | suggests **exploratory** actions (experiments), trading short-term performance for learning — see [exploration-vs-exploitation](exploration-vs-exploitation.md) |

Any of types 1–4 can be built as a learning agent. Learning = modifying each component to agree better with feedback.

## Connection to the rest of the course
- Search agents (Ch 3) = goal-based, atomic states → [search-problem-formulation](search-problem-formulation.md).
- Game agents use utility on terminal states → [minimax](../algorithms/minimax.md).
- Bio-inspired optimisers maximise a fitness (utility-like) function → [optimization-and-local-optima](optimization-and-local-optima.md).

Related: [state-representations](state-representations.md) · [rationality](rationality.md)
