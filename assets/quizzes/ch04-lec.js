// Chapter 4 — questions from the professor's lectures (Sep 7, 16).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "mcq", q: R`In state 1, $q_\pi(1,a)$ for actions 1–4 is $(0.5,\ 6.8,\ 1.9,\ 5.4)$. What does greedy policy improvement set $\pi'(1)$ to?`,
      options: ["6.8", "Action 2", "Action 4", R`The average, 3.65`], answer: 1,
      explain: R`$\arg\max_a$ returns the action (2); $\max_a$ returns the value 6.8. The same is done separately in every state.` },
    { tag: "lecture", type: "mcq", q: R`For the current policy π, $v_\pi(s)=4$ and $q_\pi(s,a)=3$ for some action $a$. What does this say about switching to $a$ in $s$ (and then following π)?`,
      options: ["It is an improvement", R`It is worse: the advantage $q_\pi(s,a)-v_\pi(s)=-1\lt0$`, "It is equally good", "Nothing can be said without the model"], answer: 1,
      explain: R`The advantage compares one deviation with the current behaviour. Negative advantage means the deviation lowers expected return.` },
    { tag: "lecture", type: "mcq", q: "Why is a policy that greedy improvement leaves unchanged guaranteed to be globally (not just locally) optimal?",
      options: ["Because policy iteration explores randomly", "Because its value then satisfies the Bellman optimality equation, which has a unique solution v*", "Because the number of policies is finite", "It is only locally optimal"], answer: 1,
      explain: R`If $\pi'=\pi$, then $v_\pi(s)=\max_a\sum p[r+\gamma v_\pi(s')]$ for all $s$ — the optimality equation, whose unique fixed point is $v_*$.` },
    { tag: "lecture", type: "tf", q: "Value iteration has a single loop, so it always converges in less computation than policy iteration.", answer: false,
      explain: "Policy iteration's inner evaluation is a stable linear problem for a fixed policy; value iteration's max makes it nonlinear and the greedy action may keep changing. Either can be faster depending on the MDP." },
    { tag: "lecture", type: "num", q: R`Value iteration with $\gamma=0.9$ starts with $\lVert V_0-v_*\rVert_\infty=10$. Using the contraction property, what is the guaranteed bound on $\lVert V_5-v_*\rVert_\infty$? (2 decimals)`, answer: 5.90, tol: 0.01,
      explain: R`$\gamma^5\cdot10=0.59049\cdot10\approx5.90$. Each sweep shrinks the worst-case error by at least a factor γ.` },
    { tag: "lecture", type: "num", q: R`4×4 gridworld, reward −1 per step, equiprobable policy, $\gamma=1$, $V_0\equiv0$, terminal value 0. After sweep 1 every non-terminal state has $V_1=-1$. For the state immediately right of the top-left terminal (left → terminal; up → wall; right and down → non-terminal states), what is $V_2$?`, answer: -1.75, tol: 0.001,
      explain: R`$\tfrac14[(-1+0)+(-1-1)+(-1-1)+(-1-1)]=\tfrac14(-7)=-1.75$ (shown as −1.7 in the book's figure). The wall move costs −1 and returns to the same state, whose $V_1=-1$.` },
    { tag: "lecture", type: "tf", q: "In the gridworld, an action that would leave the grid costs −1 even though the agent's position does not change.", answer: true,
      explain: "A step has been taken, so the per-step penalty applies; the next state is the same cell." },
    { tag: "lecture", type: "tf", q: "In policy iteration every new policy is strictly better than the previous one in every state.", answer: false,
      explain: R`The improvement theorem guarantees $v_{\pi'}\ge v_\pi$ — at least as good. Equal value signals that an optimal policy has been reached.` },
    { tag: "lecture", type: "num", q: R`An MDP has 5 states; states 1–3 have 2 actions and states 4–5 have 3 actions. How many deterministic policies are there?`, answer: 72, tol: 0,
      explain: R`$\prod_s|\mathcal A(s)|=2^3\cdot3^2=8\cdot9=72$ — finite, so policy iteration terminates.` }
  );
})();
