# PRODUCT — Core Smart Aquascaping Light (`AQ-LT-A`)

| | |
|---|---|
| **Product ID** | `AQ-LT-A` |
| **Family** | Aquarium / Aquascaping · Lighting |
| **Owner class** | A — Product |
| **Stage** | **Phase 0A research complete (2026-09-11) — no engineering; 0B decisions pending** |
| **Platform** | Intended shared aquarium lighting platform with `AQ-LT-B`, ADR-007; **control architecture per ADR-008 (PROPOSED): Core Light Engine with a control port, sold as Core Basic or Core Smart (with the shared Smart Module)**; see `../PLATFORM.md` §1a |
| **Authoritative CAD** | None |

*This document replaced the earlier single "Programmable aquarium light" document on
2026-09-11 (moved with `git mv`). The per-channel programmable intent moved to
`AQ-LT-B`; the earlier reference points and open decisions are carried forward in
§4 and §5.*

---

## 1. What the product is

A planted-aquarium LED light for nano to mid-size tanks with a **fixed, engineered
spectrum** driven as **one logical intensity channel**, with dimming, a local
schedule, sunrise/sunset ramps and acclimation. It runs standalone from its own
stored schedule; a phone app (and later an aquarium controller) writes the schedule
but is never required for operation. External certified DC adapter; the fixture
contains the constant-current driver and the controller.

## 2. Why it exists

It is the intended higher-volume, higher-value aquarium product and the one that
funds the shared platform. The Indian Core price point is occupied by a thin-spec,
white-only, non-dimmable incumbent (`COMPETITOR_LIGHTING_REFERENCE.md` §2, Neo Helios
XP, ₹1,910–3,999). The gap is dimming, scheduling, measured and published
performance, a stated ingress class and a stated warranty, delivered with visible
care in execution rather than raw output.

**Owner intent (not engineering decisions):** retail envelope ~₹2,500–3,500 subject to
validation; ~200 MOQ planning; preliminary manufacturing figures around ₹1,400 /
₹1,600 for the smaller size classes are **commercial planning assumptions requiring
scope validation, not approved COGS**; the objective is not the cheapest LED but a
cost-efficient, sufficiently reliable, visually good engine that benefits from the
shared platform.

## 3. Inherited constraints — DECIDED

| Constraint | Value | Source |
|---|---|---|
| Two products on one intended shared platform with late differentiation | Core is the volume product; sharing per `PLATFORM.md` §3 and the cost test in §4 | ADR-007 §1–3 |
| Standalone-first | Local schedule persistence; app/controller/cloud optional; no continuous cloud dependency | ADR-007 §4 |
| Power topology | 230 V AC → external certified adapter → ELV DC bus → fixture → internal CC driver | ADR-007 §5 |
| **One logical intensity channel** exposed to the user, whatever the engine contains | Decided | ADR-007 §6 |
| Safe with no power and no signal; software never commands a safe state | Fail state on loss of control is "resume last schedule", never full-on | `platform/electrical-standards` §4; `PLATFORM.md` §8 |
| Connector discipline | Keyed; ingress-appropriate for a wet zone | `platform/electrical-standards` §5 (in principle; the CEA mains schedule does not apply) |
| Identifier standard | `AQ-LT-A`; part-number bands to be defined here when parts exist | `platform/IDENTIFIER_STANDARD.md` |

## 4. Industry and research reference points — NOT TROPHIC DECISIONS

| Item | Reference | Note |
|---|---|---|
| Tank lengths served | 30 / 45 / 60 / 90 / 120 cm; Indian nano 30 × 18 × 18, 36 × 22 × 26, 40 cm cubes, 45 × 27 × 30, 60 × 30 × 36, 2–3 ft rimmed | Carried from the earlier document; size decision is `PLATFORM.md` §6 |
| Mounting | Rimless clamp/legs, rail stand, suspension; rimless glass 6–12 mm is the aquascaping norm | Carried forward |
| Ingress | Competitors mostly IP43 or unrated; IP67 is a marketing differentiator; condensation and salt creep are the real problems | Carried forward; competitor reference §3 |
| Substrate PPFD tiers (field) | 20–40 shade, 40–90 typical, 90–150 demanding reds; carbon, not photons, is usually the binding limit | `LIGHTING_PLATFORM_REFERENCE.md` D2 |
| Photoperiod (field) | 6–10 h; ramps and "siesta" have no algae evidence | D2 |
| Core engine classes biologically adequate | White-only, warm+cool, white+red, white+red+blue all adequate for low-to-medium tech; no biological case for user spectral control | D2 |
| Lead engine candidate (engineering) | White + 660 nm red, series-mixed on one string, PWM-dimmed; high-CRI white-only as the baseline reference; fixed-ratio RGB rejected for Core | B2 |
| Incumbent price band (India, 2026-09-11) | ₹1,910–3,999 for 30–60 cm | Competitor reference §2 |
| Warranty norms | 1 year is the category floor; 2 years at some EU/UK retailers; Fluval 3 years | Competitor reference §4 |

## 5. Open — must be decided before CAD

Carried-forward decisions from the earlier document are marked (†); the rest arise from ADR-007 and the 2026-09-11 research.

| # | Decision required | Blocks | Owner |
|---|---|---|---|
| 1 | Positioning confirmed as above (†1) | Everything | Owner: **confirmed by intent 2026-09-11**; retail envelope still NEEDS VALIDATION |
| 2 | Size classes: 30/40, 30/45, or the common 30/45/60 (†2; `PLATFORM.md` §6) | Length, output, family structure, MCPCB modulus | **OWNER DECISION REQUIRED** |
| 3 | Engine class: white-only vs white+red vs white+red+blue (†3 reframed) | Optics, MCPCB, thermal, rendering | Engineering after bench SPD and the D2 trial |
| 4 | Mounting system: legs, clamp, suspension (†4) | The whole mechanical design | Owner + Industrial Design + engineering |
| 5 | Ingress target and condensation handling (†5) | Sealing, materials, service access | Engineering; drives §9 of the platform |
| 6 | Control: accept ADR-008 (engine MCU + signal-only port + optional Smart Module, no radio in the engine) or integrated control; then radio class and RTC backup in the module (†6 reframed) | Electronics, end cap, cable, ingress, cost, tiers | **OWNER DECISION REQUIRED** (ADR-008), then engineering |
| 7 | Whether anything from `LT-A` is reused (†7, X1) | Development cost | Owner after engineering comparison; recommendation in `PLATFORM.md` §11 #10 |
| 8 | Bus voltage and PSU family (shared) | Driver stage, connector, adapter sourcing | Lighting/Electronics; `PLATFORM.md` §7 |
| 9 | Serviceable modules vs sealed-and-replace | BOM, sealing, warranty economics | Owner with the warranty decision |
| 10 | Warranty (owner believes 3–6 months initially; 12 months to be tested against evidence) | Service model, spares | **OWNER DECISION REQUIRED**, not before Gate C; evidence table in roadmap §7 |
| 11 | Dimming method: PWM (colour-stable for a mixed engine) vs analogue vs hybrid; PWM frequency and bit depth | Driver design, flicker, camera behaviour | Engineering; reference A3 and B3 |
| 12 | Binning tolerance for white (3-step MacAdam is an assumption) and 660 nm peak bin | Sourcing, unit-to-unit consistency | Engineering |
| 13 | Price and go/no-go for Core in batch 1: the planning cost model shows no contribution at 50–100-unit costs below ~₹4,000–5,000 retail (`platform/lighting/costing/LIGHTING_BOM_COST_MODEL.md` §3–§5, §8) | Launch plan, positioning | **OWNER DECISION REQUIRED** |

## 6. Explicitly not decided

No dimensions, no extrusion section, no LED type, count, pitch or current, no wattage,
no lumen or PPFD figure, no CCT, no bus voltage, no PSU rating, no connector, no IP
rating, no materials, no finish (the design direction in `PLATFORM.md` §10 is a brief),
no BOM, no cost, no warranty. The ₹ figures in §2 are planning assumptions.

## 7. Interfaces

| Applies | Standard or boundary |
|---|---|
| In principle | Fail-safe with no power and no signal; keyed connectors; conformal-coating and enclosure discipline |
| No | CEA mains protection schedule (Type A RCBO, SPD, TN-S); platform mechanical standards for fabricated steel |
| To software | `light.dim` + `light.schedule` capability classes (CEA suite ADR-0002). Device model and schedule semantics to be drafted into `trophic-contracts` at Concept; transport at Design freeze. Never geometry, BOM or cost. See `PLATFORM.md` §8 |
| To `AQ-CT-A` | Optional client of the same device model; X4 stays open |
| Regulatory (research, not interpretation) | Adapter under BIS CRS (IS 13252 → IS/IEC 62368-1); WPC ETA for the radio; whether the fixture itself is caught by IS 10322 is RESEARCH REQUIRED; IEC 62471 assessment by analysis first |

## 8. Sourcing

Product-specific implications: `sourcing/SOURCING_STRATEGY.md`. Shared landscape:
`docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`.

## 9. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No.** Length classes, mounting and the shared-chassis decision determine the entire form |
| What would make it possible | Decisions 2, 4 and 5 above and the platform cost test (`PLATFORM.md` §4) |
| What must NOT be inferred from any early model | Extrusion section, fin geometry, cover form, LED layout, mass, thermal behaviour |

## 10. Next action

Answer decision 2 (size classes) through the framework in `PLATFORM.md` §6, because it
gates RFQ package A (extrusion) and the cost test, and it is an owner decision that
needs retail sell-through evidence rather than engineering.
