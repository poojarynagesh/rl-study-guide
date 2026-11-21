// Chapter 6 — questions from the professor's lectures (Sep 30 – Oct 14).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "num", q: R`Random walk, TD(0), $\alpha=0.1$, $\gamma=1$, all non-terminal values start at 0.5. The first episode is C → B → A → F (all rewards 0). What is $V(A)$ after the episode?`, answer: 0.45, tol: 0.0001,
      explain: R`C and B: $0+0.5-0.5=0$, no change. A: $0.5+0.1(0+0-0.5)=0.45$ — the only change, revealing a left exit.` },
    { tag: "lecture", type: "num", q: R`In the 5-state random walk (γ = 1, +1 only on exiting right), what is the true value of state D? (3 decimals)`, answer: 0.667, tol: 0.002,
      explain: R`Chaining the Bellman equations gives $V(A)=1/6$ and $V(k\text{th state})=k/6$, so $V(D)=4/6$ — the probability of exiting right.` },
    { tag: "lecture", type: "mcq", q: R`The identity $G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k$ holds exactly when…`,
      options: ["…the step size is 1", R`…the value estimates are held fixed during the episode (V does not change between steps)`, R`…$\gamma=1$ only`, "…the policy is greedy"], answer: 1,
      explain: R`The telescoping uses the same $V$ in every $\delta_k$. With online TD updates, $V$ changes after each step and the identity is only approximate.` },
    { tag: "lecture", type: "mcq", q: "On the random walk, α = 0.15 had the lowest RMS error after 25 episodes, while α = 0.03 was poor at 100 episodes. What is the right conclusion?",
      options: ["α = 0.15 is the best step size for this problem", "The best α depends on the episode budget and on which values were tried; a small α may win over a much longer run", "Smaller α is always better", "MC is better than TD"], answer: 1,
      explain: "Large α learns fast but keeps oscillating with the noisy TD error; small α is slow but settles lower. Untested values (0.12, 0.09…) might be better still." },
    { tag: "lecture", type: "mcq", q: R`In Example 6.4 (A→B with 0, then B's rewards are 1 six times and 0 twice), why can batch TD use the six B episodes to value A?`,
      options: ["Because MC is biased", R`Because of the Markov property: from B onward the future does not depend on having come from A, so all visits to B estimate $V(B)$, and $V(A)=0+V(B)=3/4$`, "Because γ < 1", "Because A was visited six times"], answer: 1,
      explain: R`Batch TD solves the empirical Markov model; batch MC uses only A's own return (0).` },
    { tag: "lecture", type: "num", q: R`ε-greedy with ε = 0.1 over 4 actions. What is the probability of choosing the greedy action?`, answer: 0.925, tol: 0.0001,
      explain: R`$1-\varepsilon+\varepsilon/4=0.9+0.025=0.925$; each other action gets 0.025.` },
    { tag: "lecture", type: "num", q: R`At the next state, $Q=(4,\,6,\,3)$ and the policy is ε-greedy with ε = 0.1. What value does Expected Sarsa put in its target in place of $Q(S_{t+1},A_{t+1})$? (2 decimals)`, answer: 5.83, tol: 0.01,
      explain: R`π = (1/30, 14/15, 1/30): $4/30+6\cdot14/15+3/30=35/6\approx5.83$. Q-learning would use 6.` },
    { tag: "lecture", type: "mcq", q: "Why does cliff walking give −1 per ordinary step instead of +1?",
      options: ["To make γ irrelevant", "A positive per-step reward would pay the agent to wander in cycles instead of finishing; a living cost makes the shortest safe completion optimal", "Because rewards must be negative in RL", "To make Sarsa and Q-learning identical"], answer: 1,
      explain: "With −1 per step the undiscounted return is −(number of steps), so shorter is better. With +1 per step the agent would never want to stop." },
    { tag: "lecture", type: "mcq", q: "During ε-greedy training on the cliff, which statement matches the lecture?",
      options: ["Q-learning has the higher average training return", "Sarsa learns a longer, safer route and has the higher (less negative) training return; Q-learning learns the 13-step edge route but falls more while exploring", "Both learn the same route", "Sarsa learns the edge route"], answer: 1,
      explain: "Q-learning's target ignores its own exploratory slips; Sarsa's target includes them. Once exploration stops, Q-learning's edge route is the optimal one." },
    { tag: "lecture", type: "num", q: R`In the maximization-bias MDP, with ε = 0.1 and two actions in A, what is the lowest achievable fraction of "left" choices once right is greedy?`, answer: 0.05, tol: 0.0001,
      explain: R`Left is chosen only through exploration: $\varepsilon/2=0.05$. That 5% floor is what the curves converge to.` },
    { tag: "lecture", type: "mcq", q: R`Double Q-learning at state A: $Q_1(\text{left},\text{right})=(-3.5,\,0)$, $Q_2=(2.6,\,0)$, ε = 0.1. Which action is greedy for the behaviour policy, and with what probability is it taken?`,
      options: ["Left, 0.95", "Right, 0.95", "Left, 0.9", "Right, 1.0"], answer: 1,
      explain: R`Behaviour uses $Q_1+Q_2=(-0.9,\,0)$, so right is greedy: $0.9+0.1/2=0.95$; left gets $\varepsilon/2=0.05$.` },
    { tag: "lecture", type: "num", q: R`B's reward is $\mathcal N(-0.1,1)$. What fraction of individual rewards from B are positive? (2 decimals)`, answer: 0.46, tol: 0.01,
      explain: R`$P(R\gt0)=1-\Phi(0.1)\approx0.46$. Nearly half the samples look better than right's 0, which is what fools the max early on.` }
  );
})();
