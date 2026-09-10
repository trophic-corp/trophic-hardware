# RK-A-QC Rev 4 — Engineering Validation Record, CEA Rack Platform (Rack A)

| | |
|---|---|
| **Document** | RK-A-QC · Rev 4 · 10 September 2026 · controlled document — supersede rather than edit |
| **Supersedes** | Rev 3 (2026-09-09). Rev 3 content stands except where restated below; Stage 2 (room) is unchanged and not reproduced |
| **Stage 1 basis** | Fusion `CEA_RACK_INTEGRATED_v3` **v1** (Rev 6) — ECP-01 applied on the v8 baseline |
| **Inputs** | RK-A-REV Rev A (independent review), RK-A-ECP-01 Rev A (change package), EDR-014…020, ICR-005…007 |
| **Format note** | Issued as Markdown in the repository; the published HTML rendering follows at the next document cycle |

---

## 00 · What changed in this revision

Rev 3 recorded fourteen Stage-1 validation areas, nineteen findings closed, and five open items. An independent read-only review (RK-A-REV Rev A, 2026-09-10) inspected the v8 model and the document set and raised 35 findings, of which one was Critical and eight High. The controlled engineering change ECP-01 resolved them in the model (v3 v1) and this record restates every check whose basis changed. Nothing in Rev 3 that was correct has been re-run; VERIFICATION_INDEX §4 applies.

### Rev 3 checks and results that stand unchanged

V2 (NIOSH), V3 (irrigation flow), V4 (drainage capacity with sequencing), V5 (gravity head — restated as VR-04), V7 (electrical load), V9 (fan placement), V13 (fail-safe polarity), V14 (manufacturability — reconfirmed with the rivet-nut setter added). Beam bending and deflection (Rev 3 V1 arithmetic) reproduce exactly and stand.

---

## 01 · Stage 1 — restated structural checks (MFG §02 numbering)

| # | Check | Rev 3 | **Rev 4** | Criterion | Verdict |
|---|---|---|---|---|---|
| 1 | Beam bending, 80 kg UDL | σ 37.3 MPa, SF 5.6 | **confirmed** 37.3 MPa / SF 5.6 (independent re-calculation) | fy 210 | Pass |
| 2 | Shelf deflection service / fault / design | 0.50 / 0.85 / 1.79 mm | **confirmed**; 0.50 mm is the 22.5 kg case, 0.85 mm the 38 kg fault case | ≤ 3 mm | Pass |
| 3 | Upright compression and buckling | 2.31 MPa; Pcr 746 kN at Le 400 (SF 1313) | **restated**: rated post load 1119 N (136.4 kg dry + 4 × 80 kg); σ 4.6 MPa; effective length **1950 mm** (frame is now braced in both planes by cross beams + moment-capable joints), Pcr 31.4 kN, **SF 28**; P-Δ included in VR-07 | fy; Euler | Pass |
| 4 | Joint strength — `RK-A-107B`, 4 × M8 | 2 × M8, SF 157/108 | bolt shear SF > 100; rivet-nut pull-out ≥ 8 kN vs 0.45 kN couple force at 300 N sway; crush-tube bearing on 1.5 mm wall 13 MPa | — | Pass |
| 4a | **Joint stiffness** (new) | not checked | ≈ 8 kN·m/rad calculated (two 25 mm bolt couples in series); friction slip moment ≈ 110 N·m vs ≈ 25 N·m demand | qualified by **T19** | Pass on paper, **T19 required** |
| 5 | Rack stability — seismic | 74 vs 489 N·m, Ah 0.05 | **restated** (VR-11): IS 1893 Pt 1:2016 cl. 7.13, Z 0.16, ap/Rp 2.5/2.5, loaded rack 288 kg at CG Z 0.91 m: overturning 207 N·m vs restoring 642 N·m (rear), **SF 3.1**; rigid-component assumption SF 7.8 | ≥ 1.5 | Pass |
| 6 | Tip-over — horizontal pull at 1500 mm | 139 N empty / 307 N loaded | **restated from the v3 v1 CG (X 642, Y 350, Z 907)**: dry all-systems **170 N push-to-rear**, 294 N push-to-front, 555 N sideways; loaded 4 × 38 kg: 428 / 553 / 1173 N; Phase-1 configuration (no plenums/panels/fixtures, 108 kg, CG moves forward to Y ≈ 315): ≈ 160 N push-to-rear, ≈ 210 N push-to-front | anchors mandatory | Anchor (EDR-017) |
| 7 | Water loading — blocked drain | 38.0 kg tier | unchanged; overflow level at 7.2 L/min **≈ 38 mm** (weir), freeboard 9 mm | T8 ≤ 42 mm | Pass |
| 8 | LED rail with 2 / 4 kg fixture | 0.93 mm | 0.6 / 1.1 mm on 1172 mm rail | visually flat | Pass |
| 9 | LED heat clearance | 144 mm | 144 mm to canopy; nozzle-to-fixture 145 mm | band 80–200 mm | Pass |
| 10 | Fan vibration | 13.3 Hz vs 33/233 | 13.0 Hz — confirmed | no coincidence | Pass |
| 11 | Drainage — DN40 outlet at 22 mm head | 30.7 L/min | orifice 30.7 L/min confirmed; **valve-governed**: motorised DN40 Kv 60 drops 9.6 mm at 30.7 L/min; drain time ≈ 19 s calculated (quasi-static, incl. 85 mm fall to the valve, strainer excluded) | T7 ≤ 60 s | Pass |
| 12 | Operator access | LI 0.50–0.72 | unchanged | LI ≤ 1.0 | Pass |
| 13 | Floor clearance | 150 mm | 150 mm; tundish/leak sensor now behind the rear-right upright at Y 570–660 | 150 mm | Pass |
| 14 | Electrical / water separation | 236 mm | **restated**: enclosure bottom Z 1700 vs highest water (tier-4 drop run top Z 1638, supply riser top 1300) = **62 mm** vertical at the drop, 400 mm at the riser; separation is by ELV boundary and IP65, not by distance — W9 wording corrected | ELV below canopy; IP65 | Pass (restated) |
| 15 | Manufacturability | saw, punch, bolt | + laser plates, rivet-nut setting, crush-tube dropping; no welding | Coimbatore capability | Pass |
| 16 | **Overflow capacity** (new) | orifice 11.9 L/min | weir over Ø32 crest: 7.6 L/min at 8 mm head; 23.7 L/min at the rim; level at 7.2 L/min ≈ 38 mm | freeboard > 0 at fill rate | Pass |
| 17 | **Valve operability** (new) | — | fill: zero-ΔP NC solenoid at 0.26 bar; drain: motorised spring-return-open at 0 bar | ΔP-min = 0 | Pass by specification (EDR-016) |
| 18 | **Fill air gap** (new) | — | nozzle outlet Z 385, rim 347 → 38 mm ≥ 2 × DN16 | EN 1717 AA | Pass, **T20** |

---

## 02 · VR-07 — Depth-plane frame stability (NT-02 closed by analysis, confirmed by T16)

**Method.** Matrix-stiffness model of one Y–Z end frame: two uprights (40 × 40 × 1.6, continuous, pinned at the feet), five post-to-post links (base beam at Z 165 and cross beams at 258.4 + 400·n, all 30 × 30 × 1.5) with identical rotational springs *k* at both ends (Monforton–Wu semi-rigid elements); geometric stiffness (P-Δ) at the rated post load 1119 N; half the test load applied at Z 1500, four uprights sharing.

| Joint stiffness k | Sway at 1500 mm, 200 N | 300 N | 300 N with P-Δ |
|---|---|---|---|
| 1 kN·m/rad | 23.1 mm | 34.6 mm | 60 mm |
| 5 kN·m/rad | 5.1 mm | 7.6 mm | 8.3 mm |
| **8 kN·m/rad (`RK-A-107B` calculated)** | **3.4 mm** | **5.1 mm** | **5.4 mm** |
| 20 kN·m/rad | 1.7 mm | 2.5 mm | 2.6 mm |
| Rigid | 0.5 mm | 0.8 mm | 0.8 mm |

**Result.** With the ECP-01 joints the frame passes T16 (≤ 10 mm elastic) with a factor of ≈ 1.9 on the calculated stiffness; the test passes down to k ≈ 3.5 kN·m/rad. Friction capacity of the preloaded joint (≈ 110 N·m) exceeds the joint moment at 300 N (≈ 25 N·m), so no bolt slip and no residual set is expected. **T19 measures k on a coupon before T16 is interpreted.** Limitations: joint stiffness is calculated, not measured; bolt-hole clearance take-up is assumed prevented by preload; the deck is treated as non-structural (conservative).

## 03 · VR-11 — Seismic (recorded for the first time)

IS 1893 Part 1:2016 cl. 7.13, ground-floor component, Zone III assumed (Z 0.16; Zone II gives lower demand). Flexible component ap/Rp = 2.5/2.5, Ip 1.0 → coefficient 0.08. Loaded rack 288 kg (136.4 dry + 4 × 38): overturning 0.08 × 288 × 9.81 × 0.914 = 207 N·m; restoring about the rear feet 288 × 9.81 × 0.227 = 642 N·m; **SF 3.1** unanchored, and the rack is anchored in any case. Zone remains unresolved in the brief (immaterial to the verdict).

## 04 · Model verification — `CEA_RACK_INTEGRATED_v3` v1

| Quantity | v8 (Rev 5) | **v3 v1 (Rev 6)** |
|---|---|---|
| Unique parts / occurrences | 45 / 177 | **70 / 417** |
| Dry mass, all systems, fixture envelopes at 1.18 kg | 112.66 kg | **136.39 kg** |
| Centre of gravity (X, Y, Z) | 640.7, 357.3, 930.4 | **642.0, 349.8, 907.0** |
| Envelope | 1456 × 690 × 1960 | **1456 × 690 × 1960** (unchanged) |
| User parameters | 55 | 63 |
| Interference results | 94 (Rev 3 count) / 133 (review re-run) | **204**, all designed connections — whitelist below |
| Structural clashes | — | **0** |

**Interference whitelist (recorded, Rev 4).** All 204 results fall in these classes and no other: (a) rivet nuts embedded in the upright wall (80); (b) tank connectors, strainer and overflow bulkhead through the tray floor and deck panel (24); (c) LED hangers through fixture envelope and rail (32); (d) pipe-to-pipe, pipe-to-valve, pipe-to-manifold, pipe-to-header and nozzle-to-drop joints (68). Any result outside these classes at the next run is an unresolved clash.

**Mass by system (kg):** structure 82.4 (uprights 14.6, long beams 15.8, short beams 6.4, deck rails 19.4, deck panels 7.9, brace 2.2, gusset plates 10.3, rivet nuts/crush tubes 2.7, feet/inserts 2.2, anchor struts 0.9) · trays 9.3 · irrigation/drainage 4.1 · ventilation 18.3 · lighting 15.2 · electrical 2.0 · sensing 0.3.

**Superseded model version.** `CEA_RACK_INTEGRATED_v2` v9 (saved 2026-09-10 during ECP-01) carries collateral cuts on original bodies from API extrude features whose participant bodies were not restricted. It is **not** a design revision and must not be used; the ECP-01 content was rebuilt on the v8 baseline with participant bodies restricted and saved as the new lineage `CEA_RACK_INTEGRATED_v3` v1 (see CAD_INDEX).

---

## 05 · Findings register — RK-A-REV Rev A dispositions

| ID | Sev | Finding (short) | Disposition | Closed by |
|---|---|---|---|---|
| F-01 | Critical | Depth-plane stability unverified, joint-dependent | Cross beams + rivet-nut gusset joints; VR-07 | EDR-014/015, T16, T19 |
| F-02 | High | RK-A-107 undefined / not modelled | RK-A-107B defined, modelled, 40 joints | EDR-015 |
| F-03 | High | 18 N·m through thin walls | Rivet nuts, crush tubes, 4 N·m rule | EDR-015 |
| F-04 | High | Brace 1797 = bbox diagonal; no holes | 1810 / 1780.1 on grid rows 150/1450 | EDR-018 |
| F-05 | High | Anchor cannot reach | Telescoping strut 90–320 mm | EDR-017 |
| F-06 | High | Nozzle below rim | Outlet 38 mm above rim | ICR-005, T20 |
| F-07 | High | Valve ΔP-min unspecified | Valve types specified | EDR-016 |
| F-08 | High | Tray STEP not tooling geometry | Formed tray modelled; R1 tray STEP not-for-tooling; ND-10 (fall) | EDR-019 |
| F-09 | High | Buckling Le 400 | Check 3 restated, SF 28 | this record |
| F-10 | Medium | Overflow orifice vs weir; T8 unattainable | Check 16; T8 ≤ 42 mm | ICR-007 |
| F-11 | Medium | Two T16 definitions | One T16 | ICR-007 |
| F-12 | Medium | No joints; whitelist unrecorded; duplicate drops; panel clash | Whitelist recorded; drops rebuilt without overlap; overflow rerouted clear of panels | §04 |
| F-13 | Medium | Structure depends on removable deck | Decks non-structural | EDR-014 |
| F-14 | Medium | Foot thread interface | RK-A-108 insert | EDR-020 |
| F-15 | Medium | 236 mm separation claim | Restated (check 14) | this record |
| F-16 | Medium | Sealed uprights trap water | Ø6 drain holes at Z 55 | EDR-020 |
| F-17 | Medium | Mesh unspecified; datum ambiguity | Flattened mesh spec; on-top datum confirmed | EDR-020 |
| F-18 | Medium | LED rail mount undefined; fixture mass | Saddles RK-A-302, 1172 rail; tip-over at 4 kg fixtures in check 6 | EDR-020 |
| F-19 | Medium | Tip-over basis untraceable | Check 6 restated with CG and directions | this record |
| F-20 | Medium | Four drain-time criteria | T7 ≤ 60 s | ICR-007 |
| F-21 | Low | Seismic unrecorded | VR-11 | this record |
| F-22 | Medium | Tray lift-out through Ø40 hole | Ø52 / Ø46 deck clearance holes | EDR-019 |
| F-23 | Low | Corridor overlaps | Depth table restated in IF-RK-A-MEC Rev 2; cable trays at Y 525–559 | ICR-006 |
| F-24 | Low | V1 label | Corrected (check 2) | this record |
| F-25 | Low | Foot area | Ø50 → 331 kPa; pads 65 kPa | this record |
| F-26 | Low | Phase-1 depth 648 | Withdrawn; Phase-1 depth is 690 (fans in place) | MFG Rev 3 |
| F-27 | Low | 3–5 tier claims | Withdrawn | MFG/DWG Rev 3 |
| F-28…F-30 | Obs | References, base pan, flood-depth wording | Corrected in Rev 3 documents | — |
| F-31 | Medium | T18 mass band | Per configuration (§T18) | ICR-007 |
| F-32…F-35 | Obs | Confirmations | No action | — |

---

## 06 · Acceptance tests T1–T20 (complete set, supersedes Rev 3 T1–T18)

| Test | What | Method | Acceptance | Frequency |
|---|---|---|---|---|
| T1 | Frame squareness | Diagonals, both faces | equal within 3 mm | every rack |
| T2 | Bed flatness | 1200 mm straightedge, 5 positions | ≤ 3 mm over 1176 | every tier |
| T3 | Bed level | digital level, both axes, mesh face | ≤ 1 mm/m | every tier |
| T4 | Static load | 80 kg UDL per tier, 24 h | deflection ≤ 3 mm; no set | first article |
| T5 | Flood volume/time | metered fill | 14.5 ± 1.0 L in ≤ 30 s | every tier |
| T6 | Flood depth uniformity | 5 positions at dwell | 22 ± 2 mm | every tier |
| T7 | Drain time | from end of valve stroke to visually empty | **≤ 60 s** | every tier |
| T8 | Overflow | drain blocked, 7.2 L/min, 10 min | **depth ≤ 42 mm; no spill** | first article, annually |
| T9 | Leak test | all tiers flooded 30 min | zero drips; sensors dry | every rack |
| T10 | Canopy air velocity | 5 points per tier | 0.2–0.5 m/s; max/min ≤ 2.0 | commissioning |
| T11 | PPFD uniformity | 9-point grid | 150–210; min/avg ≥ 0.75 | commissioning |
| T12 | Earth continuity | earth bar to frame **at every gusset-plate joint group** | ≤ 0.1 Ω | every rack |
| T13 | Insulation resistance | 500 V | ≥ 1 MΩ | every rack |
| T14 | RCBO trip | ramp | 15–30 mA, < 300 ms | every circuit |
| T15 | Fail-safe | supply removed mid-flood | fills close, drains open (within stroke time), beds empty, diverter to waste | every rack |
| T16 | Depth-plane sway (closes NT-02) | **300 N** at the top bed, front–back and side, rack loaded 4 × 38 kg | **elastic ≤ 10 mm, residual ≤ 2 mm** | first article |
| T17 | Tip-over with struts fitted | 250 N at 1500 mm, empty | no lift-off | first article |
| T18 | Mass check | weigh dry | **Core 91.7 ± 5 kg · Grow Phase 1 (no plenums, panels, fixtures) 108.0 ± 6 kg · Grow complete without fixtures 126.9 ± 6 kg · model all-systems 136.4 kg** | first article |
| **T19** | `RK-A-107B` joint coupon | one upright stub + beam stub, moment–rotation to 100 N·m | secant k ≥ 5 kN·m/rad to 50 N·m; no slip below 80 N·m | first plate batch, before T16 |
| **T20** | Fill air gap | tray to the rim with drain and overflow blocked | nozzle outlet visibly ≥ 30 mm above water | every rack |

---

## 07 · Open items after Rev 4

| ID | Item | Closes on |
|---|---|---|
| NT-02 | Depth-plane stability — **closed by analysis (VR-07)**; T16/T19 confirm | prototype |
| NT-03 | T19 coupon must be run on the first `RK-A-107B` batch before T16 is interpreted | prototype |
| ND-09 | Valve technology comparison trial (EDR-016 alternatives) | pilot grow |
| ND-10 | Tray floor: flat + level tolerance, or formed channels to the drain boss | before tooling quotation |
| S1-O2, S1-O3, S1-O4 | unchanged from Rev 3 | T10, quotation, lab |
| ICR-004 | Plenum interface not frozen; reserve now Y 571–690 minus the header zone X 1200–1250 and the four lateral windows | Phase 2 |
| R2 export | `RK-A R2` STEP/F3D/DXF export from `CEA_RACK_INTEGRATED_v3` v1 with `ExportManager.execute()` checked | before fabrication |

## 08 · Revision rule (unchanged from Rev 3) — additions

| If this changes… | …re-run |
|---|---|
| Gusset plate thickness, bolt count or rivet-nut spec | VR-07, T19 |
| Header or lateral routing | interference with the recorded whitelist; ICR-006 windows |
| Valve type | check 11, 17; T7, T15 |

## Sign-off

Stage 1 — design validation: **Complete on the v3 v1 baseline · 18 checks · 35 review findings dispositioned**. Stage 1 — release status: **approved for `RK-A R2` export and prototype fabrication once RK-A-DWG Rev 3 sheets are generated from v3 v1** (tabular part definitions are issued in Rev 3 now). Stage 2: unchanged from Rev 3.

*Every structural, hydraulic and thermal result here remains a closed-form or matrix-stiffness calculation checked against the CAD model. Before the platform is sold as a commercial product the structural cases should be confirmed by finite-element analysis with the measured T19 joint stiffness, the airflow by measurement, and the electrical installation by inspection to IS 732.*
