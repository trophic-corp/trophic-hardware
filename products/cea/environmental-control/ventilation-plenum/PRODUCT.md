# PRODUCT — Ducted Ventilation Plenum (`EV-A`)

| | |
|---|---|
| **Product ID** | `EV-A` |
| **Family** | CEA · Environmental control |
| **Owner class** | A — Product (rack accessory) |
| **Stage** | **Phase 0 — deliberately deferred** (ADR-005) |
| **Authoritative CAD** | None. `07_PLENUM` in `CEA_RACK_INTEGRATED_v2` is a **massing placeholder**, and its 4.018 kg is a shelled primitive, not a design |

---

## 1. What the product is

A ducted plenum that bolts to the rack's existing grid, houses the EC fans the rack
already ships with, and replaces point-source discharge with distributed discharge
across the canopy.

## 2. Why it exists

Airflow **uniformity**, not airflow volume. A point-source fan produces a canopy
velocity coefficient of variation around **33 %**; a ducted plenum around **10 %**.
The rack ships Phase 1 with standalone EC fans and accepts the 33 % as a known
penalty — this product is how that penalty gets paid back.

ADR-005 deferred it because duct geometry, static pressure distribution, fan-curve
matching and acoustics are a meticulous design problem in their own right, and
holding a ready rack for them made no sense.

## 3. Inherited constraints — DECIDED

| Constraint | Value | Source |
|---|---|---|
| Fans | **Reuses the rack's existing EC fans** — 1 per tier, 178 m³/h, PWM or 0–10 V with tacho | `RK-A-SYS` Rev 2 |
| Mounting | Bolts to the **same 50 mm grid**, Ø9 | Platform mechanical standards |
| Depth available | **42 mm** — the difference between the Phase-1 build (648 mm) and the installed envelope (690 mm) | `RK-A-PARAM` Rev 1, ICR-004 |
| Canopy velocity target | **0.2 – 0.5 m/s**, upper stress bound 1.3 m/s | `RK-A-SYS` §05; `RK-A-ROOM` §06 |
| Uniformity target | Improve CV from ~33 % toward ~10 % | Published CFD, REF-04 |
| Retrofit rule | Must fit racks **already built and installed**, without moving them | ADR-005 |
| Verification | 5-point-per-tier hot-wire anemometer traverse — acceptance test **T10** | `RK-A-MFG` Rev 2 |
| Indicative cost | ₹2,640/rack, "month 2–3" | CEA suite device model, sourced to the rack set |

## 4. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | **Freeze the rack-to-plenum interface.** ICR-004 is OPEN. No mounting provision is specified, so Phase-1 racks cannot be guaranteed plenum-ready | Everything, and it lands on racks built first |
| 2 | Confirm room set-out uses the plenum-ready 690 mm pitch (ND-04) | Whether retrofit needs racks moved |
| 3 | Duct cross-section and discharge pattern within 42 mm | The actual design |
| 4 | Static pressure budget against the existing fan curve — do the current fans still deliver 178 m³/h through a duct? | Whether fan reuse survives |
| 5 | Which CV action threshold applies — 15 % or 20 % (ND-05) | Whether this product is an optimisation or a required fix |
| 6 | Cleanability. It sits above a food crop | Material, access, joints |

## 5. Explicitly not decided

No duct geometry, no discharge slot pattern, no material, no mass, no pressure drop,
no acoustic figure, no BOM. **The 4.018 kg in the release manifest is a shelled
primitive standing in for volume — it is not this product's mass and must never be
quoted as one.**

## 6. Interfaces

Platform mechanical standards apply in full. The fan electrical interface is
inherited unchanged — this product adds no electrical interface of its own, which is
deliberate: it should not require a rack rewire.

The removable-part rule matters here: the plenum comes off for cleaning, so **it
carries no structural duty** and the rack must be complete without it.

## 7. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **Massing only** — a 42 mm slab at the rear face |
| Good for | Envelope reservation, room set-out, clash |
| Must NOT be inferred | Duct form, discharge geometry, mass, pressure drop, airflow performance |

The existing `07_PLENUM` placeholder already does this. Do not model a "real" plenum
until decision 1 is closed — a design built against an unfrozen interface will be
rebuilt.

## 8. Next action

Close **ICR-004** — freeze the rack-to-plenum mounting interface. It must happen
before the Phase-1 fabrication release, not before the plenum design, because the
constraint lands on the racks that get built first.
