# Release Index

An **engineering release** is a frozen, verifiable set of artifacts issued for a
purpose (prototype, fabrication, vendor quotation). A document revision is not a
release.

---

## 1. Releases issued

**None.**

No engineering release has been issued for any Trophic product. The rack
document set is at issue-ready revisions, but the CAD exchange artifacts that a
release must carry do not exist.

---

## 2. Release blocker RB-01 — CAD exchange artifacts missing

| | |
|---|---|
| **Status** | OPEN — blocks all releases for `RK-A` |
| **Affects** | `RK-A-MFG` §15, `RK-A-DWG` |
| **Referenced location** | `C:\Users\karex\Desktop\CEA_RACK_v1` |
| **Actual state** | Folder does not exist. No CEA-named `.step`, `.stp`, `.f3d` or `.dxf` anywhere in the user profile |
| **Checked** | Both `Desktop` and `OneDrive\Desktop` exist and contain no such folder |
| **Not a permissions problem** | A probe write to the Desktop succeeded |
| **Root cause** | The export script incremented its success counter when no exception was raised, instead of checking the return value of `ExportManager.execute()`. Silent failure was reported as success |

Two published documents currently reference an artifact that does not exist.

---

## 3. Planned release — `RK-A R1`

The first release, once RB-01 is closed.

| Field | Value |
|---|---|
| Release ID | `RK-A R1` |
| Purpose | Prototype fabrication |
| Source design | Fusion `CEA_RACK_INTEGRATED_v2` **v8** (Rev 5) |
| Hardware revision | Rev 5 |

### Contents

| Artifact | Format | Source |
|---|---|---|
| Full assembly | STEP AP242 | Fusion v8 |
| Full assembly | F3D archive | Fusion v8 |
| Flat patterns, sheet parts | DXF | Fusion v8 |
| Structural drawings | `RK-A-DWG` Rev 2 | this repository |
| Manufacturing pack | `RK-A-MFG` Rev 2 | this repository |
| Systems specification | `RK-A-SYS` Rev 2 + addendum | this repository |
| Validation record | `RK-A-QC` Rev 3 | this repository |
| Parameter master | `RK-A-PARAM` Rev 1 | to be created — closes NT-01 |
| Manifest | per-file SHA-256 | generated at export |

### Export acceptance criteria

An export is not complete until all five hold:

1. Exported from `CEA_RACK_INTEGRATED_v2` **v8**, with the version recorded in
   the manifest.
2. `ExportManager.execute()` returned **true** for every file, checked
   explicitly.
3. Every expected file exists on disk with non-zero size, verified after the
   call.
4. The manifest lists every file with its SHA-256 hash.
5. The manifest is recorded in this index with export date and manifest hash.

Criteria 2 and 3 exist specifically because their absence caused RB-01.

### Release gate

`RK-A R1` must not be issued while any of these are open:

| Item | Type |
|---|---|
| RB-01 | Release blocker — export missing |
| ND-01 | Part-drawings divergence unresolved |
| ND-04 | Room set-out pitch not confirmed plenum-ready |

NT-01 (parameter master) is closed by the release itself. NT-02 (structural
metadata) and ND-02 (duplicate artifact) do not block a **prototype** release
but must be closed before a production release.

---

## 4. Release numbering

`<PRODUCT-ID> R<n>` — e.g. `RK-A R1`. Increments on any change to release
contents. A release is never edited after issue; it is superseded.
