# RK-A-REV Rev A — Independent Engineering Review, CEA Rack Platform (Rack A)

| | |
|---|---|
| **Document** | RK-A-REV · Rev A · 10 September 2026 |
| **Type** | Independent read-only engineering review and verification |
| **Subject** | `RK-A` CEA Rack Platform, release `RK-A R1` (Fusion `CEA_RACK_INTEGRATED_v2` v8 / Rev 5) |
| **Phase** | Review → Inspect → Simulate → Verify → Analyze → Report. **No project artifact was modified.** |
| **Reviewer** | Independent senior mechanical/product engineering review (Claude, Cowork session) |
| **Status** | Issued for evaluation. Recommendations only — nothing in this document has been applied. |

---

## A. Executive assessment

**Classification: Requires engineering revision before prototype.**

The rack architecture is sound and well reasoned: a bolted, welding-free galvanised frame on a 50 mm accessory grid, separated wet modules, a single wet-services corridor, gravity supply, fail-safe valve polarity and a documented air gap. The beam sizing, tier ergonomics, hydraulic sizing and most of the systems integration hold up under independent check, and the document set is unusually candid about its own limits. The design does not need to be redesigned.

It is not, however, ready to be cut. Independent inspection of the Fusion model and the released drawings found a group of defects that would each stop or invalidate a first article, and they sit in exactly the areas the existing validation record admits it never checked:

1. **The depth-plane (front–back) stability of the frame is, as documented, a mechanism.** The model contains no joints, brackets or fasteners; the beam-to-upright bracket RK-A-107 is not modelled and its documented geometry cannot be reconciled with the 50 mm grid; the base short beams and decks are attached through single-bolt brackets in Ø9 clearance holes; the 18 N·m torque specified for M8 bolts passing through both walls of 1.5–1.6 mm hollow sections will collapse the tube walls at roughly 5 % of that torque. A semi-rigid frame analysis (Section D) shows that sway under the T16 test load is governed entirely by joint rotational stiffness, and that the joint as described is unlikely to achieve the ~2.5 kN·m/rad per joint needed to pass T16 at 10 mm. Eight of the eleven racks in the reference room rely on this stiffness because the back-to-back pairing is self-stabilising against rigid-body tip-over only, not against racking.
2. **Three structural parts as drawn cannot be fitted.** The rear X-brace RK-A-104 was "corrected" to 1797 mm using the bounding-box diagonal (1195 × 1342) rather than the bar centreline: the modelled bar is 1771.6 mm, has no holes, and its ends stop at the upright inner faces; the drawn 1757 mm hole centres do not land on any grid pair. The wall-anchor bracket RK-A-106 has a 60 mm reach, but the room set-out places 127 mm of plenum and fans between the rack rear face and the wall (Row A) and 254 mm between the rear faces of rows B and C. The beam-end bracket RK-A-107 is specified with 3 holes, 2 bolts, 12 pieces for 24 joints and two different blank sizes.
3. **Two safety-critical invariants are not honoured by the model.** The fill nozzle outlet sits at Z 345, 2 mm *below* the tray rim at Z 347 — there is no physical air gap at the fill point in the fault case the air gap exists for. The fail-safe drain concept depends on 24 V normally-open DN40 solenoid valves opening on 0.002 bar of gravity head; no minimum operating differential is specified anywhere and most solenoid valves of that size will not open at that pressure.
4. **The released tray model is not tooling geometry.** RK-A-401 in v8 is a flat-floored open box with one Ø40 hole: no moulded collar, no bosses, no 2–3 mm fall, no radiused corners and no overflow penetration. Under the project's own "the model governs" rule, the R1 STEP would produce the wrong thermoforming tool.

None of these requires a change of concept. All of them require a controlled engineering-change cycle and a model reissue before a fabricator receives anything. The prototype and the T16 test remain the right next step *after* that cycle, not instead of it.

---

## B. Design baseline reviewed

### B.1 CAD inspected (Fusion 360, read-only, via the Fusion MCP)

| Design | Version | What was read |
|---|---|---|
| `CEA_RACK_INTEGRATED_v2` | **v8** (Rev 5), lineage `khAY4bsfToGEcB_lXi-5Zg` | Component list (45 unique / 177 occurrences), per-component material, density, volume and mass; assembly mass and centre of gravity; bounding box of every occurrence; joint/rigid-group/as-built-joint counts; face topology of every structural body (hole counts, radii); brace vertex geometry; all 55 user parameters; full pairwise interference analysis re-run |
| `CEA_RACK_PLATFORM_RackA_v1` | v5 | Not opened (preserved baseline; parameter set confirmed identical by RK-A-PARAM) |

Verified against the record: 45 parts, 177 occurrences, **112.657 kg** dry, envelope X −160…1296, Y −5…685, Z −10…1950 (1456 × 690 × 1960), 55 user parameters — all reconcile with RK-A-PARAM Rev 1, CURRENT_STATE and RK-A-QC Rev 3. Dry centre of gravity, read from the model and not previously recorded anywhere: **X 640.7, Y 357.3, Z 930.4 mm**.

### B.2 Documents reviewed

| Document | Rev | Role in this review |
|---|---|---|
| `CLAUDE.md`, repository `CURRENT_STATE.md`, rack `CURRENT_STATE.md`, `PRODUCT.md` | 2026-09-09 | Authority rules, frozen definition, open items ND-01…ND-07, NT-02 |
| `RK-A-BRIEF` platform brief | G | Requirement source; load-case derivation; §12/§14 bracing rationale |
| `RK-A-SYS` systems specification (+ addendum) | 2 | Irrigation, drainage, sensing, ventilation, LED, electrical, FMEA |
| `RK-A-DWG` structural drawings | 2 | Eleven structural parts, tolerances, revision record |
| `RK-A-MFG` manufacturing pack | 2 | Fifteen structural checks, part schedule, fasteners, assembly, QC, costs |
| `RK-A-QC` engineering validation record | 3 | Stage 1/2 validation, findings, corrections, T1–T18 acceptance tests |
| `RK-A-PARAM` parameter master | 1 | Parameter values (independently re-read from v8 — match) |
| `RK-A-WRS` closed-loop water recovery | 3 | Interface B side; head budget |
| `RK-A-ROOM` floor plan | 4 | Set-out coordinates, anchoring, floor loads |
| `interfaces/mechanical`, `hydraulic`, `electrical`, `control` | current | Frozen interfaces |
| `DECISION_REGISTER` + ADR-005, EDR-001/003/010, ICR-001 | current | Decision status |
| `CAD_INDEX`, `VERIFICATION_INDEX`, `RELEASE_INDEX`, `RK-A-R1_MANIFEST` | current | CAD lineage, VR-01…VR-10, release content |
| `platform/mechanical-standards`, `electrical-standards` | current | Platform rules (incl. §5 "structure never depends on a removable part") |
| `drawings/generator/*.py` | — | Not executed; consulted only to confirm drawings are generated, not hand-drawn |

### B.3 Authority as applied

Fusion v8 was treated as authoritative for geometry (ADR-006), the published HTML documents as authoritative for engineering values, and the one recorded exception (EDR-004) as valid. Where the model and a document disagree, both are quoted and the disagreement is recorded as a finding — nothing was reconciled.

### B.4 Classification of what was found in the baseline

| Class | Examples |
|---|---|
| Approved decisions | EDR-001 tier stack, EDR-002 four tiers, EDR-003 wet corridor, EDR-005 gravity feed, EDR-006 air gap, EDR-007 valve polarity, EDR-008 Type A RCBO |
| Engineering assumptions (stated) | Shelf_Load 80 kg UDL; blocked-drain 38 kg governs; Le = 400 mm for upright buckling; joint rigidity sufficient for depth-plane stability; LED fixture 1.23 kg in the mass model against a ≤ 4 kg spec |
| Provisional / deferred | Plenum interface (ICR-004 OPEN); RK-A-301/501/502 held; Phase-1 fans |
| Open questions carried by the project | NT-02, ND-01…ND-07, S1-O1…O4, R-1…R-6 |
| Superseded | RK-A-SYS §4 drain-to-waste; RK-A-DWG Rev 1; P1–P5 test plan (by T1–T18) |
| Inconsistencies found (new) | See findings register: T16 criteria, bracket definition, brace length, anchor reach, nozzle height, drain-time criteria, 236 mm separation, V1 result label, foot area, tier-count claims |

### B.5 Information that was unavailable

- **No joints, constraints, fasteners, brackets or rivets exist in the Fusion model** (0 joints, 0 rigid groups, 0 as-built joints). Joint behaviour therefore cannot be inspected in CAD at all.
- **Fusion Simulation could not be run from this session.** The Fusion API does not expose study creation, and — more importantly — with no contacts, fasteners or brackets in the model, any FEA would have to bond every interface, which returns the rigid-joint bound already obtained analytically (Section D) and would be *non-conservative* for the one question that matters. Structural verification was therefore done by independent calculation and a semi-rigid frame model, and confidence levels are stated per case.
- Solenoid valve datasheets (Kv, minimum operating differential, NO/NC construction), the expanded-mesh specification (LWD/SWD/strand, flattened or raised), the levelling-foot insert detail, the thermoformer's tool geometry, and the RK-A-107 bracket geometry are not in the repository.
- The release store (`E:\My Drive\...`) was not connected to this session; STEP content was taken as reported in `RK-A-R1_MANIFEST.md`.

---

## C. Findings register

Severity: **Critical** — would produce an unsafe, unbuildable or invalid first article; **High** — must be resolved before fabrication release; **Medium** — resolve before manufacturing release / affects validation validity; **Low** — correct at next reissue; **Obs** — observation, no action required.

Evidence codes: **CAD** = Fusion v8 inspection · **CALC** = independent calculation (Section D) · **DOC** = project documentation · **SIM** = frame model (Section D).

| ID | Area | Finding | Sev | Evidence | Engineering impact | Recommended future action |
|---|---|---|---|---|---|---|
| F-01 | Structure — depth plane | Front–back stability relies solely on rotational stiffness of bolted L-bracket joints in Ø9 clearance holes (base short beams RK-A-103 and deck-to-beam corners). No diagonal, no moment connection, feet pinned. Semi-rigid frame model: sway at 1500 mm under 200 N = 23 mm at 1 kN·m/rad per joint, 2.8 mm at 10 kN·m/rad, 0.5 mm rigid. A 3 mm bracket with one bolt in the beam leg and 0.5 mm radial hole clearance has ~0.02 rad free play before any stiffness engages (≈ 30 mm free sway at the top bed). T16 (≤ 10 mm) is unlikely to pass as documented. Rows B/C (8 of 11 racks) depend on this because a rear-to-rear pair is self-stabilising against rigid-body tip-over only, not racking. | **Critical** | CAD (0 joints, no brackets); DOC RK-A-MFG §02, RK-A-QC S1-O1, NT-02; SIM | Rack racks front–back under tray handling; residual set through bolt slip; P-Δ amplification ≈ 25 % at 30 mm sway with 265 kg; unwall-anchored pairs not stable in Y | Define the beam-to-upright and deck-to-beam joint (geometry, bolt count, crush tubes) and either (a) reinstate per-tier cross beams (₹562, already costed) or (b) add an end-frame diagonal/knee in the two YZ end planes, or (c) qualify the bracket joint by test coupon (moment–rotation) before relying on it. Re-run the frame model with measured joint stiffness. Keep T16 but make it confirmatory, not exploratory |
| F-02 | Structure — joints | RK-A-107 beam-end bracket is not in the model or the release STEP set. Documents disagree: 3 holes (2 upright leg @ 50 pitch + 1 beam leg) vs "2 × M8 per bracket"; 12 brackets vs 24 beam-end joints (fastener schedule 24 × 2 = 48); blank 50 × 50 × 3 (DWG) vs 50 × 50 × 40 (MFG). A 50 mm leg cannot carry two holes at 50 mm pitch with edge distance. With beams occupying Z 243.4–273.4 on the upright inner face, grid holes at 250 fall behind the beam end and 300 in the deck-rail zone; the bracket cannot be placed between beam end and upright (beam 1176 = clear width, 0 interference) — its actual position is undefined | **High** | CAD; DOC RK-A-DWG CH07, RK-A-MFG §05/§07/§11 | The primary structural connection of the rack has no defined geometry; interference-clean claim excludes it; joint strength/stiffness figures (SF 157/108) cannot be tied to a real detail | Model the bracket and fasteners in Fusion; resolve counts and blank size; re-run interference; issue the bracket drawing from the model |
| F-03 | Structure — fastening | M8 A2-70 at 18 N·m (≈ 11 kN preload) through both walls of 40 × 40 × 1.6, 30 × 30 × 1.5 and 25 × 25 × 1.5 sections with no crush tubes. Wall collapse (plastic strip mechanism) occurs at ≈ 0.6–0.9 kN, i.e. at ≈ 1 N·m. The torque spec cannot be reached; walls dish, preload relaxes, joints become bearing-only in 1 mm oversize holes | **High** | CALC §D.7 | Joint slip and rotation (feeds F-01); loss of earth-bond continuity at joints; QC torque check at 18 N·m is not meaningful; visible tube deformation | Specify crush tubes/spacers in every through-bolted section, or rivet nuts / threaded inserts, or a torque-limited spec with Nord-Lock/serrated flange nuts; re-derive joint stiffness and the T12 earth-continuity path |
| F-04 | Structure — brace | RK-A-104: model bar is a single merged X body, centreline length **1771.6 mm** (√(1176² + 1325²)), no holes, ends at the upright inner faces (X 40 and 1216). Drawing length 1797 = diagonal of the 1195 × 1342 bounding box, not the bar. Drawing hole centres 1757 imply ΔZ 1268 on ΔX 1216 — not a 50 mm grid pair (grid-compatible options: 1744 for ΔZ 1250, 1780 for ΔZ 1300 on post centrelines). Crossing of two coplanar 3 mm flats at Y 560–563 has no packer/joggle detail. "4 ends × 2" bolts vs "one Ø9 per end" | **High** | CAD (vertices, 0 cylindrical faces); DOC EDR-010, RK-A-DWG CH04, RK-A-MFG §07 | Second consecutive unfittable brace issue; the only diagonal in the structure cannot be bolted to the grid as drawn; EDR-010 needs re-opening | Re-derive from hole-to-hole geometry on the post centrelines, model the two bars separately with holes and a crossing packer, re-issue CH04 and EDR-010 |
| F-05 | Structure — anchoring | RK-A-106 is a 60 × 60 × 4 bracket at Y 560–564, Z 1870–1930. Room set-out: Row A rear structural face is 127 mm from the north wall (plenum/fans occupy Y 565–685); rows B/C rear faces are 254 mm apart. A 60 mm leg reaches neither. Room specifies 2 × M10 anchors; DWG/MFG specify M8 masonry anchors and M8 through-bolts | **High** | CAD (bbox); DOC RK-A-ROOM §set-out table, RK-A-DWG CH06, RK-A-MFG §07 | The mandatory tip-over mitigation cannot be installed as drawn; B/C rear-to-rear bolting infeasible | Design a stand-off anchor strut/channel spanning ≥ 130 mm (Row A) and a rear-to-rear tie ≥ 254 mm (B/C), or anchor from the top of the uprights to the ceiling/wall; align fastener size across documents |
| F-06 | Hydraulic — safety | Fill nozzle 08_FILL_NOZZLE occupies Z 345–390 inside the tray plan (X 140–160, Y 490–510). Tray rim is Z 347: the nozzle outlet is **2 mm below the rim**, 15 mm above the overflow crest. The "physical air gap at all sixteen fill points" invariant is not met in the fault case (drain and overflow both blocked) it exists for. EN 1717 / IS practice: ≥ 2 × d (≥ 32 mm for DN16) above the spill-over level | **High** | CAD (bbox); DOC RK-A-SYS §01/§02, PRODUCT.md invariants | Back-siphonage path from a flooded tray into the gravity main under negative pressure at the terrace | Raise the nozzle so its outlet is ≥ 32 mm above the tray rim (≈ Z 380+) — the LED fixture underside at 583 leaves room; record as an ICR since it touches the hydraulic interface |
| F-07 | Hydraulic — valves | Drain solenoids (DN40, 24 V, normally open) must open on ≈ 0.002 bar (22 mm tray head + ≈ 85 mm fall); fill solenoids (DN20, Kv 4) see ≈ 0.26 bar static. No minimum operating differential, Kv, or construction (direct-acting / zero-ΔP / servo-assisted) is specified. Servo-assisted valves need ≥ 0.2–0.5 bar and will not open on the drain side. A DN40 valve at Kv 30 alone drops 38 mm at 30.7 L/min — more than the 22 mm driving head, so the "30.7 L/min, ≈ 55 s" drain figure ignores the governing resistance | **High** | CALC §D.9; DOC RK-A-SYS §02/§03, IF-RK-A-HYD §3 | Fail-safe drain (EDR-007) may not function at all; drain time and T7/T15 acceptance unattainable; NO zero-ΔP DN40 24 V solenoids are uncommon — a spring-return motorised ball valve is the likely real part | Specify valve type with Kv and minimum ΔP = 0 for all eight valves; re-run drain time with valve + pipe losses; confirm NO fail-safe behaviour with the chosen actuator technology |
| F-08 | CAD — wet module | 08_FLOOD_TRAY in v8: open box, 3 mm walls, flat floor, one Ø40 hole; no moulded collar, bosses, 2–3 mm fall, radiused corners, or Ø32 overflow hole. Overflow collar, bulkhead and strainer are separate bodies overlapping the tray floor (whitelisted). Deck panel has one Ø40 hole and no overflow hole. R1 STEP for RK-A-401 is therefore not the tooling geometry the drawing describes | **High** | CAD (faces/cylinders); DOC RK-A-DWG CH11, RK-A-MFG §15 ("structural set is manufacturing geometry") | A thermoformer working from the STEP under "the model governs" builds the wrong tool; ICR-001 continuity is proven only through overlapping placeholders | Model the tray as the formed part (collar, bosses, fall, radii, both penetrations) and cut both penetrations in the deck panel before any tooling quotation; note the released R1 tray STEP as not-for-tooling |
| F-09 | Structure — uprights | Buckling check uses Le = 400 mm (Pcr 746 kN, SF 1313). The upright is braced at 400 mm only in the width plane; in the depth plane the frame is an unbraced sway frame (F-01) with pinned feet, so Le ≥ 1950 (SF ≈ 30 at rated load) and up to ≈ 3900 if sway is unrestrained (SF ≈ 7). Drawing text "Euler margin over a thousand" is unsupported. Compressive stress 2.6 MPa at service, 4.3 MPa at rated — fine | **High** (as a validation claim) / Low (as a risk) | CALC §D.3; DOC RK-A-MFG §02 check 3, RK-A-DWG CH01 | Check 3 verdict rests on an assumption contradicted by the design; margin is adequate but by ~7–30×, not 1300× | Restate check 3 with the correct effective length once F-01 is resolved; include P-Δ |
| F-10 | Hydraulic — overflow | DN32 collar capacity "11.9 L/min at 8 mm head, 1.65×" uses an orifice formula; a crest at low head is a weir: ≈ 7.6 L/min at 8 mm (margin ≈ 1.05×); 7.2 L/min needs ≈ 7.7 mm head → tray level ≈ 38 mm, 9 mm below the rim (acceptable). Consequently acceptance test T8 ("bed depth never exceeds 30 mm" with the drain blocked) is physically unattainable — overflow requires head above the crest | **Medium** | CALC §D.8; DOC RK-A-SYS §02 R2, RK-A-QC T8 | Margin overstated; T8 would fail every first article regardless of build quality; freeboard is still adequate | Re-state the overflow calculation as a weir; change the T8 criterion to a level (e.g. ≤ 40 mm at full fill rate) in the change phase; keep DN32 |
| F-11 | Validation — T16 | T16 is stated as 200 N / ≤ 10 mm, no permanent set (RK-A-QC Rev 3, RK-A-DWG CH03) and as 300 N / residual ≤ 5 mm (CURRENT_STATE ×2, VERIFICATION_INDEX VR-07, RK-A-MFG P3). Two different tests carry one ID | **Medium** | DOC | The test that closes NT-02 has no single acceptance criterion; results could be read as pass under one and fail under the other | Decide one criterion (recommend: 300 N, elastic ≤ 10 mm, residual ≤ 2 mm, both axes, loaded) and reissue in one place |
| F-12 | CAD — assembly integrity | Assembly has 0 joints / rigid groups; all positions absolute. Independent full interference re-run: **133** overlapping pairs (record states 94), all within plumbing/LED hangers; new against the record: 09_PANEL_SIDE × 09_OVF_X (tiers 2–4, overflow lateral passes through the optional side panel) and 08_TIER_DROP_V1 × V2 (248 mm of duplicated coaxial pipe). "0 unresolved" depends on a whitelist that also masks missing penetrations (F-08) | **Medium** | CAD (analyzeInterference) | Interference-clean is only as good as the whitelist; two genuine items missed; mass slightly double-counted | Cut real penetrations, delete duplicate segments, notch the side panel or reroute the lateral, and record the whitelist explicitly with the next interference run |
| F-13 | Structure — platform rule | Decks are removable ("no tool needed for deck or tray removal", P4) yet are the only front-to-rear tie at tier level and the diaphragm that carries front-post sway to the rear brace. Platform mechanical standard §5: structure must never depend on a part removed for cleaning. Assembly manual bolts decks at four corners — contradicting P4 | **Medium** | DOC RK-A-DWG CH08/09, RK-A-MFG §11/§13, platform §5 | Either the cleaning promise or the structural role must yield; a rack washed with decks out is a mechanism in both planes | Decide: bolted decks (structural, tool required) + revised cleaning procedure, or reinstated cross beams (decks non-structural). Record as an EDR |
| F-14 | Structure — feet | 13_FOOT is a Ø50 × 10 disc at post centre; no threaded insert, nut plate or tube insert in BOM or model; upright bottom is a "pressed plastic cap". Drawing itself says "confirm the thread engages the upright base or a nut plate". ±20 mm adjustment and M12 × 60 not represented | **Medium** | CAD; DOC RK-A-DWG CH05, RK-A-MFG §06 | Foot has nothing to thread into; levelling (a functional requirement for flood depth) undefined; base-cap and foot occupy the same end | Add an M12 tube insert / welded nut plate part; update BOM and CH05 |
| F-15 | Electrical / water separation | Documents claim 236 mm vertical separation and "electrical at the left end, water at the right". Model: enclosure bottom Z 1700; tier-4 nozzle/drop top Z 1590–1598 → **102 mm**. Supply riser, fill manifold and four fill solenoids sit at the left end (X 42–97) within 50–100 mm of the vertical cable channel (X −45…−5) | **Medium** | CAD; DOC RK-A-SYS §01, IF-RK-A-ELE §3, RK-A-QC W9 | Claims are not evidence; ELV-only-below-canopy still holds, IP65 glands-down still holds — risk is documentary, not electrical | Re-measure and restate the separation from the model; correct the W9 statement |
| F-16 | Corrosion / cleaning | Uprights carry 144 Ø9 through-holes into a sealed hollow (plastic end caps both ends); wash-down water enters and cannot drain. Beams/rails are open-ended tubes with touch-up only. Burr note in DWG acknowledges water inside tubes | **Medium** | CAD; DOC RK-A-DWG CH01 M4/M5 | Internal white-rust and biofilm reservoir in a food room; not inspectable | Bottom drain hole / open-bottom insert in uprights; consider capped-and-drained ends on beams; add to cleaning validation |
| F-17 | Deck mesh | Mesh unspecified beyond "1.6 mm strand, ≥ 70 % open": no LWD/SWD, strand width, or *flattened* vs raised. Raised expanded metal gives a 1176 × 560 HDPE tray point support on diamond knuckles, contradicting ±2 mm flood uniformity and the "bed datum = mesh top face". Model: panel sits **on top of** the rail frame (Z 298.4–300) while DWG requires flush ≤ 1 mm step; 20 mm folded edge not modelled | **Medium** | CAD; DOC RK-A-DWG CH10, EDR-001 | Bed datum ambiguous by 1.6 mm; mesh sag between 359 mm bays unverifiable; tray point loading | Specify flattened expanded metal with pattern; decide flush vs on-top and make EDR-001 and the model agree |
| F-18 | Lighting mount | LED rails (Y 168–188, 372–392) span between uprights with no modelled attachment; documented saddle-to-grid on "the underside of the tier above" has no matching holes (beams/cross rails hold end holes only; 0 cylindrical faces in the model). Top-tier "dedicated rail" mount undefined (RK-A-301 held). Fixture mass in the mass model 1.23 kg vs spec ≤ 4 kg (+22 kg per rack at full spec). Clearance 144 mm recorded as pass against a ≥ 150 mm criterion (V8) | **Medium** | CAD; DOC RK-A-SYS §06, RK-A-QC V8, RK-A-MFG §09 | Mounting not buildable from the documented hole pattern; tip-over/post load understated at spec fixture mass; criterion/result mismatch | Model saddles and rail fixings; add grid holes or use the cross-rail positions; re-run mass/tip-over at 4 kg fixtures; reconcile V8 criterion |
| F-19 | Stability — tip-over | Dry CG Y 357 (rear-heavy: plenums, fans, drain, riser). Independent rigid-body result: **135 N** push-to-rear, 249 N push-to-front, 457 N sideways (dry, 1500 mm); loaded 4 × 38 kg: 393/507 N; top tier only with a 38 kg tray pulled 200 mm forward: 249 N. Record figures (139 N / 307 N) reproduce approximately but their basis (mass state, direction, CG) is not recorded; Phase-1 racks without plenums have a different CG | **Medium** | CAD (CG); CALC §D.4; DOC RK-A-MFG check 6 | Anchors mandatory — agreed; but the anchor cannot be fitted (F-05) and freestanding pairs are not covered | Record the tip-over basis (mass state, CG, direction, height); re-run for Phase-1 and Phase-2 mass states and 4 kg fixtures |
| F-20 | Validation — drain time | Four criteria for one quantity: T7 ≤ 30 s; SYS ≈ 55 s; assembly flood test "< 1 min"; QC checklist "< 90 s" | **Medium** | DOC | Acceptance ambiguity; with realistic valve losses (F-07) 30 s is unlikely | Single criterion after valve selection |
| F-21 | Seismic | Check 5 (74 N·m vs 489 N·m, Ah 0.050) is not reproducible from stated inputs. Independent IS 1893 Pt 1 cl. 7.13 component check: loaded rack, Z 0.16, ap/Rp 2.5/2.5 → 192 N·m overturning vs 589 N·m restoring (SF 3.1); rigid-component assumption SF 7.7. Passes, but no record of a completed check exists (VERIFICATION_INDEX §3) | **Low** | CALC §D.10; DOC | Verdict likely correct; traceability absent | Record the check with inputs in the change phase |
| F-22 | Serviceability — tray lift-out | Deck panel hole Ø40; tank connector body (09_TRAY_OUTLET) Ø50 spans Z 294–324 through the panel. A tray with connectors fitted cannot lift through a Ø40 hole; the "lift out after releasing one clamp coupling" sequence is unverified | **Medium** | CAD | Cleaning cycle P4 (≤ 45 min, no tools) may not be achievable | Model the connector, nut and the required deck clearance hole; verify the lift path |
| F-23 | Space allocation | Wet corridor Y 435–525 (EDR-003) claims exclusivity; 11_CABLE_TRAY_TIER occupies Y 515–555 (10 mm inside the corridor); supply riser/manifold/solenoids at Y 568–643 are outside "one corridor for all wet services" | **Low** | CAD; DOC EDR-003, IF-RK-A-MEC §2 | Documentary; no physical clash | Update the depth-allocation table to what the model shows |
| F-24 | Validation record | V1 "0.50 mm at 38.0 kg/tier" — 0.50 mm is the 22.5 kg service case; 38 kg gives 0.85 mm (beam only) or 0.55 mm (beam + rail, non-composite). MFG §02 check 2 has it right | **Low** | CALC §D.1 | Mislabelled result | Correct label |
| F-25 | Floor loading | Foot pressure computed on 50 × 50 (2500 mm²); modelled foot is Ø50 (1963 mm²): 331 kPa, not 260–272. Spreader pads (65 kPa) still resolve it | **Low** | CAD; CALC | Minor understatement | Correct at reissue |
| F-26 | Envelope | Phase-1 build depth 648 not derivable from the model (fans at Y 685 in both phases); RK-A-PARAM carries the 2 mm gap as unresolved | **Low** | CAD; DOC | Set-out uses 690 anyway | Derive 648 from a Phase-1 configuration or drop it |
| F-27 | Tier count claims | EDR-002 rules out a fifth tier; RK-A-DWG/MFG still state "structure takes 3 to 5", "uprights drilled for 5", and the roadmap offers 5-tier "now" | **Low** | DOC | Contradicts an accepted decision | Reconcile at reissue |
| F-28 | Document references | RK-A-MFG cites RK-A-QC Rev 2 (current Rev 3); RK-A-SYS uses P3 for T16; MFG/DWG cite a release path that does not exist (errata already recorded) | **Obs** | DOC | Naming lag only | — |
| F-29 | Sensing | "Leak puck in the base pan" — no base pan exists in model or BOM; 10_LEAK_SENSOR sits on the floor at Z 0–20 under the tundish | **Obs** | CAD | Detection is at floor level, which is acceptable | Correct wording |
| F-30 | Flood depth statement | "The crest sets the flood depth mechanically (22 mm)" — the crest is at 30 mm; 22 mm is set by the timed 14.5 L volume. The crest is a fault cap | **Obs** | DOC | Wording; no design impact | Clarify |
| F-31 | Mass model | Mass includes 4 plenums (16 kg), 8 fixture envelopes (9.8 kg at 1.23 kg each), 12 optional panels — a Phase-1 Grow rack without plenums/panels is ≈ 94 kg, and ≈ 84 kg if weighed without the separately-procured fixtures; T18 (112.7 ± 7 kg) would fail a correct Phase-1 build | **Medium** | CAD | Weighbridge test miscalibrated for the configuration actually built first | Publish per-configuration masses for T18 |
| F-32 | Fan / vibration | Beam first mode ≈ 13 Hz vs fan 33/233 Hz — agrees with check 10. Phase-1 fans are grid-mounted, so "off the structure" (SYS §05) is not true until Phase 2 | **Obs** | CALC | None | — |
| F-33 | Beam sizing | 30 × 30 × 1.5 long beam: 1.79 mm / 37.3 MPa at 80 kg, 0.85 mm at 38 kg — **confirmed**. Cross rails: 0.17 mm at 80 kg — confirmed adequate | **Obs** (pass) | CALC §D.1–D.2 | — | — |
| F-34 | Hydraulics — supply | Gravity head budget 2.66 m vs 0.33 m — arithmetic confirmed; DN40 orifice 30.7 L/min at 22 mm confirmed (but see F-07 for what governs) | **Obs** (pass) | CALC | — | — |
| F-35 | Ergonomics | NIOSH LI 0.50–0.76 confirmed reasonable; top tier clear height above bed to fixture underside 283 mm — tray + crop 139 mm passes | **Obs** (pass) | DOC; CAD | — | — |

---

## D. Simulation and verification results

### D.0 Method statement

Fusion Simulation was not run (see B.5). Every case below is an independent closed-form or matrix-stiffness calculation against v8 geometry, with material YST210 (fy 210 MPa, E 200 GPa) for GI sections, 6061 for the LED rail, and the model's own masses and CG. The Python script used is delivered alongside this report (`rack_review_calcs.py`) so every number can be re-run.

### D.1 LC-02/LC-03 — Tier beam bending and deflection (RK-A-102, two beams per tier, 1176 span, UDL)

| Load per tier | Deflection, beam only | Beam + deck rail (non-composite) | Stress | SF on yield |
|---|---|---|---|---|
| 22.5 kg (normal microgreens) | 0.50 mm | 0.32 mm | 10.5 MPa | 20 |
| 31.3 kg (aquatics) | 0.70 mm | — | 14.6 MPa | 14 |
| 38.0 kg (blocked drain, LC-03 service fault) | 0.85 mm | 0.55 mm | 17.7 MPa | 12 |
| 80.0 kg (rated) | 1.79 mm | 1.15 mm | 37.3 MPa | 5.6 |

Interpretation: agrees with RK-A-MFG check 1/2 to three figures; flatness ≤ 3 mm holds with margin. Cross rails RK-A-202 (510 span, 3 bays): 0.17 mm / 16 MPa at 80 kg. **Confidence: high.** Limitation: assumes UDL onto two beams; deck-to-beam bolt slip could unload the rail contribution — use "beam only".

### D.2 LC-01 — Empty rack, uprights (RK-A-101)

Per post: 649 N at service (112.66 + 4 × 38 kg), 1061 N at rated. Compressive stress 2.6 / 4.3 MPa.

| Effective length assumption | Pcr | SF at rated load |
|---|---|---|
| Le 400 mm (as documented) | 746 kN | 703 |
| Le 1950 mm (pinned–pinned, no sway) | 31.4 kN | 30 |
| Le 3600–3900 mm (sway frame, pinned feet) | 7.9–9.2 kN | 7.4–8.7 |

Interpretation: strength is not in question; the documented 1313 margin is an artefact of an effective length the depth plane does not provide. **Confidence: high** on the bounds, medium on which bound applies (depends on F-01).

### D.3 LC-05 / T16 — Depth-plane sway, semi-rigid frame model

Model: one Y–Z end frame (two uprights, pinned at the feet, continuous 40 × 40 × 1.6), base link at Z 165 (30 × 30 × 1.5), four tier links at the beam centrelines (2 × 25 × 25 × 1.5 cross rails), every link with identical rotational springs *k* at both ends (Monforton–Wu semi-rigid elements); half the test load applied at Z 1500, four posts sharing.

| Joint stiffness k (per joint) | Sway at 1500 mm, 200 N | 300 N |
|---|---|---|
| 1 kN·m/rad | 23.0 mm | 34.5 mm |
| 2.5 kN·m/rad (≈ T16 threshold) | 9.5 mm | 14.3 mm |
| 10 kN·m/rad | 2.8 mm | 4.1 mm |
| 100 kN·m/rad | 0.7 mm | 1.1 mm |
| Rigid | 0.5 mm | 0.7 mm |
| Reference: four fixed-base cantilevers, no links | 3.3 mm | 4.9 mm |

Interpretation: the rack passes T16 only if each bracket joint delivers ≳ 2.5 kN·m/rad *with no free play*. A 3 mm L-bracket with one M8 in the beam leg is, in rotation about the rack X-axis, a friction pin; the two-bolt post leg gives bearing stiffness only after ≈ 0.02 rad of clearance take-up (≈ 30 mm of free sway at the top bed). With the crushed-wall preload of F-03 the friction contribution is negligible. P-Δ at 30 mm sway with 265 kg adds ≈ 26 % to the sway moment. **Prediction: T16 fails as documented; residual set through slip is likely.** **Confidence: medium** — the joint stiffness is unknown (that is the finding); the frame model itself is verified against the rigid and cantilever bounds.

### D.4 LC-04 / LC-05 — Rigid-body tip-over (model CG X 640.7, Y 357.3, Z 930.4; feet at post centres)

| Mass state | Push toward rear | Push toward front | Push sideways |
|---|---|---|---|
| Dry, all systems (112.7 kg) | **135 N** | 249 N | 457 N |
| Structure only (62 kg, CG assumed central) | 105 N | 105 N | 252 N |
| Loaded 4 × 38 kg | 393 N | 507 N | 1074 N |
| Loaded + fixtures at spec 4 kg (287 kg) | 431 N | 545 N | 1164 N |
| Top tier only, 38 kg tray pulled 200 mm forward | 249 N | 263 N | 612 N |

Interpretation: confirms "anchors mandatory" and shows the governing direction is a *push toward the rear* (leaning on the front of a dry rack), because the rear-mounted systems put the dry CG 77 mm behind mid-depth. Sideways tip-over (the X-brace plane) is not critical. **Confidence: high** for the model mass state; the Phase-1 (no plenum) CG differs and was not computed because the configuration is not modelled.

### D.5 Width-plane sway with the X-brace

At 200 / 300 N: brace force 301 / 452 N, stress 4 / 6 MPa, elastic sway 0.05 / 0.08 mm; bolt bearing on the 3 mm flat 13 / 19 MPa. Hole-clearance slip alone can permit ≈ 3 mm sway before the brace engages. **Confidence: high** — provided the brace can actually be bolted (F-04).

### D.6 Joint strength (documented 2 × M8 per bracket, 196 N reaction)

Bolt shear and bearing margins (> 100) are confirmed as order of magnitude. **Confidence: high** for strength; **not applicable** to stiffness (D.3).

### D.7 Fastener preload vs tube wall (M8, 18 N·m)

Preload ≈ 11.3 kN (K = 0.2). Wall strip (36.8 mm span, 1.6 mm) reaches a plastic mechanism at ≈ 0.58 kN (≈ 0.9 N·m); 30 × 30 × 1.5 at 0.70 kN; 25 × 25 × 1.5 at 0.86 kN. **Confidence: high** (simple plastic strip model; real walls collapse progressively but at the same order).

### D.8 Overflow collar (weir over a Ø32 crest, Cd 0.6)

| Head over crest | 5 mm | 8 mm | 10 mm | 15 mm | 17 mm (rim) |
|---|---|---|---|---|---|
| DN32 capacity | 3.8 L/min | 7.6 | 10.7 | 19.6 | 23.7 |

Head for 7.2 L/min: 7.7 mm → level 37.7 mm, freeboard 9 mm. DN25 would need 9.1 mm. **Confidence: high** on physics, medium on Cd.

### D.9 Tray drain

Orifice DN40 at 22 mm: 30.7 L/min (confirmed). Valve pressure drop at 30.7 L/min: Kv 10 → 346 mm; Kv 20 → 86 mm; Kv 30 → 38 mm; Kv 50 → 14 mm, against ≈ 107 mm total available head at the valve. Drain rate is valve-governed; minimum-ΔP opening is the unresolved question. **Confidence: high** on the conclusion, low on the number until a valve is chosen.

### D.10 Seismic (IS 1893 Pt 1:2016 cl. 7.13, loaded rack, ground floor)

| Zone / component class | Coefficient | Overturning | Restoring (rear) | SF |
|---|---|---|---|---|
| Z 0.10 rigid / flexible | 0.020 / 0.050 | 48 / 120 N·m | 589 N·m | 12 / 4.9 |
| Z 0.16 rigid / flexible | 0.032 / 0.080 | 77 / 192 N·m | 589 N·m | 7.7 / 3.1 |

**Confidence: medium** (zone unresolved in the brief; anchors present in any case).

### D.11 Other

LED rail 20 × 20 × 1.5 Al, 2 / 4 kg fixture on hangers at 876 centres: 0.6 / 1.1 mm — acceptable. Beam first mode at 80 kg: 13.0 Hz — agrees with check 10. Foot pressure: 331 kPa on a Ø50 foot, 65 kPa on a 100 × 100 pad.

### D.12 Load cases not evaluated and why

Fatigue (no cyclic load of consequence at these stresses); thermal (LED junction model outside rack scope); CFD (explicitly deferred to T10 by the project — agreed); tolerance stack-up (no bracket geometry to stack — see F-02).

---

## E. Existing validation and QA review

**Assessment: Partially complete.**

What is good: the record is explicit about method weight and about what was not done (no FEA, no CFD, no stack-up); every finding has a correction and a verification method; the dependency map in RK-A-QC "Revision rule" is exactly the kind of artefact most projects lack; T18 (weigh the rack) is a smart low-cost check; the hydraulic and ergonomic arithmetic reproduces.

What is missing or questionable:

| Item | Status |
|---|---|
| Depth-plane frame check (NT-02, S1-O1) | Never performed; this review shows it *can* be bounded by analysis and that the bound is unfavourable (F-01) |
| Joint definition and joint stiffness | No coupon test, no detail, no model (F-02, F-03) |
| Interference check | Whitelist not recorded; brackets, bolts, rivets, foot inserts and LED fixings absent from the model so the check does not cover them (F-12) |
| Buckling check 3 | Invalid effective length (F-09) |
| Overflow capacity check 6 / T8 | Wrong flow regime; unattainable criterion (F-10) |
| Valve operability at gravity head | Not checked anywhere (F-07) |
| Air-gap verification at fill points | Documented as "by geometry" but geometry fails (F-06); only the tundish gap is on the physical-verification list |
| Tip-over basis | Result recorded, inputs not (F-19) |
| Seismic | Referenced, never recorded (F-21) |
| T16 criterion | Two versions (F-11) |
| Drain time criterion | Four versions (F-20) |
| T18 mass band | Calibrated to the full model, not the Phase-1 build (F-31) |
| Tolerance stack-up | Not done; cumulative ±0.2/400 mm grid tolerance is well specified but bracket/beam/deck stack is undefined |
| Traceability per case (design rev, CAD version, loads, BCs, criterion, limitation) | Present for VR-01…VR-10 in the index; absent inside RK-A-MFG §02 checks 1–15 (this is NT-02 as originally worded and it still stands) |

---

## F. Improvement opportunities (recommendations only — nothing applied)

### F.1 Required engineering corrections (before fabrication release)

1. **Define and model the beam-to-upright and deck-to-beam joints** (F-02), including crush tubes or inserts (F-03), and re-run interference with them present.
2. **Resolve depth-plane stability by design, not by test alone** (F-01, F-13): reinstate per-tier cross beams (already costed at ₹562) *or* add end-plane diagonals/knee plates *or* qualify the bracket joint by a moment–rotation coupon test and re-run the frame model. Then keep T16 as confirmation.
3. **Re-derive RK-A-104** from hole-to-hole geometry on the post centrelines; model two bars with holes and a crossing packer; reopen EDR-010 (F-04).
4. **Redesign the anchor interface** for the real 127 mm / 254 mm stand-offs and unify the anchor bolt size (F-05).
5. **Raise the fill nozzle** to a true air gap above the rim and record it as an ICR (F-06).
6. **Specify all eight valves** by Kv, minimum operating ΔP (= 0) and fail state technology, then recompute drain time and the T7/T15 criteria (F-07, F-20).
7. **Model the flood tray as the formed part** and cut both deck penetrations before any tooling quote; mark the R1 tray STEP as not-for-tooling (F-08, F-22).
8. **Correct the buckling and overflow calculations and the T8/T16 criteria** in the validation record (F-09, F-10, F-11).

### F.2 High-value improvements

- Levelling-foot insert part and detail (F-14).
- Flattened expanded metal specification and a single decision on flush vs on-top mesh (F-17).
- Modelled LED saddle/rail fixings and a top-tier rail mount; mass model at 4 kg fixtures (F-18).
- Drain provision for the sealed uprights; capped-and-drained beam ends (F-16).
- Per-configuration mass table for T18 and per-configuration tip-over (F-19, F-31).
- Record the interference whitelist as a controlled list with the next run (F-12).

### F.3 Manufacturing / cost optimisations (future, not for this revision)

- The keyhole beam-end and tabbed cross rail already on the roadmap would also *solve* F-02/F-03 if the keyhole is designed as a hook-in connector with defined moment capacity (this is how pallet racking achieves down-aisle stability without diagonals) — worth bringing forward rather than treating as a volume-only item.
- Three-rack nesting is already good; brackets and anchors on one 3 mm sheet (drop the 4 mm) removes a material line.
- Rivet-nuts in the uprights (Ø9 grid becomes M8 rivet-nut at the bracket positions only) delete flange nuts, crush tubes and the far-wall access problem at once.
- Foot spreader pads: make them part of the foot (moulded 100 × 100 base) rather than a loose pad.

### F.4 Platform improvements

- Publish the joint moment–rotation characteristic as a platform property; every future rack variant (germination, deep bed, 3-tier) inherits the same stability question.
- Freeze a rear stand-off dimension (rack rear face → wall / partner rack) as part of IF-RK-A-MEC so anchor, plenum and set-out are designed to one number (ND-03/ND-04 become one decision).
- Add the valve minimum-ΔP rule to the platform hydraulic standard: any gravity-operated valve is specified at ΔP-min = 0.
- Add "through-bolts in hollow sections require crush tubes or inserts" to the platform mechanical standard.

### F.5 Optional refinements

- Model the fixture envelope at the spec maximum, not a placeholder.
- Fold the rear panel/plenum optional parts into named configurations in Fusion so mass, CG and envelope per configuration are one query away.
- Move the T/RH node text to match the model (right end face, Z 1200–1280).
- Tidy the duplicated tier-drop segments.

---

## G. Open questions / missing information

1. What is the actual RK-A-107 bracket: geometry, hole positions, which upright face it bolts to, and how many per rack?
2. Which of the two T16 definitions is intended, and is the test to be run loaded, empty, or both?
3. Valve make/model for fill and drain — Kv, minimum ΔP, NO/NC construction, coil duty at 100 % during dwell?
4. Expanded mesh specification (pattern, flattened?) and the intended tray support condition.
5. Levelling-foot thread interface — insert, nut plate, or threaded end cap?
6. Intended rack-rear-to-wall stand-off in Phase 1 and Phase 2, and the anchoring detail for rows B/C.
7. Is the deck intended to be structural (bolted, tool required) or removable without tools? (Platform §5 must be honoured either way.)
8. Which mass state do the 139 N / 307 N tip-over figures and the T18 band refer to?
9. Has anyone confirmed a DN32 crest at 30 mm with a 47 mm rim is compatible with the thermoformer's draw ratio and 3 mm sheet (collar wall thinning)?
10. Seismic zone for Ooty (II or III) — immaterial to the verdict, material to the record.
11. LED fixture actual mass for the Ooty build (spec allows 4 kg; model carries 1.23 kg).

---

## H. Final engineering recommendation

Proceed through **Engineering Review → Controlled Revision → Prototype → Physical Load Testing → Pilot Grow Validation → Manufacturing Release**, with the following gates:

| Gate | Must be complete before |
|---|---|
| **G1 — Joint and stability definition** (F.1 items 1–3): joints modelled, crush tubes/inserts specified, depth-plane stability resolved by design or by coupon-qualified joint stiffness, brace re-derived | Any fabrication release |
| **G2 — Interfaces and safety invariants** (F.1 items 4–6): anchor stand-off, fill air gap, valve specification | Any fabrication release; ICRs issued for hydraulic and mechanical interfaces |
| **G3 — Model reissue** (F.1 item 7, F-12, F-17, F-18): tray as formed part, penetrations cut, brackets/fixings/inserts present, interference re-run with a recorded whitelist, R2 export with `ExportManager.execute()` checked | Drawing reissue (RK-A-DWG Rev 3) and ND-01 decision |
| **G4 — Validation record reissue** (F.1 item 8, F-19…F-21, F-31): corrected checks 3/5/6, single T16/T7/T8 criteria, per-configuration mass and tip-over | Prototype acceptance testing |
| **G5 — Prototype and physical tests**: T1–T18 as corrected, plus a bracket-joint moment–rotation coupon test and a blocked-fill/blocked-drain nozzle submersion check | Pilot grow |
| **G6 — Pilot grow**: T10 traverse feeding the plenum design (ND-03), leak/biofilm inspection of hollow sections after a wash cycle | Manufacturing release |

The rack is a good design that has been documented more honestly than most. The purpose of this review is to make sure that the first article tests the design and not the drawings.

---

*Read-only review. No Fusion design, drawing, BOM, specification, QA/QC document, validation record, decision record or project instruction was modified. Temporary Fusion access was limited to read-only API queries (component, mass, bounding-box, topology, parameter and interference reads) on `CEA_RACK_INTEGRATED_v2` v8; no study, body, parameter or occurrence was created or changed.*
