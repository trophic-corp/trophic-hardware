# Platform Mechanical Standards

Derived from decisions validated on `RK-A`. A new product complies or raises a
decision record to deviate.

**Scope caveat:** these are standards for *fabricated steel structural products*.
They are stated as platform standards because that is what exists today. Glass,
acrylic and moulded products (most of the aquarium family) will need their own set —
see `platform/README.md`.

## 1. Materials

| Application | Specification | Source |
|---|---|---|
| Structural sections and decks | Pre-galvanised steel to **IS 4923**, grade **YST210**, **Z275** coating | `RK-A-SYS` Rev 2 |
| Flat bar bracing | Pre-galvanised flat, e.g. 25 × 3 mm | `RK-A-PARAM`, `RK-A-DWG` Rev 2 |
| Deck panel | ≥70 % open expanded mesh, effective density **1884 kg/m³** | EDR-004 |
| Pipework, wet side | uPVC to **IS 4985** | `RK-A-SYS` Rev 2 |
| Sheared edges | Touched up with zinc-rich paint | `RK-A-DWG` Rev 2 |

**Placeholder densities are a review item.** EDR-004 exists because an unverified
placeholder density put the rack mass out by 31 %. Any material property in a CAD
model that has not been checked against the specified material is a defect waiting to
be found.

## 2. Hole grid and fixing

| Parameter | Value |
|---|---|
| Grid pitch | **50 mm** |
| Hole diameter | **Ø9 mm** |
| Grid start height | 150 mm above floor datum |
| Fastener | M8 |
| **M8 torque** | **18 N·m** |

## 3. Structural rules

| Rule | Value | Source |
|---|---|---|
| Earth continuity, every frame | **< 0.1 Ω**, tested and recorded per unit | IS 3043 |
| Seismic | Per **IS 1893** | |
| Wall anchoring | **Mandatory**, not optional, on floor-standing racks | `RK-A-MFG` Rev 2 §11 |
| Shelf flatness | 3 mm | `RK-A-PARAM` |

Height:depth ratio 3.48:1 on `RK-A` is below the 4:1 threshold at which anchoring is
normally mandated, so freestanding is technically defensible. It was rejected anyway:
the empty-rack tip-over pull is 139 N (~14 kgf), called "genuinely marginal" in the
source. **Anchoring is specified because the marginal case is the one that hurts.**

## 4. Ergonomics

| Rule | Value |
|---|---|
| Method | **NIOSH revised lifting equation** |
| Acceptance | Lifting Index **< 1.0** (`RK-A` achieves 0.50–0.72) |
| Hard ceiling | RWL falls to **zero above 1750 mm** — no routine manual task above it |

This is what limits `RK-A` to four tiers (EDR-002). It applies to any product with a
loading or servicing task, not only racks.

## 5. Structure must never depend on a removable part

From `RK-A-DWG` Rev 2, on why the rear panel is not used as a diaphragm:

> The panel comes off for cleaning, and structure must never depend on a part
> somebody removes to wash.

Generalised: if a part can be removed for cleaning, service or access, it carries no
structural duty.

## 6. Wet/dry separation

| Rule | Value |
|---|---|
| Minimum electrical/water vertical separation | **236 mm** |
| Cable crossing a wet zone | Not permitted without a drip loop |
| Overflow rule | Every vessel keeps a gravity overflow **one nominal size larger than its largest inlet**, terminating in a **visible air gap** |

**An overflow discharging into a closed pipe is not an overflow** — it is a second way
to pressurise the vessel. This is a design rule, not a preference.
