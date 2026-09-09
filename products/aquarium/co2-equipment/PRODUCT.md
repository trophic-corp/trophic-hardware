# PRODUCT — CO₂ Equipment (`AQ-CO-A`)

| | |
|---|---|
| **Product ID** | `AQ-CO-A` |
| **Family** | Aquarium / Aquascaping |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no engineering** |
| **Authoritative CAD** | None |

---

## 1. What the product is

CO₂ injection equipment for planted aquariums: regulator, solenoid, bubble counter, check valve, and diffuser or reactor.

## 2. Why it exists

CO₂ is what separates a planted tank from a decorative one, and the equipment is where most hobbyists have a bad experience — end-of-tank dumps, drifting rates, failed check valves. It is also the only aquarium product with a **genuine safety dimension**, and the one place CEA experience transfers honestly.

## 3. Inherited constraints — DECIDED

**None.** No Trophic decision has been made about this product. It inherits the
identifier standard and, where it is an electronic device, the principle that a
device must be safe with no power and no signal. Nothing else.

## 4. Industry reference points — NOT TROPHIC DECISIONS

Typical market values, to bound the design space. **Not specifications. No drawing may
cite this section.**

| Item | Typical range | Note |
|---|---|---|
| Cylinder connections | CGA320, DIN477, and regional variants | A real compatibility constraint that varies by market |
| Working pressure | Regulated output typically 1–2 bar | Diffuser dependent |
| Control | Solenoid on a timer, or pH-controlled | pH control closes the loop and needs `AQ-CT-A` |
| Diffusion | Ceramic diffuser, inline reactor, or inline atomiser | Inline suits a canister system |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | Product scope: full kit, or individual components | Everything |
| 2 | Cylinder standard(s) supported — market-specific | Regulator design |
| 3 | Solenoid **fail state** — and it must be CLOSED | Safety. Decide it first and write it down |
| 4 | End-of-tank-dump protection: dual-stage regulator or accept single-stage | Cost against the failure hobbyists most complain about |
| 5 | pH-controlled or timer-only | Whether `AQ-CT-A` is required |
| 6 | Diffusion method | Whether this couples to `AQ-FL-A` |

## 6. Explicitly not decided

Nothing about the equipment itself. But one thing **is** already decided in
principle, and should not be re-litigated:

**The CO₂ solenoid fails CLOSED.** The CEA design does this (`co2_safety_alarm_ppm`
5000 with a fail-closed solenoid, cylinder sited outside the occupied space) and the
reasoning is not scale-specific: a stuck-open CO₂ valve is dangerous to fish in a tank
and to people in a room. It is the same failure with different casualties.

CEA also records that a 22 kg cylinder released into a 60.2 m³ room produces roughly
12 m³ of gas — lethal well before it is noticed. A domestic room is smaller than
60.2 m³. **This deserves an explicit safety assessment before the product ships**, not
an assumption that hobby scale is inherently safe.

No dimensions, no materials, no BOM, no cost, no performance figures of any kind.

## 7. Interfaces

Platform **mechanical** standards do not apply — they are written for fabricated steel
structural products. Platform **electrical** standards apply only in principle
(fail-safe, connector discipline); the CEA mains protection schedule does not.

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No.** Cylinder standard and scope are both open |
| What to do first | Decisions 3 and 4 are safety decisions that cost nothing to make now and get expensive to change later |

## 9. Next action

Write down the fail-safe behaviour (decision 3) and settle end-of-tank-dump
protection (decision 4). Both are safety decisions available today at zero
engineering cost.
