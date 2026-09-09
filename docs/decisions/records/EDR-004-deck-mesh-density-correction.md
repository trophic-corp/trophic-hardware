# EDR-004 — Correct deck mesh density to 1884 kg/m3 — the drawing governed over the model

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | RK-A |

## Context

The mass model was wrong twice. First, solid placeholder primitives gave 1,246.4 kg (the plenums alone accounted for 1,008 kg). Shelling to real wall thicknesses and assigning correct materials brought it to 147.67 kg. It was still wrong: the deck mesh had been given the density of 35 %-open perforated sheet.

## Decision

Deck mesh is **>=70 % open expanded mesh**, correctly modelled as an effective density of **1884 kg/m3** — 1.98 kg per panel. Rack dry mass is **112.66 kg**.

This is the one recorded case where **the drawing was right and the model was wrong**. It is the documented exception to the standing rule that the model governs.

## Consequences

- Rack dry mass falls from 147.67 kg to 112.66 kg, which changes floor loading, anchor sizing and the room point-load calculation.
- The manufacturing pack and structural drawings were reissued at Rev 2 against the corrected figure.
- Standing rule amended: 'the model governs' holds, **except** where the model carries a placeholder property that was never verified against the specified material. Placeholder densities are now a review item.

## Evidence

Fusion `CEA_RACK_INTEGRATED_v2` v8 release note: 'Rev 5 - deck mesh density corrected to 76 pc open area'; `RK-A-QC_Rev3`
