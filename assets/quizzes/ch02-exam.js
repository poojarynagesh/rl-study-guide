// Chapter 2 exam-style (interpretation) questions — appended to the chapter quiz.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "mcq", q: R`A 3-armed bandit uses ε-greedy with sample averages and $Q_1(a)=0$ for all $a$. The log is:
      <div class="tw"><table><tr><th>t</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><th>$A_t$</th><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td></tr><tr><th>$R_t$</th><td>1</td><td>−1</td><td>0</td><td>2</td><td>1</td></tr></table></div>
      On which steps did the random (ε) case <em>definitely</em> occur?`,
      options: ["Steps 2, 3 and 5", "Steps 2 and 3 only", "Step 5 only", "Steps 1 and 4"], answer: 0,
      explain: R`After step 1, $Q=(1,0,0)$, so action 1 is greedy. Step 2 chose 2 ⇒ random; $Q=(1,-1,0)$. Step 3 chose 3 (greedy is 1) ⇒ random; $Q_3=0$. Step 4 chose the greedy action 1 (could be either); $Q_1=1.5$. Step 5 chose 2 (greedy is 1) ⇒ random. Steps 1 and 4 <em>could</em> also have been random draws that landed on a greedy action.` },
    { tag: "exam", type: "num", q: R`UCB with $c=2$ at $t=100$: action 1 has $Q=0$, $N=1$; action 2 has $Q=1$, $N=60$. Compute action 1's UCB score $Q+c\sqrt{\ln t/N}$ (2 decimals).`, answer: 4.29, tol: 0.01,
      explain: R`$0+2\sqrt{4.605/1}=4.29$; action 2 scores $1+2\sqrt{4.605/60}=1.55$. UCB picks the rarely-tried action 1 despite its lower estimate — the uncertainty bonus dominates.` },
    { tag: "exam", type: "num", q: R`Constant $\alpha=0.5$, $Q_1=0$. Rewards $R_1=2$, $R_2=4$ for one arm. What is $Q_3$?`, answer: 2.5, tol: 0.001,
      explain: R`$Q_2=0+0.5(2-0)=1$; $Q_3=1+0.5(4-1)=2.5$. The sample average would give 3 — constant α keeps a bias toward $Q_1$ (weight $0.5^2=0.25$).` },
    { tag: "exam", type: "mcq", q: "A learning curve for optimistic greedy (Q₁ = 5) shows % optimal action jumping up sharply around step 11 and then dropping again. The best interpretation is:",
      options: ["A bug in the averaging over runs", "After every action has been tried about once, the optimal action looks least disappointing and many runs pick it together; picking it lowers its estimate, so they move away", "The step size becomes 1 at step 11", "ε switches on at step 11"], answer: 1,
      explain: "The synchronised early exploration schedule across runs produces the spike and dip (Exercise 2.6)." },
    { tag: "exam", type: "mcq", q: "On a nonstationary bandit, after 10,000 steps the sample-average agent selects the optimal action 43% of the time and the constant-α agent 76%. Why?",
      options: ["Sample averages explore more", "Sample averages give equal weight to old rewards, so with growing n they react ever more slowly to changes; constant α weights recent rewards", "Constant α converges faster to the mean", "The constant-α agent uses UCB"], answer: 1,
      explain: R`$1/n$ is ideal for stationary problems but poor when $q_*$ drifts — this is exactly Exercise 2.5.` },
    { tag: "exam", type: "mcq", q: R`Gradient bandit: action $A_t$ was taken and $R_t$ is <em>below</em> the baseline $\bar R_t$. What happens to the preferences?`,
      options: [R`$H(A_t)$ increases, the others decrease`, R`$H(A_t)$ decreases, the others increase`, "All decrease", "No change"], answer: 1,
      explain: R`$H_{t+1}(a)=H_t(a)+\alpha(R_t-\bar R_t)(\mathbb 1_{a=A_t}-\pi_t(a))$ with a negative error term.` },
  );
})();
