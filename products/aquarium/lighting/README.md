# Aquarium Lighting

Two products on one intended shared platform (ADR-007). Both are **Phase 0A
research complete, 0B decisions pending**; neither has engineering or CAD.

| Product | ID | Positioning | Document |
|---|---|---|---|
| Core smart aquascaping light | `AQ-LT-A` | Affordable, fixed engineered spectrum, one logical channel, scheduling, standalone | `core-smart-light/PRODUCT.md` |
| Premium programmable WRGB aquascaping light | `AQ-LT-B` | High-tech tanks, independent spectral channels, higher output, small pilot | `wrgb-light/PRODUCT.md` |

| Shared | Document |
|---|---|
| Platform strategy: sharing map, cost-of-commonality method, delayed differentiation, size classes, power platform, control boundary, serviceability, industrial-design brief, open decisions | `PLATFORM.md` |
| Product-specific sourcing implications | `core-smart-light/sourcing/SOURCING_STRATEGY.md`, `wrgb-light/sourcing/SOURCING_STRATEGY.md` |
| Shared lighting knowledge, LED engines, power platform research, biology | `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` |
| Competitor architectures, Indian prices, warranty norms | `docs/references/lighting/COMPETITOR_LIGHTING_REFERENCE.md` |
| Supplier landscape (Coimbatore, India, import) | `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md` |
| Phases, gates, test categories, warranty evidence | `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md` |

## Read this first

- The platform is an **intent** recorded in ADR-007, not a design. Which elements are actually shared is decided per element by the cost test in `PLATFORM.md` §4, after RFQs.
- The retail, MOQ and manufacturing ₹ figures in these documents are **owner planning assumptions**, not approved COGS.
- Industry reference points in the product documents are not Trophic decisions; no drawing may cite them.
- Fusion 360 does not start until the 0B decisions in `PLATFORM.md` §11 exist.

## History

Until 2026-09-11 this folder held a single `PRODUCT.md` describing one programmable
per-channel aquarium light. That file was moved with `git mv` to
`core-smart-light/PRODUCT.md` and rewritten for the Core scope; its per-channel
intent now lives in `wrgb-light/PRODUCT.md`. Its industry reference points and its
seven open decisions were carried forward, not discarded.
