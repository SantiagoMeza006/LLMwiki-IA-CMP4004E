---
title: Practice — Intelligent Agents
type: practice
unit: agents
sources: [slides-03-intelligent-agents, rn-ch02-intelligent-agents]
updated: 2026-09-29
---

# Practice — Intelligent Agents

1. Define *agent function* and *agent program*. Why must the agent program remember percepts itself?
   <details><summary>answer</summary>Function: abstract map from percept sequences to actions. Program: concrete implementation on an architecture. The program only receives the current percept, so if behaviour depends on history it must store it.</details>
2. Why is the TABLE-DRIVEN-AGENT doomed? Give the table size formula.
   <details><summary>answer</summary>Σ_{t=1..T} |P|^t entries — astronomically large (chess ≥ 10^150, taxi 10^600,000,000,000): no space to store it, no time to build it, impossible to learn.</details>
3. State the definition of a rational agent and the four things rationality depends on.
   <details><summary>answer</summary>For each percept sequence, select the action expected to maximise the performance measure given the percepts and built-in knowledge. Depends on: performance measure, prior knowledge, available actions, percept sequence.</details>
4. "A rational agent is omniscient." True or false? Explain with the street example.
   <details><summary>answer</summary>False. Rationality maximises expected performance given what's known; omniscience/perfection maximise actual outcomes. Being hit by a falling cargo door while crossing a clear street isn't irrational.</details>
5. A vacuum's performance measure is "amount of dirt sucked up". What goes wrong? What's a better measure?
   <details><summary>answer</summary>It can dump dirt and re-clean it forever. Better: +1 per clean square per time step (maybe minus energy/noise). Measure what you want in the environment, not how the agent should behave.</details>
6. Write the PEAS description for a self-checkout robot at a supermarket.
   <details><summary>answer</summary>P: correct charges, speed, low theft, customer satisfaction. E: checkout area, products, customers, payment terminal, staff. A: display/speaker, scale lock, receipt printer, alarm/call staff. S: barcode scanner, weight scale, camera, touchscreen, card reader. (Many valid answers.)</details>
7. Classify: (a) crossword, (b) poker, (c) taxi, (d) image analysis — on observable, agents, deterministic, episodic, static, discrete.
   <details><summary>answer</summary>(a) fully, single, deterministic, sequential, static, discrete. (b) partially, multi, stochastic, sequential, static, discrete. (c) partially, multi, stochastic, sequential, dynamic, continuous. (d) fully, single, deterministic, episodic, semidynamic, continuous.</details>
8. What is a *semidynamic* environment? Example?
   <details><summary>answer</summary>The world doesn't change while deliberating, but the performance score does (with time). Chess with a clock.</details>
9. Known vs unknown vs fully/partially observable — give a known-but-partially-observable and an unknown-but-fully-observable example.
   <details><summary>answer</summary>Solitaire (know rules, can't see face-down cards); a new video game (whole screen visible, don't know what the buttons do).</details>
10. Why does a simple reflex vacuum agent without a location sensor get stuck, and how can randomisation help?
    <details><summary>answer</summary>With only [Clean]/[Dirty] percepts, a fixed "move Left on Clean" loops forever if it started in A. Flipping a coin reaches the other square in 2 steps on average.</details>
11. What two models does a model-based agent use (R&N names)? What names did the slides use?
    <details><summary>answer</summary>R&N: transition model (how the world evolves + effects of actions) and sensor model (how state appears in percepts). Slides: "world model" (how the environment evolves) and "transition model" (how my actions affect it).</details>
12. Why is a goal-based agent insufficient for a taxi, and what fixes it?
    <details><summary>answer</summary>Goals are binary — they can't prefer quicker/safer/cheaper routes or trade off conflicting goals. A utility-based agent maximising expected utility fixes this.</details>
13. Name the four components of a learning agent and what each does.
    <details><summary>answer</summary>Performance element (chooses actions), learning element (improves it), critic (feedback vs fixed performance standard), problem generator (suggests exploratory actions).</details>
14. Atomic, factored or structured? (a) Romania route finding (b) Sudoku (c) "the truck is backing into the farm driveway blocked by a cow" (d) Prolog family KB.
    <details><summary>answer</summary>(a) atomic, (b) factored, (c) structured, (d) structured.</details>
