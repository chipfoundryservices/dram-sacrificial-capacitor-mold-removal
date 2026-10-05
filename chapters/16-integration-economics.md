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

[Previous](./15-metrology-qualification.md) · [Index](../INDEX.md) · [Appendices](../INDEX.md)
