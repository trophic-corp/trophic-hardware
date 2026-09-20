# AQ-LP-A — Proposed Launch Specification (Rev P0)

| | |
|---|---|
| **Document** | Proposed launch specification for the first lily-pipe product (P1) |
| **Revision** | **P0 — proposal, 2026-09-17** |
| **Stage** | Phase 0 (0A research complete; 0B validation not started) |
| **Status** | **PROPOSED — not approved, not frozen, not for drawings, tooling, RFQ commitment or marketing** |
| **Owner of approval** | Karthik |
| **Supersedes** | Nothing. Adds provisional values to the PROPOSED requirements in [PRELIMINARY_REQUIREMENTS.md](PRELIMINARY_REQUIREMENTS.md) |

## Approval status of rows (updated 2026-09-17)

| Rows | Status | Record |
|---|---|---|
| L-02 hose 16/22 | **APPROVED by owner** | EDR-022 |
| L-05 glass 5–12 mm; L-06 rimless only | **APPROVED by owner** | EDR-023 |
| L-40 tube grade | **APPROVED by owner as 316L specified, 304 qualified alternate** (design must be grade-independent) | EDR-021 |
| All other rows | PROPOSED — targets for CONCEPT CAD and Stage 0B, not decisions | — |

## How to read this document

- The owner asked for a concrete recommendation of what to launch. This document gives one, with numbers, so the design phase has **starting targets** and Stage 0B knows exactly what to test.
- Every value carries its **basis** (sourced fact, market reference, function-derived estimate, or planning assumption), a **confidence**, and the **check that confirms or changes it** (IDs in [VALIDATION_PLAN.md](../verification/VALIDATION_PLAN.md)).
- `CLAUDE.md` §3 still applies. Market reference points inform these values but are not Trophic decisions. **No value here may appear on a drawing or in a model described as a design until the owner approves this document at a later revision (P1 or later) after Stage 0B evidence.** Before that, a model built from it is class ENVELOPE or CONCEPT only (`docs/system/CAD_SEED_GUIDE.md`).
- Nothing here copies a competitor's form. Lengths and depths are derived from tank geometry and function, not taken from a competitor product.

---

## 1. The proposed launch product in one paragraph

A **matched stainless-steel inflow + outflow set for 16/22 mm canister-filter hose**, sized for **rimless planted tanks of 60–90 cm length and 35–45 cm height with 5–12 mm glass**. Both pipes are **one-piece bent 316L tube with no welds in the water**, passivated, in **one low-gloss, through-material satin finish**. They mount with a **Trophic stainless clip with replaceable soft pads — no suction cups, no fasteners in water** — which lets the user adjust height and aim. The inflow has a **fine slotted intake with a removable end cap**, so a brush can pass through the whole pipe without removing the hose. The outflow ends in a **formed, directional nozzle** meant to create a surface current rather than splash. The set ships with a cleaning brush, spare pads and a measured compatibility and care card, in a foam-free board pack. **One SKU, one finish, no skimmer**; the skimmer (P2) and a 12/16 size follow later.

## 2. Specification at a glance

| Area | Proposed launch value | Confidence |
|---|---|---|
| SKU | One set: inflow + outflow + 2 clips, 16/22 hose size | Medium |
| Target installation | Rimless glass tanks, 60–90 cm long, 35–45 cm tall, 5–12 mm glass, canister filter rated ≈800–1,500 l/h with 16/22 hose | Medium |
| Supported installed flow | 400–1,000 l/h | Low — needs rig |
| Material | 316L stainless tube, 17 mm OD × 1.0–1.2 mm wall, EN 10204 3.1 certificate | Medium |
| Construction | One-piece CNC mandrel bends; laser-cut intake slots; end-formed nozzle and hose beads; no wetted welds | Medium — samples needed |
| Finish | Non-directional fine satin, passivated (ASTM A967); electropolish if QA roughness limit requires; low gloss, no mirror, no coating | Medium |
| Mounting | Laser-cut formed 316L clip ×2; replaceable grey silicone pads in two ranges (5–8 mm, 8–12 mm glass); ±20 mm height and ±30° aim adjustment by friction; no fasteners in water | Low–medium |
| Inflow | Slot width ≤1.0 mm (provisional), open area ≥5× bore; removable push-fit end cap with detent (no O-ring, no thread) | Low — needs V-T5 |
| Outflow | Formed directional nozzle, modest flare, aimed slightly up; depth and aim set by the clip | Low — needs V-T3/V-T9 |
| Hose interface | Two rolled retention beads; 20–25 mm hose engagement; no hose clamp needed | Medium |
| Marking | One small laser mark on the top of the hook, above water, re-passivated | Medium |
| Contents | Inflow, outflow, 2 clips (pads fitted), 1 spare pad set, cleaning brush, compatibility and care card; **no hose** | Medium |
| Pack | Kraft rigid board box with board cavities, no foam; outer ≤45 × 18 × 9 cm (≈1.5 kg volumetric) | Medium |
| Price | MRP ₹3,999 incl. GST (test ₹3,499–4,499) | Low |
| Pilot lot | 50 sets, then 100 | Medium |
| Warranty | 2 years against manufacturing defects and corrosion under stated care, **only if V-T7 passes**; otherwise 1 year | Low |
| Spares at launch | Clip pair, pad sets, end cap, brush | Medium |

## 3. Why these choices

| Choice | Proposed | Alternatives considered | Evidence for the choice | What would change it |
|---|---|---|---|---|
| **Hose size** | **16/22** | 12/16 first; both at launch | **The value canister actually in stock in India uses 16/22.** Sunsun HW-302 is listed at ₹4,240 by Aqua Zones as "16mm / 22mm (inside/outside diameter), both inlet and outflow", rated 1000 l/h, up to about 300 L ([Aqua Zones](https://www.aquazones.in/sunsun-hw-302-external-filter/)). At Chennai Aquarium, Sunsun HW-302/303B/304A/3000/5000/603B were all in stock, while most Eheim models (including an "External Classic (250L)" at ₹13,350) were out of stock ([Chennai Aquarium](https://www.chennaiaquarium.in/filtration-system/canisters)). Retailer spare-hose listings give 16/22 for HW-302/303/402B/403B ([WilTec](https://www.wiltec.de/en/spare-part-sunsun-hw-302-external-aquarium-filter-hose-set-16-22mm/50197-18)). Oase BioMaster, Eheim Professionel 4+, Eheim Classic 600 and JBL e1502 also use 16/22 [M] (TECHNICAL REF §2). 16/22 also suits 60–90 cm tanks: a 15 mm bore at 1,000 l/h is ≈1.6 m/s, against ≈3.1 m/s in a 10.7 mm bore (EST) | 12/16 covers Eheim Classic 250/350, JBL e402–e902, Tetra EX 400–800 and Dennerle hang-on | V-C2 survey shows 12/16 on more than ≈50 % of target owners' filters |
| **Tank class** | 60–90 cm, 35–45 cm tall, rimless | Nano (≤45 cm); 120 cm+ | Matches the Sunsun HW-302 class (up to ≈250–300 L per retailers) and typical planted-tank sizes (ADA's 60P and 90P classes are 36–45 cm tall with 5–10 mm glass [M], TECHNICAL REF §7). One immersion length is feasible across 35–45 cm heights (§4.3) | V-C1/V-C2 show a different dominant tank size |
| **Material** | 316L | 304 | Chloride margin (≈1000 vs ≈200 ppm, [ASSDA](https://www.assda.asn.au/component/content/article?id=271%3Achlorine-and-chloride--same-element%2C-very-different-effect)) in CO₂-acidified tanks with crevices, at a small material cost difference (tube is ≈11 % of COGS). Grade trust is itself a selling point: the market shows contradictory 304/316 claims | V-T7 shows 304 performs equally **and** quotes show a meaningful saving (D-05; the earlier 304 view is preserved) |
| **Tube size** | 17 mm OD × 1.0–1.2 mm | 16 mm tube with beads formed up to hose-fit size; 19.05 mm reduced | Pipe OD ≈1 mm over hose ID is the published fit rule ([Oase](https://us.oase.com/blogs/upgrading-equipment/upgrading-tubing-and-glassware)); 1.2 mm is a wall thickness a branded stainless pipe publishes (Chihiros Pro, [R]). **Small-lot availability of 17 mm × 1.0–1.2 mm 316L is not yet confirmed** — stockists list 316L ranges from 16 mm OD with 0.5–3.0 mm walls ([Steel Tubes India](https://www.steeltubesindia.net/stainless-steel-316l-pipe-tube.html)) but not this exact size | RFQ V-S1; bend samples V-S2; pull-off V-T2 |
| **Construction** | One-piece bends, formed nozzle, rolled beads | Welded or spun nozzle; separate barb | No crevice or heat tint in the flow path (TECHNICAL REF §8.2); Chennai end-forming capability published (SOURCING §9) | V-S2 shows the nozzle cannot be formed from tube without wrinkling (D-18) |
| **Finish** | Through-material low-gloss satin, passivated | Mirror/electropolish bright; bead blast; dark PVD | CMF: one finish at launch; avoid mirror glints and jewellery look; a coating that chips "reads as failure"; no underwater PVD data exists (AESTHETIC REF §4–5). A through-material finish can be restored by the user | V-A2 photo panel fails in dark scapes **and** V-A3/V-T7 clear a dark coating |
| **Mounting** | Stainless clip, soft replaceable pads, no suction cups, no wet fasteners | Suction cups; acrylic holders; screw clamps | Mounting is the market's weakest criterion and the clearest recognisable detail (AESTHETIC REF §3, §5); dark fasteners corrode in water (D-19) | V-T8 shows pads cannot hold under hose load across 5–12 mm |
| **Serviceable intake** | Removable end cap, fine slots | Sealed slotted tip; mesh guard add-on | Breakage, hose removal and cleaning were the strongest complaints; shrimp guards are a paid add-on today (COMPETITOR REF §4) | V-T5/V-T6 show the cap leaks debris or is lost in use |
| **No skimmer** | Excluded | Include skimmer | Highest engineering risk (bouncing, air ingestion, entrapment) and doubles development; retained as P2 (COMMERCIAL §2) | Interviews show buyers will not consider a set without a skimmer at this price |
| **No hose supplied** | Excluded | Supply tinted or clear 16/22 hose | Owners already have 16/22 hose with the filter; supplying hose adds cost, stock and a plasticiser question (D-09) | V-A2 month-3 photos show the rim crossing fails with owners' hoses |
| **Brush included** | Included | Sold separately | Cleaning is the core promise; the family packaging rule wants a serviceable kit (AESTHETIC REF §6 Q10) | Cost too high, or no brush fits the bore and slots well |
| **Price** | ₹3,999 | ₹3,499 / ₹4,499 | Base case gives ≈₹1,420 contribution direct and ≈₹620 through dealers (COMMERCIAL §5); parity with Neo Flow Premium and generic stainless skimmer sets | V-C4/V-C6 willingness-to-pay results; quotes |

## 4. Detailed proposed specification

Columns: **Basis** — F sourced fact · R market reference (not a Trophic decision) · E function-derived estimate · A planning assumption. **PR** links to [PRELIMINARY_REQUIREMENTS.md](PRELIMINARY_REQUIREMENTS.md).

### 4.1 Scope and compatibility

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-01 | SKU | `AQ-LP-A` launch set, 16/22 size (SKU code to be assigned per `platform/IDENTIFIER_STANDARD.md`) | A | Owner | SC-01 |
| L-02 | Hose | 16 mm ID / 22 mm OD flexible hose, verified on **measured** hoses from Sunsun HW-302/303, Oase BioMaster, Eheim Professionel 4+ / Classic 600, JBL e1502 (list to follow V-C2) | F/R | V-M1, V-T2 | CP-01/02/03 |
| L-03 | Filter class | Canisters rated ≈800–1,500 l/h with 16/22 hose | F/R | V-T3 | CP-07 |
| L-04 | Tank | Rimless glass, 60–90 cm long, 35–45 cm tall | E/R | V-C2, V-M3 | CP-04 |
| L-05 | Glass thickness | 5–12 mm, covered by two pad ranges | R/E | V-M3, V-T8 | CP-04 |
| L-06 | Rimmed tanks | **Not supported at launch**; stated plainly on pack and listing | A | — | CP-05 |
| L-07 | Clearance above rim | Top of hook ≤25 mm above the glass edge (lids, light legs) | E | V-M2 (including `AQ-LT-*` legs) | CP-06 |
| L-08 | Rear clearance | Hose-connection end sits behind the tank ≤35 mm from outer glass face and ends 60–100 mm below the rim so the hose drops without kinking at the rim | E | V-M2, R12 bend test | CP-06 |

### 4.2 Function and hydraulics

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-10 | Supported installed flow | 400–1,000 l/h | E (installed flow ≈40–68 % of rated, TECHNICAL REF §3) | V-T3 | FN-06 |
| L-11 | Pipe bore | ≈14.6–15.0 mm (17 mm OD less wall) | E | Inspection | FN-01 |
| L-12 | Velocity in bore at 1,000 l/h | ≈1.6 m/s (EST) | E | V-T3 | FN-01 |
| L-13 | Added loss (inflow + outflow) | Installed flow ≥95 % of flow with the filter's stock pipework | A (proposed acceptance) | V-T3 | FN-01 |
| L-14 | Outflow behaviour | Surface current that moves film toward the intake without breaking the surface at the recommended setting; more agitation available by raising or aiming the nozzle | E | V-T9 | FN-02/03 |
| L-15 | Noise and air | No audible splash or air entrainment at the recommended setting; ≤3 dB(A) above stock pipework at 1 m; no air in canister after restart | A | V-T10 | FN-04/05 |

### 4.3 Geometry envelope (provisional, function-derived — not a form)

Derived for a 35–45 cm tall tank with water 20–30 mm below the rim and 50–100 mm of substrate. The form language inside this envelope is the design phase's job.

| # | Parameter | Proposed launch value | Derivation | Confirm by |
|---|---|---|---|---|
| L-20 | Outflow nozzle depth (centre, below rim) | 70–110 mm, user-adjustable ±20 mm at the clip | 40–80 mm below a water surface sitting 20–30 mm below the rim: shallow enough to drive a surface current, deep enough not to splash | V-T9 |
| L-21 | Outflow nozzle reach from inner glass face | **70–100 mm** (was 40–70; changed by owner 2026-09-18 after concept r1a showed 90–94 mm is the minimum consistent with `clr` and `straight_min` at 1.5 × OD — D-21; still a TARGET pending V-T9) | Clears the glass for flow spread; keeps hardware close to the glass | V-T9, V-A2 |
| L-22 | Inflow intake end depth (below rim) | 230–250 mm | In a 35 cm tank with 60 mm substrate this leaves ≈40–60 mm above the substrate; in a 45 cm tank it draws from the lower-middle water column | V-M2, V-T5 |
| L-23 | Intake slot zone length | 60–90 mm, starting at the intake end | Open-area requirement L-31 with slots no wider than L-30 | V-T5 |
| L-24 | Pipe centreline to inner glass face | 20–30 mm | Set by the smallest clean bend radius the supplier achieves on 17 mm thin-wall tube | V-S2 |
| L-25 | Hook inner gap | Glass thickness + pad thickness; covered 5–12 mm by two pad ranges | R/E | V-T8 |
| L-26 | Inflow/outflow spacing on the glass | Not specified; user-positioned | — | — |
| L-27 | Set mass | ≈0.3–0.4 kg (tube ≈0.40–0.47 kg/m, EST) | E | Weigh first article |

### 4.4 Material and finish

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-40 | Tube grade | 316L (304 qualified alternate, EDR-021), welded-and-drawn with bead-conditioned bore, or seamless | F/E | MTC; PMI at incoming | MT-01, MT-03 |
| L-41 | Tube size | 17.0 mm OD × 1.0–1.2 mm wall (fallback: 16 mm tube with beads formed to hose-fit size) | R/E | V-S1, V-S2, V-T2 | CP-01 |
| L-42 | Traceability | EN 10204 3.1 mill test certificate per heat; heat number recorded to finished lot; BIS mark if the SS tube QCO applies at purchase | F | Inspection | MF-05 |
| L-43 | Surface, outside | Non-directional fine satin, low gloss; no mirror; no coating | E (CMF direction) | V-A1/A2 photo panel | AE-01/07/10 |
| L-44 | Surface, bore | Free of dross, burr and lubricant; passivated | E | Inspection; water-break test | MF-04 |
| L-45 | Passivation | ASTM A967 (citric method preferred); electropolish to ASTM B912 if QA sets a roughness limit the satin cannot meet | F/E | V-T7 | MT-02 |
| L-46 | Corrosion acceptance | No rust, pitting or tea staining at 30 cm after 90 days in CO₂-acidified soft water and hard Coimbatore tap water with 12 cleaning cycles | A (proposed acceptance) | V-T7 | MT-04 |
| L-47 | Clip pads | Platinum-cure silicone, mid-grey, replaceable; no plasticiser or colourant known to be harmful to invertebrates (supplier declaration) | E | V-T8; supplier data | LS-04, MO-02 |

### 4.5 Inflow

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-30 | Slot width | ≤1.0 mm (provisional) | E: juvenile dwarf shrimp 1–2 mm ([Green Aqua](https://greenaqua.hu/en/blog/post/how-to-protect-shrimp-from-filter-and-surface-skimmer-intake)); no brand publishes a figure | V-T1 competitor survey; V-T5 live test | LS-01 |
| L-31 | Slot open area | ≥5× bore area (≈≥900 mm²), keeping mean slot velocity ≤≈0.3 m/s at 1,000 l/h (EST) | E | V-T5 | LS-02 |
| L-32 | Slot manufacture | Fibre-laser cut before bending; no internal dross; slot edges deburred | E | V-S2 | MF-02 |
| L-33 | End cap | Removable 316L cap; push-fit with a positive detent; no thread, no O-ring; cannot trap shrimp in gaps | E | V-T5, V-T6 | SV-01/04, LS-03 |
| L-34 | Brushability | A supplied brush passes through the full inflow from the open end with the hose attached | E | V-T6 | SV-01 |
| L-35 | Skimmer interface | The straight vertical section through the water-surface zone is left uninterrupted so a later P2 sleeve can fit; no visible stub or unused feature | E (CMF review) | V-A1 | SC-02 |

### 4.6 Outflow

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-50 | Termination | Formed from the tube: a directional nozzle with a modest flare, aimed slightly upward; no petal or bloom shape | E (CMF O7; D-18) | V-S2, V-T9, anti-mimicry review | FN-03, AE-06 |
| L-51 | Adjustment | Aim ±30° and depth ±20 mm through the clip, **plus independent nozzle yaw by a dry friction swivel above the waterline (EDR-024, 2026-09-19)**; no swivel joint in the water | E | V-T6, V-T9 | SV-04 |
| L-52 | Brushability | A supplied brush passes from the nozzle end with the hose attached | E | V-T6 | SV-01 |

### 4.7 Clip (mounting)

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-60 | Material | 316L sheet, laser-cut and formed, same finish family as the pipes, passivated | E | V-T7 | MO-03 |
| L-61 | Contact | Soft pads on both glass faces; no metal contact with glass | E | V-T8 edge inspection | MO-02 |
| L-62 | Pad ranges | Two pad sets: 5–8 mm and 8–12 mm glass (one fitted, one spare) | E | V-T8 | CP-04 |
| L-63 | Hold | No slip and ≤2° tilt change over 30 days under a water-filled hose load at 5 mm and 12 mm glass | A (proposed acceptance) | V-T8 | MO-01 |
| L-64 | Adjustment | Tool-free friction adjustment of height (±20 mm) and aim (±30°); no fasteners below the rim | E | V-T6 | MO-03 |
| L-65 | Family role | The clip is the proposed primary recognition cue candidate (D-08 to confirm) and should be reusable for later wet accessories | E (CMF review) | Design phase | AE-04/08 |

### 4.8 Hose interface

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-70 | Retention | Two rolled beads on the tube end; no welded barb | E | V-T2 | SV-03 |
| L-71 | Engagement length | 20–25 mm of hose over the pipe | R: 1.5–2 cm overlap practice ([Aquasabi](https://www.aquasabi.com/aquascaping-wiki_filtration_hose-diameters-and-glassware)) | V-T2 | SV-03 |
| L-72 | Pull-off | At least equal to the filter's stock pipework with the same hose at 15 °C and 30 °C; no creep over 14 days | A (proposed acceptance) | V-T2 | SV-03 |
| L-73 | Removal | Hose removable by hand after warming, 50 cycles without damage to pipe or hose seat | A | V-T2 | SV-02 |
| L-74 | Rim crossing | Pipe-to-hose transition behind the glass, below the rim line (L-08), so from above the eye reads pipe then hose as one line | E (CMF O6) | V-A2 | AE-05 |

### 4.9 Marking, pack and contents

| # | Parameter | Proposed launch value | Basis | Confirm by | PR |
|---|---|---|---|---|---|
| L-80 | Mark | One small Trophic wordmark laser-marked on the top of each hook, above water, re-passivated after marking | E (CMF O10; R19) | V-T7 marked coupons | AE-09 |
| L-81 | Regulatory text | On the pack and listing only, per Legal Metrology review | F | Consultant | CL-02 |
| L-82 | Contents | Inflow; outflow; 2 clips with 8–12 mm pads fitted; 1 spare 5–8 mm pad set; cleaning brush sized to the 15 mm bore; compatibility and care card (includes **no bleach on stainless**, a verified cleaning method, supported filters and glass range, warranty) | E | V-T6, V-T7 | PK-03, MT-06 |
| L-83 | Pack | Kraft rigid board, one-colour matte print, board cavities, no foam, no window; outer ≤45 × 18 × 9 cm (≈1.5 kg volumetric at the 5000 divisor) | E (family rule; [iCarry](https://www.icarry.in/icarry-sample-rates-by-zones.pdf) volumetric pricing) | V-P1 | PK-01/02 |

### 4.10 Quality and inspection at launch

| # | Parameter | Proposed launch value | Confirm by |
|---|---|---|---|
| L-90 | First article | Full dimensional check against the approved drawing; slot width sample measurement; bend ovality; bead OD; passivation verification; PMI | V-S2 / pilot |
| L-91 | Per-lot checks | MTC review; PMI on a sample; slot width on a sample; visual finish against a reference sample; hose fit gauge on every pipe; clip fit on 5 mm and 12 mm glass coupons | Pilot |
| L-92 | Critical characteristics | Bead OD and position; slot width; hook gap; nozzle aim angle; absence of internal burr | Gauges defined in design (MF-02) |
| L-93 | Scrap allowance used in costing | 6 % (EST) | Pilot yield |

### 4.11 Commercial launch parameters

| # | Parameter | Proposed launch value | Basis | Confirm by |
|---|---|---|---|---|
| L-100 | MRP | ₹3,999 incl. GST (test band ₹3,499–4,499) | COMMERCIAL §4–5 | V-C4, V-C6 |
| L-101 | Pilot lot | 50 sets, then 100 once sell-through is proven | MANUFACTURING_COST_AND_MARGIN §3 (COGS ≈₹1,540 at 50, ≈₹1,190 at 100, EST) | Quotes, cash |
| L-102 | Channels | Own site first; 3–5 specialist retailers at a fixed dealer margin ≤40 %; Amazon.in later | COMMERCIAL §8 | V-C5 |
| L-103 | Warranty | 2 years, manufacturing defects and corrosion under stated care — conditional on V-T7; else 1 year | E | V-T7, counsel |
| L-104 | Spares | Clip pair ₹499–599; pad set; end cap; brush (prices to set) | E | Cost |
| L-105 | Claims permitted at launch | Only claims with recorded evidence: "316L stainless (certificate per lot)", "fits [measured filter list]", "shrimp-safe intake" only after V-T5, flow range only after V-T3. No "food/surgical/medical grade" | PR-CL-01 | Counsel |

## 5. Explicitly not in the launch

Surface skimmer (P2) · 12/16 size · nano (≤45 cm) and 120 cm+ tank sizes · rimmed-tank mounting · dark or coated finishes · two finishes · supplied hose · suction cups · swivel joints in water · welded parts in the flow path · clip/guard accessory kit for other brands' pipes (P3) · any "food-grade", "surgical-grade" or unverified "shrimp safe" claim.

## 6. Effect on cost estimates

The cost models assume a set of ≈0.8–1.0 m of tube and no brush. Proposed changes against that base (EST, per set at 100):

| Change | Effect |
|---|---|
| 17 mm × 1.0–1.2 mm tube instead of the 12.7 mm reference price | Tube ≈0.40–0.47 kg/m; at listed ≈₹300/kg for 316L seamless ([IndiaMART](https://www.indiamart.com/proddetail/stainless-steel-seamless-tube-316l-4132207233.html)) ≈₹120–140/m — within the model's ₹130 tube line, subject to quotes |
| Cleaning brush included | +₹40–80 |
| Spare pad set and silicone pads | +₹20–40 |
| Satin finish instead of plain passivated | +₹0–60, depending on process |
| **Estimated S1 COGS at 100 sets with these changes** | **≈₹1,250–1,370** (model base ₹1,190) — contribution at ₹3,999 falls by roughly ₹60–180 per set; re-run [costing/margin_model.py](../costing/margin_model.py) once quotes arrive |

## 7. Path from this proposal to a frozen launch specification

| Revision | Trigger | Content |
|---|---|---|
| **P0 (this document)** | Owner request, 2026-09-17 | Proposed values from desk research |
| P1 | Stage 0B complete: V-C1/C2/C4/C5, V-M1–M3, V-T1, V-A1, V-S1/S2 | Values revised with survey, measurement, teardown and supplier evidence; owner approves or rejects each L-row; D-04/05/06/07/10 recorded |
| P2 | Prototype gate: V-T2–T10, V-A2, V-A3 started, V-P1 | Acceptance values confirmed; QA review; finish and nozzle geometry fixed |
| Released launch spec | Pilot first-article and launch gate | Frozen, change-controlled; values may appear on drawings |

**Decisions this proposal asks the owner to take provisionally** (tracked in [DECISIONS_AND_OPEN_QUESTIONS.md](../DECISIONS_AND_OPEN_QUESTIONS.md) §3): D-04 hose size 16/22 · D-05 316L · D-06 5–12 mm glass, rimless only · D-07 through-material satin finish at launch · D-08 clip as the candidate primary recognition cue · D-09 no hose supplied · D-10 ₹3,999 test price.
