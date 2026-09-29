---
title: Practice — Problem Solving & Search
type: practice
unit: search
sources: [slides-02-problem-solving, rn-ch03-search]
updated: 2026-09-29
---

# Practice — Problem Solving & Search

1. List the five components of a problem formulation and give them for the 8-puzzle.
   <details><summary>answer</summary>Initial state (any configuration), actions (blank Left/Right/Up/Down when applicable), transition model (swap blank with neighbouring tile), goal test (tiles in order), action cost (1 per move).</details>
2. State space vs search tree — two differences.
   <details><summary>answer</summary>The state space represents the problem, each state once; the search tree represents the search process, a state can appear many times via different paths; the tree can be infinite even if the graph is finite.</details>
3. What are the frontier and the explored/reached set for? What happens without repeated-state control?
   <details><summary>answer</summary>Frontier: generated but unexpanded nodes. Reached/explored: states already generated/expanded, never re-expanded. Without them the algorithm may loop forever (e.g. Arad↔Sibiu) even when a solution exists.</details>
4. Give complete/optimal/time/space for BFS and DFS as in the slides.
   <details><summary>answer</summary>BFS: complete; optimal with uniform costs; O(b^d); O(b^d). DFS: complete only with repeated-state control in finite spaces; not optimal; O(b^m); O(b·m).</details>
5. Why does BFS use an early goal test while UCS and A* must use a late one?
   <details><summary>answer</summary>BFS's first path to a state is always the shallowest, so returning on generation is safe (when costs are uniform). In UCS/A*, a cheaper path may be found later (Sibiu→Bucharest: 310 via Fagaras generated before 278 via Pitesti), so the goal must be tested when popped.</details>
6. Compute N(IDS) and N(BFS) for b = 10, d = 5. Why is IDS worth it?
   <details><summary>answer</summary>123,450 vs 111,110. Only ~11% more time but O(b·d) memory instead of O(b^d).</details>
7. What is the time complexity of UCS and why can it exceed b^d?
   <details><summary>answer</summary>O(b^(1+⌊C*/ε⌋)); it may explore large trees of cheap actions before trying an expensive but useful one.</details>
8. Define admissible and consistent heuristics. Which implies which?
   <details><summary>answer</summary>Admissible: h(n) ≤ true cost to goal. Consistent: h(n) ≤ c(n,a,n') + h(n') for every successor. Consistent ⇒ admissible, not vice-versa.</details>
9. What does it mean for h2 to dominate h1? Which 8-puzzle heuristic dominates?
   <details><summary>answer</summary>h2(n) ≥ h1(n) ∀n with both admissible → A* with h2 expands no more nodes. Manhattan distance dominates misplaced tiles.</details>
10. Run greedy best-first from Arad to Bucharest with h_SLD. Path, cost, optimal?
    <details><summary>answer</summary>Arad → Sibiu → Fagaras → Bucharest, 450; not optimal (418 exists).</details>
11. In A* on Romania, Bucharest appears with f = 450 before the search ends. Why isn't it returned?
    <details><summary>answer</summary>Goal test happens on expansion; Pitesti with f = 417 < 450 is expanded first and yields Bucharest with f = 418.</details>
12. Prove briefly that A* with an admissible heuristic is optimal.
    <details><summary>answer</summary>If A* returned cost C > C*, some node n on an optimal path is unexpanded with f(n) = g*(n) + h(n) ≤ g*(n) + h*(n) = C* < C, so n would have been expanded before the goal of cost C — contradiction.</details>
13. What does A* expand relative to C*?
    <details><summary>answer</summary>All nodes with f < C*, some with f = C*, none with f > C*.</details>
14. Express UCS, A*, greedy, weighted A* as f = g + W·h.
    <details><summary>answer</summary>UCS W = 0; A* W = 1; weighted A* 1 < W < ∞; greedy W = ∞.</details>
15. A* runs out of memory. Name two alternatives and their trade-off.
    <details><summary>answer</summary>IDA* (linear memory, re-expands nodes each iteration), RBFS (linear, "mind changes"), SMA* (uses all memory, drops worst leaves, may thrash), beam search (fast, incomplete/suboptimal), weighted A* (fewer nodes, suboptimal within W).</details>
16. Effective branching factor: A* generates 52 nodes to find a solution at depth 5. b*?
    <details><summary>answer</summary>Solve 53 = 1 + b + b² + b³ + b⁴ + b⁵ → b* ≈ 1.92.</details>
17. Why is Dijkstra a special case of A*?
    <details><summary>answer</summary>It's A* with h(n) = 0 (f = g) — trivially admissible but uninformed, so it expands more nodes.</details>
18. Is h(n) = straight-line distance × 1.3 admissible for Romania? Consequence?
    <details><summary>answer</summary>Not guaranteed — it may overestimate (some roads are nearly straight). A* may return a suboptimal path, but faster (it's like weighted A*).</details>
