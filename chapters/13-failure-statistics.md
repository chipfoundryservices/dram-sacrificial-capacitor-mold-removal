# Chapter 13: Collapse, Clusters, and Rare-Event Statistics

A DRAM array contains enough electrodes that a visually impressive field represents a small fraction of the population. Inspection evidence needs a denominator, a detection capability, and a model connecting defects to electrical yield.

## 13.1 Zero observed defects is a bound

For independent events with zero observations in n trials, the approximate one-sided 95% upper probability is −ln(0.05)/n, about 3/n. At n = 10⁶ inspected pillars, the upper bound is roughly 3×10⁻⁶ per pillar. It does not establish a 10⁻⁹ rate. About three billion independent observations with perfect detection would be needed for that bound.

Pillars in the same damaged support region are correlated. Detection can also miss subtle tilt or buried bridges. State effective sampling units and detection limitations rather than treating every visible pillar as an independent trial.

## 13.2 From cells to die yield

For a hypothetical 16 Gibit array, N = 2³⁴ = 17,179,869,184 cells. An independent probability q = 10⁻⁹ gives Nq = 17.18 expected affected cells. With no repair and every event fatal, the zero-event probability is exp(−Nq), about 3.46×10⁻⁸. A claim that one event per billion automatically yields good dies would therefore be misleading.

Real redundancy changes this model. Define which errors consume row, column, or other repair resources, and whether a spatial cluster exceeds available coverage. Cell defects, bridge events, and defective support regions are different denominators. Specify which one q describes.

## 13.3 Experimental response

Retain wafer maps and cluster size distributions. Compare defect orientation with drying trajectories and access geometry. Include electrical bridge tests and retention distributions, then trace failures back to structural samples where possible.

A qualification statement should read like: zero detected bridges in a stated area under a stated inspection method, plus a stated electrical sample and confidence model. It should not read simply: collapse free.

## Study questions

1. What upper bound follows from zero events in 10⁷ trials?
2. Why does cluster correlation weaken a pillar-count denominator?
3. Which repair architecture data are required for a useful yield prediction?

---

[Previous](./12-residual-stop.md) · [Index](../INDEX.md) · [Next](./14-alternative-molds.md)
