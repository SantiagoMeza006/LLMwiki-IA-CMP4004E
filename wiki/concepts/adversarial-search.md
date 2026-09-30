---
title: Adversarial Search and Games
type: concept
unit: games-csp
sources: [slides-02-problem-solving, rn-ch06-games]
updated: 2026-09-30
---

# Adversarial Search and Games

(Sources: [slides-02](../sources/slides-02-problem-solving.md) s.17–22 and [R&N Ch 6](../sources/rn-ch06-games.md).)

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

"Zero-sum" is traditional; **constant-sum** would be more accurate (chess outcomes sum to 1: 1 + 0 or ½ + ½) (R&N §6.1). "Perfect information" = fully observable.

## Algorithms
- [Minimax](../algorithms/minimax.md) — exact optimal decision, explores the whole tree: O(b^m) time.
- [Alpha–beta pruning](../algorithms/alpha-beta-pruning.md) — same decision, prunes branches that can't matter; best case O(b^(m/2)).
- [Heuristic alpha–beta](../algorithms/heuristic-alpha-beta.md) — cut off at a depth, apply an evaluation function (Type A strategy).
- [Monte Carlo tree search](../algorithms/monte-carlo-tree-search.md) — average many playouts, UCB1 selection (Type B, Go).
- [Expectiminimax](../algorithms/expectiminimax.md) — games with dice (chance nodes).
- Side by side: [game-algorithms-comparison](../comparisons/game-algorithms-comparison.md). Worked: [minimax-alpha-beta-trace](../exercises/minimax-alpha-beta-trace.md), [games-traces](../exercises/games-traces.md).

## Beyond the basic setting
(R&N §6.6–6.7)
- **Partially observable games** (Kriegspiel, poker, bridge): reason about **belief states** of both players; a common approximation averages over possible deals/configurations ("averaging over clairvoyance"), which fails to value information-gathering and bluffing.
- Programs beat champions at chess, checkers, Othello, Go and poker; humans kept an edge longer in bridge and Kriegspiel.
- **Limitations:** evaluation errors compound, search considers one move at a time, and good players reason about *which* computations are worth doing (**metareasoning**).

## How games relate to the environment taxonomy
Chess: fully observable, **multiagent (competitive)**, deterministic, sequential, static (semidynamic with a clock), discrete. See [task-environment-properties](task-environment-properties.md).

Related: [practice-games-and-csp](../practice/practice-games-and-csp.md)
