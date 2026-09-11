# ADR-007 — Aquarium lighting: Core and WRGB products on one intended shared platform with late differentiation

| | |
|---|---|
| **Status** | ACCEPTED — recorded 2026-09-11 from owner product intent stated for the lighting Phase 0 task. The owner should confirm this record on next review; it commits to the *intent* below and to nothing in §4 |
| **Affects** | `AQ-LT-A`, `AQ-LT-B`, `products/aquarium/lighting/**`, `platform/IDENTIFIER_STANDARD.md`, `products/PRODUCT_INDEX.md` |
| **Related** | ADR-004 (hardware/software boundary), cross-product decisions X1, X4, X5 in `products/PRODUCT_INDEX.md`. **Refined by ADR-008 (PROPOSED 2026-09-11):** if accepted, the "MCU/control board" element in §3 becomes an engine board per variant plus one shared Smart Module; nothing else in this record changes |

## Context

Until 2026-09-11 the repository held one aquarium light, `AQ-LT-A`, described as a programmable per-channel light with everything open. The owner's product strategy now has two aquarium lights at different price points and volumes: an affordable **Core** light (fixed engineered spectrum, one logical intensity channel, scheduling, standalone, planning MOQ ~200) and a premium **WRGB** light (independent spectral channels, higher output, pilot of 10–20 units). The owner's indicative 100-unit manufacturing figures for the WRGB (~₹10k/14k/19k for ~30/45/60 cm) are the reason a stand-alone WRGB tooling programme is not attractive, and the reason the two products should share what is economically shareable.

Research on 2026-09-11 (`docs/references/lighting/COMPETITOR_LIGHTING_REFERENCE.md` §3) found that every established brand tiers inside one housing by LED population and controller grade, so the strategy has industry precedent; it has no Trophic cost evidence yet.

## Decision

1. Trophic aquarium lighting consists of **two products**: `AQ-LT-A` (Core smart aquascaping light) and `AQ-LT-B` (premium programmable WRGB aquascaping light). The existing `AQ-LT-A` identifier is re-scoped to the Core product; `AQ-LT-B` is added to the identifier standard. This is consistent with the standard's rule that variant letters advance for a materially different product on the same platform.
2. The two products are developed around an **intended shared aquarium lighting platform** with **delayed differentiation**: common elements are manufactured and stocked at pooled volume as an undifferentiated housing kit per length class, and the products diverge at a late decoupling point where the LED board, driver stage, controller configuration, PSU rating, firmware exposure and labelling are committed.
3. The **default sharing direction** is: share the industrial-design language, mounting and suspension interface, fasteners, sealing approach, cable exit, DC connector, communications protocol, firmware base and app/backend device model by default; share the extrusion/chassis, end caps, optical cover, bus voltage, PSU family and MCU board **only if the cost-of-commonality test** in `products/aquarium/lighting/PLATFORM.md` §4 passes; never share the LED MCPCB, LED population, spectral architecture, channel count, current-driver stage, maximum thermal load, PSU rating or firmware-exposed spectral control.
4. Both products are **standalone-first**: the light executes its own schedule from local persistence; app, aquarium controller and any cloud are optional writers of the schedule, never required for operation, and there is no continuous cloud dependency.
5. Both products use the power topology **230 V AC → external certified AC/DC adapter → ELV DC bus → fixture → internal constant-current LED driver(s)**, so that mains-voltage development and certification risk is kept out of the fixture in early generations. The bus voltage, adapter family and adapter sourcing route are not decided by this record.
6. The Core light exposes **one logical intensity channel** to the user even where its engine contains several LED types. This is owner intent for the product's positioning; whether the engine is white-only or a white-plus-red mix is an engineering decision that follows validation.

## What this record does not decide (§4)

Bus voltage (24/36/48 V) · PSU family, rating or supplier · whether the extrusion, end caps, cover and MCU board are in fact shared (the cost test decides) · size classes and whether Core and WRGB use identical length classes · WRGB channel count · LED classes, spectra, currents, wattage, dimensions, materials, IP ratings · controller placement (inline vs in-fixture) · serviceability boundaries · warranty · whether anything is shared with `LT-A` (cross-product decision X1 stays open) · the app-to-light protocol and its ownership · the relationship to `AQ-CT-A` (X4 stays open).

Each of these is tracked in `products/aquarium/lighting/PLATFORM.md` §8 and will get its own record (ADR, EDR or ICR as appropriate) when actually decided. None may be inferred from this record.

## Consequences

- `products/aquarium/lighting/` now holds a family index, a platform document and two product folders with sourcing strategies. The prior single `PRODUCT.md` was migrated with `git mv` to the Core folder and rewritten; its content survives in the Core document's §4 reference points and §5 open items.
- Serialisation and traceability must be designed for one serial family with a variant field assigned at the decoupling point; the LED/driver board should physically carry the hardware identity so a Core unit cannot become a WRGB by software alone.
- One firmware image resolved by hardware identity at boot is the intended model; the app device model treats channel count as a property, not a type. This is the first real test of the CEA suite's claim that a tank light needs "no new platform work" (capability classes `light.dim` and `light.schedule`); whether the software side's capability class supports a channel array must be raised with the software repository now.
- A shared chassis carries a risk in both directions: Core may carry WRGB thermal capacity it does not need, or WRGB output may be capped by a profile chosen for Core. The cost test exists to make that trade explicit before a die is cut.
- Nothing in this record permits CAD. Fusion 360 work on either product waits for the 0B decisions in the platform document.

## Revisit triggers

Cost-test result showing the shared chassis penalises Core by more than the avoided WRGB tooling; WRGB demand evidence after the pilot; a decision on X1 that would make `LT-A` a third platform member.
