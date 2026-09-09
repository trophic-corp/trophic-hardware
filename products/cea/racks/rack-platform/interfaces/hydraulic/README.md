# Interface Specification — Hydraulic

**Interface ID:** `IF-RK-A-HYD`
**Between:** A — Rack product · B — Shared CEA infrastructure
**Authority:** `RK-A-SYS` Rev 2, `RK-A-WRS` Rev 3
**Related decisions:** ADR-001, EDR-005, EDR-006, ICR-001, ICR-002, ICR-003

---

## 1. Scope of the interface

The rack's hydraulic responsibility begins at the **rack inlet** and ends at the
**rack drain header outlet**. Everything upstream of the inlet and downstream of
the outlet belongs to shared CEA infrastructure (ICR-003).

```
  terrace source tank  ──┐   (B)
        gravity main     │
                    ┌────▼────┐
                    │ RACK    │   inlet  ◄── interface point 1
                    │ INLET   │
                    ├─────────┤
                    │  tiers  │   (A) — rack internal, not an interface
                    ├─────────┤
                    │ DRAIN   │
                    │ HEADER  │   outlet  ◄── interface point 2  (Z 200)
                    └────┬────┘
                         ╎  100 mm AIR GAP — must never be plumbed closed
                    ┌────▼────┐
                    │ tundish │   rim at Z 100          (B)
                    └────┬────┘
                  common drain → sump trough → recovery pump → terrace
```

---

## 2. Interface point 1 — rack inlet

| Parameter | Value | Note |
|---|---|---|
| Supply type | **Gravity** | No supply pump exists (EDR-005) |
| Source outlet elevation | +4250 mm | Terrace slab +3750 + 500 mm plinth |
| Reference point | Top nozzle at +1590 mm | |
| Static head available | **2.66 m** | |
| Design flow, single tier | 7.2 L/min | |
| Rack-side loss at design flow | 0.33 m | See §3 |
| Four tiers concurrent | 28.8 L/min at 0.67 m | Passes |
| **Flow ceiling** | **~15 L/min** | Head is exhausted beyond this |
| Pipework | uPVC to IS 4985 | |

**Constraint on infrastructure (B):** the source outlet elevation of +4250 mm
is a hard facility requirement. Lowering it invalidates the head budget.

**Constraint on the rack (A):** no change may increase rack-side loss beyond the
head budget. Nozzle count, tier concurrency and solenoid Kv are all
head-critical — there is no pump to absorb an increase.

## 3. Head budget

Hazen-Williams, C = 150, at 7.2 L/min:

| Element | Loss (m) |
|---|---|
| DN32 main | 0.028 |
| DN25 riser | 0.012 |
| DN20 drop | 0.023 |
| DN20 solenoid, Kv 4 | **0.119** |
| Fittings | 0.150 |
| **Total** | **0.33** |

Available 2.66 m against required 0.33 m — margin ≈ **8×**.

The DN20 solenoid is the single largest rack-side loss. Substituting a
lower-Kv valve consumes margin disproportionately and must be recalculated,
not assumed equivalent.

---

## 4. Interface point 2 — rack drain header outlet

| Parameter | Value |
|---|---|
| Outlet elevation | **Z 200 mm** |
| Nominal size | DN50 |
| Tundish rim elevation | Z 100 mm |
| **Air gap** | **100 mm = 2 × DN50** |
| Standard | IS 12234 / EN 1717 |

### The air gap is safety-critical

The 100 mm gap is the only physical barrier preventing used bed water from
reaching the source in a closed loop. **It must never be plumbed closed** — not
by revision, not by site modification, not by a temporary hose.

Because the gap sits exactly on the A/B ownership boundary, **neither owner may
close it**, and neither may assume the other is maintaining it. It is verified
physically at installation, not from drawings (see `VERIFICATION_INDEX.md` §3).

The drain chain is continuous joint-by-joint from every tray outlet to the
outlet at Z 200, and then deliberately discontinuous. A reader of the model must
not mistake the gap for a modelling omission.

---

## 5. Rack-internal drain chain (informative, not an interface)

Established by ICR-001. Listed here because its continuity is what makes the
interface valid:

`tray floor` → `09_TRAY_OUTLET` → `09_TRAY_STRAINER` → `09_OVF_BULKHEAD` →
moulded overflow collar (Z 300–330) → `09_OVF_V` vertical drop (Z 160–300) →
branch → rack drain header → outlet (Z 200).

Tray `RK-A-401` carries the moulded features: `boss_y = 480`, `ovf_x = 120`,
`ovf_dia = 32`, `collar_h = 30`.

---

## 6. Fail-safe positions at the interface

| Device | Owner | Fail state |
|---|---|---|
| Fill solenoids | A — rack | Normally **CLOSED** |
| Drain solenoids | A — rack | Normally **OPEN** |
| Recovery diverter `FV-01` | B — infrastructure | Spring-return **TO WASTE** |
| Terrace master valve `MV-01` | B — infrastructure | Fails **CLOSED** |

Aggregate failure state: beds drain by gravity, supply isolates, recovery
discards. See EDR-007.

---

## 7. Reserved space

The wet-services corridor at **Y 435 – 525 mm** from the rack front face is
reserved exclusively for irrigation and drainage (EDR-003). No other service may
claim depth in it.
