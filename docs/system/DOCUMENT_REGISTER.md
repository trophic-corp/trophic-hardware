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

## 5. Documents that do not exist yet

| Would-be ID | Subject | Why it is needed |
|---|---|---|
| `RK-A-PARAM` | Fusion parameter master | NT-01. The ~55-parameter set is unpersisted |
| `RK-A-REL` | Engineering release manifest | RB-01. No release has been issued |

---

## 6. Rules

1. The repository copy and the published artifact are the **same content at the
   recorded revision**. Content hashes for the repository copies are recorded in
   the migration baseline commit.
2. To revise an authoritative document, issue a new revision — do not edit in
   place. The prior revision moves to `archive/superseded/`.
3. Never take a current value from anything classified SUPERSEDED.
4. An `UNKNOWN — NEEDS REVIEW` document is not usable for engineering until its
   NEEDS DECISION item is closed.
