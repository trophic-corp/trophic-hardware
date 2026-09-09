# EDR-013 — Terrace tank on a steel structure, not bearing on the slab

| | |
|---|---|
| **Status** | ACCEPTED (owner decision) |
| **Date** | 2026-09-09 |
| **Affects** | RK-A-WRS, RK-A-ROOM |
| **Relates to** | ND-07 |

## Context

RK-A-WRS §04 Risk 3 gives the terrace tank loading as **5.5 kN/m² concentrated**
worst case, 2.2 kN/m² spread over beam lines, against a typical accessible-terrace
rating of **1.5–2.0 kN/m²**. The source document calls this the one item in the
water recovery design that cannot be resolved by choosing better equipment, and
requires a structural engineer's sign-off against the building's actual drawings
before the tank is ordered.

Read as written, that reads like a hard procurement blocker.

## Decision

**The tank will be mounted on a purpose-built steel structure spanning to suitable
bearing points, not bearing directly on the slab.**

The concentrated slab load figure therefore does not gate the tank order, and ND-07
is **downgraded to low priority**.

## Consequences

- The 5.5 kN/m² concentrated figure applies to a load case the design will not use.
  It should not be quoted as a live risk against the current arrangement.
- **ND-07 stays open as UNKNOWN, deliberately.** The steel structure is not yet
  designed: its span, its bearing points, and the reactions it delivers into the
  building are all unquantified. Nothing has been *resolved* — the load has been
  *relocated*, and where it lands has not been checked.
- The structural engineer's sign-off is not cancelled, only re-scoped: it now covers
  the steel structure and its bearing points rather than the slab under a tank
  footprint.
- Re-raise ND-07 to normal priority as soon as the steel structure is specified, and
  close it only when the reactions are checked against the building.

## Why this is recorded rather than simply closed

Downgrading a risk because the load path changed is not the same as retiring it. A
future reader finding "terrace slab loading — closed" with no structure design on
file would be entitled to assume the building had been checked. It has not.
