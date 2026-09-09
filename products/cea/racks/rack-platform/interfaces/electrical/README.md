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

## 3. NEEDS SPECIFICATION

The following are **not established** in the current document set and have not
been invented here. They must be specified before the electrical design can be
called complete:

| Item | Status |
|---|---|
| Rack connected load and diversity | Not recorded |
| Supply voltage, phases and connector type at the rack inlet | Not recorded |
| Circuit schedule internal to the rack (ways, ratings, segregation) | Not recorded |
| Cable sizes and derating basis | Not recorded |
| Emergency stop architecture and its scope (rack vs room) | Not recorded |
| Protective earthing continuity test points | Not recorded |
| Isolation for maintenance — where, and lockable or not | Not recorded |

Detailed electrical content exists in `RK-A-SYS` Rev 2; where a value above is
in fact present there, move it into this table rather than leaving the
interface unstated. This index records what could be established without
opening the full specification, and deliberately does not guess the rest.
