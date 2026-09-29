---
title: Adversarial Search and Games
type: concept
unit: games-csp
sources: [slides-02-problem-solving]
updated: 2026-09-29
---

# Adversarial Search and Games

(Source: slides-02 s.17–22, which reproduce R&N Ch 6 figures. Ch 6 is not in our PDF excerpt.)

## Setting 🎯
- Until now: **one** agent searching in a cooperative/neutral environment. In games: **two or more agents with opposing objectives**.
- The task is no longer "find a path to the goal" but **find an optimal strategy**, assuming the opponent also plays optimally.
- Standard assumptions: two players **MAX** and **MIN**, alternating turns; **zero-sum** (one's gain is the other's loss); **perfect information** (fully observable); **deterministic** (no dice).

## Game formulation (R&N style, as used in the minimax pseudocode)
| Element | Meaning |
|---|---|
| `TO-MOVE(s)` | whose turn it is |
| `ACTIONS(s)` | legal moves |
| `RESULT(s, a)` | transition model |
| `IS-TERMINAL(s)` | game over? |
| `UTILITY(s, p)` | final payoff for player p at terminal s (e.g. +1/0/−1 or a score) |

The **game tree** alternates MAX levels (△) and MIN levels (▽); one **ply** = one move by one player.

## Algorithms
- [Minimax](../algorithms/minimax.md) — exact optimal decision, explores the whole tree: O(b^m) time.
- [Alpha–beta pruning](../algorithms/alpha-beta-pruning.md) — same decision, prunes branches that can't matter; best case O(b^(m/2)).
- Worked example on R&N Fig 6.2: [minimax-alpha-beta-trace](../exercises/minimax-alpha-beta-trace.md).

## How games relate to the environment taxonomy
Chess: fully observable, **multiagent (competitive)**, deterministic, sequential, static (semidynamic with a clock), discrete. See [task-environment-properties](task-environment-properties.md).

Related: [practice-games-and-csp](../practice/practice-games-and-csp.md)
