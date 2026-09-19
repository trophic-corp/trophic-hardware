# AQ-LP-A — Concept round 1, direction r1a — build report

| | |
|---|---|
| **Model class** | **CONCEPT — not a design.** No dimension in this model is a decision (`docs/system/CAD_SEED_GUIDE.md` §2) |
| **Direction** | r1a — the **pipe crosses the rim** (two-bend hook), clip spans the gap between each leg and the glass |
| **Fusion design** | `AQ-LP-A_CONCEPT_r1a`, folder `AQ-LP-A`, Karthikeyan's First Project · lineage `urn:adsk.wipprod:dm.lineage:xj1GzVeUTQKhlSVwAK0uWQ` · **v3** (2026-09-17) |
| **Brief followed** | [CONCEPT_DESIGN_BRIEF.md](../CONCEPT_DESIGN_BRIEF.md) (round 1) |
| **Built by** | Claude (Cowork) via the Fusion MCP, 2026-09-17, under the owner's prompt `CONCEPT_R1_FUSION_PROMPT.md` |
| **Not permitted from this model** | Drawings, STEP release, public images, supplier geometry, promotion to DESIGN |

---

## 1. What was built

**Component tree** (brief §3), all bodies in their own components; reference components are not product:

| Component | Bodies | Notes |
|---|---|---|
| `00_REF_TANK` | `GLASS_WALL`, `WATER_SURFACE_REF`, `SUBSTRATE_REF` + construction planes `WATER_PLANE`, `SUBSTRATE_PLANE`, `TANK_FLOOR` | Glass inner face at X = 0, rim at Z = 0; driven by `glass_t`, `tank_h`, `water_below_rim`, `substrate_h` |
| `01_REF_HOSE` | `HOSE_IN`, `HOSE_OUT` | 16/22 hose stubs, `hose_engage` overlap; hose ID modelled at `tube_od` (stretched over the pipe) |
| `02_REF_KEEPOUT` | `LID_LIGHT_KEEPOUT_PLACEHOLDER` | Slab from `hook_above_rim_max` upward — placeholder until V-M2 |
| `10_INFLOW` | `INFLOW_TUBE` (one hollow Pipe body + 2 beads + 54 slots) | Skeleton `CL_INFLOW` fully constrained by parameters |
| `10_INFLOW/11_END_CAP` | `END_CAP` | Separate body, spigot into the bore, chamfered parting line, no thread, no O-ring |
| `20_OUTFLOW` | `OUTFLOW_TUBE` (one hollow Pipe body + 2 beads + nozzle) | Skeleton `CL_OUTFLOW`; nozzle = straight-taper diffuser, 7.3° half-angle, to `nozzle_od_max` |
| `30_CLIP_IN`, `31_CLIP_OUT` | `CLIP_IN`, `CLIP_OUT` | Identical part. Sheet-metal body (rule copied from library "Stainless Steel (mm)", thickness 1.5), **flat pattern created**: 131.6 × 26.0 × 1.5 mm blank |
| `40_PADS` | `PAD_IN_a/b`, `PAD_OUT_a/b` (in position, thickness follows `glass_t`), `PAD_SET_A_5to8_ref_a/b`, `PAD_SET_B_8to12_ref_a/b` (reference sets beside the inflow) | Rubber material for mass only |

**Modelling approach.** Skeleton first: each pipe centreline is a sketch of lines and tangent arcs dimensioned only by user parameters and anchored to the sketch origin (glass inner face / rim). Every secondary sketch (beads, nozzle, slots, cap, clip path, collars, pads, hose stubs) is anchored to a projected skeleton point or to the origin with parameter expressions, so switching `glass_t` 5 → 12 and `tank_h` 360 → 450 re-solves the whole set. Physical material Stainless Steel 316L (mass only); appearance "Stainless Steel – Satin"; no chrome or mirror.

**Clip form (r1a).** One 1.5 mm strip, 26 mm wide, folded as a U-saddle over the rim (inside width `glass_t_max + 2·pad_t` = 16 mm, pads fill the rest), legs 30 mm down each glass face, then 90° outward under each pipe leg into a flat **collar tab** with a Ø17.2 hole the leg passes through and a 1 mm slit to the tab end as a schematic friction spring. All bends are about one axis, inner radius = `clip_t`, so it lays flat as one laser blank. Assembly: slide the clip up both legs from below, hang the pipe, slide the clip down onto the rim. Height adjustment = sliding on the legs, aim = rotating the pipe in the collars. No fasteners anywhere. **A first attempt at a part-wrap cradle in the vertical section was wrong and was discarded** (see §4).

**User parameters** — 55 in the model, class in every comment. Values at the primary configuration:

| Name | Expression | Value | Class / note |
|---|---|---|---|
| `hose_id` | 16 | 16 mm | DECIDED — EDR-022 |
| `hose_od` | 22 | 22 mm | DECIDED — EDR-022 |
| `glass_t` | 5 | 5 mm | DECIDED range 5–12 — EDR-023 |
| `glass_t_max` | 12 | 12 mm | DECIDED — upper end of EDR-023; sizes the clip saddle |
| `tank_h` | 360 | 360 mm | REFERENCE — check at 450 |
| `tube_od` | 17 | 17 mm | TARGET — L-41 |
| `tube_wall` | 1.0 | 1 mm | TARGET (1.0–1.2) — L-41 |
| `tube_bore` | `tube_od - 2*tube_wall` | 15 mm | derived |
| `clr` | `1.5*tube_od` | 25.5 mm | **ASSUMPTION** — V-S2 |
| `straight_min` | `1.5*tube_od` | 25.5 mm | **ASSUMPTION** |
| `hook_above_rim_max` | 25 | 25 mm | TARGET — L-07 |
| `bridge_clear` | 3 | 3 mm | ASSUMPTION |
| `bridge_len` | 0 | 0 mm | ASSUMPTION (single 180° return) |
| `water_below_rim` | 25 | 25 mm | ASSUMPTION (20–30) |
| `substrate_h` | 60 | 60 mm | ASSUMPTION (50–100) |
| `out_nozzle_depth` | 90 | 90 mm | TARGET (70–110) — L-20 |
| `out_adjust` | 20 | 20 mm | TARGET — L-20/L-51 (not modelled as motion; expressed by the sliding collar) |
| `out_aim` | 30 | 30° | TARGET — L-51 (modelled at 0°, mid-aim; rotation in the collar) |
| `out_reach` | 55 | 55 mm | TARGET (40–70) — L-21 — **not met, see §2** |
| `nozzle_od_max` | `1.3*tube_od` | 22.1 mm | **ASSUMPTION** |
| `nozzle_len` | 20 | 20 mm | ASSUMPTION |
| `in_end_depth` | 240 | 240 mm | TARGET (230–250) — L-22 |
| `slot_zone` | 75 | 75 mm | TARGET (60–90) — L-23 |
| `slot_w` | 1.0 | 1 mm | TARGET (≤1.0) — L-30 |
| `slot_len` | 20 | 20 mm | ASSUMPTION |
| `slot_web` | `1.5*tube_wall` | 1.5 mm | ASSUMPTION |
| `slot_rows`, `slot_count` | 3, 18 | 54 slots | ASSUMPTION |
| `open_area_min` | `5*PI*tube_bore^2/4` | 883.6 mm² | TARGET — L-31 |
| `rear_offset_max` | 35 | 35 mm | TARGET — L-08 |
| `rear_drop` | 80 | 80 mm | TARGET (60–100) — L-08 |
| `hose_engage` | 22 | 22 mm | TARGET (20–25) — L-71 |
| `bead_h`, `bead_pitch`, `bead_end_offset` | 0.8, 8, 6 | mm | ASSUMPTION — V-T2 |
| `clip_t`, `clip_bend_r` | 1.5, `clip_t` | 1.5 mm | ASSUMPTION |
| `clip_w`, `clip_drop` | 26, 30 | mm | ASSUMPTION |
| `clip_saddle_inner` | `glass_t_max + 2*pad_t` | 16 mm | derived |
| `collar_margin`, `collar_clear`, `collar_slit` | 4, 0.2, 1.0 | mm | ASSUMPTION |
| `clip_wrap` | 210 | ° | **UNUSED** — left over from the abandoned wrap-cradle attempt |
| `pad_t`, `pad_h`, `pad_top_below_rim` | 2, 25, 3 | mm | ASSUMPTION |
| `pad_fit` | `(clip_saddle_inner - glass_t)/2` | 5.5 mm (2.0 at 12 mm glass) | derived |
| `cap_h`, `cap_spigot_len`, `cap_clearance`, `cap_chamfer` | 10, 8, 0.2, 0.5 | mm | ASSUMPTION |
| `pipe_spacing` | 250 | 250 mm | REFERENCE/ASSUMPTION — layout only |
| `hose_stub_len` | 30 | 30 mm | REFERENCE |
| `keepout_z0`, `keepout_h` | `hook_above_rim_max`, 30 | mm | REFERENCE placeholder — V-M2 |

## 2. Check table (brief §7)

Measured in the model (bounding boxes, sketch geometry, `analyzeInterference`, physical properties). Both configurations were solved from the same parameters; the model was returned to 5 mm / 360 mm before saving.

| Check | Target | Glass 5 mm, tank 360 | Glass 12 mm, tank 450 | Result |
|---|---|---|---|---|
| Hook height above rim (top of tube) | ≤ 25 mm | 20.0 | 20.0 | **pass** |
| In-tank leg centre to inner glass | 20–30 mm | 23.0 | **19.5** | pass at 5 mm; **0.5 mm short at 12 mm** (as the brief's §4.2 table predicted for `clr` = 1.5 OD, `bridge_len` = 0) |
| Rear leg centreline to outer glass | ≤ 35 mm | 23.0 | 19.5 | pass |
| Rear tip depth below rim | 60–100 mm | 80.0 | 80.0 | pass |
| Nozzle depth (centre) | 70–110 mm | 90.0 | 90.0 | pass |
| Nozzle reach from inner glass (tube end / nozzle mid / tip) | 40–70 mm | 74.0 / 84.0 / **94.0** | 70.5 / 80.5 / **90.5** | **fail — target left unmet.** Reach = leg offset + `clr` + `straight_min` + `nozzle_len`; meeting 40–70 would need a straight shorter than `straight_min` before the formed end (breaks M3) or a smaller `clr` (breaks M2) |
| Intake end (cap bottom) below rim | 230–250 mm | 240.0 | 240.0 | pass |
| Clearance above substrate | clear | 60.0 (120 above floor) | 150.0 | pass |
| Open area (54 × 1.0 × 20 mm) | ≥ 883.6 mm² | 1080 | 1080 | **pass**, 1.22×; web at the bore 1.62 mm ≥ `slot_web` |
| Slot zone position | ≥ 1 × OD from bends/ends | starts 17 mm above the tube end; 199 mm below the hook | — | pass |
| Every bend ≥ `clr` | 25.5 | inflow 25.5; outflow 25.5, 25.5 | same | pass (all bends exactly `clr`) |
| Straights ≥ `straight_min` | 25.5 | inflow 66 (rear), 216 (in-tank); outflow 66, 50.5, 25.5 | same | pass (outflow horizontal is exactly the minimum) |
| Clip bends ≥ `clip_t` | 1.5 | inner radius 1.5 | same | pass |
| Brush line of sight | straight from an open end to every wetted surface | Inflow: cap end → in-tank leg straight → **blind past the 180° hook**; hose end → rear leg → blind past the hook. Outflow: nozzle → horizontal → **blind past the 90° bend**; hose end → rear leg → blind past the hook | same | **partial / fail for r1a.** A 17 mm bore with 25.5 mm CLR bends cannot be brushed straight; a flexible brush is needed for the hook (and outflow elbow) |
| Clip flat pattern | one blank, no fasteners below rim | 131.6 × 26.0 × 1.5 mm blank, both clips; no fasteners at all | same | **pass** |
| Interference (product vs reference and product vs product) | designed contacts only | tube × hose 111.7 mm³ each (beads inside the hose — designed); tube × clip **0.28 mm³** each at the hook underside vs the saddle top strip (see §4) | tube × hose 391 mm³ each (hose stub now overlaps a bead zone fully — reference only); tube × clip 0.28 mm³ | pass with one near-touch to resolve |
| Set mass (2 pipes + cap + 2 clips, 316L) | ~0.3–0.4 kg (L-27) | **345 g** (inflow 137.7, outflow 115.5, cap 20.9, clips 2 × 35.5) | same | pass |
| Section (wall constant except formed ends) | — | Pipe feature: constant 1.0 mm wall; beads are added rings, nozzle is a 1.0 mm tapered wall | — | pass (visual section not captured) |

## 3. Assumptions made

Everything marked ASSUMPTION in §1, plus the following invented in the session and **not** in the brief's table: `slot_rows` 3, `slot_count` 18, `bead_end_offset` 6 mm, `nozzle_len` 20 mm, `cap_h` 10 mm, `cap_spigot_len` 8 mm, `cap_clearance` 0.2 mm, `cap_chamfer` 0.5 mm, `clip_w` 26 mm, `clip_drop` 30 mm, `clip_bend_r` = `clip_t`, `collar_margin` 4 mm, `collar_clear` 0.2 mm, `collar_slit` 1.0 mm, `pad_h` 25 mm, `pad_top_below_rim` 3 mm, `pipe_spacing` 250 mm, `keepout_z0`/`keepout_h`, `tank_h`, `hose_stub_len`. Also non-parametric choices: the nozzle family (straight-taper diffuser, ends formed), the slot orientation (axial slots in three rows around 18 positions), the bead form (half-round added ring rather than a rolled wall), the clip grip principle (collar tab), and the keep-out slab extents. All of these are recorded as decisions owed in `PRODUCT.md` §5a.

## 4. Problems, failed features, things stopped on

- **Clip first attempt was geometrically wrong.** The cradle was drawn as a partial loop in the vertical section; the pipe legs are vertical, so the loop passed through the tube (320 mm³ interference). A curl around a vertical tube off a horizontal arm is not a single-axis sheet-metal fold either. Replaced by the flat collar tab. The parameter `clip_wrap` remains in the file, marked UNUSED.
- **Near-touch at the saddle.** With `bridge_clear` = 3 mm at the apex, the 180° hook's underside is only ~1.5 mm above the rim at the saddle corners (±8.5 mm from the glass centre), so the 1.5 mm saddle top strip just touches it (0.28 mm³). Either `bridge_clear` ≥ 4.5 mm, a flat between hook bends (`bridge_len` > 0), or the hook rests intentionally on the saddle. Not resolved in the model — reported.
- **Outflow reach target unmet** (§2). Left unmet deliberately per brief §4.1 ("do not change the rule quietly").
- **Brush access** fails for the hook in this direction (§2).
- API/process failures fixed in session, none silently: a 180°-only pipe path (chaining picked one curve), a 90° bend stored as a 270° arc, an end cap anchored at the wrong end of its axis, a sketch `offset` that refuses a shared-point chain (clip now swept instead), and one interrupted script that left an arc-only stub which was found and rebuilt. Two connection drops occurred; the document was recovered by Fusion and saved as soon as the link returned.
- `CL_OUTFLOW` and `END_CAP` sketches report "not fully constrained" for one redundant-dimension reason each; their geometry follows the parameters correctly at both configurations.
- Three secondary-sketch dimensions were skipped as redundant; no geometry was hand-placed in the saved state.
- The reference water slab is opaque in the captures; a transparent appearance was not applied.

## 5. Review images (internal only — do not publish)

`products/aquarium/lily-pipes/design/concepts/images/`: `r1a_01_front_1m.png` (front through the glass, ~1 m), `r1a_02_top_rim_crossing.png`, `r1a_03_iso_45.png`, `r1a_04_clip_closeup.png`, `r1a_05_nozzle_closeup.png`, `r1a_06_intake_cap_closeup.png`. Viewport captures, satin stainless appearance, 1600 × 1000.

## 6. What r1a taught about Q1–Q6

- **Q1 (pipe or hose crosses the rim):** the pipe-crossing hook works dimensionally at 1.5 × OD — 20 mm above the rim, 23/19.5 mm standoff — but it costs brush access (no straight line of sight through a 180° return) and puts the whole clip below the waterline at 25 mm water depth. Those two are the strongest arguments to model r1b.
- **Q2 (20–30 mm standoff at a bendable radius):** yes at 5 mm glass, 0.5 mm short at 12 mm with `bridge_len` = 0; 10 mm of flat between the hook bends fixes it (brief §4.2) at the price of a wider crossing and a bigger saddle question. Everything hinges on whether a supplier bends 17 × 1.0 at 25.5 mm CLR (V-S2).
- **Q3 (clip as the signature):** because a symmetric hook keeps both legs symmetric about the glass centreline, **one clip part fits the whole 5–12 mm range**, with pads absorbing the 7 mm. The collar-tab clip is quiet and structurally honest, but it is submerged and its friction is only a schematic slit — retention needs V-T8 before it can carry the recognition role.
- **Q4 (nozzle from the flow job):** a plain 7° taper diffuser reads as function, not flower, but the reach targets and the bend rules are in direct conflict: 90–94 mm reach at 1.5 × OD. Either L-21 relaxes or the outflow needs a different form (e.g. the nozzle turned along the glass, or a shallower exit angle).
- **Q5 (≤1.0 mm slots, ≥5× bore):** met with margin (1080 vs 884 mm²) using 54 axial slots in three bands; 18 around a 17 mm tube leaves a 1.6 mm web at the bore. Whether three bands "look calm" is for the C1–C12 review; two bands would fall short (720 mm²).
- **Q6 (end cap reading):** a flush cap with a 0.5 mm chamfer parting line and an 8 mm spigot reads as a service detail rather than a bolt-on, but its retention (detent) and the 0.2 mm parting gap against PR-LS-03 are undecided.

## 7. Provenance

Parameters, constraints and checks were created and read by scripts run through the Fusion MCP; values above are printed from the model, not typed. The model is CONCEPT and stays CONCEPT until `PRODUCT.md` §5/§5a decisions are answered.
