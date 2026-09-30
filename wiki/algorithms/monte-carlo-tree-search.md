---
title: Monte Carlo Tree Search (MCTS)
type: algorithm
unit: games-csp
sources: [rn-ch06-games]
updated: 2026-09-30
---

# Monte Carlo Tree Search (MCTS)

(R&N §6.4.) Why: Go's branching factor starts at **361** (alpha–beta reaches only 4–5 ply) and good evaluation functions are hard to write. MCTS estimates a state's value as the **average result of many simulated games (playouts / rollouts)** from it — no evaluation function needed, only the rules.

## Ingredients
- **Playout policy:** how moves are chosen during a simulation (random, game heuristics, or a neural net learned by self-play).
- **Selection policy:** where to spend playouts — balances **exploitation** (nodes with good results) and **exploration** (nodes with few playouts).
- *Pure Monte Carlo search* = N playouts from the root only; usually not enough.

## The four steps (repeat while time remains) 🎯
1. **Selection** — from the root, follow the selection policy down the tree to a leaf.
2. **Expansion** — add a new child of that leaf.
3. **Simulation** — play out from the child to the end with the playout policy (moves not stored in the tree).
4. **Back-propagation** — update win/playout counts on the path back to the root (winners' nodes get +1 win and +1 playout; losers' nodes +1 playout).

```
function MONTE-CARLO-TREE-SEARCH(state) returns an action
    tree ← NODE(state)
    while IS-TIME-REMAINING():
        leaf ← SELECT(tree)
        child ← EXPAND(leaf)
        result ← SIMULATE(child)
        BACK-PROPAGATE(result, child)
    return the move in ACTIONS(state) whose node has highest number of playouts
```

## UCT / UCB1 selection 🎯
```
UCB1(n) = U(n)/N(n) + C · sqrt( log N(PARENT(n)) / N(n) )
          exploitation      exploration
```
U(n) = total utility (wins) of playouts through n; N(n) = number of playouts through n. Theory suggests C = √2; in practice C is tuned.
Example (R&N Fig 6.10, parent N = 100; verified in code):
| Node | U/N | UCB1, C = 1.4 | UCB1, C = 1.5 |
|---|---|---|---|
| 60/79 | 0.759 | **1.098** ← chosen | 1.122 |
| 1/10 | 0.100 | 1.050 | 1.118 |
| 2/11 | 0.182 | 1.088 | **1.152** ← chosen |

**Return the most-played move**, not the best average: 65/100 is more trustworthy than 2/3.

## Properties
- Playout cost is **linear** in game length (one move per ply). With b = 32, 100-ply games and a budget of 10⁹ states: minimax ≈ 6 ply, alpha–beta (perfect ordering) ≈ 12 ply, MCTS ≈ 10 million playouts.
- ✅ Huge b, no good evaluation function, brand-new games; robust to a single bad estimate (aggregates many playouts).
- ❌ Can miss a single critical move (stochastic Type B pruning); slow to confirm "obvious" wins.
- Hybrids: truncate playouts with an evaluation function; **early playout termination**. AlphaGo/AlphaZero combine MCTS with neural networks (AlphaZero adds move probabilities to UCB).
- Handles chance naturally (random dice in playouts) → alternative to [expectiminimax](expectiminimax.md).
- It is a form of **reinforcement learning** (simulate, observe outcomes, prefer good moves).

Related: [exploration-vs-exploitation](../concepts/exploration-vs-exploitation.md) · [game-algorithms-comparison](../comparisons/game-algorithms-comparison.md) · [games-traces](../exercises/games-traces.md)
