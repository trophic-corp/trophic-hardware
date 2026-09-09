# Platform Electrical Standards

Derived from `RK-A-SYS` Rev 2 §07, `RK-A-MFG` Rev 2 §01/§05 and `RK-A-ROOM` Rev 4 §05.
Published to software as `trophic-contracts` `electrical/elv-boundary.md`.

**Scope caveat:** these are mains-connected CEA installation standards. A 12 V
desktop aquarium product inherits the connector and enclosure discipline but not the
RCBO and SPD schedule. Deviation for such products does not need a decision record;
it needs the product's own `PRODUCT.md` to say which clauses apply.

## 1. The ELV boundary

**All conductors at or below bed/canopy level are 24 V or 48 V DC only.** Mains
(230 V) is confined to an **IP65 enclosure above canopy height**.

It is the ELV boundary — **not the ingress rating** — that makes the electrical and
water systems genuinely independent. An IP-rated enclosure at bed level is not
equivalent and does not satisfy this.

## 2. Protection

| Item | Specification |
|---|---|
| RCD type | **Type A. Type AC is not acceptable anywhere** |
| Per rack | 16 A Type A RCBO, 30 mA |
| Per group of 8 racks | 63 A MCCB, Type 2 SPD |
| Terrace / outdoor circuit | **10 mA** RCBO — tighter than indoor |
| Surge | Type 1+2 SPD at the main board; Type 2 SPD per group panel, 10 kA, max 3 m lead to earth bar |
| Earthing | **TN-S** per IS 3043, every frame bonded, < 0.1 Ω, recorded per unit |
| Inspection and testing | Per **IS 732** |

**Why Type A:** LED drivers, PWM/EC fans and inverter-compressor HVAC produce
pulsating DC residual current that a Type AC device can fail to trip on, and which
can saturate its core and blind it to a genuine AC fault. Specified at
circuit-schedule level so it cannot be substituted at procurement.

## 3. Emergency stop and isolation

**E-stop is room-level, one latching mushroom head per aisle/door.** It drops the
group contactor, all fill solenoids, `MV-01` and all pumps; drains de-energize open.

There is deliberately **no per-unit E-stop**: sixteen rack-level E-stops are sixteen
devices nobody can reach in an emergency. The **per-unit isolator is for
lock-out/tag-out maintenance** — a different function. Never label or present it as
an emergency stop.

## 4. Fail-safe is a hardware property

Every controlled device adopts a defined state with no power and no signal, and that
state is chosen so the system fails **empty and isolated**. The full table is in
`trophic-contracts` `safety/valve-fail-states.md`.

**Control software is never responsible for commanding a safe state.** Any product
that requires software to act in order to be safe has failed this standard.

## 5. Signal and connector conventions

| Item | Convention |
|---|---|
| Dimming | 0–10 V pair per controlled zone |
| Fan control | PWM or 0–10 V, **with tacho feedback — the tacho alarm is not optional** |
| Connectors in wet zones | IP65, keyed |
| Drivers | Remote, in the end enclosure — not at the fixture |
| In-room bus | **Modbus RTU over RS485**, multi-drop, 120 Ω both ends |
| Facility backbone | MQTT over TLS — owned by the software side (ADR-0004 in the CEA suite) |

Wired-first is a deliberate choice: a room of galvanised racks is a poor 2.4 GHz
environment.
