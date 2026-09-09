# Contract Extraction — candidate `trophic-contracts` content

**Purpose:** identify the hardware facts the existing Trophic CEA software
should consume, and record where each is derived from, so the published contract
does not drift from the engineering.

**This document does not create the software implementation.** The CEA software
project already exists, is independent, and is not modified from here (ADR-004).

---

## 1. The rule

| Repository | Carries | Does not carry |
|---|---|---|
| `trophic-hardware` | Geometry, drawings, BOMs, costs, validation, manufacturing | — |
| `trophic-contracts` | Stable machine-consumable interface facts | Geometry, drawings, BOMs, costs |
| Trophic CEA software | Implementation | Anything from `trophic-hardware` |

The software repository **must not ingest this repository**. A contract change
is a deliberate, reviewed event — not a silent consequence of a CAD edit.

---

## 2. Ready to publish now

These are established, stable, and are exactly the facts control software most
often gets wrong.

### 2.1 Fail-safe polarity — `safety/valve-fail-states`

Derived from EDR-007, `IF-RK-A-CTL` §2.

| Device | Fail state |
|---|---|
| Fill solenoids | Normally CLOSED |
| Drain solenoids | Normally OPEN |
| Recovery diverter `FV-01` | Spring-return TO WASTE |
| Terrace master valve `MV-01` | Fails CLOSED |

**Contract assertion:** every valve is safe with no power and no signal.
Software drives valves *away* from safe. Loss of control authority is not a
hazard, and software must never be written as though it is responsible for
commanding a safe state.

### 2.2 Hydraulic limits — `hydraulic/supply-limits`

Derived from EDR-005, ICR-002, `IF-RK-A-HYD`.

| Fact | Value |
|---|---|
| Supply type | Gravity. **No supply pump exists** |
| Static head at top nozzle | 2.66 m |
| Single-tier design flow | 7.2 L/min |
| Concurrent four-tier flow | 28.8 L/min — permitted |
| **Flow ceiling** | ~15 L/min through a single path before head is exhausted |

**Contract assertion:** supply pressure is not constant and cannot be commanded.
Concurrency limits are physical.

### 2.3 Drain topology — `hydraulic/drain-topology`

Derived from EDR-006, ICR-001, ICR-003.

**Contract assertion:** the drain path contains a permanent 100 mm air gap at
the rack outlet. There is no valve there and it can never be closed. Software
must not model the drain path as closable, must not attempt to isolate it, and
must not raise an alarm on its openness.

### 2.4 Bed datum and geometry — `geometry/bed-datum`

Derived from EDR-001.

| Fact | Value |
|---|---|
| Datum definition | Top face of the deck mesh panel |
| Bed datums | 300 / 700 / 1100 / 1500 mm |
| Tiers per rack | 4 |
| Tier pitch | 400 mm |

**Contract assertion:** all level and flood-depth setpoints reference the bed
datum, not the tray floor and not the beam. This is the definition that most
easily goes wrong across the hardware/software boundary.

### 2.5 Water quality decision — `process/reuse-decision`

Derived from ADR-001, EDR-009.

**Contract assertion:** recovered water is returned to source only when within
defined reuse parameters (EC, pH, contamination risk); otherwise discarded. The
default on uncertainty is discard, matching the hardware fail state. Where UV-C
is in the loop, dissolved iron requires monthly verification and the chelate is
Fe-DTPA or Fe-EDDHA — never Fe-EDTA.

### 2.6 Units and identifiers — `conventions/units`

| Convention | Value |
|---|---|
| Length | mm |
| Flow | L/min |
| Head | m water |
| Volume | L |
| Mass | kg |
| Pressure | kPa |
| Device identifiers | `FV-01`, `MV-01` and the pattern they follow |
| Part identifiers | `RK-A-###` |

---

## 3. Blocked — cannot publish yet

The largest and most useful part of the contract does not exist because the
hardware side has not been specified. See `IF-RK-A-CTL` §4.

| Contract | Blocked on |
|---|---|
| `sensors/inventory` | Sensor identity, type, measurand, units, range, accuracy — not tabulated |
| `sensors/placement` | Mounting locations exist in CAD; not extracted to bed-datum coordinates |
| `actuators/inventory` | Actuator identity, type and per-tier mapping — not tabulated |
| `addressing/channel-map` | No channel numbering or addressing scheme exists |
| `transport/protocol` | Bus/protocol between rack enclosure and room controller not chosen |
| `safety/interlocks` | Hardware interlock set not defined |
| `telemetry/rates` | Not defined |
| `alarms/set` | Alarm identities, thresholds and latching behaviour not defined |

**These are hardware deliverables, not software ones.** Producing them is the
main prerequisite for software integration, and it is the correct next step
after the release blocker is cleared.

---

## 4. Never publish to contracts

| Content | Reason |
|---|---|
| Fusion designs, STEP, F3D, DXF | Geometry. Not a software concern (ADR-006) |
| Structural drawings | Geometry |
| Manufacturing pack, BOM, costs | Commercial and manufacturing |
| Structural simulation records | Evidence, not interface |
| Room floor plan | Facility-specific (ADR-003) |
| Supplier research | Commercial |

---

## 5. `trophic-contracts` repository shape

Created as a **separate repository**, a sibling of this one — not a
subdirectory, so it cannot be pulled in by accident.

```
trophic-contracts/
  README.md
  CHANGELOG.md          every change is a reviewed event
  conventions/units.md
  safety/valve-fail-states.md
  safety/interlocks.md            (blocked)
  hydraulic/supply-limits.md
  hydraulic/drain-topology.md
  geometry/bed-datum.md
  process/reuse-decision.md
  sensors/                        (blocked)
  actuators/                      (blocked)
  addressing/                     (blocked)
```

### Rules for the contract repository

1. Every entry names its derivation — the hardware decision or interface spec it
   came from — so drift is detectable.
2. A contract change requires a `CHANGELOG.md` entry and review by both sides.
3. Contracts are versioned. The software pins a version; it does not track a
   branch.
4. If a contract cannot be stated without geometry, it does not belong here.
