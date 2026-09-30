---
title: Search with Nondeterminism, Partial Observability and Unknown Environments
type: concept
unit: search
sources: [rn-ch04-complex-environments]
updated: 2026-09-30
---

# Beyond Classical Search: Nondeterminism, Partial Observability, Online Search

(R&N §4.3–4.5. Not on the slides — useful for understanding *why* the Ch 3 assumptions matter, and for the AND–OR idea reused by Prolog.)

## Nondeterministic actions (§4.3)
- **RESULTS(s, a)** returns a **set** of possible outcomes. *Erratic vacuum*: Suck on a dirty square sometimes also cleans the neighbour; on a clean square it sometimes deposits dirt → RESULTS(1, Suck) = {5, 7}.
- A solution is a **conditional plan** (contingency plan / strategy), e.g. `[Suck, if State = 5 then [Right, Suck] else []]` — a **tree**, not a sequence.
- **AND–OR search tree:** **OR nodes** = the agent chooses an action; **AND nodes** = every possible outcome must be handled. A solution subtree has a goal at every leaf, one action per OR node, all branches at every AND node.
- AND-OR-SEARCH is recursive DFS; returns failure on a cycle on the current path (a non-cyclic solution, if any, is reachable from the earlier copy).
- **Cyclic plans** ("try, try again"): slippery vacuum → `[Suck, while State = 5 do Right, Suck]`. Valid only if the failure is random and independent (not a snapped drive belt).

## Partial observability (§4.4)
- **Belief state** = set of physical states the agent might be in.
- **Sensorless (conformant) problems:** no percepts at all; search in belief-state space (2^N belief states). Vacuum: from {1..8}, `[Right, Suck, Left, Suck]` **coerces** the world into goal state 7. Solutions are sequences (percepts are predictable: always empty).
- With percepts: **prediction** (apply action to the belief state) → **possible percepts** → **update** (filter by the observed percept). Use AND–OR search over belief states; the agent keeps its belief state updated as it acts (state estimation).

## Online search in unknown environments (§4.5)
- The agent must act to learn what its actions do (exploration). Performance measured by the **competitive ratio** (actual cost / cost if the space were known).
- Needs **safely explorable** spaces (no dead ends / irreversible actions).
- A random walk eventually works but may take exponentially many steps.
- **LRTA\*** (learning real-time A\*): keeps a table H(s) of cost estimates, updates H(s) from its neighbours' estimates as it moves, and uses **optimism under uncertainty** (untried actions assumed cheapest) → guaranteed to find a goal in any finite, safely explorable environment.

## Connections
- The AND–OR graph here is the same structure as the **proof tree of backward chaining** in Prolog (OR = which clause, AND = all body goals) → [forward-and-backward-chaining](forward-and-backward-chaining.md), [sld-resolution](../algorithms/sld-resolution.md).
- Belief states link to [task-environment-properties](task-environment-properties.md) (partially observable) and to the model-based agent's internal state ([agent-architectures](agent-architectures.md)).
- Exploration vs exploitation again: [exploration-vs-exploitation](exploration-vs-exploitation.md).
