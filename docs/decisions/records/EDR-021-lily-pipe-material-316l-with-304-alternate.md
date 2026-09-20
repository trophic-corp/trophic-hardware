# EDR-021 — `AQ-LP-A` wetted material: 316L stainless primary, 304 as qualified alternate

| | |
|---|---|
| **Status** | ACCEPTED (owner decision, 2026-09-17) |
| **Date** | 2026-09-17 |
| **Affects** | AQ-LP-A |
| **Answers** | `products/aquarium/lily-pipes/PRODUCT.md` §5 decision 1 (widened from "glass or acrylic" to material route); lily-pipe decisions D-02 and D-05 |

## Context

Phase 0A research (`products/aquarium/lily-pipes/`) compared borosilicate glass, stainless steel and acrylic/PETG. Glass breakage, hose-removal stress and cleaning are the strongest recurring customer problems; glass also has weak repeatability and fragile freight for a Coimbatore venture, and no Coimbatore glass capability was proven. Stainless tube fabrication is available in Tamil Nadu job-work, repeatable, traceable by mill certificate, and low transit risk. The research proposed 316L for chloride margin (≈1000 ppm vs ≈200 ppm for 304) in CO₂-acidified tanks with crevices; earlier owner work had assumed 304.

## Decision

1. The launch product `AQ-LP-A` is **stainless steel**. Glass and acrylic/PETG are not the launch material.
2. **316L is the specified grade.**
3. **304 is a qualified alternate**, usable only if 316L tube in the required size cannot be obtained at acceptable cost or lead time, **and** 304 passes the same corrosion and finish tests (lily-pipe `VALIDATION_PLAN.md` V-T7).
4. The design must not depend on which of the two grades is used: same geometry, same processes, same finish.
5. Grades are never mixed within a production lot; the grade is proven per lot by EN 10204 3.1 certificate and PMI, and product claims state the grade actually supplied.

## Consequences

- CAD may proceed as class CONCEPT with stainless forming rules (`docs/system/CAD_SEED_GUIDE.md` §4).
- RFQs ask for 316L first and 304 as a priced alternate.
- V-T7 must test both grades if 304 is to remain available.
- Glass remains open only for possible future accessories, not for this product.

## Evidence

`docs/references/lily-pipes/COMPETITOR_LILY_PIPE_REFERENCE.md` §4; `LILY_PIPE_TECHNICAL_REFERENCE.md` §8.2; `SOURCING_STRATEGY.md` §2, §9; `LILY_PIPE_AESTHETIC_REFERENCE.md` §5. Evidence tier: desk research — not yet tested.
