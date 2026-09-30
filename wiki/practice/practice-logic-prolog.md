---
title: Practice — Logic Programming & Prolog
type: practice
unit: logic
sources: [slides-xx-prolog, rn-ch07-logical-agents, rn-ch08-first-order-logic, rn-ch09-fol-inference]
updated: 2026-09-30
---

# Practice — Logic Programming & Prolog

1. Explain "Algorithm = Logic + Control". Who said it?
   <details><summary>answer</summary>Kowalski (1979). The programmer writes the logic (clauses); the language supplies control (Prolog: depth-first, left-to-right backward chaining).</details>
2. Rank propositional logic, FOL, Horn clauses by expressiveness and cost.
   <details><summary>answer</summary>Propositional: decidable, no objects/"every". FOL: objects + quantifiers, undecidable. Horn clauses: restricted fragment, cheap (linear propositional entailment).</details>
3. Define Horn clause, definite clause, fact, goal clause. Write ¬A ∨ ¬B ∨ C as an implication.
   <details><summary>answer</summary>Horn: ≤ 1 positive literal. Definite: exactly one (a rule). Fact: definite with empty body. Goal: no positive literal (a query). ¬A ∨ ¬B ∨ C ≡ A ∧ B ⇒ C.</details>
4. Why can't Prolog express P ∨ Q?
   <details><summary>answer</summary>Two positive literals — not a Horn clause.</details>
5. Forward vs backward chaining — which does Prolog use and what's the advantage?
   <details><summary>answer</summary>Backward: goal-driven; touches only facts relevant to the query; space linear in the proof size.</details>
6. Translate: ∀x,y Parent(x,y) ∧ Female(x) ⇒ Mother(x,y).
   <details><summary>answer</summary>`mother(X, Y) :- parent(X, Y), female(X).`</details>
7. Unify (or say fail): (a) `f(X, b) = f(a, Y)` (b) `g(X, X) = g(a, b)` (c) `[H|T] = [a]` (d) `p(X) = q(X)` (e) `X = f(X)` in SWI.
   <details><summary>answer</summary>(a) X=a, Y=b (b) fail (c) H=a, T=[] (d) fail (different functor) (e) succeeds, cyclic term (no occurs check).</details>
8. Describe SLD resolution in four steps. Why is Prolog incomplete even though SLD resolution is complete?
   <details><summary>answer</summary>Leftmost goal; first matching clause in file order (unify); replace goal by body; backtrack on failure; succeed when no goals remain. Prolog's depth-first search rule can follow an infinite branch (left recursion).</details>
9. Why does `path(X,Z) :- path(X,Y), link(Y,Z).` placed first overflow the stack? Two fixes.
   <details><summary>answer</summary>Left recursion: it calls itself before consuming anything, forever. Fixes: `:- table path/2.`, or reorder to `path(X,Z) :- link(X,Y), path(Y,Z).` with the base case first.</details>
10. Results of: `X = 2*3.`, `X is 2*3.`, `2*3 =:= 6.`, `2*3 == 6.`, `X is Y*2.`
    <details><summary>answer</summary>X = 2*3; X = 6; true; false; instantiation error.</details>
11. findall vs setof when there are no solutions? With duplicates?
    <details><summary>answer</summary>findall returns [] and keeps duplicates/order; setof fails with no solutions, sorts and removes duplicates.</details>
12. What does `\+` mean, and what assumption makes it logical negation? What's the danger?
    <details><summary>answer</summary>Negation as failure: succeeds if the goal can't be proved. Equals negation under the closed-world assumption. Danger: with unbound variables it means "there is no X such that...", not "for this X": bind first.</details>
13. What's wrong with `max(X, Y, X) :- X >= Y, !.  max(_, Y, Y).`?
    <details><summary>answer</summary>`max(5, 3, 3)` succeeds: head unification fails for the first clause so the second clause answers 3. Put output unification after the cut or use if-then-else.</details>
14. Why does the isPerm program accept [1,1,2] and [1,2,2]?
    <details><summary>answer</summary>It checks mutual inclusion (set equality), not multiset equality/length. Fix with msort/2 or permutation/2.</details>
15. N-Queens: why is "test as you go" 17× faster than "generate and test" at N=8?
    <details><summary>answer</summary>It prunes a partial board as soon as a queen is attacked, instead of generating all N! permutations first — backtracking/CSP pruning.</details>
16. Lab 01: why does `sibling/2` need `X \= Y`, and why do some rules return duplicate answers?
    <details><summary>answer</summary>Otherwise everyone is their own sibling. Duplicates arise because there are several proofs (e.g. siblings share two parents → found once via mother and once via father; symmetric relations list each pair twice).</details>

## Propositional & first-order logic (R&N Ch 7–9)
17. Define entailment, soundness and completeness. Give the haystack analogy.
    <details><summary>answer</summary>α ⊨ β iff β is true in every model of α. Sound: derives only entailed sentences. Complete: derives all of them. Entailment = the needle is in the haystack; inference = finding it.</details>
18. State the deduction theorem and the refutation principle.
    <details><summary>answer</summary>α ⊨ β iff (α ⇒ β) is valid; α ⊨ β iff (α ∧ ¬β) is unsatisfiable.</details>
19. When is P ⇒ Q false? Is "5 is even ⇒ Sam is smart" true?
    <details><summary>answer</summary>Only when P is true and Q false. Yes — a false antecedent makes the implication true.</details>
20. How many models does TT-ENTAILS? check for the wumpus KB R1–R5, and in how many is the KB true?
    <details><summary>answer</summary>2⁷ = 128 models; 3 satisfy the KB, all with ¬P1,2.</details>
21. Convert B1,1 ⇔ (P1,2 ∨ P2,1) to CNF.
    <details><summary>answer</summary>(¬B1,1 ∨ P1,2 ∨ P2,1) ∧ (¬P1,2 ∨ B1,1) ∧ (¬P2,1 ∨ B1,1).</details>
22. How does resolution prove KB ⊨ α? When does PL-RESOLUTION return false?
    <details><summary>answer</summary>Convert KB ∧ ¬α to CNF and resolve pairs until the empty clause appears (⇒ entailed). It returns false when no new clauses can be added.</details>
23. Why can't WalkSAT be used to prove that a wumpus square is safe?
    <details><summary>answer</summary>Proving safety = showing KB ∧ ¬Safe is unsatisfiable; WalkSAT can find models but cannot prove none exist.</details>
24. Name DPLL's three improvements over truth-table enumeration.
    <details><summary>answer</summary>Early termination, pure symbol heuristic, unit clause heuristic (unit propagation).</details>
25. What is the frame problem?
    <details><summary>answer</summary>The need to state what does not change after actions; naive frame axioms need O(m·n) sentences; successor-state axioms fix it.</details>
26. What does FOL commit to ontologically that propositional logic doesn't?
    <details><summary>answer</summary>Objects and relations among them (not just facts).</details>
27. Fix these translations: "∀x Student(x) ∧ Smart(x)" for "all students are smart"; "∃x Student(x) ⇒ Smart(x)" for "some student is smart".
    <details><summary>answer</summary>∀x Student(x) ⇒ Smart(x); ∃x Student(x) ∧ Smart(x).</details>
28. Universal vs existential instantiation — how many times can each be applied, and what is a Skolem constant?
    <details><summary>answer</summary>UI: any number of times with any ground term. EI: once, with a brand-new constant (Skolem constant); then the ∃ sentence can be dropped.</details>
29. Why is FOL entailment only semidecidable?
    <details><summary>answer</summary>Procedures can confirm every entailed sentence, but no procedure can always say "no" for non-entailed ones (Turing/Church; related to the halting problem).</details>
30. Unify Knows(John, x) with Knows(x, Elizabeth). Why does it fail and how is it fixed?
    <details><summary>answer</summary>x can't be both John and Elizabeth; the shared variable name is accidental → standardize apart (rename to x17) → {x/Elizabeth, x17/John}.</details>
31. Why do Prolog systems omit the occur check?
    <details><summary>answer</summary>It makes unification quadratic; omitting it is faster and rarely causes unsound results in practice.</details>
32. Why do 4 course facts mean "exactly 4 courses" in Prolog but not in FOL?
    <details><summary>answer</summary>Prolog uses database semantics (unique names + closed world); in FOL the facts allow other courses and allow names to co-refer (1 to ∞ courses).</details>
33. Forward vs backward chaining on path/2 over a graph — which can loop, and what fixes it?
    <details><summary>answer</summary>Depth-first backward chaining (Prolog) loops with left recursion and repeats work (877 vs 62 inferences in R&N's example); forward chaining reaches a fixed point. Tabling fixes Prolog.</details>
34. Skolemize ∀x ∃y Loves(y, x). Why not a constant?
    <details><summary>answer</summary>Loves(G(x), x). A constant would force the same lover for everyone; the Skolem function lets the lover depend on x.</details>
35. What does constraint logic programming add? Example?
    <details><summary>answer</summary>Variables can be constrained instead of bound; triangle(3,4,Z) returns 1 < Z < 7 instead of failing.</details>
