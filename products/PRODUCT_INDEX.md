# Product Index

Every Trophic hardware product, its stage, and what exists for it.

**Stages:** Phase 0 (scope only) · Concept · Design · Validated · **Released**

---

## CEA

| Product | ID | Class | Stage | CAD | Documents |
|---|---|---|---|---|---|
| CEA Rack Platform | `RK-A` | A | **Released — `RK-A R1`** | `CEA_RACK_INTEGRATED_v2` v8, class DESIGN | BRIEF, SYS, DWG, MFG, QC, PARAM, R1 |
| Closed-loop water recovery | `WR-A` | B | Validated | None | `RK-A-WRS` Rev 3 |
| LED grow bar | `LT-A` | A | **Phase 0** | Envelope only (`06_LED_FIXTURE_ENV`) | PRODUCT.md |
| Ducted ventilation plenum | `EV-A` | A | **Phase 0** (deferred, ADR-005) | Envelope only (`07_PLENUM`) | PRODUCT.md |
| Rack controller | `CT-A` | A | **Phase 0** | Envelope only (`11_ENCLOSURE_IP65`) | PRODUCT.md |
| Room controller | `CT-B` | B | **Phase 0** | **None** | PRODUCT.md |

Facility reference (not a product): Ooty 20 × 12 ft room, `RK-A-ROOM` Rev 4.

## Aquarium / Aquascaping

No engineering exists in this family. All Phase 0, no CAD.

| Product | ID | Notes |
|---|---|---|
| Programmable aquarium light | `AQ-LT-A` | Closest to existing competence — see `LT-A` |
| Sensor / controller | `AQ-CT-A` | Tests the CEA capability model's claim of "no new platform work" |
| Lily pipes | `AQ-LP-A` | Glass or acrylic — first material decision |
| Filtration | `AQ-FL-A` | Highest complexity, furthest from competence |
| Pumps | `AQ-PU-A` | Make-or-buy may be the whole answer |
| CO₂ equipment | `AQ-CO-A` | The one aquarium product with a real safety dimension |
| Tools and accessories | `AQ-TL-A` | Lowest risk; plausible first ship |

---

## Honest summary

**One product is engineered.** One more has a validated design and no CAD. Eleven are
scope statements.

That ratio is correct for where the company is, and the tree is shaped to hold it
without pretending otherwise. What matters is that a Phase 0 folder is visibly Phase 0
— every document in one leads with its stage and separates decided from open.

## Cross-product decisions outstanding

Decisions that affect more than one product and should not be made inside one:

| # | Decision | Products |
|---|---|---|
| X1 | Do `LT-A` and `AQ-LT-A` share a driver platform and optical toolchain? | `LT-A`, `AQ-LT-A` |
| X2 | Does `AQ-FL-A` use `AQ-PU-A` or a bought-in pump? | `AQ-FL-A`, `AQ-PU-A` |
| X3 | Hose size standard across the aquarium range | `AQ-LP-A`, `AQ-FL-A` |
| X4 | Is `AQ-CT-A` a standalone product or the hub of an `AQ-*` system? | All aquarium |
| X5 | Do `CT-A` and `AQ-CT-A` share firmware, bus or enclosure? | `CT-A`, `AQ-CT-A` |

X3 is the one most likely to be decided twice by accident.

## Adding a product

1. Assign an ID from `platform/IDENTIFIER_STANDARD.md`.
2. Copy `platform/PRODUCT_TEMPLATE.md` to the product folder as `PRODUCT.md`.
3. Add a row here.
4. Do **not** create the sub-folder structure (`design/`, `drawings/`,
   `manufacturing/`, `verification/`, `release/`) until there is something to put in
   it. Empty folders are not scaffolding, they are noise.
