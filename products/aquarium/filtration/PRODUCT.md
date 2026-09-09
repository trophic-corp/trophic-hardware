# PRODUCT — Filtration (`AQ-FL-A`)

| | |
|---|---|
| **Product ID** | `AQ-FL-A` |
| **Family** | Aquarium / Aquascaping |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no engineering** |
| **Authoritative CAD** | None |

---

## 1. What the product is

Filtration for planted aquariums — canister, hang-on-back, or in-tank, plus the media that goes in it.

## 2. Why it exists

Filtration is the highest-value, highest-complexity product in the aquarium range and the one furthest from current competence. Trophic has real experience of **water treatment at CEA scale** — filtration, UV disinfection, and an eight-condition reuse gate — but none of that transfers directly to a 200 L display tank with a biological population.

## 3. Inherited constraints — DECIDED

**None.** No Trophic decision has been made about this product. It inherits the
identifier standard and, where it is an electronic device, the principle that a
device must be safe with no power and no signal. Nothing else.

## 4. Industry reference points — NOT TROPHIC DECISIONS

Typical market values, to bound the design space. **Not specifications. No drawing may
cite this section.**

| Item | Typical range | Note |
|---|---|---|
| Types | Canister, hang-on-back, internal | Canister is the aquascaping default |
| Turnover | Roughly 4–10× tank volume per hour | A design target range, not a specification |
| Media | Mechanical / biological / chemical stages | Media is often the recurring-revenue half of the product |
| Hose sizes | 12/16 mm and 16/22 mm | Must match `AQ-LP-A` — see below |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | Type: canister, HOB, or internal | Everything. These are three different products |
| 2 | Tank volume range served | Pump duty, media volume, body size |
| 3 | Whether media is a Trophic product or a consumable it accepts | Business model as much as design |
| 4 | Pump: bought in, or `AQ-PU-A` | Whether two products in this family are coupled |
| 5 | Priming and maintenance workflow — the thing owners actually complain about | Body design, seals, valve block |
| 6 | Hose size, which must match `AQ-LP-A` | Cross-product interface |

## 6. Explicitly not decided

Nothing. **The CEA water skid is not a starting point.** Gate logic sized for a 46 L
recovery batch against a 79 L trough has no bearing on a display tank, and reusing its
figures would be a category error.

No dimensions, no materials, no BOM, no cost, no performance figures of any kind.

## 7. Interfaces

Platform **mechanical** standards do not apply — they are written for fabricated steel
structural products. Platform **electrical** standards apply only in principle
(fail-safe, connector discipline); the CEA mains protection schedule does not.

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **No.** Type and tank volume are both open, and they determine form completely |

## 9. Next action

Decide 1 (type). Then decide 6 (hose size) — because it is the one cross-product
interface in this family, and if `AQ-LP-A` and `AQ-FL-A` settle it independently they
will settle it differently.
