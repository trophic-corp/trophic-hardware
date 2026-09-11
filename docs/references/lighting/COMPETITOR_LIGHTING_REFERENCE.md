# Competitor Lighting Reference — planted-aquarium LED fixtures

**Status:** RESEARCH · **Researched:** 2026-09-11 (Lighting/Electronics specialist, synthesised by the main session) · **Re-check by:** 2027-03 for prices and lineups
**Applies to:** `AQ-LT-A` (Core), `AQ-LT-B` (WRGB); architectural insight only

**Nothing in this document is a Trophic requirement.** CLAUDE.md §3 rule 6 applies:
no drawing, model or contract may cite it. It exists so later sessions do not
re-research the same brands. Evidence classes: **[M]** manufacturer site or
manual, **[D]** authorised distributor or brand-region site, **[R]** retailer
listing, **[F]** community field observation, **[I]** inference. Prices are as
displayed on the access date, Indian retail including GST where the retailer
says so.

---

## 1. Why this matters to Trophic

Three things the market shows that shape the aquarium platform hypothesis:

1. **Every serious brand tiers inside one housing.** Twinstar B/E/S, Chihiros Slim/II/Pro and Week Aqua Standard/Pro use the same extrusion and length classes and differ by LED population, RGB:white ratio and controller grade. Length scales as LED count on one pitch. This is delayed differentiation practised by the incumbents, and it supports Trophic's Core/WRGB shared-platform hypothesis without proving Trophic's cost case.
2. **The controller and the adapter are where products fail.** Field complaints cluster on inline Bluetooth controllers dying after power cycles, swollen or failed adapters, and mis-plugged adapters on identical barrel connectors across different rail voltages. Fixture LED arrays rarely fail. This shapes reliability testing (see `docs/engineering/LIGHTING_PROGRAM_ROADMAP.md` gate evidence) and the serviceability argument.
3. **The Indian Core price point is occupied by a thin-spec white-only product.** Neo Helios XP-300/450/600 sell at ₹1,910–3,999 with no published lumens, LED count, IP, adapter spec or warranty period, and two Indian retailers disclose it is an 8000 K white light despite "WRGB" marketing. An honest, measured spec sheet is itself a differentiator at this price.

## 2. Brand-by-brand

### Neo Helios (made in Zhongshan, China; Indian partner Umino Aquarium, Chennai)

| Item | Finding | Class |
|---|---|---|
| Family | Flat Solar **XP** (flat panel, 30–120 cm), **Flat Nano S3 / S3 Plus** (8 W / 13 W clip-on), Solar Color Booster | M |
| XP sizes and wattage | XP-300 16 W (30–40 cm), XP-450 24 W, XP-600 32 W (60–75 cm), XP-800 46 W, XP-900 48 W, XP-1200 55–64 W (retailers disagree) | R |
| Spectrum | Retailers Aquazones and Something Fishy state "not a WRGB or RGB light – an LED light of 8000 K"; Aquariums India copy says "full spectrum WRGB chips". Conflicting; treat as white-only until verified | R, conflicting |
| Controls | Single on/off button, no dimming, no schedule | R |
| Construction, mounting | Aluminium body; bracket legs 10 cm (300/450) or 25 cm (larger) | R |
| PSU | "2-pin US flat plug" adapter; voltage/current not published | R |
| IP, warranty | Site claims "IP67" and "comprehensive warranty" with no period | M |
| Indian price | XP-300 ₹2,400–2,550; XP-450 ₹1,910 (sale)–2,250; XP-600 ₹3,250–3,999; XP-900 ₹4,999; Nano S3 ₹699–1,599 | R, 2026-09-11 |
| Field | Almost no independent failure reports; one Amazon.in review says growth "not that good" vs a household LED | F |
| Lesson | The incumbent at Trophic's Core price. Thin published spec; no dimming or schedule; no stated warranty | I |

### Chihiros (Shanghai Ogino Biotechnology)

| Line | Channels | 60 cm class figure | Sizes | Notes | Class |
|---|---|---|---|---|---|
| C II / C II RGB | white 16 W 1500 lm / RGB 20 W 1580 lm | — | 20–36 cm | nano, BT dimming | R |
| A II | white ~8000 K, 3 rows, 67 × 10 mm section | 26 W, 2450 lm, 60 LED, IP43 | 30–120 | A II Max 601 50 W 4700 lm | R |
| Universal WRGB | W + RGB, 3000–15000 K | 29 W 2245 lm | 55–150 | **IP67**, clip-in for rimmed tanks | R |
| WRGB II Slim | RGB 3-in-1 | 45 W 2400 lm 40 LED, 584 × 128 × 15 mm, IP43 | 30–120 | | D |
| WRGB II | RGB 3-in-1 | 67 W 5900 lm 60 LED, 600 × 140 × 18, IP43 | 30–120 | 10/12 mm glass | D |
| WRGB II Pro | WRGB 4-in-1 | 74 W 6630 lm 60 LED, IP43 | 30–120 | | D |
| Vivid 2 | RGB pendant, fan | 130 W 12 200 lm 160 RGB | 60–90 | | R |

- **LED count scales linearly** (30/50/60/90/120 LEDs for 30/45/60/90/120 cm) on a constant 140 mm section: one MCPCB pitch scaled in length [I from D data].
- **Controller placement:** marketed as "built-in Bluetooth", but Chihiros' own support forum diagnosed a WRGB II Pro 120 fault by unplugging the Bluetooth controller from the adapter, and sells a "Bluetooth Controller Replacement" SKU that "uses a different connector type than the LED fixture"; an owner describes "the Bluetooth module built into the cord" [M support forum, F]. **Inference: WRGB II family uses an inline controller between adapter and passive fixture.** RESEARCH REQUIRED per model.
- **PSU catalogue:** 12 V (1/3.5/5 A) and 36 V (0.8–5.5 A) families, "standard" or "waterproof" connector; model mapping not published [M]. A Slim owner plugged a Chihiros Doctor adapter in by mistake: same connector, wrong rail [M support].
- Manufacturer warns the light is "not intended for operation under sealed lids… corrosion due to water vapor" [D].
- **Warranty:** 1 year official (excludes water damage, physical damage, **power-surge damage**, modifications) [M]; 2 years via EU distributor [D]; India 1 year with serial registration (Aquazones) [R].
- **Indian price (Aquazones, 2026-09-11):** WRGB II 60 ₹24,725; WRGB II Pro 60 ₹28,275 (out of stock); Slim 60 ₹15,525 [R].
- **Field complaints [F]:** controller dead after ~1 year following a power cycle; red-blink fault with hot, smelling controller; green channel shutting down after 40 min at ≥ 75 % (WRGB60 II); red LEDs failing (Pro 90); schedule not executing; shock/spark from 2-pin adapter with a travel converter (UKAPS); slow support; grey-market purchases void support. Support's explanation for controller death: "unstable current may cause it short circuit".

### Week Aqua

- Ladder: S (entry WRGB), M/MD (30–45 cm), L (slim strip), P (panel), T (pendant), Z (spotlight), V (clip). Pro variants add UV: L600 Pro 55–65 W, L900 Pro 85 W, L1200 Pro 110 W, P600 Pro 90 W "100+10 LEDs" 5400 lm, Z400 Pro 90 W "100+20" 5850 lm; 5-channel RGB+UV, Bluetooth app, 7 presets, timer [R].
- **PSU and controller:** adapter families DC 24 V (0.5–5.5 A) and DC 36 V (1–5.56 A); "Bluetooth replacement B2.0 (24 V)" and "Bluetooth replacement 36 V" sold as separate parts; 2-pin extender for WRGB lines vs 4-pin for others [R, M]. Inference: inline Bluetooth controller keyed to rail voltage; 2-wire link on WRGB lines. RESEARCH REQUIRED.
- **Warranty:** 1 year at retail (Singapore); direct international store: 30-day replacement plus an optional paid 1-year warranty (US$60, parts free, customer pays shipping) [M].
- **Indian price (Aquazones, mostly sold out):** S-series ₹5,999–7,999; M Pro ₹13,900–21,375; P and L Pro ₹17,955–38,900; T90 Pro ₹19,750 [R].
- Field: no substantive complaint threads found; RESEARCH REQUIRED.

### Twinstar (Korea)

- Three tiers in one 60 cm form factor: **B-line** 60B 22 W 1741 lm; **E-line** 600EA III 40 W 2500 lm, 36 white + 64 RGB, 600 × 117 × 17 mm, 6500–7000 K; **S-line** 600S III 52 W 3250 lm, 14 white + 126 RGB; S IV 3620 lm; S V 59 W [R]. Tier = RGB:white ratio and LED density on the same extrusion and legs [I].
- **Fixture passive, control inline:** 600S adapter DC 24 V 3.5 A; inline dimmer with 5.5 × 2.5 mm barrel, DC 5–24 V, ≤ 150 W, 7-step dimming, 6/8/10 h timer, sunrise/sunset; LightControl Manual / Standard (BT) / Pro (BT + 4-colour, bundled only with S-line V) [R]. E-line owners mention 12 V adapters and PC-PSU substitutes [F].
- Mounting: acrylic legs (EA), metal fixed legs (SM), adjustable/pendant (SA). Certifications KC, CE; IP not stated [R].
- **Warranty:** 2 years (UK retailer), 1 year (US) [R]; region-dependent.
- **Indian price:** 600EA III ₹18,000 (Aquazones); 600S III ₹27,499 (Indian Aquarium). Aquazones requires an unboxing video within 48 h for LED claims [R].
- **Field [F]:** adapters "very low quality and fail often", swollen adapter; flicker linked to overheating (owners added fans); diffuser gaps and moisture ingress; acrylic-mount QC; intermittent flashing after lights-off.

### ONF (Taiwan)

- Flat Nano+ 15 W 1300 lm 7000 K, **IP54**, BT, 4–20 dim levels; Flat One+ 60 70 W 5600 lm **CRI 90**, tunable 3000–6500 K, 100–270 V input, 50 000 h; restores previous setting on power-up; BT 10 m; iOS groups 2–8 devices [M FAQ, R]. White-only tunable CCT, no RGB. Warranty 1 year [M].
- Field [F]: schedule randomly firing 100 %; heatsink adequacy questioned; CCT shifts yellow at low dim; support experience poor.

### ADA (Japan)

- Solar RGB: 130 W pendant, 160 RGB LEDs, 3000–3500 lm, 9000–12000 K, separate electronic ballast (1.5 kg) [M]. Aquasky RGB 60: 40 W, 70 RGB LEDs, no dimming, 6 mm glass only; Aquasky RGB II 60: 108 W, 7200 lm [R]. Warranty period not found; RESEARCH REQUIRED.
- Indian price: Aquasky RGB 60 ₹52,000 at Aquariums India, listed "warranty: No" [R].

### Others, compressed

| Product | Architecture facts | Class |
|---|---|---|
| Fluval Plant 3.0 | 22/32/46/59 W, 6 independent channels, BT app, **IP67**, 120° LEDs, **3-year warranty** | M/R |
| Aquael Leddy Slim Link 36 W | 2750 lm, 1–7000 K, app, sunrise/sunset/storm, 2-year | M |
| Hygger 957 | 20–72 W, IP68, DC 15 V / 20 V adapters (2 A / 3 A), inline controller, 24/7 cycle | M |
| NICREW RGB+W 24/7 | 17/22/39 W, inline controller + IR remote, IP67 | R |
| UNS Titan 1 | 90 W, 200 Epistar RGB, aluminium pendant, suspension | M |
| Netlea AT5 D Pro | 130 W, 140 × 4-in-1 chips, DC 36 V 5 A, 50 000 h | R |
| Kessil A360X Tuna Sun | 90 W, 19 V DC, onboard + K-Link/0–10 V, Wi-Fi dongle optional, 12-month | R |
| AI Prime 16HD FW | 55 W, 16 LEDs (6 CW, 4 WW, 2 B, 1 R, 1 G + moon), BLE app | R |

## 3. Architectural patterns across brands

1. **Controller placement, three patterns.** (a) Inline module on the DC cable (Twinstar, Chihiros WRGB II by support evidence, Week Aqua, NICREW, Hygger): fixture stays passive, controller is a replaceable spare and the dominant failure item; one fixture sells in manual / BT / BT-colour tiers by swapping the module. (b) In-fixture electronics (ONF, Fluval, Aquael, AI, Kessil): better IP story, Core carries the cost. (c) Separate ballast (ADA Solar RGB).
2. **Spectrum tiers.** Entry = fixed white or white+RGB with intensity-only dimming (Neo Helios, Chihiros A II, Twinstar B); mid = 3-ch RGB (WRGB II, Slim); premium = 4-ch WRGB 4-in-1 (Pro, Netlea) or 5-ch RGB+UV (Week Aqua Pro). Tunable-white (ONF, Aquael) is a separate CRI-led branch.
3. **Tiering inside a brand**: same extrusion, same length classes, different LED population and ratio; length scaling is linear LED count on one pitch.
4. **PSUs standardised on 2–3 DC rails per brand** (Chihiros 12/36 V; Week Aqua 24/36 V; Twinstar 12/24 V; Netlea 36 V; Kessil 19 V; Hygger 15/20 V), sold as spares, with identical barrel connectors across rails: a documented cause of mis-plugging.
5. **Ingress**: strip lights are mostly IP43 or unrated; IP67/68 is the differentiator of Fluval, Hygger, NICREW and Chihiros Universal. Chihiros disclaims lidded tanks outright.
6. **Mounting**: acrylic or metal legs on rimless glass 6–12 mm; clip-in for rimmed European tanks; suspension for pendants.

## 4. Warranty norms

| Brand | Period | Class |
|---|---|---|
| Chihiros | 1 yr official; 2 yr EU distributor; India 1 yr with registration | M, D, R |
| Twinstar | 1 yr (US) / 2 yr (UK); India not stated | R |
| Week Aqua | 1 yr retail; 30 days direct + paid 1-yr option | M, R |
| ONF | 1 yr | M |
| Kessil | 12 months | R |
| Aquael | 2 yr | M |
| Fluval | 3 yr | M |
| Neo Helios | "comprehensive", no period | M |
| ADA | not found; Indian retailer lists "no warranty" | R |

Indian retailer conditions (unboxing video within 48 h) substitute for manufacturer service. Indian Consumer Protection Act obligations for a domestic brand: RESEARCH REQUIRED.

## 5. What the field complaints imply for reliability testing

- **Adapter**: thermal and ageing at Indian mains with surge, brownout and 230 V tolerance; Twinstar swelling, the Chihiros surge exclusion and its "unstable current" explanation all point at the PSU as the weakest link. Specify surge/EFT immunity and derating at 40 °C.
- **Inline or in-fixture controller**: power-cycle endurance (thousands of hot-plug and cold-start cycles), thermal soak in a cable loom, short-circuit and reverse-polarity protection, wrong-rail mis-plug tolerance.
- **Fixture**: thermal derating so a channel does not self-shed at ≥ 75 %; flicker under heat; red-channel colour stability; humidity and condensation exposure including the lidded-tank case; diffuser seam ingress.
- **Firmware**: schedule persistence through power loss, RTC drift, BLE reconnect after app restart.
- **Safety**: plug and adapter mechanical fit; BIS / IS 13252 compliance of the adapter for India, NEEDS VALIDATION.

## 6. Lessons applicable to Trophic (inference, not requirements)

- Core at ₹2,500–3,500 competes with Neo Helios XP at ₹1,910–3,999. The gap to fill is dimming, scheduling, published measured performance, a stated warranty and a stated IP class, not raw output.
- Shared extrusion, shared MCPCB pitch and a shared DC rail let Core (fixed spectrum, one channel) and WRGB share tooling; the industry populates fewer or different LEDs rather than cutting new housings.
- Whether the controller is inline or in-fixture is the pivotal architecture decision: inline is cheaper for Core, field-replaceable and tier-by-accessory but is the item that fails and runs hot; in-fixture gives a better ingress story but makes Core carry the electronics cost. NEEDS DECISION (Systems Architect and Industrial Design).
- Keyed connectors per rail voltage, or one rail across the platform, removes the mis-plug failure class seen at Chihiros and Week Aqua.
- Schedule and state must persist on the device; ONF restores state and Chihiros schedule misfires are a recurring complaint.

## 7. Not verified — RESEARCH REQUIRED

Chihiros adapter voltage/current per model and definitive controller placement for Slim, A II, Universal, Pro (manual pages blocked); Week Aqua LED counts, PAR/CRI, adapter-to-model mapping, 2-pin vs 4-pin protocol, Indian field experience; Neo Helios LED count, lumens, adapter, IP, warranty, whether XP is truly white-only, Umino's service model; Twinstar E-line adapter spec, IP rating, Korean warranty, LightControl Pro spec; ADA warranty and Aquasky RGB II controls; Netlea and UNS Titan Indian pricing; any independent PAR/PPFD data for Neo Helios, Week Aqua, Twinstar III; CRI for any RGB-only fixture (only ONF publishes CRI 90).

## Sources (all accessed 2026-09-11)

Chihiros: https://chihiros.eu/led-light/chihiros-wrgb-ii-pro · https://chihiros.eu/chihiros-wrgb-ii · https://chihiros.eu/led-light/chihiros-wrgb-ii-slim · https://chihiros.com/pages/warranty-policy · https://www.chihirosaquaticstudio.com/products/chihiros-power-supply-replacement · https://bbs.chihirosaquaticstudio.com/threads/huge-problem-with-my-wrgb-ii-pro-120.117/ · https://bbs.chihirosaquaticstudio.com/threads/wrgb-ii-slim-not-turning-on.101/ · https://jungleaquatics.com/products/chihiros-universal-wrgb-with-controller · https://greenaqua.hu/en/chihiros-aii-601-60-cm-led-lampa-26-w-2450-lm.html · https://greenaqua.hu/en/chihiros-c2-led-lampa-16-w-1500-lm.html · https://buceplant.com/products/chihiros-rgb-vivid2-led-light-silver-10th-anniversary-edition · https://www.aquazones.in/chihiros-wrgb-ii-60-cm-led-light/ · https://www.aquazones.in/chihiros-wrgb-ii-pro-60-cm/ · https://www.aquazones.in/chihiros-wrgb-ii-slim-60-cm-led-light/ · https://www.plantedtank.net/threads/chihiros-wrgb-ii-dead.1319266/ · https://www.ukaps.org/forum/threads/chihiros-owners-warning.73294/ · https://www.ukaps.org/forum/threads/chihiros-wrgb2-pro-problem.71134/
Neo Helios: https://www.neo-helios.in/ · https://www.aquazones.in/neo-helios-xp-series-flat-led-aquarium-light/ · https://somethingfishy.co.in/product/neo-helios-xp-series-flat-led-planted-aquarium-light/ · https://www.aquariumsindia.com/shop/lighting-units/planted-aquarium/neo-helios-wrgb-plant-led-xp-300/ · https://www.aquariumsindia.com/shop/lighting-units/planted-aquarium/neo-helios-wrgb-plant-led-xp-900/ · https://www.amazon.in/NeoHelios-Spectrum-Planted-Aquarium-Suitable/dp/B09GMQ2X4W · https://petkadai.com/product/neo-helios-xp-600-planted-light-suits-60-75-cms-32w/ · https://www.indiamart.com/proddetail/neo-helios-xp-600-flat-led-light-24595402812.html · https://www.petzlifeworld.in/products/neo-helios-flat-nano-s3-plus-13w-full-spectrum-planted-tank-aquarium-light · https://esperar.shop/product/neo-helios-flat-nano-s3-plus/
Week Aqua: https://eastoceansg.com/products/week-aqua-l1200-pro-light · https://eastoceansg.com/products/week-aqua-adapter-accessories-draft-mode · https://weekaqua.world/products/week-aqua-l900-pro-rgb-uva-aquarium-lightning-week-aqua-international · https://weekaqua.world/products/avis-option-1718000211314-660658 · https://aquaticmotiv.com/products/week-aqua-p-series · https://www.aquazones.in/brand/week-aqua/
Twinstar: https://www.aquazones.in/twinstar-iii-600ea-wrgb-led-light/ · https://indianaquarium.com/products/twinstar-600s-vr-iii-planted-tank-led-light · https://www.finestaquatics.co.uk/twinstar-led-light-iii-sa-600 · https://www.amazon.com/Twinstar-Aquarium-LED-Light-B-Line/dp/B08LMYQLMP · https://aquaforestaquarium.com/products/twinstar-inline-dimmer-w-built-in-timer-function · https://aquaforestaquarium.com/products/twinstar-lightcontrol-standard · https://www.amazon.com/Twinstar-Aquarium-Lighting-Spectrum-Controller/dp/B0CW3NLXFK · https://www.ukaps.org/forum/threads/twinstar-600e-v3-power-adapter.70038/ · https://www.ukaps.org/forum/threads/twinstar-light-issue.56095/ · https://www.ukaps.org/forum/threads/twinstar-900e-fail-night-before-holiday.67061/
ONF: https://www.onf.com.tw/pages/support?locale=en · https://www.onf.com.tw/en/products/onf-flat-nano-plus-stand-black · https://www.akvarieboden.net/products/onf-flat-one-plus-led-light-60-cm5600-lm-70-w · https://www.plantedtank.net/threads/onf-flat-one-problems.1326743/ · https://www.plantedtank.net/threads/thoughts-on-onf-flat-one-led-light.1229122/
ADA: https://www.adana.co.jp/en/solar_rgb/lighting.html · https://www.aquariumsindia.com/shop/lighting-units/planted-aquarium/ada-aquasky-rgb-60/ · https://aquaforestaquarium.com/products/ada-aquasky-rgb-ii-60-for-w60cm-tank-with-glass-thickness-of-6mm
Others: https://fluvalaquatics.com/us/shop/product/plant-3-0-bluetooth-led-32w-24-34-61-85-cm · https://www.aquael.com/products/aquaristics/aquaristics/leddy-slim-link/ · https://www.hyggerstore.com/product/hygger-957-auto-on-off-led-with-extendable-brackets-aquarium-light/ · https://www.amazon.com/NICREW-Aquarium-Spectrum-Freshwater-Extendable/dp/B08LBB85LC · https://ultumnaturesystems.com/titan-1/ · https://veroaquatics.com.au/products/netlea-at5-d-pro-130w-wrgb-app-controlled-freshwater-led-lights · https://www.bulkreefsupply.com/a360x-controllable-led-aquarium-light-tuna-sun-kessil.html · https://fresh.bulkreefsupply.com/prime-16-hd-led-freshwater-light-white-body-aqua-illumination.html
