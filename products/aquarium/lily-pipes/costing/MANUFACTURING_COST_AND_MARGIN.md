# AQ-LP-A — Manufacturing Cost and Profit Margin

**Status:** RESEARCH / ESTIMATE · **Date:** 2026-09-17 · **No supplier quotation exists.**
Scope: product hypothesis **P1 — serviceable stainless inflow + outflow set (S1)**, the PROPOSED first product. Every ₹ figure below is an engineering estimate (EST) or planning assumption unless it cites a published price. Treat margins as a way to see which inputs matter, not as forecasts.

Relationship to other documents: this document owns the **per-step cost build-up, location cost effect and margin/P&L view**. The option comparison, channel assumptions, sensitivity and break-even stay in [COMMERCIAL_FEASIBILITY.md](COMMERCIAL_FEASIBILITY.md); manufacturing routes, suppliers and the location capability assessment stay in [SOURCING_STRATEGY.md](../sourcing/SOURCING_STRATEGY.md) §9. Both models run from the same inputs: [costing/unit_economics_model.py](unit_economics_model.py) and [costing/margin_model.py](margin_model.py) — re-run the second to regenerate every table here.

---

## 1. Summary

1. **Estimated manufacturing cost (COGS) for S1: about ₹2,030 per set at 25 sets, ₹1,540 at 50, ₹1,190 at 100, ₹1,040 at 200** (base case, ex-GST, including packaging, setups and scrap). Range at 100 sets: ₹660–2,140.
2. **Small batches are expensive because of setups, not material.** Tube is about 11 % of COGS; lot setups alone add ₹600 per set at 25 units but ₹150 at 100.
3. **Gross margin is healthy; profit is not automatic.** At MRP ₹3,999 and 100-set lots, gross margin is about **65 % selling direct** and **41 % selling to a dealer**. After selling costs, contribution falls to 42 % and 31 %.
4. **Net profit depends on volume.** After overheads, amortised development costs and tax, the illustrative net margin is **about −67 % at 84 sets a year, about 1 % at 264 sets and about 17 % at 600 sets** (MRP ₹3,999). At ₹4,499 the same scenarios give about −49 %, 9 % and 23 %. In the adverse-cost case the line loses money at every volume.
5. **Manufacturing location changes COGS by only about 1–12 %.** Capability, small-lot pricing and quality control matter more than distance (§4).

## 2. Terms used

| Term | Meaning here |
|---|---|
| **MRP** | Retail price including 18 % GST |
| **Net revenue** | What Trophic keeps before costs, ex-GST: MRP ÷ 1.18 when selling direct; the invoice price to the dealer when selling through a store |
| **COGS** | Manufacturing cost per set delivered to Trophic's store: material, job-work, finishing, clips, marking, inspection, packaging, lot setups, scrap |
| **Gross profit / gross margin** | Net revenue − COGS; margin = gross profit ÷ net revenue |
| **Contribution / contribution margin** | Gross profit − channel fees, outbound shipping, returns, warranty/breakage, acquisition allowance |
| **Operating profit** | Contribution − attributable overheads − amortised development and launch costs |
| **Net profit (illustrative)** | Operating profit − income tax at 25.17 % (domestic company under s.115BAA: 22 % + 10 % surcharge + 4 % cess, [ClearTax](https://cleartax.in/s/section-115-baa-tax-rate-domestic-companies)). The real rate depends on Trophic's legal entity and elections — confirm with a CA. Owner salary is **not** included, so real net profit is lower |
| **Margin vs markup** | Margin is a share of the selling price; markup is a share of cost. A 40 % dealer margin = 67 % markup on the dealer's cost |
| **GST** | Collected and remitted; never counted as revenue or margin. Input GST on costs assumed creditable |

## 3. Cost build-up per set (S1, base case, INR ex-GST)

Small-lot job-work premium applied to variable steps (×1.35 at 25, ×1.18 at 50, ×1.00 at 100, ×0.93 at 200). Low/high cases are in the model.

| Step | 25 sets | 50 | 100 | 200 | Basis |
|---|---|---|---|---|---|
| 316L tube (~0.8–1.0 m incl. offcut) | 180 | 150 | 130 | 120 | EST from 304 tube ₹79–117/m (PUB, [Roopam Steel](https://www.roopamsteel.com/stainless-steel-pipe-tube-price-list.html)) plus 316L premium and offcut |
| Tube laser: intake slots | 110 | 90 | 80 | 70 | EST; pipe laser listings ₹50–800/m (PUB, IndiaMART) |
| CNC mandrel bending (3–4 bends) | 200 | 180 | 150 | 140 | EST — no published per-bend price found |
| End forming: outlet termination + hose beads | 160 | 140 | 120 | 110 | EST |
| Degrease / ultrasonic clean | 70 | 60 | 50 | 50 | EST |
| Passivation or electropolish | 80 | 70 | 60 | 60 | EST; electropolishing listed ₹120/kg Coimbatore (PUB, unverified) — small lots pay minimum charges |
| Rim clips ×2 (laser-cut SS + pad) | 180 | 150 | 130 | 120 | EST |
| Laser mark | 40 | 40 | 30 | 30 | EST |
| Inspection and packing labour | 110 | 90 | 80 | 70 | EST |
| Packaging (board box, board/pulp insert, card) | 190 | 170 | 140 | 130 | EST |
| Lot setups (bending, forming, laser, finisher minimum, print) at ₹15,000 per lot | 600 | 300 | 150 | 80 | EST |
| Scrap / rework allowance (6 %) | 120 | 90 | 70 | 60 | EST (90–97 % yield after first article, specialist estimate) |
| **COGS per set** | **2,030** | **1,540** | **1,190** | **1,040** | |
| Low – high range | 1,110–3,630 | 850–2,760 | 660–2,140 | 580–1,870 | Model cases |

**Share of COGS at 100 sets:** bending 13 %, packaging 12 %, tube 11 %, clips 11 %, end forming 10 %, laser 7 %, inspection/packing 7 %, passivation 5 %, cleaning 4 %, marking 3 %, plus setups and scrap.

**Not included in COGS:** tooling and fixtures (₹0.5–2.5 lakh, one-time, in fixed costs), development, test equipment, overheads, inbound freight of tube stock (small).

**Variants (EST, per set at 100):** a dark PVD finish adds roughly ₹100–200 plus a minimum lot charge (from ₹300/sq ft PUB, [Crystal PVD](https://www.crystalpvd.in/pvd-coating-service.html)); a skimmer module adds about ₹650 (S2 COGS ≈₹1,840); a borosilicate glass set to Trophic's design is ≈₹1,720 with higher breakage allowance; an imported OEM set in a Trophic box is ≈₹2,460 landed.

**What makes COGS fall fastest:** larger lots (setups), fewer bends and forming operations, a clip made in the same laser/bend operations as the pipe, and a smaller pack. **What makes it rise:** thin-wall bends that wrinkle (scrap), separate welded terminations, electropolish inside the bore, dark coatings, two hose sizes in one lot.

## 4. Where it is made — cost effect of location

Capability evidence and the recommendation are in [SOURCING_STRATEGY.md](../sourcing/SOURCING_STRATEGY.md) §9. The cost effect is logistics between processors plus trips for first-article checks (EST; courier from [iCarry rate card](https://www.icarry.in/icarry-sample-rates-by-zones.pdf), Chennai–Coimbatore ≈510 km by road per [Yatra](https://www.yatra.com/distance-between/distance-from-chennai-to-coimbatore.html)).

| Location scenario | Extra per set at 25 (low / base / high) | Extra per set at 100 | S1 COGS at 100 incl. logistics (base) | Change |
|---|---|---|---|---|
| L1 — All steps in Coimbatore (only if a local tube shop proves capable) | 0 / 30 / 60 | 0 / 10 / 20 | 1,200 | +1 % |
| L2 — Tube forming in Chennai; finishing in Chennai or Coimbatore; QC and packing in Coimbatore | 140 / 220 / 300 | 40 / 60 / 80 | 1,250 | +5 % |
| L3 — Tube forming in Pune (or Bengaluru); QC and packing in Coimbatore | 360 / 550 / 820 | 90 / 140 / 200 | 1,330 | +12 % |

Reading: moving forming from Chennai to Coimbatore would save about ₹50 per set at 100 sets — less than the uncertainty in any single process estimate. A supplier that quotes ₹100 less per bend, or scraps 5 % fewer parts, is worth more than proximity. Proximity's real value is faster iteration during prototyping and easier quality control, which the numbers above do not capture.

## 5. From cost to retail price (S1, MRP ₹3,999, 100-set lot, base)

| Level | Amount (₹) | Margin on that selling price | Markup on the cost below it |
|---|---|---|---|
| COGS (ex-GST) | 1,190 | — | — |
| Trophic's price to dealer (ex-GST) | 2,030 | Trophic gross margin 41 % | 71 % on COGS |
| Retail price ex-GST (MRP ÷ 1.18) | 3,390 | Dealer margin 40 % (assumption) | 67 % on dealer price |
| GST 18 % | 610 | Not margin | — |
| **MRP** | **3,999** | — | "236 % over COGS" — misleading, because it includes GST and the dealer |
| Selling direct: Trophic gross profit at MRP | 2,200 | Gross margin 65 % | 184 % on COGS |

## 6. Per-set margins by price and channel (S1, 100-set lot, base)

| MRP | Channel | Net revenue | COGS | Gross profit | Gross margin | Contribution | Contribution margin |
|---|---|---|---|---|---|---|---|
| 3,499 | Direct (own site) | 2,970 | 1,190 | 1,770 | 60 % | 1,030 | 35 % |
| 3,499 | Amazon.in | 2,970 | 1,190 | 1,770 | 60 % | 570 | 19 % |
| 3,499 | Specialist retailer | 1,780 | 1,190 | 590 | 33 % | 380 | 21 % |
| **3,999** | **Direct (own site)** | 3,390 | 1,190 | 2,200 | **65 %** | 1,420 | **42 %** |
| 3,999 | Amazon.in | 3,390 | 1,190 | 2,200 | 65 % | 890 | 26 % |
| **3,999** | **Specialist retailer** | 2,030 | 1,190 | 840 | **41 %** | 620 | **31 %** |
| 4,499 | Direct (own site) | 3,810 | 1,190 | 2,620 | 69 % | 1,810 | 47 % |
| 4,499 | Amazon.in | 3,810 | 1,190 | 2,620 | 69 % | 1,210 | 32 % |
| 4,499 | Specialist retailer | 2,290 | 1,190 | 1,100 | 48 % | 860 | 38 % |

Selling-cost assumptions (Razorpay 2.36 %, Amazon referral 9.5–14 % + GST, dealer margin 35–45 %, shipping, returns, warranty, acquisition) are listed in [COMMERCIAL_FEASIBILITY.md](COMMERCIAL_FEASIBILITY.md) §5.

Gross margin looks high because aquarium accessories are low-material, high-handling products; most of the gap to profit is consumed by setups at small lots, selling costs, and fixed costs spread over few units.

## 7. Illustrative annual profit for the lily-pipe line

Assumptions (all EST): year-1 volume scenarios from [COMPETITOR_LILY_PIPE_REFERENCE.md](../../../../docs/references/lily-pipes/COMPETITOR_LILY_PIPE_REFERENCE.md) §7 — conservative 48 direct + 36 dealer sets in 50-set lots; base 120 + 144 in 100-set lots; optimistic 240 + 360 in 200-set lots. Development and launch costs (₹4.77 lakh base, ₹8.2 lakh adverse) amortised over 3 years. Attributable overheads (storage share, subscriptions, accounting/compliance share, travel, spare samples) ₹60k / ₹90k / ₹1.5 lakh a year. Owner time not costed. Tax only on positive profit; no loss carry-forward modelled.

### 7.1 MRP ₹3,999, base unit costs

| ₹ per year | Conservative (84 sets) | Base (264 sets) | Optimistic (600 sets) |
|---|---|---|---|
| Net revenue ex-GST | 2,35,870 | 6,99,490 | 15,45,380 |
| COGS | 1,29,090 | 3,14,550 | 6,23,680 |
| **Gross profit** | 1,06,780 | 3,84,930 | 9,21,700 |
| Selling costs | 45,300 | 1,25,200 | 2,66,330 |
| **Contribution** | 61,480 | 2,59,730 | 6,55,360 |
| Attributable overheads | 60,000 | 90,000 | 1,50,000 |
| Amortised development/launch | 1,59,000 | 1,59,000 | 1,59,000 |
| **Operating profit** | −1,57,520 | 10,730 | 3,46,360 |
| Income tax (illustrative) | 0 | 2,700 | 87,180 |
| **Net profit (illustrative)** | **−1,57,520** | **8,030** | **2,59,180** |
| Gross margin | 45 % | 55 % | 60 % |
| Contribution margin | 26 % | 37 % | 42 % |
| Operating margin | −67 % | 2 % | 22 % |
| **Net margin** | **−67 %** | **1 %** | **17 %** |

### 7.2 Same volumes at MRP ₹4,499

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Net profit (illustrative) | −1,30,180 | 69,040 | 3,94,350 |
| Gross / contribution / net margin | 51 % / 33 % / −49 % | 60 % / 43 % / 9 % | 64 % / 48 % / 23 % |

### 7.3 Stress test — MRP ₹3,999, adverse unit costs and fixed costs

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Contribution | −73,910 | −92,640 | −72,580 |
| Net profit (illustrative) | −4,07,240 | −4,55,980 | −4,95,920 |
| Net margin | −177 % | −68 % | −33 % |

If job-work costs land near the high estimate (≈₹2,140 per set at 100) while prices stay at ₹3,999, selling more makes the loss larger. That is why supplier quotations come before tooling or inventory.

## 8. What would make the margin credible

| Lever | Effect (from the models) | How to check |
|---|---|---|
| Quoted COGS at or below ≈₹1,200 per set at 100 | Keeps dealer contribution positive (≈₹620) | RFQs, [VALIDATION_PLAN.md](../verification/VALIDATION_PLAN.md) V-S1 |
| Price achievable at ₹4,499 rather than ₹3,999 | Base-scenario net margin 1 % → 9 % | Willingness-to-pay test V-C4, pre-orders V-C6 |
| Direct-sales share | Direct contribution ≈2.3× dealer at ₹3,999 | Channel plan, retailer interviews V-C5 |
| Lot size ≥100 | COGS ₹2,030 → ₹1,190 | Cash for inventory; sell-through |
| Dealer margin ≤40 %, no distributor | Distributor layer would cut dealer contribution to ≈₹230 | V-C5 |
| Keep the finish simple at launch | Dark PVD adds ₹100–200 per set plus minimums | V-T7, V-A3 |
| Pack volume | Courier price is set by volumetric weight | Pack design, V-P1 |

## 9. Open items before any figure here is relied on

- Replace every EST process line with quotes from at least two suppliers at 25/50/100/200 sets.
- Confirm tax treatment, GST input credit and entity type with a CA.
- Validate dealer margin norms, acquisition cost and returns rates.
- Re-run `costing/margin_model.py` and update this document and [CURRENT_STATE.md](../CURRENT_STATE.md).
