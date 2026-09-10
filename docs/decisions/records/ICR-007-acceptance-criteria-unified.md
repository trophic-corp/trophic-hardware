# ICR-007 — Acceptance-test criteria unified

**Interface:** Verification (`RK-A-QC`), `trophic-contracts` (timing) · **Status:** ACCEPTED

| Test | Old | New |
|---|---|---|
| T7 drain time | ≤ 30 s / ≈ 55 s / < 60 s / < 90 s | **≤ 60 s** from end of valve stroke to visually empty, every tier |
| T8 overflow | bed depth never exceeds 30 mm | **≤ 42 mm** at 7.2 L/min with the drain blocked for 10 min; no spill over the rim (weir physics: ≈ 38 mm expected) |
| T16 sway | 200 N / ≤ 10 mm *or* 300 N / residual ≤ 5 mm | **300 N** at the top bed, front–back and side, rack loaded 4 × 38 kg: elastic ≤ 10 mm, residual ≤ 2 mm |
| T18 mass | 112.7 ± 7 kg | Per configuration (RK-A-QC Rev 4 §T18) |
| **T19 (new)** | — | `RK-A-107B` joint moment–rotation coupon: ≥ 5 kN·m/rad secant to 50 N·m, no slip below 80 N·m |
| **T20 (new)** | — | Fill air gap: tray filled to the rim with drain and overflow blocked; nozzle outlet visibly ≥ 30 mm above water |
