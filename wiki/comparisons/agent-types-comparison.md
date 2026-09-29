---
title: Agent Types — Comparison
type: comparison
unit: agents
sources: [rn-ch02-intelligent-agents, slides-03-intelligent-agents]
updated: 2026-09-29
---

# Agent Types — Comparison 🎯

| | Simple reflex | Model-based reflex | Goal-based | Utility-based | Learning |
|---|---|---|---|---|---|
| Decides from | current percept | internal state (percept history + models) | state + **goals**, simulating the future | state + **utility function** (expected utility) | any of the others, improved by feedback |
| Memory | none | internal state | internal state | internal state | + learned knowledge |
| Mechanism | condition–action rules | UPDATE-STATE + rules | search / planning | decision theory: maximise expected utility | critic → learning element; problem generator explores |
| Handles partial observability | ❌ (loops) | ✅ | ✅ | ✅ | ✅ |
| Distinguishes better vs worse solutions | ❌ | ❌ | ❌ (goals are binary) | ✅ | ✅ |
| Handles conflicting goals / uncertainty | ❌ | ❌ | ❌ | ✅ | ✅ |
| Flexibility to change objective | low (rewrite rules) | low | **high** (change the goal) | high (change utility) | adapts itself |
| Example | vacuum: "if Dirty then Suck" | taxi tracking cars it can't see | taxi planning a route to a destination | taxi trading off speed, safety, cost | taxi learning braking on wet roads |

Each column adds something to the previous one. Details: [agent-architectures](../concepts/agent-architectures.md).
