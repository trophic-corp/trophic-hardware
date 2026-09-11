# PRODUCT — LED Grow Bar (`LT-A`)

| | |
|---|---|
| **Product ID** | `LT-A` |
| **Family** | CEA · Lighting |
| **Owner class** | A — Product |
| **Stage** | **Phase 0A research complete (2026-09-11) — no engineering; 0B decisions pending** |
| **Authoritative CAD** | None. `06_LED_FIXTURE_ENV` in `CEA_RACK_INTEGRATED_v3` is a **keep-out envelope**, not a fixture design |
| **Reference material** | `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` Parts A, B1, D1; `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`; `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md` |

---

## 1. What the product is

A dimmable LED bar for CEA growing racks, mounting on the `RK-A-301` rail, fed from the
rack's remote LED drivers with a 0–10 V dimming pair. Two bars share one dimming pair,
so a tier is one control zone. Microgreens are the initial primary crop class. One
modular lighting platform, not a retail SKU family; integrated with the Trophic CEA
suite; optimised for crop performance and industrial operation.

## 2. Why it exists

LED fixtures are bought in today and excluded from every rack cost figure. They are
the largest uncosted line in the system, the component most likely to determine crop
performance, and the one the rack has already been designed around. Making them
in-house closes the cost model and puts the optical result under Trophic's control.

**Priorities (owner intent):** PPFD, uniformity, efficacy, thermal performance,
reliability, crop repeatability, serviceability, manufacturability, controllability.

## 3. Inherited constraints — DECIDED

Every row is fixed by the rack and is not open to this product. **One correction
(2026-09-11):** the supply row previously read "48 V DC"; RK-A-SYS §07 actually
permits either a constant-voltage 48 V DC supply or a constant-current supply with
output ≤ 60 V. Which applies is decision 1 below, not an inherited fact.

| Constraint | Value | Source |
|---|---|---|
| Supply to fixture | **Constant-voltage 48 V DC, or constant-current with output ≤ 60 V** | `RK-A-SYS` Rev 2 §07 (verified 2026-09-11) |
| Dimming | **0–10 V pair per tier**, two bars share one pair | `RK-A-SYS` Rev 2 §07 |
| Connector | IP65, keyed | `RK-A-SYS` Rev 2 §07 |
| Driver location | **Remote, in the end enclosure**, not at the fixture | `RK-A-SYS` Rev 2 §07 |
| Fixtures per rack | 8 (2 rows × 4 tiers) | `RK-A R1` manifest, `06_LED_FIXTURE_ENV` qty 8 |
| Keep-out envelope | `LED_Fixture_H` **40 mm** × `LED_Fixture_W` **60 mm** | `RK-A-PARAM` Rev 1 |
| Mounting rail | `RK-A-301`, `LED_Rail_Size` 20 mm; LED saddles per EDR-020 | `RK-A-PARAM` Rev 1; EDR-020 |
| Row positions | Y **148–208** and Y **352–412** mm from the rack front face | EDR-003 |
| Clearance to canopy | `LED_Clearance` **150 mm** above a 139 mm canopy | `RK-A-PARAM` Rev 1 |
| Bed | 1176 × 569 mm | `RK-A-PARAM` Rev 1 |
| ELV boundary | Fixture sits **at canopy level → ELV DC only**. No mains at the bar | Platform electrical standards |
| PPFD operating band | **150–210 µmol/m²/s**, **CV ≤ 15 %** at canopy | `RK-A-SYS` §00; `RK-A-MFG` QC criterion T2 |
| PPFD limits | Below **100** suppresses growth; above **210** is the operating ceiling. **The rationale "above 210 risks photoinhibition" is a Trophic assumption, not a finding: see ND-11** | CEA suite `safety-rules.json`, sourced to Phase A; challenged by D1 |
| Verification method | Portable quantum sensor on a jig, commissioning and quarterly; no fixed PAR sensor | `trophic-contracts` `capabilities/absent-by-design.md` |
| Thermal acceptance | Air rise **≤ 3 K** over 24 h continuous; no LED derating | `RK-A-MFG` Rev 2, test P2 |
| RCD | Type A on the supplying circuit | EDR-008 |
| Tier fan | 178 m³/h EC fan per tier, PWM or 0–10 V with tacho | `IF-RK-A-ELE` |

## 4. Spectrum philosophy — owner preference, research position, not yet frozen

**Owner Gen-1 preference:** engineered fixed horticultural spectrum + programmable
intensity + programmable photoperiod; no spectral sliders for the CEA operator.

**Research position (2026-09-11, Plant Science + Lighting/Electronics, reference D1
and B1):** the evidence **supports the preference**. Yield and morphology in
microgreens are driven by intensity and photoperiod; spectral effects are quality-only,
species-specific and directionally inconsistent; the strongest "tunable" use case
(pre-harvest blue finishing) is confounded with an intensity drop a dimmer reproduces.
Tunability is justified only for an R&D fixture, a future nutrition-labelled crop, or
mixed-crop rooms, none of which is Gen-1. On the hardware side every added channel
multiplies remote drivers, 0–10 V pairs and connector pins and crosses frozen rack
interfaces (ICR territory), so tunability is not free either.

**Evidence-backed design space for the fixed spectrum (ranges, not a spec):** broad
phosphor white base; blue 15–25 % of PPFD; green 15–30 %; added ~660 nm red bringing
red to ~40–60 %; far-red 0–7 % optional, decided by trial; no UV-A. CCT ~3500–5700 K
is an **assumption** with no peer-reviewed microgreen comparison, NEEDS VALIDATION.

This section becomes DECIDED only when recorded as a decision record after the Ooty
trial in D1 (radish, mustard or kale, sunflower, pea; non-inferiority ≥ 95 % fresh
weight vs the bought-in reference).

## 5. Open — must be decided before CAD

| # | Decision required | Blocks | Notes from 2026-09-11 research |
|---|---|---|---|
| 1 | **Driver model and supply reading.** CV 48 V bus vs remote CC ≤ 60 V; also decides whether photoperiod-off is dim-to-off or a relay. Open in the CEA suite as `[OQ-14]` and in `IF-RK-A-ELE` | Control interface, `trophic-contracts`, everything electrical | Reading (a) remote CC per bar keeps the bar passive; **the driver's open-circuit voltage must be ≤ 60 V** (Mean Well XLG-H class; L/M classes present 115–225 V at the canopy connector when a bar is unplugged) — **ND-12**. Reading (b) CV bus + on-bar CC contradicts "driver not at the fixture" and needs an ICR. Open dim wires on a sourcing driver → full output, so **hardware, not software, must cap 100 % at ≤ 210 µmol/m²/s** |
| 2 | Spectrum: confirm fixed (§4) by trial; then record | Everything optical | Research supports fixed |
| 3 | LED class and drive current class | Thermal, efficacy, cost | Samsung horticultural parts are last-time-buy (LED business exit, production ended H1 2026); candidates are Bridgelux/Nichia/Lumileds/Osram/Seoul horti whites and Osram/Lumileds 660 nm; B1 |
| 4 | Optic: lens, reflector, diffuser, edge baffles | CV ≤ 15 % | Bare boards give bed edges at ~25–30 % of centre because the EDR-003 rows sit ~180 mm inboard; realistic fixture-only CV 10–20 % with lenses or reflectors; ≤ 15 % likely needs edge reflectors or tray-side baffles (a rack-side conversation) |
| 5 | Thermal path: extrusion profile, passive convection at 40 × 60 mm | Extrusion section | Illustrative 25–50 W per bar, 15–30 W heat, ΔT 5–10 K plausible; **tier air rise ≤ 3 K is tight with four stacked tiers at reduced fan speed**, NEEDS VALIDATION |
| 6 | IP rating at the bar, above a flood tray | Sealing, connector entry | |
| 7 | Length: one bar per bed width (1176 mm) or segmented | Bar count, MCPCB panels | 2–3 MCPCB segments (~360–560 mm) likely regardless; Indian fab panel limits RESEARCH REQUIRED |
| 8 | Make vs buy on the LED board; MCPCB vs FR-4 with thermal vias for mid-power whites | BOM structure | FR-4 2 oz often adequate for 3030 whites ≤ 100 mA; high-current reds push to MCPCB |
| 9 | Re-populatable footprint strategy (dual-footprint positions in one string) | Later spectrum adjustment without channels | B1 |
| 10 | Regulatory route: is a DC-only ELV bar a CRS "luminaire" (IS 10322) or an LED module (IS 16104/16103)? IEC 62471 risk group | Marking, test scope | RESEARCH REQUIRED with BIS counsel |
| 11 | Dimming floor: the fixture must dim to ≤ ~75 µmol/m²/s without flicker for low-PPFD species (broccoli, cabbage, pea) | Driver choice | D1 |
| 12 | What, if anything, is shared with the aquarium platform (X1) | Toolchain, supplier base | Recommendation: share LED knowledge, MCPCB process, driver-IC know-how, test jigs and dimming maths; not interfaces, PSU, connector or form factor |

## 6. Explicitly not decided

No dimensions beyond the inherited 40 × 60 mm envelope. No wattage, no efficacy, no
spectrum, no diode count, no materials, no BOM, no cost, no thermal figures. Every
number in §4 and §5 marked illustrative is illustrative. **The 40 × 60 mm envelope is
the space the fixture must fit inside, not a design.**

## 7. Interfaces

| Applies | Standard |
|---|---|
| Yes | ELV boundary at canopy, Type A RCBO upstream, IP65 keyed connectors, remote drivers, one 0–10 V pair per tier |
| Yes | Platform mechanical standards for any steel bracketry |
| Not yet | Nothing published to `trophic-contracts`; the `light.dim` capability class is defined on the software side (CEA suite ADR-0002) and this product must fit it, not redefine it |
| Conflict surfaced, not resolved | Any tunable-spectrum variant would need N 0–10 V pairs per tier, N drivers per bar and a larger connector, all crossing frozen rack interfaces. Recorded as a conflict; no redesign proposed |

## 8. Sourcing

Product-specific implications: `sourcing/SOURCING_STRATEGY.md`. Shared landscape:
`docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`.

## 9. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **Massing only**, and it already exists as `06_LED_FIXTURE_ENV`. Do not build a second one |
| Good for | Clash checking, cable routing, service access, visualisation |
| Must NOT be inferred | Extrusion profile, fin geometry, lens form, diode layout, mass, thermal behaviour |

## 10. Next action

Answer decision 1 (driver model and supply reading, with the ≤ 60 V open-circuit
criterion). It blocks two other documents, it is a procurement question rather than a
design one, and it now has a concrete selection criterion.
