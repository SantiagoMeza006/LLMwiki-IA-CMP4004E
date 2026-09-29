---
title: History of AI — Timeline
type: concept
unit: intro
sources: [slides-01-intro-to-ai, rn-ch01-introduction, slides-04-optimization, slides-xx-prolog, holland-1992-genetic-algorithms]
updated: 2026-09-29
---

# History of AI — Timeline

Merged from [slides-01](../sources/slides-01-intro-to-ai.md) (class timeline) and [R&N §1.3](../sources/rn-ch01-introduction.md). 🎯 = on the slides.

## Precursors
| When | What |
|---|---|
| ~800 BC? | 🎯 **Talos** (Greek myth): bronze automaton guarding Crete. |
| ~200 BC | 🎯 **Antikythera mechanism**: earliest known analog computer; predicted astronomical positions and eclipses up to 19 years ahead; found 1900, studied 1902/1951/1971. |
| 1768–1774 | 🎯 Jaquet-Droz automata (musician, draughtsman, writer). |
| 1770 | 🎯 **Mechanical Turk** (von Kempelen): *appeared* to play strong chess (it was a hoax with a hidden human operator). |
| 1936 | 🎯 **Z1** (Konrad Zuse): binary, punched-card program, floating point, memory. |
| 1945 | 🎯 **ENIAC**: general-purpose, programmable, vacuum tubes, 170 m², 27 t. |

## Birth of AI (1943–1956)
| When | What |
|---|---|
| 1943 | McCulloch & Pitts: artificial neurons (on/off) can compute any computable function and implement logic gates (R&N). |
| 1949 | Hebbian learning (Hebb). |
| 1950 | 🎯 **Turing, "Computing Machinery and Intelligence"** — Turing test; also introduced ML, GAs and RL ideas. SNARC (Minsky & Edmonds), first neural-net computer, 40 neurons. |
| 1952 | Checkers programs (Strachey; Samuel at IBM — learned to beat its creator). |
| 1956 | 🎯 **Dartmouth workshop** (McCarthy, Minsky, Shannon, Rochester; 10 attendees): first use of the term *artificial intelligence*. Newell & Simon's **Logic Theorist**. |

## Early enthusiasm (1952–1969)
| When | What |
|---|---|
| 1957 | 🎯 FORTRAN (IBM). GPS (Newell & Simon) → physical symbol system hypothesis. |
| 1958 | 🎯 **LISP** (McCarthy) — dominant AI language for 30 years; Advice Taker. 🎯 **Perceptron** (Rosenblatt). |
| 1960 | 🎯 Fogel: evolutionary programming (evolving finite-state machines). |
| 1965 | Robinson's resolution (complete theorem proving for FOL). |
| mid-1960s | Holland develops the genetic algorithm (Holland 1992). |
| 1960s | Microworlds (SAINT, ANALOGY, STUDENT), blocks world, SHRDLU (1972). |

## A dose of reality (1966–1973)
Combinatorial explosion; Lighthill report (1973) ends UK funding; **Minsky & Papert, *Perceptrons* (1969)**: a single perceptron cannot learn XOR ("inputs differ") → neural-net funding collapses.

## Knowledge & logic (1969–1986)
| When | What |
|---|---|
| 1969 | DENDRAL — first successful knowledge-intensive (expert) system. |
| 1970 | 🎯 Rechenberg & Schwefel: evolution strategies. |
| 1972 | 🎯 **Prolog** (Colmerauer & Roussel, Marseille; theory from Kowalski). Slides-01 lists it under 1970. |
| 1975 | 🎯 Holland's GA book (*Adaptation in Natural and Artificial Systems*). 🎯 Backpropagation dated 1975 on slides-01 (R&N: invented in early 1960s, popularised in late 1980s). |
| 1979 | Kowalski: *Algorithm = Logic + Control*. |

## Statistical & bio-inspired era (1986–)
| When | What |
|---|---|
| 1986 | 🎯 Term "deep learning"; return of neural networks (backprop). |
| 1987 | 🎯 Judea Pearl: causal calculus / Bayesian networks (DAGs) — probabilistic reasoning era. |
| 1995 | 🎯 **SVM** (Vapnik, AT&T Bell Labs). 🎯 **PSO** (Kennedy & Eberhart). |
| 1996 | 🎯 **Ant System / ACO** (Dorigo, Maniezzo, Colorni). |
| 2000s | 🎯 Deep learning foundations: Bengio, Hinton, LeCun (Turing Award 2019). Big data (2001–). |
| 2007 | 🎯 **Artificial Bee Colony** (Karaboga). |
| 2011– | Deep learning revolution (R&N). |
| 2020s | 🎯 Generative AI, LLMs, agents (slides-01 s.2). |

## Turing Award shortcut (R&N §1.3)
Minsky (1969) & McCarthy (1971) — foundations/representation; Newell & Simon (1975) — symbolic problem solving; Feigenbaum & Reddy (1994) — expert systems; Pearl (2011) — probabilistic reasoning; Bengio, Hinton, LeCun (2019) — deep learning.

Related: [what-is-ai](what-is-ai.md) · [evolutionary-computation](evolutionary-computation.md) · [prolog](prolog.md)
