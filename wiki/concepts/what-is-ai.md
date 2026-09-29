---
title: What Is AI?
type: concept
unit: intro
sources: [rn-ch01-introduction, slides-01-intro-to-ai]
updated: 2026-09-29
---

# What Is AI?

## Four approaches (R&N §1.1) 🎯
Two axes: **human vs rational** fidelity, and **thought vs behaviour**.

|  | Human | Rational |
|---|---|---|
| **Thinking** | *Thinking humanly* — cognitive modelling (introspection, psychological experiments, brain imaging). E.g. Newell & Simon's GPS compared its reasoning steps with humans'. → cognitive science. | *Thinking rationally* — "laws of thought": Aristotle's syllogisms → formal logic → the **logicist** tradition. Problem: real knowledge is rarely certain → probability; and correct thought alone doesn't produce behaviour. |
| **Acting** | *Acting humanly* — the [Turing test](#the-turing-test). | *Acting rationally* — the **rational agent** approach: act to achieve the best outcome, or the best **expected** outcome under uncertainty. ✅ Dominant approach. |

**Why the rational-agent approach won** (R&N §1.1.4): (1) more general than laws-of-thought — correct inference is only one way to act rationally (e.g. a reflex recoil from a hot stove is rational without inference); (2) rationality is mathematically well-defined, so we can derive agent designs that provably achieve it.

## The Turing test
- Slides-01 s.5: 2 humans + 1 computer; an isolated interrogator asks questions via text and must tell which is the machine; if fooled, the machine is deemed intelligent — an *operational* definition of intelligence (Turing 1950).
- Capabilities needed (R&N): **natural language processing**, **knowledge representation**, **automated reasoning**, **machine learning**. The **total Turing test** adds **computer vision** (+ speech recognition) and **robotics**. These six disciplines compose most of AI.
- AI researchers rarely aim to pass it: like aeronautics stopped imitating birds, AI studies the underlying principles.

## The standard model and its limits
- **Standard model:** build agents that optimise a fixed objective given to them — shared with control theory (minimise cost), operations research (maximise reward), statistics (minimise loss), economics (maximise utility).
- **Limited rationality:** perfect rationality is computationally infeasible in complex environments; act appropriately with limited time.
- **Value alignment problem:** the objective we put in must match what we truly want (King Midas). A chess machine that only values winning might try to blackmail its opponent. Proposal: machines that pursue *our* objectives while **uncertain** about them → cautious, ask permission, defer to humans → **provably beneficial** AI.

## Intelligence (slides-01 s.2)
Informal senses listed in class: ability to understand/comprehend; to solve problems; knowledge and comprehension; the meaning assignable to a proposition; ability, skill and experience.

## AI vs ML
Machine learning is a *subfield* of AI (improving from experience); some AI systems use ML, some don't (R&N fn.1).

Related: [rationality](rationality.md) · [agents-and-environments](agents-and-environments.md) · [history-of-ai](history-of-ai.md)
