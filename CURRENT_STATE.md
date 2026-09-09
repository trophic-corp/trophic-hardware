# CURRENT_STATE — trophic-hardware

**As of:** 2026-09-09
**Repository state:** migrated and consolidated; first engineering release pending.

---

## 1. Where the engineering actually stands

One product line is engineered: the **CEA Rack Platform (Rack A)**. Its design
is validated, clash-free and costed, and its document set is internally
consistent. It is **not released**, because the release artifacts (STEP / F3D /
manifest) do not exist on disk — see §4.

Two adjacent scopes were separated out of the rack during migration and are
correctly owned elsewhere:

- **Closed-loop water recovery** — shared CEA infrastructure serving a whole
  room, not a rack subassembly.
- **Ooty 20 × 12 ft room** — a reference implementation of a facility built
  from racks, not a product.

Eleven further products now have **Phase 0 documents** — four CEA and seven
aquarium. None has engineering. Each document separates what is inherited and
decided from what is open, and does not fill the gaps; the CEA ones carry real
inherited interface facts because the rack fixed them, and the aquarium ones are
mostly open questions, which is correct.

Shared standards extracted from the rack's decisions now live in `platform/`.

---

## 2. Product index

| Product / scope | ID | Owner class | Location | Stage |
|---|---|---|---|---|
| CEA Rack Platform (Rack A) | `RK-A` | A — Rack product | `products/cea/racks/rack-platform/` | Design validated |
| Closed-loop water recovery | `RK-A-WRS` | B — Shared CEA infra | `products/cea/irrigation/water-recovery/` | Design validated |
| Ooty 20 × 12 ft CEA room | `RK-A-ROOM` | C — Facility reference | `products/cea/facility-reference/ooty-room-20x12/` | Layout validated |
| LED grow bar | `LT-A` | A | `products/cea/lighting/led-grow-bar/` | **Phase 0** |
| Ducted ventilation plenum | `EV-A` | A | `products/cea/environmental-control/ventilation-plenum/` | **Phase 0** |
| Rack controller | `CT-A` | A | `products/cea/sensors-controllers/rack-controller/` | **Phase 0** |
| Room controller | `CT-B` | B | `products/cea/sensors-controllers/room-controller/` | **Phase 0** |
| Aquarium range, 7 products | `AQ-*` | A | `products/aquarium/` | **Phase 0** |

Owner classes are defined in `products/cea/racks/rack-platform/PRODUCT.md` §2.
Full map with cross-product open decisions: `products/PRODUCT_INDEX.md`.

---

## 3. Headline engineering figures

These are the current, post-correction values. They supersede any earlier
figure found in `archive/`.

| Quantity | Value | Source |
|---|---|---|
| Installed envelope (W × D × H) | 1456 × 690 × 1960 mm | RK-A-SYS Rev 2 |
| Structure-only envelope | 1256 × 563 × 1960 mm | RK-A-DWG Rev 2 |
| Phase-1 build envelope (no plenum) | 1456 × 648 × 1960 mm | RK-A-SYS Rev 2 |
| Dry mass | **112.66 kg** | Fusion `CEA_RACK_INTEGRATED_v2` v8 |
| Parts / occurrences | 45 / 177 | Fusion v8 |
| Unresolved interferences | **0** | Fusion v8 interference check |
| Tiers × bed heights | 4 × 300 / 700 / 1100 / 1500 mm | EDR-001 |
| Rack cost, Grow Phase 1 | ₹49,296 | RK-A-MFG Rev 2 |
| Room total, 11 racks | ₹13.2 lakh (ex-LED fixtures) | RK-A-ROOM Rev 4 |
| Water recovery ratio | 87.7 % | RK-A-WRS Rev 3 |
| Annual discharge saved vs drain-to-waste | 554 m³ | RK-A-WRS Rev 3 |

---

## 4. First release issued

**`RK-A R1`** — prototype fabrication, from Fusion `CEA_RACK_INTEGRATED_v2` **v8**
(Rev 5). Exported 2026-09-05, **verified 2026-09-09**.

45 of 45 part STEP files present, plus assembly STEP and F3D. None missing, none
extra, none zero-byte, all valid ISO-10303-21. Envelope, mass, part count and
occurrence count all reconcile against the live Fusion model.

Release store: `E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\INTEGRATED_v2_Rev5\`
Manifest with per-file SHA-256:
`products/cea/racks/rack-platform/release/RK-A-R1_MANIFEST.md`

**RB-01 is closed.** The earlier finding that the export had silently failed was
wrong: the files were written to a synced Google Drive path rather than the Desktop
path the documents cite. What remains true is that two issued documents cite a path
that holds nothing (recorded as errata), and that the export script still does not
check `ExportManager.execute()`.

Two constraints on how R1 may be used:

- **Do not issue part drawings with it** — ND-01 is unresolved.
- **Regenerate the DXF flat patterns from v8 before cutting any sheet-metal part.**
  The existing `DXF/` set came from the platform design and covers 5 parts.

---

## 5. Open items, repository-wide

| ID | Type | Item |
|---|---|---|
| ~~NT-01~~ | **CLOSED 2026-09-09** | Parameter master persisted as `RK-A-PARAM` Rev 1 — 55 parameters read directly from `CEA_RACK_INTEGRATED_v2` v8 |
| NT-02 | NEEDS TRACEABILITY | **Depth-plane bracing was never checked by frame analysis** (RK-A-MFG Rev 2, stated plainly). The tip-over figures assume it holds. Closes at prototype acceptance test T16, not by analysis |
| ND-01 | NEEDS DECISION | `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` holds Rev 2 content while the published artifact of the same ID holds Rev 1. Which is the intended part-drawing release must be decided before drawings are reissued |
| ND-02 | NEEDS DECISION | Two published "Rack A Manufacturing Pack" artifacts exist. `9f5e09e5` is Rev 2 and current; `817abd35` is an orphan and should be retired or deliberately kept |
| ND-03 | NEEDS DECISION | Ventilation plenum is deferred to a Phase-2 entity. Phase 1 ships standalone EC fans. The plenum's interface to the rack is not yet frozen |
| ND-05 | NEEDS DECISION | Canopy velocity CV action threshold — RK-A-SYS §01 says 15 %, RK-A-ROOM §04 says 20 %. Plausibly a two-step escalation ladder; not reconciled |
| ND-06 | NEEDS DECISION | Room electrical phase imbalance ~20 % against a 15 % target; resolved on paper by specifying 3-phase HVAC, recorded as an open finding |
| ND-07 | **UNKNOWN — low priority** | Terrace slab loading 5.5 kN/m² concentrated against a typical 1.5–2.0 kN/m² rating. **Owner decision 2026-09-09: not a blocker** — the tank will be mounted on a steel structure rather than bearing directly on the slab. Kept open as unknown: the steel structure's own design and its bearing points are not yet specified |

ND-05 to ND-07 were raised by the CEA suite audit. Full detail is in
`products/cea/racks/rack-platform/CURRENT_STATE.md`,
`docs/system/MIGRATION_REPORT.md` and `docs/system/CEA_SUITE_AUDIT.md`.

---

## 6. Recommended next engineering action

**Build the prototype and run acceptance test T16.**

The release is issued and the parameter master is persisted, so the paper work no
longer blocks anything. The remaining open engineering question that cannot be
closed on paper is the depth-plane bracing (NT-02): the frame was never checked by
analysis, and the tip-over figures assume it holds. T16 — 300 N horizontal at the
top bed, residual deflection ≤ 5 mm — closes it, with a costed fallback (restore the
cross beams, ₹562) if it fails.

Before cutting metal: regenerate the DXF flat patterns from v8, and put ND-01 (the
part-drawings divergence) to a decision.
