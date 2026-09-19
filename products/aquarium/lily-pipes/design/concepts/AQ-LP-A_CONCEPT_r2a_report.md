# AQ-LP-A — Concept round 2, direction r2a — build report

| | |
|---|---|
| **Model class** | **CONCEPT — not a design.** No dimension in this model is a decision (`docs/system/CAD_SEED_GUIDE.md` §2) |
| **Direction** | r2a — r1b straight pipe inside the glass **+ hose-end swivel (EDR-024) + telescopic intake cap (EDR-025) + formed hose guide on the J-clip; no skimmer (ADR-009)** |
| **Fusion design** | `AQ-LP-A_CONCEPT_r2a`, folder `AQ-LP-A` · lineage `urn:adsk.wipprod:dm.lineage:7PMY6e_CSgaQaXfmHi1Pdg` · **v3** (2026-09-19) · branched from `AQ-LP-A_CONCEPT_r1b` v1 |
| **Owner choices applied** | D-24 → r1b pipe + formed hose guide; swivel at the hose end; EDR-024/025; ADR-009 |
| **Not permitted from this model** | Drawings, STEP release, public images, supplier geometry, promotion to DESIGN |

## 1. What was built (changes from r1b)

| Component | r2a content |
|---|---|
| `10_INFLOW` | Straight tube, top **20 mm** above the rim (raised from 15 so the hose-guide curl clears the saddle), tube end at 189.5 mm below the rim; slot zone 97.5–172.5 mm below the rim (54 slots, unchanged); beads at the top |
| `10_INFLOW/11_END_CAP` | **Telescopic cap**: a cup 62.5 mm long (Ø19.3 mm), closed bottom, with a rolled groove near the rim carrying a **silicone/PTFE band** (`CAP_BAND`, 4 mm wide, 0.2 mm radial interference on the tube). `cap_pos` 0 = fully open (cup bottom 240 below rim, all slots clear); `cap_pos` 1 = raised 47.5 mm, covers 42.5 mm of the slot zone |
| `20_OUTFLOW` | Tube top is now a **formed socket** (mouth 10 mm above the rim, bore Ø18.2, OD Ø20.2, 15 mm engagement, 4 mm cone) — one body with the pipe. **`OUTFLOW_STUB`**: a 42 mm spigot of the same tube (Ø17 × 1.0) carrying the two hose beads and a stop bead that rests on the socket mouth; spigot bottom 4 mm below the rim (21 mm above the water plane). **`SWIVEL_RING_PTFE`**: 0.5 × 4 mm friction ring mid-engagement. Elbow and taper nozzle unchanged (tip 96 mm) |
| `30_CLIP_IN`, `31_CLIP_OUT` | J-clip as r1b (collar tab 13.5–15 mm below the rim, above the water); flat 74.7 × 26 × 1.5 |
| `32_HOSE_GUIDE_IN`, `33_HOSE_GUIDE_OUT` | **New**: one-blank 16 × 1.5 mm strip — 10 mm foot on the saddle top, 90° up, stem, 90° toward the glass, short run, then a **270° curl** of centreline radius 18.25 mm centred on the hose loop; the hose (loop radius 30) rides on the curl's outer face. Loop centre 28 mm (inflow) / 51 mm (outflow) above the rim. Sheet metal, flat pattern 115 × 16 mm. Joined to the saddle dry, above the rim — method open |
| `01_REF_HOSE` | Reference hoses now start at the pipe/stub top plus 8 mm straight and loop at `hose_guide_r` = 30 mm |

New parameters (all with class comments): swivel — `swivel_mouth_above_rim` 10, `swivel_engage` 15, `swivel_cone` 4, `swivel_ring_t` 0.5, `swivel_ring_w` 4, `swivel_clear` 0.1, `socket_id` (derived 18.2), `stub_gap` 1, `stub_top_margin` 6; cap — `cap_travel` (2 rows + gap = 47.5), `cap_engage_min` 12, `cap_floor` 3, `cap_clear` 0.15, `band_t` 1.5, `band_w` 4, `band_interf` 0.2, `cap_lip` 2, `cap_pos` (0…1), `tube_end_depth` (derived), `slot_from_end` 17; guide — `hose_guide_r` 30, `guide_tab_w` 16, `guide_foot` 10, `guide_wrap` 270°, `guide_stem_x` 0, `guide_x`/`guide_r` (derived), `hose_straight` 8, `hose_top_in`/`hose_top_out` (derived). All ASSUMPTION unless marked derived; listed in `PRODUCT.md` §5a rows 27–32.

## 2. Check table

| Check | Target | Glass 5 / 360 | Glass 12 / 450 | Result |
|---|---|---|---|---|
| Pipe height above rim — inflow / outflow socket mouth / stub top | ≤ 25 (L-07, pipe) | 20 / 10 / 38 | same | pipes pass; **stub top 38 and hose loops 69 / 87 exceed 25** — L-07 cannot be met by any hose-over-rim form; owner to decide whether L-07 applies above the pipe |
| Leg centre to inner glass | 20–30 | 25 | 25 | pass |
| Hose outside centreline from outer glass / outer edge | ≤ 35 (L-08 spirit) | 30 / 41 | 23 / 34 | pass on centreline at a supported R30 loop (r1b's free hose was 146) |
| Swivel joint below waterline? | none allowed (EDR-024) | spigot bottom −4 mm vs water −25 | same | pass, 21 mm margin |
| Nozzle depth · tip reach | 70–110 · 70–100 | 90 · 96 | same | pass |
| Intake end (cup bottom, open) · above substrate | 230–250 · clear | 240 · 60 | 240 · 150 | pass |
| Cap closed: covered zone · est. open area | user throttle | 42.5 mm (row 1 + gap + 15 mm of row 2) · ≈468 mm² (43 % of 1080) | same | works; **≈2 rows needs the open rim 5 mm lower or `cap_travel` +5** |
| Open area, cap open | ≥ 884 | 1080 | 1080 | pass |
| Bends ≥ `clr`, straights ≥ `straight_min` | 25.5 | outflow 25.5; 79.5 / 25.5 | same | pass |
| Brush line of sight | straight | inflow straight end to end with the cup off; outflow: nozzle → straight → blind past the elbow; **from the hose end the spigot comes out, giving a straight view down to the elbow** | same | inflow pass; outflow one elbow |
| Sheet parts flatten as one blank | yes | clips 74.7 × 26; guides 115 × 16 | same | pass (4 parts) |
| Interference | designed contacts only | beads inside the hoses (111.7 mm³ each); cap band on the tube (42.2 mm³, the 0.2 mm interference); guide strip tangent to the hose (0) | same | pass |
| Set mass (2 tubes, stub, ring, cup, band, 2 clips, 2 guides) | ~0.3–0.4 kg | **282 g** | 284 g | pass (r1a 345, r1b 221) |

## 3. Assumptions

Rows 27–32 in `PRODUCT.md` §5a plus everything carried from r1a/r1b. Non-parametric choices: swivel retention by friction ring plus stop bead only (no groove); band in a rolled groove with a 2 mm lip; hose guide as a separate part rather than a lanced tab (a tab from the 16 mm saddle top cannot supply the ~105 mm of strip the curl needs); guide joined above the rim by spot/laser weld or rivet.

## 4. Problems, stops, things to look at

- **The cup is long.** 62.5 mm of Ø19.3 sleeve under a Ø17 pipe; closed, it is the most visible thing at the bottom of the tank (image 08). One row of travel (27.5 mm) would make it 42.5 mm and keep the intake end nearer the r1 depth. Owner call.
- **Intake depth semantics changed**: 240 is now the cup bottom when open; the tube ends at 189.5 and the slot zone is 97.5–172.5 below the rim — higher than the r1 concepts. If the slots should stay deep, `in_end_depth` must grow or the travel shrink.
- **Hose loops stand 69 / 87 mm above the rim** even with the guide; the guide fixes the kink and the outward reach, not the height. The lid/light keep-out placeholder is violated; V-M2 has to say what lids and light legs actually allow.
- The outflow hose loop is 18 mm higher than the inflow's because the stub adds the swivel engagement above the mouth. A lower mouth would put the spigot bottom closer to the water (now 21 mm margin).
- Build issues fixed in session: a first cup profile with a degenerate groove; two dimension-sign flips (cup and band) fixed with construction-line drivers; a socket that would not join (needed 1 mm overlap); a guide whose stem met the curl non-tangentially. Nothing was hand-placed in the saved state; sketches re-solve at 12 mm / 450 mm and at both cap positions.
- Sketches `GUIDE_PATH`, `TELESCOPIC_CAP`, `BAND`, `SWIVEL_SOCKET`, `SWIVEL_STUB`, `SWIVEL_RING_PTFE` are driven but not "fully constrained" by Fusion's definition (redundant dims skipped).

## 5. Review images (internal only)

`images/r2a_01_front_1m.png` … `r2a_09_hose_loop_side.png`, including `r2a_05_swivel_closeup.png`, `r2a_07_cap_open_closeup.png`, `r2a_08_cap_closed_closeup.png`.

## 6. What r2a settles and what it asks

The three owner decisions of 2026-09-19 are all expressible in stainless tube and sheet without a wetted joint: the swivel is a formed socket and a 42 mm spigot; the throttle is the cap; the hose crossing is a 16 mm strip. What it asks back: (1) accept hose loops of ~70–90 mm above the rim, or measure lids first (V-M2); (2) one or two rows of cap travel; (3) how the guide joins the saddle; (4) whether 21 mm of spigot margin above the water is enough given water-change habits (`water_below_rim` is itself an assumption). The evidence that closes round 2 is unchanged: V-M1 (hose kink radius, now "supported at R30"), V-S2 (bend and end-forming samples, now including the socket expansion), V-T5/V-T6/V-T8 as before.
