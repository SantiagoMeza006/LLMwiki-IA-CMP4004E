---
title: "R&N Chapter 5 — Constraint Satisfaction Problems"
type: source
unit: games-csp
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch05-csp]
updated: 2026-09-30
---

# R&N Chapter 5 — Constraint Satisfaction Problems (pp. 164–191)

Textbook behind [slides-02](slides-02-problem-solving.md) s.23–25. States become **factored** (variables with values), which lets solvers use general-purpose, domain-independent heuristics.

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 5.1 | CSP = ⟨X, D, C⟩, constraint = ⟨scope, rel⟩; consistent/complete/partial assignments; **NP-complete** in general. Map colouring of Australia (7 vars, 9 constraints), job-shop scheduling (precedence + disjunctive constraints), 8-queens as CSP. Discrete/infinite/continuous domains; unary, binary, global (Alldiff), n-ary constraints; constraint graph/hypergraph; dual graph; preference constraints → COP. | [constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md) |
| 5.2 | **Constraint propagation**: node consistency, **arc consistency (AC-3, O(cd³))**, path consistency, k-consistency (strongly n-consistent ⇒ solve without backtracking in O(n²d)), global constraints (Alldiff, Atmost, bounds propagation), Sudoku (27 Alldiff constraints; AC-3 solves easy ones). | [ac-3](../algorithms/ac-3.md) |
| 5.3 | **Backtracking search** (commutativity: dⁿ leaves instead of n!·dⁿ); **MRV** ("fail-first"), **degree heuristic**, **least-constraining value** ("fail-last"); **forward checking**, **MAC**; chronological backtracking vs **backjumping**, conflict sets, **conflict-directed backjumping**; **constraint learning** (no-goods). | [backtracking-search-csp](../algorithms/backtracking-search-csp.md) |
| 5.4 | **Local search for CSPs: min-conflicts** (million-queens in ~50 steps; Hubble scheduling 3 weeks → 10 min); plateau search, tabu search, constraint weighting; online repair. | [min-conflicts](../algorithms/min-conflicts.md) |
| 5.5 | Structure: independent subproblems (Tasmania); **tree-structured CSPs solvable in O(nd²)** (topological sort + directional arc consistency); **cutset conditioning** O(d^c·(n−c)d²); **tree decomposition** (tree width w → O(n·d^(w+1))); value symmetry and symmetry-breaking constraints. | [constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md#structure-of-problems) |

## Takeaways 🎯
1. CSP solvers prune whole subtrees the moment a partial assignment violates a constraint — atomic search can't (SA = blue cuts 3⁵ = 243 neighbour assignments to 2⁵ = 32, −87%).
2. **Variable choice: fail-first (MRV, degree). Value choice: fail-last (LCV).**
3. Inference during search: forward checking ⊂ MAC (MAC propagates further).
4. Structure matters: trees are easy; cutsets/tree decompositions reduce general graphs to trees.
5. Min-conflicts local search is astonishingly effective on large, loosely constrained problems.
