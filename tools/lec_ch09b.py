"""Merge the professor's later Chapter-9 lectures (Oct 26, Oct 28, Nov 2 NN part) into ch09."""
from lecmerge import merge

BOXES = [
    # ---------------- Oct 26 ----------------
    ('<h2 id="ve">', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: how fast state spaces blow up, and what a good approximator needs <span class="lec-date">Oct 26</span></span>
  <ul>
    <li><strong>Exponential growth.</strong> Five routers, each queue taking about 1000 values: $|\mathcal S|\approx1000^5=10^{15}$. Add five more routers and it is $1000^{10}=10^{30}$. The state <em>vector</em> only doubled in length (5 to 10 numbers), but the number of <em>combinations</em> squared. The same happens for traffic networks with many junctions. Tabular TD, SARSA and Q-learning all need one number per state (or state-action pair), so they cannot even be stored.</li>
    <li><strong>The key condition is $d\ll|\mathcal S|$.</strong> Even $d=1000$ weights is fine when $|\mathcal S|$ is $10^{50}$, $10^{70}$ or $10^{100}$. The weights do <em>not</em> depend on the state: a new state only supplies a new feature vector, and the same $\mathbf w$ gives its value instantly. Learning is <em>one</em> optimisation problem for $\mathbf w^*$, not one per state. For control the same idea parameterises $\hat q(s,a,\mathbf w)$ instead of one entry per state-action tuple.</li>
    <li><strong>Trade-off.</strong> Reducing dimension only helps if the class is rich enough that some $\mathbf w$ approximates the relevant value function closely. Too few or poorly chosen features give <em>irreducible</em> approximation error; richer features cut that error but cost more computation and make estimation harder.</li>
  </ul>
</div>
'''),
    ('<h3>9.5.1 Polynomials</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: "linear" means linear in $\mathbf w$; features are designed; why a constant feature; why polynomials are rich <span class="lec-date">Oct 26</span></span>
  <ul>
    <li><strong>Linear in the parameters, not in the state.</strong> $\hat v(s,\mathbf w)=w_1+w_2s_1+w_3s_2+w_4s_1s_2$ is nonlinear in $(s_1,s_2)$ (because of $s_1s_2$) but linear in $(w_1,\dots,w_4)$. Each $x_i(s)$ may be as nonlinear as you like as long as it does not depend on $\mathbf w$. So adding squares or products does <strong>not</strong> make the approximator nonlinear in the sense of this chapter (a recurring student question).</li>
    <li><strong>Features are chosen, the state is given.</strong> The state is the physical description; $\mathbf x(s)$ is a representation you design (emphasise some components, interactions, or regions). There is no theorem telling you the best finite feature set for every task; domain knowledge and experiments guide the choice, then optimisation tunes $\mathbf w$. With raw features $\mathbf x=(s_1,s_2)^\top$ you can only represent a plane through the origin.</li>
    <li><strong>Why include a constant feature.</strong> Drop it and use $\mathbf x=(s_1,s_2,s_1s_2)^\top$: then $\hat v((0,0),\mathbf w)=0$ for <em>every</em> $\mathbf w$. The architecture is forced to give the zero state value 0, although its true value need not be 0 (it could even be the best state). The constant need not be 1, but 1 is conventional and makes $w_1$ the intercept. It must not vary with the state.</li>
    <li><strong>Why polynomials are a rich class (aside, not examinable).</strong> Weierstrass: if $f$ is continuous on a <em>compact</em> interval $[a,b]$, then for every $\epsilon\gt0$ some polynomial $p$ has $\sup_{x\in[a,b]}|f(x)-p(x)|\lt\epsilon$, i.e. polynomials are dense in continuous functions under the uniform norm. Compactness matters: the statement says nothing about the whole real line. Rationals are dense in $\mathbb R$ in the same sense ($\sqrt2$ has a rational within $10^{-10}$), so even polynomials with <em>rational</em> coefficients are dense.</li>
  </ul>
</div>
'''),
    ('<h3>9.5.2 Fourier basis</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: Exercise 9.3 worked out, and what "order $n$" means <span class="lec-date">Oct 26</span></span>
  <p>Write each feature as $x_i(s)=s_1^{c_{i1}}s_2^{c_{i2}}$. Row $i$ is a feature, column $j$ is a state component. For the nine features of Exercise 9.3:</p>
  <div class="table-wrap"><table>
    <tr><th>$i$</th><th>$x_i(s)$</th><th>$c_{i1}$</th><th>$c_{i2}$</th></tr>
    <tr><td>1</td><td>$1$</td><td>0</td><td>0</td></tr>
    <tr><td>2</td><td>$s_1$</td><td>1</td><td>0</td></tr>
    <tr><td>3</td><td>$s_2$</td><td>0</td><td>1</td></tr>
    <tr><td>4</td><td>$s_1s_2$</td><td>1</td><td>1</td></tr>
    <tr><td>5</td><td>$s_1^2$</td><td>2</td><td>0</td></tr>
    <tr><td>6</td><td>$s_2^2$</td><td>0</td><td>2</td></tr>
    <tr><td>7</td><td>$s_1s_2^2$</td><td>1</td><td>2</td></tr>
    <tr><td>8</td><td>$s_1^2s_2$</td><td>2</td><td>1</td></tr>
    <tr><td>9</td><td>$s_1^2s_2^2$</td><td>2</td><td>2</td></tr>
  </table></div>
  <ul>
    <li>Solve one row at a time: $s_1^{c_{11}}s_2^{c_{12}}=1\Rightarrow c_{11}=c_{12}=0$; $s_1^{c_{21}}s_2^{c_{22}}=s_1\Rightarrow(c_{21},c_{22})=(1,0)$; $s_1^{c_{91}}s_2^{c_{92}}=s_1^2s_2^2\Rightarrow(2,2)$. Take care with the mixed terms: $s_1^2s_2$ is "square the first, times the second" (row 8), $s_1s_2^2$ the other way round (row 7).</li>
    <li>The largest exponent is 2, so $n=2$ and $k=2$. <strong>Trap (a student made it)</strong>: $n=9$ because "there are nine features". No: nine is the <em>count</em> $(n+1)^k=3^2$; $n$ is the largest allowed exponent.</li>
    <li><strong>Convention warning.</strong> Here "order $n$" bounds <em>each exponent</em> by $n$, so total degree can reach $kn$. Many other texts mean "total degree $\le n$": for $k=2,n=2$ that would be only 6 features ($1,s_1,s_2,s_1^2,s_1s_2,s_2^2$), not 9. Use the book's/lecture's definition in this course.</li>
    <li>Nothing stops you going beyond 2 ($s_1^3$, $s_1^3s_2^2,\dots$); the lecture stopped at 2 only to keep the example small. The count grows as $(n+1)^k$: for $k=4$, $n=3$ it is already $4^4=256$.</li>
  </ul>
</div>
'''),
    ('<h3>9.5.3 Coarse coding</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: reading the Fourier feature formula <span class="lec-date">Oct 26</span></span>
  <ul>
    <li>Use Fourier features when the value function has periodic or repeating structure. States are scaled to $s_j\in[0,1]$, and the feature is $x_i(\mathbf s)=\cos(\pi\,\mathbf s^\top\mathbf c^i)$ with $c^i_j\in\{0,\dots,n\}$, so there are $(n+1)^k$ coefficient vectors.</li>
    <li>$c^i_j$ is the <strong>frequency along dimension $j$</strong>: 0 means no variation in that direction, larger values oscillate faster. Example $k=2$, $n=1$: the four vectors $(0,0),(0,1),(1,0),(1,1)$ give $1,\ \cos(\pi s_2),\ \cos(\pi s_1),\ \cos(\pi(s_1+s_2))$. The all-zero vector is the constant (bias) feature, just as the all-zero exponent vector gave $1$ in the polynomial basis.</li>
    <li>The professor only introduced the formula in this class and deferred a worked Fourier example.</li>
  </ul>
</div>
'''),
    # ---------------- Oct 28 ----------------
    ('<p>In practice $v_\pi(S_t)$ is unknown; substitute a target $U_t$:</p>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: deriving the update step by step, and why the exact gradient is not implementable <span class="lec-date">Oct 28</span></span>
  <ul>
    <li><strong>Derivation.</strong> Because the state space is finite, the gradient moves inside the sum (an infinite sum or integral would need a limit theorem). Chain rule: $\nabla\overline{\mathrm{VE}}=-2\sum_s\mu(s)[v_\pi(s)-\hat v(s,\mathbf w)]\nabla\hat v(s,\mathbf w)$. The minus sign comes from differentiating $-\hat v$, the 2 from the square. Descent with step $\alpha/2$ absorbs the 2: $\mathbf w_{t+1}=\mathbf w_t+\alpha\sum_s\mu(s)[v_\pi(s)-\hat v(s,\mathbf w_t)]\nabla\hat v(s,\mathbf w_t)$. The lecture assumed $\mu(s)\gt0$ for every $s$.</li>
    <li><strong>Global vs local.</strong> For nonlinear $\hat v$ the objective need not be convex, so one settles for a stationary point $\nabla\overline{\mathrm{VE}}(\mathbf w^*)=0$ (a positive-definite Hessian there is sufficient for a strict local minimum). Convex means every local minimum is global, but convexity depends on the parameterisation.</li>
    <li><strong>Three obstacles</strong> to running this exactly: (1) the sum over all states is enormous; (2) $\mu$ is unknown (it depends on the unknown transition probabilities under $\pi$); (3) $v_\pi(s)$ is unknown, since estimating it is the whole problem. <em>Not</em> an obstacle: a "too high learning rate" ($\alpha$ is ours to choose and shrink). Also, $\mu$ is a property of the Markov chain (environment plus policy); it is <strong>not</strong> produced by $\mathbf w$.</li>
    <li><strong>Fixes.</strong> (1)+(2): sample the visited state $S_t$; in steady state it has distribution $\mu$, so $\mathbb E_\mu[f(S_t)]=\sum_s\mu(s)f(s)$ and the sampled step has the right expected direction without knowing $\mu$ or summing over $\mathcal S$ (stochastic approximation). (3): $v_\pi(S_t)=\mathbb E_\pi[G_t\mid S_t]$, so replace it by the observed return $G_t$, an unbiased sample target. The result is gradient Monte Carlo: "gradient" because derived from $\overline{\mathrm{VE}}$, "Monte Carlo" because it uses the full sampled return.</li>
    <li><strong>No explicit averaging needed.</strong> You do not generate many trajectories, average returns, then optimise: the repeated small updates average implicitly, and under the usual step-size conditions converge almost surely to a stationary point. Limitation: $G_t$ is known only after the episode ends, which motivates bootstrapping.</li>
  </ul>
</div>
'''),
    ('<p><strong>State aggregation</strong>: group states', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: why "semi"-gradient, and the $\mathbf w_t$ versus $\mathbf w_{t+1}$ correction <span class="lec-date">Oct 28</span></span>
  <ul>
    <li><strong>TD target and error.</strong> Since $v_\pi(S_{t+1})$ is unknown, bootstrap: $U_t=R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)$, $\delta_t=U_t-\hat v(S_t,\mathbf w_t)$, and $\mathbf w_{t+1}=\mathbf w_t+\alpha\delta_t\nabla\hat v(S_t,\mathbf w_t)$.</li>
    <li><strong>Why "semi".</strong> Differentiate $\tfrac12\delta_t^2$ literally and you must also differentiate $\hat v(S_{t+1},\mathbf w)$ inside the target, since it depends on $\mathbf w$. Semi-gradient TD treats the target as a fixed number and differentiates only $\hat v(S_t,\mathbf w)$. So it is <strong>not</strong> the true gradient of the squared bootstrapped error.</li>
    <li><strong>A slip the professor corrected live.</strong> Both value estimates use the <em>current</em> weights $\mathbf w_t$. Writing $\hat v(S_{t+1},\mathbf w_{t+1})$ in the target would make the update implicit: $\mathbf w_{t+1}$ would appear on both sides, and it is the very quantity being computed.</li>
    <li><strong>Fully incremental.</strong> As soon as $(S_t,A_t,R_{t+1},S_{t+1})$ is seen the update can be done; no return and no end of episode are needed.</li>
    <li><strong>Terminal-state constraint $\hat v(S_T,\mathbf w)=0$ for all $\mathbf w$</strong> mirrors the true episodic value (no reward after termination). With a linear $\hat v$ and $\mathbf w=\mathbf 0$ every state starts at value 0, and each later update changes all predictions through the shared weights.</li>
  </ul>
</div>
'''),
    ('<h3>The TD fixed point</h3>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: linear semi-gradient TD, with a dimension check <span class="lec-date">Oct 28</span></span>
  <ul>
    <li>For $\hat v=\mathbf w^\top\mathbf x(s)=\sum_iw_ix_i(s)$, $\partial\hat v/\partial w_i=x_i(s)$, hence $\nabla\hat v=\mathbf x(s)$. With $\mathbf x_t=\mathbf x(S_t)$: $\mathbf w_{t+1}=\mathbf w_t+\alpha\,\mathbf x_t\,[R_{t+1}+\gamma\mathbf x_{t+1}^\top\mathbf w_t-\mathbf x_t^\top\mathbf w_t]$. The bracket is a <em>scalar</em>, $\mathbf x_t$ is $d$-dimensional, so the increment has the dimension of $\mathbf w$.</li>
    <li>Expanding and factoring $\mathbf w_t$ out: $R_{t+1}\mathbf x_t\in\mathbb R^d$, and $\mathbf x_t(\mathbf x_t-\gamma\mathbf x_{t+1})^\top$ is a column times a row, a $d\times d$ matrix; times $\mathbf w_t$ it is again a vector in $\mathbb R^d$. This is exactly the form (9.9) below.</li>
  </ul>
</div>
'''),
    ('<details class="card" style="margin:14px 0"><summary style="cursor:pointer;font-weight:650">Why it converges', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: reading $\mathbf A\mathbf w=\mathbf b$ <span class="lec-date">Oct 28</span></span>
  <ul>
    <li>The expectations in $\mathbf A$ and $\mathbf b$ are over the steady-state trajectory under $\pi$ (including transition and reward randomness). The expected update direction is $\mathbf b-\mathbf A\mathbf w$; at equilibrium it vanishes, so $\mathbf A\mathbf w=\mathbf b$ and $\mathbf w_{TD}=\mathbf A^{-1}\mathbf b$ if $\mathbf A$ is invertible.</li>
    <li><strong>The algorithm never forms $\mathbf A$, $\mathbf b$ or $\mathbf A^{-1}$.</strong> Each transition is a noisy sample of the mean update; stochastic approximation drifts to the same fixed point. Only if the model and $\mu$ were known could you compute them directly.</li>
    <li><strong>Terminology.</strong> The lecture called $\mathbf A$ "positive definite", explained as eigenvalues with positive real part, none zero. For a possibly non-symmetric matrix the precise name is <em>positive stable</em>; "positive definite" ($\mathbf z^\top\mathbf A\mathbf z\gt0$) is usually reserved for symmetric matrices. The proof sketch below uses the quadratic-form version.</li>
    <li><strong>One-feature sanity check</strong> (our own, not from the lecture): a single state that loops to itself with reward $r$ and one feature $x=1$ gives $\mathbf A=1-\gamma$, $\mathbf b=r$, so $w_{TD}=r/(1-\gamma)$, the true value of that state. With $r=2$, $\gamma=0.9$: $w_{TD}=20$.</li>
  </ul>
</div>
'''),
    ('<div class="box key"><span class="box-title">TD vs MC with function approximation</span>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: the assumptions behind these results, and the feature matrix $X$ <span class="lec-date">Oct 28</span></span>
  <ul>
    <li><strong>Markov-chain assumptions.</strong> A state is <em>transient</em> (return probability $\lt1$), <em>null recurrent</em> (returns w.p. 1 but with infinite expected return time) or <em>positive recurrent</em> (returns w.p. 1 with $\mathbb E_s[\tau_s^+]\lt\infty$, where $\tau_s^+=\inf\{t\ge1:S_t=s\}$). For an irreducible positive-recurrent chain the stationary distribution is $\mu(s)=1/\mathbb E_s[\tau_s^+]\gt0$ for every $s$, which is the lecture's assumption $\mu(s)\gt0$. (Positive recurrence of one class does not give positive mass everywhere on a reducible chain; irreducibility or restriction to the recurrent class supplies it.)</li>
    <li><strong>Feature matrix.</strong> Enumerate the states and stack the feature vectors as rows: $X\in\mathbb R^{|\mathcal S|\times d}$, row $s$ = $\mathbf x(s)^\top$. Columns are the <em>basis functions</em> (feature $j$ evaluated at every state), and since $d\ll|\mathcal S|$ the matrix is <strong>tall</strong>.</li>
    <li>Assume the columns are linearly independent: $\sum_ja_jX_{:j}=\mathbf 0\Rightarrow$ all $a_j=0$, i.e. $\operatorname{rank}X=d$ (full column rank). A dependent feature is a combination of others and adds no new direction. Being tall makes this plausible, but it is an assumption to check, not a consequence of the shape. It is the $X$ in $\mathbf A=X^\top D(I-\gamma P)X$ above.</li>
  </ul>
</div>
'''),
    # ---------------- Nov 2 (NN part) ----------------
    ('<div class="box exam"><span class="box-title">Exercises 9.7 and 9.8', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: a single-hidden-layer value network and what the activation must satisfy <span class="lec-date">Nov 2</span></span>
  <ul>
    <li><strong>Building the network.</strong> Feature vector $x(i)=(x_1(i),\dots,x_d(i))$. First linear layer: $\sum_{l=1}^dw_{kl}x_l(i)$ for $k=1,\dots,K$ ($d$ inputs, $K$ outputs). Hidden layer: apply $\sigma$ to each. Second linear layer aggregates:
      $$\hat v\big(x(i),\mathbf w\big)=\sum_{k=1}^{K}w_k\,\sigma\Big(\sum_{l=1}^{d}w_{kl}\,x_l(i)\Big).$$
      $\mathbf w$ stacks all $w_k$ and all $w_{kl}$: $Kd+K=K(d+1)$ numbers in this bias-free form (e.g. $d=4$, $K=10$ gives 50). A network with hundreds to a few thousand parameters is typical.</li>
    <li><strong>One network, not one per state.</strong> A new state only gives a new $x$; the weights are the same. Training (say on a long episode) is done once; then any state's value is a forward pass. The target is $v_\pi$ for a fixed $\pi$.</li>
    <li><strong>Requirements on $\sigma$</strong>: differentiable, monotonically increasing, and bounded: $-\infty\lt\lim_{\xi\to-\infty}\sigma(\xi)\lt\lim_{\xi\to+\infty}\sigma(\xi)\lt\infty$.
      <div class="table-wrap"><table>
        <tr><th>Function</th><th>Formula</th><th>Range / behaviour</th></tr>
        <tr><td>tanh</td><td>$\frac{e^{\xi}-e^{-\xi}}{e^{\xi}+e^{-\xi}}$</td><td>$(-1,1)$, symmetric, $\tanh0=0$</td></tr>
        <tr><td>Sigmoid (logistic)</td><td>$\frac1{1+e^{-\xi}}$</td><td>$(0,1)$, never negative, $\sigma(0)=\tfrac12$</td></tr>
        <tr><td>ReLU</td><td>$\max(0,\xi)$</td><td>0 for $\xi\lt0$, 45&deg; line for $\xi\gt0$; used in deep nets</td></tr>
      </table></div></li>
    <li><strong>Problems with raw ReLU</strong> (as discussed): (1) not differentiable at 0: left derivative 0, right derivative 1, so the derivative jumps; (2) unbounded as $\xi\to\infty$. Remedies are to smooth the kink (e.g. the GELU, a Gaussian-smoothed ReLU, mentioned as an aside). Differentiability matters because the TD update needs $\nabla_{\mathbf w}\hat v$ via the chain rule, so the professor would not use the raw ReLU directly. (In practice libraries simply assign a derivative at 0; that is an aside of ours.)</li>
  </ul>
</div>
'''),
    ('<h2 id="lstd">9.8 Least-squares TD</h2>', 'before', r'''<div class="box prof">
  <span class="box-title">From the lectures: TD with a network, and deeper architectures as design choices <span class="lec-date">Nov 2</span></span>
  <ul>
    <li><strong>TD update on network weights</strong> (same semi-gradient rule as before): $\mathbf w_{t+1}=\mathbf w_t+\alpha[R_{t+1}+\gamma\hat v(X_{t+1},\mathbf w_t)-\hat v(X_t,\mathbf w_t)]\nabla_{\mathbf w}\hat v(X_t,\mathbf w_t)$. For fixed $\mathbf w_t$ the network values both $X_t$ and $X_{t+1}$ (so you must know the next state); only the gradient $\nabla_{\mathbf w}\hat v(X_t,\mathbf w_t)$ requires the chain rule through the layers, which is why $\sigma$ must be (continuously) differentiable. The only change from the linear case is that $\nabla\hat v$ is no longer simply $\mathbf x$.</li>
    <li><strong>Going deeper.</strong> Stack more nonlinear layers ($\sigma$ of $\sigma$ of $\dots$), possibly with different activations $\sigma_1,\sigma_2,\dots$ per layer; add more linear layers (a matrix mapping $K$ inputs to $P$ outputs), then another nonlinearity, and finally a linear aggregation layer.</li>
    <li><strong>All of this is design</strong>: how many layers, how many units per layer, which activations. These are hyperparameters, not learned. (Using networks to represent <em>policies</em> was explicitly postponed.)</li>
  </ul>
</div>
'''),
]

QUIZ = r'''// Chapter 9 — questions from the professor's lectures (Oct 21, 26, 28, Nov 2).
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
      explain: "The true value function may lie outside the chosen function class (representation error), but approximate solutions often give very good policies in practice." },

    // ---- Oct 26 ----
    { tag: "lecture", type: "num", q: "A network has five routers with about 1000 queue values each. Doubling to ten routers makes the number of states $10^x$. What is $x$?", answer: 30, tol: 0,
      explain: R`$1000^{10}=10^{30}$ (five routers gave $10^{15}$). The state vector only doubled in length, but the number of combinations was squared.` },
    { tag: "lecture", type: "tf", q: R`$\hat v(s,\mathbf w)=w_1+w_2s_1+w_3s_2+w_4s_1s_2$ is a nonlinear function approximator, because it contains the product $s_1s_2$.`, answer: false,
      explain: R`"Linear" refers to the weights: the expression is linear in $(w_1,\dots,w_4)$. It is nonlinear only as a function of the state, which is allowed for linear function approximation.` },
    { tag: "lecture", type: "mcq", q: R`A designer uses $\mathbf x(s)=(s_1,s_2,s_1s_2)^\top$ with no constant feature. What is guaranteed?`,
      options: [R`$\hat v$ is a plane through the origin`, R`$\hat v((0,0),\mathbf w)=0$ for every $\mathbf w$, even if the true value of that state is not 0`, "The weights cannot be learned by gradient methods", "The approximation is exact"], answer: 1,
      explain: R`Every feature vanishes at $(0,0)$, so the output is 0 whatever $\mathbf w$ is. A constant feature (usually 1) adds an intercept that removes this restriction.` },
    { tag: "lecture", type: "mcq", q: "Which statement of the Weierstrass approximation theorem, as given in the lecture, is correct?",
      options: ["Any function on the real line is a limit of polynomials", R`A continuous function on a compact interval can be approximated within any $\epsilon\gt0$ in sup-norm by some polynomial`, "Polynomials of degree at most 2 approximate any function exactly", "Only differentiable functions can be approximated by polynomials"], answer: 1,
      explain: "Continuity and a compact domain are both part of the theorem; it says nothing about the whole real line. Higher degree may be needed as ε shrinks." },
    { tag: "lecture", type: "num", q: R`Polynomial basis (order $n$ bounds each exponent), $k=3$ state components, $n=2$. How many features?`, answer: 27, tol: 0,
      explain: R`Each of the $k$ exponents takes $n+1$ values: $(n+1)^k=3^3=27$.` },
    { tag: "lecture", type: "num", q: R`Polynomial basis with $k=4$ state components and $n=3$. How many features?`, answer: 256, tol: 0,
      explain: R`$(n+1)^k=4^4=256$. This exponential growth in $k$ is why the full basis is usually pruned.` },
    { tag: "lecture", type: "num", q: R`The "total degree at most $n$" convention would give how many features for $k=2$, $n=2$? (The lecture's per-exponent convention gives 9.)`, answer: 6, tol: 0,
      explain: R`Monomials $1,s_1,s_2,s_1^2,s_1s_2,s_2^2$. The terms $s_1^2s_2,\ s_1s_2^2,\ s_1^2s_2^2$ (degree 3 or 4) are excluded. Always check which definition of "order" is being used.` },
    { tag: "lecture", type: "mcq", q: R`Exercise 9.3's feature vector $(1,s_1,s_2,s_1s_2,s_1^2,s_2^2,s_1s_2^2,s_1^2s_2,s_1^2s_2^2)$ has nine components. A student says $n=9$. What are the correct $n$ and the exponent pair $(c_{81},c_{82})$ of the 8th feature $s_1^2s_2$?`,
      options: [R`$n=9$, $(c_{81},c_{82})=(2,1)$`, R`$n=2$, $(c_{81},c_{82})=(2,1)$`, R`$n=2$, $(c_{81},c_{82})=(1,2)$`, R`$n=3$, $(c_{81},c_{82})=(2,1)$`], answer: 1,
      explain: R`$n$ is the largest exponent (2), not the number of features (nine is $(n+1)^k=3^2$). The 8th feature is $s_1^{2}s_2^{1}$, so $(2,1)$; the 7th, $s_1s_2^2$, is $(1,2)$.` },
    { tag: "lecture", type: "num", q: R`Fourier cosine basis of order $n=4$ on $k=2$ state dimensions. How many coefficient vectors $\mathbf c^i$ (features)?`, answer: 25, tol: 0,
      explain: R`$c^i_j\in\{0,\dots,4\}$ for each of 2 dimensions: $(n+1)^k=5^2=25$.` },
    { tag: "lecture", type: "mcq", q: R`In the Fourier feature $x_i(\mathbf s)=\cos(\pi\,\mathbf s^\top\mathbf c^i)$ with $\mathbf c^i=(0,3)$, what does the feature do?`,
      options: [R`It equals $\cos(3\pi s_2)$: constant along $s_1$, oscillating fast along $s_2$`, R`It equals $\cos(3\pi s_1)$`, "It is the constant feature 1", R`It equals $\cos(\pi s_1)\cos(\pi s_2)$`], answer: 0,
      explain: R`$\mathbf s^\top\mathbf c^i=0\cdot s_1+3s_2$. A 0 entry means no variation along that dimension; larger entries mean higher frequency. Only $\mathbf c=\mathbf 0$ gives the constant feature.` },

    // ---- Oct 28 ----
    { tag: "lecture", type: "mcq", q: R`Which is NOT one of the obstacles to running exact gradient descent on $\overline{\mathrm{VE}}$ model-free?`,
      options: ["The sum over all states is enormous", R`The stationary distribution $\mu$ is unknown`, R`The true value $v_\pi(s)$ is unknown`, R`The learning rate $\alpha$ is necessarily too large`], answer: 3,
      explain: R`$\alpha$ is chosen by the designer and can be reduced. The real obstacles are the huge state sum, the unknown $\mu$ and the unknown $v_\pi$.` },
    { tag: "lecture", type: "tf", q: R`The state distribution $\mu(s)$ in $\overline{\mathrm{VE}}$ is determined by the value-function weights $\mathbf w$.`, answer: false,
      explain: R`$\mu$ is a property of the Markov chain induced by the environment and the policy $\pi$; it does not depend on $\mathbf w$.` },
    { tag: "lecture", type: "tf", q: R`In gradient Monte Carlo, $G_t$ is an unbiased sample of $v_\pi(S_t)$, so the sampled update has the same expected direction as the exact gradient step (visiting states in proportion to $\mu$).`, answer: true,
      explain: R`$\mathbb E[G_t\mid S_t=s]=v_\pi(s)$, and in steady state $S_t\sim\mu$. Repeated updates average implicitly; no separate averaging of trajectories is needed.` },
    { tag: "lecture", type: "mcq", q: R`Why is semi-gradient TD(0) called "semi"-gradient?`,
      options: ["It uses half the step size", R`It differentiates $\hat v(S_t,\mathbf w)$ but treats the bootstrapped target $R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w)$ as a constant, ignoring its dependence on $\mathbf w$`, "It only updates half of the weights", "It averages the MC return and the TD target"], answer: 1,
      explain: "The full gradient of the squared TD error would also differentiate through the next-state estimate; semi-gradient omits that term." },
    { tag: "lecture", type: "mcq", q: R`The implementable one-step update computes the target with which weights?`,
      options: [R`$\mathbf w_t$ for both $\hat v(S_t,\cdot)$ and $\hat v(S_{t+1},\cdot)$`, R`$\mathbf w_{t+1}$ for $\hat v(S_{t+1},\cdot)$`, R`$\mathbf w_0$`, "Random weights"], answer: 0,
      explain: R`Using $\mathbf w_{t+1}$ on the right would make the equation implicit, because $\mathbf w_{t+1}$ is the unknown being computed.` },
    { tag: "lecture", type: "num", q: R`Linear semi-gradient TD: $\mathbf w=(0.5,\,1)$, $\mathbf x_t=(1,\,2)$, $\mathbf x_{t+1}=(1,\,0)$, $R_{t+1}=1$, $\gamma=0.9$, $\alpha=0.1$. What is the new second weight $w_2$? (2 decimals)`, answer: 0.79, tol: 0.005,
      explain: R`$\hat v(S_t)=0.5+2=2.5$, $\hat v(S_{t+1})=0.5$. $\delta=1+0.9(0.5)-2.5=-1.05$. $\Delta\mathbf w=0.1(-1.05)(1,2)=(-0.105,-0.21)$, so $w_2=1-0.21=0.79$ (and $w_1=0.395$).` },
    { tag: "lecture", type: "num", q: R`A single state loops to itself with reward $r=2$ each step, $\gamma=0.9$, one feature $x=1$. What is the TD fixed point $w_{TD}=\mathbf A^{-1}\mathbf b$?`, answer: 20, tol: 0.001,
      explain: R`$\mathbf A=\mathbb E[x(x-\gamma x)]=1-0.9=0.1$, $\mathbf b=\mathbb E[Rx]=2$, so $w_{TD}=2/0.1=20=r/(1-\gamma)$, the true value.` },
    { tag: "lecture", type: "mcq", q: R`With $d$ features, what is the shape of $\mathbf x_t(\mathbf x_t-\gamma\mathbf x_{t+1})^\top$ in the linear TD update?`,
      options: [R`$1\times1$`, R`$d\times1$`, R`$d\times d$`, R`$|\mathcal S|\times d$`], answer: 2,
      explain: R`A $d\times1$ column times a $1\times d$ row is a $d\times d$ matrix. Multiplying by $\mathbf w_t\in\mathbb R^d$ gives a vector in $\mathbb R^d$, the same shape as $R_{t+1}\mathbf x_t$.` },
    { tag: "lecture", type: "tf", q: R`The linear-TD algorithm computes $\mathbf A^{-1}\mathbf b$ explicitly at each step.`, answer: false,
      explain: R`Each transition gives a noisy sample of the mean update; stochastic approximation converges to $\mathbf w_{TD}$ without ever forming $\mathbf A$, $\mathbf b$ or $\mathbf A^{-1}$.` },
    { tag: "lecture", type: "mcq", q: R`$\mathbf A$ is not symmetric in general. What is the precise term for "all eigenvalues have strictly positive real part"?`,
      options: ["Positive semi-definite", "Positive stable", "Orthogonal", "Idempotent"], answer: 1,
      explain: R`Positive definiteness ($\mathbf z^\top\mathbf A\mathbf z\gt0$) is the quadratic-form notion, mainly for symmetric matrices; "positive stable" is the eigenvalue statement.` },
    { tag: "lecture", type: "mcq", q: R`The feature matrix $X$ has one row per state and one column per feature. If $d\ll|\mathcal S|$ and the features are linearly independent, which is true?`,
      options: [R`$X$ is wide with rank $|\mathcal S|$`, R`$X$ is tall ($|\mathcal S|\times d$) with rank $d$ (full column rank)`, R`$X$ is square`, R`$X$ has rank 1`], answer: 1,
      explain: "Independent columns mean the only combination giving the zero vector is trivial: rank = d. The tall shape makes this plausible but it is still an assumption to verify." },
    { tag: "lecture", type: "mcq", q: R`For an irreducible positive-recurrent chain, the stationary probability of state $s$ is $\mu(s)=$`,
      options: [R`$\mathbb E_s[\tau_s^+]$`, R`$1/\mathbb E_s[\tau_s^+]$, which is strictly positive`, R`$\Pr_s(\tau_s^+\lt\infty)$`, "0 for transient states and 1 otherwise"], answer: 1,
      explain: R`Positive recurrence means a finite expected return time, so its reciprocal is positive: every state has $\mu(s)\gt0$, the lecture's assumption.` },

    // ---- Nov 2 (neural-network approximation) ----
    { tag: "lecture", type: "num", q: R`A bias-free single-hidden-layer network $\hat v=\sum_{k=1}^Kw_k\sigma(\sum_{l=1}^dw_{kl}x_l)$ has $d=4$ inputs and $K=10$ hidden units. How many parameters?`, answer: 50, tol: 0,
      explain: R`First layer $Kd=40$ weights $w_{kl}$, second layer $K=10$ weights $w_k$: $K(d+1)=50$.` },
    { tag: "lecture", type: "mcq", q: "After training a value network on a long episode, how is the value of a new state obtained?",
      options: ["Re-run the optimisation for that state", "Compute its feature vector and do a forward pass with the same weights", "Look it up in a table", "Average the values of neighbouring states"], answer: 1,
      explain: "There is one network for all states; the weights do not depend on the state. Optimisation is done once, not per state." },
    { tag: "lecture", type: "mcq", q: R`Which set of properties did the lecture require of the activation $\sigma$?`,
      options: ["Differentiable, monotonically increasing, bounded", "Unbounded and linear", "Periodic and non-differentiable", "Decreasing and bounded"], answer: 0,
      explain: R`Differentiability is needed for the chain rule in $\nabla_{\mathbf w}\hat v$; monotone and bounded (finite limits at $\pm\infty$) hold for sigmoid and tanh.` },
    { tag: "lecture", type: "mcq", q: "Which activation takes only values in (0, 1), has σ(0) = 1/2, and is used as the standard example hidden unit?",
      options: ["tanh", "ReLU", "Logistic sigmoid", "Identity"], answer: 2,
      explain: R`$\sigma(\xi)=1/(1+e^{-\xi})$. tanh ranges in $(-1,1)$ with $\tanh0=0$; ReLU is $\max(0,\xi)$.` },
    { tag: "lecture", type: "tf", q: "The two problems the lecture raised with the raw ReLU were that it is not differentiable at 0 (left derivative 0, right derivative 1) and that it is unbounded as ξ → ∞.", answer: true,
      explain: "A smoothed variant such as GELU was mentioned as a remedy. Differentiability matters because the TD update on network weights needs the gradient of the network output." }
  );
})();
'''

merge("ch09", BOXES, QUIZ)
