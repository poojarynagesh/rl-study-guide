"""Build the exam cheat sheet: ONE A4 sheet printed back-to-back (2 pages), RL_Cheat_Sheet.pdf.

Formulas come from formulas.html (only the ones taught in class); this file adds short hints
and the 'quick facts' boxes. A script in the page picks the largest font size at which each
page still fits (three columns, no overflow), so the space is used fully.

Run:  python tools/make_cheatsheet.py     (needs Chrome or Edge)
"""
import html as H
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import make_formula_pdf as fp  # noqa: E402  (reuses the row parser)

# short hints, matched by chapter + longest prefix of the row name; rows without a hint show none
HINT = {
    "general": [("Incremental rule", "any running estimate"), ("Step-size", "1/n ok; const α tracks"), ("Return", "compute backwards"), ("Unified", "T=∞ or γ=1")],
    "ch2": [("Action value", "target of estimation"), ("Sample average", "stationary"), ("Greedy", "greedy arm also gets ε/k"), ("Incremental mean", "O(1) memory"), ("Constant α", "non-stationary"), ("UCB", "N=0 ⇒ pick first"), ("Soft-max", "from preferences H"), ("Gradient bandit", "baseline R̄; all arms updated")],
    "ch3": [("Dynamics", "defines the MDP"), ("Derived", "marginalise p"), ("Constant reward", "r/(1−γ)"), ("State value", ""), ("Action value", ""), ("v ↔ q", "needs model for q"), ("Bellman for $v", "linear system"), ("Bellman for $q", ""), ("Optimal values", ""), ("Bellman optimality $v", "max ⇒ non-linear"), ("Bellman optimality $q", "basis of Q-learning"), ("Optimal policy", "greedy on $q_*$: no model")],
    "ch4": [("Policy evaluation", "sweep until Δ<θ"), ("Deviate once", "test one-step change"), ("Improvement theorem", "⇒ π′ ≥ π"), ("Greedy improvement", "needs model"), ("Value iteration", "OLD V on right; stop Δ<θ ⇒ err ≤ γθ/(1−γ)")],
    "ch5": [("Greedy from q", "ES control"), ("IS ratio", "p cancels; need b>0 where π>0"), ("IS expectation", ""), ("Ordinary IS", "unbiased, high var"), ("Weighted IS", "biased, low var")],
    "ch6": [("Constant-α MC", "waits for episode end"), ("TD(0)", "online, bootstrap"), ("TD error", ""), ("MC error", "if V fixed"), ("Sarsa", "on-policy: A′ taken"), ("Q-learning", "off-policy: max"), ("Expected Sarsa", "lower variance"), ("Double Q-learning", "removes max bias")],
    "ch7": [("n-step return", "ends at T ⇒ G_t"), ("n-step TD", "update waits n steps"), ("Error reduction", ""), ("n-step Sarsa return", ""), ("Off-policy n-step TD", ""), ("IS ratio span", ""), ("Off-policy n-step Sarsa", "ratio starts t+1")],
    "ch9": [("Value error", "weighted by μ"), ("On-policy distribution", ""), ("SGD", "needs true $v_\\pi$"), ("General SGD target", "bootstrap ⇒ semi-gradient"), ("Linear", "∇v̂ = x"), ("Linear TD(0)", "v̂(terminal)=0"), ("Expected linear", ""), ("A and b", ""), ("TD fixed point", "not min of VE"), ("Polynomial", "include const feature"), ("Fourier", ""), ("Single hidden", "weights, no bias"), ("Activations", "need non-linearity"), ("TD with a network", ""), ("Logistic", "")],
    "ch13": [("Gradient ascent", ""), ("Soft-max policy", "discrete actions"), ("Performance", ""), ("Policy gradient theorem", "no ∇μ"), ("Expectation form", ""), ("Log-derivative", ""), ("REINFORCE", "MC: wait for episode end"), ("Soft-max eligibility", ""), ("Zero-mean", "self-check"), ("Theorem with baseline", ""), ("REINFORCE with baseline", "b = v̂(s,w)"), ("Linear critic", ""), ("TD error", "0 at terminal"), ("Actor update", "δ replaces G_t"), ("Critic update", "β ≫ α"), ("Two time-scales", ""), ("Gaussian policy", ""), ("Mean and std", "σ>0 via exp"), ("Gaussian scores", "log first, then ∇"), ("Sigmoid", ""), ("Short corridor", "stochastic optimum")],
    "ch16": [("Semi-gradient Q", ""), ("Bellman optimality", ""), ("DQN target", "y=r at terminal"), ("Loss", ""), ("Gradient", "θ⁻ held fixed"), ("SGD step", "clip error [−1,1]"), ("Target-network", "every C steps"), ("Reward clipping", ""), ("Uniform replay", "breaks correlation")],
}
TITLES = {"general": "General", "ch2": "Ch 2 Bandits", "ch3": "Ch 3 MDPs", "ch4": "Ch 4 DP", "ch5": "Ch 5 Monte Carlo", "ch6": "Ch 6 TD", "ch7": "Ch 7 n-step",
          "ch9": "Ch 9 Function approximation", "ch13": "Ch 13 Policy gradient", "ch16": "§16.5 DQN"}

FACTS1 = """
<div class="box"><b>Targets at a glance</b>
<table><tr><th></th><th>target for the update</th><th>boot</th></tr>
<tr><td>MC</td><td>$G_t$ (starts at $R_{t+1}$)</td><td>no</td></tr>
<tr><td>TD(0)</td><td>$R+\\gamma V(S')$</td><td>yes</td></tr>
<tr><td>Sarsa</td><td>$R+\\gamma Q(S',A')$ — $A'$ from the episode</td><td>on</td></tr>
<tr><td>Exp. Sarsa</td><td>$R+\\gamma\\sum_b\\pi(b|S')Q(S',b)$</td><td>on/off</td></tr>
<tr><td>Q-learning</td><td>$R+\\gamma\\max_bQ(S',b)$</td><td>off</td></tr>
<tr><td>DP</td><td>$\\E_\\pi[R+\\gamma V(S')]$ (needs model)</td><td>—</td></tr></table>
Terminal next state ⇒ target is just $R$. Sarsa = Q-learning if $A'$ is greedy.</div>
<div class="box"><b>Stop / optimal?</b> VI: update from the <u>old</u> $V_k$ (synchronous); stop when $\\Delta=\\max_s|V_{k+1}-V_k|\\lt\\theta$ ⇒ $\\|V-V_*\\|\\le\\gamma\\theta/(1-\\gamma)$. PI stops when the policy is stable. $\\pi$ optimal ⇔ $v_\\pi$ satisfies Bellman optimality ⇔ improvement changes nothing. Greedy w.r.t. $V_k$ ($k$ finite) is <u>not</u> guaranteed optimal. $\\gamma=1$ needs absorbing goals.</div>
<div class="box"><b>Traps</b> ε-greedy: greedy arm has $1-\\varepsilon+\\varepsilon/k$ · UCB: untried arm first · first- vs every-visit: repeats count only in every-visit · ordinary IS can exceed every observed return · "using the initial estimates" ⇒ all δ from the original $V$ (offline) · constant α never converges, tracks · reward is on the transition: $r(s,a)=\\sum p\\,r$.</div>
"""
FACTS2 = """
<div class="box"><b>Linear semi-gradient TD(0) — recipe</b> ① $\\hat v(s)=\\mathbf w^\\top\\mathbf x(s)$ ② $\\delta=r+\\gamma\\mathbf w^\\top\\mathbf x(s')-\\mathbf w^\\top\\mathbf x(s)$ (next term 0 if terminal) ③ $\\mathbf w\\leftarrow\\mathbf w+\\alpha\\delta\\,\\mathbf x(s)$ ④ in time order, use the updated $\\mathbf w$. $d$ = number of columns of the feature matrix $X$ (rows = states); full column rank ⇒ non-redundant features. Tabular = one-hot $X=I$.</div>
<div class="box"><b>Score function ∇ln π</b> take $\\ln\\pi$ first, differentiate term by term. Check: $\\E_{a\\sim\\pi}[\\nabla\\ln\\pi]=0$ and the gradient has the shape of $\\mathbf x$. Gaussian: $\\nabla_{\\theta_\\mu}=\\frac{a-\\mu}{\\sigma^2}\\mathbf x_\\mu$, $\\nabla_{\\theta_\\sigma}=\\big[\\frac{(a-\\mu)^2}{\\sigma^2}-1\\big]\\mathbf x_\\sigma$. Bernoulli: $\\nabla\\ln\\pi(1)=(1-\\pi_1)\\mathbf x$. Baseline $b(s)$ must not depend on the action.</div>
<div class="box"><b>REINFORCE vs actor–critic</b> REINFORCE: unbiased, high variance, waits for episode end. Actor–critic: $\\delta$ replaces $G_t$ — online, lower variance, biased; critic step β ≫ actor step α (critic must track the current policy).</div>
<div class="box"><b>DQN</b> replay ⇒ decorrelated, reused data; frozen $\\theta^-$ ⇒ stable target (moving target + bootstrapping + off-policy + deep net = unstable). Terminal tuple: $y=r$, no max term. Larger $C$ ⇒ steadier but staler target.</div>
<div class="box"><b>Exam routine</b> state the update rule first · tabulate $(s,a,r,s',a')$ · keep a running table (cross out, rewrite) · write target → δ → α·δ → new value · say your terminal/γ assumptions · check: probabilities sum to 1, Bellman residual 0.</div>
"""

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: "Segoe UI", Arial, sans-serif; color: #000; }
.sheet { width: 210mm; height: 297mm; padding: 5.5mm 6mm 5mm 6mm; page-break-after: always; overflow: hidden; position: relative; }
.sheet:last-child { page-break-after: auto; }
.bar { height: 5mm; font-size: 8pt; font-weight: 700; display: flex; justify-content: space-between; border-bottom: 0.35mm solid #000; margin-bottom: 1.5mm; }
.pg { height: calc(297mm - 5.5mm - 5mm - 6.5mm); column-count: 3; column-gap: 3.2mm; column-rule: 0.2mm solid #999; column-fill: auto; overflow: hidden; line-height: 1.22; font-size: 7.4pt; }
h3 { margin: 1.2mm 0 0.6mm; font-size: 1.12em; background: #000; color: #fff; padding: 0.3mm 1.4mm; break-after: avoid; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.r { break-inside: avoid; padding: 0.35mm 0; border-bottom: 0.1mm dotted #888; }
.r b { font-weight: 700; }
.r i { color: #444; font-size: 0.88em; }
.r .nm { font-weight: 700; margin-right: 1mm; }
.katex { font-size: 1em; }
.box { break-inside: avoid; border: 0.25mm solid #000; padding: 0.8mm 1.4mm; margin: 1.2mm 0; }
.box table { width: 100%; border-collapse: collapse; margin: 0.4mm 0; }
.box th, .box td { border: 0.1mm solid #999; padding: 0.1mm 0.8mm; text-align: left; font-size: 0.95em; }
.box th { background: #ddd; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
"""

FIT_JS = """
document.addEventListener("DOMContentLoaded", function () {
  renderMathInElement(document.body, { delimiters: [{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}],
    macros: {"\\\\E":"\\\\mathbb{E}","\\\\Pr":"\\\\operatorname{Pr}","\\\\argmax":"\\\\operatorname*{arg\\\\,max}","\\\\argmin":"\\\\operatorname*{arg\\\\,min}","\\\\doteq":"\\\\stackrel{.}{=}","\\\\w":"\\\\mathbf{w}","\\\\x":"\\\\mathbf{x}","\\\\VE":"\\\\overline{\\\\mathrm{VE}}"}, throwOnError: false });
  function fit() {
    var sizes = [];
    document.querySelectorAll(".pg").forEach(function (pg) {
      var fs = 10.5, step = 0.05;
      while (fs > 5) {
        pg.style.fontSize = fs + "pt";
        var r = pg.getBoundingClientRect(), over = false;
        pg.querySelectorAll(":scope > *").forEach(function (c) { if (c.getBoundingClientRect().left >= r.right - 2) over = true; });
        var last = pg.lastElementChild.getBoundingClientRect();
        if (last.bottom > r.bottom + 1 || last.left >= r.right - 2) over = true;
        if (!over && pg.scrollWidth <= pg.clientWidth + 1) break;
        fs -= step;
      }
      pg.style.fontSize = (fs - 0.15) + "pt";   // small safety margin for print layout
      sizes.push(fs.toFixed(2));
    });
    document.title = "FIT " + sizes.join(" ");
  }
  (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(function () { fit(); setTimeout(fit, 1500); setTimeout(fit, 3500); });
});
"""


def hint_for(cid, name):
    hits = [(len(p), t) for p, t in HINT.get(cid, []) if name.startswith(p)]
    return max(hits)[1] if hits else ""


def short_name(n):
    return n.replace("Logistic unit $\hat v=\sigma(\mathbf w^\top\mathbf x)$", "Logistic unit").replace("Semi-gradient Q-learning (network)", "Semi-gradient Q-learning")


def compact(f):
    f = f.replace("\\dfrac", "\\frac").replace("\\Big", "\\big").replace("\\Bigg", "\\big")
    return f


def row(cid, name, f):
    h = hint_for(cid, name)
    nm = H.escape(short_name(name)) if short_name(name) else H.escape(name)
    return f"<div class='r'><span class='nm'>{nm}</span>{compact(f)}" + (f" <i>— {H.escape(h)}</i>" if h else "") + "</div>"


def build():
    sections, _ = fp.parse()
    byid = {cid: rows for cid, rows in sections}
    p1 = ["general", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7"]
    p2 = ["ch9", "ch13", "ch16"]

    def page(ids, facts, label):
        out = []
        for cid in ids:
            out.append(f"<h3>{TITLES[cid]}</h3>")
            out += [row(cid, n, f) for n, f, r in byid[cid]]
        out.append(facts)
        return f"<div class='sheet'><div class='bar'><span>RL formula cheat sheet · E1 277o · Sutton &amp; Barto</span><span>{label}</span></div><div class='pg'>{''.join(out)}</div></div>"

    doc = ("<!doctype html><html lang='en'><head><meta charset='utf-8'><title>RL cheat sheet</title>"
           '<link rel="stylesheet" href="../assets/vendor/katex/katex.min.css">'
           f"<style>{CSS}</style>"
           '<script src="../assets/vendor/katex/katex.min.js"></script><script src="../assets/vendor/katex/auto-render.min.js"></script>'
           f"<script>{FIT_JS}</script></head><body>"
           + page(p1, FACTS1, "side 1 of 2: bandits → n-step") + page(p2, FACTS2, "side 2 of 2: approximation, policy gradient, DQN")
           + "</body></html>")
    d = ROOT / "print"
    d.mkdir(exist_ok=True)
    (d / "cheat_sheet.html").write_text(doc, encoding="utf-8")
    print("wrote print/cheat_sheet.html")


def chrome():
    return next((c for c in fp.CHROME if Path(c).exists()), None)


def render():
    c = chrome()
    src = (ROOT / "print" / "cheat_sheet.html").resolve().as_uri()
    pdf = ROOT / "RL_Cheat_Sheet.pdf"
    subprocess.run([c, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=20000", f"--print-to-pdf={pdf}", src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    dom = subprocess.run([c, "--headless", "--disable-gpu", "--virtual-time-budget=20000", "--dump-dom", src], capture_output=True, text=True, encoding="utf-8").stdout
    m = re.search(r"<title>(FIT[^<]*)</title>", dom)
    print("wrote", pdf, pdf.stat().st_size // 1024, "KB;", m.group(1) if m else "no fit info", "; katex errors:", dom.count("katex-error"))


if __name__ == "__main__":
    build()
    render()
