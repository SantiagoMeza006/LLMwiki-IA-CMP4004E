---
title: "R&N Chapter 8 — First-Order Logic"
type: source
unit: logic
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch08-first-order-logic]
updated: 2026-09-30
---

# R&N Chapter 8 — First-Order Logic (pp. 268–297)

The language Prolog is a fragment of (definite clauses of FOL). Slides-XX s.2 summarises it as "objects and quantifiers. Undecidable."

## Section map → wiki pages
| Section | Content | Wiki page |
|---|---|---|
| 8.1 | Representation revisited: programming languages vs natural language; declarative, compositional, context-independent, unambiguous; **ontological commitment** (facts vs objects & relations) and **epistemological commitment** (true/false/unknown vs degrees of belief); fuzzy, temporal, higher-order logic. | [first-order-logic](../concepts/first-order-logic.md) |
| 8.2 | Models (domain, objects, relations as sets of tuples, total functions); symbols (**constants, predicates, functions**, arity) and **interpretations**; terms, atomic sentences, connectives; **quantifiers ∀, ∃**, nested quantifiers, De Morgan for quantifiers; **equality**; **database semantics** (unique-names, closed-world, domain closure). | same |
| 8.3 | TELL/ASK/ASKVARS, substitutions (binding lists); **kinship domain** axioms (Mother, Husband, Parent/Child, Grandparent, Sibling with x ≠ y), axioms vs theorems vs definitions; numbers (Peano), sets, lists; wumpus world in FOL. | same |
| 8.4 | Knowledge engineering process (identify questions, assemble knowledge, choose vocabulary/ontology, encode general knowledge, encode the instance, query, debug); electronic circuits domain. | same |

## Takeaways 🎯
1. FOL assumes the world has **objects** and **relations**; propositional logic only **facts**.
2. **∀ goes with ⇒, ∃ goes with ∧.** `∀x King(x) ∧ Person(x)` says everything is a king; `∃x Crown(x) ⇒ OnHead(x, John)` says almost nothing.
3. Quantifier order matters: `∀x ∃y Loves(x,y)` ≠ `∃y ∀x Loves(x,y)`.
4. Standard FOL semantics doesn't assume distinct names or a closed world; **Prolog uses database semantics** (unique names + closed world + domain closure) — which is why negation as failure works there.
5. The textbook kinship definition of Sibling includes **x ≠ y** — exactly the point of Lab 01's `X \= Y` question.
