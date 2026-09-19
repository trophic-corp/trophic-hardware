# AQ-LP-A — Launch Strategy and Commercial Feasibility

**Status:** RESEARCH / PROPOSED · **Date:** 2026-09-17
**No supplier quotation exists.** Per-step cost build-up, location cost effect and gross/operating/net margin views: [MANUFACTURING_COST_AND_MARGIN.md](MANUFACTURING_COST_AND_MARGIN.md). Every cost is either a published price (PUB, see [SOURCING_STRATEGY.md](../sourcing/SOURCING_STRATEGY.md) §5) or an engineering estimate (EST). Prices are planning hypotheses to test, not approved retail prices. Model: [costing/unit_economics_model.py](unit_economics_model.py) (re-run to regenerate every table below); outputs: [sources/unit_economics_outputs.csv](unit_economics_outputs.csv).

---

## 1. Conventions

- **Tax:** retail prices are **MRP including 18 % GST**. Revenue in the model is **ex-GST** (MRP ÷ 1.18). Supplier costs are **ex-GST**, assuming Trophic is GST-registered and input GST is creditable (assumption A5; confirm with a CA). GST is a pass-through, not margin.
- **Margin vs markup:** margin is a share of the *selling* price; markup is a share of the *cost*. A dealer margin of 40 % of MRP equals a 66.7 % markup on the dealer's purchase price. Dealer margins below are stated as margins on MRP.
- **Contribution** = net revenue − COGS − channel fees − outbound shipping − returns allowance − warranty/breakage allowance − acquisition allowance. **It is not net profit**: it excludes owner salary, overheads, rent, interest, depreciation, income tax and fixed costs.
- **Cases:** *low/favourable*, *base*, *high/adverse*. The adverse case sets every cost input adverse at once, so it is a stress case, not a likely outcome.
- **FX:** ₹94.7/USD (assumption A6).

## 2. Launch strategy options

| Option | Customer / use case | Compatibility range | Differentiation | Manufacturing route | Evidence for | Evidence against / risk | Recommendation |
|---|---|---|---|---|---|---|---|
| **P1 — Serviceable stainless inflow + outflow set** | Dedicated planted-tank hobbyists who maintain their own tanks, including shrimp keepers; rimless glass; canister filter | One hose size at pilot (12/16 or 16/22 chosen by interview data), second size once the first passes validation; rimless glass within a stated thickness range; rimmed tanks later or via a variant | Survives handling (no breakage), hose releases without drama, every wetted surface brushable, shrimp-conscious intake, a clip designed with the pipe, a traceable grade, honest ageing, published measured compatibility — and a Trophic design language where stainless has none | (b) 316L tube, Tamil Nadu job-work, passivated/electropolished; finish variant tested | STRONG recurring problems (breakage, hose removal, cleaning, shrimp) and observed switching to stainless; weak design language and grade trust in stainless competitors; lowest-risk Tamil Nadu route | Must win against ₹1,950–3,999 stainless imports on visible care, not price; "industrial steel" risk in nature scapes; skimmer buyers not served at launch | **PROPOSED as the first product** |
| **P2 — Surface-skimmer module for P1's intake** | Same, plus owners fighting surface film | Tied to P1 sizes; stated flow window | A skimmer that tolerates level change without slurping or air, with an integrated guard | Machined parts at first; moulded float only after freeze and volume | STRONG complaints about skimmer noise/air/level; buyers replace skimmers | Highest engineering risk (float stability, air ingestion, entrapment); extra ₹0.4–1.5 lakh development | **PROPOSED as conditional second step**, only after rig and appearance gates |
| **P3 — Clip + intake-guard accessory kit** | Owners of existing glass or stainless pipes | Broad (many pipe ODs) | Replaces clear suction cups/holders; shrimp guard | Laser-cut/formed SS + pad; mesh or slotted guard | Paid guard market exists; mounting weakest across the market | CMF review: selling the signature clip on generic pipes dilutes the cue before P1 establishes it; fit across unknown pipe ODs | **PROPOSED to follow P1**; a clip prototype may be used as research, not sold first |
| G — Glass set to a Trophic design | Premium scapers valuing invisibility | 12/16, 16/22 | Better glass | (a) Ambala lampwork | Glass is the aesthetic archetype | Breakage is the category's main complaint; fragile freight; ADA/Cal Aqua Labs own invisibility; weak economics (§5); no Coimbatore capability proven | **Not proposed** as a first product |
| M — Private-label imported set | Price buyers | As supplied | Box and brand only | (e) import | Fast, low development | No design language; grade trust problem; negative contribution at a premium price (§5); copying risk | **Not proposed**; import samples for teardown only |
| Full set with skimmer at launch | — | — | — | — | Market has many skimmer sets | Doubles development risk before the core product is proven | **Not proposed** at launch |

**Smallest coherent initial portfolio (PROPOSED):** **P1 in one hose size and one finish**, with the skimmer interface reserved and a published compatibility chart. Inventory at launch is one SKU (plus spare clips), sized to a 50–100-set pilot lot.

## 3. Unit cost per set (INR ex-GST, including lot-setup amortisation and scrap)

Low / base / high. EST throughout; small-lot job-work premium applied (×1.35 at 25, ×1.18 at 50, ×1.00 at 100, ×0.93 at 200).

| Route | 25 units | 50 | 100 | 200 |
|---|---|---|---|---|
| **S1** SS316L set (inflow + outflow + 2 clips), Tamil Nadu job-work, passivated | 1,110 / **2,030** / 3,630 | 850 / **1,540** / 2,760 | 660 / **1,190** / 2,140 | 580 / **1,040** / 1,870 |
| **S2** = S1 + skimmer module (machined, no mould) | 1,610 / **3,030** / 5,470 | 1,250 / **2,340** / 4,240 | 990 / **1,840** / 3,340 | 880 / **1,620** / 2,950 |
| **G1** borosilicate set, Ambala lampwork to Trophic drawing | 1,290 / **2,630** / 5,400 | 1,040 / **2,120** / 4,330 | 850 / **1,720** / 3,480 | 770 / **1,550** / 3,120 |
| **M1** imported OEM SS set in Trophic box (benchmark) | 1,930 / **3,260** / 4,940 | 1,620 / **2,730** / 4,030 | 1,470 / **2,460** / 3,580 | 1,390 / **2,330** / 3,350 |

**S1 base build-up at a 100-set lot (EST, ₹ per set):** tube 316L 130 · laser slots 80 · CNC bending 150 · end forming 120 · degrease/ultrasonic 50 · passivation/electropolish 60 · two clips 130 · laser mark 30 · inspection and packing labour 80 · packaging 140 → **variable 970**; + lot setups ₹15,000 ÷ 100 = 150; ÷ (1 − 6 % scrap) → **₹1,190**. Material is ~11 %; process labour, setups and finishing dominate, which is why lot size matters so much. A dark PVD variant would add roughly ₹100–200 per set plus a minimum lot charge (EST from ₹300/sq ft PUB).

**M1 basis:** FOB US$9 / 14 / 17 per set (observed listing range) + freight/clearance ₹120–350 + non-creditable duty ₹150–420 + inspection/repack + Trophic packaging + ₹15–40k per-lot import administration. At ₹3,499 MRP it does not cover its costs, and it offers no differentiation.

**Source of each input:** SS tube and finishing rates PUB (SOURCING §5); every process price EST pending RFQ; packaging EST; courier from the iCarry rate card PUB. **Replace EST lines with quotations at 25/50/100/200 before any decision** ([VALIDATION_PLAN.md](../verification/VALIDATION_PLAN.md) V-S1).

## 4. Price bands (hypotheses to test)

| Offer | Proposed test band (MRP incl. GST) | Anchors observed in India |
|---|---|---|
| P1 set, no skimmer | **₹3,499–4,499** (model base ₹3,999) | Generic SS pair ₹1,950–2,100; SS + skimmer ₹2,790–3,999; Neo Flow Normal ₹2,499–3,399; Chihiros SS ₹3,000–4,600 (out of stock); Aquatic Venturez SS + skimmer ₹5,000–6,000 |
| P1 + P2 skimmer | **₹4,999–5,999** (base ₹5,499) | Neo Flow Premium ₹3,699–4,150; Aquatic Venturez ₹5,000–6,000 |
| P2 module alone (upgrade) | ₹1,499–1,999 (not modelled) | Generic skimmer adds ₹500–1,000 |
| Spare clip pair | ₹399–699 (not modelled) | Neo Holder ₹750; Chihiros clamp €6.49 |

P1 at ₹3,999 is about 1.9–2× a generic stainless pair and at parity with Neo Flow Premium and a generic SS skimmer set — without a skimmer. **That gap must be justified by visible care in photos and by the handling/cleaning experience** (CMF review, AESTHETIC REF §5). Willingness to pay at these bands is unverified (interviews V-C4, pre-order test V-C6).

## 5. Contribution per set by channel — base case, 100-set lot

| Route | Channel | MRP | Net rev ex-GST | COGS | Fees | Ship | Returns | Warranty/breakage | Contribution before acquisition | Acquisition allowance | **Contribution** | % of net rev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | DTC own site | 3,999 | 3,390 | 1,190 | 90 | 130 | 140 | 70 | 1,770 | 350 | **1,420** | 42 % |
| S1 | Amazon.in, seller-fulfilled | 3,999 | 3,390 | 1,190 | 660 | 130 | 200 | 70 | 1,140 | 250 | **890** | 26 % |
| S1 | Specialist retailer | 3,999 | 2,030 | 1,190 | 0 | 40 | 40 | 40 | 720 | 100 | **620** | 31 % |
| S2 | DTC own site | 5,499 | 4,660 | 1,840 | 130 | 130 | 190 | 140 | 2,240 | 350 | **1,890** | 40 % |
| S2 | Amazon.in | 5,499 | 4,660 | 1,840 | 870 | 130 | 280 | 140 | 1,410 | 250 | **1,160** | 25 % |
| S2 | Specialist retailer | 5,499 | 2,800 | 1,840 | 0 | 40 | 60 | 80 | 780 | 100 | **680** | 24 % |
| G1 | DTC own site | 3,499 | 2,970 | 1,720 | 80 | 130 | 120 | 240 | 680 | 350 | **330** | 11 % |
| G1 | Specialist retailer | 3,499 | 1,780 | 1,720 | 0 | 40 | 40 | 140 | −160 | 100 | **−260** | −14 % |
| M1 | DTC own site | 3,499 | 2,970 | 2,460 | 80 | 130 | 120 | 120 | 50 | 350 | **−300** | −10 % |
| M1 | Specialist retailer | 3,499 | 1,780 | 2,460 | 0 | 40 | 40 | 70 | −830 | 100 | **−930** | −52 % |

**Channel assumptions (base; ranges in the model):**

| Input | DTC own site | Amazon.in (seller-fulfilled) | Specialist retailer |
|---|---|---|---|
| Payment/marketplace fee | Razorpay standard 2 % + 18 % GST on fee = 2.36 % of MRP ([Razorpay, Feb 2026](https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/)) PUB | Referral 9.5–14 % for pet accessories above ₹1,000 from 16 Mar 2026 ([secondary summary](https://www.kwickmetrics.com/blog/amazon-referral-fee-2026-india); confirm on Seller Central) + 18 % GST on fee; closing/other fees ₹60–130 EST | None; **dealer margin 35 / 40 / 45 % of MRP — assumption, no Indian source found** |
| Outbound shipping | ₹90–200 per order EST (courier card PUB; pack volume drives it) | same | ₹25–70 per unit (bulk to store) EST |
| Returns allowance | 2–6 % of net revenue EST | 4–9 % EST | 1–4 % EST |
| Warranty/breakage | S1 1–3 %; S2 2–5 %; G1 5–12 %; M1 2–6 % EST | | |
| Acquisition allowance | ₹150–600 per unit EST (samples, seeding, ads) | ₹100–450 EST (sponsored listings) | ₹50–200 EST (demo units, dealer support) |

**Dealer viability (PROPOSED reading):** at base inputs P1 earns ≈₹620 per set through a specialist retailer — **viable but thin**. It stays positive only with MRP ≥ ≈₹3,999, dealer margin ≤ ≈40 %, and COGS near the base estimate; in the adverse case it is negative. A **two-tier distributor + dealer chain** (EST dealer 40 % + distributor 12 % of MRP) would leave ≈₹230 per set and is not recommended. Glass and import routes are not viable through dealers at comparable prices.

## 6. Sensitivity (S1, 100-set lot, contribution per set)

| Change from base | DTC own site | Specialist retailer |
|---|---|---|
| Base (MRP ₹3,999) | 1,420 | 620 |
| MRP ₹2,999 | 650 | 130 |
| MRP ₹3,499 | 1,030 | 380 |
| MRP ₹4,499 | 1,810 | 860 |
| COGS × 0.7 | 1,780 | 980 |
| COGS × 1.3 | 1,060 | 260 |
| Dealer margin 30 % of MRP | — | 950 |
| Dealer margin 50 % of MRP | — | 300 |
| Acquisition ₹0 per unit | 1,770 | 720 |
| Acquisition ₹800 per unit | 970 | −80 |

**By lot size (favourable / base / adverse):** S1 DTC 580 at 25 sets, 1,070 at 50, 1,420 at 100, 1,570 at 200 (base). S1 dealer is **negative at a 25-set lot** in the base case (−220) — do not open dealer supply until lots of ≥50–100 are affordable. Full table in the model output.

The three inputs that move the answer most: **retail price achievable, job-work COGS at small lots, and dealer margin.** All three are unvalidated.

## 7. One-time costs, launch investment and break-even

| Item (EST) | Low | Base | High |
|---|---|---|---|
| Benchmark samples + teardown (6–8 sets incl. imports) | 35,000 | 50,000 | 70,000 |
| Flow/hose test rig (2 canisters, flow meter, hoses, tank) | 30,000 | 55,000 | 80,000 |
| Prototype rounds (3 × 3–5 sets, job-work) | 45,000 | 80,000 | 1,20,000 |
| Tooling and fixtures (bend dies if absent, flare tooling, gauges) | 50,000 | 1,20,000 | 2,50,000 |
| Corrosion/finish/material lab tests (PMI, A967 verification, immersion) | 15,000 | 35,000 | 60,000 |
| Packaging development (dieline, samples, drop tests) | 15,000 | 25,000 | 40,000 |
| IP: attorney FTO search + design filing(s) (filing fee ₹1,000 small entity PUB; attorney EST) | 30,000 | 60,000 | 1,20,000 |
| Compliance/label review (LMPC, e-commerce) | 5,000 | 12,000 | 20,000 |
| Photography, listing, launch content | 20,000 | 40,000 | 60,000 |
| **Total fixed, P1** | **2,45,000** | **4,77,000** | **8,20,000** |
| Add for P2 skimmer (extra prototype rounds, rig time) | 40,000 | 80,000 | 1,50,000 |

**Credible investment ranges (PROPOSED for planning):**

| Stage | What it buys | Range |
|---|---|---|
| **Prototype stage** (to validated prototypes, no tooling, no IP filing, no inventory) | Samples + rig + three prototype rounds + lab tests | **≈₹1.25–3.3 lakh** (base ≈₹2.2 lakh) |
| **Launch of P1** (fixed costs + first 100-set lot at unit cost) | All fixed items above + inventory ≈₹0.66–2.14 lakh | **≈₹3.1–10.3 lakh** (base ≈₹6.0 lakh) |
| P2 skimmer later | Development add + first 50-set lot | ≈₹1.0–3.6 lakh |

Owner design time is excluded (assumption A7). Glass would carry similar fixed costs but worse contribution; import would need ≈₹0.75–1.9 lakh fixed but loses money per unit at a premium price.

**Break-even units against P1 fixed costs** (contribution at the 100-set lot cost):

| Route · channel | Favourable (low fixed) | Base | Adverse (high fixed) |
|---|---|---|---|
| S1 · DTC own site | 107 | **336** | effectively not reached |
| S1 · Amazon.in | 132 | **536** | not reached |
| S1 · Specialist retailer | 173 | **769** | not reached |
| S2 · DTC own site | 92 | **296** | not reached |
| G1 · DTC own site | 155 | **1,449** | not reached |

S1 base break-even by price: at ₹3,499 → 462 (DTC) / 836 (Amazon) / 1,267 (dealer); at ₹4,499 → 265 / 395 / 552.

Against the year-1 volume scenarios in [COMPETITOR_LILY_PIPE_REFERENCE.md](../../../../docs/references/lily-pipes/COMPETITOR_LILY_PIPE_REFERENCE.md) §7 (≈84 / 264 / 600 sets), fixed costs are recovered in roughly 10 months (optimistic), 22 months (base) or not within five years (conservative). **The adverse case does not break even at any volume** — the reason COGS quotations and price testing come before tooling and IP spend.

## 8. Channel comparison — direct-to-consumer vs specialist retailer

| Factor | DTC (own site; marketplace as secondary) | Specialist retailer |
|---|---|---|
| Contribution per set (S1 base) | ≈₹1,420 own site; ≈₹890 Amazon | ≈₹620 |
| Volume per effort | Low until community awareness exists | Higher once stocked; stores have thin stock depth (observed 1–66 units per SKU) |
| Customer learning | Direct feedback on fit, cleaning, ageing — valuable during the first year | Filtered through store staff |
| Brand presentation | Full control of photographs, compatibility chart, care instructions (critical for a "visible care" product) | Depends on store listing quality; Indian listings observed omit dimensions and warranty |
| Returns and fit errors | Trophic bears them; compatibility chart reduces them | Store handles first contact; margin covers some risk |
| Working capital | Trophic holds all stock | Dealer may buy stock, or ask for consignment (unknown — interview) |
| Risk | Acquisition cost could exceed ₹800 per set and erase margin | Dealer margin above ~45 % or distributor layer makes it marginal |

**PROPOSED channel stance:** launch DTC-led (own site), add 3–5 specialist retailers at a fixed dealer margin (no distributor tier) once the lot size reaches 100, and treat Amazon.in as a later discovery channel after reviews exist. Validate dealer margin norms and consignment expectations before committing (V-C5).
