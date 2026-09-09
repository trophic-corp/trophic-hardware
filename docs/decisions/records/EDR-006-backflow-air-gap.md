# EDR-006 — 100 mm air gap at the rack drain outlet, never plumbed closed

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A, RK-A-WRS |

## Context

A closed-loop recovery system connects used bed water back toward a source reservoir. Without a physical break, a pressure event or a blocked drain can drive contaminated water back into the supply.

## Decision

Maintain a **100 mm air gap** between the rack drain header outlet (Z 200) and the tundish rim (Z 100). That is **2 x DN50**, satisfying IS 12234 / EN 1717 for a Type AA/AB air gap.

**This gap must never be plumbed closed.** No revision, no site modification, no 'temporary' hose may bridge it.

## Consequences

- The drain chain is continuous joint-by-joint from every tray outlet to the rack drain header outlet, and then deliberately discontinuous at the gap. Anyone reading the model must not mistake the gap for a modelling omission.
- Rack base height and the tundish elevation are both fixed by this dimension.
- Installation inspection must verify the gap physically, not from drawings.

## Evidence

IS 12234 / EN 1717; `RK-A-SYS_Rev2`; `RK-A-WRS_Rev3`
