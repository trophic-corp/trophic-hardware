# EDR-010 — Rear brace RK-A-104 is 1797 mm, not 1345 mm

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A |

## Context

Rev 1 of the part drawings dimensioned the rear brace `RK-A-104` at 1345 mm. The braced bay is 1194.7 x 1341.6 mm, whose true diagonal is 1797 mm. The 1345 mm figure appears to have been taken from a single bay edge rather than the diagonal.

## Decision

`RK-A-104` overall length is **1797 mm**, hole centres at **20 and 1777 mm**, mass **1.06 kg each** (from 1.04 kg).

## Consequences

- Rev 1, if released, would have produced a part **452 mm short** — an unbuildable rack and a scrapped batch. This is the strongest single argument for the drawing reissue.
- The drawing generator part table (`drawings/generator/parts.py`) was corrected at source, so the error cannot reappear on regeneration.
- Structural drawings reissued at Rev 2 carrying the correction.
- Review lesson: any dimension that should be a computed diagonal is now checked against the bay envelope rather than trusted.

## Evidence

`RK-A-DWG_Rev2`; `drawings/generator/parts.py`
