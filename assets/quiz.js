/* Scored chapter quizzes.
   A page includes its question bank (assets/quizzes/chNN.js, which sets window.RL_QUIZ)
   and a container <div class="cq" id="chapter-quiz"></div>. This file renders the quiz:
   multiple choice ("mcq"), true/false ("tf") and numeric ("num", with tolerance), with
   instant feedback, an explanation per question, a running score, retry with shuffling,
   and the best score remembered per chapter (localStorage key rlsg:quizBest). */
(function () {
  "use strict";

  function shuffle(a, r) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  function mathify(el) {
    if (!window.renderMathInElement) return;
    renderMathInElement(el, {
      delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }],
      macros: { "\\E": "\\mathbb{E}", "\\argmax": "\\operatorname*{arg\\,max}", "\\w": "\\mathbf{w}", "\\x": "\\mathbf{x}", "\\VE": "\\overline{\\mathrm{VE}}" },
      throwOnError: false,
    });
  }

  function init() {
    const box = document.getElementById("chapter-quiz");
    const bank = window.RL_QUIZ;
    if (!box || !bank || !bank.length) return;
    const page = document.body.dataset.page;
    const store = window.RL && RL.store;
    let order = bank.map((_, i) => i);
    let state; // per question: null | {correct}

    function bestText() {
      const best = store ? store.get("quizBest", {})[page] : null;
      return best ? "Best so far: <strong>" + best.score + " / " + best.total + "</strong>" : "Not attempted yet";
    }

    function render() {
      state = order.map(() => null);
      let h = '<div class="cq-head"><div><div class="cq-score" aria-live="polite">Score: <strong>0</strong> / ' + order.length + ' · answered 0</div>' +
        '<div class="cq-best small muted">' + bestText() + '</div></div>' +
        '<button class="btn ghost cq-retry" type="button">Shuffle &amp; restart</button></div>';
      order.forEach((qi, k) => {
        const q = bank[qi];
        h += '<div class="cq-q" data-k="' + k + '"><div class="cq-text"><span class="cq-n">' + (k + 1) + "</span><div>" + q.q + "</div></div>";
        if (q.type === "num") {
          h += '<div class="cq-num"><input type="text" inputmode="decimal" placeholder="Your answer" aria-label="Numeric answer"><button class="btn" type="button">Check</button></div>';
        } else {
          const opts = q.type === "tf" ? ["True", "False"] : q.options;
          h += '<div class="cq-opts">' + opts.map((o, i) => '<button class="cq-opt" type="button" data-i="' + i + '">' + o + "</button>").join("") + "</div>";
        }
        h += '<div class="cq-fb" hidden></div></div>';
      });
      h += '<div class="cq-final" hidden></div>';
      box.innerHTML = h;
      mathify(box);
      box.querySelector(".cq-retry").addEventListener("click", () => { order = shuffle(order.slice(), Math.random); render(); });
      box.querySelectorAll(".cq-q").forEach((el) => wire(el));
    }

    function wire(el) {
      const k = +el.dataset.k, q = bank[order[k]];
      const answer = (correct, detail) => {
        if (state[k]) return;
        state[k] = { correct };
        el.classList.add(correct ? "ok" : "bad");
        const fb = el.querySelector(".cq-fb");
        fb.hidden = false;
        fb.innerHTML = '<strong class="' + (correct ? "yes" : "no") + '">' + (correct ? "Correct." : "Not quite.") + "</strong> " + (detail || "") + " " + q.explain;
        mathify(fb);
        update();
      };
      if (q.type === "num") {
        const input = el.querySelector("input"), btn = el.querySelector("button");
        const go = () => {
          const v = parseFloat(input.value.replace(",", "."));
          if (isNaN(v)) { input.focus(); return; }
          const ok = Math.abs(v - q.answer) <= (q.tol != null ? q.tol : 1e-6);
          input.disabled = true; btn.disabled = true;
          answer(ok, ok ? "" : "Expected <strong>" + q.answer + "</strong>.");
        };
        btn.addEventListener("click", go);
        input.addEventListener("keydown", (e) => { if (e.key === "Enter") go(); });
      } else {
        const right = q.type === "tf" ? (q.answer ? 0 : 1) : q.answer;
        el.querySelectorAll(".cq-opt").forEach((b) => b.addEventListener("click", () => {
          if (state[k]) return;
          const i = +b.dataset.i;
          el.querySelectorAll(".cq-opt").forEach((x) => { x.disabled = true; if (+x.dataset.i === right) x.classList.add("right"); });
          if (i !== right) b.classList.add("wrong");
          answer(i === right);
        }));
      }
    }

    function update() {
      const done = state.filter(Boolean).length, score = state.filter((s) => s && s.correct).length;
      box.querySelector(".cq-score").innerHTML = "Score: <strong>" + score + "</strong> / " + order.length + " · answered " + done;
      if (done === order.length) {
        if (store) {
          const all = store.get("quizBest", {});
          if (!all[page] || score > all[page].score) { all[page] = { score, total: order.length }; store.set("quizBest", all); }
        }
        const pct = score / order.length;
        const fin = box.querySelector(".cq-final");
        fin.hidden = false;
        fin.innerHTML = "<strong>You scored " + score + " / " + order.length + " (" + Math.round(pct * 100) + "%).</strong> " +
          (pct >= 0.9 ? "Excellent — you know this chapter well." : pct >= 0.7 ? "Good. Re-read the sections behind the questions you missed." : "Worth another pass through the chapter, then retry the quiz.");
        box.querySelector(".cq-best").innerHTML = bestText();
      }
    }

    render();
  }

  document.addEventListener("rl:ready", init);
})();
