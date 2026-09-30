---
title: "R&N Chapter 3 — Solving Problems by Searching"
type: source
unit: search
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch03-search]
updated: 2026-09-30
---

# R&N Chapter 3 — Solving Problems by Searching (pp. 81–127)

The textbook behind [slides-02](slides-02-problem-solving.md) (search part).

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 3.1 | Problem-solving agent; 4 phases (goal formulation, problem formulation, search, execution); open- vs closed-loop; formal problem (states, initial, goals/IS-GOAL, ACTIONS, RESULT, ACTION-COST); path, solution, optimal solution; abstraction (valid, useful). | [search-problem-formulation](../concepts/search-problem-formulation.md) |
| 3.2 | Standardized problems: vacuum grid world (n·2^n states), Sokoban, 8-puzzle/15-puzzle, Knuth's "4" problem (infinite state space); real-world: route finding, airline travel, TSP, VLSI, robot navigation, assembly sequencing, protein design. | [example-search-problems](../concepts/example-search-problems.md) |
| 3.3 | Search tree over state-space graph; expand, frontier, reached; **BEST-FIRST-SEARCH** (Fig 3.7); node = (STATE, PARENT, ACTION, PATH-COST); queues (priority, FIFO, LIFO); redundant paths & cycles; **graph search vs tree-like search**; 4 criteria; b, d, m. | [state-space-and-search-tree](../concepts/state-space-and-search-tree.md), [best-first-search](../algorithms/best-first-search.md), [search-evaluation-criteria](../concepts/search-evaluation-criteria.md) |
| 3.4 | BFS (early goal test), UCS/Dijkstra (late goal test, O(b^{1+⌊C*/ε⌋})), DFS, backtracking, depth-limited, iterative deepening, bidirectional; **Fig 3.15 comparison**. | [uninformed-search-comparison](../comparisons/uninformed-search-comparison.md) + algorithm pages |
| 3.5 | Heuristic h(n); h_SLD table (Fig 3.16); greedy best-first; **A\*** (Fig 3.18 trace, optimal cost 418); admissibility + proof; consistency; contours; optimally efficient; weighted A*; beam, IDA*, RBFS, SMA*; bidirectional heuristic search (f2 = max(2g, g+h)). | [a-star-search](../algorithms/a-star-search.md), [heuristics](../concepts/heuristics.md), [memory-bounded-and-weighted-search](../algorithms/memory-bounded-and-weighted-search.md) |
| 3.6.1 | 8-puzzle heuristics h1 (misplaced tiles = 8) and h2 (Manhattan = 18) for a problem whose true cost is 26; 9!/2 = 181,440 reachable 8-puzzle states; **effective branching factor** b* (52 nodes, d=5 → b*=1.92); Fig 3.26 (BFS vs A*(h1) vs A*(h2)); dominance ⇒ never more expansions. | [heuristics](../concepts/heuristics.md), [8-puzzle-heuristics](../exercises/8-puzzle-heuristics.md) |
| 3.6.2 | **Relaxed problems**: optimal cost of a relaxed problem is an admissible *and consistent* heuristic; h1, h2 derived by removing preconditions; ABSOLVER; h = max(h1..hm) is admissible and dominates each. | [heuristics](../concepts/heuristics.md#inventing-heuristics-rn-362366) |
| 3.6.3 | **Pattern databases** (1-2-3-4 subproblem: 15,120 patterns); disjoint pattern databases (additive; 15-puzzle 10,000× fewer nodes). | same |
| 3.6.4 | **Landmarks**: h_L (inadmissible), **differential heuristic** h_DH (admissible), shortcuts — how map services answer in milliseconds. | same |
| 3.6.5–3.6.6 | Metalevel state space / metalevel learning; learning heuristics from experience (features, h = c1·x1 + c2·x2). | same |
| Summary | Problem = 5 parts; judge algorithms by completeness, cost optimality, time, space; A* complete and optimal with admissible h; memory-bounded variants. | — |

> Note: the OCR in the PDF prints "181, 400" for 9!/2; the correct value is **181,440**.

Continues in [Chapter 4](rn-ch04-complex-environments.md) (local search, nondeterminism, partial observability).
