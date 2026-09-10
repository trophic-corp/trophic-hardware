# PRODUCT — CEA Rack Platform (Rack A)

**Product ID:** `RK-A`
**Family:** CEA
**Type:** Modular controlled-environment growing rack
**Authoritative CAD:** Fusion 360 `CEA_RACK_INTEGRATED_v3` v1 (Rev 6, ECP-01) — see `docs/engineering/CAD_INDEX.md`

---

## 1. What the product is

A four-tier modular growing rack for controlled-environment agriculture, built
from galvanised steel section, carrying flood-and-drain grow beds, LED
lighting, forced ventilation, environmental sensing and a local control
enclosure. It is designed to be built in Coimbatore, deployed in rows, and
serviced by shared room infrastructure rather than being self-sufficient.

The rack is sold and built in three configurations:

| Configuration | Contents | Cost |
|---|---|---|
| **Core** | Frame, decks, trays, drainage. No active systems | ≈ ₹17,400 (Rev 3 estimate; was ₹12,391) |
| **Grow (Phase 1)** | Core + irrigation, LED interface, standalone EC fans, sensing, control enclosure | **≈ ₹54,300** before valve re-quote (was ₹49,296) |
| **Grow (complete)** | Grow Phase 1 + ducted plenum ventilation | ₹51,936 |
| **Pro** | Grow complete + reflective panel set and extended sensing | ₹56,996 |

LED fixtures themselves are excluded from these figures and are procured
separately.

---

## 2. Scope boundary — what is and is not this product

This distinction was established during the workspace migration and governs
where new work is filed.

### A — Rack product (this directory)

Frame and structure · deck and tray assemblies · in-rack irrigation
distribution from the rack inlet to the nozzles · in-rack drainage from the
tray outlets to the rack drain header outlet · LED mounting interface · rack
ventilation (fans, and later the plenum) · rack sensing and the local control
enclosure · in-rack cable and pipe routing · rack-level protection.

### B — Shared CEA infrastructure (`products/cea/irrigation/water-recovery/`)

The terrace source and recovery reservoirs · the recovery skid, its pumps,
diverter and instrumentation · the room distribution main and the room common
drain · water quality management and blowdown. These serve a whole room and are
sized by room demand, not by rack count of one. They are **not** rack
subassemblies.

### C — Facility / reference implementation (`products/cea/facility-reference/ooty-room-20x12/`)

The Ooty room itself — its dimensions, slab, rack set-out coordinates, aisle
widths, electrical distribution board, room-level HVAC and egress. This is one
worked example of a facility built from the product. It is a reference, not a
deliverable of the rack.

**The interface between A and B is the rack inlet and the rack drain header
outlet.** Both are specified in `interfaces/hydraulic/`.

---

## 3. Frozen product definition

These values are frozen for the current revision. Changing any of them requires
a decision record.

### Envelope and mass

| Parameter | Value |
|---|---|
| Installed envelope (W × D × H) | 1456 × 690 × 1960 mm |
| Structure-only envelope | 1256 × 563 × 1960 mm |
| Phase-1 build envelope | 1456 × 690 × 1960 mm (648 withdrawn) |
| Dry mass | 136.39 kg model, all systems · Core 91.7 · Grow Phase 1 108.0 · Grow complete 126.9 kg |

### Tier geometry

Four tiers. Bed datum heights **300 / 700 / 1100 / 1500 mm**, pitch 400 mm.

The **bed datum is the top face of the deck mesh panel** — not the beam, not
the tray floor. The stack below each datum is fixed:

| Element | Z range (first tier) |
|---|---|
| Beam | 243.4 – 273.4 |
| Deck rail | 273.4 – 298.4 |
| Deck mesh panel | 298.4 – **300.0** |
| Tray | from 300.0 upward |

Four tiers at a 1500 mm top bed is the reach-limited maximum: by the NIOSH
revised lifting equation the recommended weight limit falls to zero above
1750 mm, which rules out a fifth tier at 1900 mm (EDR-002).

### Reserved corridors

| Corridor | Location | Purpose |
|---|---|---|
| Wet services | Y 435 – 525 mm from the front face | In-bed drain hardware. Laterals leave at Y 500–540 and cross the rear plane only in the ICR-006 windows |
| Rear service zone | Y 571 – 690 | Header, laterals, tundish, Phase-1 fans; plenum reserve X ≤ 1150 |
| LED row 1 | Y 148 – 208 mm | Fixture body |
| LED row 2 | Y 352 – 412 mm | Fixture body |

### Safety-critical invariants

| Invariant | Rule |
|---|---|
| Backflow air gap | 100 mm between drain header outlet (Z 200) and tundish rim (Z 100) = 2 × DN50. **Must never be plumbed closed** (IS 12234 / EN 1717) |
| Fill solenoids (zero-ΔP) | Normally **closed** |
| Drain valves (motorised ball) | Spring-return **open** |
| Fill-point air gap | Nozzle outlet ≥ 30 mm above the tray rim (38 nominal) — ICR-005 |
| Recovery diverter FV-01 | Spring-return **to waste** |
| Terrace master valve MV-01 | Fails **closed** |
| Residual current device | **Type A RCBO**, not Type AC — LED drivers and inverter compressors produce pulsating DC residual current |

### Materials

Frame and decks: GI to **IS 4923 YST210, Z275** coating. Joints: 3 mm GI gusset plates on M8 rivet nuts with crush tubes (EDR-015). Deck mesh: flattened expanded metal. uPVC pipework to
**IS 4985**. Earthing to **IS 3043**. Seismic per **IS 1893**. Inspection per
**IS 732**.

Where UV-C treatment is used in the shared water loop, chelated iron must be
**Fe-DTPA or Fe-EDDHA**, not Fe-EDTA, which UV-C degrades. Iron is verified
monthly. This constrains the nutrient specification, not the rack hardware.

---

## 4. Document set

| Document | ID | Rev | Location |
|---|---|---|---|
| Platform brief | `RK-A-BRIEF` | G | `requirements/` |
| Systems specification | `RK-A-SYS` | 2 + addenda A, B | `design/` |
| Parameter master | `RK-A-PARAM` | 2 | `design/` |
| Structural drawings | `RK-A-DWG` | 3 (tabular) | `drawings/` |
| Manufacturing pack | `RK-A-MFG` | 3 | `manufacturing/` |
| Engineering validation record | `RK-A-QC` | 4 | `verification/` |
| Independent review | `RK-A-REV` | A | `verification/` |
| Change package | `RK-A-ECP-01` | A | `changes/` |

Interface specifications live under `interfaces/`. Published-artifact URLs for
each document are in `docs/system/DOCUMENT_REGISTER.md`.

---

## 5. Design rules that must survive

1. **The model governs** over the drawing when they disagree — one recorded
   exception, EDR-004.
2. Component relocation in Fusion is done by **deleting occurrences and
   recreating the component at absolute coordinates**. `occ.transform2` silently
   reverts in parametric mode and `moveFeatures.createInput2()` rejects
   occurrences.
3. A pump never lifts water from the room to the terrace. At Ooty's altitude
   atmospheric pressure is 77.2 kPa and practical self-priming suction lift is
   2.5–4 m. **The pump goes at the low point and pushes up** (EDR-005).
4. Supply is **gravity fed** from the terrace. Static head 2.66 m against
   0.33 m of loss at 7.2 L/min — margin of about 8×. Head runs out near
   15 L/min; four tiers concurrent (28.8 L/min) still passes at 0.67 m loss.
   There is no supply pump.
5. The drain chain must be continuous joint-by-joint from every tray outlet to
   the rack drain header outlet, and then break at the air gap.
6. **No bolt through a hollow section without a crush tube or rivet nut** at 18 N·m; 4 N·m otherwise (EDR-015).
7. **No pipe intersects a brace bar**; crossings of the rear plane only in the ICR-006 windows.
8. **Every gravity-operated valve is specified at ΔP-min = 0** (EDR-016).
