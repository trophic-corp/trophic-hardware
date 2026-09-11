# CURRENT_STATE — trophic-hardware

**As of:** 2026-09-11
**Repository state:** rack design reviewed and revised (ECP-01, Rev 6); `RK-A R2` export pending; lighting program Phase 0A research complete, ADR-008 (modular control) proposed, common lighting area and planning cost model created.

---

## 1. Where the engineering actually stands

One product line is engineered: the **CEA Rack Platform (Rack A)**. On 2026-09-10 an independent engineering review found the v8 design not ready for prototype (depth-plane stability unverified and joint-dependent; three unfittable parts; two safety invariants not met in CAD; tray STEP not tooling geometry). The owner's decisions were applied the same day as controlled change **ECP-01**: the design of record is now **`CEA_RACK_INTEGRATED_v3` v1 (Rev 6)**, re-validated in RK-A-QC Rev 4. `RK-A R1` is constrained; `RK-A R2` is to be exported from v3 v1.

Two adjacent scopes were separated out of the rack during migration and are
correctly owned elsewhere:

- **Closed-loop water recovery** — shared CEA infrastructure serving a whole
  room, not a rack subassembly.
- **Ooty 20 × 12 ft room** — a reference implementation of a facility built
  from racks, not a product.

Twelve further products now have **Phase 0 documents** — four CEA and eight
aquarium. None has engineering. On 2026-09-11 the three lighting products (`LT-A`,
`AQ-LT-A`, `AQ-LT-B`) completed **Phase 0A research**: shared reference material in
`docs/references/lighting/` and `docs/references/suppliers/`, a platform strategy
(`products/aquarium/lighting/PLATFORM.md`, ADR-007), product sourcing strategies, and
a roadmap with phase-gate evidence (`docs/engineering/LIGHTING_PROGRAM_ROADMAP.md`).
No CAD was touched; the 0B architecture decisions (bus voltage, PSU family, chassis
sharing, size classes, WRGB channel count, `LT-A` driver model) are open. Each document separates what is inherited and
decided from what is open, and does not fill the gaps; the CEA ones carry real
inherited interface facts because the rack fixed them, and the aquarium ones are
mostly open questions, which is correct.

Shared standards extracted from the rack's decisions now live in `platform/`.

---

## 2. Product index

| Product / scope | ID | Owner class | Location | Stage |
|---|---|---|---|---|
| CEA Rack Platform (Rack A) | `RK-A` | A — Rack product | `products/cea/racks/rack-platform/` | **Rev 6 (ECP-01) — re-validated, R2 export pending** |
| Closed-loop water recovery | `RK-A-WRS` | B — Shared CEA infra | `products/cea/irrigation/water-recovery/` | Design validated |
| Ooty 20 × 12 ft CEA room | `RK-A-ROOM` | C — Facility reference | `products/cea/facility-reference/ooty-room-20x12/` | Layout validated |
| LED grow bar | `LT-A` | A | `products/cea/lighting/led-grow-bar/` | **Phase 0A research complete (2026-09-11), 0B pending** |
| Ducted ventilation plenum | `EV-A` | A | `products/cea/environmental-control/ventilation-plenum/` | **Phase 0** |
| Rack controller | `CT-A` | A | `products/cea/sensors-controllers/rack-controller/` | **Phase 0** |
| Room controller | `CT-B` | B | `products/cea/sensors-controllers/room-controller/` | **Phase 0** |
| Aquarium lighting, Core + WRGB | `AQ-LT-A`, `AQ-LT-B` | A | `products/aquarium/lighting/` | **Phase 0A research complete (2026-09-11), 0B pending** — shared platform, ADR-007 |
| Aquarium range, 6 further products | `AQ-*` | A | `products/aquarium/` | **Phase 0** |

Owner classes are defined in `products/cea/racks/rack-platform/PRODUCT.md` §2.
Full map with cross-product open decisions: `products/PRODUCT_INDEX.md`.

---

## 3. Headline engineering figures

These are the current, post-correction values. They supersede any earlier
figure found in `archive/`.

| Quantity | Value | Source |
|---|---|---|
| Installed envelope (W × D × H) | 1456 × 690 × 1960 mm | unchanged by ECP-01 |
| Structure-only envelope | 1256 × 569 × 1960 mm (brace bars to Y 569; gusset plates −3 mm at the front) | v3 v1 |
| Phase-1 build envelope | 1456 × 690 × 1960 mm (648 withdrawn) | RK-A-MFG Rev 3 |
| Dry mass | **136.39 kg** model (all systems); Core 91.7 · Grow Phase 1 108.0 · Grow complete 126.9 | Fusion `CEA_RACK_INTEGRATED_v3` v1 |
| Parts / occurrences | 70 / 417 | Fusion v3 v1 |
| Structural clashes | **0** (204 designed-connection contacts, whitelist in RK-A-QC Rev 4) | Fusion v3 v1 |
| Frame sway, 300 N at top bed with P-Δ | 5.4 mm (T16 ≤ 10) | RK-A-QC Rev 4 VR-07 |
| Tiers × bed heights | 4 × 300 / 700 / 1100 / 1500 mm | EDR-001 |
| Rack cost, Grow Phase 1 | ≈ ₹54,300 estimate before valve re-quote (was ₹49,296) | RK-A-MFG Rev 3 |
| Room total, 11 racks | ₹13.2 lakh (ex-LED fixtures) | RK-A-ROOM Rev 4 |
| Water recovery ratio | 87.7 % | RK-A-WRS Rev 3 |
| Annual discharge saved vs drain-to-waste | 554 m³ | RK-A-WRS Rev 3 |

---

## 4. Releases

**`RK-A R1`** (v8, Rev 5) — issued 2026-09-05, verified 2026-09-09, now **constrained**: not to be used for gusset plates, brace bars, anchor struts, drainage or tray tooling. **`RK-A R2`** from `CEA_RACK_INTEGRATED_v3` v1 is the next release (RELEASE_INDEX §3).

## 5. Open items, repository-wide

| ID | Type | Item |
|---|---|---|
| ~~NT-01~~ | **CLOSED 2026-09-09** | Parameter master persisted as `RK-A-PARAM` Rev 1 — 55 parameters read directly from `CEA_RACK_INTEGRATED_v2` v8 |
| ~~NT-02~~ | **CLOSED 2026-09-10** | Depth-plane frame checked by analysis (VR-07, RK-A-QC Rev 4) after ECP-01; T16 confirmatory |
| NT-03 | NEEDS TRACEABILITY | `RK-A-107B` joint stiffness calculated, not measured — T19 coupon before T16 |
| ND-01 | NEEDS DECISION | `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` holds Rev 2 content while the published artifact of the same ID holds Rev 1. Which is the intended part-drawing release must be decided before drawings are reissued |
| ND-02 | NEEDS DECISION | Two published "Rack A Manufacturing Pack" artifacts exist. `9f5e09e5` is Rev 2 and current; `817abd35` is an orphan and should be retired or deliberately kept |
| ND-03 | NEEDS DECISION | Ventilation plenum is deferred to a Phase-2 entity. Phase 1 ships standalone EC fans. The plenum's interface to the rack is not yet frozen |
| ND-05 | NEEDS DECISION | Canopy velocity CV action threshold — RK-A-SYS §01 says 15 %, RK-A-ROOM §04 says 20 %. Plausibly a two-step escalation ladder; not reconciled |
| ND-06 | NEEDS DECISION | Room electrical phase imbalance ~20 % against a 15 % target; resolved on paper by specifying 3-phase HVAC, recorded as an open finding |
| ND-08 | NEEDS DECISION | `RK-A-ROOM` Rev 5: floor/anchor loads at 136.4 kg, strut anchoring detail; no set-out change |
| ND-09 | NEEDS DECISION | Valve technology trial scope (EDR-016 alternatives) |
| ND-10 | NEEDS DECISION | Tray floor: flat + tolerance, or formed drainage channels — before tooling |
| ND-11 | NEEDS DECISION | **PPFD ceiling rationale.** RK-A-SYS §00 and the CEA suite `safety-rules.json` state that PPFD above 210 µmol/m²/s risks photoinhibition. The 2026-09-11 microgreen literature review (`docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` D1) found no evidence of photoinhibition at ≤ 210; Brassica microgreens were grown to 315–600 without damage. The 210 ceiling is defensible as an energy, thermal and uniformity optimum, not as a biological limit. **Nothing has been changed**; the operating band stands. Decide whether the safety-rule rationale is restated (and whether `trophic-contracts` and the suite need the change) |
| ND-12 | NEEDS DECISION | **LED supply reading and driver open-circuit voltage.** RK-A-SYS §07 permits either a constant-voltage 48 V DC supply or a constant-current supply with output ≤ 60 V; `LT-A`'s Phase 0 document had simplified this to "48 V DC". Under the CC reading a remote driver's open-circuit voltage appears at the IP65 canopy connector when a bar is unplugged (Mean Well XLG-L 225 V, -M 115 V, -H 60 V). Only ≤ 60 V OCV drivers keep the ELV boundary. This becomes a selection criterion inside the open "driver model" decision (`IF-RK-A-ELE` §4); recorded so it is not lost |
| ND-07 | **UNKNOWN — low priority** | Terrace slab loading 5.5 kN/m² concentrated against a typical 1.5–2.0 kN/m² rating. **Owner decision 2026-09-09: not a blocker** — the tank will be mounted on a steel structure rather than bearing directly on the slab. Kept open as unknown: the steel structure's own design and its bearing points are not yet specified |

ND-05 to ND-07 were raised by the CEA suite audit; ND-11 and ND-12 by the lighting Phase 0A research. Full detail is in
`products/cea/racks/rack-platform/CURRENT_STATE.md`,
`docs/system/MIGRATION_REPORT.md` and `docs/system/CEA_SUITE_AUDIT.md`.

---

## 6. Recommended next engineering action

**Export `RK-A R2` from `CEA_RACK_INTEGRATED_v3` v1, regenerate the drawing sheets, decide ND-10, then build the prototype and run T19 → T1–T20.** The depth-plane question is closed on paper (5.4 mm at 300 N); T16 confirms it with the measured joint stiffness from T19.
