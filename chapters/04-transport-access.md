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

[Previous](./03-oxide-chemistry.md) · [Index](../INDEX.md) · [Next](./05-wet-hardware.md)
