# EDR-019 — Flood tray RK-A-401 modelled as the formed part

**Status:** ACCEPTED · **Type:** Engineering · **Affects:** `RK-A-DWG` CH11, `RK-A-MFG` §05/§10, `RK-A R1` release note

## Context

The v8 tray was a flat-floored open box with one Ø40 hole: no collar, bosses, fall, radii or overflow penetration. Under "the model governs" the R1 STEP would produce the wrong thermoforming tool (RK-A-REV F-08).

## Decision

The tray body carries the 30 mm overflow collar (Ø32 bore, 3 mm wall) at X 120 from the right end / Y 480 and both floor openings (Ø40 drain at 60 from the right end, Ø32 overflow). Deck panel `RK-A-203` gains Ø52 and Ø46 clearance holes so a tray with tank connectors fitted lifts straight up (closes F-22). The `RK-A R1` tray STEP is annotated **not-for-tooling** in the release index.

**Floor fall (ND-10):** a 2–3 mm fall on a tray whose floor rests on the deck mesh cannot be formed without either a sloped underside (loses deck support) or formed drainage channels. The model carries a flat 3 mm floor; the drawing note "fall 2–3 mm" is withdrawn pending a decision between (a) flat floor + level tolerance, (b) formed channels to the drain boss (recommended, also stiffens the floor). Open item ND-10.
