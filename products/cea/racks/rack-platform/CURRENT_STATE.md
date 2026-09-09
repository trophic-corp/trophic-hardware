# CURRENT_STATE — CEA Rack Platform (Rack A)

**As of:** 2026-09-09
**Design stage:** validated, pre-prototype
**Release stage:** blocked (see §4)

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

What is *not* done is the release: the CAD exchange artifacts referenced by the
manufacturing pack were never actually written to disk.

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

## 4. Release blocker

**RB-01 — CAD release artifacts do not exist.**

`RK-A-MFG` §15 and `RK-A-DWG` both reference a release set at
`C:\Users\karex\Desktop\CEA_RACK_v1`. The folder does not exist. No CEA-named
`.step`, `.stp`, `.f3d` or `.dxf` file exists anywhere in the user profile, in
either `Desktop` or `OneDrive\Desktop`. A probe write to the Desktop succeeded,
so the location is writable and the failure is not a permissions problem.

Root cause: the export script incremented its success counter when no exception
was raised, instead of checking the return value of
`ExportManager.execute()`. Silent failure was therefore reported as success.

Until this is fixed, two documents contain a reference to an artifact that does
not exist, and no fabrication package can be issued.

---

## 5. NEEDS TRACEABILITY

| ID | Item | Why it is open |
|---|---|---|
| NT-01 | Fusion parameter master (~55 parameters) | Only `Shelf_Pitch`, `Bed_Width`, `Grid_Pitch`, `Top_Bed_Height`, `Flood_Depth` and `Number_of_Tiers` are persisted, partially, in `RK-A-BRIEF` Rev G. The full current set exists only inside the Fusion design. Reading it requires opening the design. **Not invented here** |
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

---

## 7. Deferred by design

| Item | Status |
|---|---|
| Ducted plenum ventilation | Deferred to month 2–3. Phase 1 uses standalone EC fans. Point-source fan velocity CV ≈ 33 % against ≈ 10 % for a ducted plenum, so this is a known, accepted uniformity penalty for Phase 1 |
| Reflective panel accessory set | Specified (`RK-A-501`, `RK-A-502`) but held out of the structural drawing reissue |
| LED mounting rail `RK-A-301` | Specified, held out of the Rev 2 structural set |

---

## 8. Next engineering action

1. Re-run the Fusion export for `CEA_RACK_INTEGRATED_v2` v8, checking
   `ExportManager.execute()` return values and confirming file size on disk.
   Record as release **RK-A R1** in `docs/system/RELEASE_INDEX.md`. Closes RB-01.
2. In the same session, dump the full parameter table from the open design and
   persist it to `design/RK-A-PARAM_Rev1_parameter-master.md`. Closes NT-01.
3. Put ND-01 to the user before any part-drawing reissue.
