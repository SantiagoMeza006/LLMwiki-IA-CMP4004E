"""Mechanical lint for wiki/: broken links, broken #anchors, orphans, pages missing from index.md,
pages missing frontmatter. Semantic checks (contradictions, stale claims) are the LLM's job.

Usage: python tools/lint_wiki.py
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "wiki")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
META = {"index.md", "log.md"}


def slugify(heading):
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def main():
    pages = {}
    for dirpath, _, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".md"):
                p = os.path.normpath(os.path.join(dirpath, f))
                pages[p] = open(p, encoding="utf-8").read()

    anchors = {p: {slugify(h) for h in re.findall(r"^#+\s+(.*)$", t, re.M)} for p, t in pages.items()}
    inbound = {p: 0 for p in pages}
    problems = []

    for p, text in pages.items():
        rel = os.path.relpath(p, ROOT)
        if os.path.basename(p) not in META and not text.startswith("---"):
            problems.append(f"no frontmatter: {rel}")
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, anchor = target.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else p
            if dest not in pages:
                problems.append(f"broken link: {rel} -> {target}")
                continue
            if dest != p:
                inbound[dest] += 1
            if anchor and anchor not in anchors[dest]:
                problems.append(f"broken anchor: {rel} -> {target}")

    index_text = pages.get(os.path.join(ROOT, "index.md"), "")
    for p in pages:
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        if os.path.basename(p) in META:
            continue
        if inbound[p] == 0:
            problems.append(f"orphan (no inbound links): {rel}")
        if f"({rel})" not in index_text:
            problems.append(f"missing from index.md: {rel}")

    print(f"{len(pages)} pages checked")
    for line in sorted(problems):
        print("  " + line)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
