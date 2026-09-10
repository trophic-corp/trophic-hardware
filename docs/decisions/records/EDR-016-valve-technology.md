# EDR-016 — Valve technology: zero-ΔP fill solenoids, motorised spring-return-open drain valves

**Status:** ACCEPTED as baseline (owner 2026-09-10) · **Open comparison:** owner intends to trial alternatives (ND-09) · **Type:** Engineering · **Affects:** `RK-A`, `IF-RK-A-HYD`, `trophic-contracts` (actuator timing)

## Context

No minimum operating differential was specified for the eight rack valves. Drain valves must open on ≈ 0.002 bar of gravity head; fill valves see ≈ 0.26 bar (RK-A-REV F-07). Servo-assisted solenoids will not open on the drain side.

## Decision

- **Fill (4 ×):** DN20 direct-acting / forced-lift **zero-differential** solenoid, normally **closed**, 24 V DC, Kv ≥ 4 (head budget unchanged, 0.119 m at 7.2 L/min), PP/PA body, EPDM seals, IP65 coil.
- **Drain (4 ×):** DN40 full-bore **motorised ball valve**, 24 V DC, **spring-return to OPEN**, Kv ≈ 60, stroke 5–15 s, IP67 actuator, EPDM seats, PP/PVC-U body, position feedback to the rack controller. Energised closed during fill + dwell.
- Fail-safe matrix (EDR-007) unchanged in effect.
- **Control consequence:** drain open is no longer instantaneous; fault detection and the sequential-draining interlock count from end of stroke (contracts change).

## Recorded for later trial (ND-09)

(a) all-solenoid with zero-ΔP normally-open DN40 valves; (b) all-motorised. Compare energy per cycle, drain time, failure-to-open events over 30 days, cost. The trial does not change the frozen interface until an EDR supersedes this one.
