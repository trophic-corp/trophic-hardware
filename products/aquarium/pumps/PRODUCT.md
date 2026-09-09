# PRODUCT — Pumps (`AQ-PU-A`)

| | |
|---|---|
| **Product ID** | `AQ-PU-A` |
| **Family** | Aquarium / Aquascaping |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no engineering** |
| **Authoritative CAD** | None |

---

## 1. What the product is

Circulation and return pumps for planted aquariums — powerheads, wavemakers, and filter return pumps.

## 2. Why it exists

Pumps are the component most likely to be shared across the aquarium range: filtration needs one, CO₂ reactors benefit from one, and circulation is a product in its own right. Deciding it once, deliberately, is worth more than three separate procurement decisions.

## 3. Inherited constraints — DECIDED

**None.** No Trophic decision has been made about this product. It inherits the
identifier standard and, where it is an electronic device, the principle that a
device must be safe with no power and no signal. Nothing else.

## 4. Industry reference points — NOT TROPHIC DECISIONS

Typical market values, to bound the design space. **Not specifications. No drawing may
cite this section.**

| Item | Typical range | Note |
|---|---|---|
| Types | Submersible powerhead, external return, controllable wavemaker | Controllability is the current market differentiator |
| Voltage | 24 V DC controllable is displacing AC synchronous | A DC pump is controllable; an AC one is on or off |
| Control | PWM or proprietary bus | If controllable, it should speak the platform capability vocabulary |
| Ingress | Fully submersible | The defining environmental requirement |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | Make or buy — pumps are a mature commodity with strong incumbents | Whether this is a product at all |
| 2 | Type and duty range | Everything |
| 3 | Controllable or fixed-speed | Whether `AQ-CT-A` has anything to control |
| 4 | Whether `AQ-FL-A` uses this pump or a bought-in one | Coupling between two products |
| 5 | Motor: synchronous AC or brushless DC | Efficiency, noise, controllability, cost |

## 6. Explicitly not decided

Nothing. **Do not assume the CEA pump work transfers.** `P-02` is a 25 L/min,
0.75 kW surface pump lifting 4.76 m on a terrace. An aquarium powerhead shares the
word "pump" and nothing else.

No dimensions, no materials, no BOM, no cost, no performance figures of any kind.

## 7. Interfaces

Platform **mechanical** standards do not apply — they are written for fabricated steel
structural products. Platform **electrical** standards apply only in principle
(fail-safe, connector discipline); the CEA mains protection schedule does not.

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No** |
| Honest assessment | Decision 1 may well be "buy". Modelling before answering it risks designing a product that should never have been designed |

## 9. Next action

Answer decision 1 (make or buy) before any engineering effort. It is the highest-leverage question in the aquarium family.
