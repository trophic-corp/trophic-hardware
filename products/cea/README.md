# CEA — Controlled Environment Agriculture

Five product families. Only `racks` has completed engineering; `irrigation` has a
validated design for shared infrastructure. The rest are Phase 0.

| Family | Products | Stage |
|---|---|---|
| `racks/` | `RK-A` CEA Rack Platform | **Released — `RK-A R1`** |
| `irrigation/` | `WR-A` Closed-loop water recovery | Design validated |
| `lighting/` | `LT-A` LED grow bar | **Phase 0** |
| `environmental-control/` | `EV-A` Ducted ventilation plenum | **Phase 0**, deferred by ADR-005 |
| `sensors-controllers/` | `CT-A` Rack controller · `CT-B` Room controller | **Phase 0** |
| `facility-reference/` | Ooty 20 × 12 ft room | Reference, not a product |

## Ownership classes (ADR-003)

| Class | Test | Example |
|---|---|---|
| **A — Product** | Scales with unit count; identical in every installation | `RK-A`, `LT-A` |
| **B — Shared infrastructure** | Sized by room demand; serves many units | `WR-A` |
| **C — Facility reference** | Specific to one building | `facility-reference/` |

Check this before filing anything new. The rack accumulated content belonging to all
three classes before the migration separated them.

## Why Phase 0 documents look thin

Because the engineering has not been done. A Phase 0 document holds what is decided,
what is inherited, and what is open — and refuses to fill the gaps. `LT-A` and `EV-A`
carry real inherited interface facts because the rack fixed them; the rest of those
documents is open questions, and that is correct.
