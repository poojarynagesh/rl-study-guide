// Chapter 7 exam-style questions.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`$n=4$, $\gamma=0.5$. After time $t$ the episode receives $R_{t+1}=1$, $R_{t+2}=2$ and then terminates. What is $G_{t:t+4}$?`, answer: 2, tol: 0.001,
      explain: R`Because $t+n\ge T$, the n-step return is just the full return: $1+0.5\cdot2=2$ — no bootstrap term.` },
    { tag: "exam", type: "mcq", q: "5-state walk, all V = 0.5, first episode C → D → E → right exit (+1). With 2-step TD, which values change after this episode?",
      options: ["Only E", "D and E", "C, D and E", "None"], answer: 1,
      explain: "One-step updates only E; two-step updates the two states before termination; n ≥ 3 updates all three by the same amount (Example 7.1)." },
    { tag: "exam", type: "mcq", q: R`Off-policy 3-step Sarsa with a greedy target π. In the window, $A_{t+1}$ was greedy ($b=0.5$) but $A_{t+2}$ was non-greedy. What happens to the update of $Q(S_t,A_t)$?`,
      options: ["It is doubled", R`$\rho_{t+1:t+3}=0$, so this update is ignored`, R`It uses $\rho=2$`, "It becomes a one-step update"], answer: 1,
      explain: R`$\pi(A_{t+2}|S_{t+2})=0$ makes the whole product zero — the return is irrelevant to π. Tree backup would instead cut the backup off there.` },
    { tag: "exam", type: "num", q: R`2-step tree backup, $\gamma=1$: $R_{t+1}=1$. In $S_{t+1}$ the taken action has $\pi=0.6$; the other action has $\pi=0.4$ and $Q=2$. Then $R_{t+2}=0$ and $\sum_a\pi(a|S_{t+2})Q(S_{t+2},a)=3$. Compute $G_{t:t+2}$.`, answer: 3.6, tol: 0.001,
      explain: R`$G=R_{t+1}+0.4\cdot2+0.6\,(R_{t+2}+3)=1+0.8+1.8=3.6$ — leaves weighted by π, no importance ratios.` },
    { tag: "exam", type: "mcq", q: "In the n-step parameter study, the n = 512 curve only does well at very small α and shoots up for α > 0.1. Interpretation?",
      options: ["n = 512 is buggy", "With such long returns n-step TD is essentially Monte Carlo: high-variance targets need small steps", "Large n always needs larger α", "The walk is too short"], answer: 1,
      explain: "The best α shrinks as n grows; intermediate n with moderate α wins overall." },
  );
})();
