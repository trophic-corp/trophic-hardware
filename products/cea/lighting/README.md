# CEA Lighting

| Product | ID | Stage |
|---|---|---|
| LED grow bar | `LT-A` | **Phase 0A research complete (2026-09-11), 0B decisions pending** |

LED **fixtures** are currently procured, not made — every cost figure in `RK-A-MFG`
excludes them. The rack provides the mounting rail, the 48 V supply and the 0–10 V
dimming pair; what hangs off it is somebody else's product today.

`LT-A` is the decision to change that. The interface is already fixed by the rack, so
this is an unusually well-bounded Phase 0: the envelope, the supply, the control
signal and the optical target are all inherited. What is open is everything inside
the extrusion.

**2026-09-11 research position:** a fixed horticultural spectrum with programmable
intensity and photoperiod is supported by the microgreen evidence; the rack spec
permits either a CV 48 V or a CC ≤ 60 V supply, and which one is the open driver
decision; the remote driver's open-circuit voltage must stay ≤ 60 V at the canopy
connector (ND-12); the "photoinhibition above 210" rationale is unsupported (ND-11).
Research lives in `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` (Parts
B1, D1) and the product's `sourcing/SOURCING_STRATEGY.md`.
