"""Build the printable formula sheet (RL_Formula_Sheet.pdf).

Reads the formula rows from formulas.html (so the web page and the PDF never
disagree), adds a "When to use" note from USES below, writes print/formula_sheet.html
and renders it to RL_Formula_Sheet.pdf with headless Chrome (KaTeX is bundled offline).

Run:  python tools/make_formula_pdf.py
Every formula row must have a USES entry (matched by chapter + start of the row name);
the script stops and lists any that are missing.
"""
import html as H
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]

TITLES = {
    "general": "General", "ch2": "Chapter 2 — Bandits", "ch3": "Chapter 3 — Finite MDPs",
    "ch4": "Chapter 4 — Dynamic programming", "ch5": "Chapter 5 — Monte Carlo", "ch6": "Chapter 6 — TD learning",
    "ch7": "Chapter 7 — n-step bootstrapping", "ch9": "Chapter 9 — Function approximation",
    "ch13": "Chapter 13 — Policy gradient", "ch16": "§16.5 — Deep Q-network (DQN)",
}

# (row-name prefix, when to use)  -- per chapter
USES = {
    "general": [
        ("Incremental rule", "Any running estimate: bandits, MC, TD, function approximation. Move the estimate a fraction of the way to a target."),
        ("Step-size conditions", "Check convergence of a step-size schedule. 1/n passes; a constant α fails the 2nd condition (so it tracks change but never settles)."),
        ("Return", "Define what the agent maximises. Use $G_t=R_{t+1}+\\gamma G_{t+1}$ to compute returns backwards through an episode."),
        ("Unified return", "Write episodic and continuing tasks in one formula ($T=\\infty$ or $\\gamma=1$, never both)."),
    ],
    "ch2": [
        ("Action value", "Definition of an arm's true value; the quantity every bandit method tries to estimate."),
        ("Sample average", "Stationary bandit, estimating $Q(a)$ from observed rewards."),
        ("Greedy", "Action selection. Pure greedy exploits only; use ε-greedy when you must keep exploring."),
        ("Incremental mean", "Compute the average in O(1) memory without storing past rewards."),
        ("Constant α", "Non-stationary problems: recent rewards weigh more (exponential recency-weighted average)."),
        ("Unbiased constant step", "Constant α without the bias from the initial estimate (optional)."),
        ("UCB", "Explore by uncertainty: rarely tried actions get a bonus. Stationary bandits; needs the count $N_t(a)$."),
        ("Soft-max", "Turn action preferences $H$ into probabilities (gradient bandit policy)."),
        ("Gradient bandit", "Learn preferences instead of values; subtract the baseline $\\bar R_t$ to reduce variance. Rewards' absolute scale then does not matter."),
    ],
    "ch3": [
        ("Dynamics", "Defines an MDP; every other quantity is derived from $p$. Use it when the model is known."),
        ("Derived quantities", "Marginalise $p$ to get transition probabilities or expected reward when the algorithm needs only these."),
        ("Constant reward", "Closed-form return of a continuing task with constant reward $r$: $r/(1-\\gamma)$."),
        ("State value", "Definition: expected return from $s$ following π. The target of prediction."),
        ("Action value", "Definition: expected return after taking $a$ in $s$, then following π. Needed for control without a model."),
        ("v ↔ q", "Convert between value types: $v=\\sum\\pi q$; $q=\\sum p[r+\\gamma v]$ (needs the model)."),
        ("Bellman for $v", "Check or solve policy evaluation (a linear system for small MDPs, e.g. gridworlds)."),
        ("Bellman for $q", "Same as above for action values."),
        ("Optimal values", "Definition of $v_*$ and $q_*$: best achievable value over all policies."),
        ("Bellman optimality $v", "Solve for the optimal value function (non-linear because of the max). Basis of value iteration."),
        ("Bellman optimality $q", "Optimal action values; basis of Q-learning (sample version of the max backup)."),
        ("Optimal policy", "Extract the policy: greedy w.r.t. $q_*$ (no model needed), or one-step look-ahead on $v_*$ (model needed)."),
        ("Reward shift", "Effect of adding a constant to all rewards in a continuing task (optional)."),
    ],
    "ch4": [
        ("Policy evaluation", "Model known, evaluate π: sweep all states with the Bellman expectation backup until Δ < θ."),
        ("Deviate once", "Test whether choosing $a\\ne\\pi(s)$ at one state then following π beats π."),
        ("Improvement theorem", "Guarantee: if $q_\\pi(s,\\pi'(s))\\ge v_\\pi(s)$ for all s, then $\\pi'\\ge\\pi$. Justifies greedy improvement."),
        ("Greedy improvement", "Policy-improvement step: take argmax over the one-step look-ahead (needs the model)."),
        ("Value iteration", "Find $v_*$ directly: one sweep of the max backup replaces a full evaluation. Stop when Δ small, then act greedily."),
        ("Q value iteration", "Value iteration on action values (optional)."),
    ],
    "ch5": [
        ("Greedy from q", "Model-free policy improvement in MC control (exploring starts): pick $\\arg\\max_a q(s,a)$."),
        ("ε-greedy improvement", "Improvement within ε-soft policies, no exploring starts (optional)."),
        ("IS ratio", "Off-policy: re-weight a behaviour-policy trajectory by $\\prod\\pi/b$ to evaluate π. Transition probabilities cancel; needs coverage ($\\pi>0\\Rightarrow b>0$)."),
        ("IS expectation", "Why the ratio works: $\\E_b[\\rho G]=v_\\pi(s)$ (change of measure)."),
        ("Ordinary IS", "Unbiased but can have infinite variance. Use when unbiasedness matters."),
        ("Weighted IS", "Biased (bias → 0) but far lower variance: the practical choice. Equals the plain average when ratios are equal."),
        ("Incremental weighted", "Online weighted IS (optional)."),
        ("Per-decision IS", "Variance reduction by weighting each reward only by the ratios up to it (optional)."),
        ("Flat partial return", "Discounting-aware IS (optional)."),
    ],
    "ch6": [
        ("Constant-α MC", "Update toward the full return $G_t$; must wait until the episode ends."),
        ("TD(0)", "Online prediction: update every step toward $R+\\gamma V(S')$ (bootstrapping). Works in continuing tasks."),
        ("TD error", "The surprise $\\delta_t$; appears in every TD method, critics and n-step sums."),
        ("MC error = Σ TD errors", "Relates MC and TD when $V$ is fixed: $G_t-V(S_t)=\\sum\\gamma^{k-t}\\delta_k$."),
        ("Sarsa", "On-policy TD control: target uses the action actually taken next, so it learns the ε-greedy policy's value (safer path in Cliff Walking)."),
        ("Q-learning", "Off-policy TD control: learns $q_*$ whatever the behaviour policy; target uses max. Risky online (cliff) but optimal asymptotically."),
        ("Expected Sarsa", "Averages over next actions: lower variance than Sarsa, same cost as Q-learning; can be on- or off-policy."),
        ("Double Q-learning", "Removes maximisation bias: one table picks the action, the other evaluates it."),
        ("Off-policy TD(0)", "TD with an importance ratio (optional)."),
    ],
    "ch7": [
        ("n-step return", "Bridge between TD ($n=1$) and MC ($n=\\infty$): $n$ real rewards, then bootstrap. If the episode ends first, use $G_t$."),
        ("n-step TD", "Prediction with n-step targets; update $S_t$ only after $n$ steps (delay). Pick intermediate $n$ for best learning."),
        ("Error reduction", "Guarantee that the expected n-step target is $\\gamma^n$-closer to $v_\\pi$ than $V$ is (worst case)."),
        ("n-step Sarsa return", "On-policy control with n-step targets; bootstrap with $Q(S_{t+n},A_{t+n})$."),
        ("n-step Expected Sarsa", "n-step control with an expected last step (optional)."),
        ("Off-policy n-step TD", "Off-policy prediction: scale the update by the ratio $\\rho_{t:t+n-1}$ (importance sampling over the n steps)."),
        ("IS ratio span", "Which steps the ratio covers: $t$ to $\\min(t+n-1,T-1)$ for TD, one more for Sarsa."),
        ("Off-policy n-step Sarsa", "Off-policy control with n-step targets (ratio starts at $t+1$ because $A_t$ is given)."),
        ("Control variate (v)", "Variance reduction for off-policy n-step (optional)."),
        ("Control variate (q)", "Action-value version (optional)."),
        ("Tree backup", "Off-policy n-step without importance sampling (optional)."),
        ("Q(σ)", "Unifies Sarsa, tree backup and Expected Sarsa (optional)."),
    ],
    "ch9": [
        ("Value error", "The objective: mean-square error weighted by how often states are visited, so frequent states matter more."),
        ("On-policy distribution", "Compute $\\mu(s)$ (fraction of time in each state) to weight the error; for episodic tasks from expected visit counts."),
        ("SGD", "Idealised supervised update that needs the true $v_\\pi$ (unavailable): the template for the practical methods below."),
        ("General SGD target", "Replace $v_\\pi$ by any target $U_t$: $G_t$ (gradient MC, unbiased, true SGD) or a bootstrap target (semi-gradient: biased but faster)."),
        ("Linear", "Hand-crafted features: $\\hat v=\\mathbf w^\\top\\mathbf x(s)$, gradient is just $\\mathbf x(s)$; one optimum, convergence guarantees."),
        ("Linear TD(0)", "Online semi-gradient TD with linear features; the workhorse update."),
        ("Expected linear TD update", "Analysis: shows the expected dynamics $\\mathbf b-\\mathbf A\\mathbf w$ and where it settles."),
        ("A and b", "Compute the TD fixed point for a small problem: build $\\mathbf A,\\mathbf b$ from features, rewards and γ."),
        ("TD fixed point", "What linear semi-gradient TD converges to: $\\mathbf w_{TD}=\\mathbf A^{-1}\\mathbf b$ (not the minimum of the value error)."),
        ("Error bound", "Quality of the TD fixed point vs the best linear fit (optional; mentioned only in passing)."),
        ("n-step semi-gradient", "n-step version with function approximation (optional)."),
        ("n-step return (FA)", "n-step target with approximation (optional)."),
        ("Polynomial basis", "Features from products of state components; $(n+1)^k$ features for order $n$ in $k$ variables; always include a constant feature."),
        ("Fourier basis", "Cosine features with integer vectors $\\mathbf c^i$; good for smooth functions; use a smaller step size for high-frequency terms."),
        ("RBF", "Smooth localised features (optional)."),
        ("Step-size rule", "Rule of thumb for linear methods (optional)."),
        ("LSTD", "Data-efficient direct solve of $\\mathbf A^{-1}\\mathbf b$ (optional)."),
        ("Sherman", "Incremental inverse for LSTD (optional)."),
        ("Kernel regression", "Memory-based / kernel methods (optional)."),
        ("Emphatic update", "Emphatic TD with interest weighting (optional)."),
        ("Single hidden layer", "Count weights and write the forward pass of a one-hidden-layer value network ($K(d+1)$ weights, no bias)."),
        ("Activations", "Pick a non-linearity: sigmoid/tanh are smooth but saturate; ReLU is cheap but can die at 0. Needs non-linearity or the net collapses to a linear function."),
        ("TD with a network", "Train a network value function with semi-gradient TD: gradient by backprop."),
        ("Logistic unit", "Worked case: gradient of a single sigmoid unit, $\\hat v(1-\\hat v)\\mathbf x$, for squared error."),
    ],
    "ch13": [
        ("Gradient ascent on", "General recipe: climb the performance $J$; any unbiased sample of the gradient will do."),
        ("Soft-max policy", "Discrete actions: probabilities from action preferences $h(s,a,\\theta)$; can be made nearly deterministic and can learn stochastic policies."),
        ("Performance (episodic)", "The objective: value of the start state under $\\pi_\\theta$."),
        ("Policy gradient theorem", "Gradient of $J$ without differentiating the state distribution — the foundation of every method below."),
        ("Expectation form", "Turns the theorem into something you can sample (states and actions from π)."),
        ("Log-derivative trick", "$\\nabla\\pi=\\pi\\nabla\\ln\\pi$: lets you sample actions from π instead of summing over them."),
        ("REINFORCE", "Monte Carlo policy gradient: wait for the episode end, then update with $G_t\\nabla\\ln\\pi$. Unbiased, high variance, slow."),
        ("Soft-max eligibility vector", "Compute $\\nabla\\ln\\pi$ for a soft-max policy with linear preferences: $\\mathbf x(s,a)-\\sum_b\\pi\\,\\mathbf x(s,b)$."),
        ("Zero-mean score", "Why a baseline is allowed: $\\E_\\pi[\\nabla\\ln\\pi]=0$, so subtracting any $b(s)$ leaves the gradient unchanged."),
        ("Theorem with baseline", "Same gradient with $q_\\pi(s,a)-b(s)$."),
        ("REINFORCE with baseline", "Reduce variance: use $b(s)=\\hat v(s,\\mathbf w)$, learned by gradient MC; update both θ and w."),
        ("Linear critic step", "Rule of thumb for the critic step size with linear features."),
        ("TD error", "One-step critic signal $\\delta=R+\\gamma\\hat v(S')-\\hat v(S)$ (0 for the terminal next state)."),
        ("Actor update", "Actor–critic: replace $G_t$ by δ: online, lower variance, small bias. Use when episodes are long or continuing."),
        ("Critic update", "Semi-gradient TD(0) for $\\hat v$ with a (larger) step size β."),
        ("Two time-scales", "Why critic faster than actor ($\\alpha\\ll\\beta$): the critic sees a nearly fixed policy, so δ is a good signal."),
        ("Average reward", "Continuing tasks (optional)."),
        ("Continuing actor", "Continuing actor–critic (optional)."),
        ("Gaussian policy", "Continuous actions: $a\\sim\\mathcal N(\\mu(s),\\sigma(s)^2)$ with separately parametrised mean and std."),
        ("Mean and std", "Parametrisation: μ linear in features, σ via exp so it stays positive."),
        ("Gaussian scores", "Gradients of $\\ln\\pi$ for the mean ($(a-\\mu)/\\sigma^2$) and std parameters; plug into REINFORCE or actor–critic."),
        ("Sigmoid", "Two-action policy with a sigmoid; score is $(\\mathbb 1_{a}-\\pi)\\mathbf x$ style; the tutorial's worked example."),
        ("Short corridor", "Why policy gradients: with aliased states no ε-greedy value method does well; the best policy is stochastic ($p^*\\approx0.586$)."),
    ],
    "ch16": [
        ("Semi-gradient Q-learning", "Q-learning with function approximation: the starting point; unstable with a deep net on its own."),
        ("Bellman optimality ($Q", "The fixed-point equation the DQN target samples."),
        ("DQN target", "Compute the target: just $r$ at terminal states, else $r+\\gamma\\max_{a'}Q(s',a';\\theta^-)$ using the frozen target network."),
        ("Loss", "Mean squared TD error over a replayed minibatch."),
        ("Gradient (", "Gradient with the target treated as a constant ($\\theta^-$ fixed): semi-gradient."),
        ("SGD step on one tuple", "The update rule per sampled tuple; clip the error to $[-1,1]$ for stability."),
        ("Target-network update", "Copy $\\theta^-\\leftarrow\\theta$ every $C$ steps: keeps the target steady (stabilises learning)."),
        ("Reward clipping", "Same learning rate across games with different score scales."),
        ("Uniform replay", "Sample minibatches uniformly from the last $N$ tuples: breaks correlation, reuses data."),
        ("Conv output size", "Check layer shapes (optional)."),
    ],
}

CHOOSER = [
    ("Bandit only (no states)", "ε-greedy, UCB or gradient bandit", "Ch 2"),
    ("Model known, small state space", "Dynamic programming: policy iteration / value iteration", "Ch 4"),
    ("No model, episodic, can wait for the episode to end", "Monte Carlo (first/every-visit; off-policy needs importance sampling)", "Ch 5"),
    ("No model, learn online or continuing task", "TD: Sarsa (on-policy), Q-learning (off-policy), Expected Sarsa", "Ch 6"),
    ("Want something between TD and MC", "n-step TD / n-step Sarsa", "Ch 7"),
    ("Huge or continuous state space", "Function approximation: linear + features (poly/Fourier) or a neural net; semi-gradient TD", "Ch 9"),
    ("Q-learning from images with a neural net", "DQN: experience replay + target network", "§16.5"),
    ("Continuous or stochastic actions, parametrised policy", "REINFORCE (+ baseline) → actor–critic", "Ch 13"),
]


def strip(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def parse():
    s = (ROOT / "formulas.html").read_text(encoding="utf-8")
    a = s.index('<h2 id="general">')
    b = s.index("</main>")
    body = s[a:b]
    cut = body.index('<h2 id="not-taught">')
    main, skip = body[:cut], body[cut:]
    row = re.compile(r'<div class="k">(.*?)</div><div>(.*?)</div><div class="r">(.*?)</div>', re.S)
    sections = []
    cur = None
    for tok in re.split(r'(<h[23] id="[^"]+"[^>]*>.*?</h[23]>)', main, flags=re.S):
        m = re.match(r'<h[23] id="([^"]+)"', tok)
        if m:
            cid = "ch9" if m.group(1) == "ch9nn" else m.group(1)
            cur = next((x for x in sections if x[0] == cid), None)
            if cur is None:
                cur = [cid, []]
                sections.append(cur)
        elif cur is not None:
            cur[1] += [(strip(k), f, r.strip()) for k, f, r in row.findall(tok)]
    optional = []
    for det in re.findall(r"<details class=\"fs-skip\">(.*?)</details>", skip, re.S):
        summ = strip(re.search(r"<summary>(.*?)</summary>", det, re.S).group(1))
        m = re.match(r"Chapter (\d+)", summ)
        cid = "ch16" if ("§16.5" in summ.split(" — ")[0] or (m and m.group(1) == "16")) else "ch" + m.group(1)
        optional.append((cid, [(strip(k), f, r.strip()) for k, f, r in row.findall(det)]))
    return sections, optional


def use_for(cid, name, missing):
    hits = [(len(prefix), text) for prefix, text in USES[cid] if name.startswith(prefix)]
    if hits:
        return max(hits)[1]  # longest matching prefix wins
    missing.append((cid, name))
    return ""


CSS = """
@page { size: A4; margin: 13mm 12mm 14mm 12mm; @bottom-center { content: "RL formula sheet — page " counter(page) " of " counter(pages); font: 8pt sans-serif; color: #777; } }
* { box-sizing: border-box; }
body { font-family: "Segoe UI", Arial, sans-serif; color: #111; font-size: 9.6pt; line-height: 1.32; margin: 0; }
h1 { font-size: 20pt; margin: 0 0 2px; }
.sub { color: #555; font-size: 9.5pt; margin-bottom: 8px; }
h2 { font-size: 12.5pt; margin: 14px 0 4px; padding: 3px 8px; background: #1f3a5f; color: #fff; border-radius: 3px; break-after: avoid; }
h2.opt { background: #666; }
h3 { font-size: 10.5pt; margin: 10px 0 3px; color: #444; break-after: avoid; }
table { width: 100%; border-collapse: collapse; margin-bottom: 4px; }
th { background: #e8edf4; text-align: left; font-size: 8.6pt; padding: 3px 6px; border: 1px solid #b9c3d1; }
td { padding: 4px 6px; border: 1px solid #c9d0db; vertical-align: top; }
tr { break-inside: avoid; }
td.n { width: 15%; font-weight: 600; }
td.f { width: 43%; font-size: 10.2pt; }
td.w { width: 34%; font-size: 8.9pt; color: #222; }
td.r { width: 8%; font-size: 8pt; color: #666; text-align: right; }
.katex { font-size: 1.04em; }
tbody tr:nth-child(even) td { background: #f7f9fc; }
.tip { border: 1px solid #b9c3d1; background: #f4f7fb; padding: 6px 9px; border-radius: 4px; font-size: 9pt; margin: 6px 0; }
.opt td { color: #444; }
"""


def build():
    sections, optional = parse()
    missing = []
    out = []
    out.append("<!doctype html><html lang='en'><head><meta charset='utf-8'><title>RL formula sheet</title>")
    out.append('<link rel="stylesheet" href="../assets/vendor/katex/katex.min.css">')
    out.append(f"<style>{CSS}</style>")
    out.append('<script src="../assets/vendor/katex/katex.min.js"></script><script src="../assets/vendor/katex/auto-render.min.js"></script></head><body>')
    out.append("<h1>Reinforcement Learning — Formula Sheet</h1>")
    out.append("<div class='sub'>E1 277o · Sutton &amp; Barto (2nd ed.) · only formulas taught in the lectures, with <b>when to use</b> each. Formulas not discussed in class are in the grey appendix at the end (optional).</div>")
    out.append("<h2>Which method when?</h2><table><thead><tr><th style='width:34%'>Situation</th><th>Use</th><th style='width:8%'>Where</th></tr></thead><tbody>")
    for a, b, c in CHOOSER:
        out.append(f"<tr><td>{H.escape(a)}</td><td>{H.escape(b)}</td><td>{c}</td></tr>")
    out.append("</tbody></table>")
    out.append("<div class='tip'><b>Notation.</b> $G_t$ return · $\\gamma$ discount · $\\alpha$ step size · $\\delta_t$ TD error · $\\pi$ policy · $b$ behaviour policy · $\\rho$ importance ratio · $\\mathbf w$ value weights · $\\boldsymbol\\theta$ policy weights · $\\mu(s)$ on-policy distribution · $\\theta^-$ DQN target-network weights. Eq. numbers refer to the book (&quot;paper&quot; = Mnih et al.).</div>")

    def table(cid, rows, cls=""):
        o = [f"<table class='{cls}'><thead><tr><th>Name</th><th>Formula</th><th>When to use</th><th>Ref</th></tr></thead><tbody>"]
        for name, f, r in rows:
            o.append(f"<tr><td class='n'>{name}</td><td class='f'>{f}</td><td class='w'>{use_for(cid, name, missing)}</td><td class='r'>{r}</td></tr>")
        o.append("</tbody></table>")
        return "".join(o)

    for cid, rows in sections:
        out.append(f"<h2>{TITLES[cid]}</h2>")
        if cid == "ch9":
            lin = [r for r in rows if not r[0].startswith(("Single hidden", "Activations", "TD with a network", "Logistic"))]
            nn = [r for r in rows if r not in lin]
            out.append(table(cid, lin))
            out.append("<h3>§9.7 Neural-network value functions</h3>")
            out.append(table(cid, nn))
        else:
            out.append(table(cid, rows))
    out.append("<h2 class='opt' style='margin-top:18px;break-before:page'>Appendix — in the book but NOT discussed in class (optional)</h2>")
    for cid, rows in optional:
        out.append(f"<h3>{TITLES[cid]}</h3>")
        out.append(table(cid, rows, "opt"))
    out.append("""<script>
document.addEventListener("DOMContentLoaded", function () {
  renderMathInElement(document.body, { delimiters: [{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}],
    macros: {"\\\\E":"\\\\mathbb{E}","\\\\Pr":"\\\\operatorname{Pr}","\\\\argmax":"\\\\operatorname*{arg\\\\,max}","\\\\argmin":"\\\\operatorname*{arg\\\\,min}","\\\\doteq":"\\\\stackrel{.}{=}","\\\\w":"\\\\mathbf{w}","\\\\x":"\\\\mathbf{x}","\\\\VE":"\\\\overline{\\\\mathrm{VE}}"}, throwOnError: false });
});
</script></body></html>""")
    if missing:
        print("MISSING 'when to use' entries:")
        for m in missing:
            print("  ", m)
        sys.exit(1)
    d = ROOT / "print"
    d.mkdir(exist_ok=True)
    (d / "formula_sheet.html").write_text("".join(out), encoding="utf-8")
    n = sum(len(r) for _, r in sections) + sum(len(r) for _, r in optional)
    print(f"wrote print/formula_sheet.html ({n} formulas)")


def render():
    chrome = next((c for c in CHROME if Path(c).exists()), None)
    if not chrome:
        print("Chrome/Edge not found: open print/formula_sheet.html and print to PDF")
        return
    src = (ROOT / "print" / "formula_sheet.html").resolve().as_uri()
    pdf = ROOT / "RL_Formula_Sheet.pdf"
    subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000", f"--print-to-pdf={pdf}", src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("wrote", pdf, pdf.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    build()
    render()
