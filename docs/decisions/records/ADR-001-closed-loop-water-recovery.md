# ADR-001 — Replace drain-to-waste with closed-loop water recovery

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A, RK-A-WRS, RK-A-ROOM |

## Context

The original irrigation configuration was drain-to-waste: irrigation water passing through the beds was discharged. At room scale this is 632 m3/year of discharge for an 11-rack room, in a location where water is neither free nor unlimited, and it discards nutrient solution that is still within reuse parameters for most of its life.

## Decision

Collect bed drainage, return it to a dedicated recovery reservoir, and make the reuse decision on water quality rather than on time:

1. **Discard** when EC, pH, contamination risk or another monitored parameter makes reuse unsuitable.
2. **Return to the main source reservoir** when the water is within the defined reuse parameters.

The diverter that makes this decision is `FV-01`. Its fail-safe position is *to waste* (EDR-007) — the system discards on failure rather than contaminating the source.

## Consequences

- Recovery ratio 87.7 % at 11 racks / 44 beds: 1,914 L/day circulated, 88.9 L consumed, 146 L blowdown, 235 L make-up.
- Annual discharge falls from 632 m3 to 48.2 m3 — **554 m3/year saved**.
- Introduces a water-quality monitoring obligation the drain-to-waste design did not have (EC, pH, and monthly iron once UV-C is in the loop — EDR-009).
- Introduces the recovery skid, its pumps and instrumentation as **shared CEA infrastructure**, not rack hardware (ADR-003).
- Capital cost: recovery stage R1 Rs 145,250; stage R2 a further Rs 94,600.

## Evidence

`products/cea/irrigation/water-recovery/RK-A-WRS_Rev3_closed-loop-water-recovery.html`
