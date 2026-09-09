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
| VR-07 | Depth-plane bracing / frame stability | Rev 2 | n/a | Residual deflection ≤ 5 mm under 300 N horizontal at the top bed, front-back and side | **NOT PERFORMED.** RK-A-MFG Rev 2: "It has not been checked by frame analysis." Closes at prototype acceptance test **T16** | **NT-02 — restated** |
| VR-08 | Room floor and point loading | Rev 4 | n/a | Slab capacity ≥ imposed rack point loads | Recomputed and passed at 112.66 kg dry | Complete |
| VR-09 | Room water balance | Rev 4 | n/a | Make-up and blowdown close against consumption | 1,914 L/day circulated, 88.9 consumed, 146 blowdown, 235 make-up; **87.7 % recovery** | Complete |
| VR-10 | Drawing dimensional review | Rev 2 | v8 | Every dimension reconcilable to model geometry | **2 real errors found and corrected** — EDR-004, EDR-010 | Complete |

---

## 2. NEEDS TRACEABILITY

### NT-02 — Depth-plane bracing is unverified (restated 2026-09-09)

Originally recorded as missing metadata on a completed analysis. The CEA suite audit
showed that understates it. RK-A-MFG Rev 2 states plainly:

> Removing the per-tier cross beams and relying on the decks as horizontal diaphragms plus
> the base frame is sound in principle and the tip-over numbers above assume it holds.
> **It has not been checked by frame analysis.**

So the analysis was never performed, and the tip-over figures (139 N empty, 307 N loaded
horizontal pull; height:depth 3.48:1) **depend on an unverified assumption**. Wall anchors
are specified as mandatory rather than optional partly for this reason.

**Closure is a physical test, not an analysis:**

| Test | Criterion |
|---|---|
| **T16** — depth-plane sway | 300 N horizontal at the top bed, front-back and side. Residual deflection **≤ 5 mm** |
| Fallback if it fails | Restore the per-tier cross beams, ₹562 |

T16 supersedes the older staged-build test **P3**. RK-A-SYS §10 still uses the P3
numbering; RK-A-MFG Rev 2 states the supersession explicitly, so this is a naming lag
rather than a conflict. **T16 is the ID to use.**

Related: **T10**, the canopy velocity traverse, closes the airflow uniformity item and
doubles as the design input for the Phase 2 plenum. The acceptance set is T1–T18 in
RK-A-QC. (RK-A-MFG Rev 2 cites RK-A-QC **Rev 2** for that set; the current QC revision is
Rev 3 — a reference lag, not a content conflict.)

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
