---
title: "Exercise — Prolog Traces (family KB, factorial, lists, bugs)"
type: exercise
unit: logic
sources: [slides-xx-prolog]
updated: 2026-09-29
---

# Prolog Traces

## 1. The family knowledge base (slides-XX s.12–13)
```prolog
parent(hector, ana).  parent(hector, luis).
parent(ana, sofia).   parent(luis, diego).
male(hector). male(luis). male(diego).
female(ana).  female(sofia).
father(X, Y)      :- parent(X, Y), male(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y)     :- parent(P, X), parent(P, Y), X \= Y.
ancestor(X, Y)    :- parent(X, Y).
ancestor(X, Y)    :- parent(X, Z), ancestor(Z, Y).
```
| Query | Answers |
|---|---|
| `?- parent(hector, Who).` | Who = ana ; Who = luis. |
| `?- grandparent(G, sofia).` | G = hector ; false. (a choicepoint survived) |
| `?- findall(D, ancestor(hector, D), Ds).` | Ds = [ana, luis, sofia, diego]. |
| `?- setof(P, C^parent(P, C), Ps).` | Ps = [ana, hector, luis]. |
| `?- sibling(ana, S).` | S = luis. |
| `?- sibling(X, Y).` | X = ana, Y = luis ; X = luis, Y = ana ; false. — each pair **twice** (symmetry) |

**SLD trace of `grandparent(G, sofia)`:** goal → `parent(G, Y), parent(Y, sofia)`. Try `parent(hector, ana)`: G = hector, Y = ana → `parent(ana, sofia)` ✔ → answer G = hector. On `;` backtrack: `parent(hector, luis)` → `parent(luis, sofia)` ✘; `parent(ana, sofia)` → `parent(sofia, sofia)` ✘; `parent(luis, diego)` → `parent(diego, sofia)` ✘ → false.

**Why `sibling/2` needs `X \= Y`:** without it `sibling(ana, ana)` is true (same parent, same person).

## 2. Factorial (slides-XX s.17)
```prolog
factorial(0, 1).
factorial(A, B) :- A > 0, C is A - 1, factorial(C, D), B is A * D.
```
`?- factorial(3, X).` → C = 2 → C = 1 → C = 0 hits the fact (D = 1) → B = 1·1 = 1 → 2·1 = 2 → 3·2 = **6**. Multiplications happen **on the way back up**.
- `C is A - 1` must come **before** the recursive call (is/2 needs bound right side).
- `?- factorial(X, 120).` → **error**: `A > 0` with A unbound → "Arguments are not sufficiently instantiated". Arithmetic runs one way only.
- Tail-recursive version:
  ```prolog
  fact(N, F) :- fact(N, 1, F).
  fact(0, Acc, Acc).
  fact(N, Acc, F) :- N > 0, Acc1 is Acc * N, N1 is N - 1, fact(N1, Acc1, F).
  ```

## 3. Fibonacci: naive vs accumulator (s.18)
Naive `fibo/2` spawns two recursive calls per call → exponential (`fibo(25)` ≈ **1,092,530 inferences**). Accumulator `fib/2` carries the previous two values → linear. Or memoise with `:- table fibo/2.` Note the course seeds fib(0) = fib(1) = 1, so fibo(10) = **89**, fib(30) = **1,346,269**.

## 4. Lists run backwards (s.19)
`?- append(X, Y, [1,2,3]).` → X=[] Y=[1,2,3] ; X=[1] Y=[2,3] ; X=[1,2] Y=[3] ; X=[1,2,3] Y=[].

## 5. Spot the bug — isPerm (s.21)
```prolog
isPerm(X, Y) :- isInc(X, Y), isInc(Y, X).   % "every element of each occurs in the other"
```
`?- isPerm([1,1,2], [1,2,2]).` → **true** (wrong): that's **set equality**, not permutation; it also ignores length. Fix: `is_perm(X, Y) :- msort(X, S), msort(Y, S).` or use `permutation/2`.

## 6. Spot the bug — max with a cut (s.23)
`max(X, Y, X) :- X >= Y, !.  max(_, Y, Y).` → `?- max(5, 3, 3).` is **true**: the first head fails to unify (X = 5 vs third arg 3), so the second clause fires. Output unification must come **after** the cut: `max(X, Y, M) :- X >= Y, !, M = X.` — or avoid the cut: `max2(X, Y, M) :- ( X >= Y -> M = X ; M = Y ).`

## 7. Negation as failure
`?- \+ parent(X, ana).` → **false** (there is an X, hector). `?- X = sofia, \+ parent(X, _).` → X = sofia. Rule: bind before negating.

## 8. Arithmetic quick quiz
<details><summary>`X = 3 + 4.`</summary>X = 3+4 (a term)</details>
<details><summary>`X is 3 + 4.`</summary>X = 7</details>
<details><summary>`3 + 4 = 7.`</summary>false (structures differ)</details>
<details><summary>`3 + 4 =:= 7.`</summary>true</details>
<details><summary>`X is Y + 1.`</summary>ERROR: arguments not sufficiently instantiated</details>
<details><summary>`X is 17 mod 5.`</summary>X = 2</details>

Related: [prolog](../concepts/prolog.md) · [sld-resolution](../algorithms/sld-resolution.md) · [unification](../concepts/unification.md)
