---
title: "R&N Chapter 3 — Solving Problems by Searching"
type: source
unit: search
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch03-search]
updated: 2026-09-29
---

# R&N Chapter 3 — Solving Problems by Searching (pp. 81–116, excerpt ends in §3.6.1)

The textbook behind [slides-02](slides-02-problem-solving.md) (search part).

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 3.1 | Problem-solving agent; 4 phases (goal formulation, problem formulation, search, execution); open- vs closed-loop; formal problem (states, initial, goals/IS-GOAL, ACTIONS, RESULT, ACTION-COST); path, solution, optimal solution; abstraction (valid, useful). | [search-problem-formulation](../concepts/search-problem-formulation.md) |
| 3.2 | Standardized problems: vacuum grid world (n·2^n states), Sokoban, 8-puzzle/15-puzzle, Knuth's "4" problem (infinite state space); real-world: route finding, airline travel, TSP, VLSI, robot navigation, assembly sequencing, protein design. | [example-search-problems](../concepts/example-search-problems.md) |
| 3.3 | Search tree over state-space graph; expand, frontier, reached; **BEST-FIRST-SEARCH** (Fig 3.7); node = (STATE, PARENT, ACTION, PATH-COST); queues (priority, FIFO, LIFO); redundant paths & cycles; **graph search vs tree-like search**; 4 criteria; b, d, m. | [state-space-and-search-tree](../concepts/state-space-and-search-tree.md), [best-first-search](../algorithms/best-first-search.md), [search-evaluation-criteria](../concepts/search-evaluation-criteria.md) |
| 3.4 | BFS (early goal test), UCS/Dijkstra (late goal test, O(b^{1+⌊C*/ε⌋})), DFS, backtracking, depth-limited, iterative deepening, bidirectional; **Fig 3.15 comparison**. | [uninformed-search-comparison](../comparisons/uninformed-search-comparison.md) + algorithm pages |
| 3.5 | Heuristic h(n); h_SLD table (Fig 3.16); greedy best-first; **A\*** (Fig 3.18 trace, optimal cost 418); admissibility + proof; consistency; contours; optimally efficient; weighted A*; beam, IDA*, RBFS, SMA*; bidirectional heuristic search (f2 = max(2g, g+h)). | [a-star-search](../algorithms/a-star-search.md), [heuristics](../concepts/heuristics.md), [memory-bounded-and-weighted-search](../algorithms/memory-bounded-and-weighted-search.md) |
| 3.6 (start) | 8-puzzle heuristics h1 (misplaced tiles = 8) and h2 (Manhattan = 18) for a problem whose true cost is 26; 9!/2 = 181,440 reachable 8-puzzle states; **effective branching factor** b* (52 nodes, d=5 → b*=1.92). | [heuristics](../concepts/heuristics.md), [8-puzzle-heuristics](../exercises/8-puzzle-heuristics.md) |

> Note: the OCR in the PDF prints "181, 400" for 9!/2; the correct value is **181,440**.

## Not in the excerpt (but taught in slides-02)
Chapter 5 (CSPs), Chapter 6 (games: minimax, alpha-beta), Chapter 7/9 (logic). Wiki pages on those rely on the slides and the R&N figures reproduced in them.
