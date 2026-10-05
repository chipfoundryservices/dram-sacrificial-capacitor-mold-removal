# Chapter 5: Wet Release Hardware and Wafer Transitions

The equipment must maintain a repeatable chemical environment while the mechanical support changes from oxide to a thin lattice. Removal, rinse, and drying are coupled operations. An apparatus that achieves good blanket-film uniformity may still introduce release defects during dispense, draining, or transfer.

## 5.1 Single-wafer and batch routes

Single-wafer tools provide explicit timing and dispense control for each wafer. Evaluate center-to-edge replenishment, backside protection, nozzle stability, and uninterrupted wet coverage. Batch immersion changes the unit of control: tank loading, wafer spacing, bath age, and withdrawal history become part of the process definition. Neither route is intrinsically superior without response data from the actual structures.

| Hardware variable | Possible response | Qualification observation |
|---|---|---|
| Dispense interruption | Premature meniscus formation | Transition logs and collapse maps |
| Loading change | Chemical depletion or thermal shift | First/last and full/partial-load splits |
| Drain trajectory | Local drying fronts | Spatial orientation of bridges |
| Transfer duration | Residue and surface alteration | Matched queue splits |

## 5.2 Preserve transition history

A Hynix patent describes carrying mold removal, rinsing, and drying through a common chamber to reduce intermediate exposure and bridging. It establishes a disclosed integration route; it does not show that one chamber eliminates every collapse mechanism. [US7498267B2](https://patents.google.com/patent/US7498267B2/en)

The engineering inference is to log the entire wet history. A chemistry timestamp should be paired with rinse entry, exchange completion, dry entry, and transfer completion. Compare failed wafers against transition events, not only against chemical dwell time.

## 5.3 Match chambers by outcome

Match film rates, release-front progression, local support loss, post-dry defect distributions, and electrical outcomes. Equal setpoints do not establish equal exposure. A replacement nozzle or flow sensor can change the delivered process even when the controller recipe is unchanged.

A practical qualification split compares nominal dwell in two chambers using the same incoming lot, then samples near the worst expected access regions. Include transition-only controls when attempting to attribute defects to chemistry.

## Study questions

1. Which batch variable is absent from a single-wafer dwell specification?
2. How could a nozzle replacement alter collapse while film rate stays constant?
3. What timestamps belong in a release traveler?

---

[Previous](./04-transport-access.md) · [Index](../INDEX.md) · [Next](./06-vapor-hf.md)
