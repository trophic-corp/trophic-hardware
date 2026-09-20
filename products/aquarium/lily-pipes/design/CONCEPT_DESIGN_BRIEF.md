# AQ-LP-A — Concept Design Brief for Fusion 360 (Round 1)

| | |
|---|---|
| **Model class** | **CONCEPT** (`docs/system/CAD_SEED_GUIDE.md` §2). No dimension in a concept model is a decision |
| **Model names** | `AQ-LP-A_CONCEPT_r1a`, `_r1b`, `_r1c` (one design per direction) |
| **Date** | 2026-09-17 |
| **Unblocked by** | Owner decisions 1–3: [EDR-021](../../../../docs/decisions/records/EDR-021-lily-pipe-material-316l-with-304-alternate.md) stainless 316L (304 alternate) · [EDR-022](../../../../docs/decisions/records/EDR-022-lily-pipe-hose-size-16-22.md) 16/22 hose · [EDR-023](../../../../docs/decisions/records/EDR-023-lily-pipe-rimless-glass-5-12mm.md) rimless 5–12 mm glass |
| **Not allowed from this round** | Drawings, supplier tooling, STEP release, public images (IP — see §9), promotion to DESIGN by editing |

---

## 1. Purpose of round 1

Produce **two or three concept directions** of the launch set (inflow, outflow, clip) that can be judged side by side on:

1. **Look** — the Trophic target reaction: "They cared about every detail; this is a premium, thoughtfully engineered product" ([LILY_PIPE_AESTHETIC_REFERENCE.md](../../../../docs/references/lily-pipes/LILY_PIPE_AESTHETIC_REFERENCE.md) §1).
2. **Function fit** — the geometry targets in §4 of this brief.
3. **Makeability** — the stainless tube and sheet rules in §6.

Round 1 answers questions. It does not settle a form. Expect to discard most of it (`CAD_SEED_GUIDE.md` §7).

**Questions round 1 must answer**

| # | Question | Why it matters |
|---|---|---|
| Q1 | Does the **pipe** cross the rim, or does the **hose** cross the rim and the pipe stay inside the tank? | Sets the hook geometry, how visible the rim crossing is, the clip's job, and the hose kink risk. Both are open |
| Q2 | Can the in-tank leg sit **20–30 mm from the glass** at a bend radius a supplier can realistically bend? | Visual weight in the tank against bending limits (§4.2) |
| Q3 | Is the **clip** strong enough to be the one signature detail (D-08), while staying quiet? | Recognisability without ornament |
| Q4 | What **nozzle** family comes from the flow job (surface current) without reading as a flower? | Distinctive by function, anti-mimicry |
| Q5 | Can a **≤1.0 mm slot** pattern reach **≥5× bore open area** in a 60–90 mm zone and still look calm? | Shrimp safety against flow against appearance |
| Q6 | How does the **removable intake end cap** read: a service detail or a bolt-on? | "Function is the decoration" |

## 2. Inputs — and what kind of input each one is

| Class | Meaning in the model | Items |
|---|---|---|
| **DECIDED** | May drive geometry as a fixed value | Stainless tube; hose 16 mm ID / 22 mm OD; rimless glass 5–12 mm; no rimmed-tank support |
| **TARGET** | Drives geometry as a parameter you expect to change | Values from [AQ-LP-A-BRIEF_RevP0_launch-specification.md](../requirements/AQ-LP-A-BRIEF_RevP0_launch-specification.md): tube size, depths, reach, slot width, open area, hook height, rear offset, hose engagement |
| **ASSUMPTION** | Invented to close the model; **must be listed** in the round report and added to `PRODUCT.md` §5 | Bend radius, straight lengths between bends, bead size, sheet thickness, pad thickness, nozzle expansion, slot web width |
| **FORBIDDEN** | Must not be used | Any competitor's dimensions or shape; anything in `archive/`; industry reference points copied as values; earlier concept output treated as a constraint |

The design must work with **either 316L or 304**. Nothing in the form may depend on the grade (EDR-021).

## 3. Fusion 360 setup

| Item | Setting |
|---|---|
| Hub / project | Karthikeyan D / Karthikeyan's First Project (`docs/engineering/CAD_INDEX.md` §1); create folder **`AQ-LP-A`** |
| Design | One design per direction: `AQ-LP-A_CONCEPT_r1a` etc. Put "CONCEPT" in the name and the design description |
| Units | mm, degrees |
| Modelling approach | Parametric, **skeleton first**: drive paths from user parameters, build bodies from paths |
| Physical material | Closest stainless 316/316L material in the Fusion library (mass estimates only) |
| Appearance | A satin or brushed stainless appearance for renders; **no mirror or chrome** (launch spec L-43) |

**Component structure (suggested)**

```
AQ-LP-A_CONCEPT_r1x
├── 00_REF_TANK          (not product) glass wall slab, glass edge, water plane, substrate plane — two configurations: 5 mm/360 mm tall, 12 mm/450 mm tall
├── 01_REF_HOSE          (not product) 16/22 hose stubs on each pipe end
├── 02_REF_KEEPOUT       (not product) lid/light-leg zone above rim — placeholder until measured (V-M2)
├── 10_INFLOW            tube body, slot zone, bead zone
│   └── 11_END_CAP       removable intake cap
├── 20_OUTFLOW           tube body, nozzle, bead zone
├── 30_CLIP_IN           clip for inflow (sheet metal)
├── 31_CLIP_OUT          clip for outflow (sheet metal; same part if possible)
└── 40_PADS              pad sets 5–8 mm and 8–12 mm (reference geometry)
```

Keep reference components in their own components so they never get confused with product parts in a later export.

## 4. User parameters

Enter them in **Modify → Change Parameters → User Parameters**. Names are suggestions; keep the Class in each parameter's comment field so the model carries its own status.

### 4.1 Parameter table

| Name | Expression | Unit | Class | Source / note |
|---|---|---|---|---|
| `hose_id` | 16 | mm | DECIDED | EDR-022 |
| `hose_od` | 22 | mm | DECIDED | EDR-022 |
| `glass_t` | 5 (switch to 12 for the second check) | mm | DECIDED range 5–12 | EDR-023 |
| `tube_od` | 17 | mm | TARGET | L-41; pipe OD ≈ hose ID + 1 mm |
| `tube_wall` | 1.0 | mm | TARGET (1.0–1.2) | L-41 |
| `tube_bore` | `tube_od - 2 * tube_wall` | mm | derived | ≈15 mm |
| `clr` | `1.5 * tube_od` | mm | **ASSUMPTION** | Bend centre-line radius; supplier sample V-S2 sets the real minimum |
| `straight_min` | `1.5 * tube_od` | mm | **ASSUMPTION** | Straight length between bends and next to formed ends, for bender clamping |
| `hook_above_rim_max` | 25 | mm | TARGET | L-07: top of anything above the glass edge |
| `bridge_clear` | 3 | mm | ASSUMPTION | Gap between glass edge and underside of the rim-crossing part |
| `bridge_len` | 0 | mm | ASSUMPTION | Straight between two 90° hook bends (0 = one 180° return) |
| `water_below_rim` | 25 | mm | ASSUMPTION (20–30) | Reference water plane |
| `substrate_h` | 60 | mm | ASSUMPTION (50–100) | Reference substrate plane |
| `out_nozzle_depth` | 90 | mm | TARGET (70–110) | L-20: nozzle centre below rim |
| `out_adjust` | 20 | mm | TARGET | L-20/L-51: ± height travel at the clip |
| `out_aim` | 30 | deg | TARGET | L-51: ± aim |
| `out_reach` | 55 | mm | TARGET (40–70) | L-21: nozzle reach from inner glass face |
| `nozzle_od_max` | `1.3 * tube_od` | mm | **ASSUMPTION** | Formable expansion limit; confirm by end-forming sample |
| `in_end_depth` | 240 | mm | TARGET (230–250) | L-22: intake end below rim |
| `slot_zone` | 75 | mm | TARGET (60–90) | L-23 |
| `slot_w` | 1.0 | mm | TARGET (≤1.0) | L-30 |
| `slot_len` | 20 | mm | ASSUMPTION | Per slot |
| `slot_web` | `1.5 * tube_wall` | mm | ASSUMPTION | Minimum metal between slots |
| `open_area_min` | `5 * PI * tube_bore ^ 2 / 4` | mm^2 | TARGET | L-31; ≈880 mm² at a 15 mm bore |
| *(check only)* centre to inner glass | 20–30 | mm | TARGET | L-24; **not a user parameter** — measure it, don't drive it (§4.2) |
| `rear_offset_max` | 35 | mm | TARGET | L-08: hose-end leg centreline from outer glass face |
| `rear_drop` | 80 | mm | TARGET (60–100) | L-08: hose-end tip below rim |
| `hose_engage` | 22 | mm | TARGET (20–25) | L-71 |
| `bead_h` | 0.8 | mm | ASSUMPTION | Bead height above tube OD; pull-off test V-T2 sets it |
| `bead_pitch` | 8 | mm | ASSUMPTION | Two beads within `hose_engage` |
| `clip_t` | 1.5 | mm | ASSUMPTION | 316L sheet; bend radius ≥ `clip_t` |
| `pad_t` | 2 | mm | ASSUMPTION | Silicone pad; two pad sets cover 5–8 and 8–12 mm |

If a TARGET cannot be met without breaking a rule in §6, **leave the TARGET unmet and report it** — do not change the rule quietly.

### 4.2 Hook geometry — the relationship to check first

If the pipe crosses the rim (Q1 option "pipe crosses"), the hook is two 90° bends with an optional straight between them. Then:

- Leg centre spacing **S = 2 × clr + bridge_len**
- Face-to-face space between the legs **= S − tube_od**
- Gap on each side of the glass **g = (S − tube_od − glass_t) / 2**
- In-tank leg centre to inner glass face **= g + tube_od / 2**

Worked values with `tube_od` = 17 mm (hand calculation — check in the model):

| `clr` | `bridge_len` | Glass 5 mm: centre-to-glass | Glass 12 mm: centre-to-glass | Meets 20–30 mm target? |
|---|---|---|---|---|
| 25.5 mm (1.5 × OD) | 0 | 23.0 mm | 19.5 mm | Yes (just) |
| 25.5 mm | 10 | 28.0 mm | 24.5 mm | Yes |
| 34 mm (2 × OD) | 0 | 31.5 mm | 28.0 mm | Only at 12 mm glass |
| 34 mm | 10 | 36.5 mm | 33.0 mm | No |

What this means:

- **The 20–30 mm target needs a bend radius near 1.5 × OD** on thin-wall tube. That is the first question for the bending supplier. If the achievable radius is nearer 2 × OD, either the in-tank leg moves further from the glass or the "hose crosses the rim" option wins.
- **The gap per side (about 11–20 mm) is the clip's job.** The clip and pads span it and absorb the 7 mm glass range. That makes the clip structurally necessary, which suits its role as the signature detail.
- **The in-tank leg and the rear leg sit the same distance from the glass** with a symmetric hook. `rear_offset_max` (rear-leg centreline ≤35 mm from the outer glass face) is met in the first three rows, not the fourth.

## 5. Modelling sequence (suggested)

1. **Reference tank.** In `00_REF_TANK`, sketch the glass wall section on the XZ plane: glass thickness `glass_t`, rim at Z = 0, water plane at −`water_below_rim`, substrate at the tank floor + `substrate_h`. Save two configurations or swap `glass_t` 5 ↔ 12 and tank height 360 ↔ 450.
2. **Skeleton paths.** In `10_INFLOW` and `20_OUTFLOW`, draw each pipe centreline as one sketch of lines and **tangent arcs of radius `clr`**, dimensioned only with parameters. Constrain it to the reference glass (rim, inner face, outer face).
3. **Tube bodies.** Use **Create → Pipe** on each path with section = circular, size = `tube_od`, **Hollow** with thickness = `tube_wall`. One continuous body per pipe (one-piece bent tube, no joints).
4. **Hose-end beads.** Revolve two small bead profiles within `hose_engage` of the rear tip. Model a reference hose stub in `01_REF_HOSE` (ID 16, OD 22, 22 mm overlap) and check it visually.
5. **Nozzle (outflow).** Revolve or loft the termination from the tube end, keeping the largest diameter ≤ `nozzle_od_max` and a smooth wall (end-formed, not welded). Aim it with `out_aim` about the vertical axis. Try one or two nozzle families per direction.
6. **Intake slot zone (inflow).** Sketch one slot (`slot_w` × `slot_len`) on a plane tangent to the tube, cut through the wall, then **circular and rectangular pattern** it inside `slot_zone`. Use **Inspect → Measure** (or the cut profile areas) to confirm total open area ≥ `open_area_min`. If you cannot reach it at `slot_w` ≤ 1.0 mm, record the shortfall (Q5).
7. **End cap.** In `11_END_CAP`, model the removable cap as a separate body with a visible, intentional parting line. Represent the detent only as a note or simple feature; no thread, no O-ring (L-33).
8. **Clip.** In `30_CLIP_IN`, switch to **Sheet Metal**, create a rule for 316L at `clip_t` with bend radius ≥ `clip_t`, and build a flange-and-bend part that spans tube to glass and carries the pads. Check **Create Flat Pattern** succeeds: the clip must lay flat as one laser-cut blank. Express height and aim adjustment in the form; the friction mechanism can stay schematic in round 1.
9. **Pads.** Model pad sets for 5–8 mm and 8–12 mm glass as reference bodies in `40_PADS`.
10. **Checks** (§7), then renders (§8).

## 6. Rules the concept must respect

### 6.1 Makeability (stainless tube and sheet)

| # | Rule | Class | Why |
|---|---|---|---|
| M1 | One continuous tube per pipe; constant OD and wall except at formed ends | DECIDED direction (L-40, EDR-021) | No welds or joints in the water |
| M2 | Bend radius ≥ `clr`; no compound bends tighter than that | ASSUMPTION until V-S2 | Thin-wall wrinkling and ovality |
| M3 | Straight ≥ `straight_min` between bends and next to formed ends or the slot zone | ASSUMPTION | Bender clamping; laser fixturing |
| M4 | Nozzle and beads formed at tube ends only; nozzle ≤ `nozzle_od_max` | ASSUMPTION | End-forming limits |
| M5 | Slots only in straight tube, at least 1 × `tube_od` from any bend or formed end; webs ≥ `slot_web` | ASSUMPTION | Laser distortion, strength, bending after slotting |
| M6 | Every internal surface reachable by a straight brush from an open end (inflow via removable cap; outflow via nozzle) | TARGET (L-34, L-52) | Cleaning is the core promise |
| M7 | Clip is one flat-pattern sheet part (plus pads); no fasteners below the rim | TARGET (L-60, L-64) | Laser-cut and formed; wet fasteners corrode |
| M8 | No gap or crevice in wetted areas where a juvenile shrimp could be trapped or pinched; parting lines either closed or open wide | TARGET (PR-LS-03) | Livestock safety |
| M9 | Laser mark only above water (top of the rim crossing) | TARGET (L-80) | Marking can start corrosion |
| M10 | Form must be identical for 316L and 304 | DECIDED (EDR-021) | Grade-independent design |

### 6.2 Appearance (Trophic direction — criteria, not forms)

- **Quiet in the tank, rewarding in the hand.** Judge the in-water view from 1 m first.
- **Function is the decoration.** Every visible feature does a job: slots, beads, cap line, clip, nozzle. Nothing added to look expensive.
- **One primary recognition cue.** Candidate is the clip (D-08). Keep nozzle and cap quiet unless the direction deliberately tests another cue.
- **One bend-radius rule** shared by inflow and outflow, so the pair reads as a family.
- **No petal, bloom, bell or flower** readings for the nozzle; no jewellery, chrome or mirror look.
- **Anti-mimicry check** against ADA Lily Pipe P/V, ADA Poppy, Cal Aqua Labs funnel, Aquario Neo Flow joints, Chihiros slim stainless and Week Aqua curved steel ([LILY_PIPE_AESTHETIC_REFERENCE.md](../../../../docs/references/lily-pipes/LILY_PIPE_AESTHETIC_REFERENCE.md) §6 Q9). Do not look up their dimensions for this work.
- **The unused skimmer interface must not show** (L-35): keep the straight through the water-surface zone clean.
- **Designed for real use:** consider fingerprints above water, scale at the waterline and a brushed satin finish that wears evenly.

### 6.3 Suggested directions for round 1 (exploration axes, not forms)

| Direction | Varies | Holds constant |
|---|---|---|
| **r1a — Pipe crosses the rim** | Two-bend hook with the clip spanning the gap; clip as signature | All §6 rules |
| **r1b — Hose crosses the rim** | Pipe stays inside the glass; clip holds a straight top section; hose loops over the rim | All §6 rules; check hose kink and rim-crossing appearance |
| **r1c — Clip variant (optional)** | Same pipe as the stronger of r1a/r1b; a clearly different clip expression and adjustment language | Pipes unchanged, so only the clip is judged |

## 7. Checks before calling a direction "done" for round 1

| Check | How in Fusion | Pass condition |
|---|---|---|
| Hook height | Measure from glass edge to highest point | ≤ `hook_above_rim_max` |
| Centre to inner glass | Measure at 5 mm and 12 mm glass | 20–30 mm (report actual) |
| Rear offset and drop | Measure hose-end leg | Centreline ≤ 35 mm from outer face; tip 60–100 mm below rim |
| Nozzle depth and reach | Measure to water and glass | Within §4 targets at the mid adjustment |
| Intake end depth | Measure; check above substrate in the 360 mm tank | 230–250 mm below rim; clear of substrate |
| Open area | Sum of slot areas | ≥ `open_area_min` with `slot_w` ≤ 1.0 mm, or shortfall reported |
| Bend radius | Inspect curvature or sketch dimensions | Every bend ≥ `clr` |
| Straights | Measure between bends, slots, ends | ≥ `straight_min` |
| Brush access | Section Analysis along each pipe | Straight line of sight from an open end to all internal surfaces, or report the blind zones |
| Clip | Flat Pattern | Unfolds as one blank; no fasteners below rim |
| Interference | Inspect → Interference (product parts vs reference glass/hose) | Only designed contacts (pads on glass, hose on beads) |
| Mass | Inspect → Properties | Report; expect roughly 0.3–0.4 kg for a set (L-27, EST) |
| Section | Section Analysis through bead zone and nozzle | Wall shown constant except at formed ends |

## 8. Round 1 deliverables

For each direction:

1. The Fusion design `AQ-LP-A_CONCEPT_r1x` with parameters named as in §4.
2. Renders with the satin stainless appearance, **for internal review only**:
   - front view from about 1 m through the glass, with the water plane visible
   - top-down view showing the rim crossing
   - 45° view from above
   - close-up of the clip on the rim
   - close-up of the nozzle and of the intake with its cap
3. A **check table** (§7) with measured values.
4. An **assumptions list**: every ASSUMPTION parameter actually used, plus anything else invented to close the model.
5. Three lines on what the direction taught (Q1–Q6).

## 9. After round 1 — what happens to the output

| Step | Who | Where |
|---|---|---|
| Record each concept design with class CONCEPT, lineage and version | You or Claude | `docs/engineering/CAD_INDEX.md` §2 |
| Add the assumptions list as decisions still owed | Claude | `products/aquarium/lily-pipes/PRODUCT.md` §5 |
| Appearance review against the C1–C12 rubric and anti-mimicry list | `industrial-design-cmf` specialist | Review note in this folder |
| DFM review of bends, slots, end forming and clip flat pattern | `manufacturing-sourcing-engineer` specialist | Same review note; drives the V-S2 sample request |
| Choose the direction(s) for round 2 | Owner | `DECISIONS_AND_OPEN_QUESTIONS.md` |
| Share geometry with suppliers for bend/end-form samples | Owner, under an NDA and after the IP attorney has advised | RFQ (SOURCING §6) |
| **Do not** post renders publicly, list pre-orders with images, or send to marketplaces | — | Design-registration novelty (SOURCING §8) |
| **Do not** issue drawings or releases, or rename a concept to DESIGN | — | `CAD_SEED_GUIDE.md` §2, §6 |

## 10. What stays open while you model

Tube size and wall (RFQ), bend radius (V-S2), bead geometry (V-T2), slot width and open area (V-T5), nozzle geometry (V-T3/V-T9), depths and reach (V-M2/V-T9), clip mechanism and pad material (V-T8), finish (V-T7/V-A3), primary recognition cue (D-08), and whether Trophic specifies the hose (D-09). A concept that makes one of these look settled has not settled it.
