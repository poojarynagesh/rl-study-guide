// Chapter 5 — questions from the professor's lectures (Sep 21, 23, 28).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "num", q: R`Two episodes visit states $2,4,2,1,3,4,2$ and $4,1,3,4,2,1,3$. How many returns does <em>every-visit</em> MC average to estimate $V(2)$?`, answer: 4, tol: 0,
      explain: R`State 2 occurs three times in episode 1 (t = 0, 2, 6) and once in episode 2 (t = 4). First-visit MC would use only 2 (one per episode).` },
    { tag: "lecture", type: "mcq", q: "Why are the every-visit returns for the same state within one episode not independent samples?",
      options: ["Because the policy changes between visits", "Because they share most of the same future rewards (overlapping trajectory suffixes)", "Because the Markov property fails", R`Because $\gamma\lt1$`], answer: 1,
      explain: R`$G_0$ and $G_2$ in the same episode contain almost the same rewards, so they are correlated. First-visit returns from independent episodes are independent.` },
    { tag: "lecture", type: "mcq", q: "According to the lecture, when is every-visit MC the more attractive choice?",
      options: ["When episodes are abundant and cheap", "When episodes are scarce or expensive, so that each episode should yield as many samples as possible", "Only for continuing tasks", "Never — first-visit is always better"], answer: 1,
      explain: "With plentiful episodes, first-visit's clean independence is attractive; with scarce data, every-visit extracts more (correlated) information from each episode." },
    { tag: "lecture", type: "mcq", q: R`Evaluating a deterministic policy that always takes $a_1$ in state $s$ by Monte Carlo, why can't the greedy step tell whether $a_2$ is better, and what fixes it?`,
      options: [R`$Q(s,a_2)$ is always 0`, R`$(s,a_2)$ never appears in the data, so $Q_\pi(s,a_2)$ has no samples; exploring starts give every pair a positive probability of starting an episode`, "The model is unknown; learn it first", R`Increase $\gamma$`], answer: 1,
      explain: "Without coverage of other actions, action values cannot be compared. Exploring starts (or a soft/off-policy behaviour) supply those samples." },
    { tag: "lecture", type: "mcq", q: "In the traffic-signal example, logs come from the existing fixed-time controller while we want to evaluate an adaptive RL controller. Which is the behaviour policy?",
      options: ["The adaptive RL controller", "The fixed-time (hard-wired) controller", "Both", "Neither — this is on-policy"], answer: 1,
      explain: R`The data-generating policy is the fixed controller ($b$); the adaptive controller is the target π, never deployed. That is exactly the off-policy setting.` },
    { tag: "lecture", type: "mcq", q: R`In some state, the target policy uses actions $\{a_1,a_4,a_5\}$ and the behaviour policy uses $\{a_1,a_2,a_3,a_4,a_5\}$. Does coverage hold?`,
      options: ["No — b uses actions π never uses", R`Yes — every action with $\pi\gt0$ also has $b\gt0$; extra actions in $b$ are harmless`, "Only if b is greedy", "Cannot tell without rewards"], answer: 1,
      explain: R`Coverage requires $\operatorname{supp}\pi\subseteq\operatorname{supp}b$. The reverse situation (π using actions b never takes) would make off-policy estimation impossible.` },
    { tag: "lecture", type: "num", q: R`An episode takes three actions with $\pi/b$ probabilities $0.8/0.4$, $0.5/0.25$ and $1.0/0.5$. What is the importance-sampling ratio of the episode?`, answer: 8, tol: 0.0001,
      explain: R`$\rho=2\times2\times2=8$. Environment probabilities cancel, so only the action probabilities matter.` },
    { tag: "lecture", type: "num", q: R`Three episodes from $s$ give returns 10, 4 and 6 with importance ratios 2, 0.5 and 0. What is the <em>weighted</em> importance-sampling estimate? (1 decimal)`, answer: 8.8, tol: 0.01,
      explain: R`$\sum\rho G=20+2+0=22$; $\sum\rho=2.5$; weighted $=22/2.5=8.8$. The ordinary estimate is $22/3\approx7.33$. The third episode ($\rho=0$) is impossible under π and contributes nothing to either.` },
    { tag: "lecture", type: "tf", q: "Importance sampling for off-policy Monte Carlo requires the transition probabilities of the environment.", answer: false,
      explain: R`They appear in both the π- and b-trajectory probabilities and cancel, leaving $\rho=\prod\pi(A_k|S_k)/b(A_k|S_k)$.` },
    { tag: "lecture", type: "num", q: R`With the clipped update $x_{n+1}=x_n+\alpha\,\mathrm{clip}(z;-1,1)$, $x_n=3$, $\alpha=0.1$ and a noisy update $z=25$, what is $x_{n+1}$?`, answer: 3.1, tol: 0.0001,
      explain: R`$\mathrm{clip}(25;-1,1)=1$, so $x_{n+1}=3+0.1\cdot1=3.1$; without clipping it would jump to 5.5.` }
  );
})();
