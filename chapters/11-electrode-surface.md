# Chapter 11: Electrode Integrity and the Dielectric Handoff

The bottom electrode must remain conductive and geometrically useful after release. Its surface also becomes the substrate for the capacitor dielectric. Preserving bulk thickness alone does not establish that this interface is ready.

## 11.1 Separate geometric and chemical damage

Geometric responses include top recess, wall thinning, cracks, seams, and broken landing connections. Chemical responses include altered surface composition and retained species. Determine which are inherited from support access and which appear during mold removal using pre-release controls and matched process splits.

A thin interfacial layer may matter even when imaging finds no obvious loss. Use surface analysis with a stated information depth and sample-handling history. Blanket witnesses help compare trends, while patterned samples are needed to assess inaccessible or locally altered regions.

## 11.2 Queue time is a variable

Define the handoff clock from a specific event: dry completion or controlled-environment unload. Record storage environment and transfer duration. A queue study should span the actual expected production delay and compare both interface measurements and capacitor electrical distributions.

An immediate deposition split and a delayed split can reveal a queue effect, but they need the same incoming wafer and dielectric conditions. Avoid changing preclean and queue simultaneously when trying to establish the cause.

## 11.3 Residual oxide and capacitance

Use an EOT model to distinguish inaccessible surface from an insulating residue. If fraction f of otherwise active area retains a SiO₂ film of thickness t, with baseline EOT e, then C/C₀ = (1 − f) + f e/(e+t). For f = 0.10, e = 0.50 nm, and t = 2 nm, C/C₀ = 0.92. The covered fraction loses 80% of its local capacitance; the whole capacitor loses 8% under these assumptions.

This assumes conformal downstream layers and unchanged active geometry. A support-occluded region is not the same as an added oxide layer, and a chemically altered electrode interface may not behave as ideal SiO₂.

## Study questions

1. Why can sheet resistance miss an interface change?
2. What event starts your queue-time clock?
3. Compute C/C₀ for f = 0.25 using the same film thicknesses.

---

[Previous](./10-support-survival.md) · [Index](../INDEX.md) · [Next](./12-residual-stop.md)
