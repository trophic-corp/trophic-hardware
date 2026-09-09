# ADR-006 — Fusion 360 remains authoritative for native CAD

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | Repository-wide |

## Context

Migrating engineering into a Git repository creates pressure to also pull CAD into it, so the tree looks self-contained. Fusion 360 is cloud-hosted with its own version lineage; copying or moving those projects to satisfy repository symmetry would break that lineage and create a second, non-authoritative copy.

## Decision

Fusion cloud projects stay exactly where they are. This repository holds an **index** (`docs/engineering/CAD_INDEX.md`) mapping product ID, component/assembly, Fusion project, design, version, hardware revision, engineering release, related drawing and related STEP export.

STEP and F3D files are **exchange and release artifacts**. They are not substitutes for the parametric design and are never edited as the source of truth.

## Consequences

- Fusion version history is preserved intact — v1 to v8 for the integrated design, v1 to v5 for the platform design.
- The repository can be read without a Fusion licence, but cannot be used to reconstruct geometry. That is intentional.
- Every release must record which Fusion version it was exported from, or it is untraceable.

## Evidence

`docs/engineering/CAD_INDEX.md`
