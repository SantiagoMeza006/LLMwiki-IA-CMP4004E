---
title: Practice — Introduction & History of AI
type: practice
unit: intro
sources: [slides-01-intro-to-ai, rn-ch01-introduction]
updated: 2026-09-29
---

# Practice — Introduction & History

Answer before opening each `answer`.

1. Name the four approaches to AI and the two axes that generate them. Which one does R&N adopt and why?
   <details><summary>answer</summary>Human vs rational × thinking vs acting → thinking humanly (cognitive modelling), thinking rationally (laws of thought), acting humanly (Turing test), acting rationally (rational agents). R&N adopts acting rationally: more general than laws-of-thought (correct inference is just one route to rational action) and mathematically well-defined, so designs can be proven to achieve it.</details>
2. Describe the Turing test setup as presented in class. What capabilities must a machine have to pass it? What does the *total* Turing test add?
   <details><summary>answer</summary>Two humans + one computer; an isolated interrogator converses via text and must identify the machine; if fooled, the machine is deemed intelligent (operational definition). Needs NLP, knowledge representation, automated reasoning, machine learning. Total test adds computer vision/speech recognition and robotics.</details>
3. Why don't AI researchers focus on passing the Turing test? (analogy)
   <details><summary>answer</summary>They'd rather study underlying principles — like aeronautics succeeded by studying aerodynamics, not by building machines that fool pigeons.</details>
4. What happened at Dartmouth in 1956 and who organised it?
   <details><summary>answer</summary>Two-month workshop organised by McCarthy with Minsky, Shannon and Rochester; the conjecture that every aspect of intelligence can be precisely described so a machine can simulate it; first official use of the term "artificial intelligence"; Newell & Simon presented the Logic Theorist.</details>
5. Match: LISP · FORTRAN · Perceptron · SVM · Prolog → (Rosenblatt 1958, IBM 1957, McCarthy 1958, Colmerauer & Roussel 1972, Vapnik 1995).
   <details><summary>answer</summary>LISP–McCarthy 1958; FORTRAN–IBM 1957; Perceptron–Rosenblatt 1958; SVM–Vapnik (AT&T Bell Labs) 1995; Prolog–Colmerauer & Roussel 1972 (⚠️ slides-01 wrongly credits Dennis Ritchie — that's C).</details>
6. Why did backpropagation matter for neural networks? Which problem could a single perceptron not solve?
   <details><summary>answer</summary>It computes the gradient of the loss w.r.t. every weight, allowing multi-layer (nonlinear) networks to be trained; a single perceptron can't learn XOR (Minsky & Papert 1969), which multi-layer nets trained with backprop can.</details>
7. What is the value alignment problem? Give R&N's chess example.
   <details><summary>answer</summary>Ensuring the objective we give the machine matches what we truly want. A machine whose sole objective is winning at chess might blackmail/hypnotise its opponent or grab more computing power — logical consequences of a misspecified objective.</details>
8. What is the "standard model" of AI, and what refinement does limited rationality make?
   <details><summary>answer</summary>Build agents that optimise a fixed, given objective (as in control theory, OR, statistics, economics). Limited rationality: perfect rationality is computationally infeasible in complex environments, so agents must act appropriately with limited time.</details>
9. What is the Antikythera mechanism and why was it included in the course timeline?
   <details><summary>answer</summary>~200 BC Greek analog computer that predicted astronomical positions and eclipses up to 19 years ahead; it challenges the idea that technological development has always been incremental.</details>
10. Distinguish formal vs statistical methods for building models (slides-01 s.10) with two examples each.
    <details><summary>answer</summary>Formal: first-order calculus, lambda calculus, temporal logic, rewriting systems, causal calculus. Statistical: regression, classification, Bayesian networks, Markov networks.</details>
