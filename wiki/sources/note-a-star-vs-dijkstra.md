---
title: "My note — A* vs Dijkstra (Shortest Path)"
type: source
unit: search
raw: "raw/A^star vs Dijkstra - Shortest Path.pdf"
sources: [note-a-star-vs-dijkstra]
updated: 2026-09-29
---

# My homework note — A* vs Dijkstra: Shortest Path (Santiago Meza)

One-page note. Raw: `raw/A^star vs Dijkstra - Shortest Path.pdf`.

## Claims in the note
- Dijkstra (f(n) = g(n)) finds Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest, total **418**.
- A* (f(n) = g(n) + h(n), h = straight-line distance) finds the same optimal path, 418, while exploring fewer nodes.
- Dijkstra is the special case of A* with h(n) = 0.

## Check against the textbook ✅ / ⚠️
- ✅ Path and cost match R&N Fig 3.18 (A* reaches Bucharest with f = 418 = 418 + 0).
- ✅ "Dijkstra = A* with h = 0" matches R&N §3.5.4 (uniform-cost search is weighted A* with W = 0).
- ⚠️ **Units:** the note says **418 km**; R&N's Romania map (Fig 3.1) gives distances in **miles**. Use "418" (or 418 miles).
- 💡 Could be strengthened by: naming the nodes A* never expands (Timisoara f=447, Zerind f=449 — R&N §3.5.3), and stating the condition that makes A* optimal (h_SLD is admissible and consistent).

Filed as the comparison page [a-star-vs-dijkstra](../comparisons/a-star-vs-dijkstra.md).
