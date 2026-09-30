---
title: Knowledge-Based Agents and the Wumpus World
type: concept
unit: logic
sources: [rn-ch07-logical-agents]
updated: 2026-09-30
---

# Knowledge-Based Agents 🎯

(R&N §7.1–7.2, 7.7; [source](../sources/rn-ch07-logical-agents.md).) The agent type that logic — and Prolog — is built for.

## Structure
- **Knowledge base (KB):** a set of **sentences** in a **knowledge representation language**. Sentences taken as given = **axioms**.
- **TELL** adds sentences, **ASK** queries; both may use **inference** (deriving new sentences). Answers must *follow* from what was TELLed.
```
function KB-AGENT(percept) returns an action
    persistent: KB, t (time counter, initially 0)
    TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
    action ← ASK(KB, MAKE-ACTION-QUERY(t))
    TELL(KB, MAKE-ACTION-SENTENCE(action, t))
    t ← t + 1
    return action
```
- Describable at the **knowledge level** (what it knows and wants) independent of the **implementation level** (data structures).
- **Declarative** approach: build the agent by TELLing it knowledge — vs **procedural** (code the behaviour). Real systems mix both. Prolog = declarative programming ([prolog](prolog.md)).

## The wumpus world (PEAS)
| | |
|---|---|
| **P** | +1000 climb out with gold, −1000 fall in a pit / eaten, −1 per action, −10 for using the arrow |
| **E** | 4×4 grid, start [1,1] facing east; gold and wumpus uniformly at random (not [1,1]); each other square is a pit with P = 0.2 |
| **A** | Forward, TurnLeft, TurnRight, Grab, Shoot (one arrow), Climb (only at [1,1]) |
| **S** | Stench (next to wumpus), Breeze (next to pit), Glitter (gold here), Bump (wall), Scream (wumpus killed) → percept `[Stench, Breeze, None, None, None]` |

Properties: deterministic, discrete, static, single-agent, **sequential**, **partially observable**. ~21% of worlds are unfair (gold in or surrounded by pits).

**Informal reasoning (Figs 7.3–7.4):** nothing in [1,1] → [1,2], [2,1] OK. Breeze in [2,1] → pit in [2,2] or [3,1]. Stench in [1,2], no stench earlier in [2,1] → wumpus in [1,3] (W!). No breeze in [1,2] → no pit in [2,2] → pit in [3,1] (P!). Conclusions from correct information are **guaranteed correct** — the key property of logical reasoning. Formalised in [propositional-logic](propositional-logic.md) and [logic-inference-traces](../exercises/logic-inference-traces.md).

## Limits of propositional agents
(R&N §7.7)
- Things that change are **fluents** (e.g. L^t_{x,y}, agent at [x,y] at time t) → symbols multiply per time step.
- **Frame problem:** stating what does *not* change after each action; frame axioms need O(m·n) sentences for m actions and n fluents → **successor-state axioms**: `F^{t+1} ⇔ ActionCausesF^t ∨ (F^t ∧ ¬ActionCausesNotF^t)`.
- Logical state estimation and **SATPLAN** (planning as satisfiability) work, but propositional logic lacks the power to say "for all squares" concisely → [first-order-logic](first-order-logic.md).

Related: [agent-architectures](agent-architectures.md) (a KB agent is a model-based/goal-based agent with an explicit, declarative model) · [state-representations](state-representations.md)
