// Chapter 1 exam-style (interpretation) questions — appended to the chapter quiz.
(function () {
  const R = String.raw;
  (window.RL_QUIZ = window.RL_QUIZ || []).push(
    { tag: "exam", type: "num", q: R`During a game the learner makes a <em>greedy</em> move from a position with $V(S_t)=0.5$ to one with $V(S_{t+1})=0.8$. With $\alpha=0.2$, what is the updated $V(S_t)$?`, answer: 0.56, tol: 0.001,
      explain: R`$0.5+0.2(0.8-0.5)=0.56$. The earlier state moves a fraction α of the way toward the later one.` },
    { tag: "exam", type: "mcq", q: R`On the next turn the learner makes an <em>exploratory</em> move to a position valued 0.9. In the book's version of the algorithm, what happens to the value of the position it moved from?`,
      options: ["It moves toward 0.9", "It is reset to 0.5", "Nothing — exploratory moves do not cause a backup", "It moves toward 1"], answer: 2,
      explain: "Only greedy moves trigger the TD backup; that is why the learned values estimate win probabilities under greedy play." },
    { tag: "exam", type: "mcq", q: R`Two learners face an opponent who changes strategy halfway through training. Learner A uses a constant $\alpha=0.1$; learner B reduces $\alpha$ toward 0. Which keeps winning after the change, and why?`,
      options: ["B — its values have converged", "A — a constant step size keeps adapting to the changed opponent", "Both equally", "Neither can adapt"], answer: 1,
      explain: "A step size reduced to zero stops learning; one that is not reduced all the way to zero lets the player track an opponent who changes." },
    { tag: "exam", type: "mcq", q: R`Exercise 1.4 scenario: updates are made after <em>all</em> moves, including exploratory ones, and exploration continues forever. What do the values converge to?`,
      options: ["Win probabilities under optimal (greedy) play", "Win probabilities under the actual behaviour, including exploratory moves", "Zero", "The opponent's win probabilities"], answer: 1,
      explain: "Learning from every move estimates the behaviour policy's values (more accurate about what will happen); not learning from exploratory moves estimates the greedy policy's values — the on- vs off-policy distinction." },
  );
})();
