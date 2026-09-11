# PRODUCT — Premium Programmable WRGB Aquascaping Light (`AQ-LT-B`)

| | |
|---|---|
| **Product ID** | `AQ-LT-B` |
| **Family** | Aquarium / Aquascaping · Lighting |
| **Owner class** | A — Product |
| **Stage** | **Phase 0A research complete (2026-09-11) — no engineering; 0B decisions pending** |
| **Platform** | Intended shared aquarium lighting platform with `AQ-LT-A`, ADR-007; **control architecture per ADR-008 (PROPOSED): WRGB Light Engine with a control port, sold with the shared Smart Module; standalone operation is a safety property and possibly not a sold SKU**; see `../PLATFORM.md` §1a |
| **Authoritative CAD** | None |

---

## 1. What the product is

A premium planted-aquarium LED light for serious, high-tech (CO₂-injected)
aquascaping, with **independently controllable spectral channels**, higher output
than the Core light, the same standalone schedule foundation and the same Trophic
aquarium app ecosystem. It is materially different from `AQ-LT-A` in its LED board,
spectral architecture, channel count, driver stage, thermal load and possibly optics,
and is intended to share the mechanical, power, control and firmware platform.

## 2. Why it exists

It carries the brand's technical credibility in the segment where Chihiros WRGB II,
Twinstar S-line and Week Aqua Pro sell at ₹15,000–39,000 in India
(`COMPETITOR_LIGHTING_REFERENCE.md` §2). It is deliberately a **small pilot first**:
Trophic does not want to commit to 100 finished units per size. The owner's indicative
100-unit manufacturing figures (~₹10,000 / ₹14,000 / ₹19,000 for ~30 / 45 / 60 cm) are
planning assumptions, not COGS; they are recorded because they motivate making the
common parts at Core volume and assembling only **10–20 WRGB units** to validate demand.

## 3. Inherited constraints — DECIDED

| Constraint | Value | Source |
|---|---|---|
| Two products on one intended shared platform; WRGB is the late-differentiated premium variant | Sharing per `PLATFORM.md` §3 and the cost test in §4 | ADR-007 §1–3 |
| Standalone-first; app and controller optional; no cloud dependency | | ADR-007 §4 |
| Power topology | External certified adapter → ELV DC → internal CC drivers, one per channel | ADR-007 §5 |
| Pilot quantity before scale | 10–20 units; scaling gated by the validation in `LIGHTING_PROGRAM_ROADMAP.md` §6 | Owner intent 2026-09-11; roadmap |
| Safe with no power and no signal | Resume last schedule on restore | `platform/electrical-standards` §4 |
| Same device model and protocol as Core; channel count is a property | | ADR-007 consequences; `PLATFORM.md` §8 |

## 4. Industry and research reference points — NOT TROPHIC DECISIONS

| Item | Reference | Note |
|---|---|---|
| Competitor channel architectures | 3-ch RGB (Chihiros WRGB II, Slim), 4-ch WRGB 4-in-1 (WRGB II Pro, Netlea), 5-ch RGB+UV (Week Aqua Pro) | Competitor reference §3 |
| Competitor 60 cm figures | 45–74 W, 2,400–6,630 lm claimed; no published PAR or CRI except ONF CRI 90 | Competitor reference §2 |
| Indian prices, 2026-09-11 | Chihiros WRGB II 60 ₹24,725; Pro 60 ₹28,275; Slim 60 ₹15,525; Twinstar 600S III ₹27,499; Week Aqua Pro ₹13,900–38,900 | Competitor reference §2 |
| Channel-count engineering | 3-ch RGB cannot make efficient high-CRI white (Rf < 80); 4-ch WRGB is the efficiency-sane norm; a 5th channel (660 nm, royal blue) buys pigment appearance at a driver, bin and mixing cost | `LIGHTING_PLATFORM_REFERENCE.md` B3 |
| Channel-count biology | A white channel gives the evidence-supported broad baseline; 660 nm is the most photon-efficient way to raise PPFD without more blue; 450 nm is where compactness/anthocyanin extrapolations act; green has no aquatic physiological role beyond rendering; far-red has no case | D2 |
| Red choice | 620–630 nm gives ~5× the visual red per watt; 660 nm gives more red PAR and pigment saturation but needs 2–3× the radiant power for the same look | B3 |
| Colour mixing | Discrete dies at ≥ 10 mm pitch at 15–30 cm height produce coloured shadows; diffuser, lens array or mixing chamber are the options; shimmer vs uniformity is an aesthetic decision with thermal and optical cost | B3 |
| Dimming | ≥ 12-bit PWM at ≥ 3 kHz for smooth low-end ramps and camera-safe video | B3 |
| Thermal | ~15–40 W class dissipation over 30–60 cm at high-tech output; Tj ≤ 85 °C to limit red and green drift; RGB needs ~30–50 % more input than phosphor white for equal lumens | B3 |
| UVA | No biological case; materials ageing, IEC 62471 UV labelling and an extra channel. **Excluded unless evidence appears** | B3, D2 |
| Photobiological | A 6500 K + royal blue bar viewed at 200 mm needs an IEC 62471 measurement | B3 |
| "RGB makes reds pop" | A rendering effect, instant and reversible; whether RGB *makes* more red pigment is unproven and must not be claimed | D2 |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks | Owner |
|---|---|---|---|
| 1 | Channel count: 4 (WRGB) with a 5th optional, or 3, or 5 | Driver stage, MCPCB, firmware, app | Owner (positioning) + Lighting; bench SPD tests decide the 5th |
| 2 | Package class: discrete high-power common-footprint colour, multi-die RGBW, or dense mid-power arrays | MCPCB, optics, thermal, cost | Engineering trade study (Phase 1) |
| 3 | Red channel: 620–630 nm, 660 nm, or both | Rendering vs PAR | Engineering after SPD tests |
| 4 | Colour-mixing approach: diffuser, lens array, mixing chamber | Cover (shared or not), optical loss, thermal, shimmer | Engineering + Industrial Design |
| 5 | Size classes: 30/45/60 confirmed or not; identical to Core or not | Everything mechanical | **OWNER DECISION REQUIRED** (`PLATFORM.md` §6) |
| 6 | Whether the shared chassis passes the cost test for the WRGB thermal envelope | Extrusion die | Engineering, owner sign-off (`PLATFORM.md` §4) |
| 7 | Bus voltage and PSU rating per size class (shared family, own rating) | Driver stage, adapter | Lighting/Electronics |
| 8 | Binning strategy at 10–20 units: one reel per colour, single flux and wavelength bin per lot | Sourcing, unit-to-unit hue match | Engineering + Sourcing |
| 9 | What "measurable biological benefit" the WRGB must show over Core before any biological claim is made | Marketing claims | Owner; trial protocol in D2 |
| 10 | Validation set before production exceeds pilot | Scaling | QA gate (roadmap §6) |
| 11 | Mounting, ingress, control and serviceability | As for Core | Shared decisions in `core-smart-light/PRODUCT.md` §5 and `PLATFORM.md` |
| 12 | Accept ADR-008; whether WRGB Standalone is a sold SKU; per-channel control lives in the module and the engine exposes channels at handshake | SKU list, firmware split, app | **OWNER DECISION REQUIRED** |

## 6. Explicitly not decided

No dimensions, no extrusion section, no LED type, count, pitch or current, no
channel count, no wattage, no output figure, no bus voltage, no PSU rating, no
connector, no IP rating, no materials, no BOM, no cost, no warranty. The ₹ figures in
§2 are planning assumptions.

## 7. Interfaces

As for `AQ-LT-A` §7, with one addition: per-channel dimming requires the software
side's `light.dim` capability class to support a channel array; this must be raised
with the software repository now (`PLATFORM.md` §8) and published to
`trophic-contracts` as a property of the device model, not a new device type.

## 8. Sourcing

Product-specific implications: `sourcing/SOURCING_STRATEGY.md`. Shared landscape:
`docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`.

## 9. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No.** Size classes, chassis sharing and channel count all shape the form |
| What would make it possible | Decisions 5 and 6 above plus the Core mounting and ingress decisions |
| What must NOT be inferred from any early model | Extrusion section, fin geometry, LED layout, cover form, mass, thermal behaviour |

## 10. Next action

Decide channel count (decision 1) at the 4 + 1-optional level so the driver-stage
architecture and the MCPCB modulus can be traded against the shared chassis in Phase 1;
it is a positioning decision the owner must make with Lighting/Electronics input.
