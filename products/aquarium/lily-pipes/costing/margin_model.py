"""AQ-LP-A manufacturing cost and profit-margin model (illustrative).
Builds on unit_economics_model.py (same inputs, same cases). Adds: per-step cost build-up,
manufacturing-location logistics scenarios, margin ladder (COGS -> dealer -> MRP), gross /
contribution / operating / net margins, and annual P&L scenarios.
ALL figures are ESTIMATES or PLANNING ASSUMPTIONS. No supplier quotation exists.
Run: python3 margin_model.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unit_economics_model as u

S1 = "S1 SS316L set (inflow+outflow+2 clips), Tamil Nadu job-work, passivated"
GST = u.GST
TAX = 0.2517  # s.115BAA effective rate for a domestic company (22% + 10% surcharge + 4% cess); entity-dependent
r = u.r

def step_table():
    print("## A. S1 cost build-up per set by step, base case (INR ex-GST)\n")
    print("| Step | 25 sets | 50 | 100 | 200 |\n|---|---|---|---|---|")
    steps = u.ROUTES[S1]
    tot = {q: 0 for q in u.QTYS}
    for name, v in steps.items():
        cells = []
        for q in u.QTYS:
            c = v[1] * u.LOT_PREMIUM[q]
            tot[q] += c
            cells.append(f"{r(c):,}")
        print(f"| {name} | " + " | ".join(cells) + " |")
    setup = {q: u.LOT_SETUP['S1'][1] / q for q in u.QTYS}
    print("| Lot setups (bending, forming, laser, finisher minimum, print) ₹15,000/lot | " + " | ".join(f"{r(setup[q]):,}" for q in u.QTYS) + " |")
    scrap = {q: (tot[q] + setup[q]) * (1 / (1 - u.SCRAP['S1'][1]) - 1) for q in u.QTYS}
    print("| Scrap / rework allowance (6 %) | " + " | ".join(f"{r(scrap[q]):,}" for q in u.QTYS) + " |")
    print("| **COGS per set** | " + " | ".join(f"**{r(tot[q]+setup[q]+scrap[q]):,}**" for q in u.QTYS) + " |")
    print("| Check: unit_economics_model | " + " | ".join(f"{r(u.unit_cost(S1,q,1)):,}" for q in u.QTYS) + " |")
    print("\nShare of COGS at 100 sets: " + ", ".join(
        f"{k.split(' (')[0].split(':')[0]} {steps[k][1]/u.unit_cost(S1,100,1)*100:.0f}%" for k in steps) + "\n")

LOC = {  # per-lot extra logistics (freight between processors and to Coimbatore) and oversight trips, INR, (low, base, high)
    "L1 All process steps in Coimbatore (only if a local tube shop proves capable)": dict(freight=(0, 200, 500), trips=(0, 500, 1000)),
    "L2 Forming in Chennai, finishing Chennai or Coimbatore, QC/pack in Coimbatore": dict(freight=(600, 1000, 1500), trips=(3000, 4500, 6000)),
    "L3 Forming in Pune (or Bengaluru), QC/pack in Coimbatore": dict(freight=(1000, 1800, 2500), trips=(8000, 12000, 18000)),
}

def location_table():
    print("## B. Location logistics effect on S1 COGS per set (INR, base process costs)\n")
    print("| Location scenario | Extra per set @25 (low / base / high) | Extra per set @100 | S1 COGS @100 incl. logistics (base) | Change vs process-cost base |")
    print("|---|---|---|---|---|")
    base100 = u.unit_cost(S1, 100, 1)
    for k, v in LOC.items():
        e25 = [(v['freight'][i] + v['trips'][i]) / 25 for i in range(3)]
        e100 = [(v['freight'][i] + v['trips'][i]) / 100 for i in range(3)]
        print(f"| {k} | {' / '.join(f'{r(x):,}' for x in e25)} | {' / '.join(f'{r(x):,}' for x in e100)} | {r(base100+e100[1]):,} | +{e100[1]/base100*100:.0f}% |")
    print()

def ladder(mrp=3999, q=100):
    cogs = u.unit_cost(S1, q, 1)
    net_mrp = mrp / (1 + GST)
    dm = 0.40
    dealer_price = net_mrp * (1 - dm)
    print(f"## C. Price ladder, S1, MRP ₹{mrp:,}, {q}-set lot, base (INR per set)\n")
    print("| Level | Amount | Margin on that selling price | Markup on the cost below it |\n|---|---|---|---|")
    print(f"| COGS (ex-GST) | {r(cogs):,} | — | — |")
    print(f"| Trophic price to dealer (ex-GST) | {r(dealer_price):,} | Trophic gross margin {(dealer_price-cogs)/dealer_price*100:.0f}% | {(dealer_price/cogs-1)*100:.0f}% on COGS |")
    print(f"| Retail price ex-GST (MRP ÷ 1.18) | {r(net_mrp):,} | Dealer margin {dm*100:.0f}% | {(net_mrp/dealer_price-1)*100:.0f}% on dealer price |")
    print(f"| GST 18 % (collected, remitted — not margin) | {r(mrp-net_mrp):,} | — | — |")
    print(f"| MRP incl. GST | {mrp:,} | — | {(mrp/cogs-1)*100:.0f}% over COGS (misleading: includes GST and dealer) |")
    print(f"| DTC: Trophic gross margin selling at MRP | {r(net_mrp-cogs):,} | {(net_mrp-cogs)/net_mrp*100:.0f}% | {(net_mrp/cogs-1)*100:.0f}% on COGS |\n")

def margin_grid(q=100):
    print(f"## D. Per-set margins by price and channel, S1, {q}-set lot, base case\n")
    print("| MRP | Channel | Net revenue | COGS | Gross profit | Gross margin | Contribution (after fees, ship, returns, warranty, acquisition) | Contribution margin |")
    print("|---|---|---|---|---|---|---|---|")
    for p in (3499, 3999, 4499):
        for ch in u.CHANNELS:
            c = u.contribution(S1, ch, q, 1, p)
            gp = c['net_rev'] - c['cogs']
            print(f"| {p:,} | {ch} | {r(c['net_rev']):,} | {r(c['cogs']):,} | {r(gp):,} | {gp/c['net_rev']*100:.0f}% | {r(c['contrib_after_acq']):,} | {c['contrib_after_acq']/c['net_rev']*100:.0f}% |")
    print()

SCEN = {  # name: (DTC units, dealer units, lot size, annual attributable overhead INR)
    "Conservative": (48, 36, 50, 60000),
    "Base": (120, 144, 100, 90000),
    "Optimistic": (240, 360, 200, 150000),
}
AMORT_YEARS = 3

def pnl(mrp=3999, case=1):
    fixed = u.fixed_total(S1, case)
    amort = fixed / AMORT_YEARS
    print(f"## E. Illustrative annual P&L for the lily-pipe line, S1, MRP ₹{mrp:,}, {['favourable','base','adverse'][case]} unit inputs (INR)\n")
    print(f"Development and launch fixed costs ₹{fixed:,} amortised over {AMORT_YEARS} years = ₹{r(amort):,}/yr. Owner time not costed. Tax at 25.17 % applied only to positive profit.\n")
    rows = {}
    for s, (d, dl, lot, oh) in SCEN.items():
        cd = u.contribution(S1, "DTC own site", lot, case, mrp)
        cr = u.contribution(S1, "Specialist retailer (dealer)", lot, case, mrp)
        rev = d * cd['net_rev'] + dl * cr['net_rev']
        cogs = (d + dl) * cd['cogs']
        gp = rev - cogs
        var_sell = d * (cd['net_rev'] - cd['cogs'] - cd['contrib_after_acq']) + dl * (cr['net_rev'] - cr['cogs'] - cr['contrib_after_acq'])
        contrib = gp - var_sell
        op = contrib - oh - amort
        tax = max(op, 0) * TAX
        net = op - tax
        rows[s] = dict(units=d + dl, rev=rev, cogs=cogs, gp=gp, var=var_sell, contrib=contrib, oh=oh, amort=amort, op=op, tax=tax, net=net)
    names = list(rows)
    print("| Line | " + " | ".join(f"{n} ({rows[n]['units']} sets)" for n in names) + " |")
    print("|---|" + "---|" * len(names))
    for label, key in [("Net revenue ex-GST", "rev"), ("COGS", "cogs"), ("**Gross profit**", "gp"), ("Selling costs (fees, shipping, returns, warranty, acquisition)", "var"), ("**Contribution**", "contrib"), ("Attributable overheads (EST)", "oh"), ("Amortised development/launch costs", "amort"), ("**Operating profit**", "op"), ("Income tax (illustrative)", "tax"), ("**Net profit (illustrative)**", "net")]:
        print(f"| {label} | " + " | ".join(f"{r(rows[n][key]):,}" for n in names) + " |")
    for label, key in [("Gross margin", "gp"), ("Contribution margin", "contrib"), ("Operating margin", "op"), ("Net margin", "net")]:
        print(f"| {label} | " + " | ".join(f"{rows[n][key]/rows[n]['rev']*100:.0f}%" for n in names) + " |")
    print()

if __name__ == "__main__":
    step_table(); location_table(); ladder(); margin_grid(); pnl(3999, 1); pnl(4499, 1); pnl(3999, 2)
