# Wiki Index

Catalog of every page. **LLM: read this first when answering a question.** Updated 2026-09-29 · 76 pages · 9 sources.
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
| [rn-ch03-search](sources/rn-ch03-search.md) | R&N Ch 3: search problems, BFS/UCS/DFS/IDS/bidirectional, greedy, A*, memory-bounded search, 8-puzzle heuristics. |
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
| [heuristics](concepts/heuristics.md) | search | Admissible, consistent, dominance; h_SLD table; h1/h2; effective branching factor. |
| [adversarial-search](concepts/adversarial-search.md) | games-csp | MAX/MIN, zero-sum, perfect info; game formulation. |
| [constraint-satisfaction-problems](concepts/constraint-satisfaction-problems.md) | games-csp | Variables/domains/constraints; forward checking, arc consistency, MRV. |
| [optimization-and-local-optima](concepts/optimization-and-local-optima.md) | optimization | Optimization vs path search, local vs global optima, metaheuristics overview. |
| [evolutionary-computation](concepts/evolutionary-computation.md) | optimization | Fogel, Rechenberg & Schwefel, Holland; biology → algorithm vocabulary. |
| [swarm-intelligence](concepts/swarm-intelligence.md) | optimization | Stigmergy, positive/negative feedback, why swarms work. |
| [exploration-vs-exploitation](concepts/exploration-vs-exploitation.md) | optimization | The trade-off across learning agents, GA, PSO, ACO, ABC. |
| [logic-to-horn-clauses](concepts/logic-to-horn-clauses.md) | logic | Propositional → FOL → Horn → Prolog; CNF; definite/fact/goal clauses. |
| [forward-and-backward-chaining](concepts/forward-and-backward-chaining.md) | logic | Data- vs goal-driven inference; Criminal(West) proof tree. |
| [unification](concepts/unification.md) | logic | Rules, examples, MGU, occurs check. |
| [prolog](concepts/prolog.md) | logic | Syntax, terms, is vs =, lists, findall/setof, NAF, cut, mistakes, Lab 01 checklist. |

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
| [minimax](algorithms/minimax.md) | games-csp | Recursive value, pseudocode, Fig 6.2 example, O(b^m). |
| [alpha-beta-pruning](algorithms/alpha-beta-pruning.md) | games-csp | α/β bounds, pruning rule, pseudocode, O(b^(m/2)) best case. |
| [backtracking-search-csp](algorithms/backtracking-search-csp.md) | games-csp | BACKTRACK pseudocode with MRV/LCV/inference hooks. |
| [genetic-algorithms](algorithms/genetic-algorithms.md) | optimization | Encoding, selection, crossover, mutation, schemata. |
| [particle-swarm-optimization](algorithms/particle-swarm-optimization.md) | optimization | Velocity/position updates, p_best, g_best. |
| [ant-colony-optimization](algorithms/ant-colony-optimization.md) | optimization | Transition probability, pheromone update, ρ conventions, Dorigo's findings. |
| [artificial-bee-colony](algorithms/artificial-bee-colony.md) | optimization | Employed/onlooker/scout bees, neighbour formula, parameters. |
| [sld-resolution](algorithms/sld-resolution.md) | logic | Prolog's execution: DFS backward chaining; order matters; tabling. |

## Comparisons
| Page | Summary |
|---|---|
| [uninformed-search-comparison](comparisons/uninformed-search-comparison.md) | R&N Fig 3.15 table + rules of thumb. |
| [informed-search-comparison](comparisons/informed-search-comparison.md) | UCS/greedy/A*/weighted/IDA*/RBFS/SMA*/beam; Romania results side by side. |
| [a-star-vs-dijkstra](comparisons/a-star-vs-dijkstra.md) | Filed from my homework; nodes expanded, h = 0 special case. |
| [agent-types-comparison](comparisons/agent-types-comparison.md) | 5 agent types across 8 criteria. |
| [environment-examples](comparisons/environment-examples.md) | R&N Fig 2.6 + extra examples to classify. |
| [bio-inspired-algorithms-comparison](comparisons/bio-inspired-algorithms-comparison.md) | GA vs PSO vs ACO vs ABC. |

## Exercises
| Page | Summary |
|---|---|
| [romania-ucs-trace](exercises/romania-ucs-trace.md) | Full UCS expansion order, 13 pops, cost 418. |
| [romania-greedy-and-a-star-trace](exercises/romania-greedy-and-a-star-trace.md) | Greedy (450) vs A* (418) step by step + self-test. |
| [uninformed-search-traces](exercises/uninformed-search-traces.md) | BFS/DFS/IDS on a binary tree and on Romania; IDS node counts. |
| [8-puzzle-heuristics](exercises/8-puzzle-heuristics.md) | h1 = 8, h2 = 18 tile by tile; b* = 1.92. |
| [minimax-alpha-beta-trace](exercises/minimax-alpha-beta-trace.md) | Fig 6.2 minimax + alpha–beta table; practice tree. |
| [ga-one-generation](exercises/ga-one-generation.md) | f(x) = x², roulette selection, crossover, mutation — avg 292.5 → 414.75. |
| [aco-transition-step](exercises/aco-transition-step.md) | P(j\|i) for several α, β; one pheromone update. |
| [pso-update-step](exercises/pso-update-step.md) | One velocity/position update; overshoot. |
| [prolog-traces](exercises/prolog-traces.md) | Family KB queries, factorial, Fibonacci, lists, isPerm and max bugs, arithmetic quiz. |
| [n-queens-prolog](exercises/n-queens-prolog.md) | Representation, test-as-you-go vs generate-and-test, inference counts. |

## Practice (exam-style questions, answers hidden)
| Page | Questions |
|---|---|
| [practice-intro](practice/practice-intro.md) | 10 |
| [practice-agents](practice/practice-agents.md) | 14 |
| [practice-search](practice/practice-search.md) | 18 |
| [practice-games-and-csp](practice/practice-games-and-csp.md) | 14 |
| [practice-optimization](practice/practice-optimization.md) | 18 |
| [practice-logic-prolog](practice/practice-logic-prolog.md) | 16 |

## Meta
| Page | Summary |
|---|---|
| [overview](overview.md) | Course map, unit table, cross-unit threads, exam prep steps. |
| [discrepancies](discrepancies.md) | 16 slide/textbook/paper conflicts and OCR errors. |
| [log](log.md) | Append-only history. |
