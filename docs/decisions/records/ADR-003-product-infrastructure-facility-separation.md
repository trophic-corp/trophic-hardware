# ADR-003 — Separate rack product, shared CEA infrastructure and facility reference

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | Repository-wide |

## Context

During integration the rack model accumulated content that is not rack hardware: terrace reservoirs, the recovery skid, room distribution, room electrical distribution and the room itself. Treating all of it as 'the rack' would make the rack product unsellable in any other building and would force every facility change through a rack revision.

## Decision

Three ownership classes, applied by asking *what varies with what*:

| Class | Test | Location |
|---|---|---|
| **A — Rack product** | Scales with rack count; identical in every installation | `products/cea/racks/rack-platform/` |
| **B — Shared CEA infrastructure** | Sized by room demand; serves many racks | `products/cea/irrigation/water-recovery/` |
| **C — Facility reference** | Specific to one building | `products/cea/facility-reference/ooty-room-20x12/` |

The A/B boundary is the **rack inlet and the rack drain header outlet**.

## Consequences

- `RK-A-WRS` moved out of the rack directory into shared infrastructure.
- `RK-A-ROOM` moved out into facility reference. It is a worked example, not a deliverable.
- A second CEA facility can now be designed by reusing A and B and writing a new C, with no rack revision.
- Interface specifications at the A/B boundary become mandatory — they are the only thing holding the two sides together.

## Evidence

Migration classification, `docs/system/MIGRATION_REPORT.md` §2
