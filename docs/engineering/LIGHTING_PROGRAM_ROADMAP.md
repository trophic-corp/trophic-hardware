# Lighting Program Roadmap and Phase Gates

**Products:** `LT-A` (CEA grow bar), `AQ-LT-A` (Core aquarium light), `AQ-LT-B` (WRGB aquarium light), and, if ADR-008 is accepted, the Smart Module
**Created:** 2026-09-11 · **Current phase:** 0A for all three
**Gate evidence framework:** proposed by the QA/Reliability specialist on 2026-09-11 as a *framework*, not an approval. QA approves nothing here; there is no validated product.

This document is deliberately proportionate to a small hardware company. A gate is a
short list of evidence that must exist, at a stated tier, before the next phase
spends money it cannot recover. It is not a stage-gate bureaucracy.

**Evidence tiers (never blurred):** `analysis` (calculation, datasheet, spreadsheet) →
`simulation` (thermal, optical, FEA model) → `prototype test` (measured on real
hardware, small n) → `validated design` (DVT passed on design-intent hardware against
written acceptance criteria, reproducible) → `production-qualified` (PVT passed on
production-process units from approved vendors, EOL test in place). Passing a lower
tier never promotes a claim to a higher one.

---

## 1. Phases

| Phase | Name | What happens | Outputs | Fusion 360? |
|---|---|---|---|---|
| **0A** | Product, market, biological and sourcing research | **Current.** Product intent, reference research, competitor architecture, biological requirements, sourcing landscape, commercial assumptions, unresolved questions | `PRODUCT.md` per product, `docs/references/lighting/**`, `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`, product `sourcing/SOURCING_STRATEGY.md`, this roadmap, ADR-007 | No |
| **0B** | Architecture decisions | Freeze enough to begin engineering: product family, size classes, performance envelopes, spectrum philosophy, Core vs WRGB differentiation, bus voltage, PSU strategy, channel architecture, sharing boundaries, control architecture, serviceability strategy, key commercial limits | Decision records (ADR/EDR as appropriate), `PRODUCT.md` §"Open" rows moved to "Decided", `trophic-contracts` draft device model | **No.** Fusion does not start until the 0B decisions the geometry depends on exist |
| **1** | Engineering concept | Optical, electronics, thermal and mechanical-envelope concepts; preliminary LED/driver trade studies; preliminary BOM; DFM considerations | Concept documents, trade-study records, RFQ packages A–D (see §3) | CAD may begin as class CONCEPT once the relevant inputs are frozen |
| **2** | Detailed engineering | Fusion design, extrusion/chassis, mounting, sealing, MCPCB, driver and control electronics, optics, thermal work, cables and connectors, DFM/DFA | `SYS`, `DWG` series; schematics; CAD class DESIGN | Yes |
| **3** | Engineering prototypes | Physical validation: PAR/PPFD maps, spectra, thermal, electrical, firmware, plant-growth and aquarium trials, condensation and moisture, accelerated ageing, fault tests. **Simulation does not substitute for physical validation** | `QC` verification records | Revisions |
| **4** | Manufacturing qualification | Supplier RFQs, samples, tooling, process validation, supplier qualification, incoming QC, assembly procedure, end-of-line test, pilot BOM, manufacturing pack, serialisation. **Only here do qualified suppliers move toward an AVL** | `MFG` pack, qualification records | Release exports |
| **5** | Pilot release | Core: larger pilot quantity (planning figure ~200). WRGB: deliberately limited, ~10–20 units where economically practical. Real customer evidence before scaling premium inventory | Release manifest `R1`, field-return log | — |
| **6** | Production release | Scale only after engineering validation, manufacturing validation, supplier qualification, field reliability, software stability, warranty economics and actual demand support it | Stage **Released** | — |

## 1a. Phase 0B order (revised 2026-09-11 after the ADR-008 evaluation)

The aquarium and CEA tracks are independent. Within the aquarium track the control-architecture decision now comes first because it sets the end-cap penetration count, cap material freedom, engine cavity and connector access that the extrusion RFQ and the cost test depend on.

| Order | Decision or action | Why here | Owner |
|---|---|---|---|
| CEA-1 | `LT-A` driver model with the ≤ 60 V open-circuit criterion (ND-12) | Unchanged; independent of the aquarium track | Owner + Lighting/Electronics |
| AQ-1 | **Accept or reject ADR-008** (modular engine + port + module vs integrated) | Sets cap penetrations, cap material, cavity, connector access, module SKU | Owner |
| AQ-2 | Port definition: link class, pin count, rail budget, connector class, placement (tether/dock) | Follows AQ-1; feeds end-cap machining and the blanking cap | Lighting/Electronics + Industrial Design |
| AQ-3 | Bus voltage and PSU family (PLATFORM.md §11 #3, #4) | Independent of AQ-1/2 except that DC-in and the port share the end cap; sets 40 V vs 80 V-class engine parts | Lighting/Electronics + Sourcing |
| AQ-4 | WRGB channel count (4 + 1 optional) | Affects engine MCU I/O, not the port | Owner + Lighting |
| AQ-5 | Size classes and whether Core and WRGB share them (§11 #8, #9) | Unchanged in substance; a common end cap now also carries the port, strengthening one cap and one module across lengths. Needs retail sell-through data | Owner |
| AQ-6 | Cost-of-commonality study, now with the port and cavity Δ, the module as its own Δ line, and the MCU-less Core challenger | Needs AQ-1 to AQ-5 | Engineering + Sourcing |
| AQ-7 | RFQ package A (extrusion) and B (end caps with two penetrations) | Needs AQ-6 | Sourcing |
| AQ-8 (parallel) | Raise the channel-array question with the software repository; scope WPC ETA for a module-only radio and BIS scope for a radio-free ELV luminaire; obtain the source of the owner's COGS figures | Regulatory and commercial inputs to AQ-6 | Main session |

Engineering prototypes (Phase 1–2) run on **stock extrusion and CNC**; the die is committed at DVT (`platform/lighting/manufacturing/LAUNCH_PLAN.md`). No CAD before AQ-1, AQ-2 and AQ-5.

## 2. Gates and the evidence each requires

### Gate A — before detailed engineering (0B → 1/2)

Must exist, tier `analysis`:
- Every `PRODUCT.md` "Open — must be decided before CAD" row answered as a record. For `LT-A`: driver model, spectrum, diode class and current class, optic class, thermal path, IP at the bar, length, make/buy. For the aquarium platform: adapter class, bus voltage, radio choice, ingress target, mount concept, size classes, channel count, sharing boundaries.
- Requirements list with numeric, testable acceptance criteria (PPFD band and CV; air rise ≤ 3 K/24 h; Tj ceiling; ingress class; adapter spec; warranty target as a *hypothesis*).
- Thermal budget: watts in, Rth chain, Tj estimate at 40 °C ambient; four-tier stacking allowance for `LT-A`.
- Optical first-order calculation showing CV ≤ 15 % is plausible with the chosen optic at 150 mm (`LT-A`).
- Electrical architecture with the protection concept listed (reverse polarity, overvoltage, wrong adapter, surge path); under ADR-008 also the port definition (link, pins, rail, connector class), the fail-safe state machine and fallback policy, and the protocol version-1 command set.
- Applicable-standards list (IEC 62368-1 / IS 13252, IEC 62471, IEC 60598 / IS 10322, CISPR 15 / IS 6842, IEC 60529, IEC 60068-2) with a one-line "how we will show it" per standard.
- Preliminary FMEA (seed in §5).
- Sourcing risks understood: the supplier landscape read, RFQ packages drafted.

Producers: Systems Architect and Lighting/Electronics; Plant Science for the spectrum records. **Not required:** any test, any CAD beyond envelope, supplier qualification, cost to ±10 %.

### Gate B — before prototype freeze (2 → 3)

Tier `analysis` + `simulation`, plus bench `prototype test` on breadboards where cheap:
- Thermal simulation or lumped model of the final extrusion; `LT-A` stacked-rack case.
- Optical simulation or ray-trace of the chosen optic at design height; predicted PPFD map.
- Schematic and PCB review against the protection concept; creepage and clearance check on the ELV side.
- Bench-measured driver efficiency, dimming linearity and 0–10 V behaviour (`LT-A`) on evaluation hardware.
- Materials rationale (cover, gasket, anodise, fasteners) with datasheet UV and heat data.
- Firmware test plan (aquarium) with persistence, watchdog and reconnect cases written.
- DVT test plan: which §4 tests, sample sizes (typically 3–5 units), pass criteria.
- Components traceable: long-lead LED reels sourced through authorised distribution.

**Not required:** environmental testing on production materials, EMC lab visit, own LM-80 data, tooling.

### Gate C — before manufacturing pilot (3 → 4/5)

Tier `validated design` (DVT on design-intent prototypes, minimum 3 units, reproducible):
- Thermal imaging and Tj estimate confirmed against measured case temperatures at 40 °C soak; `LT-A` four-tier stack test on a real rack (air rise ≤ 3 K/24 h).
- PAR map on the quantum-sensor jig meeting 150–210 µmol/m²/s and CV ≤ 15 % (`LT-A`); spectral output measured (WRGB).
- Ingress and condensation cycling passed; salt fog at least started on aquarium units.
- Electrical abuse tests passed (reverse polarity, wrong adapter, surge, ESD).
- EMC pre-compliance scan with margin.
- Photobiological risk group determined (IEC 62471): by measurement for WRGB and any blue-rich configuration, by analysis with margin for `LT-A` white.
- Firmware acceptance cases passed on prototype hardware.
- Mechanical: mount load, drop, cable flex, connector cycles passed.
- 500–1000 h powered soak on ≥ 3 units with no photon-flux drop beyond measurement noise and no cover discolouration.
- Plant and aquarium trials run per the protocols in `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` Part D.
- Supplier samples verified: sample and first-article stages passed (§4) for LED, driver IC or module, adapter, cover material; FAI on tooled parts.
- DFM completed; EOL test concept written.

**Not required:** full compliance certificates beyond the bought-certified adapter, own LM-80 data, field hours, statistically significant reliability numbers.

### Gate D — before production release (5 → 6)

Tier `production-qualified`:
- PVT: ≥ 10 units (Core) or all pilot units (WRGB) built on the production process and passing EOL test; yield and top fallout modes recorded.
- Pilot field data: WRGB per §6; Core ≥ 3 months with ≥ 50 % of the pilot fleet reporting, return rate and failure modes tabulated.
- Formal EMC report at the class claimed; adapter certificate on file and BIS-registered where applicable; `LT-A` luminaire safety assessment against IEC 60598 (self-declared with test evidence or lab, owner decides).
- Salt fog complete; ongoing powered soak ≥ 2000 h on 3+ units with photon maintenance tracked.
- Warranty decision made as a record with cited evidence.
- Incoming QC, serialisation and a corrective-action loop in operation; critical suppliers qualified.

**Not required:** own LM-80 of the product, six-sigma-style capability programmes, third-party vendor audits.

## 3. What must exist before Phase 2 RFQs (from the manufacturing view)

1. The aquarium platform decisions on positioning, sizes, channels, mounting, ingress; RFQ packages cannot be written without them.
2. A section concept with mass per metre and a thermal budget for the *WRGB* case, so one die vs two can be quoted.
3. **RFQ package A, extrusion:** section drawing, alloy and temper, straightness and twist tolerance, lengths, annual estimate, anodise spec (colour, film thickness, sealing); ask for die cost, ₹/kg, MOQ, lead time, and a DFM review of the section. Two or three Tamil Nadu/Kerala extruders plus one national benchmark.
4. **RFQ package B, end caps:** CNC and moulded routes in parallel on the same interface drawing.
5. **RFQ package C, MCPCB:** dielectric conductivity, base thickness, solder mask, panel; to two Indian fabs and one Chinese benchmark.
6. **RFQ package D, PCBA:** BOM, Gerbers, IPC class, nitrogen reflow yes/no, AOI, test spec; to the two Coimbatore EMS candidates plus one Chennai/Bengaluru fallback.
7. Cover material samples (extruded profile vs sheet) with transmission and haze measured on a sample rig.
8. PSU: single vs dual rating decided; BIS-registered adapter candidates obtained; the fixture's own CRS obligation confirmed.

## 4. Reliability and test categories

| Category | Purpose | Realistic minimal method | Where | Applies |
|---|---|---|---|---|
| Thermal, Tj | LED junction below vendor limit at worst ambient | Tj = Tcase + Rth(j-c)·P per LED; confirm by forward-voltage method on 2 LEDs where the vendor gives Vf(T) | In-house (thermocouples, IR camera, DMM) | All |
| Thermal, ambient soak | Coimbatore/Chennai summer | 40 °C chamber or insulated box, 24–72 h, full output, log Tcase and current | In-house | All |
| Thermal, stacking | Tier above heats tier below | 8 bars on a real rack, 24 h; air rise per tier | In-house (Ooty or Coimbatore rack) | `LT-A` |
| Photon maintenance | Lifetime claim | Vendor LM-80/TM-21 at the *actual* current and measured Tcase; own data by re-measuring soak units on the jig at 0/500/1000/2000 h | Vendor data + in-house jig; own LM-80 is not realistic | All |
| PAR / photometric | PPFD band and CV | Quantum sensor on a grid jig (e.g. 100 mm pitch at 150 mm), dark room, fixed geometry; spectroradiometer once per design and per LED lot change | Jig in-house; spectroradiometer rented or lab | `LT-A` primary; aquarium for spectrum and PAR at 300 mm |
| Electrical abuse | Survive user error | Reverse polarity, 0–1.5× Vin, wrong-adapter plug (12/24/60 V), hot-plug, output short; survive or fail safe | In-house | All |
| Surge | Pumps, heaters, relays on the same circuit | IEC 61000-4-5 on the DC port ±0.5–1 kV; mains side relies on the adapter certificate | Pre-compliance lab, 1 day | Aquarium mainly; `LT-A` driver enclosure |
| ESD | Touch on controls | IEC 61000-4-2 ±4 kV contact / ±8 kV air | Bench ESD gun or lab | Aquarium |
| EMC | Legal sale | CISPR 15 / IS 6842 conducted and radiated pre-scan; formal report before Gate D | Pre-compliance lab; near-field probe in-house | All |
| Ingress, splash | Above open water / flood tray | IEC 60529 IPX4 equivalent, then power-on and inspect | In-house approximation for DVT; lab for the claimed rating | Aquarium; `LT-A` at the decided IP |
| Condensation cycling | Cold light in a humid room | IEC 60068-2-30 style damp-heat cyclic (25↔40 °C, > 95 % RH), 6–10 cycles, powered off then on; inspect for water and corrosion | In-house with humidity box; lab for formal | All |
| Salt fog | Coastal and marine tanks | IEC 60068-2-11 or ASTM B117, 48–96 h on anodised parts, connector, exposed metal | Lab (common in Coimbatore) | Aquarium (mandatory for any marine claim); `LT-A` optional |
| Drop | Shipping and handling | Packaged 0.8–1 m on faces and corners; unpackaged 0.5 m once | In-house | Aquarium |
| Mount load | Arm or clamp on the rim | 3× fixture mass static 24 h; 5000 articulation cycles if adjustable | In-house | Aquarium; `LT-A` saddle on `RK-A-301` |
| Cable flex, connector | Field life | 5000 flex cycles at the gland; 50–100 mating cycles then re-test ingress | In-house | All |
| Cover ageing | Yellowing, crazing | Coupons under the actual LED at 1.5× flux and 60 °C, 1000 h; transmission by quantum sensor | In-house | All (blue-rich WRGB worst) |
| Gasket | Compression set | ISO 815 style: 25 % compression, 70 °C, 72 h; re-test ingress after thermal cycles | In-house | All |
| Anodise | Fertiliser and salt corrosion | Coupons dipped or misted 500 h; salt fog covers marine | In-house + lab | All |
| Firmware | Persistence and recovery | Scripted power cut at random times ×100 with schedule intact; RTC drift over 30 days; watchdog fault injection; BLE reconnect ×50; factory reset | In-house | Aquarium |
| Adapter safety | Mains isolation | Buy only adapters with an IEC 62368-1 report and BIS registration; verify marking, output and connector. Never test mains in-house | Vendor evidence | Aquarium |
| Photobiological | Eye risk | IEC 62471 risk group: measured for WRGB and any high-blue channel; analysis from LED datasheet RG data with margin for `LT-A` white | Lab (one-off; CPRI Bengaluru is a candidate) | `AQ-LT-B` mandatory; others by analysis first |
| Luminaire safety | `LT-A` is a luminaire | IEC 60598-1 relevant clauses at ELV: touch temperature, wiring, marking, IP, mechanical | Self-assessment with test data; lab if sold outside Trophic racks | `LT-A` |
| Touch temperature | Burn risk | IEC 62368-1 touch limits at 40 °C ambient | In-house | All |
| Touch/leakage current over water | Adapter Y-capacitor leakage path through fixture → water → earth | IEC 62368-1 / IEC 60990 method with the fixture over conductive water | Lab | Aquarium |

## 5. Top risks (FMEA seed) and the evidence that retires each

**`LT-A`:** (1) Tj exceeds limit in a stacked 4-tier rack at 40 °C → stack test on a real rack. (2) CV > 15 % at canopy with the chosen optic → jig map on 3 units, repeated after lot change. (3) Condensation ingress at the connector above a flood tray → IPX4 + damp-heat cyclic then power-on. (4) Two bars on one 0–10 V pair behave non-identically → bench test, current mismatch < 5 %. (5) Cover yellowing pulls PPFD below 150 → coupon test plus soak-unit re-measure. (6) Anodise or fastener corrosion from fertiliser mist → coupons and a deployed unit inspected at 3 months. (7) Off-state not fail-safe or photoperiod-off ambiguous (open decision 1) → decision record then bench test of off-state leakage light. (8) Bar exceeds 40 × 60 mm or saddle fit fails → FAI against `RK-A-301` and the envelope. (9) The remote CC driver's open-circuit voltage exceeds 60 V at the canopy connector → driver selection criterion and a measurement.

**`AQ-LT-A` Core:** (1) Wrong or counterfeit adapter used by the customer → wrong-adapter abuse test, keyed connector, adapter sourcing controls. (2) Splash or condensation reaches the PCB → IPX4 and damp-heat cyclic; conformal coating verified. (3) Schedule lost on power cut → 100-cycle power-cut script. (4) BLE/Wi-Fi reconnect failure → 50-cycle test and pilot logs. (5) Mount slips or arm fatigues → 3× load and cycle test. (6) Touch temperature or thermal shutdown at 40 °C → soak test with touch-temperature map. (7) Connector corrosion on marine tanks → salt fog and coastal pilot units.

**`AQ-LT-B` WRGB:** (1) Photobiological risk group too high for unlabelled sale → IEC 62471 measurement and labelling. (2) Blue-channel cover degradation → coupon test at 1.5× blue flux. (3) Channel colour drift or unit-to-unit mismatch with heat → spectroradiometer cold and hot. (4) Higher power drives Tj beyond the LM-80 test point → Tj estimate at measured Tcase vs vendor condition. (5) Multichannel driver EMC failure → pre-compliance then formal scan. (6) Salt creep into a denser board → salt fog, condensation cycling, conformal coat. (7) Multichannel schedule corrupts persistence → extended persistence and watchdog fault injection. (8) Pilot too small to see failure rates → §6 before scaling.

## 6. WRGB: validation required before production exceeds pilot quantity

Before any build above 10–20 units: all pilot units serialised and ≥ 80 % traceable to a known installation; ≥ 1000 h per unit average and ≥ 3 months calendar on ≥ 10 units, including ≥ 3 on marine or coastal tanks if marine is ever claimed; field returns ≤ 2 units with root cause closed and corrective action verified on hardware; tests complete at `validated design` tier: IEC 62471 measured risk group and labelling, salt fog 96 h, condensation cycling, formal EMC, 2000 h photon maintenance on 3 units with a blue-channel cover transmission check, app and firmware persistence and reconnect cases re-run on pilot firmware. Any change to LED bin, cover material or driver between pilot and production reopens the affected tests.

## 7. Warranty evidence (Core), for the owner's decision

| Failure mode | Evidence supporting 6 months | Evidence supporting 12 months |
|---|---|---|
| Adapter | Certified adapter with vendor warranty ≥ 12 months; wrong-adapter test | Same plus adapter field returns from pilot |
| Controller / PCB | Abuse, ESD, surge passed; 1000 h soak, n = 3 | 2000 h soak, n ≥ 5, zero controller failures; damp-heat cyclic passed with conformal coat verified |
| LED board | TM-21 projection at measured Tj; 1000 h photon maintenance within noise | Same plus 2000 h data and one lot-to-lot check |
| Cover | 1000 h coupon test, transmission loss < 5 % | Same, extrapolated with margin to 8760 h |
| Mount | 3× static load, cycle test | Same plus pilot field returns |
| Connector corrosion | Salt fog 48 h, mating cycles, condensation cycling | Salt fog 96 h plus 3 months of coastal field units |

Cross-cutting: a field-return log with serial, date, mode and root cause from pilot day one; return-rate trend at 3 and 6 months. **Serviceability is the warranty-cost lever:** if adapter, controller and LED board are replaceable modules, a 12-month warranty cost is dominated by cheap module swaps rather than whole-unit replacement. Competitor norms are in `docs/references/lighting/COMPETITOR_LIGHTING_REFERENCE.md` §4 (1 year is the category floor; Fluval offers 3).

## 8. Supplier qualification stages (small-company scale)

| Stage | Evidence | Meaning |
|---|---|---|
| Sample | Datasheet, RoHS declaration, samples bench-tested; for LEDs an LM-80 report at the relevant current and temperature, bin code | May be used in prototypes |
| First article | Dimensional FAI on 3–5 parts against the drawing; material certificate; for adapters the 62368-1 report and BIS number verified on the BIS portal; for LED reels the authorised-distributor invoice, reel label photo, lot and date code recorded | May be used in DVT |
| Pilot lot | Incoming inspection (AQL 1.0–2.5, ISO 2859-1, or a fixed sample such as 8 of 50); functional test on a sample; yield recorded | May be used in pilot production |
| Qualified (approved vendor) | Pilot lot passed; no open corrective actions; second-source status noted; entry in an approved-vendor list with part number and revision and what was verified | May be used in production until part or process changes |

"Approved vendor" means a specific part from a specific supplier at a specific revision, verified by the evidence above, not the company in general. LED traceability: buy LEDs, driver ICs and radio modules only from the manufacturer or authorised distribution; refuse brokers; record reel label, lot, bin and date code at goods-in; spot-check Vf and spectrum of 5 LEDs per reel; keep lot-to-serial mapping.

## 9. Production and release gate logic

**Incoming QC:** per §8 sampling; PCBAs: visual, AOI report, first-power test on a sample; covers: transmission and dimensional spot check; adapters: label and certificate check, output and load test on 2 %.

**End-of-line test, every unit:** power-on current and voltage at rated dim; two-point dimming check; PAR spot check on a single-point jig against a golden unit (±10 %); firmware version, RTC set, schedule write/read, radio advertisement seen, factory reset works (aquarium); `LT-A`: 0–10 V response and connector keying. Ingress: sampled (e.g. 1 in 25) spray plus a visual gasket check on every unit. Burn-in: yes during pilot (4–8 h powered) to learn the infant-mortality rate; shorten for production once pilot data shows it catches nothing.

**Serialisation minimum:** serial on the controller PCBA (label and stored in firmware), mirrored on the housing label. Per serial record: build date, LED reel lot, PCBA lot, adapter lot, firmware version, EOL results, later field returns. Under the delayed-differentiation model the housing kit carries an extrusion lot and anodise batch code, and the serial links housing kit to electronics kit at final assembly.

**Stage meaning in this repository, mapped to the existing vocabulary:**

| Stage | Means |
|---|---|
| Phase 0 | Scope only, no engineering (current) |
| Concept | Gate A passed; tier `analysis` |
| Design | Gate B passed; CAD is class DESIGN only after the open decisions are recorded |
| Validated | Gate C passed: DVT on design-intent hardware, reproducible, recorded in a `verification/` record. The owner marks it, never an agent |
| Released | Gate D passed: PVT units, EOL in operation, compliance evidence on file, warranty decision recorded |

## 10. Readiness today

**Not yet, all three products.** Every item above is at tier *none*. The first artifacts required are the Gate A decision records, starting with `LT-A` open decision 1 (driver model) and the aquarium platform's 0B decisions listed in `products/aquarium/lighting/PLATFORM.md` §8.
