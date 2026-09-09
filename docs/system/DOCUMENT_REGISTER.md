# Document Register

Every engineering document, its authority classification, its revision, where
the repository copy lives and where the published artifact lives.

**Classification**

| Class | Meaning |
|---|---|
| `AUTHORITATIVE` | The governing source for its subject. Never overwritten — superseded by a new revision |
| `CURRENT WORKING` | Actively edited, not yet issued |
| `SUPPORTING EVIDENCE` | Records results; does not define requirements |
| `REFERENCE` | Informative only |
| `SUPERSEDED` | Retained for provenance. **Never a source of current values** |
| `UNKNOWN — NEEDS REVIEW` | Authority cannot be established without a decision |

---

## 1. Rack product — `RK-A`

| Doc ID | Title | Rev | Class | Repository copy | Published artifact |
|---|---|---|---|---|---|
| `RK-A-BRIEF` | CEA Rack Platform Brief | G | AUTHORITATIVE | `products/cea/racks/rack-platform/requirements/RK-A-BRIEF_RevG_platform-brief.html` | `claude.ai/code/artifact/d7a1cc62-50f1-4220-84ad-c3029f1d8e44` |
| `RK-A-SYS` | Rack A Systems Specification | 2 + addendum | AUTHORITATIVE | `.../design/RK-A-SYS_Rev2_systems-specification.html` | `.../0c57d39f-9bc9-4948-905b-133c1d5968b8` (v5) |
| `RK-A-DWG` | Rack A Structural Drawings | 2 | AUTHORITATIVE | `.../drawings/RK-A-DWG_Rev2_structural-drawings.html` | `.../d66da629-a6ca-406d-bb9d-f914d187d7ee` |
| `RK-A-MFG` | Rack A Manufacturing Pack | 2 | AUTHORITATIVE | `.../manufacturing/RK-A-MFG_Rev2_manufacturing-pack.html` | `.../9f5e09e5-c02a-4d5b-965e-43731a32c19c` |
| `RK-A-QC` | Engineering Validation Record | 3 | SUPPORTING EVIDENCE | `.../verification/RK-A-QC_Rev3_engineering-validation-record.html` | `.../62520307-f088-4d7d-8a69-242f1bff45c9` (v4) |
| `RK-A-PARAM` | Fusion Parameter Master | 1 | AUTHORITATIVE | `.../design/RK-A-PARAM_Rev1_parameter-master.md` | — read from CAD, not published |
| `RK-A-R1` | Engineering Release Manifest | — | AUTHORITATIVE | `.../release/RK-A-R1_MANIFEST.md` | — |

## 2. Shared CEA infrastructure

| Doc ID | Title | Rev | Class | Repository copy | Published artifact |
|---|---|---|---|---|---|
| `RK-A-WRS` | Closed-Loop Water Recovery | 3 | AUTHORITATIVE | `products/cea/irrigation/water-recovery/RK-A-WRS_Rev3_closed-loop-water-recovery.html` | `.../9145c6e4-0bf1-4b1a-ae46-3e77eea48917` |

## 3. Facility reference

| Doc ID | Title | Rev | Class | Repository copy | Published artifact |
|---|---|---|---|---|---|
| `RK-A-ROOM` | CEA Room Floor Plan, Ooty 20 × 12 ft | 4 | REFERENCE | `products/cea/facility-reference/ooty-room-20x12/RK-A-ROOM_Rev4_floor-plan.html` | `.../7d874376-ae8f-43c3-920b-aadcd35cf5c3` (v4) |

Classified REFERENCE, not AUTHORITATIVE, because it documents one worked
implementation rather than defining a product requirement. Its **engineering
content** (loads, set-out, water balance) is nonetheless validated and current.

## 4. Superseded and ambiguous

| Doc ID | Title | Rev | Class | Location | Note |
|---|---|---|---|---|---|
| `RK-R-01` | CEA Room Scaling Study | 1 | SUPERSEDED | `archive/superseded/RK-R-01_Rev1_cea-room-scaling-study.html` | Superseded by `RK-A-ROOM` Rev 4 |
| `RK-A-DWG` (part drawings, local build) | Rack A Part Drawings | 2 content | **UNKNOWN — NEEDS REVIEW** | `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` | **ND-01.** Holds Rev 2 content (11 chapters, corrected 1797 mm brace) while the published artifact of the same ID holds Rev 1 (14 chapters). Three chapters exist only in the published Rev 1. Not reconciled |
| `RK-A-DWG` (part drawings, published) | Rack A Part Drawings | 1 | SUPERSEDED (contested) | `.../1328d04f-6ad5-496c-b648-84346b111e39` | Superseded by structural drawings Rev 2 for the structural set, but carries three chapters the local build lacks. See ND-01 |
| `RK-A-MFG` (duplicate) | Rack A Manufacturing Pack | unlabelled, 04 Sep | **UNKNOWN — NEEDS REVIEW** | `.../817abd35-78e4-4efe-99dd-22aa8f558700` | **ND-02.** Orphaned duplicate. Referenced by nothing. Retire or state why kept |

---

## 5. Errata against issued documents

| Document | Erratum | Effect |
|---|---|---|
| `RK-A-MFG` Rev 2 §15 | Cites the CAD release location as `C:\Users\karex\Desktop\CEA_RACK_v1`. The actual store is `E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\` | Location reference only. No engineering value affected. Correct at next revision |
| `RK-A-DWG` Rev 2 | Same incorrect path | As above |
| `RK-A-MFG` Rev 2 | Cites `RK-A-QC` **Rev 2** for the T1–T18 acceptance set; current QC revision is Rev 3 | Reference lag, not a content conflict |
| `RK-A-SYS` Rev 2 §10 | Names the depth-plane sway test **P3**; superseded by **T16** in the RK-A-QC T1–T18 set | Naming lag. `RK-A-MFG` states the supersession explicitly. **T16 is the ID to use** |

## 6. BOM line-item mapping, drawing ↔ CAD

One case where the two disagree in form but not in substance, recorded so nobody
"fixes" it:

| | Drawing (`RK-A-DWG` / `parts.py`) | CAD (`RK-A R1` manifest) |
|---|---|---|
| Identity | `RK-A-104` Rear X-brace | `05_REAR_BRACE` |
| Quantity | **2** | **1** |
| Mass each | 1.06 kg | 2.071 kg |
| Total | 2.116 kg | 2.071 kg |

The drawing counts two individual braces; the CAD models the crossing pair as one
component. Totals agree to 2 %, consistent with shared material at the crossing.
1797 × 25 × 3 mm of steel at 7850 kg/m³ = 1.058 kg, so the drawing's per-piece figure
is arithmetically correct. **Not a discrepancy — a representation difference.**

---

## 7. Rules

1. The repository copy and the published artifact are the **same content at the
   recorded revision**. Content hashes for the repository copies are recorded in
   the migration baseline commit.
2. To revise an authoritative document, issue a new revision — do not edit in
   place. The prior revision moves to `archive/superseded/`.
3. Never take a current value from anything classified SUPERSEDED.
4. An `UNKNOWN — NEEDS REVIEW` document is not usable for engineering until its
   NEEDS DECISION item is closed.
