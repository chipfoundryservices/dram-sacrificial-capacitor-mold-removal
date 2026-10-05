# Chapter 6: Vapor HF: Opportunity and Material Compatibility

Vapor HF is an alternative route for sacrificial oxide removal, but a MEMS release capability is not automatically a DRAM electrode-release capability. The actual electrode, supports, stop, mold, and residues must be assessed together.

## 6.1 What the public tool documentation establishes

EPFL documents an anhydrous-HF and ethanol process for sacrificial oxide release. Its documentation links water generation and loading to process behavior and lists TiN, TaN, and several other materials as incompatible, with exceptions for some silicon nitride. These are restrictions for that facility's implementation. They neither prohibit every possible vapor-HF process nor validate another tool for DRAM. [EPFL SPTS uEtch](https://www.epfl.ch/research/facilities/cmi/equipment/etching/spts-uetch/)

## 6.2 Define a compatibility gate

Begin with the exact electrode film, including deposition and anneal history. Measure thickness, resistance, surface chemistry, and morphology before and after the candidate environment. Repeat for support and stop films. Then test patterned specimens: a blanket compatibility result cannot resolve trapped reaction products or local condensation beneath supports.

Set a rejection criterion before comparing throughput. A route that removes oxide but changes the electrode beyond the downstream dielectric's tolerance is unsuitable regardless of its apparent drying advantage.

## 6.3 Loading and condensation

Track exposed oxide area and its change during release. Control and record wafer temperature, delivered gas conditions, chamber condition, and the sequence of reaction and purge periods. Condensation or retained byproducts can restore liquid-mediated or residue-mediated failure mechanisms. A gas inlet does not guarantee that the structure remains dry everywhere.

Use splits that distinguish chemical exposure from purge history. Inspect the underside of supports and dense array interiors, not only open test pads. Connect the observations to electrical monitors after dielectric deposition.

## 6.4 Route comparison

Compare wet and vapor routes at equal outgoing acceptance criteria. Do not compare one route's blanket rate with another route's total removal/rinse/dry time. Include failed wafers, maintenance, consumables, and queue constraints in the economic denominator.

## Study questions

1. What is the scope of EPFL's TiN restriction?
2. Why must patterned compatibility follow blanket tests?
3. Which measurement would detect electrode damage without obvious film loss?

---

[Previous](./05-wet-hardware.md) · [Index](../INDEX.md) · [Next](./07-rinse-exchange.md)
