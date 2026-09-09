# PRODUCT — Aquarium Sensor / Controller (`AQ-CT-A`)

| | |
|---|---|
| **Product ID** | `AQ-CT-A` |
| **Family** | Aquarium / Aquascaping |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no engineering** |
| **Authoritative CAD** | None |

---

## 1. What the product is

A controller for planted aquariums: monitors water parameters, schedules lighting and CO₂, and drives dosing.

## 2. Why it exists

The CEA suite's capability model (ADR-0002) was written so this family integrates with **no new platform work** — a tank light is `light.dim` + `light.schedule`, a dosing pump is `dosing.*`. That claim is currently untested. This product is the test.

## 3. Inherited constraints — DECIDED

**None.** No Trophic decision has been made about this product. It inherits the
identifier standard and, where it is an electronic device, the principle that a
device must be safe with no power and no signal. Nothing else.

## 4. Industry reference points — NOT TROPHIC DECISIONS

Typical market values, to bound the design space. **Not specifications. No drawing may
cite this section.**

| Item | Typical range | Note |
|---|---|---|
| Parameters sensed | Temperature, pH, TDS/EC; sometimes ORP | pH is the CO₂ control variable in planted tanks |
| Probe standard | BNC probes are near-universal | Interchangeable probes are an expectation, not a differentiator |
| Control outputs | Switched mains sockets and/or low-voltage | Determines whether this is a mains product |
| Connectivity | Wi-Fi with app is the current market baseline | CEA is wired-first for a reason that does not apply to a living room |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | Mains switching, or low-voltage only | Whether the entire CEA electrical standard applies |
| 2 | Parameter set and probe types | Enclosure, IO, calibration workflow |
| 3 | Standalone product, or the hub of an `AQ-*` system | Scope, and whether the other products need it |
| 4 | Connectivity and whether it touches the Trophic platform at all | Software scope — a decision that must not be made here alone |
| 5 | Calibration workflow — probes drift and users are not lab technicians | UX, enclosure, firmware |
| 6 | Fail-safe behaviour: what happens to a heater, a CO₂ solenoid, a dosing pump on power loss | Safety. Decide this first, as CEA did |

## 6. Explicitly not decided

Nothing. In particular, **do not assume this product shares firmware, bus or
enclosure with `CT-A`** — that would be a real decision with real consequences, and
nobody has made it.

No dimensions, no materials, no BOM, no cost, no performance figures of any kind.

## 7. Interfaces

Platform **mechanical** standards do not apply — they are written for fabricated steel
structural products. Platform **electrical** standards apply only in principle
(fail-safe, connector discipline); the CEA mains protection schedule does not.

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No.** Mains vs low-voltage alone changes the enclosure entirely |
| What to do instead | Settle decision 6 (fail-safe) on paper. It costs nothing and it is what CEA got right |

## 9. Next action

Decide 1 (mains or low-voltage). It gates which safety standards apply, and therefore most of the engineering effort.
