---
title: Simulated Annealing
type: algorithm
unit: optimization
sources: [rn-ch04-complex-environments, dorigo-1996-ant-system]
updated: 2026-09-30
---

# Simulated Annealing 🎯

## Idea
Hill climbing never goes downhill → stuck on local maxima. A pure random walk eventually finds the global optimum but is hopelessly slow. **Simulated annealing combines them**: pick a **random** move; always accept improvements; accept a worse move with a probability that shrinks with (a) how much worse it is and (b) the **temperature T**, which decreases over time. Metaphor: metallurgical annealing / shaking a bumpy tray so a ping-pong ball lands in the deepest hole — shake hard first, then gently.

## Pseudocode (R&N Fig 4.5, cost-minimisation view)
```
function SIMULATED-ANNEALING(problem, schedule) returns a solution state
    current ← problem.INITIAL
    for t = 1 to ∞:
        T ← schedule(t)
        if T = 0: return current
        next ← a randomly selected successor of current
        ΔE ← VALUE(current) − VALUE(next)        # VALUE is a cost here: ΔE > 0 means next is better
        if ΔE > 0: current ← next
        else: current ← next only with probability e^(ΔE/T)
```
In the **maximisation** form (R&N 3rd ed. and most courses) ΔE = VALUE(next) − VALUE(current) with the same rule. Either way: **bad move ⇒ ΔE < 0 ⇒ acceptance probability e^(ΔE/T) ∈ (0, 1)**.

## Acceptance probability e^(ΔE/T)
| ΔE (how much worse) | T = 10 | T = 5 | T = 1 | T = 0.5 |
|---|---|---|---|---|
| −1 | 0.905 | 0.819 | 0.368 | 0.135 |
| −2 | 0.819 | 0.670 | 0.135 | 0.018 |
| −5 | 0.607 | 0.368 | 0.007 | ≈ 0 |

(Computed in code.) High T ≈ random walk (exploration); T → 0 ≈ hill climbing (exploitation).

## Properties
- If the schedule lowers T **slowly enough**, the Boltzmann distribution concentrates on the global maxima → finds a global optimum with probability approaching 1 (R&N).
- In practice the cooling schedule is a tuning problem; a common choice is geometric cooling T(t+1) = a·T(t), e.g. a = 0.99 (the schedule Dorigo 1996 used for its SA baseline).
- Uses O(1) memory.
- Applications: VLSI layout (since the 1980s), factory scheduling, large-scale optimization.
- In Dorigo 1996's comparison on Oliver30, SA did worse than Ant System and tabu search under the same one-hour budget (best 422, average 459.8 vs AS 420/420.4).

## Common mistakes
- Accepting *all* improving moves **and** deciding downhill ones with the same formula — correct; but forgetting that the probability depends on **both** ΔE and T.
- Cooling too fast = hill climbing with extra steps.

Related: [hill-climbing](hill-climbing.md) · [exploration-vs-exploitation](../concepts/exploration-vs-exploitation.md) · [local-search-traces](../exercises/local-search-traces.md)
