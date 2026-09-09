# PRODUCT — Lily Pipes (`AQ-LP-A`)

| | |
|---|---|
| **Product ID** | `AQ-LP-A` |
| **Family** | Aquarium / Aquascaping |
| **Owner class** | A — Product |
| **Stage** | **Phase 0 — no engineering** |
| **Authoritative CAD** | None |

---

## 1. What the product is

Glass or acrylic inlet and outlet pipes for planted aquariums — the visible plumbing between a canister filter and the tank, valued as much for appearance as for flow.

## 2. Why it exists

The lowest-technology product in the range and the one most dependent on manufacturing skill rather than design. It is also the clearest test of whether Trophic can make something in a material it has never worked: every other product in both families is steel, plastic or electronics.

## 3. Inherited constraints — DECIDED

**None.** No Trophic decision has been made about this product. It inherits the
identifier standard and, where it is an electronic device, the principle that a
device must be safe with no power and no signal. Nothing else.

## 4. Industry reference points — NOT TROPHIC DECISIONS

Typical market values, to bound the design space. **Not specifications. No drawing may
cite this section.**

| Item | Typical range | Note |
|---|---|---|
| Hose sizes | 12/16 mm and 16/22 mm ID/OD | Two sizes cover most canister filters. This is a real compatibility constraint |
| Material | Borosilicate glass; acrylic as the durable alternative | Glass is the aesthetic standard and the breakage complaint |
| Rim thickness accommodated | Rimless tanks, typically 5–12 mm glass | Determines the hook geometry |
| Forms | Inflow with strainer; outflow as spin/violet/poppy type | Named market forms, not Trophic designs |

## 5. Open — must be decided before CAD

| # | Decision required | Blocks |
|---|---|---|
| 1 | Glass or acrylic — this is the whole product | Process, tooling, supplier, cost, failure mode |
| 2 | Hose sizes supported | Every dimension |
| 3 | Tank rim thickness range | Hook geometry |
| 4 | Outflow form(s) | The visible design, which is what sells it |
| 5 | Manufacture: in-house glasswork, or a specialist supplier to Trophic design | Whether this is a manufacturing product or a design-and-source product |
| 6 | Packaging — the product is fragile and returns are expensive | Cost, and it is usually an afterthought |

## 6. Explicitly not decided

Nothing. **Do not infer dimensions from any competitor product.** A generated model
that happens to match a market part is a copy, not a design.

No dimensions, no materials, no BOM, no cost, no performance figures of any kind.

## 7. Interfaces

Platform **mechanical** standards do not apply — they are written for fabricated steel
structural products. Platform **electrical** standards apply only in principle
(fail-safe, connector discipline); the CEA mains protection schedule does not.

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | **Massing only, and only after decisions 2 and 3** — hose size and rim thickness are the two dimensions everything else hangs from |
| Good for | Visualising a form language, discussing proportion |
| Must NOT be inferred | Wall thickness, bend radii, strainer geometry, manufacturability. Glass has forming constraints that a CAD model will not respect on its own |

## 9. Next action

Decide 1 (glass or acrylic). Nothing else can be usefully discussed until it is settled — the two materials share almost no design logic.
