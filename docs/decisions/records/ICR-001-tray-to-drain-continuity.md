# ICR-001 — Close the overflow discontinuity and model the tray penetrations

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | Hydraulic — tray outlet to rack drain header |

## Context

The user asked directly whether the missing pipe connection from the flood bed to the common drain was by design or an omission. Investigation found both an answer and a real defect: the common drain header **was** connected, but the overflow line had a genuine **90 mm break** between the moulded collar (Z 300-330) and the vertical drop (Z 160-210), and the tray penetrations had never been modelled at all.

## Decision

Interface closed:

- `09_OVF_V` extended to span **Z 160 - 300**, eliminating the break.
- `09_TRAY_OUTLET` added — the penetration through the tray floor.
- `09_TRAY_STRAINER` added.
- `09_OVF_BULKHEAD` added — the sealed bulkhead fitting at the penetration.

The drain chain is now continuous joint-by-joint from every tray outlet to the rack drain header outlet, and breaks only at the air gap (EDR-006).

## Consequences

- The tray becomes a moulded part with tooling features, not a plain vessel: the drawing now dimensions the moulded overflow collar in section and both boss positions as tooling features (`boss_y`, `ovf_x`, `ovf_dia`, `collar_h` in the generator).
- Tray part `RK-A-401` gained `boss_y = 480`, `ovf_x = 120`, `ovf_dia = 32`, `collar_h = 30`.
- Found by human review, not by the interference check — a clash check cannot detect a gap between two things that should touch. Continuity is now a separate, explicit verification step.

## Evidence

`CEA_RACK_INTEGRATED_v2` v7 'tray bulkheads, strainers, overflow drop continuity'; `RK-A-QC_Rev3`
