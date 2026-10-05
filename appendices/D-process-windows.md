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

[Index](../INDEX.md)
