---
title: Practice — Adversarial Search & CSPs
type: practice
unit: games-csp
sources: [slides-02-problem-solving, rn-ch05-csp, rn-ch06-games]
updated: 2026-09-30
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

## More from R&N Ch 5–6
15. Why does backtracking assign one variable per tree level? How many leaves does that save?
    <details><summary>answer</summary>CSPs are commutative (assignment order doesn't matter), so we branch only on one variable's values: dⁿ leaves instead of n!·dⁿ.</details>
16. Complexity of AC-3? What can it *not* detect?
    <details><summary>answer</summary>O(c·d³). It can't detect inconsistencies involving 3+ variables, e.g. 2-colouring the WA–NT–SA triangle (needs path consistency).</details>
17. Forward checking vs MAC?
    <details><summary>answer</summary>Forward checking prunes only the neighbours of the just-assigned variable; MAC runs AC-3 from those arcs and keeps propagating — strictly stronger.</details>
18. Why is variable ordering "fail-first" but value ordering "fail-last"?
    <details><summary>answer</summary>All variables must be assigned, so find failures early; but only one solution is needed, so try the most promising value first.</details>
19. What is conflict-directed backjumping? What is a no-good?
    <details><summary>answer</summary>Backtrack to the most recent variable in the (propagated) conflict set, skipping irrelevant ones like Tasmania. A no-good is a recorded minimal conflicting partial assignment (constraint learning).</details>
20. Min-conflicts on the million-queens problem: how many steps? Why so easy?
    <details><summary>answer</summary>~50 steps after the initial assignment; solutions are dense (underconstrained problem).</details>
21. How fast can a tree-structured CSP be solved? What is cutset conditioning?
    <details><summary>answer</summary>O(n·d²). Assign a cycle cutset S so the rest is a tree, then solve the tree for each assignment of S: O(d^|S| · (n−|S|)·d²).</details>
22. What are an evaluation function's requirements? Give the chess material weights.
    <details><summary>answer</summary>Equal to utility at terminals, between loss and win elsewhere, fast, strongly correlated with winning chances. Pawn 1, knight 3, bishop 3, rook 5, queen 9.</details>
23. What is the horizon effect and one mitigation? What is quiescence search?
    <details><summary>answer</summary>An unavoidable loss pushed beyond the search depth by delaying moves; singular extensions. Quiescence search keeps searching non-quiet positions (pending captures) before applying EVAL.</details>
24. What does a transposition table store and what does it buy in chess?
    <details><summary>answer</summary>Values of positions already evaluated (reached by different move orders); it roughly doubles the reachable depth.</details>
25. List the four steps of MCTS and write UCB1.
    <details><summary>answer</summary>Selection, expansion, simulation (playout), back-propagation. UCB1(n) = U(n)/N(n) + C·√(log N(parent)/N(n)).</details>
26. Why does MCTS return the most-played move rather than the highest win rate?
    <details><summary>answer</summary>Few playouts give unreliable averages (2/3 vs 65/100); UCB1 ensures the most-played move is almost always the best-rated anyway.</details>
27. When does MCTS beat alpha–beta and when is it weaker?
    <details><summary>answer</summary>Better with huge branching factors (Go) or no good evaluation function; weaker when a single move is decisive (it may never sample it) or when obvious wins take long playouts to confirm.</details>
28. Expectiminimax value of a chance node with outcomes 10 (P = 0.25) and 2 (P = 0.75)? Why must EVAL be calibrated in games of chance?
    <details><summary>answer</summary>0.25·10 + 0.75·2 = 4. Because averages depend on magnitudes: an order-preserving rescaling of leaves can change the best move (R&N Fig 6.14).</details>
29. Why is "zero-sum" a slightly wrong name for chess?
    <details><summary>answer</summary>Outcomes sum to 1 (1+0 or ½+½), so it's constant-sum; it's zero-sum if each player pays an entry fee of ½.</details>
