# Sourcing Strategy — `AQ-LT-A` Core Smart Aquascaping Light

**Status:** Phase 0A, research 2026-09-11 · **Owner:** Manufacturing/Sourcing with the main session
**Shared landscape (do not duplicate here):** `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`
**Platform manufacturing model:** `../../PLATFORM.md` §4–5

Vocabulary: **Sourcing** (this strategy), **Procurement** (buying against it),
**Supplier Research** (the landscape), later **Vendor Qualification** (roadmap §8).
Supplier statuses: researched · longlisted · candidate · RFQ required · sample
required · qualification required. Nothing is approved, qualified or on an AVL.

This document records the **Core-specific implication** of each category. Columns
that the roadmap's Gate C requires (incoming QC, certificates, alternates) are
filled where research supports them and left as RESEARCH REQUIRED otherwise. Cost
columns are classes dated 2026-09-11 and are all RFQ required.

---

## 1. Volume and cost context (owner planning assumptions, not COGS)

~200 units first run; two size classes hypothesised; preliminary figures ~₹1,400 /
₹1,600 for the smaller classes; retail ~₹2,500–3,500. Every component below is
evaluated against that envelope. The shared platform pools extrusion, anodise, end
caps, mounting, cable hardware and cartons with the WRGB pilot; it does **not** pool
LEDs, driver ICs, MCPCB artwork or PSU rating.

## 2. Category table

| Category | Functional requirement | Make / buy | Intended process | Coimbatore | TN / India | Import likely? | Candidate region and sources | Status | MOQ / tooling / cost class (2026-09-11) | Quality-critical characteristics | Evidence and incoming QC | Alternate | Risks | Localisation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aluminium extrusion body | Heatsink and chassis for the Core thermal load, with the WRGB envelope only if the cost test passes | Buy | Custom die, 6063-T5/T6, cut to length | **No press verified** (traders only) | Hindalco Alupuram (Kerala), Malabar (Kochi), KMC (Chennai), Bhoruka (Mysuru) | No | Kerala / TN / Karnataka | candidate; RFQ required | Die ₹13.5k–35k class; ₹300–420/kg finished; new-die MOQ 500–1,000 kg vs ~70–120 kg needed for 220 units | Straightness, twist, wall thickness, anodise-grade surface, tongue ratio of any fins | Mill test certificate; FAI on length, straightness, key dimensions; retained reference piece | Second extruder on the same Trophic-owned die | MOQ overrun (5–10× need) becomes stock; single die = single point of failure | Already India | Medium |
| Anodising | Type II, dark grey/graphite, fine bead-blast under (design brief); seal quality near water | Buy | Batch anodise after machining | First Class Metal Finishers, PRM, Alcoat, A.K. Micro Process (all unverified specs) | Extruders' in-house lines (Hindalco, Malabar, Bhoruka) | No | Coimbatore first, extruder second | RFQ required; sample required | ₹80–120/m² decorative, minimums ₹2–5k per job; black dye needs ~12–15 µm | Film thickness, colour repeatability batch to batch, seal quality, no bare cut edges | Thickness measurement per batch; colour reference piece; salt-fog coupon | Extruder's line | Colour mismatch between body and machined caps if not the same bath | Local | Low until samples |
| CNC end machining | Cable-exit hole, mounting bosses, gasket groove, deburr | Buy | VMC job work | Hi-Tech CNC, Sangeetha, Parekh, Pitrukrupa | — | No | Coimbatore | longlisted; RFQ required | ₹40–150 per end at 200–500 pcs | Position of exit and bosses to the cap interface; burr-free | FAI 3–5 parts; fit check to actual cap | Any Coimbatore VMC shop | Low | Local | Medium |
| End caps | Seal, cable exit, mounting interface, service door (brief) | Buy | **CNC 6061/6063 (no tooling) or moulded PC/ABS with deliberate tonal step** | RTI, Tooling Temple (moulding); VMC shops (machined) | — | No | Coimbatore | candidate; RFQ required both routes | Machined: no MOQ; moulded: simple mould ₹2–8 lakh, amortised over 440 caps dominates cost | Seal face, finish match (machined) or deliberate contrast (moulded), fastener bosses | FAI 5–10 pcs; fit to actual extrusion; anodise batch matched to body | The other route | Die-cast rejected (anodises poorly) | Local | Medium |
| Gasket / seal | Cap-to-body and cover seal; compression set at heat | Buy | Die-cut EPDM locally; moulded silicone elsewhere | Varrmas (EPDM die-cut) | Chennai/Bengaluru moulders for silicone: RESEARCH REQUIRED | No | TN | longlisted | Low | Compression set (ISO 815 test), material temperature class | Material datasheet; compression-set coupon | Silicone if EPDM fails heat | Moulded silicone not evidenced in Coimbatore | Local | Low |
| Optical cover | Diffusion or clear per optics decision; PMMA preferred for UV stability, PC for impact | Buy | Extruded profile (custom die) or cut sheet | Sheet stockists only | Plextrusion (Mumbai) profiles; Akmy/Hexatron sheet | Possibly for optical-grade profile | Mumbai / Gujarat | candidate; RFQ required | Profile die + MOQ; sheet no MOQ | Transmission, haze, yellowing under blue and heat | Transmission and haze on a sample rig; 1000 h coupon | Glass (heavy, sealing challenge) | Custom profile MOQ at 220 units | Partial | Low |
| LED emitters | Fixed engine: high-CRI white and/or white + 660 nm red, one binned reel per type | Buy | Reels via authorised distribution | No | Nichia India (Bengaluru), Bridgelux via AqTronics/Kevin, Mouser/Arrow/Avnet India | **Yes, all emitters** | JP / US-Asia / DE / KR; Chinese Sanan/Hongli direct as a cost class | candidate; sample required | Reels 2–5k per type; one reel per type covers 200 units; Japanese/Korean high-CRI 2–4× Chinese 2835 | Flux and chromaticity bin (3-step MacAdam is an assumption), 660 nm peak ±5 nm, Vf bin | LM-80 at the actual current; CoC; reel label photo, lot, bin, date code; 5-LED spectroradiometer spot check per reel | Footprint-compatible second manufacturer | **Samsung exited**; counterfeit reels on grey channels; Lumileds ownership unresolved | None | Medium |
| MCPCB (LED board) | Single artwork per length; 1–2 W/m·K adequate for mid-power whites at ≤ 100 mA; higher for a high-current red string | Buy | Fab in India; populate in Coimbatore | No fab | Buljin (Chennai), AS&R (Gandhinagar), Ascent (Hosur), PCB Power | JLCPCB as prototype fallback (ADD may apply) | TN / Gujarat | candidate; RFQ required | MOQ ~100 per artwork; ₹200/pc listing class at MOQ 100 | Dielectric conductivity and thickness, white-mask reflectance and yellowing, solderability | Fab coupon or CoC for dielectric; solderability sample | Second Indian fab + JLCPCB | Artwork count sets NRE (one per length) | Already India | Medium |
| Control / driver PCBA (FR-4) | MCU + radio, RTC with backup, input protection, one CC channel; conformal coated | Buy assembly | SMT at Coimbatore EMS | Enthu, Michael (both qualification required) | Syrma SGS (Chennai) as fallback | ICs and modules imported | Coimbatore | candidate; qualification required | Stencil ₹3–8k, setup ₹5–15k per artwork | MSL handling, reflow profile on the actual board, AOI, IPC-A-610 class agreed | Site visit; first-article 10–20 boards with AOI and functional report | Syrma SGS | Coimbatore EMS claims unverified (Michael's facility claims implausible until visited) | Local assembly | Low until visited |
| MCU / radio module | ESP32-C3 class (BLE now, Wi-Fi optional) or nRF52 (BLE only) | Buy | Module on the control board | No | Rabyte, Campus Component, Millennium, Mouser, DigiKey | **Yes** | CN / NO | candidate | Modules from 1 pc; reels 1–2.5k | Regional radio approval of the module; WPC ETA route | Module datasheet and approval certificates | The other MCU class | Single-source Espressif; WPC ETA process unclear | None | Medium |
| RTC and backup | Days-to-weeks hold-up through Indian outages | Buy | RV-3028-class RTC + supercap or coin cell | No | Distributors | **Yes** | CH | researched | Cut tape | Drift, backup hold-up | Bench drift test 30 days | Coin cell variant | Transport rules if a cell is used | None | Medium |
| Driver ICs, protection parts | Buck CC stage sized to the bus decision; ideal-diode, TVS, eFuse | Buy | Standard parts | No | Arrow/Avnet/Mouser | **Yes** | US / DE | researched | Cut tape | Current accuracy, PWM capability, thermal | Datasheet; bench efficiency | Second IC vendor | None specific | None | Medium |
| External DC adapter | Certified, BIS-registered, sober matte finish, family shared with WRGB at a Core rating | Buy as-is (Gen-1 leaning); private-label later | Mean Well GST class or equivalent | Dealers only | Mean Well official Indian distributors (Nippon India BBY, Sterling Sign, Digital Promoters, Network Inc.); NCR OEMs for private label; Salcomp at scale | Likely (Taiwan-made, India-distributed) | TW via India distribution | candidate; RFQ required | Low tens of US$ at distribution; 100–500 MOQ per rating from importers | IEC 62368-1 report, BIS number verified on the portal, output regulation and ripple, plug polarity | Certificate check; 2 % load test at incoming | Second certified family | **BIS category scope unsettled**; plug changes across ratings; wrong-rail mis-plug | Private-label with an Indian OEM later | Medium |
| DC connector | Keyed to the shared bus voltage; salt-creep tolerant; ingress-appropriate | Buy | Barrel (24 V-rated jacks) or sealed circular (SP13/M8 class) | No | Mouser/DigiKey India for branded; no Indian IP68 maker found | **Yes** for IP-rated branded | TW / DE / CN | researched; RFQ required | 10s–100s | Voltage rating (most barrels 24 V), current, IP when mated, plating | Datasheet; mating cycles then ingress re-test | Second brand | Marketplace clones | None | Low |
| Cable assemblies | Adapter-to-fixture lead if Trophic supplies it; braided dark jacket per brief | Buy | Local harness shop | Chiranjivee, Eagle, Orange, Unotronix | PSM Tech | Braided jacket stock may be imported | Coimbatore | longlisted; RFQ required | Low volumes accepted | Strain relief, flex life, jacket finish | Flex test 5000 cycles | Any local harness shop | Overmoulded IP65 ends not evidenced locally | Local | Medium |
| Mounting legs / hardware | Thin-but-stiff shaped section, dark-finish stainless fasteners, glass pads | Buy | Machined or sheet aluminium + stock fasteners | VMC shops; Precicut (sheet); fastener stockists | — | No | Coimbatore | longlisted | Low | Stability (3× mass static), no glass marking, galvanic pairing | Load and cycle test | — | Fastener corrosion class near water | Local | Medium |
| Packaging | Kraft-tone corrugated, die-cut pulp or board cavities, one-colour print, sleeve per product | Buy | Local | MNR (printed corrugated), Shree Bharath / Kamatchi (EPE), Innovative Pulp (directory only) | — | No | Coimbatore | longlisted | Offset print MOQ 500–1,000 sleeves; digital for small runs | Drop test 0.8–1 m packaged | Packaged drop test | — | Low | Local | Medium |
| Assembly, EOL test | Housing kit + electronics kit + adapter + label; EOL per roadmap §9 | Make (Trophic, Coimbatore) | Bench assembly with jigs; golden-unit PAR spot jig | Trophic | — | Test instruments imported | — | — | Jig NRE small | Serial linking housing lot to electronics lot | EOL record per serial | — | — | Local | High |

## 3. Core-specific make/buy conclusions (proposals)

- **Buy everything, assemble in-house.** No component justifies in-house fabrication at 200 units; Trophic's value-add is design, assembly, test and the shared platform.
- **Do not buy the adapter's certification burden.** A certified, BIS-registered adapter bought as-is is the Gen-1 leaning; the fixture must still fail safe with a wrong or undersized adapter in hardware.
- **Emitters are the one category where the cheapest source is the wrong answer**: binned reels from authorised distribution or a direct factory relationship with certificate of conformance; never grey-market reels.
- **Serviceability vs sealed** is undecided and is a Core-specific economics question (`PLATFORM.md` §9): connectorising costs ~₹20–60 per unit; a sealed Core with a returns policy may be cheaper at this price.

## 4. What must exist before Phase 2 RFQs

RFQ packages A–D and the cover, PSU and connector samples listed in `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md` §3, all gated by the size-class, mounting, ingress and bus-voltage decisions.

## 5. Supply-chain risks specific to Core

| Risk | Mitigation |
|---|---|
| Extrusion MOQ 5–10× requirement | Pool with WRGB; treat overrun as stable stock; negotiate metre-based MOQ |
| Coimbatore EMS unverified | Site visits and first articles before pilot; Syrma SGS fallback |
| Emitter continuity (Samsung gone, Lumileds unsettled) | Footprint-compatible second manufacturer designed in |
| BIS scope for adapter and fixture | Confirm with BIS or a consultant before the adapter RFQ |
| Counterfeit LEDs | Authorised channels only; reel-label and spot-check discipline |
| Anodise colour mismatch body vs cap | Same bath and batch for machined caps; deliberate tonal step for polymer caps |

## 6. RESEARCH REQUIRED

Indian pricing of high-CRI whites and 660 nm reds per reel (dated); anodising specs and batch sizes at the Coimbatore shops; Coimbatore EMS site visits; WPC ETA route for a module-based product; BIS category for the fixture; overmoulded cable ends and silicone gaskets in Chennai/Bengaluru; duty confirmation for HS 8541, 8534, 8504, 8536; retail sell-through by tank length (for the size decision).
