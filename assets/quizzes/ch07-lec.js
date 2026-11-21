// Chapter 7 — questions from the professor's lectures (Oct 14, 19, 21).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "num", q: R`With $\gamma=0.9$ and $n=10$, what weight does the bootstrap estimate $V(S_{t+n})$ receive in the n-step target? (3 decimals)`, answer: 0.349, tol: 0.002,
      explain: R`$\gamma^n=0.9^{10}\approx0.349$, versus 0.9 in one-step TD. Early inaccurate estimates influence the target less.` },
    { tag: "lecture", type: "num", q: R`The error-reduction property bounds the expected n-step target error by $\gamma^n$ times the current max error. With $\gamma=0.5$, $n=3$ and current max error 0.4, what is the bound?`, answer: 0.05, tol: 0.0001,
      explain: R`$0.5^3\times0.4=0.125\times0.4=0.05$ (one-step TD would only guarantee $0.5\times0.4=0.2$).` },
    { tag: "lecture", type: "num", q: R`Random walk, all V = 0.5, α = 0.1, γ = 1. Episode C→D→E→G (reward 1 only on E→G). After this episode with <strong>2-step</strong> TD, what is $V(D)$?`, answer: 0.55, tol: 0.0001,
      explain: R`D's 2-step target is $0+1\cdot1=1$ (the episode ends), so $V(D)=0.5+0.1(1-0.5)=0.55$. C's 2-step target $0+0+V(E)=0.5$ leaves $V(C)=0.5$.` },
    { tag: "lecture", type: "tf", q: R`In the same episode, 3-step TD changes $V(C)$, $V(D)$ and $V(E)$, while 1-step TD changes only $V(E)$.`, answer: true,
      explain: "With n steps the terminal reward reaches back n states in one episode — at the price of waiting n transitions before each update." },
    { tag: "lecture", type: "mcq", q: R`At time $t=T-4$ an n-step method with $n=6$ forms its target. What is it?`,
      options: [R`$R_{t+1}+\dots+\gamma^5R_{t+6}+\gamma^6V(S_{t+6})$`, R`The Monte Carlo return $R_{T-3}+\gamma R_{T-2}+\gamma^2R_{T-1}+\gamma^3R_T$ with no bootstrap term`, "The update is skipped", R`$R_{t+1}+\gamma V(S_{t+1})$`], answer: 1,
      explain: R`Only four rewards remain; after termination nothing is added and $V(S_T)=0$.` },
    { tag: "lecture", type: "mcq", q: "After one training episode that reaches the goal, which state-action pairs does 10-step Sarsa update with information about the goal?",
      options: ["Only the last pair before the goal", "The last ten pairs on the path; a pair eleven steps back is not yet affected", "Every pair in the episode", "None — Sarsa waits for convergence"], answer: 1,
      explain: "Each pair's target looks at most n rewards ahead. One-step Sarsa would strengthen only the final pair." },
    { tag: "lecture", type: "tf", q: "Experiments show that increasing n always lowers the prediction error, so n should be as large as possible.", answer: false,
      explain: "On the 19-state walk, intermediate n did best; very large n behaved like Monte Carlo and was worse. n and α interact and must be tuned together." },
    { tag: "lecture", type: "mcq", q: R`A two-timescale scheme updates values with $a_m$ and the horizon n with $b_m$. Which choice gives the required separation?`,
      options: [R`$a_m=1/m$, $b_m=1/m^{2/3}$`, R`$a_m=1/m^{2/3}$, $b_m=1/m$ (so $b_m/a_m=m^{-1/3}\to0$)`, R`$a_m=b_m=1/m$`, R`$a_m=0.1$, $b_m=0.1$`], answer: 1,
      explain: R`The slow recursion (n) must have the smaller step: $b_m/a_m\to0$, while both satisfy $\sum=\infty$, $\sum(\cdot)^2\lt\infty$.` },
    { tag: "lecture", type: "mcq", q: R`In off-policy n-step Sarsa, why does the importance ratio start at $t+1$ ($\rho_{t+1:t+n}$) rather than at $t$?`,
      options: ["To reduce variance arbitrarily", R`Because $Q(S_t,A_t)$ is already conditioned on the first action $A_t$; only the subsequent actions must be corrected`, R`Because $A_t$ is always greedy`, "Because the first reward is ignored"], answer: 1,
      explain: R`For state values the first action is part of what is averaged, so $\rho_{t:t+n-1}$ starts at $t$; for action values it is given.` },
    { tag: "lecture", type: "mcq", q: R`In an off-policy n-step update, the behaviour policy took an action in the window that has $\pi(A_k\mid S_k)=0$. What happens?`,
      options: ["The update uses ρ = 1", R`$\rho=0$, so the increment is zero and the estimate is unchanged`, "The update is reversed", "The ratio is undefined and training stops"], answer: 1,
      explain: "A segment containing an action the target policy never takes is not evidence about the target policy's return." }
  );
})();
