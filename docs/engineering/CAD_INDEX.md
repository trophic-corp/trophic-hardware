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
| `RK-A` | Integrated rack, all systems | `CEA_RACK_INTEGRATED_v2` | f3d | `urn:adsk.wipprod:dm.lineage:khAY4bsfToGEcB_lXi-5Zg` | **v8** | Rev 5 | *none issued* | `RK-A-DWG` Rev 2 | **MISSING — see §5** |
| `RK-A` | Core structural platform | `CEA_RACK_PLATFORM_RackA_v1` | f3d | `urn:adsk.wipprod:dm.lineage:-iwIJ6QmSo-KS5PPHXubCg` | v5 | Rev H | *none issued* | `RK-A-DWG` Rev 2 | **MISSING — see §5** |

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

## 5. Release exports — MISSING

`RK-A-MFG` §15 and `RK-A-DWG` both reference a release artifact set at:

```
C:\Users\karex\Desktop\CEA_RACK_v1
```

**That folder does not exist.** No CEA-named `.step`, `.stp`, `.f3d` or `.dxf`
file exists anywhere in the user profile — checked in both `Desktop` and
`OneDrive\Desktop`, both of which exist. A probe write to the Desktop
succeeded, so this is not a permissions failure.

Root cause: the export script incremented its success counter when no exception
was raised, rather than checking the return value of
`ExportManager.execute()`. Silent failure was reported as success.

**Two published documents therefore reference an artifact that does not exist.**
This is release blocker **RB-01**. See `docs/system/RELEASE_INDEX.md`.

### Re-export requirements

When the export is re-run it must:

1. Export from `CEA_RACK_INTEGRATED_v2` **v8** specifically, and record that
   version number in the manifest.
2. Check the boolean return of `ExportManager.execute()` for every file.
3. Confirm each file exists on disk with a non-zero size after the call.
4. Emit a manifest with per-file SHA-256 hashes.
5. Be recorded in `docs/system/RELEASE_INDEX.md` as release **RK-A R1**, with
   the Fusion version, export date and manifest hash.

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

## 7. Not yet persisted

The full Fusion **parameter master** (~55 parameters) exists only inside the
design. Only `Shelf_Pitch`, `Bed_Width`, `Grid_Pitch`, `Top_Bed_Height`,
`Flood_Depth` and `Number_of_Tiers` are persisted, partially, in `RK-A-BRIEF`
Rev G. Reading the full set requires opening the design.

Tracked as **NT-01**. It has not been reconstructed from memory.
