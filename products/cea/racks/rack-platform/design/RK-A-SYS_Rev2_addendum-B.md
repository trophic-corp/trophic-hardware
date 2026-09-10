# RK-A-SYS Rev 2 — Addendum B (ECP-01)

**Date:** 2026-09-10 · **Applies to:** RK-A-SYS Rev 2 + addendum (integration validation) · **Authority:** EDR-016, ICR-005, ICR-006, ICR-007, RK-A-QC Rev 4

Sections 00–14 stand. The following statements in RK-A-SYS Rev 2 are superseded:

| § | Was | Now |
|---|---|---|
| 01 rule 1 / 07 L4 | "Minimum 236 mm vertical separation" | Separation is by the ELV boundary (only 24/48 V at or below canopy) and IP65 enclosures, not by distance. The measured vertical distance from the enclosure bottom (Z 1700) to the highest water-carrying part (tier-4 drop run, Z 1638) is 62 mm; to the supply riser 400 mm. Glands-down and drip-loop rules unchanged |
| 01 rule 2 / 02 "How water reaches a tray" | nozzle "above the rim" | Nozzle **outlet Z 385, 38 mm above the rim** (Z 347), ≥ 2 × DN16 (ICR-005). Verified by T20 |
| 02 tier drop | "DN16 drops … terminating above the tray rim" | Drops re-spanned: X/Y runs at Z 422–438 + 400·n; verticals V1 438–1030, V2 838–1100, V3 1170–1238, V4 1300–1638 (no overlapping segments) |
| 02 / 03 valves | fill solenoid 12 V; drain solenoid DN40 | **Fill:** DN20 zero-ΔP direct-acting solenoid, NC, 24 V DC, Kv ≥ 4. **Drain:** DN40 full-bore motorised ball valve, spring-return OPEN, 24 V DC, IP67, Kv ≈ 60, stroke 5–15 s, position feedback (EDR-016). The controller allows the stroke time before declaring a drain fault; sequential-draining interlock counts from end of stroke. Alternatives to be trialled — ND-09 |
| 02 table "Drain header" | "Right rear upright, vertical" | **Behind the rear-right upright, X 1200–1250, Y 575–625, Z 200–1450** (ICR-006). Laterals cross the rear beam plane in defined windows (X 1040–1080 drain; 1080–1112 overflow tiers 2–4; 990–1022 overflow tier 1) and never intersect a brace bar |
| 02 table "Discharge" | "Base of the right rear upright, 150 mm" | Header outlet Z 200 over the tundish (rim Z 100) at X 1180–1270, Y 570–660 — 100 mm air gap unchanged |
| 02 R2 / 12 H3 | DN32 collar 11.9 L/min at 8 mm, 1.65× | Weir: 7.6 L/min at 8 mm; the level self-adjusts to ≈ 38 mm at 7.2 L/min, 9 mm below the rim. T8 criterion ≤ 42 mm (ICR-007) |
| 03 "Tray empty time ≈ 55 s" | — | ≈ 19 s calculated with the motorised valve (Kv 60), strainer excluded; T7 ≤ 60 s from end of stroke |
| 09 routing | "Rear service zone, right upright: DN40 drain header" | Rear service zone Y 571–690 carries the header, laterals and tundish at X 990–1270 and the Phase-1 fans; the Phase-2 plenum must respect X ≤ 1150 and the lateral windows (ICR-004 open) |
| 10 F4 | header high-level switch at 200 mm | at Z 250–310 in the relocated header (unchanged height) |
| 11 R3 / open items | depth-plane bracing → P3 | closed by analysis VR-07; confirmed by T16 after T19 |
| 06 LED mounting | "GI saddle bracket bolted to the 50 mm grid on the underside of the tier above" | `RK-A-302` end saddles on the upright inner faces at rows 600/1000/1400/1800; rail 1172 mm; fixture envelope 62–1194 |
