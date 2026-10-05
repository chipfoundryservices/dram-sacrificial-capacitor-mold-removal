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

[Preface](../PREFACE.md) · [Index](../INDEX.md) · [Next](./02-reference-geometry.md)
