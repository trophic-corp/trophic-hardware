# EDR-025 — `AQ-LP-A` intake adjustment by a telescopic end cap; no sleeve above the slot zone

| | |
|---|---|
| **Status** | **WITHDRAWN by the owner, 2026-09-19 (same day)** — the plain removable end cap of concept r1b/r2b is reinstated; see §Withdrawal below |
| **Date** | 2026-09-19 |
| **Affects** | AQ-LP-A |
| **Answers** | Lily-pipe decision D-26; changes PROPOSED launch-spec rows L-32/L-33 (end cap) and adds an adjustment row; M8 and L-34 unchanged in intent |

## Context

The owner wants the intake draw to be user-adjustable. Specialist review rejected a rotating or sliding sleeve over the slot zone (full-length crevice, blocks the straight brush path, thin-wall ovality makes the fit unmakeable as cut, stainless galling). The removable end cap already exists and already has a parting line; extending it into a sleeve that enters from the free end adjusts open area with one moving part that is also the part removed for cleaning. The FZone reference intake is fixed, not adjustable; market "adjustable intakes" are skimmer bypasses.

## Decision

1. The intake end cap becomes a **telescopic cap**: a plain sleeve, closed at the bottom, that slides up over the tube from the free end to cover **zero to two of the three slot rows**, and pulls off entirely for brushing.
2. The sliding pair is not stainless on stainless: a **silicone lip or PTFE band** in the cap carries the friction and seals the crevice; the band is a wear part supplied as a spare.
3. Fully retracted, open area is the full slot zone (≥5× bore, L-31); the slot width limit (≤1.0 mm, L-30) is unchanged; the sleeve edge never leaves a gap in the 1–2 mm range (M8) — the band closes it.
4. Stepped fixed caps remain the fallback if the telescopic cap fails the sample or shrimp-safety test.

## Consequences

- Round-2 CAD replaces the fixed cap with the telescopic cap; assumptions added: sleeve length, band section, travel, detent or friction torque, clearance.
- Open-area-vs-position becomes a stated table on the care card once V-T5 measures it.
- Verification: V-T5 (shrimp safety at every position, including the band edge), V-T6 (brushability with the cap off), a 200-cycle slide test with the band, and post-slot ovality data from the laser vendor (RFQ) because the sleeve fit depends on it.
- Estimated +₹150–300 per set at 100; COGS model updated.

## Evidence

`products/aquarium/lily-pipes/design/SPECIALIST_REVIEW_2026-09-18_swivel-intake-skimmer.md` §2. Evidence tier: specialist review; no sample yet.

## Withdrawal (owner, 2026-09-19)

Built as `AQ-LP-A_CONCEPT_r2a` and reviewed: a 62.5 mm cup under a Ø17 pipe became the largest object in the tank, moved the slot zone 40 mm higher, added a wear band, a sliding fit on thin-wall tube and two tests, for a throttle no customer evidence asked for (Phase 0A research; the FZone reference intake is fixed). Owner withdrew the feature; the intake returns to a straight tube, one slot band and a plain removable cap that is the brush entry. The intake-throttle idea, if it returns, belongs with a P2 skimmer bypass (ADR-009). D-26 is closed as "no adjustable intake in P1".
