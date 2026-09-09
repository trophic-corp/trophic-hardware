# Release Index

An **engineering release** is a frozen, verifiable set of artifacts issued for a
purpose (prototype, fabrication, vendor quotation). A document revision is not a
release.

---

## 1. Releases issued

| Release | Product | Source design | HW rev | Purpose | Issued | Status |
|---|---|---|---|---|---|---|
| **`RK-A R1`** | `RK-A` | Fusion `CEA_RACK_INTEGRATED_v2` **v8** | Rev 5 | Prototype fabrication | Exported 2026-09-05, verified 2026-09-09 | **ISSUED** |

Manifest with per-file SHA-256:
`products/cea/racks/rack-platform/release/RK-A-R1_MANIFEST.md`

**Release store:** `E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\INTEGRATED_v2_Rev5\`

Binaries are not committed to this repository. The manifest is the verifiable record.

---

## 2. RB-01 — CLOSED 2026-09-09

**The export existed all along; it was written to a different location.**

The earlier diagnosis — that the export silently failed and produced no files — was
**wrong**. The files were written to a synced Google Drive path, not to the Desktop
path that `RK-A-MFG` §15 and `RK-A-DWG` cite. Searching only the user profile found
nothing and the absence was misread as failure.

What was genuinely true:

| Claim | Verdict |
|---|---|
| `C:\Users\karex\Desktop\CEA_RACK_v1` does not exist | **Correct** — re-confirmed 2026-09-09 |
| Two issued documents cite a path that holds nothing | **Correct** — recorded as errata |
| The export script does not check `ExportManager.execute()` | **Correct** — still a defect, fix before the next export |
| The export produced no files | **Wrong** — 45 of 45 part files, plus assembly STEP and F3D, all present and valid |

Verification performed on the actual release: 45/45 files present, none missing,
none extra, none zero-byte, all `.step` files carrying a valid `ISO-10303-21`
header, and every headline figure reconciling against the live Fusion model.

**Lesson recorded:** an artifact not being where a document says it is, is not
evidence that it does not exist. Search by content and by product, not only by the
documented path.

---

## 3. Release definition — `RK-A R1`

What the release contains and the criteria it was verified against.

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
| Parameter master | `RK-A-PARAM` Rev 1 | **created** — closes NT-01 |
| Manifest | per-file SHA-256 | generated at export |

### Export acceptance criteria

All five were verified for `RK-A R1` on 2026-09-09 — criteria 2 and 3 after the fact rather than at export time. An export is not complete until all five hold:

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

`RK-A R1` is issued for **prototype fabrication**. Two items remain open against it
and constrain how it may be used:

| Item | Effect on this release |
|---|---|
| ND-01 | Part-drawings divergence unresolved — **do not issue part drawings** with this release. The structural drawings (`RK-A-DWG` Rev 2) are unaffected |
| **DXF flat patterns are stale** | The `DXF/` folder was exported from the platform design and covers 5 parts. **Regenerate from v8 before cutting any sheet-metal part** |
| ND-04 | Room set-out pitch not confirmed plenum-ready — affects installation, not fabrication |

NT-01 is **closed** by `RK-A-PARAM` Rev 1. NT-02 (depth-plane bracing) closes at
prototype test **T16** — which is precisely what this release exists to enable.

Before a **production** release: close ND-01, ND-02, NT-02, regenerate the DXF set,
and fix the export script to check `ExportManager.execute()`.

---

## 4. Release numbering

`<PRODUCT-ID> R<n>` — e.g. `RK-A R1`. Increments on any change to release
contents. A release is never edited after issue; it is superseded.
