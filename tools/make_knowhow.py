"""Assemble knowhow.html (Exam know-how by algorithm) from the fragments in tools/knowhow_parts/.

Fragments: partA.html (bandits, returns, Bellman, policy evaluation, policy iteration, value iteration),
partB.html (MC, off-policy MC/IS, TD(0), SARSA/Expected SARSA/Q-learning, n-step),
partC.html (function approximation, policy gradient, DQN, exam tactics + source index).
Each fragment is a series of <section class="kh" id="kh-..."><h2 id="..."> blocks.

Run:  python tools/make_knowhow.py   then   python tools/build_index.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = ["partA.html", "partB.html", "partC.html"]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Exam know-how by algorithm — RL Study Guide</title>
<link rel="stylesheet" href="assets/vendor/katex/katex.min.css">
<link rel="stylesheet" href="assets/style.css">
<script defer src="assets/vendor/katex/katex.min.js"></script>
<script defer src="assets/vendor/katex/auto-render.min.js"></script>
<script defer src="assets/search-index.js"></script>
<script defer src="assets/site.js"></script>
<style>
  .kh { margin-top: 8px; }
  .kh .asked { margin: 6px 0 10px; display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
  .kh .asked .src { font-size: 13px; font-weight: 650; color: var(--text-3); margin-right: 2px; }
  .kh .box ul, .kh .box ol { margin: 4px 0 2px; }
  .kh details.kh-worked { margin: 12px 0; border: 1px solid var(--border); border-radius: var(--radius); padding: 2px 14px; background: var(--surface); }
  .kh details.kh-worked > summary { cursor: pointer; font-weight: 650; padding: 8px 0; color: var(--text-2); }
  .kh-index { display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0 4px; }
  .kh-index a { text-decoration: none; }
  @media print { .kh details.kh-worked:not([open]) > :not(summary) { display: block; } }
</style>
</head>
<body data-page="knowhow" data-root=".">
<main class="content">

<div class="hero">
  <div class="kicker">Revision · from the sample papers</div>
  <h1>Exam know-how by algorithm</h1>
  <p class="lead">The six sample papers (Final 2025, Tutorials 2 and 3, Midterm 1, Aug 2020, Jan 2021) keep asking the same kinds of questions. For each algorithm this page gives the <strong>facts you must know</strong>, the <strong>exact method</strong>, the <strong>tests and stopping rules</strong> (when to stop value iteration, is this policy optimal?), the <strong>traps</strong>, and what to do when the question changes. Items marked <em>(standard result)</em> come from the textbook, not from the lectures.</p>
  <div class="meta">
    <span class="chip">{n} algorithm topics</span>
    <span class="chip">Patterns from 6 papers</span>
    <span class="chip">Worked micro-examples</span>
  </div>
</div>

<div class="box key">
  <span class="box-title">Jump to an algorithm</span>
  <div class="kh-index">
{index}
  </div>
</div>

"""

TAIL = """
</main>
</body>
</html>
"""


def main():
    body = []
    index = []
    for name in PARTS:
        p = ROOT / "tools" / "knowhow_parts" / name
        if not p.exists():
            raise SystemExit(f"missing fragment {p}")
        text = p.read_text(encoding="utf-8")
        body.append(text.strip())
        for sid, title in re.findall(r'<section class="kh" id="(kh-[^"]+)">\s*<h2[^>]*>(.*?)</h2>', text, re.S):
            t = re.sub(r"<[^>]+>", "", title).strip()
            index.append(f'    <a class="chip" href="#{sid}">{t}</a>')
    ids = re.findall(r'\bid="([^"]+)"', "\n".join(body))
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"duplicate ids across fragments: {sorted(dup)}")
    page = HEAD.replace("{n}", str(len(index))).replace("{index}", "\n".join(index)) + "\n\n".join(body) + "\n" + TAIL
    (ROOT / "knowhow.html").write_text(page, encoding="utf-8")
    print(f"wrote knowhow.html with {len(index)} sections, {len(page)//1024} KB")


if __name__ == "__main__":
    main()
