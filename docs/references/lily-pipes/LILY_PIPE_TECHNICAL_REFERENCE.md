# Lily Pipe Technical Reference — function, compatibility, materials, failure modes

**Applies to:** `AQ-LP-A` (product folder `products/aquarium/lily-pipes/`) · **Index:** `docs/references/REFERENCE_INDEX.md` LPREF

**Status:** RESEARCH · **Researched:** 2026-09-17 · **Re-check by:** 2027-03 (hose data after V-M1) · **Nothing here is a design value.**
Every calculation marked **EST** is an untested hand estimate for order of magnitude only. Pages were read through a summarising fetch; check primary PDFs before any figure becomes a requirement. Tags: [LILY_PIPE_RESEARCH_BRIEF.md](LILY_PIPE_RESEARCH_BRIEF.md) §5. Hose data: [sources/hose_compatibility.csv](sources/hose_compatibility.csv).

---

## 1. Dimensional vocabulary — use these five terms, never a bare "13 mm"

| Term | Symbol used here | Meaning | Where labels mislead |
|---|---|---|---|
| **Hose internal diameter** | hose ID | Bore of the flexible hose; the first number in "12/16" | "5/8 in" in the US is Oase's 16/22 **ID** (15.9 mm) [M] |
| **Hose external diameter** | hose OD | Outside of the hose; the second number in "12/16" | Sunsun HW-304 hose sold as 19/27 by one retailer and 19/25 by another [R] |
| **Pipe external diameter** | pipe OD | Outside of the rigid glass/steel pipe that goes *into* the hose; market "10 / 13 / 17 mm" | Pipes are sold by OD; buyers read it as hose size ([UKAPS 13/17 mm](https://www.ukaps.org/forum/threads/13mm-17mm-lily-pipes.19420/)) |
| **Pipe internal diameter** | pipe ID (bore) | Flow bore of the rigid pipe = pipe OD − 2 × wall | Almost never published; ADA walls ~2 mm vs thinner clones [F]; Chihiros Pro states 1.2 mm wall [R] |
| **Nominal commercial label** | label | Whatever the seller writes ("13 mm", "M", "12/16 or 13 mm") | Fluval states one number ("14.5 mm", "17 mm") without saying ID or OD [M]; a Resun hose listed 22 mm measured 25 mm [F] |

**Fit rule published by Oase:** pipe OD should be about **1 mm larger than hose ID** for a secure push fit ([Oase](https://us.oase.com/blogs/upgrading-equipment/upgrading-tubing-and-glassware)) [M]. Aquasabi: 10 mm pipe ↔ 9/12 hose; 13 mm ↔ 12/16; 17 mm ↔ 16/22; wet both parts, warm the hose end, keep **1.5–2 cm overlap** ([Aquasabi hose wiki](https://www.aquasabi.com/aquascaping-wiki_filtration_hose-diameters-and-glassware)) [R].

**Consequence [I]:** a Trophic specification must state pipe OD with tolerance, pipe bore, and the hose ID/OD it is verified against — and verification must use **measured** hoses, because labels are not consistent between suppliers.

## 2. Hose compatibility of common canister filters

Condensed; URLs and notes per row in the CSV.

| Hose (ID/OD, mm) | Filters (label as published) | Tag | Confidence |
|---|---|---|---|
| **9/12** | Eheim Classic 150 (with 12/16); Oase FiltoSmart 60 | [R→M][M] | Medium |
| **12/16** | Eheim Classic 250 (440 l/h), 350 (620 l/h); Oase FiltoSmart 100; JBL CristalProfi e402/e702/e902 greenline; Tetra EX 400/600/800 Plus; Dennerle Scaper's Flow (hang-on, max glass 10 mm); Chihiros "M" glassware | [M][R] | High |
| **16/22** | Eheim Classic 600; Eheim Professionel 4+ 250/350/600; Eheim Professionel 5e (suction side 16.0/22.0, verify per variant); Oase BioMaster/Thermo 250–850; Oase FiltoSmart 200/300; JBL e1502; Tetra EX 1200; **Sunsun HW-302/303/402B/403B** (spare-hose retailer); Chihiros "L" | [M][R] | High, except Sunsun (retailer) |
| **19/25 or 19/27** | Sunsun HW-304/404B/704/HW-3000; JBL e1902 (19/25 [M]) | [R][M] | Low for Sunsun (conflicting) |
| **≈25 mm ("1 in")** | Fluval FX4/FX6 (community; Fluval publishes no diameter); Resun EF-2800U (measured) | [F] | Low |
| **Ambiguous** | Fluval 105–107/205–207 "14.5 mm", 305–407 "17 mm" (ID or OD unstated; one user says 107 is 16/22); Sunsun HW-602/603B "12 mm ID" | [M][F][R] | **Unresolved** |
| **Not found** | Hygger, Aqueon QuietFlow | — | Measure |

**Pattern [I]:** 12/16 and 16/22 cover most branded mid-market canisters; the "large" class (19–25 mm) is poorly served by lily pipes ("difficult to source" for FX6, [UKAPS](https://www.ukaps.org/forum/threads/fluval-fx6-pipe-to-big.37548/)). Which sizes dominate **Indian** installed filters (Sunsun and other Chinese brands are common in Indian stores [I]) is unknown and is the most important compatibility question for India ([VALIDATION_PLAN.md](../../../products/aquarium/lily-pipes/verification/VALIDATION_PLAN.md) V-C2, V-M1). This is cross-product decision **X3**.

**Hose materials and grip:** most filter hose is plasticised PVC; silicone is softer, works well on glass, not gas-tight ([Garnelio](https://www.garnelio.de/en/more/blog/aquarium-technology/aquarium-hoses-and-their-use-in-aquaristics)) [R]. Thick vinyl kinks easily ([aquariumscience.org](https://aquariumscience.org/index.php/14-5-piping/)) [F/secondary]. All flexible plastics creep, so barbed or interference seals loosen over time (same source). Smooth glass or plain tube retains the hose only by interference and friction; a bead or barb resists pull-off better [I] — **no pull-off data found; test**. PVC stiffens in cold; Ooty winters matter for fitting force [I].

## 3. Flow: rated vs actual, and why tank volume alone is the wrong sizing basis

**Published:** Fluval gives both pump output and "filter circulation": 107 550→360 LPH (65 %), 307 1150→780 (68 %), FX6 3500→2130 (61 %) [M]. Others publish only a maximum (zero head, no media) plus Hmax (Oase BioMaster² 1.3–2.2 m) [M]. No full pump curves found.

**Field reports:** real flow typically 40–60 % of label ([UKAPS stated vs actual flow](https://www.ukaps.org/forum/threads/eheim-external-filters-stated-flow-actual-flow.36418/)); Resun EF-2800U measured ≈1990 l/h at 37 in head against 2800 rated ([MonsterFishKeepers](https://www.monsterfishkeepers.com/forums/threads/resun-ef-2800u-740gph-canister-filter-review-and-test.373696/)) [F]. Guidance "~10× turnover" ([2Hr Aquarist](https://www.2hraquarist.com/blogs/filters-overview/filter-buying-checklist)) does not say rated or actual [F].

**Why volume-based sizing fails [I]:**

1. Installed flow is 40–68 % of label and falls further as media and prefilters clog (Eheim's Pro 4+ has a flow "Xtender" for this reason).
2. A canister loop is a closed siphon when full; static cabinet height largely cancels. **Dynamic losses** — hose friction, bends, intake strainer, prefilter, media, outlet, inline reactors/heaters — set the flow the pump curve can deliver.
3. Losses rise with velocity squared, so hose size dominates at higher flow (EST table below). The rigid pipe's bore is narrower than the hose, adding loss out of proportion to its length.
4. Circulation depends on the **jet** (termination geometry and placement), not just litres per hour; a single lily outlet may leave dead zones a spray bar would not ([Barr Report](https://barrreport.com/threads/spray-bar-vs-lilly-pipe-vs-poppy-outflow.8288/)) [F].
5. Tank geometry matters: long-shallow and tall-narrow tanks of equal volume need different jet reach.

**Hose friction — EST, not validated** (25 °C water, smooth straight hose, Blasius friction factor, fittings and ribbing excluded):

| Flow | Hose ID | Velocity | Head loss per metre | 3 m of hose |
|---|---|---|---|---|
| 600 l/h | 12 mm | 1.47 m/s | ≈0.24 m/m | ≈0.7 m |
| 600 l/h | 16 mm | 0.83 m/s | ≈0.06 m/m | ≈0.2 m |
| 1000 l/h | 12 mm | 2.46 m/s | ≈0.6 m/m | ≈1.8 m |
| 1000 l/h | 16 mm | 1.38 m/s | ≈0.15 m/m | ≈0.45 m |

Interpretation [I]: 1000 l/h through 12 mm hose would consume most of a 1.3–1.4 m Hmax pump by itself, consistent with makers moving to 16/22 hose near 900–1000 l/h. **Rig measurement required** ([VALIDATION_PLAN.md](../../../products/aquarium/lily-pipes/verification/VALIDATION_PLAN.md) V-T3).

## 4. Outlet geometry, placement, surface agitation and noise

| Market term (vendors disagree) | Geometry | Described effect | Source |
|---|---|---|---|
| Classic lily | Flared bell turned slightly up | Moderate surface movement; limits CO₂ loss | [Aquasabi wiki](https://www.aquasabi.com/aquascaping-wiki_filtration_lily-pipe) [R] |
| Bubble / poppy | Rounded end directing flow upward | Much more intense surface agitation; more O₂, less film | same |
| Jet / straight | Nozzle ≈ pipe bore | Stronger, longer reach | same |
| Spin / loop | Two lateral openings | Decelerates and disperses the jet | same |
| Violet / funnel | Directs flow downward | Minimal surface disturbance | same; Cal Aqua Labs [R] |
| Outflow skimmer attachment (Neo Skimmer) | Draws air into the jet | "Shreds surface film"; "65 % more air volume" (claim) | [Aquasabi Neo Skimmer](https://aquasabi.com/Aquario-Neo-Skimmer) [R→M] |

**Principles:**

- Continuity v = Q/A. **EST:** 600 l/h through a 10 mm bore ≈ 2.1 m/s; through 13 mm ≈ 1.26 m/s. A submerged jet loses its dynamic head at the exit (loss coefficient ≈ 1): ≈0.23 m head at 2.1 m/s, ≈0.08 m at 1.26 m/s ([Engineering ToolBox](https://www.engineeringtoolbox.com/minor-loss-coefficients-pipes-d_626.html)) [T].
- **Flares do not slow the jet by their area ratio** unless flow stays attached; short, sharply flared lips separate, so much of the jet leaves near pipe velocity, spread by the lip. Lip radius relative to jet width sets whether the jet hugs the surface (Coandă attachment, roughly when jet width/radius < 0.5, [Coandă effect](https://en.wikipedia.org/wiki/Coand%C4%83_effect)) [T][I]. This is a design lever and a CFD/rig question, not a styling choice.
- **Surface action [I]:** an upward-turned end meets the surface with momentum and breaks film (more gas exchange); a lily a few centimetres below the surface, angled slightly up, creates a slow surface current that carries film toward the intake or skimmer.
- **CO₂ trade-off:** more agitation allows higher CO₂ injection safely but off-gasses CO₂; O₂ and CO₂ exchange are independent ([2Hr Aquarist](https://www.2hraquarist.com/blogs/choosing-co2-why/how-to-push-the-limits-of-co2-safely)) [F/expert]. **No quantitative off-gassing data by outlet type found** — test with pH/drop checker/DO logging.
- **Placement:** outlet opposite the CO₂ diffuser so the downdraft carries bubbles through the tank (2Hr Aquarist) [F/expert].
- **Noise [I]:** splashing, air entrainment (poppy or Neo-style set too high) and air returning to the intake are audible. No dB data for lily pipes found.

## 5. Intake: restriction, clogging, livestock protection, maintenance

- **Open area [I]:** total slot area should be several times the bore area. EST example (hypothetical geometry, not a proposal): 10 slots × 1 × 30 mm = 300 mm² vs 78.5 mm² bore → ratio ≈3.8, mean slot velocity ≈0.56 m/s at 600 l/h. As slots clog, velocity at the remaining slots rises.
- **Shrimp size:** newly hatched dwarf shrimp 1–2 mm; adults 15–40 mm ([Green Aqua](https://greenaqua.hu/en/blog/post/how-to-protect-shrimp-from-filter-and-surface-skimmer-intake)) [R].
- **No manufacturer publishes a shrimp-safe slot width.** Guards are described as "so fine that even the tiniest shrimp cannot be sucked in" without a figure ([Aquasabi](https://www.aquasabi.com/aquascaping-wiki_invertebrate_making-the-filter-shrimp-proof)) [R]. Measure competitors; derive from test, not from marketing.
- **Prefilter sponges** reduce flow "significantly" and clog "very easily" (sometimes every couple of days); a plastic screen mesh showed "very little" reduction ([MFK FX6 prefilter](https://www.monsterfishkeepers.com/forums/threads/pre-filter-on-fx6-reduced-flow.723461/)) [F]. Unquantified — test.
- **Maintenance:** glassware cleaning once or twice a month (Aquasabi) [R]; slotted glass inlets are hard to brush and usually need the hose removed ([UKAPS](https://www.ukaps.org/forum/threads/cleaning-glass-lily-pipes.57187/)) [F]. A removable or open-ended intake tip addresses the moment breakage occurs [I].

## 6. Surface skimmers

Two product classes:

1. **Self-powered skimmer** (e.g. Eheim skim350: own 5 W pump, float protrudes up to 3 cm, i.e. ≈3 cm level range, vinegar descaling) ([Aquasabi](https://www.aquasabi.com/EHEIM-skim350), [manual](https://www.manualslib.com/manual/820891/Eheim-Skim-350.html)) [M/R].
2. **Inflow-mounted floating skimmer** sharing canister suction with a bottom intake — the lily-pipe type.

**Behaviour and failure physics:**

- The float cup sits at the surface; water spills over its rim into the inflow. The water level must stay within the float/slot range (patent background, [US 2022/0159937](https://patents.justia.com/patent/20220159937)) [T].
- **Bouncing/oscillation:** buoyancy vs suction imbalance; at high flow (1200 l/h case) the float bobs and draws air into the filter; debris under the float worsens it; fixes were throttling the bottom regulator, cleaning, enlarging holes, limiting float travel ([UKAPS skimmer bouncing](https://www.ukaps.org/forum/threads/surface-skimmer-bouncing.56168/)) [F].
- **Re-adjustment** needed after the filter stops or after water changes ([UKAPS steel](https://www.ukaps.org/forum/threads/steel-lily-pipes-advice.63951/)) [F].
- **Air ingestion:** trapped air in the canister "can cause noise"; never let the pump run dry (Oase BioMaster² manual) [M].
- **Flow split [I]:** skimmer and bottom intake are parallel paths; as the bottom strainer or prefilter clogs, more flow goes through the skimmer, pulling the float down and starting air ingestion. A skimmer therefore needs an adjustable bypass or a self-limiting float, and a specified flow window per size. **Rig test 300–1500 l/h, clean and clogged.**
- **Level variation [I]:** open rimless tanks evaporate daily in Indian summers; float range must follow a study of top-up habits, not the Eheim 3 cm reference.

## 7. Mounting, rims and clearances

| Tank (reference) | Glass | Source |
|---|---|---|
| ADA Cube Garden 15 | 4 mm | [ADA tanks](https://www.adana.co.jp/en/contents/products/na_tank/detail01.html) [M] |
| ADA 20C–60 low | 5 mm | same |
| ADA 60P/60H/60×45 | 6 mm | same |
| ADA 90P | 10 mm | same |
| ADA 120 | 12 mm | same |
| ADA 150/180 | 15 mm | same |
| Aqua Zones ultra-clear cubes 20–30 cm (India) | 5 mm | [Aqua Zones](https://www.aquazones.in/ultra-clear-tanks-cubes/) [R] |
| Neo Holder / Chihiros Pro clamp accept | ≤ 12 mm | [R] |
| Dennerle Scaper's Flow hanger | ≤ 10 mm | [R] |

- **Locally built Indian tanks:** no published glass-thickness practice found — survey Coimbatore/Bengaluru builders (V-M3).
- A 4–15 mm range cannot be met by one fixed clip [I]; options are clip families by range or an adjustable clamp — **open**.
- **Methods in market:** suction cups (hold problems discussed in forums), rimless brackets in metal or clear acrylic, clamps with glass limits. Rimmed tanks: brackets often do not fit; pipes sit crooked from hose stiffness ([Aquarium Co-Op](https://forum.aquariumcoop.com/topic/32162-lily-pipe-brackets-for-rimmed-tanks/)) [F].
- **Load path [I]:** hose weight and stiffness (worse cold) create a bending moment at the hook; in glass this concentrates at the flame-worked bend; in clips it becomes point load on the glass edge.
- **Clearances to measure:** lid, light legs/arms (including Trophic AQ-LT mounts), rear wall, hose bend radius behind the tank (PVC minimum bend radius not published), cabinet cut-out passing hose OD plus quick-disconnects/valves.
- **Reference immersion depths** (not Trophic values): Chihiros glass M/L ≈165/175 mm; Dennerle hang-on ≈165 mm; Aqua Rebell OF4 ≈100 mm [R].

## 8. Materials, corrosion, finish and cleanability

### 8.1 Borosilicate 3.3 (e.g. SCHOTT DURAN, ISO 3585)

CTE 3.3×10⁻⁶ K⁻¹; transformation 525 °C; hydrolytic class HGB 1, acid S 1, alkali A 2; density 2.23 g/cm³; E = 63 GPa; thermal-shock guidance ≈120 K difference ([DURAN datasheet](https://www.cmscientific.com/info-sheets/Schott-duran-glass-material.pdf); [ISO 3585](https://www.iso.org/standard/24774.html)) [M][T]. Hot-water hose fitting is not the risk; **leverage and impact at flame-worked bends are**, and annealing after forming is a manufacturing control point [I]. Aquasabi warns not to use boiling water on ADA glass [R]. Soda-lime glass has roughly three times the expansion (commonly cited ~9×10⁻⁶ K⁻¹, not sourced this pass) [I].

### 8.2 Stainless steel

- **Grades:** 304 (18–20 Cr, 8–10.5 Ni) vs 201 (16–18 Cr, 3.5–5.5 Ni, 5.5–7.5 Mn) — 201 tea-stains and rusts in chloride environments ([Walmay](https://walmaystainless.com/201-vs-304-stainless-steel-manganese-grades/)) [T-secondary].
- **Chloride tolerance** (continuous, neutral pH, ambient): 304 ≈200 ppm, 316 ≈1000 ppm; **chlorine** tolerance 304 ≈2 ppm, 316 ≈5 ppm ([ASSDA](https://www.assda.asn.au/component/content/article?id=271%3Achlorine-and-chloride--same-element%2C-very-different-effect)) [T]. Freshwater tanks are normally far below 200 ppm chloride [I], but **CO₂-lowered pH, crevices (hose over tube, float adjuster), weld heat tint and bleach cleaning** reduce margin. The common 1:1 bleach soak used for glass is far above 304/316 chlorine tolerance — **stainless parts need different cleaning instructions**.
- **Why "stainless" lily pipes rust [I, consistent with sources]:** 201 or unknown grade; free iron embedded by bending/cutting tools and not passivated; unpickled weld heat tint; crevice corrosion; bleach soaks. Field rust evidence in freshwater is anecdotal.
- **Passivation** ASTM A967 (nitric or citric; verification by water immersion, humidity, salt spray, copper sulfate, ferroxyl) ([Astro Pak A967](https://astropak.com/astm-a967/)); **electropolishing** ASTM B912 (finish specified by purchaser; current edition B912-26 per [Astro Pak B912](https://astropak.com/astm-b912/)) [T-secondary]. Electropolish reduces surface roughness and is expected to reduce biofilm adhesion [I].
- **Bore quality [I]:** welded-and-drawn tube carries an internal weld bead unless bead-conditioned; seamless or bead-conditioned sanitary tube (ASTM A269/A270 family — confirm scope) avoids a crevice in the bore.

### 8.3 Polymers

- **Acrylic (PMMA)** — resistant to IPA ≤50 %, ethanol ≤15 %, hypochlorite, H₂O₂ ≤40 %, citric ≤20 %, vinegar, ammonia; **not** resistant to ethanol >30 %, methanol, acetone ([ACRYLITE chart](https://www.acrylite.co/files/content/acrylite.co/documents/ACRYLITE-Chemical-Resistance-Chart.pdf)) [M]. Stressed bends and solvent joints craze at lower concentrations; brushes haze it [I].
- **Polycarbonate** — **attacked by ammonia even at 0.1 %** and 1 % NaOH ([PC resistance guide](https://www.theplasticshop.co.uk/plastic_technical_data_sheets/chemical_resistance_guide_polycarbonate_sheet.pdf)) [T]; unsuitable where users may use ammonia glass cleaner [I].
- **PETG** — used by Aquario Neo ("shatterproof") [R]; chemical data not researched.

### 8.4 Coatings and dark finishes

No aquarium-specific evidence found on PVD or black-coating adhesion, chipping or leaching under immersion and brushing — **evidence gap**. Any coated wetted part needs adhesion testing after immersion and brush cycles, leach/ecotoxicity checks relevant to shrimp, and chemical resistance to citric acid and H₂O₂ before it can be proposed [I].

### 8.5 Cleaning-agent compatibility (synthesised [I] from §8 sources)

| Agent | Borosilicate | SS 304/316 | Acrylic | Polycarbonate |
|---|---|---|---|---|
| Bleach soak (1:1 household) | OK [R] | **Avoid long soaks** [T] | Resistant [M] | Not listed |
| Citric acid (descaling) | OK | OK (also a passivation chemistry) | ≤20 % [M] | 10 % [T] |
| Vinegar | OK | OK | Resistant [M] | Resistant [T] |
| H₂O₂ 3–6 % | OK | OK short-term [I] | ≤40 % [M] | 30 % [T] |
| Alcohol | OK | OK | IPA ≤50 %; ethanol >30 % not resistant | IPA at 23 °C |
| Ammonia glass cleaner | OK | OK | Resistant | **Not resistant** |
| Pipe brush | Leverage breaks thin glass [R] | OK | Scratches [I] | Scratches [I] |

Hose materials (PVC, silicone) against these agents: not verified.

## 9. Failure modes and preliminary risk register

Likelihood (L) and severity (S) are **preliminary judgements [I]** on a 1–3 scale for prioritising tests, not an FMEA. "Evidence" gives the tier of what exists today.

| ID | Failure mode | Mechanism | Evidence today | L | S | Mitigation direction (not a requirement) | Verification route |
|---|---|---|---|---|---|---|---|
| R01 | Hose slips off / seeps at pipe | Plastic creep on smooth interference fit; cold stiff hose; re-used heated hose end | [F] creep; worry only, no flood report | 2 | 3 | Retention bead/barb; OD tolerance to measured hoses; insertion length; optional clip | Pull-off at 15/30 °C; weeks-long creep with pressure (V-T2) |
| R02 | Glass breaks during cleaning/hose removal | Leverage on thin glass; stress at bends | [F][R] STRONG | 3 (glass) | 2 | Avoid glass route, or thicker walls, anneal, removal aid | Bend-moment, drop, thermal shock (glass only) |
| R03 | Glass crack at hook bend in service | Hose moment + residual stress | [I] only | 2 (glass) | 3 | Strain relief; clamp near bend | Static load + polariscope |
| R04 | Mount slips; pipe falls in or tilts | Suction-cup vacuum loss; clip wrong for glass thickness; hose torque | [F] RECURRING | 2 | 2 | Clip families by thickness; contact material | Long-duration hold under hose load on 4–15 mm glass, rimless and rimmed (V-T8) |
| R05 | Clip damages or chips glass edge | Point load; hard contact | [I] | 1 | 3 | Pad material; force limit | Edge inspection after cycles; force measurement |
| R06 | Skimmer float sticks, bounces, ingests air | Buoyancy vs suction imbalance; debris; level change | [F] STRONG | 3 (if skimmer) | 2 | Flow window; bypass/regulator; guided float | Rig 300–1500 l/h clean/clogged (V-T4) |
| R07 | Canister noise, impeller wear, airlock | Air entrained by skimmer or outlet; air pocket | [M] Oase; [F] | 2 | 2 | Skimmer limits; outlet submerged; priming guidance | Acoustic + restart test (V-T10) |
| R08 | Rust / tea staining on stainless | 201 grade, free iron, heat tint, crevices, bleach | [T] mechanism; [F] anecdotal | 2 | 2 | 316L; passivate/electropolish; no wetted welds; no bleach instruction | A967 verification; immersion in CO₂-acidified water + cleaning cycles; PMI (V-T7) |
| R09 | Biofilm/algae inside pipes | Light + nutrients; roughness | [R][F] STRONG for glass | 3 | 1 | Brushable bore end-to-end; smooth bore; opaque material | Field interval study; brushability check |
| R10 | Intake clogging and flow loss | Slots or prefilter load | [F] | 2 | 2 | Open-area ratio; coarse guard option | Standard-debris clog-time test (V-T5) |
| R11 | Shrimplets trapped at intake/skimmer | Slot > 1–2 mm juveniles; approach velocity | [F] STRONG; [R] | 2 | 2 | Slot and velocity targets from test | Competitor slot survey; live-shrimp test (V-T5) |
| R12 | Hose kinks, flow collapses | Thin-wall PVC bends; cabinet routing | [F] | 2 | 2 | Bend guidance; rim geometry that avoids tight hose bends | Bend-radius test |
| R13 | Too much / too little surface agitation (CO₂ loss or poor O₂) | Termination and depth | [F/expert] | 2 | 2 | Aimable or depth-adjustable outlet | pH/drop checker/DO logging (V-T9) |
| R14 | Dead zones, poor circulation | Concentrated jet; tank geometry | [F] | 2 | 1 | Jet spread; placement guidance | Dye test; later CFD |
| R15 | Coating chips, flakes or leaches | Adhesion loss under brushing/chemicals | **None found** | ? | 3 | Do not propose until tested | Adhesion + leach tests (V-A3) |
| R16 | Polymer crazing | Solvent + stress | [M][T] | 2 (polymer) | 2 | Material choice; annealing; cleaning label | Stressed-strip immersion |
| R17 | Product does not fit customer's hose | Label ambiguity between brands | [M][R][F] | 3 | 2 | Compatibility chart from **measured** hoses | Calliper survey (V-M1) |
| R18 | Separable joint leaks, loosens or re-aims | Vibration, tolerance, fouling | [I] | 2 | 2 | Joint design; retention | Leak and vibration test |
| R19 | Laser mark corrodes | Passive layer damaged | [I] | 2 | 1 | Mark above water or re-passivate | Immersion of marked coupons |
| R20 | Transit damage | Long thin parts; courier handling | [R] indirect | 3 (glass) / 1 (SS) | 2 | Pack design | ISTA-style drop tests (V-P1) |

## 10. What needs testing, simulation or specialist review

**Physical testing (bench rig):** hose calliper survey; pull-off and fit force vs pipe OD and finish at 15/30 °C plus creep; flow vs configuration (hose size and length, pipe bore, termination, prefilter, media state) for 3–4 canisters to check §3 estimates; skimmer flow window and air ingestion; intake open area, slot width and clog time, shrimp safety; mount hold; stainless A967 verification, immersion and PMI of competitor pipes; gas exchange vs termination and depth; noise. Procedures and proposed acceptance criteria: [VALIDATION_PLAN.md](../../../products/aquarium/lily-pipes/verification/VALIDATION_PLAN.md) §3.

**CFD (later, only after rig data exists to calibrate it):** termination lip radius and angle (jet attachment, spread, surface interaction); tank circulation by outlet type and tank aspect ratio; slot-array suction uniformity; skimmer cup inflow and float force balance.

**Specialist review:** Manufacturing/Sourcing (bend and end-forming limits, bore finish, passivation vendors); CMF (finish and clip appearance within engineering limits); QA (acceptance criteria at the prototype gate); Plant Science (CO₂/O₂ criteria, livestock safety); an external corrosion/materials specialist for any coating on wetted parts and for cleaning-chemical exposure.

**Gaps (not found):** hose diameters for Hygger, Aqueon, most Resun and Sunsun from the maker; Fluval ID vs OD; pump curves; any branded shrimp-safe slot width; prefilter flow penalty; underwater PVD durability; Indian local tank glass practice; Eheim hose material; soda-lime CTE source.
