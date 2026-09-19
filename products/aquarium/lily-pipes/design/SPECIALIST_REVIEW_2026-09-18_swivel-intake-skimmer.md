# Specialist review — rotatable outlet, adjustable intake, surface skimmer (2026-09-18)

| | |
|---|---|
| **Trigger** | Owner request after concept round 1: (1) outlet rotatable via a swivel joint, (2) an adjustable feature on the inlet, (3) add the surface skimmer to the design — feasibility, cost and complexity |
| **Routing** | Level 2 (`docs/system/AGENT_ROUTING_POLICY.md`): `systems-architect` + `manufacturing-sourcing-engineer`; Main Claude reconciled. CMF not consulted yet (appearance of a visible joint is flagged for it). QA not invoked — no gate |
| **Status** | Recommendations only. Nothing here is decided; decisions D-25…D-27 opened in `DECISIONS_AND_OPEN_QUESTIONS.md` §3 |
| **Cost basis** | `costing/MANUFACTURING_COST_AND_MARGIN.md` S1 base: COGS ≈₹1,190 per set at 100 (EST). All deltas below are EST per set, ex-GST |

## 1. Rotatable outlet by swivel joint

**Where the joint sits decides everything.** Both specialists reject a wetted swivel (at the elbow, or at the hose end below the rim): it breaks M1 (one continuous tube), creates the worst M8 crevice, cannot be passivated once assembled, and is the classic crevice-corrosion site under the bleach soaks hobbyists use — with 304 as the qualified alternate (EDR-021) the margin is worse still, so grade-independence would be lost. Competitor "360° outlets" are wetted swivels and are not a precedent.

The one defensible form is a **two-part pipe with a dry friction/taper joint above the waterline** (above the rim in r1a; at the pipe top in r1b). It decouples nozzle aim from the pipe body — the real gain over collar rotation, where aiming across the tank makes the pipe look crooked — and stays drainable, brushable and inspectable. It requires M1 to be restated as "no joint below the waterline" (a PROPOSED-spec edit, not an EDR change) and it puts a visible joint on the product, which CMF must judge against "function is the decoration".

| Option | Process | Δ COGS @100 | Δ @25 | Verdict |
|---|---|---|---|---|
| (a) Machined 316L two-piece coupling, O-ring or PTFE seat, **dry, above rim** | CNC turning, Coimbatore — yes | **₹280–480** | ₹520–850 | Makeable in TN job-work; the only version to carry |
| (b) Same, in the water at the elbow | same | ₹280–480 + rework | ₹520–850 | Rejected (crevice, passivation, M1/M8) |
| (c) Ball/socket or bayonet | turning + EDM / 5-axis; not routine locally | ₹700–1,400 | ₹1,300–2,400 | Import or specialist; not recommended |

Assembly 3–5 min, leak/torque check, O-ring MOQ 500–1,000 (sample required). **Cheaper alternative to test first:** pitch from nozzle form plus yaw from collar rotation, which r1b already gives.

## 2. Adjustable intake

Interpretation matters. A **rotating or sliding sleeve over the slot zone** is the weak reading: full-length annular crevice (M8 fail), blocks the straight brush path (L-34 — r1b's chief virtue), weakens ≤1.0 mm slot webs, traps debris where shrimp graze; on 17 × 1.0 tube the 0.1–0.2 mm fit is not achievable as laser-cut (post-slot ovality 0.10–0.30 mm → sizing op + 100 % gauging, 8–15 % early rejects) and stainless-on-stainless galls. Both specialists reject it.

Sound readings: **adjustment outside the water** — interchangeable end caps of two or three heights that blank part of the slot zone in steps (still ≥5× bore), or a bought valve at the hose end. Note the competitor "flow gate" is a **skimmer bypass**, not intake adjustment; it only exists once a skimmer exists.

| Option | Δ @100 | Δ @25 | Verdict |
|---|---|---|---|
| (a) Rotating slotted sleeve | ₹320–560 | ₹600–1,000 | Rejected: crevice, brush path, tolerance, galling |
| (b) Sliding plain sleeve | ₹220–400 | ₹420–750 | Rejected, same reasons |
| (c) Interchangeable end caps, 2–3 heights | **₹90–180** | ₹150–320 | Recommended for P1; fits the removable-cap decision; ≤2 % rejects |
| (d) Valve at hose end (bought, dry) | ₹120–260 | ₹150–300 | Zero manufacturing risk; weakest product story |

NEEDS VALIDATION: whether anyone wants intake throttling without a skimmer (interviews, V-C3) — the request may be request 3 in disguise.

## 3. Surface skimmer

| Option | Parts added | Δ @100 | Δ @25 | Tooling / NRE | Schedule |
|---|---|---|---|---|---|
| (a) Integrated float in the pipe top | 5–7 | ₹620–900 | ₹1,100–1,700 | mould ₹1.2–3.5 lakh at MOQ 2,000–5,000, or turned POM ₹120–220/part at ≤200 | Kills P1: pipe top must sit at the water surface (conflicts with D-22 hook geometry), imports the STRONG field failures (air ingestion, bouncing, re-adjustment, shrimp), makes V-T4 a P1 gate |
| (b) Modular clip-on to the reserved interface (PR-SC-02) | 6–8 + interface | ₹700–1,050 | ₹1,250–1,900 | as (a); interface feature ₹30–60 on every P1 set | Correct failure containment; but the interface must be frozen now from a Phase 0 concept |
| (c) Separate product later | 0 now | 0 | 0 | deferred | No P1 impact |

At 25–200 sets machined POM floats are right; moulding does not amortise below ~2,000. A stainless hollow float needs a sealed weld (rejected). Every unit needs an air-ingestion / flow-window test: ₹60–120 per unit plus a ₹15–40 k rig. Packaging grows a size (+₹40–70). **The existing ≈₹650/set skimmer estimate is parts-only and optimistic; with test and packaging it is ₹780–1,020.**

**Disagreement (preserved, NEEDS DECISION):** Systems recommends holding (b) as the target and freezing a *minimum dimensional envelope* now so a module can follow (ICR when frozen). Manufacturing recommends deferring the interface entirely because a reserved feature taxes every P1 set (₹30–60) and freezes geometry from a concept. Resolving evidence: interviews on skimmer demand (V-C3) and the round-2 pipe form (D-24) — the envelope is cheap to reserve on a straight r1b pipe and expensive on an r1a hook.

## 4. Combined effect

P1 = dry swivel (a) + stepped caps (c), skimmer deferred: **+₹370–660 per set at 100**, taking S1 COGS from ≈₹1,190 to ≈₹1,560–1,850. At MRP ₹3,999 the model's dealer contribution (≈₹620) does not survive that; DTC (≈₹1,420) does. Adding an integrated skimmer as well would put COGS near ₹2,300–2,900 at 100. **None of the three changes an approved decision (EDR-021/022/023); all land on PROPOSED Rev P0 rows** (M1, L-51, L-34, M8, L-30/31, PR-SC-02) and on D-22/D-24.

## 5. What settles it (before any CAD)

- Swivel: one turned 316L coupling pair from a Coimbatore turning shop (sample required) + 50-cycle rotate/leak test; CMF review of a visible above-rim joint.
- Intake: RFQ to the laser vendor for post-slot ovality on 10 pieces (kills or keeps the sleeve idea on data); interview question on throttling demand.
- Skimmer: three turned-POM float samples + a 20-unit flow-window trial before any tooling; interviews on skimmer demand vs a separate skimmer.
- Standing rule proposal: an ADR "no joints and no crevices below the waterline; all adjustment above the waterline" so future requests resolve against it.
