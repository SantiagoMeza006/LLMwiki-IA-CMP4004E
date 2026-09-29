---
title: Agents and Environments (incl. PEAS)
type: concept
unit: agents
sources: [rn-ch02-intelligent-agents, slides-03-intelligent-agents]
updated: 2026-09-29
---

# Agents and Environments

## Definitions 🎯
- **Agent:** anything that perceives its **environment** through **sensors** and acts on it through **actuators** (R&N §2.1). Human: eyes/ears → brain → hands/mouth; robot: cameras/sensors → processor → motors; software: files/keyboard/network → program → screen/network (slides-03 s.2).
- **Percept:** what the sensors perceive now. **Percept sequence:** complete history of everything perceived.
- **Agent function:** abstract mathematical map *percept sequence → action*. Could in principle be a (usually infinite) lookup table.
- **Agent program:** concrete implementation of the agent function, running on a physical **architecture**. `agent = architecture + program`.
- Agent *function* can depend on the whole history; the agent *program* only receives the **current** percept, so it must remember whatever history it needs.
- "All AI design is the search for good programs that approximate the ideal function" (slides-03 s.3).

The notion of agent is an **analysis tool**, not an absolute classification (a calculator *can* be seen as an agent, but that doesn't help).

## Vacuum world (R&N Fig 2.2–2.3; slides-03 s.4)
Two squares A, B; percept = `[location, Dirty/Clean]`; actions Left, Right, Suck (NoOp).

| Percept sequence | Action |
|---|---|
| [A, Clean] | Right |
| [A, Dirty] | Suck |
| [B, Clean] | Left |
| [B, Dirty] | Suck |
| [A, Clean], [A, Clean] | Right |
| ... | ... |

Agent program (simple reflex): `if status = Dirty then Suck else if location = A then Right else Left`.

## Why lookup tables fail
Table size = Σ_{t=1..T} |P|^t for lifetime T and percept set P. Taxi camera for one hour → >10^600,000,000,000 entries; chess ≥ 10^150 (atoms in the universe < 10^80). No room to store it, no time to build it, no way to learn it. The goal of AI is to produce rational behaviour from a *small program* (as Newton's method replaced square-root tables).

## Task environment & PEAS 🎯
The **task environment** is the "problem" to which a rational agent is the "solution". Specify it first, always, as **PEAS**:

| Agent | Performance | Environment | Actuators | Sensors |
|---|---|---|---|---|
| Automated taxi | safe, fast, legal, comfortable, max profit, min impact on others | roads, traffic, police, pedestrians, customers, weather | steering, accelerator, brake, signal, horn, display, speech | cameras, radar/lidar, speedometer, GPS, engine sensors, accelerometer, microphones, touchscreen |
| Medical diagnosis | healthy patient, reduced costs | patient, hospital, staff | display of questions, tests, diagnoses, treatments | touchscreen/voice entry of symptoms & findings |
| Satellite image analysis | correct categorisation | orbiting satellite, downlink, weather | display of scene categorisation | high-res digital camera |
| Part-picking robot | % parts in correct bins | conveyor belt, bins | jointed arm and hand | camera, tactile & joint-angle sensors |
| Refinery controller | purity, yield, safety | refinery, raw materials, operators | valves, pumps, heaters, stirrers, displays | temperature, pressure, flow, chemical sensors |
| Interactive English tutor | student's test score | students, testing agency | display of exercises, feedback, speech | keyboard entry, voice |

(R&N Fig 2.4–2.5.) For the environment's *properties* see [task-environment-properties](task-environment-properties.md).

Related: [rationality](rationality.md) · [agent-architectures](agent-architectures.md) · [practice-agents](../practice/practice-agents.md)
