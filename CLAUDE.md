# AI Course Wiki — Schema

This folder is an **LLM-maintained study wiki** for my university Artificial Intelligence course
(USFQ, instructor Daniel Riofrío), built on the pattern in [llm-wiki.md](llm-wiki.md) (Karpathy's gist).
I curate sources and ask questions; you (the LLM) write and maintain every page in `wiki/`.
I talk to you in Spanish; **the wiki itself is written in English.** Reply to me in Spanish.

## Layers

| Path | Owner | Rule |
|---|---|---|
| `raw/` | me | Source documents (slides, papers, textbook excerpts, my homework). **Immutable — never edit, rename or delete.** |
| `extracted/` | tool | Plain-text dumps of `raw/`, produced by `python tools/extract_sources.py`. Derived; safe to regenerate. Grep these instead of re-parsing PDFs. |
| `wiki/` | you | All knowledge pages. You create, update, cross-link and keep them consistent. |
| `tools/` | shared | Small helper scripts. |
| `CLAUDE.md` | both | This schema. Propose edits when a convention stops working; we co-evolve it. |

## Wiki layout

```
wiki/
  index.md            catalog of every page (read this FIRST when answering anything)
  log.md              append-only timeline of ingests, queries, lint passes
  overview.md         course map: units, how topics connect, what to study for exams
  discrepancies.md    errors / contradictions found between sources (exam traps)
  sources/            one summary page per raw source
  concepts/           ideas & definitions (rationality, heuristics, Horn clauses, ...)
  algorithms/         one page per algorithm (BFS, A*, minimax, GA, ACO, ...)
  comparisons/        side-by-side tables (search algorithms, agent types, bio-inspired methods)
  exercises/          worked, step-by-step traces (A* on Romania, alpha-beta, one GA generation, ...)
  practice/           exam-style questions per unit, answers hidden in <details>
```

## Page conventions

- **File names:** lowercase-kebab-case, `.md`. One topic per page.
- **Frontmatter** on every page (except index/log):
  ```yaml
  ---
  title: A* Search
  type: algorithm        # source | concept | algorithm | comparison | exercise | practice | overview
  unit: search           # intro | agents | search | games-csp | optimization | logic
  sources: [slides-02-problem-solving, rn-ch03-search]
  updated: 2026-09-29
  ---
  ```
- **Links:** standard relative markdown links, e.g. `[A*](../algorithms/a-star-search.md)`. No `[[wikilinks]]` (I don't use Obsidian).
- **Citations:** every non-trivial claim cites where it came from, inline, e.g.
  `(slides-02 s.14)`, `(R&N §3.5.2)`, `(Dorigo 1996 §III)`, `(Holland 1992)`. Link the source page the first time on a page.
- **Standard sections for algorithm pages:** Idea → Pseudocode / formula → Properties (complete? optimal? time? space?) → Worked example link → Common mistakes → Related.
- **Math:** use inline code or LaTeX-style `$...$`; keep formulas copy-pasteable (e.g. `f(n) = g(n) + h(n)`).
- **Flag disagreements.** When sources conflict or a slide is wrong, say so on the page with a `> ⚠️ Discrepancy:` callout AND add a row to `discrepancies.md`. Prefer the textbook (R&N) over slides for definitions, but always tell me what the slide says, because the exam may follow the slides.
- **Exam focus:** mark things the instructor emphasized (appears in slides) with `🎯` so I can skim what is most likely to be tested.
- Keep pages dense and skimmable: short paragraphs, tables, bullet lists. No filler.

## Workflows

### Ingest (I drop a file in `raw/` and say "ingest X")
1. Run `python tools/extract_sources.py`, then read the new `extracted/*.txt` (and look at images/figures if text is missing — slide formulas are often images inside the .pptx).
2. Tell me the 3–6 key takeaways in chat and ask if I want any emphasis before writing.
3. Create `wiki/sources/<slug>.md` (summary, what's covered, where it fits in the course).
4. Update or create every affected concept/algorithm/comparison page (often 5–15 pages). Add new cross-links both ways.
5. Add practice questions / worked exercises for new material.
6. Update `index.md`, `overview.md` if the course map changed, `discrepancies.md` if needed.
7. Append to `log.md`.

### Query (I ask a question)
1. Read `wiki/index.md`, open the relevant pages, then `extracted/` if the wiki lacks detail.
2. Answer in Spanish with citations to wiki pages / sources.
3. If the answer is reusable (a comparison, a derivation, a trace), **offer to file it** as a new wiki page, and do so if I agree. Log the query.

### Quiz me ("quiz me on <unit>")
Pull questions from `practice/` (or generate new ones from the pages), ask them **one at a time**, wait for my answer, grade it, explain, then continue. At the end, append weak spots to the log entry so we can review them later.

### Lint ("lint the wiki")
First run `python tools/lint_wiki.py` (mechanical: broken links/anchors, orphans, pages missing from index, missing frontmatter). Then check semantically for: broken links, orphan pages (no inbound links), pages missing from index, concepts mentioned but lacking a page, stale claims, contradictions between pages, missing citations, units with no practice questions. Fix what is safe; list the rest for me. Log it.

## Log format

Each entry starts with `## [YYYY-MM-DD] <op> | <title>` where op ∈ {ingest, query, quiz, lint, schema}.
`grep "^## \[" wiki/log.md | tail -5` shows the last 5 events.
