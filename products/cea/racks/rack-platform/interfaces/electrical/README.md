# Interface Specification — Electrical

**Interface ID:** `IF-RK-A-ELE`
**Between:** A — Rack product · C — Facility distribution
**Authority:** `RK-A-SYS` Rev 2, `RK-A-ROOM` Rev 4
**Related decisions:** EDR-008

---

## 1. Established requirements

| Requirement | Value | Basis |
|---|---|---|
| Residual current protection | **Type A RCBO** on every circuit serving LED drivers, EC fans or inverter loads. **Type AC is not acceptable anywhere** | EDR-008 |
| Earthing | Per **IS 3043** | |
| Installation, inspection and testing | Per **IS 732** | |
| Local control enclosure | Mounted at the rack end (Fusion v4 relocation) | |
| Ventilation | Standalone EC fans in Phase 1; same fans reused by the Phase-2 plenum | ADR-005 |
| LED fixtures | Procured separately, excluded from rack cost | |

### Why Type A specifically

A Type AC device detects only sinusoidal AC residual current. LED drivers and
inverter-driven compressors produce **pulsating DC** residual current, which a
Type AC device may fail to detect — and which can saturate its core and blind it
to a genuine AC fault. This is specified at circuit-schedule level so it cannot
be substituted at procurement.

The requirement crosses the A/C boundary: it applies to the room distribution
board as well as to the rack, and appears in both `RK-A-SYS` and `RK-A-ROOM`.

---

## 2. Interface points

| Point | Owner boundary | Content |
|---|---|---|
| Rack supply connection | C → A | Single protected supply to the rack control enclosure |
| LED fixture connections | A → fixture | Within the rack; fixtures procured separately |
| Room distribution board | C | Type A RCBO circuit schedule, `RK-A-ROOM` Rev 4 |

---

## 3. Specified — corrected 2026-09-09

The CEA suite audit (`docs/system/CEA_SUITE_AUDIT.md` §4.5) showed these were specified in
RK-A-SYS §07 and RK-A-MFG §01/§05 all along. This section previously listed them as
unspecified; that was an under-read of our own document set.

### The ELV boundary

**All conductors at or below bed/canopy level are 24 V or 48 V DC only.** Mains (230 V) is
confined to an **IP65 enclosure mounted above canopy height**.

| Parameter | Value |
|---|---|
| Minimum electrical/water vertical separation | **236 mm** |
| Cable crossing a wet zone | Not permitted without a drip loop |

It is the ELV boundary — **not the ingress rating** — that makes the electrical and water
systems genuinely independent.

### Circuit ratings and protection

| Item | Specification |
|---|---|
| Per rack | 16 A Type A RCBO, 30 mA |
| Per group of 8 racks | 63 A MCCB, Type 2 SPD |
| Terrace circuit | **10 mA** RCBO — tighter, outdoor/wet installation |
| Surge protection | Type 1+2 SPD at the main board; Type 2 SPD per group panel, 10 kA, max 3 m lead to earth bar |
| Earthing | TN-S per IS 3043; every frame bonded, **< 0.1 Ω**, tested and recorded per rack |
| Room HVAC | 2.0 TR 3-phase inverter + 50 L/day dehumidifier; circuits C12/C13 allocated |

### Loads

| Item | Value |
|---|---|
| LED supply | 48 V DC, one 0–10 V dimming pair per tier, IP65 keyed connector. Two bars share one pair |
| LED drivers | Remote, in the end enclosure |
| EC fan | One per tier, 178 m³/h, PWM or 0–10 V, tacho feedback |
| Drain solenoid holding power | ~8 W each, energised through the dwell |

### Emergency stop and isolation

**Room-level E-stop only** — one latching mushroom head per aisle/door. It drops the group
contactor, all fill solenoids, `MV-01` and all pumps; drains de-energize open.

There is deliberately **no per-rack E-stop**: sixteen rack-level E-stops are sixteen
devices nobody can reach in an emergency. The **per-rack isolator is for lock-out/tag-out
maintenance**, which is a different function and must not be presented as an E-stop.

---

## 4. Still open

| Item | Status |
|---|---|
| Rack connected load and diversity | Not consolidated; derivable from the LED, fan and solenoid figures above but not stated as a total |
| Supply connector type at the rack inlet | Not recorded |
| Cable sizes and derating basis | Not recorded |
| Room electrical phase imbalance | **ND-06** — as-designed 11-rack layout lands at ~20 % against a 15 % target on single-phase HVAC; resolved on paper by specifying 3-phase, recorded as an open finding rather than a clean pass |
| LED driver model | **Not chosen.** Determines whether photoperiod-off is dim-to-off or a relay. Blocks the software's photoperiod actuation design |
