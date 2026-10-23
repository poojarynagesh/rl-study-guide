// Chapter 9 exam-style questions.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`Two states with $\mu=(0.75,\,0.25)$, true values $v_\pi=(1,\,3)$ and approximations $\hat v=(2,\,2)$. Compute $\overline{\mathrm{VE}}$.`, answer: 1, tol: 0.001,
      explain: R`$0.75(1-2)^2+0.25(3-2)^2=0.75+0.25=1$.` },
    { tag: "exam", type: "num", q: R`Tile coding, 10 tilings, $\alpha=1/10$. State $s$ is trained once with target error $U-\hat v(s)=1$. State $s'$ shares 7 of its 10 tiles. By how much does $\hat v(s')$ change?`, answer: 0.7, tol: 0.001,
      explain: R`Each of $s$'s 10 active weights rises by $0.1$; $s'$ sums 7 of them ⇒ $+0.7$ (while $\hat v(s)$ rises by exactly 1 — one-trial learning).` },
    { tag: "exam", type: "num", q: R`Linear semi-gradient TD(0): $\mathbf x(s)=(1,0)$, $\mathbf x(s')=(0,1)$, $\mathbf w=(1,2)$, $R=1$, $\gamma=0.5$, $\alpha=0.1$. What is the new $w_1$?`, answer: 1.1, tol: 0.001,
      explain: R`$\delta=1+0.5\cdot2-1=1$; $w_1\leftarrow1+0.1\cdot1\cdot1=1.1$; $w_2$ is unchanged because $x_2(s)=0$.` },
    { tag: "exam", type: "mcq", q: "With state aggregation on the 1000-state walk, the leftmost group's learned value is clearly above the average true value of its states. Why?",
      options: ["A bug in the aggregation", "VE weights states by μ; within that group, states near 100 are visited more than 3× as often as state 1, pulling the value toward their (higher) true values", "Semi-gradient bias", "The step size is too large"], answer: 1,
      explain: "Gradient MC converges near the μ-weighted optimum — the distribution matters." },
    { tag: "exam", type: "mcq", q: "Learning curves on the same task: after 100 episodes semi-gradient TD has lower error than gradient MC; after 100,000 episodes MC's error is lower. Is this consistent with the theory?",
      options: ["No — TD should always win", "Yes: TD learns faster (lower variance) but converges to the TD fixed point, whose error can be up to 1/(1−γ) times the minimum that MC attains", "No — MC should always win", "Only if γ = 0"], answer: 1,
      explain: "Speed vs asymptotic accuracy — bound (9.14)." },
    { tag: "exam", type: "mcq", q: "A single tiling uses α = 10⁻⁴ while 50 tilings use α = 10⁻⁴/50. What is the reason for the smaller α?",
      options: ["50 tilings need less learning", "To make the initial learning rate the same: with 50 active features each update changes the value 50× as much per unit of α", "To avoid divergence of TD", "Hashing"], answer: 1,
      explain: R`Change in $\hat v(s)$ per update $=\alpha\,\mathbf x^\top\mathbf x\times$error, and $\mathbf x^\top\mathbf x$ = number of tilings.` },
    { tag: "exam", type: "mcq", q: "Why is LSTD awkward to use directly inside a control (GPI) loop?",
      options: ["It needs a step size", "It never forgets: statistics gathered under old policies keep influencing the solution as π changes", "It is O(d) per step", "It only works for nonlinear approximators"], answer: 1,
      explain: "LSTD accumulates A and b over all past data; control needs some forgetting mechanism." },
  );
})();
