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
  mechanical-standards/   Shared mechanical conventions across products
products/
  cea/
    racks/rack-platform/  Rack A — the CEA growing rack product
    irrigation/water-recovery/   Shared CEA infrastructure (not part of the rack)
    facility-reference/ooty-room-20x12/   Reference implementation, not a product
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
| Aquarium / aquascaping line | — | Not started | Family reserved in the tree only |

## Where to start

Read `CLAUDE.md` first — it defines the context policy, authority rules and the
hardware/software boundary. Then `CURRENT_STATE.md`.

## Related repositories

| Repository | Relationship |
|---|---|
| `trophic-contracts` | Hardware→software interface contracts, **v0.2.0**. Published *from* here, consumed by the software project |
| `trophic-corp/cea-orchestrator` | The CEA software suite. **Independent.** Not part of this repository, not modified from here, and must not ingest it. Audited 2026-09-09 — see `docs/system/CEA_SUITE_AUDIT.md` |

Native CAD lives in Autodesk Fusion 360 and is authoritative there. See
`docs/engineering/CAD_INDEX.md`.
