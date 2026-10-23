// Chapter 5 exam-style questions: tracing returns and importance-sampling estimates.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`Episode (γ = 1): $A \xrightarrow{r=1} B \xrightarrow{r=2} A \xrightarrow{r=3}$ terminal. What is the <em>every-visit</em> MC estimate of $V(A)$ from this episode?`, answer: 4.5, tol: 0.001,
      explain: R`Returns after the visits to A: first visit $1+2+3=6$, second visit $3$. Every-visit averages them: $4.5$. First-visit uses only $6$.` },
    { tag: "exam", type: "num", q: R`Off-policy: at step 1 the taken action has $\pi=0.9$, $b=0.5$; at step 2 it has $\pi=0.1$, $b=0.5$. What is the importance-sampling ratio for the two steps?`, answer: 0.36, tol: 0.001,
      explain: R`$\rho=\frac{0.9}{0.5}\cdot\frac{0.1}{0.5}=1.8\times0.2=0.36$ — the trajectory is less likely under π than under b.` },
    { tag: "exam", type: "num", q: R`Three returns from state $s$ with their ratios:
      <div class="tw"><table><tr><th>$G$</th><td>5</td><td>3</td><td>−1</td></tr><tr><th>$\rho$</th><td>0</td><td>2</td><td>2</td></tr></table></div>
      What is the <em>weighted</em> importance-sampling estimate of $V(s)$?`, answer: 1, tol: 0.001,
      explain: R`$\frac{0\cdot5+2\cdot3+2\cdot(-1)}{0+2+2}=\frac44=1$. Ordinary IS gives $4/3\approx1.33$. The first return (ρ = 0) is inconsistent with π and is ignored by both.` },
    { tag: "exam", type: "mcq", q: R`Off-policy MC control: in an episode of length $T=20$, the behaviour policy last took a non-greedy action at time $t=16$. During the backward loop, which pairs $(S_t,A_t)$ get updated?`,
      options: ["All 20", R`Only $t=19,18,17,16$ — the loop exits after updating $t=16$, where $A_t\ne\pi(S_t)$`, R`Only $t=0$`, "None"], answer: 1,
      explain: "It learns only from the tail of the episode after the last non-greedy action — the main weakness of off-policy MC control." },
    { tag: "exam", type: "mcq", q: "Ten runs of ordinary-importance-sampling MC on a one-state problem are still jumping between 0.5 and 3 after a million episodes, while the true value is 1. The most likely explanation:",
      options: ["The step size is too large", "The scaled returns have infinite variance (loops make ρ grow like 2ᵏ), so the estimates never settle", "A bug in the simulator", "Weighted IS would be worse"], answer: 1,
      explain: "Example 5.5. Weighted IS would give exactly 1 after the first episode consistent with π." },
    { tag: "exam", type: "mcq", q: "In the MC estimate of the blackjack value function, values with player sum 20–21 are high but drop for the column where the dealer shows an ace. Why?",
      options: ["Too few episodes", "The policy sticks on 20–21 and usually wins; an ace is the dealer's strongest showing card", "Aces are counted as 1", "First-visit bias"], answer: 1,
      explain: "Exercise 5.1." },
  );
})();
