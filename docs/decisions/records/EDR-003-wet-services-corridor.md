# EDR-003 — Reserve Y 435-525 mm as the wet-services corridor

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A |

## Context

Irrigation and drainage runs, LED fixtures and the rear bracing plane all compete for depth within a 563 mm structural envelope. Without a reserved corridor, pipe routing collides with either lighting or bracing at every revision.

## Decision

Reserve **Y 435 - 525 mm from the front face** exclusively for wet services.

The corridor is forward of the rear bracing plane and clear of both LED rows:

| Zone | Y range |
|---|---|
| LED row 1 | 148 - 208 |
| LED row 2 | 352 - 412 |
| **Wet services** | **435 - 525** |

## Consequences

- Pipe routing and LED placement can be revised independently without re-checking each other.
- A leak in the corridor drips forward of the bracing and clear of the fixture bodies.
- Any new service claiming depth must be checked against this table before it is modelled.
- Contributed directly to reaching 0 unresolved interferences in v8.

## Evidence

`RK-A-SYS_Rev2`; Fusion interference check, v8
