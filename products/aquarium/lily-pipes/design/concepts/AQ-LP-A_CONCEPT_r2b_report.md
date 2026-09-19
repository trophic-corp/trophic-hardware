# AQ-LP-A — Concept round 2, direction r2b — build report (current round-2 candidate)

| | |
|---|---|
| **Model class** | **CONCEPT — not a design.** No dimension in this model is a decision |
| **Direction** | r2b — r2a simplified after the CMF review of 2026-09-19: plain removable cap reinstated (EDR-025 withdrawn), hose guides removed, one slot band, no stop bead, equal loop heights, pipes at the L-07 limit |
| **Fusion design** | `AQ-LP-A_CONCEPT_r2b`, folder `AQ-LP-A` · lineage `urn:adsk.wipprod:dm.lineage:gxpx7wAwQ1q_zw6ct4m0ig` · **v5** (2026-09-19) · branched from r2a v3 |
| **Keeps** | EDR-024 dry swivel at the hose end; ADR-009 no skimmer; J-clip with collar tab (D-23); straight pipes inside the glass (D-24) |
| **Not permitted from this model** | Drawings, STEP release, public images, supplier geometry, promotion to DESIGN |

## 1. What is in it

Seven product bodies: `INFLOW_TUBE` (straight Ø17 × 1.0, top 25 mm above the rim, end 230 below, one band of 18 × 60 × 1.0 mm slots 153–213 below the rim, beads at the top), `END_CAP` (flush, 0.5 mm chamfer parting line, 8 mm spigot — the brush entry), `OUTFLOW_TUBE` (formed socket at rim level: Ø18.2 bore, Ø20.2 OD, 12 mm engagement, 4 mm cone; 90° elbow at `clr`; 24 mm taper to Ø22.1, tip 100 mm from the glass), `OUTFLOW_STUB` (37 mm spigot of the same tube, hose beads at the top, rests on the socket cone, top 25 mm above the rim), `SWIVEL_RING_PTFE` (0.5 × 4 mm, mid-engagement, hidden), `CLIP_IN`/`CLIP_OUT` (one 1.5 × 26 mm blank each: saddle over the rim, 18 mm legs, collar tab with Ø17.2 hole and 1 mm slit; flat pattern 80.7 × 26 mm). Pads matte black, 5.5 mm at 5 mm glass / 2.0 at 12 mm. Reference hoses loop at R30 from the pipe tops plus 8 mm straight; loop tops 74 mm above the rim.

Set mass **241 g** (inflow 94.7, outflow 64.5, stub 15.8, ring 0.2, cap 20.9, clips 2 × 22.4). Parameters changed from r2a: `swivel_mouth_above_rim` 0, `swivel_engage` 12, `stub_gap` 0, `stub_top_margin` 3, `pipe_top_above_rim` = stub top (derived, 25), `clip_drop_b` 18, `slot_rows` 1, `slot_len` 60, `slot_zone` 60, `nozzle_len` 24, `hose_straight` 8; cap, guide and rest parameters left in the file marked UNUSED.

## 2. Check table

| Check | Target | Glass 5 / 360 | Glass 12 / 450 | Result |
|---|---|---|---|---|
| Pipe tops above rim (inflow / stub) | ≤ 25 (L-07) | 25.0 / 25.0 | same | **pass, at the limit** |
| Hose loop top (reference, R30) | — | 74 | 74 | outside the 25 mm keep-out placeholder; V-M2 decides whether L-07 applies to the hose (D-28) |
| Leg centre to inner glass | 20–30 | 25 | 25 | pass |
| Hose outside centreline from outer glass | ≤ 35 | 30 | 23 | pass at R30 (unsupported — V-M1) |
| Swivel below waterline? | none | spigot bottom −12 vs water −25 | same | pass, 13 mm margin |
| Nozzle depth · tip reach | 70–110 · 70–100 | 90 · 100.0 | same | pass, at the limit |
| Intake end · above substrate | 230–250 · clear | 240 · 60 | 240 · 150 | pass |
| Open area | ≥ 883.6 mm² | 1080 (one band) | same | pass; web at bore 1.62 mm; 60 mm webs flagged |
| Bends ≥ `clr`, straights ≥ `straight_min` | 25.5 | outflow 25.5; 79.5 / 25.5 | same | pass |
| Brush line of sight | straight | inflow: cap end to hose end, straight; outflow: spigot out → straight to the elbow; nozzle → straight to the elbow | same | inflow pass; outflow one elbow |
| Sheet parts | one blank | clips 80.7 × 26 × 1.5, both flatten | same | pass |
| Interference | designed only | beads inside hoses (111.7 mm³ ×2) | same | **pass — nothing else touches** |
| Set mass | 0.3–0.4 kg est. | 241 g | 243 g | lighter than the estimate |

## 3. Assumptions

`PRODUCT.md` §5a rows 27–28 (swivel), 33–36 (r2b), plus everything carried from r1a/r1b. Withdrawn: rows 29–31.

## 4. Problems and stops

- A hose-rest tab folded up from the saddle edge (CMF's fallback) was built twice; the base J-clip flattens but Fusion would not unfold the opposed tab from a converted solid (flat body stayed 22 mm thick), and each edit left a stale flat-pattern object that forced a component rebuild. Dropped rather than carried unproven.
- The socket sketch is not fully constrained; when the mouth moved it split into a separate body and was rebuilt at the new position. It should be fully dimensioned before any further parameter play.
- Nozzle taper 24 mm is below the CMF's 1.5 D wish because the 100 mm reach limit (D-21) wins; owner call.
- Swivel retention: with no stop bead the only pull-out resistance is the PTFE ring's friction — a hose tug could lift the spigot. A rolled retaining groove is the likely fix if the sample fails.
- Reference tank visibility was off in the first r2b capture set; re-shot.

## 5. Review images (internal only)

`images/r2b_01_front_1m.png` … `r2b_08_hose_loop_side.png`.

## 6. Where this leaves round 2

r2b is the simplest expression of the decided set: two straight tubes, one bend, one formed socket, one spigot, one cap, two identical clips, no fasteners, no wetted joints, 241 g. What it still cannot answer from CAD: the hose (loop height and kink radius, V-M1; lid and light clearance, V-M2), the bend and socket forming (V-S2), the slot band (laser trial, V-T5), swivel retention (sample), clip hold (V-T8), and how it looks on a real tank under real lights (V-A1). Those are the round-3 inputs.
