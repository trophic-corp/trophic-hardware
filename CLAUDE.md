# CLAUDE.md — Trophic Hardware Engineering Repository

This repository holds **physical product engineering** for Trophic. It is
deliberately separate from the Trophic CEA **software** repository, which is not
part of this repository and must never be ingested into it.

---

## 1. What this repository is

Trophic designs and manufactures hardware in two product families:

| Family | Scope |
|---|---|
| **CEA** | Growing racks, LED lighting, irrigation, environmental control, sensors and controllers |
| **Aquarium / Aquascaping** | Programmable lighting, sensors and controllers, lily pipes, filtration, pumps, CO₂ equipment, tools and accessories |

Manufacturing base: **Coimbatore, India** (411 m ASL).
R&D facility: **Ooty, India** (2,240 m ASL) — the reference CEA room.

Today only one product line has completed engineering: the **CEA Rack Platform
(Rack A)**. Everything else in the tree exists because it was needed to hold
that work, not as speculative scaffolding.

---

## 2. Context policy — read this before opening files

Artifacts here are large. A normal working session must **not** load the whole
tree. Load in this order and stop as soon as you have what you need.

### Always load (the working set)

1. `CLAUDE.md` — this file
2. `CURRENT_STATE.md` — repository-level state
3. `products/cea/racks/rack-platform/PRODUCT.md` — rack product definition
4. `products/cea/racks/rack-platform/CURRENT_STATE.md` — rack state and open items
5. `docs/decisions/DECISION_REGISTER.md` — the decision index (not the individual records)
6. The specific `products/cea/racks/rack-platform/interfaces/**` spec relevant to the task

That set is small and is enough for most rack work.

### Load only when the task requires it

| Artifact | Load when |
|---|---|
| `design/RK-A-SYS_Rev2_systems-specification.html` | Changing or querying a system in detail (irrigation, electrical, ventilation, sensing) |
| `drawings/RK-A-DWG_Rev2_structural-drawings.html` | Working on part geometry or fabrication detail |
| `manufacturing/RK-A-MFG_Rev2_manufacturing-pack.html` | Sourcing, BOM, costing, vendor packs |
| `verification/RK-A-QC_Rev3_engineering-validation-record.html` | Reviewing validation evidence or adding a verification record |
| `products/cea/irrigation/water-recovery/**` | Water recovery, reservoirs, terrace plant |
| `products/cea/facility-reference/ooty-room-20x12/**` | Room layout, multi-rack ecosystem, facility services |
| `docs/engineering/CAD_INDEX.md` | Touching Fusion 360 or a release export |
| `docs/references/REFERENCE_INDEX.md` | Looking for supplier research, standards, historical studies |
| `archive/**` | Provenance questions only. Never as a source of current values |

### Never load by default

- Anything under `archive/`
- Render captures (`archive/render-captures/`)
- The drawing generator source (`drawings/generator/`) unless regenerating drawings

---

## 3. Authority rules

1. **Fusion 360 is authoritative for native CAD geometry.** No file in this
   repository replaces it. STEP and F3D exports are *release artifacts*, not
   the design.
2. **The published HTML documents listed in `docs/system/DOCUMENT_REGISTER.md`
   are authoritative for engineering values.** The copies in this repository are
   the same content at the recorded revision.
3. Where a drawing and the CAD model disagree, **the model governs** — with one
   recorded historical exception (EDR-004, deck mesh density) where the drawing
   was right and the model was wrong.
4. Never silently reconcile a conflicting engineering value. Record it as
   **NEEDS DECISION** in the rack `CURRENT_STATE.md` and stop.
5. Never overwrite an artifact classified AUTHORITATIVE. Issue a new revision.

---

## 4. Identifier conventions

| Prefix | Meaning |
|---|---|
| `RK-A-###` | Rack A part number |
| `RK-A-BRIEF / SYS / DWG / MFG / QC / WRS / ROOM` | Document series |
| `ADR-###` | Architecture decision record — product architecture, scope, topology |
| `EDR-###` | Engineering decision record — sizing, material, physics, tolerance |
| `ICR-###` | Interface change record — a change crossing a defined interface |

File naming: `<DOC-ID>_<Rev>_<slug>.<ext>` — e.g.
`RK-A-SYS_Rev2_systems-specification.html`.

Decision records are written for **real decisions with consequences**, not for
routine CAD operations.

---

## 5. Hardware / software boundary

The existing Trophic CEA software project is a **separate repository** and is
out of scope here.

- Do **not** copy the Rack Specification, Fusion files, structural simulations
  or the Manufacturing Pack into the software repository.
- Do **not** modify software architecture or source from this repository.
- Information the software legitimately needs is published through
  **`trophic-contracts`** — a third, independent repository. See
  `docs/system/CONTRACT_EXTRACTION.md` for what is a candidate and why.

`trophic-contracts` carries only stable, machine-consumable interface facts
(channel maps, sensor identities, actuator polarity, safety interlocks, units).
It never carries geometry, drawings, BOMs or costs.

---

## 6. Working rules

- Preservation beats tidiness. If a reorganisation would risk provenance, keep
  the original and add an index entry pointing at it.
- Do not re-run a simulation or a validation because files moved. Existing
  evidence stays valid until the underlying design materially changes.
- Do not split an authoritative document merely because a folder exists for the
  pieces. Prefer indexing and linking over duplication.
- Do not create empty folders for structural symmetry.
- The rack product, shared CEA infrastructure, and the reference facility are
  three different owners. Check `PRODUCT.md` before filing anything new.
