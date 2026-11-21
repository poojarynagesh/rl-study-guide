// Chapter 13 exam-style questions.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`Softmax with linear preferences, 2 actions, $\mathbf x(s,a_1)=(1,0)$, $\mathbf x(s,a_2)=(0,1)$, $\boldsymbol\theta=(0,0)$. Action $a_1$ is taken and $G_t=10$ ($\gamma=1$, $\alpha=0.2$). What is the new $\theta_1$ after one REINFORCE step?`, answer: 1, tol: 0.001,
      explain: R`$\pi=(0.5,0.5)$; $\nabla\ln\pi(a_1)=(1,0)-(0.5,0.5)=(0.5,-0.5)$; $\Delta\boldsymbol\theta=0.2\cdot10\cdot(0.5,-0.5)=(1,-1)$, so $\theta_1=1$.` },
    { tag: "exam", type: "num", q: R`Continue the previous question: after the update $\boldsymbol\theta=(1,-1)$. What is the new $\pi(a_1)$? (3 decimals)`, answer: 0.881, tol: 0.001,
      explain: R`$\pi(a_1)=\frac{e^{1}}{e^{1}+e^{-1}}=\frac{1}{1+e^{-2}}\approx0.8808$ (up from 0.5).` },
    { tag: "exam", type: "num", q: R`Sigmoid policy $\pi(A_1)=\sigma(\theta)$, $\pi(A_2)=1-\sigma(\theta)$, $\theta=0$. $A_1$ is taken, $G_t=4$, baseline $b=3$, $\alpha=0.5$ ($\gamma=1$). What is $\Delta\theta$?`, answer: 0.25, tol: 0.001,
      explain: R`$\nabla\ln\pi(A_1)=1-\sigma(0)=0.5$; $\Delta\theta=0.5\cdot(4-3)\cdot0.5=0.25$.` },
    { tag: "exam", type: "mcq", q: R`Same sigmoid policy ($\pi(A_2)=1-\sigma(\theta)$). Action $A_2$ is taken and $G_t-b=+2$. What happens to $\theta$ and to $\pi(A_2)$?`,
      options: [R`$\theta$ increases; $\pi(A_2)$ decreases`, R`$\theta$ decreases; $\pi(A_2)$ increases`, R`$\theta$ increases; $\pi(A_2)$ increases`, "Nothing changes in expectation, so no change"], answer: 1,
      explain: R`$\nabla\ln\pi(A_2)=-\sigma(\theta)<0$, so a positive advantage gives $\Delta\theta<0$, which lowers $\sigma(\theta)=\pi(A_1)$ and raises $\pi(A_2)$.` },
    { tag: "exam", type: "num", q: R`In the switched-action short corridor, $J(p)=-\dfrac{2(2-p)}{p(1-p)}$ for $\Pr(\text{right})=p$. What is $J(0.5)$?`, answer: -12, tol: 0.01,
      explain: R`$-2(1.5)/(0.25)=-12$ — already close to the optimum $-11.66$ at $p=2-\sqrt2\approx0.586$.` },
    { tag: "exam", type: "mcq", q: "In the short corridor, J(p) → −∞ as p → 0 or p → 1. What does this say about near-deterministic policies?",
      options: ["They are optimal", "They get stuck in the reversed state (or the first state), so a deterministic policy is terrible and a stochastic mixture is needed", "They need more exploration only at the start", "They are only bad for ε-greedy"], answer: 1,
      explain: "A deterministic choice in the reversed state bounces back and forth forever; only an intermediate p escapes quickly." },
    { tag: "exam", type: "num", q: R`Tabular one-step actor–critic: $\mathbf w=(5,8)$ for states $S_1,S_2$; transition $S_1\to S_2$ with $R=4$, $\gamma=0.9$. Critic step $\beta=0.1$. What is $w_1$ after the update?`, answer: 5.62, tol: 0.001,
      explain: R`$\delta=4+0.9\cdot8-5=6.2$; $w_1\leftarrow5+0.1\cdot6.2=5.62$; $w_2$ unchanged.` },
    { tag: "exam", type: "num", q: R`Same transition. The actor is a sigmoid policy at $\theta=0$ that took $A_1$; actor step $0.05$, $I=1$. What is $\Delta\theta$ using the same $\delta=6.2$?`, answer: 0.155, tol: 0.001,
      explain: R`$\Delta\theta=\alpha\,I\,\delta\,\nabla\ln\pi(A_1)=0.05\cdot1\cdot6.2\cdot0.5=0.155$.` },
    { tag: "exam", type: "num", q: R`Step-size schedules $\alpha_t=1/(t+1)$ and $\beta_t=1/(t+1)^{0.7}$. What is $\alpha_t/\beta_t$ at $t+1=10^5$? (3 decimals)`, answer: 0.032, tol: 0.001,
      explain: R`$(t+1)^{0.7-1}=(10^5)^{-0.3}=10^{-1.5}\approx0.0316$ — it tends to 0, as the two-time-scale condition requires.` },
    { tag: "exam", type: "num", q: R`Gaussian policy with scalar features $x_\mu=1$, $\mu=0$, $\sigma=2$. The action $a=3$ is sampled and the (advantage) signal is $\delta=2$. With $\alpha=0.1$, what is $\Delta\theta_\mu$?`, answer: 0.15, tol: 0.001,
      explain: R`$\nabla_{\theta_\mu}\ln\pi=(a-\mu)/\sigma^2\cdot x_\mu=3/4=0.75$; $\Delta\theta_\mu=0.1\cdot2\cdot0.75=0.15$.` },
    { tag: "exam", type: "num", q: R`Same Gaussian policy with $\sigma=\exp(\theta_\sigma x_\sigma)$, $x_\sigma=1$. What is $\Delta\theta_\sigma$ (same $a=3$, $\delta=2$, $\alpha=0.1$)?`, answer: 0.25, tol: 0.001,
      explain: R`$\nabla_{\theta_\sigma}\ln\pi=\big(\frac{(a-\mu)^2}{\sigma^2}-1\big)x_\sigma=\frac94-1=1.25$; $\Delta\theta_\sigma=0.1\cdot2\cdot1.25=0.25$. The sample was beyond one σ and did well ⇒ σ grows.` },
    { tag: "exam", type: "mcq", q: "Two learning curves on the same task: REINFORCE (no baseline) is very noisy and slow; adding a state-value baseline makes it learn much faster with the same expected update. Why?",
      options: ["The baseline adds bias that helps", "The baseline does not change the expected gradient but reduces its variance", "The baseline makes the policy deterministic", "The baseline turns REINFORCE into an off-policy method"], answer: 1,
      explain: "Same expectation (the extra term is zero), lower variance — Figure 13.2." },
  );
})();
