# Aquarium Lighting Platform — `AQ-LT-A` Core and `AQ-LT-B` WRGB

| | |
|---|---|
| **Scope** | The intended shared platform under two products. Not a product, not a design |
| **Stage** | **Phase 0A — research complete 2026-09-11; 0B decisions pending** |
| **Governing records** | ADR-007 (two products on one intended shared platform with late differentiation, ACCEPTED); **ADR-008 (Light Engine + signal-only port + optional Smart Module, PROPOSED 2026-09-11, owner to confirm)** |
| **Authoritative CAD** | None. No CAD may start until the 0B decisions in §8 exist |
| **Reference material** | `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` (Parts B2–B4, C, D2), `docs/references/lighting/COMPETITOR_LIGHTING_REFERENCE.md`, `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`; **common lighting area `platform/lighting/README.md`** (control interface concept, cost model, launch plan) |

This document holds what the two aquarium lights are intended to share, how a later
session decides whether each element is actually shared, the proposed
manufacturing model, the size-class question, the control boundary, the
serviceability proposal, the industrial-design brief, and the open decisions.
Product-specific intent is in each product's `PRODUCT.md`. **Everything below that
is not marked as decided in ADR-007 is a proposal.**

---

## 1. The two products, briefly

| | `AQ-LT-A` Core | `AQ-LT-B` WRGB |
|---|---|---|
| Positioning | Affordable, well-engineered, software-enabled planted-tank light. "Thoughtfully engineered, every detail considered", not luxury | Serious high-tech aquascaping; premium optical and electronic capability |
| Spectrum | Fixed engineered spectrum; several LED types allowed; **one logical intensity channel** | Independent spectral channels (3, 4 or 5 under investigation) |
| Control | Dimming, schedule, sunrise/sunset, acclimation; local persistence; standalone; no cloud dependency | Same foundation plus per-channel control |
| Retail envelope (assumption) | ~₹2,500–3,500 | Not set; owner's 100-unit manufacturing figures ~₹10k / 14k / 19k by size are planning inputs, not COGS |
| Volume planning | ~200 MOQ | 10–20 pilot units, common parts made at Core volume |
| Sizes (hypothesis) | ~30 and 40/45 cm | ~30 / 45 / 60 cm |

## 1a. Control architecture — ADR-008 (PROPOSED)

The owner's modular proposal was evaluated on 2026-09-11 and is recommended with
modifications. If accepted it changes the platform in these ways; until accepted
the integrated alternative in ADR-008 §4.1 remains live.

```
COMMON MECHANICAL / PLATFORM COMPONENTS (housing kit per length, caps, seals, mount, DC-in, port)
                  │
        ┌─────────┴─────────┐
   CORE LIGHT ENGINE    WRGB LIGHT ENGINE      ← LED board + CC drivers + engine MCU + thermal
   (1 ch, fixed)        (4–5 ch)                 backstop + hardware ID + default profile
        └─────────┬─────────┘
          COMMON CONTROL PORT (5 V · GND · TX · RX, signal only; never LED power)
                  │
          OPTIONAL SMART MODULE (radio, RTC, schedules, app, OTA)  ← one SKU, pooled
```

- Tiers from the same engines: **Core Basic** (engine + blanking cap), **Core Smart** (engine + module), **WRGB Smart** (engine + module), **Smart Module** upgrade/replacement, optional dimmer puck. Whether **WRGB Standalone** is a sold SKU is doubted (the WRGB buyer expects control) and is open.
- The engine MCU is mandatory; the engine is a complete safe light alone; the module is never in the power path; the engines carry no radio (WPC ETA and radio EMC attach to the module only).
- Concept interface, fail-safe state machine, protocol sketch and open items: `platform/lighting/electronics/LIGHT_ENGINE_CONTROL_INTERFACE.md`.
- The sharing map in §3 and the manufacturing model in §5 are annotated below for the ADR-008 case.

## 2. What the market does (context, not requirement)

Every established brand tiers inside one housing: Twinstar B/E/S, Chihiros Slim/II/Pro, Week Aqua Standard/Pro share extrusion and length classes and differ by LED population, RGB:white ratio and controller grade; LED count scales linearly with length on one pitch; brands standardise on 2–3 DC rails sold as spares; the adapter and the inline controller are where the products fail. Details and sources: `COMPETITOR_LIGHTING_REFERENCE.md` §3 and §5.

## 3. Sharing map by element

Classification from the Systems Architect analysis of 2026-09-11. "Share by default" is the ADR-007 direction; "cost test" means §4 decides; "do not share" is where the differentiation lives.

| Element | Feasibility | What forces it apart | Failure mode if shared wrongly | Class |
|---|---|---|---|---|
| Industrial-design language | High | WRGB needs a legible premium cue | WRGB reads "same as the cheap one" | **Share by default** |
| Extrusion / chassis | Medium | WRGB thermal load and MCPCB width | Core carries metal it does not need; or WRGB output capped by a Core-sized profile | **Cost test** |
| End caps | High (length-agnostic) | Cable-exit count | Low if the connector is shared | Share by default if chassis shared |
| Sealing / gaskets | High | None if chassis shared | Gasket section tied to the extrusion die | Share by default (follows chassis) |
| Cable exit | High | Conductor count; with internal drivers the exit is DC + nothing else either way | Low | Share by default |
| Mounting / suspension interface | High | WRGB mass | Bracket rated for Core fails on WRGB | Share by default, rate for WRGB mass |
| Fasteners | High | — | — | Share by default |
| Service architecture | Medium | Core cost may not justify field service (§7) | Core pays for connectors it never uses | Share the concept; allow Core to be a "no-service" configuration |
| Optical cover / diffuser | Medium | WRGB colour mixing may want a diffuser Core does not | Shared cover compromises one product | Cost test |
| Packaging | High (system), medium (carton) | Length classes | Low | Share the system; carton per length |
| DC connector | High | — | **High if voltage is not also shared**: same plug, different volts destroys a fixture | Share by default, **conditional on a shared bus voltage** |
| Bus voltage | High | WRGB power may push voltage up | Diverging voltages force keyed connectors and two PSU families | Cost test; decide once, for the WRGB power case |
| PSU family | High (family), low (rating) | Wattage | Under-powered fixture if the wrong rating ships | Share the family; **rating per product** |
| Engine board (MCU + drivers) — *per ADR-008 replaces the shared "MCU/control board"* | Per variant | Channel count → driver channels and PWM outputs | — | **Do not share the board; share the MCU class, firmware base, protection design and port** |
| **Smart Module** (ADR-008) | High | — | Two module variants = two ETAs, two app paths | **Share by default: one module for every engine, length and tier** |
| Communications protocols (ADR-008: engine port protocol, ICR-governed here; app-to-module protocol in `trophic-contracts`) | High | — | Two *app* protocols = two apps = two support lines | **Share by default** (one port protocol, one app protocol) |
| Firmware base | High | Feature exposure | Hard-coded channel count breaks one variant | Share by default; variant by hardware ID |
| App / backend device model | High | Channel count is a property, not a type | Model that assumes 1 or 4 channels | Share by default |
| LED MCPCB, LED population, spectral architecture, channel count, driver stage, PSU rating, firmware-exposed spectral control | — | This *is* the differentiation | — | **Do not share** |

## 4. Cost-of-commonality decision method

No universal threshold is set; the evidence does not support one. Later sessions compare **Separate** (Core-optimised chassis X, WRGB chassis Y) against **Shared** (X + Δ for both) over a planning horizon with expected volumes N_core and N_wrgb.

```
C_separate = NRE_X + NRE_Y + N_core·c_X(N_core) + N_wrgb·c_Y(N_wrgb) + Inv₂ + Sp₂ + Asm₂ + Svc₂
C_shared   = NRE_(X+Δ) + (N_core + N_wrgb)·c_(X+Δ)(N_core + N_wrgb) + Inv₁ + Sp₁ + Asm₁ + Svc₁
```

where c(·) is unit cost *as a function of pooled volume* (this is where extrusion-die MOQ in kg, end-cap mould shots and anodising batch minimums enter), Inv is inventory carrying cost, Sp spare-part SKU cost, Asm assembly jig and work-instruction cost, Svc warranty and service cost.

**Breakeven in Core units:**

```
N*_core = [ NRE_Y − (NRE_(X+Δ) − NRE_X) + ΔInv + ΔSp + ΔAsm + ΔSvc + MOQ_penalty_avoided ] / [ c_(X+Δ) − c_X ]
```

Shared wins if expected lifetime N_core is below N*_core. If the denominator is ≈ 0 (Δ costs nothing per unit), sharing always wins; if the numerator is ≈ 0 (WRGB would never get its own chassis anyway), the real question is whether WRGB exists as a chassis at all.

Include explicitly: **Δ mass** (freight, bracket rating, perceived value, expressed as ₹/unit and as a mounting-load check); the **WRGB pilot term** (at 10–20 units WRGB cannot amortise any tooling, so under Separate either 10–20 units pay NRE_Y or WRGB is hand-built; this real-option value of sharing is recorded as a scenario, not a number); a **risk term** P(WRGB never scales) (if high, sharing is cheap insurance; if low, Core over-spec is a permanent tax).

**What drives Δ** (manufacturing view): wall thickness and fin area for the WRGB heat load; width for more LED rows or a wider MCPCB; an internal cavity for the controller board; more end-machining. These add mass per metre and die complexity, rarely a second process. Illustrative only: if the WRGB-capable profile is +0.2 kg/unit at ~₹350/kg, Core carries ≈ ₹70/unit, ≈ ₹14k across 200 units, against a second die (≥ ₹30k listing class) plus a second 500–1,000 kg MOQ carry that is mostly dead stock at 20 units. The numbers that decide it are the profile mass per metre (needs a section concept), the extruder's real MOQ, and die quotes: all **RFQ required**.

**Inputs later phases must gather:** extrusion die cost and MOQ (kg or m) from two or three extruders; end-cap mould cost and shot MOQ; anodise batch minimum; per-metre extrusion price at two volume tiers; Δ cross-section area; carrying-cost rate; SKU count each way; jig and work-instruction count; expected N_core and N_wrgb; warranty return-rate assumption. Repeat the same structure for the MCU board and the PSU family with their own Δ.

## 5. Delayed-differentiation manufacturing model (proposal)

```
common aquarium mechanical platform
        ↓
extrusion (one die per width class) → cut-to-length → CNC end machining
(cable-exit hole, mounting bosses, gasket groove) → deburr → anodise
        ↓
+ end caps + gasket + mounting hardware + cable gland/strain relief
+ plain carton blank  →  HOUSING KIT per length class (stocked, no shelf life)
        ↓                    DECOUPLING POINT 1 (hardware)  — ADR-008: no shared control board step
   LED MCPCB + engine board (MCU + CC drivers, per variant) married to housing;
   thermal interface, cover, final seal; DC-in and control port in the end cap
       ↙                                   ↘
AQ-LT-A Core engine                   AQ-LT-B WRGB engine
       ↓                                   ↓
                DECOUPLING POINT 2 (configuration)
   engine EEPROM holds variant / hardware ID / defaults; firmware exposes channel count
   + PSU rating + rating label + printed sleeve/insert + manual + fixture serial
                ↓
                DECOUPLING POINT 3 (kitting) — ADR-008
   + Smart Module (own serial, built and tested outside the housing flow) for Smart tiers,
   or blanking cap for Core Basic
```

| Aspect | Implication |
|---|---|
| Inventory | Housing kits and control boards held by length only; MCPCB/driver held by variant. WRGB pilot draws from pooled housing stock. Housing kits absorb the extrusion MOQ overrun; LEDs and PCBAs are MSL-bearing and stored dry-packed |
| MOQ | Housing, caps, gaskets, connectors, mounting and cartons pooled. **Sharing does nothing for LEDs, driver ICs, MCPCB artwork or PSU rating.** WRGB LED boards at 20 units sit below Indian PCB MOQ (~100): panelise or order from China |
| QC stages | Incoming extrusion (length, straightness, key dimensions, anodise thickness and colour against a retained reference); incoming PCBA (EMS functional test plus Trophic sample re-test); housing kit (visual, gasket seat, threads); final (power-on, channel check, sample photometric and colour check, sample seal check, label and serial) |
| Serialisation | **One serial family with a variant field**, assigned at decoupling point 1. NEEDS DECISION |
| Traceability | Serial physically on the housing label (survives a board swap) and electronically on the control board; housing kit carries extrusion lot + anodise batch; MCPCB carries its fab lot; the build record links them. A field-replaced control board must have its electronic serial re-written: a service process requirement |
| Hardware identity | The **engine board carries the hardware ID in EEPROM** (and the MCPCB a resistor strap if sourced separately) so a Core cannot be unlocked to WRGB by software alone; a module swap re-reads the correct identity at handshake |
| Module traceability (ADR-008) | The module has its own serial family (identifier NEEDS DECISION); the kitting record links the pairing but **the pairing is not permanent**, so traceability never assumes a fixed fixture–module bond |
| Firmware | **One image, hardware-ID-resolved at boot.** Two images invites shipping the wrong one. The app model reads channel count from the device |
| Assembly | One common branch and one jig set, then two work-instruction branches; WRGB adds harnesses and connectors only |

Risks: the shared chassis carries WRGB thermal capacity Core does not need (mass, cost, size against ₹2,500–3,500 competitors); the shared MCU is over-specified for Core; the *WRGB* output ceiling is set by a profile chosen with Core in mind; a single extrusion die is a single point of failure (two extruders can share one Trophic-owned die, confirm ownership in the RFQ); software-only hardware ID invites grey-market "unlocks". **Delayed differentiation only works if the WRGB thermal and width envelope is designed into the common extrusion, which is why the cost test precedes the die.**

## 6. Size-class strategy — OWNER DECISION REQUIRED

What a length class actually costs is not extrusion tooling (cut-to-length is free) but one MCPCB layout per variant, one cover cut, one carton, one SKU per variant, one photometric qualification, one spare-housing SKU and one incoming-QC reference length. The real coupling is between length classes and the **PCB modulus**: a ~15 cm repeated module tiles 2/3/4 → 30/45/60 and 40 does not fit; a ~20 cm module tiles 2/3 → 40/60 and 30/45 do not; one panel per length allows any set at the cost of a full layout per length per variant. At 200 units, one board per length is usually simpler than tiling (tiling adds board-to-board joints and optical gaps); JLCPCB accepts aluminium boards to 602 × 506 mm, Indian fab limits RFQ required.

| Option | Pros | Cons |
|---|---|---|
| **A: common 30/45/60 for both** | Maximum pooling; one modulus; simple story; three housing SKUs total | Core 60 may exceed the price point; 40 cm cubes served by a 45 with adjustable brackets |
| **B: Core 30/40 + WRGB 30/45/60** | Core tuned to the nano segment | Breaks the modulus; 40 and 45 housing kits are separate SKUs 5 cm apart; pooling lost on the length Core sells most; four lengths total across both products is materially costlier to run than three |
| **C: Core 30/45, WRGB 45/60** | Overlap on 45 = pooled volume where WRGB most likely sells | Core has no 60; WRGB no 30 |

Indian tank references (market, not Trophic data): 30 × 18 × 18 cm nano, 36 × 22 × 26, 40 cm cubes, 45 × 27 × 30, 60 × 30 × 36 ("60P"-type), and 2 ft / 3 ft rimmed tanks common in India.

**Decision framework:** (1) obtain sell-through by tank length in the target segment from Indian retailers, the missing evidence; (2) set bracket adjustability per class (a "45" spanning ~36–48 cm tanks is explainable to customers; a fixture shorter than the tank is not); (3) choose the PCB modulus that covers the chosen classes; (4) only then fix lengths. The Systems Architect's lean is identical classes for both (A or C), because the 40-vs-45 split in B is where inventory pooling quietly dies; the Core 30/40 hypothesis should be tested against bracket range on a 45 class before being kept. Mounting arms that fix to the end caps are length-independent, so a common end cap gives one arm SKU across all lengths.

## 7. Power platform (summary; research in `LIGHTING_PLATFORM_REFERENCE.md` Part C)

Topology per ADR-007: external certified adapter → ELV DC bus → internal CC drivers. Findings that shape the 0B decision, none of them a decision:

- The bus voltage is derived **LED topology → driver topology → system power → supply**, never copied from a competitor. A small Core fixture fits one buck string on any bus; a 60 cm WRGB white channel needs two strings at 24 V but one at 48 V. Driver-stage count, not efficiency or cable loss (≤ 2 % in every case), is the main 24 V penalty.
- **36 V is the weakest option on adapter availability**: the mainstream BIS-marked desktop families (Mean Well GST60A/90A) skip it; only the IP67 OWA family (no BIS mark on its datasheet) and niche lines offer it.
- 48 V halves cable current and driver count on the larger fixture but needs 80 V-class input parts, exceeds the 24 V rating of most barrel jacks, and drives twice the leakage and corrosion current across a condensation or salt film. 24 V has the deeper Indian OEM pool and cheaper parts.
- **Gen-1 leaning (not decided):** buy an established certified adapter as-is, with private-labelling a certified platform as the volume follow-on; Indian OEM custom only after a factory audit; custom or in-house design not justified at low tens of watts. The decisive unknown is the **BIS category scope** (IT adaptor under IS 13252 / 62368-1, LED control gear under IS 15885, or the fixture itself under IS 10322), which no source settles and which must be confirmed with BIS or a consultant.
- "One family, one voltage, one connector, multiple ratings" is realistic for voltage and safety family, **not automatically for the connector** (the GST plug changes from 5.5×2.1 to 5.5×2.5 between 60 W and 90 W); a uniform custom plug is possible at MOQ.
- The fixture must protect itself in hardware (reverse polarity, overvoltage, under-voltage lockout, inrush, DC-side surge, ESD) and must fail safe with a wrong or undersized adapter without firmware, per the platform principle that software never commands a safe state.
- Sharing the PSU or connector with `LT-A` would be a false economy; sharing LED string designs, driver-IC layouts and dimming firmware is real but confined to the engine.

## 8. Control and software boundary (proposal)

- **Standalone-first.** Under ADR-008 the *module* executes the schedule from its RTC and persistence; the *engine* is a complete safe light without it (default profile with soft-start; thermal protection in hardware). App, `AQ-CT-A` and any cloud are writers and overriders, never required. Loss of the module → hold for a grace window then a bounded fallback (policy OWNER DECISION REQUIRED, interface concept §4); loss of power → resume on restore. Never "full on".
- **`AQ-CT-A` is an optional hub** (cross-product decision X4 stays open). The light exposes one device model regardless of whether the app or the controller talks to it; the controller is just another client. This prevents X4 being decided by accident inside the light.
- **Capability vocabulary:** map to the CEA suite's `light.dim` + `light.schedule` classes. WRGB needs per-channel dim; whether that capability class supports a channel array is a software-side question this repository must not answer. **Raise it with the software repository now**; it is the first real test of the "no new platform work" claim.
- **Publish to `trophic-contracts`:** device model (capabilities, channel count as a property, dim range, resolution and curve semantics), schedule semantics (time of day, ramps, sunrise/sunset, acclimation, RTC and timezone behaviour), fail states, and the transport and message schema once chosen, with versioning. When: device model and schedule semantics as a draft at Concept; transport and protocol at Design freeze, not before the BLE/Wi-Fi decision. **Never:** geometry, BOM, LED types, cost, thermal figures.
- **Protocol ownership.** Two protocols under ADR-008: the **engine port protocol** is a hardware interface owned here and changed by ICR (`platform/lighting/electronics/LIGHT_ENGINE_CONTROL_INTERFACE.md`); the **app-to-module protocol** lives in `trophic-contracts` with the module firmware as reference implementer. The published device model is one light with channel count as a property; the port protocol is not published unless `AQ-CT-A` is decided to speak it (X4). The CEA "wired-first" rationale does not apply to a living room.
- **Time and persistence** (reference Part B4): the schedule in flash is trivial; the clock is the problem. A backup-capable RTC with supercapacitor hold-up is the natural Core default given Indian grid outages; a coin cell is the long-hold alternative; phone or NTP re-sync is the cheapest with a "safe day" fallback. NEEDS DECISION.
- **Radio:** BLE alone satisfies a standalone light; Wi-Fi adds NTP, cloud/voice and OTA convenience with a larger support surface. An ESP32-C3-class part keeps Wi-Fi as a firmware option without a hardware change. NEEDS DECISION. WPC ETA applies to any 2.4 GHz product sold in India; whether an already-approved module suffices is RESEARCH REQUIRED.

## 9. Serviceability architecture (proposal)

| Module | Replaceable by | Condition |
|---|---|---|
| External PSU | User | Shared connector requires a shared voltage or keying |
| Mounting hardware | User | — |
| Smart Module (ADR-008) | **User** | Unplug and replace; no seal opened; module carries its own serial |
| Engine board (MCU + drivers) | Factory | Inside the sealed cavity with the LED board |
| LED MCPCB + driver board | Factory | Thermal interface, gasket, photometric re-test |
| Optical cover | Customer service (user if clip-in and unsealed) | Sealing-dependent |

Every field boundary is a connector plus a re-sealable joint in a condensing, salt-creep environment. Recommended: the LED/driver cavity factory-sealed, the serviceable boundary at the end cap (control board, cable) and outside (PSU). The goal stands: avoid replacing an expensive aluminium fixture for a small electronics failure. **For Core at ₹2,500–3,500 the economic case for any field service may not exist**; a sealed Core with a returns policy may be cheaper than connectors, which would make service architecture a *divergence* between Core and WRGB rather than a shared element. The Core warranty decision (§11 #15) decides it. Connectorising costs roughly ₹20–60 per unit in BOM (supplier landscape §4); the common middle path is an external adapter carrying its own warranty, connectorised LED and control boards, and conformal coating on the control board only.

## 10. Industrial-design brief (Phase 0, direction only, no geometry)

From the Industrial Design/CMF specialist, 2026-09-11. Every item that touches an engineering constraint is flagged; none is a constraint yet.

**Family language.** One section, two levels of execution: Core and WRGB share the profile silhouette, end-cap grammar, cable-exit logic and mounting interface; the sibling relationship is carried by proportion rules, not a logo band. Premium is legible through what the hand and the close-up camera find: a tighter cap-to-body seam, a machined rather than moulded cap or a higher-grade polymer with matched texture, a second finish operation, a captive service fastener, a better cable. Function is the decoration: any visible feature does a job (fin, drip edge, strain relief, fastener, status window). Quiet above the tank, rewarding in the hand. Non-negotiable avoidances: polished chamfers, gloss black, gold/rose-gold/chrome, "floating" bezels, tapered jewellery profiles, oversized wordmarks, rainbow status lighting, and any silhouette a hobbyist would mistake for Chihiros, ONF, ADA, Twinstar or Week Aqua.

**CMF.** Type II anodise over a fine bead-blasted matte surface (hides die lines and fingerprints, photographs without directional flare; brushed shows every mineral streak). *Flag:* blast media and anodise thickness affect emissivity; thermal specialist confirms. Family colour: dark grey / graphite, not pure black (shows water spots, reads generic) and not natural silver (reads unfinished, yellows visually under warm white); Core and WRGB in the same colour, never colour as the tier signal. End caps are the biggest CMF risk: polymer-to-anodised-aluminium mismatch at a seam inspected daily. Preference for WRGB: machined and anodised aluminium in the same batch; for Core: matched-texture polymer with a *deliberate* tonal step so it reads as designed contrast, never a "perfect match" that fails within one anodise batch. *Flag:* cap material drives sealing, thermal path and cost. Optical cover matte or lightly textured on the outer face if optics permit; gloss shows every droplet and produces a specular hotspot in photos. *Flag:* diffusion changes output and beam; optics confirms. Ageing near water: wipeable surfaces, no underside corners that collect deposits, no bare aluminium cut edges, anodise seal quality as a sourcing quality gate.

**Cable.** Single exit, one end, in line with the body axis, dropping down the back corner of the tank; the strain relief is a designed part of the end cap. Matte dark braided or low-sheen TPE cable in body colour; WRGB may use braid as an execution signal. If an inline controller exists (Core), it sits at the adapter end, same colour and radius grammar; WRGB ideally has no puck. *Flag:* controller location affects cable, connector count and ingress. Specify a sober matte adapter; a glossy generic wall wart undermines the package.

**Mounting.** Legs on rimless glass as the default visual; legs that read thin but stiff, a shaped section rather than round rod, with a visible, intentional rotation or slide interface; the leg-to-body junction should look machined, not a screw in a slot. Glass pads in body colour, never clear sticky pads. Suspension hardware shares one visual grammar; clamp lowest priority. **Stability wins over lightness.** *Flag:* leg section, glass thickness range and fixture mass are mechanical decisions.

**Fasteners.** Honest, few, designed: a small number of exposed countersunk or socket-head stainless fasteners in a dark finish (black oxide or dark PVD, never bright zinc or chrome) at the end caps, positioned as a graphic element, one type across both products. Hidden snap-fits that creak are the wrong trade. *Flag:* stainless-on-aluminium galvanic contact near water needs materials confirmation. No fasteners on the underside or optical face.

**Graphics and status.** One small laser-marked wordmark on one end cap or the top face near an end; regulatory text on the underside or adapter; no model name on the top face. One small dim single-colour status LED with a purpose, aimed at the user, dimmable or off; no RGB status light, no breathing animations. *Flag:* whether a status LED exists is a control decision.

**Service access.** The end cap is the service door and says so: removable with the same fastener the customer already sees, revealing an ordered interior. This collides directly with ingress and condensation handling; if the cap must be sealed, the seal line should be a straight, designed gasket edge rather than a glue seam. Engineering decides.

**Packaging.** Kraft-tone corrugated or rigid board, one-colour matte print, no gloss lamination, no foam plastic, no window; presentation through arrangement (fixture, legs, cable, adapter each in a die-cut pulp or board cavity), cable coiled with a reusable strap in body colour; one card with wordmark, mounting steps and service-access note. A well-organised tool case, not a gift box. Same box family for both; WRGB in a heavier board grade.

**Photographability.** Clean horizontal from 45° down, straight-on at eye level, and top-down flat lay; no visible die lines, wavy cover or colour step at the seam. Light-off appearance: dark matte body; the LED array must not show as dots through the cover. Light-on: avoid leakage through cover edges and end caps and glossy side faces catching spill; the cover's outer face should not add a specular band. Underside and legs appear in the glass reflection and must be finished to the same standard.

**Engineering must confirm before any of this becomes a constraint:** fin exposure and emissivity; ingress class, condensation handling, gasket line and serviceable-cap feasibility; drip-edge geometry; cover material and texture; fastener corrosion class and galvanic pairing; bead-blast and anodise feasibility and cost at Coimbatore vendors; machined vs moulded caps at Core volume; braided cable and matte adapter availability; status LED, inline controller and any `LT-A` driver sharing.

Adjacent-category references (directions, not templates): Peak Design hardware (anodised dark grey, honest fasteners, serviceable machined interfaces); Teenage Engineering OP-1 / TX-6 bodies (function-driven detail, restrained laser marks); Leatherman and Knipex tools (matte finishes, exposed pivots as design, wear that looks intentional); Braun-era appliances (proportion and calm with visible function); Leica and Sigma fp bodies (bead-blasted anodise, tight seams, one small etched mark).

## 11. Open decisions

The sixteen decisions the program tracks, with recommended ownership and the evidence that closes each. Decision 6 is the only one made (ADR-007 §6).

| # | Decision | Owner | Evidence needed | Status |
|---|---|---|---|---|
| 1 | How much architecture Core and WRGB share | Owner (intent) / engineering (per element) | §4 cost test per element | Direction set by ADR-007; per-element **NEEDS DECISION** |
| 2 | Shared aluminium chassis without harming Core economics | Engineering, owner sign-off | Extrusion quotes, Δ section and mass, WRGB thermal budget | **NEEDS DECISION** after RFQ package A |
| 3 | One DC bus voltage for both | Lighting/Electronics | WRGB peak power per size, driver efficiency, adapter availability at ratings, connector current and voltage rating, BIS scope | **NEEDS DECISION** (0B) |
| 4 | One PSU family | Lighting/Electronics + Sourcing | Certified Indian-available families at the required ratings; BIS category confirmed | **NEEDS DECISION** (0B) |
| 5 | Shared MCU/controller board | Lighting/Electronics | Superseded by ADR-008 if accepted: engine board per variant, one shared Smart Module | **Re-framed by ADR-008 (PROPOSED)** |
| 6 | Core uses one logical channel despite mixed LEDs | Owner | — | **DECIDED**, ADR-007 §6 |
| 7 | WRGB channel count | Owner (positioning) + Lighting | 4 mandatory + 1 optional planning; bench SPD tests decide the 5th | **NEEDS DECISION** (0B) |
| 8 | Identical length classes for Core and WRGB | Owner | Tank sell-through data; bracket range | **OWNER DECISION REQUIRED** |
| 9 | 30/45/60 as the common mechanical system | Owner | Same, plus PCB modulus | **OWNER DECISION REQUIRED** |
| 10 | What stays shared with `LT-A` (X1) | Owner after engineering comparison | `LT-A` decisions 1 and 8; bus voltage; one-page driver-stage comparison | **NEEDS DECISION**; recommendation: share toolchain, supplier base and know-how, not platform hardware |
| 11 | Coimbatore parts | Manufacturing/Sourcing | Anodising samples, machining and moulding RFQs, EMS site visits | Landscape researched; **RFQ required** |
| 12 | Elsewhere-India parts | Manufacturing/Sourcing | Extruder, MCPCB fab, diffuser extrusion quotes | Landscape researched; **RFQ required** |
| 13 | Intentionally imported components | Manufacturing/Sourcing | Emitter, IC, module, connector availability and duty confirmation | Landscape researched (§0.4 of the supplier landscape) |
| 14 | Dual sourcing | Owner (risk appetite) | Single-die risk assessment; emitter footprint-compatible pairs | Map proposed (supplier landscape §5) |
| 15 | Core warranty | Owner | Roadmap §7 evidence table; service-cost model vs sealed-and-replace | **OWNER DECISION REQUIRED**, not before Gate C |
| 16 | Validation before WRGB exceeds pilot | QA gate, owner | Roadmap §6 | Framework written; evidence tier none |

Additional open items raised by research: serial family and variant field (§5); adapter identification pin (Part C3); UVA is **excluded unless evidence appears** (reference Parts B3 and D2), reopen only by decision.

**Open items carried by ADR-008 (PROPOSED):**

| # | Decision | Owner | Status |
|---|---|---|---|
| 17 | Accept ADR-008 (modular engine + port + module) over integrated control | Owner | **OWNER DECISION REQUIRED** |
| 18 | Message port (engine MCU on every engine) vs signal-wire MCU-less Core | Engineering, cost test | NEEDS DECISION |
| 19 | Module placement: tethered puck, recess-dock, or module-as-end-cap; visible-element conflict with the design brief | Industrial Design + engineering | NEEDS DECISION |
| 20 | Port link and connector class (4-pin UART; M8 / SP13 / USB-C carrier / dock) | Lighting/Electronics | NEEDS DECISION |
| 21 | Fallback on module loss (hold-then-default vs coasting schedule) and grace window; power-on photoperiod | Owner (behaviour), EDR (values) | **OWNER DECISION REQUIRED** |
| 22 | Smart Module product identifier and serial family | Owner, identifier standard | NEEDS DECISION |
| 23 | Whether WRGB Standalone is a sold SKU | Owner | OWNER DECISION REQUIRED |
| 24 | Whether the owner's Core COGS figure includes the module; Core Basic go/no-go for batch 1 | Owner | OWNER DECISION REQUIRED (cost model §8) |
| 25 | ETA reuse for a pre-approved radio module; BIS scope of a radio-free ELV luminaire | Regulatory research | RESEARCH REQUIRED |

## 12. Explicitly not decided

No dimensions, no extrusion section, no wall thickness, no LED type, count, pitch or current, no wattage, no lumen or PPFD figure, no channel count for WRGB, no bus voltage, no PSU rating, no connector part, no IP rating, no materials, no finish beyond the design direction in §10, no BOM, no cost. The owner's ₹ figures in §1 are planning assumptions requiring scope validation and are not COGS.
