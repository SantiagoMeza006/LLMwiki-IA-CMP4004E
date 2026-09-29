---
title: Unification
type: concept
unit: logic
sources: [slides-xx-prolog]
updated: 2026-09-29
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

## Why it matters
Unification is how [backward chaining](forward-and-backward-chaining.md) matches a goal against clause heads in [SLD resolution](../algorithms/sld-resolution.md); the **answer** to a Prolog query is the substitution that made the proof work.

Related: [prolog](prolog.md) · [prolog-traces](../exercises/prolog-traces.md)
