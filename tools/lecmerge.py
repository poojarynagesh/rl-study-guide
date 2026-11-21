"""Helper for merging lecture content into a chapter page.

merge(ch, boxes, quiz) inserts each (anchor, 'before'|'after', html) into
chapters/<ch>.html exactly once (skips boxes already present, so re-running is
safe), writes assets/quizzes/<ch>-lec.js and adds its <script> tag.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def merge(ch, boxes, quiz):
    page = ROOT / "chapters" / f"{ch}.html"
    src = page.read_text(encoding="utf-8")
    added = 0
    for anchor, where, html in boxes:
        title = html.split('<span class="box-title">', 1)[1].split("<", 1)[0]
        if title in src:
            continue
        if src.count(anchor) != 1:
            raise SystemExit(f"{ch}: anchor not unique/found: {anchor!r} ({src.count(anchor)})")
        src = src.replace(anchor, (html + anchor) if where == "before" else (anchor + "\n" + html), 1)
        added += 1
    tag = f'<script defer src="../assets/quizzes/{ch}-lec.js"></script>'
    if tag not in src:
        exam = f'<script defer src="../assets/quizzes/{ch}-exam.js"></script>'
        src = src.replace(exam, exam + "\n" + tag, 1)
    page.write_text(src, encoding="utf-8")
    (ROOT / "assets" / "quizzes" / f"{ch}-lec.js").write_text(quiz, encoding="utf-8")
    print(f"{ch}: added {added} lecture boxes, quiz {ch}-lec.js")
