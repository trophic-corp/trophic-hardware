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

Today one product line has completed engineering: the **CEA Rack Platform
(Rack A)** — independently reviewed and revised on 2026-09-10 (ECP-01, Rev 6, design of record `CEA_RACK_INTEGRATED_v3` v1); `RK-A R1` is constrained and `RK-A R2` is pending. Twelve other products exist as **Phase 0**
scope documents — real folders with real documents, no engineering. Three of them, the lighting program (`LT-A`, `AQ-LT-A`, `AQ-LT-B`), completed Phase 0A research on 2026-09-11 and wait on 0B architecture decisions.

`products/PRODUCT_INDEX.md` is the map. A Phase 0 document holds what is decided,
what is inherited, and what is open, and refuses to fill the gaps. **Thin sections
in those documents are accurate, not incomplete.**

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

For work on any **other** product, load `products/PRODUCT_INDEX.md` and that
product's `PRODUCT.md` instead of items 3–4.

That set is small and is enough for most rack work.

### Load only when the task requires it

| Artifact | Load when |
|---|---|
| `design/RK-A-SYS_Rev2_systems-specification.html` + `design/RK-A-SYS_Rev2_addendum-B.md` | Changing or querying a system in detail (irrigation, electrical, ventilation, sensing) |
| `drawings/RK-A-DWG_Rev3_structural-drawings.md` / `manufacturing/RK-A-MFG_Rev3_manufacturing-pack.md` | Part geometry, BOM, fasteners, assembly — Rev 2 HTML only for the sections Rev 3 does not restate |
| `drawings/RK-A-DWG_Rev2_structural-drawings.html` | Working on part geometry or fabrication detail |
| `manufacturing/RK-A-MFG_Rev2_manufacturing-pack.html` | Sourcing, BOM, costing, vendor packs |
| `verification/RK-A-QC_Rev4_engineering-validation-record.md` (Rev 3 HTML for Stage 2) | Reviewing validation evidence or adding a verification record |
| `verification/RK-A-REV_RevA_independent-engineering-review.md`, `changes/RK-A-ECP-01_RevA_engineering-change-package.md` | Understanding why Rev 6 differs from Rev 5, or reopening any ECP-01 decision |
| `products/cea/irrigation/water-recovery/**` | Water recovery, reservoirs, terrace plant |
| `products/cea/facility-reference/ooty-room-20x12/**` | Room layout, multi-rack ecosystem, facility services |
| `docs/engineering/CAD_INDEX.md` | Touching Fusion 360 or a release export |
| `docs/references/REFERENCE_INDEX.md` | Looking for supplier research, standards, historical studies |
| `docs/system/CEA_SUITE_AUDIT.md` | Any question about what the CEA software suite believes about the hardware, or why a contract says what it says |
| `docs/system/CAD_SEED_GUIDE.md` | **Before generating any 3D model from a Phase 0 document.** Defines model classes and what a generation prompt may not use |
| `docs/system/AGENT_ROUTING_POLICY.md` | Deciding whether and which specialist agent(s) to delegate to — see §7 |
| `platform/lighting/README.md` (common lighting area: control interface concept, cost model, launch plan), `products/aquarium/lighting/PLATFORM.md`, `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md`, `docs/references/lighting/**` | Any lighting work (`LT-A`, `AQ-LT-A`, `AQ-LT-B`, Smart Module): start at the common area's index, then the platform strategy, phase gates and shared research so nothing is redone |
| `platform/**` | Starting a new product, or deviating from a shared standard |
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
6. **A Phase 0 document's §4 "Industry reference points" are NOT Trophic decisions.**
   They may inform a conversation. They may never appear on a drawing, in a model
   that claims to be a design, or in a contract.
7. A generated CAD model is class ENVELOPE or CONCEPT until the product's open
   decisions are answered. It never becomes DESIGN by being edited.

This authority hierarchy is not delegable. No specialist agent under §7 may
approve a product, alter an approved requirement, change an authoritative CAD
model, mark a product Validated/Released, change a frozen interface, or write
a decision record as "decided" — see `docs/system/AGENT_ROUTING_POLICY.md`.

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
(instrument tags, actuator polarity, safety interlocks, hydraulic limits, units).
It never carries geometry, drawings, BOMs or costs.

**Audited 2026-09-09.** The CEA suite had been extracting hardware facts directly
from OCR'd copies of our documents — the coupling ADR-004 exists to prevent. The
audit found one wrong value in the suite (the G1 EC multiplier) and one dangerous
omission in our own contract (sequential draining). Both are fixed in
`trophic-contracts` v0.2.0. Read `docs/system/CEA_SUITE_AUDIT.md` before changing
anything that crosses the boundary.

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

---

## 7. Specialist agent routing

Six project-scoped specialist agents live in `.claude/agents/`:
`systems-architect`, `lighting-electronics-engineer`,
`plant-science-specialist`, `industrial-design-cmf`,
`manufacturing-sourcing-engineer`, `qa-reliability-engineer`.

Operating principle: **Main Claude owns the task. Specialists are consulted
only when their domain materially changes the answer. QA is a gate, not a
participant in every conversation.** Most tasks need zero or one specialist;
cross-domain tasks default to at most two; QA is invoked specifically for
verification, validation, release, and safety-critical gates — never as a
routine third participant.

Full routing levels, the routing table, disagreement handling, and the
"agents do not create authority" rule are in
`docs/system/AGENT_ROUTING_POLICY.md`. Each agent's own file states its
domain, when to use it, when not to, and its authority boundary — read the
policy file to decide *whether and which* agent to use, not this section.
