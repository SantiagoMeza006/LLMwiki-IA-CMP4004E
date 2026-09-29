# AI Course Wiki — an LLM-maintained knowledge base

**Santiago Meza · Artificial Intelligence, USFQ (Prof. Daniel Riofrío)**

Class activity: build a retrieval/knowledge system over the course materials. I implemented Andrej Karpathy's **LLM Wiki** pattern ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), copy in [`llm-wiki.md`](llm-wiki.md)) with **Claude Code** as the agent that writes and maintains the wiki. I use it to study for the course.

## Why a wiki instead of classic RAG?
| Classic RAG | LLM Wiki (this repo) |
|---|---|
| Chunks raw documents, retrieves fragments at query time | The LLM **reads each source once** and compiles it into interlinked markdown pages |
| Knowledge re-derived on every question; nothing accumulates | Knowledge **compounds**: summaries, cross-references, contradictions are already there |
| Needs an embedding index / vector DB | At this scale an `index.md` catalog is enough; the agent reads it, then opens the relevant pages |
| Answers vanish into chat history | Good answers are **filed back** as new wiki pages |

Retrieval still happens, but over a curated, human-readable layer, with citations back to the original sources.

## Architecture (three layers)
```
raw/          immutable sources (slides, textbook excerpt, papers, my notes) — copyrighted files not committed
extracted/    plain-text dumps of raw/ for grep (generated, not committed)
wiki/         LLM-written pages — the knowledge base
CLAUDE.md     the schema: structure, conventions and workflows the agent must follow
tools/        extract_sources.py (raw → text), lint_wiki.py (links, orphans, index coverage)
```

`wiki/` contains 76 pages: source summaries, concepts, algorithms, comparison tables, worked exercises (numbers verified by running code), practice questions with hidden answers, a course [overview](wiki/overview.md), an [index](wiki/index.md), a [log](wiki/log.md), and a [discrepancies](wiki/discrepancies.md) page listing 16 places where slides, textbook and papers disagree.

## Operations (defined in `CLAUDE.md`)
- **Ingest:** drop a file in `raw/`, ask the agent to ingest it → summary page, updates to 5–15 related pages, index and log entries.
- **Query:** ask a question → the agent reads `index.md`, then the relevant pages, and answers with citations; reusable answers become new pages.
- **Quiz:** "quiz me on search" → one question at a time, graded, weak spots logged.
- **Lint:** `python tools/lint_wiki.py` + a semantic check for contradictions, stale claims and gaps.

## Reproduce
```bash
pip install python-pptx          # plus poppler's pdftotext on PATH
python tools/extract_sources.py  # after putting the sources listed in raw/SOURCES.md into raw/
python tools/lint_wiki.py
```
Then open the folder with Claude Code (or another agent that reads `CLAUDE.md`/`AGENTS.md`).

## How it was built
- **My part:** chose and collected the sources, chose the design (language, study features, scope of the textbook), directed the ingest, and review and use the pages.
- **Claude Code's part:** wrote the schema, the helper scripts and all wiki pages, following the gist's pattern, where the LLM does the writing and bookkeeping and the human curates and asks questions.
