# ADR-009 — `AQ-LP-A` P1 ships without a surface skimmer and without a reserved skimmer interface

| | |
|---|---|
| **Status** | ACCEPTED (owner decision, 2026-09-19) |
| **Date** | 2026-09-19 |
| **Affects** | AQ-LP-A (P1); P2 skimmer scope |
| **Answers** | Lily-pipe decisions D-15 (timing) and D-27; retires PR-SC-02 from P1 requirements |

## Context

Specialist review (2026-09-18) put an integrated float skimmer at +₹780–1,020 per set at 100 including the per-unit air-ingestion test, forced the pipe top to the water surface (conflicting with the rim-hook geometry), and made the 300–1500 l/h clean/clogged flow-window rig (V-T4) a launch gate. Systems Architect proposed reserving a minimum interface envelope for a later clip-on module; Manufacturing/Sourcing proposed reserving nothing because a reserved feature costs every P1 set ₹30–60 and freezes geometry from a concept.

## Decision

1. **No skimmer in P1**, integrated or modular.
2. **No reserved skimmer interface on P1** (the Manufacturing view is adopted; the Systems view is preserved below). PR-SC-02 is withdrawn from P1 requirements; PR-P2-* stay parked.
3. A skimmer, if ever offered, is a **separate product (P2)** designed against its own requirements, with its own validation; it may mount to the P1 clip family if that proves natural, but P1 makes no promise.

## Preserved alternative

Systems Architect: freeze a minimum dimensional envelope (pipe-top OD and length, clip datum, waterline offset range) now so a P2 module can follow without a P1 revision. Re-open this record if Stage 0B interviews (V-C3) show skimmer demand attached to Trophic pipes specifically rather than to a separate skimmer.

## Consequences

- The intake-adjustment decision (EDR-025) is standalone and not a skimmer bypass.
- The pipe top is free to sit above the rim; D-24 (round-2 form) is unconstrained by skimmer needs.
- Launch spec "explicitly not in launch" keeps the skimmer; the care card may say a separate skimmer works alongside the set.

## Evidence

`products/aquarium/lily-pipes/design/SPECIALIST_REVIEW_2026-09-18_swivel-intake-skimmer.md` §3; `docs/references/lily-pipes/LILY_PIPE_TECHNICAL_REFERENCE.md` §6 (skimmer failure modes, field evidence STRONG). Evidence tier: specialist review and desk research.
