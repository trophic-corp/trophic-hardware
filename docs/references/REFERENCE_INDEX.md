# Reference Index

Reference and research material used by Trophic hardware engineering.

**Large historical research documents stay outside default context.** This index
exists so they can be found without being loaded. Load a reference only when the
question you are answering actually requires it.

**Status values:** `RESEARCH` · `REFERENCE ONLY` · `VENDOR SOURCE` ·
`TEST EVIDENCE` · `HISTORICAL` · `SUPERSEDED`

---

## 1. Standards

| ID | Title | Location | Purpose | Relevant product/system | Authority | Status |
|---|---|---|---|---|---|---|
| STD-01 | IS 4923 — Hollow steel sections | External standard | Frame section specification, YST210 grade, Z275 coating | `RK-A` structure | Statutory / normative | REFERENCE ONLY |
| STD-02 | IS 3043 — Code of practice for earthing | External standard | Earthing design and test | `RK-A`, `RK-A-ROOM` electrical | Statutory / normative | REFERENCE ONLY |
| STD-03 | IS 1893 — Criteria for earthquake resistant design | External standard | Seismic loading on racks and anchors | `RK-A` structure, `RK-A-ROOM` | Statutory / normative | REFERENCE ONLY |
| STD-04 | IS 4985 — uPVC pipes for potable water supplies | External standard | Pipework specification | `RK-A` irrigation, `RK-A-WRS` | Statutory / normative | REFERENCE ONLY |
| STD-05 | IS 732 — Code of practice for electrical wiring installations | External standard | Installation, inspection and testing | `RK-A`, `RK-A-ROOM` electrical | Statutory / normative | REFERENCE ONLY |
| STD-06 | IS 12234 / EN 1717 — Backflow protection | External standard | Air gap classification and sizing | `RK-A` drainage, `RK-A-WRS` | Statutory / normative | REFERENCE ONLY |

## 2. Engineering methods and published data

| ID | Title | Location | Purpose | Relevant product/system | Authority | Status |
|---|---|---|---|---|---|---|
| REF-01 | NIOSH revised lifting equation | Published method | Reach and lift limits; basis for rejecting a fifth tier | `RK-A` ergonomics | Peer-reviewed method | REFERENCE ONLY |
| REF-02 | Hazen-Williams formula, C = 150 for uPVC | Published method | Gravity supply head-loss calculation | `RK-A` irrigation, `RK-A-WRS` | Established method | REFERENCE ONLY |
| REF-03 | Standard atmosphere pressure vs altitude | Published data | Suction-lift limits: Ooty 2,240 m → 77.2 kPa (7.87 m water); Coimbatore 411 m → 96.5 kPa (9.84 m) | `RK-A-WRS` pump architecture | Established data | REFERENCE ONLY |
| REF-04 | Published CFD on grow-rack airflow uniformity | External literature | Velocity uniformity: point-source fan CV ≈ 33 %, ducted plenum CV ≈ 10 % | `RK-A` ventilation, plenum | Third-party literature | RESEARCH |
| REF-05 | UV-C degradation of chelated iron | Horticultural literature | Fe-EDTA degrades under UV-C; Fe-DTPA / Fe-EDDHA required | `RK-A-WRS` nutrient management | Third-party literature | RESEARCH |
| REF-06 | Expanded metal mesh effective density | Material data | ≥70 % open mesh → 1884 kg/m³ effective; basis for the mass correction | `RK-A` deck panels | Vendor / material data | VENDOR SOURCE |

## 2a. Lighting program references (added 2026-09-11)

| ID | Title | Location | Purpose | Relevant product/system | Authority | Status |
|---|---|---|---|---|---|---|
| LREF-01 | Lighting Platform Reference | `lighting/LIGHTING_PLATFORM_REFERENCE.md` | Part A durable fundamentals (units, LED physics, MCPCB, control, optics, environment). Part B LED engines: B1 CEA fixed-spectrum bar hardware incl. the 48 V remote-driver readings and OCV hazard, B2 aquarium Core engine classes, B3 WRGB architectures and UVA assessment, B4 shared control electronics and Indian radio/BIS notes. Part C power platform: 24/36/48 V derivation, adapter availability, BIS scope, PSU-family standardisation, fixture protection. Part D biology: D1 microgreens (fixed vs tunable, PPFD/DLI, photoperiod, trial protocol), D2 planted aquaria (PAR, attenuation, spectrum, algae, UVA, trial protocol). **Answers most "what does the science or the datasheet say" questions for all three lights** | `LT-A`, `AQ-LT-A`, `AQ-LT-B` | Peer-reviewed, datasheets, standards summaries, inference (labelled) | RESEARCH (Part A REFERENCE ONLY) |
| LREF-02 | Competitor Lighting Reference | `lighting/COMPETITOR_LIGHTING_REFERENCE.md` | Neo Helios, Chihiros, Week Aqua, Twinstar, ONF, ADA and others: family architecture, channels, controls, PSU rails, controller placement, ingress, warranty, Indian prices (dated 2026-09-11), field complaints, cross-brand patterns, lessons. Not requirements | `AQ-LT-A`, `AQ-LT-B` | Manufacturer, distributor, retailer, community (labelled) | RESEARCH |
| VEN-02 | Lighting Supplier Landscape | `suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md` | Coimbatore / Tamil Nadu-India / import tiers for extrusion, anodise, machining, end caps, gaskets, harness, packaging, EMS, MCPCB, drivers, adapters, optics, connectors, distributors, test labs; cost classes; supply events (Samsung exit, Lumileds, ams OSRAM, Cree); duty pointers; dual-sourcing map; research-required list. **No supplier is qualified** | `LT-A`, `AQ-LT-A`, `AQ-LT-B` | Website claims, directory listings, manufacturer partner lists (labelled) | VENDOR SOURCE |

Product-specific sourcing implications are in each product's `sourcing/SOURCING_STRATEGY.md`, not here. The program roadmap and phase-gate evidence are in `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md`.

## 3. Historical and superseded material

| ID | Title | Location | Purpose | Relevant product/system | Authority | Status |
|---|---|---|---|---|---|---|
| HIST-01 | CEA Room Scaling Study Rev 1 | `archive/superseded/RK-R-01_Rev1_cea-room-scaling-study.html` | Earlier room capacity study; superseded by `RK-A-ROOM` Rev 4 | `RK-A-ROOM` | Internal, superseded | SUPERSEDED |
| HIST-02 | Rack A Part Drawings, diverged local build | `archive/superseded/RK-A-DWG_local-build_DIVERGED-from-published-Rev1.html` | Holds Rev 2 content against a published Rev 1. **Unresolved — ND-01** | `RK-A` | Contested | HISTORICAL |
| HIST-03 | Render captures | `archive/render-captures/` | Working screenshots of model and drawing states | `RK-A`, `RK-A-ROOM` | Internal working | HISTORICAL |
| HIST-04 | Working tooling scripts | `archive/working-tooling/` | One-off Fusion capture scripts, retained for reproducibility | Method | Internal working | HISTORICAL |

## 4. Supplier and vendor research

| ID | Subject | Location | Status |
|---|---|---|---|
| VEN-01 | Component sourcing, pricing and lead times | `RK-A-MFG` Rev 2 (embedded in the manufacturing pack) | VENDOR SOURCE |

Rack vendor research is held inside the manufacturing pack. Lighting vendor research
is the first standalone supplier document, `suppliers/LIGHTING_SUPPLIER_LANDSCAPE.md`
(VEN-02 above).

---

## 5. Rules

1. A reference is **never** an authority for a Trophic engineering value. It
   informs a decision; the decision is recorded in `docs/decisions/`.
2. Do not load `SUPERSEDED` or `HISTORICAL` material to answer a current
   question. It exists for provenance.
3. When new research is done, index it here first. An unindexed research
   document will be re-read into context by accident.
