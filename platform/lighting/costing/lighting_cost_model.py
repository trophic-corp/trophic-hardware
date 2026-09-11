#!/usr/bin/env python3
"""
Trophic lighting — early planning BOM, commercial and programme cash model.

THIS IS A PLANNING MODEL, NOT COMMERCIAL TRUTH. Every input is labelled with an
evidence class:
  QUOTE   confirmed supplier quotation (none yet)
  RMKT    researched market price class, dated (see supplier landscape / competitor ref)
  EST     engineering estimate by the main session, 2026-09-11
  ASSUME  owner or planning assumption, configurable
  TBD     unknown; placeholder value carried so totals compute, must be replaced

Run:  python3 lighting_cost_model.py > LIGHTING_BOM_COST_MODEL.md
Edit the ASSUMPTIONS blocks; do not hand-edit the generated markdown.
"""
from collections import OrderedDict

DATE = "2026-09-11"
GST = 0.18

# --------------------------------------------------------------------------
# Volume tiers and per-category volume factors (multiplier on the 100-unit base)
# --------------------------------------------------------------------------
TIERS = OrderedDict([
    ("proto", 5), ("pilot", 15), ("25", 25), ("50", 50), ("100", 100), ("scaled", 500)])

VF = {  # category: (proto, pilot, 25, 50, 100, scaled)   evidence: EST
    "extrusion": (4.0, 1.5, 1.3, 1.15, 1.0, 0.85),   # proto = stock profile + CNC, no die
    "machining": (3.0, 2.0, 1.5, 1.2, 1.0, 0.6),
    "anodise":   (3.0, 2.0, 1.6, 1.3, 1.0, 0.8),     # minimum charges dominate small lots
    "endcaps":   (3.0, 2.0, 1.5, 1.2, 1.0, None),    # scaled uses moulded caps (explicit)
    "leds":      (2.0, 1.5, 1.3, 1.15, 1.0, 0.8),    # proto = cut tape
    "pcbfab":    (2.5, 1.8, 1.5, 1.2, 1.0, 0.7),
    "elec":      (1.8, 1.5, 1.3, 1.15, 1.0, 0.8),
    "pcba":      (3.0, 2.0, 1.5, 1.2, 1.0, 0.7),
    "psu":       (1.3, 1.2, 1.1, 1.05, 1.0, 0.8),
    "optics":    (2.5, 1.8, 1.4, 1.2, 1.0, 0.7),
    "assembly":  (3.0, 2.0, 1.5, 1.2, 1.0, 0.7),
    "packaging": (2.0, 1.8, 1.5, 1.3, 1.0, 0.7),
    "connector": (1.5, 1.3, 1.2, 1.1, 1.0, 0.8),
}
SCRAP = {"proto": 0.05, "pilot": 0.05, "25": 0.04, "50": 0.03, "100": 0.03, "scaled": 0.02}  # EST
MOULDED_CAPS_SCALED = 80   # ₹ per pair, EST, requires ~₹3–5 lakh tool (not in unit cost)
MOULDED_PUCK_SCALED = 70   # ₹ per Smart Module enclosure at scale, EST, tool ~₹3 lakh

# --------------------------------------------------------------------------
# Unit BOM lines at the 100-unit tier, ₹.  (value, category, evidence, note)
# --------------------------------------------------------------------------
EXT_KG_PER_M = 0.8      # ASSUME — profile mass; needs a section concept
EXT_RS_PER_KG = 380     # RMKT — ₹300–420/kg finished 6063, supplier landscape §2.1
def extrusion(L): return round(EXT_KG_PER_M * (L + 0.02) * EXT_RS_PER_KG)

def core(L, n_white, n_red, strings):
    return OrderedDict([
        ("Extrusion body", (extrusion(L), "extrusion", "RMKT/ASSUME", f"{EXT_KG_PER_M} kg/m × {L+0.02:.2f} m × ₹{EXT_RS_PER_KG}/kg; profile mass is an assumption")),
        ("CNC end machining", ({0.30:150,0.45:160,0.60:170}[L], "machining", "RMKT", "₹40–150 per end class, two ends")),
        ("Bead-blast + Type II anodise", ({0.30:110,0.45:130,0.60:150}[L], "anodise", "EST", "per-piece incl. minimum-charge share")),
        ("End caps, machined Al pair", (300, "endcaps", "EST", "moulded ₹80/pair at scale + tool")),
        ("LEDs: mid-power white", (n_white*8, "leds", "RMKT", f"{n_white} × ₹8 (Bridgelux/Nichia 3030 class, reel qty)")),
        ("LEDs: 660 nm red", (n_red*25, "leds", "RMKT", f"{n_red} × ₹25 (3030 red, reel qty)")),
        ("MCPCB", ({0.30:140,0.45:190,0.60:240}[L], "pcbfab", "RMKT", "Indian fab ₹200/pc listing class at MOQ 100, scaled by length")),
        ("CC driver stage", (110*strings, "elec", "EST", f"{strings} buck CC string(s) × ₹110 (IC + inductor + passives)")),
        ("Engine board: MCU, NTC, ID EEPROM, ideal diode/eFuse, UVLO/OVP, 5 V housekeeping buck, port load switch + TVS, FR-4", (340, "elec", "EST", "Lighting/Electronics 2026-09-11: engine board excl. drivers ₹400–700 class at 100 incl. housekeeping; mid value used")),
        ("DC input connector", (50, "connector", "EST", "barrel class; sealed circular ₹120+")),
        ("Control port connector", (80, "connector", "EST", "sealed 3–4 pin class, fixture side")),
        ("PCBA (SMT labour, two boards)", ({0.30:110,0.45:115,0.60:120}[L], "pcba", "EST", "Coimbatore EMS; setup charged separately")),
        ("Optical cover", ({0.30:80,0.45:110,0.60:140}[L], "optics", "EST", "PMMA cut sheet or profile")),
        ("Thermal interface material", ({0.30:12,0.45:16,0.60:20}[L], "elec", "EST", "")),
        ("Mounting hardware (legs, pads, fasteners)", (200, "machining", "EST", "machined/sheet at low volume")),
        ("Gaskets / seals", (35, "elec", "EST", "die-cut EPDM/silicone")),
        ("External adapter (certified)", ({0.30:480,0.45:480,0.60:650}[L], "psu", "RMKT", "24 V-class 36 W / 60 W BIS-registered adapter ₹400–700 class (Indian OEM); Mean Well GST higher")),
        ("Final assembly labour", (130, "assembly", "EST", "")),
        ("EOL test", (35, "assembly", "EST", "jig speaks the control protocol")),
        ("Packaging", ({0.30:110,0.45:125,0.60:140}[L], "packaging", "EST", "kraft carton + pulp/board insert + sleeve")),
    ])

def wrgb(L, n_col, n_white, channels):
    return OrderedDict([
        ("Extrusion body", (extrusion(L), "extrusion", "RMKT/ASSUME", "shared housing assumed (cost test pending); +20 % if a wider WRGB-only profile")),
        ("CNC end machining", ({0.30:170,0.45:180,0.60:190}[L], "machining", "RMKT", "")),
        ("Bead-blast + Type II anodise", ({0.30:110,0.45:130,0.60:150}[L], "anodise", "EST", "")),
        ("End caps, machined Al pair", (300, "endcaps", "EST", "")),
        ("LEDs: colour (R/G/B/deep red)", (n_col*35, "leds", "RMKT/EST", f"{n_col} × ₹35 (branded 3030 colour, reel/cut-tape mix)")),
        ("LEDs: high-CRI white", (n_white*10, "leds", "RMKT", f"{n_white} × ₹10")),
        ("MCPCB (denser, higher-k)", ({0.30:200,0.45:270,0.60:340}[L], "pcbfab", "EST", "")),
        ("CC driver stages", (105*channels, "elec", "EST", f"{channels} channels × ₹105")),
        ("Engine board: MCU (≥5 PWM), NTC, ID EEPROM, protection, 5 V housekeeping, port switch + TVS, FR-4", (420, "elec", "EST", "more PWM channels, 80 V-class parts if 48 V bus")),
        ("DC input connector", (50, "connector", "EST", "")),
        ("Control port connector", (80, "connector", "EST", "")),
        ("PCBA (SMT labour, two boards)", ({0.30:170,0.45:180,0.60:190}[L], "pcba", "EST", "")),
        ("Optical cover / diffuser", ({0.30:110,0.45:140,0.60:170}[L], "optics", "EST", "mixing diffuser; lens array would be higher")),
        ("Thermal interface material", ({0.30:15,0.45:20,0.60:25}[L], "elec", "EST", "")),
        ("Mounting hardware", (220, "machining", "EST", "rated for WRGB mass")),
        ("Gaskets / seals", (35, "elec", "EST", "")),
        ("External adapter (certified)", ({0.30:700,0.45:900,0.60:1100}[L], "psu", "RMKT", "60 / 90 / 120 W class; Mean Well GST or Indian OEM")),
        ("Final assembly labour", (220, "assembly", "EST", "")),
        ("EOL test", (70, "assembly", "EST", "per-channel photometric + thermal")),
        ("Packaging", ({0.30:180,0.45:200,0.60:220}[L], "packaging", "EST", "heavier board grade")),
    ])

SMART_MODULE = OrderedDict([
    ("MCU + radio module (ESP32-C3 class)", (160, "elec", "RMKT", "pre-approved module")),
    ("RTC + supercapacitor backup", (150, "elec", "RMKT", "RV-3028 class + supercap")),
    ("PCB (FR-4)", (35, "pcbfab", "EST", "")),
    ("Passives, port driver, protection, regulator", (90, "elec", "EST", "")),
    ("Buttons / status LED", (20, "elec", "EST", "")),
    ("Port connector + 1 m tether cable", (170, "connector", "EST", "sealed 3–4 pin + cable")),
    ("Enclosure (machined Al or polymer puck)", (260, "endcaps", "EST", "moulded ₹70 at scale + ~₹3 lakh tool")),
    ("Gasket", (20, "elec", "EST", "")),
    ("PCBA (SMT labour)", (90, "pcba", "EST", "")),
    ("Final assembly", (80, "assembly", "EST", "")),
    ("EOL test (radio, RTC, port)", (40, "assembly", "EST", "")),
    ("Packaging", (60, "packaging", "EST", "")),
])

SKUS = OrderedDict([
    ("Core 30", core(0.30, 20, 4, 1)),
    ("Core 45", core(0.45, 30, 6, 1)),
    ("Core 60", core(0.60, 40, 8, 2)),
    ("WRGB 30", wrgb(0.30, 24, 12, 5)),
    ("WRGB 45", wrgb(0.45, 36, 18, 5)),
    ("WRGB 60", wrgb(0.60, 48, 24, 5)),
    ("Smart Module", SMART_MODULE),
])

def unit_cost(bom, tier):
    ti = list(TIERS).index(tier); total = 0.0
    for name, (v, cat, ev, note) in bom.items():
        f = VF[cat][ti]
        if cat == "endcaps" and tier == "scaled":
            v = MOULDED_PUCK_SCALED if "Enclosure" in name else MOULDED_CAPS_SCALED; f = 1.0
        total += v * f
    return total * (1 + SCRAP[tier])

# --------------------------------------------------------------------------
# Commercial assumptions (ASSUME unless marked)
# --------------------------------------------------------------------------
GATEWAY = 0.02          # ASSUME — payment gateway + D2C platform, % of gross
SHIP = {"Core": 180, "WRGB": 260, "Smart Module": 90}   # ASSUME — packaging/shipping allowance ₹ per order line
WARRANTY = {"Core": 0.04, "WRGB": 0.05, "Smart Module": 0.05}   # ASSUME — reserve, % of COGS
DEALER_MARGIN = 0.25    # ASSUME — future dealer/distributor margin off retail incl. GST, for the "dealer floor" check

# Retail prices incl. GST, ₹ — ASSUME (positioning per competitor reference; see doc §5)
PRICES = OrderedDict([
    ("Core 30 Basic",   ("Core 30", None,          3499)),
    ("Core 30 Smart",   ("Core 30", "Smart Module", 4499)),
    ("Core 45 Basic",   ("Core 45", None,          3999)),
    ("Core 45 Smart",   ("Core 45", "Smart Module", 4999)),
    ("Core 60 Basic",   ("Core 60", None,          4499)),
    ("Core 60 Smart",   ("Core 60", "Smart Module", 5499)),
    ("WRGB 30 Standalone", ("WRGB 30", None,       7999)),
    ("WRGB 30 Smart",   ("WRGB 30", "Smart Module", 8999)),
    ("WRGB 45 Standalone", ("WRGB 45", None,       9999)),
    ("WRGB 45 Smart",   ("WRGB 45", "Smart Module", 10999)),
    ("WRGB 60 Standalone", ("WRGB 60", None,      12499)),
    ("WRGB 60 Smart",   ("WRGB 60", "Smart Module", 13499)),
    ("Smart Module (upgrade)", ("Smart Module", None, 1499)),
])

def family(sku): return "Smart Module" if sku.startswith("Smart") else ("WRGB" if sku.startswith("WRGB") else "Core")

def commercial(sku_key, tier, cogs_scale=1.0):
    engine, bundle, price = PRICES[sku_key]
    cogs = unit_cost(SKUS[engine], tier) * cogs_scale
    if bundle: cogs += unit_cost(SKUS[bundle], tier) * cogs_scale
    net = price / (1 + GST)
    gw = price * GATEWAY
    ship = SHIP[family(engine)]
    warr = cogs * WARRANTY[family(engine)]
    contrib = net - cogs - gw - ship - warr
    gm = (net - cogs) / net
    return dict(price=price, net=net, cogs=cogs, gw=gw, ship=ship, warr=warr, contrib=contrib, gm=gm, cm=contrib/net)

# --------------------------------------------------------------------------
# Programme plan quantities (ASSUME — see LAUNCH_PLAN.md)
# --------------------------------------------------------------------------
EP   = {"Core 30":1, "Core 45":2, "WRGB 45":2, "WRGB 60":1, "Smart Module":4}                  # tier proto
DVT  = {"Core 30":3, "Core 45":4, "Core 60":3, "WRGB 30":2, "WRGB 45":4, "WRGB 60":2, "Smart Module":14}   # tier pilot
B1   = {"Core 30":12, "Core 45":16, "WRGB 30":4, "WRGB 45":8, "Smart Module":30}               # tier 50
B2   = {"Core 30":20, "Core 45":30, "Core 60":15, "WRGB 30":8, "WRGB 45":15, "WRGB 60":12, "Smart Module":80}  # tier 100
B1_SALES = OrderedDict([("Core 30 Basic",6),("Core 30 Smart",6),("Core 45 Basic",6),("Core 45 Smart",10),
                        ("WRGB 30 Standalone",1),("WRGB 30 Smart",3),("WRGB 45 Standalone",2),("WRGB 45 Smart",6),
                        ("Smart Module (upgrade)",5)])
# Scenario B: WRGB-led first batch (ASSUME) — fewer Core, Core only as Smart bundles, 60 cm WRGB included
B1B  = {"Core 45":10, "WRGB 30":6, "WRGB 45":12, "WRGB 60":8, "Smart Module":36}
B1B_SALES = OrderedDict([("Core 45 Smart",10),("WRGB 30 Smart",6),("WRGB 45 Smart",12),("WRGB 60 Smart",8),
                         ("Smart Module (upgrade)",0)])

NRE = OrderedDict([  # (₹, evidence, note, cash class: 'expense' or 'inventory')
    ("Extrusion die", (40000, "RMKT/EST", "₹13.5k–35k listing class; finned profile assumed at the upper end", "expense")),
    ("Extrusion minimum run (150 kg negotiated)", (150*EXT_RS_PER_KG, "ASSUME", "500 kg standard MOQ would be ₹1,90,000; ~187 m ≈ 400 fixtures at 45 cm → stock", "inventory")),
    ("MCPCB MOQ carry (6 artworks × 100 pcs)", (90000, "RMKT/EST", "Indian fab folds NRE into MOQ 100; overrun is usable stock", "inventory")),
    ("PCBA stencils + setup, batch 1 (9 artworks)", (72000, "EST", "₹3–8k stencil + ₹5–15k setup per artwork, per run", "expense")),
    ("Packaging print run (sleeves, 2 designs)", (20000, "EST", "offset MOQ 500–1,000", "expense")),
    ("Test instruments: quantum sensor", (60000, "RMKT", "Apogee MQ-500 class", "expense")),
    ("Test instruments: thermal camera, bench PSU, e-load, DMM", (85000, "EST", "", "expense")),
    ("Spectroradiometer (rental / lab per design)", (30000, "EST", "", "expense")),
    ("Lab tests: IEC 62471, EMC pre-scan, salt fog, damp-heat box", (105000, "EST", "40k + 40k + 10k + 15k", "expense")),
    ("Regulatory: WPC ETA (module) + BIS scope consulting", (75000, "EST", "25k + 50k contingency; adapter bought registered", "expense")),
    ("Firmware + app development (external contract)", (200000, "ASSUME", "set to 0 if fully in-house; founder labour not costed", "expense")),
    ("Prototype consumables, spare boards, stock extrusion, CNC", (60000, "EST", "", "expense")),
    ("Field pilot logistics and support", (20000, "EST", "12 serialised units from DVT stock", "expense")),
])
DEFERRED_TOOLING = OrderedDict([
    ("End-cap injection mould", (400000, "RMKT", "₹2–8 lakh simple mould class; justified at ≥ ~300 units")),
    ("Smart Module puck mould", (300000, "EST", "justified at ≥ ~300 modules")),
])

# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------
def rs(x): return f"₹{x:,.0f}"
out = []
P = out.append
P(f"# Lighting BOM, Commercial and Programme Cash Model\n")
P(f"**Status:** EARLY PLANNING MODEL, NOT COMMERCIAL TRUTH · **Generated:** {DATE} by `lighting_cost_model.py` · **Owner:** main session\n")
P("Every input carries an evidence class: **QUOTE** (none yet), **RMKT** researched market class (dated, see the supplier landscape and competitor reference), **EST** engineering estimate, **ASSUME** configurable planning assumption, **TBD**. No line is a supplier quotation. Regenerate by editing the script's assumption blocks; do not hand-edit this file. Gross revenue, revenue excluding GST, gross margin, contribution and net profit are kept distinct throughout; **nothing here is net profit** because fixed operating expenses, salaries, marketing and R&D amortisation are not included except where §7 says so.\n")

P("## 1. Unit BOM at the 100-unit tier\n")
for sku, bom in SKUS.items():
    P(f"### {sku}\n\n| Line | ₹ at 100 | Category | Evidence | Note |\n|---|---:|---|---|---|")
    for n,(v,c,e,note) in bom.items(): P(f"| {n} | {v:,.0f} | {c} | {e} | {note} |")
    P(f"| **Subtotal + {SCRAP['100']*100:.0f} % scrap/rework** | **{unit_cost(bom,'100'):,.0f}** | | | |\n")

P("## 2. Unit cost by volume tier\n")
P("Volume factors per category (proto = hand-built on stock extrusion with cut-tape LEDs; scaled = 500 units with moulded end caps and puck). Scrap/rework 5 / 5 / 4 / 3 / 3 / 2 %.\n")
P("| SKU | " + " | ".join(f"{t} ({n})" for t,n in TIERS.items()) + " |\n|---|" + "---:|"*len(TIERS))
for sku,bom in SKUS.items():
    P(f"| {sku} | " + " | ".join(rs(unit_cost(bom,t)) for t in TIERS) + " |")
P("\nOwner planning figures for comparison (ASSUME, from the Phase 0 brief): Core small sizes ~₹1,400–1,600; WRGB ~₹10,000 / 14,000 / 19,000 at 100 units. **The bottom-up Core estimate is roughly 1.7–2× the owner figure at 100 units and approaches it only at the scaled tier with moulded caps; the bottom-up WRGB estimate is well below the owner figure.** Both gaps must be closed by RFQ, not by adjusting the model. See §8.\n")

P("## 3. Commercial model per SKU\n")
P(f"Assumptions: GST {GST*100:.0f} %; payment gateway/platform {GATEWAY*100:.0f} % of gross; packaging/shipping allowance Core ₹{SHIP['Core']}, WRGB ₹{SHIP['WRGB']}, module ₹{SHIP['Smart Module']}; warranty reserve Core {WARRANTY['Core']*100:.0f} %, WRGB {WARRANTY['WRGB']*100:.0f} % of COGS. Prices are positioning assumptions (see §5). Contribution = net revenue − COGS − gateway − shipping − warranty reserve. It is **not** net profit.\n")
for tier in ("50","100","scaled"):
    P(f"### At the {tier}-unit COGS tier\n\n| SKU | Retail incl. GST | Net ex-GST | COGS | Gateway | Ship | Warranty | Gross margin % | Contribution ₹ | Contribution % |\n|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for k in PRICES:
        c = commercial(k, tier)
        P(f"| {k} | {rs(c['price'])} | {rs(c['net'])} | {rs(c['cogs'])} | {rs(c['gw'])} | {rs(c['ship'])} | {rs(c['warr'])} | {c['gm']*100:.0f} % | {rs(c['contrib'])} | {c['cm']*100:.0f} % |")
    P("")

P("## 4. Sensitivity to COGS (contribution ₹ per unit at the 100-unit tier)\n")
P("| SKU | COGS −20 % | −10 % | base | +10 % | +20 % | Retail floor for 25 % contribution (base COGS) |\n|---|---:|---:|---:|---:|---:|---:|")
for k in PRICES:
    row = [commercial(k,"100",s)['contrib'] for s in (0.8,0.9,1.0,1.1,1.2)]
    base = commercial(k,"100")
    # price P such that (P/1.18 - cogs - 0.02P - ship - warr)/(P/1.18) = 0.25  => P(1/1.18*0.75 - 0.02) = cogs+ship+warr
    floor = (base['cogs']+base['ship']+base['warr'])/(0.75/(1+GST)-GATEWAY)
    P(f"| {k} | " + " | ".join(rs(v) for v in row) + f" | {rs(floor)} |")
P("")

P("## 5. Pricing rationale (positioning, not COGS × markup)\n")
P("""Reference points from `docs/references/lighting/COMPETITOR_LIGHTING_REFERENCE.md` (Indian retail, 2026-09-11): Neo Helios XP-300 ₹2,400–2,550, XP-450 ₹1,910–2,250, XP-600 ₹3,250–3,999 (white-only, no dimming, no schedule, no stated warranty); Week Aqua S-series ₹5,999–7,999 (entry WRGB, app); Chihiros WRGB II Slim 60 ₹15,525, WRGB II 60 ₹24,725, Pro 60 ₹28,275; Twinstar 600EA III ₹18,000, 600S III ₹27,499; ADA Aquasky RGB 60 ₹52,000.

- **Core Basic** sits at the top of the Neo Helios band, justified by dimming, a soft-start default profile, a published PPFD/spectrum sheet, a stated IP class, a stated warranty and an upgrade port. It cannot sit at the bottom of that band at pilot volumes: §3 shows the 50-unit COGS leaves no contribution below ~₹3,500 for 30 cm.
- **Core Smart** adds the module for ~₹1,000; the pair lands under Week Aqua S while offering app scheduling on a fixed spectrum.
- **WRGB Standalone** occupies the space above budget WRGB (Week Aqua S) and below Chihiros Slim; **WRGB Smart** at 60 cm lands ~₹2,000 under Slim 60 and ~₹11,000 under WRGB II 60, the premium-value position the owner asked for.
- **Dealer floor check:** at a future 25 % dealer margin off retail, the D2C contribution % in §3 falls by roughly that share of net revenue; Core Basic at the 100-unit tier does not survive a dealer margin, WRGB does. Dealer channel is therefore a scaled-tier question.
- Indian willingness to pay for a domestic brand above the Chinese incumbent is **unvalidated (TBD)**; the field pilot should test price acceptance directly.
""")

P("## 6. Programme cash\n")
def batch_cost(q, tier): return sum(unit_cost(SKUS[s],tier)*n for s,n in q.items())
ep = batch_cost(EP,"proto"); dvt = batch_cost(DVT,"pilot"); b1 = batch_cost(B1,"50"); b2 = batch_cost(B2,"100")
nre_exp = sum(v for v,_,_,c in NRE.values() if c=="expense"); nre_inv = sum(v for v,_,_,c in NRE.values() if c=="inventory")
P("| Item | ₹ | Evidence | Note | Cash class |\n|---|---:|---|---|---|")
for n,(v,e,note,c) in NRE.items(): P(f"| {n} | {rs(v)} | {e} | {note} | {c} |")
P(f"| Engineering prototypes ({sum(EP.values())} units, proto tier) | {rs(ep)} | EST | {dict(EP)} | expense |")
P(f"| EVT/DVT build ({sum(DVT.values())} units, pilot tier, first die run) | {rs(dvt)} | EST | {dict(DVT)} | expense (12 reused for field pilot) |")
P(f"| First commercial batch ({sum(B1.values())} units, 50-unit tier) | {rs(b1)} | EST | {dict(B1)} | inventory |")
P(f"| **Total cash before first meaningful sales** | **{rs(nre_exp+nre_inv+ep+dvt+b1)}** | | of which expense {rs(nre_exp+ep+dvt)}, inventory {rs(nre_inv+b1)} | |")
P(f"| Deferred tooling (not in the above) | {rs(sum(v for v,_,_ in DEFERRED_TOOLING.values()))} | RMKT/EST | " + "; ".join(f"{k} {rs(v)} ({n})" for k,(v,e,n) in DEFERRED_TOOLING.items()) + " | later |")
P("")
def sellthrough(label, sales, tier):
    rev = sum(PRICES[k][2]*n for k,n in sales.items()); net = rev/(1+GST)
    cogs = sum(commercial(k,tier)['cogs']*n for k,n in sales.items())
    contrib = sum(commercial(k,tier)['contrib']*n for k,n in sales.items())
    P(f"**{label}** (mix: {dict(sales)}; COGS at the {tier}-unit tier): gross revenue incl. GST {rs(rev)}; net revenue ex-GST {rs(net)}; COGS {rs(cogs)}; **contribution after variable costs {rs(contrib)}** ({contrib/net*100:.0f} % of net).\n")
    return contrib
P("### Batch-1 scenarios sold through\n")
cA = sellthrough("Scenario A, Core-led (40 fixtures + 30 modules, build cost " + rs(b1) + ")", B1_SALES, "50")
b1b = batch_cost(B1B,"50")
cB = sellthrough("Scenario B, WRGB-led (36 fixtures + 36 modules, build cost " + rs(b1b) + ")", B1B_SALES, "50")
P("Neither scenario recovers the programme expense; both are market-entry batches. Scenario B turns a negative variable contribution into a positive one because WRGB carries margin at pilot volume and Core does not. Scenario A is retained because it tests the volume product with real customers, which Scenario B does not. A hybrid (Scenario B plus ~10 Core Smart at a deliberately loss-making entry price, tracked as a marketing cost) is the recommended shape; OWNER DECISION REQUIRED.\n")
contrib = cA
# break-even
mix_contrib_100 = sum(commercial(k,"100")['contrib']*n for k,n in B1_SALES.items())/sum(B1_SALES.values())
mix_contrib_scaled = sum(commercial(k,"scaled")['contrib']*n for k,n in B1_SALES.items())/sum(B1_SALES.values())
fixed = nre_exp + ep + dvt
P(f"**Approximate break-even quantity** (programme expense {rs(fixed)} ÷ weighted contribution per unit at the batch-1 mix): at 100-unit COGS {rs(mix_contrib_100)}/unit → **{fixed/mix_contrib_100:,.0f} units**; at scaled COGS {rs(mix_contrib_scaled)}/unit → **{fixed/mix_contrib_scaled:,.0f} units**. Excludes salaries, marketing and other operating expenses; with those included the figure is materially higher (ASSUME: add them as a line before relying on this).\n")
P(f"**Working capital for batch 2** ({sum(B2.values())} units at the 100-unit tier, 60 cm launched): {rs(b2)} plus PCBA setup ~{rs(72000)} and a second packaging run; the extrusion and MCPCB MOQ stock from batch 1 covers it. Assume 60–90 days between paying suppliers and D2C cash receipt (ASSUME).\n")

P("## 7. What is not in this model\n")
P("Salaries and founder time; marketing and content; D2C platform subscription; office and lab rent; insurance; product liability; returns beyond the warranty reserve; import duty and freight on LEDs and modules beyond the RMKT unit classes (see supplier landscape §3.3, duties unconfirmed); GST input credit timing; any dealer margin (see §5); price erosion; the owner's own COGS figures (see §8).\n")

P("## 8. Reconciliation required with owner figures\n")
P("""| Item | Owner planning figure | Bottom-up estimate (100 units) | Gap | Likely cause | Action |
|---|---|---|---|---|---|
| Core small size COGS | ₹1,400–1,600 | ~₹2,700–3,000 | ~1.8× | Machined end caps (₹300), engine board with port (₹290), certified adapter (₹480), mounting (₹200) and Coimbatore low-volume labour; the owner figure is plausible only with moulded caps, an Indian-OEM adapter and ≥ 500-unit pricing, or a Chinese contract-manufactured fixture | RFQ packages A–D; decide whether Core Basic launches at the top of the band or as a loss-leader |
| WRGB COGS by size | ₹10k / 14k / 19k | ~₹4.4k / 5.4k / 6.4k | ~0.4× | Owner figure may be a contract-manufacturer finished-product quote including their margin and smart electronics, or premium high-power emitters; bottom-up assumes branded mid-power colour LEDs and a shared housing | Obtain the source of the owner figure; RFQ the WRGB LED board and driver stage |
""")
print("\n".join(out))
