# EDR-007 — Fail-safe polarity for every valve

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A, RK-A-WRS |

## Context

On loss of power or loss of control signal, every valve in the system adopts a position. If those positions are chosen individually, the aggregate failure state is arbitrary — and the plausible bad outcome is a bed that keeps filling while a drain stays shut.

## Decision

Polarity is set so the system fails to *empty and isolated*:

| Device | Fail state | Reasoning |
|---|---|---|
| Fill solenoids | Normally **CLOSED** | No supply on power loss |
| Drain solenoids | Normally **OPEN** | Beds empty by gravity on power loss |
| Recovery diverter `FV-01` | Spring-return **TO WASTE** | Never contaminate the source when uncertain |
| Terrace master valve `MV-01` | Fails **CLOSED** | Isolates 4.25 m of static head from the building |

## Consequences

- A total power failure drains the beds rather than flooding the room. Crop stress is accepted as the lesser failure.
- Water loss on a failure is deliberate and bounded: the diverter discards rather than recovers.
- Solenoids must be specified by fail position, not just by size and voltage — this is a procurement constraint carried into the manufacturing pack.
- These four states are safety-critical and are candidate `trophic-contracts` content: control software must never assume it can command a valve into a safe state, because the valve is already safe without it.

## Evidence

`RK-A-SYS_Rev2`; `RK-A-WRS_Rev3`
