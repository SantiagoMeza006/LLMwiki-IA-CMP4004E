---
title: Properties of Task Environments
type: concept
unit: agents
sources: [rn-ch02-intelligent-agents, slides-03-intelligent-agents]
updated: 2026-09-29
---

# Properties of Task Environments 🎯

| Dimension | Question to ask (slides-03) | Notes (R&N §2.3.2) |
|---|---|---|
| **Fully vs partially observable** (vs *unobservable*) | Can sensors access the complete *relevant* state at every moment? Does the agent need memory/state estimation? | "Effectively fully observable" if sensors capture everything relevant to the action choice. Partial: noisy sensors, missing info (local dirt sensor; other drivers' intentions). No sensors ⇒ unobservable. |
| **Single vs multiagent** | Are there other agents? Competitive or cooperative? | B is an *agent* if its behaviour is best described as maximising a performance measure that depends on A's behaviour. Chess = competitive; taxi = partially cooperative (avoid collisions) + partially competitive (parking spot). Randomisation can be rational in competitive settings. |
| **Deterministic vs nondeterministic** | Is the next state fully determined by current state + action? | Partial observability can make a deterministic env *appear* nondeterministic. R&N distinguishes **stochastic** (explicit probabilities, "25% chance of rain") from **nondeterministic** (possibilities listed, not quantified). Slides use "stochastic" loosely for "same input, different outputs due to randomness". |
| **Episodic vs sequential** | Is each percept–action episode independent? | Classification on an assembly line = episodic. Chess, taxi = sequential (short-term actions have long-term consequences). |
| **Static vs dynamic** (and *semidynamic*) | Does the world change while the agent deliberates? | Dynamic: not deciding = deciding to do nothing. **Semidynamic:** world doesn't change but the *score* does (chess with a clock). Crossword = static. |
| **Discrete vs continuous** | Finite well-defined states, percepts, actions? Time? | Applies to state, time, percepts, actions. Chess discrete; taxi continuous (state, time, actions). |
| **Known vs unknown** | (R&N only) Does the agent know the "laws of physics" (outcomes/probabilities of actions)? | Not a property of the environment itself but of the agent's knowledge. Known but partially observable: solitaire. Unknown but fully observable: new video game. |

**Hardest case:** partially observable, multiagent, nondeterministic, sequential, dynamic, continuous, unknown. Taxi driving is all of these except (mostly) known.

See the full example table: [environment-examples](../comparisons/environment-examples.md).

**Why it matters:** the properties decide the agent design — e.g. [problem-solving search](search-problem-formulation.md) (Ch 3) assumes episodic*, single-agent, fully observable, deterministic, static, discrete, known. (*R&N §3 intro literally lists "episodic", though planning a sequence is inherently sequential — the point is that the world holds still.) Adversarial search drops "single-agent"; CSPs keep the rest but use factored states.

Related: [agents-and-environments](agents-and-environments.md) · [agent-architectures](agent-architectures.md)
