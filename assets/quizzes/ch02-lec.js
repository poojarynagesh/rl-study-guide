// Chapter 2 — questions from the professor's lectures (Aug 10–19).
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
