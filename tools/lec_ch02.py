"""Merge the professor's Chapter-2 lecture content (Aug 10, 12, 17, 19) into chapters/ch02.html."""
from lecmerge import merge

BOXES = [
    ('<h2 id="action-value">2.2 Action-value methods</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: the casino set-up and a worked $q_*(a)$ <span class="lec-date">Aug 10</span></span>
  <p>A gambler pays up front for tokens; each token buys one pull of any machine's lever; rewards are random and the distributions are built into the machines but unknown. $K$ one-armed bandits are equivalent to one $K$-armed machine. A bandit is the <strong>simplest RL problem</strong>: an action produces a reward but <em>the state never changes</em> — effectively there is only one state.</p>
  <p>If the distributions were known, $q_*(a)=\mathbb E[R_t\mid A_t=a]$ is a plain expectation:</p>
  <div class="table-wrap"><table>
    <tr><th>Arm 1</th><td>10 w.p. 1/3</td><td>100 w.p. 1/3</td><td>110 w.p. 1/3</td><td>$q_*(1)=220/3\approx73.3$</td></tr>
    <tr><th>Arm 2</th><td>10 w.p. 1/2</td><td>300 w.p. 1/4</td><td>400 w.p. 1/4</td><td>$q_*(2)=5+75+100=180$</td></tr>
  </table></div>
  <p>Arm 2 is best, but the agent doesn't know the table — it must <em>play</em> and estimate. With the indicator $\mathbb 1(A_i=a)$:
  $Q_t(a)=\dfrac{\sum_{i\le t}R_i\mathbb 1(A_i=a)}{\sum_{i\le t}\mathbb 1(A_i=a)}$ (taken as 0 if $a$ was never chosen), which tends to $q_*(a)$ by the law of large numbers. The <em>choice</em> of arm is the agent's decision; only the rewards are random.</p>
</div>
'''),
    ('<h2 id="testbed">2.3 The 10-armed testbed</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: how ε should change <span class="lec-date">Aug 12</span></span>
  <p>"Start off with a large value of ε and lower it as time progresses": early estimates are built on few samples and are unreliable, so explore a lot; as estimates improve, exploration is wasted, so <strong>ε should eventually go to zero</strong>. Pure greedy can lock onto an arm that merely got lucky early — it is greedy on the <em>estimates</em>, whereas we want to be greedy on the <em>true</em> values eventually.</p>
</div>
'''),
    ('<h2 id="stepsize">2.5 Tracking a nonstationary problem — constant vs varying step size</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: why incremental, and the noise decomposition <span class="lec-date">Aug 12</span></span>
  <p><strong>Storage.</strong> Recomputing $\frac1n(R_1+\dots+R_n)$ needs every past reward — an ever-growing list and $n$ additions per update. The incremental form $Q\leftarrow Q+\frac1{N_a}(R-Q)$ needs just <strong>two numbers per arm</strong>, $Q(a)$ and $N_a$: increment $N_a$, overwrite $Q(a)$.</p>
  <p><strong>Stochastic approximation view.</strong> Split the random target into its mean and a zero-mean part:
  $$Q_{\text{new}}=Q_{\text{old}}+\alpha\big(\underbrace{\mathbb E[\text{Target}]-Q_{\text{old}}}_{\text{deterministic}}\big)+\alpha\big(\underbrace{\text{Target}-\mathbb E[\text{Target}]}_{\text{zero-mean noise}}\big).$$
  The random algorithm behaves like a deterministic one tracking $\mathbb E[\text{Target}]$; with diminishing steps the noise is averaged out. This is the template for every learning rule in the course.</p>
</div>
'''),
    ('<h3>Exercise 2.4 — general step-size weighting</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: step-size rules and the two kinds of convergence <span class="lec-date">Aug 17</span></span>
  <p><strong>Weights with constant α</strong>: $R_n$ gets $\alpha$, $R_{n-1}$ gets $\alpha(1-\alpha)$, … , $Q_1$ gets $(1-\alpha)^n$ — and these sum to exactly 1 (geometric series). With $\alpha=0.5$: 0.5, 0.25, 0.125, … — α acts as a <em>forgetting factor</em>.</p>
  <div class="table-wrap"><table>
    <tr><th>Step size $\alpha_n$</th><th>$\sum\alpha_n=\infty$?</th><th>$\sum\alpha_n^2\lt\infty$?</th><th>Robbins–Monro?</th></tr>
    <tr><td>$1/n$</td><td>yes</td><td>yes ($\pi^2/6$)</td><td>✓</td></tr>
    <tr><td>$1/n^{\beta}$, $\tfrac12\lt\beta\le1$</td><td>yes</td><td>yes</td><td>✓</td></tr>
    <tr><td>$\log(n+1)/(n+1)$</td><td>yes</td><td>yes</td><td>✓</td></tr>
    <tr><td>$1/\big((n+1)\log(n+1)\big)$</td><td>yes</td><td>yes</td><td>✓</td></tr>
    <tr><td>$1/n^{\beta}$, $\beta\le\tfrac12$</td><td>yes</td><td>no</td><td>✗</td></tr>
    <tr><td>constant $\alpha$</td><td>yes</td><td>no</td><td>✗</td></tr>
  </table></div>
  <ul>
    <li>Under Robbins–Monro (stationary rewards): $Q_n\to q_*$ <strong>almost surely</strong> (with probability 1, along every sample path).</li>
    <li>With a constant step size there is an $\alpha^*\gt0$ such that for every $\alpha\in(0,\alpha^*)$, $Q_n\to q_*$ <strong>in probability</strong>: $\lim_n P(|Q_n-q_*|\gt\epsilon)=0$ — weaker, but enough, and constant α can <em>track</em> a changing $q_*$.</li>
    <li>In practice: stop when the iterates stay inside a small δ-ball, i.e. stop changing appreciably.</li>
  </ul>
  <p class="small"><em>Beyond the syllabus (shown for interest):</em> the proof writes $R_{n+1}=q_*+(R_{n+1}-q_*)$; the accumulated noise $\sum\alpha_i(R_{i+1}-q_*)$ is a martingale whose quadratic variation is finite when $\sum\alpha_n^2\lt\infty$ and rewards have finite variance, so it converges; the remaining recursion is an Euler discretisation of the ODE $\dot Q=q_*-Q$, which is globally stable at $q_*$.</p>
</div>
'''),
    ('<h2 id="gradient">2.8 Gradient bandit algorithms</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: where the UCB bonus comes from <span class="lec-date">Aug 17</span></span>
  <p>For independent, zero-mean, 1-sub-Gaussian rewards ($\mathbb E[e^{\lambda X}]\le e^{\lambda^2/2}$; e.g. Gaussian or bounded rewards) the sample mean of $n$ samples obeys $P(Q_n\ge\epsilon)\le e^{-n\epsilon^2/2}$. Setting the right side to δ gives
  $$\epsilon=\sqrt{\frac{2\ln(1/\delta)}{n}}:$$
  with probability at least $1-\delta$ the true mean is below $Q_n(a)+\sqrt{2\ln(1/\delta)/N_a}$ — the <em>largest plausible</em> value of arm $a$. UCB acts optimistically on this bound, replacing $\sqrt2$ by $c$ and letting δ shrink with time, giving $Q_t(a)+c\sqrt{\ln t/N_t(a)}$.</p>
  <ul>
    <li>$N_t(a)=0$ makes the bonus infinite, so <strong>every arm is played at least once</strong> first.</li>
    <li>$\ln t$ grows extremely slowly ($\log_{10}10^8=8$), so the bonus shrinks mainly because $N_t(a)$ grows — exploitation takes over automatically.</li>
  </ul>
</div>
'''),
    ('<h2 id="contextual">2.9 Associative search (contextual bandits)</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: deriving the gradient bandit <span class="lec-date">Aug 17 &amp; 19</span></span>
  <ol>
    <li>Preferences $H_t(a)$ matter only relatively; softmax (Gibbs/Boltzmann) $\pi_t(a)=e^{H_t(a)}/\sum_be^{H_t(b)}$. With $H_0\equiv0$, $\pi_0(a)=1/K$ — uniform.</li>
    <li>Objective $\mathbb E[R_t]=\sum_x\pi_t(x)\,q_*(x)$. Gradient ascent: $H_{t+1}(a)=H_t(a)+\alpha\,\partial\mathbb E[R_t]/\partial H_t(a)$.</li>
    <li>$\partial q_*(x)/\partial H_t(a)=0$: preferences affect <em>which</em> arm is pulled, not what an arm pays once pulled.</li>
    <li><strong>Baseline</strong>: $\sum_xB_t\,\partial\pi_t(x)/\partial H_t(a)=B_t\,\partial(\sum_x\pi_t(x))/\partial H_t(a)=B_t\cdot\partial(1)=0$, so any action-independent $B_t$ can be subtracted without bias; $B_t=\bar R_t$ reduces variance.</li>
    <li>Result: $H_{t+1}(a)=H_t(a)+\alpha(R_t-\bar R_t)\big(\mathbb 1_{A_t=a}-\pi_t(a)\big)$.</li>
  </ol>
  <p>Gradient ascent finds a <strong>local</strong> maximum: $\nabla J(x^*)=0$ is necessary; adding a negative-definite Hessian (locally concave) makes it sufficient. The global maximum is hard in general.</p>
</div>
'''),
]

QUIZ = r'''// Chapter 2 — questions from the professor's lectures (Aug 10–19).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "num", q: R`Arm 2 pays 10 with probability 1/2, 300 with probability 1/4 and 400 with probability 1/4. What is $q_*(2)$?`, answer: 180, tol: 0.01,
      explain: R`$10\cdot\tfrac12+300\cdot\tfrac14+400\cdot\tfrac14=5+75+100=180$ — larger than arm 1's $220/3\approx73.3$, so arm 2 is optimal. The agent can only discover this by sampling.` },
    { tag: "lecture", type: "mcq", q: "With the incremental sample-average update, how much must be stored per arm, however many times it is pulled?",
      options: ["Every reward ever received from that arm", R`Two numbers: the current estimate $Q(a)$ and the count $N_a$`, "Only the last reward", R`The last two estimates $Q_n$ and $Q_{n+1}$`], answer: 1,
      explain: R`Update $N_a\leftarrow N_a+1$, then $Q(a)\leftarrow Q(a)+\frac1{N_a}(R-Q(a))$, overwriting the old $Q$. Storage is constant per arm.` },
    { tag: "lecture", type: "num", q: R`With constant step size $\alpha=0.5$, what weight does the reward three steps back, $R_{n-2}$, receive in $Q_{n+1}$?`, answer: 0.125, tol: 0.0001,
      explain: R`Weight $\alpha(1-\alpha)^{2}=0.5\cdot0.25=0.125$. Weights halve with each step back: 0.5, 0.25, 0.125, …` },
    { tag: "lecture", type: "num", q: R`Constant step size $\alpha=0.1$, after $n=10$ updates. What weight does the initial value $Q_1$ still carry? (3 decimals)`, answer: 0.349, tol: 0.002,
      explain: R`$(1-\alpha)^n=0.9^{10}\approx0.349$. Constant-α estimates are biased by $Q_1$, but the bias decays geometrically.` },
    { tag: "lecture", type: "mcq", q: "Which step-size sequence does NOT satisfy the Robbins–Monro conditions?",
      options: [R`$\alpha_n=1/n$`, R`$\alpha_n=1/n^{0.75}$`, R`$\alpha_n=1/n^{0.4}$`, R`$\alpha_n=\log(n+1)/(n+1)$`], answer: 2,
      explain: R`$\sum1/n^{0.4}=\infty$ is fine, but $\sum\alpha_n^2=\sum1/n^{0.8}=\infty$, so the noise is not averaged out. $1/n^\beta$ works only for $\tfrac12\lt\beta\le1$.` },
    { tag: "lecture", type: "mcq", q: "In a stationary bandit, what convergence does a small constant step size give, according to the lecture?",
      options: ["Almost-sure convergence to the true value", R`Convergence in probability to $q_*$, for all α below some threshold $\alpha^*$`, "No convergence of any kind", "Convergence only if rewards are Gaussian"], answer: 1,
      explain: R`Robbins–Monro step sizes give almost-sure convergence; constant α fails $\sum\alpha^2\lt\infty$ but still gives the weaker convergence in probability (for small enough α), and can track non-stationary values.` },
    { tag: "lecture", type: "mcq", q: R`UCB with $c=1$ at $t=12$: arm 1 has $Q=0.5$, $N=10$; arm 2 has $Q=0.4$, $N=2$ ($\ln12\approx2.48$). Which arm does UCB pick?`,
      options: [R`Arm 1, score $\approx1.00$ vs $0.90$`, R`Arm 2, score $\approx1.51$ vs $1.00$`, "Arm 1, because its estimate is higher", "Either — the scores tie"], answer: 1,
      explain: R`Arm 1: $0.5+\sqrt{2.48/10}=0.5+0.50=1.00$. Arm 2: $0.4+\sqrt{2.48/2}=0.4+1.11=1.51$. The rarely tried arm gets the larger optimism bonus.` },
    { tag: "lecture", type: "num", q: R`For 1-sub-Gaussian rewards, the confidence width is $\epsilon=\sqrt{2\ln(1/\delta)/n}$. With $\delta=0.01$ and $n=100$ samples, what is ε? (2 decimals)`, answer: 0.30, tol: 0.01,
      explain: R`$\ln100=4.605$; $\sqrt{9.21/100}=0.303$. With probability ≥ 0.99 the true mean is at most $Q_n+0.30$.` },
    { tag: "lecture", type: "mcq", q: R`Why can a baseline $B_t$ be subtracted in the gradient-bandit derivation without changing the expected gradient?`,
      options: [R`Because $B_t$ is always zero`, R`Because $\sum_x\partial\pi_t(x)/\partial H_t(a)=\partial(1)/\partial H_t(a)=0$`, R`Because $q_*(x)$ does not depend on $x$`, "Because softmax is linear"], answer: 1,
      explain: R`The probabilities always sum to 1, so their total derivative is 0 and $B_t\sum_x\partial\pi_t(x)/\partial H_t(a)=0$. The baseline only reduces variance.` },
    { tag: "lecture", type: "num", q: R`Gradient bandit with $K=3$, all $H=0$ (so $\pi=1/3$ each), $\alpha=0.3$, baseline $\bar R=1$. Action 1 is chosen and pays $R=2$. What is the new $H(1)$? (2 decimals)`, answer: 0.2, tol: 0.001,
      explain: R`$H(1)\leftarrow0+0.3\,(2-1)(1-\tfrac13)=0.2$. The unchosen arms move by $0.3\,(1)(0-\tfrac13)=-0.1$ each.` },
    { tag: "lecture", type: "tf", q: R`In the gradient bandit derivation, $\partial q_*(x)/\partial H_t(a)=0$ because the preferences only influence which action is selected, not the reward distribution of an action once selected.`, answer: true,
      explain: R`$q_*(x)=\mathbb E[R\mid A=x]$ is a property of the arm. $H$ enters $\mathbb E[R_t]=\sum_x\pi_t(x)q_*(x)$ only through $\pi_t$.` }
  );
})();
'''

if __name__ == "__main__":
    merge("ch02", BOXES, QUIZ)
