# AQ-LP-A — Validation Plan

**Status:** PROPOSED plan · **Date:** 2026-09-17 · **Nothing has been run.**
Acceptance criteria below are **proposals for owner and QA review**; several are relative to stock pipework because no absolute reference exists. Evidence tiers must not be blurred: desk research ≠ analysis ≠ prototype test ≠ validated design ≠ production-qualified product (QA agent rule).

---

## 1. Sequence and gates

| Stage | Purpose | Work | Exit evidence | Gate |
|---|---|---|---|---|
| **0A — Desk research** | Frame the opportunity | This folder | Complete 2026-09-17 | Owner reviews proposals |
| **0B — Pre-design validation** | Retire the assumptions that could invalidate the recommendation | V-C1–C7, V-M1–M3, V-T1 benchmark teardown, V-A1 sample scoring, V-S1 RFQs, V-S2 process samples, IP search started | Handoff checklist in [DECISIONS_AND_OPEN_QUESTIONS.md](../DECISIONS_AND_OPEN_QUESTIONS.md) §5 complete | **Design start** (owner decision; QA review optional) |
| **1 — Concept and prototype** | Prove function, safety, cleanability, appearance | Prototype rounds; V-T2–T10; V-A2–A3 started; V-P1 | Prototype test records against PR-* | **Prototype gate** (QA invoked) |
| **2 — Pilot** | Prove repeatability, cost, sell-through | 50–100-set pilot lot; first-article inspection; field feedback; V-A3 12-month board continues | FAI, yield, returns, customer feedback | **Launch gate** (QA invoked) |

## 2. Customer, channel and market validation

| ID | Activity | Sample | Questions / method | Decides |
|---|---|---|---|---|
| **V-C1** | Hobbyist interviews (planted-tank owners, shrimp keepers, premium scapers) | 12–15, Coimbatore/Chennai/Bengaluru + online; at least 5 who own stainless and 5 who own glass | Breakage count and moment (cleaning, hose removal, install, transit) in last 2 years; cost of a break; cleaning frequency, tools, chemicals (confirm whether citric acid or H₂O₂ are used), minutes per clean, hose removed each time; rimless or rimmed, glass thickness, mounting today, tilt; skimmer use, noise at night, air in canister, re-adjustment after top-offs; shrimp/fry losses and guard cleaning; rust seen; glass clarity vs durability trade-off; month-6 vs contest-photo priorities; where they buy; spares value | Target segment, first problem, O1 positioning, finish priorities |
| **V-C2** | Filter and hose survey | ≥50 responses via stores and community groups; photo of filter label + hose | Filter brand/model, hose label, measured hose ID/OD if possible, tank size and glass thickness | Pilot hose size (X3), compatibility chart scope |
| **V-C3** | Water-level habit survey | Within V-C2 | Daily/weekly evaporation estimate, top-up frequency, auto top-off use | P2 level-range requirement |
| **V-C4** | Willingness-to-pay test | Within V-C1 (Van Westendorp-style price questions plus a forced choice vs a ₹2,000 generic stainless pair and ₹3,999 Neo Flow Premium) | Too cheap / cheap / expensive / too expensive for a set that does not break, releases the hose easily, is shrimp-safe and cleans without hose removal | Price band (D-10) |
| **V-C5** | Retailer interviews | 5–8 specialist stores (online and physical) | Monthly unit sales by lily-pipe type and price band; stock turns; transit breakage rate and who absorbs it; return rate from size mismatch; top customer questions; dealer margin norms; consignment expectations; interest in stocking a Trophic set; minimum order | Volume scenarios, dealer margin, channel plan |
| **V-C6** | Pre-order / waitlist test (after IP filing decision, no design images before filing) | Landing page or community post with non-binding reservation | Conversion at a stated price band | WTP confirmation before pilot lot |
| **V-C7** | Maintenance-business interviews | 3–5 aquarium service businesses | Glass use or avoidance on client tanks; breakages per 100 visits; who pays; preferred material; volume per year | Whether the professional segment is real |

**Proposed acceptance for proceeding to design:** at least 8 of 12–15 hobbyists report one or more of breakage, hose-removal stress or cleaning burden as a current problem; the median "expensive but acceptable" price is ≥ ₹3,499; at least 3 retailers express conditional interest at a dealer margin ≤ 40 %; one hose size covers ≥ 60 % of surveyed filters.

## 3. Measurements and bench tests

### 3.1 Measurements before design

| ID | Measurement | Method | Output |
|---|---|---|---|
| **V-M1** | Hose calliper survey | Buy or borrow hoses/fittings for the filters surfaced by V-C2 (expected: Sunsun HW-30x/40x, Eheim Classic, Oase BioMaster, JBL e-series, Fluval x07; also Hygger, Aqueon, Resun if found) — hose ID, OD, wall, hardness (Shore A if a gauge is available), stiffness at 15 °C and 30 °C | Measured compatibility table replacing [sources/hose_compatibility.csv](../../../../docs/references/lily-pipes/sources/hose_compatibility.csv) labels |
| **V-M2** | Clearance survey | Measure lid gaps, light leg positions (including Trophic `AQ-LT-*` concepts when available), rear wall gaps and cabinet cut-outs on 5–10 real installations | Clearance envelope for design |
| **V-M3** | Glass thickness survey | Coimbatore/Bengaluru tank builders and stores: glass thickness by tank size, rimless vs rimmed share, edge finish | Supported glass range (PR-CP-04) |

### 3.2 Bench and rig tests

| ID | Test | Setup and procedure (outline) | Proposed acceptance criterion (for review) | Requirement |
|---|---|---|---|---|
| **V-T1** | Benchmark teardown | 6–8 purchased sets: measure pipe OD/bore/wall, slot width and open area, bend quality, welds; PMI (XRF service) on stainless; ferroxyl free-iron test; pack drop observation | Record only; establishes the bar and grade reality | Informs all |
| **V-T2** | Hose retention and removal | Force gauge; each measured hose on prototype ends at 15 °C and 30 °C; pull-off force, fit force; 50 remove/refit cycles; creep: pressurised loop 14 days with position marks | Pull-off force ≥ that of the stock filter pipework with the same hose at each temperature; no visible creep movement over 14 days; no damage after cycles | PR-SV-02, PR-SV-03 |
| **V-T3** | Flow and pressure loss | Loop with two canisters (one 12/16, one 16/22 as chosen), inline flow meter, water-column differential taps; compare stock pipework vs prototype across clean and loaded media; vary hose length | Installed flow with prototype ≥ 95 % of flow with stock pipework at the same state; supported flow range stated per size | PR-FN-01, PR-FN-06 |
| **V-T4** | Skimmer window (P2 only) | Same loop; 300–1500 l/h in steps; clean and clogged bottom intake; ±level steps; video float behaviour; air trap at canister | No bouncing or air ingestion across the stated window; tolerates the level range from V-C3 without adjustment | PR-P2-01/02 |
| **V-T5** | Intake: clog and livestock | Standard debris dose (leaf fragments + fine detritus, defined recipe) over 14 days, flow logged; live Neocaridina juveniles (≥20, 1–3 mm) in a test tank at maximum supported flow for 7 days; count entrapped or passed (sponge-free canister inlet check) | Flow ≥ 80 % of clean after 14 days; zero juveniles entrapped or passed; no trap gaps found in inspection | PR-LS-01–03 |
| **V-T6** | Cleaning and service | 5 hobbyists clean and refit prototype vs their stock/glass set; time, brush reach (every internal surface visible after brushing), errors on refit; joints leak/aim check after 50 cycles | Clean-and-refit time ≤ stock; 100 % internal surface reached; no refit errors; no leaks or aim change | PR-SV-01, 04, 05 |
| **V-T7** | Corrosion and finish durability | Coupons and prototypes: A967 verification (ferroxyl / copper sulfate as applicable); 90-day immersion in (a) CO₂-acidified soft water, pH ≈6.3–6.6, (b) hard Coimbatore tap water; 12 cleaning cycles with the proposed care method; marked and unmarked areas; PMI per lot | No rust, pitting or tea staining visible at 30 cm; verification tests pass; marked areas unchanged | PR-MT-01–04, 06 |
| **V-T8** | Mount hold and glass safety | Minimum and maximum supported glass thickness, rimless and rimmed coupons; hose loaded with water-filled hose; 30 days; 100 fit/remove cycles; inspect edge under magnification | No slip; tilt change ≤ 2°; no chips, scratches or marks on glass edge | PR-MO-01, 02 |
| **V-T9** | Gas exchange and surface action | Reference 60 cm planted tank; outlet at 2–3 depths/angles; log pH (CO₂ on, fixed rate), drop checker, optional DO meter; observe surface film clearance | Recommended position achieves surface film clearance with pH drop within 0.1 of the best tested alternative; adjustment covers both CO₂ and non-CO₂ use | PR-FN-02, 03 |
| **V-T10** | Noise and air | Quiet room, sound meter at 1 m: stock vs prototype; restart after power cut and after water change; check for air pocket in canister | No audible splash/air noise; ≤ 3 dB(A) above stock pipework; no air accumulation after restart | PR-FN-04, 05 |

## 4. Appearance validation (CMF-owned, QA acceptance)

| ID | Activity | Method | Proposed acceptance |
|---|---|---|---|
| **V-A1** | Physical scoring of references and prototypes | Score ~7 reference sets and each prototype with the C1–C12 rubric ([LILY_PIPE_AESTHETIC_REFERENCE.md](../../../../docs/references/lily-pipes/LILY_PIPE_AESTHETIC_REFERENCE.md) §2), two scorers minimum, new and aged | Prototype weighted score exceeds best stainless reference; no criterion at 1; anti-mimicry check passed |
| **V-A2** | Photo protocol | Three scape types (bright iwagumi, dark jungle, nature style) × white/black background; reference LEDs incl. Trophic `AQ-LT-*` when available; full-tank, 45°, top-down, macro; clear vs tinted hose at month 3; blind preference panel (≥10 hobbyists) vs generic stainless and glass | C3 ≥ 4 in ≥ 2 of 3 scapes; C12 ≥ 4; prototype preferred over generic stainless by a majority of panel |
| **V-A3** | Ageing board | Finish candidates on coupons and prototypes; 1, 3, 12 months of simulated maintenance (brush cycles, clip cycles, hard-water scale, CO₂ water); adhesion (cross-hatch) and chip inspection for any coating; leach check (specialist lab) before any coated part touches livestock | Weighted new-vs-aged gap ≤ 3; no failure-looking wear; coating adhesion and leach pass before proposal |

## 5. Supplier and cost validation

| ID | Activity | Output | Proposed acceptance |
|---|---|---|---|
| **V-S1** | RFQs (lists in [SOURCING_STRATEGY.md](../sourcing/SOURCING_STRATEGY.md) §6) to ≥2 suppliers per process step | Quotes at 25/50/100/200 with setup charges, tooling and lead time | Replace EST lines in the model; quoted 100-set cost supports positive dealer contribution at the approved price (PR-MF-03) |
| **V-S2** | Process samples | Bend, laser slot, end-form and passivation samples on candidate tube; PVD coupons if a dark finish is pursued | Bends without wrinkling or visible ovality; slot edges burr-free inside; passivation verification pass |
| **V-S3** | Supplier qualification (pilot stage) | Site visit, FAI, capability on critical characteristics, MTC chain | Status moves from `sample required` to `qualification required` — never "approved" without evidence |

## 6. Packaging

| ID | Activity | Method | Proposed acceptance |
|---|---|---|---|
| **V-P1** | Transit test | ISTA-style parcel drop and vibration sequence (confirm the appropriate ISTA procedure with a lab), plus 10 real courier shipments to three zones | No finish damage, no deformation; volumetric weight within the courier slab assumed in the cost model |

## 7. Test equipment and budget classes (EST)

| Equipment | Use | Estimate |
|---|---|---|
| Two canister filters matching the pilot hose sizes (models from V-C2) | V-T3, T4, T10 | Included in ₹30–80k rig line |
| Inline flow meter, water-column differential tubes, valves, hose set | V-T3, T4 | Rig line |
| Digital force gauge, calliper, thermometer, cold/warm water baths | V-M1, V-T2 | ₹5–15k |
| Sound level meter | V-T10 | ₹2–6k |
| pH logger or controller, drop checker; optional DO meter | V-T9 | ₹5–20k |
| Test tanks (60 cm rimless 6 mm; glass coupons across thickness range) | V-T5, T8, T9 | ₹10–25k |
| Neocaridina colony, debris recipe | V-T5 | ₹2–5k |
| Ferroxyl/copper sulfate kits; external PMI (XRF) service; coating adhesion kit | V-T1, T7, A3 | In ₹15–60k lab line |
| Camera, reference LEDs, backgrounds | V-A2 | Existing where possible |

These fold into the fixed-cost lines in [COMMERCIAL_FEASIBILITY.md](../costing/COMMERCIAL_FEASIBILITY.md) §7.

## 8. Claims that must not be made until evidence exists

Grade (needs MTC + PMI), "shrimp safe" (V-T5), compatibility with a named filter (V-M1 + V-T2), flow figures (V-T3), "rust-free"/durability (V-T7), "silent" (V-T10), ageing or "looks new after a year" (V-A3). Untested hand calculations in [LILY_PIPE_TECHNICAL_REFERENCE.md](../../../../docs/references/lily-pipes/LILY_PIPE_TECHNICAL_REFERENCE.md) are not performance claims.
