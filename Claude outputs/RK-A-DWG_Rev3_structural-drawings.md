# RK-A-DWG Rev 3 — Structural Drawings, CEA Rack Platform (Rack A)

| | |
|---|---|
| **Document** | RK-A-DWG · Rev 3 · 10 September 2026 · structural set, ECP-01 |
| **Supersedes** | Rev 2 (2026-09-05) for the parts listed below. Sheets for RK-A-101 (except the added holes), 102, 105, 201, 202 are unchanged and Rev 2 remains valid for them |
| **Source model** | `CEA_RACK_INTEGRATED_v3` v1 (Rev 6). Where a drawing and the model disagree the model governs |
| **Format note** | Rev 3 is issued as tabular part definitions. The four-view sheets are regenerated from the model with the drawing generator at the next document cycle (`drawings/generator/parts.py` needs the new parts added first) |

## Part index

| Part | Description | Status in Rev 3 |
|---|---|---|
| RK-A-101 | Upright | **revised** — added holes |
| RK-A-103 | Beam, short | **revised** — quantity 10, tier positions |
| RK-A-104 | Rear brace bar | **revised** — 1810 / 1780.1, two bars |
| RK-A-104P | Brace packer | **new** |
| RK-A-106B | Anchor strut, telescoping | **new** — replaces RK-A-106 |
| RK-A-107B | Beam-end gusset plate | **new** — replaces RK-A-107 |
| RK-A-108 | Foot insert | **new** |
| RK-A-109 | Crush tube | **new** |
| RK-A-203 | Deck mesh panel | **revised** — clearance holes, flattened mesh, datum note |
| RK-A-301 | LED rail | **revised** — 1172 mm (sheet released from hold) |
| RK-A-302 | LED saddle | **new** |
| RK-A-401 | Flood tray | **revised** — formed features, floor per ND-10 |

## RK-A-101 · Upright — additions

- 2 × Ø6 drain holes at Z 55 from the foot end, one on each grid face, through both walls.
- Rivet-nut holes **Ø11.0 +0.1/−0, near wall only**, replacing the Ø9 grid hole at: Y-face rows 150, 200, 250, 300, 650, 700, 1050, 1100, 1450, 1500 (gusset plates, long beams); X-face rows 150, 200, 250, 300, 650, 700, 1050, 1100, 1450, 1500 (gusset plates, cross beams); X-face inner rows 600, 1000, 1400, 1800 (LED saddles); rear Y-face rows 1850, 1900 (anchor strut). The far wall keeps Ø9. Note on the sheet: "near wall = the face the plate lies on".
- Bottom end: `RK-A-108` insert pressed in place of the plastic cap. Top cap retained.
- Inspection adds: Ø11 go / Ø11.3 no-go at the listed rows; drain holes present.

## RK-A-103 · Beam, short — qty 10

Unchanged part. Positions: base at Z 150–180 (2), tiers at Z 243.4–273.4 + 400·n (8), in the upright columns X 0–30 and 1226–1256, Y 40–520. End holes 2 × Ø9 at 25 and 75 from each end on the **outer** face (the face the gusset plate lies on).

## RK-A-104 · Rear brace bar — two bars

| Item | Value |
|---|---|
| Material | GI flat 25 × 3 |
| Length | **1810 ± 1.5 mm** |
| Holes | 2 × Ø9, **1780.1 ± 1.0 mm** centres, 15 mm end distance, on the centreline |
| Fitted geometry | hole to hole from (X 20, Z 150) to (X 1236, Z 1450) on the rear-upright centrelines, angle 46.9°; bar B mirrored |
| Layering | bar A at Y 563–566 on the rear gusset plates; bar B at Y 566–569 on packers RK-A-104P (40 × 25 × 3) at its ends. Bars not joined at the crossing |
| Fixing | M8 × 25 into the plate's rivet nut, 18 N·m, after squaring, before final torque |
| Inspection | length; hole centres; fitted with ≥ 10 mm clearance to every pipe crossing the rear plane |

## RK-A-104P · Brace packer

GI flat 25 × 3, 40 long, one Ø9 at centre. Qty 2 (bar B ends).

## RK-A-106B · Anchor strut, telescoping

| Element | Specification |
|---|---|
| Rack plate | GI 3 mm, 60 × 100, 2 × Ø9 at 50 pitch (rows 1850/1900), on the rear face of each rear upright |
| Outer tube | GI SHS 30 × 30 × 1.5, 100 long, welded-free: bolted to the plate through 2 × Ø9 with crush tubes; Ø9 holes at 20 mm pitch on the top face |
| Inner tube | GI SHS 25 × 25 × 1.5, 140 long, Ø9 holes at 20 mm pitch |
| Lock | 2 × M8 × 45 + flange nut through both tubes with crush tubes Ø8.5 × 36.8 |
| Wall foot | GI 4 mm, 60 × 60, slot 9 × 20 for one M10 masonry anchor (≥ 60 mm embedment) |
| Partner foot | GI 4 mm, 60 × 60, 2 × Ø11 for M10 × 30 through-bolts to the partner strut's foot |
| Range | **90–320 mm** rack rear face to wall/partner, in 20 mm steps plus slot |
| Inspection | strut engaged ≥ 40 mm overlap; both lock bolts with tubes; foot bolted to sound substrate |

## RK-A-107B · Beam-end gusset plate

| Element | Specification |
|---|---|
| Material | GI sheet 3 mm |
| Blank | 140 × 80 (tier) / 140 × 80 (base), flat, no bend |
| Post holes | 2 × Ø9 on the post centreline (20 from the plate's post edge), at 50 pitch: rows 250/300 + 400·n (tier), 150/200 (base) |
| Beam holes | 2 × Ø9 at 25 and 75 mm from the beam end (65 and 115 from the plate's post edge), on the beam centreline (15 mm above the beam bottom) |
| Variants | LH / RH × tier / base — four hole patterns; mark each blank |
| Fitting | on the outer face of post and beam together: front and rear faces for long beams, outer X faces for cross beams; plate top flush with the beam top |
| Fasteners | 2 × M8 × 20 into rivet nuts; 2 × M8 × 45 through the beam with crush tubes RK-A-109; all 18 N·m |
| Inspection | flat within 0.5 mm; hole positions ± 0.3; deburred both faces (handled repeatedly) |
| Qualification | **T19** joint coupon on the first batch |

## RK-A-108 · Foot insert

Zinc-plated steel square tube insert, 36.6 mm across flats × 40 long, M12 threaded boss, press-fit into the upright bottom (36.8 bore). Bought out; confirm interference fit 0.1–0.2 mm.

## RK-A-109 · Crush tube

SS304 tube Ø10 × Ø8.5, cut 27.0 ± 0.2 (30 × 30 beams) and 36.8 ± 0.2 (upright/strut through-bolts). Square ends, deburred.

## RK-A-203 · Deck mesh panel — revisions

- **Flattened** expanded metal, 1.6 mm strand, ≥ 70 % open (LWD 30 × SWD 12 or equivalent), LWD along the 1176 span.
- Clearance holes **Ø52** at (1156, 480) and **Ø46** at (1096, 480) from the left/front datum.
- The panel sits **on top of** the deck frame: rail top 298.4, panel 298.4–300.0, **mesh top face = bed datum 300** (EDR-001). The Rev 2 "flush ≤ 1 mm step" instruction is withdrawn.
- 20 mm folded edge on the two long sides only, folding down outside the long rails.

## RK-A-301 · LED rail — released, 1172 mm

Al 6061 SHS 20 × 20 × 1.5, **1172 ± 1.0**, one Ø6.5 at 10 mm from each end on the bottom face (saddle tab bolt). Two per tier at Y 168–188 and 372–392, rail top at 643.4 + 400·n (tiers 1–3) and 1843.4 (top tier).

## RK-A-302 · LED saddle

GI sheet 2 mm. Plate 53.4 (Z) × 198 (Y, front variant: from the post grid line at Y 20 to Y 198; rear variant: Y 362–560) on the upright inner X face, with one Ø9 at (Y 20 or 540, row 600/1000/1400/1800) into a rivet nut, and a 20 × 20 tab bent inward under the rail end with one Ø6.5. Nylon washer between rail and tab. Qty 16 (4 variants × 4 tiers).

## RK-A-401 · Flood tray — revisions

- Model carries the 30 mm overflow collar (Ø32 bore, 3 mm wall, 2° draft) at 120 from the right end / 480 from the front, and both floor openings (Ø40 at 60 from the right end, Ø32 under the collar).
- **Floor:** flat 3 mm in the model. The Rev 2 note "fall 2–3 mm toward the drain boss" is **withdrawn pending ND-10** (flat + level tolerance, or formed drainage channels to the boss). Do not quote tooling until ND-10 is decided.
- All other Rev 2 content (material, flood test, boss tolerances, radii, colour) stands.

## General tolerances — additions

| Feature | Tolerance |
|---|---|
| Rivet-nut hole Ø11 | +0.1 / −0 |
| Gusset plate holes | ± 0.3 from the plate's post edge |
| Crush tube length | ± 0.2 |
| Strut hole pitch 20 | ± 0.2 cumulative over the overlap |
