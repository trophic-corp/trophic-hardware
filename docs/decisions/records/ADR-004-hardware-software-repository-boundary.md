# ADR-004 — Keep hardware and software repositories independent; publish via trophic-contracts

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | Repository-wide |

## Context

A Trophic CEA software project already exists and is in development independently. The obvious but wrong move is to let the software repository ingest the hardware repository so it can read sensor lists and valve maps directly. That couples a software build to CAD, drawings, BOMs and costs it has no business reading, and makes every hardware document revision a software concern.

## Decision

Three repositories, not two:

1. **`trophic-hardware`** — this repository. Geometry, drawings, BOMs, validation, manufacturing.
2. **`trophic-contracts`** — a thin, independent repository carrying only stable machine-consumable interface facts.
3. **The existing CEA software repository** — unchanged, untouched, and consuming `trophic-contracts` only.

The software repository must not ingest this repository. This repository must not modify the software repository's architecture or source.

## Consequences

- Hardware documents can revise freely without touching software, as long as the contract does not change.
- A contract change becomes a deliberate, visible event with its own review, rather than a silent consequence of a CAD edit.
- Cost: contract content must be maintained in two places conceptually — the authoritative engineering document, and the published contract derived from it. `docs/system/CONTRACT_EXTRACTION.md` records the derivation so it does not drift.

## Evidence

`docs/system/CONTRACT_EXTRACTION.md`
