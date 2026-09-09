# CEA Racks

| Product | ID | Stage |
|---|---|---|
| CEA Rack Platform (Rack A) | `RK-A` | **Released — `RK-A R1`** |

The only fully engineered product Trophic has. Four tiers, 1456 × 690 × 1960 mm
installed, 112.66 kg dry, released for prototype fabrication.

See `rack-platform/PRODUCT.md` for the product definition and
`rack-platform/CURRENT_STATE.md` for what is open.

## Future variants

A materially different rack takes the next variant letter (`RK-B`), not a revision of
Rack A. Revisions are `Rev n` and never change the ID.

Two constraints any future rack inherits, because they are physics rather than
preference:

- **Four tiers is the reach-limited maximum** at a 400 mm pitch. NIOSH RWL falls to
  zero above 1750 mm (EDR-002). A taller rack needs a handling aid, not a re-argument.
- **The bed datum is the deck mesh top face** (EDR-001). Every downstream elevation
  measures from it, and it is published as a contract.

Nothing else about Rack A is binding on a successor.

## What is not filed here

In-rack irrigation, drainage, LED mounting and the control enclosure are all `RK-A`
parts and live under `rack-platform/`. The products that *interface* with the rack —
`LT-A` fixtures, `EV-A` plenum, `CT-A` controller — have their own folders under their
own families, because they are separable products with their own lifecycles.
