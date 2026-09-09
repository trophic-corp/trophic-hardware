# Closed-Loop Water Recovery — Shared CEA Infrastructure

**ID:** `RK-A-WRS`
**Owner class:** B — Shared CEA infrastructure
**Authoritative document:** `RK-A-WRS_Rev3_closed-loop-water-recovery.html`

---

## Why this is not part of the rack

This scope was moved out of the rack product during the workspace migration
(ADR-003, ICR-003). The reservoirs, the recovery skid, the diverter and the room
distribution are sized by **room demand** and serve **every rack** in a
facility. They scale with the room, not with the rack.

The rack's hydraulic responsibility ends at the rack drain header outlet at
Z 200, above the 100 mm air gap. Everything below and beyond that gap is this
scope.

A rack can be installed in a facility with entirely different recovery
arrangements — or none — provided the tundish and the air gap are respected.

## What it covers

Terrace source reservoir · terrace recovery reservoir · recovery skid, pumps and
instrumentation · diverter `FV-01` · terrace master valve `MV-01` · room
distribution main · room common drain and sump trough · water quality
management and blowdown · nutrient chelate constraints under UV-C.

## Architecture in one paragraph

Supply is **gravity fed** from the terrace — outlet at +4250 mm, 2.66 m of
static head to the top nozzle, no supply pump (EDR-005). Bed drainage falls to a
surface sump trough in a corner of the room, and the **recovery pump sits at
that low point and pushes up** to the terrace, because a pump cannot lift from
the room at Ooty's altitude. On the terrace, diverter `FV-01` either returns the
water to the source reservoir or discards it, on water quality. `FV-01` fails
**to waste**.

## Key figures — 11 racks / 44 beds

| Quantity | Value |
|---|---|
| Circulated | 1,914 L/day |
| Consumed | 88.9 L/day |
| Blowdown | 146 L/day |
| Make-up | 235 L/day |
| **Recovery ratio** | **87.7 %** |
| Annual discharge | 48.2 m³ vs 632 m³ drain-to-waste |
| **Saved** | **554 m³/year** |
| Capital, stage R1 | ₹145,250 |
| Capital, stage R2 | +₹94,600 |

## Constraints this scope imposes on others

| On | Constraint |
|---|---|
| Facility (C) | Terrace outlet elevation of +4250 mm is a hard requirement. Tank loading is 5.5 kN/m² concentrated against a typical 1.5–2.0 kN/m² terrace rating — resolved by mounting the tank on a steel structure rather than the slab (EDR-013). The structure itself is not yet designed; ND-07 stays open as unknown |
| Rack (A) | The 100 mm air gap must never be plumbed closed — neither owner may close it |
| Operations | Monthly dissolved iron verification once UV-C is in the loop; Fe-DTPA or Fe-EDDHA only, never Fe-EDTA (EDR-009) |

## Related

- Interface: `products/cea/racks/rack-platform/interfaces/hydraulic/README.md`
- Decisions: ADR-001, ADR-002, EDR-005, EDR-006, EDR-007, EDR-009, ICR-002, ICR-003
