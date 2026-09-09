# EDR-009 — Fe-DTPA or Fe-EDDHA under UV-C, not Fe-EDTA

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A-WRS |

## Context

UV-C sterilisation in the recovery loop degrades Fe-EDTA, the most common and cheapest iron chelate. The failure is quiet: iron precipitates, the plants show deficiency, and the nutrient dosing looks correct on paper because the iron was added.

## Decision

Where UV-C is in the loop, specify **Fe-DTPA or Fe-EDDHA**. Verify dissolved iron **monthly**.

## Consequences

- Nutrient cost rises; Fe-EDDHA in particular is materially more expensive than Fe-EDTA.
- Adds a recurring analytical obligation to operations, not just a one-time specification.
- Constrains the nutrient specification only. No rack hardware consequence.
- This is the kind of coupling that only appears once the loop is closed — it did not exist under drain-to-waste.

## Evidence

`RK-A-WRS_Rev3`
