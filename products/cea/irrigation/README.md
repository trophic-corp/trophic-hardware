# CEA Irrigation

| Product | ID | Stage |
|---|---|---|
| Closed-loop water recovery | `WR-A` | **Design validated** |

Shared CEA infrastructure (owner class B): sized by room demand, serving every rack.
See `water-recovery/README.md`.

## Scope boundary

**In-rack irrigation is part of the rack product, not this family.** The fill
manifold, solenoids, nozzles, tier drops, tray outlets, strainers, overflow and drain
header are all `RK-A` parts. This family begins at the rack inlet and resumes below
the rack drain header outlet — with the 100 mm air gap sitting exactly on the
boundary (ICR-003).

Fertigation dosing (`DOS-01`) is part of the recovery skid, not a separate product.
Splitting it out would be a product decision nobody has made.

## Not scoped

A standalone fertigation skid for non-rack use, and any irrigation product for the
aquarium family. Neither has been requested.
