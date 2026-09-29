---
title: "Exercise — One PSO Update Step"
type: exercise
unit: optimization
sources: [slides-04-optimization]
updated: 2026-09-29
---

# One PSO Update Step — minimise f(x) = x²

One particle in 1-D:
- x_t = 4, v_t = −1, p_best = 3 (f = 9), g_best = 1 (f = 1)
- α1 = α2 = 2, random draws φ1 = 0.5, φ2 = 0.25

## Velocity
```
v_{t+1} = v_t + α1·φ1·(p_best − x_t) + α2·φ2·(g_best − x_t)
        = −1  + 2·0.5·(3 − 4)       + 2·0.25·(1 − 4)
        = −1  + (−1)                + (−1.5)
        = −3.5
```
Inertia −1, cognitive pull −1, social pull −1.5 → all push left toward the minimum at 0.

## Position
`x_{t+1} = x_t + v_{t+1} = 4 − 3.5 = 0.5`, f(0.5) = 0.25.

## Memory updates
- f(0.5) = 0.25 < f(p_best) = 9 → **p_best = 0.5**
- f(0.5) = 0.25 < f(g_best) = 1 → **g_best = 0.5** (shared with the whole swarm)

## Try it
Next step with φ1 = 0.2, φ2 = 0.6 (p_best = g_best = 0.5 now). <details><summary>answer</summary>v = −3.5 + 2·0.2·(0.5 − 0.5) + 2·0.6·(0.5 − 0.5) = −3.5 → x = 0.5 − 3.5 = −3, f = 9 (worse; bests unchanged). The particle **overshoots** because of inertia — which is why practical PSO adds an inertia weight w < 1 or velocity clamping. Overshooting also provides exploration.</details>
