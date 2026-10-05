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

[Index](../INDEX.md)
