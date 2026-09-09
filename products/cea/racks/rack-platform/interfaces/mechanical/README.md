# Interface Specification — Mechanical

**Interface ID:** `IF-RK-A-MEC`
**Between:** A — Rack product · C — Facility · and the deferred plenum entity
**Authority:** `RK-A-DWG` Rev 2, `RK-A-SYS` Rev 2
**Related decisions:** EDR-001, EDR-002, EDR-003, EDR-004, ICR-004

---

## 1. Envelope

| Envelope | W × D × H (mm) | Applies to |
|---|---|---|
| **Installed** | 1456 × **690** × 1960 | Room set-out, clearance planning |
| Structure only | 1256 × 563 × 1960 | Fabrication |
| Phase-1 build (no plenum) | 1456 × **648** × 1960 | As-built Phase 1 |

**Room set-out uses the installed 690 mm depth even for Phase-1 racks** so the
plenum can be retrofitted without moving racks. Confirming this is ND-04.

| Property | Value |
|---|---|
| Dry mass | **112.66 kg** |
| Parts / occurrences | 45 / 177 |
| Height limit rationale | Reach-limited, see §3 |

## 2. Depth allocation (from the front face)

| Y range (mm) | Allocation |
|---|---|
| 148 – 208 | LED row 1, fixture body |
| 352 – 412 | LED row 2, fixture body |
| **435 – 525** | **Wet services corridor — reserved (EDR-003)** |
| to 563 | Structure, rear bracing plane |
| 648 → 690 | Plenum reserve, Phase 2 — **not frozen (ICR-004)** |

No service may claim depth without checking this table.

## 3. Tier geometry and the bed datum

Four tiers. Bed datums at **300 / 700 / 1100 / 1500 mm**. Pitch 400 mm.

**The bed datum is the top face of the deck mesh panel.** Not the beam, not the
deck rail, not the tray floor.

| Element | Z range, first tier |
|---|---|
| Beam | 243.4 – 273.4 |
| Deck rail | 273.4 – 298.4 |
| Deck mesh panel | 298.4 – **300.0** |
| Tray | from 300.0 |

Every downstream elevation — nozzle height, LED hanging height, drain fall,
overflow collar — is measured from this datum and no other. Changing the deck
build-up changes every bed datum; it is a frozen interface, not a detail.

**Four tiers is the maximum.** A fifth tier at 1900 mm is ruled out: the NIOSH
revised lifting equation gives RWL = 0 above 1750 mm (EDR-002). Any taller
variant requires a handling aid, not a re-argument.

## 4. Materials and structure

| Item | Specification |
|---|---|
| Frame and decks | GI to IS 4923, YST210 grade, **Z275** coating |
| Deck mesh | ≥70 % open expanded mesh, effective density 1884 kg/m³, 1.98 kg/panel |
| Seismic | Per IS 1893 |
| Wall anchors | Present from platform Rev H |
| Base frame | Raised for cleaning clearance (platform Rev H) |

The deck mesh density figure is load-bearing: it is the correction that took
rack mass from 147.67 kg to 112.66 kg and therefore changes floor loading,
anchor sizing and room point loads (EDR-004).

## 5. Facility interface (A ↔ C)

| Parameter | Requirement on the facility |
|---|---|
| Floor | Must carry the rack point loads at 112.66 kg dry plus flooded bed mass. Verified for the Ooty room, `RK-A-ROOM` Rev 4 §08 |
| Wall fixings | Required — the rack is anchored, not free-standing |
| Ceiling height | Must clear 1960 mm plus service access above |
| Set-out pitch | At the installed 690 mm depth |

## 6. Plenum interface — NOT FROZEN

The rack-to-plenum mechanical interface is **open** (ICR-004). 42 mm of depth
is reserved between the Phase-1 build (648 mm) and the installed envelope
(690 mm), but no mounting provision is specified.

Phase-1 racks therefore cannot be guaranteed plenum-ready. This must be decided
before the Phase-1 fabrication release, not before the plenum design — the
constraint lands on the racks that get built first.

## 7. Held parts

Specified but excluded from the Rev 2 structural drawing set:

| Part | Description |
|---|---|
| `RK-A-301` | LED mounting rail |
| `RK-A-501` | Reflective panel, rear |
| `RK-A-502` | Reflective panel, side |
