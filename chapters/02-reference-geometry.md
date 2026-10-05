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

[Previous](./01-release-module.md) · [Index](../INDEX.md) · [Next](./03-oxide-chemistry.md)
