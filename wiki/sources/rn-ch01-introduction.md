---
title: "R&N Chapter 1 — Introduction"
type: source
unit: intro
raw: "raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf"
sources: [rn-ch01-introduction]
updated: 2026-09-30
---

# Russell & Norvig, *AIMA* 4th ed. (Global), Chapter 1 — Introduction

Raw: `raw/Russell, S. J. (2022). Artificial intelligence. Pearson.pdf` — since 2026-09-30 the **full book** (1167 PDF pages; PDF page ≈ book page + 2). Ingested so far: Ch 1–9 (up to what the slides cover). Text dump: `extracted/Russell, S. J. (2022)...txt`.

## Key content
- **§1.1 Four approaches** (human vs rational × thinking vs acting) → [what-is-ai](../concepts/what-is-ai.md):
  - *Acting humanly* — Turing test (1950). Needs NLP, knowledge representation, automated reasoning, machine learning; the **total** Turing test adds computer vision/speech and robotics. "These six disciplines compose most of AI."
  - *Thinking humanly* — cognitive modelling (introspection, psychological experiments, brain imaging); GPS (Newell & Simon); cognitive science.
  - *Thinking rationally* — "laws of thought", Aristotle's syllogisms, the logicist tradition; limited because knowledge is rarely certain → probability.
  - *Acting rationally* — **rational agent** approach: act to achieve the best (expected) outcome. Prevails because it is more general than laws-of-thought and mathematically well-defined. → the **standard model**.
- **§1.1.5 Beneficial machines** — the standard model assumes a fully specified objective; the **value alignment problem**; King Midas; we want machines that are *provably beneficial* and uncertain about our objectives.
- **§1.2 Foundations** — philosophy, mathematics, economics, neuroscience, psychology, computer engineering, control theory, linguistics (not summarised in detail here).
- **§1.3 History** — Turing-award summary; McCulloch & Pitts 1943; Hebb 1949; SNARC 1950; Dartmouth 1956 (10 attendees; first use of the term "artificial intelligence"); Logic Theorist; GPS & physical symbol system hypothesis; Samuel's checkers; McCarthy's Lisp (1958) and Advice Taker; Robinson's resolution (1965); microworlds/blocks world; perceptrons; "a dose of reality" (1966–73: combinatorial explosion, Lighthill report, Minsky & Papert 1969); expert systems (DENDRAL); return of neural nets (1986–); probabilistic reasoning & ML (1987–); big data (2001–); deep learning (2011–). → [history-of-ai](../concepts/history-of-ai.md)
- **§1.4–1.5** State of the art; risks and benefits (not detailed in this wiki yet).

## Notes
- Footnote: AI ≠ machine learning; ML is the subfield that improves from experience.
- Backpropagation had been developed in other contexts in the early **1960s** (Kelley 1960; Bryson 1962) — compare slides-01's "1975" date (see [discrepancies](../discrepancies.md)).
