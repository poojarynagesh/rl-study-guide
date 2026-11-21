// Chapter 1 — questions from the professor's lectures (Aug 3 & 5).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "mcq", q: "In the professor's analogy, a mother teaches a baby who cannot understand language using an angry face or a chocolate. What property of RL does this illustrate?",
      options: ["The feedback is instructive: it says which action is correct", "The feedback is evaluative: it says how good the behaviour was, not what the right behaviour is", "There is no feedback at all, as in unsupervised learning", "The baby has a model of the mother's reactions"], answer: 1,
      explain: "The chocolate/angry face is a scalar judgement of the behaviour, like a reward. Supervised learning would tell the child exactly what to do; unsupervised learning (the bicycle example) has no teacher at all." },
    { tag: "lecture", type: "mcq", q: "Who chooses the policy in the agent–environment framework, as stressed in class?",
      options: ["The environment, which also generates rewards", "A designer who hands the final policy to the agent", "The agent itself — it may start with an arbitrary policy and refine it from data; the environment is oblivious to it", "The model of the environment"], answer: 2,
      explain: R`"Nobody gives the agent a policy." The environment only changes state and emits rewards; it does not know or care which policy the agent follows.` },
    { tag: "lecture", type: "num", q: R`An MDP has 4 states and 2 actions available in every state. How many distinct deterministic policies (lookup tables) are there?`, answer: 16, tol: 0,
      explain: R`Each of the 4 states independently gets one of 2 actions: $2^4=16$. In general $|\mathcal A|^{|\mathcal S|}$.` },
    { tag: "lecture", type: "mcq", q: R`Which of these rows can belong to a stochastic policy over actions $\{A,B\}$?`,
      options: [R`$\pi(A|s)=0.6,\ \pi(B|s)=0.5$`, R`$\pi(A|s)=0.3,\ \pi(B|s)=0.7$`, R`$\pi(A|s)=1.2,\ \pi(B|s)=-0.2$`, R`$\pi(A|s)=0.4,\ \pi(B|s)=0.4$`], answer: 1,
      explain: R`For each state the action probabilities must be non-negative and sum to 1. Only (0.3, 0.7) qualifies.` },
    { tag: "lecture", type: "mcq", q: "Without a model of the environment, what does an RL agent have access to?",
      options: [R`The transition probabilities $p(s'|s,a)$`, R`Data tuples $(S_n,A_n,R_{n+1},S_{n+1})$ collected while interacting`, "The optimal value function", "A labelled set of correct actions"], answer: 1,
      explain: "In most RL problems the dynamics are unknown (e.g. the probability of an accident if you change lanes). The agent records state, action, reward and next state, and learns from that data." },
    { tag: "lecture", type: "mcq", q: "To treat chess as a single-agent RL problem, the professor suggests:",
      options: ["Ignoring the opponent's moves", "Letting the opponent play a fixed (already learned) strategy and treating it as part of the environment; the next state is the board after both moves", "Making the reward depend only on the opponent's move", "Giving each player its own environment"], answer: 1,
      explain: "With the opponent's strategy fixed, its reply is just part of how the environment responds. The agent observes the net board after its own move and the opponent's reply." },
    { tag: "lecture", type: "mcq", q: "In the course's map of methods, where do Monte Carlo and TD learning (as in Chapters 5–6) belong?",
      options: ["Model-based methods", "Model-free methods that estimate values exactly (no approximation)", "Model-free methods with function approximation", "Policy-gradient methods"], answer: 1,
      explain: "Model-based = bandits, MDPs, DP (Ch. 1–4). MC and TD learn from data without a model and keep a separate value per state. Approximation (Ch. 9, DQN, policy gradients such as PPO) is needed when there are too many states." },
    { tag: "lecture", type: "tf", q: "According to the professor, exploration vs. exploitation is a challenge specific to RL that does not arise in supervised or unsupervised learning.", answer: true,
      explain: "Because the agent's own actions determine which data it sees, it must trade trying new actions against using the best known one. Supervised and unsupervised learners work on a given data set." }
  );
})();
