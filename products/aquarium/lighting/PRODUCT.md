# PRODUCT — Programmable Aquarium Light (`AQ-LT-A`)

| | |
|---|---|
| **Product ID** | `AQ-LT-A` |
| **Family** | Aquarium / Aquascaping |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no engineering** |
| **Authoritative CAD** | None |

---

## 1. What the product is

A programmable LED light for planted aquariums and aquascapes, with scheduled photoperiod, dimming, and per-channel spectrum control.

## 2. Why it exists

It is the product with the most overlap with existing Trophic competence. `LT-A` (CEA grow bar) solves a closely related problem — driving LEDs to a defined optical target with 0–10 V dimming and remote drivers — and the CEA suite's capability model already anticipates this device class explicitly.

**Worth checking before starting:** whether `AQ-LT-A` and `LT-A` should share a driver
platform and optical toolchain. If yes, `LT-A`'s open decision 1 (driver model) should
be made with this product in view. If no, say so explicitly — an unexamined
assumption of sharing is how two products end up compromised for each other.

## 3. Inherited constraints — DECIDED

**None.** No Trophic decision has been made about this product. It inherits the
identifier standard and, where it is an electronic device, the principle that a
device must be safe with no power and no signal. Nothing else.

## 4. Industry reference points — NOT TROPHIC DECISIONS

Typical market values, to bound the design space. **Not specifications. No drawing may
cite this section.**

| Item | Typical range | Note |
|---|---|---|
| Tank lengths served | 30 / 45 / 60 / 90 / 120 cm | Standard aquarium footprints; a light family usually spans several |
| Mounting | Rimless clamp, rail/leg stand, or suspension | Rimless glass is the aquascaping norm; rim thickness varies |
| Ingress | Splash-resistant to immersion-rated | Above-water fixture; condensation and salt creep are the real problems |
| Channels | Fixed white through 4–5 channel tunable | Aquascaping buyers expect tunable; a fixed spectrum is a positioning decision |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | Product positioning: hobby aquascaping, or professional/retail display | Everything — cost, finish, channel count |
| 2 | Tank size range the family covers | Length, output, family structure |
| 3 | Channel count and spectrum | Optics, driver, control |
| 4 | Mounting system: clamp, stand, or suspension | The entire mechanical design |
| 5 | Ingress rating and how condensation is handled | Sealing, materials |
| 6 | Control: onboard schedule, app, or `AQ-CT-A` integration | Whether this is a standalone product or part of a system |
| 7 | Whether it reuses `LT-A` driver and optical work | Development cost, and whether the two products share a platform |

## 6. Explicitly not decided

Nothing. This product has never been specified.

No dimensions, no materials, no BOM, no cost, no performance figures of any kind.

## 7. Interfaces

Platform **mechanical** standards do not apply — they are written for fabricated steel
structural products. Platform **electrical** standards apply only in principle
(fail-safe, connector discipline); the CEA mains protection schedule does not.

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No.** Length, mounting and channel count are all open, and they determine the entire form |
| What would make it possible | Answering decisions 2 and 4 — tank size range and mounting system |

## 9. Next action

Decide positioning (decision 1). Every other decision in §5 follows from it, and it is a business question, not an engineering one.
