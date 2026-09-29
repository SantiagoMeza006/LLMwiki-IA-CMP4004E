---
title: "Exercise — Greedy and A* on Romania (Arad → Bucharest)"
type: exercise
unit: search
sources: [rn-ch03-search, slides-02-problem-solving]
updated: 2026-09-29
---

# Greedy Best-First vs A* — Arad → Bucharest

h = h_SLD (see table in [heuristics](../concepts/heuristics.md#h_sld-to-bucharest-rn-fig-316)). Verified in code.

## 1. Greedy best-first (f = h)
| Step | Pop (h) | Frontier after expansion (h) |
|---|---|---|
| 1 | Arad 366 | **Sibiu 253**, Timisoara 329, Zerind 374 |
| 2 | Sibiu 253 | **Fagaras 176**, Rimnicu Vilcea 193, Timisoara 329, Zerind 374, Oradea 380 |
| 3 | Fagaras 176 | **Bucharest 0**, RV 193, ... |
| 4 | Bucharest 0 → goal | |

Path Arad–Sibiu–Fagaras–Bucharest = 140 + 99 + 211 = **450**. Not optimal (32 more than 418).

## 2. A* (f = g + h)
| Step | Pop: f = g + h | Children added: f = g + h |
|---|---|---|
| 1 | Arad 366 = 0 + 366 | Sibiu 393 = 140+253 · Timisoara 447 = 118+329 · Zerind 449 = 75+374 |
| 2 | Sibiu 393 | Fagaras 415 = 239+176 · RV 413 = 220+193 · Oradea 671 = 291+380 · (Arad 646 = 280+366) |
| 3 | RV 413 | Pitesti 417 = 317+100 · Craiova 526 = 366+160 · (Sibiu 553 = 300+253) |
| 4 | Fagaras 415 | Bucharest 450 = 450+0 · (Sibiu 591 = 338+253) |
| 5 | Pitesti 417 | **Bucharest 418 = 418+0** (improves 450) · (Craiova 615 = 455+160, RV 607 = 414+193) |
| 6 | Bucharest 418 → goal ✅ | |

(Entries in parentheses are what R&N's *tree-like* figure shows; a graph search discards them because the state was already reached more cheaply.)

**Answer:** Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest, **418**.

## Questions to test yourself
1. Why isn't Bucharest (450) returned at step 4? <details><summary>answer</summary>It's only *generated* at step 4; A* tests goals when popping. At that moment Pitesti (417) has lower f, and a path through it might be cheaper — it is (418).</details>
2. Which nodes does A* never expand, and why? <details><summary>answer</summary>Timisoara (447), Zerind (449), Craiova (526), Oradea (671): all have f > C* = 418. A* expands no node with f > C*.</details>
3. Is h_SLD admissible here? Consistent? <details><summary>answer</summary>Yes to both: a straight line is never longer than a road path (admissible), and by the triangle inequality h(n) ≤ c(n,n') + h(n') (consistent).</details>
4. What would greedy do if h(Fagaras) were 250 instead of 176? <details><summary>answer</summary>After Sibiu it would pop Rimnicu Vilcea (193) first, then Pitesti (100), then Bucharest — finding 418 by luck. Greedy's result depends entirely on h.</details>
