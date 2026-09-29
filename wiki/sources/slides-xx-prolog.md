---
title: "Slides XX — Logic Programming with Prolog"
type: source
unit: logic
raw: "raw/XX_Logic Programming with Prolog.pptx"
sources: [slides-xx-prolog]
updated: 2026-09-29
---

# Slides XX — Logic Programming with Prolog

31 slides · Raw: `raw/XX_Logic Programming with Prolog.pptx` · Text-heavy, code-rich deck; includes **Prolog Lab 01** assignment. Reading: R&N §7.5 (Horn clauses, chaining) and §9.4 (backward chaining, logic programming) — *not in our PDF excerpt*.

## What it covers

| Slides | Topic | Wiki page |
|---|---|---|
| 2 | 🎯 The ladder: propositional calculus (decidable, no "every") → first-order (objects, quantifiers, undecidable) → Horn clauses (≤1 positive literal, cheap entailment) → Prolog (Horn + backward chaining + unification). **Algorithm = Logic + Control** (Kowalski 1979). | [logic-to-horn-clauses](../concepts/logic-to-horn-clauses.md) |
| 3 | CNF: literal, clause, conjunction of clauses; resolution needs clause form. | same |
| 4–5 | 🎯 Horn clauses: definite clause (rule), fact, goal clause (query); P ∨ Q has no Horn form; propositional definite-clause entailment is linear; AND–OR graph explored depth-first, left-to-right. | same |
| 6 | 🎯 Backward chaining, proof tree for `Criminal(West)`. | [forward-and-backward-chaining](../concepts/forward-and-backward-chaining.md) |
| 7 | 🎯 FOL → Prolog syntax: `C :- A, B.`, uppercase = variable, implicit ∀, comma = and, semicolon = or, period ends clause. | [prolog](../concepts/prolog.md) |
| 8–11 | History (Colmerauer & Roussel, Marseille 1972; Kowalski), SWI-Prolog, install, first session (`?-` vs `\|:` prompts, `;` for more answers). | same |
| 12–13 | Terms (atom, number, variable, compound), facts/rules/queries, name/arity, `family.pl`, `findall/3` vs `setof/3`. | same |
| 14 | 🎯 Unification rules; no occurs check (`X = f(X)` builds a cyclic term). | [unification](../concepts/unification.md) |
| 15 | 🎯 SLD resolution = depth-first backward chaining + unification; clause/goal order matters; left recursion loops; `:- table` fixes it. | [sld-resolution](../algorithms/sld-resolution.md) |
| 16 | 🎯 `is/2` vs `=/2`, `=:=`, `==`, `\=`, `=<` (never `<=`). | [prolog](../concepts/prolog.md) |
| 17–18 | Recursion: factorial, naive vs accumulator Fibonacci (`fibo(25)` ≈ 1.09 M inferences). | [prolog-exercises](../exercises/prolog-traces.md) |
| 19–22 | Lists (`[H\|T]`, `append` runs backwards), isEven/isOdd, **isPerm bug** (set equality ≠ permutation), binary search tree as terms. | same |
| 23 | 🎯 Negation as failure `\+` (closed-world assumption; bind variables first) and the cut `!` (prefer `( C -> T ; E )`). | [prolog](../concepts/prolog.md) |
| 24 | Built-ins worth memorising (findall, bagof/setof, aggregate_all, forall, between, select, permutation, msort, format, time). | same |
| 25–27 | 🎯 N-Queens case study; generate-and-test vs test-as-you-go (N=8: 1,058,230 vs 61,770 inferences, 17×). Solution counts N=4..10: 2, 10, 4, 40, 92, 352, 724. | [n-queens-prolog](../exercises/n-queens-prolog.md) |
| 28 | Debugging with `trace/0`; classic mistakes. | [prolog](../concepts/prolog.md) |
| 29–30 | **Prolog Lab 01** (family KB ≥16 people/4 generations, ≥8 rules, ≥20 plunit tests, analysis; bonus `related/2`). | [prolog](../concepts/prolog.md#lab-01-checklist) |
| 31 | Further reading: R&N 7.5, 9.4; Luger; Bratko; Sterling & Shapiro; learnprolognow.org. | — |

## Where it fits
Unit **logic**. Also relevant to search: Prolog's execution is a **depth-first search** of an AND–OR tree, so it inherits DFS's incompleteness (see [depth-first-search](../algorithms/depth-first-search.md)).
