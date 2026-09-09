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

## 4. NEEDS SPECIFICATION

The physical sensor and actuator inventory is modelled in Fusion and described
in `RK-A-SYS` Rev 2, but the **control interface** — the machine-readable map —
has not been extracted. It is **not invented here**.

| Item | Status |
|---|---|
| Sensor inventory: identity, type, measurand, units, range, accuracy | NEEDS SPECIFICATION |
| Sensor physical mounting location per tier, in bed-datum coordinates | Modelled in CAD; not tabulated |
| Actuator inventory: identity, type, per-tier mapping | NEEDS SPECIFICATION |
| Channel numbering and addressing scheme | NEEDS SPECIFICATION |
| Bus / protocol between the rack enclosure and the room controller | NEEDS SPECIFICATION |
| Interlocks: which conditions inhibit which actuator, in hardware | NEEDS SPECIFICATION |
| Telemetry rates and units | NEEDS SPECIFICATION |
| Alarm set: identity, threshold, latching behaviour | NEEDS SPECIFICATION |

Until this table is filled, `trophic-contracts` can publish only §2 and §3 —
which is genuinely useful (fail-safe polarity and physical limits are the facts
software most needs and most often gets wrong) but is not a complete contract.

**Filling this table is the main prerequisite for the software integration**,
and it is a hardware deliverable, not a software one.
