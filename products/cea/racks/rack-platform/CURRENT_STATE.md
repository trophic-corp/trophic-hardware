# CURRENT_STATE — CEA Rack Platform (Rack A)

**As of:** 2026-09-09
**Design stage:** validated, pre-prototype
**Release stage:** **`RK-A R1` issued** (see §4)

---

## 1. Where the design stands

The integrated rack model is complete and internally consistent. All systems —
irrigation, drainage and recovery interface, electrical, LED mounting,
ventilation, sensing, control enclosure, routing and protection — are modelled
in `CEA_RACK_INTEGRATED_v2` v8. The model reports **45 parts, 177 occurrences,
0 unresolved interferences, 112.66 kg dry**.

The document set (brief, systems specification, structural drawings,
manufacturing pack, validation record) has been cross-referenced and swept for
stale figures. The rack has been set out into an 11-rack room layout and the
room-level water balance closes.

The release **`RK-A R1`** is issued and verified: 45 of 45 part STEP files plus
assembly STEP and F3D, hashed and reconciled against the live model.

---

## 2. Validated this design cycle

| Item | Result |
|---|---|
| Mass model | Corrected twice — 1246 kg (solid placeholders) → 147.67 kg (shelled, real materials) → **112.66 kg** (deck mesh density corrected) |
| Interference | All clashes resolved; 0 unresolved in v8 |
| Drain continuity | Proven joint-by-joint from every tray outlet through the tray strainer, bulkhead, overflow drop and branch to the rack drain header outlet |
| Gravity supply | 2.66 m static head vs 0.33 m loss at 7.2 L/min. Passes ~8×. Four tiers concurrent still passes |
| Suction-lift architecture | Terrace supply pump deleted; recovery pump relocated to the low point |
| Tier count | Four confirmed as the reach-limited maximum (NIOSH RWL = 0 above 1750 mm) |
| Structural drawings | Reissued Rev 2; two real dimensional errors caught and corrected |
| Manufacturing pack | Reissued Rev 2 against the corrected geometry and mass |
| Room integration | 11 racks set out to coordinates; 29.0 m² grow area, 1.30× floor multiplier |

Full evidence, assumptions and limitations are in
`verification/RK-A-QC_Rev3_engineering-validation-record.html` and indexed in
`docs/quality/VERIFICATION_INDEX.md`.

---

## 3. Errors caught and corrected (kept because they are load-bearing)

| # | Error | Correction |
|---|---|---|
| 1 | Deck mesh given a 35 %-open perforated-sheet density | Corrected to 1884 kg/m³ for ≥70 % open expanded mesh — 1.98 kg/panel. **The drawing was right and the model was wrong**; recorded as EDR-004, the one exception to "the model governs" |
| 2 | `RK-A-104` rear brace dimensioned 1345 mm against a true diagonal of 1797 mm | Corrected to 1797 mm, hole centres at 20 / 1777. Rev 1 would have produced a part 452 mm short |
| 3 | Overflow line had a 90 mm break between the moulded collar (Z 300–330) and the vertical drop (Z 160–210); tray penetrations were never modelled | `09_OVF_V` extended to Z 160–300; `09_TRAY_OUTLET`, `09_TRAY_STRAINER` and `09_OVF_BULKHEAD` added. Caught by the user, not by the model |
| 4 | Terrace-mounted supply pump lifting from the room | Physically impossible at 2,240 m. Architecture changed to gravity feed with the recovery pump at the low point (EDR-005) |
| 5 | Room Rev 3 rewrite silently dropped the Building section | Restored as §08 in Rev 4 with recomputed loads |

---

## 4. Release — `RK-A R1`, ISSUED

| | |
|---|---|
| Source | Fusion `CEA_RACK_INTEGRATED_v2` **v8** (Rev 5) |
| Exported | 2026-09-05 10:21 · **verified 2026-09-09** |
| Store | `E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\INTEGRATED_v2_Rev5\` |
| Manifest | `release/RK-A-R1_MANIFEST.md` — per-file SHA-256 |

**RB-01 closed.** The export was never missing — it was written to Google Drive, not
to the Desktop path `RK-A-MFG` §15 and `RK-A-DWG` cite. Those two references are
errata; no engineering value is affected.

The release content independently confirms two of the corrections in §3:
`04_DECK_PANEL` at 1.981 kg each (EDR-004), and the presence of `09_TRAY_OUTLET`,
`09_TRAY_STRAINER` and `09_OVF_BULKHEAD` with `09_OVF_V` at nearly double its
pre-correction size (ICR-001).

**Constraints on use:** do not issue part drawings with R1 (ND-01 open); regenerate
the DXF flat patterns from v8 before cutting any sheet-metal part.

---

## 5. NEEDS TRACEABILITY

| ID | Item | Why it is open |
|---|---|---|
| ~~NT-01~~ | Fusion parameter master | **CLOSED 2026-09-09.** All 55 user parameters read from `CEA_RACK_INTEGRATED_v2` v8 and persisted as `design/RK-A-PARAM_Rev1_parameter-master.md`. The read also resolved the apparent `Rack_Height` 1950 vs envelope 1960 conflict — the feet sit 10 mm below the floor datum |
| NT-02 | Structural validation metadata | The validation record states conclusions but does not consistently record, per case: design revision tested, CAD version, assumed loads, boundary conditions, acceptance criterion and limitation. Marked NEEDS TRACEABILITY rather than reconstructed |

Neither item invalidates the engineering. Both mean the evidence cannot
currently be audited to the standard the rest of the set meets.

---

## 6. NEEDS DECISION

| ID | Decision required |
|---|---|
| ND-01 | **Part-drawings divergence.** The local build archived at `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` holds Rev 2 content (11 chapters, contains the corrected 1797 mm brace) while the published artifact of the same ID holds Rev 1 (14 chapters). The published Rev 1 contains three chapters the local build does not. Which is the intended part-drawing release, and what happens to the three missing chapters, must be decided before part drawings are reissued. **Nothing has been reconciled** |
| ND-02 | **Duplicate manufacturing pack artifact.** Two published "Rack A Manufacturing Pack" artifacts exist: `9f5e09e5` (Rev 2, current, referenced everywhere) and `817abd35` (dated 04 Sep, orphaned, referenced by nothing). Retire the orphan or state why it is kept |
| ND-03 | **Plenum interface freeze.** The ducted plenum is deferred to a Phase-2 entity; Phase 1 ships standalone EC fans. The rack-to-plenum mechanical and electrical interface is not frozen, so the Phase-1 build cannot be guaranteed plenum-ready. Decide whether to freeze the interface now or accept rework at plenum introduction |
| ND-04 | **Installed depth allowance.** Installed depth is 690 mm with the plenum and 648 mm without. Room set-out currently assumes the installed figure. Confirm that Phase-1 racks are spaced at the plenum-ready pitch so the plenum can be retrofitted without moving racks |
| ND-05 | **Canopy velocity CV action threshold.** Two thresholds appear in our own source set: RK-A-SYS §01 gives 15 % → fit side/rear enclosure panels; RK-A-ROOM §04 gives 20 % → below it the plenum is an optimisation, above it a required fix. These read naturally as a two-step escalation ladder, but no document says so and inferring it would be a silent reconciliation. Confirm the ladder or pick one |
| ND-06 | **Room electrical phase imbalance.** The as-designed 11-rack layout lands at ~20 % imbalance on single-phase HVAC against a 15 % target. RK-A-ROOM §05 records it as resolved by specifying 3-phase HVAC, but explicitly as an open engineering finding rather than a clean pass. Confirm the 3-phase specification is committed |
| ND-07 | **Terrace slab loading — LOW PRIORITY, kept as UNKNOWN.** RK-A-WRS §04 Risk 3 gives 5.5 kN/m² concentrated against a typical 1.5–2.0 kN/m² terrace rating. **Owner decision 2026-09-09: this is not a blocker** — the tank will sit on a purpose-built steel structure spanning to suitable bearing points, not directly on the slab. It stays open as an unknown because that steel structure is not yet designed and its bearing reactions are unquantified. Re-raise when the structure is specified |

---

## 7. Deferred by design

| Item | Status |
|---|---|
| Ducted plenum ventilation | Deferred to month 2–3. Phase 1 uses standalone EC fans. Point-source fan velocity CV ≈ 33 % against ≈ 10 % for a ducted plenum, so this is a known, accepted uniformity penalty for Phase 1 |
| Reflective panel accessory set | Specified (`RK-A-501`, `RK-A-502`) but held out of the structural drawing reissue |
| LED mounting rail `RK-A-301` | Specified, held out of the Rev 2 structural set |

---

## 8. Next engineering action

1. **Build the prototype and run T16** — 300 N horizontal at the top bed,
   front-back and side, residual deflection ≤ 5 mm. This is the only way to close
   NT-02, and everything else is now ready for it.
2. **Regenerate the DXF flat patterns from v8** before cutting sheet metal. The
   existing set came from the platform design and covers 5 parts.
3. **Put ND-01 to a decision** before any part-drawing reissue.
4. Fix the export script to check `ExportManager.execute()` before the next export.
