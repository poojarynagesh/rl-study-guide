"""Merge the professor's Chapter-1 lecture content (Aug 3 & 5) into chapters/ch01.html."""
from lecmerge import merge

BOXES = [
    # after the "Common mistake" box in 1.1
    ('<h3>Exploration vs. exploitation</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: the three paradigms by analogy <span class="lec-date">Aug 3</span></span>
  <ul>
    <li><strong>Supervised</strong> — a classroom: the teacher tells the student exactly what is right.</li>
    <li><strong>Unsupervised</strong> — a five-year-old learning to ride a bicycle: nobody tells the child anything; it falls, adjusts and discovers balance on its own.</li>
    <li><strong>Reinforcement</strong> — a mother teaching a baby who cannot understand language: an angry face for cranky behaviour, a chocolate for good behaviour. There <em>is</em> feedback, but it only says how good the behaviour was, never what the right behaviour is.</li>
  </ul>
  <p>The professor's one-line definition: <strong>RL is dynamic decision making under uncertainty.</strong> The reward "will not tell you that this is the best thing you could have done"; the environment only changes its state and lets the agent <em>sense</em> whether its action was good.</p>
</div>
'''),
    ('<h2 id="elements">1.3 Elements of reinforcement learning</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: applications discussed in class <span class="lec-date">Aug 3</span></span>
  <div class="table-wrap"><table>
    <tr><th>Application</th><th>States</th><th>Actions</th><th>Remark</th></tr>
    <tr><td>Traffic-signal control (Bangalore junctions)</td><td>Congestion measured by cameras on each lane</td><td>Green-time of each <em>phase</em> (group of lanes that go green together)</td><td>The professor's own work: ~20–25% less congestion than fixed 60-second timers; road infrastructure limits more</td></tr>
    <tr><td>Self-driving car</td><td>Positions/speeds of nearby vehicles, road conditions</td><td>Change lane, speed up/slow down, turn</td><td>Lane change is hard: safe distance, others' speeds, no collision</td></tr>
    <tr><td>Drone swarm surveillance</td><td>Drone positions, coverage</td><td>Where each drone moves</td><td>"Self-organisation": keep apart (no redundant footage), maximise coverage, relay data</td></tr>
    <tr><td>Healthcare</td><td>Patient's condition and response</td><td>Medicine and dosage</td><td>A robot could handle minor ailments once it knows what state information to watch</td></tr>
    <tr><td>Semiconductor fab</td><td>Demand, machine status</td><td>Which product, which wafer, deposition thickness</td><td>Demand is dynamic</td></tr>
    <tr><td>Networks</td><td>Traffic, battery/solar energy</td><td>Bandwidth per application; energy per sensor node</td><td>Ad hoc wireless sensor networks</td></tr>
    <tr><td>Go / AlphaGo</td><td>Board positions: more than $10^{100}$ states</td><td>Moves</td><td>Too many states to even store a value vector → function approximation (Ch. 9)</td></tr>
  </table></div>
  <p class="small">The professor also cited game playing against Kasparov (1997). Note for accuracy: IBM's Deep Blue relied mainly on search; the classic RL milestone in games is Tesauro's TD-Gammon (backgammon, early 1990s).</p>
</div>
'''),
    ('<h2 id="scope">1.4 Limitations and scope</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: the interaction loop, policies as tables, and data <span class="lec-date">Aug 5</span></span>
  <p><strong>The loop.</strong> At time 0 the environment is in $S_0$; the agent observes it and picks $A_0$. In response <em>two things happen together</em>: the environment moves (randomly, by probabilities the agent may not know) to $S_1$ <em>and</em> gives reward $R_1$. Then the agent picks $A_1$, and so on. States belong to the environment, actions to the agent, rewards are what the environment gives back; in general rewards depend on states and actions.</p>
  <p><strong>Who chooses the policy?</strong> The agent — "nobody gives the agent a policy". It may start from an arbitrary (even random) policy and refine it from data. The environment is <strong>oblivious</strong> to the policy being used.</p>
  <div class="grid-2">
    <div><p><strong>Deterministic policy</strong> $\pi:\mathcal S\to\mathcal A$ — a lookup table. With $\mathcal S=\{1,2,3,4\}$, $\mathcal A=\{A,B\}$:</p>
      <div class="table-wrap"><table><tr><th>state</th><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><th>action</th><td>A</td><td>B</td><td>B</td><td>A</td></tr></table></div>
      <p class="small">"Once you freeze on the policy, the actions get frozen to the state." There are $|\mathcal A|^{|\mathcal S|}=2^4=16$ such tables.</p></div>
    <div><p><strong>Stochastic policy</strong> $\pi(a|s)=P(A_t=a\mid S_t=s)$ — each row sums to 1:</p>
      <div class="table-wrap"><table><tr><th>state</th><th>$\pi(A|s)$</th><th>$\pi(B|s)$</th></tr><tr><td>1</td><td>0.5</td><td>0.5</td></tr><tr><td>2</td><td>0.6</td><td>0.4</td></tr><tr><td>3</td><td>0.3</td><td>0.7</td></tr><tr><td>4</td><td>0.1</td><td>0.9</td></tr></table></div>
      <p class="small">Some rows may be 0/1, but if all are, the policy is deterministic.</p></div>
  </div>
  <p><strong>What the agent actually has.</strong> The model $P(S_{t+1}=s'\mid S_t=s,A_t=a)$ is usually unknown ("with what probability will there be an accident if I turn left? — impossible to tell"). What the agent does have is <strong>data</strong>: tuples $(S_n,A_n,R_{n+1},S_{n+1})$, $n\ge0$. RL asks what sense can be made of this data.</p>
  <p><strong>Preview of the whole course</strong>: fix a policy → find its value function → improve the policy → evaluate again → … converging to an optimal policy. "These are not heuristic methods — they rest on sound theory." With 4 states and 2 actions this takes seconds; with $10^{50}$ states and 1000 actions we must approximate the value function, and then "optimal" means optimal for the approximation architecture — usually still close to the true optimum.</p>
</div>
<div class="box prof">
  <span class="box-title">From the lectures: how the course is organised <span class="lec-date">Aug 3</span></span>
  <div class="table-wrap"><table>
    <tr><th>Block</th><th>Chapters</th><th>Idea</th></tr>
    <tr><td>Model-based</td><td>1–4 (bandits, MDPs, DP)</td><td>The transition probabilities are known — how do we use them to decide under uncertainty?</td></tr>
    <tr><td>Model-free, no approximation</td><td>5 (Monte Carlo), 6 (TD), 7</td><td>Learn values exactly from data. MC is "trajectory-based": wait for the whole episode. TD updates incrementally.</td></tr>
    <tr><td>Model-free with approximation</td><td>9 (and DQN, 2015), 13 (REINFORCE, actor–critic, TRPO, PPO)</td><td>Too many states to estimate each value — approximate. Done properly, little accuracy is lost and much compute is saved.</td></tr>
  </table></div>
  <p class="small">Exploration vs exploitation, introduced through bandits (Ch. 2), is a challenge specific to RL — it does not arise in supervised or unsupervised learning.</p>
</div>
'''),
    ('<h3>What the example shows</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: modelling a two-player game as one agent <span class="lec-date">Aug 5</span></span>
  <p>In chess the state is the board (where each piece is; captured pieces are deleted; pawns of one colour need not be distinguished). Chess is a <strong>two-player</strong> game; to treat it as a single-agent RL problem, assume the opponent plays a fixed strategy and make the opponent <em>part of the environment</em>. Each decision cycle has two moves: the agent moves, the opponent replies, and the agent then sees the <strong>net</strong> board after both — that board is the next state. "The environment is not playing": it responds to the agent's move by changing state and giving a reward. Tic-tac-toe in this section is modelled exactly this way.</p>
</div>
'''),
]

QUIZ = r'''// Chapter 1 — questions from the professor's lectures (Aug 3 & 5).
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
'''

if __name__ == "__main__":
    merge("ch01", BOXES, QUIZ)
