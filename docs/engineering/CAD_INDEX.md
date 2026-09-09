# CAD Index — Fusion 360 mapping

**Fusion 360 is authoritative for native CAD (ADR-006).** Cloud projects are not
moved, copied or mirrored into this repository. This index is the mapping
between them and the engineering artifacts held here.

STEP and F3D files are **exchange and release artifacts**, not the design.

---

## 1. Hub and project

| | |
|---|---|
| Hub | Karthikeyan D |
| Project | Karthikeyan's First Project |
| Project ID | `2016062635672326` |
| Data ID | `a.cGVyc29uYWw6dWUyOGQ0ZTQyIzIwMTYwNjI2MzU2NzIzMjY` |

Other projects on the hub, not used by this repository: `Assets`
(`D202609031134899751`), `Demo Project` (`D2016062635672301`).

---

## 2. Design mapping

| Product | Component / assembly | Fusion design | Type | Lineage URN | Latest | HW rev | Engineering release | Related drawing | Related STEP export |
|---|---|---|---|---|---|---|---|---|---|
| `RK-A` | Integrated rack, all systems | `CEA_RACK_INTEGRATED_v2` | f3d | `urn:adsk.wipprod:dm.lineage:khAY4bsfToGEcB_lXi-5Zg` | **v8** | Rev 5 | **`RK-A R1`** | `RK-A-DWG` Rev 2 | `INTEGRATED_v2_Rev5/` — verified, §5 |
| `RK-A` | Core structural platform | `CEA_RACK_PLATFORM_RackA_v1` | f3d | `urn:adsk.wipprod:dm.lineage:-iwIJ6QmSo-KS5PPHXubCg` | v5 | Rev H | *none — superseded by R1* | `RK-A-DWG` Rev 2 | root `STEP/`, superseded |

`CEA_RACK_INTEGRATED_v2` v1 is a working copy of `CEA_RACK_PLATFORM_RackA_v1`.
The platform design is the structural ancestor; the integrated design is the
current working model. **Do not edit the platform design to change the current
rack** — it is retained as the pre-integration baseline.

---

## 3. Version lineage — `CEA_RACK_INTEGRATED_v2`

| Version | Release note | Significance |
|---|---|---|
| **v8** | Rev 5 — deck mesh density corrected to 76 % open area | **Current.** Mass 112.66 kg. EDR-004 |
| v7 | Rev 4 — tray bulkheads, strainers, overflow drop continuity | ICR-001 |
| v6 | Rev 3 — systems integration, clash-free, closed-loop drainage | 0 unresolved interferences |
| v5 | Final integration geometry; depth held for 3-row room | Depth frozen for room set-out |
| v4 | Relocate enclosure to rack end; hold installed depth | EDR-011 method established |
| v3 | Systems integration: ventilation, electrical, sensors, LED hangers | |
| v2 | Systems integration: irrigation + drainage + recovery interface | ADR-001 |
| v1 | Working copy of RackA v1 — full systems integration | Branch point from the platform design |

## 4. Version lineage — `CEA_RACK_PLATFORM_RackA_v1`

| Version | Release note |
|---|---|
| v5 | User Saved |
| v4 | Rev H — base frame raised for cleaning clearance, wall anchors added |
| v3 | Rev F+ reflective panel accessory set |
| v2 | Rev E — interference clean, LED interface resolved |
| v1 | Modular CEA growing rack — Core/Grow platform, 4-tier, GI frame |

Version history for both designs was read from
`app.data.activeHub.dataProjects` → `dataFiles` → `versions` **without opening
any document**, so no version was consumed by the inventory.

---

## 5. Release exports — FOUND AND VERIFIED

**Corrected 2026-09-09.** This section previously recorded the export as missing.
It was not missing; it was in a different place.

| | |
|---|---|
| **Actual release store** | `E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\` |
| **Current release** | `INTEGRATED_v2_Rev5/` — `RK-A R1` |
| Path cited by `RK-A-MFG` §15 and `RK-A-DWG` | `C:\Users\karex\Desktop\CEA_RACK_v1` — **does not exist**, erratum |

### Store contents

| Folder | Content | Status |
|---|---|---|
| `INTEGRATED_v2_Rev5/` | 45 part STEP + assembly STEP + F3D + `MANIFEST.txt` | **CURRENT — release `RK-A R1`** |
| `INTEGRATED_v2/` | Pre-Rev5 integrated export; lacks the ICR-001 tray/overflow parts | Superseded |
| `STEP/`, `ASSEMBLY/`, `DXF/` (root) | Earlier `CEA_RACK_PLATFORM_RackA_v1` export | Superseded |
| `DXF/` | 5 flat patterns, from the **platform** design | **STALE — regenerate from v8 before cutting** |
| `mass_report.txt` | v5 working mass report, 1,246.35 kg (solid placeholders) | Historical. **Never quote as a mass** |

Full manifest with SHA-256 per file:
`products/cea/racks/rack-platform/release/RK-A-R1_MANIFEST.md`

### The export script defect is still real

The script increments its success counter when no exception is raised rather than
checking the return of `ExportManager.execute()`. That did not cause a failure here,
but it means a future failure would again be reported as success. Fix it before the
next export; the acceptance criteria below stand.

### Re-export requirements

1. Export from `CEA_RACK_INTEGRATED_v2` at the stated version, recorded in the manifest.
2. Check the boolean return of `ExportManager.execute()` for every file.
3. Confirm each file exists on disk with non-zero size after the call.
4. Emit a manifest with per-file SHA-256 hashes.
5. **Write to the documented release store, and make the documents cite it correctly.**
6. Record in `docs/system/RELEASE_INDEX.md`.

---

## 6. Working notes for scripted Fusion access

These are hard-won and prevent silent failures (EDR-011):

- Output returns via **stdout `print()`**, not the function return value.
- `occ.transform2 = matrix` silently reverts in parametric mode. Relocate by
  deleting all occurrences and recreating the component at absolute coordinates.
- `moveFeatures.createInput2()` rejects occurrences with
  `invalid argument inputEntities`.
- Interference results expose `BRepBody`. Read the component name via
  `b.assemblyContext.component.name`, falling back to `parentComponent`.
- Material density properties are in **kg/m³** — do not divide by 1000.
- Lineage can be read without opening a document (see §4).

---

## 7. Parameter master — PERSISTED

**NT-01 closed 2026-09-09.** The 55 user parameters were read directly from
`CEA_RACK_INTEGRATED_v2` v8 and persisted as
`products/cea/racks/rack-platform/design/RK-A-PARAM_Rev1_parameter-master.md`.

The identical set exists in `CEA_RACK_PLATFORM_RackA_v1`, confirming the integrated
design inherited it unchanged. `allParameters` totals 237 in the integrated design;
the remaining 182 are feature-level parameters from modelling operations, not design
inputs, and are deliberately not persisted.

Two things the parameter read resolved:

- **`Rack_Height` = 1950 mm against a 1960 mm envelope is not a conflict.** The model
  bounding box runs Z −10.0 to +1950.0; the feet sit 10 mm below the floor datum.
- **`Panel_Depth` = 563 mm** is the structure-only depth, confirming the documented
  figure. A 2 mm gap between `Rack_Depth` (650) and the documented Phase-1 build
  depth (648) remains unexplained and is carried as a low-priority item.
