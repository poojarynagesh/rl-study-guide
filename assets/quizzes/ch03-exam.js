// Chapter 3 exam-style questions: return calculations (geometric series) and Bellman checks.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`From time $t$ the agent receives $+1$ on every step forever, plus a one-time bonus of $+10$ in $R_{t+3}$. With $\gamma=0.9$, what is $G_t$?`, answer: 18.1, tol: 0.01,
      explain: R`Geometric series: $\sum_k\gamma^k=1/(1-0.9)=10$. The bonus arrives $k=2$ steps after $R_{t+1}$, so it adds $10\gamma^2=8.1$. $G_t=18.1$.` },
    { tag: "exam", type: "num", q: R`Rewards alternate $+2,0,+2,0,\dots$ starting with $R_{t+1}=2$, and $\gamma=0.5$. What is $G_t$? (2 decimals)`, answer: 2.67, tol: 0.01,
      explain: R`$G_t=2(1+\gamma^2+\gamma^4+\dots)=\dfrac{2}{1-\gamma^2}=\dfrac{2}{0.75}=2.67$.` },
    { tag: "exam", type: "num", q: R`A maze gives $-1$ per step; the goal is reached after 4 steps (4 rewards of $-1$). With $\gamma=0.9$, what is $G_0$? (3 decimals)`, answer: -3.439, tol: 0.001,
      explain: R`$-(1+0.9+0.81+0.729)=-3.439$. With $\gamma=1$ it would be $-4$ (minus the number of steps).` },
    { tag: "exam", type: "num", q: R`You know $G_t=10$, $R_{t+1}=2$ and $\gamma=0.8$. What is $G_{t+1}$?`, answer: 10, tol: 0.001,
      explain: R`From $G_t=R_{t+1}+\gamma G_{t+1}$: $G_{t+1}=(10-2)/0.8=10$.` },
    { tag: "exam", type: "num", q: R`Bellman check. In state $s$ the policy picks $a_1$ or $a_2$ with probability ½ each; both transitions are deterministic.
      <div class="tw"><table><tr><th>action</th><th>reward</th><th>next state value $v_\pi(s')$</th></tr><tr><td>$a_1$</td><td>1</td><td>4</td></tr><tr><td>$a_2$</td><td>0</td><td>6</td></tr></table></div>
      With $\gamma=0.5$, what must $v_\pi(s)$ be?`, answer: 3, tol: 0.001,
      explain: R`$v_\pi(s)=\tfrac12(1+0.5\cdot4)+\tfrac12(0+0.5\cdot6)=1.5+1.5=3$.` },
    { tag: "exam", type: "mcq", q: R`In some state, $q_*(s,\cdot)=(3,\,5,\,5)$ for actions $a_1,a_2,a_3$. Which statement is correct?`,
      options: [R`$v_*(s)=13/3$ and only $a_2$ is optimal`, R`$v_*(s)=5$, and any policy putting all its probability on $a_2$ and/or $a_3$ is optimal in $s$`, R`$v_*(s)=3$`, "There is no optimal action because of the tie"], answer: 1,
      explain: R`$v_*(s)=\max_aq_*(s,a)=5$; ties give multiple optimal policies (any split between $a_2,a_3$), while $v_*$ is unique.` },
    { tag: "exam", type: "num", q: R`With $\gamma=0.9$, after how many steps $k$ does the discount weight $\gamma^k$ first fall below 0.01 (i.e. rewards matter less than 1%)?`, answer: 44, tol: 0,
      explain: R`$0.9^{43}\approx0.0108$, $0.9^{44}\approx0.0097$. So $k=44$ — compare the rough horizon $1/(1-\gamma)=10$.` },
    { tag: "exam", type: "mcq", q: "Pole balancing is formulated as episodic with reward +1 per step and no discounting. A policy balances the pole forever. What is the return, and what does this suggest?",
      options: ["0 — use a different reward", "Infinite — returns are not well defined, so a discounted (continuing) formulation with −1 on failure is preferable", "1", "Equal to the episode length T"], answer: 1,
      explain: R`Undiscounted +1 forever diverges; the continuing version with $-1$ on failure gives $-\gamma^{K-1}$, which is always finite.` },
  );
})();
