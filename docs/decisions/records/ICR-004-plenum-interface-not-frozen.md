# ICR-004 — Rack-to-plenum interface is deliberately not frozen

| | |
|---|---|
| **Status** | OPEN |
| **Date** | 2026-09 |
| **Affects** | Mechanical / electrical — plenum mount |

## Context

ADR-005 defers the plenum to Phase 2. Phase-1 racks will be built and installed before the plenum exists, so they will carry whatever mounting provision was guessed at, not what the plenum will need.

## Decision

**No decision yet.** The interface is recorded as open rather than assumed.

What is currently held, and is not a commitment:

| Item | Current state |
|---|---|
| Installed depth with plenum | 690 mm (room set-out assumes this) |
| Phase-1 build depth | 648 mm |
| Depth reserved for plenum | 42 mm |
| Mounting provision | Not specified |
| Fan electrical interface | Standalone EC fans, wired at the rack; plenum reuses the same fans |

## Consequences

- Phase-1 racks cannot be guaranteed plenum-ready. Retrofit rework is a live risk.
- Room set-out must be confirmed at the plenum-ready pitch so the retrofit does not require moving racks (ND-04).
- Decision required before the Phase-1 fabrication release, not before the plenum design: the constraint lands on the racks that get built first.

## Evidence

`products/cea/racks/rack-platform/CURRENT_STATE.md` ND-03, ND-04
