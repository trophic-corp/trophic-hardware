# ADR-005 — Defer the ducted plenum to a Phase-2 entity; ship standalone EC fans in Phase 1

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A |

## Context

The ventilation plenum is a meticulous design problem in its own right — duct geometry, static pressure distribution, fan curve matching and acoustic behaviour. Holding the whole rack release until the plenum is optimal would stall a prototype that is otherwise ready.

## Decision

Phase 1 ships **standalone EC fans**. The plenum is designed as a separate entity in month 2-3 and introduced as a retrofit that houses those same fans.

The rack keeps the plenum-inclusive installed depth of 690 mm in room set-out even though the Phase-1 build is 648 mm deep.

## Consequences

- Accepted uniformity penalty for Phase 1: point-source fan velocity CV is about 33 % against about 10 % for a ducted plenum (published CFD). Phase-1 crop data must be read with that in mind and is not directly comparable to Phase-2 data.
- Racks are spaced at the plenum-ready pitch so the retrofit does not require moving racks — this needs explicit confirmation in the room set-out (ND-04).
- The rack-to-plenum interface is **not frozen**, which is an open risk carried as ICR-004.

## Evidence

User direction; `RK-A-SYS_Rev2` ventilation section
