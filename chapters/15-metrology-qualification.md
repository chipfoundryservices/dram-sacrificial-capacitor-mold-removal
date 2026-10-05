# Chapter 15: Metrology, Experiments, and Qualification

Qualification combines mechanistic evidence and population evidence. Mechanistic measurements explain why the module works. Population measurements establish repeatability and bound failures within the tested conditions.

## 15.1 Build the measurement chain

Pair incoming film thickness, composition, and opening geometry with partial-release cross-sections. Follow with post-dry inspection, support measurements, surface analysis, and electrical capacitors. Preserve wafer and site identifiers so these observations can be related rather than averaged separately.

| Method | Primary role | Limitation to record |
|---|---|---|
| Cross-sectional microscopy | Buried release and attachment geometry | Destructive, small sampled volume |
| Top-down/tilted inspection | Tilt, bridges, spatial clustering | Detection sensitivity and occlusion |
| Surface chemical analysis | Composition at dielectric handoff | Information depth and handling |
| Electrical capacitors | Integrated interface and geometry response | Multiple possible causes |

## 15.2 Design splits for attribution

An initial design can vary removal dwell and drying route while blocking by incoming film lot. Keep the dielectric process fixed. Measure structural and electrical responses for every split. Add a queue-time factor only after basic clearance and drying effects can be separated.

Avoid optimizing on the mean capacitance alone. Include distribution tails, bridge signatures, support integrity, and stop survival. A process that improves the median while worsening a rare short tail may be unsuitable.

## 15.3 Gate progression

Proceed from material compatibility to patterned clearance, then transition robustness, electrical handoff, and repeatability across lots and chambers. Define what evidence closes each gate before running the lot. Record conditions outside the tested envelope explicitly.

For production control, use feed-forward only from measurements causally linked to release. Film thickness may justify a calibrated time adjustment; an access-connectivity defect generally requires a different response. Keep correction limits within the demonstrated support and stop budgets.

## Study questions

1. Which measurement connects buried clearance with an electrical response?
2. Why should incoming lot be a block in the experiment?
3. What prevents an automated dwell correction from eroding the process window?

---

[Previous](./14-alternative-molds.md) · [Index](../INDEX.md) · [Next](./16-integration-economics.md)
