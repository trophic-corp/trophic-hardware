# EDR-005 — Gravity-feed supply from the terrace; no supply pump; recovery pump at the low point

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A, RK-A-WRS |

## Context

The proposed arrangement placed a pump on the terrace drawing water up from the room. This is not possible. At Ooty (2,240 m) atmospheric pressure is 77.2 kPa, equal to 7.87 m of water, and practical self-priming suction lift is 2.5-4 m. Even at Coimbatore (411 m, 96.5 kPa, 9.84 m) practical lift is only 4.5-5.5 m. A pump cannot reliably lift from a room floor to a terrace at either site.

## Decision

Two changes:

1. **Supply is gravity fed.** The terrace slab at +3750 mm plus a 500 mm plinth puts the outlet at +4250 mm. The top nozzle is at +1590 mm, giving **2.66 m static head**.
2. **The recovery pump goes at the low point and pushes up.** A pump pushes; it does not suck from a distance.

There is no supply pump.

## Consequences

Head check (Hazen-Williams, C = 150), at 7.2 L/min:

| Element | Loss (m) |
|---|---|
| DN32 main | 0.028 |
| DN25 riser | 0.012 |
| DN20 drop | 0.023 |
| DN20 solenoid, Kv 4 | 0.119 |
| Fittings | 0.150 |
| **Total** | **0.33** |

2.66 m available against 0.33 m required — a margin of about **8x**. Head runs out near 15 L/min. Four tiers irrigating concurrently (28.8 L/min) costs 0.67 m and still passes.

- One less pump to buy, power, protect and maintain; supply survives a power failure.
- Flow is now head-limited, so any future increase in nozzle count or solenoid Kv must be re-checked against the 15 L/min ceiling.
- The terrace outlet elevation becomes a hard facility requirement, not a convenience.

## Evidence

`RK-A-WRS_Rev3`; `RK-A-QC_Rev3`
