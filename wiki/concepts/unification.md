---
title: Unification
type: concept
unit: logic
sources: [slides-xx-prolog, rn-ch09-fol-inference]
updated: 2026-09-30
---

# Unification 🎯

**Given two terms, find the substitution that makes them identical — or fail.** It is pattern matching in **both directions**: neither side is the "input" (slides-XX s.14).

## Rules
1. **Atoms and numbers** unify only with themselves.
2. A **variable** unifies with anything, and then stays **bound**.
3. **Compound terms** unify iff same **functor and arity**, and arguments unify pairwise (left to right, carrying bindings along).
4. Prolog does **no occurs check** by default: `X = f(X)` builds a cyclic term. `unify_with_occurs_check(X, f(X))` fails, as logic requires.

## Examples
```prolog
?- f(a, Y) = f(X, b).        % X = a, Y = b.
?- [H|T] = [1, 2, 3].        % H = 1, T = [2, 3].
?- f(a) = g(a).              % false. (different functors)
?- f(X, X) = f(a, b).        % false. (X can't be both a and b)
?- p(X, g(Y)) = p(h(Z), g(X)).  % X = h(Z), Y = h(Z).
?- X = f(X).                 % X = f(X). (cyclic, no occurs check)
?- 3 + 4 = 7.                % false. (+(3,4) vs 7 — no evaluation!)
```

## Most general unifier (MGU)
Unification returns the **most general** substitution — it binds only what it must. `f(X, Y) = f(a, Z)` gives `X = a, Y = Z`, not `Y = Z = b`.

## The UNIFY algorithm (R&N Fig 9.1)
```
function UNIFY(x, y, θ = empty) returns a substitution to make x and y identical, or failure
    if θ = failure: return failure
    else if x = y: return θ
    else if VARIABLE?(x): return UNIFY-VAR(x, y, θ)
    else if VARIABLE?(y): return UNIFY-VAR(y, x, θ)
    else if COMPOUND?(x) and COMPOUND?(y): return UNIFY(ARGS(x), ARGS(y), UNIFY(OP(x), OP(y), θ))
    else if LIST?(x) and LIST?(y): return UNIFY(REST(x), REST(y), UNIFY(FIRST(x), FIRST(y), θ))
    else return failure

function UNIFY-VAR(var, x, θ) returns a substitution
    if {var/val} ∈ θ for some val: return UNIFY(val, x, θ)
    else if {x/val} ∈ θ for some val: return UNIFY(var, val, θ)
    else if OCCUR-CHECK?(var, x): return failure
    else return add {var/x} to θ
```
R&N examples (FOL notation: lowercase = variable):
| UNIFY(…) | Result |
|---|---|
| Knows(John, x), Knows(John, Jane) | {x/Jane} |
| Knows(John, x), Knows(y, Bill) | {x/Bill, y/John} |
| Knows(John, x), Knows(y, Mother(y)) | {y/John, x/Mother(John)} |
| Knows(John, x), Knows(x, Elizabeth) | **failure** — x can't be John and Elizabeth |
| Knows(John, x), Knows(x17, Elizabeth) | {x/Elizabeth, x17/John} — after **standardizing apart** |

- **Standardizing apart:** rename variables of one sentence so the two share none (`Knows(x, Elizabeth)` means *everyone* knows Elizabeth; the clash of names was accidental). Prolog does this automatically for every clause it uses.
- **MGU:** Knows(John, x) vs Knows(y, z) → {y/John, x/z} (most general) rather than {y/John, x/John, z/John}. Every unifiable pair has a single MGU up to renaming.
- **Occur check:** S(x) can't unify with S(S(x)). It makes UNIFY quadratic, so **many logic programming systems (Prolog) omit it** — occasionally unsound, rarely a problem in practice (R&N §9.2.1, §9.4.2).

## Why it matters
Unification is how [backward chaining](forward-and-backward-chaining.md) matches a goal against clause heads in [SLD resolution](../algorithms/sld-resolution.md); the **answer** to a Prolog query is the substitution that made the proof work.

Related: [prolog](prolog.md) · [prolog-traces](../exercises/prolog-traces.md)
