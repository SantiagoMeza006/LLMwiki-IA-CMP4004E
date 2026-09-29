---
title: Prolog (language essentials)
type: concept
unit: logic
sources: [slides-xx-prolog, slides-01-intro-to-ai]
updated: 2026-09-29
---

# Prolog

**Programmation en logique.** Born in **Marseille, 1972** (Alain Colmerauer & Philippe Roussel) on theory from **Robert Kowalski** (Edinburgh). You state **what holds**, not how to compute it; the interpreter searches for a proof, and the answer is the substitution that made it work. Used for expert systems, rule engines, legal/medical reasoning, NLP (definite clause grammars), compilers, constraints. Course implementation: **SWI-Prolog** ≥ 9.2 (or SWISH in the browser).

> ⚠️ slides-01 s.9 attributes Prolog to "Dennis Ritchie at Bell Labs" and calls it imperative — that's **C**. Trust slides-XX. See [discrepancies](../discrepancies.md).

## From FOL to Prolog — 4 conventions 🎯
1. Implication is written **backwards**: `A ∧ B ⇒ C` becomes `C :- A, B.`
2. **Case is inverted**: **Uppercase = variable**, lowercase = constant (opposite of the textbook).
3. **Quantifiers are implicit**: every variable is universally quantified.
4. **Punctuation**: `,` = and, `;` = or, every clause ends with `.`

## Terms
| Kind | Examples |
|---|---|
| Atom | `ana`, `prolog`, `'Ana María'` |
| Number | `42`, `3.14` (integers unbounded: `factorial(20)` fine) |
| Variable | `X`, `Qs`, `_` (anonymous) |
| Compound | `parent(hector, ana)`, `[1,2,3]` |

**Fact** `parent(hector, ana).` · **Rule** `father(X,Y) :- parent(X,Y), male(X).` · **Query** `?- father(hector, Who).`
A predicate is named by **name/arity**: `father/2` ≠ `father/3`. A predicate is a **relation**, not a function — one query may succeed many times (`;` for the next answer).

## Execution
[SLD resolution](../algorithms/sld-resolution.md) = depth-first [backward chaining](forward-and-backward-chaining.md) with [unification](unification.md). **Clause order and goal order change behaviour.** Left recursion (`path(X,Z) :- path(X,Y), link(Y,Z).` first) → stack overflow; `:- table path/2.` fixes it.

## Arithmetic: `is/2` is not `=/2` 🎯
| Op | Meaning |
|---|---|
| `=` | unify (no evaluation): `X = 3+4` gives the *term* `3+4` |
| `is` | evaluate right side, then unify: `X is 3+4` → 7. Right side must be **bound** ("Arguments are not sufficiently instantiated") |
| `=:=`, `=\=` | arithmetic equal / not equal (`3+4 =:= 7` true) |
| `<`, `>`, `=<`, `>=` | comparisons — note `=<`, never `<=` |
| `==` | term identity (no binding) |
| `\=` | not unifiable |

## Lists
`[]` or `[Head|Tail]`; `[1,2,3]` is `[1|[2|[3|[]]]]`. Relations run **backwards**: `append(X, Y, [1,2,3])` enumerates all 4 splits.
```prolog
mymember(X, [X|_]).
mymember(X, [_|T]) :- mymember(X, T).
myappend([], L, L).
myappend([H|T], L, [H|R]) :- myappend(T, L, R).
mylen([], 0).
mylen([_|T], N) :- mylen(T, N0), N is N0 + 1.
```

## Collecting answers
- `findall(T, G, L)` — all solutions, **keeps duplicates and order**, `[]` if none.
- `bagof/3`, `setof/3` — grouped; `setof` **sorts and deduplicates**, **fails** if none; `Var^Goal` = "any Var will do".
- `aggregate_all(count, G, N)`, `forall(C, A)`, `between(L, H, X)`, `select(X, L, Rest)`, `permutation(L, P)`, `msort/2` (keeps dups) vs `sort/2` (removes dups), `format("~w~n", [X])`, `time(Goal)`, `listing/1`, `make/0`.

## Negation as failure and the cut 🎯
- `\+ Goal` succeeds when Prolog **fails to prove** Goal. Equals logical negation only under the **closed-world assumption** (whatever isn't derivable is false). **Bind variables before negating**: `\+ parent(X, ana)` is `false` (some X exists), while `X = sofia, \+ parent(X, _)` works.
- `!` (cut) commits to choices made so far in the clause: no retrying goals to its left, no later clauses of this predicate. Faster but destroys the declarative reading. Bug: `max(X,Y,X) :- X >= Y, !.  max(_,Y,Y).` makes `max(5,3,3)` **true**. Fix: `max(X,Y,M) :- X >= Y, !, M = X.` or better `( X >= Y -> M = X ; M = Y )`.

## Classic mistakes (s.28)
Missing period · `=` instead of `is` · singleton-variable warnings (use `_`) · left recursion · uppercase where an atom was meant (`parent(Hector, ana)` = "some Hector") · `\+` on unbound variables. Debug with `trace/0` (ports: **Call, Exit, Redo, Fail**).

## Toplevel
`swipl` → `?-` expects a query; `[user].` or `consult('f.pl')` / `[f].` loads clauses (`|:` prompt); `;` next answer, Enter stops; `halt.` quits.

## Lab 01 checklist
From slides-XX s.29–30 (due same day, 23:59):
- [ ] KB from `family.pl`: ≥ 16 people, 4 generations, new `spouse/2`, both parents for every child, a couple with ≥ 3 children, someone childless (20 pts)
- [ ] ≥ 8 rules incl. `mother/2, sister/2, grandmother/2, uncle/2, cousin/2, father_in_law/2` + one **new recursive** rule ≠ `ancestor/2` (35)
- [ ] ≥ 20 plunit tests, ≥ 6 negative, one proves nobody is their own sibling; `?- run_tests.` all pass (25)
- [ ] ½-page analysis: why `sibling/2` needs `X \= Y`; which rules return duplicate answers and why; what the closed-world assumption claims (20)
- [ ] Bonus `related/2` that terminates (+10)
- [ ] Deliver `lastname_firstname_lab01.pl` + `.pdf` (≤ 2 pages); must load cleanly with `swipl -g true -t halt file.pl`; declare AI-assistant use in a header comment.

Worked programs: [prolog-traces](../exercises/prolog-traces.md), [n-queens-prolog](../exercises/n-queens-prolog.md). Practice: [practice-logic-prolog](../practice/practice-logic-prolog.md).
