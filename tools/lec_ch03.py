"""Merge the professor's Chapter-3 lecture content (Aug 5, 19, 24, 31, Sep 2, 9) into chapters/ch03.html."""
from lecmerge import merge

BOXES = [
    ('<h3>Where is the agent–environment boundary?</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: the Markov property, pictured <span class="lec-date">Aug 5</span></span>
  <p>Draw time on one axis and states on the other. Two very different paths both arrive in state 2 at time 4. If the agent now takes action $a$, is the chance of moving to state 5 different for the two paths? Under the <strong>Markov assumption</strong>, no:
  $$P(S_{t+1}=s'\mid S_t=s,A_t=a,S_{t-1},A_{t-1},\dots,S_0,A_0)=P(S_{t+1}=s'\mid S_t=s,A_t=a).$$
  "Regardless of whatever path you have chosen", only the current state and action matter — so a policy $\pi(a\mid s)$ need only look at the current state.</p>
  <ul>
    <li>The course also assumes <strong>stationary dynamics</strong>: these probabilities do not change with $t$.</li>
    <li>Markov is an assumption, not a law. If the dynamics depend on the past, the history (past states and actions) must be recorded and the policy becomes $\pi(a\mid s_0,a_0,\dots,s_t)$ — or the state must be enriched until it is Markov.</li>
  </ul>
</div>
'''),
    ('<h2 id="rewards">3.2 Goals and rewards</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: the recycling robot as taught, and why not learn the model <span class="lec-date">Aug 19 &amp; 24</span></span>
  <p>In class the battery-dies case carried a <strong>rescue penalty of −5</strong> (the book uses −3): from <em>low</em>, <em>search</em> keeps the robot low with probability β (reward $r_{\text{search}}$) and drains it with probability $1-\beta$ (reward −5, carried back to <em>high</em>); <em>recharge</em> goes to <em>high</em> with reward 0. So
  $$r(\text{low},\text{search})=\beta\,r_{\text{search}}+(1-\beta)(-5).$$
  A student asked why waiting forever in <em>high</em> never drains the battery: the table is a <strong>single-stage</strong> model — one decision step at a time; longer horizons come from applying it repeatedly.</p>
  <p>Deriving $r(s,a,s')$: $P(R_{t+1}=r\mid s,a,s')=p(s',r\mid s,a)/p(s'\mid s,a)$, so $r(s,a,s')=\sum_r r\,\dfrac{p(s',r\mid s,a)}{\sum_{r'}p(s',r'\mid s,a)}$ (don't forget the factor $r$ — the professor's slip, corrected in class).</p>
  <p><strong>Why the course goes model-free:</strong> "Learning the system model is not easy — it requires much more data than what our algorithms will need." So later chapters use the data $(S_t,A_t,R_{t+1},S_{t+1})$ directly, and approximation when there are $10^{100}$ states (e.g. city-wide traffic control).</p>
</div>
'''),
    ('<h3>Example 3.4 — pole balancing, two formulations</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: why γ &lt; 1 makes returns finite — and when γ = 1 is fine <span class="lec-date">Aug 31</span></span>
  <p>If every reward satisfies $|R_{t+1}|\le B$, then by the triangle inequality
  $$|G_t|\le B+\gamma B+\gamma^2B+\cdots=\frac{B}{1-\gamma}\qquad(0\le\gamma\lt1).$$
  Even $\gamma=0.99$ gives the finite bound $100B$. With $\gamma=1$ the denominator vanishes and there is no bound.</p>
  <ul>
    <li><strong>Why γ = 1 fails for continuing tasks</strong>: a policy earning $1,1,1,\dots$ and one earning $1,\tfrac12,\tfrac13,\dots$ both have return $\infty$ (the harmonic series diverges), although the first is clearly better. Infinite returns cannot be ranked.</li>
    <li><strong>Why γ = 1 is fine for episodic tasks</strong>: the sum has finitely many bounded terms — provided the policy is <strong>proper</strong>, i.e. it reaches the terminal state in finite time with probability one (with $n$ non-terminal states, a positive probability of terminating within $n$ steps). A bad policy that wanders forever would otherwise break the argument.</li>
    <li>A return is a <strong>random</strong> quantity (actions and transitions are random); the value function is its <em>expectation</em>, which is what we compare.</li>
  </ul>
</div>
'''),
    ('<h2 id="unified">3.4 Unified notation for episodic and continuing tasks</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: three reward designs for pole balancing <span class="lec-date">Aug 31</span></span>
  <p>Students first proposed rewards for a small angle or for corrective moves (30° → 20°). Plausible — but they assume the exact angle can be measured, which may not be true in practice. Compare three simpler designs (episode ends when the pole falls):</p>
  <div class="table-wrap"><table>
    <tr><th>Rewards</th><th>γ</th><th>Return $G_0$ if the pole falls at step $T$</th><th>Verdict</th></tr>
    <tr><td>+1 each step survived, 0 on failure</td><td>1</td><td>number of steps survived</td><td>Return = survival time — exactly the goal</td></tr>
    <tr><td>0 before failure, −1 on failure</td><td>1</td><td>$-1$ for <em>every</em> episode</td><td>Useless: falling at step 1 and at step 1000 look the same</td></tr>
    <tr><td>0 before failure, −1 on failure</td><td>$0\lt\gamma\lt1$</td><td>$-\gamma^{T-1}$</td><td>Works: later failure ⇒ return closer to 0</td></tr>
  </table></div>
  <p>With $\gamma=0.9$: failing at step 1 gives −1, at step 3 gives $-0.81$, at step 10 gives $-0.9^9\approx-0.387$. "The absolute value of the reward matters less than whether its <strong>trend</strong> captures the real objective."</p>
</div>
'''),
    ('<h3>Adding a constant to all rewards (Exercises 3.15, 3.16)</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: checking the gridworld values yourself <span class="lec-date">Sep 2</span></span>
  <p>Equiprobable policy, $\gamma=0.9$; off-grid moves leave the agent in place with reward −1 (a "reflecting boundary").</p>
  <ul>
    <li><strong>State A</strong> (every action → A′, reward +10): the four ¼-weighted terms are identical, so $v_\pi(A)=10+0.9\,v_\pi(A')=10+0.9(-1.3)=8.83$. <em>Below</em> its reward of 10, because A′ is a negative-value state.</li>
    <li><strong>State B</strong> (→ B′, reward +5): $5+0.9(0.4)=5.36$ — <em>above</em> its reward, because B′ is positive. A value is never just the one-step reward.</li>
    <li><strong>Bottom-right corner D</strong>: Up → −1.2, Left → −1.4 (reward 0); Right and Down hit the wall (reward −1) and <em>return to D</em>. The self-loops put $v_\pi(D)$ on both sides:
      $$v=\tfrac14(0+0-1-1)+0.9\cdot\tfrac14\big(-1.2-1.4+v+v\big)\ \Rightarrow\ 0.55v=-1.085\ \Rightarrow\ v\approx-1.97\ (\text{table: }-2.0).$$
      Keep the $+\gamma v(s')$ sign — the −1 is the reward; $v$ itself just turns out negative.</li>
    <li>Why are the bottom rows negative? There is no goal; they are far from A and B and the random policy often bumps into walls.</li>
  </ul>
  <p>Expected one-step reward under a policy (Aug 31): $\mathbb E_\pi[R_{t+1}\mid S_t=s]=\sum_r r\sum_a\pi(a\mid s)\sum_{s'}p(s',r\mid s,a)$. And remember: $q_\pi(s,a)$ takes action $a$ first — <em>even if π would never choose it</em> — and follows π only from the next step.</p>
</div>
'''),
    ('<h3>Example 3.8 — solving the gridworld</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: reading optimality <span class="lec-date">Sep 2 &amp; 9</span></span>
  <ul>
    <li><strong>"Optimal" means optimal in every state</strong>: $v_{\pi_*}(s)=v_*(s)$ for all $s$, not just a chosen start state.</li>
    <li><strong>$v_*$ is unique; $\pi_*$ need not be.</strong> If two candidate "optimal" values for a state were 7.9 and 8.4, the smaller could not be the maximum. Ties between actions (two equally short paths) give several optimal policies with the same $v_*$.</li>
    <li>In the gridworld every action in A (or B) leads to the same place with the same reward, so <em>all four actions tie</em> there.</li>
    <li><strong>Why the optimal gridworld values are all non-negative</strong>: the optimal policy never walks into a wall — it only takes value-maximising moves — whereas the random policy did so with probability ¼ near the edges.</li>
    <li><strong>Reading $\pi_*$ off a Q-table</strong>: in each row (state) pick the action(s) with the largest $q_*(s,a)$; $v_*(s)=\max_aq_*(s,a)$.</li>
    <li>Number of deterministic policies: $m^n$ for $n$ states and $m$ actions — exhaustive search is hopeless, hence Chapter 4. Two stochastic policies differ if their action probabilities differ in any state (0.1 vs 0.8 for $a_1$).</li>
  </ul>
</div>
'''),
]

QUIZ = r'''// Chapter 3 — questions from the professor's lectures (Aug 5 – Sep 9).
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "lecture", type: "num", q: R`Rewards satisfy $|R_t|\le2$ and $\gamma=0.95$. What upper bound on $|G_t|$ follows from the geometric-series argument?`, answer: 40, tol: 0.001,
      explain: R`$|G_t|\le B/(1-\gamma)=2/0.05=40$.` },
    { tag: "lecture", type: "mcq", q: R`A continuing task with $\gamma=1$: policy P earns 1 at every step, policy Q earns $1,\tfrac12,\tfrac13,\dots$. What goes wrong?`,
      options: ["Q has the larger return", R`Both returns are infinite (the harmonic series diverges), so returns cannot rank the policies although P is clearly better`, "Both returns are finite", "Only P's return is infinite"], answer: 1,
      explain: R`$\sum1=\infty$ and $\sum1/n=\infty$. Discounting with $\gamma\lt1$ makes both finite ($1/(1-\gamma)$ vs something smaller) and restores the ranking.` },
    { tag: "lecture", type: "mcq", q: R`Pole balancing with reward 0 on every step and −1 when the pole falls, and $\gamma=1$. What is the return of an episode?`,
      options: ["The number of steps survived", R`Always $-1$, whatever the policy — so it cannot distinguish good from bad balancing`, R`$-\gamma^{T-1}$`, "Zero"], answer: 1,
      explain: R`Every episode ends in exactly one −1. Adding $\gamma\lt1$ fixes it: $G_0=-\gamma^{T-1}$ rises towards 0 as the fall comes later.` },
    { tag: "lecture", type: "num", q: R`Same failure-only reward but $\gamma=0.9$; the pole falls at step $T=10$. What is $G_0$? (3 decimals)`, answer: -0.387, tol: 0.002,
      explain: R`$G_0=-\gamma^{T-1}=-0.9^9\approx-0.387$, better than falling at step 3 ($-0.81$).` },
    { tag: "lecture", type: "num", q: R`Gridworld, equiprobable policy, $\gamma=0.9$. In corner D, Up leads to a state of value −1.2 and Left to −1.4 (reward 0); Right and Down hit the wall (reward −1, stay in D). Solve the Bellman equation for $v_\pi(D)$. (2 decimals)`, answer: -1.97, tol: 0.02,
      explain: R`$v=-0.5+0.225(-2.6+2v)\Rightarrow0.55v=-1.085\Rightarrow v\approx-1.97$. The two wall moves contribute both a −1 reward and the self-loop term $\gamma v_\pi(D)$.` },
    { tag: "lecture", type: "mcq", q: R`In the gridworld, $v_\pi(A)=8.8$ is below A's reward of 10 while $v_\pi(B)=5.3$ is above B's reward of 5. Why?`,
      options: ["Rounding error in the table", R`A always jumps to A′, whose value is negative (−1.3); B jumps to B′, whose value is positive (0.4)`, "B is visited more often", R`$\gamma$ is applied only to A`], answer: 1,
      explain: R`$v(A)=10+0.9(-1.3)=8.83$; $v(B)=5+0.9(0.4)=5.36$. A state's value adds the discounted value of where it leads.` },
    { tag: "lecture", type: "mcq", q: "Why does the optimal gridworld value table contain no negative numbers, unlike the equiprobable one?",
      options: ["Because γ changes to 1", "Because the optimal policy never chooses wall-bumping moves (−1); it only takes value-maximising actions", "Because negative rewards are removed from the problem", "Because optimal values are always positive in any MDP"], answer: 1,
      explain: "The random policy hits walls with probability 1/4 near edges. The optimal policy avoids those penalties and heads towards A and B, so every state's optimal value is non-negative here (not a general law)." },
    { tag: "lecture", type: "num", q: "How many deterministic policies does an MDP with 3 states and 4 actions per state have?", answer: 64, tol: 0,
      explain: R`$m^n=4^3=64$.` },
    { tag: "lecture", type: "num", q: R`Recycling robot as in class: from <em>low</em>, <em>search</em> stays low with probability $\beta=0.6$ and reward $r_{\text{search}}=2$; otherwise the battery dies (penalty −5). What is $r(\text{low},\text{search})$?`, answer: -0.8, tol: 0.001,
      explain: R`$0.6\cdot2+0.4\cdot(-5)=1.2-2=-0.8$. Searching on a low battery is a losing bet in expectation here.` },
    { tag: "lecture", type: "tf", q: R`An MDP can have several different optimal policies, but its optimal value function $v_*$ is unique.`, answer: true,
      explain: R`$v_*(s)=\max_\pi v_\pi(s)$ is a single number per state; policies that tie between equally good actions all attain it.` },
    { tag: "lecture", type: "mcq", q: "If the state evolution is NOT Markov (the next state depends on earlier states too), what must the policy depend on?",
      options: ["Only the current state, as usual", "The history of past states and actions (or an enlarged state that summarises it)", "Only the reward", "Nothing — a random policy is optimal"], answer: 1,
      explain: "Without the Markov property the current state is not a sufficient statistic, so history must be tracked, as stressed in the Aug 5 lecture." }
  );
})();
'''

if __name__ == "__main__":
    merge("ch03", BOXES, QUIZ)
