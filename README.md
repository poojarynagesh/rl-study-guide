# RL Study Guide — Sutton & Barto, Chapters 1–9

An interactive, offline-friendly study website for *Reinforcement Learning: An
Introduction* (Sutton & Barto, 2nd edition, 2020), covering Chapters 1–7 and 9
(Chapter 8 is out of scope). Built for exam preparation.

Each chapter page has:

- the concepts in the book's section order, with definitions, key ideas,
  exam tips and common mistakes called out
- every algorithm as pseudocode, with its salient features and how it differs
  from related algorithms
- all key formulas (with book equation numbers)
- the hyperparameters involved and what each one controls
- an interactive simulation you can re-run with different settings
- self-test questions with model answers

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
tools/build_index.py              regenerates the search index
```

After adding or editing a page, run `python tools/build_index.py` so search and
navigation pick it up.

Content is a study aid summarising the textbook; refer to the book itself for
full derivations and proofs.
