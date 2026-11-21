# Project plan

## Phase 1 — chapter pages (done)

- [x] Scaffold (layout, nav, KaTeX, charts, search)
- [x] Ch 1 Introduction
- [x] Ch 2 Multi-armed Bandits
- [x] Ch 3 Finite MDPs
- [x] Ch 4 Dynamic Programming
- [x] Ch 5 Monte Carlo Methods
- [x] Ch 6 Temporal-Difference Learning
- [x] Ch 7 n-step Bootstrapping
- [x] Ch 9 Function Approximation — On-policy Prediction with Approximation
- [x] Revision pages: algorithm catalogue, hyperparameters, formula sheet, mixed practice

## Phase 2 — per-chapter quizzes (done)

Add a scored quiz to every chapter to check understanding (beyond the
existing reveal-the-answer self-test): multiple-choice / true-false /
numeric questions, instant feedback with an explanation per question, a
score, retry, and the best score remembered per chapter.

## Phase 3 — publish online (done)

- Push the repo to GitHub (confirm repo name and visibility with the user first).
- Enable GitHub Pages on `main` so `index.html` is reachable at a public URL.
- Check that every page, KaTeX fonts and the search index load correctly from the hosted site.

Phase 2 delivered: assets/quiz.js engine + assets/quizzes/chNN.js banks (98 questions across 8 chapters).

Phase 3 delivered: https://github.com/poojarynagesh/rl-study-guide (public), served by GitHub Pages at https://poojarynagesh.github.io/rl-study-guide/

Follow-up (2026-10-23): 51 exam-style interpretation questions added (assets/quizzes/chNN-exam.js): stopping value iteration from Δ tables, recognising an optimal policy in PI, ε-greedy log analysis, geometric-series returns, IS/batch estimates, reading learning curves. Total quiz bank: 149 questions.

## Phase 4 — professor's lecture content (done 2026-10-26)

Source: `lecture_notes_RL/` (E1 277o class notes, Aug 3 – Oct 21, 21 classes; kept out of
git — see .gitignore). The course follows the same book, so nothing was added as separate
material: the professor's own explanations, examples, numbers and tips were merged into the
matching chapter sections as purple **"From the lectures"** boxes (dated), and lecture-based
questions were added to each chapter quiz with a **"From lectures"** badge.

| Chapter | Classes | Boxes | Quiz questions |
|---|---|---|---|
| 1 | Aug 3, 5 | 5 | 8 |
| 2 | Aug 10, 12, 17, 19 | 6 | 11 |
| 3 | Aug 5, 19, 24, 31, Sep 2, 9 | 6 | 11 |
| 4 | Sep 7, 16 | 4 | 9 |
| 5 | Sep 21, 23, 28 | 5 | 10 |
| 6 | Sep 30, Oct 7, 12, 14 | 7 | 12 |
| 7 | Oct 14, 19, 21 | 4 | 10 |
| 9 | Oct 21 | 1 | 6 |

Total quiz bank now 226 questions (149 + 77).

### Adding notes from a new class

1. Put the new notes file in `lecture_notes_RL/` and read it in full; map each topic to its chapter section.
2. Keep only what is **not already in the book page**: the professor's examples and numbers, derivations done differently, clarifications from student questions, tips and warnings.
3. Add boxes to `tools/lec_chNN.py` (anchor = an existing heading; the helper `tools/lecmerge.py` skips boxes already present, so re-running is safe) and append questions to its quiz string.
4. Run `python tools/lec_chNN.py`, then `python tools/build_index.py` (lecture boxes are indexed for search).
5. Check the chapter page renders without KaTeX errors, then commit and push.

For a chapter not yet on the site (e.g. Chapter 10 or 13 if covered later), create the chapter page in the same style first, then merge its lecture content the same way.

## Phase 5 — later lectures (done 2026-11-21)

Lecture notes 22–27 (Oct 26 – Nov 20) merged into the site, same method as Phase 4:

- Ch 9 gained 11 lecture boxes and 27 questions (function approximation, semi-gradient, TD fixed point, polynomial/Fourier features, neural networks).
- New Ch 13 page (Policy Gradient Methods): 12 lecture boxes, 49 questions.
- New Ch 16 page (§16.5 Deep Q-network, plus DRQN): 10 lecture boxes, 48 questions.

Mapping of classes to chapters:

| Class | Chapter(s) |
|---|---|
| 22–23 | ch9 |
| 24 | ch9 (neural networks) + ch16 |
| 25 | ch16 + ch13 |
| 26–27 | ch13 (27 also DQN problems) |

Revision pages updated for the new chapters: algorithm catalogue (REINFORCE, baseline, actor–critic, DQN, DRQN rows; new `pg` and `deep` filter tags; value-based vs policy-gradient vs actor–critic and tabular Q-learning vs DQN comparisons), formula sheet (Ch 13, §16.5, extra Ch 9 equations), hyperparameters (actor/critic two-time-scale, policy parameterisation, DQN table), mixed practice (Ch 13 / Ch 16 items), roadmap (chapter groups and notation).

The `lecture_notes_RL/` folder stays out of git (see .gitignore), as in Phase 4. The scope note under "Adding notes from a new class" still applies; Chapters 10–12 and 14–15 are not planned.
