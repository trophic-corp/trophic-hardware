# Ooty CEA Room, 20 × 12 ft — Facility Reference

**ID:** `RK-A-ROOM`
**Owner class:** C — Facility / reference implementation
**Authoritative document:** `RK-A-ROOM_Rev4_floor-plan.html`
**Classification:** REFERENCE — this is one worked implementation, not a product

---

## What this is and is not

This is the R&D facility at Ooty (2,240 m ASL), laid out as a **realistic
engineering set-out** — real clearances, real coordinates, real loads — rather
than racks arranged visually.

It is **not** a rack deliverable and **not** a product specification. A second
CEA facility is designed by reusing the rack product (A) and the shared
infrastructure (B) and writing a new document like this one (ADR-003). No rack
revision is required.

Its engineering content is nonetheless validated and current: floor loads, rack
set-out coordinates and the room water balance are all live figures.

## Layout adopted

**11 racks, water plant on the terrace** (ADR-002, EDR-012).

| Option | Grow area | Floor multiplier | Status |
|---|---|---|---|
| 9 racks, plant inside the room | — | 1.06× | Rejected — plant consumes grow floor |
| **11 racks, plant on the terrace** | **29.0 m²** | **1.30×** | **Adopted** |
| 12 racks, plant fully external | — | 1.42× | Rejected — insufficient service aisle |

| Quantity | Value |
|---|---|
| Room total cost | ₹1,321,506 (≈ ₹13.2 lakh), excluding LED fixtures |
| Beds | 44 (11 racks × 4 tiers) |
| Make-up water | 235 L/day |
| Set-out depth per rack | 690 mm installed (plenum-ready), not 648 mm |

## Contents

Rack set-out coordinates · aisle and service clearances · room electrical
distribution with Type A RCBO schedule · room HVAC · egress · and §08
**Building** — ceiling height, floor and point loading, slab, floor finish, wall
fixings.

§08 was silently dropped in the Rev 3 rewrite and restored in Rev 4 with
recomputed loads. It is easy to lose and must be checked on every reissue.

## Open item

**ND-04** — set-out assumes the plenum-ready 690 mm installed depth for
Phase-1 racks, which are only 648 mm deep. This needs explicit confirmation so
the Phase-2 plenum retrofit does not require moving racks.

## Related

- Decisions: ADR-002, EDR-008, EDR-012
- Superseded predecessor: `archive/superseded/RK-R-01_Rev1_cea-room-scaling-study.html`
