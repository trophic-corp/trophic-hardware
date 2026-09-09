# PRODUCT — Rack Controller (`CT-A`)

| | |
|---|---|
| **Product ID** | `CT-A` |
| **Family** | CEA · Sensors and controllers |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no hardware design** |
| **Authoritative CAD** | None. `11_ENCLOSURE_IP65` in the rack model is a massing block |

---

## 1. What the product is

The per-rack controller: runs the tier fill/dwell/drain sequence locally, drives fan
PWM, reads the leak and header interlocks, and holds a last-known-good schedule so
the rack keeps irrigating when the bus or the room controller drops.

## 2. Why it exists

Edge autonomy is an architectural requirement, not a convenience. The room must not
depend on the cloud, and a rack must not depend on the room. Eleven of these run one
room.

## 3. Inherited constraints — DECIDED

| Constraint | Value | Source |
|---|---|---|
| Quantity | **11 per room** (one per rack), part of 14 bus nodes | CEA suite device model |
| Compute | **ESP32** | CEA suite device model |
| IO | **8-channel relay** — 4 fill + 4 drain solenoids | CEA suite device model |
| Bus | **Modbus RTU over RS485**, multi-drop, 120 Ω both ends | CEA suite ADR-0004 |
| Owns locally | Tier sequence, fan PWM, leak/header interlocks, last-known-good schedule | CEA suite device model |
| Does **not** own | Drain token, reuse gate, dosing, HVAC/CO₂ setpoints, alarms — all room controller | CEA suite device model |
| Enclosure | **IP65, mounted above canopy height**, at the rack end | `RK-A-SYS` Rev 2; platform electrical standards |
| Mains boundary | Mains terminates **inside this enclosure**. Everything leaving it at or below canopy is 24/48 V DC | Platform electrical standards |
| Interlocks | Leak puck and `LSH-04` are **hard-wired, bus-independent**. Controller reads, never mediates | `trophic-contracts` `safety/interlocks.md` |
| Fan feedback | Tacho input per fan — **the tacho alarm is not optional** | CEA suite device model |
| Boot behaviour | Must boot to documented de-energized fail-safe states **before** schedules resume | `trophic-contracts` `safety/valve-fail-states.md` |
| Commissioning | Fill solenoids proven to close within **60 s** with a blocked drain — QC hold point | `trophic-contracts` `safety/interlocks.md` |
| Sequencing | **Sequential draining is mandatory** — one tier at a time | `trophic-contracts` `hydraulic/drain-sequencing.md` |
| Protection | 16 A Type A RCBO, 30 mA on the rack circuit | Platform electrical standards |

## 4. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | **Modbus register map** — the single largest gap on the hardware side | Firmware, `trophic-contracts` |
| 2 | Make vs buy: off-the-shelf ESP32 + relay board in an enclosure, or a Trophic PCB | Everything downstream |
| 3 | Sensor ranges, accuracy classes and calibration intervals per tag | Component selection |
| 4 | Enclosure size and gland schedule — driven by 2 and the cable count | The only part with real geometry |
| 5 | Power: 48 V rail shared with LED, or separate supply | Enclosure thermal, PSU |
| 6 | Local UI: any, or headless with the room controller carrying it | Enclosure face |
| 7 | Thermal: sealed IP65 above a warm canopy | Enclosure material, venting |

## 5. Explicitly not decided

No enclosure dimensions, no PCB, no schematic, no component selection, no gland
count, no mass, no cost. **`11_ENCLOSURE_IP65` at 0.834 kg is a shelled primitive
reserving space at the rack end. It is not this product.**

## 6. Interfaces

Platform electrical standards apply in full. This is the product where the ELV
boundary is physically realised, so it is the one that most has to get it right.

Everything the software needs from this product is published through
`trophic-contracts`. The register map (decision 1) is a **hardware deliverable** that
the software is currently blocked on.

## 7. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **Massing only** — a box at the rack end |
| Good for | Space reservation, cable routing, service access, clash |
| Must NOT be inferred | Enclosure size, gland positions, internal layout, mass, thermal behaviour |

## 8. Next action

Answer decision 2 (make vs buy). Everything else in §4 depends on it, and it is a
business decision that does not need any engineering to make.
