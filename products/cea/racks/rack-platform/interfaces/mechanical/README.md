# Interface Specification — Mechanical

**Interface ID:** `IF-RK-A-MEC`
**Between:** A — Rack product · C — Facility · and the deferred plenum entity
**Authority:** `RK-A-DWG` Rev 3, `RK-A-SYS` Rev 2 + addendum B, `RK-A-QC` Rev 4
**Related decisions:** EDR-001, EDR-002, EDR-003, EDR-004, EDR-014, EDR-015, EDR-017, EDR-018, ICR-004, ICR-006
**Revision:** 2 (2026-09-10, ECP-01)

---

## 1. Envelope

| Envelope | W × D × H (mm) | Applies to |
|---|---|---|
| **Installed** | 1456 × **690** × 1960 | Room set-out, clearance planning |
| Structure only | 1256 × 563 × 1960 | Fabrication |
| Phase-1 build (no plenum) | 1456 × **690** × 1960 | Fans, drain header and tundish occupy the rear zone from Phase 1; the 648 figure is withdrawn |

**Room set-out uses the installed 690 mm depth even for Phase-1 racks** so the
plenum can be retrofitted without moving racks. Confirming this is ND-04.

| Property | Value |
|---|---|
| Dry mass | **136.39 kg** (all systems, fixture envelopes 1.18 kg); Core 91.7 · Grow Phase 1 108.0 · Grow complete 126.9 kg — see RK-A-QC Rev 4 T18 |
| Parts / occurrences | 70 / 417 |
| Height limit rationale | Reach-limited, see §3 |

## 2. Depth allocation (from the front face)

| Y range (mm) | Allocation |
|---|---|
| 148 – 208 | LED row 1, fixture body |
| 352 – 412 | LED row 2, fixture body |
| **435 – 525** | **Wet services corridor — in-bed drain hardware, reserved (EDR-003)** |
| 500 – 540 (Z 190–230 + 400·n) | Drain lateral runs to the crossing window at X 1040–1080 (ICR-006) |
| 525 – 559 | Tier cable trays (X 110–1030) |
| 560 – 563 | Rear gusset plates `RK-A-107B` (EDR-015) |
| 563 – 569 | Rear brace bars A and B (EDR-018) |
| 569 – 571 | Rear panel `RK-A-501` |
| 571 → 690 | Rear service zone: Phase-1 fans (X 1150–1188), drain header X 1200–1250 / Y 575–625, laterals at Y 580–620 and 623–655, tundish X 1180–1270 / Y 570–660; **plenum reserve X ≤ 1150 between the lateral windows — not frozen (ICR-004)** |
| −3 – 0 | Front gusset plates `RK-A-107B` (protrude 3 mm into the aisle) |

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
| Joints | `RK-A-107B` 3 mm gusset plates, M8 rivet nuts (near wall), crush tubes; 18 N·m; 4 N·m for any M8 through a section without a tube (EDR-015) |
| Cross beams | `RK-A-103` × 10 — full rectangle at every level (EDR-014); decks non-structural |
| Anchors | `RK-A-106B` telescoping strut, 90–320 mm, wall (M10) or partner foot (EDR-017) |
| Base frame | Raised for cleaning clearance (platform Rev H); `RK-A-108` foot inserts; upright drain holes Z 55 |

The deck mesh density figure is load-bearing: it is the correction that took
rack mass from 147.67 kg to 112.66 kg and therefore changes floor loading,
anchor sizing and room point loads (EDR-004).

## 5. Facility interface (A ↔ C)

| Parameter | Requirement on the facility |
|---|---|
| Floor | Must carry the rack point loads at 136.4 kg dry plus flooded bed mass (288 kg loaded; 331 kPa on a Ø50 foot, 65 kPa on the 100 × 100 pad). `RK-A-ROOM` Rev 4 §08 figures at 112.7 kg are to be restated (+21 %) |
| Wall fixings | Required — `RK-A-106B` strut to wall (Row A, 127 mm stand-off, M10) or to the partner rack (rows B/C, 254 mm) |
| Ceiling height | Must clear 1960 mm plus service access above |
| Set-out pitch | At the installed 690 mm depth |

## 6. Plenum interface — NOT FROZEN

The rack-to-plenum mechanical interface is **open** (ICR-004). The plenum reserve is Y 571–690, X 110–1150, in four tier bands, with the drain/overflow laterals crossing between the bands at Z 190–230, 544–576, 590–630, 944–976, 990–1030, 1344–1376, 1390–1430 (and 182–214 for the tier-1 overflow). No mounting provision is specified.

Phase-1 racks therefore cannot be guaranteed plenum-ready. This must be decided
before the Phase-1 fabrication release, not before the plenum design — the
constraint lands on the racks that get built first.

## 7. Held parts

Specified but excluded from the Rev 2 structural drawing set:

| Part | Description |
|---|---|
| `RK-A-301` | LED mounting rail — **released in Rev 3 at 1172 mm** |
| `RK-A-501` | Reflective panel, rear (now Y 569–571) — held |
| `RK-A-502` | Reflective panel, side — held |
