# Migration Report — Trophic Hardware Workspace

**Date:** 2026-09-09
**Scope:** Migration and consolidation of existing CEA rack engineering work
into a long-term hardware engineering repository.
**Nature:** Non-destructive. No engineering was redesigned, no artifact was
recreated where an authoritative one existed, and no design work was restarted.

---

## Deliverable 1 — Existing artifact inventory

### 1.1 Workspace files found

| File | Size | Type |
|---|---|---|
| `cea_rack_phase0.html` | 179.1 KB | Platform brief, Rev G |
| `cea_rack_systems_spec.html` | 92.8 KB | Systems specification, Rev 2 |
| `cea_rack_structural_drawings.html` | 153.9 KB | Structural drawings, Rev 2 |
| `cea_rack_mfg_pack.html` | 67.3 KB | Manufacturing pack, Rev 2 |
| `cea_qaqc_record.html` | 56.0 KB | Engineering validation record, Rev 3 |
| `cea_water_recovery.html` | 42.8 KB | Closed-loop water recovery, Rev 3 |
| `cea_room_phase2.html` | 41.0 KB | Room floor plan, Rev 4 |
| `cea_room_phase2_rev1_backup.html` | 34.9 KB | Room scaling study, Rev 1 |
| `cea_rack_part_drawings.html` | 153.6 KB | Part drawings — **diverged**, see D15 |
| `dwg/gen.py` | 19.6 KB | SVG four-view drawing generator |
| `dwg/parts.py` | 23.8 KB | 14-part dimension table |
| `dwg/build.py` | 22.2 KB | Drawing document assembler |
| `shot.py`, `shot2.py`, `shot3.py`, `shot4.py` | 2.3 KB total | One-off Fusion capture scripts |
| 9 × PNG | 1.5 MB total | Render and drawing captures |

**24 files.** Nothing else was present in the workspace.

### 1.2 Published artifacts found

| Document | Rev | Artifact URL |
|---|---|---|
| CEA Rack Platform Brief | G | `claude.ai/code/artifact/d7a1cc62-50f1-4220-84ad-c3029f1d8e44` |
| Rack A Systems Specification | 2 + addendum | `.../0c57d39f-9bc9-4948-905b-133c1d5968b8` (v5) |
| Closed-Loop Water Recovery | 3 | `.../9145c6e4-0bf1-4b1a-ae46-3e77eea48917` |
| CEA Room Floor Plan | 4 | `.../7d874376-ae8f-43c3-920b-aadcd35cf5c3` (v4) |
| Rack A Structural Drawings | 2 | `.../d66da629-a6ca-406d-bb9d-f914d187d7ee` |
| Rack A Part Drawings | 1 | `.../1328d04f-6ad5-496c-b648-84346b111e39` |
| Rack A Manufacturing Pack | 2 | `.../9f5e09e5-c02a-4d5b-965e-43731a32c19c` |
| Rack A Manufacturing Pack — **duplicate** | unlabelled | `.../817abd35-78e4-4efe-99dd-22aa8f558700` |
| Engineering Validation Record | 3 | `.../62520307-f088-4d7d-8a69-242f1bff45c9` (v4) |

**9 published artifacts, of which 1 is an orphaned duplicate.**

### 1.3 Fusion 360 inventory

Read from `app.data.activeHub.dataProjects` → `dataFiles` → `versions`
**without opening any document**, so no version was consumed by the inventory.

Hub `Karthikeyan D`, project `Karthikeyan's First Project`
(`2016062635672326`). Two relevant designs:

- `CEA_RACK_INTEGRATED_v2` — 8 versions, latest v8 (Rev 5)
- `CEA_RACK_PLATFORM_RackA_v1` — 5 versions, latest v5 (Rev H)

Full lineage with per-version release notes is in
`docs/engineering/CAD_INDEX.md` §3–4. Other hub projects (`Assets`,
`Demo Project`) are unrelated.

### 1.4 Filesystem probe — target machine

> **Corrected 2026-09-09.** The conclusion drawn from this probe was wrong. See
> §"Correction" at the end of this report.


Searched the entire user profile for CEA-named `.step`, `.stp`, `.f3d` and
`.dxf`. **Zero results.** `C:\Users\karex\Desktop\CEA_RACK_v1` does not exist.
Both `Desktop` and `OneDrive\Desktop` exist and contain no such folder. A probe
write to the Desktop succeeded.

---

## Deliverable 2 — Authority and revision classification

| Artifact | Class | Rationale |
|---|---|---|
| `RK-A-BRIEF` Rev G | AUTHORITATIVE | Governing requirements for the rack |
| `RK-A-SYS` Rev 2 + addendum | AUTHORITATIVE | Governing systems definition |
| `RK-A-DWG` Rev 2 (structural) | AUTHORITATIVE | Current issued drawing set; supersedes Rev 1 for the structural parts |
| `RK-A-MFG` Rev 2 | AUTHORITATIVE | Current manufacturing definition |
| `RK-A-QC` Rev 3 | SUPPORTING EVIDENCE | Records results; does not define requirements |
| `RK-A-WRS` Rev 3 | AUTHORITATIVE | Governing for shared water infrastructure |
| `RK-A-ROOM` Rev 4 | REFERENCE | One worked facility implementation, not a product requirement. Engineering content nonetheless current |
| `RK-R-01` Rev 1 (room scaling study) | SUPERSEDED | Superseded by `RK-A-ROOM` Rev 4 |
| `cea_rack_part_drawings.html` (local) | **UNKNOWN — NEEDS REVIEW** | Content-revision conflict, see D15 |
| Part Drawings published Rev 1 | SUPERSEDED (contested) | Carries three chapters the local build lacks |
| Manufacturing Pack `817abd35` | **UNKNOWN — NEEDS REVIEW** | Orphaned duplicate, referenced by nothing |
| `dwg/*.py` | CURRENT WORKING | Live generator; source of `RK-A-DWG` Rev 2 |
| PNG captures | REFERENCE / HISTORICAL | Working captures |
| `shot*.py` | HISTORICAL | One-off tooling, kept for reproducibility |

**Revision relationships established**

- `RK-A-ROOM` Rev 4 ← Rev 3 (dropped §08 Building, restored) ← `RK-R-01` Rev 1
- `RK-A-DWG` Rev 2 ← Rev 1 — Rev 2 corrects the `RK-A-104` brace length
- `CEA_RACK_INTEGRATED_v2` v1 ← working copy of `CEA_RACK_PLATFORM_RackA_v1`
- `RK-A-MFG` Rev 2 ← Rev 1, reissued against corrected mass and geometry

**Newest filename was not assumed authoritative.** The clearest case:
`cea_rack_part_drawings.html` is the newer file on disk but its authority is
genuinely in question, so it was archived rather than promoted.

---

## Deliverable 3 — Migration map

| Current location | Target location | Action |
|---|---|---|
| `cea_rack_phase0.html` | `products/cea/racks/rack-platform/requirements/RK-A-BRIEF_RevG_platform-brief.html` | MOVE + RENAME |
| `cea_rack_systems_spec.html` | `.../rack-platform/design/RK-A-SYS_Rev2_systems-specification.html` | MOVE + RENAME |
| `cea_rack_structural_drawings.html` | `.../rack-platform/drawings/RK-A-DWG_Rev2_structural-drawings.html` | MOVE + RENAME |
| `cea_rack_mfg_pack.html` | `.../rack-platform/manufacturing/RK-A-MFG_Rev2_manufacturing-pack.html` | MOVE + RENAME |
| `cea_qaqc_record.html` | `.../rack-platform/verification/RK-A-QC_Rev3_engineering-validation-record.html` | MOVE + RENAME |
| `cea_water_recovery.html` | `products/cea/irrigation/water-recovery/RK-A-WRS_Rev3_...html` | MOVE + RENAME + **REASSIGN OWNER** |
| `cea_room_phase2.html` | `products/cea/facility-reference/ooty-room-20x12/RK-A-ROOM_Rev4_floor-plan.html` | MOVE + RENAME + **REASSIGN OWNER** |
| `dwg/{gen,parts,build}.py` | `.../rack-platform/drawings/generator/` | MOVE |
| `cea_room_phase2_rev1_backup.html` | `archive/superseded/RK-R-01_Rev1_cea-room-scaling-study.html` | ARCHIVE |
| `cea_rack_part_drawings.html` | `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` | ARCHIVE + **NEEDS REVIEW** |
| 9 × PNG | `archive/render-captures/` | ARCHIVE |
| `shot*.py` (4) | `archive/working-tooling/` | ARCHIVE |
| Fusion cloud projects | *unchanged* | **INDEX** — `docs/engineering/CAD_INDEX.md` |
| 9 published artifacts | *unchanged* | **INDEX** — `docs/system/DOCUMENT_REGISTER.md` |

No file was deleted. No file content was altered.

---

## Deliverable 4 — Final repository tree

```
trophic-hardware/
├── CLAUDE.md                  context policy, authority rules, HW/SW boundary
├── CURRENT_STATE.md           repository-level state
├── README.md
├── docs/
│   ├── system/
│   │   ├── DOCUMENT_REGISTER.md
│   │   ├── RELEASE_INDEX.md
│   │   ├── CONTRACT_EXTRACTION.md
│   │   └── MIGRATION_REPORT.md          (this file)
│   ├── decisions/
│   │   ├── DECISION_REGISTER.md
│   │   └── records/   6 ADR · 12 EDR · 4 ICR
│   ├── engineering/CAD_INDEX.md
│   ├── quality/VERIFICATION_INDEX.md
│   └── references/REFERENCE_INDEX.md
├── products/cea/
│   ├── racks/rack-platform/             A — rack product
│   │   ├── PRODUCT.md
│   │   ├── CURRENT_STATE.md
│   │   ├── requirements/  RK-A-BRIEF Rev G
│   │   ├── design/        RK-A-SYS Rev 2
│   │   ├── drawings/      RK-A-DWG Rev 2 + generator/
│   │   ├── manufacturing/ RK-A-MFG Rev 2
│   │   ├── verification/  RK-A-QC Rev 3
│   │   └── interfaces/    mechanical · electrical · hydraulic · control
│   ├── irrigation/water-recovery/       B — shared CEA infrastructure
│   │   ├── README.md
│   │   └── RK-A-WRS Rev 3
│   └── facility-reference/ooty-room-20x12/   C — facility reference
│       ├── README.md
│       └── RK-A-ROOM Rev 4
└── archive/
    ├── superseded/        2 documents
    ├── render-captures/   9 PNG
    └── working-tooling/   4 scripts
```

Sibling repository, **not** a subdirectory:

```
trophic-contracts/   README · CHANGELOG · conventions · safety · hydraulic · geometry · process
```

Empty directories created during scaffolding (`platform/mechanical-standards`,
`docs/manufacturing`, `.../release`) were **removed** rather than kept to
satisfy the tree.

---

## Deliverable 5 — Files created

| File | Purpose |
|---|---|
| `CLAUDE.md` | Context policy, authority rules, identifier conventions, HW/SW boundary |
| `CURRENT_STATE.md` | Repository state, headline figures, release blocker, open items |
| `README.md` | Repository map and product status |
| `products/cea/racks/rack-platform/PRODUCT.md` | Rack product definition, scope boundary, frozen parameters |
| `products/cea/racks/rack-platform/CURRENT_STATE.md` | Rack state, corrections made, NEEDS TRACEABILITY, NEEDS DECISION |
| `docs/decisions/DECISION_REGISTER.md` + 22 records | 6 ADR, 12 EDR, 4 ICR |
| `docs/engineering/CAD_INDEX.md` | Fusion mapping, lineage, export requirements, scripting notes |
| `docs/system/DOCUMENT_REGISTER.md` | Every document, class, revision, repository copy, published URL |
| `docs/system/RELEASE_INDEX.md` | Release blocker, planned `RK-A R1`, export acceptance criteria |
| `docs/system/CONTRACT_EXTRACTION.md` | Candidate contract content and what is blocked |
| `docs/system/MIGRATION_REPORT.md` | This report |
| `docs/quality/VERIFICATION_INDEX.md` | 10 verification records, traceability gaps |
| `docs/references/REFERENCE_INDEX.md` | Standards, methods, historical and vendor material |
| `interfaces/{hydraulic,mechanical,electrical,control}/README.md` | Four interface specifications |
| `products/cea/irrigation/water-recovery/README.md` | Scope, architecture, key figures |
| `products/cea/facility-reference/ooty-room-20x12/README.md` | Scope and layout rationale |
| `trophic-contracts/` (8 files) | Contract publication v0.1.0 |

**No created file replaces or restates an authoritative document.** Every one is
an index, a decision record, an interface specification or a state summary.

---

## Deliverable 6 — Files moved and renamed

12 moves and 2 groups (9 PNG, 4 scripts) — see Deliverable 3. All content
byte-identical; SHA-256 hashes of every migrated HTML are recorded in the
baseline commit `9c4b72e`.

---

## Deliverable 7 — Files deliberately left in place

| Artifact | Why |
|---|---|
| Both Fusion cloud designs and all 13 versions | ADR-006. Moving or copying them would break the lineage that is the point of them. Indexed instead |
| All 9 published artifacts | The published URLs are the shareable record. Repository copies carry the same content; the artifacts are indexed, not migrated |
| The existing CEA software repository | Out of scope, untouched, and must remain independent (ADR-004) |
| `archive/**` contents | Retained in place after archiving. Nothing was deleted |

---

## Deliverable 8 — Fusion 360 mapping

Full mapping in `docs/engineering/CAD_INDEX.md`. Summary:

| Product | Component | Fusion design | Latest | HW rev | Release | Drawing | STEP |
|---|---|---|---|---|---|---|---|
| `RK-A` | Integrated rack | `CEA_RACK_INTEGRATED_v2` | v8 | Rev 5 | none | `RK-A-DWG` Rev 2 | **MISSING** |
| `RK-A` | Structural platform | `CEA_RACK_PLATFORM_RackA_v1` | v5 | Rev H | none | `RK-A-DWG` Rev 2 | **MISSING** |

Version history preserved intact; the inventory did not open a document.

---

## Deliverable 9 — Current CEA Rack product state

Design validated, pre-prototype, **not released**.

| Quantity | Value |
|---|---|
| Installed envelope | 1456 × 690 × 1960 mm |
| Phase-1 build envelope | 1456 × 648 × 1960 mm |
| Dry mass | 112.66 kg |
| Parts / occurrences | 45 / 177 |
| Unresolved interferences | 0 |
| Tiers | 4, bed datums 300/700/1100/1500 mm |
| Cost, Grow Phase 1 | ₹49,296 |

Full detail in `products/cea/racks/rack-platform/CURRENT_STATE.md`.

---

## Deliverable 10 — Existing validation evidence retained

10 verification records indexed in `docs/quality/VERIFICATION_INDEX.md`.
**Nothing was re-run because of the migration.** Eight records are fully
traceable; VR-07 (structural adequacy) is marked NEEDS TRACEABILITY rather than
having its missing metadata invented.

---

## Deliverable 11 — Decision records extracted

**22 records: 6 ADR, 12 EDR, 4 ICR.** Indexed in
`docs/decisions/DECISION_REGISTER.md`.

Records were written for decisions with consequences — architecture, physics,
material, safety polarity, interface change. **No record was manufactured for a
routine CAD operation.** ICR-004 is recorded as **OPEN**, not resolved, because
the plenum interface genuinely is not frozen.

---

## Deliverable 12 — Hardware/software interfaces discovered

Four interface specifications written, from the existing designs:

| Interface | State |
|---|---|
| Hydraulic (`IF-RK-A-HYD`) | **Complete.** Both interface points fully specified |
| Mechanical (`IF-RK-A-MEC`) | **Mostly complete.** Plenum interface open (ICR-004) |
| Electrical (`IF-RK-A-ELE`) | **Partial.** Type A RCBO and standards established; 7 items marked NEEDS SPECIFICATION |
| Control (`IF-RK-A-CTL`) | **Partial.** Fail-safe polarity and physical limits established; 8 items marked NEEDS SPECIFICATION |

The control interface gap is the significant finding: the sensor and actuator
inventory is modelled in CAD but has never been extracted into a machine-readable
map. **That is a hardware deliverable and it is the main prerequisite for
software integration.**

---

## Deliverable 13 — Candidate `trophic-contracts` content

Published as v0.1.0 in the sibling `trophic-contracts` repository:

| Contract | Derivation |
|---|---|
| `safety/valve-fail-states` | EDR-007 |
| `hydraulic/supply-limits` | EDR-005, ICR-002 |
| `hydraulic/drain-topology` | EDR-006, ICR-001, ICR-003 |
| `geometry/bed-datum` | EDR-001 |
| `process/reuse-decision` | ADR-001, EDR-009 |
| `conventions/units` | Uniform usage across the document set |

**Deliberately not published** (blocked on hardware specification): sensor
inventory, sensor placement, actuator inventory, channel map, transport
protocol, interlocks, telemetry rates, alarm set. A placeholder contract would
be worse than a missing one.

**No software implementation was created and the existing software repository
was not touched.**

---

## Deliverable 14 — Reference-only material

Indexed in `docs/references/REFERENCE_INDEX.md`: 6 standards (IS 4923, IS 3043,
IS 1893, IS 4985, IS 732, IS 12234/EN 1717), 6 methods and published data sets
(NIOSH, Hazen-Williams, altitude/pressure, plenum CFD, UV-C iron degradation,
mesh density), 4 historical items and 1 vendor source.

Held **outside default context** by policy. The index exists so they can be
found without being loaded.

---

## Deliverable 15 — Superseded and ambiguous artifacts

| Artifact | Disposition |
|---|---|
| `RK-R-01` Rev 1, room scaling study | SUPERSEDED. Archived, indexed as HIST-01 |
| PNG captures, `shot*.py` | HISTORICAL. Archived |
| **Part drawings divergence** | **UNRESOLVED — ND-01** |
| **Duplicate manufacturing pack** | **UNRESOLVED — ND-02** |

### ND-01 — the part-drawings divergence, in detail

The local file `cea_rack_part_drawings.html` contains **Rev 2 content**:
11 chapters, and it contains the corrected `1797` mm brace dimension. The
published artifact bearing the same document ID (`1328d04f`) contains
**Rev 1**: 14 chapters, with the erroneous 1345 mm brace.

So the local build is *more correct on the dimension that matters* but has
*three fewer chapters*. Neither is a clean superset of the other.

**This was not silently reconciled.** The local build was archived under a name
that states the conflict, and the decision is escalated.

---

## Deliverable 16 — NEEDS TRACEABILITY items

| ID | Item |
|---|---|
| **NT-01** | Fusion parameter master (~55 parameters) exists only inside the design. Only 6 parameters are persisted, partially, in `RK-A-BRIEF` Rev G. Reading the full set requires opening the design. **Not reconstructed from memory** |
| **NT-02** | Structural validation (VR-07) records a conclusion but not the design revision analysed, CAD version, assumed loads, boundary conditions, acceptance criterion or limitations. **Metadata not invented** |

---

## Deliverable 17 — NEEDS DECISION items

| ID | Decision required |
|---|---|
| **RB-01** | **Release blocker.** The CAD export referenced by two published documents never produced files. Root cause: the export script counted success on the absence of an exception rather than on `ExportManager.execute()`'s return value |
| **ND-01** | Part-drawings divergence — which build is the intended release, and what happens to the three chapters that exist only in published Rev 1 |
| **ND-02** | Duplicate manufacturing pack artifact `817abd35` — retire or state why kept |
| **ND-03** | Plenum interface freeze — decide before the Phase-1 fabrication release, because the constraint lands on the racks built first |
| **ND-04** | Confirm room set-out uses the plenum-ready 690 mm pitch for Phase-1 racks that are only 648 mm deep |

---

## Deliverable 18 — Recommended next engineering action

**Re-run the Fusion export with verified success, and persist the parameter
master in the same session.**

1. Open `CEA_RACK_INTEGRATED_v2` **v8**.
2. Export STEP AP242, F3D and sheet-part DXF, checking
   `ExportManager.execute()` returns true for every file and confirming non-zero
   file size on disk after each call.
3. Emit a manifest with per-file SHA-256 hashes.
4. In the same session, dump the full parameter table and persist it as
   `design/RK-A-PARAM_Rev1_parameter-master.md`. **Closes NT-01.**
5. Record the result in `docs/system/RELEASE_INDEX.md` as release `RK-A R1`.
   **Closes RB-01.**

That single session clears the release blocker and the larger traceability gap,
and unblocks the prototype build. ND-01 should be put to the user before any
part-drawing reissue; it does not block the release above.

---

## Safety check (Phase 4) — findings

| Risk | Assessment |
|---|---|
| Possible information loss | **None.** No file deleted; no content altered; SHA-256 recorded for every migrated HTML in commit `9c4b72e` |
| Duplicate authoritative files | **One found** — Manufacturing Pack `817abd35`. Flagged ND-02, not resolved unilaterally |
| Broken links | Published-artifact URLs preserved verbatim in `DOCUMENT_REGISTER.md`. Internal document cross-references are unchanged because no document content was edited |
| Fusion dependencies | **Preserved.** No cloud project moved, copied or opened. Lineage intact |
| Unresolved revision relationships | **Two** — ND-01 (part drawings) and ND-02 (duplicate pack). Both escalated, neither reconciled |
| Provenance risk | Where authority was uncertain, the original was retained and named to state the conflict rather than being promoted or discarded |

## What was explicitly *not* done

- The rack was **not** redesigned, and no component was changed to fit the
  repository structure.
- No simulation or calculation was re-run because of the migration.
- No authoritative document was split merely because a folder existed for the
  pieces.
- No conflicting engineering value was silently reconciled.
- The existing CEA software repository was **not** read, modified or ingested.
- No decision record was manufactured for a routine CAD operation.
- No missing metadata was invented to make a record look complete.


---

## Correction — 2026-09-09

**Deliverable 17 recorded RB-01 as "the export never produced files". That was wrong.**

The Phase 1 probe searched the Windows user profile, found no CEA-named `.step`,
`.stp`, `.f3d` or `.dxf`, and concluded the export had silently failed. The export
had in fact written to a synced Google Drive path outside the user profile:

```
E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\
```

It contains a complete, valid release — 45 of 45 part STEP files, assembly STEP and
F3D, and a manifest — verified on 2026-09-09 and issued as **`RK-A R1`**.

What the probe got right: the Desktop path really does not exist, and two issued
documents really do cite it. Those are now recorded as errata rather than as a
release blocker.

**Method lesson.** An artifact not being where a document says it is, is not evidence
that it does not exist. The probe searched one location family and generalised from
its emptiness. Searching by product name across accessible drives — or simply asking
— would have found it. The absence of evidence was reported with more confidence
than it deserved.

The same caution applies to the remaining open items: NT-02, ND-01 and ND-02 are
recorded as unresolved because the information genuinely conflicts or is genuinely
absent from the documents, not because a single search came back empty.
