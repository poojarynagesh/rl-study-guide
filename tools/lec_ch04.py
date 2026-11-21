"""Merge the professor's Chapter-4 lecture content (Sep 7, 16) into chapters/ch04.html."""
from lecmerge import merge

BOXES = [
    ('<h2 id="improvement">4.2 Policy improvement</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: details of the 4×4 gridworld sweep <span class="lec-date">Sep 7</span></span>
  <ul>
    <li><strong>A wall move still costs −1.</strong> The agent stays put, but a step has been used. Terminal (goal) states are fixed at value 0 — nothing is earned after the episode ends.</li>
    <li>With $V_0\equiv0$, the first sweep gives just the expected one-step reward: $V_1(s)=-1$ for every non-terminal state. Each further sweep pushes information one step further back from the goals.</li>
    <li>A policy that is greedy with respect to $V_0\equiv0$ is uninformative — every action ties. Greedy choices only become meaningful as the values separate.</li>
    <li>Why −1 per step? It turns the task into a <strong>shortest-path</strong> problem: fewer steps ⇒ less accumulated penalty.</li>
    <li>Typical thresholds mentioned: θ = 0.01, 0.05 or 0.1 — smaller θ means more sweeps and more accuracy.</li>
  </ul>
</div>
'''),
    ('<h2 id="pi">4.3 Policy iteration</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: advantage, greedy rows, and why "stable" means globally optimal <span class="lec-date">Sep 16</span></span>
  <p><strong>Is a different action worth it?</strong> Compare $q_\pi(s,a)$ with $v_\pi(s)$; the difference $A_\pi(s,a)=q_\pi(s,a)-v_\pi(s)$ is the <em>advantage</em>: positive = better than the current behaviour, 0 = equally good, negative = worse.</p>
  <p><strong>Greedy improvement, one state at a time.</strong> If state 1 has $q_\pi(1,\cdot)=(0.5,\ 6.8,\ 1.9,\ 5.4)$ then $\pi'(1)=\arg\max=$ action 2 (while $\max=6.8$ is a <em>value</em>, not an action). Repeat for every state to get the whole new table, e.g. $1\to2,\ 2\to1,\ 3\to4,\ 4\to2$.</p>
  <p><strong>Proof idea of the improvement theorem</strong>: $v_\pi(s)\le q_\pi(s,\pi'(s))=\mathbb E_{\pi'}[R_{t+1}+\gamma v_\pi(S_{t+1})]$; apply the same inequality at $S_{t+1}$, then $S_{t+2}$, … ; the leftover $\gamma^nv_\pi(S_{t+n})\to0$, leaving $v_{\pi'}(s)$.</p>
  <p><strong>Not a local optimum.</strong> If greedy improvement changes nothing, $v_\pi$ satisfies the Bellman <em>optimality</em> equation — a max over every action in every state — whose solution is unique. So the stable policy is globally optimal, not stuck at a local peak.</p>
</div>
'''),
    ('<h2 id="vi">4.4 Value iteration</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: why policy iteration terminates, and how to stop <span class="lec-date">Sep 16</span></span>
  <ul>
    <li>A finite MDP has $m^n$ deterministic policies ($\prod_s|\mathcal A(s)|$ if action sets differ). Each improvement step is at least as good everywhere and strictly better somewhere until the policy is stable, so the outer loop ends after finitely many policy changes.</li>
    <li>The finite bound counts <em>policy changes</em>; each inner evaluation is itself stopped when the largest change in a sweep, Δ, falls below θ.</li>
    <li>Two signs of convergence: no action changes (policy-stable), or a changed policy has the same value everywhere (ties between optimal actions). Use a fixed tie-breaking rule so the algorithm doesn't flip forever between equally good actions.</li>
    <li>Successive policies are <strong>at least as good</strong>, not necessarily strictly better.</li>
  </ul>
</div>
'''),
    ('<h2 id="async">4.5 Asynchronous dynamic programming</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: is one loop faster than two? <span class="lec-date">Sep 16</span></span>
  <p>A student argued that value iteration (one loop) must beat policy iteration (two nested loops). <strong>Not necessarily.</strong> In policy iteration's inner loop the policy is fixed, so the Bellman equation is <em>linear</em> and evaluation is stable. Value iteration's $\max_a$ makes every backup <em>nonlinear</em> and the implied greedy action can keep changing, which can need many sweeps. Which is faster depends on the MDP (transition structure, $n$, $m$, γ, θ). Both use the same state and action sets.</p>
  <p><strong>Why value iteration converges</strong>: the optimality operator $T_*$ is a γ-contraction in the max-norm, $\lVert T_*U-T_*V\rVert_\infty\le\gamma\lVert U-V\rVert_\infty$, so $\lVert V_k-v_*\rVert_\infty\le\gamma^k\lVert V_0-v_*\rVert_\infty$ from any start.</p>
  <p><strong>DP as the template for the rest of the course</strong>: Monte Carlo control and SARSA imitate policy iteration from samples; Q-learning is a sample-based value-iteration backup; actor–critic (critic evaluates, actor improves) echoes policy iteration.</p>
</div>
'''),
]

QUIZ = r'''// Chapter 4 — questions from the professor's lectures (Sep 7, 16).
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
'''

if __name__ == "__main__":
    merge("ch04", BOXES, QUIZ)
