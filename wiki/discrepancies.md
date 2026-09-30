---
title: Discrepancies & Exam Traps
type: overview
unit: all
sources: [slides-01-intro-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, rn-ch01-introduction, rn-ch03-search, dorigo-1996-ant-system, holland-1992-genetic-algorithms, note-a-star-vs-dijkstra, rn-ch04-complex-environments, rn-ch05-csp, rn-ch06-games, rn-ch07-logical-agents, rn-ch08-first-order-logic, rn-ch09-fol-inference]
updated: 2026-09-30
---

# Discrepancies & Exam Traps

Where sources disagree, contain errors, or use different conventions. **Rule of thumb:** trust the textbook/original paper for facts, but know the slide's wording because exams may follow the slides.

| # | Topic | Source A says | Source B says | Resolution |
|---|---|---|---|---|
| 1 | Who created Prolog | slides-01 s.9: "Created by Dennis Ritchie at Bell Labs... imperative, compiled" | slides-XX s.8: Colmerauer & Roussel, Marseille, **1972**, theory from Kowalski; declarative | slides-01 describes **C**. Prolog = Colmerauer & Roussel 1972. |
| 2 | Prolog date | slides-01 timeline: 1970 | slides-XX: 1972 | 1972 (timeline block rounding). |
| 3 | "Best-first search" | slides-02 s.12: the greedy algorithm, f = h | R&N §3.3.1: the generic family (any f); greedy is one member | Say "greedy best-first" for f = h. |
| 4 | A* completeness | slides-02 s.14: complete "if h is admissible" (R&N's own Ch 3 **summary** says the same: "complete and optimal, provided that h(n) is admissible") | R&N §3.5.2 body: complete given positive costs and a finite space or an existing solution; admissibility is what gives **optimality** | Safe exam answer: "complete (positive costs) and optimal if h is admissible". |
| 5 | Model-based agent models | slides-03 s.15: "world model" (how the env evolves) + "transition model" (effects of my actions) | R&N §2.4.3: **transition model** (both) + **sensor model** (how state appears in percepts) | Know both naming schemes. |
| 6 | "What is an agent?" slide | slides-03 s.2 contains "A proposition is a statement that can be true or false..." | — | Copy-paste from a logic deck; ignore for agents. |
| 7 | Stochastic vs nondeterministic | slides-03 s.9: non-deterministic ≈ stochastic ("randomness") | R&N §2.3.2: *stochastic* = probabilities quantified; *nondeterministic* = possibilities listed without probabilities | R&N distinction is more precise. |
| 8 | ACO ρ | slides-04 s.14: τ ← (1−ρ)τ + ΣΔτ, ρ = **evaporation** | Dorigo 1996 eq. 1: τ ← ρτ + Δτ, ρ = **persistence** (evaporation = 1−ρ) | Read the formula. Equal only at ρ = 0.5. |
| 9 | GA date | slides-04 s.5: "John Holland – 1992" | slides-04 s.2: Holland 1975; Holland 1992: developed mid-1960s | 1992 = the Sci. Am. article; GAs: 1960s, book 1975. |
| 10 | Backpropagation date | slides-01 s.11: 1975 | R&N §1.3.3: developed early 1960s (Kelley 1960, Bryson 1962); resurgence late 1980s | Slide date is close to Werbos's 1974 PhD thesis (applying backprop to neural nets); R&N stresses earlier roots. Know both. |
| 11 | Romania units | my note: "418 km" | R&N Fig 3.1: distances in **miles** | Use miles (or unitless 418). |
| 12 | 8-puzzle state count | PDF OCR: "181, 400" | 9!/2 = **181,440** | OCR error. |
| 13 | Prisoner's Dilemma encoding | Holland PDF OCR: "54 possibilities", "2^54" | 4 outcomes³ = **64**; 2^64 strategies | OCR error. |
| 14 | DFS completeness | slides-02 s.9: complete only with repeated-state control and finite space | R&N Fig 3.15 (tree-like): "No"; graph-search version complete in finite spaces | Consistent — just be explicit about which version. |
| 15 | Environment list for Ch 3 search | slides-02 s.2: observable, deterministic, discrete, static | R&N Ch 3 intro: also episodic, single-agent, known | R&N's list is longer; both fine. |
| 16 | CSP "constraint propagation" list | slides-02 s.24 lists forward checking, arc consistency **and MRV** as propagation | R&N: MRV is a *variable-ordering heuristic*, not propagation | Know MRV's real role. |

| 17 | Simulated annealing ΔE | R&N 4th ed. Fig 4.5: ΔE = VALUE(current) − VALUE(next), VALUE treated as a **cost** | R&N 3rd ed. / most courses: ΔE = VALUE(next) − VALUE(current) for **maximisation** | Same rule either way: improvements always accepted; a worse move has ΔE < 0 and is accepted with probability e^(ΔE/T). |
| 18 | Case of variables | FOL in R&N: constants/predicates **Uppercase**, variables **lowercase** | Prolog: variables **Uppercase**, constants lowercase (slides-XX s.7; R&N §9.4.2) | Don't mix notations in an answer. |
| 19 | Where the CSP/games/logic material comes from | Initial ingest (2026-09-29): Ch 5–9 "not in excerpt", pages based on slides | Full book added 2026-09-30 | Pages now cite R&N Ch 4–9 directly; slide wording kept where the exam may follow it. |
| 20 | "Mutation" in GAs | slides-04 s.5: variation "emulated by changing a bit with a certain probability" | R&N §4.1.4: per-bit flip with probability = mutation rate; for 8-queens digit strings, mutation = move a queen to a random row | Same idea, different encodings (bit vs digit strings). |

*Add a row whenever a new source contradicts an existing page.*
