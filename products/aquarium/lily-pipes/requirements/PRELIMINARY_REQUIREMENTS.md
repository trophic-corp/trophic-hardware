# AQ-LP-A — Preliminary Requirements

**Status: every requirement below is PROPOSED.** None is approved, none is a specification, and none may appear on a drawing until the owner approves it and, where marked, test evidence sets the value. **No dimensions are specified.** Where a number is needed, the requirement names the test that will set it ("value: from V-T5").

**Scope:** first product hypothesis **P1 — serviceable stainless inflow + outflow set** ([COMMERCIAL_FEASIBILITY.md](../costing/COMMERCIAL_FEASIBILITY.md) §2). Requirements that would apply to any material route are marked *(route-independent)*. P2 skimmer requirements are listed separately in §12 so they do not creep into P1.

**Priority:** **M** must (a prototype failing it is rejected) · **S** should · **C** could.
**Verification:** **T** test · **I** inspection · **A** analysis · **D** demonstration · **R** review. Test IDs refer to [VALIDATION_PLAN.md](../verification/VALIDATION_PLAN.md).
**Evidence strength** refers to [COMPETITOR_LILY_PIPE_REFERENCE.md](../../../../docs/references/lily-pipes/COMPETITOR_LILY_PIPE_REFERENCE.md) §4 and [LILY_PIPE_TECHNICAL_REFERENCE.md](../../../../docs/references/lily-pipes/LILY_PIPE_TECHNICAL_REFERENCE.md) §9.

---

## 1. Product scope

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-SC-01 | The launch product is a matched inflow + outflow set with its mounting parts, sold as one SKU per hose size | Smallest coherent portfolio; normalises against market sets | Competitor ref §5; Commercial §2 | M | R |
| PR-SC-02 | The inflow provides a reserved interface for a later skimmer module without the unused interface looking unfinished | Keeps P2 possible without a second intake; CMF review | Aesthetic ref §5 | S | R, I (V-A1) |
| PR-SC-03 | No feature is included unless it addresses a recurring problem in Competitor ref §4 or a requirement below | Owner brief: no unnecessary features | Brief | M | R |

## 2. Compatibility *(route-independent)*

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-CP-01 | Every size is specified by pipe OD (with tolerance), pipe bore, and the hose ID/OD it is verified with — never by a bare nominal label | Labels are inconsistent between suppliers | Technical ref §1 | M | I |
| PR-CP-02 | Compatibility is verified against **measured** hoses from the filters most used by the target Indian customer, not against published labels | Fluval, Sunsun and Resun labels conflict | Technical ref §2 | M | T (V-M1) |
| PR-CP-03 | The pilot hose size is chosen from interview and retailer data on installed filters in India (cross-product decision X3) | Unknown Indian installed base | Technical ref §2 | M | R (V-C2) |
| PR-CP-04 | The set fits rimless glass across a stated thickness range; the range is set from tank-builder and customer survey data | ADA alone spans 4–15 mm; Indian local practice unknown | Technical ref §7 | M | T (V-T8), survey V-M3 |
| PR-CP-05 | Rimmed-tank use is either supported by a stated method or explicitly excluded in product information | Recurring rimmed-tank mounting complaints | Competitor ref §4 | S | R |
| PR-CP-06 | The installed set clears common lids, light legs (including Trophic `AQ-LT-*` mounts), rear walls and cabinet hose routes; clearances are measured and published | Clearance is rarely published | Technical ref §7 | S | I, D (V-M2) |
| PR-CP-07 | Trophic publishes a compatibility chart listing measured filter/hose combinations, supported glass range, immersion depth and supported flow range | Only ADA publishes flow/tank data; hose-size mistakes recur | Competitor ref §6 | M | R |

## 3. Function and hydraulics

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-FN-01 | Added pressure loss of inflow + outflow at the supported flow range does not materially reduce installed filter flow compared with the filter's stock pipework; limit value from V-T3 | Losses scale with velocity²; pipe bore narrower than hose | Technical ref §3 (EST only) | M | T (V-T3) |
| PR-FN-02 | The outlet produces a surface current that carries surface film toward the intake without breaking the surface at the recommended depth; a user-adjustable aim or depth to increase agitation is provided if V-T9 shows one fixed behaviour does not suit CO₂-injected and non-CO₂ tanks | CO₂ loss vs O₂ trade-off; no quantitative data | Technical ref §4 | S | T (V-T9) |
| PR-FN-03 | The outlet termination geometry is derived from a measured hydraulic target (jet spread, surface interaction), not from proportion alone | CMF O7 and engineering agree | Aesthetic ref §4 | M | A, T (V-T3, V-T9) |
| PR-FN-04 | In normal operation the set adds no audible splashing or air-entrainment noise at 1 m in a quiet room; threshold from V-T10 | Noise complaints concentrate on skimmers and air | Competitor ref §4 | S | T (V-T10) |
| PR-FN-05 | The set does not introduce air into the canister in normal operation, after a water change, or at restart | Air causes noise and pump risk (Oase manual) | Technical ref §6 | M | T (V-T10) |
| PR-FN-06 | Supported flow range per size is stated in product information and verified on the rig | Rated flow ≠ installed flow | Technical ref §3 | M | T (V-T3) |

## 4. Livestock protection and intake

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-LS-01 | The intake prevents entry of juvenile dwarf shrimp at the supported flow range without an add-on guard; slot width and approach velocity set by V-T5 | Shrimp entrapment STRONG; juveniles 1–2 mm; no published slot width | Competitor ref §4; Technical ref §5 | M | T (V-T5) |
| PR-LS-02 | Intake open area keeps flow within the supported range for a stated interval under a standard debris load; interval from V-T5 | Clogging raises slot velocity and cuts flow | Technical ref §5 | M | T (V-T5) |
| PR-LS-03 | No gap, joint, crevice or edge on any wetted part can trap or pinch shrimp or fry | Joints create traps (CMF O4) | Aesthetic ref §4 | M | I (V-A1), T (V-T5) |
| PR-LS-04 | No wetted material, coating, lubricant residue or marking releases substances harmful to shrimp or snails | Coating and blackening safety unknown | Technical ref §8.4 | M | T (V-T7, V-A3), specialist review |

## 5. Materials, corrosion and cleanability

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-MT-01 | Wetted metal is austenitic stainless of a grade proven by mill test certificate per lot and PMI at incoming inspection; candidate 316L, final grade by owner decision D-05 | Grade claims contradict in market; 316 has chloride margin | Competitor ref §5; Technical ref §8.2 | M | I (MTC), T (PMI) |
| PR-MT-02 | Wetted stainless surfaces are free of embedded iron and heat tint, verified to ASTM A967 (or B912 if electropolished) | Free iron and tint cause rust and tea staining | Technical ref §8.2 | M | T (V-T7) |
| PR-MT-03 | No weld and no crevice in the wetted flow path unless V-T7 shows it does not stain, trap biofilm or corrode | Crevices and tint reduce resistance; biofilm seeds | Technical ref §8.2 | S | I, T (V-T7) |
| PR-MT-04 | After immersion in CO₂-acidified tap water and in hard tap water with repeated cleaning cycles, no rust, pitting or tea staining is visible; duration and cycles from V-T7 | Indian water hardness and CO₂ tanks | Technical ref §8.2 | M | T (V-T7) |
| PR-MT-05 | Any coating or dark finish on wetted parts is proposed only after adhesion, brushing, chemical and leach tests pass | No aquarium evidence exists | Technical ref §8.4 | M (gate) | T (V-A3) |
| PR-MT-06 | Care instructions exclude bleach soaks for stainless parts and specify a verified cleaning method (e.g. brush plus citric acid or H₂O₂, to be confirmed by test) | Bleach far above 304/316 chlorine tolerance | Technical ref §8.5 | M | T (V-T7), R |

## 6. Serviceability and cleaning *(largely route-independent)*

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-SV-01 | Every wetted internal surface can be brushed with a commonly available or supplied brush, without removing the hose where practical | Cleaning burden STRONG; slotted glass inlets need hose removal | Competitor ref §4; Technical ref §5 | M | D (V-T6) |
| PR-SV-02 | Removing and refitting a hose does not require leverage that could damage the set or the tank, and the set survives repeated removal cycles without damage; cycle count from V-T2 | Hose removal and breakage STRONG | Competitor ref §4 | M | T (V-T2) |
| PR-SV-03 | The hose stays retained under filter operation without a separate clamp across supported temperatures; pull-off force target from V-T2 at 15 °C and 30 °C | Creep; cold PVC stiffness (Ooty) | Technical ref §2 | M | T (V-T2) |
| PR-SV-04 | Every separable joint is obvious to operate, cannot be refitted wrongly, does not leak, loosen or change aim in service | CMF O4; R18 | Aesthetic ref §4; Technical ref §9 | M | T (V-T6), I |
| PR-SV-05 | A full clean-and-refit by a hobbyist takes no longer than the stock pipework it replaces; time from V-T6 | Converts "less stressful to clean" into a measurable claim | Competitor ref §4 | S | D (V-T6) |
| PR-SV-06 | Wearing parts (clips, pads, any seals) are available as spares from launch | Spares visible only at Neo and Chihiros | Competitor ref §6 | S | R |

## 7. Mounting

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-MO-01 | The set holds its position and orientation under hose load for the stated glass range without suction cups; duration from V-T8 | Mounting tilt RECURRING; suction cups weak | Competitor ref §4; Technical ref §7 | M | T (V-T8) |
| PR-MO-02 | Mounting cannot chip, scratch or mark the glass edge through repeated fitting cycles; contact force within a limit set by QA/Systems review | Glass-edge safety | Technical ref §9 R05 | M | T (V-T8), R |
| PR-MO-03 | Mounting is installable and adjustable without tools, or with a single visible fastener that is not in water | CMF O5; wet fasteners corrode | Aesthetic ref §4 | S | D |

## 8. Appearance and design language (from the CMF review; outcomes, not forms)

Scored with the rubric in [LILY_PIPE_AESTHETIC_REFERENCE.md](../../../../docs/references/lily-pipes/LILY_PIPE_AESTHETIC_REFERENCE.md) §2. Thresholds are proposals for the design phase, owned by CMF with QA acceptance.

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-AE-01 | **Considered presence:** C3 (visual weight in water) ≥ 4 in at least two of three reference scape types under reference lighting; the product does not rely on transparency | O1; stainless "distracting" risk | Aesthetic ref §3, §5 | M | T (V-A2 photo protocol) |
| PR-AE-02 | **Honest ageing:** after simulated 12-month maintenance, wear reads even and intentional, is restorable with household tools, and the weighted new-vs-aged score gap is ≤ 3 points | O3; central CMF tension | Aesthetic ref §4–5 | M | T (V-A3 ageing board) |
| PR-AE-03 | **Function is the decoration:** every visible feature does a job; serviceable break points are the family's visible detail; no ornament | O4; CMF brief | Aesthetic ref §1, §4 | M | R (CMF), I |
| PR-AE-04 | **Mounting and pipe read as one design:** no clear suction-cup or clear-acrylic look; the clip language is reusable for future wet accessories | O5; weakest criterion in market | Aesthetic ref §3–4 | M | R, T (V-A1) |
| PR-AE-05 | **Rim crossing:** from above, pipe and hose read as one resolved line, and remain acceptable when hose clouds (month-3 photograph) | O6 | Aesthetic ref §4 | S | T (V-A2) |
| PR-AE-06 | **No mimicry:** passes an anti-mimicry review against ADA P/V, ADA Poppy, Cal Aqua Labs funnel, Neo Flow joints, Chihiros slim stainless and Week Aqua curved steel; no petal or bloom metaphors | Brand rule; IP risk | Aesthetic ref §4, §6; Sourcing §8 | M | R (CMF + IP attorney) |
| PR-AE-07 | **Photographability:** C12 ≥ 4 in full-tank and macro shots; no distracting glints or front-glass reflections under reference LEDs including Trophic `AQ-LT-*` | O11 | Aesthetic ref §4 | M | T (V-A2) |
| PR-AE-08 | **One primary recognition cue** (clip, rim collar or termination) is chosen and the others kept quiet | CMF review question 1 | Aesthetic ref §6 | M | R (owner decision D-08) |
| PR-AE-09 | **Marking:** at most one small mark, above water or on a service-only surface, never front-facing in water | O10; laser mark corrosion | Aesthetic ref §4; Technical R19 | S | I |
| PR-AE-10 | **One finish at launch**, chosen only from finishes that passed PR-MT-04/05 and PR-AE-02 | CMF review | Aesthetic ref §5 | S | R |
| PR-AE-11 | The two hose sizes, when both exist, share proportion rules so they read as one family | CMF risk table | Aesthetic ref §5 | S | R |

## 9. Manufacturing and quality

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-MF-01 | The design is producible by Tamil Nadu job-work processes proven by supplier samples (bending, laser, end forming, passivation) without dedicated moulds at launch volumes | Route (b) assessment; mould threshold | Sourcing §2, §7 | M | R (DFM review), T (V-S2 samples) |
| PR-MF-02 | Critical characteristics (pipe OD at hose end, slot width, clip fit range, bend geometry affecting fit) have defined gauges and a first-article inspection record | Repeatability; fit to hose | Sourcing §3 | M | I |
| PR-MF-03 | Supplier-quoted unit cost at a 100-set lot is at or below the level that gives positive dealer contribution at the approved retail price (base model ≈₹1,190; recalculate with quotes) | Dealer viability is thin | Commercial §5–6 | M | A (V-S1) |
| PR-MF-04 | Parts are degreased and free of machining/bending lubricant and particulate before packing | Aquarium safety; passivation quality | Sourcing §3 | M | I, T (water-break or wipe test) |
| PR-MF-05 | Material traceability from tube heat number to finished lot is retained | Grade trust | Competitor ref §5 | S | I |

## 10. Packaging

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-PK-01 | Packaging protects the finish through courier transit (drop and vibration test) with no foam plastic | Family packaging rule; transit | Aesthetic ref §1; Sourcing §5 | M | T (V-P1) |
| PR-PK-02 | Pack dimensions are minimised for volumetric courier weight | Volumetric pricing dominates long boxes | Sourcing §5 | S | A |
| PR-PK-03 | The pack presents parts as an organised tool case and includes compatibility, installation, care (no bleach on steel) and service information | Family rule; hose-size and cleaning problems | Aesthetic ref §1; Competitor ref §4 | S | R |

## 11. Claims, compliance and IP

| ID | Proposed requirement | Rationale | Evidence | Pri | Verify |
|---|---|---|---|---|---|
| PR-CL-01 | Every product claim (grade, "shrimp safe", compatibility, flow, durability) is backed by a recorded test or certificate; no "food/surgical/medical grade" language | Claim risk; competitor practice | Sourcing §8 | M | R (counsel) |
| PR-CL-02 | Pack and listings carry the Legal Metrology declarations required at launch, confirmed by a consultant | LMPC Rules incl. 2026 amendment | Sourcing §8 | M | R |
| PR-CL-03 | An IP freedom-to-operate search and a design-registration decision are completed before any public reveal of the design | Novelty lost on disclosure | Sourcing §8 | M | R (IP attorney) |
| PR-CL-04 | "Made in India" is claimed only if manufacture is genuinely domestic | E-commerce rules | Sourcing §8 | M | R |
| PR-CL-05 | Warranty terms are stated plainly on pack and listing | Warranty almost never stated in market | Competitor ref §5 | S | R |

## 12. P2 skimmer module — parked requirements (not part of P1)

| ID | Proposed requirement | Evidence | Verify |
|---|---|---|---|
| PR-P2-01 | Stable skimming without bouncing or air ingestion across the stated flow range with clean and clogged bottom intake | Competitor ref §4 STRONG; Technical ref §6 | V-T4 |
| PR-P2-02 | Tolerates a stated water-level variation without adjustment; range from top-up habit survey | Technical ref §6 | V-T4, V-C3 |
| PR-P2-03 | Integrated guard meets PR-LS-01 at the skimmer mouth, including the float gap | Competitor ref §4 | V-T5 |
| PR-P2-04 | Appearance scores C3, C8 and C12 at least equal to P1's intake; a float that works but looks cluttered fails | CMF review | V-A1, V-A2 |
| PR-P2-05 | Fits P1's reserved interface without tools | PR-SC-02 | D |

## 13. Explicitly not specified

**2026-09-17:** provisional launch values (hose size, tube size, tank and glass range, slot width, depths, finish, price) are now **proposed** in [AQ-LP-A-BRIEF_RevP0_launch-specification.md](AQ-LP-A-BRIEF_RevP0_launch-specification.md) Rev P0. They remain unapproved and may not be used on drawings until a later approved revision. This file still specifies no values.

No dimensions (lengths, ODs, wall thickness, bend radii, slot widths, immersion depth, glass range), no finish, no grade decision, no termination form, no clip form, no hose supply decision, no price, no supplier. Competitor values in other documents are reference points only and must not be copied into this file.
