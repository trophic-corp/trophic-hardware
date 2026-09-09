# EDR-011 — Relocate Fusion components by delete-and-recreate at absolute coordinates

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | Method — all Fusion work |

## Context

Two obvious relocation methods both fail silently in this model. Setting `occ.transform2` reports success and then reverts in parametric mode — bounding boxes are unchanged afterwards. `moveFeatures.createInput2()` rejects occurrences outright with 'invalid argument inputEntities'. A script using either appears to work and does nothing.

## Decision

**Delete every occurrence and recreate the component at absolute coordinates.** Do not attempt occurrence transforms in parametric mode.

Two supporting rules for scripted Fusion work in this project:

- Output returns via **stdout `print()`**, not the function return value.
- Interference results expose `BRepBody`, not components. Read the component name via `b.assemblyContext.component.name`, with `parentComponent` as fallback.
- Full lineage can be read from `app.data.activeHub.dataProjects` -> `dataFiles` -> `versions` **without opening a document**.

## Consequences

- Relocation scripts are longer and rebuild geometry rather than moving it, but they are verifiable: the bounding box actually changes.
- Any relocation must re-establish material assignment and shell features, because the component is genuinely recreated.
- Silent-success is the recurring hazard in this toolchain. Scripts in this project verify results rather than trusting the absence of an exception — the same failure mode that produced the missing STEP export (RB-01).

## Evidence

Working experience, `CEA_RACK_INTEGRATED_v2` v4-v8; `archive/working-tooling/`
