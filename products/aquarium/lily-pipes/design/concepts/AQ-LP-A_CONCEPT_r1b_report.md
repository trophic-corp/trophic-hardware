# AQ-LP-A — Concept round 1, direction r1b — build report and round-1 comparison

| | |
|---|---|
| **Model class** | **CONCEPT — not a design.** No dimension in this model is a decision (`docs/system/CAD_SEED_GUIDE.md` §2) |
| **Direction** | r1b — the **hose crosses the rim**; the pipe is a straight tube inside the glass, held by a J-clip on the inner face |
| **Fusion design** | `AQ-LP-A_CONCEPT_r1b`, folder `AQ-LP-A` · lineage `urn:adsk.wipprod:dm.lineage:G5tTYuVjQYWk1vyX45qxiQ` · **v1** (2026-09-18) · branched from `AQ-LP-A_CONCEPT_r1a` v3 before any change |
| **Brief followed** | [CONCEPT_DESIGN_BRIEF.md](../CONCEPT_DESIGN_BRIEF.md); owner decisions D-20…D-23 of 2026-09-18 applied |
| **Not permitted from this model** | Drawings, STEP release, public images, supplier geometry, promotion to DESIGN |

## 1. What was built

Same component tree, parameters and reference tank as r1a (see the [r1a report](AQ-LP-A_CONCEPT_r1a_report.md) §1); the product components were deleted and rebuilt:

| Component | r1b content |
|---|---|
| `10_INFLOW` / `11_END_CAP` | One straight hollow Pipe body, top 15 mm above the rim, bottom at −230 mm; two beads within `hose_engage` of the **top** (the hose end is now the top); 54 slots as r1a; same end cap |
| `20_OUTFLOW` | Straight leg from +15 mm to the 90° elbow at `clr`, `straight_min` run, same taper nozzle. Tip at 96 mm from the inner glass |
| `30_CLIP_IN`, `31_CLIP_OUT` | **J-clip**: saddle over the rim (inside width 16 mm), outer leg 12 mm long carrying the outside pad, inner leg then 90° arm into the collar tab (Ø17.2 hole + 1 mm slit) at 13.5–15 mm below the rim — above the 25 mm water plane and below the hose end (−7 mm). Sheet metal, flat pattern **74.7 × 26 × 1.5 mm**, 20.6 g |
| `40_PADS` | 10 mm tall pads (`pad_h_b`) both faces, thickness follows `glass_t`; reference sets A/B beside |
| `01_REF_HOSE` | Reference hose swept along a parametric path: 22 mm engagement on the pipe, vertical rise, 180° loop of centreline radius `hose_bend_r`, descent outside the glass. Hose ID drawn at `tube_od` (stretched) |

New parameters (all in the model with class comments): `leg_standoff` 25 mm (TARGET, L-24 — in r1b it drives the pipe position), `pipe_top_above_rim` 15 mm (ASSUMPTION), `hose_bend_r` = 4 × `hose_od` = 88 mm (ASSUMPTION, rule of thumb; V-M1), `clip_drop_b` 15 mm (ASSUMPTION), `pad_h_b` 10 mm (ASSUMPTION). `bridge_clear` was set to `clip_t` per D-22 for r1a use; `bridge_len`, `clip_wrap` are unused here.

## 2. Check table (brief §7)

| Check | Target | Glass 5 / 360 | Glass 12 / 450 | Result |
|---|---|---|---|---|
| Height above rim — **pipe** | ≤ 25 mm | 15.0 | 15.0 | pass |
| Height above rim — **hose loop** (reference, `hose_bend_r` 88) | L-07 is written for the product; the hose is not the product, but it is what the customer sees | **114** | 114 | **fail in spirit** — see §5 |
| In-tank leg centre to inner glass | 20–30 mm | 25.0 | 25.0 | pass (driven) |
| Outside hose centreline from outer glass (in place of the L-08 rear-leg check) | ≤ 35 mm | **146** (80 at R 55; 30 at R 30) | 139 | **fail** at any hose radius a 22 mm hose will tolerate |
| Rear tip depth | 60–100 | n/a — no rear leg; hose descends freely | — | n/a |
| Nozzle depth · reach (tube end / mid / tip) | 70–110 · 70–100 (D-21) | 90 · 76 / 86 / 96 | same | pass |
| Intake end depth · clearance above substrate | 230–250 · clear | 240 · 60 | 240 · 150 | pass |
| Open area | ≥ 883.6 mm² | 1080 | 1080 | pass |
| Bends ≥ `clr` · straights ≥ `straight_min` | 25.5 | outflow 25.5 · 79.5 / 25.5; inflow single 245 mm straight | same | pass |
| Brush line of sight | straight, end to end | **Inflow: full straight line of sight cap end ↔ hose end.** Outflow: nozzle → straight → blind past the single 90° elbow; from the hose end, straight to the elbow | same | **pass for the inflow, partial for the outflow** (one 90° elbow instead of r1a's 180° + 90°) |
| Clip flat pattern · fasteners | one blank · none | 74.7 × 26 × 1.5, both · none | same | pass |
| Clip position vs waterline | — | collar 13.5–15 mm below rim, **above** water (25) | same | pass (r1a: below) |
| Interference | designed contacts only | beads inside the hose (designed); hose loop × keep-out placeholder 4829 mm³ | same | pass for product bodies; **the hose loop enters the lid/light keep-out** |
| Set mass | ~0.3–0.4 kg | **221 g** (inflow 90.7, outflow 68.5, cap 20.9, clips 2 × 20.6) | 223 | below the estimate — less tube, smaller clip |

## 3. Assumptions made

`leg_standoff` as a driving value, `pipe_top_above_rim`, `hose_bend_r`, `clip_drop_b`, `pad_h_b`, plus everything carried from r1a (`clr`, `straight_min`, nozzle, slots, beads, cap, collar, pads, spacing, keep-out). Recorded in `PRODUCT.md` §5a as decisions 23–26.

## 4. Problems and stops

- A first clip sweep used a section plane 0.75 mm past the path start and produced a skewed body that would not flatten; rebuilt with the section plane placed by distance-on-path. `31_CLIP_OUT` then held a corrupt flat-pattern object and was deleted and rebuilt from scratch; both clips now flatten.
- Nothing hand-placed; every sketch is anchored to the skeleton or origin and re-solves at 12 mm glass / 450 mm tank.
- The hose is modelled as a smooth torus; a real hose sags and ovalises, so the loop height is if anything understated.

## 5. Round-1 comparison — r1a vs r1b

| | r1a — pipe crosses the rim | r1b — hose crosses the rim |
|---|---|---|
| Rim crossing height | 20 mm (pipe) | 15 mm (pipe) + **56–114 mm hose loop** depending on hose radius |
| Outside the glass | rear leg 23 mm (19.5 at 12 mm glass) | hose at 30 mm only if the hose bends at R 30 (kink risk); 146 mm at 4 × OD |
| Brush access | blind past the 180° hook (both pipes) | inflow straight through; outflow one elbow |
| Clip | below the waterline; one blank 131.6 × 26; carries the hook (D-22) | above the waterline; one blank 74.7 × 26; lighter, less to see |
| Tube mass / set mass | 138 + 116 g / 345 g | 91 + 69 g / 221 g |
| Bends per set | 3 (two 180°, one 90°) | 1 (one 90°) — much less V-S2 risk |
| What the customer sees above the rim | a formed stainless hook: Trophic geometry | a bent hose: not Trophic geometry, and it decides the look (D-09) |
| Standoff at 12 mm glass | 19.5 (needs `bridge_len`) | 25 (driven, glass-independent) |

**Reading.** r1b wins on everything Trophic controls (cleaning, corrosion exposure of the clip, mass, bend risk, glass-independence) and loses on the one thing it does not control: the hose. A 16/22 hose cannot cross a rim tidily at 30 mm radius, and at a safe radius it stands 5–6 tube diameters above the tank. r1a solves that with the very hook that costs it brush access.

**Recommendation for round 2 (not a decision).** Neither direction as drawn. The obvious third form is r1a's stainless hook made **openable** for cleaning or **shortened** so the hose does the first bend: that is r1c territory, and the clip decision D-23 already fits either. Concretely: (a) r1b pipe + a **formed stainless hose guide** riding on the J-clip saddle (a 90° or 180° quarter-shell, not a closed tube, so the brush path stays straight); or (b) r1a hook with a **`bridge_len`** of 10 mm and the end cap made the brush entry, accepting a flexible brush for the hook. Both keep D-21/D-22/D-23. The choice needs two measurements before CAD: the real kink radius of the specified hose (V-M1) and whether a bender can hold 25.5 mm CLR on 17 × 1.0 tube (V-S2).

## 6. Review images (internal only)

`images/r1b_01_front_1m.png` … `r1b_06_intake_cap_closeup.png`, plus `r1b_07_hose_loop_side.png` (side view of the loop against the rim).

## 7. Q1–Q6 for r1b

Q1: hose-over-rim removes the hook and the blind bend, but the free hose loop is 56–114 mm tall and 30–146 mm out — the rim crossing cannot be left to the hose alone. Q2: standoff is simply driven (25 mm) and glass-independent. Q3: the J-clip is smaller, above water and still one blank; the collar tab carries over unchanged (D-23). Q4: the taper diffuser now meets the relaxed 70–100 mm reach (96 mm tip). Q5: unchanged, 1080 mm². Q6: unchanged; with r1b the cap is also the brush entry to a fully straight bore, which strengthens the "service detail" reading.
