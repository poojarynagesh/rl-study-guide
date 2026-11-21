# RL Study Guide — Sutton & Barto, Chapters 1–7, 9, 13 and 16 (§16.5)

An interactive, offline-friendly study website for *Reinforcement Learning: An
Introduction* (Sutton & Barto, 2nd edition, 2020), covering Chapters 1–7, 9 and 13
(policy gradient methods) plus Chapter 16 §16.5 (DQN, with a note on DRQN).
Chapters 8, 10–12 and the rest of 14–17 are out of scope. Built for exam preparation.

Each chapter page has:

- the concepts in the book's section order, with definitions, key ideas,
  exam tips and common mistakes called out
- every algorithm as pseudocode, with its salient features and how it differs
  from related algorithms
- all key formulas (with book equation numbers)
- the hyperparameters involved and what each one controls
- an interactive simulation you can re-run with different settings
- the course professor's own explanations, worked examples and tips, merged into the matching sections as dated "From the lectures" boxes
- self-test questions with model answers
- a scored chapter quiz (multiple choice, true/false, numeric) with instant
  feedback and explanations; best scores show on the home page

Revision pages pull everything together: an algorithm catalogue with
comparison tables, a hyperparameter and step-size page, a one-page formula
sheet and mixed exam practice.

## Using it

Open `index.html` in a browser. No server, build step or internet connection
is needed — KaTeX (math rendering) and the Source Serif 4 / Inter fonts (SIL Open
Font License) are vendored in `assets/vendor`.

Reading aids: text size (A−/A+), focus mode (hides the sidebar), light/dark
theme, reading-progress bar and estimated reading time per chapter.

Progress ("mark chapter as studied") and the theme choice are stored in your
browser's localStorage only.

## Layout

```
index.html, roadmap.html          home page; study path and notation
chapters/chNN.html                one page per chapter
algorithms.html, hyperparameters.html, formulas.html, quiz.html
assets/style.css                  all styles (light + dark tokens)
assets/site.js                    nav, theme, math, backup diagrams, charts, search
assets/search-index.js            generated — do not edit
assets/quiz.js, assets/quizzes/   quiz engine and per-chapter question banks
tools/build_index.py              regenerates the search index
```

After adding or editing a page, run `python tools/build_index.py` so search and
navigation pick it up.

Content is a study aid summarising the textbook; refer to the book itself for
full derivations and proofs.

## Online version

Hosted with GitHub Pages: https://poojarynagesh.github.io/rl-study-guide/

This is an independent study aid; it is not affiliated with or endorsed by the
book's authors. The book itself is freely available from the authors at
http://incompleteideas.net/book/the-book-2nd.html.


**Printable formula sheet:** `RL_Formula_Sheet.pdf` (A4, with a "when to use" note per formula; lecture-taught formulas first, optional appendix). Regenerate after editing `formulas.html` with `python tools/make_formula_pdf.py` (needs Chrome or Edge).

**Exam know-how page:** `knowhow.html` collects the patterns of the sample papers per algorithm (methods, stopping rules, "is it optimal?" tests, traps). Built from `tools/knowhow_parts/` by `python tools/make_knowhow.py`.

**Exam cheat sheet:** `RL_Cheat_Sheet.pdf` is one A4 sheet printed back-to-back (2 pages, 3 columns, taught formulas only, font auto-fitted to fill the page). Print double-sided, flip on the long edge. Regenerate with `python tools/make_cheatsheet.py`.
