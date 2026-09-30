# Wiki Index

Catalog of every page. **LLM: read this first when answering a question.** Updated 2026-09-30 · 104 pages · 9 raw sources (R&N ingested as Ch 1–9).
Start at [overview](overview.md) (course map) and [discrepancies](discrepancies.md) (exam traps). History: [log](log.md).

## Sources
| Page | Summary |
|---|---|
| [slides-01-intro-to-ai](sources/slides-01-intro-to-ai.md) | Class timeline of AI: automata, Turing test, Dartmouth, LISP, perceptron, Prolog, backprop, SVM, deep learning, causal models. |
| [slides-02-problem-solving](sources/slides-02-problem-solving.md) | Problem formulation, BFS/DFS, heuristics, greedy, A*, minimax, alpha–beta, CSPs. |
| [slides-03-intelligent-agents](sources/slides-03-intelligent-agents.md) | Agent function/program, rationality, PEAS, environment properties, 4 agent types, representations. |
| [slides-04-optimization](sources/slides-04-optimization.md) | Evolutionary computation, GA, PSO, ACO, ABC with formulas. |
| [slides-xx-prolog](sources/slides-xx-prolog.md) | Horn clauses → Prolog: syntax, unification, SLD, arithmetic, lists, NAF, cut, N-Queens, Lab 01. |
| [rn-ch01-introduction](sources/rn-ch01-introduction.md) | R&N Ch 1: four approaches, standard model, value alignment, history. |
| [rn-ch02-intelligent-agents](sources/rn-ch02-intelligent-agents.md) | R&N Ch 2: agents, rationality, PEAS, environment table, agent programs, learning agents. |
| [rn-ch03-search](sources/rn-ch03-search.md) | R&N Ch 3: search problems, uninformed/informed search, A*, memory-bounded search, heuristic design (relaxation, pattern DBs, landmarks). |
| [rn-ch04-complex-environments](sources/rn-ch04-complex-environments.md) | R&N Ch 4: local search (hill climbing, SA, beam, evolutionary), continuous spaces, AND–OR search, belief states, online search. |
| [rn-ch05-csp](sources/rn-ch05-csp.md) | R&N Ch 5: CSP formalism, consistency (AC-3…), backtracking + MRV/LCV/MAC/backjumping, min-conflicts, tree-structured CSPs. |
| [rn-ch06-games](sources/rn-ch06-games.md) | R&N Ch 6: minimax, alpha–beta & move ordering, evaluation functions, MCTS/UCT, expectiminimax, imperfect information. |
| [rn-ch07-logical-agents](sources/rn-ch07-logical-agents.md) | R&N Ch 7: KB agents, wumpus world, entailment, propositional logic, resolution, Horn clauses, chaining, DPLL/WalkSAT. |
| [rn-ch08-first-order-logic](sources/rn-ch08-first-order-logic.md) | R&N Ch 8: FOL syntax & semantics, quantifiers, equality, database semantics, kinship, knowledge engineering. |
| [rn-ch09-fol-inference](sources/rn-ch09-fol-inference.md) | R&N Ch 9: UI/EI, unification, GMP, forward & backward chaining, Prolog vs logic, tabling, CLP, FOL resolution. |
| [holland-1992-genetic-algorithms](sources/holland-1992-genetic-algorithms.md) | Holland's Sci. Am. article: GA loop, schemata, implicit parallelism, classifier systems, applications. |
| [dorigo-1996-ant-system](sources/dorigo-1996-ant-system.md) | Founding ACO paper: transition rule, pheromone update, ant-cycle, parameters, stagnation, TSP/QAP/JSP. |
| [note-a-star-vs-dijkstra](sources/note-a-star-vs-dijkstra.md) | My homework note comparing A* and Dijkstra on Romania (checked; units fixed). |

## Concepts
| Page | Unit | Summary |
|---|---|---|
| [what-is-ai](concepts/what-is-ai.md) | intro | Four approaches, Turing test, rational agents, standard model, value alignment. |
| [history-of-ai](concepts/history-of-ai.md) | intro | Merged timeline from ~800 BC to LLM agents; Turing Award shortcut. |
| [agents-and-environments](concepts/agents-and-environments.md) | agents | Agent, percept, agent function vs program, vacuum world, PEAS examples. |
| [rationality](concepts/rationality.md) | agents | Definition, 4 dependencies, performance measures, omniscience, learning, autonomy. |
| [task-environment-properties](concepts/task-environment-properties.md) | agents | The 7 dimensions (+ known/unknown) with tests and examples. |
| [agent-architectures](concepts/agent-architectures.md) | agents | Simple reflex, model-based, goal-based, utility-based, learning agents. |
| [state-representations](concepts/state-representations.md) | agents | Atomic / factored / structured; where each is used in the course. |
| [search-problem-formulation](concepts/search-problem-formulation.md) | search | Problem-solving agent phases, formal problem definition, abstraction. |
| [example-search-problems](concepts/example-search-problems.md) | search | Vacuum, Sokoban, 8-puzzle, Knuth's 4, Romania edges, real-world problems. |
| [state-space-and-search-tree](concepts/state-space-and-search-tree.md) | search | Graph vs tree, node structure, frontier, reached, redundant paths, graph vs tree-like search. |
| [search-evaluation-criteria](concepts/search-evaluation-criteria.md) | search | Completeness, optimality, time, space; b, d, m, C*, ε. |
| [heuristics](concepts/heuristics.md) | search | Admissible, consistent, dominance; h_SLD; h1/h2; b*; relaxed problems, pattern DBs, landmarks, learning. |
| [nondeterministic-and-partially-observable-search](concepts/nondeterministic-and-partially-observable-search.md) | search | AND–OR search, conditional plans, belief states, sensorless problems, online search, LRTA*. |
| [adversarial-search](concepts/adversarial-search.md) | games-csp | MAX/MIN, zero-sum (constant-sum), perfect info; game formulation; algorithm map; imperfect information. |
| [constraint-satisfaction-problems](concepts/constraint-satisfaction-problems.md) | games-csp | ⟨X, D, C⟩, examples, constraint kinds, propagation, heuristics, problem structure. |
| [local-search](concepts/local-search.md) | optimization | State-space landscape, the local search family, local beam search, continuous spaces. |
| [optimization-and-local-optima](concepts/optimization-and-local-optima.md) | optimization | Optimization vs path search, local vs global optima, metaheuristics overview. |
| [evolutionary-computation](concepts/evolutionary-computation.md) | optimization | Fogel, Rechenberg & Schwefel, Holland; GA vs ES vs GP; biology → algorithm vocabulary. |
| [swarm-intelligence](concepts/swarm-intelligence.md) | optimization | Stigmergy, positive/negative feedback, why swarms work. |
| [exploration-vs-exploitation](concepts/exploration-vs-exploitation.md) | optimization | The trade-off across learning agents, SA, GA, PSO, ACO, ABC, MCTS, LRTA*. |
| [knowledge-based-agents](concepts/knowledge-based-agents.md) | logic | KB, TELL/ASK, declarative approach, wumpus world PEAS, frame problem. |
| [propositional-logic](concepts/propositional-logic.md) | logic | Syntax, truth tables, entailment, validity, satisfiability, soundness/completeness, equivalences. |
| [first-order-logic](concepts/first-order-logic.md) | logic | Objects/relations, terms, quantifiers (∀⇒, ∃∧), equality, database semantics, kinship, knowledge engineering. |
| [first-order-inference](concepts/first-order-inference.md) | logic | UI, EI, Skolem constants, propositionalization, semidecidability, Generalized Modus Ponens. |
| [logic-to-horn-clauses](concepts/logic-to-horn-clauses.md) | logic | Propositional → FOL → Horn → Prolog; CNF; definite/fact/goal clauses. |
| [forward-and-backward-chaining](concepts/forward-and-backward-chaining.md) | logic | PL-FC-ENTAILS?, Criminal(West), FOL-FC-ASK, Datalog, Rete, FOL-BC-ASK. |
| [unification](concepts/unification.md) | logic | Rules, examples, UNIFY algorithm, standardizing apart, MGU, occur check. |
| [prolog](concepts/prolog.md) | logic | Syntax, terms, is vs =, lists, findall/setof, NAF, cut, Prolog vs FOL, tabling, CLP, Lab 01 checklist. |

## Algorithms
| Page | Unit | Summary |
|---|---|---|
| [best-first-search](algorithms/best-first-search.md) | search | Generic f(n)-driven graph search; pseudocode; family table. |
| [breadth-first-search](algorithms/breadth-first-search.md) | search | FIFO, early goal test, complete, optimal for uniform costs, O(b^d). |
| [uniform-cost-search](algorithms/uniform-cost-search.md) | search | Dijkstra, f = g, late goal test, O(b^(1+⌊C*/ε⌋)). |
| [depth-first-search](algorithms/depth-first-search.md) | search | LIFO, O(b·m) memory, incomplete/not optimal; backtracking variant. |
| [depth-limited-and-iterative-deepening](algorithms/depth-limited-and-iterative-deepening.md) | search | DLS with cutoff; IDS = best uninformed method for big spaces. |
| [bidirectional-search](algorithms/bidirectional-search.md) | search | Two frontiers, b^(d/2); f2 = max(2g, g+h). |
| [greedy-best-first-search](algorithms/greedy-best-first-search.md) | search | f = h; Romania gives 450; not optimal. |
| [a-star-search](algorithms/a-star-search.md) | search | f = g + h; Romania trace (418); optimality proof; contours. |
| [memory-bounded-and-weighted-search](algorithms/memory-bounded-and-weighted-search.md) | search | Weighted A*, beam, IDA*, RBFS, SMA*. |
| [minimax](algorithms/minimax.md) | games-csp | Recursive value, pseudocode, Fig 6.2 example, O(b^m); multiplayer vectors. |
| [alpha-beta-pruning](algorithms/alpha-beta-pruning.md) | games-csp | α/β bounds, pruning rule, pseudocode, move ordering, transposition tables. |
| [heuristic-alpha-beta](algorithms/heuristic-alpha-beta.md) | games-csp | H-MINIMAX, evaluation functions, cutoff, quiescence, horizon effect, forward pruning, lookup. |
| [monte-carlo-tree-search](algorithms/monte-carlo-tree-search.md) | games-csp | Playouts, 4 steps, UCT/UCB1, when MCTS beats alpha–beta. |
| [expectiminimax](algorithms/expectiminimax.md) | games-csp | Chance nodes, backgammon, calibrated evaluation functions (Fig 6.14). |
| [backtracking-search-csp](algorithms/backtracking-search-csp.md) | games-csp | BACKTRACK pseudocode, MRV/LCV/inference hooks, forward checking table, backjumping, no-goods. |
| [ac-3](algorithms/ac-3.md) | games-csp | Arc consistency algorithm, REVISE, O(cd³), limits, Sudoku, MAC. |
| [min-conflicts](algorithms/min-conflicts.md) | games-csp | Local search for CSPs; million-queens in ~50 steps; plateaus, tabu, weighting. |
| [hill-climbing](algorithms/hill-climbing.md) | optimization | Steepest ascent, 8-queens stats (14% / 94%), stochastic, first-choice, random restart. |
| [simulated-annealing](algorithms/simulated-annealing.md) | optimization | Accept worse moves with e^(ΔE/T); schedule; acceptance table. |
| [genetic-algorithms](algorithms/genetic-algorithms.md) | optimization | Encoding, selection, crossover, mutation, schemata; R&N 8-queens GA and pseudocode. |
| [particle-swarm-optimization](algorithms/particle-swarm-optimization.md) | optimization | Velocity/position updates, p_best, g_best. |
| [ant-colony-optimization](algorithms/ant-colony-optimization.md) | optimization | Transition probability, pheromone update, ρ conventions, Dorigo's findings. |
| [artificial-bee-colony](algorithms/artificial-bee-colony.md) | optimization | Employed/onlooker/scout bees, neighbour formula, parameters. |
| [resolution](algorithms/resolution.md) | logic | Resolution rule, CNF conversion (propositional & FOL with Skolem functions), PL-RESOLUTION, completeness. |
| [dpll-and-walksat](algorithms/dpll-and-walksat.md) | logic | Complete backtracking SAT vs local-search SAT; phase transition at m/n ≈ 4.26. |
| [sld-resolution](algorithms/sld-resolution.md) | logic | Prolog's execution: DFS backward chaining; order matters; tabling (877 vs 62 inferences). |

## Comparisons
| Page | Summary |
|---|---|
| [uninformed-search-comparison](comparisons/uninformed-search-comparison.md) | R&N Fig 3.15 table + rules of thumb. |
| [informed-search-comparison](comparisons/informed-search-comparison.md) | UCS/greedy/A*/weighted/IDA*/RBFS/SMA*/beam; Romania results side by side. |
| [a-star-vs-dijkstra](comparisons/a-star-vs-dijkstra.md) | Filed from my homework; nodes expanded, h = 0 special case. |
| [agent-types-comparison](comparisons/agent-types-comparison.md) | 5 agent types across 8 criteria. |
| [environment-examples](comparisons/environment-examples.md) | R&N Fig 2.6 + extra examples to classify. |
| [game-algorithms-comparison](comparisons/game-algorithms-comparison.md) | Minimax, alpha–beta, H-minimax, MCTS, expectiminimax, lookup; parallels with single-agent search. |
| [local-search-comparison](comparisons/local-search-comparison.md) | HC variants, SA, beam, GA, PSO, ACO, ABC, min-conflicts, WalkSAT, gradient methods. |
| [bio-inspired-algorithms-comparison](comparisons/bio-inspired-algorithms-comparison.md) | GA vs PSO vs ACO vs ABC. |
| [inference-methods-comparison](comparisons/inference-methods-comparison.md) | Model checking, DPLL, WalkSAT, resolution, FC, BC, Prolog — soundness, completeness, cost. |

## Exercises
| Page | Summary |
|---|---|
| [romania-ucs-trace](exercises/romania-ucs-trace.md) | Full UCS expansion order, 13 pops, cost 418. |
| [romania-greedy-and-a-star-trace](exercises/romania-greedy-and-a-star-trace.md) | Greedy (450) vs A* (418) step by step + self-test. |
| [uninformed-search-traces](exercises/uninformed-search-traces.md) | BFS/DFS/IDS on a binary tree and on Romania; IDS node counts. |
| [8-puzzle-heuristics](exercises/8-puzzle-heuristics.md) | h1 = 8, h2 = 18 tile by tile; b* = 1.92. |
| [minimax-alpha-beta-trace](exercises/minimax-alpha-beta-trace.md) | Fig 6.2 minimax + alpha–beta table; practice tree. |
| [games-traces](exercises/games-traces.md) | Material eval, expectiminimax, UCB1 (Fig 6.10), MCTS back-propagation, horizon effect, multiplayer. |
| [csp-traces](exercises/csp-traces.md) | AC on Y = X², path consistency, forward checking, MRV/degree, LCV, bounds, Atmost, tree CSPs, min-conflicts. |
| [local-search-traces](exercises/local-search-traces.md) | 8-queens h values, hill-climbing run to a local minimum, restarts, SA acceptance, beam, gradient/Newton. |
| [ga-one-generation](exercises/ga-one-generation.md) | f(x) = x², roulette selection, crossover, mutation — avg 292.5 → 414.75. |
| [aco-transition-step](exercises/aco-transition-step.md) | P(j\|i) for several α, β; one pheromone update. |
| [pso-update-step](exercises/pso-update-step.md) | One velocity/position update; overshoot. |
| [logic-inference-traces](exercises/logic-inference-traces.md) | Wumpus model checking (3/128), inference-rule proof, CNF, resolution, FC trace, FOL translation, unification, Skolemization, GMP. |
| [prolog-traces](exercises/prolog-traces.md) | Family KB queries, factorial, Fibonacci, lists, isPerm and max bugs, arithmetic quiz. |
| [n-queens-prolog](exercises/n-queens-prolog.md) | Representation, test-as-you-go vs generate-and-test, inference counts. |

## Practice (exam-style questions, answers hidden)
| Page | Questions |
|---|---|
| [practice-intro](practice/practice-intro.md) | 10 |
| [practice-agents](practice/practice-agents.md) | 14 |
| [practice-search](practice/practice-search.md) | 18 |
| [practice-games-and-csp](practice/practice-games-and-csp.md) | 29 |
| [practice-optimization](practice/practice-optimization.md) | 30 |
| [practice-logic-prolog](practice/practice-logic-prolog.md) | 35 |

## Meta
| Page | Summary |
|---|---|
| [overview](overview.md) | Course map, unit table, cross-unit threads, exam prep steps. |
| [discrepancies](discrepancies.md) | 20 slide/textbook/paper conflicts, conventions and OCR errors. |
| [log](log.md) | Append-only history. |
