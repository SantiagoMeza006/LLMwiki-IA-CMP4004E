---
title: Practice — Logic Programming & Prolog
type: practice
unit: logic
sources: [slides-xx-prolog]
updated: 2026-09-29
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
