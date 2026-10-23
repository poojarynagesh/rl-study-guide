// Chapter 6 exam-style questions: interpreting TD updates, batch results and learning curves.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`Driving home: leaving the office you predict 30 min to go; 5 minutes later, at the car, you predict 35 more (total 40). With α = 1, by how many minutes does TD(0) change the office state's estimate of time-to-go?`, answer: 10, tol: 0.001,
      explain: R`Target $=R+V(\text{car})=5+35=40$; change $=40-30=+10$ — immediately, without waiting to get home. MC would wait and move it to the actual 43 (+13).` },
    { tag: "exam", type: "mcq", q: R`5-state random walk, all $V=0.5$, TD(0) with $\alpha=0.1$. The first episode is C → B → A → left exit (reward 0). Which values change?`,
      options: ["A, B and C", R`Only $V(A)$, to 0.45`, "Only C", "None"], answer: 1,
      explain: R`Intermediate TD errors are $0+0.5-0.5=0$; only the last step gives $\delta=0+0-0.5$, so $V(A)=0.45$ (Exercise 6.3).` },
    { tag: "exam", type: "num", q: R`Batch data: episode 1 is $A\xrightarrow{0}B\xrightarrow{1}$ end; episodes 2 and 3 are $B\xrightarrow{0}$ end. What does batch TD(0) give for $V(A)$? (3 decimals)`, answer: 0.333, tol: 0.002,
      explain: R`$V(B)=(1+0+0)/3=1/3$; A always goes to B with reward 0, so certainty equivalence gives $V(A)=1/3$. Batch MC gives $V(A)=1$ (the one return observed from A).` },
    { tag: "exam", type: "num", q: R`Expected Sarsa target with ε-greedy (ε = 0.1, 3 actions), $R=0$, $\gamma=1$, $Q(S',\cdot)=(1,2,4)$. Compute the target (3 decimals).`, answer: 3.833, tol: 0.002,
      explain: R`Greedy action 3 has probability $0.9+0.1/3=0.9333$; others $0.0333$ each. Target $=0.0333(1)+0.0333(2)+0.9333(4)=3.833$. Q-learning's target would be 4.` },
    { tag: "exam", type: "mcq", q: "Cliff walking learning curves: Sarsa averages about −25 per episode, Q-learning about −50. Yet Q-learning's greedy path is 13 steps and Sarsa's 17. Which statement is correct?",
      options: ["Sarsa learned the optimal policy", "Q-learning learned the optimal (edge) policy; its online reward is worse only because ε-greedy exploration sometimes walks it off the cliff", "Q-learning diverged", "Both are equally optimal"], answer: 1,
      explain: "Online reward measures the behaviour (ε-greedy) policy, not the learned greedy policy." },
    { tag: "exam", type: "mcq", q: "Windy gridworld: after 8000 steps, Sarsa's episodes average about 17 steps although the shortest path is 15. Why?",
      options: ["Sarsa has not learned anything", "ε-greedy exploration (ε = 0.1) keeps taking occasional non-greedy actions", "The wind is stochastic", "α is too small"], answer: 1,
      explain: "The greedy policy is (near) optimal; continued exploration costs a couple of steps per episode." },
    { tag: "exam", type: "tf", q: R`If ten actions all have true value 0 but noisy estimates, then $\E[\max_aQ(s,a)]\gt0$.`, answer: true,
      explain: "That positive bias is maximization bias; Double Q-learning removes it by selecting with one estimate and evaluating with another." },
  );
})();
