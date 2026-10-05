# Chapter 12: Residual Mold and Bottom-Stop Protection

The last remaining mold often controls the minimum process time, while the earliest exposed support or stop controls the maximum. The process window exists only if these constraints overlap.

## 12.1 Find the last oxide

Inspect under supports, near unopened access sites, at array edges, and close to bottom landings. Cross-section selection should follow a hypothesis about access, not convenience. A clean top-down image may coexist with buried oxide. Elemental oxygen detection must also distinguish mold residue from legitimate oxide, contamination, or sample preparation.

Map clearance as a function of dwell using matched structures and repeated sites. Treat the result as a distribution of local clearance times. A single nominal time from one cross-section underestimates process variation.

## 12.2 Construct the feasible interval

Let the illustrative worst-case clear time be 1.2 min. Suppose a 50 nm support must retain 44 nm and each face loses 1 nm/min after immediate exposure. The support allows at most 3 min. Suppose a 20 nm stop must retain 18 nm and loses 1 nm/min from one face. The stop allows at most 2 min. The feasible teaching interval is therefore 1.2–2.0 min.

At nominal 1.75 min, a 20% slowdown raises clearance to 1.5 min while a 20% increase in stop attack lowers its maximum to 1.667 min. The nominal recipe then violates the revised stop budget. This illustrates why independent worst-case combinations matter.

## 12.3 Do not fix connectivity with overetch

An opening sealed by scum or a disconnected cavity may not gain useful access from more dwell. Meanwhile, already released regions continue to lose support or stop material. Inspect the entry structure before extending time. If the window is empty, change access, material, selectivity, or the integration sequence.

## Study questions

1. Which upper bound controls the example?
2. How does delayed stop exposure change its budget?
3. What upstream variable can reopen an empty process window?

---

[Previous](./11-electrode-surface.md) · [Index](../INDEX.md) · [Next](./13-failure-statistics.md)
