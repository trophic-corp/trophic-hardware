# CURRENT_STATE — Lily Pipes (`AQ-LP-A`)

**As of:** 2026-09-19 · **Stage:** Phase 0A research complete; CONCEPT CAD rounds 1–2 built (r1a, r1b, r2a); evidence gates V-M1/V-M2/V-S2 open; Stage 0B not started · **Approved decisions:** EDR-021 stainless 316L (304 alternate) · EDR-022 16/22 hose · EDR-023 rimless 5–12 mm glass · EDR-024 above-water swivel · EDR-025 (withdrawn) · ADR-009 no skimmer in P1

## Where it stands

Desk research is done across market, customers, competitors, aesthetics, engineering, manufacturing, compliance/IP and economics. No supplier contacted, no interviews held, no samples bought, no tests run, no CAD. Every figure is either a published observation (dated 2026-09-17) or an estimate; every recommendation is PROPOSED.

## Proposed direction (awaiting owner approval)

| Item | Proposal | Confidence |
|---|---|---|
| Pursue category | Yes, to Stage 0B (≈₹1.25–3.3 lakh before tooling/IP/inventory) | Medium — desk evidence only |
| First customer problem | Handling: breakage, hose removal, cleaning, shrimp at intake, month-6 appearance | Medium–high (STRONG forum evidence, not Indian interviews) |
| First product (P1) | Serviceable stainless inflow + outflow set, one hose size, one finish, designed clip, reserved skimmer interface | Medium |
| Proposed launch spec (Rev P0) | 16/22 hose; rimless 60–90 cm × 35–45 cm tanks, 5–12 mm glass; 316L 17 mm tube, one-piece bends, no wetted welds; low-gloss satin, passivated; stainless clip with silicone pads, no suction cups or wet fasteners; ≤1.0 mm slots with removable end cap; formed nozzle; brush included, no hose; MRP ₹3,999; pilot 50 then 100 ([AQ-LP-A-BRIEF_RevP0_launch-specification.md](requirements/AQ-LP-A-BRIEF_RevP0_launch-specification.md)) | Low–medium — not approved |
| Route | 316L tube, Tamil Nadu job-work (bending, laser, end forming, passivation), no moulds | Medium — capability inferred, not sampled |
| Not proposed | Glass first product; private-label import; skimmer at launch | Medium–high |
| Price test band | MRP ₹3,499–4,499 | Low — WTP untested |
| Unit cost (EST) | ≈₹2,030 at 25 · ≈₹1,190 at 100 · ≈₹1,040 at 200 per set | Low — no quotes |
| Contribution (base, ₹3,999) | ≈₹1,420 DTC · ≈₹890 Amazon · ≈₹620 dealer | Low |
| Launch investment | ≈₹3.1–10.3 lakh (base ≈₹6 lakh) incl. first 100 sets | Low |
| Break-even (base) | ≈340 sets DTC / ≈770 via dealers | Low |
| Margins (base, ₹3,999, 100-set lots) | Gross ≈65 % direct / ≈41 % dealer; illustrative net margin ≈−67 % / 1 % / 17 % at 84 / 264 / 600 sets a year ([MANUFACTURING_COST_AND_MARGIN.md](costing/MANUFACTURING_COST_AND_MARGIN.md)) | Low |
| Location | Coimbatore for QC, clips, packing, dispatch and likely finishing; tube forming best evidenced in Chennai (Polyfit) until a Coimbatore shop passes samples (SOURCING §9) | Medium — desk evidence |

## Concept round 1 (CAD)

- **r1a built 2026-09-17** — `AQ-LP-A_CONCEPT_r1a` v3, class CONCEPT ([report](design/concepts/AQ-LP-A_CONCEPT_r1a_report.md)). Passes hook height, standoff (23 mm at 5 mm glass, 19.5 at 12), open area (1080 vs 884 mm²), clip flat pattern, mass 345 g. Fails/unresolved: nozzle reach 90–94 mm vs 40–70; no straight brush path through the 180° hook; clip sits below the waterline.
- **Owner review 2026-09-18** — D-20 build r1b before choosing; D-21 L-21 relaxed to 70–100 mm; D-22 hook rests on the clip saddle; D-23 develop the collar-tab clip. Assumptions owed: `PRODUCT.md` §5a (7–22).
- **r1b built 2026-09-18** — `AQ-LP-A_CONCEPT_r1b` v1 ([report and comparison](design/concepts/AQ-LP-A_CONCEPT_r1b_report.md)). Straight pipes, J-clip above the waterline, 221 g, straight brush path on the inflow; but a free 16/22 hose loop stands 56–114 mm above the rim and 30–146 mm out depending on bend radius. Neither direction is recommended as drawn; round 2 should test a formed hose guide on the r1b pipe or an openable/shortened r1a hook, after V-M1 (hose kink radius) and V-S2 (bend samples).
- **Next:** owner picks the round-2 form; V-M1 and V-S2 requests go out (SOURCING §6) — CAD cannot close the remaining questions without them.

## Specialist review 2026-09-18 — swivel outlet, adjustable intake, skimmer

Owner asked for a swivel-rotatable outlet, an adjustable inlet and a skimmer. Systems Architect + Manufacturing/Sourcing reviewed ([note](design/SPECIALIST_REVIEW_2026-09-18_swivel-intake-skimmer.md)): wetted swivel and intake sleeves rejected on crevice/corrosion/brushability grounds; a dry above-waterline joint (+₹280–480/set @100) and stepped intake caps (+₹90–180) are feasible; an integrated skimmer is not recommended for P1 (+₹780–1,020/set incl. test, new validation gate); disagreement on reserving the skimmer interface preserved. Decisions D-25, D-26, D-27 opened.

## Decided (owner, 2026-09-19)

EDR-024 outflow swivel: dry, above the waterline, formed-socket construction first; no joint below the waterline. ~~EDR-025 telescopic end cap~~ — WITHDRAWN the same day; plain removable cap stands. ADR-009: no skimmer in P1 and no reserved skimmer interface; skimmer is a separate P2 product. These change PROPOSED spec rows only. D-24 answered the same day: **r1b pipe + formed hose guide, swivel at the hose end.**

## Concept round 2 (CAD)

- **r2a built 2026-09-19** — `AQ-LP-A_CONCEPT_r2a` v3 ([report](design/concepts/AQ-LP-A_CONCEPT_r2a_report.md)): formed socket + 42 mm spigot swivel with PTFE ring (spigot 21 mm above the water), telescopic cap (62.5 mm cup, band, 0–47.5 mm travel), one-blank hose guides on the J-clips, 282 g set; designed contacts only at 5 and 12 mm glass. Open: hose loops 69/87 mm above the rim vs the 25 mm keep-out placeholder; cup length (1 vs 2 rows of travel); guide joining method; intake depth semantics. Assumptions in `PRODUCT.md` §5a rows 27–32.
- **Owner review 2026-09-19 (later):** telescopic cap withdrawn (EDR-025 WITHDRAWN); CMF review requested ([note](design/CMF_REVIEW_2026-09-19_r2a.md)) — C6 mounting and C7 rim crossing failed on r2a (separate hose guide read as ornament; clip stack; mismatched loop heights); recommendation: clip as the one cue, everything else quiet.
- **r2b built 2026-09-19** — `AQ-LP-A_CONCEPT_r2b` v5 ([report](design/concepts/AQ-LP-A_CONCEPT_r2b_report.md)): plain cap back, guides removed, one slot band, no stop bead, both pipe tops at 25 mm (L-07 limit), collar at 18 mm, 241 g, designed contacts only. **Current round-2 candidate.** New open items D-28 (hose loop guided or specified) and D-29 (cue = clip, PROPOSED).
- **Next:** V-M1, V-M2, V-S2 requests; fully dimension the socket sketch before further parameter play.

## Decided (owner, 2026-09-17)

D-02 stainless · D-05 316L specified, 304 qualified alternate (design grade-independent) · D-04 16/22 hose · D-06 rimless 5–12 mm, rimmed excluded. Records EDR-021/022/023.

## Blocking open decisions

D-17 timing vs microgreen rollout · D-03 first product scope · D-08 primary recognition cue · D-10 price band · D-18 nozzle formed vs joined. Full list: [DECISIONS_AND_OPEN_QUESTIONS.md](DECISIONS_AND_OPEN_QUESTIONS.md) §3.

## Flagged conflicts (not resolved)

- Termination formed from tube vs joined part (Mfg/Sys) — affects appearance and the no-wetted-weld rule (D-18).
- Dark-fastener rule from the lights may not transfer to wet parts (D-19).
- Matte/dark finishes vs hygiene, coating safety and honest ageing (D-07).

## Next actions (in order)

1. **Owner models concept round 1 in Fusion 360** from [CONCEPT_DESIGN_BRIEF.md](design/CONCEPT_DESIGN_BRIEF.md) (`AQ-LP-A_CONCEPT_r1a/b/c`); then record in `docs/engineering/CAD_INDEX.md`, add assumptions to `PRODUCT.md` §5, and run CMF + DFM review.
1a. In parallel: ask the bending supplier for the minimum centre-line radius on 17 × 1.0 mm stainless tube — it decides the hook geometry (brief §4.2).
2. Buy benchmark sets (V-T1, V-A1) and start the filter/hose survey (V-C2).
3. Run hobbyist, retailer and maintenance-business interviews (V-C1, V-C5, V-C7).
4. Send stainless-route RFQs and request process samples (V-S1, V-S2); confirm SS tube QCO status.
5. Commission IP freedom-to-operate search before any public design reveal.
6. Re-run `costing/unit_economics_model.py` with quotes; update this file.

## Evidence gaps that most affect confidence

Amazon.in reviews and prices; Indian community discussions (Reddit blocked); Indian installed filter/hose base; Indian tank glass practice; supplier capability on thin-wall small-OD bends; any underwater durability data for dark finishes; willingness to pay.

## History

- 2026-09-09 — `PRODUCT.md` Phase 0 created (decision 1 framed as glass or acrylic).
- 2026-09-17 (fourth follow-up) — documents re-filed to repository conventions: research to `docs/references/lily-pipes/` (LPREF-01–05), product documents into `requirements/`, `design/`, `verification/`, `sourcing/`, `costing/`; launch spec renamed `AQ-LP-A-BRIEF_RevP0` and registered; links updated. Content unchanged.
- 2026-09-17 (third follow-up) — owner approved decisions 1–3 (EDR-021 316L with 304 alternate, EDR-022 16/22, EDR-023 rimless 5–12 mm); CONCEPT_DESIGN_BRIEF.md added; CAD_SEED_GUIDE readiness updated.
- 2026-09-17 (second follow-up) — added AQ-LP-A-BRIEF_RevP0_launch-specification.md Rev P0 at owner request; provisional recommendations recorded against D-04–D-10.
- 2026-09-17 (follow-up) — added MANUFACTURING_COST_AND_MARGIN.md, costing/margin_model.py and SOURCING §9 location assessment.
- 2026-09-17 — Phase 0A research completed; folder index, research documents and `sources/` added; `PRODUCT.md` stage and next action updated, content otherwise preserved.
