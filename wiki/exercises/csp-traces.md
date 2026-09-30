---
title: "Exercise — CSP traces (arc consistency, forward checking, MRV, min-conflicts)"
type: exercise
unit: games-csp
sources: [rn-ch05-csp, slides-02-problem-solving]
updated: 2026-09-30
---

# CSP Traces

## 1. Arc consistency on Y = X²
X, Y ∈ {0..9}, constraint Y = X².
- REVISE(X, Y): keep x only if x² ∈ D_Y → **X ∈ {0,1,2,3}**.
- REVISE(Y, X): keep y only if y = x² for some x ∈ D_X → **Y ∈ {0,1,4,9}**.
- Nothing else changes → arc-consistent.

## 2. Arc consistency does nothing on Australia
With all domains {R,G,B}, for every colour of SA there is a different colour for WA (and vice versa). AC-3 removes nothing; search is still needed.
Two colours only? Still arc-consistent, yet **no solution** (WA, NT, SA form a triangle) — path consistency on {WA, SA} w.r.t. NT detects it: the only consistent pairs (WA=R, SA=B) and (WA=B, SA=R) leave NT no colour.

## 3. Forward checking (R&N Fig 5.7) — verified in code
See the table in [backtracking-search-csp](../algorithms/backtracking-search-csp.md#forward-checking-in-action-rn-fig-57-verified-in-code): WA = R, Q = G, V = B ⇒ SA's domain becomes **empty** ⇒ backtrack.

## 4. MRV + degree on Australia
<details><summary>Which variable first? second? (no assignments yet)</summary>All domains have 3 values → MRV ties everywhere → degree heuristic picks **SA** (degree 5). After SA = R (with forward checking), WA, NT, Q, NSW, V all have {G, B} → MRV ties again; degree counting only *unassigned* neighbours: WA 1 (NT), NT 2 (WA, Q), Q 2 (NT, NSW), NSW 2 (Q, V), V 1 (NSW) → pick one of NT, Q, NSW. After that, each remaining mainland region has a single legal colour (forced around the ring), and T (degree 0, 3 values) comes last.</details>

## 5. Why does LCV prefer Q = red after WA = red, NT = green?
<details><summary>answer</summary>SA's domain is then {B}. Q = blue would wipe out SA's last value; Q = red leaves SA = blue possible. LCV picks the value that eliminates fewest neighbour options → red.</details>

## 6. Bounds propagation
F1 ∈ [0, 165], F2 ∈ [0, 385], F1 + F2 = 420. New bounds?
<details><summary>answer</summary>F1 ≥ 420 − 385 = 35 and F2 ≥ 420 − 165 = 255 → F1 ∈ [35, 165], F2 ∈ [255, 385].</details>

## 7. Atmost
Atmost(10, P1..P4), each Pi ∈ {3,4,5,6}: satisfiable? With each Pi ∈ {2,…,6}?
<details><summary>answer</summary>Minimum sum 12 > 10 → unsatisfiable. With {2..6}: min of the others = 6, so each Pi ≤ 4 → delete 5 and 6 from every domain.</details>

## 8. Tree-structured CSP cost
A tree-shaped constraint graph with n = 100 variables, d = 3. Backtracking worst case vs tree algorithm?
<details><summary>answer</summary>Generic: O(dⁿ) = 3¹⁰⁰. Tree algorithm: O(n·d²) = 100·9 = 900 constraint checks.</details>

## 9. Min-conflicts step
Queens in columns 1–4 of a 4×4 board at rows (1, 2, 3, 4) — all on one diagonal. Pick Q1 (conflicted). Conflicts for each row of Q1 given the others fixed?
<details><summary>answer</summary>Others at (2,2), (3,3), (4,4). Q1 at row 1: attacks all 3 on the diagonal → 3. Row 2: same row as Q2 → 1; diagonal with Q3? |2−3| = 1 ≠ 2, no; Q4: |2−4| = 2 ≠ 3, no → 1. Row 3: same row as Q3 → 1; Q2: |3−2| = 1 = 1 column apart → diagonal → 2. Row 4: same row as Q4 → 1; Q2: |4−2| = 2 ≠ 1; Q3: |4−3| = 1 ≠ 2 → 1. Min = 1 at rows 2 and 4 → choose randomly between them. (Counts 3, 1, 2, 1 verified in code.)</details>
