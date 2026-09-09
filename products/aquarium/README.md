# Aquarium / Aquascaping

**No engineering exists in this family.** Every product below is Phase 0: a scope
statement, the design variables that must be settled, and — where useful — industry
reference points that bound the design space.

| Product | ID | Stage |
|---|---|---|
| Programmable aquarium light | `AQ-LT-A` | Phase 0 |
| Sensor / controller | `AQ-CT-A` | Phase 0 |
| Lily pipes | `AQ-LP-A` | Phase 0 |
| Filtration | `AQ-FL-A` | Phase 0 |
| Pumps | `AQ-PU-A` | Phase 0 |
| CO₂ equipment | `AQ-CO-A` | Phase 0 |
| Tools and accessories | `AQ-TL-A` | Phase 0 |

## Read this before using any document in this family

Each product document has a section headed **"Industry reference points — NOT TROPHIC
DECISIONS"**. Those numbers are typical market values, included so that a design
conversation and a massing model have something to push against. **They are not
specifications, no drawing may cite them, and no CAD model built from them may be
described as a Trophic design.**

Where a document has nothing to say, it says nothing. Thin sections here are accurate,
not lazy.

## Sequencing

The CEA suite's owner decisions put **microgreens first and aquatic production after
the first microgreen rollout**. This family is real but not next. Its main near-term
value is that the platform standards get tested against products that are not
fabricated steel — see `platform/README.md`.

## What this family shares with CEA

Genuinely shared today:

- **Identifier standard** — same product/part/document scheme
- **Capability vocabulary** — the CEA suite's ADR-0002 explicitly anticipates this
  family: a programmable tank light is a `light.dim` + `light.schedule` device, and
  its platform integration is *none new*. `AQ-LT-A` and `AQ-CT-A` should be designed
  to that vocabulary rather than inventing one
- **Fail-safe thinking** — a device is safe with no power and no signal

Not shared, and should not be forced:

- Mains protection schedules (Type A RCBO, SPD, TN-S) — sized for a CEA installation
- The 50 mm Ø9 hole grid, GI sections, M8 at 18 N·m
- The 236 mm wet/dry separation
