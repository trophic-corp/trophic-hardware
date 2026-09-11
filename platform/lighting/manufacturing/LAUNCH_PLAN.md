# Lighting Launch Plan — prototypes, EVT/DVT, field pilot, first commercial batches

**Status:** PROPOSAL, 2026-09-11 · **Numbers:** from `../costing/lighting_cost_model.py` (planning model, not commercial truth) · **Gates:** `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md` §2
**Applies to:** `AQ-LT-A` Core, `AQ-LT-B` WRGB, Smart Module. `LT-A` follows the rack programme and is not in this plan.

The plan is built around one principle: **commit tooling and MOQ only after the evidence that justifies it exists.** Stock extrusion until DVT; the die at DVT; moulds never before ~300 units; no production MOQ purchase before the field pilot has returned data.

---

## 1. Stages, quantities and what each stage proves

| Stage | Units | Built on | Proves | Cost tier in the model |
|---|---|---|---|---|
| **EP, engineering prototypes** (Phase 1–2 end) | 6 fixtures: Core 45 ×2, Core 30 ×1, WRGB 45 ×2, WRGB 60 ×1; 4 Smart Modules | **Stock extrusion or heatsink profile, CNC-modified**; machined caps; JLCPCB/Indian small-lot boards; cut-tape LEDs; breadboard-to-first-PCB electronics | Electrical design, LED engine spectrum and PPFD, thermal behaviour in the intended body class, optic and mixing approach, engine/module port and protocol, firmware state machine, mechanical concept and mounting | proto |
| **EVT/DVT** (Phase 3) | 18 fixtures: Core 30/45/60 = 3/4/3, WRGB 30/45/60 = 2/4/2; 14 modules | **First die run** (die committed here, minimum negotiated run); machined caps; Indian MCPCB at MOQ; EMS first article | Everything in Gate C at `validated design` tier across all three lengths, including 60 cm; supplier first articles; EOL jig; DFM | pilot |
| **Field pilot** (Phase 5-lite) | 12 serialised units drawn from DVT stock: Core ×8 (30/45), WRGB ×4 (45/60), each with a module; plus 4 spare modules | DVT units refurbished to pilot grade | Real-tank behaviour, condensation and corrosion, app and schedule reliability, price acceptance, failure modes, 3 months of field hours | (no extra unit cost) |
| **Batch 1, first commercial** | **~36–40 fixtures + ~30–36 modules** (§3) | Die stock, machined caps, MOQ boards, adapters bought in tens | Sell-through, D2C operations, warranty process, second-batch demand signal | 50 |
| **Batch 2** | ~100 fixtures + ~80 modules, 60 cm commercially introduced | Same tooling; moulds considered if cumulative demand > ~300 | Scaled costing, dealer economics | 100 |

Why 60 cm is engineering-validated in DVT but commercially second: it is the highest-COGS Core, the length where the shared-housing cost test bites hardest, and (for WRGB) the SKU whose contribution is highest, so it belongs in the WRGB-led scenario; the Core 60 waits for scaled costs.

## 2. Prototype strategy and budget

- **Stock extrusion first.** A finned heatsink profile or U-channel from an Indian stockist, cut and CNC-modified, costs a few hundred rupees per prototype against a ₹40k die plus a ≥ 150 kg minimum run. EP units validate thermal class, optics and electronics; only the DVT units need the real section. The model applies a 4× extrusion factor at proto tier for this.
- **Machined end caps and machined or polymer puck** through batch 1; moulds (~₹4 lakh caps, ~₹3 lakh puck) are deferred until cumulative demand is proven.
- **Boards:** JLCPCB or an Indian fab at 5–10 pieces for EP; Indian fab at MOQ 100 per artwork for DVT (the overrun is batch-1 stock).
- **LEDs:** cut tape from authorised distribution for EP; one reel per type for DVT onward.
- **Adapters:** off-the-shelf certified units in tens; no adapter MOQ before batch 2.

EP budget (model, proto tier): 6 fixtures + 4 modules ≈ **₹68k in units**, plus consumables, spare boards, stock extrusion and CNC ≈ ₹60k, plus the instrument set (quantum sensor ≈ ₹60k, thermal camera and bench equipment ≈ ₹85k, spectroradiometer rental ≈ ₹30k) and the external firmware/app contract line (₹2 lakh, set to zero if in-house). **Prototype-phase cash ≈ ₹5 lakh including instruments and external firmware; ≈ ₹3 lakh without the firmware contract; ≈ ₹1.3 lakh for units and consumables alone.** All EST/ASSUME.

## 3. First commercial batch: recommendation

The model shows why "100 Core + 30 Premium" is the wrong first batch: at 50–100-unit costs the Core SKUs lose money at the intended prices, WRGB does not. Two scenarios were modelled (cost model §6):

| Scenario | Build | Cash in inventory (50-unit tier) | Gross revenue if sold through | Net ex-GST | Contribution after variable costs |
|---|---|---|---|---|---|
| A, Core-led | Core 30 ×12, Core 45 ×16, WRGB 30 ×4, WRGB 45 ×8; 30 modules | ≈ ₹2.2 lakh | ≈ ₹2.5 lakh | ≈ ₹2.1 lakh | **≈ −₹29k** |
| B, WRGB-led | Core 45 ×10, WRGB 30 ×6, WRGB 45 ×12, WRGB 60 ×8; 36 modules | ≈ ₹2.6 lakh | ≈ ₹3.4 lakh | ≈ ₹2.9 lakh | **≈ +₹2k** |

**Recommended shape: Scenario B plus a deliberately small Core presence** (≈ 10 Core 45 Smart, treated as a market-entry cost, not a profit line), i.e. **36–40 fixtures and ~36 modules**, launching **45 cm as the lead length for both products, 30 cm for WRGB, and 60 cm for WRGB only**; Core 30 and Core 60 follow in batch 2 once RFQs and pilot data show whether Core can reach a contributing price. A 30–50 fixture batch is more capital-efficient than 130 units because: extrusion stock from the minimum run already exists; MCPCB MOQ stock exists; PCBA setup is per run (₹70–90k) and is the only step that favours larger batches; adapters and LEDs have no meaningful MOQ at these quantities; and Core inventory at a loss-making price is the last thing to build ahead of demand.

OWNER DECISION REQUIRED: the Core price and whether Core sells in batch 1 at all (cost model §5 and §8).

## 4. Financial impact of MOQ and tooling items

| Item | Cash | When | Note |
|---|---|---|---|
| Extrusion die | ≈ ₹40k (RMKT/EST) | DVT | One die for both products if the cost test passes; otherwise two |
| Extrusion minimum run | ≈ ₹57k at a negotiated 150 kg (ASSUME); ₹1.9 lakh at a standard 500 kg | DVT | ~187 m ≈ 400 fixtures at 45 cm; stable stock, but cash up front. Negotiate metre-based or 100–150 kg minimums; this is the single largest avoidable cash item |
| Custom MCPCB MOQ | ≈ ₹90k across 6 artworks at MOQ 100 (RMKT/EST) | DVT | Overrun is batch-1 and batch-2 stock; WRGB boards could be panelised with Core to cut artworks |
| PSU MOQ | none at batch 1 (bought in tens from distribution); 100–500 per rating if private-labelled | Batch 2+ | Keep one voltage and one family so ratings pool |
| PCBA setup | ≈ ₹72k per run (9 artworks) | Every run | The one item that argues for fewer, larger runs; mitigate by panelising and by fewer artworks (one end-cap/engine board per product) |
| Packaging print | ≈ ₹20k for 500 sleeves | Batch 1 | Digital print for the WRGB run, offset only for Core at scale |
| End-cap mould | ≈ ₹4 lakh | Deferred | Justified at ≥ ~300 units; cuts caps from ₹300 to ₹80 per pair |
| Puck mould | ≈ ₹3 lakh | Deferred | Justified at ≥ ~300 modules |

## 5. Cash summary (model §6)

| | ₹ (model) |
|---|---|
| Programme expense before sales (die, NRE, instruments, labs, regulatory, firmware contract, EP + DVT units, pilot logistics) | ≈ 10.0 lakh (≈ 8.0 lakh without the firmware contract) |
| Inventory before sales (extrusion and MCPCB MOQ stock + batch 1 at Scenario A) | ≈ 3.7 lakh |
| **Total cash before first meaningful sales** | **≈ 13.6 lakh** (≈ 11.6 lakh without the firmware contract) |
| Batch 1 sold through, Scenario B | gross ≈ 3.4 lakh, net ex-GST ≈ 2.9 lakh, contribution ≈ +₹2k |
| Break-even against programme expense | ≈ 730 units at scaled COGS, not reachable at 100-unit COGS at current Core prices; excludes salaries and marketing |
| Working capital for batch 2 (100 fixtures + 80 modules, 60 cm launched) | ≈ 5.0 lakh + ₹72k PCBA setup, 60–90 days before D2C cash returns |

These are planning figures with EST/ASSUME inputs; the RFQ packages in the roadmap §3 replace them.

## 6. What this plan does not decide

Prices; the Core go/no-go for batch 1; die count (one or two profiles); bus voltage and PSU family; connector; whether WRGB Standalone is a sold SKU (the Systems Architect doubts it); dealer channel timing. Each is tracked in `products/aquarium/lighting/PLATFORM.md` §11.
