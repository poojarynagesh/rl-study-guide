// Chapter 3 — questions from the professor's lectures (Aug 5 – Sep 9).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "num", q: R`Rewards satisfy $|R_t|\le2$ and $\gamma=0.95$. What upper bound on $|G_t|$ follows from the geometric-series argument?`, answer: 40, tol: 0.001,
      explain: R`$|G_t|\le B/(1-\gamma)=2/0.05=40$.` },
    { tag: "lecture", type: "mcq", q: R`A continuing task with $\gamma=1$: policy P earns 1 at every step, policy Q earns $1,\tfrac12,\tfrac13,\dots$. What goes wrong?`,
      options: ["Q has the larger return", R`Both returns are infinite (the harmonic series diverges), so returns cannot rank the policies although P is clearly better`, "Both returns are finite", "Only P's return is infinite"], answer: 1,
      explain: R`$\sum1=\infty$ and $\sum1/n=\infty$. Discounting with $\gamma\lt1$ makes both finite ($1/(1-\gamma)$ vs something smaller) and restores the ranking.` },
    { tag: "lecture", type: "mcq", q: R`Pole balancing with reward 0 on every step and −1 when the pole falls, and $\gamma=1$. What is the return of an episode?`,
      options: ["The number of steps survived", R`Always $-1$, whatever the policy — so it cannot distinguish good from bad balancing`, R`$-\gamma^{T-1}$`, "Zero"], answer: 1,
      explain: R`Every episode ends in exactly one −1. Adding $\gamma\lt1$ fixes it: $G_0=-\gamma^{T-1}$ rises towards 0 as the fall comes later.` },
    { tag: "lecture", type: "num", q: R`Same failure-only reward but $\gamma=0.9$; the pole falls at step $T=10$. What is $G_0$? (3 decimals)`, answer: -0.387, tol: 0.002,
      explain: R`$G_0=-\gamma^{T-1}=-0.9^9\approx-0.387$, better than falling at step 3 ($-0.81$).` },
    { tag: "lecture", type: "num", q: R`Gridworld, equiprobable policy, $\gamma=0.9$. In corner D, Up leads to a state of value −1.2 and Left to −1.4 (reward 0); Right and Down hit the wall (reward −1, stay in D). Solve the Bellman equation for $v_\pi(D)$. (2 decimals)`, answer: -1.97, tol: 0.02,
      explain: R`$v=-0.5+0.225(-2.6+2v)\Rightarrow0.55v=-1.085\Rightarrow v\approx-1.97$. The two wall moves contribute both a −1 reward and the self-loop term $\gamma v_\pi(D)$.` },
    { tag: "lecture", type: "mcq", q: R`In the gridworld, $v_\pi(A)=8.8$ is below A's reward of 10 while $v_\pi(B)=5.3$ is above B's reward of 5. Why?`,
      options: ["Rounding error in the table", R`A always jumps to A′, whose value is negative (−1.3); B jumps to B′, whose value is positive (0.4)`, "B is visited more often", R`$\gamma$ is applied only to A`], answer: 1,
      explain: R`$v(A)=10+0.9(-1.3)=8.83$; $v(B)=5+0.9(0.4)=5.36$. A state's value adds the discounted value of where it leads.` },
    { tag: "lecture", type: "mcq", q: "Why does the optimal gridworld value table contain no negative numbers, unlike the equiprobable one?",
      options: ["Because γ changes to 1", "Because the optimal policy never chooses wall-bumping moves (−1); it only takes value-maximising actions", "Because negative rewards are removed from the problem", "Because optimal values are always positive in any MDP"], answer: 1,
      explain: "The random policy hits walls with probability 1/4 near edges. The optimal policy avoids those penalties and heads towards A and B, so every state's optimal value is non-negative here (not a general law)." },
    { tag: "lecture", type: "num", q: "How many deterministic policies does an MDP with 3 states and 4 actions per state have?", answer: 64, tol: 0,
      explain: R`$m^n=4^3=64$.` },
    { tag: "lecture", type: "num", q: R`Recycling robot as in class: from <em>low</em>, <em>search</em> stays low with probability $\beta=0.6$ and reward $r_{\text{search}}=2$; otherwise the battery dies (penalty −5). What is $r(\text{low},\text{search})$?`, answer: -0.8, tol: 0.001,
      explain: R`$0.6\cdot2+0.4\cdot(-5)=1.2-2=-0.8$. Searching on a low battery is a losing bet in expectation here.` },
    { tag: "lecture", type: "tf", q: R`An MDP can have several different optimal policies, but its optimal value function $v_*$ is unique.`, answer: true,
      explain: R`$v_*(s)=\max_\pi v_\pi(s)$ is a single number per state; policies that tie between equally good actions all attain it.` },
    { tag: "lecture", type: "mcq", q: "If the state evolution is NOT Markov (the next state depends on earlier states too), what must the policy depend on?",
      options: ["Only the current state, as usual", "The history of past states and actions (or an enlarged state that summarises it)", "Only the reward", "Nothing — a random policy is optimal"], answer: 1,
      explain: "Without the Markov property the current state is not a sufficient statistic, so history must be tracked, as stressed in the Aug 5 lecture." }
  );
})();
