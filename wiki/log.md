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
