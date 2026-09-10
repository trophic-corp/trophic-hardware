# Verification Index

Index of engineering validation evidence. **Existing evidence remains valid
unless the underlying design has materially changed.** Nothing here was re-run
because of the workspace migration.

For each record: design revision tested · CAD version · assumptions · loads and
inputs · constraints · acceptance criteria · results · conclusion ·
limitations. Where that metadata is absent it is marked **NEEDS TRACEABILITY**
rather than reconstructed.

Full narrative evidence is in
`products/cea/racks/rack-platform/verification/RK-A-QC_Rev3_engineering-validation-record.html`.

---

## 1. Verification records

| ID | Subject | Design rev | CAD version | Acceptance criterion | Result | Traceability |
|---|---|---|---|---|---|---|
| VR-01 | Mass properties | Rev 5 | `CEA_RACK_INTEGRATED_v2` v8 | Mass derived from specified materials and real wall thicknesses, no placeholder densities | **112.66 kg dry**, 45 parts, 177 occurrences | Complete |
| VR-02 | Interference / clash | Rev 3 onward | v6 → v8 | Zero unresolved interferences | **0 unresolved** | Complete |
| VR-03 | Drain chain continuity | Rev 4 | v7 | Continuous joint-by-joint from every tray outlet to the rack drain header outlet; discontinuous only at the air gap | **Pass** — proven joint by joint | Complete |
| VR-04 | Gravity supply head | Rev 4 | n/a (hydraulic calculation) | Available static head ≥ total loss at design flow | 2.66 m vs 0.33 m at 7.2 L/min — **pass, ~8× margin**. Four tiers concurrent (28.8 L/min) 0.67 m — pass | Complete |
| VR-05 | Suction-lift feasibility | Rev 4 | n/a | Pump suction lift within practical self-priming limit at site altitude | **Fail as originally proposed** → architecture changed (EDR-005) | Complete |
| VR-06 | Tier reach ergonomics | Rev 5 | n/a | NIOSH revised lifting equation RWL > 0 at the top bed | 1500 mm **pass**; 1900 mm **fail** (RWL = 0 above 1750 mm) | Complete |
| VR-07 | Depth-plane frame stability | **Rev 6** | `CEA_RACK_INTEGRATED_v3` v1 | Elastic sway ≤ 10 mm at 300 N at the top bed, loaded, with P-Δ | **PERFORMED 2026-09-10** — semi-rigid frame model, k = 8 kN·m/rad (calculated `RK-A-107B`): **5.4 mm**; passes down to k ≈ 3.5 kN·m/rad. Joint stiffness to be measured (T19); T16 confirmatory | Complete — NT-03 for the coupon |
| VR-08 | Room floor and point loading | Rev 4 | n/a | Slab capacity ≥ imposed rack point loads | Passed at 112.66 kg dry; **to be restated at 136.4 kg (+21 %) in RK-A-ROOM Rev 5 — ND-08**; distributed load ≈ 1.6 kN/m², still within a normal ground slab | Complete, restatement pending |
| VR-09 | Room water balance | Rev 4 | n/a | Make-up and blowdown close against consumption | 1,914 L/day circulated, 88.9 consumed, 146 blowdown, 235 make-up; **87.7 % recovery** | Complete |
| VR-10 | Drawing dimensional review | Rev 2 | v8 | Every dimension reconcilable to model geometry | 2 errors found (EDR-004, EDR-010) — **EDR-010 itself later found wrong** (bounding-box diagonal); corrected by EDR-018 | Complete, superseded for RK-A-104 |
| VR-11 | Seismic, IS 1893 Pt 1 cl. 7.13 | Rev 6 | v3 v1 | Overturning SF ≥ 1.5 unanchored | Z 0.16, flexible component: **SF 3.1** | Complete |
| VR-12 | Independent engineering review | Rev 5 → 6 | v8 | Design sound, buildable, validated | 35 findings; Critical/High resolved by ECP-01 — `RK-A-REV` Rev A | Complete |
| VR-13 | ECP-01 model verification | Rev 6 | v3 v1 | 0 structural clashes; mass, CG, envelope reconciled | 204 contacts, all in the recorded whitelist; 136.39 kg; CG 642/350/907; 1456 × 690 × 1960 | Complete |
| VR-14 | Fill air gap | Rev 6 | v3 v1 | Nozzle outlet ≥ 2 × DN16 above the rim | 38 mm | Complete (physical check T20) |

---

## 2. NEEDS TRACEABILITY

### NT-02 — CLOSED 2026-09-10

Closed by analysis (VR-07) after ECP-01 reinstated per-tier cross beams and defined the `RK-A-107B` joint. **T16 is now confirmatory**: 300 N at the top bed, loaded, elastic ≤ 10 mm, residual ≤ 2 mm (ICR-007).

### NT-03 — Joint stiffness is calculated, not measured

`RK-A-107B` k ≈ 8 kN·m/rad is a calculation. **T19** (moment–rotation coupon, ≥ 5 kN·m/rad secant to 50 N·m, no slip below 80 N·m) must be run on the first plate batch before T16 is interpreted.

## 3. Verification not yet performed

| Item | Why it matters |
|---|---|
| Air gap physical verification at install — tundish (EDR-006) **and every fill nozzle (ICR-005, T20)** | Safety-critical; cannot be verified from drawings |
| T19 joint coupon | Qualifies the calculated joint stiffness behind VR-07 |
| Earthing and RCD testing per IS 732 / IS 3043 | Commissioning activity, not yet scheduled |
| Phase-1 airflow uniformity measurement | Baseline needed before the plenum (ADR-005) can be shown to improve on it |
| `RK-A R2` export integrity | Export from `_v3` v1 with `ExportManager.execute()` checked |

---

## 4. Rule

Do **not** re-run a simulation or a calculation because files moved, because a
document was reissued, or because a revision number changed. Re-run when the
underlying design has materially changed — and when you do, record every field
in §1 at the time of the run, not afterwards.
