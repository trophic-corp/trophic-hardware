# EDR-024 — `AQ-LP-A` outflow aim: a dry swivel joint above the waterline; no joint below it

| | |
|---|---|
| **Status** | ACCEPTED (owner decision, 2026-09-19) |
| **Date** | 2026-09-19 |
| **Affects** | AQ-LP-A |
| **Answers** | Lily-pipe decision D-25; changes PROPOSED launch-spec rows L-40/M1 and L-51 (wording), not any approved decision |

## Context

Concept round 1 gave nozzle aim only by rotating the whole pipe in the clip collar (yaw coupled to the pipe's visual alignment). The owner wants the outflow nozzle to aim independently by a swivel. Systems Architect and Manufacturing/Sourcing review (2026-09-18) rejected any joint in the water: it breaks the one-continuous-tube rule, creates a shrimp-trapping crevice, cannot be passivated once assembled, and is the classic crevice-corrosion site under the bleach soaks hobbyists use — worse with the 304 alternate. A joint above the waterline is drainable, brushable, inspectable and grade-neutral. The FZone reference set's "360° adjustable" outflow appears to turn at a joint above the rim (mechanism only noted; no dimensions or forms taken).

## Decision

1. The outflow **may be a two-part pipe** joined by a **friction swivel located above the waterline** (above the rim on a rim-crossing form; at the pipe top on an inside-the-glass form).
2. **No joint, seal, thread or sliding fit of any kind below the waterline.** M1 is restated as: *one continuous tube from the waterline down; no joint below the waterline.* L-51 "no swivel joint in the water" stands; "aim through the clip" becomes "aim through the clip and/or the above-water swivel".
3. Construction to model first: a **socket formed on the tube end** (end-forming already in the process) with a short spigot and a PTFE or silicone friction ring — estimated +₹80–150 per set at 100. The machined 316L coupling (+₹280–480) is the fallback if the formed socket fails sample tests.
4. The nozzle remains formed from the tube (L-50); the swivel gives yaw. Pitch stays a nozzle-form property.

## Consequences

- Round-2 CAD carries the swivel on the outflow; the joint must pass a rotate/leak cycle test (V-T6 extension: 50 cycles, no drip at the joint with the hose pressurised by the canister head) and a CMF review as a visible detail.
- Passivate parts loose, assemble clean; the friction ring material is an assumption until sampled.
- COGS model gains a swivel line; PRODUCT.md §5a gains the assumptions (socket depth, ring section, friction torque).
- Sample required: one formed-socket pair from the tube-forming vendor; one turned coupling pair from a Coimbatore turning shop as fallback.

## Evidence

`products/aquarium/lily-pipes/design/SPECIALIST_REVIEW_2026-09-18_swivel-intake-skimmer.md` §1; `docs/references/lily-pipes/LILY_PIPE_TECHNICAL_REFERENCE.md` (chloride/crevice notes). Evidence tier: specialist review and desk research; no sample yet.
