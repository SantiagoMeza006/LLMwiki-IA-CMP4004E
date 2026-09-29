---
title: Rationality and Performance Measures
type: concept
unit: agents
sources: [rn-ch02-intelligent-agents, slides-03-intelligent-agents]
updated: 2026-09-29
---

# Rationality

## Definition 🎯
> For each possible percept sequence, a **rational agent** should select an action that is **expected** to maximise its **performance measure**, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has. (R&N §2.2.2)

What is rational at a given time depends on **four things**:
1. the **performance measure** (criterion of success),
2. the agent's **prior knowledge** of the environment,
3. the **actions** it can perform,
4. its **percept sequence** to date.

## Performance measure
- AI uses **consequentialism**: judge behaviour by the sequence of *environment states* it produces.
- Defined by the **designer**, external to the agent (slides-03 s.5).
- 🎯 "You get what you ask for": rewarding *amount of dirt cleaned* lets a vacuum dump dirt and re-clean it. Reward what you want in the environment (clean floor per time step), not how you think the agent should behave.
- Averages hide tradeoffs (steady mediocre vs energetic-with-breaks).
- May be unknown/uncertain → agents should learn it (links to [value alignment](what-is-ai.md#the-standard-model-and-its-limits)).

## Is the reflex vacuum agent rational? "It depends!"
Yes, **if**: +1 point per clean square per time step over 1000 steps; geography known, dirt and start unknown; actions Left/Right/Suck; perfect perception. **No**, if each move costs −1 (it oscillates forever) — better to do nothing once everything is clean; or if dirt reappears (should re-check); or if geography is unknown (should explore).

## Rationality ≠ omniscience ≠ perfection 🎯
- **Omniscient** agent knows actual outcomes — impossible.
- Rationality maximises **expected** performance; perfection maximises **actual** performance. (Crossing the street and being hit by a falling cargo door is not irrational.)
- But rational agents must do **information gathering** (look before crossing) and **exploration**.

## Learning and autonomy
- A rational agent should **learn** as much as possible from its percepts.
- **Autonomy:** relying on own percepts/learning rather than only on the designer's prior knowledge. Counter-examples: dung beetle keeps plugging the nest without the dung ball; sphex wasp repeats its routine forever when the caterpillar is moved.
- Start with some built-in knowledge + ability to learn (like evolution's reflexes).

Related: [agents-and-environments](agents-and-environments.md) · [agent-architectures](agent-architectures.md) (utility = internalised performance measure)
