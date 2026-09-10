# CURRENT_STATE — CEA Rack Platform (Rack A)

**As of:** 2026-09-10
**Design stage:** **Rev 6 (ECP-01) — reviewed, revised, re-validated; pre-prototype**
**Release stage:** `RK-A R1` issued but **constrained** (§4); `RK-A R2` export pending

---

## 0. What happened on 2026-09-10

An independent read-only engineering review (`verification/RK-A-REV_RevA_independent-engineering-review.md`) classified the v8 design as **requires engineering revision before prototype** — 35 findings, one Critical (depth-plane stability), eight High. The owner took four decisions the same day and a controlled change package (`changes/RK-A-ECP-01_RevA_engineering-change-package.md`) was applied:

- Fusion: ECP-01 rebuilt on the v8 baseline and saved as the new lineage **`CEA_RACK_INTEGRATED_v3` v1 (Rev 6)** — 70 parts, 417 occurrences, 136.39 kg, envelope unchanged 1456 × 690 × 1960, zero structural clashes (204 designed-connection contacts, whitelist recorded). `CEA_RACK_INTEGRATED_v2` v9 is a defective intermediate and must not be used (CAD_INDEX).
- Documents: RK-A-PARAM Rev 2, RK-A-DWG Rev 3 (tabular), RK-A-MFG Rev 3, RK-A-QC Rev 4, RK-A-SYS addendum B, interface specs Rev 2, EDR-014…020, ICR-005…007.

## 1. Where the design stands

The integrated rack model is complete and internally consistent at **`CEA_RACK_INTEGRATED_v3` v1**. Every tier is now a closed rectangle (per-tier cross beams), every beam end is a modelled gusset-plate joint on rivet nuts with crush tubes, the rear brace is two grid-compatible bars, the anchor is an adjustable strut, the fill nozzle clears the rim by 38 mm, the tray carries its formed features, and the drain header sits behind the rear-right upright with its laterals in verified crossing windows. The model reports **70 parts, 417 occurrences, 0 structural clashes, 136.39 kg dry (all systems)**.

The document set (brief, systems specification, structural drawings,
manufacturing pack, validation record) has been cross-referenced and swept for
stale figures. The rack has been set out into an 11-rack room layout and the
room-level water balance closes.

The release **`RK-A R1`** is issued and verified: 45 of 45 part STEP files plus
assembly STEP and F3D, hashed and reconciled against the live model.

---

## 2. Validated this design cycle

| Item | Result |
|---|---|
| Mass model | Corrected twice — 1246 kg (solid placeholders) → 147.67 kg (shelled, real materials) → **112.66 kg** (deck mesh density corrected) |
| Interference | All clashes resolved; 0 unresolved in v8 |
| Drain continuity | Proven joint-by-joint from every tray outlet through the tray strainer, bulkhead, overflow drop and branch to the rack drain header outlet |
| Gravity supply | 2.66 m static head vs 0.33 m loss at 7.2 L/min. Passes ~8×. Four tiers concurrent still passes |
| Suction-lift architecture | Terrace supply pump deleted; recovery pump relocated to the low point |
| Tier count | Four confirmed as the reach-limited maximum (NIOSH RWL = 0 above 1750 mm) |
| Structural drawings | Rev 3 tabular part definitions for 12 changed/new parts; sheets to be regenerated |
| Manufacturing pack | Rev 3 — part schedule, fasteners, assembly, QC, cost delta |
| Depth-plane frame | **VR-07 performed**: 5.4 mm sway at 300 N with P-Δ at k = 8 kN·m/rad; T16 confirmatory after T19 |
| Seismic | VR-11 recorded: SF 3.1 unanchored |
| Room integration | 11 racks set out to coordinates; 29.0 m² grow area, 1.30× floor multiplier |

Full evidence, assumptions and limitations are in
`verification/RK-A-QC_Rev3_engineering-validation-record.html` and indexed in
`docs/quality/VERIFICATION_INDEX.md`.

---

## 3. Errors caught and corrected (kept because they are load-bearing)

| # | Error | Correction |
|---|---|---|
| 1 | Deck mesh given a 35 %-open perforated-sheet density | Corrected to 1884 kg/m³ for ≥70 % open expanded mesh — 1.98 kg/panel. **The drawing was right and the model was wrong**; recorded as EDR-004, the one exception to "the model governs" |
| 2 | `RK-A-104` rear brace dimensioned 1345 mm against a true diagonal of 1797 mm | Corrected to 1797 mm, hole centres at 20 / 1777. Rev 1 would have produced a part 452 mm short |
| 3 | Overflow line had a 90 mm break between the moulded collar (Z 300–330) and the vertical drop (Z 160–210); tray penetrations were never modelled | `09_OVF_V` extended to Z 160–300; `09_TRAY_OUTLET`, `09_TRAY_STRAINER` and `09_OVF_BULKHEAD` added. Caught by the user, not by the model |
| 4 | Terrace-mounted supply pump lifting from the room | Physically impossible at 2,240 m. Architecture changed to gravity feed with the recovery pump at the low point (EDR-005) |
| 5 | Room Rev 3 rewrite silently dropped the Building section | Restored as §08 in Rev 4 with recomputed loads |
| 6 | Rear brace "corrected" to 1797 mm from the bounding-box diagonal; modelled bar 1771.6 mm with no holes | 1810 mm bars, holes 1780.1 on grid rows 150/1450 (EDR-018) |
| 7 | Beam-end bracket never modelled; documented geometry unbuildable; 18 N·m through 1.6 mm walls | `RK-A-107B` gusset plates on rivet nuts with crush tubes (EDR-015) |
| 8 | Fill nozzle outlet 2 mm below the tray rim — no air gap in the fault case | Outlet raised to 38 mm above the rim (ICR-005) |
| 9 | 60 mm wall anchor against a 127 / 254 mm stand-off | Telescoping strut 90–320 mm (EDR-017) |
| 10 | Drain valves specified without a minimum operating differential on 0.002 bar of head | Motorised spring-return-open drain valves; zero-ΔP fill solenoids (EDR-016) |
| 11 | Tray STEP carried none of the formed features the drawing promised | Formed tray modelled; R1 tray STEP not-for-tooling (EDR-019) |
| 12 | `CEA_RACK_INTEGRATED_v2` v9 saved with collateral cuts from unrestricted participant bodies | Rebuilt on v8 with participants restricted → `_v3` v1; v9 quarantined |

---

## 4. Release — `RK-A R1`, ISSUED

| | |
|---|---|
| Source | Fusion `CEA_RACK_INTEGRATED_v2` **v8** (Rev 5) |
| Exported | 2026-09-05 10:21 · **verified 2026-09-09** |
| Store | `E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\INTEGRATED_v2_Rev5\` |
| Manifest | `release/RK-A-R1_MANIFEST.md` — per-file SHA-256 |

**RB-01 closed.** The export was never missing — it was written to Google Drive, not
to the Desktop path `RK-A-MFG` §15 and `RK-A-DWG` cite. Those two references are
errata; no engineering value is affected.

The release content independently confirms two of the corrections in §3:
`04_DECK_PANEL` at 1.981 kg each (EDR-004), and the presence of `09_TRAY_OUTLET`,
`09_TRAY_STRAINER` and `09_OVF_BULKHEAD` with `09_OVF_V` at nearly double its
pre-correction size (ICR-001).

**Constraints on use (revised 2026-09-10):** `RK-A R1` is superseded for the frame joints, brace, anchor, drainage and tray: **do not fabricate gusset plates, brace bars, anchor struts, drainage or tray tooling from R1.** Uprights, long beams, deck rails and mesh panels from R1 remain valid only with the Rev 3 hole additions. Issue **`RK-A R2`** from `CEA_RACK_INTEGRATED_v3` v1 (RELEASE_INDEX) before fabrication.

---

## 5. NEEDS TRACEABILITY

| ID | Item | Status |
|---|---|---|
| ~~NT-01~~ | Parameter master | CLOSED — RK-A-PARAM Rev 2 (63 parameters from v3 v1) |
| ~~NT-02~~ | Depth-plane frame stability | **CLOSED by analysis 2026-09-10** — VR-07 in RK-A-QC Rev 4; T16 becomes confirmatory |
| NT-03 | `RK-A-107B` joint stiffness is calculated, not measured | Closes at **T19** coupon on the first plate batch, before T16 is interpreted |

## 6. NEEDS DECISION

| ID | Decision required |
|---|---|
| ND-01 | **Part-drawings divergence.** The local build archived at `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` holds Rev 2 content (11 chapters, contains the corrected 1797 mm brace) while the published artifact of the same ID holds Rev 1 (14 chapters). The published Rev 1 contains three chapters the local build does not. Which is the intended part-drawing release, and what happens to the three missing chapters, must be decided before part drawings are reissued. **Nothing has been reconciled** |
| ND-02 | **Duplicate manufacturing pack artifact.** Two published "Rack A Manufacturing Pack" artifacts exist: `9f5e09e5` (Rev 2, current, referenced everywhere) and `817abd35` (dated 04 Sep, orphaned, referenced by nothing). Retire the orphan or state why it is kept |
| ND-03 | **Plenum interface freeze.** The ducted plenum is deferred to a Phase-2 entity; Phase 1 ships standalone EC fans. The rack-to-plenum mechanical and electrical interface is not frozen, so the Phase-1 build cannot be guaranteed plenum-ready. Decide whether to freeze the interface now or accept rework at plenum introduction |
| ND-08 | **`RK-A-ROOM` Rev 5.** Floor and anchor loads restated at 136.4 kg dry; anchor detail becomes the strut (M10 masonry, 127 mm Row A, 254 mm B/C); no set-out change (installed width unchanged) |
| ND-09 | **Valve technology trial** (EDR-016 alternatives): scope, duration and metrics for comparing all-solenoid zero-ΔP and all-motorised against the baseline, at the pilot grow |
| ND-10 | **Tray floor**: flat floor with a level tolerance, or formed drainage channels to the drain boss (recommended). Decide before the thermoforming quotation |
| ND-04 | **Installed depth allowance.** Installed depth is 690 mm with the plenum and 648 mm without. Room set-out currently assumes the installed figure. Confirm that Phase-1 racks are spaced at the plenum-ready pitch so the plenum can be retrofitted without moving racks |
| ND-05 | **Canopy velocity CV action threshold.** Two thresholds appear in our own source set: RK-A-SYS §01 gives 15 % → fit side/rear enclosure panels; RK-A-ROOM §04 gives 20 % → below it the plenum is an optimisation, above it a required fix. These read naturally as a two-step escalation ladder, but no document says so and inferring it would be a silent reconciliation. Confirm the ladder or pick one |
| ND-06 | **Room electrical phase imbalance.** The as-designed 11-rack layout lands at ~20 % imbalance on single-phase HVAC against a 15 % target. RK-A-ROOM §05 records it as resolved by specifying 3-phase HVAC, but explicitly as an open engineering finding rather than a clean pass. Confirm the 3-phase specification is committed |
| ND-07 | **Terrace slab loading — LOW PRIORITY, kept as UNKNOWN.** RK-A-WRS §04 Risk 3 gives 5.5 kN/m² concentrated against a typical 1.5–2.0 kN/m² terrace rating. **Owner decision 2026-09-09: this is not a blocker** — the tank will sit on a purpose-built steel structure spanning to suitable bearing points, not directly on the slab. It stays open as an unknown because that steel structure is not yet designed and its bearing reactions are unquantified. Re-raise when the structure is specified |

---

## 7. Deferred by design

| Item | Status |
|---|---|
| Ducted plenum ventilation | Deferred to month 2–3. Phase 1 uses standalone EC fans. Point-source fan velocity CV ≈ 33 % against ≈ 10 % for a ducted plenum, so this is a known, accepted uniformity penalty for Phase 1 |
| Reflective panel accessory set | Specified (`RK-A-501`, `RK-A-502`) but held out of the structural drawing reissue |
| LED mounting rail `RK-A-301` | Specified, held out of the Rev 2 structural set |

---

## 8. Next engineering action

1. **Export `RK-A R2`** from `CEA_RACK_INTEGRATED_v3` v1 with `ExportManager.execute()` checked, DXF flat patterns for the 3 mm / 2 mm / 4 mm plates and the mesh panel included.
2. **Regenerate the RK-A-DWG sheets** from v3 v1 (add the new parts to `drawings/generator/parts.py`) and put ND-01 to a decision.
3. **Decide ND-10** (tray floor) and get the thermoforming quotation.
4. **Build the prototype**: T19 coupon on the first `RK-A-107B` batch, then T1–T20 with the unified criteria (T16 at 300 N, elastic ≤ 10 mm, residual ≤ 2 mm).
5. Reissue `RK-A-ROOM` Rev 5 (ND-08) and publish the Rev 3 / Rev 4 documents as HTML.
