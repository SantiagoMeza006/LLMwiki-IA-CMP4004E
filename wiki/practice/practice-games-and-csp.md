---
title: Practice — Adversarial Search & CSPs
type: practice
unit: games-csp
sources: [slides-02-problem-solving]
updated: 2026-09-29
---

# Practice — Adversarial Search & CSPs

## Games
1. What four assumptions define the games studied in class?
   <details><summary>answer</summary>Two players (MAX, MIN) with opposing goals, zero-sum, perfect information (fully observable), deterministic.</details>
2. Give the recursive definition of the minimax value.
   <details><summary>answer</summary>Utility(s) if terminal; max over successors if MAX to move; min over successors if MIN to move.</details>
3. Time and space of minimax? Why is it impractical for chess?
   <details><summary>answer</summary>O(b^m) time, O(b·m) space. Chess b ≈ 35, m ≈ 80 → 35^80 nodes.</details>
4. Define α and β. When do we prune?
   <details><summary>answer</summary>α = best value for MAX so far (lower bound); β = best for MIN so far (upper bound). Prune at a MIN node when its value ≤ α; at a MAX node when its value ≥ β.</details>
5. Can alpha–beta return a different move from minimax?
   <details><summary>answer</summary>No; it returns the same value and move, only faster.</details>
6. Best-case complexity of alpha–beta, and what it requires?
   <details><summary>answer</summary>O(b^(m/2)) with perfect move ordering (best moves first) — doubles the searchable depth.</details>
7. Run minimax and alpha–beta on: MAX root; MIN children X=[3,5,10], Y=[2,15,7], Z=[6,8,1]. Value, move, pruned leaves?
   <details><summary>answer</summary>X=3, Y=2, Z=1 → root 3, move to X. α=3 after X. Y: 2 ≤ 3 → prune 15, 7. Z: 6 > 3 continue; 8 continue; 1 → Z=1. Pruned leaves: 15, 7 (2 leaves).</details>

## CSPs
8. What makes a CSP different from standard search?
   <details><summary>answer</summary>States have internal structure (factored): variables with values that must satisfy constraints; goal = complete and consistent assignment, not a path.</details>
9. Define consistent and complete assignment.
   <details><summary>answer</summary>Consistent: violates no constraint. Complete: every variable assigned.</details>
10. Formulate Sudoku as a CSP.
    <details><summary>answer</summary>Variables: 81 cells; domains: {1..9} (singletons for givens); constraints: all-different in each row, column and 3×3 box.</details>
11. Explain forward checking vs arc consistency.
    <details><summary>answer</summary>Forward checking: after assigning X, remove inconsistent values from X's unassigned neighbours only. Arc consistency: make every arc X→Y consistent (each value of X has support in Y), propagating repeatedly across the whole network — stronger.</details>
12. What is MRV and why "fail-first"?
    <details><summary>answer</summary>Minimum remaining values: choose the variable with the fewest legal values; if it's going to fail, discover it early and prune the tree.</details>
13. Map colouring: WA, NT, SA, Q, NSW, V, T with 3 colours, adjacent differ. After WA=red with forward checking, what are NT's and SA's domains?
    <details><summary>answer</summary>NT = {green, blue}, SA = {green, blue} (red removed from WA's neighbours).</details>
14. In BACKTRACK, what do SELECT-UNASSIGNED-VARIABLE, ORDER-DOMAIN-VALUES and INFERENCE correspond to?
    <details><summary>answer</summary>Variable ordering (MRV/degree), value ordering (least-constraining value), constraint propagation (forward checking/AC-3).</details>
