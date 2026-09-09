# ICR-003 — Recovery diverter and reservoirs leave rack scope for shared infrastructure

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | Hydraulic — rack drain outlet |

## Context

Early integration modelled the recovery reservoir interface as part of the rack. Under ADR-003 that is wrong: the reservoirs and the diverter are sized by room demand and serve every rack, so they belong to shared CEA infrastructure.

## Decision

The rack's hydraulic responsibility **ends at the rack drain header outlet at Z 200**. Everything beyond it — tundish, common drain, sump trough, recovery pump, diverter `FV-01`, reservoirs — is shared infrastructure.

The interface is defined by three facts and nothing else: outlet elevation Z 200, DN50, and the 100 mm air gap below it (EDR-006).

## Consequences

- `RK-A-WRS` relocated to `products/cea/irrigation/water-recovery/`.
- The rack can be installed in a facility with entirely different recovery arrangements, or with none, provided the tundish and gap are respected.
- Recovery sizing changes (more racks, different blowdown regime) no longer touch the rack.
- The air gap is now the boundary object between two owners, which makes EDR-006 doubly binding: neither side may close it.

## Evidence

`docs/system/MIGRATION_REPORT.md`; `RK-A-WRS_Rev3`
