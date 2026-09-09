# PRODUCT — Room Controller (`CT-B`)

| | |
|---|---|
| **Product ID** | `CT-B` |
| **Family** | CEA · Sensors and controllers |
| **Owner class** | B — Shared infrastructure (one per room) |
| **Stage** | **Phase 0 — no hardware design** |
| **Authoritative CAD** | None |

---

## 1. What the product is

The room's bus master and local historian: owns the drain token, the eight-condition
reuse gate, fertigation dosing, HVAC and CO₂ setpoints, alarms and the local log.
Carries a local UI and runs on a UPS.

## 2. Why it exists

Someone has to arbitrate between eleven racks and one water skid. The drain token is
the clearest case: sequential draining is mandatory and the trough is sized for one
rack's 46 L batch against 79 L, so **something must ensure only one rack drains at a
time**. That something is this product.

## 3. Inherited constraints — DECIDED

| Constraint | Value | Source |
|---|---|---|
| Quantity | **One per room** | CEA suite device model |
| Role | Bus master, local time-series store, local UI, **UPS-backed** | CEA suite device model |
| Owns | Drain token, 8-condition reuse gate, dosing, HVAC and CO₂ setpoints, alarms, local log | CEA suite device model |
| Bus | Modbus RTU / RS485 master to 13 other nodes | CEA suite ADR-0004 |
| Upstream | **Edge MQTT client** over TLS to the facility broker | CEA suite ADR-0004 |
| Cloud dependency | **None.** The cloud owns remote view and history and nothing the room depends on | CEA suite ADR-0001 |
| Reuse gate | G1–G8; G1/G2/G3/G6/G7/G8 per batch, **G4 and G5 continuously during transfer** | `trophic-contracts` `process/reuse-decision.md` |
| Blowdown | Daily 02:00, first batch dumped **regardless of gate result** — not an error | `trophic-contracts` `process/reuse-decision.md` |
| Pump run limit | `P-02` stops on `LS-01` low **or** 4 min — the limit catches a stuck float | `trophic-contracts` |
| Not in the safety path | E-stop, `MV-01` flood sensor, leak pucks are hard-wired | `trophic-contracts` `safety/interlocks.md` |
| Platform decision | Open in the CEA suite as `[OQ-3]` — a Linux SBC here is a named monorepo split trigger | CEA suite ADR-0008 |

## 4. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | **Compute platform** — `[OQ-3]`. Owned by the software side; hardware must not pre-empt it | Enclosure, power, thermal |
| 2 | UPS: integrated or external, and runtime | Enclosure volume, the largest single driver |
| 3 | Mounting: wall-mount panel, rack-mount, or DIN enclosure | Form factor |
| 4 | Local UI: panel display or a browser on a tablet | Enclosure face, IP rating |
| 5 | Location in the room, and its IP requirement — the room runs 55–70 % RH | Ingress spec |
| 6 | Storage sizing for the local historian | Compute selection |

## 5. Explicitly not decided

No enclosure, no compute selection, no UPS sizing, no storage sizing, no mass, no
cost. There is **no CAD placeholder for this product at all** — unlike `CT-A`, it does
not yet appear in any model.

## 6. Interfaces

Platform electrical standards apply. Decision 1 is **not this family's to make** — it
is `[OQ-3]` on the software side, and taking it here would be exactly the boundary
violation ADR-004 exists to prevent.

## 7. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No** — not even massing. Volume depends entirely on decisions 1 and 2 |
| What to do instead | Reserve wall area in the room layout once decision 3 is made |

Of all the Phase 0 products, this is the one where a generated model would be pure
invention. **Do not model it.**

## 8. Next action

Wait for `[OQ-3]` on the software side. Meanwhile, decision 3 (mounting) can be
settled from the room layout without any compute decision, and would let the room
drawing reserve space.
