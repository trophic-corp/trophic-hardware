# EDR-008 — Type A RCBO, not Type AC

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A, RK-A-ROOM |

## Context

A Type AC residual current device only detects sinusoidal AC residual current. LED drivers and inverter-driven compressors produce pulsating DC residual current, which a Type AC device can fail to detect — and which can also blind it to a genuine AC fault by saturating its core.

## Decision

Every circuit serving LED drivers, EC fans or inverter loads is protected by a **Type A RCBO**. Type AC is not acceptable anywhere in the installation.

Earthing to IS 3043; inspection and testing per IS 732.

## Consequences

- Marginal cost increase per circuit, accepted without further analysis.
- Specified at circuit-schedule level in the systems specification so it cannot be substituted at procurement.
- Applies to the room distribution board as well as the rack, so it crosses the A/C ownership boundary and appears in both documents.

## Evidence

IS 3043, IS 732; `RK-A-SYS_Rev2`; `RK-A-ROOM_Rev4`
