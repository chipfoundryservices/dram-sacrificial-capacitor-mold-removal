# Chapter 9: Chemical Delivery, Loading, and Drift

Delivered exposure depends on the chemical supply as well as the nominal recipe. Concentration drift, contamination, bath age, temperature offsets, and flow changes can alter release while the displayed dwell remains constant.

## 9.1 Separate independent controls

Measure concentration with an appropriate qualified method and temperature at a location whose relation to the wafer is established. Record lot loading and prior tool history. Do not infer chemical health solely from an oxide monitor because the same oxide rate can coexist with different support attack or electrode alteration.

| Control | Leading observation | Lagging observation |
|---|---|---|
| Chemical composition | Qualified composition measurement | Rate and selectivity drift |
| Temperature | Wafer-correlated temperature trace | Spatial clearance variation |
| Contamination | Incoming and recirculation analysis | Residue and leakage tails |
| Delivery | Flow and pressure trace | Asymmetric release defects |

## 9.2 Use loading calculations as estimates

Chapter 2's simplified oxide inventory is 0.91493 µm³ per µm² of array. Multiply by actual array area and subtract the access-etch volume before estimating consumption. Do not multiply by the entire wafer area when large fractions are peripheral circuitry or exclusions.

For SiO₂, assumed density 2200 kg/m³ and molar mass 0.0600843 kg/mol give 36,615 mol/m³. Combining this inventory with the balanced reaction gives a stoichiometric reagent requirement. Delivered chemical demand also includes excess concentration, replenishment, losses, and any other reactive films. Stoichiometric demand is a lower accounting bound, not the bath design.

## 9.3 Maintenance changes need release checks

After pump, filter, nozzle, seal, or sensor work, compare both film responses and patterned release outcomes. Particle control needs size and composition information where available; a count trend alone cannot locate its source.

A control chart should distinguish common drift from a sudden change and use a defined response plan. For a suspected delivery interruption, hold affected wafers for inspection rather than compensating automatically with extra time. Longer time cannot restore a structure damaged during an early drying event.

## Study questions

1. Why is a blanket oxide monitor insufficient to monitor chemistry health?
2. Which wafer area belongs in the consumption estimate?
3. What response can a dwell increase worsen?

---

[Previous](./08-drying-mechanics.md) · [Index](../INDEX.md) · [Next](./10-support-survival.md)
