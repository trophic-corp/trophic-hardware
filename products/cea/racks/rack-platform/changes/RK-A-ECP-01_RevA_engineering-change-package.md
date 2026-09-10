# RK-A-ECP-01 Rev A — Engineering Change Package, CEA Rack Platform (Rack A)

| | |
|---|---|
| **Document** | RK-A-ECP-01 · Rev A · 10 September 2026 |
| **Purpose** | Controlled engineering-change phase closing the findings of RK-A-REV Rev A |
| **Input baseline** | Fusion `CEA_RACK_INTEGRATED_v2` **v8** (Rev 5) · RK-A-DWG Rev 2 · RK-A-MFG Rev 2 · RK-A-QC Rev 3 · RK-A-SYS Rev 2 · RK-A-PARAM Rev 1 |
| **Output baseline** | Fusion **`CEA_RACK_INTEGRATED_v3` v1** (Rev 6) · RK-A-DWG Rev 3 · RK-A-MFG Rev 3 · RK-A-QC Rev 4 · RK-A-SYS Rev 2 addendum B · RK-A-PARAM Rev 2 · decision records EDR-014…020, ICR-005…007 |
| **Owner decisions** | Recorded 2026-09-10 (Section 2) |
| **Status** | **Executed 2026-09-10.** Part 1 (design, decisions, verification) and Part 2 (CAD, document reissue) complete — see §9 for what was executed differently from the plan and why. |

---

## 1. Scope and rules

This package applies the corrections required by RK-A-REV Rev A Section F.1 and the high-value items of F.2, using the owner's decisions of 2026-09-10. Rules observed:

- Authoritative artifacts are never overwritten; every change is a new revision or a new Fusion version with a release note.
- Every engineering-value change carries a decision record. Interface-crossing changes carry an ICR.
- Component relocation in Fusion is done by delete-and-recreate at absolute coordinates (EDR-011).
- Existing verification evidence stays valid where the design has not materially changed (VERIFICATION_INDEX §4); the dependency map in RK-A-QC "Revision rule" decides what re-runs.

---

## 2. Owner decisions (2026-09-10)

| # | Question | Decision | Record |
|---|---|---|---|
| D1 | Depth-plane stability (F-01, F-13) | **Reinstate per-tier cross beams**; decks become non-structural | EDR-014 |
| D2 | Fastening through thin-wall sections (F-03) | **Rivet nuts in the uprights** at bracket positions; crush tubes where a bolt must still pass through a section | EDR-015 |
| D3 | Valve technology (F-07) | **Zero-ΔP solenoids for fill, motorised spring-return-open ball valves for drain** as the baseline. Owner intends to trial the alternatives (all-solenoid zero-ΔP; all-motorised) at a later stage to compare efficiency — recorded as an open comparison, not a reopening of the baseline | EDR-016 |
| D4 | Anchoring (F-05) | **RK-A-106 redesigned as a modular, adjustable stand-off** so installers do not need millimetre-accurate room dimensions | EDR-017 |

---

## 3. Decision records (drafted for `docs/decisions/records/`)

### EDR-014 — Per-tier cross beams reinstated; decks non-structural

**Status:** ACCEPTED (owner, 2026-09-10) · **Supersedes:** RK-A-BRIEF §12 lever L1 · **Affects:** RK-A, IF-RK-A-MEC

**Context.** The v8 frame has no front-to-rear member at tier level; depth-plane stability relied on the deck frames and on rotational stiffness of undefined bracket joints (RK-A-REV F-01, F-13). A semi-rigid frame model showed sway at the top bed is governed entirely by joint stiffness; the platform standard §5 forbids structural dependence on a removable part.

**Decision.** Two RK-A-103 short beams (GI SHS 30 × 30 × 1.5, 480 mm) are fitted at every tier, in the upright columns at X 0–30 and X 1226–1256, Y 40–520, Z 243.4–273.4 + 400·n — the same section, length and position family as the existing base pair. Total RK-A-103 quantity 2 → **10**. Deck assemblies carry no structural duty and may be lifted out without tools.

**Consequences.** +8 × 0.644 kg = **+5.15 kg**, **+₹562** (already costed in RK-A-BRIEF §12). The DN50 drain header in the right-hand column clashes with the new beams and moves outboard (ICR-006). LED rails gain a support member above them at each tier (F-18). Verification: with EDR-015 joints the frame model gives 3.4 mm sway at 200 N and 5.4 mm at 300 N including P-Δ at rated post load — inside the T16 limit with margin (RK-A-QC Rev 4 VR-07).

### EDR-015 — Rivet-nut joints and RK-A-107B gusset-plate connector

**Status:** ACCEPTED (owner, 2026-09-10) · **Affects:** RK-A, platform mechanical standard §2

**Context.** M8 at 18 N·m (≈ 11 kN preload) through both walls of 1.5–1.6 mm hollow sections collapses the walls at ≈ 0.6–0.9 kN (RK-A-REV F-03). RK-A-107 was not modelled and its documented geometry could not be reconciled with the grid (F-02).

**Decision.**
1. **M8 steel flat-head rivet nuts** (zinc-plated, grip 1.0–3.0 mm, Ø11.0 +0.1/−0 hole) are set in the *near wall only* of the upright at every bracket position. The Ø9 grid hole in the far wall stays as-is and is unused at that position. 80 rivet nuts per rack (40 joints × 2).
2. **RK-A-107B beam-end gusset plate**: a *flat* 3 mm GI plate 140 × 88 (tiers) / 140 × 80 (base) lying on the outer face of post and beam together — front and rear faces (Y −3…0 and 560…563) for the long beams, outer X faces (X −3…0 and 1256…1259) for the cross beams. Two Ø9 holes on the post centreline at the two grid rows straddling the beam (rows 200/250 + 400·n at tiers; 150/200 at the base) bolt to rivet nuts; two Ø9 holes at 25 and 75 mm from the beam end bolt *through* the beam's existing end holes with **crush tubes** (Ø8.5 × 27). No bend line, so the plate is in-plane stiff and nests flat. Each joint: 4 × M8. Quantity: 40 joints per rack (16 long-beam ends and 16 cross-beam ends at the tiers, 8 at the base); left/right-hand and base/tier hole patterns give four plate variants from one blank.
3. **Torque 18 N·m** stays valid for M8 into rivet nuts and for through-bolts with crush tubes. Any M8 through a hollow section without a crush tube is limited to **4 N·m** with a serrated flange nut (LED rail saddles, panels).
4. Grid rows used: Z 200/250 + 400·n at the tiers and 150/200 at the base, on the post *front/rear* (Y) faces for the long beams and the post *outer* (X) faces for the cross beams. The plate top is flush with the beam top (273.4 + 400·n) so the deck rails are unaffected; the plate bottom at row − 15 mm. The beam end bears directly on the post face in compression.

**Consequences.** Joint rotational stiffness ≈ 8 kN·m/rad (two 25 mm couples in series with the plate), friction slip moment ≈ 110 N·m against ≈ 25 N·m demand at 300 N sway → no slip, no residual set. Fastener count: 208 → **≈ 360** (40 × 4 bolts + 32 deck + 8 brace + 16 LED + 4 anchor + 48 panel + 80 rivet nuts + 80 crush tubes). Tooling: one M8 rivet-nut setter. The keyhole/hook connector remains the volume roadmap item; RK-A-107B is its prototype-stage stand-in and its moment–rotation test (new acceptance test T19) is the qualification data for the hook design.

### EDR-016 — Valve technology: zero-ΔP fill solenoids, motorised spring-return-open drain valves

**Status:** ACCEPTED as baseline (owner, 2026-09-10) · **Open comparison:** owner intends to trial the alternatives · **Affects:** RK-A, IF-RK-A-HYD, `trophic-contracts` (actuator polarity, timing)

**Context.** No minimum operating differential was specified for any of the eight valves; drain valves must open on ≈ 0.002 bar of gravity head and fill valves see 0.26 bar (RK-A-REV F-07). Servo-assisted solenoids will not open on the drain side.

**Decision.**
- **Fill (4 ×):** DN20 direct-acting or forced-lift **zero-differential** solenoid, normally **closed**, 24 V DC, Kv ≥ 4 (head budget unchanged: 0.119 m at 7.2 L/min), PP/PA body, EPDM seals, IP65 coil, coil duty ≤ 30 s per tier per cycle.
- **Drain (4 ×):** DN40 full-bore **motorised ball valve**, 24 V DC, **spring-return to OPEN** (power-off = drain), Kv ≈ 60, stroke 5–15 s, IP67 actuator, EPDM seats, PP/PVC-U body, position feedback contact to the rack controller. Energised closed during fill + dwell (≈ 12 min per cycle).
- Fail-safe matrix (EDR-007) unchanged in effect: loss of 24 V → fills closed, drains open.
- **Control consequence (contracts):** drain "open" is no longer instantaneous; the controller must allow the stroke time before declaring a drain fault, and the sequential-draining interlock counts a tier as draining from *end of stroke*.

**Recorded for later trial (owner):** (a) all-solenoid with zero-ΔP NO DN40 valves; (b) all-motorised. Metrics to compare: coil/actuator energy per cycle, drain time, failure-to-open events over 30 days, cost. Trial does not change the frozen interface until an EDR supersedes this one.

### EDR-017 — Modular adjustable anchor RK-A-106B

**Status:** ACCEPTED (owner, 2026-09-10) · **Supersedes:** RK-A-106 (60 × 60 × 4 bracket) · **Affects:** RK-A, IF-RK-A-MEC §5, RK-A-ROOM

**Context.** The 60 mm bracket cannot reach a wall 127 mm behind the rack rear face nor a partner rack 254 mm away (RK-A-REV F-05). Installers should not need millimetre-accurate room dimensions.

**Decision.** RK-A-106B is a telescoping strut: outer GI SHS 30 × 30 × 1.5, inner GI SHS 25 × 25 × 1.5, both with Ø9 holes at 20 mm pitch along the overlap, locked with 2 × M8 through-bolts with crush tubes. Rack end: 3 mm GI plate 60 × 100 with 2 × Ø9 at 50 pitch bolting to rivet nuts at Z 1850/1900 on the rear face of each rear upright. Far end: **two interchangeable feet** — (a) wall foot, 60 × 60 × 4 plate with a 9 × 20 slot for one M10 masonry anchor (min 60 mm embedment); (b) partner foot, 60 × 60 × 4 plate with 2 × Ø11 that bolts face-to-face to the partner rack's strut foot. **Adjustment range 90–320 mm** in 20 mm steps plus slot; covers Row A (127 mm), rows B/C rear-to-rear (254 mm) and racks pushed against a wall (90 mm). Two struts per rack.

**Consequences.** Anchor bolt size unified at **M10** for masonry (RK-A-ROOM) and **M8** for strut-to-rack and strut-to-strut. Capacity: 25 × 25 × 1.5 over 320 mm buckles at > 250 kN; demand ≤ 0.5 kN — the strut is stiffness- and installability-driven, not strength-driven. Mass +1.8 kg. T17 unchanged.

### EDR-018 — Rear X-brace RK-A-104 re-derived on the grid; supersedes EDR-010

**Status:** ACCEPTED · **Affects:** RK-A-DWG CH04, RK-A-MFG §07/§08

**Context.** EDR-010's 1797 mm was the bounding-box diagonal; the v8 bar is 1771.6 mm with no holes and its ends stop at the upright inner faces; 1757 mm hole centres land on no grid pair (RK-A-REV F-04).

**Decision.** Two separate bars, GI flat 25 × 3. Holes on the rear-upright centrelines (X 20 and X 1236) at grid rows **Z 150 and Z 1450**. Hole centres **1780.1 mm**, end distance 15 mm, **bar length 1810 mm**, angle 46.9°. The rear gusset plates (EDR-015) occupy Y 560–563, so bar A lies at Y 563–566 on 3 mm packers (40 × 25 × 3) at its ends and bar B at Y 566–569 on 6 mm packers; the bars cross without being joined and lie flat on the plate faces where they cross them. Rear panel RK-A-501 moves to Y 569–571; plenum reserve start moves 565 → 571 (ICR-004 remains open; plenum not frozen). Each end: one M8 through the Y-grid hole of the upright (both walls) **with a crush tube** (Ø8.5 × 36.8), 18 N·m. Net section 48 mm² → 10 kN capacity against 0.44 kN demand at 300 N.

### EDR-019 — Flood tray RK-A-401 modelled as the formed part

**Status:** ACCEPTED · **Affects:** RK-A-DWG CH11, RK-A-MFG §05/§10, R1 release note

**Decision.** The v9 tray body carries: 30 mm collar (Ø32 bore, 3 mm wall, 2° draft) at X 120 from the right end / Y 480; Ø40 drain boss and Ø32 overflow boss with 4 mm flat seats; floor fall 2.5 mm from the front-left corner to the drain boss; R6 internal corners; 3 mm wall. Deck panel RK-A-203 gains a Ø52 drain clearance hole and a Ø46 overflow clearance hole (tank-connector nut clearance) so a tray with connectors fitted lifts straight up (closes F-22). The R1 tray STEP is annotated in the release index as **not-for-tooling**.

### EDR-020 — Miscellaneous structural details (feet, uprights, LED saddles, deck mesh)

**Status:** ACCEPTED · **Affects:** RK-A-DWG CH01/05/10, RK-A-MFG BOM

1. **Foot insert** RK-A-108: zinc-plated steel M12 square tube insert for 36.8 mm bore, press-fit in the upright bottom (replaces the bottom plastic cap). Foot RK-A-105 M12 × 60, nylon base, ±20 mm — unchanged.
2. **Upright drainage:** 2 × Ø6 holes at Z 40 on the two grid faces (below the base beam, above the insert) so wash-down water inside the tube drains. Top cap retained.
3. **LED rail saddles** RK-A-302: 2 mm GI end saddle at each rail end, bolted to a rivet nut on the upright inner X-face at Z 650/1050/1450/1850 with an 8.4 mm drop tab so the rail top sits at 643.4/1043.4/1443.4/1843.4 (unchanged rail positions). Nylon isolating washer retained. Top-tier rails use the same saddle — no "dedicated rail" part.
4. **Deck mesh:** *flattened* expanded metal, 1.6 mm strand, LWD 30 × SWD 12 (or equivalent ≥ 70 % open), laid with LWD along the 1176 span; panel sits **on top** of the deck frame as modelled (Z 298.4–300.0) — EDR-001 datum stack confirmed, the "flush ≤ 1 mm" note in DWG CH10 is withdrawn. 20 mm folded edge on the two long sides only, folding downward outside the long rails.

### ICR-005 — Fill nozzle air gap

**Interface:** Hydraulic (rack inlet side, EDR-006 family) · **Status:** ACCEPTED

The v8 nozzle outlet at Z 345 sits 2 mm below the tray rim (Z 347). Nozzle body moves to **Z 385–430** (outlet 38 mm above the rim ≥ 2 × DN16 = 32 mm, EN 1717 type AA); tier-drop X-run to Z 422–438, Y-run to Z 422–438. Clearance to the LED fixture underside: 145 mm. Applies to all four tiers. Verified physically at install (added to VERIFICATION_INDEX §3 alongside the tundish gap).

### ICR-006 — Drain header outboard; installed width 1456 → 1472 mm

**Interface:** Mechanical envelope (IF-RK-A-MEC §1), facility set-out (RK-A-ROOM) · **Status:** ACCEPTED, **room set-out check required**

The DN50 header moves from X 1216–1266 to **X 1262–1312** (outside the right-hand upright column and clear of the 3 mm cross-beam gusset plates at X 1256–1259), Y 455–505 unchanged; header level switch, tray-drain laterals and overflow laterals extend +46 mm; tundish becomes 60 (X) × 120 (Y) × 80 at X 1252–1312, Y 425–545, Z 20–100 (air gap 100 mm unchanged, outlet Z 200 unchanged). Installed envelope **1472 × 690 × 1960**. RK-A-ROOM Rev 4 rack pitch 1476 no longer clears the next rack's end enclosure; the pitch becomes **1492** (20 mm inter-rack gap). Rows B/C (4 racks) then end at X 6048 against the wall at 6096 — fits with 48 mm; Row A (3 racks) unaffected. RK-A-ROOM must be reissued (Rev 5) — recorded as ND-08.

### ICR-007 — Acceptance-test criteria unified

**Interface:** Verification (RK-A-QC), `trophic-contracts` (timing) · **Status:** ACCEPTED

| Test | Old | New |
|---|---|---|
| T7 drain time | ≤ 30 s / ≈ 55 s / < 60 s / < 90 s | **≤ 60 s** from end of valve stroke to visually empty, every tier |
| T8 overflow | bed depth never exceeds 30 mm | **≤ 42 mm** at 7.2 L/min with the drain blocked for 10 min; no spill over the rim (weir physics: ≈ 38 mm expected) |
| T16 sway | 200 N/≤ 10 mm *or* 300 N/residual ≤ 5 mm | **300 N** at the top bed, front–back and side, rack loaded 4 × 38 kg: elastic ≤ 10 mm, residual ≤ 2 mm |
| T18 mass | 112.7 ± 7 kg | Per configuration (Section 6) |
| **T19 (new)** | — | RK-A-107B joint moment–rotation coupon: ≥ 5 kN·m/rad secant to 50 N·m, no slip below 80 N·m |
| **T20 (new)** | — | Fill air gap: tray filled to the rim with drain and overflow blocked; nozzle outlet visibly ≥ 30 mm above water |

---

## 4. Finding-by-finding disposition

| ID | Sev | Disposition | Closed by |
|---|---|---|---|
| F-01 | Critical | Per-tier cross beams + RK-A-107B rivet-nut joints; frame model 5.4 mm at 300 N with P-Δ | EDR-014, EDR-015, T16, T19 |
| F-02 | High | RK-A-107B defined and modelled; 40 joints, 4 bolts each, one blank size 150 × 100 × 3 developed | EDR-015, DWG Rev 3 CH07 |
| F-03 | High | Rivet nuts + crush tubes; 4 N·m limit elsewhere | EDR-015, platform std §2 |
| F-04 | High | Two bars 1810 mm, holes 1780.1 on grid rows 150/1450, packers | EDR-018, DWG Rev 3 CH04 |
| F-05 | High | Telescoping strut 90–320 mm, two feet, M10 masonry | EDR-017, DWG Rev 3 CH06 |
| F-06 | High | Nozzle Z 385–430 | ICR-005, T20 |
| F-07 | High | Valve types specified; drain ≈ 19 s calculated with Kv 60 | EDR-016, T7 |
| F-08 | High | Tray modelled as formed; deck clearance holes | EDR-019 |
| F-09 | High | Check 3 restated: Le 1950 no-sway (braced by cross beams + joints), SF 30 | QC Rev 4 |
| F-10 | Medium | Weir calc; T8 ≤ 42 mm | ICR-007 |
| F-11 | Medium | Single T16 | ICR-007 |
| F-12 | Medium | Penetrations cut, duplicate drop segments removed, side-panel notch 40 × 40 at the overflow lateral; whitelist recorded in QC Rev 4 | v9, QC Rev 4 |
| F-13 | Medium | Decks non-structural | EDR-014 |
| F-14 | Medium | RK-A-108 insert | EDR-020 |
| F-15 | Medium | Separation restated from v9 (enclosure 1700 vs highest water 438 at nozzle runs, riser top 1300 → **400 mm**); W9 wording corrected | QC Rev 4, SYS addendum B |
| F-16 | Medium | Upright drain holes | EDR-020 |
| F-17 | Medium | Flattened mesh spec, on-top datum confirmed | EDR-020 |
| F-18 | Medium | Saddles RK-A-302; mass model at 4 kg fixtures; V8 criterion restated as 80–200 mm band (144 pass) | EDR-020, QC Rev 4 |
| F-19 | Medium | Tip-over table per configuration and direction | QC Rev 4 |
| F-20 | Medium | T7 ≤ 60 s | ICR-007 |
| F-21 | Low | Seismic check recorded (Z 0.16 flexible, SF 3.1) | QC Rev 4 VR-11 |
| F-22 | Medium | Deck clearance holes | EDR-019 |
| F-23 | Low | Depth table restated: wet corridor 435–525 drainage; supply zone Y 568–643 left end; cable tray moved to Y 525–559 (10 mm shift) | IF-RK-A-MEC Rev 2 |
| F-24, F-25, F-26, F-27, F-28, F-29, F-30 | Low/Obs | Text corrections at reissue; "3–5 tiers" removed; Phase-1 depth defined as 690 (fans in place) — 648 withdrawn | MFG/DWG Rev 3 |
| F-31 | Medium | T18 per configuration | ICR-007 |
| F-32…F-35 | Obs | No action | — |

---

## 5. CAD change list for `CEA_RACK_INTEGRATED_v2` v8 → v9 (absolute coordinates, mm)

All operations create new components or delete-and-recreate (EDR-011). Materials: "Steel, Galvanized" for GI, "Stainless Steel AISI 304" for fasteners, existing library materials otherwise.

| # | Operation | Component | Geometry |
|---|---|---|---|
| C1 | Add 8 | `03_BEAM_SHORT` (tier) | 30 × 30 × 1.5 shell, X 0–30 & 1226–1256, Y 40–520, Z 243.4–273.4 + {0, 400, 800, 1200} |
| C2 | Add 40 | `03_PL107B_LB_L/R`, `_LB_*_BASE`, `03_PL107B_CB_F/B`, `_CB_*_BASE` | 3 mm flat gusset plates 140 × 88 (tiers) / 140 × 80 (base) with 4 × Ø9, on Y −3…0 / 560…563 (long beams) and X −3…0 / 1256…1259 (cross beams); eight component variants, 40 occurrences |
| C3 | Add 80 | `15_RIVET_NUT_M8` | Ø11 × 12 cylinder + Ø13 × 1 flange on the upright near wall at each bracket flange hole |
| C4 | Add 40 | `15_CRUSH_TUBE` | Ø8.5 ID × Ø10 OD × 27 in beam side holes (tier and base beams) and × 36.8 at brace and strut through-bolts |
| C5 | Delete 1, add 2 (+4 packers) | `05_REAR_BRACE_A/B`, `05_BRACE_PACKER` | Bars 1810 × 25 × 3 with 2 × Ø9 at 1780.1 centres, from (X 20, Z 150) to (X 1236, Z 1450) and mirror; A at Y 563–566, B at Y 566–569; packers 40 × 25 × 3 / × 6 |
| C6 | Move | `09_PANEL_REAR` ×4 | Y 563–565 → 569–571 |
| C7 | Delete/recreate | `08_FILL_NOZZLE` ×4, `08_TIER_DROP_X` ×4, `08_TIER_DROP_Y` ×4, `08_TIER_DROP_V1–V4` | Nozzle Z 385–430 (+400·n); X/Y runs Z 422–438; verticals re-spanned without overlap (V1 382→1030 becomes 438→1030 etc.) |
| C8 | Delete/recreate | `09_DRAIN_HEADER`, `09_HEADER_LEVEL_SW`, `09_TRAY_DRAIN_X` ×4, `09_OVF_X` ×4, `09_TUNDISH`, `10_LEAK_SENSOR` | Header X 1262–1312; laterals extended to X 1287 (drain) / 1267 (ovf); tundish 60 × 120 × 80 at X 1252–1312, Y 425–545; leak sensor X 1226–1306 |
| C9 | Replace | `08_FLOOD_TRAY` ×4 | Formed tray per EDR-019 (collar, bosses, 2.5 mm fall, R6, Ø40 and Ø32 floor openings); `09_OVF_COLLAR` deleted (now part of the tray) |
| C10 | Modify | `04_DECK_PANEL` ×4 | Ø52 at (X 1156, Y 480) and Ø46 at (X 1096, Y 480) |
| C11 | Delete/recreate | `14_WALL_ANCHOR` ×2 → `14_ANCHOR_STRUT_106B` ×2 | Outer 30 SHS Y 564–~700 (set at 127 for the room), inner 25 SHS, rack plate 60 × 100 × 3 at Y 560–563, Z 1830–1930; wall foot 60 × 60 × 4 |
| C12 | Add 4 | `13_FOOT_INSERT_108` | 36.6 sq × 40 long insert at Z 0–40 inside each upright |
| C13 | Modify | `02_UPRIGHT` | Ø6 drain holes at Z 40, two grid faces; Ø11 rivet-nut holes replace Ø9 on the near wall at bracket rows |
| C14 | Add 16 | `06_LED_SADDLE_302` | 2 mm end saddles at rail ends on the upright inner faces |
| C15 | Modify | `09_PANEL_SIDE` (right, tiers 2–4) | 40 × 40 notch at the overflow lateral crossing |
| C16 | Shift | `11_CABLE_TRAY_TIER` ×4 | Y 515–555 → 525–559 (clear of the wet corridor, still forward of the brace plane at 560); sits below the tier beams (Z 600–625 vs 643.4), no clash |
| C17 | Parameters | user parameters | add `Brace_Len` 1810, `Brace_Hole_Pitch` 1780.1, `Anchor_Range_Min/Max` 90/320, `Nozzle_Z_Offset` 85 (rim → outlet 38), `Header_X` 1262; `Rack_Width_Installed` 1472 |
| C18 | Verify | — | interference re-run with recorded whitelist; mass, CG, envelope; save as **v9 — "Rev 6 — ECP-01: cross beams, rivet-nut gusset joints, brace re-derived, nozzle air gap, formed tray, header outboard, adjustable anchor"** |

---

## 6. Expected v9 properties (to be replaced by the model read)

| Quantity | v8 | v9 (calculated) |
|---|---|---|
| Unique parts | 45 | ≈ 55 |
| Structure mass | 62.0 kg | ≈ 73 kg |
| Dry mass, all systems, fixture envelopes at 1.23 kg | 112.66 kg | ≈ 124.5 kg |
| Dry mass, fixtures at 4 kg spec | — | ≈ 146.6 kg |
| **T18 bands** | 112.7 ± 7 | Core (frame + decks + trays, no systems) ≈ 84 ± 4 · Grow Phase 1 without plenums/panels/fixtures ≈ 96 ± 5 · Grow complete without fixtures ≈ 115 ± 6 |
| Installed envelope | 1456 × 690 × 1960 | **1472 × 690 × 1960** |
| Tip-over, dry, push-to-rear at 1500 mm | 135 N | ≈ 150 N (anchors remain mandatory) |
| Rated post load | 1061 N | 1090 N; Le 1950, SF ≈ 29 |
| Frame sway, 300 N loaded, with P-Δ | unverified | 5.4 mm (T16 ≤ 10) |
| Fasteners | 208 | ≈ 360 incl. 80 rivet nuts, 80 crush tubes |
| Core cost | ₹12,391 | ≈ ₹14,300 (+cross beams ₹562, +gusset plates/rivet nuts/tubes ≈ ₹1,300, +strut ≈ ₹250) |

---

## 7. Document reissue list (Part 2)

| Document | New rev | Content |
|---|---|---|
| RK-A-PARAM | 2 | 55 → ≈ 61 parameters from v9 |
| RK-A-DWG | 3 | CH03 (qty 10), CH04 (1810/1780.1, two bars, packer), CH06 (strut), CH07 (107B), CH10 (mesh spec, datum note), CH11 (formed tray), new CH12 RK-A-108 insert, CH13 RK-A-302 saddle; tolerances add rivet-nut hole Ø11 +0.1 |
| RK-A-MFG | 3 | Spec (1472 wide), checks 3/5/6 restated, part schedule, BOM (rivet nuts, crush tubes, valves by type), fastener schedule (4 N·m rule), assembly manual (rivet-nut setting step, cross beams, strut adjustment), QC (rivet-nut pull check 10 % sample, air gap), T18 per configuration, costs |
| RK-A-QC | 4 | VR-07 performed (frame model), VR-11 seismic, T7/T8/T16/T18 restated, T19/T20 added, interference whitelist recorded, findings F-01…F-35 register with dispositions |
| RK-A-SYS | 2 addendum B | Valve specification (EDR-016), nozzle height, header position, separation figure, drain time |
| IF-RK-A-MEC / HYD | 2 | Envelope, depth table, anchor stand-off, nozzle air gap, valve stroke timing |
| DECISION_REGISTER | — | EDR-014…020, ICR-005…007 added; EDR-010 SUPERSEDED |
| CURRENT_STATE (repo, rack) | — | NT-02 closed by analysis + T16 confirmatory; ND-04 subsumed by ICR-006 decision; new ND-08 (room pitch 1476 vs 1486) |
| VERIFICATION_INDEX, CAD_INDEX, RELEASE_INDEX | — | v9 lineage, R1 tray STEP not-for-tooling, R2 export requirements |
| `trophic-contracts` | v0.3.0 candidate | drain-valve stroke time, installed width — flagged for the software boundary, not edited from this repository |
| RK-A-REV Rev A | filed | `verification/RK-A-REV_RevA_independent-engineering-review.md` |

---

## 8. Open items created by this package

| ID | Item | Owner |
|---|---|---|
| ND-08 | Room rack pitch 1476 → 1492 after ICR-006 (installed width 1472); RK-A-ROOM Rev 5 set-out table | Owner / RK-A-ROOM Rev 5 |
| ND-09 | Valve technology comparison trial (EDR-016 alternatives) — scope, duration, metrics | Owner, at pilot grow |
| NT-03 | T19 joint coupon test must be run on the first RK-A-107B batch before T16 is interpreted | Prototype |
| — | Plenum reserve now starts at Y 571 (ICR-004 still OPEN) | Phase 2 |


---

## 9. As executed (2026-09-10) — deviations from the plan above

| Planned | Executed | Why |
|---|---|---|
| Fusion v9 of `CEA_RACK_INTEGRATED_v2` | **`CEA_RACK_INTEGRATED_v3` v1** (new lineage `xCLydKPCQ9u2qm-nE7FGag`) | The first pass was saved as `_v2` v9 but its API cut features had unrestricted participant bodies and trimmed original geometry (uprights, beams, hangers, drain fittings). v8 was reopened, every step re-run with participants restricted to the owning component, and — because Fusion will not save an older version back into its lineage through the API — saved as `_v3` v1. `_v2` v9 is quarantined in CAD_INDEX |
| Header outboard at X 1262–1312; installed width 1472; room pitch 1492 (ND-08 as a pitch decision) | **Header behind the rear-right upright** at X 1200–1250, Y 575–625; **installed width unchanged 1456**; ND-08 becomes an RK-A-ROOM reissue for loads/anchor detail only | An outboard header collides with the right-hand cross-beam gusset plates and the tier-1 laterals cannot cross the base beam/plate zone; the rear service zone had room right of the fan end cap. Laterals cross the rear plane in verified windows (ICR-006) |
| Gusset plate rows 200/250 (tier) | **250/300** (tier), 150/200 (base) | Rows 200/250 made tier-1 and base plates overlap on row 200 |
| U-hanger RK-A-107B | Flat gusset plate 140 × 80 × 3 | Hanger side plates clashed with deck rails and the rear brace; a flat plate on the outer face has no bend line and nests flat |
| Brace packers under both bars | Bar A on the rear gusset plates (they are the packer); packers under bar B only; brace bolts share the plate rivet nuts | Plates occupy Y 560–563 |
| Plenum 565–685 | 571–690 (119 deep) | Behind the two brace layers and the rear panel |
| Tray with 2.5 mm floor fall | Flat 3 mm floor; **ND-10** raised | A fall on a floor that rests on the deck cannot be formed without channels or a sloped underside — a real design decision, not a modelling detail |
| LED rail 1176 with saddles bolted to the tier above | Rail **1172**; end saddles on the upright inner faces at rows 600/1000/1400/1800; fixture envelope 62–1194 | Grid holes only exist on the post centreline; saddles need the post |
| Cable trays Y 525–559, X 110–1110 | X 110–**1030** | Clear of the drain crossing window |
| Side-panel notch | Not needed | Overflow laterals no longer pass the panel |
| Mass ≈ 124.5 kg | **136.39 kg** | Gusset plates are 0.26 kg each (10.3 kg total) — heavier than the placeholder estimate; crush tubes and rivet nuts modelled as solids |
| Fasteners ≈ 320 | ≈ 450 items (264 threaded, 100 rivet nuts, 84 crush tubes) | Four bolts per joint at 40 joints |

### Verification of the executed model (`_v3` v1)

70 unique parts · 417 occurrences · 136.39 kg dry (all systems) · CG X 642.0, Y 349.8, Z 907.0 · envelope X −160…1296, Y −5…690, Z −10…1950 · 63 user parameters · interference 204 results, all in the four designed-connection classes recorded in RK-A-QC Rev 4 §04 · original component masses unchanged from v8 (uprights 3.6455 after the Ø6 drain holes; long beams 1.5786; deck panel 1.970 after clearance holes; tray 2.319 with collar).

### Documents issued

EDR-014…020, ICR-005…007 · DECISION_REGISTER · RK-A-PARAM Rev 2 · RK-A-QC Rev 4 · RK-A-MFG Rev 3 · RK-A-DWG Rev 3 (tabular) · RK-A-SYS Rev 2 addendum B · IF-RK-A-MEC Rev 2 · IF-RK-A-HYD Rev 2 · PRODUCT.md · CURRENT_STATE (repo, rack) · CAD_INDEX · VERIFICATION_INDEX · DOCUMENT_REGISTER · RELEASE_INDEX · platform mechanical standards · racks README · RK-A-REV Rev A filed under `verification/`.

### Still to do after this package

`RK-A R2` export with `ExportManager.execute()` checked · regenerate RK-A-DWG sheets (add the new parts to `drawings/generator/parts.py`) · publish the Markdown revisions as HTML · RK-A-ROOM Rev 5 (ND-08) · decide ND-10 · `trophic-contracts` v0.3.0 candidate (drain-valve stroke time) · T19 coupon before the prototype's T16.
