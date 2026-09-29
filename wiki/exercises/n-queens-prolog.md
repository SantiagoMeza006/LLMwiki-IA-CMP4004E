---
title: "Exercise — N-Queens in Prolog (generate-and-test vs test-as-you-go)"
type: exercise
unit: logic
sources: [slides-xx-prolog, slides-02-problem-solving]
updated: 2026-09-29
---

# N-Queens in Prolog (slides-XX s.25–27)

Place N queens on an N×N board so none attack each other.

## Representation does half the work
`Qs` is a **permutation of 1..N**: the i-th element is the column of the queen in row i.
- one queen per **row** by construction,
- distinct values ⇒ one per **column**,
- only **diagonals** remain to check: queens in rows i, j clash if |Qi − Qj| = |i − j|.

## Test as you go (backtracking)
```prolog
queens(N, Qs) :- range(1, N, Ns), queens(Ns, [], Qs).
queens([], Qs, Qs).
queens(Unplaced, Safe, Qs) :-
    select(Q, Unplaced, NewUnplaced),   % choice point
    \+ threat(Q, Safe),                 % prune immediately
    queens(NewUnplaced, [Q|Safe], Qs).

threat(X, Xs) :- threat(X, 1, Xs).
threat(X, N, [Y|_])  :- X is Y + N ; X is Y - N.   % same diagonal, N rows apart
threat(X, N, [_|Ys]) :- N1 is N + 1, threat(X, N1, Ys).

range(M, N, [M|Ns]) :- M < N, M1 is M + 1, range(M1, N, Ns).
range(N, N, [N]).
```
`?- queens(8, Qs).` → `Qs = [4,2,7,3,6,8,5,1] ; ...` · `findall(...)`, `length` → **92** solutions for N = 8.

## Generate and test
```prolog
queens_perm(N, Qs) :- range(1, N, Ns), permutation(Ns, Qs), safe(Qs).
```
Builds a whole board, then checks it.

## Measured cost (inferences to enumerate all solutions, SWI 9.2.9)
| N | generate & test | test as you go | ratio |
|---|---|---|---|
| 4 | 425 | 200 | 2.1× |
| 6 | 15,358 | 3,090 | 5.0× |
| 8 | 1,058,230 | 61,770 | 17.1× |
| 10 | 113,230,594 | 1,468,869 | 77.1× |

Solution counts: N = 4..10 → 2, 10, 4, 40, 92, 352, 724; **N = 2, 3 have none**.

## Connections 🎯
- This is a **CSP** ([constraint-satisfaction-problems](../concepts/constraint-satisfaction-problems.md)): variables = rows, domain = columns, constraints = no shared column/diagonal. Test-as-you-go = [backtracking search](../algorithms/backtracking-search-csp.md); pruning early is why it wins.
- "Kowalski's equation at work": **same logic, different control** → very different efficiency.
- Prolog explores the choices depth-first via `select/3` — [SLD resolution](../algorithms/sld-resolution.md).
