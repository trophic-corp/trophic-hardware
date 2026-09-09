# CURRENT_STATE — trophic-hardware

**As of:** 2026-09-09
**Repository state:** migrated and consolidated; first engineering release pending.

---

## 1. Where the engineering actually stands

One product line is engineered: the **CEA Rack Platform (Rack A)**. Its design
is validated, clash-free and costed, and its document set is internally
consistent. It is **not released**, because the release artifacts (STEP / F3D /
manifest) do not exist on disk — see §4.

Two adjacent scopes were separated out of the rack during migration and are
correctly owned elsewhere:

- **Closed-loop water recovery** — shared CEA infrastructure serving a whole
  room, not a rack subassembly.
- **Ooty 20 × 12 ft room** — a reference implementation of a facility built
  from racks, not a product.

The Aquarium / Aquascaping family has no engineering yet. The tree names the
family and nothing more.

---

## 2. Product index

| Product / scope | ID | Owner class | Location | Stage |
|---|---|---|---|---|
| CEA Rack Platform (Rack A) | `RK-A` | A — Rack product | `products/cea/racks/rack-platform/` | Design validated |
| Closed-loop water recovery | `RK-A-WRS` | B — Shared CEA infra | `products/cea/irrigation/water-recovery/` | Design validated |
| Ooty 20 × 12 ft CEA room | `RK-A-ROOM` | C — Facility reference | `products/cea/facility-reference/ooty-room-20x12/` | Layout validated |

Owner classes are defined in `products/cea/racks/rack-platform/PRODUCT.md` §2.

---

## 3. Headline engineering figures

These are the current, post-correction values. They supersede any earlier
figure found in `archive/`.

| Quantity | Value | Source |
|---|---|---|
| Installed envelope (W × D × H) | 1456 × 690 × 1960 mm | RK-A-SYS Rev 2 |
| Structure-only envelope | 1256 × 563 × 1960 mm | RK-A-DWG Rev 2 |
| Phase-1 build envelope (no plenum) | 1456 × 648 × 1960 mm | RK-A-SYS Rev 2 |
| Dry mass | **112.66 kg** | Fusion `CEA_RACK_INTEGRATED_v2` v8 |
| Parts / occurrences | 45 / 177 | Fusion v8 |
| Unresolved interferences | **0** | Fusion v8 interference check |
| Tiers × bed heights | 4 × 300 / 700 / 1100 / 1500 mm | EDR-001 |
| Rack cost, Grow Phase 1 | ₹49,296 | RK-A-MFG Rev 2 |
| Room total, 11 racks | ₹13.2 lakh (ex-LED fixtures) | RK-A-ROOM Rev 4 |
| Water recovery ratio | 87.7 % | RK-A-WRS Rev 3 |
| Annual discharge saved vs drain-to-waste | 554 m³ | RK-A-WRS Rev 3 |

---

## 4. Release blocker

**The engineering release artifacts do not exist.**

`RK-A-MFG` §15 and `RK-A-DWG` reference a STEP/F3D/manifest set at
`C:\Users\karex\Desktop\CEA_RACK_v1`. That folder does not exist on the target
machine, and no CEA-named `.step`, `.stp`, `.f3d` or `.dxf` file exists anywhere
in the user profile. A probe write to the Desktop succeeded, so the path is
writable — the export never produced files. The export script counted a step as
successful when no exception was raised, rather than checking the return value
of `ExportManager.execute()`, so failure was never surfaced.

Nothing downstream of the CAD model can be released until the export is re-run
with a verified result. This is the single item standing between the rack and a
prototype build package. See `docs/system/RELEASE_INDEX.md`.

---

## 5. Open items, repository-wide

| ID | Type | Item |
|---|---|---|
| NT-01 | NEEDS TRACEABILITY | The full Fusion parameter master (~55 parameters) exists only in the Fusion design and in conversation history. Only a partial set is persisted, in `RK-A-BRIEF` Rev G |
| NT-02 | NEEDS TRACEABILITY | Structural validation records lack recorded load cases, acceptance criteria and the CAD version tested |
| ND-01 | NEEDS DECISION | `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` holds Rev 2 content while the published artifact of the same ID holds Rev 1. Which is the intended part-drawing release must be decided before drawings are reissued |
| ND-02 | NEEDS DECISION | Two published "Rack A Manufacturing Pack" artifacts exist. `9f5e09e5` is Rev 2 and current; `817abd35` is an orphan and should be retired or deliberately kept |
| ND-03 | NEEDS DECISION | Ventilation plenum is deferred to a Phase-2 entity. Phase 1 ships standalone EC fans. The plenum's interface to the rack is not yet frozen |

Full detail is in `products/cea/racks/rack-platform/CURRENT_STATE.md` and
`docs/system/MIGRATION_REPORT.md`.

---

## 6. Recommended next engineering action

Re-run the Fusion export for `CEA_RACK_INTEGRATED_v2` v8 with verified success
(check `ExportManager.execute()` return values and confirm file size on disk),
capture the manifest with per-file hashes, and record the result in
`docs/system/RELEASE_INDEX.md` as release **RK-A R1**. Persist the parameter
master in the same pass to close NT-01. That unblocks the prototype build.
