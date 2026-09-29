---
title: Artificial Bee Colony (ABC)
type: algorithm
unit: optimization
sources: [slides-04-optimization]
updated: 2026-09-29
---

# Artificial Bee Colony (ABC) 🎯

**Dervis Karaboga, 2007.** Swarm-intelligence method imitating the **foraging behaviour of honeybees**. Food sources = candidate solutions; nectar amount = fitness. Success depends on quickly **discovering** and efficiently **using** the best resources (slides-04 s.16–17).

## Three kinds of bees 🎯
| Bee | Role | Explore / exploit |
|---|---|---|
| **Employed** | one per food source; searches a neighbour of its source and keeps it if better | **exploitation** |
| **Onlooker** | waits in the hive, picks sources **with probability proportional to fitness** (from employed bees' "dances"), then searches near them | **exploitation** |
| **Scout** | replaces a source that hasn't improved for `limit` trials with a **random** new source | **exploration** |

## Parameters (slides-04 s.18)
- Number of food sources = number of employed bees (**BN**) = number of onlooker bees (**SN**) — the slide uses both symbols.
- **limit** — trials without improvement before a source is abandoned.
- **MCN** — maximum number of cycles.
- *Recruitment rate*: how fast the colony finds and exploits a new source ≈ how fast good solutions are discovered.

## Neighbour (candidate) generation 🎯
```
v_ij = x_ij + φ_ij · (x_ij − x_kj)
```
- `i` = current source, `j ∈ {1..D}` a random dimension, `k ∈ {1..BN}` a random **other** source (k ≠ i),
- `φ_ij` random in **[−1, 1]**.
Greedy selection: keep v_i if it's better than x_i, otherwise increment x_i's trial counter.

Onlooker selection probability (standard ABC, not on the slide): `p_i = fit_i / Σ_n fit_n`.

## Main loop (slides-04 s.19)
```
Initialise.
REPEAT
   (a) Place the employed bees on the food sources in memory;
   (b) Place the onlooker bees on the food sources in memory;
   (c) Send the scouts to the search area to discover new food sources.
UNTIL (requirements are met)
```

Compare: [bio-inspired-algorithms-comparison](../comparisons/bio-inspired-algorithms-comparison.md) · [exploration-vs-exploitation](../concepts/exploration-vs-exploitation.md)
