# RK-A-MFG Rev 3 — Manufacturing Pack, CEA Rack Platform (Rack A)

| | |
|---|---|
| **Document** | RK-A-MFG · Rev 3 · 10 September 2026 · systems-integrated, ECP-01 |
| **Supersedes** | Rev 2 (2026-09-05). Sections not restated here (GA, tier section, cut-list nesting method, subsystem layouts other than drainage, powder-coat option, roadmap) are unchanged from Rev 2 |
| **Source model** | Fusion `CEA_RACK_INTEGRATED_v3` **v1** (Rev 6) — 70 unique parts, 417 occurrences, 136.39 kg dry (all systems, fixture envelopes 1.18 kg each), 1456 × 690 × 1960 mm |
| **Validation** | RK-A-QC Rev 4 — 18 structural checks, VR-07/VR-11, tests T1–T20 |
| **Format note** | Issued as Markdown; HTML rendering at the next document cycle. Structural part sheets: RK-A-DWG Rev 3 |

---

## 01 · Specification — lines changed by ECP-01

| Parameter | Rev 2 | **Rev 3** | Basis |
|---|---|---|---|
| Installed envelope | 1456 × 690 × 1960 | **1456 × 690 × 1960** (unchanged) | ICR-006 keeps the header inside the rear service zone |
| Envelope, Phase-1 build | 1456 × 648 × 1960 | **1456 × 690 × 1960** — the 648 figure is withdrawn; fans, header and tundish occupy the rear zone from Phase 1 | F-26 |
| Tiers | 4 (structure supports 3–5) | **4** — five ruled out (EDR-002); the "3–5" and "drilled for 5" statements are withdrawn | F-27 |
| Dry mass, model, all systems | 112.7 kg | **136.4 kg** (structure 82.4) | v3 v1 |
| Mass per configuration (T18) | — | Core 91.7 · Grow Phase 1 (no plenums/panels/fixtures) 108.0 · Grow complete without fixtures 126.9 kg | ICR-007 |
| Depth-plane stability | open (T16) | **closed by analysis** (VR-07: 5.4 mm at 300 N with P-Δ); confirmed by T16 after T19 | EDR-014/015 |
| Rated shelf load / flatness | 80 kg UDL; ≤ 3 mm | unchanged | — |
| Overflow | 30 mm collar, DN32 | unchanged — level at 7.2 L/min ≈ 38 mm (weir), T8 ≤ 42 mm | ICR-007 |
| Fill nozzle | above the rim | **outlet 38 mm above the rim** (Z 385) | ICR-005 |
| Valves | solenoid fill and drain | **fill: DN20 zero-ΔP solenoid NC · drain: DN40 motorised ball valve, spring-return OPEN** | EDR-016 |
| Drain header | DN50 in the right upright column | **DN50 behind the rear-right upright, X 1200–1250, Y 575–625**; laterals cross the rear plane in defined windows | ICR-006 |
| Anchoring | `RK-A-106` 60 mm bracket | **`RK-A-106B` telescoping strut 90–320 mm**, wall foot (M10) or partner foot | EDR-017 |
| Fasteners | 208, M8 18 N·m through sections | **≈ 450 items (264 threaded)**; M8 into rivet nuts or with crush tubes 18 N·m; M8 through a section without a crush tube **4 N·m** | EDR-015 |
| Accessory interface | Ø9 grid, 2 faces | unchanged; **Ø11 at rivet-nut positions, near wall only** | EDR-015 |

## 02 · Engineering validation

Restated in full in RK-A-QC Rev 4 §01 (checks 1–18), §02 (VR-07 frame model) and §03 (VR-11 seismic). Headline: beam sizing unchanged and confirmed; upright SF 28 at Le 1950; frame sway 5.4 mm at 300 N; tip-over dry 170 N push-to-rear — struts mandatory; overflow and drain restated on the correct physics.

## 05 · Part schedule (complete, Rev 3)

| Part no. | Description | Material / section | Cut size | Qty | Mass (kg) | Process | Change |
|---|---|---|---|---|---|---|---|
| RK-A-101 | Upright | GI SHS 40 × 40 × 1.6 | 1950 | 4 | 3.65 | saw, punch Ø9 grid 2 faces; **Ø11 near-wall at plate rows; 2 × Ø6 drain at Z 55** | EDR-015/020 |
| RK-A-102 | Beam, long | GI SHS 30 × 30 × 1.5 | 1176 | 10 | 1.58 | saw, punch 2 × Ø9 per end (25/75) one face | — |
| RK-A-103 | Beam, short | GI SHS 30 × 30 × 1.5 | 480 | **10** | 0.64 | as 102 | EDR-014 (qty 2 → 10) |
| RK-A-104 | Rear brace bar | GI flat 25 × 3 | **1810** | 2 | 1.06 | shear/laser, 2 × Ø9 at **1780.1** centres, 15 from ends | EDR-018 |
| RK-A-104P | Brace packer | GI flat 25 × 3 | 40 | 2 | 0.02 | shear | EDR-018 |
| RK-A-105 | Levelling foot | M12 × 60, nylon base, ±20 | — | 4 | 0.15 | bought out | — |
| RK-A-106B | Anchor strut, telescoping | GI SHS 30 × 30 × 1.5 (outer, 100) + 25 × 25 × 1.5 (inner, 140) + 3 mm rack plate 60 × 100 + 4 mm foot 60 × 60 | — | 2 | 0.47 | saw, drill Ø9 @ 20 pitch, laser plates, bolt | EDR-017 |
| RK-A-107B | Beam-end gusset plate (4 variants: LH/RH × tier/base) | GI sheet 3 mm | 140 × 80 | **40** | 0.26 | laser, 4 × Ø9, deburr | EDR-015 (replaces 107) |
| RK-A-108 | Foot insert | zinc-plated steel, M12 | 36.6 sq × 40 | 4 | 0.39 | bought out | EDR-020 |
| RK-A-109 | Crush tube | SS304 tube Ø10 × Ø8.5 | 27 (beams) / 36.8 (strut, brace) | 80 + 8 | 0.02 | cut | EDR-015 |
| RK-A-110 | Rivet nut M8, flat head, steel zinc | grip 1.0–3.0 | — | 80 (+ 4 strut + 16 saddle) | 0.01 | set with M8 tool | EDR-015 |
| RK-A-201 | Deck rail, long | GI SHS 25 × 25 × 1.5 | 1176 | 8 | 1.30 | as before | — |
| RK-A-202 | Deck rail, cross | GI SHS 25 × 25 × 1.5 | 510 | 16 | 0.56 | as before | — |
| RK-A-203 | Deck mesh panel | **flattened** GI expanded mesh 1.6, ≥ 70 % open | 1176 × 560 | 4 | 1.97 | shear, fold long edges, rivet; **Ø52 and Ø46 clearance holes** | EDR-019/020 |
| RK-A-301 | LED rail | Al 6061 SHS 20 × 20 × 1.5 | **1172** | 8 | 0.35 | saw | EDR-020 |
| RK-A-302 | LED saddle (F/R variants) | GI sheet 2 mm | 200 × 53 + tab | 16 | 0.17 | laser, bend tab | EDR-020 |
| RK-A-401 | Flood tray, wet module | HDPE 3 mm food grade, white | 1176 × 560 × 47 | 4 | 2.32 | thermoform — **collar and both floor openings in the tool; floor per ND-10** | EDR-019 |
| RK-A-402 / 403 / 404 | Tray bulkheads, strainer | as Rev 2 | — | 4 each | — | bought out | — |
| RK-A-501 / 502 | Reflective panels | white PP 2 mm | as Rev 2 | 4 / 8 | — | held (plenum) | rear panel now at Y 569–571 |
| — | Fill solenoid, DN20 zero-ΔP NC 24 V DC | PP/PA, EPDM | — | 4 | — | bought out | EDR-016 |
| — | Drain valve, DN40 motorised ball, spring-return open, 24 V DC, IP67 | PP/PVC-U, EPDM | — | 4 | — | bought out | EDR-016 |

## 06 · BOM and materials — additions

| Item | Specification | Source |
|---|---|---|
| Gusset plates 107B, LED saddles 302, strut plates | Pre-galvanised sheet 3 mm / 2 mm / 4 mm, IS 4923 | local laser |
| Rivet nuts | M8 steel, zinc-plated, flat head, grip 1.0–3.0, knurled body | bought out |
| Crush tubes | SS304 Ø10 × 0.75 wall, cut to 27 / 36.8 | bought out, cut in-house |
| Foot inserts | M12 tube insert for 36.6 sq bore | bought out |
| Valves | per EDR-016; datasheet with Kv and ΔP-min = 0 on file per batch | bought out |

**Material clause added.** Every rivet nut is set in the near wall only; a rivet nut set through both walls or in a Ø9 hole is a reject.

## 07 · Fastener schedule (Rev 3)

| Application | Fastener | Qty | Torque |
|---|---|---|---|
| Gusset plate to upright | M8 × 20 hex SS304 into rivet nut | 80 | 18 N·m |
| Gusset plate through beam end | M8 × 45 hex SS304 + flange nut, **crush tube Ø8.5 × 27** | 80 | 18 N·m |
| Deck long rail to beam | M8 × 20 + flange nut, **no crush tube** | 16 | **4 N·m**, serrated flange nut |
| Deck cross to long rail | M8 × 20 + flange nut, no crush tube | 32 | 4 N·m |
| Rear brace to upright (shares plate rivet nut) | M8 × 25 into rivet nut | 4 | 18 N·m |
| LED saddle to upright | M8 × 16 into rivet nut | 16 | 12 N·m |
| LED rail to saddle tab | M6 × 12 + nylon washer | 16 | 6 N·m |
| Anchor strut to upright | M8 × 20 into rivet nut | 4 | 18 N·m |
| Strut telescopic lock | M8 × 45 + flange nut, crush tube Ø8.5 × 36.8 | 4 | 18 N·m |
| Strut to wall | **M10** masonry anchor, ≥ 60 mm embedment | 2 | per maker |
| Strut to partner strut | M10 × 30 + nut | 2 | 25 N·m |
| Levelling feet | M12 × 60 into RK-A-108 | 4 | hand + locknut |
| Deck mesh to frame | 4.8 mm SS blind rivet | 32 | — |
| Reflective panels | M6 × 16 + penny washer | 48 | 6 N·m |

Threaded fasteners 264 · rivet nuts 100 · crush tubes 84 · blind rivets 32.

## 08 · Cut list — additions

| Stock | Cuts, 1 rack | Note |
|---|---|---|
| GI SHS 30 × 30 × 1.5, 6 m | 10 × 1176 · **10 × 480** | 4 bars per rack; nest across 3 racks |
| GI flat 25 × 3 | 2 × **1810** + 2 × 40 | |
| GI sheet 3 mm | 40 gusset plates 140 × 80 + 2 strut plates 60 × 100 | one sheet 1250 × 2500 covers 4 racks |
| GI sheet 2 mm | 16 saddles | |
| GI sheet 4 mm | 2 strut feet 60 × 60 | |
| Al SHS 20 × 20 × 1.5 | 8 × **1172** | |

## 09 · Drainage layout (replaces Rev 2 §09 "Drainage")

Each tray drains through the DN40 bulkhead and lift-out strainer into the drain valve under the tray (X 1126–1186, Y 455–515). From the valve the lateral runs **−X at Y 500–540** to the crossing window at **X 1040–1080**, turns **+Y** through the rear beam plane (between the beams, clear of both brace bars), and runs **+X behind the rack at Y 580–620** into the DN50 header at X 1200–1250, Y 575–625, Z 200–1450. Overflow laterals from the moulded collar cross at X 1080–1112 (tiers 2–4) and at X 990–1022 for tier 1 (Z 182–214), entering the header rear face. Header outlet at Z 200 over the tundish (rim Z 100, **100 mm air gap**) at X 1180–1270, Y 570–660; leak sensor under the tundish. Nothing water-carrying passes above the tray rim except the fill nozzle, whose outlet is 38 mm above it.

## 10 · Fabrication — additions

- **Set rivet nuts** with an M8 hand or pneumatic setter into Ø11.0 +0.1 holes, near wall only, before assembly. Check pull-out on a 10 % sample (≥ 5 kN).
- **Drop a crush tube** into every beam end hole before bolting a gusset plate; a bolt tightened to 18 N·m without a tube will dish the beam wall — reject and replace the beam.
- **Gusset plates** are fitted with the two post bolts first (finger tight), then the two beam bolts, then squared and torqued base-up.
- **Rear brace**: bar A sits on the rear gusset plates; bar B on its packers; the four brace bolts go into the plate rivet nuts (M8 × 25). Fit after squaring, before final torque.
- **Upright**: 2 × Ø6 drain holes at Z 55 on the grid faces; foot insert pressed into the bottom before the foot; top cap only.

## 11 · Assembly — changed steps

3. Fit the tier beams: at each tier bolt **two long and two short beams** through their gusset plates (rows 250/300 + 400·n). The rack is now a full rectangle at every level.
7. Fit the **anchor struts** to the rear uprights at Z 1850/1900, extend to the wall or partner rack, lock with the two through-bolts, then the foot bolts.
8. Drop in the decks — bolt at 4 N·m (or leave unbolted for a wash-down rack: the deck is not structural).
13. Plumb: header behind the rear-right upright; laterals through the crossing windows; **confirm every lateral clears both brace bars by ≥ 10 mm** — a bar touching a pipe is a reject.
15. Fit the drain valves with their actuators facing the aisle; confirm spring-return-open on power-off before commissioning (T15).

## 12 · QC additions

Rivet-nut pull-out sample · crush tube present at every beam bolt (count 80) · plate torque 18 N·m, deck bolts 4 N·m · brace bar ends on the plates, bars not touching pipes · nozzle outlet ≥ 30 mm above the rim (T20) · joint coupon T19 result on file for the plate batch · mass per configuration (T18).

## 14 · Cost — Core delta (estimate, to be re-quoted)

| Element | Rev 2 | Rev 3 |
|---|---|---|
| GI sections | ₹3,467 | ₹4,029 (+8 cross beams) |
| L-brackets 12 laser | ₹840 | — |
| Gusset plates 40 laser + 10.3 kg | — | ≈ ₹2,600 |
| Rivet nuts 100, crush tubes 84 | — | ≈ ₹1,000 |
| Fasteners | ₹1,444 | ≈ ₹2,500 |
| Anchor struts 2, foot inserts 4 | ₹520 (feet/caps) | ≈ ₹1,300 |
| **Core** | ₹12,391 | **≈ ₹17,400** (+₹5,000, of which ≈ ₹3,600 is the joint system) |

Grow Phase 1 moves accordingly (≈ ₹54,300 before valve re-quote; motorised drain valves add ≈ ₹6,000 over solenoids). These are estimates against Rev 2 rates; re-quote before the price list is reissued.

## 15 · CAD release

`RK-A R1` remains the last issued release and is **not** to be used for gusset plates, brace, anchor, tray tooling or drainage. `RK-A R2` is to be exported from `CEA_RACK_INTEGRATED_v3` v1 with `ExportManager.execute()` checked per RELEASE_INDEX. The R1 tray STEP is annotated not-for-tooling.
