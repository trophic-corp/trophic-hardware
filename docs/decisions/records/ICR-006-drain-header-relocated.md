# ICR-006 — Drain header relocated behind the rear-right upright

**Interface:** Mechanical depth allocation (`IF-RK-A-MEC` §2), hydraulic drain chain (`IF-RK-A-HYD` §5) · **Status:** ACCEPTED

## Context

The per-tier cross beams (EDR-014) occupy the right-hand upright column where the DN50 header stood (X 1216–1266, Y 455–505). An outboard header (X 1262–1312) was evaluated and rejected: it collides with the cross-beam gusset plates and grows the installed width to 1472 mm, which the Ooty set-out cannot absorb.

## Decision

The header moves to **X 1200–1250, Y 575–625, Z 200–1450** — behind the rear-right upright, in the plenum reserve zone, right of the fan end cap. Installed envelope **unchanged at 1456 × 690 × 1960**. Per tier: tray-drain lateral runs in −X from the drain valve at Y 500–540 to a crossing window at **X 1040–1080**, then +Y through the rear beam plane between the beams, then +X behind the rack at Y 580–620 into the header. Overflow laterals cross at X 1080–1112 (tiers 2–4) and, for tier 1, at X 990–1022 (Z 182–214) entering the header rear face at Y 623–655. Tundish 90 × 90 × 80 at X 1180–1270, Y 570–660, Z 20–100 (air gap 100 mm unchanged, outlet Z 200 unchanged); leak sensor beneath it. Header level switch at Z 250–310 unchanged.

## Consequences

- V11's rule "no pipe through a structural bracing plane" is restated as **"no pipe intersecting a brace bar; crossings only in the defined windows"** — the windows are verified clear of both bars at every tier in `CEA_RACK_INTEGRATED_v3` v1.
- The wet-services corridor (EDR-003) remains Y 435–525 for the in-bed drain hardware; the rear service zone Y 571–690 now carries the header and laterals and is shared with the plenum reserve (ICR-004 still OPEN — the Phase-2 plenum must respect X ≤ 1150 and the four lateral windows between plenum tiers).
- ND-04 unchanged. No room set-out change.
