# AQ-LP-A — Prompt to start concept round 1 in Fusion 360

**Use:** paste the block below into a Claude Code session opened at the `trophic-hardware` repository root with the Fusion 360 connection active. Run it once per direction (change `DIRECTION`). It follows `docs/system/CAD_SEED_GUIDE.md` §5 and the lessons from the rack's Fusion work (ECP-01).
**Class:** CONCEPT only. **Date:** 2026-09-17.

```text
DIRECTION = r1a   # r1a = pipe crosses the rim · r1b = hose crosses the rim, pipe stays inside · r1c = clip variant on the stronger of r1a/r1b

ROLE AND AUTHORITY
You are building a class-CONCEPT Fusion 360 model of the Trophic lily-pipe set AQ-LP-A.
No dimension in this model is a decision. You may not create drawings, STEP releases,
or rename anything to DESIGN. You may not open, edit or save any RK-A / CEA design.

READ FIRST (in this order, nothing else unless needed)
1. CLAUDE.md
2. docs/system/CAD_SEED_GUIDE.md
3. products/aquarium/lily-pipes/PRODUCT.md  (§3a DECIDED, §5 open)
4. products/aquarium/lily-pipes/design/CONCEPT_DESIGN_BRIEF.md  (the working brief — follow it)
5. docs/engineering/CAD_INDEX.md  §1 (hub/project)

DIMENSION RULES
- DECIDED values (PRODUCT.md §3a / EDR-021, EDR-022, EDR-023) may drive geometry:
  stainless tube, hose 16 mm ID / 22 mm OD, rimless glass 5–12 mm.
- TARGET and ASSUMPTION values come ONLY from CONCEPT_DESIGN_BRIEF.md §4.1, entered as
  Fusion user parameters with the class written in each parameter's comment.
- Do NOT use any competitor's dimensions or shapes, industry reference points copied as
  values, anything in archive/, or earlier concept output as a constraint.
- Every value you invent to close the model is an ASSUMPTION: name it as a parameter,
  and list it in your report.
- The form must not depend on 316L vs 304.

FUSION SETUP
- Project: the hub/project in CAD_INDEX.md §1. Create folder "AQ-LP-A" if absent.
- New design named "AQ-LP-A_CONCEPT_<DIRECTION>"; description starts "CONCEPT — not a design".
- Units mm. Remember the API works in cm internally (mm × 0.1).
- Create the component tree in brief §3 (00_REF_TANK, 01_REF_HOSE, 02_REF_KEEPOUT,
  10_INFLOW/11_END_CAP, 20_OUTFLOW, 30_CLIP_IN, 31_CLIP_OUT, 40_PADS).
- Create all user parameters in brief §4.1 before any geometry.

BUILD SEQUENCE (brief §5) — execute in small chunks; after EACH chunk, report a one-line
result and check body counts per component
1. Reference tank at glass_t = 5, tank height 360: glass slab, rim at Z=0, water plane,
   substrate plane. Reference only.
2. Centreline sketches for inflow and outflow: lines + tangent arcs of radius clr, fully
   dimensioned by parameters, constrained to the glass faces and rim.
   For r1a use the hook relations in brief §4.2; for r1b keep the pipe inside the glass and
   route a reference hose over the rim.
3. Pipe feature on each path: circular, tube_od, hollow, tube_wall. One continuous body per pipe.
4. Two hose-retention beads within hose_engage of each rear tip; reference hose stubs 16/22.
5. Outflow nozzle by revolve/loft from the tube end, max diameter ≤ nozzle_od_max, aimed by
   out_aim. One nozzle family only in this pass; no petal/bloom/bell forms.
6. Intake slot zone: one slot (slot_w × slot_len) cut through the wall, then patterned inside
   slot_zone, respecting slot_web and ≥ 1 × tube_od from bends/ends. Report total open area
   vs open_area_min; if short, report the shortfall — do not widen slots.
7. End cap as a separate body in 11_END_CAP with a clear parting line; no thread, no O-ring.
8. Clip in Sheet Metal: rule 316L, thickness clip_t, bend radius ≥ clip_t; spans tube to glass,
   carries pads on both glass faces, no fasteners below the rim. Must produce a Flat Pattern.
9. Pads (5–8 mm and 8–12 mm sets) as reference bodies in 40_PADS.
10. Repeat the fit checks at glass_t = 12 and tank height 450.

SAFETY RULES LEARNED ON RK-A
- Every cut/combine must set explicit participant bodies limited to the target component.
  Never let a cut touch reference or other product bodies.
- Make each step idempotent: check whether the component/feature already exists first.
- Do not save a new version over a design you did not create in this session.
- If a feature fails or geometry looks wrong, stop and report; do not work around it silently.

CHECKS (brief §7) — report measured values in a table
Hook height above rim (≤ 25) · in-tank leg centre to inner glass at 5 and 12 mm glass
(target 20–30) · rear leg centreline to outer glass (≤ 35) and rear tip depth (60–100) ·
nozzle depth (70–110) and reach (40–70) · intake end depth (230–250) and clearance above
substrate in the 360 mm tank · open area vs open_area_min · every bend ≥ clr · straights ≥
straight_min · brush line of sight (section analysis) · clip flat pattern OK · interference:
only designed contacts · set mass.

AFTER BUILDING
- Save the design. Report its lineage URN and version.
- Capture viewport images for INTERNAL review only: front through glass at ~1 m, top-down
  rim crossing, 45° from above, clip close-up, nozzle close-up, intake/end-cap close-up.
  Satin stainless appearance; no mirror/chrome.
- Then, in the repository:
  a) add a row for the design to docs/engineering/CAD_INDEX.md §2 with Class = CONCEPT;
  b) add every ASSUMPTION used to products/aquarium/lily-pipes/PRODUCT.md §5 as decisions still owed;
  c) write products/aquarium/lily-pipes/design/concepts/AQ-LP-A_CONCEPT_<DIRECTION>_report.md with the
     parameter values, the check table, the assumptions list, image paths, and 3–5 lines
     answering brief §1 questions Q1–Q6 for this direction.
- Do NOT post images publicly, send geometry to suppliers, or create drawings.

FINAL REPLY FORMAT
1. What was built (components, bodies, parameters).
2. Check table with pass / fail / shortfall.
3. Every assumption made (the CAD_SEED_GUIDE says a run with no assumptions is hiding something).
4. Problems, failed features, anything you stopped on.
5. What this direction taught about Q1–Q6.
```

## If Fusion is not connected

Use the same block as your own step list in Fusion: create the parameters from the brief §4.1, follow build steps 1–10, and fill in the check table by hand. Then ask Claude to do the "After building" repository steps.
