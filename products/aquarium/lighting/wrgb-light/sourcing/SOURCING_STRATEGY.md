# Sourcing Strategy — `AQ-LT-B` Premium Programmable WRGB Aquascaping Light

**Status:** Phase 0A, research 2026-09-11 · **Owner:** Manufacturing/Sourcing with the main session
**Shared landscape (do not duplicate here):** `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`
**Platform manufacturing model:** `../../PLATFORM.md` §4–5
**Core strategy (read first; only differences are recorded here):** `../../core-smart-light/sourcing/SOURCING_STRATEGY.md`

Supplier statuses: researched · longlisted · candidate · RFQ required · sample
required · qualification required. Nothing is approved, qualified or on an AVL.

---

## 1. Volume and cost context (owner planning assumptions, not COGS)

**10–20 pilot units** across up to three size classes, with the common housing kit,
end caps, gaskets, mounting, cable hardware, cartons and (if shared) control board
drawn from the Core run. The owner's 100-unit figures (~₹10k / 14k / 19k) are the
reason WRGB does not get its own tooling; at 10–20 units **WRGB cannot amortise any
tooling of its own**, so every WRGB-unique item must be tooling-free or made on
Core tooling.

## 2. What WRGB shares with Core (same suppliers, same RFQs)

Extrusion, anodise, CNC end machining, end caps, gaskets, mounting hardware, cable
assemblies, adapter family (own rating), DC connector, packaging box family (own
sleeve), MCU/radio module and RTC (if the control board is shared), assembly and EOL.
None of these needs a separate sourcing entry; the WRGB pilot simply draws from the
Core housing-kit stock at the decoupling point.

## 3. WRGB-unique categories

| Category | Functional requirement | Make / buy | Intended process | India | Import likely? | Candidate sources | Status | MOQ / cost class (2026-09-11) | Quality-critical characteristics | Evidence and incoming QC | Alternate | Risks | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colour LED emitters (R, G, B, W, optional deep red) | 4 mandatory + 1 optional channel; discrete common-footprint high-power (Cree XE-G, Luxeon Rubix), multi-die RGBW, or dense mid-power arrays: Phase 1 trade study | Buy | Cut tape or single reels via authorised distribution | Mouser/Arrow India cut tape; Nichia India for whites | **Yes** | US / NL / DE / JP; Chinese 3535/5050 RGBW as a cost class with weak bin documentation | candidate; sample required | Cut tape at a per-LED premium for ~200 LEDs per colour; one reel per colour if bin consistency across the pilot matters | **Single flux and wavelength bin per colour per build lot** (green bin spread makes unit-to-unit hue mismatch visible at 10–20 units); 660 nm peak ±5 nm | CoC, reel label, lot, bin, date code; spectroradiometer on 5 LEDs per reel; Δu'v' across pilot units | Footprint-compatible pair (Osram + Lumileds/Bridgelux) | Colour BOM several times the Core white BOM; Cree LED continuity under Penguin Solutions to verify; Lumileds ownership unresolved | Medium |
| WRGB MCPCB | One artwork per length with per-channel strings; possibly higher-k dielectric for the denser board | Buy | Indian fab; JLCPCB fallback | Buljin, AS&R, Ascent, PCB Power | Fallback CN | TN / Gujarat | candidate; RFQ required | **20 boards sit below the Indian ~100 MOQ**: panelise with Core boards, accept MOQ overrun, or order from JLCPCB (ADD scope to check) | Dielectric conductivity for the higher thermal density; white-mask yellowing under blue | Fab CoC; coupon | JLCPCB | MOQ overrun or import paperwork | Medium |
| Multichannel driver / control PCBA | 4–5 CC channels, ≥ 12-bit PWM at ≥ 3 kHz, per-channel current precision ±3 % (ratio precision matters more) | Buy assembly | SMT at Coimbatore EMS on the same line as Core | Enthu, Michael; Syrma SGS fallback | ICs imported | Coimbatore | candidate; qualification required | One or two extra artworks; stencil and setup NRE per artwork | Channel-to-channel current match; thermal; EMC | First-article AOI and functional; EMC pre-scan | Syrma SGS | 20 boards is a hand-built quantity; EMS may price it as NRE-only | Low until visited |
| Optical mixing element | Diffuser, lens array or mixing chamber per the colour-mixing decision; may diverge from the Core cover | Buy | Extruded diffuser profile, lens array (LEDiL/Carclo/Khatod), or machined mixing chamber | Plextrusion (diffuser) | **Yes** for lens arrays | FI / UK / IT / CN | researched; RFQ required | Lens arrays 100s MOQ; diffuser profile die if unique | Colour uniformity Δu'v' across the substrate; transmission; blue-driven yellowing | Hardscape shadow test; coupon under 1.5× blue flux | Diffuser vs lens | A WRGB-unique cover breaks cover sharing (cost test) | Low |
| Adapter, higher rating | Same family, voltage and safety class as Core; higher wattage (plug may change between ratings within a family) | Buy as-is | Mean Well GST90A/120A class or OWA | Mean Well official Indian distributors | Likely | TW via India distribution | candidate; RFQ required | 100–500 MOQ per rating from importers; 20 units may mean buying distributor stock | Same as Core plus derating above 40 °C (GST90A derates above 40 °C) | Certificate check; load test | Second family | **Plug and cable gauge change between 60 W and 90 W in the GST family**; uniform custom plug only at MOQ | Medium |
| Photobiological assessment | IEC 62471 risk group by measurement for the highest-CCT/blue configuration | Buy test | Lab | CPRI Bengaluru (candidate) | No | Karnataka | candidate | One-off test cost | Labelling if RG1 or above | Test report | North-India labs | Unlabelled sale of an RG2 product | Medium |
| Pilot serialisation and field tracking | ≥ 80 % of pilot units traceable to a known installation; ≥ 1000 h and ≥ 3 months on ≥ 10 units before scale | Make (Trophic) | Serial family with variant field; field-return log from day one | Trophic | No | — | — | — | Traceability of LED lot to serial (bin consistency matters here) | Build record | — | Too few units to see failure rates | High |

## 4. WRGB-specific conclusions (proposals)

- **Tooling-free by design.** Every WRGB-unique part (MCPCB artwork, driver PCBA, optical element) must be procurable without a die or mould; where a diffuser profile die is needed, it must be the Core die or the cost test must justify it.
- **Bin discipline is the product.** Buy one reel per colour per pilot lot and record lot-to-serial; do not mix reels across the pilot.
- **Expect MOQ overruns on boards and adapters** at 20 units; treat overruns as pre-paid stock for the post-pilot decision, and record them so the pilot's true cost is known.
- **UVA is excluded** unless evidence appears (reference Parts B3 and D2); no UVA emitter is sourced.

## 5. Risks specific to WRGB

| Risk | Mitigation |
|---|---|
| Hue mismatch across pilot units | One bin per colour per lot; Δu'v' acceptance in EOL |
| Colour LED availability and continuity | Footprint-compatible second manufacturer; verify Cree LED and Lumileds status before design-in |
| Higher adapter rating changes plug and cable | Decide the connector once for the family; custom plug at MOQ or a sealed circular connector |
| WRGB cover diverges from Core | Cost test in `PLATFORM.md` §4 decides; a divergent cover is acceptable if the die is cheap or it is a cut sheet |
| Board MOQ at 20 units | Panelise with Core, or JLCPCB with duty and ADD checked |

## 6. RESEARCH REQUIRED

Cut-tape pricing and lead times for candidate colour parts in India (dated); Cree LED component continuity; Indian availability of lens arrays; JLCPCB ADD scope for MCPCB; GST90A/120A stock at Indian distributors; CPRI test cost and lead time.
