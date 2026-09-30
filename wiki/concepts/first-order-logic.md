---
title: First-Order Logic (FOL)
type: concept
unit: logic
sources: [rn-ch08-first-order-logic, slides-xx-prolog]
updated: 2026-09-30
---

# First-Order Logic 🎯

(R&N Ch 8, [source](../sources/rn-ch08-first-order-logic.md); slides-XX s.2: "constants, variables, predicates, quantifiers — objects and quantifiers, undecidable".)

## Why go beyond propositional logic
Propositional logic can't state general rules concisely ("squares next to the wumpus are smelly" needs one sentence per square). FOL, like natural language, talks about **objects**, **relations** (properties are unary relations) and **functions**.

| Language | Ontological commitment (what exists) | Epistemological commitment (what the agent believes) |
|---|---|---|
| Propositional logic | facts | true / false / unknown |
| **First-order logic** | facts, **objects, relations** | true / false / unknown |
| Temporal logic | facts, objects, relations, times | true / false / unknown |
| Probability theory | facts | degree of belief ∈ [0, 1] |
| Fuzzy logic | facts with degree of truth ∈ [0, 1] | known interval value |

## Syntax
- **Constant symbols** (Richard, John) → objects; **predicate symbols** (Brother, King) → relations; **function symbols** (LeftLeg) → functions. Each has an **arity**. (R&N: symbols start with **uppercase**, variables are **lowercase** — the *opposite* of Prolog.)
- **Term** = constant | variable | f(term, …) — "a complicated name", not a subroutine call. **Ground term**: no variables.
- **Atomic sentence** = Predicate(term, …) or term = term, e.g. `Brother(Richard, John)`, `Married(Father(Richard), Mother(John))`.
- Complex sentences with ¬ ∧ ∨ ⇒ ⇔, and **quantifiers** ∀, ∃.

## Semantics
A **model** = a nonempty **domain** of objects + an **interpretation** mapping constants → objects, predicates → relations (sets of tuples), functions → total functions. Unlike propositional logic there are infinitely many models, so entailment can't be checked by enumeration.

## Quantifiers 🎯
- `∀x King(x) ⇒ Person(x)` — "all kings are persons". **∀ pairs with ⇒.** (`∀x King(x) ∧ Person(x)` would claim everything is a king and a person.)
- `∃x Crown(x) ∧ OnHead(x, John)` — "John has a crown on his head". **∃ pairs with ∧.** (`∃x Crown(x) ⇒ OnHead(x, John)` is true as soon as anything is not a crown — says almost nothing.)
- **Order matters:** `∀x ∃y Loves(x, y)` (everybody loves somebody) vs `∃y ∀x Loves(x, y)` (someone is loved by everybody).
- **De Morgan for quantifiers:** ¬∃x P ≡ ∀x ¬P · ¬∀x P ≡ ∃x ¬P · ∀x P ≡ ¬∃x ¬P · ∃x P ≡ ¬∀x ¬P.
- A variable belongs to the innermost quantifier that mentions it; use distinct names to avoid confusion.

## Equality and database semantics
- `Father(John) = Henry`. "Richard has at least two brothers": `∃x, y Brother(x, Richard) ∧ Brother(y, Richard) ∧ ¬(x = y)`.
- "Richard's brothers are John and Geoffrey" needs, in standard FOL, `… ∧ John ≠ Geoffrey ∧ ∀x Brother(x, Richard) ⇒ (x = John ∨ x = Geoffrey)`.
- **Database semantics** makes this easy: **unique-names assumption** (distinct constants = distinct objects) + **closed-world assumption** (unknown atoms are false) + **domain closure** (no unnamed objects). **Prolog uses database semantics** → [prolog](prolog.md#negation-as-failure-and-the-cut-).

## Using FOL — the kinship domain (R&N §8.3.2)
```
∀m, c  Mother(c) = m ⇔ Female(m) ∧ Parent(m, c)
∀w, h  Husband(h, w) ⇔ Male(h) ∧ Spouse(h, w)
∀p, c  Parent(p, c) ⇔ Child(c, p)
∀g, c  Grandparent(g, c) ⇔ ∃p Parent(g, p) ∧ Parent(p, c)
∀x, y  Sibling(x, y) ⇔ x ≠ y ∧ ∃p Parent(p, x) ∧ Parent(p, y)
```
- These are **axioms** that are also **definitions** (they bottom out in primitives like Child, Female). `∀x,y Sibling(x,y) ⇔ Sibling(y,x)` is a **theorem** (entailed) — storing theorems saves recomputation.
- Note the **x ≠ y** in Sibling — the same reason Lab 01's `sibling/2` needs `X \= Y`.
- ASK returns true/false; **ASKVARS** returns **substitutions** (binding lists) like {x/John}.

## Knowledge engineering process (R&N §8.4)
1. Identify the questions. 2. Assemble the relevant knowledge. 3. Decide on a vocabulary (the **ontology**). 4. Encode general domain knowledge. 5. Encode the specific problem instance. 6. Pose queries and get answers. 7. Debug the KB (missing or wrong axioms). Example domain: electronic circuits (one-bit adder).

Related: [propositional-logic](propositional-logic.md) · [first-order-inference](first-order-inference.md) · [unification](unification.md) · [logic-inference-traces](../exercises/logic-inference-traces.md)
