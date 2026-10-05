# Research and Editorial Decisions

## Repository inspection

The target remote was empty at initial inspection. SSH authenticated as the chipfoundryservices account through its configured identity; private keys and tokens were neither read into the book nor copied into this repository.

Read-only sibling clones were inspected at these revisions:

- DRAM Capacitor Mold Etch: `19f5974b9f2633ea5f68763da553b68ff8a0c240`. Reviewed README, preface, index, release chemistry and geometry context. The layout contains front matter, 16 chapters in four parts, and appendices A–G.
- DRAM Capacitor Support Layer Etch: `c8dc0db215987c71e7b2f716402726b155b7d72c`. The inspected revision contains 16 chapter files. Reviewed support-role geometry and dedicated support-open scope. The incomplete front matter in this revision was not treated as a completed template.

## Scope decision

The user confirmed creating only dram-sacrificial-capacitor-mold-removal. The volume begins after access opening and covers complete release, structural preservation, surfaces, qualification, and economics. No series number is assigned because a maintained catalog establishing the new slot was not available.

## Primary-source findings

The [evidence map](../REFERENCES.md) records five primary publications/disclosures. Their narrow supported claims appear beside the relevant chapter text. The search included oxide/HF capacitor release, integrated wet processing, vapor HF, supercritical drying, and carbon molds. Public evidence was checked before drafting. No proprietary production recipe, vendor quote, or node-specific yield specification was available.

Vapor-HF compatibility is a material gate: EPFL's published implementation restricts TiN. Its capability cannot be used as evidence that a TiN DRAM stack is compatible. Carbon-mold radical removal is a patent proposal; it is not represented as production adoption.

## Independently checked corrections

- A 45 nm triangular pitch gives 1753.70 nm² per cell and 570.22 pillars/µm².
- The inherited mold/support stack sums to 1580 nm; the 20 nm stop completes 1600 nm. Exposed sidewall height is conservatively 1410 nm.
- A serial 650 nm path at 70 nm/min plus 760 nm at 600 nm/min takes 10.55 min. A shorter claimed release requires a different access geometry and measured rates.
- Support loss must integrate exposure separately for each face; stop breakthrough cannot be excluded from average thickness alone.
- A residue covering 10% of the active surface and losing 80% of local capacitance loses 8% of total capacitance in the stated model.
- Zero observed failures does not certify a one-per-billion rate without a sufficient denominator and detection model.
- Cantilever calculations are screening models. The book does not assert a universal pair-collapse threshold for a connected lattice.

## Remaining evidence boundaries

The educational edition is complete, but the example reference stack is unqualified for manufacturing. Stack-specific chemistry rates, actual material compatibility, electrode-interface response, lattice mechanics, repair architecture, and production defect distributions require measured data. The text identifies those gaps where they affect decisions.
