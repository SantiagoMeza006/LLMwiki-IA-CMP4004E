---
title: Resolution (propositional and first-order) and CNF conversion
type: algorithm
unit: logic
sources: [rn-ch07-logical-agents, rn-ch09-fol-inference, slides-xx-prolog]
updated: 2026-09-30
---

# Resolution 🎯

Slides-XX s.3: "Resolution — a single inference rule that is refutation-complete for propositional logic — needs clause form as input." (R&N §7.5.2, §9.5.)

## The rule
**Unit resolution:** `ℓ1 ∨ … ∨ ℓk,  m  ⊢  ℓ1 ∨ … ∨ ℓ(i−1) ∨ ℓ(i+1) ∨ … ∨ ℓk` where ℓi and m are complementary.
**Full resolution:** two clauses with complementary literals ℓi and mj produce a clause with **all other literals of both**:
```
P1,1 ∨ P3,1,   ¬P1,1 ∨ ¬P2,2
-----------------------------
        P3,1 ∨ ¬P2,2
```
- Resolve on **one** complementary pair at a time (from P ∨ ¬Q ∨ R and ¬P ∨ Q you get ¬Q ∨ Q ∨ R, *not* R).
- **Factoring:** keep one copy of repeated literals (A ∨ A → A).
- Sound: if ℓi is true then mj is false, so the rest of the second clause holds, and vice versa.

## Converting to CNF (propositional) 🎯
Example `B1,1 ⇔ (P1,2 ∨ P2,1)`:
1. **Eliminate ⇔**: `(B1,1 ⇒ (P1,2 ∨ P2,1)) ∧ ((P1,2 ∨ P2,1) ⇒ B1,1)`
2. **Eliminate ⇒** (α ⇒ β ≡ ¬α ∨ β): `(¬B1,1 ∨ P1,2 ∨ P2,1) ∧ (¬(P1,2 ∨ P2,1) ∨ B1,1)`
3. **Move ¬ inwards** (De Morgan, double negation): `(¬B1,1 ∨ P1,2 ∨ P2,1) ∧ ((¬P1,2 ∧ ¬P2,1) ∨ B1,1)`
4. **Distribute ∨ over ∧**: `(¬B1,1 ∨ P1,2 ∨ P2,1) ∧ (¬P1,2 ∨ B1,1) ∧ (¬P2,1 ∨ B1,1)`

## The algorithm — proof by refutation
To show KB ⊨ α, show **KB ∧ ¬α is unsatisfiable**:
```
function PL-RESOLUTION(KB, α) returns true or false
    clauses ← the set of clauses in the CNF representation of KB ∧ ¬α
    new ← {}
    while true:
        for each pair of clauses Ci, Cj in clauses:
            resolvents ← PL-RESOLVE(Ci, Cj)
            if resolvents contains the empty clause: return true
            new ← new ∪ resolvents
        if new ⊆ clauses: return false
        clauses ← clauses ∪ new
```
- **Empty clause** = False (a disjunction with no disjuncts) → contradiction found → KB ⊨ α.
- No new clauses → KB ⊭ α.
- Clauses containing both P and ¬P are tautologies — discard them.
- **Ground resolution theorem:** if a set of clauses is unsatisfiable, its **resolution closure** contains the empty clause → PL-RESOLUTION is **complete** (and always terminates, since only finitely many clauses exist over k symbols).

## First-order resolution (R&N §9.5)
**CNF for FOL** — "Everyone who loves all animals is loved by someone": `∀x [∀y Animal(y) ⇒ Loves(x, y)] ⇒ [∃y Loves(y, x)]`
1. Eliminate ⇒: `∀x ¬[∀y ¬Animal(y) ∨ Loves(x, y)] ∨ [∃y Loves(y, x)]`
2. Move ¬ inwards (¬∀x p → ∃x ¬p, ¬∃x p → ∀x ¬p): `∀x [∃y Animal(y) ∧ ¬Loves(x, y)] ∨ [∃y Loves(y, x)]`
3. **Standardize variables**: `∀x [∃y Animal(y) ∧ ¬Loves(x, y)] ∨ [∃z Loves(z, x)]`
4. **Skolemize** — replace each ∃ variable by a **Skolem function** of the enclosing ∀ variables: `∀x [Animal(F(x)) ∧ ¬Loves(x, F(x))] ∨ Loves(G(x), x)` (constants A, B would be wrong: they'd force the *same* animal/lover for everyone)
5. **Drop ∀**: `[Animal(F(x)) ∧ ¬Loves(x, F(x))] ∨ Loves(G(x), x)`
6. **Distribute ∨ over ∧**: `[Animal(F(x)) ∨ Loves(G(x), x)] ∧ [¬Loves(x, F(x)) ∨ Loves(G(x), x)]`

**Lifted rule:** literals are complementary if one **unifies** with the negation of the other; apply the unifier θ to the resolvent. E.g. `[Animal(F(x)) ∨ Loves(G(x), x)]` and `[¬Loves(u, v) ∨ ¬Kills(u, v)]` with θ = {u/G(x), v/x} → `[Animal(F(x)) ∨ ¬Kills(G(x), x)]`. **Binary resolution + factoring** is refutation-complete for FOL.

**Examples:** the crime KB (resolution "spine" from ¬Criminal(West) — exactly the goal list of backward chaining: **backward chaining = resolution with a particular control strategy**), and "Curiosity killed the cat" (needs Skolem functions and factoring). Answer extraction: negate `∃w Kills(w, Tuna)` and track the binding {w/Curiosity}.

**Strategies:** unit preference, set of support, input resolution (every step uses an input clause — Horn KBs + Modus Ponens), subsumption. Equality: demodulation, paramodulation.

## Properties
| | Propositional | First-order |
|---|---|---|
| Sound | ✅ | ✅ |
| Complete | refutation-complete; always terminates | refutation-complete; may not terminate if α is not entailed (semidecidable) |
| Needs | CNF | CNF + Skolemization + unification |

Worked: [logic-inference-traces](../exercises/logic-inference-traces.md). Related: [propositional-logic](../concepts/propositional-logic.md) · [logic-to-horn-clauses](../concepts/logic-to-horn-clauses.md) · [inference-methods-comparison](../comparisons/inference-methods-comparison.md)
