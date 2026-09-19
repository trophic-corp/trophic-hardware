# Sourcing Strategy — `AQ-LP-A` Lily Pipes

*Manufacturing routes, supplier shortlist, cost data, compliance, IP and location assessment.*

**Status:** RESEARCH · **Date:** 2026-09-17 · **Prepared under:** `manufacturing-sourcing-engineer` brief (Coimbatore first → Tamil Nadu/India → import where justified), synthesised by Main Claude
**No supplier has been contacted. No supplier is qualified.** Status vocabulary only: `candidate`, `longlisted`, `RFQ required`, `sample required`, `qualification required`. Numbers are **PUB** (published listing/price, with source, not a quote) or **EST** (engineering estimate to be replaced by RFQ). Nothing here is legal, tax or customs advice. Structured shortlist: [sources/supplier_shortlist.csv](supplier_shortlist.csv).

---

## 1. Summary

1. **Stainless steel tube fabrication is the strongest make-in-India route.** Every required step — CNC mandrel bending, tube laser cutting, end forming (flare, beads), TIG with back-purge if needed, passivation/electropolishing, PVD — has at least one public lead in Coimbatore or Chennai. The best single process match found is Polyfit (Chennai: CNC bending 4.76–120 mm OD plus flaring, beading, bulging, welding). **All are INFERRED capability until samples prove it.**
2. **Borosilicate glass belongs to the Ambala cluster** (SGC Labs, JSGW) with Mumbai (Borosil) as a large-MOQ option. Coimbatore and Chennai glassblowers are unverified directory leads. Hand-work repeatability and fragile freight across ~2,500 km are the dominant risks.
3. **Acrylic is not recommended for the pipe** (crazing, scratching, flared forms hard to bend) but is usable for small parts.
4. **Injection moulds (₹2–8 lakh, PUB) are not justified at launch volumes** (specialist threshold ~2,000 sets/year). Machine or laser-cut small parts first.
5. **Importing finished OEM sets** (observed US$9–17 per set, MOQ 5–100, trading companies) is a benchmark and a teardown source, not a differentiated product.
6. **No Indian manufacturer of lily pipes was found.** Indian brands observed are sellers of imports.

---

## 2. Route comparison

| Criterion | (a) Borosilicate lampworking | (b) Stainless tube fabrication | (c) Acrylic (PMMA) tube | (d) Injection moulding (small parts) | (e) Import finished OEM |
|---|---|---|---|---|---|
| Fit to product | Classic transparent form; competes with ADA on invisibility | Durable; allows textured or dark finishes; matches market shift to steel | Light, cheap; scratches and crazes | Floats, clips, caps, adapters only | Whole product, no differentiation |
| Process steps | Cut tube → torch/lathe bends on graphite forms → flare by paddle or carbon mould → diamond-cut slots → **kiln anneal** → polariscope → fire polish → DI rinse | Cut 316L/304 tube → **laser-cut slots** → **CNC mandrel bends** → **end-form flare and hose beads** (or spun flare + TIG) → degrease/ultrasonic → pickle/**passivate (A967)** → optional **electropolish (B912)** or bead blast + PVD → inspect (bend, slot width, PMI, pull-off) | Cut → heat-bend on jig → CNC/laser slots → solvent bond → polish → cure/out-gas | Mould design → T1 samples → production | Sample → PMI/teardown → order → import clearance |
| Tooling / fixtures | Low: graphite forms, jigs, gauges (EST few thousand to tens of thousands ₹; no Indian price found) | Medium: bend die set per OD/CLR EST ₹25k–1L if vendor lacks it; flare/end-form tooling EST ₹15k–75k; weld/inspection fixtures EST ₹10k–40k; laser program setup only | Low: bending jigs | High: simple steel mould **₹2–8 lakh, 4–6 weeks; medium ₹8–15 lakh** ([Moldrite, Apr 2026](https://www.moldrite.in/blog/injection-molding-cost-india)) PUB | Nil; private label extra |
| MOQ | Custom single pieces accepted by scientific glassblowers (claim); MOQ not published | Job shops accept small lots; tube stock in 6 m random lengths | Small | Economic above ~2,000/yr (EST) | 5–100 pieces observed |
| Repeatability | **Low–medium** (hand work; flare, hook gap, slot width vary) | **High** once CNC program and tooling fixed | Medium | Very high | Batch-dependent, uncontrolled |
| Yield / rejection (EST) | 70–90 % at pilot; breakage in slotting, annealing, transit | 90–97 % after first article; wrinkling, ovality, heat tint, PVD shade mismatch, scratches | 85–95 %; crazing at joints | >97 % after tool trial | Unknown; incoming inspection essential |
| Material traceability | Weak: tubing brand/COE 3.3 declaration, rarely lot certificates | **Strong:** EN 10204 3.1 mill test certificate normal; BIS-marked tube (QCO status to confirm, §8) | Weak–medium | Resin CoA | Weak: "304" claims; PMI needed |
| Joining | Fused glass — no adhesive | One-piece bent tube + formed flare + rolled beads avoids wetted welds; otherwise TIG with internal argon purge and tint removal | Solvent cement (residual monomer risk) | Snap, ultrasonic, press fit | n/a |
| Internal cleanliness | Excellent, inspectable | Good if degreased, passivated, electropolished; weld tint inside is a corrosion and algae seed | Solvent residue risk | Good | Unknown |
| Finishing options | Fire polish | Passivated natural, bead blast, electropolish, PVD (black, gunmetal) | Flame/buff polish | Colour in resin | As offered |
| Packaging / transit | **High risk**: cavity cradle, rigid double-wall; volumetric weight of long boxes drives courier cost | Low: scratch/dent protection | Low–medium | Low | Low (SS) / high (glass) |
| Repair / replacement | Replace only | Re-polish or re-passivate possible; skimmer/clip replaceable | Replace | Replace | Replace |
| Prototype feasibility | Good if a local workshop proves capable (unverified) | **Good**: all steps have Tamil Nadu leads | Good | Use 3D print / machining instead | Immediate (buy samples) |
| Repeat-production feasibility | Medium, Ambala-dependent | **High**, Tamil Nadu | Medium | High once frozen | Medium, supplier-dependent |
| Location suitability | Ambala (depth), Mumbai (Borosil, likely high MOQ), Vadodara (process glass, weaker fit); Coimbatore/Chennai unverified; **Firozabad is soda-lime decorative glass, not a borosilicate lampworking cluster [I, verify]** | **Coimbatore + Chennai**; Mumbai/Ahmedabad for tube stock and hygienic finishing | Coimbatore sheet fabricators; Mumbai tube extruder | Coimbatore (strong moulders) | China |
| Import duty if bought finished (PUB aggregator, broker to confirm) | HSN 7020 00 90 ≈32.3 % effective incl. IGST | 7326 90 99 ≈40.4 % + **SIMS registration** | 3926 90 99 ≈40.4 % | — | per material |
| **Specialist view (PROPOSED, not decided)** | Not first product; secondary/reference only | **Primary route to prove** | Small parts only | Only after design freeze and volume | Benchmark and teardown only |

## 3. Route detail notes

**(a) Glass** — capabilities to demand: bench burner and glass lathe, kiln annealing (schedule to be confirmed by vendor; EST ≈560 °C for 3.3), diamond slotting, 100 % polariscope stress inspection, jig-based repeat to a master sample. Budget breakage in transit (EST 3–8 % of courier shipments without a validated pack). An imported 17 mm glass skimmer set is listed at ~600 g boxed ([toolsvilla](https://www.toolsvilla.com/17mm-glass-pipe-for-aqua-canister-filter)) PUB.

**(b) Stainless** — design-for-manufacture points raised by the specialist, all to be confirmed at RFQ:

- Thin wall (≈0.8–1.2 mm) at tight centre-line radius needs mandrel + wiper die to avoid wrinkling and ovality.
- Laser-cut slots before bending if slots are away from bends; check internal dross and burr.
- Prefer rolled hose-retention beads over a welded barb (no weld in the wetted path).
- A flared termination can be end-formed (ratio limit to confirm), spun and welded, or hydroformed (EST only justified above 5–10k/yr).
- Bending lubricant must be removed (alkaline degrease + ultrasonic) before passivation.
- Laser marking on wetted surfaces damages the passive layer; re-passivate or mark above water.
- PVD on 304/316 is available locally; **no immersion durability data found** — sample and test before proposing.
- EST set weight 150–350 g; low transit risk.

**(c) Acrylic** — Coimbatore fabricators found are sheet/display-oriented (Devi Plastic Arts ≤5 mm sheet curve bending; Tekno Plastic Systems acrylic displays plus moulding); tube bending unverified. FZONE sells SS pipes with acrylic "pipe fixers" (observed listing).

**(d) Moulding** — PP ₹15–50 per simple part at 1k–5k/yr; resin ₹150–180/kg (Q2 2026) (Moldrite) PUB. Consider one family mould (float + clip + cap) only after freeze.

**(e) Import** — observed listings (PUB, not quotes; FOB basis not always stated):

| Listing | Supplier (type) | Material | Price | MOQ | Source |
|---|---|---|---|---|---|
| Lily pipe SG-1212/1616/1612 | Bests Industrial and Trading, Hefei (**trading company**) | "GB304 stainless, mirror polish" | US$14–17 per pc (piece vs set unclear); sample US$30 | 100 | [made-in-china](https://aquatosun.en.made-in-china.com/product/LAmYobGhRaWp/China-Aquarium-Lily-Pipe-for-Glass-Acrylic-Fish-Tank-Aquarium-External-Filter.html) |
| 12/16 SS skimmer lily pipe | Bests Industrial | SS | US$32.10–41.30 | 10 | same supplier |
| 13/17 glass skimmer lily pipe | Bests Industrial | Glass | US$23.90–26.10 | 10 | same supplier |
| Glass inlet/outlet with skimmer | Beijing Uuidear Technology and Trade | Glass | US$3.88–8.92 | 20 | [made-in-china search](https://www.made-in-china.com/products-search/hot-china-products/Lily_Pipe.html) |
| Metal lily pipe / skimmer | Beijing Uuidear | SS | US$9.24–17.56 | 5 | same |
| AliExpress retail (ZRDR, AQUAPRO, Week Aqua) | various | 304 SS | US$14–45 per set | 1 | [AliExpress](https://www.aliexpress.com/w/wholesale-stainless-steel-lily-pipe.html) |

Risks: trading companies without process control; unverified grade; no MTC; batch-to-batch finish; SIMS for Chapter 73; country-of-origin display; copying branded forms.

## 4. Supplier shortlist (desk research; nobody contacted)

Evidence: **CONFIRMED** = public evidence of this or a very close product · **INFERRED** = evidence of the process capability · **UNVERIFIED** = directory lead only.

| # | Supplier | City | Route | What the public evidence shows | Evidence | Status |
|---|---|---|---|---|---|---|
| S01 | [Polyfit Fabricators](https://polyfit.co.in/tube-bending/) | Chennai (Ambattur) | (b) bending, end forming, welding | CNC 5-axis tube bending 4.76–120 mm OD; flaring, swaging, beading, bulging; welding; prototyping | INFERRED (strong) | longlisted — RFQ required, sample required |
| S02 | Techno Tool Engineering / Saxeo Manufacturing / S.R.L Industries ([IndiaMART category](https://m.indiamart.com/coimbatore/pipe-bending-services.html)) | Coimbatore | (b) bending | Directory listings for CNC/SS pipe and tube bending | UNVERIFIED | candidate — RFQ required (confirm thin-wall small-OD mandrel bending) |
| S03 | [Endee Infrastructure & Engineering](https://www.endee-engg.in/main.html) | Coimbatore / Chennai / Bengaluru | (b) clips, brackets | Laser cutting SS, CNC bending, TIG, finishing (sheet focus) | INFERRED | candidate — RFQ required |
| S04 | Ace Tech / AGP Steels ([IndiaMART](https://m.indiamart.com/impcat/pipe-laser-cutting-service.html)) | Coimbatore | (b) tube laser | Pipe laser cutting listings | UNVERIFIED | candidate — RFQ required |
| S05 | [Crystal PVD Technologies](https://www.crystalpvd.in/pvd-coating-service.html) | Coimbatore | (b) finish | PVD on SS 304 incl. black and gunmetal; listed ₹300/sq ft | INFERRED | longlisted — sample required (immersion durability) |
| S06 | [Metallica](https://www.metallica.works/) | Chennai | (b) finish | PVD on SS for bath/kitchen fittings | INFERRED | candidate — sample required |
| S07 | [Sri Murugan Electro Polishing](https://www.electropolishing.org/) | Chennai (Korattur) | (b) finish | Dedicated electropolishing business | INFERRED | candidate — RFQ required |
| S08 | [Sri Iyyappa Electropolishing](https://www.sriiyyappaelectropolishing.com/stainless-steel-electropolishing-services-in-chennai/) | Chennai | (b) finish | Site title: SS electropolishing services (detail not retrievable) | UNVERIFIED | candidate — RFQ required |
| S09 | Arunn Coats ([IndiaMART](https://m.indiamart.com/impcat/ss-electro-polishing-service.html)) | Coimbatore | (b) finish | SS electropolishing listed ₹120/kg | UNVERIFIED | candidate — RFQ required |
| S10 | [Bharat Metals](https://www.stainlesssteeldealers.com/) | Chennai (Parrys) | (b) tube stock | SS 304/316L tubes; cutting/bending/polishing; mill certificates | INFERRED | candidate — RFQ required (small OD thin wall, BIS mark) |
| S11 | [SGC Labs](https://labsglass.com/) | Ambala | (a) | Borosilicate 3.3; custom fabrication; skilled glassblowers; OEM; ISO 9001 claim | INFERRED (close) | longlisted — RFQ required, sample required |
| S12 | [Jain Scientific Glass Works (JSGW)](https://www.jsgw.com/) | Ambala Cantt | (a) | Since 1950; Boro 3.3 to ISO 3585; customised specifications | INFERRED | longlisted — RFQ required |
| S13 | [Borosil Scientific OEM](https://www.borosilscientific.com/oem/) | Mumbai | (a) + tubing | OEM/custom glassware, four plants; MOQ unpublished | INFERRED | candidate — RFQ required (likely high MOQ) |
| S14 | [Ablaze Glass Works](https://www.ablazeglassworks.com/) | Vadodara | (a) | Custom glassblowing, process equipment focus | INFERRED (weaker fit) | candidate |
| S15 | Laboratory Scientific Glass Works ([directory](https://www.kovaipublishers.com/index/laboratory-scientific-glass-works/)) | Coimbatore | (a) prototypes | "Manufacturers of industrial, scientific lab glasswares & servicing" | UNVERIFIED | candidate — RFQ required, sample required |
| S16 | J S Scientific Works ([IndiaMART](https://m.indiamart.com/js-scientific-works-chennai/)) | Chennai | (a) prototypes | Lists scientific glass blowing | UNVERIFIED | candidate — RFQ required |
| S17 | [Roots Polycraft](https://www.rootspolycraft.com/) | Coimbatore | (d) | ISO 9001, IATF 16949; 50–550 T; in-house tooling; ultrasonic welding | INFERRED | longlisted — RFQ required (post-freeze) |
| S18 | [RK Poly Products](https://www.rkpolyproducts.com/) | Coimbatore | (d) | Injection moulding + tool development | INFERRED | candidate |
| S19 | [Tooling Temple](https://toolingtemple.com/precision-moulds-and-components/plastic-injection-moulds-manufacturer-coimbatore/) | Coimbatore | (d) | Mould making + moulding; acrylic, PC, nylon | INFERRED | candidate |
| S20 | [Tekno Plastic Systems](https://www.teknoacrylic.com/) | Coimbatore (Annur) | (c)/(d) | Acrylic products since 1994 + moulded components | INFERRED (sheet) | candidate |
| S21 | Ashwin Plastic Industries ([IndiaMART](https://m.indiamart.com/ashwin-plastic-industries/pmma-acrylic-tube.html)) | Mumbai | (c) stock | Extruded PMMA tube 5–150 mm OD | INFERRED | candidate |
| S22 | [Bests Industrial and Trading](https://aquatosun.en.made-in-china.com/) | Hefei, CN | (e) | Sells SS and glass lily pipes with price/MOQ; trading company | CONFIRMED (sells product; not a factory) | longlisted — sample required |
| S23 | Beijing Uuidear ([store](https://uuidearaqua.com/collections/lily-pipe), [Alibaba](https://uu.en.alibaba.com/)) | Beijing, CN | (e) | Glass, SS, metal jet pipes and skimmers; name indicates trading | CONFIRMED (sells); manufacturing UNVERIFIED | longlisted — sample required |

Directory pointers not individually assessed: [Ambala lab-glass list](https://lubics.in/top-laboratory-glassware-manufacturers-in-ambala/), [Shamboo Scientific](https://www.ssgwlab.com/), [Goel Scientific](https://goelscientific.com/), [Justdial Chennai lab glassware](https://www.justdial.com/Chennai/Lab-Glassware-Manufacturers/nct-10290415), [Justdial Coimbatore electropolishing](https://www.justdial.com/Coimbatore/Stainless-Steel-Electropolishing-Services/nct-11968913). Alibaba listings (AQUAPRO SS; "same factory as ADA" glass; Hebei glass skimmer) exist but prices and company details did not render — UNVERIFIED.

## 5. Cost data points (PUB unless marked; not quotations)

| Item | Value | Basis / source |
|---|---|---|
| SS 304 welded tube 12.7 × 1.21 mm | ₹79/m | Price list, undated ([Roopam Steel](https://www.roopamsteel.com/stainless-steel-pipe-tube-price-list.html)) |
| SS 304 welded tube 19.05 × 1.21 mm | ₹116.6/m | same |
| SS 316L premium over 304 | "+5 %" (Roopam) vs "15–25 %" ([Mahadev](https://mahadevdairypharmafitting.com/blog/latest-ss-pipe-price-per-meter-per-kg-per-foot/)) | Inconsistent claims |
| SS 316L seamless tube | ₹300/kg | [IndiaMART listing](https://www.indiamart.com/proddetail/stainless-steel-seamless-tube-316l-4132207233.html) |
| Borosilicate tube | ₹115/kg (26 × 2.8 mm, Ambala) – ₹295/kg (32 mm coloured, Delhi) | [IndiaMART](https://m.indiamart.com/impcat/borosilicate-glass-tube.html) |
| SS electropolishing | ₹120/kg (Coimbatore); ₹250–580/sq ft (Chennai) | IndiaMART categories |
| PVD on SS | ₹300/sq ft; some items ₹500/pc | Crystal PVD |
| Pipe laser cutting | ₹50–800/m nationally | IndiaMART category |
| Courier, Delhivery Surface, first 0.5 kg + each 0.5 kg, incl. GST | ₹44.78 + 16.42 (within city) … ₹58.22 + 37.31 (rest of India) | [iCarry rate card, 1 Aug 2026](https://www.icarry.in/icarry-sample-rates-by-zones.pdf); volumetric divisor 5000 |
| Example volumetric effect | 54 × 28 × 10 cm box = 3.0 kg volumetric → EST ₹160–250 rest-of-India surface | EST from card — **keep packs short** |
| Material in one SS set | EST ₹60–150 (0.7–1.0 m of 304 welded tube) | Material is a minor cost; labour, finishing and setups dominate |

**Import duty (PUB aggregator, rates as at 13 May 2026, citing CBIC/ICEGATE) — broker must confirm classification and rates:** 7020 00 90 other articles of glass, BCD 10 %, ≈32.28 % effective; 7017 20 00 lab glassware, ≈32.28 % (avoid this classification for an aquarium accessory); 7326 90 99 other steel articles, BCD 15 %, ≈40.39 %, SIMS; 7306 40 00 SS welded tube, ≈40.39 %, SIMS + BIS; 7307 29 00 SS fittings, ≈40.39 %; 3926 90 99 plastic articles, ≈40.39 % ([EximPe 70200090](https://eximpe.com/hsncode-finder/70200090), [73269099](https://eximpe.com/hsncode-finder/73269099), [39269099](https://eximpe.com/hsncode-finder/39269099)). The aggregator shows an AIDC component on these lines, which is unusual — **treat as questionable**. IGST (18 %) in these totals is creditable for a GST-registered importer; the non-creditable part is roughly BCD + social welfare surcharge [I].

**Domestic GST:** 18 % at heading level for 7017, 7020, 7306, 7307, 7326, 3926 after the 22 Sep 2025 rationalisation (Notification 9/2025-CT(Rate), per [TaxGuru chart](https://taxguru.in/goods-and-service-tax/notification-9-2025-ctrate-complete-hsn-wise-gst-rate-chart-effective-22nd-sept-2025.html)). Verify the 8-digit line with a CA.

## 6. RFQ question lists (for later use; not sent)

**Stainless fabrication (bender / laser / end-former / finisher)**

1. Min/max OD and min wall for CNC mandrel bending; minimum centre-line radius for 12.7/16/19 mm × 0.8–1.2 mm without wrinkling; ovality limit.
2. Existing dies for these OD/CLR combinations? New die cost, lead time, tooling ownership.
3. Tube laser: minimum chuck OD, achievable slot width (e.g. 0.8–2 mm), internal dross/burr, cut before or after bending.
4. End forming: maximum flare ratio of OD; bead rolling for hose retention; alternative spun flare + TIG.
5. TIG with internal back-purge? Heat-tint removal method?
6. Passivation to ASTM A967 and electropolish to ASTM B912 — certificates per lot? Can the bore be electropolished?
7. PVD: coating type (TiN/CrN/TiCN/DLC), thickness, adhesion test, lot-to-lot colour, any continuous-immersion data.
8. 316L tube with EN 10204 3.1 MTC and BIS licence mark; PMI verification at incoming.
9. Lubricants and degreasing/ultrasonic cleaning before packing.
10. First-article inspection report, gauges, capability on bend angle.
11. Price at 10 / 25 / 50 / 100 / 200 / 1,000; setup charges per lot; lead time; capacity.
12. Scratch protection and packing; defect history on decorative stainless parts.
13. Confidentiality and non-sale of Trophic-specific forms.

**Borosilicate glassblower**

1. Tubing brand and grade (3.3?), available OD/wall and tolerances; supplier declaration.
2. Repeat to drawing + master sample? Tolerances on hook gap, termination diameter, overall height, bend angle.
3. Forming method for flared terminations; mould/jig cost and ownership.
4. Slot cutting method, minimum slot width, chipping control.
5. Annealing schedule; 100 % polariscope inspection?
6. Price at 10 / 100 / 500 / 1,000; lead time; how many glassblowers can make the form.
7. In-process breakage; who bears transit breakage to Coimbatore; packaging used; drop-test history.
8. Cleanliness (DI rinse, residue-free); GST invoice; sample cost; confidentiality.

**Acrylic:** tube source (cast vs extruded) and tolerance; bend radius on 16–22 mm tube without whitening; annealing; solvent, cure and residual-monomer removal; slot method; price and lead time.

**Injection moulding (after design freeze):** resin for float/clip (PP, POM, PC), CoA, heavy-metal-free colourants; prototype aluminium vs P20 vs H13; family mould; cost, shot life, lead time, ownership; tolerances; piece price at 1k/5k/20k; ISO/IATF; T1 sample count.

**China OEM:** factory or trader (factory name/address, audit); actual grade with batch MTC and acceptance of PMI rejection; wall, bore finish, passivation; FOB price per 100/500/1,000, sample price, lead time, pack size; private-label MOQ; country-of-origin marking; any design patents or IP complaints; HS code on invoice; defect and spares policy.

## 7. Specialist recommendations (advisory; decisions belong to the owner)

1. Prove route (b) first: one-piece bent 316L tube with laser-cut slots, formed termination, rolled hose beads, passivated or electropolished; dark PVD only as a tested variant. Candidate sample sources S01, S02, S05/S06, S07–S09.
2. Buy benchmark samples from S22/S23 plus one branded set for teardown (wall, grade by PMI, welds, finish, slot width, pack). Low cost, high information.
3. Glass only if the owner's product decision requires transparency; prototype locally, pilot from Ambala; budget pack development and breakage.
4. No injection moulds until skimmer/clip design is frozen and volume exceeds ~2,000/yr.
5. IP attorney freedom-to-operate search and Indian design filing decision **before any public reveal**.
6. Confirm the current status of the stainless pipes and tubes QCO before buying tube; require BIS-marked tube with 3.1 MTC if it applies.

## 8. Compliance, product claims and IP — questions for professionals (no clearance given)

| Topic | Finding | Status | Who verifies |
|---|---|---|---|
| **Legal Metrology (Packaged Commodities) Rules 2011** | Retail packs need Rule 6 declarations (manufacturer/packer/importer name and address, common name, net quantity e.g. "1 set", month/year of manufacture or import, MRP incl. taxes, consumer care; country of origin for imports). E-commerce listings must display them (Rule 6(10)). **LMPC Amendment Rules 2026** add a searchable country-of-origin filter duty for platforms from **1 July 2026** ([SCC Online summary](https://www.scconline.com/blog/post/2026/02/21/legal-metrology-packaged-commodities-amendment-rules-2026-explained/)). Importers of packaged goods may need registration (Rule 27, verify) | FACT (secondary summaries) + verify text | Legal Metrology consultant / counsel |
| **Consumer Protection (E-Commerce) Rules 2020** | Sellers provide country of origin and seller details for display. A "Made in India" claim must reflect genuine domestic manufacture; mixing imported parts into a domestic SKU is a misrepresentation risk | Flag | Counsel |
| **BIS — Stainless Steel Pipes and Tubes QCO 2025** (IS 17875 seamless / IS 17876 welded) | In force Feb 2025, mandatory Aug 2025; covers the tubes, not stated to cover articles made from them ([BIS PDF](https://www.bis.gov.in/wp-content/uploads/2025/02/Stainless-Steel-Pipes-and-Tubes-QCO-2025.pdf)). Finished lily pipe likely outside scope. **November 2025 steel QCO suspensions/withdrawals may affect it** ([Business Standard](https://www.business-standard.com/economy/news/the-shift-qco-rollbacks-gather-steam-suspended-for-55-steel-products-125111401460_1.html); [consultancy summary](https://www.consultancycounsel.com/post/bis-qco-update-nov-2025)) — status on 2026-09-17 **not confirmed** | Open | BIS consultant; steel.gov.in |
| **SIMS** | Steel Import Monitoring System registration required before importing Chapter 73 lines | FACT (aggregator) | Customs broker |
| **Glassware QCOs** | Exist for specific laboratory glassware (e.g. beakers); none found for aquarium pipes or "other articles of glass". Do not market or classify as laboratory glassware | Flag | BIS consultant |
| **Product claims** | Avoid "food grade", "FDA", "surgical/medical grade" (a competitor uses "surgical-grade"). State facts with evidence ("316L stainless, passivated", with MTC). Tie "shrimp safe" to a defined internal test. "Borosilicate 3.3" only with tubing declaration | PROPOSED claim policy | Counsel + QA |
| **Design protection (Designs Act 2000)** | New, original shape/configuration judged by eye; prior publication anywhere (including social media and marketplace listings) destroys novelty — **file before public reveal**. Term 10 + 5 years; e-filing fee ₹1,000 for natural persons/startups/small entities, ₹4,000 others ([Intepat summary](https://www.intepat.com/blog/industrial-design-e-filing-fee-structure-in-india); [IP India eDesign](https://online.ipindia.gov.in/eDesign)). Functional features need patents, not design registration | FACT (secondary) | IP attorney |
| **Freedom to operate** | The lily pipe originated with ADA / Takashi Amano ([ADA story](https://www.adana.co.jp/en/history/story_02.html)) and has been widely copied for 20+ years, so the generic form is **probably** not protected in India — **inference, not clearance**. Newer spin, skimmer, rotating-elbow and metal-jet forms may carry current design registrations or CN/US utility models; searches found no specific lily-pipe patent, but aquarium flow devices are actively design-patented (e.g. [US D410992](https://patents.justia.com/patent/D410992)). "Lily Pipe" wording and ADA trademark status in India to be checked | Open | IP attorney: Indian Design Office (Locarno classes), Google Patents/Espacenet/CNIPA, WIPO Global Design Database; ADA, Chihiros, Week Aqua, ZRDR, FZONE, Aqua Worx trade dress |
| **Trophic trade mark** | A conflict with "Trophic Labs" (Singapore) and phonetic proximity to "Tropica" were flagged in earlier owner work outside this repository | Open, cross-product | IP attorney |

## 9. Is Coimbatore the best place to manufacture? (location assessment, added 2026-09-17)

**Question asked by the owner:** is Coimbatore the best option for manufacturing the proposed stainless set? **Short answer: Coimbatore is the right home for Trophic's own work (final inspection, assembly, packing, dispatch, supplier management) and plausibly for finishing, but public evidence does not yet show a Coimbatore shop that can do the critical step — thin-wall, small-diameter stainless tube bending and end forming. The strongest public match for that step is in Chennai.** This is desk evidence only; a sample round decides it.

| Location | Steps it could do | Public evidence (2026-09-17) | Distance / oversight | Cost effect (see [MANUFACTURING_COST_AND_MARGIN.md](../costing/MANUFACTURING_COST_AND_MARGIN.md) §4) | Assessment |
|---|---|---|---|---|---|
| **Coimbatore** | Final QC, clip parts, packing, dispatch; PVD; electropolishing; laser cutting; later moulding; tube bending **unproven** | PVD on SS incl. black (Crystal PVD, INFERRED); SS electropolishing listed ₹120/kg (Arunn Coats, UNVERIFIED); pipe laser cutting listings (UNVERIFIED); strong injection moulders (Roots Polycraft IATF 16949, INFERRED). **Tube bending: directory names only (S02).** A follow-up search of a Coimbatore "CNC bending services" directory page returned mainly press-brake **sheet** bending locally (e.g. Acetech, 0.5–6 mm sheet), with the tube benders listed being in Bengaluru and Pune ([TradeIndia Coimbatore CNC bending](https://www.tradeindia.com/coimbatore/cnc-bending-services-city-228082.html)) | Trophic's base; no travel | Lowest logistics (+≈1 % COGS) | **Best for integration and QC. Not evidenced as best for tube forming** |
| **Chennai** | Tube cutting, CNC bending, end forming (flare, bead, swage), welding, prototyping; electropolishing; PVD; SS tube stock | Polyfit re-checked 2026-09-17: 5-axis CNC bending 4.76–120 mm OD in carbon steel, **stainless** and aluminium; flaring, swaging, beading, bulging; welding; prototyping; pan-India delivery ([Polyfit](https://polyfit.co.in/tube-bending/), INFERRED strong). Electropolishers S07/S08, PVD S06, stockist S10 | ≈510 km by road ([Yatra](https://www.yatra.com/distance-between/distance-from-chennai-to-coimbatore.html)); overnight train or bus; first-article trips needed | +≈5 % COGS at 100 sets | **Best evidenced location for the forming step** |
| **Pune** (and Bengaluru) | Tube bending and assemblies | Pune has several CNC tube bending and assembly service providers serving automotive, EV and agriculture ([Wadhokar](https://www.wadhokar.com/products/cnc-tube-bending-and-assembly-services-in-pune/), [TradeIndia Pune](https://www.tradeindia.com/pune/cnc-pipe-bending-services-city-213577.html)); stated ranges are generic, small thin-wall stainless unconfirmed. Bengaluru listing found is mild steel 10–50 mm, 1–5 mm wall (Indotech) | Far (Pune) / nearer (Bengaluru); costlier oversight | +≈12 % COGS at 100 sets (Pune) | **Backup** if Tamil Nadu samples fail |
| **Ambala** | Borosilicate glass | SGC Labs, JSGW (INFERRED) | ≈2,500 km; fragile freight | Not applicable to stainless | Only if glass is chosen |
| **China (import)** | Finished sets | Trading-company listings (S22, S23) | Import clearance | Landed ≈₹2,460 in a Trophic box | Benchmark and teardown only |

**Why distance matters less than capability:** logistics and first-article trips add only ≈₹10–140 per set at a 100-set lot (≈1–12 % of COGS). Scrap from wrinkled thin-wall bends, per-bend pricing and minimum lot charges each move COGS more than that. Proximity mainly buys faster prototype iteration and easier quality control.

**PROPOSED sourcing sequence (not a decision):**

1. Send the stainless RFQ (§6) to Polyfit (Chennai) **and** at least two Coimbatore candidates (S02 names, plus any shop found by local visit), asking specifically for thin-wall 12.7–19 mm stainless mandrel bending and end forming samples.
2. Run finishing (passivation/electropolish, and PVD coupons only if a dark finish stays open) in Coimbatore if samples pass, otherwise Chennai.
3. Keep inspection, clip assembly, packing and dispatch in Coimbatore from the start.
4. If a Coimbatore shop passes V-S2 at a price within ≈₹50 per set of Chennai, move forming to Coimbatore (scenario L1); otherwise run scenario L2 (Chennai forming, Coimbatore QC/pack).
5. Keep Pune or Bengaluru as the fallback for forming.
