"""AQ-LP-A Phase 0A preliminary unit-economics model.
All inputs are ENGINEERING ESTIMATES or PLANNING ASSUMPTIONS unless tagged PUB (published price; sources in ../sourcing/SOURCING_STRATEGY.md §5 and docs/references/lily-pipes/sources/SOURCE_REGISTER.md).
No supplier quotation exists. Outputs are ranges for discussion, not approved COGS.
Run: python3 unit_economics_model.py  -> writes markdown tables to stdout and CSVs next to the script.
"""
import csv, os, itertools

OUT = os.path.dirname(os.path.abspath(__file__))
GST = 0.18
QTYS = [25, 50, 100, 200]
# small-lot job-work premium multiplier on variable cost (ESTIMATE)
LOT_PREMIUM = {25: 1.35, 50: 1.18, 100: 1.00, 200: 0.93}
CASES = ["low", "base", "high"]

# ---- Variable cost per set at ~100-unit lot, INR ex-GST (input GST assumed recoverable) ----
ROUTES = {
    "S1 SS316L set (inflow+outflow+2 clips), Tamil Nadu job-work, passivated": {
        "tube 316L (~0.8-1.0 m, incl. offcut)":      (90, 130, 250),
        "tube laser: intake slots":                   (40, 80, 150),
        "CNC mandrel bending (3-4 bends)":            (90, 150, 250),
        "end forming: outlet flare + hose beads":     (60, 120, 220),
        "degrease / ultrasonic clean":                (25, 50, 80),
        "passivation or electropolish":               (30, 60, 120),
        "rim clips x2 (laser-cut SS + pad)":          (70, 130, 220),
        "laser mark":                                 (15, 30, 50),
        "inspection + packing labour":                (50, 80, 120),
        "packaging (board box, board/pulp insert, card)": (90, 140, 220),
    },
    "S2 = S1 + intake surface-skimmer module (machined, no mould)": None,  # built below
    "G1 borosilicate glass set, Ambala lampwork, to Trophic drawing": {
        "glasswork per set (forming, slots, anneal)": (400, 800, 1500),
        "inbound freight Ambala-Coimbatore + breakage in transit": (40, 90, 180),
        "polariscope + dimensional inspection":       (40, 70, 110),
        "rim clips x2":                               (70, 130, 220),
        "packaging (rigid, cavity insert, double wall)": (150, 220, 320),
        "packing labour":                             (30, 50, 80),
    },
    "M1 imported OEM SS set, private-label (benchmark only)": {
        "FOB US$9-17/set @ Rs94.7 (PUB listing range)": (9*94.7, 14*94.7, 17*94.7),
        "freight + clearance per set":                (120, 200, 350),
        "customs duty, non-creditable part (~15-22% of CIF)": (150, 300, 420),
        "incoming PMI/inspection + repack":           (60, 100, 150),
        "packaging (Trophic box)":                    (90, 140, 220),
    },
}
SKIMMER_ADD = {
    "skimmer: telescoping SS sleeve + machined POM float + stop": (250, 450, 800),
    "skimmer: extra finishing, assembly, flow check": (40, 80, 140),
}
s2 = dict(ROUTES["S1 SS316L set (inflow+outflow+2 clips), Tamil Nadu job-work, passivated"])
s2.update(SKIMMER_ADD)
ROUTES["S2 = S1 + intake surface-skimmer module (machined, no mould)"] = s2

# per-lot setup charges (bending/forming/laser setups, finisher minimum lot, print plates), INR
LOT_SETUP = {"S1": (8000, 15000, 25000), "S2": (10000, 19000, 32000),
             "G1": (5000, 10000, 20000), "M1": (15000, 25000, 40000)}  # M1: samples, broker, SIMS/LMPC admin
SCRAP = {"S1": (0.03, 0.06, 0.10), "S2": (0.04, 0.08, 0.12), "G1": (0.08, 0.15, 0.25), "M1": (0.03, 0.06, 0.12)}

# ---- One-time development (INR), ESTIMATES ----
FIXED = {
    "benchmark samples + teardown (6-8 sets incl. imports)": (35000, 50000, 70000),
    "flow/hose test rig (2 canisters, flow meter, hoses, tank)": (30000, 55000, 80000),
    "prototype rounds (3 x 3-5 sets, job-work)": (45000, 80000, 120000),
    "tooling & fixtures (bend dies if absent, flare tooling, gauges)": (50000, 120000, 250000),
    "corrosion/finish/material lab tests (PMI, A967 verification, immersion)": (15000, 35000, 60000),
    "packaging development (dieline, samples, drop tests)": (15000, 25000, 40000),
    "IP: attorney FTO search + design filing(s)": (30000, 60000, 120000),
    "compliance/label review (LMPC, e-commerce)": (5000, 12000, 20000),
    "photography, listing, launch content": (20000, 40000, 60000),
}
SKIMMER_FIXED_ADD = (40000, 80000, 150000)  # extra skimmer prototype rounds + rig time

# ---- Channel assumptions ----
# price points are MRP incl. GST (PLANNING ASSUMPTIONS to test in interviews)
PRICE = {"S1": 3999, "S2": 5499, "G1": 3499, "M1": 3499}
CHANNELS = {
    # name: dict(fee_pct of MRP, fixed per order, ship, returns_pct of net rev, warranty_pct of net rev, acq per unit)
    "DTC own site": dict(fee_pct=0.0236, per_order=0, ship=(90, 130, 200), ret=(0.02, 0.04, 0.06),
                          acq=(150, 350, 600)),
    "Amazon.in (seller-fulfilled)": dict(fee_pct=(0.095*1.18, 0.12*1.18, 0.14*1.18), per_order=(60, 90, 130),
                          ship=(90, 130, 200), ret=(0.04, 0.06, 0.09), acq=(100, 250, 450)),
    "Specialist retailer (dealer)": dict(dealer_margin=(0.35, 0.40, 0.45), ship=(25, 40, 70), ret=(0.01, 0.02, 0.04),
                          acq=(50, 100, 200)),
}
WARRANTY = {"S1": (0.01, 0.02, 0.03), "S2": (0.02, 0.03, 0.05), "G1": (0.05, 0.08, 0.12), "M1": (0.02, 0.04, 0.06)}

def pick(v, i):
    return v[i] if isinstance(v, tuple) else v

def key(route):
    return route.split()[0]

def unit_cost(route, q, i):
    k = key(route)
    var = sum(pick(v, i) for v in ROUTES[route].values())
    prem = LOT_PREMIUM[q] if k != "M1" else 1.0
    c = var * prem + pick(LOT_SETUP[k], i) / q
    return c / (1 - pick(SCRAP[k], i))

def contribution(route, channel, q, i, price=None, dealer_margin=None, acq=None, cogs_mult=1.0):
    """contribution per unit before fixed costs; i: 0 favourable,1 base,2 adverse (cost side adverse together)"""
    k = key(route)
    mrp = price or PRICE[k]
    net = mrp / (1 + GST)              # revenue ex-GST at MRP
    ch = CHANNELS[channel]
    cogs = unit_cost(route, q, i) * cogs_mult
    if "dealer_margin" in ch:
        dm = dealer_margin if dealer_margin is not None else pick(ch["dealer_margin"], i)
        rev = net * (1 - dm)            # Trophic invoice to dealer ex-GST
        fees = 0
    else:
        rev = net
        fees = mrp * pick(ch["fee_pct"], i) + pick(ch.get("per_order", 0), i)
    ship = pick(ch["ship"], i)
    ret = rev * pick(ch["ret"], i)
    war = rev * pick(WARRANTY[k], i)
    acq = acq if acq is not None else pick(ch["acq"], i)
    pre_acq = rev - cogs - fees - ship - ret - war
    return dict(mrp=mrp, net_rev=rev, cogs=cogs, fees=fees, ship=ship, returns=ret, warranty=war,
                contrib_before_acq=pre_acq, acq=acq, contrib_after_acq=pre_acq - acq)

def fixed_total(route, i):
    f = sum(pick(v, i) for v in FIXED.values())
    if key(route) == "S2":
        f += SKIMMER_FIXED_ADD[i]
    if key(route) == "M1":
        f = FIXED["benchmark samples + teardown (6-8 sets incl. imports)"][i] + FIXED["compliance/label review (LMPC, e-commerce)"][i] \
            + FIXED["photography, listing, launch content"][i] + FIXED["packaging development (dieline, samples, drop tests)"][i]
    return f

def r(x):
    return int(round(x, -1))

def main():
    rows = []
    print("## Unit cost per set (INR ex-GST, incl. setup amortisation and scrap) — low / base / high\n")
    print("| Route | 25 | 50 | 100 | 200 |\n|---|---|---|---|---|")
    for route in ROUTES:
        cells = []
        for q in QTYS:
            vals = [unit_cost(route, q, i) for i in range(3)]
            cells.append(" / ".join(f"{r(v):,}" for v in vals))
            for i, c in enumerate(CASES):
                rows.append(["unit_cost", route, "", q, c, r(vals[i])])
        print(f"| {route} | " + " | ".join(cells) + " |")

    print("\n## Contribution per unit at 100-unit lot, base case (INR)\n")
    print("| Route | Channel | MRP | Net rev ex-GST | COGS | Fees | Ship | Returns | Warranty | Contrib. before acquisition | Acquisition | Contrib. after acquisition | Contrib. margin on net rev |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for route, ch in itertools.product(ROUTES, CHANNELS):
        c = contribution(route, ch, 100, 1)
        print(f"| {key(route)} | {ch} | {c['mrp']:,} | {r(c['net_rev']):,} | {r(c['cogs']):,} | {r(c['fees']):,} | {r(c['ship'])} | {r(c['returns'])} | {r(c['warranty'])} | {r(c['contrib_before_acq']):,} | {r(c['acq'])} | {r(c['contrib_after_acq']):,} | {c['contrib_after_acq']/c['net_rev']*100:.0f}% |")
        for i, cs in enumerate(CASES):
            cc = contribution(route, ch, 100, i)
            rows.append(["contrib_after_acq_q100", route, ch, 100, cs, r(cc["contrib_after_acq"])])

    print("\n## Contribution after acquisition by lot size — favourable / base / adverse (INR per unit)\n")
    print("| Route | Channel | 25 | 50 | 100 | 200 |\n|---|---|---|---|---|---|")
    for route, ch in itertools.product(["S1 SS316L set (inflow+outflow+2 clips), Tamil Nadu job-work, passivated",
                                         "S2 = S1 + intake surface-skimmer module (machined, no mould)"], CHANNELS):
        cells = [" / ".join(f"{r(contribution(route, ch, q, i)['contrib_after_acq']):,}" for i in range(3)) for q in QTYS]
        print(f"| {key(route)} | {ch} | " + " | ".join(cells) + " |")

    print("\n## One-time development + launch fixed costs (INR)\n")
    print("| Item | Low | Base | High |\n|---|---|---|---|")
    for k, v in FIXED.items():
        print(f"| {k} | {v[0]:,} | {v[1]:,} | {v[2]:,} |")
    print(f"| skimmer module extra (S2 only) | {SKIMMER_FIXED_ADD[0]:,} | {SKIMMER_FIXED_ADD[1]:,} | {SKIMMER_FIXED_ADD[2]:,} |")
    for route in ROUTES:
        print(f"| **Total, {key(route)}** | {fixed_total(route,0):,} | {fixed_total(route,1):,} | {fixed_total(route,2):,} |")

    print("\n## Break-even units (fixed costs / contribution after acquisition at 100-unit lot cost)\n")
    print("| Route | Channel | Favourable (low fixed) | Base | Adverse (high fixed) |\n|---|---|---|---|---|")
    for route, ch in itertools.product(ROUTES, CHANNELS):
        cells = []
        for i in range(3):
            c = contribution(route, ch, 100, i)["contrib_after_acq"]
            f = fixed_total(route, i)
            cells.append("not reached (≤0)" if c <= 0 else (f"{int(-(-f // c)):,}" if f/c < 5000 else ">5,000 (effectively not reached)"))
            rows.append(["breakeven_units", route, ch, 100, CASES[i], cells[-1]])
        print(f"| {key(route)} | {ch} | " + " | ".join(cells) + " |")

    print("\n## Sensitivity — S1 base case, 100-unit lot, contribution after acquisition (INR/unit)\n")
    print("| Variable changed | DTC own site | Specialist retailer |\n|---|---|---|")
    s1 = "S1 SS316L set (inflow+outflow+2 clips), Tamil Nadu job-work, passivated"
    base_d = contribution(s1, "DTC own site", 100, 1)["contrib_after_acq"]
    base_r = contribution(s1, "Specialist retailer (dealer)", 100, 1)["contrib_after_acq"]
    print(f"| Base (MRP 3,999) | {r(base_d):,} | {r(base_r):,} |")
    for p in (2999, 3499, 4499):
        print(f"| MRP {p:,} | {r(contribution(s1,'DTC own site',100,1,p)['contrib_after_acq']):,} | {r(contribution(s1,'Specialist retailer (dealer)',100,1,p)['contrib_after_acq']):,} |")
    for f in (0.7, 1.3):
        print(f"| COGS x{f} | {r(contribution(s1,'DTC own site',100,1,cogs_mult=f)['contrib_after_acq']):,} | {r(contribution(s1,'Specialist retailer (dealer)',100,1,cogs_mult=f)['contrib_after_acq']):,} |")
    for dm in (0.30, 0.50):
        print(f"| Dealer margin {int(dm*100)}% of MRP | — | {r(contribution(s1,'Specialist retailer (dealer)',100,1,dealer_margin=dm)['contrib_after_acq']):,} |")
    for a in (0, 800):
        print(f"| Acquisition cost ₹{a}/unit | {r(contribution(s1,'DTC own site',100,1,acq=a)['contrib_after_acq']):,} | {r(contribution(s1,'Specialist retailer (dealer)',100,1,acq=a)['contrib_after_acq']):,} |")
    print("\n## Break-even units, S1, base fixed costs, by MRP and channel (base contribution, 100-unit lot)\n")
    print("| MRP | DTC own site | Amazon.in | Specialist retailer |\n|---|---|---|---|")
    for p in (3499, 3999, 4499):
        cells=[]
        for ch in CHANNELS:
            c = contribution(s1, ch, 100, 1, p)["contrib_after_acq"]
            cells.append("not reached" if c<=0 else f"{int(-(-fixed_total(s1,1)//c)):,}")
        print(f"| {p:,} | " + " | ".join(cells) + " |")

    with open(os.path.join(OUT, "unit_economics_outputs.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["metric", "route", "channel", "lot_qty", "case", "value_inr"]); w.writerows(rows)

if __name__ == "__main__":
    main()
