# EDR-014 — Per-tier cross beams reinstated; decks non-structural

**Status:** ACCEPTED (owner decision 2026-09-10) · **Type:** Engineering · **Supersedes:** RK-A-BRIEF Rev G §12 lever L1 · **Affects:** `RK-A`, `IF-RK-A-MEC`

## Context

The v8 frame had no front-to-rear member at tier level. Depth-plane stability relied on the deck frames as horizontal ties and on the rotational stiffness of an undefined bracket joint (RK-A-REV Rev A findings F-01, F-13). A semi-rigid frame model showed the top-bed sway under the T16 load is governed entirely by joint stiffness, and the platform mechanical standard §5 forbids structural dependence on a part removed for cleaning.

## Decision

Two `RK-A-103` short beams (GI SHS 30 × 30 × 1.5, 480 mm) are fitted at every tier in the upright columns at X 0–30 and X 1226–1256, Y 40–520, Z 243.4–273.4 + 400·n — the same part, length and position family as the existing base pair. `RK-A-103` quantity 2 → **10**. Deck assemblies carry no structural duty and may be lifted out without tools.

## Consequences

- +8 × 0.644 kg = +5.15 kg; +₹562 (costed in RK-A-BRIEF §12).
- The DN50 drain header, which occupied the right-hand upright column, is relocated (ICR-006).
- With EDR-015 joints, the frame model gives 3.4 mm sway at 200 N and 5.4 mm at 300 N including P-Δ at rated post load — inside T16 with margin (RK-A-QC Rev 4, VR-07).
- CAD: `03_BEAM_SHORT_TIER` × 8 in `CEA_RACK_INTEGRATED_v3` v1.
