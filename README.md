# trophic-hardware

Physical product engineering for Trophic — Controlled Environment Agriculture
and Aquarium / Aquascaping hardware.

Manufacturing: Coimbatore, India · R&D: Ooty, India

---

## Repository map

```
docs/
  system/          Cross-product registers: documents, releases, contracts, migration
  decisions/       ADR / EDR / ICR records and the decision register
  engineering/     CAD index (Fusion 360 mapping), engineering notes
  manufacturing/   Cross-product manufacturing practice
  quality/         Verification index and QA practice
  references/      Reference index — research, vendor sources, historical material
platform/
  IDENTIFIER_STANDARD.md  Product IDs, part numbers, document series, instrument tags
  PRODUCT_TEMPLATE.md     The Phase 0 document every new product starts from
  mechanical-standards/   Materials, grid, fasteners, ergonomics, wet/dry separation
  electrical-standards/   ELV boundary, protection, earthing, connectors
products/
  PRODUCT_INDEX.md        Every product, its stage, and what exists for it
  cea/
    racks/rack-platform/         RK-A — released
    irrigation/water-recovery/   WR-A — shared infrastructure, not the rack
    lighting/led-grow-bar/       LT-A — Phase 0
    environmental-control/ventilation-plenum/   EV-A — Phase 0, deferred
    sensors-controllers/         CT-A rack, CT-B room — Phase 0
    facility-reference/ooty-room-20x12/   Reference implementation, not a product
  aquarium/               7 products, all Phase 0, no engineering
archive/
  superseded/      Retained for provenance. Never a source of current values
  render-captures/ Working screenshots
  working-tooling/ One-off scripts kept for reproducibility
```

## Product status

| Product | ID | Stage | Notes |
|---|---|---|---|
| CEA Rack Platform (Rack A) | `RK-A` | Design validated, pre-prototype | Release blocked — see rack `CURRENT_STATE.md` |
| Closed-loop water recovery | `RK-A-WRS` | Design validated | Shared CEA infrastructure |
| Ooty 20 × 12 ft room | `RK-A-ROOM` | Layout validated | Reference implementation |
| LED grow bar | `LT-A` | Phase 0 | Interface fixed by the rack; internals open |
| Ducted ventilation plenum | `EV-A` | Phase 0 | Deferred by ADR-005; interface not frozen |
| Rack / room controller | `CT-A`, `CT-B` | Phase 0 | Architecture owned by the software side |
| Aquarium / aquascaping line | `AQ-*` | Phase 0 | 7 products, scope documents only |

## Where to start

Read `CLAUDE.md` first — it defines the context policy, authority rules and the
hardware/software boundary. Then `CURRENT_STATE.md`, then
`products/PRODUCT_INDEX.md`.

Before generating any 3D model from a Phase 0 document, read
`docs/system/CAD_SEED_GUIDE.md`.

## Related repositories

| Repository | Relationship |
|---|---|
| `trophic-contracts` | Hardware→software interface contracts, **v0.2.0**. Published *from* here, consumed by the software project |
| `trophic-corp/cea-orchestrator` | The CEA software suite. **Independent.** Not part of this repository, not modified from here, and must not ingest it. Audited 2026-09-09 — see `docs/system/CEA_SUITE_AUDIT.md` |

Native CAD lives in Autodesk Fusion 360 and is authoritative there. See
`docs/engineering/CAD_INDEX.md`.
