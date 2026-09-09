# Identifier Standard

## 1. Product IDs

Format: `<CODE>-<VARIANT>` — a two-letter product code and a variant letter.
Aquarium products carry an `AQ-` family prefix because their codes would otherwise
collide with CEA.

### CEA

| ID | Product | Family |
|---|---|---|
| `RK-A` | CEA Rack Platform (Rack A) | Racks |
| `LT-A` | LED grow bar | Lighting |
| `WR-A` | Closed-loop water recovery | Irrigation |
| `EV-A` | Ducted ventilation plenum | Environmental control |
| `CT-A` | Rack controller | Sensors and controllers |
| `CT-B` | Room controller | Sensors and controllers |

### Aquarium / aquascaping

| ID | Product |
|---|---|
| `AQ-LT-A` | Programmable aquarium light |
| `AQ-CT-A` | Aquarium sensor / controller |
| `AQ-LP-A` | Lily pipes |
| `AQ-FL-A` | Filtration |
| `AQ-PU-A` | Pumps |
| `AQ-CO-A` | CO₂ equipment |
| `AQ-TL-A` | Tools and accessories |

Variant letters advance for a materially different product on the same platform
(`RK-B` would be a different rack, not a revision of Rack A). Revisions are `Rev n`
and never change the ID.

## 2. Legacy IDs — retained deliberately

Two documents carry a `RK-A-` prefix but do not belong to the rack product:

| Document ID | Actually belongs to | Product ID |
|---|---|---|
| `RK-A-WRS` | Shared CEA infrastructure | `WR-A` |
| `RK-A-ROOM` | Facility reference, Ooty room | *(facility, not a product)* |

**These document IDs are not being renamed.** They are cited by issued documents and
by the CEA orchestrator suite, and renaming them would break references to gain
tidiness. The product IDs above are the correct handle for new work; the document IDs
remain what they are. Recorded so the mismatch is understood rather than "fixed".

## 3. Part numbers

`<PRODUCT-ID>-<NNN>` — e.g. `RK-A-104`.

| Range | Meaning on `RK-A` |
|---|---|
| 100–199 | Frame and structure |
| 200–299 | Deck |
| 300–399 | Lighting interface |
| 400–499 | Trays and wet parts |
| 500–599 | Panels and accessories |

The banding is per product. A new product defines its own bands in its `PRODUCT.md`
rather than inheriting the rack's.

## 4. Document series

`<PRODUCT-ID>-<SERIES>` — e.g. `RK-A-SYS`.

| Series | Document |
|---|---|
| `BRIEF` | Phase 0 product brief |
| `SYS` | Systems specification |
| `DWG` | Drawings |
| `MFG` | Manufacturing pack |
| `QC` | Verification / validation record |
| `PARAM` | CAD parameter master |
| `R<n>` | Engineering release manifest |

File naming: `<DOC-ID>_<Rev>_<slug>.<ext>`.

## 5. Instrument tags

ISA-style, shared across products so hardware and software name the same device the
same way. The current set is published in `trophic-contracts`
`sensors/instrument-tags.md`. Patterns: `TE` temperature element, `AT` analyser,
`LT`/`LS`/`LSH` level, `LD` leak detector, `PDI` differential pressure, `UV`/`UIT`
UV unit and intensity, `FS` flow switch, `P` pump, `DOS` dosing, `MV` master valve,
`FV` flow/diverter valve, `TK` tank.

## 6. Decision records

`ADR-###` architecture · `EDR-###` engineering · `ICR-###` interface change.
Numbered repository-wide, not per product, so a decision affecting two families has
one number.
