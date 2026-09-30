---
title: SLD Resolution (how Prolog executes a query)
type: algorithm
unit: logic
sources: [slides-xx-prolog, rn-ch09-fol-inference]
updated: 2026-09-30
---

# SLD Resolution — Prolog's Execution Strategy 🎯

**SLD resolution = depth-first [backward chaining](../concepts/forward-and-backward-chaining.md) with [unification](../concepts/unification.md)** (slides-XX s.15).

## Procedure
1. Take the **leftmost** goal.
2. Scan the clauses **in file order** for one whose head **unifies** with it (rename clause variables first).
3. **Replace** the goal by that clause's body (applying the substitution).
4. On failure, **backtrack**: undo bindings, try the next matching clause (a *choicepoint*).
5. **Succeed** when no goals remain; the answer is the accumulated substitution. `;` asks Prolog to backtrack for another answer.

It is a [DFS](depth-first-search.md) of the proof (AND–OR) tree, left to right.

## Consequence: order matters 🎯
Logically identical programs can behave differently:
```prolog
link(a, b).   link(b, c).

% base case first: finds an answer (but ';' then loops)
path(X, Z) :- link(X, Z).
path(X, Z) :- path(X, Y), link(Y, Z).
?- path(a, c).   % true.

% left recursion first: no answer at all
path(X, Z) :- path(X, Y), link(Y, Z).
path(X, Z) :- link(X, Z).
?- path(a, c).   % ERROR: Stack limit (1.0Gb) exceeded
```
> **SLD resolution is complete; Prolog's search rule (depth-first) is not.**
Fix: `:- table path/2.` (tabling/memoisation) — or put the recursive call after a goal that consumes input (`path(X,Z) :- link(X,Y), path(Y,Z).`).

R&N §9.4.3 on the same example: Prolog is **incomplete as a theorem prover even for Datalog**, while forward chaining halts after inferring path(a,b), path(b,c), path(a,c). Depth-first backward chaining also **repeats work**: 877 inferences for a path in R&N Fig 9.8(b) vs 62 with forward chaining. **Tabled logic programming** = goal-directed backward chaining + the caching of dynamic programming; complete for Datalog.

## Relation to search theory
- Frontier = stack of pending goals/choicepoints → O(depth) memory, like DFS.
- Incompleteness in infinite/cyclic spaces = DFS going down an infinite branch.
- Tabling plays the role of the `reached` set in graph search.

Traces: [prolog-traces](../exercises/prolog-traces.md). Language: [prolog](../concepts/prolog.md).
