# EDR-015 — Rivet-nut joints and RK-A-107B gusset-plate connector

**Status:** ACCEPTED (owner decision 2026-09-10) · **Type:** Engineering · **Affects:** `RK-A`, `platform/mechanical-standards` §2

## Context

M8 at 18 N·m (≈ 11 kN preload) through both walls of 1.5–1.6 mm hollow sections collapses the walls at ≈ 0.6–0.9 kN (RK-A-REV F-03). The bracket `RK-A-107` was not modelled and its documented geometry could not be reconciled with the 50 mm grid (F-02).

## Decision

1. **M8 steel flat-head rivet nuts** (zinc-plated, grip 1.0–3.0 mm, hole Ø11.0 +0.1/−0) set in the *near wall only* of the upright at every plate position. The Ø9 grid hole in the far wall is unused at that position. 80 per rack.
2. **`RK-A-107B` gusset plate**: flat 3 mm GI plate, 140 × 80, lying on the outer face of post and beam together — front/rear faces (Y −3…0, 560…563) for the long beams, outer X faces (X −3…0, 1256…1259) for the cross beams. Two Ø9 on the post centreline at grid rows 250/300 + 400·n (tiers) or 150/200 (base); two Ø9 at 25 and 75 mm from the beam end bolting *through* the beam's end holes with **crush tubes** Ø8.5 × 27. Four M8 per joint; 40 joints per rack; four hole-pattern variants (LH/RH × tier/base) from one blank.
3. **18 N·m** remains the torque for M8 into rivet nuts and for through-bolts with crush tubes. Any M8 through a hollow section *without* a crush tube is limited to **4 N·m** with a serrated flange nut (LED saddles, panels).
4. The rear plates double as the packers under rear-brace bar A; the brace bolts at (X 20, Z 150) and (X 1236, Z 1450) share the plate's rivet nut (M8 × 25).

## Consequences

Joint rotational stiffness ≈ 8 kN·m/rad; friction slip moment ≈ 110 N·m against ≈ 25 N·m demand at 300 N — no slip, no residual set. Mass +10.3 kg plates, +2.7 kg fasteners. Fastener items 208 → ≈ 450 (264 threaded). One M8 rivet-nut setter added to shop tooling. The keyhole/hook connector stays on the volume roadmap; new acceptance test **T19** (joint moment–rotation coupon) is its qualification data.
