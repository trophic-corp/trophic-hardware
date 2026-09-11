# platform/lighting — common lighting area

Reusable engineering, manufacturing and commercial knowledge for **all Trophic
lighting**: aquarium (`AQ-LT-A` Core, `AQ-LT-B` WRGB, Smart Module) and CEA
(`LT-A`). It does **not** merge the product requirements; those stay in each
product's `PRODUCT.md`. This folder holds what is shared, and an index to the
shared material that already lives elsewhere so nothing is duplicated.

| Topic | Where it lives | Status |
|---|---|---|
| **Platform architecture** (Light Engine / Smart Module boundary, tiers, what is shared) | ADR-008 (`docs/decisions/records/`), `products/aquarium/lighting/PLATFORM.md` | Proposed / planning |
| **Control interface** (engine port, protocol concept, fail-safe state machine) | `electronics/LIGHT_ENGINE_CONTROL_INTERFACE.md` | Concept, ICR-governed once frozen |
| **Electronics reference** (LED engines, drivers, PSU and bus-voltage research, MCU/radio, RTC, standards) | `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` Parts A–C | Research |
| **Biology** (microgreens, planted aquaria) | same reference, Part D | Research |
| **LED, extrusion, MCPCB, EMS, adapter, connector, lab suppliers** by Coimbatore / India / import tier | `docs/references/suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md` | Vendor source, nothing qualified |
| **Product sourcing implications** | each product's `sourcing/SOURCING_STRATEGY.md` | Phase 0A |
| **Competitors, Indian prices, warranty norms** | `docs/references/lighting/COMPETITOR_LIGHTING_REFERENCE.md` | Research |
| **BOM, unit cost by volume, pricing, contribution, programme cash** | `costing/lighting_cost_model.py` → `costing/LIGHTING_BOM_COST_MODEL.md` | Planning model, not commercial truth |
| **Prototype, EVT/DVT, pilot and first-batch plan** | `manufacturing/LAUNCH_PLAN.md` | Proposal |
| **Phases, gates, test categories, supplier qualification, warranty evidence** | `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md` | Framework |
| **Thermal, optical and MCPCB design principles** | reference Part A (fundamentals) and B1 (CEA bar analysis) | Reference |
| **Compliance considerations** (BIS, WPC, IEC 62471, EMC) | reference B4 and C2; roadmap §4 | Research, RESEARCH REQUIRED items open |
| **Common components** (adapter family, connector, MCU/radio module, RTC) | reference B4 and C3; will become platform standards when decided | Not decided |

## Rules for this folder

1. It holds **shared** knowledge and planning models. A product-specific requirement or decision goes in the product's `PRODUCT.md` or a decision record, not here.
2. The cost model is generated from `costing/lighting_cost_model.py`; edit the labelled assumption blocks and regenerate. Do not hand-edit the generated markdown. When a supplier quotation arrives, change the line's evidence class to `QUOTE` and record the date.
3. Nothing here is a standard until a decision record says so. When the engine port, the adapter family or the connector are decided, they move into `platform/electrical-standards/` or an ICR-governed interface specification, and this index points there.
4. `LT-A` shares the knowledge (LED sourcing, MCPCB process, thermal principles, test jigs, dimming maths) and **not** the aquarium hardware (port, module, adapter, connector); see PLATFORM.md §11 #10.
