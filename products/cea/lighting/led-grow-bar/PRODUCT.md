# PRODUCT — LED Grow Bar (`LT-A`)

| | |
|---|---|
| **Product ID** | `LT-A` |
| **Family** | CEA · Lighting |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no engineering** |
| **Authoritative CAD** | None. `06_LED_FIXTURE_ENV` in `CEA_RACK_INTEGRATED_v2` is a **keep-out envelope**, not a fixture design |

---

## 1. What the product is

A dimmable LED bar for CEA growing racks, mounting on the `RK-A-301` rail and driven
from the rack's 48 V DC supply with a 0–10 V dimming pair. Two bars share one dimming
pair, so a tier is one control zone.

## 2. Why it exists

Today LED fixtures are bought in and excluded from every rack cost figure. They are
the largest uncosted line in the system, the component most likely to determine crop
performance, and the one the rack has already been designed around. Making them
in-house closes the cost model and puts the optical result under Trophic's control.

## 3. Inherited constraints — DECIDED

Every row is fixed by the rack and is not open to this product.

| Constraint | Value | Source |
|---|---|---|
| Supply | **48 V DC** | `RK-A-SYS` Rev 2 §07 |
| Dimming | **0–10 V pair per tier**, two bars share one pair | `RK-A-SYS` Rev 2 §07 |
| Connector | IP65, keyed | `RK-A-SYS` Rev 2 §07 |
| Driver location | **Remote, in the end enclosure** — not at the fixture | `RK-A-SYS` Rev 2 §07 |
| Fixtures per rack | 8 (2 rows × 4 tiers) | `RK-A R1` manifest, `06_LED_FIXTURE_ENV` qty 8 |
| Keep-out envelope | `LED_Fixture_H` **40 mm** × `LED_Fixture_W` **60 mm** | `RK-A-PARAM` Rev 1 |
| Mounting rail | `RK-A-301`, `LED_Rail_Size` 20 mm | `RK-A-PARAM` Rev 1 |
| Row positions | Y **148–208** and Y **352–412** mm from the rack front face | EDR-003 |
| Clearance to canopy | `LED_Clearance` **150 mm** above a 139 mm canopy | `RK-A-PARAM` Rev 1 |
| ELV boundary | Fixture sits **at canopy level → 48 V DC only**. No mains at the bar | Platform electrical standards |
| PPFD operating band | **150 – 210 µmol/m²/s**, **CV ≤ 15 %** | `RK-A-SYS` §00; `RK-A-MFG` QC criterion T2 |
| PPFD limits | Below **100** suppresses growth; above **210** risks photoinhibition | CEA suite `safety-rules.json`, sourced to Phase A |
| Verification method | **Portable quantum sensor on a jig**, commissioning and quarterly. There is no fixed PAR sensor | `trophic-contracts` `capabilities/absent-by-design.md` |
| Thermal acceptance | Air rise **≤ 3 K** over 24 h continuous; no LED derating | `RK-A-MFG` Rev 2, test P2 |
| RCD | Type A on the supplying circuit | EDR-008 |

## 4. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | **Driver model.** Also decides whether photoperiod-off is dim-to-off or a relay. Open in the CEA suite as `[OQ-14]` and in `IF-RK-A-ELE` | Control interface, `trophic-contracts` |
| 2 | Spectrum / channel count — fixed white, or tunable channels | Everything optical |
| 3 | Diode selection and drive current | Thermal, efficacy, cost |
| 4 | Optic: bare, lensed, or reflector — this is what delivers CV ≤ 15 % | Uniformity, the whole reason for the band |
| 5 | Thermal path: extrusion profile, whether passive convection suffices at 40 × 60 mm | Extrusion cross-section |
| 6 | IP rating at the bar — it sits above a flood tray | Sealing, connector entry |
| 7 | Length: one bar per bed width (1176 mm) or segmented | Bar count, cost |
| 8 | Make vs buy on the LED board itself | BOM structure |

## 5. Explicitly not decided

No dimensions beyond the inherited 40 × 60 mm envelope. No wattage, no efficacy, no
spectrum, no diode count, no materials, no BOM, no cost, no thermal figures. **The
40 × 60 mm envelope is the space the fixture must fit inside, not a design.**

## 6. Interfaces

| Applies | Standard |
|---|---|
| Yes | ELV boundary (48 V at canopy), Type A RCBO upstream, IP65 keyed connectors, remote drivers, 0–10 V dimming |
| Yes | Platform mechanical standards for any steel bracketry |
| Not yet | Nothing published to `trophic-contracts` — the `light.dim` capability class is defined on the software side (CEA suite ADR-0002) and this product must fit it, not redefine it |

## 7. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **Massing only** — the 40 × 60 mm envelope at both row positions, four tiers |
| Good for | Clash checking, cable routing, service access, visualisation |
| Must NOT be inferred | Extrusion profile, fin geometry, lens form, diode layout, mass, thermal behaviour |

A massing model of this product **already exists** as `06_LED_FIXTURE_ENV` in the rack
assembly. Do not build a second one; a real `LT-A` model starts when §4 is answered.

## 8. Next action

Answer decision 1 (driver model). It is the only item blocking two other documents,
and it is a procurement question rather than a design one.
