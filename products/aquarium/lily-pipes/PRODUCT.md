# PRODUCT — Lily Pipes (`AQ-LP-A`)

| | |
|---|---|
| **Product ID** | `AQ-LP-A` |
| **Family** | Aquarium / Aquascaping |
| **Owner class** | A — Product |
| **Stage** | **Phase 0A research complete; decisions 1–3 answered (2026-09-17); CONCEPT CAD may start — no engineering** |
| **Authoritative CAD** | None |

> **2026-09-17 — Phase 0A research added.** Start at [README.md](README.md) and [CURRENT_STATE.md](CURRENT_STATE.md). The research widens decision 1 from "glass or acrylic" to glass / stainless steel / polymer and **proposes** (not approved) a stainless first product; see [DECISIONS_AND_OPEN_QUESTIONS.md](DECISIONS_AND_OPEN_QUESTIONS.md) §3, which maps decisions 1–6 below to D-02, D-04, D-06, D-08/D-18, D-12 and D-13. A **proposed launch specification (Rev P0, not approved)** with provisional values is in [AQ-LP-A-BRIEF_RevP0_launch-specification.md](requirements/AQ-LP-A-BRIEF_RevP0_launch-specification.md); §6 below remains true for decided values. The sections below are preserved as written on 2026-09-09.

---

## 1. What the product is

Glass or acrylic inlet and outlet pipes for planted aquariums — the visible plumbing between a canister filter and the tank, valued as much for appearance as for flow.

## 2. Why it exists

The lowest-technology product in the range and the one most dependent on manufacturing skill rather than design. It is also the clearest test of whether Trophic can make something in a material it has never worked: every other product in both families is steel, plastic or electronics.

## 3. Inherited constraints — DECIDED

**None.** No Trophic decision has been made about this product. It inherits the
identifier standard and, where it is an electronic device, the principle that a
device must be safe with no power and no signal. Nothing else.

## 3a. Product decisions — DECIDED (owner, 2026-09-17)

These are Trophic decisions for this product, not inherited constraints. A CONCEPT model may use them.

| # | Decision | Value | Record |
|---|---|---|---|
| 1 | Wetted material | Stainless steel: **316L specified; 304 qualified alternate** subject to V-T7; design must not depend on grade; grades never mixed in a lot | [EDR-021](../../../docs/decisions/records/EDR-021-lily-pipe-material-316l-with-304-alternate.md) |
| 2 | Hose size (launch) | **16 mm ID / 22 mm OD**; 12/16 later | [EDR-022](../../../docs/decisions/records/EDR-022-lily-pipe-hose-size-16-22.md) |
| 3 | Mounting range (launch) | **Rimless glass 5–12 mm**; rimmed tanks excluded | [EDR-023](../../../docs/decisions/records/EDR-023-lily-pipe-rimless-glass-5-12mm.md) |

Everything else in [AQ-LP-A-BRIEF_RevP0_launch-specification.md](requirements/AQ-LP-A-BRIEF_RevP0_launch-specification.md) (tube size, depths, slot width, finish, clip method, price) remains a **target**, not a decision.

## 4. Industry reference points — NOT TROPHIC DECISIONS

Typical market values, to bound the design space. **Not specifications. No drawing may
cite this section.**

| Item | Typical range | Note |
|---|---|---|
| Hose sizes | 12/16 mm and 16/22 mm ID/OD | Two sizes cover most canister filters. This is a real compatibility constraint |
| Material | Borosilicate glass; acrylic as the durable alternative | Glass is the aesthetic standard and the breakage complaint |
| Rim thickness accommodated | Rimless tanks, typically 5–12 mm glass | Determines the hook geometry |
| Forms | Inflow with strainer; outflow as spin/violet/poppy type | Named market forms, not Trophic designs |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | ~~Glass or acrylic — this is the whole product~~ **ANSWERED 2026-09-17: stainless, 316L with 304 alternate (EDR-021)** | Process, tooling, supplier, cost, failure mode |
| 2 | ~~Hose sizes supported~~ **ANSWERED 2026-09-17: 16/22 at launch (EDR-022)** | Every dimension |
| 3 | ~~Tank rim thickness range~~ **ANSWERED 2026-09-17: rimless 5–12 mm (EDR-023)** | Hook geometry |
| 4 | Outflow form(s) — **partly answered 2026-09-19: nozzle formed from the tube, aimed by a dry swivel above the waterline (EDR-024); the nozzle family itself is still open (round 2)** | The visible design, which is what sells it |
| 5 | Manufacture: in-house glasswork, or a specialist supplier to Trophic design | Whether this is a manufacturing product or a design-and-source product |
| 6 | Packaging — the product is fragile and returns are expensive | Cost, and it is usually an afterthought |
| 6a | ~~Skimmer with P1~~ **ANSWERED 2026-09-19: no skimmer in P1, no reserved interface (ADR-009)** | Scope |
| 6b | ~~Intake adjustment~~ **CLOSED 2026-09-19: none in P1 — EDR-025 withdrawn the same day; plain removable cap stands** | — |

### 5a. Decisions owed by concept round 1 (`AQ-LP-A_CONCEPT_r1a`, 2026-09-17)

Every value below was **invented to close the CONCEPT model** (`CAD_SEED_GUIDE.md` §6). None is a decision; each is a decision someone owes before the model class can change. Values and evidence routes are in [design/concepts/AQ-LP-A_CONCEPT_r1a_report.md](design/concepts/AQ-LP-A_CONCEPT_r1a_report.md).

| # | Decision required (assumption used in r1a) | Value used | Evidence that settles it |
|---|---|---|---|
| 7 | Bend centre-line radius `clr` | 1.5 × OD = 25.5 mm | Supplier bend samples V-S2 |
| 8 | Minimum straight between bends / before formed ends `straight_min` | 1.5 × OD = 25.5 mm | V-S2, bender clamp length |
| 9 | Hook form: rim-crossing gap `bridge_clear` and flat between hook bends `bridge_len` | 3 mm / 0 mm (single 180° return) | **Owner 2026-09-18 (D-22): hook rests on the clip saddle, `bridge_clear` = `clip_t`.** `bridge_len` still open |
| 10 | Reference water level and substrate depth (`water_below_rim`, `substrate_h`) | 25 mm / 60 mm | Tank measurement set V-M2 |
| 11 | Nozzle expansion limit and length (`nozzle_od_max`, `nozzle_len`) | 1.3 × OD = 22.1 mm / 20 mm | End-forming sample V-T3; flow test V-T9 |
| 12 | Slot length, web, rows and count (`slot_len`, `slot_web`, `slot_rows`, `slot_count`) | 20 mm / 1.5 mm / 3 / 18 | Shrimp-safety and flow test V-T5; laser trial |
| 13 | Hose bead height, pitch and end offset (`bead_h`, `bead_pitch`, `bead_end_offset`) | 0.8 mm / 8 mm / 6 mm | Pull-off test V-T2 |
| 14 | Clip sheet thickness and bend radius (`clip_t`, `clip_bend_r`) | 1.5 mm / 1.5 mm | Clip retention test V-T8; laser/brake trial |
| 15 | Clip strip width, saddle drop, collar tab margin, collar clearance and slit (`clip_w`, `clip_drop`, `collar_margin`, `collar_clear`, `collar_slit`) | 26 / 30 / 4 / 0.2 / 1.0 mm | V-T8; appearance review C1–C12 |
| 16 | Clip grip principle: flat collar tab the leg passes through (r1a) vs a wrap cradle or other | Collar tab | **Owner 2026-09-18 (D-23): develop the collar tab; spring/friction detail in round 2, sized by V-T8** |
| 17 | Pad thickness, height and set split (`pad_t`, `pad_h`, sets 5–8 / 8–12 mm) | 2 mm / 25 mm / two sets | Pad material V-T8 |
| 18 | End cap visible height, spigot length, clearance and parting chamfer (`cap_h`, `cap_spigot_len`, `cap_clearance`, `cap_chamfer`) | 10 / 8 / 0.2 / 0.5 mm | Detent design; livestock-safety check PR-LS-03 |
| 19 | Inflow-to-outflow spacing along the glass (`pipe_spacing`, layout only) | 250 mm | Interviews / V-M2 |
| 20 | Lid / light-leg keep-out above the rim (`keepout_z0`, `keepout_h`) | 25 mm / 30 mm placeholder | V-M2 |
| 21 | **Outflow reach target vs bend rules** — with `clr` and `straight_min` at 1.5 × OD the nozzle tip lands 90–94 mm from the inner glass; the 40–70 mm target (L-21) cannot be met without breaking M2/M3 | target left unmet | **Owner 2026-09-18 (D-21): L-21 relaxed to 70–100 mm; bend rules kept.** Confirm by V-T9 |
| 22 | **Brush access through a 180° hook** — a straight brush cannot pass the return bend from either open end (M6/L-34) | unresolved for r1a | **Owner 2026-09-18 (D-20): build r1b before choosing** |
| 23 | r1b: in-tank leg standoff drives the pipe position (`leg_standoff`) | 25 mm | Interviews / V-M2; appearance review |
| 24 | r1b: pipe top above the rim for hose fitting (`pipe_top_above_rim`) and saddle drop with collar above the waterline (`clip_drop_b`, `pad_h_b`) | 15 / 15 / 10 mm | V-M2, V-T8 |
| 25 | **r1b: free-hose bend radius (`hose_bend_r`)** — at 4 × OD (88 mm) the loop stands 114 mm above the rim and 146 mm out from the glass; at 30 mm it is 56 mm / 30 mm but a 16/22 hose will kink | 4 × OD | V-M1 measure the real kink radius of the specified hose; decide whether a formed hose guide / elbow is part of the product (D-09) |
| 26 | r1b: hose crossing is a bought or specified part, not Trophic geometry — the visible rim crossing is then outside Trophic's control | — | D-09; appearance review C1–C12 |
| 27 | r2a swivel (EDR-024): socket mouth height, engagement, cone, ring section/width, clearance, spigot gap, stub top margin (`swivel_mouth_above_rim`, `swivel_engage`, `swivel_cone`, `swivel_ring_t`, `swivel_ring_w`, `swivel_clear`, `stub_gap`, `stub_top_margin`) | 10 / 15 / 4 / 0.5 / 4 / 0.1 / 1 / 6 mm | Formed-socket sample from the tube former; ring material (PTFE vs silicone); 50-cycle rotate/leak test |
| 28 | r2a swivel retention: a stop bead on the spigot rests on the socket mouth; pull-out retention is the ring's friction only | schematic | Friction/pull-out test; consider a rolled retaining groove if the sample pulls out under hose load |
| 29 | ~~r2a telescopic cap (EDR-025)~~ **withdrawn 2026-09-19; parameters left UNUSED in the model** — was: travel, minimum engagement, floor, clearance, band section/width/interference, lip, plain tube below the slots (`cap_travel`, `cap_engage_min`, `cap_floor`, `cap_clear`, `band_t`, `band_w`, `band_interf`, `cap_lip`, `slot_from_end`) | 2 rows + gap = 47.5 / 12 / 3 / 0.15 / 1.5 / 4 / 0.2 / 2 / 17 mm | Slide test 200 cycles; V-T5 at every position; laser ovality data. **The 62.5 mm cup reads long — consider `cap_travel` = one row (27.5 mm)** |
| 30 | ~~r2a: `in_end_depth` (240) now refers to the cup bottom~~ **reverted in r2b: 240 is the cap bottom, tube ends at 230, slot band 153–213 below the rim** — was: at the fully **open** position; the tube itself ends at 189.5 and the slot zone sits 97.5–172.5 mm below the rim | derived | Interviews / V-M2 (is a shorter intake acceptable?) |
| 31 | ~~r2a hose guide~~ **dropped in r2b after CMF review (ornament); a low rest tab folded from the clip was tried and could not be proven as one blank in CAD; loop shape now belongs to the hose spec (D-28)** — was: a separate one-blank sheet part (16 × 1.5 mm strip) with a foot on the J-clip saddle, stem, and a 270° curl of centreline radius 18.25 mm under a 30 mm hose loop; joined to the saddle **dry, above the rim** by spot/laser weld or rivet (`hose_guide_r`, `guide_tab_w`, `guide_foot`, `guide_wrap`, `guide_stem_x`, `hose_straight`) | 30 / 16 / 10 / 270° / 0 / 8 mm | V-M1 (does a supported 16/22 hose take R30?); the joining method is an owner decision (fastener rule D-19 is for wet parts) |
| 32 | r2a: inflow pipe top raised to 20 mm above the rim so the guide curl clears the saddle; hose loop tops at 69 mm (inflow) and 87 mm (outflow) above the rim — **the lid / light-leg keep-out placeholder (25 mm) is violated by any hose-over-rim form**; L-07 is met by the pipes, not by the hose | 20 mm | V-M2 lid and light-leg measurements; owner to decide whether L-07 applies to the hose |
| 33 | r2b: socket mouth at rim level, 12 mm engagement, 4 mm cone; stub top and inflow top both at 25 mm (= `hook_above_rim_max`); spigot bottom 12 mm below the rim, 13 mm above the water plane; no stop bead — the spigot rests on the socket cone, pull-out retention is the PTFE ring's friction only | 0 / 12 / 4 / 25 / 3 mm | Formed-socket sample; 50-cycle rotate/leak; pull-out under hose load (add a rolled retaining groove if it fails) |
| 34 | r2b: one slot band of 18 × 60 × 1.0 mm (1080 mm²) instead of three rows — long 1.6 mm webs | one band, 153–213 mm below rim | Laser trial for distortion and web strength (M5); V-T5 |
| 35 | r2b: nozzle taper 24 mm (~1.4 D) so the tip sits at the 100 mm reach limit; CMF asked ≥1.5 D | 24 mm | V-T9 (exit velocity at 4.5° half-angle); owner: reach limit vs taper length |
| 36 | r2b: clip saddle drop 18 mm (collar 16.5–18 below rim, below the socket cone, 7 mm above the water plane); pads matte dark grey/black per CMF | 18 mm | V-T8; appearance review |

## 6. Explicitly not decided

Nothing. **Do not infer dimensions from any competitor product.** A generated model
that happens to match a market part is a copy, not a design.

No dimensions, no materials, no BOM, no cost, no performance figures of any kind.

## 7. Interfaces

Platform **mechanical** standards do not apply — they are written for fabricated steel
structural products. Platform **electrical** standards apply only in principle
(fail-safe, connector discipline); the CEA mains protection schedule does not.

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **Yes, class CONCEPT (from 2026-09-17)** — decisions 1–3 are answered (§3a). Follow [CONCEPT_DESIGN_BRIEF.md](design/CONCEPT_DESIGN_BRIEF.md). *Original 2026-09-09 answer: massing only, after decisions 2 and 3* |
| Good for | Visualising a form language, discussing proportion |
| Must NOT be inferred | Wall thickness, bend radii, slot geometry, nozzle flare, manufacturability. Stainless tube bending and end forming have limits a CAD model will not respect on its own; supplier samples (V-S2) set them |

## 9. Next action

**Current (2026-09-17):** start concept round 1 in Fusion 360 from [CONCEPT_DESIGN_BRIEF.md](design/CONCEPT_DESIGN_BRIEF.md) (class CONCEPT, `AQ-LP-A_CONCEPT_r1*`), in parallel with Stage 0B evidence (supplier bend samples, hose measurements, interviews).

*Superseded (2026-09-17, earlier):* owner reviews the decision brief and decides D-01 and D-02.

*Original (2026-09-09):* Decide 1 (glass or acrylic). Nothing else can be usefully discussed until it is settled — the two materials share almost no design logic.
