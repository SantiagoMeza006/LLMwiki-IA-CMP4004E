# Wiki Log

Append-only. Each entry starts with `## [YYYY-MM-DD] <op> | <title>`. Last 5: `grep "^## \[" wiki/log.md | tail -5`.

## [2026-09-29] schema | Wiki bootstrapped from Karpathy's llm-wiki gist
- Downloaded the gist to `llm-wiki.md`; wrote `CLAUDE.md` schema (English wiki, Spanish chat, plain markdown links, no Obsidian; study extras: practice questions, worked exercises, comparison tables).
- Added `tools/extract_sources.py` → `extracted/*.txt` (pptx via python-pptx, pdf via pdftotext).

## [2026-09-29] ingest | Initial batch — 9 sources
- Sources: slides 01, 02, 03, 04, XX (Prolog); R&N 4th ed. excerpt (Ch 1–3, 117 pp.; ingested as 3 chapter pages); Holland 1992; Dorigo et al. 1996; my A* vs Dijkstra note.
- Read image-only slides where they carried content (heuristic properties, PSO/ACO/ABC formulas, minimax/alpha–beta figures, backtracking pseudocode).
- Created 76 pages: 11 source, 22 concept, 17 algorithm, 6 comparison, 10 exercise, 6 practice, plus overview, discrepancies, index, log.
- All numeric traces (UCS/A*/greedy/BFS/DFS on Romania, 8-puzzle h1/h2, b*, GA generation, ACO probabilities, PSO step, minimax/alpha–beta) verified by running code.
- Flagged 16 discrepancies (notably: slides-01 credits Prolog to Dennis Ritchie; ACO ρ = evaporation vs persistence; "best-first" naming; A* completeness wording; my note's km vs miles).
- Gaps: R&N Ch 4 (local search: hill climbing, simulated annealing), Ch 5 (CSPs), Ch 6 (games), Ch 7–9 (logic) are not in `raw/` — games/CSP/logic pages rely on slides. Adding those chapters would let me deepen those pages.

## [2026-09-30] ingest | R&N full book, Chapters 3.6-9 (up to the slides)
- Raw PDF replaced by the full book (1167 pp.). Ingested what the slides cover: rest of Ch 3 (3.6.2-3.6.6), Ch 4, 5, 6, 7, 8, 9 (stopped before Ch 10).
- New pages (28): sources rn-ch04 ... rn-ch09; concepts local-search, nondeterministic-and-partially-observable-search, knowledge-based-agents, propositional-logic, first-order-logic, first-order-inference; algorithms hill-climbing, simulated-annealing, ac-3, min-conflicts, heuristic-alpha-beta, monte-carlo-tree-search, expectiminimax, resolution, dpll-and-walksat; comparisons local-search, game-algorithms, inference-methods; exercises csp-traces, games-traces, logic-inference-traces, local-search-traces.
- Updated ~20 pages: heuristics (relaxed problems, pattern DBs, landmarks), genetic-algorithms (R&N view, 8-queens GA), CSP concept (rewritten from Ch 5), backtracking (forward-checking table, backjumping), minimax/alpha-beta/adversarial-search, chaining, unification (UNIFY), Horn clauses, prolog (Prolog vs FOL, tabling, CLP), sld-resolution, exploration-vs-exploitation, overview (new unit map), slide source pages (removed "not in excerpt" notes).
- Verified in code: R&N 8-queens fitness values, a hill-climbing run ending at h = 1, SA acceptance probabilities, UCB1 values of Fig 6.10, wumpus model checking (3 of 128 models), PL-FC-ENTAILS order, forward-checking domains (Fig 5.7), min-conflicts counts.
- Discrepancies: row 4 updated (R&N's own summary matches the slide on A*); added rows 17-20 (SA ΔE sign, FOL vs Prolog variable case, provenance note, mutation encodings).
- Practice: +44 questions (now 136 total). Lint: 104 pages, 0 problems.
- Not ingested: R&N Ch 10+ (knowledge representation, planning, probability, learning). Ingest when the course reaches them.
