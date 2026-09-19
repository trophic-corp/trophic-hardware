# AQ-LP-A — Decision Brief, Open Decisions and Design Handoff

**Status:** every recommendation is **PROPOSED — awaiting owner approval.** Nothing here has been entered in `docs/decisions/DECISION_REGISTER.md`; records are written only when the owner decides.
**Date:** 2026-09-17

---

## 1. Decision brief

### 1.1 Is this category worth pursuing for Trophic?

**Proposed answer: yes, to Stage 0B (pre-design validation), with a modest cash exposure of ≈₹1.25–3.3 lakh before any tooling, IP filing or inventory.** Reasons:

- The recurring customer problems are real, specific and already cost money: glass breakage, hose-removal stress, the cleaning chore, skimmer air/noise and shrimp entrapment each have four or more independent sources ([COMPETITOR_LILY_PIPE_REFERENCE.md](../../../docs/references/lily-pipes/COMPETITOR_LILY_PIPE_REFERENCE.md) §4).
- The Indian market is served entirely by imports with thin specifications, unstated warranties, contradictory grade claims and unreliable premium availability (§5). No Indian manufacturer was found.
- Stainless steel has won on durability but has no design language of its own — a credible opening for Trophic's "evidence of care" direction ([LILY_PIPE_AESTHETIC_REFERENCE.md](../../../docs/references/lily-pipes/LILY_PIPE_AESTHETIC_REFERENCE.md) §3, §5).
- The best route uses processes available in Tamil Nadu without moulds, so inventory and capital stay small ([SOURCING_STRATEGY.md](sourcing/SOURCING_STRATEGY.md) §2).

Honest limits: it is a **brand-building, low-capital line, not a large profit engine** — base break-even ≈340 sets direct or ≈770 through dealers ([COMMERCIAL_FEASIBILITY.md](costing/COMMERCIAL_FEASIBILITY.md) §7), and the repository's sequencing puts aquarium products after the microgreen rollout. Whether to start 0B now is the owner's call (D-17).

### 1.2 Which customer problem should we address first?

**Proposed:** the **handling problem of the dedicated planted-tank hobbyist** — hardware that survives removal and cleaning without breaking, releases and retains the hose without drama, lets every wetted surface be brushed, keeps juvenile shrimp out without an add-on guard, and still looks cared-for at month 6–12. Skimmer noise/air is the next problem (P2), deliberately deferred because it carries the highest engineering risk.

### 1.3 Strongest initial product hypothesis and manufacturing route

**Proposed P1:** a **serviceable stainless inflow + outflow set** in one hose size and one finish, with a Trophic rimless-glass clip designed with the pipe, a retained hose interface with a resolved rim crossing, a removable/brushable shrimp-conscious intake, a termination derived from its flow job, a reserved skimmer interface, and a published measured compatibility chart.

**Route:** 316L stainless tube (grade to confirm, D-05), one-piece CNC mandrel-bent where possible to avoid wetted welds, tube-laser slots, end-formed termination and hose beads, degreased and passivated/electropolished, via Tamil Nadu job-work (Chennai bending/end-forming; Coimbatore/Chennai laser, finishing). Design-and-source, not in-house fabrication. Glass and private-label import are not proposed.

### 1.4 Credible prototype and launch investment ranges (EST, no quotes)

| Stage | Range | Base |
|---|---|---|
| Prototype stage: samples, rig, three prototype rounds, lab tests | ₹1.25–3.3 lakh | ≈₹2.2 lakh |
| P1 launch: all fixed costs (incl. tooling/fixtures, IP, packaging, compliance, content) + first 100-set lot | ₹3.1–10.3 lakh | ≈₹6.0 lakh |
| P2 skimmer later | ₹1.0–3.6 lakh | — |

Unit cost for P1 (EST): ≈₹2,030 per set at 25, ≈₹1,190 at 100, ≈₹1,040 at 200 (base). Proposed MRP test band ₹3,499–4,499.

### 1.5 Assumptions that could invalidate the recommendation

| # | Assumption | If false | How it is tested |
|---|---|---|---|
| X-1 | Hobbyists will pay ≈₹3,500–4,500 for a non-skimmer stainless set when generic stainless sets with skimmers cost ₹2,800–4,000 | P1 becomes a low-margin commodity; dealer channel negative | V-C4, V-C6 |
| X-2 | A stainless product can achieve "considered presence" in nature scapes (not "industrial/distracting") | Differentiation collapses to function only; premium price unsupported | V-A1, V-A2 panel |
| X-3 | Tamil Nadu job-work delivers thin-wall small-OD bends, clean slots and passivation at ≈₹1,000–1,500 per set at 100 units | COGS × 1.3 halves dealer contribution; adverse case never breaks even | V-S1, V-S2 |
| X-4 | One hose size covers most of the target Indian installed base | Two SKUs double inventory and development at launch | V-C2, V-M1 |
| X-5 | Breakage/handling problems are as common among Indian hobbyists as in UK/Singapore forums | First-problem choice weakens | V-C1 |
| X-6 | A finish exists that ages honestly **and** passes hygiene/livestock tests | Either bright steel (aesthetic risk) or coating risk (safety/appearance risk) | V-T7, V-A3 |
| X-7 | No live design registration or patent blocks the intended forms in India | Redesign or legal cost | IP attorney FTO |
| X-8 | Dealer margins ≤ ≈40 % without a distributor layer | Dealer channel marginal or negative | V-C5 |
| X-9 | Customer acquisition can stay under ≈₹600 per set via community and content | DTC contribution erodes | Pilot tracking |

### 1.6 What must be verified before design starts

Complete the Stage 0B checklist in §5. In short: hobbyist and retailer interviews; the filter/hose survey and calliper measurements; glass-thickness and clearance surveys; benchmark teardown with PMI; supplier RFQs and process samples for the stainless route; confirmation of the stainless tube QCO status; an IP freedom-to-operate search started; owner decisions D-02 to D-05, D-08 and D-10 at least provisionally made.

---

## 2. Recommendations (all PROPOSED)

| ID | Recommendation | Basis | Status |
|---|---|---|---|
| RC-1 | Proceed to Stage 0B for `AQ-LP-A` | §1.1 | PROPOSED |
| RC-2 | First product P1 serviceable stainless set; one hose size, one finish | Commercial §2; Aesthetic ref §5 | PROPOSED |
| RC-3 | P2 skimmer only after rig and appearance gates; P3 clip/guard kit only after P1 establishes the clip | Commercial §2; CMF review | PROPOSED |
| RC-4 | Do not pursue glass or private-label import as a first product; buy both as benchmarks | Sourcing §2; Commercial §5 | PROPOSED |
| RC-5 | Route (b) stainless via Tamil Nadu job-work; no moulds at launch | Sourcing §7 | PROPOSED |
| RC-6 | DTC-led launch with 3–5 specialist dealers at a fixed margin; no distributor tier; Amazon.in later | Commercial §8 | PROPOSED |
| RC-7 | File design protection decision and FTO before any public reveal (including pre-order pages with design images) | Sourcing §8 | PROPOSED |
| RC-8 | Make only evidence-backed claims; publish a measured compatibility chart and plain warranty | Competitor ref §5–6; Requirements §11 | PROPOSED |

## 3. Open decisions

| ID | Decision | Options | Recommendation | Depends on | Blocks | Status |
|---|---|---|---|---|---|---|
| D-01 | Pursue the category to Stage 0B | Yes / defer | Yes (RC-1) | Owner sequencing (D-17) | Everything | PROPOSED |
| D-02 | Primary material route (supersedes `PRODUCT.md` decision 1 "glass or acrylic") | Stainless / glass / polymer | Stainless → owner approved stainless | V-C1, V-A2 panel | Process, supplier, cost, form | **DECIDED 2026-09-17 — [EDR-021](../../../docs/decisions/records/EDR-021-lily-pipe-material-316l-with-304-alternate.md)** |
| D-03 | First product scope | P1 / P1+P2 / P3 first | P1 | V-C1, V-C4 | Requirements scope | PROPOSED |
| D-04 | Pilot hose size (cross-product **X3**) | 12/16 / 16/22 / both | **16/22 provisional** (Sunsun HW-302 class is the in-stock Indian value canister; launch spec §3); confirm with data → owner approved 16/22; V-C2 can still supersede | V-C2, V-M1 | Every dimension | **DECIDED 2026-09-17 — [EDR-022](../../../docs/decisions/records/EDR-022-lily-pipe-hose-size-16-22.md)** |
| D-05 | Stainless grade | 316L / 304 | 316L (margin at low material cost; an earlier owner discussion assumed 304 — both views preserved until V-T7 and quotes) → owner: 316L specified, **304 as qualified alternate** (both kept; V-T7 must cover both) | V-T7, V-S1 | MTC, claims | **DECIDED 2026-09-17 — [EDR-021](../../../docs/decisions/records/EDR-021-lily-pipe-material-316l-with-304-alternate.md)** |
| D-06 | Supported glass thickness range; rimmed-tank support | Ranges / variants / adjustable | **5–12 mm via two pad ranges; rimless only at launch** (provisional, launch spec L-05/L-06) → owner approved rimless 5–12 mm, rimmed excluded (pad-range method stays a design choice) | V-M3, V-T8 | Clip design (`PRODUCT.md` decision 3) | **DECIDED 2026-09-17 — [EDR-023](../../../docs/decisions/records/EDR-023-lily-pipe-rimless-glass-5-12mm.md)** |
| D-07 | Finish family for wetted parts | Passivated natural, bead-blast, electropolish, dark PVD, other | **Through-material low-gloss satin, passivated, at launch** (provisional, launch spec L-43); dark PVD only after tests | V-T7, V-A3, Bio/QA limits | PR-AE-10, cost | OPEN |
| D-08 | Primary recognition cue | Clip / rim collar / termination | **Clip as candidate** (launch spec L-65); CMF to confirm in design | Design phase | Form language | OPEN |
| D-09 | Does Trophic specify or supply hose? | Supply / specify / neither | **Specify, do not supply, at launch** (provisional, launch spec §3) | V-A2 month-3 photos, cost | Rim crossing (PR-AE-05) | OPEN |
| D-10 | Retail price band | ₹3,499 / ₹3,999 / ₹4,499 … | **₹3,999 launch, test ₹3,499–4,499** (provisional, launch spec L-100) | V-C4, V-C6, V-S1 | Channel economics | OPEN |
| D-11 | Launch channels | DTC / dealers / marketplace mix | RC-6 | V-C5 | Pack, pricing | PROPOSED |
| D-12 | Manufacture: in-house vs design-and-source (`PRODUCT.md` decision 5) | — | Design-and-source, Tamil Nadu job-work | V-S1, V-S2 | Supplier plan | PROPOSED |
| D-13 | Packaging approach (`PRODUCT.md` decision 6) | — | Board/pulp tool-case, no foam, volume-minimised; transit-tested | V-P1 | Cost | PROPOSED (direction) |
| D-14 | IP strategy | FTO + design filing before reveal / none | RC-7 | Attorney | Any public disclosure | PROPOSED |
| D-15 | P2 skimmer timing | With P1 / after gates / never | After gates | V-T4, PR-P2-* | P2 inventory | **Closed by ADR-009 (2026-09-19): separate P2 product, not with P1** |
| D-16 | P3 accessory sequencing | Before / after P1 | After P1 (CMF view adopted) | P1 launch | — | PROPOSED |
| D-17 | When to start Stage 0B relative to the CEA microgreen rollout | Now / after rollout milestone | Owner | Company priorities | D-01 | OPEN — owner |
| D-18 | Termination formed from the tube vs separate joined part | Formed / joined | Not a CMF decision; Manufacturing + Systems to evaluate with V-S2 samples | V-S2, V-T3 | Appearance of termination; wetted-weld rule | OPEN (flagged conflict) |
| D-19 | Fastener rule for wet parts | Dark fasteners (lights rule) / no wet fasteners | Likely "no fasteners in water"; to confirm | Mfg/QA corrosion review | PR-MO-03, PR-AE-03 | OPEN (flagged conflict) |
| D-20 | Concept round-1 direction to carry forward (Q1) | r1a pipe crosses rim / r1b hose crosses rim / both | r1a built and reviewed 2026-09-17 (brush access fails at the 180° hook; clip below waterline) → owner: **build r1b before choosing** | r1b concept | Round 2 form | **OWNER 2026-09-18 — r1b to be built first; choice deferred** |
| D-21 | Outflow reach target L-21 vs bend rules M2/M3 | Relax L-21 / turn nozzle along glass / shorten `straight_min` | r1a shows 90–94 mm at `clr` = `straight_min` = 1.5 × OD | V-T9, V-S2 | Outflow form | **OWNER 2026-09-18 — L-21 target relaxed to 70–100 mm (target change, launch spec Rev P0 row updated; still PROPOSED until V-T9)** |
| D-22 | How the r1a hook seats on the rim | Rests on clip saddle / air gap / flat between bends | 3 mm apex gap touches the saddle corners | V-T8 | Clip load path | **OWNER 2026-09-18 — hook rests on the clip saddle; `bridge_clear` = `clip_t`; saddle carries the pipe** |
| D-23 | Clip grip principle | Flat collar tab / formed V-jaw / wrap | Collar tab modelled in r1a; one blank, one bend axis | V-T8 | D-08 | **OWNER 2026-09-18 — develop the collar tab; round 2 adds a real spring/friction detail** |
| D-24 | Round-2 form after the r1a/r1b comparison | (a) r1b straight pipe + formed stainless hose guide on the J-clip saddle · (b) r1a hook with `bridge_len` 10 mm, cap as brush entry, flexible brush accepted · (c) other | Neither round-1 direction as drawn (r1b report §5) | **V-M1 hose kink radius, V-S2 bend samples** | Round-2 CAD, D-08, D-09 | **OWNER 2026-09-19 — (a) r1b pipe + formed hose guide; swivel at the hose end. Built as `AQ-LP-A_CONCEPT_r2a` (v3)** |
| D-25 | Independent nozzle aim by a swivel joint | Wetted swivel (elbow / hose end) / dry two-part joint above the waterline / no joint (nozzle pitch + collar yaw) | Specialists (2026-09-18, [review](design/SPECIALIST_REVIEW_2026-09-18_swivel-intake-skimmer.md) §1): **never wetted**; dry above-rim coupling makeable in Coimbatore at +₹280–480/set @100; test nozzle-form + collar first | Turned-pair sample, 50-cycle leak test, CMF review | M1/L-51 wording; round-2 form | **DECIDED 2026-09-19 — [EDR-024](../../../docs/decisions/records/EDR-024-lily-pipe-outflow-swivel-above-waterline.md): dry swivel above the waterline, formed socket first; no joint below the waterline** |
| D-26 | Adjustable intake | Rotating/sliding sleeve / stepped end caps / hose-end valve / none | Specialists: sleeves rejected (crevice, brush path, tolerance, galling); **stepped end caps** +₹90–180/set @100 if wanted; demand unverified | Laser ovality RFQ; interviews V-C3 | L-30/31/34, M8 | **CLOSED 2026-09-19 — owner withdrew EDR-025 the same day; no adjustable intake in P1; plain removable cap (r2b)** |
| D-27 | Surface skimmer in P1, and whether to reserve its interface now (supersedes D-15 timing) | Integrated / modular on reserved interface / separate later | Both specialists: **not integrated in P1** (+₹780–1,020/set incl. test, V-T4 becomes a P1 gate). Disagreement preserved: Systems — reserve a minimum envelope now (ICR); Manufacturing — defer, a reserved feature taxes every P1 set | V-C3 interviews; D-24 pipe form; POM float samples + 20-unit flow trial | PR-SC-02, packaging, price | **DECIDED 2026-09-19 — [ADR-009](../../../docs/decisions/records/ADR-009-lily-pipe-no-skimmer-in-p1.md): no skimmer in P1, no reserved interface; Systems view preserved in the record** |
| D-28 | Hose loop over the rim: guided by a Trophic part, or left to a specified hose | Separate guide (r2a, rejected by CMF as ornament) / low rest folded into the clip (not provable as one blank in CAD) / no guide, hose specified with a minimum bend radius | r2b: no guide; loop shape and height (~74 mm above rim at R30) belong to the hose spec | V-M1 hose kink radius; V-M2 lid/light-leg clearances | D-09, L-07 scope | OPEN — owner after V-M1/V-M2 |
| D-29 | Primary recognition cue (D-08 narrowed by CMF review 2026-09-19) | Clip as one folded stainless line / socket step / termination | CMF: the clip; quieten socket (one step), slots (one band), nozzle, cap | Appearance review C1–C12 on samples (V-A1) | Form language | PROPOSED (CMF) |

**Mapping to `PRODUCT.md` §5:** decision 1 → D-02; 2 → D-04; 3 → D-06; 4 (outflow forms) → D-08/D-18 plus PR-FN-03; 5 → D-12; 6 → D-13.

## 4. Preserved disagreements and uncertainties

- **P3 timing:** Main Claude's first synthesis offered a clip/guard kit as an early low-inventory option; the CMF specialist disagreed (dilutes the signature clip). The CMF view is adopted in D-16, and a clip prototype may still be used as research.
- **SS grade:** earlier owner-side work named SS304 as the default; this research proposes 316L. Not averaged — resolved by quotes and V-T7.
- **Glass:** not proposed, but the CMF specialist asks that "a non-metal where it earns its place" stay open for future accessories.
- **Transparency vs considered presence:** depends on the size of the contest-photo segment (V-C1). If that segment dominates the target, RC-2 must be revisited rather than compromised.

## 5. Design-phase handoff checklist (Stage 0B exit)

Tick each item with a link to its evidence before **design-class** work (drawings, tooling, DESIGN-class CAD) starts. **2026-09-17:** the owner answered decisions 1–3, which unblocks **CONCEPT-class** CAD only ([CONCEPT_DESIGN_BRIEF.md](design/CONCEPT_DESIGN_BRIEF.md)); the rest of this checklist still gates design.

**Owner decisions**

- [ ] D-01 proceed and D-17 timing decided
- [x] D-02 material route approved — stainless (EDR-021, 2026-09-17)
- [ ] D-03 first product scope approved
- [x] D-04 hose size decided — 16/22 (EDR-022, 2026-09-17); V-C2/V-M1 still to confirm
- [x] D-05 grade decided — 316L, 304 alternate (EDR-021)
- [x] D-06 glass range decided — rimless 5–12 mm (EDR-023)
- [ ] D-10 price band decided provisionally
- [ ] D-11 channel plan and D-12 make/source approach approved
- [ ] PRELIMINARY_REQUIREMENTS reviewed; each PR-* marked approved, changed or rejected
- [ ] D-08 recognition-cue question and D-09 hose question framed for the design phase (answers may come in design)

**Measurements**

- [ ] V-M1 hose calliper table for the filters found in V-C2
- [ ] V-M2 clearance survey (lids, light legs incl. `AQ-LT-*` concepts, rear walls, cabinet cut-outs)
- [ ] V-M3 glass thickness and rimless/rimmed share from builders and stores
- [ ] V-T1 benchmark teardown: OD, bore, wall, slot width and open area, welds, PMI grade, free-iron test

**Customer and channel evidence**

- [ ] V-C1 12–15 hobbyist interviews synthesised (problem frequencies, month-6 vs contest priorities)
- [ ] V-C2/V-C3 filter, hose and top-up survey (≥50)
- [ ] V-C4 willingness-to-pay results
- [ ] V-C5 5–8 retailer interviews (sales, returns, breakage, margins, consignment)
- [ ] V-C7 3–5 maintenance businesses
- [ ] Proceed criteria in VALIDATION_PLAN §2 met, or the recommendation revised

**Supplier confirmations**

- [ ] V-S1 quotes from ≥2 suppliers per process step at 25/50/100/200, including setup, tooling and lead time
- [ ] V-S2 process samples: thin-wall bends, internal slot quality, end-formed termination and beads, passivation verification
- [ ] Confirmation that 316L (or chosen grade) small-OD thin-wall tube with 3.1 MTC is obtainable in small quantities
- [ ] Current status of the stainless pipes and tubes QCO confirmed
- [ ] PVD/dark-finish coupons ordered only if D-07 keeps a dark option
- [ ] Cost model re-run with quotes; PR-MF-03 checked

**Aesthetic preparation**

- [ ] V-A1 reference sets bought and scored physically with the rubric
- [ ] V-A2 photo protocol and panel defined; V-A3 ageing board started on candidate finish coupons
- [ ] Anti-mimicry checklist agreed (AESTHETIC REF §6 Q9)
- [ ] QA/Bio limits for surface roughness, passivation and coating safety set before finish exploration

**Compliance and IP**

- [ ] IP attorney FTO search commissioned; design-filing plan agreed before any public reveal
- [ ] Legal Metrology labelling and e-commerce declarations reviewed
- [ ] Claim policy (PR-CL-01) accepted
- [ ] Trophic trade-mark question (cross-product) progressed

**Validation readiness**

- [ ] Rig built (two canisters, flow meter, differential taps) and shake-down run with stock pipework
- [ ] Shrimp test colony and debris recipe ready
- [ ] QA review of proposed acceptance criteria in VALIDATION_PLAN §3 (gate role)
