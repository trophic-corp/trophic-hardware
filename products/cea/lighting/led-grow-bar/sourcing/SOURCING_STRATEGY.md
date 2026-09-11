# Sourcing Strategy — `LT-A` LED Grow Bar

**Status:** Phase 0A, research 2026-09-11 · **Owner:** Manufacturing/Sourcing with the main session
**Shared landscape (do not duplicate here):** `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`
**Hardware research:** `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` Part B1

Supplier statuses: researched · longlisted · candidate · RFQ required · sample
required · qualification required. Nothing is approved, qualified or on an AVL.
Every cost figure is a class dated 2026-09-11 and RFQ required.

---

## 1. Volume and context

Eight bars per rack; the Ooty reference room holds 11 racks (88 bars); first runs are
tens to low hundreds of bars. The bar is a **passive LED assembly** under the rack's
remote-driver architecture: LEDs on a board, in an extrusion, behind an optic, with
an IP65 keyed connector. The driver, the mains, the EMC and most of the certification
burden sit in the rack end enclosure, not in this product. That makes the bar's
sourcing simpler than the aquarium lights': no MCU, no radio, no adapter.

**Inherited facts that shape sourcing:** 40 × 60 mm envelope; bed 1176 × 569 mm;
0–10 V per tier; supply either CV 48 V or CC ≤ 60 V (decision 1); no LED derating at
≤ 3 K air rise; fixture above a flood tray in a humid room.

## 2. Category table

| Category | Functional requirement | Make / buy | Intended process | Coimbatore | TN / India | Import likely? | Candidate sources | Status | MOQ / tooling / cost class (2026-09-11) | Quality-critical characteristics | Evidence and incoming QC | Alternate | Risks | Localisation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Extrusion (bar body, heatsink) | Fits 40 × 60 mm; carries 15–30 W heat passively (illustrative); optic mount; saddle interface to `RK-A-301` | Buy | Custom die 6063; cut to bar length (decision 7) | **No press verified** | Hindalco Alupuram, Malabar, KMC, Bhoruka | No | Kerala / TN / Karnataka | candidate; RFQ required | Die ₹13.5k–35k class; ₹300–420/kg; new-die MOQ 500–1,000 kg (~1.1 m × 88 bars is well under that) | Fin area vs envelope, straightness over 1.1 m, anodise-grade surface | Mill cert; FAI; straightness gauge | Second extruder on the same die | MOQ overrun; fins compete with optics for the 40 mm height | India | Medium |
| Finish | Corrosion resistance to fertiliser mist and condensation; reflectance is not required on the body | Buy | Clear or dark Type II anodise, or powder coat | Coimbatore anodisers (unverified specs); Precicut (powder) | Extruders' lines | No | Coimbatore | RFQ required; sample required | ₹80–120/m² anodise; minimums ₹2–5k | Film thickness, seal quality; fertiliser-mist coupon | Thickness per batch; 500 h coupon | Powder coat | Corrosion at cut edges | Local | Low until samples |
| Optic | Delivers CV ≤ 15 % from rows ~180 mm inboard at 150 mm: asymmetric/batwing lens, bent specular reflector, or edge baffles | Buy | Extruded lens (Ledil/Khatod/Chinese extruders) or bent Alanod-type reflector (locally fabricable) | Reflector: Precicut and sheet shops; lens: no optical-grade extrusion evidenced | Plextrusion (diffuser only) | Lenses **yes** | FI / IT / CN for lenses; Coimbatore for reflectors | researched; RFQ required | Lens tooling if custom; reflector tooling low | Beam shape, transmission, yellowing; edge fall-off | Quantum-sensor jig grid ≥ 7 × 4 plus border; ray-trace before tooling | Reflector if lenses fail cost | CV ≤ 15 % may need tray-side baffles, a rack-side conversation | Reflectors local | Low |
| LED emitters | Fixed spectrum: horti white 3030 mid-power (Bridgelux, Nichia, Lumileds, Osram, Seoul) ± 660 nm red (Osram Oslon Square, Lumileds deep red) | Buy | Binned reels via authorised distribution | No | Nichia India; Bridgelux via AqTronics/Kevin; Arrow/Avnet/Mouser | **Yes** | US-Asia / JP / DE / NL | candidate; sample required | Reels ~2–4k (3030); 12–20 weeks for specific bins; 88 bars × tens of LEDs is a few reels | PPF/flux bin, Vf bin (parallel strings), chromaticity; 660 nm peak bin | LM-80 at the actual current and Tcase; CoC; reel label, lot, bin; 5-LED spot check per reel | Footprint-compatible pair (Osram + Lumileds/Bridgelux) | **Samsung LM301-family gone**; Lumileds ownership unresolved; counterfeit reels | None | Medium |
| LED board | 2–3 segments of ~360–560 mm; FR-4 2 oz with thermal vias likely adequate for 3030 whites ≤ 100 mA; MCPCB for a high-current red string; ENIG if re-population is intended; LED-grade white mask | Buy | Indian fab; JLCPCB prototype fallback | No fab | Buljin, AS&R, Ascent, PCB Power | Fallback CN | TN / Gujarat | candidate; RFQ required | MOQ ~100 per artwork; panel length limits RESEARCH REQUIRED | Dielectric conductivity (if MCPCB), mask reflectance and yellowing, board-to-board joint | Fab CoC; solderability; segment fit in the extrusion | Second fab | Panel-length limits force segmenting anyway | India | Medium |
| Board population | Reflow of mid-power whites and ceramic reds; MSL discipline; nitrogen optional | Buy assembly | Coimbatore EMS (Enthu claims aluminium boards to 450 × 450 mm) | Enthu, Michael (qualification required) | Syrma SGS | No | Coimbatore | candidate; qualification required | Stencil and setup NRE per artwork | Reflow profile on the actual board; ESD handling of InGaN dies; AOI | Site visit; first article with AOI and Vf/current per string | Syrma SGS | Segment length vs EMS board size limit | Local | Low until visited |
| Connector | IP65 keyed, one CC pair (M12 A-coded 4-pin class) or higher current if CV bus; ≤ 60 V rating with margin | Buy | Panel-mount at the bar end | No | Mouser/DigiKey India (Amphenol LTW, Binder, Phoenix, TE) | **Yes** | TW / DE | researched; RFQ required | 10s–100s | Voltage rating vs driver open-circuit voltage; IP when mated; keying | Datasheet; mating cycles then ingress re-test | Second brand | The rack's connector type is itself unrecorded (`IF-RK-A-ELE` §4) | None | Low |
| Remote driver (rack-side, decision 1) | 0–10 V CC, 48 V-class output, **open-circuit voltage ≤ 60 V**, IS 15885 mark, dim-to-off or relay per the photoperiod decision | Buy | Mean Well XLG-H-AB / HLG-48B / ELG-48B class; Inventronics EUM/EUG | Dealers | Mean Well official Indian distributors; Inventronics India | Likely (Taiwan-made, India-distributed) | TW via India | candidate; RFQ required | 50–100 per model typical; Indian stock reduces lead time | OCV class, dim-to-off behaviour, open/short dim-wire fail state, IS 15885 registration | Datasheet; bench dim curve; BIS number verified | Inventronics | This is the rack's open decision, not the bar's; recorded here because the bar's connector rating depends on it | Not applicable | Medium |
| Cable, bar to driver | ~2–3 m, 1.0 mm² class, drip loop, P-clips in the rail | Buy | Local harness shop | Chiranjivee, Eagle, Orange, Unotronix | — | No | Coimbatore | longlisted | Low | Insulation rating, flex at the service loop | Flex test | Any harness shop | IS 694 cable makers not researched | Local | Medium |
| Saddles, brackets | Interface to `RK-A-301` per EDR-020; steel per platform mechanical standards | Buy | Laser-cut and formed, powder coat or zinc | Precicut and peers | — | No | Coimbatore | longlisted | Low | Fit to the 20 mm rail; envelope check | FAI against `RK-A-301` | — | — | Local | High |
| Gaskets, seals | IP at the bar (decision 6) | Buy | Die-cut EPDM or moulded silicone | Varrmas | Chennai/Bengaluru moulders | No | TN | longlisted | Low | Compression set at heat | ISO 815 coupon | — | — | Local | Low |
| Test equipment | Quantum sensor and grid jig (required by the rack's verification method); spectroradiometer per design and per lot | Buy | — | No | ITC India, KC India (LM-79 labs, north India); CPRI (62471) | Instruments **yes** | US / DE / CN | researched | Instrument cost class tens of thousands of ₹ for a quantum sensor; spectroradiometer rented or lab | Calibration traceability | Calibration certificate | Lab hire | No NABL LM-79 lab verified in south India | None | Medium |

## 3. `LT-A`-specific conclusions (proposals)

- **The bar is passive; keep it that way.** Reading (b) of decision 1 (CV bus with an on-bar CC stage) would import a switching stage, EMI and control-gear classification into the bar and change this whole table. Sourcing assumes reading (a) until decided.
- **Driver selection is a sourcing decision with a safety criterion**: open-circuit voltage ≤ 60 V at the canopy connector. It belongs to the rack's decision 1 but the bar's connector rating follows it.
- **Reflectors before lenses.** Bent specular reflectors are locally fabricable inside the 40 mm envelope; custom lenses are imported and tooled. Ray-trace both before tooling either.
- **Share with the aquarium platform only what is free to share**: LED supplier relationships and binning rules, MCPCB fab and EMS, the quantum-sensor jig and spectroradiometer, dimming maths. Not the extrusion, connector, PSU or form factor.
- **Do not design in Samsung horticultural parts.**

## 4. What must exist before Phase 2 RFQs

Decision 1 (driver and supply reading); decision 7 (bar length); decision 4 (optic class) at least to the level of "reflector or lens"; a section concept with fin area inside 40 × 60 mm; then RFQ packages for extrusion, LED board (two Indian fabs plus JLCPCB), PCBA (two Coimbatore EMS plus Syrma SGS), reflector or lens, and the driver.

## 5. Risks specific to `LT-A`

| Risk | Mitigation |
|---|---|
| Driver OCV above 60 V at the canopy connector | Selection criterion; measure at the connector |
| CV ≤ 15 % unachievable from the fixture alone | Edge reflectors or tray-side baffles agreed with the rack owner; jig map early |
| Tier air rise > 3 K with four stacked tiers at low fan speed | Stack test on a real rack before the extrusion die |
| Board segment length vs EMS and fab limits | Confirm panel and line limits before artwork |
| No south-India NABL photometric lab | Own jig for PPFD; rent or ship for LM-79 and 62471 |

## 6. RESEARCH REQUIRED

Indian fab panel-length limits for MCPCB and FR-4; Coimbatore EMS board-size and MSL handling; Mean Well XLG/HLG stock and BIS status at Indian distributors; connector type at the rack inlet (unrecorded); reflector material (Alanod-class) availability in India; IS 694 cable makers; whether a DC-only ELV bar is a CRS luminaire.
