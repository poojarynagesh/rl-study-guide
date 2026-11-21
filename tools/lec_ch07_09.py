"""Merge the professor's Chapter-7 (Oct 14, 19, 21) and Chapter-9 (Oct 21) lecture content."""
from lecmerge import merge

CH07 = [
    ('<h3>Example 7.1 — n-step TD on the random walk</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: where the n-step target comes from, and why it helps <span class="lec-date">Oct 14 &amp; 19</span></span>
  <ul>
    <li><strong>Unroll the Bellman equation</strong>: substitute $v_\pi(s')$ into itself to get $v_\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma R_{t+2}+\gamma^2v_\pi(S_{t+2})]$, and after $n$ substitutions the "n-step Bellman equation" $v_\pi(s)=\mathbb E_\pi\big[\sum_{k=1}^{n}\gamma^{k-1}R_{t+k}+\gamma^nv_\pi(S_{t+n})\big]$ — exactly what $G_{t:t+n}$ samples.</li>
    <li><strong>Less weight on a poor estimate</strong>: with γ = 0.9 and n = 10 the bootstrap term carries $0.9^{10}\approx0.349$ instead of 0.9 — early, inaccurate values matter less and real rewards matter more (lower bias, typically higher variance).</li>
    <li><strong>Error-reduction property</strong>: the expected-target error contracts by $\gamma^n$: $\max_s|\mathbb E_\pi[G_{t:t+n}\mid S_t=s]-v_\pi(s)|\le\gamma^n\max_s|V_{t+n-1}(s)-v_\pi(s)|$. With γ = 0.5, n = 3: factor 0.125 vs 0.5 for one-step TD. This is about expected bias; it does not mean the largest n gives the lowest sampled error.</li>
    <li>With $V$ fixed, the n-step error is a discounted sum of one-step errors: $G_{t:t+n}-V(S_t)=\sum_{k=t}^{t+n-1}\gamma^{k-t}\delta_k$ (Exercise 7.1).</li>
    <li><strong>Termination inside the window</strong>: at $t=T-4$ with $n=6$, only four rewards remain: $G_{t:t+6}=R_{T-3}+\gamma R_{T-2}+\gamma^2R_{T-1}+\gamma^3R_T$ — the Monte Carlo return, with no bootstrap ($V(S_T)=0$).</li>
  </ul>
</div>
'''),
    ('<h2 id="nstep-sarsa">7.2 n-step Sarsa</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: one episode under 1-, 2- and 3-step TD, and choosing n <span class="lec-date">Oct 19</span></span>
  <p>Random walk, all values 0.5, α = 0.1, γ = 1. Episode $C\xrightarrow0D\xrightarrow0E\xrightarrow1G$:</p>
  <div class="table-wrap"><table>
    <tr><th>Method</th><th>V(C)</th><th>V(D)</th><th>V(E)</th><th>Why</th></tr>
    <tr><td>1-step</td><td>0.50</td><td>0.50</td><td>0.55</td><td>only E's target sees the +1; D's target $0+V(E)=0.5$</td></tr>
    <tr><td>2-step</td><td>0.50</td><td>0.55</td><td>0.55</td><td>D's target $0+1=1$; C's target $0+0+V(E)=0.5$</td></tr>
    <tr><td>3-step</td><td>0.55</td><td>0.55</td><td>0.55</td><td>C's target $0+0+1=1$</td></tr>
  </table></div>
  <p>The reward travels back $n$ states per episode — but the update for $S_t$ must <strong>wait</strong> $n$ transitions (1-step: immediately; Monte Carlo: until the end). The equal 0.55s are special to zero intermediate rewards and γ = 1.</p>
  <p><strong>Choosing n.</strong> On the 19-state walk (n = 1, 2, 4, …, 512; RMS error over the first 10 episodes, averaged over 100 runs) every n gives a U-shaped curve in α, the best α differs by n, intermediate n (up to about 16) did best, and very large n drifted towards Monte Carlo's worse error. Tune n and α together.</p>
  <p><strong>Research aside — adapting n while learning</strong> (two timescales): a fast recursion updates values with step $a_m$, a slow one adjusts n (e.g. to reduce variance) with step $b_m$; both satisfy Robbins–Monro and $b_m/a_m\to0$, e.g. $a_m=1/m^{2/3}$, $b_m=1/m$. The fast one sees n as frozen; the slow one sees values as already converged — just as policy evaluation should run faster than policy improvement.</p>
</div>
'''),
    ('<h3>n-step Expected Sarsa</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: reading Figure 7.4, and n-step Sarsa as a sum of TD errors <span class="lec-date">Oct 21</span></span>
  <ul>
    <li>The path in the figure is <strong>not</strong> the optimal path — it is what the agent happened to do in one training episode (steps −1, goal 0, values initialised to 0). After it, one-step Sarsa strengthens only the last pair before the goal; ten-step Sarsa strengthens the last ten; a pair 11 steps back is untouched by that episode.</li>
    <li>On-policy means <em>every</em> action in the segment, $A_t,\dots,A_{t+n}$, is drawn from the same ε-greedy (or consistently parameterised UCB) policy. Only $Q(S_t,A_t)$ changes in an update; α = 0.1 is a reasonable default.</li>
    <li><strong>Exercise 7.4</strong>: with $\delta_k=R_{k+1}+\gamma Q_k(S_{k+1},A_{k+1})-Q_{k-1}(S_k,A_k)$,
      $$G_{t:t+n}=Q_{t-1}(S_t,A_t)+\sum_{k=t}^{\min(t+n,T)-1}\gamma^{k-t}\delta_k.$$
      Each bootstrap term is added in one δ and subtracted in the next (telescoping). If the episode ends first, the leftover $\gamma^{T-t}Q(S_T,\cdot)$ is 0 because terminal Q-values are 0 — hence the min in the upper limit.</li>
  </ul>
</div>
'''),
    ('<h2 id="control-variates">7.4 *Per-decision methods with control variates</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: off-policy n-step updates in practice <span class="lec-date">Oct 21</span></span>
  <ul>
    <li>Example: ten actions, but experience says only A and B are promising. The target π puts its probability on A and B; the behaviour $b$ spreads over all ten. Coverage ($\pi\gt0\Rightarrow b\gt0$) is needed, or a ratio would divide by zero.</li>
    <li>The ratio multiplies the <strong>whole increment</strong>: $V\leftarrow V+\alpha\rho_{t:t+n-1}[G_{t:t+n}-V]$. If any action in the window is impossible under π, $\rho=0$ and the value is left unchanged — that segment says nothing about π.</li>
    <li>For n-step Sarsa the product starts at $t+1$: $\rho_{t+1:t+n}$, because $Q(S_t,A_t)$ is already conditioned on the first action $A_t$; only the later actions need correcting.</li>
  </ul>
</div>
'''),
]

QUIZ07 = r'''// Chapter 7 — questions from the professor's lectures (Oct 14, 19, 21).
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
'''

CH09 = [
    ('<h2 id="ve">9.2 The prediction objective $\overline{\mathrm{VE}}$</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: why tables break, and what replaces them <span class="lec-date">Oct 21</span></span>
  <p><strong>The course so far</strong>: bandits (one state) → MDPs with a known model (DP) → Monte Carlo (no model, but must wait for episodes to end) → one-step TD (immediate bootstrap) → n-step TD (in between). All of Chapters 5–7 are <em>tabular</em>: one stored number per state or state-action pair.</p>
  <p><strong>Network routing example.</strong> Seven routers between a source and a destination; packets are routed dynamically like cars around congestion. Finite buffers overflow, packets are dropped and must be retransmitted, which worsens congestion. Take the state to be the queue lengths $(n_1,\dots,n_7)$. With 10,000 possible values per router, the number of states is $(10^4)^7=10^{28}$ — <em>not</em> 70,000 (states multiply, they don't add). Monte Carlo is impractical too: "termination" (all queues empty at once) almost never happens. Finite does not mean feasible: $10^{50}$, $10^{100}$ states cannot even be stored.</p>
  <p><strong>Approximation</strong>: $v(s)\approx\hat v(s,\mathbf w)$ with $\mathbf w\in\mathbb R^d$, $d\ll|\mathcal S|$ (tens to thousands of components). Linear: $\hat v=\mathbf w^\top\boldsymbol\phi(s)$ — shared weights, so an update for one state generalises to similar states. Nonlinear: a neural network $f(s;\mathbf w)$ (weights and biases are <em>parameters</em>; architecture and learning rate are <em>hyperparameters</em>). Even the best $\mathbf w$ may not reproduce $v_\pi$ exactly (representation error), yet the induced policy can be excellent.</p>
  <div class="table-wrap"><table>
    <tr><th>Method</th><th>Update target $U_t$ for $S_t$</th></tr>
    <tr><td>Monte Carlo</td><td>$G_t$</td></tr>
    <tr><td>One-step TD</td><td>$R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)$</td></tr>
    <tr><td>n-step TD</td><td>$G_{t:t+n}$</td></tr>
    <tr><td>Dynamic programming</td><td>$\mathbb E_\pi[R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)\mid S_t]$</td></tr>
  </table></div>
</div>
'''),
]

QUIZ09 = r'''// Chapter 9 — questions from the professor's lectures (Oct 21).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "num", q: R`A network has 7 routers, and the state is the vector of their queue lengths, each taking 10,000 possible values. The number of states is $10^x$. What is $x$?`, answer: 28, tol: 0,
      explain: R`$(10^4)^7=10^{28}$. A table with one entry per state is impossible, which motivates function approximation.` },
    { tag: "lecture", type: "mcq", q: "Why is 70,000 the wrong count of states for 7 routers with 10,000 queue values each?",
      options: ["Because routers can be empty", "A state is the whole vector of all seven queue lengths, so the possibilities multiply (10,000⁷), they do not add", "Because packets can be dropped", "Because the count should be 7"], answer: 1,
      explain: "Changing any single component gives a different network state; counting combinations gives 10,000 × 10,000 × … (seven factors)." },
    { tag: "lecture", type: "mcq", q: "Why is plain Monte Carlo impractical for the router network?",
      options: ["Rewards are negative", "It must wait for episode termination, and a natural terminal event (all queues empty at once) occurs too rarely", "It needs the transition model", "It cannot use discounting"], answer: 1,
      explain: "Continuing tasks with rare or no terminal states give Monte Carlo too few completed returns; TD-style bootstrapping updates every step." },
    { tag: "lecture", type: "mcq", q: R`For a neural-network value function $\hat v(s,\mathbf w)$, which of these is a hyperparameter rather than a learned parameter?`,
      options: ["A hidden-layer weight", "An output bias", "The learning rate α", R`A component of $\mathbf w$`], answer: 2,
      explain: "Weights and biases are learned from data (parameters); learning rate, architecture and regularisation strength are set from outside (hyperparameters)." },
    { tag: "lecture", type: "mcq", q: R`In the unified view "update $\hat v(S_t)$ towards target $U_t$", which pairing is correct for one-step TD with approximation?`,
      options: [R`$U_t=G_t$`, R`$U_t=R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)$`, R`$U_t=\mathbb E_\pi[R_{t+1}+\gamma\hat v(S_{t+1})\mid S_t]$`, R`$U_t=G_{t:t+n}$`], answer: 1,
      explain: R`$G_t$ is Monte Carlo, $G_{t:t+n}$ n-step TD, and the expectation is the model-based DP target.` },
    { tag: "lecture", type: "tf", q: "With function approximation, the learned values may never equal the true values exactly, yet the greedy policy they induce can still be excellent.", answer: true,
      explain: "The true value function may lie outside the chosen function class (representation error), but approximate solutions often give very good policies in practice." }
  );
})();
'''

if __name__ == "__main__":
    merge("ch07", CH07, QUIZ07)
    merge("ch09", CH09, QUIZ09)
