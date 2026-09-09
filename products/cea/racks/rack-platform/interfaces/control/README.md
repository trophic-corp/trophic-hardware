# Interface Specification — Control

**Interface ID:** `IF-RK-A-CTL`
**Between:** A — Rack product · B — Shared infrastructure · and the Trophic CEA
software (via `trophic-contracts`, never directly)
**Authority:** `RK-A-SYS` Rev 2, `RK-A-WRS` Rev 3
**Related decisions:** ADR-004, EDR-007, ICR-002

---

## 1. The software boundary

Control software **must not read this repository** (ADR-004). What it needs is
published through `trophic-contracts`. This specification is the hardware-side
source those contracts are derived from — see
`docs/system/CONTRACT_EXTRACTION.md`.

---

## 2. Established: fail-safe polarity

This is the most important control fact in the system and the least negotiable.

| Device | Owner | Fail state | Consequence |
|---|---|---|---|
| Fill solenoids | A | Normally **CLOSED** | No supply on power or signal loss |
| Drain solenoids | A | Normally **OPEN** | Beds empty by gravity on power or signal loss |
| Recovery diverter `FV-01` | B | Spring-return **TO WASTE** | Never contaminates the source when uncertain |
| Terrace master valve `MV-01` | B | Fails **CLOSED** | Isolates 4.25 m of static head from the building |

**Control software must never assume it is responsible for driving a valve into
a safe state.** Every valve is already safe with no power and no signal. Software
drives them *away* from safe, and losing the ability to do so is not a hazard.

Aggregate failure state: beds drain, supply isolates, recovery discards. Crop
stress is accepted as the lesser failure against flooding the room or
contaminating the source.

---

## 3. Established: physical constraints software must respect

| Constraint | Value | Why software must know |
|---|---|---|
| Supply is gravity-fed | 2.66 m static head, no pump | Software cannot assume constant supply pressure (ICR-002) |
| Flow ceiling | ~15 L/min before head is exhausted | Concurrency limits are physical, not policy |
| Single tier design flow | 7.2 L/min | |
| Four tiers concurrent | 28.8 L/min, 0.67 m loss — passes | Concurrency is permitted, up to the ceiling |
| Air gap | 100 mm, physical, always open | There is no valve here. Software must not model the drain path as closable |
| Bed datum | Deck mesh top face, 300/700/1100/1500 mm | Level and flood-depth setpoints reference this datum |
| Water quality decision | EC, pH, contamination → discard or return | The reuse decision is a monitored decision (ADR-001) |
| Iron verification | Monthly, where UV-C is in the loop | Fe-DTPA / Fe-EDDHA only (EDR-009) |

---

## 4. Specified — corrected 2026-09-09

The CEA suite audit (`docs/system/CEA_SUITE_AUDIT.md`) showed that much of what this
section previously called unspecified is in fact in RK-A-SYS Rev 2 and RK-A-WRS Rev 3.
Published to contracts as `sensors/instrument-tags.md`, `safety/interlocks.md` and
`capabilities/absent-by-design.md`.

### Instrument tags

`TK-01` source reservoir · `LT-02` its level · `TE-01` its temperature · `TE-02` trough
temperature · `AT-03` trough **EC** · `AT-04` trough **pH** · `LSH-04` header high level ·
`LS-01` trough low level · `LD-01…11` leak pucks, one per rack · `F-01`/`F-02` filters ·
`PDI-01` filter ΔP · `UV-01` UV unit · `UIT-01` UV intensity · `FS-01` transfer flow proof ·
`P-02` recovery pump (duty/standby A/B) · `DOS-01` dosing · `MV-01` master valve ·
`FV-01` diverter.

### Per-rack actuators

4 fill solenoids (NC) + 4 drain solenoids (NO) on an 8-channel relay; one EC fan per tier
with **mandatory** tacho alarm; one 0–10 V dimming pair per tier.

### Controller topology and bus

11 × rack controller (ESP32 + 8-ch relay + RS485), one room controller (bus master, local
historian, local UI, UPS), plus terrace, water-skid and room I/O nodes — **14 bus nodes**.
In-room bus is **Modbus RTU over RS485**, multi-drop, 120 Ω both ends. Wired-first: a room
of galvanised racks is a poor 2.4 GHz environment.

Control allocation: rack controllers own the tier fill/dwell/drain sequence, fan PWM and
the leak/header interlocks, and hold a last-known-good schedule. The room controller owns
the drain token, the eight-condition reuse gate, dosing, HVAC and CO₂ setpoints, alarms and
the local log. **The cloud owns nothing the room depends on.**

### Interlocks

Hard-wired and bus-independent — leak puck, `LSH-04`, E-stop, `MV-01` flood sensor.
Software reads their state but **is not in their safety path**. Full table in
`trophic-contracts` `safety/interlocks.md`. Commissioning hold point: fill solenoids proven
to close within **60 s** with a deliberately blocked drain.

### Absent by design

No per-tray level sensor (the standpipe sets level mechanically). No per-rack or per-tier
CO₂ sensing. No tier-level climate control — room scope. No fixed PAR sensor — portable
quantum sensor at commissioning and quarterly. No per-rack kWh meter.

---

## 5. Still open — genuine hardware deliverables

| Item | Status |
|---|---|
| Per-tier sensor mounting coordinates in bed-datum terms | Modelled in CAD; never tabulated |
| Sensor ranges, accuracy classes, calibration intervals per tag | Partially in the Phase D BOM; not consolidated |
| Modbus register map per node | Not published — the single largest remaining gap |
| MQTT payload schema version | Owned by the software side (ADR-0004); hardware must review, not author |
| LED driver model | Not chosen — blocks the photoperiod actuation mechanism |
