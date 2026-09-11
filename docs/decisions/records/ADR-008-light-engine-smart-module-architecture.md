# ADR-008 — Aquarium lighting control architecture: Light Engine with a signal-only control port and an optional Smart Module

| | |
|---|---|
| **Status** | **PROPOSED** — evaluated and recommended 2026-09-11 (Systems Architect + Lighting/Electronics, synthesised by the main session) from an owner design suggestion. **Not accepted until the owner confirms.** Until then it constrains nothing, and the alternatives in §4 remain live |
| **Affects** | `AQ-LT-A`, `AQ-LT-B`, a new Smart Module product, `products/aquarium/lighting/PLATFORM.md`, `platform/lighting/**`, future standalone CEA lights. Not `LT-A` |
| **Refines** | ADR-007 §3 (the "MCU/control board" sharing element is replaced by "engine board per variant + shared Smart Module") and PLATFORM.md §5 (the "control board with bootloader only" step is removed; a kitting decoupling point is added). ADR-007 itself is unchanged |
| **Related** | Cross-product decisions X4 (`AQ-CT-A` as hub) and X6; PLATFORM.md §11 |

## Context

ADR-007 fixed the power topology (certified adapter → ELV DC → internal constant-current drivers) and the intent to share a platform under Core and WRGB with late differentiation, leaving the control architecture as a cost-test item. The owner then proposed making the control electronics detachable: a **Light Engine** holding the LED board, drivers, thermal protection, hardware identity and safe standalone behaviour behind a common control interface, plus an **optional Smart Module** holding radio, RTC, schedules, app communication, profiles and OTA, communicating commands rather than carrying LED power.

Facts that shaped the evaluation: competitors mostly place a Bluetooth controller inline in the DC cable switching LED power per channel, and that controller plus the adapter are the dominant field-failure items (`COMPETITOR_LIGHTING_REFERENCE.md` §3, §5); an aluminium extrusion body is hostile to a 2.4 GHz antenna, so an integrated radio dictates a polymer or windowed end cap on both products; any 2.4 GHz product sold in India needs WPC ETA; Core's own positioning requires dimming and scheduling; the cost model (`platform/lighting/costing/`) shows Core has no contribution at pilot volumes, so every rupee of Core electronics matters.

## Decision (proposed)

1. **Two-part architecture.** Each aquarium light is a **Light Engine** (fixture) plus an **optional Smart Module**. The engine contains the LED MCPCB, one constant-current driver stage per channel, input protection, a small engine MCU, a hardware thermal backstop independent of the MCU, hardware identity, a stored default profile with soft-start, and a **signal-only control port**. The module contains the radio, RTC with backup, schedule and ramp logic, the app protocol, profile storage and the OTA host.
2. **The engine MCU is mandatory, not "if justified".** A message-based port (rather than per-channel signal wires) requires a protocol endpoint, and it is what gives Core and WRGB one interface, hardware identity, stored defaults, thermal telemetry and engine OTA. The MCU-less Core with signal wires is recorded as the challenger the cost comparison must beat (§4.4).
3. **The module is never in the power path.** DC-in and the control port are two connectors of different families; the port carries a housekeeping 5 V rail and data only. Placement is a short tether or a recess-dock at the end cap; "inline on the DC cable" is rejected.
4. **The engine is a complete safe light without a module**: power-on ramps to the stored default profile; thermal derating is in the engine with a hardware backstop; on loss of the module the engine holds for a grace window and then falls back to a bounded state (policy per §5). Software never commands a safe state (platform electrical standards §4).
5. **One port and one protocol across both engines**, with capability discovery (channel count as a property), min-compatible versioning, and engine OTA through the module. The port protocol is an interface owned in this repository and changed by ICR; the app-to-module protocol goes to `trophic-contracts`.
6. **Tier ladder from the same engines:** Core Basic (engine + blanking cap, mains-timer users), Core Smart (engine + module), WRGB Smart (engine + module), Smart Module as an upgrade and replacement SKU, an optional dimmer puck on the same port. Every Core engine carries the port.
7. **The engines are radio-free products.** WPC ETA and radio EMC attach to the module only; one approval covers every fixture in the family.
8. **Reuse boundary.** The module and port are reusable by a future standalone CEA or home light with internal drivers, and by other aquarium products only if the port protocol stays capability-based. They are **not** reused by `LT-A`, which is a passive bar under rack remote drivers with 0–10 V and Modbus; this reinforces PLATFORM.md §11 #10.

## Why this boundary (§3)

- It puts every safety-critical function where the platform principle demands it and moves everything that changes often (radio, app, schedule logic, regulatory radio scope) into a cheap, user-swappable part.
- The controller, the historically weakest item, becomes a warranty swap instead of a fixture return, and runs cool because it carries no LED power.
- It frees the WRGB end cap from hosting an antenna, which the design brief wanted in machined aluminium.
- The module becomes the highest-volume PCBA in the family, pooling the most expensive electronics (radio, RTC, supercapacitor) across every Core Smart, every WRGB, every length and every upgrade sale.
- Engine and module end-of-line tests each become simpler than one integrated test, and one jig serves both engines.
- The dimmer/knob tier stops being a separate architecture and becomes an accessory that may never need to be built.

## Alternatives considered and rejected (§4)

1. **Fully integrated smart control in every fixture.** Every Core carries radio, RTC and ETA; no Basic SKU is possible without a second board; a controller failure is a fixture return; the antenna forces a polymer or windowed cap on both products; the module's pooled volume is lost. Retained as the fallback if the cost test shows the modular premium (connector pair, second enclosure, second PCBA, second EOL, kitting) exceeds the Basic-SKU and service benefit.
2. **Inline controller in the DC cable with power pass-through** (competitor pattern). Bus current through user connectors, extra ingress points in the loom, the module runs hot, replicates the dominant field-failure item, and violates the owner's own principle. Rejected outright.
3. **Separate mid-tier knob/dimmer architecture.** Subsumed: a dimmer puck on the same port.
4. **MCU-less Core engine with a signal-wire port** (PWM/analogue lines, ID strap). The cheapest Core by perhaps ₹100–200, but it splits the interface into two pinouts (WRGB needs 4–5 lines), forfeits identity, stored defaults, thermal telemetry and OTA, and prevents the tier ladder. Recorded as the challenger; the cost test must show the message port earns its premium on Core.
5. **Module carrying per-channel LED power.** Rejected by owner principle.
6. **Module as the end cap itself** (board-to-board inside the seal line). More elegant, but the user must open the seal line to swap it in a condensing environment. Kept open as a placement option against the tethered puck; Industrial Design and engineering to resolve.

## Open questions (not decided by this record, §5)

Message port vs signal-wire port confirmed by the cost test · tethered puck vs recess-dock vs module-as-end-cap, and the visible-element conflict with the design brief ("WRGB ideally has no puck") · connector class and link class (4-pin UART, 3-pin half-duplex, USB-C carrier) · fallback policy on module loss and its grace window (**OWNER DECISION REQUIRED**: hold-then-default vs coasting schedule) · power-on photoperiod for no-module, no-timer users · default-level writability · port rail budget · **module product identifier and serial family** (the identifier standard has no accessory concept; options are a variant letter such as `AQ-LT-C` or a new code such as `AQ-CM-A`; do not invent without a decision) · whether WRGB Standalone is a sold SKU (the Systems Architect doubts it: the WRGB buyer expects control) · whether `AQ-CT-A` speaks the port directly (X4) · whether the owner's Core COGS figure includes the module · ETA reuse for a pre-approved radio module and BIS scope for a radio-free ELV luminaire (RESEARCH REQUIRED).

## Consequences

- PLATFORM.md §3 gains a Smart Module row and loses the shared "MCU/control board" row; §5 gains decoupling point 3 (kitting), and the fixture–module pairing is not permanent in the traceability model; §8 records two protocols; §9 makes the module user-replaceable; §11 gains the open items above.
- The Phase 0B order changes: the control-architecture decision now precedes the extrusion RFQ and the cost-of-commonality study, because it sets the end-cap penetration count, cap material freedom, engine cavity and connector access. Bus voltage, PSU family, WRGB channel count and size classes are unchanged in substance; the `LT-A` driver decision is unaffected.
- A new product, the Smart Module, needs an identifier, a `PRODUCT.md`, and a sourcing entry (most of which is already in the Core sourcing strategy's electronics rows).
- The cost model carries the modular premium explicitly (port connectors on every engine, the module as its own SKU) so the alternative-1 comparison can be run when quotations arrive.
- Two protocols now need governance: the port (ICR here) and the app protocol (`trophic-contracts`).

## Revisit triggers

Cost test showing the modular premium on Core exceeds the Basic-SKU, service and regulatory benefits; a decision that `AQ-CT-A` becomes the hub and speaks the port; field data from the pilot on module failure and swap rates.
