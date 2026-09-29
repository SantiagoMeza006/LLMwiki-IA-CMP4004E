---
title: "Slides 01 — Introduction to Artificial Intelligence"
type: source
unit: intro
raw: "raw/01_Introduction to Artificial Intelligence.pptx"
sources: [slides-01-intro-to-ai]
updated: 2026-09-29
---

# Slides 01 — Introduction to Artificial Intelligence

**Author:** Daniel Riofrío (thanks to Luciana Valdivieso) · 19 slides · Raw: `raw/01_Introduction to Artificial Intelligence.pptx`

## What it covers
A historical tour of AI, from ancient automata to LLM agents, organised as a timeline.

| Slide | Content |
|---|---|
| 2 | What do we mean by *intelligence*? (understand, solve problems, knowledge, meaning, skill). Timeline 1700 → 2026 ending in "Generative AI, LLMs, Agents". |
| 3 | Mechanical Turk (von Kempelen, 1770) — *appeared* to play chess; Jaquet-Droz automata (1768–1774: musician, draughtsman, writer). |
| 4 | Z1 (Konrad Zuse, 1936, binary, punched cards, floating point) and ENIAC (1945, vacuum tubes, 170 m², 27 t). |
| 5 | 🎯 Turing Test (1950): 2 humans + 1 computer, interrogator via text terminal; operational definition of intelligence. |
| 6 | FORTRAN (IBM, 1957, imperative) and LISP (McCarthy, 1958, lambda calculus, lists, prefix calls `(f a1 a2)`). |
| 7 | 🎯 Birth of AI: Dartmouth 1956 (McCarthy, Minsky, Shannon, Rochester) and the proposal quote ("every aspect of learning... can be so precisely described that a machine can be made to simulate it"). |
| 8 | Perceptron (Rosenblatt, 1958): neuron-inspired; knowledge stored in synaptic weights. |
| 9 | Prolog (1970s): logic programming, *Algorithm = Logic + Control*, expert systems, positive clauses ≈ first-order logic. ⚠️ see below. |
| 10 | What is a model? Formal methods (first-order calculus, lambda calculus, temporal logic, rewriting systems, causal calculus) vs statistical methods (regression, classification, Bayesian networks, Markov networks). |
| 11 | Backpropagation (dated 1975): gradient of the loss w.r.t. each weight → multi-layer nets → solves XOR. |
| 12 | Support Vector Machine (Vapnik et al., AT&T Bell Labs, 1995): maximise the margin between two subspaces. |
| 13 | Deep Learning (term 1986; Bengio, Hinton, LeCun). |
| 14–15 | Limits of statistical models → Causal models; Judea Pearl's causal calculus encodes cause→effect in a DAG. |
| 17–18 | Antikythera mechanism (~200 BC): earliest known analog computer, predicted eclipses up to 19 years ahead. |
| 19 | Talos in Greek myth (~800 BC?): a bronze automaton guarding Crete. |

## Where it fits
Unit **intro**. Pairs with [R&N Chapter 1](rn-ch01-introduction.md). Main wiki pages fed:
[history-of-ai](../concepts/history-of-ai.md), [what-is-ai](../concepts/what-is-ai.md).

> ⚠️ **Discrepancy (slide 9):** the slide says Prolog was "created by Dennis Ritchie at Bell Labs" and is an "imperative, compiled language" with state/loops. That describes **C**, not Prolog. Prolog was created in **Marseille in 1972 by Alain Colmerauer and Philippe Roussel**, building on Robert Kowalski's theory, and it is declarative ([slides-XX Prolog](slides-xx-prolog.md) s.8). See [discrepancies](../discrepancies.md).
