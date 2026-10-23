// Chapter 4 exam-style questions: when to stop, how to recognise optimality, reading sweeps.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`Value iteration with threshold $\theta=0.01$. The largest change in each sweep was:
      <div class="tw"><table><tr><th>sweep</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><th>$\Delta=\max_s|v_{k+1}(s)-v_k(s)|$</th><td>0.80</td><td>0.31</td><td>0.09</td><td>0.008</td><td>0.0006</td></tr></table></div>
      After which sweep does the algorithm stop?`, answer: 4, tol: 0,
      explain: R`The loop runs "until $\Delta\lt\theta$": sweep 4 is the first with $\Delta=0.008\lt0.01$. Sweep 5 is never computed. A greedy policy is then extracted from $V$.` },
    { tag: "exam", type: "mcq", q: "Policy iteration: you evaluate π₃ and then run the improvement step. In every state the greedy action equals π₃'s action (policy-stable = true). What can you conclude?",
      options: ["Run more evaluation sweeps to be sure", R`π₃ is optimal: $v_{\pi_3}$ satisfies the Bellman optimality equation, so stop and return $V\approx v_*$, $\pi\approx\pi_*$`, "π₃ is only better than π₂", "Switch to value iteration"], answer: 1,
      explain: R`If greedification changes nothing, $v_\pi(s)=\max_a\sum p[r+\gamma v_\pi(s')]$ for all $s$ — the Bellman optimality equation — so π is optimal.` },
    { tag: "exam", type: "mcq", q: R`Current deterministic policy π picks $a_1$ in state $s$ (γ = 1, deterministic moves):
      <div class="tw"><table><tr><th>action</th><th>reward</th><th>$v_\pi$(next state)</th></tr><tr><td>$a_1$ (π's choice)</td><td>−1</td><td>−3</td></tr><tr><td>$a_2$</td><td>−1</td><td>−2</td></tr></table></div>
      Is π optimal?`,
      options: [R`Yes, because $v_\pi(s)=-4$ is finite`, R`No: $q_\pi(s,a_2)=-3\gt v_\pi(s)=-4$, so switching to $a_2$ in $s$ strictly improves π (policy improvement theorem)`, "Cannot tell without more sweeps", "Yes, ties are broken arbitrarily"], answer: 1,
      explain: R`$v_\pi(s)=q_\pi(s,a_1)=-1-3=-4$ and $q_\pi(s,a_2)=-1-2=-3$. A strict improvement exists, so π is not optimal.` },
    { tag: "exam", type: "num", q: R`One value-iteration update for state $s$, $\gamma=0.9$:
      <div class="tw"><table><tr><th>action</th><th>outcome</th><th>reward</th><th>$V(s')$</th></tr><tr><td>$a_1$</td><td>to $s_1$ w.p. 1</td><td>0</td><td>10</td></tr><tr><td>$a_2$</td><td>to $s_2$ w.p. 0.5</td><td>2</td><td>4</td></tr><tr><td></td><td>to $s_3$ w.p. 0.5</td><td>2</td><td>8</td></tr></table></div>
      What is the new $V(s)$?`, answer: 9, tol: 0.001,
      explain: R`$q(a_1)=0+0.9\cdot10=9$; $q(a_2)=2+0.9(0.5\cdot4+0.5\cdot8)=7.4$. $V(s)=\max=9$ (greedy action $a_1$, despite its smaller immediate reward).` },
    { tag: "exam", type: "mcq", q: "Policy iteration never terminates: in some state two actions have exactly equal value and the improvement step keeps switching between them. What is the right fix?",
      options: ["Decrease θ", R`Only change π(s) if the old action is not among the maximising actions (or break ties in a fixed order)`, "Use two arrays", "Increase γ"], answer: 1,
      explain: "This is the subtle bug of Exercise 4.4: equally good policies alternate, so policy-stable is never true." },
    { tag: "exam", type: "mcq", q: "In Figure 4.1 the greedy policy w.r.t. vₖ is already optimal at k = 3, although vₖ is still far from v_π. What does this justify?",
      options: ["Running policy evaluation to full convergence", "Truncating policy evaluation — e.g. value iteration, a single sweep before improvement", "Ignoring the discount factor", "Using Monte Carlo instead"], answer: 1,
      explain: "Exact values aren't needed for improvement, only the right greedy action." },
    { tag: "exam", type: "tf", q: R`Stopping value iteration when $\Delta\lt\theta$ means the output policy is only <em>approximately</em> optimal ($\pi\approx\pi_*$), because $V$ only approximates $v_*$.`, answer: true,
      explain: R`VI converges to $v_*$ only in the limit; the algorithm box outputs "π ≈ π*". In practice the greedy policy is usually optimal well before $V$ converges.` },
    { tag: "exam", type: "tf", q: "In asynchronous value iteration, if some state is never updated after a certain point, convergence to v* is still guaranteed.", answer: false,
      explain: "Any order is allowed, but every state must keep being updated (infinitely often in the limit)." },
  );
})();
