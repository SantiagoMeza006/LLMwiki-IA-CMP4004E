---
title: "Exercise — BFS, DFS and IDS traces"
type: exercise
unit: search
sources: [rn-ch03-search, slides-02-problem-solving]
updated: 2026-09-29
---

# BFS, DFS and IDS Traces

## A. Binary tree (R&N Figs 3.8, 3.11, 3.13), goal = M
```
                 A
           B           C
        D     E     F     G
       H I   J K   L M   N O
```
| Algorithm | Expansion order until M is found |
|---|---|
| **BFS** (FIFO) | A, B, C, D, E, F — with the early goal test M is detected when F generates it (L, **M**) |
| **DFS** (LIFO, left child first) | A, B, D, H, I, E, J, K, C, F, L, **M** |
| **IDS** | ℓ=0: A · ℓ=1: A, B, C · ℓ=2: A, B, D, E, C, F, G · ℓ=3: A, B, D, H, I, E, J, K, C, F, L, **M** |

Notice: DFS explored the whole left half first; IDS re-generates upper levels on every iteration but stays O(b·d) in memory.

## B. Romania, Arad → Bucharest, successors in alphabetical order (verified in code)
| Algorithm | Nodes expanded | Path returned | Cost | Optimal? |
|---|---|---|---|---|
| BFS (early goal test) | Arad, Sibiu, Timisoara, Zerind, Fagaras | Arad–Sibiu–Fagaras–Bucharest | 450 | ❌ fewest *steps* (3), not least cost |
| DFS (cycle check on path) | Arad, Sibiu, Fagaras | Arad–Sibiu–Fagaras–Bucharest | 450 | ❌ got lucky it found anything this fast |
| UCS | 12 nodes ([trace](romania-ucs-trace.md)) | Arad–Sibiu–RV–Pitesti–Bucharest | 418 | ✅ |

**Takeaway:** BFS is optimal only when all steps cost the same. Here steps have different costs, so "fewest actions" (3) ≠ "cheapest" (418 needs 4 actions).

## C. Node counts for IDS vs BFS (b = 10, d = 5)
- N(BFS) = 10 + 100 + 1,000 + 10,000 + 100,000 = **111,110**
- N(IDS) = 5·10 + 4·100 + 3·1,000 + 2·10,000 + 1·100,000 = **123,450** (≈ 11% overhead)

## D. Try it yourself
DFS on Romania (cycle check on the current path) trying successors in **reverse** alphabetical order (Zerind first). What is expanded, and what path/cost is returned? <details><summary>answer</summary>Expanded (11): Arad, Zerind, Oradea, Sibiu, Rimnicu Vilcea, Pitesti, Craiova, Drobeta, Mehadia, Lugoj, Timisoara. From Pitesti the reverse order tries Craiova before Bucharest, so DFS dives Craiova → Drobeta → Mehadia → Lugoj → Timisoara, hits a dead end (Arad is already on the path), and backtracks all the way to Pitesti. Returned path: Arad → Zerind → Oradea → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest, cost 75+71+151+80+97+101 = **575** (optimal is 418). Moral: DFS's answer and cost depend on successor ordering and aren't optimal. (Verified in code.)</details>
