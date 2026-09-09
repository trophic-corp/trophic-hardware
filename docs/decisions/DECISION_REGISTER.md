# Decision Register

Index of architecture, engineering and interface decisions. Individual records
are in `records/`. **Load this index; load a record only when the decision it
covers is in question.**

| Prefix | Covers |
|---|---|
| `ADR` | Architecture — product scope, topology, repository and ownership structure |
| `EDR` | Engineering — sizing, material, physics, tolerance, method |
| `ICR` | Interface change — a change that crosses a defined interface |

Records are written for decisions with consequences. Routine CAD operations do
not get records.

**Status:** ACCEPTED · SUPERSEDED · PROPOSED · OPEN

---

## Architecture decisions

| ID | Decision | Status | Affects |
|---|---|---|---|
| [ADR-001](records/ADR-001-closed-loop-water-recovery.md) | Replace drain-to-waste with closed-loop water recovery | ACCEPTED | RK-A, RK-A-WRS |
| [ADR-002](records/ADR-002-water-plant-external-terrace.md) | Locate the water plant on the terrace, outside the grow room | ACCEPTED | RK-A-WRS, RK-A-ROOM |
| [ADR-003](records/ADR-003-product-infrastructure-facility-separation.md) | Separate rack product, shared CEA infrastructure and facility reference | ACCEPTED | Repository-wide |
| [ADR-004](records/ADR-004-hardware-software-repository-boundary.md) | Keep hardware and software repositories independent; publish via `trophic-contracts` | ACCEPTED | Repository-wide |
| [ADR-005](records/ADR-005-plenum-deferred-to-phase-2.md) | Defer the ducted plenum to a Phase-2 entity; ship standalone EC fans in Phase 1 | ACCEPTED | RK-A |
| [ADR-006](records/ADR-006-fusion-authoritative-for-cad.md) | Fusion 360 remains authoritative for native CAD; STEP/F3D are release artifacts | ACCEPTED | Repository-wide |

## Engineering decisions

| ID | Decision | Status | Affects |
|---|---|---|---|
| [EDR-001](records/EDR-001-tier-geometry-and-bed-datum.md) | Four tiers at 300/700/1100/1500 mm; bed datum is the deck mesh top face | ACCEPTED | RK-A |
| [EDR-002](records/EDR-002-fifth-tier-ruled-out.md) | Reject a fifth tier at 1900 mm on NIOSH reach grounds | ACCEPTED | RK-A |
| [EDR-003](records/EDR-003-wet-services-corridor.md) | Reserve Y 435–525 mm as the wet-services corridor | ACCEPTED | RK-A |
| [EDR-004](records/EDR-004-deck-mesh-density-correction.md) | Correct deck mesh density to 1884 kg/m³ — drawing governed over model | ACCEPTED | RK-A |
| [EDR-005](records/EDR-005-gravity-feed-no-supply-pump.md) | Gravity-feed supply from the terrace; no supply pump; recovery pump at the low point | ACCEPTED | RK-A, RK-A-WRS |
| [EDR-006](records/EDR-006-backflow-air-gap.md) | 100 mm air gap (2 × DN50) at the rack drain outlet, never plumbed closed | ACCEPTED | RK-A, RK-A-WRS |
| [EDR-007](records/EDR-007-fail-safe-valve-polarity.md) | Fail-safe polarity for every fill, drain, diverter and master valve | ACCEPTED | RK-A, RK-A-WRS |
| [EDR-008](records/EDR-008-type-a-rcbo.md) | Type A RCBO, not Type AC | ACCEPTED | RK-A, RK-A-ROOM |
| [EDR-009](records/EDR-009-chelated-iron-under-uvc.md) | Fe-DTPA or Fe-EDDHA under UV-C, not Fe-EDTA | ACCEPTED | RK-A-WRS |
| [EDR-010](records/EDR-010-rear-brace-true-length.md) | Rear brace `RK-A-104` is 1797 mm, not 1345 mm | ACCEPTED | RK-A |
| [EDR-011](records/EDR-011-cad-relocation-method.md) | Relocate Fusion components by delete-and-recreate at absolute coordinates | ACCEPTED | Method |
| [EDR-012](records/EDR-012-room-density-eleven-racks.md) | Ooty room carries 11 racks with the water plant external | ACCEPTED | RK-A-ROOM |

## Interface change records

| ID | Change | Status | Interface |
|---|---|---|---|
| [ICR-001](records/ICR-001-tray-to-drain-continuity.md) | Close the overflow discontinuity and model the tray penetrations | ACCEPTED | Hydraulic — tray → rack drain header |
| [ICR-002](records/ICR-002-supply-interface-pumped-to-gravity.md) | Rack supply interface changes from pumped to gravity-fed | ACCEPTED | Hydraulic — rack inlet |
| [ICR-003](records/ICR-003-recovery-interface-moved-to-shared-infra.md) | Recovery diverter and reservoirs leave rack scope for shared infrastructure | ACCEPTED | Hydraulic — rack drain outlet |
| [ICR-004](records/ICR-004-plenum-interface-not-frozen.md) | Rack-to-plenum interface is deliberately not frozen | **OPEN** | Mechanical / electrical — plenum mount |
