# DRAM Sacrificial Capacitor Mold Removal

ChipFoundryServices Technical Series · First edition · 2026-10-05


<a id="book-preface-md"></a>

# Preface: Release Is a Structural and Surface Process

Removing a sacrificial mold is easy to describe and difficult to certify. Oxide that once gave a capacitor electrode its shape must leave through restricted access, while a support lattice holds the newly exposed electrodes apart. The resulting surface must then accept a dielectric without unacceptable interfacial change.

The book asks three connected questions: has every intended region cleared, has the remaining structure survived, and is the electrode ready for the next module? None can be answered by a blanket oxide rate alone. The chapters connect chemistry, geometry, equipment transitions, mechanics, and electrical evidence so that an apparently successful dip is evaluated as a complete release module.

## Relationship to the series

The existing DRAM capacitor mold-etch volume includes support opening and dip-out. The support-layer volume concentrates on patterned nitride removal. Here the starting point is an access-open electrode array. Support-patterning details become incoming conditions, while release completeness, exposure chronology, rinse/dry stability, and qualification receive the attention.

The organization preserves the sibling series format: fundamentals in Chapters 1–4, hardware and fluid management in Chapters 5–9, failure mechanisms and alternatives in Chapters 10–14, and production qualification in Chapters 15–16. Appendices A–G collect assumptions, chemistry, workflow, budgets, calculations, metrology, and troubleshooting.

## How to interpret the numbers

The 45 nm pitch and 28 nm pillar model is an educational continuity choice. Its geometry is calculated independently. Etch rates, mechanical properties, surface tension, and cost inputs are assumptions used to demonstrate sensitivity. They are not measured specifications for a supplier, technology node, or production line.

Where a simple model is inadequate, the text says what it leaves out. A diffusion time is not proof of reagent supply. A cantilever is not a complete support-network model. Zero observed defects is not zero defect probability. A patent is not a production qualification report. These distinctions are part of the engineering content.

## Intended readers

Process and integration engineers can follow the clearance and loss budgets. Equipment engineers can trace transitions and delivered exposure. Device engineers can connect residual films and interface changes to electrical responses. Researchers can use the model limits to identify measurements that would improve the analysis.

Work the questions with [Appendix E](#book-appendices-e-worked-calculations-md) and the calculation script. When applying the ideas to a real stack, replace every assumed input and document what evidence supports the replacement.

[Continue to the index](#book-index-md).



<a id="book-index-md"></a>

# Index: DRAM Sacrificial Capacitor Mold Removal

16 chapters, four parts, appendices A–G, and a glossary.

## Part I: Fundamentals

- [Chapter 1: The Release Module and Its Acceptance Contract](#book-chapters-01-release-module-md)
- [Chapter 2: Reference Geometry and Material Inventory](#book-chapters-02-reference-geometry-md)
- [Chapter 3: Oxide Dissolution and Selectivity Budgets](#book-chapters-03-oxide-chemistry-md)
- [Chapter 4: Access, Wetting, and Moving Release Fronts](#book-chapters-04-transport-access-md)

## Part II: Hardware and Fluid Management

- [Chapter 5: Wet Release Hardware and Wafer Transitions](#book-chapters-05-wet-hardware-md)
- [Chapter 6: Vapor HF: Opportunity and Material Compatibility](#book-chapters-06-vapor-hf-md)
- [Chapter 7: Rinse, Solvent Exchange, and Residue Control](#book-chapters-07-rinse-exchange-md)
- [Chapter 8: Drying and Elastocapillary Stability](#book-chapters-08-drying-mechanics-md)
- [Chapter 9: Chemical Delivery, Loading, and Drift](#book-chapters-09-delivery-control-md)

## Part III: Failure Mechanisms and Alternatives

- [Chapter 10: Support Survival and Exposure Chronology](#book-chapters-10-support-survival-md)
- [Chapter 11: Electrode Integrity and the Dielectric Handoff](#book-chapters-11-electrode-surface-md)
- [Chapter 12: Residual Mold and Bottom-Stop Protection](#book-chapters-12-residual-stop-md)
- [Chapter 13: Collapse, Clusters, and Rare-Event Statistics](#book-chapters-13-failure-statistics-md)
- [Chapter 14: Sequential Release and Alternative Sacrificial Molds](#book-chapters-14-alternative-molds-md)

## Part IV: Qualification and Production

- [Chapter 15: Metrology, Experiments, and Qualification](#book-chapters-15-metrology-qualification-md)
- [Chapter 16: Integration, Yield, and Cost of Accepted Wafers](#book-chapters-16-integration-economics-md)

## Appendices and Reference

- [Appendix A: Geometry, Materials, and Assumption Register](#book-appendices-a-material-properties-md)
- [Appendix B: Reaction Accounting and Chemistry Evidence](#book-appendices-b-chemistry-reaction-data-md)
- [Appendix C: Qualification Workflow and Data Record](#book-appendices-c-qualification-workflow-md)
- [Appendix D: Clearance and Preservation Windows](#book-appendices-d-process-windows-md)
- [Appendix E: Worked Calculations and Selected Answers](#book-appendices-e-worked-calculations-md)
- [Appendix F: Metrology and Sampling Reference](#book-appendices-f-metrology-reference-md)
- [Appendix G: Troubleshooting Guide](#book-appendices-g-troubleshooting-guide-md)
- [Glossary](#book-glossary-md)
- [References](#book-references-md)

## Reading paths

- Process: 1 → 3 → 4 → 7 → 10 → 12 → 15, then Appendices D and G.
- Equipment: 1 → 5 → 6 → 7 → 8 → 9 → 16.
- Integration: 1 → 2 → 8 → 10 → 11 → 12 → 14 → 16.
- Device and yield: 1 → 11 → 13 → 15 → 16, then Appendix E.

Each chapter includes three study questions. Selected numerical answers and interpretation guidance appear in Appendix E.



<a id="book-chapters-01-release-module-md"></a>

# Chapter 1: The Release Module and Its Acceptance Contract

A sacrificial mold gives the bottom electrode its shape during fabrication. Once the electrode has been deposited and isolated, the surrounding mold obstructs the surface on which the capacitor dielectric and plate must be formed. Release replaces that mold with accessible space while retaining the intended mechanical supports. A successful result is therefore a structure and a surface, rather than merely a measured oxide etch rate.

This volume begins after the support access openings have been formed. Capacitor-hole etch and detailed support-pattern plasma development belong to the companion books. They enter this book as inherited variables: hole taper, electrode thickness, opening placement, polymer residues, support stress, and bottom-stop defects. Release cannot repair every defect inherited from those operations.

## 1.1 Define the incoming and outgoing wafer

The incoming wafer needs an identified mold-film stack, an electrically isolated bottom electrode, connected access paths, and a documented bottom stop. The outgoing wafer needs cleared mold, intact support attachments, adequate electrode continuity, and a surface compatible with dielectric deposition. Record each requirement as a measurable response with a sampling plan.

| Requirement | Useful evidence | What it does not prove |
|---|---|---|
| Mold cleared | Cross-section and chemical mapping | Whole-wafer absence of rare pockets |
| Pillars upright | Tilt and bridge inspection | Absence of later plate-induced movement |
| Supports preserved | Thickness and attachment inspection | Unmeasured buried fracture strength |
| Electrode ready | Surface analysis and electrical splits | Universal compatibility with another dielectric |

Avoid a single composite pass score during development. A clear wafer with weakened supports and a stable wafer with residual oxide are different failures requiring different actions.

## 1.2 Draw the process boundary

```text
Hole etch → electrode deposition → node isolation → support access
                                                   ↓
                                 mold removal → rinse/dry → surface handoff
                                                   ↓
                                        dielectric → plate → electrical test
```

The module boundary includes transitions. A rinse, transfer, or queue can change a structure already released by chemistry. Assign ownership of those transitions in the traveler rather than assuming that removal completion ends process responsibility.

## 1.3 Qualification example

Suppose blanket oxide clears, post-dry inspection finds no bridges in a small field, and capacitance falls after dielectric deposition. This is insufficient evidence to lengthen the etch. Inspect the buried release front, evaluate surface alteration, and separate the contributions using splits that keep the drying and dielectric processes fixed. The downstream response belongs in the acceptance contract.

## Study questions

1. Which incoming defect can mimic slow mold removal?
2. Why does a blanket-film endpoint fail to certify an array?
3. Write separate acceptance measures for structure and surface.

---

[Preface](#book-preface-md) · [Index](#book-index-md) · [Next](#book-chapters-02-reference-geometry-md)



<a id="book-chapters-02-reference-geometry-md"></a>

# Chapter 2: Reference Geometry and Material Inventory

All numerical examples in this book use an explicitly hypothetical reference structure derived from the sibling series geometry. They are teaching inputs, not a claim about a commercial DRAM node. Do not assign a series book number without a maintained organization catalog.

## 2.1 Geometry convention

The pillar is represented by a constant 28 nm diameter for calculations, with 45 nm nearest-neighbor pitch on a triangular lattice and 1.60 µm total height. Real taper requires local diameter measurements. The gap is 17 nm only in this constant-diameter model; a 32 nm top diameter would give a 13 nm top gap.

| Parameter | Teaching value | Use |
|---|---:|---|
| Pitch p | 45 nm | Density and neighbor spacing |
| Diameter d | 28 nm | Outer area and solid-beam example |
| Height H | 1600 nm | Total structure height |
| Top support | 120 nm | Occluded outer surface |
| Middle support | 50 nm | Occluded outer surface |
| Upper oxide | 650 nm | Upper release region |
| Lower oxide | 760 nm | Lower release region |
| Bottom stop | 20 nm | Separate film below the 1580 nm stack |

The four mold/support layers sum to 1580 nm. Adding the stop gives 1600 nm. For the capacitance example, conservatively exclude the stop height and both support thicknesses: exposed height is 1410 nm. This convention avoids silently counting the bottom landing as exposed capacitor area.

## 2.2 Inventory before chemistry

The area per pillar is A_cell = √3 p²/2 = 1753.70 nm². Density is 570.22 pillars/µm². These values correct the 1734 nm² and 577 pillars/µm² rounding used in some sibling text. They follow directly from 45 nm pitch, rather than from copying a prior headline.

The solid pillar fraction is πd²/(4A_cell) = 0.3511. A simple inventory of oxide in the upper and lower regions is (650 + 760)(1 − 0.3511) = 914.93 nm equivalent thickness. This ignores access-opening oxide already removed, edge structures, taper, and electrode interiors. It is an upper-level loading estimate rather than a release-front solution.

## 2.3 Solid pillars and cylinders

A filled pillar and a hollow electrode can have identical outer diameter and radically different bending stiffness. For a hollow tube use I = π(d_o⁴ − d_i⁴)/64. Inner and outer capacitor surfaces require separate accounting for access and dielectric coverage. Never apply the solid-beam calculation to a thin cylinder by substituting only its outer diameter.

## Study questions

1. Compute density at 42 nm pitch.
2. Why should support height be excluded from the exposed outer area?
3. Which inventory terms change when release access has already removed oxide?

---

[Previous](#book-chapters-01-release-module-md) · [Index](#book-index-md) · [Next](#book-chapters-03-oxide-chemistry-md)



<a id="book-chapters-03-oxide-chemistry-md"></a>

# Chapter 3: Oxide Dissolution and Selectivity Budgets

The chemical objective is to dissolve the mold without consuming the films that keep the electrode array attached and separated. An aqueous bookkeeping reaction is SiO₂ + 6HF → H₂SiF₆ + 2H₂O. It balances atoms but does not specify the elementary mechanism or concentration dependence. Free HF, associated fluoride species, film composition, and solution conditions influence the observed rate.

## 3.1 Measure the actual films

Build an incoming-film matrix that includes deposition route, dopants, anneal history, density proxy, and storage history. A rate from thermal oxide is insufficient for an annealed doped mold. The same applies to nitride: its hydrogen content and deposition conditions may change release loss. Use coupons from the actual film process and periodically repeat the matrix after film changes.

Define selectivity S = R_oxide/R_support only when the rates refer to the same environment. Selectivity alone does not set support survival. A slowly clearing pocket extends exposure everywhere that is already open.

## 3.2 Convert exposure into a thickness budget

For a support attacked on both faces, t_remaining = t_initial − ∫R_top dt − ∫R_bottom dt. If both faces see a constant 1 nm/min for 1.75 min, a 50 nm sheet ends at 46.5 nm. This is a teaching case. The two faces often become exposed at different times; record the exposure chronology before using the symmetric shortcut.

A bottom stop attacked from above loses 1.75 nm in the same single-face example. Pinholes or exposed edges invalidate that one-face description because they permit undercut into underlying oxide. A thickness average cannot certify that no local breakthrough exists.

## 3.3 Published context

A Samsung patent describes HF solutions with anionic surfactants for oxide removal around nitride-supported cylindrical lower electrodes. It provides a historical example of treating selectivity and wetting together, not a validated formulation for this reference structure. [US20090023265A1](https://patents.google.com/patent/US20090023265A1/en)

## 3.4 Development experiment

Separate concentration, temperature, time, and film lot in the experiment. Measure cleared oxide, support loss, and electrode changes in the same split. An apparent rate gain is useful only if the release window also remains feasible. Include partially released samples to see when surfaces first encounter chemistry.

## Study questions

1. Why can two baths with equal selectivity produce different support loss?
2. Compute two-face loss at 1.5 nm/min for 2 min.
3. How would a pinhole change the stop-loss model?

---

[Previous](#book-chapters-02-reference-geometry-md) · [Index](#book-index-md) · [Next](#book-chapters-04-transport-access-md)



<a id="book-chapters-04-transport-access-md"></a>

# Chapter 4: Access, Wetting, and Moving Release Fronts

Removal proceeds through an evolving connected volume. At the start, access openings expose a limited oxide surface. As oxide retreats, new paths and surface area become available. A fully released geometry does not describe the transport geometry at the beginning of the etch.

## 4.1 Separate three delays

An observed clearance time includes entry and wetting, reaction-front propagation, and transport of reactants and products. A blocked opening is a connectivity failure. A trapped bubble is a wetting failure. A long connected narrow passage may be a transport limitation. These mechanisms can produce similar residual images but respond differently to more etch time.

For an idealized circular opening of diameter 50 nm on a 90 nm triangular lattice, the geometric open fraction is 27.99%. The distance from a Voronoi vertex to the opening edge is 90/√3 − 25 = 26.96 nm. This is a planar bound for a uniform unobstructed lattice. It says nothing by itself about buried vertical paths, missing openings, or overlap with electrode holes.

## 4.2 Use a front model honestly

For serial path segments with lengths L_i and assumed front rates v_i, t_front = ΣL_i/v_i. A 650 nm segment at 70 nm/min followed by a 760 nm segment at 600 nm/min takes 10.55 min. Those input rates are hypothetical. A 105 s release cannot be justified from this serial model. A real access etch that exposes both levels may shorten the relevant paths; reconstruct that geometry before changing the calculation.

The diffusion estimate t_D ≈ L²/D gives 0.64 ms for L = 0.8 µm and assumed D = 10⁻⁹ m²/s. This only estimates equilibration within an already filled fluid path. It does not prove that the moving front is reaction limited or that sufficient reagent reaches every surface.

## 4.3 Reagent consumption matters

For a one-dimensional approximation, compare supply D C/L with consumption ν n_s v, where C is dissolved reagent concentration, n_s is molar density of dissolving solid, and ν is stoichiometric consumption. Their ratio ν n_s v L/(D C) includes the concentration and solid inventory missing from the simple vL/D estimate. Network geometry, evolving area, and confinement still require calibration.

## Study questions

1. What evidence distinguishes a bubble from a blocked opening?
2. Recompute serial clearance if the slow segment is only 100 nm.
3. Why is a short diffusion time insufficient proof of complete release?

---

[Previous](#book-chapters-03-oxide-chemistry-md) · [Index](#book-index-md) · [Next](#book-chapters-05-wet-hardware-md)



<a id="book-chapters-05-wet-hardware-md"></a>

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

[Previous](#book-chapters-04-transport-access-md) · [Index](#book-index-md) · [Next](#book-chapters-06-vapor-hf-md)



<a id="book-chapters-06-vapor-hf-md"></a>

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

[Previous](#book-chapters-05-wet-hardware-md) · [Index](#book-index-md) · [Next](#book-chapters-07-rinse-exchange-md)



<a id="book-chapters-07-rinse-exchange-md"></a>

# Chapter 7: Rinse, Solvent Exchange, and Residue Control

Rinsing must remove the reaction environment from deep gaps while preserving a structure that no longer has oxide reinforcement. Chemical completion and fluid replacement are different endpoints. A wafer can be fully released yet retain contaminated liquid beneath a support.

## 7.1 Exchange has a distribution

An ideal stirred compartment reduces concentration as C/C₀ = exp(−Qt/V). Five volume exchanges leave 0.00674 of the original concentration. This model assumes instant mixing and no adsorption, reaction, or isolated pockets. It describes a teaching compartment, not a wafer-specific rinse recipe.

A more useful experimental design measures a tracer washout curve on an appropriate surrogate and compares it with actual surface residue after processing. A long washout tail indicates regions poorly described by a single well-mixed volume. Increasing nominal flow may bypass those regions rather than improve their exchange.

## 7.2 Manage the liquid sequence

Track which liquid fills the gap during each transition. The wetting behavior relevant to entry can differ from that relevant to a retreating meniscus. Partial drying before exchange can create adhesion that later low-surface-tension fluid does not reverse.

Surface modification is an integration option requiring compatibility with dielectric deposition. A treatment that reduces wetting forces may also obstruct nucleation or leave an interfacial film. Evaluate both structural and electrical responses before adopting it.

## 7.3 Residue diagnosis

Map residues by location and chemical composition. Material concentrated at wafer edges suggests a different transport history from residue consistently beneath middle supports. Sample handling can introduce oxidation, redeposition, or carbon contamination; retain handling controls and unprocessed references.

Develop a mass-balance interpretation where possible: identify likely incoming sources, reaction products, removal paths, and analytical detection limits. An undetected species is bounded by the measurement method, not proven absent.

## Worked comparison

If Q/V doubles, the ideal time to a fixed C/C₀ halves. If the actual tail remains unchanged, the limiting feature is probably outside the stirred-compartment approximation. Test access and adsorption before treating a flow increase as a complete solution.

## Study questions

1. Compute the remaining fraction after three ideal exchanges.
2. Why might residue persist despite higher dispense flow?
3. What downstream response must accompany a surface-modification split?

---

[Previous](#book-chapters-06-vapor-hf-md) · [Index](#book-index-md) · [Next](#book-chapters-08-drying-mechanics-md)



<a id="book-chapters-08-drying-mechanics-md"></a>

# Chapter 8: Drying and Elastocapillary Stability

The largest mechanical load may occur after chemical clearance. A liquid bridge can pull neighboring electrodes together as the gap drains. Once contact produces adhesion, restoring the original spacing can be difficult even after the meniscus disappears.

## 8.1 Pressure scale and beam scale

For an ideal slit, ΔP ≈ 2γ cosθ/g. With assumed water surface tension 0.072 N/m, θ = 0°, and g = 17 nm, the pressure scale is 8.47 MPa. This is an illustrative curvature model. A real pillar meniscus has three-dimensional curvature, nonuniform wetting, and time-dependent contact lines.

For a solid circular beam, I = πd⁴/64. A cantilever under a tip force obeys δ = FL³/(3EI). Taking d = 28 nm, E = 400 GPa, L = 760 nm, and F = 1 nN gives δ = 12.12 nm. E and F are assumptions. The nitride-connected pillar is not necessarily a cantilever: lattice motion, attachment rotation, and load distribution change compliance.

For the same tip load, shortening L from 760 to 650 nm reduces deflection by (650/760)³ = 0.625. For a fixed distributed load per length the dependence is L⁴. Always state what load is held fixed when discussing height scaling.

## 8.2 Drying route selection

A published nanostructure study reports supercritical CO₂ drying as a route to avoid collapse in fine silicon patterns and identifies water contamination as relevant to resist deformation. This is evidence for the mechanism and studied structures, not DRAM production qualification. [Namatsu, Supercritical Drying for Nanostructure Fabrication](https://www.jstage.jst.go.jp/article/photopolymer1988/15/3/15_3_381/_article)

The engineering decision is whether the complete exchange and drying path preserves this electrode/support stack. Include pressure transitions, retained fluid, temperature exposure, and contamination in the qualification. Solvent-assisted, supercritical, and other routes need comparable outgoing measures.

## 8.3 Avoid a universal collapse threshold

A simple deflection estimate screens sensitivity. It cannot establish a universal gap fraction at which every array collapses. Pair coupling, adhesion, meniscus evolution, tube walls, and support motion affect stability. Use the calculation to choose experiments and compare trends, then calibrate with patterned data.

## Study questions

1. How does doubling a solid pillar diameter change I?
2. Why does a distributed load scale differently from a tip load?
3. What evidence is needed beyond a zero-bridge image?

---

[Previous](#book-chapters-07-rinse-exchange-md) · [Index](#book-index-md) · [Next](#book-chapters-09-delivery-control-md)



<a id="book-chapters-09-delivery-control-md"></a>

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

[Previous](#book-chapters-08-drying-mechanics-md) · [Index](#book-index-md) · [Next](#book-chapters-10-support-survival-md)



<a id="book-chapters-10-support-survival-md"></a>

# Chapter 10: Support Survival and Exposure Chronology

Supports have to survive while becoming mechanically active. Their local thickness, ligament width, stress, attachments, and exposure history jointly determine whether the released array remains stable.

## 10.1 Thickness is only one dimension

A support sheet losing material from both faces becomes thinner. The edges of an opening can also retreat, narrowing ligaments. For an initial ligament width w₀ and uniform lateral retreat ℓ at each edge, w = w₀ − 2ℓ. A 20 nm ligament with 2 nm retreat per edge becomes 16 nm wide. Simultaneous thickness loss multiplies the reduction in section area.

As a screening example, a 50 nm by 20 nm section has area 1000 nm². A 46.5 nm by 16 nm section has area 744 nm². Under the same tensile force, average stress rises by 1000/744 = 1.344. This ignores stress concentration and load redistribution, so it cannot certify strength.

## 10.2 Integrate exposed time

An upper support can encounter chemistry before a lower sheet. The lower face may become accessible only as oxide beneath it retreats. Express each loss as an integral over its local exposure rather than multiplying the full release time by two for all supports.

Build a sequence of partial-release cross-sections and pair it with film-rate measurements. Use this to bound remaining section at early, nominal, and extended dwell. Where residual oxide mechanically masks a weakness, inspect again after complete release.

## 10.3 Failure clusters

A broken attachment can redistribute load to its neighbors. A local ligament fracture can thus create a cluster larger than the first structural defect. Use spatial correlation and orientation in inspection maps. An independent single-pillar defect model may substantially understate the consequences of connected support damage.

Separate array-interior failures from edge anchoring failures. Edge regions have different load paths and access conditions; measuring only the center may miss the dominant release weakness.

## Study questions

1. Compute section-area loss if thickness becomes 44 nm and width 14 nm.
2. Why can incomplete release hide support weakness?
3. Which observation would distinguish isolated damage from load redistribution?

---

[Previous](#book-chapters-09-delivery-control-md) · [Index](#book-index-md) · [Next](#book-chapters-11-electrode-surface-md)



<a id="book-chapters-11-electrode-surface-md"></a>

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

[Previous](#book-chapters-10-support-survival-md) · [Index](#book-index-md) · [Next](#book-chapters-12-residual-stop-md)



<a id="book-chapters-12-residual-stop-md"></a>

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

[Previous](#book-chapters-11-electrode-surface-md) · [Index](#book-index-md) · [Next](#book-chapters-13-failure-statistics-md)



<a id="book-chapters-13-failure-statistics-md"></a>

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

[Previous](#book-chapters-12-residual-stop-md) · [Index](#book-index-md) · [Next](#book-chapters-14-alternative-molds-md)



<a id="book-chapters-14-alternative-molds-md"></a>

# Chapter 14: Sequential Release and Alternative Sacrificial Molds

Taller structures can force a redesign of both mechanical support and access. Sequential release changes which regions are unsupported at each stage. Alternative mold materials change the reaction products and the electrode compatibility question.

## 14.1 Sequence is a mechanical variable

Compare a single release with a staged flow using a diagram of retained oxide and active supports after every step. A partially retained mold may temporarily stabilize one region while another is released. It may also impede access or constrain the subsequent support operation.

A staged flow is attractive only if the complete sequence preserves electrodes, avoids residue, and has a feasible process window at each stage. Add the transition and queue exposure from the extra operations to the qualification, rather than comparing only nominal etch times.

## 14.2 Carbon-mold evidence

Applied Materials' published application discloses carbon capacitor molds removed by isotropic radical exposure involving oxygen, nitrogen, hydrogen, ammonia, or combinations. It motivates the route partly through oxide-release-related support consumption. This is a disclosed proposal, not evidence that the present reference design is qualified in production. [US20240038833A1](https://patents.google.com/patent/US20240038833A1/en)

The engineering questions are how well the candidate carbon molds pattern, how the electrode nucleates on them, which radicals reach buried regions, and how exposed electrodes and support films change. A dry route removes one liquid-transition concern while introducing its own chemical and transport limits.

## 14.3 Compare full flows

| Question | Oxide baseline | Candidate alternative |
|---|---|---|
| Mold patternability | Characterize taper and residues | Repeat on new film |
| Electrode formation | Established incoming baseline | Check nucleation and continuity |
| Release completeness | Inspect last oxide | Identify last candidate mold |
| Surface handoff | Validate interface | Repeat dielectric qualification |
| Economics | Total accepted-wafer cost | Include added upstream costs |

Alternative materials should be compared using a common acceptance contract. A faster release does not compensate for poorer capacitor-hole patterning or lower dielectric yield.

## Study questions

1. What temporary mechanical advantage might staged release provide?
2. Why is carbon radical removal not a drop-in wet-process replacement?
3. Which upstream module must enter the route comparison?

---

[Previous](#book-chapters-13-failure-statistics-md) · [Index](#book-index-md) · [Next](#book-chapters-15-metrology-qualification-md)



<a id="book-chapters-15-metrology-qualification-md"></a>

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

[Previous](#book-chapters-14-alternative-molds-md) · [Index](#book-index-md) · [Next](#book-chapters-16-integration-economics-md)



<a id="book-chapters-16-integration-economics-md"></a>

# Chapter 16: Integration, Yield, and Cost of Accepted Wafers

The economic output is a wafer accepted for subsequent capacitor formation. Nominal throughput is useful, but incomplete release, structural defects, rework, maintenance, and downstream loss all change the effective cost.

## 16.1 Use a consistent denominator

Let hourly operating cost be K, actual completed wafers per hour be W, consumables per processed wafer be c, and acceptance fraction be Y. A simple model is cost per accepted wafer = (K/W + c)/Y. Define whether K includes depreciation, maintenance, labor, utilities, and facilities. Do not compare vendors using different cost scopes.

For hypothetical K = $600/h, W = 60 wafers/h, c = $2/wafer, and Y = 0.98, the result is $12.24 per accepted wafer. These are illustrative economics, not a supplier quote. At Y = 0.95 the cost becomes $12.63. Downstream device yield is not included in this module-only calculation.

## 16.2 Compare a yield-enhancing route

A route costing $14 per processed wafer at Y = 0.995 costs $14.07 per accepted wafer. Against the $12 baseline process, it breaks even on module acceptance cost only when the baseline Y is below 12/(14/0.995) = 0.8529. A better device yield can justify it earlier, but then the comparison must include downstream value and downstream loss explicitly.

## 16.3 Capacity and risk

A 300 s chamber cycle gives an ideal 12 wafers/h per chamber, before availability and utilization. Five such chambers give an ideal 60 wafers/h only when shared handling and utilities do not constrain them. Batch tools need a different loading and cycle accounting model.

Queue delays can become interface risk if increased throughput at one tool creates a bottleneck before dielectric deposition. Include this coupling in capacity planning. Do not optimize release throughput while silently violating the handoff queue specification.

## 16.4 Release record

A production release package should include the acceptance contract, incoming envelope, compatibility evidence, clearance and loss window, drying qualification, downstream interface response, repeatability data, and control plan. The educational reference book supplies the reasoning and calculation templates; manufacturing acceptance requires measured data for the chosen stack.

## Study questions

1. Calculate accepted-wafer cost at 50 wafers/h and Y = 0.98.
2. What downstream value is missing from the module-only comparison?
3. Why can a throughput improvement worsen interface yield?

---

[Previous](#book-chapters-15-metrology-qualification-md) · [Index](#book-index-md) · [Appendices](#book-index-md)



<a id="book-appendices-a-material-properties-md"></a>

# Appendix A: Geometry, Materials, and Assumption Register

| Input | Value | Evidence status | Boundary |
|---|---:|---|---|
| Triangular pitch | 45 nm | Series-inspired teaching geometry | No node attribution |
| Constant pillar diameter | 28 nm | Teaching simplification | Real local taper excluded |
| Overall height | 1600 nm | Geometry convention | Includes 20 nm stop |
| Oxide regions | 650 + 760 nm | Series-inspired model | Actual access paths must be reconstructed |
| Support thicknesses | 120 + 50 nm | Series-inspired model | Initial values before release |
| Bottom stop | 20 nm | Model input | Separate from 1580 nm stack |
| TiN modulus E | 400 GPa | Assumed | Film microstructure and tube walls excluded |
| Oxide front rates | 70 and 600 nm/min | Hypothetical example | No recipe or concentration implied |
| Support/stop attack | 1 nm/min per exposed face | Hypothetical example | Exposure chronology required |
| Effective diffusion coefficient | 10⁻⁹ m²/s | Assumed | Filled aqueous path only |
| Water surface tension | 0.072 N/m | Rounded teaching input | Temperature and contamination excluded |
| Baseline EOT | 0.50 nm | Assumed device model | Uniform dielectric and accessible area |
| Oxide density | 2200 kg/m³ | Assumed inventory value | Actual mold density may differ |
| Oxide molar mass | 0.0600843 kg/mol | Rounded formula value | SiO₂ accounting |

The stack closes as 120 + 650 + 50 + 760 + 20 = 1600 nm. Exposed sidewall height is modeled as the two oxide regions, 1410 nm. Support-open material already removed must be subtracted when calculating chemical loading.

No commercial dielectric, electrode, or support film is certified by these values. Replace geometry with measured local values and properties with stack-specific data before using a model for acceptance.

[Index](#book-index-md)



<a id="book-appendices-b-chemistry-reaction-data-md"></a>

# Appendix B: Reaction Accounting and Chemistry Evidence

## Aqueous oxide balance

SiO₂ + 6HF → H₂SiF₆ + 2H₂O is an atom-balanced aqueous accounting equation. It is not an elementary reaction. Gas-phase product speciation and aqueous fluoride equilibria require their own models.

For oxide volume V, assumed density ρ, and molar mass M, n_oxide = ρV/M. The balanced reaction gives a stoichiometric 6n_oxide HF accounting requirement. Delivered process consumption includes excess chemical, replacement, and other reactive materials.

## Selectivity measurements

Use R_oxide/R_support from actual films in the same environment. Record concentration measurement method, temperature, agitation or delivery, loading, film history, and interval used to extract each rate. Short tests can be dominated by entry transients or analytical resolution. Long tests can hide early nonlinear changes.

Measure electrode responses separately; an electrode may undergo surface modification with little apparent bulk thickness loss. A favorable oxide:nitride ratio does not establish electrode compatibility.

## Source scope

- [US20090023265A1](https://patents.google.com/patent/US20090023265A1/en): historical disclosure of HF/surfactant oxide removal for supported capacitor structures. No formulation is prescribed here.
- [EPFL vapor-HF documentation](https://www.epfl.ch/research/facilities/cmi/equipment/etching/spts-uetch/): tool-specific compatibility restrictions. Chapter 6 explains why a MEMS capability does not establish TiN DRAM compatibility.
- [US20240038833A1](https://patents.google.com/patent/US20240038833A1/en): alternative carbon mold disclosed with radical removal. Chapter 14 separates disclosure from qualification.

[Index](#book-index-md)



<a id="book-appendices-c-qualification-workflow-md"></a>

# Appendix C: Qualification Workflow and Data Record

This is a development workflow, not an operating recipe. Chemical handling and equipment operation belong to the facility's approved procedures.

## Stage 1: Incoming structure

Record film identities and histories, support and stop thickness distributions, electrode continuity, taper, access-opening condition, and edge layout. Retain an incoming structural control. Resolve missing access or stop damage before attributing a later result to release chemistry.

## Stage 2: Compatibility

Expose actual film witnesses to candidate environments. Measure thickness and relevant electrical or surface responses. Progress to patterned specimens only when the material gate has an agreed criterion and supporting evidence.

## Stage 3: Moving front and loss window

Use partial-release splits to identify access and exposure chronology. Measure the local clearance distribution and loss at early-exposed films. Establish the overlap between worst-case clearance and maximum permissible loss. An empty overlap is an integration issue, not a reason to choose an arbitrary overetch.

## Stage 4: Transitions and drying

Compare complete sequences with matched incoming structures. Preserve timestamps and transitions. Inspect structure after drying and again after downstream deposition to catch later movement.

## Stage 5: Electrical and repeatability gates

Evaluate capacitance, bridges, leakage, and retention distributions. Repeat across film lots and chambers inside the proposed incoming envelope. State sampling denominators and confidence limits. Freeze the demonstrated envelope and the response plan for deviations.

## Minimum traveler fields

| Group | Fields |
|---|---|
| Identity | Wafer, incoming lot, film lots, tool, chamber |
| Incoming | Local geometry, film history, access status, stop condition |
| Exposure | Recipe revision, delivered conditions, start/end events |
| Transitions | Rinse entry, exchange completion, dry entry/end, unload |
| Handoff | Storage environment, queue duration, dielectric lot |
| Evidence | Sample sites, method, detection limits, raw data references |
| Disposition | Gate results, exceptions, owner, control-plan revision |

[Index](#book-index-md)



<a id="book-appendices-d-process-windows-md"></a>

# Appendix D: Clearance and Preservation Windows

Define clearance lower bound t_clear at the specified worst incoming condition. For film j, define loss as L_j(t) = ∫a_j(τ)R_j(τ)dτ, where a_j represents exposed faces or local exposure. The upper bound is the earliest time any required remaining-film criterion is violated.

## Constant-rate teaching case

| Constraint | Assumption | Bound |
|---|---|---:|
| Clearance | Measured-equivalent example lower bound | t ≥ 1.2 min |
| Middle support | 50 nm initial; ≥44 nm; two faces at 1 nm/min | t ≤ 3 min |
| Stop | 20 nm initial; ≥18 nm; one face at 1 nm/min | t ≤ 2 min |

Nominal feasible interval: 1.2–2.0 min. These thresholds are hypothetical, not production specifications.

If clearance rate falls by 20%, t_clear becomes 1.5 min. If stop loss rises by 20%, its bound becomes 2/1.2 = 1.667 min. The revised feasible interval is 1.5–1.667 min. Nominal 1.75 min fails this combined case.

## Delayed exposure

If a stop first sees chemistry at t₀ and the single-face rate is constant, its loss is R max(0, t−t₀). The allowable total time is then t₀ + loss_budget/R. A locally early-exposed defect can have a much smaller t₀ than the wafer-average geometry.

## Decision rule

Change time only within a demonstrated window. If no interval remains, investigate access, chemistry selectivity, film properties, and sequence. Adding supports may reduce free spans but also adds material to pattern and more surfaces whose survival must be qualified.

[Index](#book-index-md)



<a id="book-appendices-e-worked-calculations-md"></a>

# Appendix E: Worked Calculations and Selected Answers

Run `python scripts/calculations.py` from the repository root to reproduce the numerical model. SI units are used inside the mechanical and capacitance calculations; geometric summaries report nanometers and micrometers.

## E.1 Geometry

A_cell = √3(45 nm)²/2 = 1753.70 nm². Density = 10⁶/A_cell = 570.22 pillars/µm². Gap = 45−28 = 17 nm. At 42 nm pitch the density becomes 654.59 pillars/µm².

The 50 nm opening on a 90 nm triangular pitch gives π25²/(√3·90²/2) = 0.2799 open fraction. This planar calculation ignores overlap with pillars and missing openings.

## E.2 Exposed area and capacitance

For d = 28 nm and H_exposed = 1410 nm, A = πdH = 0.12403 µm². Using ε₀ = 8.8541878128×10⁻¹² F/m and SiO₂ relative permittivity 3.9, C = ε₀·3.9·A/EOT. At EOT = 0.50 nm, C = 8.57 fF. This is a thin-dielectric area approximation, not a cylinder's exact electrostatic solution.

For f = 0.10, t = 2 nm, and e = 0.50 nm, C/C₀ = 1−f+fe/(e+t) = 0.92. At f = 0.25, C/C₀ = 0.80. Thus local and whole-cell losses must be distinguished.

## E.3 Front timing

650/70 + 760/600 = 10.55 min for serial segments. Reducing the slow segment to 100 nm gives 100/70 + 760/600 = 2.70 min. Actual access geometry determines whether either serial construction is applicable.

L²/D = (0.8×10⁻⁶)²/10⁻⁹ = 0.00064 s. This is a filled-path diffusion estimate and does not close the reagent-supply balance.

## E.4 Mechanics

I = π(28×10⁻⁹)⁴/64 = 3.017×10⁻³² m⁴. With E = 400 GPa, F = 1 nN, and L = 760 nm, δ = FL³/(3EI) = 12.12 nm. Doubling solid diameter increases I sixteenfold. Hollow tubes require the difference of outer and inner fourth powers.

The pressure scale 2γ/g with γ = 0.072 N/m and g = 17 nm is 8.47 MPa. It is not a uniform actual pillar pressure.

A support section reduced from 50×20 to 46.5×16 nm² retains 74.4% of its area; the same force gives 1.344 times average stress. At 44×14 nm² the retained area is 61.6% and stress multiplier is 1.623.

## E.5 Exposure and exchange

Two faces at 1.5 nm/min for 2 min remove 6 nm total. Three ideal well-mixed rinse exchanges leave exp(−3) = 0.0498 of initial concentration; five leave 0.00674.

## E.6 Rare events and economics

Zero observations in 10⁷ independent trials give a 95% upper probability near 2.996×10⁻⁷. Required zero-event trials to bound 10⁻⁹ are about 2.996 billion.

2³⁴×10⁻⁹ = 17.18 expected affected cells under an independent per-cell model. With no repair, exp(−17.18) ≈ 3.46×10⁻⁸ zero-event probability.

At $600/h, 50 wafers/h, $2 consumables/wafer, and Y = 0.98, accepted-wafer cost is ($12+$2)/0.98 = $14.29. The nominal 60 wafers/h case gives $12.24.

## E.7 Interpreting nonnumerical questions

Incoming polymer scum can mimic slow chemistry by blocking access. Blanket rates do not prove buried clearance. Patterned compatibility follows blanket tests because buried paths and products are absent from coupons. Support fractures introduce correlated defects. A safe dwell controller remains within measured clearance and preservation bounds and rejects conditions for which no correction has been demonstrated.

[Index](#book-index-md)



<a id="book-appendices-f-metrology-reference-md"></a>

# Appendix F: Metrology and Sampling Reference

## Evidence matrix

| Failure hypothesis | Structural evidence | Chemical/electrical evidence | Main caveat |
|---|---|---|---|
| Buried residual mold | Targeted cross-section | Chemical mapping and capacitance | Oxygen has multiple sources |
| Premature meniscus | Tilt and bridge orientation | Transition logs, shorts | Correlation is not unique attribution |
| Support erosion | Thickness, ligament, attachment | Loss-vs-time splits | Average thickness misses local damage |
| Stop breakthrough | Bottom section and undercut | Landing connectivity | Sparse sampling misses pinholes |
| Electrode interface change | Wall geometry, roughness | Surface analysis and leakage | Handling can alter the surface |
| Downstream movement | Pre/post-deposition comparison | New shorts after plate | Requires matched identification |

## Sampling protocol

Name the event being counted, the area sampled, the number of effective independent units, and detection sensitivity. Sample edge, center, and known access-risk sites. Use targeted samples for mechanism and randomized or stratified samples for population claims. Do not combine the two without describing the selection rule.

For perfect detection and independent rare events, zero observations bound q by approximately −ln(0.05)/n at 95% confidence. Imperfect detection reduces what can be concluded. Clustered failures require an explicit region or cluster model rather than simply enlarging n by counting every correlated pillar.

## Measurement system checks

Repeat selected measurements across operators or analysis settings where practical. Preserve preparation conditions and raw images. Identify the minimum residual thickness, tilt, or bridge feature that the chosen method can reliably detect. A pass criterion below the detection limit is not a meaningful acceptance gate.

[Index](#book-index-md)



<a id="book-appendices-g-troubleshooting-guide-md"></a>

# Appendix G: Troubleshooting Guide

| Symptom | Competing causes | Discriminating check | Controlled next action |
|---|---|---|---|
| Residue beneath middle support | Slow front, blocked access, retained product | Partial-release sections plus chemical mapping | Fix access or qualify a bounded dwell split |
| Bridge stripes after drying | Directional meniscus, support failure | Orientation vs drain history and attachments | Compare complete transition/dry sequences |
| Array-edge clusters | Anchoring weakness, access variation | Edge vs interior structural sections | Qualify edge geometry and support budget |
| Capacitance loss without bridges | Residual film, inaccessible area, interface change | Cross-section, surface analysis, dielectric splits | Separate geometry and chemistry variables |
| Leakage tail after long queue | Surface change, contamination, unrelated dielectric drift | Matched queue controls with fixed dielectric | Define measured handoff limit |
| Bottom undercut | Stop pinhole, excess exposure, access landing error | Incoming stop and post-release bottom section | Address incoming damage and exposure bounds |
| Vapor-route electrode change | Stack incompatibility, local products | Actual film witnesses and patterned coupons | Stop route progression until compatibility closes |
| Chamber-to-chamber difference | Delivery, temperature, loading, transition history | Shared lot with complete traces | Match physical exposure and outgoing responses |

Troubleshooting starts with a competing-cause list and a test that distinguishes the causes. More time is appropriate only when incomplete reaction is demonstrated and remaining-film budgets permit it. It is ineffective for some connectivity failures and damaging to already released regions.

[Index](#book-index-md)



<a id="book-glossary-md"></a>

# Glossary

| Term | Meaning in this book |
|---|---|
| Access opening | Patterned path allowing removal chemistry to reach mold |
| ALD | Atomic layer deposition; downstream dielectric formation method |
| APC | Advanced process control; bounded corrections using measured state |
| Array | Repeated storage-node region |
| BPSG | Borophosphosilicate glass; a possible doped oxide mold |
| Bottom electrode | Storage-node conductor exposed by release |
| Bottom stop | Film protecting material beneath the mold |
| Bridge | Unintended connection between neighboring structures |
| Clearance | Removal of intended mold from a specified region |
| Cluster | Spatially correlated group of defects |
| Compatibility | Acceptable response of the actual films to a process environment |
| COO | Cost of ownership; its scope must be defined |
| Cylinder | Hollow electrode; distinct from the solid-beam teaching model |
| DHF | Diluted hydrofluoric acid |
| EOT | Equivalent oxide thickness, expressed as SiO₂-equivalent thickness |
| Exposure chronology | When each local surface begins and ends chemical exposure |
| Feed-forward | Adjustment based on measured incoming conditions |
| HF | Hydrogen fluoride; aqueous solution is hydrofluoric acid |
| Ligament | Remaining support material between openings |
| Loading | Reactive material exposed to a process environment |
| Meniscus | Curved liquid interface that can exert capillary force |
| Mold | Sacrificial material defining electrode shape during formation |
| Moving front | Boundary between removed and remaining mold |
| Pillar | Upright electrode; solid in the simple mechanics example |
| Plate | Counterelectrode deposited after capacitor dielectric |
| Release | Mold removal and preservation of the intended structure |
| Selectivity | Ratio of specified material-removal rates in a common environment |
| Stiction | Adhesion after structures contact during or after release |
| Support | Retained film that mechanically connects electrodes |
| TEOS | Tetraethyl orthosilicate; precursor associated with some oxide films |
| TiN | Titanium nitride; example bottom-electrode material |
| Vapor HF | Gas-delivered oxide-removal route requiring material validation |
| Wet-to-wet | Transfer or transition keeping the structure liquid-covered |

[Index](#book-index-md)



<a id="book-references-md"></a>

# References and Evidence Map

Sources accessed during the 2026-10-04–2026-10-05 research session. Links identify narrow source-supported statements. Numerical teaching models elsewhere are derived calculations or declared assumptions. Patent status and legal scope are not assessed here.

| ID | Primary source | Supports | Does not establish |
|---|---|---|---|
| R1 | [Samsung, US20090023265A1: Etching solution for removal of oxide film](https://patents.google.com/patent/US20090023265A1/en), published 2009-01-22 | HF/surfactant disclosure for oxide removal with supported capacitor electrodes; Chapter 3 | A qualified modern recipe |
| R2 | [Hynix, US7498267B2: Method for forming semiconductor memory capacitor without cell-to-cell bridges](https://patents.google.com/patent/US7498267B2/en), published 2009-03-03 | Integrated removal/rinse/dry disclosure; Chapter 5 | Elimination of all collapse modes |
| R3 | [EPFL CMi: SPTS uEtch](https://www.epfl.ch/research/facilities/cmi/equipment/etching/spts-uetch/) | Vapor-HF implementation, loading/water behavior, and tool-specific TiN restrictions; Chapter 6 | DRAM-stack compatibility on other equipment |
| R4 | [H. Namatsu, Supercritical Drying for Nanostructure Fabrication](https://www.jstage.jst.go.jp/article/photopolymer1988/15/3/15_3_381/_article), Journal of Photopolymer Science and Technology 15(3), 381–388 (2002), DOI 10.2494/photopolymer.15.381 | Supercritical CO₂ mechanism and studied nanostructures; Chapter 8 | Production qualification for this DRAM stack |
| R5 | [Applied Materials, US20240038833A1: Carbon mold for DRAM capacitor](https://patents.google.com/patent/US20240038833A1/en), published 2024-02-01 | Carbon mold and isotropic radical-removal proposal; Chapter 14 | Production adoption or interchangeable recipes |

## Series context

- [DRAM Capacitor Mold Etch](https://github.com/chipfoundryservices/dram-capacitor-mold-etch): organizational and reference-geometry context.
- [DRAM Capacitor Support Layer Etch](https://github.com/chipfoundryservices/dram-capacitor-support-layer-etch): dedicated support-open scope.

The series is a structural reference, not independent validation of the new book's numerical assumptions. No measured commercial etch rates, yield targets, or vendor prices are inferred from it.
