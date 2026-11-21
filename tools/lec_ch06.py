"""Merge the professor's Chapter-6 lecture content (Sep 30, Oct 7, 12, 14) into chapters/ch06.html."""
from lecmerge import merge

BOXES = [
    ('<h2 id="advantages">6.2 Advantages of TD prediction methods</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: what TD updates, and when <span class="lec-date">Sep 30</span></span>
  <ul>
    <li>TD updates the <strong>state just left</strong>: after $S_0\xrightarrow{R_1}S_1$ it updates $V(S_0)$; after $S_1\xrightarrow{R_2}S_2$ it updates $V(S_1)$ — no waiting for the episode to end. Starting from a zero table, the first update moves only $V(S_0)$, by $\alpha R_1$.</li>
    <li>"Temporal difference": the error compares the prediction now, $V(S_t)$, with the reward-adjusted prediction one step later, $R_{t+1}+\gamma V(S_{t+1})$.</li>
    <li>With $V$ held fixed during the episode, the Monte Carlo error telescopes: $G_t-V(S_t)=\delta_t+\gamma\big(G_{t+1}-V(S_{t+1})\big)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k$ (using $G_T=V(S_T)=0$). If V changes online after each step, the identity holds only approximately.</li>
  </ul>
</div>
'''),
    ('<h2 id="optimality">6.3 Optimality of TD(0) — batch updating</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: random-walk values, the first episode, and choosing α <span class="lec-date">Sep 30 &amp; Oct 7</span></span>
  <p><strong>Exact values by hand</strong> (states A–E, terminals F (reward 0) and G (reward 1 on entering from E), γ = 1). From A: $V(A)=\tfrac12V(B)$, so $V(B)=2V(A)$; from B: $V(C)=3V(A)$; then $V(D)=4V(A)$, $V(E)=5V(A)$; from E: $V(E)=\tfrac12V(D)+\tfrac12$ ⇒ $5V(A)=2V(A)+\tfrac12$ ⇒ $V(A)=\tfrac16$. So $V=\tfrac16,\tfrac26,\dots,\tfrac56$ — the probability of exiting right. Terminal states themselves are worth 0; the +1 belongs to the transition E → G.</p>
  <p><strong>First episode</strong> C → B → A → F with $\alpha=0.1$, all $V=0.5$: the C and B updates change nothing ($0+0.5-0.5=0$); only $V(A)\leftarrow0.5+0.1(0+0-0.5)=0.45$. That single dip in the plot tells you the episode ended on the left.</p>
  <p><strong>Step size depends on your budget.</strong> RMS error $\sqrt{\tfrac15\sum_s(V(s)-v_\pi(s))^2}$ vs episodes: with 25 episodes α = 0.15 was best among those tried; around 50 episodes α = 0.10; a small α = 0.03 looks poor at 100 episodes but might win after 1000. "Best" only means best among tested values at that horizon. A large α amplifies the random TD error ($\Delta V=\alpha\delta_t$) → fast start, then oscillation; α = 0.5 is not automatically better.</p>
  <p>Per-state $1/N(s)$ step sizes shrink very quickly and can stall learning; a block schedule (α = 1 for five episodes, ½ for the next five, ⅓ …) decays more gently. Small constant α is common in practice and tracks non-stationarity.</p>
</div>
'''),
    ('<h2 id="sarsa">6.4 Sarsa: on-policy TD control</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: what a batch pass actually computes <span class="lec-date">Oct 7</span></span>
  <p>With a fixed set of episodes (say only ten, and no more can be bought), compute every TD increment using the <em>current, frozen</em> $V$, sum them per state, update once, and repeat until nothing changes. If state $s$ was visited $K$ times with rewards $R_i$ and successors $S_i'$:
  $$V(s)\leftarrow V(s)+\alpha\sum_{i=1}^{K}\big[R_i+\gamma V(S_i')-V(s)\big].$$
  $K$ differs from state to state (its empirical visit count). On the next pass the data is the same but the errors change because $V$ changed.</p>
  <p>Why may batch TD use the six B→1 episodes to value A in Example 6.4, although A's own episode ended with 0? Because of the <strong>Markov property</strong>: once in B, how you got there is irrelevant, so every visit to B informs $V(B)$ and therefore $V(A)=0+V(B)=\tfrac34$. Batch MC ($V(A)=0$) and batch TD ($\tfrac34$) are each correct for what they compute.</p>
</div>
'''),
    ('<h2 id="qlearning">6.5 Q-learning: off-policy TD control</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: Sarsa details and the windy-gridworld run <span class="lec-date">Oct 7 &amp; 12</span></span>
  <ul>
    <li>$A_t$ picks <em>which entry</em> is updated; $A_{t+1}$ supplies the bootstrap value. Both must come from the <strong>same</strong> ε-greedy policy (same ε) — that is what makes Sarsa on-policy. $Q(\text{terminal},\cdot)=0$.</li>
    <li>Windy gridworld (7 × 10): wind by column $[0,0,0,1,1,1,2,2,1,0]$ pushes the agent up <em>after</em> its move, clipped at the edge. "Right" in a wind-1 column moves right 1 and up 1; "down" there leaves you in place. The shortest route is 15 steps and depends on turning left at the right row so the wind carries you into the goal.</li>
    <li>Sarsa with ε = 0.1, α = 0.5: early episodes took ~60 steps (about 50 episodes in 3000 steps); after ~170 episodes and 8000 steps the learned path was 17 steps — much better, but not the optimal 15, because exploration continues.</li>
  </ul>
</div>
'''),
    ('<h2 id="expected-sarsa">6.6 Expected Sarsa</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: ε-greedy arithmetic, the cliff, and reward design <span class="lec-date">Oct 12</span></span>
  <p><strong>ε-greedy probabilities</strong> with ε = 0.1: with 4 actions the greedy one gets $0.9+0.1/4=0.925$ and each other $0.025$; with 3 actions $0.9+0.1/3\approx0.933$ and $0.033$ each. Q-learning's target uses the greedy action at $S_{t+1}$, but the action actually executed there is drawn again ε-greedily — the update imagines greedy continuation while behaviour keeps exploring.</p>
  <p><strong>Cliff walking</strong>: each step −1; falling costs −100 and sends you back to the start <em>without ending the episode</em>. Q-learning learns the 13-step edge route (optimal once exploration stops) but falls during ε-greedy training — average training return about −50. Sarsa learns a ~17-step safer route because its target prices in its own exploratory slips — about −25 during training. Training return and final greedy-policy quality are different criteria.</p>
  <p><strong>Why −1 per step and not +1?</strong> A positive per-step reward pays the agent to wander in cycles forever; a living cost makes finishing quickly the goal. The shortest path is optimal here only because every ordinary step costs the same; shrink the cliff penalty to −10 and edge-hugging becomes more attractive. The professor's analogy: a driver may prefer a longer safe road over speeding along a cliff edge.</p>
</div>
'''),
    ('<h2 id="max-bias">6.7 Maximization bias and double learning</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: an Expected Sarsa target in numbers, and which method to use <span class="lec-date">Oct 12</span></span>
  <p>At $S_{t+1}$: $Q=(4,\,6,\,3)$, ε = 0.1, so π = (1/30, 14/15, 1/30). Expected Sarsa uses $4\cdot\tfrac1{30}+6\cdot\tfrac{14}{15}+3\cdot\tfrac1{30}=\tfrac{35}{6}\approx5.83$; Q-learning uses 6; Sarsa uses whichever action was sampled (maybe 3). (In class $0.1/3$ was first written as 0.33 — it is 0.033.)</p>
  <ul>
    <li><strong>Interim</strong> performance (first 100 episodes) measures learning speed and early safety; <strong>asymptotic</strong> (~100,000 episodes) measures where it ends up. Expected Sarsa was strong on both and robust to α; Sarsa degraded as α → 1 because its sampled target is noisy and α magnifies the noise.</li>
    <li>Cost: the expectation reads every action at $S_{t+1}$ — negligible for small action sets, noticeable for large ones.</li>
    <li>No universal winner: Sarsa for safety under persistent exploration, Q-learning for the final greedy policy, Expected Sarsa for low variance when affordable. Small α (0.1, 0.05, 0.01) usually tames variability.</li>
  </ul>
</div>
'''),
    ('<h2 id="afterstates">6.8 Games, afterstates, and other special cases</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: reading the maximization-bias experiment <span class="lec-date">Oct 14</span></span>
  <ul>
    <li>B's reward is $\mathcal N(-0.1,1)$, so $P(R\gt0)=1-\Phi(0.1)\approx0.46$ — almost half the samples look good, which the max latches onto. The flaw is using the <em>same</em> noisy numbers to <strong>select</strong> and to <strong>evaluate</strong>: $\mathbb E[\max_a\hat q(a)]\ge\max_a\mathbb E[\hat q(a)]$.</li>
    <li>With ε = 0.1 and two actions, the best achievable "% left" is <strong>5%</strong> ($\varepsilon/2$), not 0. Q-learning was still near 10% at 300 episodes; Double Q-learning approached 5% after roughly 100–200.</li>
    <li>Behaviour is ε-greedy on $Q_1+Q_2$ (same argmax as their average). Example at A: $Q_1=(-3.5,\,0)$, $Q_2=(2.6,\,0)$ for (left, right) disagree; the sum $(-0.9,\,0)$ picks right, so P(right) = 0.95, P(left) = 0.05 — and 0.05 is ε/2, not ε.</li>
    <li>Each step updates only one table (fair coin), so per-step computation is the same order as Q-learning while memory doubles. The two tables see different halves of the data, so one table's lucky upward error is not shared by the critic table.</li>
    <li>A student asked: why only two? Five tables (update one with probability 1/5, evaluate with another) is conceivable — offered as an experiment, not an established method. (Double Q-learning: van Hasselt, 2010.)</li>
  </ul>
</div>
'''),
]

QUIZ = r'''// Chapter 6 — questions from the professor's lectures (Sep 30 – Oct 14).
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
'''

if __name__ == "__main__":
    merge("ch06", BOXES, QUIZ)
