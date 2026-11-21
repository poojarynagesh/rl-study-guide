"""One-line-per-equation exam cheat sheet: RL_Cheat_Sheet_OneLine.pdf (A4, back-to-back).

Left block: every equation on ONE line (name : formula), rows too wide are shrunk, never wrapped.
Right block: a tips sidebar (when to use, targets, stopping/optimality tests, traps, recipes).
Each block auto-fits its own font size. Reuses rows/boxes from make_cheatsheet.py.
Run:  python tools/make_cheatsheet_1line.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import make_cheatsheet as cs  # noqa: E402
fp = cs.fp

CSS = cs.CSS + """
.pg { column-count: 1; display: flex; gap: 2.2mm; overflow: hidden; font-size: 8pt; }
.main { flex: 0 0 136mm; min-height: 0; overflow: hidden; }
.side { flex: 1 1 0; min-width: 0; min-height: 0; overflow: hidden; border-left: 0.25mm solid #000; padding-left: 2mm; line-height: 1.2; }
.r { white-space: nowrap; padding: 0.5mm 0; }
.r .nm::after { content: " :"; font-weight: 400; }
.side h4 { margin: 1.3mm 0 0.5mm; font-size: 1.02em; background: #000; color: #fff; padding: 0.2mm 1.2mm; break-after: avoid; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.side ul { margin: 0 0 0 3.2mm; padding: 0; }
.side li { margin: 0.2mm 0; }
.side .box { margin: 1mm 0; }
.side table { width: 100%; }
.sheet { padding: 4mm 5mm; }
.bar { display: none; }
.pg { height: 289mm; }
.main, .side { display: flex; flex-direction: column; justify-content: space-between; }
.main > *, .side > * { flex: none; }
body, .r, .side, .box, .r i { color: #000 !important; }
.r { border-bottom-color: #555; }
.katex, .katex * { color: #000; -webkit-text-stroke: 0.28px #000; }   /* thicken thin math strokes */
.r .nm, .side b, .box b { font-weight: 800; }
.box th, .box td { border-color: #444; }
.box th { background: #ccc; }
"""

TIPS = {
 r"General": [r"<b>Incremental rule</b> = the template for every update: new = old + step × (target − old).",
             r"Compute returns <b>backwards</b>: $G_t=R_{t+1}+\gamma G_{t+1}$."],
 r"Ch 2 Bandits": [r"Greedy arm also gets $\varepsilon/k$ ⇒ $\Pr=1-\varepsilon+\varepsilon/k$.", r"UCB: $N=0$ ⇒ pick that arm first.",
                  r"Constant $\alpha$ ⇒ non-stationary (tracks); $1/n$ ⇒ sample average.", r"Gradient bandit: all arms updated, baseline $\bar R$."],
 r"Ch 3 MDPs": [r"Bellman <u>expectation</u> = linear system; Bellman <u>optimality</u> has max ⇒ non-linear.", r"$q$ from $v$ needs the model; greedy on $q_*$ needs none.",
               r"Reward is on the transition: $r(s,a)=\sum p\,r$."],
 r"Ch 4 DP": [r"Value iteration: update from the <u>old</u> $V$; stop $\Delta\lt\theta$.", r"Deviate-once test ⇒ policy-improvement check.", r"Policy iteration stops when the policy is stable."],
 r"Ch 5 Monte Carlo": [r"IS ratio: $p$ cancels; need $b\gt0$ where $\pi\gt0$.", r"Ordinary IS: unbiased, high variance. Weighted: biased, low variance.", r"Every-visit counts repeats, first-visit does not."],
 r"Ch 6 TD": [r"MC error $=\sum$ TD errors only if $V$ fixed.", r"Sarsa on-policy ($A'$ taken); Q-learning off-policy (max).", r"Expected Sarsa: lower variance; Double Q removes max bias.", r"“Using initial estimates” ⇒ all $\delta$ from the original $V$."],
 r"Ch 7 n-step": [r"n-step return ends at $T$ ⇒ equals $G_t$.", r"Update waits $n$ steps; off-policy ratio for Sarsa starts at $t+1$."],
 r"Ch 9 Function approx.": [r"$\nabla\hat v=\mathbf x$ for linear; $\hat v(\text{terminal})=0$.", r"Bootstrapping target ⇒ <u>semi</u>-gradient.", r"TD fixed point $\ne$ minimiser of $\overline{\mathrm{VE}}$.", r"Network: add non-linearity; tabular = one-hot $X=I$."],
 r"Ch 13 Policy gradient": [r"Take $\ln\pi$ first, then differentiate.", r"Baseline must not depend on the action.", r"Actor–critic: $\delta$ replaces $G_t$; critic step $\beta\gg\alpha$.", r"$\delta=0$ extra term at terminal."],
 r"§16.5 DQN": [r"Terminal tuple: $y=r$, no max.", r"Clip TD error to $[-1,1]$; $\theta^-$ held fixed.", r"Copy $\theta^-\leftarrow\theta$ every $C$ steps."],
}
EXTRA1 = cs.FACTS1
EXTRA2 = cs.FACTS2

FIT_JS = cs.FIT_JS.split("function fit()")[0] + """
  function rowfit(main) {
    var worst = 1;
    main.querySelectorAll(".r").forEach(function (e) {
      e.style.zoom = 1;
      var w = main.clientWidth, s = e.scrollWidth;
      if (s > w) { var z = w / s; e.style.zoom = z; if (z < worst) worst = z; }
    });
    return worst;
  }
  function fitMain(pg, main) {
    var fs = 11, z = 1;
    while (fs > 5) {
      main.style.fontSize = fs + "pt"; z = rowfit(main);
      if (main.scrollHeight <= main.clientHeight + 1 && z >= 0.85) break;
      fs -= 0.2;
    }
    return fs;
  }
  function fitSide(side) {
    var sf = 11;
    while (sf > 5) {
      side.style.fontSize = sf + "pt";
      if (side.scrollHeight <= side.clientHeight + 1) break;
      sf -= 0.2;
    }
    return sf;
  }
  function fit() {
    var out = [];
    document.querySelectorAll(".pg").forEach(function (pg) {
      var main = pg.querySelector(".main"), side = pg.querySelector(".side");
      var total = pg.clientWidth / 3.7795 - 2.2, best = null;
      [118, 126, 134, 142, 150].forEach(function (mw) {
        main.style.flexBasis = mw + "mm";
        var m = fitMain(pg, main), sf = fitSide(side);
        var score = m + 0.4 * sf - (sf < 7.5 ? 100 : 0);
        if (!best || score > best.score) best = { mw: mw, m: m, sf: sf, score: score };
      });
      main.style.flexBasis = best.mw + "mm";
      var m = fitMain(pg, main), sf = fitSide(side);
      main.style.fontSize = (m - 0.2) + "pt"; var z = rowfit(main);
      side.style.fontSize = (sf - 0.2) + "pt";
      out.push("w" + best.mw + "/m" + m.toFixed(1) + "/z" + z.toFixed(2) + "/s" + sf.toFixed(1));
    });
    document.title = "FIT " + out.join(" ");
  }
  (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(function () { fit(); });
});
"""


def build():
    sections, _ = fp.parse()
    byid = {cid: rows for cid, rows in sections}

    def page(ids, extra, label):
        main, side = [], []
        for cid in ids:
            t = cs.TITLES[cid]
            main.append(f"<h3>{t}</h3>")
            main += [cs.row(cid, n, f).replace(re.search(r" <i>.*</i></div>$", cs.row(cid, n, f)).group(0), "</div>") if "<i>" in cs.row(cid, n, f) else cs.row(cid, n, f) for n, f, r in byid[cid]]
            key = {"Ch 9 Function approximation": "Ch 9 Function approx."}.get(t, t)
            side.append(f"<h4>{t}</h4><ul>" + "".join(f"<li>{x}</li>" for x in TIPS[key]) + "</ul>")
        side.append(extra)
        return (f"<div class='sheet'><div class='bar'><span>RL formula cheat sheet (one line per equation) · E1 277o · Sutton &amp; Barto</span>"
                f"<span>{label}</span></div><div class='pg'><div class='main'>{''.join(main)}</div><div class='side'>{''.join(side)}</div></div></div>")

    doc = ("<!doctype html><html lang='en'><head><meta charset='utf-8'><title>RL cheat sheet one-line</title>"
           '<link rel="stylesheet" href="../assets/vendor/katex/katex.min.css">'
           f"<style>{CSS}</style>"
           '<script src="../assets/vendor/katex/katex.min.js"></script><script src="../assets/vendor/katex/auto-render.min.js"></script>'
           f"<script>{FIT_JS}</script></head><body>"
           + page(["general", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7"], EXTRA1, "side 1 of 2: bandits → n-step")
           + page(["ch9", "ch13", "ch16"], EXTRA2, "side 2 of 2: approximation, policy gradient, DQN")
           + "</body></html>")
    (ROOT / "print" / "cheat_sheet_1line.html").write_text(doc, encoding="utf-8")


def render():
    c = cs.chrome()
    src = (ROOT / "print" / "cheat_sheet_1line.html").resolve().as_uri()
    pdf = ROOT / "RL_Cheat_Sheet_OneLine.pdf"
    subprocess.run([c, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=20000", f"--print-to-pdf={pdf}", src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    dom = subprocess.run([c, "--headless", "--disable-gpu", "--virtual-time-budget=20000", "--dump-dom", src], capture_output=True, text=True, encoding="utf-8").stdout
    m = re.search(r"<title>(FIT[^<]*)</title>", dom)
    print("wrote", pdf, pdf.stat().st_size // 1024, "KB;", m.group(1) if m else "no fit info", "; katex errors:", dom.count("katex-error"))


if __name__ == "__main__":
    build()
    render()
