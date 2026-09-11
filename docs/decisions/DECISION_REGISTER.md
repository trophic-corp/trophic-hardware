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
| [ADR-008](records/ADR-008-light-engine-smart-module-architecture.md) | Aquarium lights as a Light Engine (LED board, CC drivers, engine MCU, thermal backstop, hardware ID, default profile, signal-only control port) plus an optional user-swappable Smart Module (radio, RTC, schedules, app, OTA); engines radio-free; tier ladder Basic/Smart; not reused by `LT-A`. Rejected: integrated control, inline DC-path controller, MCU-less signal-wire Core (challenger), module carrying LED power | **PROPOSED** (owner to accept; evaluated 2026-09-11) | AQ-LT-A, AQ-LT-B, Smart Module |
| [ADR-007](records/ADR-007-aquarium-lighting-shared-platform.md) | Aquarium lighting is two products, `AQ-LT-A` Core and `AQ-LT-B` WRGB, on one intended shared platform with late differentiation; standalone-first; external certified adapter → ELV DC → internal CC drivers; Core exposes one logical channel. Bus voltage, PSU, chassis sharing, sizes, channel count all remain open | ACCEPTED (recorded from owner intent 2026-09-11; owner to confirm) | AQ-LT-A, AQ-LT-B |

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
| [EDR-010](records/EDR-010-rear-brace-true-length.md) | Rear brace `RK-A-104` is 1797 mm, not 1345 mm | **SUPERSEDED by EDR-018** | RK-A |
| [EDR-011](records/EDR-011-cad-relocation-method.md) | Relocate Fusion components by delete-and-recreate at absolute coordinates | ACCEPTED | Method |
| [EDR-012](records/EDR-012-room-density-eleven-racks.md) | Ooty room carries 11 racks with the water plant external | ACCEPTED | RK-A-ROOM |
| [EDR-013](records/EDR-013-terrace-tank-on-steel-structure.md) | Terrace tank on a steel structure, not bearing on the slab | ACCEPTED | RK-A-WRS, RK-A-ROOM |
| [EDR-014](records/EDR-014-per-tier-cross-beams.md) | Per-tier cross beams reinstated; decks non-structural | ACCEPTED | RK-A |
| [EDR-015](records/EDR-015-rivet-nut-gusset-joints.md) | Rivet-nut joints, `RK-A-107B` gusset plates, crush tubes, 4 N·m rule | ACCEPTED | RK-A, platform |
| [EDR-016](records/EDR-016-valve-technology.md) | Zero-ΔP fill solenoids; motorised spring-return-open drain valves (alternatives to be trialled, ND-09) | ACCEPTED | RK-A, contracts |
| [EDR-017](records/EDR-017-modular-anchor-strut.md) | Modular adjustable anchor strut `RK-A-106B`, 90–320 mm | ACCEPTED | RK-A, RK-A-ROOM |
| [EDR-018](records/EDR-018-rear-brace-on-grid.md) | Rear brace 1810 mm, holes 1780.1 mm on grid rows 150/1450; two bars | ACCEPTED | RK-A |
| [EDR-019](records/EDR-019-flood-tray-formed-geometry.md) | Flood tray modelled as the formed part; deck clearance holes; floor fall → ND-10 | ACCEPTED | RK-A |
| [EDR-020](records/EDR-020-structural-details.md) | Foot insert, upright drain holes, LED saddles, flattened mesh, datum stack confirmed | ACCEPTED | RK-A |

## Interface change records

| ID | Change | Status | Interface |
|---|---|---|---|
| [ICR-001](records/ICR-001-tray-to-drain-continuity.md) | Close the overflow discontinuity and model the tray penetrations | ACCEPTED | Hydraulic — tray → rack drain header |
| [ICR-002](records/ICR-002-supply-interface-pumped-to-gravity.md) | Rack supply interface changes from pumped to gravity-fed | ACCEPTED | Hydraulic — rack inlet |
| [ICR-003](records/ICR-003-recovery-interface-moved-to-shared-infra.md) | Recovery diverter and reservoirs leave rack scope for shared infrastructure | ACCEPTED | Hydraulic — rack drain outlet |
| [ICR-004](records/ICR-004-plenum-interface-not-frozen.md) | Rack-to-plenum interface is deliberately not frozen (reserve now starts Y 571; header occupies X 1200–1250 of the zone) | **OPEN** | Mechanical / electrical — plenum mount |
| [ICR-005](records/ICR-005-fill-nozzle-air-gap.md) | Fill nozzle outlet raised to 38 mm above the tray rim | ACCEPTED | Hydraulic — rack inlet side |
| [ICR-006](records/ICR-006-drain-header-relocated.md) | Drain header behind the rear-right upright; lateral crossing windows; envelope unchanged | ACCEPTED | Mechanical depth allocation, hydraulic drain chain |
| [ICR-007](records/ICR-007-acceptance-criteria-unified.md) | T7/T8/T16/T18 criteria unified; T19, T20 added | ACCEPTED | Verification, contracts |
