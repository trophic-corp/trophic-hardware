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
| VR-07 | Structural adequacy, frame | Rev 2 | not recorded | not recorded | Reported adequate | **NEEDS TRACEABILITY — NT-02** |
| VR-08 | Room floor and point loading | Rev 4 | n/a | Slab capacity ≥ imposed rack point loads | Recomputed and passed at 112.66 kg dry | Complete |
| VR-09 | Room water balance | Rev 4 | n/a | Make-up and blowdown close against consumption | 1,914 L/day circulated, 88.9 consumed, 146 blowdown, 235 make-up; **87.7 % recovery** | Complete |
| VR-10 | Drawing dimensional review | Rev 2 | v8 | Every dimension reconcilable to model geometry | **2 real errors found and corrected** — EDR-004, EDR-010 | Complete |

---

## 2. NEEDS TRACEABILITY

### NT-02 — Structural validation metadata

`VR-07` states a conclusion but the record does not consistently carry, per
load case:

- the design revision actually analysed
- the CAD version the mesh was taken from
- assumed loads (bed water mass at flood depth, media, crop, service loading)
- boundary conditions and anchor assumptions
- the acceptance criterion applied (stress, deflection limit, factor of safety)
- stated limitations

The conclusion is not disputed and the mass basis has since improved
(112.66 kg dry is lighter than the 147.67 kg figure that preceded it, so a
structural result obtained at the heavier mass is conservative). But the record
cannot be audited to the standard the rest of the set meets.

**This has not been fixed by inventing the missing metadata.** Closing NT-02
requires either recovering the original analysis inputs or re-running the
analysis with them recorded.

---

## 3. Verification not yet performed

| Item | Why it matters |
|---|---|
| Air gap physical verification at install | EDR-006 is safety-critical and cannot be verified from drawings |
| Seismic check per IS 1893 | Referenced as applicable; no record of a completed check |
| Earthing and RCD testing per IS 732 / IS 3043 | Commissioning activity, not yet scheduled |
| Phase-1 airflow uniformity measurement | Baseline needed before the plenum (ADR-005) can be shown to improve on it |
| Post-release CAD export integrity | RB-01 — the export itself has never succeeded |

---

## 4. Rule

Do **not** re-run a simulation or a calculation because files moved, because a
document was reissued, or because a revision number changed. Re-run when the
underlying design has materially changed — and when you do, record every field
in §1 at the time of the run, not afterwards.
