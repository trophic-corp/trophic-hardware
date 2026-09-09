# EDR-001 — Four tiers at 300/700/1100/1500 mm; bed datum is the deck mesh top face

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A |

## Context

Multiple candidate datums exist for a bed height — the beam top, the deck rail top, the mesh top, the tray floor, the water surface. Early work used them inconsistently, which put nozzle heights, LED clearances and drain falls into disagreement.

## Decision

**The bed datum is the top face of the deck mesh panel.** Bed datums are at Z = 300, 700, 1100 and 1500 mm; tier pitch is 400 mm.

The stack below each datum is fixed and must not be varied independently:

| Element | Z range, first tier |
|---|---|
| Beam | 243.4 - 273.4 |
| Deck rail | 273.4 - 298.4 |
| Deck mesh panel | 298.4 - **300.0** |
| Tray | from 300.0 |

## Consequences

- Every downstream height — nozzle elevation, LED hanging height, drain fall, overflow collar — is measured from this datum and only this datum.
- The 400 mm pitch and the 300 mm first datum together set the 1500 mm top bed, which is what EDR-002 tests against reach limits.
- Changing the deck build-up changes every bed datum. It is a frozen interface, not a detail.

## Evidence

`RK-A-SYS_Rev2`; `RK-A-DWG_Rev2`
