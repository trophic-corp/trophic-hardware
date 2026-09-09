import sys, html
sys.path.insert(0,'/home/claude/dwg')
from gen import sheet
from parts import PARTS as _ALL
STRUCT={'RK-A-101','RK-A-102','RK-A-103','RK-A-104','RK-A-105','RK-A-106','RK-A-107',
        'RK-A-201','RK-A-202','RK-A-203','RK-A-401'}
HELD={'RK-A-301':'LED mounting rail','RK-A-501':'Reflective panel, rear','RK-A-502':'Reflective panel, side'}
PARTS=[q for q in _ALL if q['pn'] in STRUCT]

def esc(s): return html.escape(str(s))
PAGE0=3  # cover 1, index 2, overview 3 -> parts start at 4

CSS = """
:root{
 --paper:#F5F4F0; --sheet:#FFFFFF; --card:#FBFAF7; --band:#ECEAE4; --band2:#E2DFD7;
 --ink:#1A1C1B; --ink2:#4A514F; --ink3:#7C8482;
 --rule:#D6D3CA; --rule2:#B4B0A5;
 --acc:#1C5A62; --acc-soft:#DCE9EA;
 --warn:#8F4326; --warn-soft:#F4E3DA;
 --line:#22282A; --hidden:#939EA1; --dim:#4B585C; --face:#EDF1F2; --hole:#C6D0D3;
 --ctr:#8794 98; --ctr:#879498; --vp:#FFFFFF; --vpline:#E1E5E6; --tb:#F4F6F6;
 --iso-top:#E6EDEE; --iso-front:#D2DDDF; --iso-side:#BECBCE;
 --mono:"IBM Plex Mono",ui-monospace,monospace; --disp:"Chivo",system-ui,sans-serif; --body:"Source Sans 3",system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --paper:#0E100F; --sheet:#151918; --card:#131716; --band:#1B201F; --band2:#232827;
 --ink:#E9EDEB; --ink2:#A6AFAC; --ink3:#79837F;
 --rule:#272D2C; --rule2:#39423F;
 --acc:#6FB6BC; --acc-soft:#122726; --warn:#D08D6E; --warn-soft:#2A1A13;
 --line:#C4CFD1; --hidden:#5D6A6D; --dim:#93A1A4; --face:#1E2626; --hole:#33403F;
 --ctr:#5F6C6E; --vp:#151918; --vpline:#262E2E; --tb:#1A201F;
 --iso-top:#26302F; --iso-front:#1E2726; --iso-side:#182120;
}}
:root[data-theme="dark"]{
 --paper:#0E100F; --sheet:#151918; --card:#131716; --band:#1B201F; --band2:#232827;
 --ink:#E9EDEB; --ink2:#A6AFAC; --ink3:#79837F; --rule:#272D2C; --rule2:#39423F;
 --acc:#6FB6BC; --acc-soft:#122726; --warn:#D08D6E; --warn-soft:#2A1A13;
 --line:#C4CFD1; --hidden:#5D6A6D; --dim:#93A1A4; --face:#1E2626; --hole:#33403F;
 --ctr:#5F6C6E; --vp:#151918; --vpline:#262E2E; --tb:#1A201F;
 --iso-top:#26302F; --iso-front:#1E2726; --iso-side:#182120;
}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:15.5px;line-height:1.62}
.pg{max-width:1220px;margin:0 auto;padding:0 26px}
h1,h2,h3,h4{font-family:var(--disp);margin:0;text-wrap:balance}
a{color:var(--acc);text-decoration:none;border-bottom:1px solid var(--rule)}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

/* ---- cover ---- */
.cover{border-bottom:3px double var(--rule2);background:var(--card)}
.cover-in{max-width:1220px;margin:0 auto;padding:56px 26px 0}
.eyebrow{font-family:var(--mono);font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--acc)}
.cover h1{font-size:clamp(40px,7vw,84px);font-weight:900;line-height:.92;letter-spacing:-.02em;margin:16px 0 12px}
.cover .st{font-family:var(--disp);font-size:clamp(17px,2.3vw,25px);font-weight:400;color:var(--ink2);max-width:52ch}
.cvgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));border-top:1px solid var(--rule);margin-top:34px}
.cvgrid div{padding:12px 15px 14px;border-right:1px solid var(--rule)}
.cvgrid div:last-child{border-right:0}
.cvgrid dt{font-family:var(--mono);font-size:10px;letter-spacing:.15em;text-transform:uppercase;color:var(--ink3)}
.cvgrid dd{margin:4px 0 0;font-family:var(--disp);font-size:20px;font-weight:700}

/* ---- chapter ---- */
.ch{padding:0 0 44px;border-bottom:1px solid var(--rule)}
.chhead{display:flex;align-items:baseline;gap:18px;flex-wrap:wrap;padding:30px 0 16px;border-bottom:2px solid var(--ink);margin-bottom:22px}
.chno{font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--acc);
      background:var(--acc-soft);padding:4px 9px;border-radius:2px;font-weight:600}
.chhead h2{font-size:clamp(26px,3.6vw,40px);font-weight:800;letter-spacing:-.01em;flex:1;min-width:220px;text-transform:uppercase}
.pgno{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3)}
.fn{font-family:var(--disp);font-size:19px;color:var(--acc);margin:-6px 0 18px;max-width:76ch;font-weight:500}

.sheetwrap{background:var(--sheet);border:1.5px solid var(--rule2);padding:10px;overflow-x:auto;margin:0 0 22px}
.sheetwrap svg{display:block;width:100%;height:auto;min-width:800px}

.two{display:grid;gap:26px;margin-bottom:8px}
@media(min-width:900px){.two{grid-template-columns:1.35fr 1fr}}
.two p{margin:0 0 12px}
h3{font-family:var(--disp);font-size:14px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);margin:0 0 10px}
h3.b{color:var(--ink);border-top:1px solid var(--rule);padding-top:16px;margin-top:24px}

table{border-collapse:collapse;width:100%;font-size:13.5px}
.spec td{padding:7px 10px;border-bottom:1px solid var(--rule);vertical-align:top;color:var(--ink2)}
.spec td:first-child{color:var(--ink3);font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;
   text-transform:uppercase;width:40%;white-space:nowrap}
.spec tr:last-child td{border-bottom:0}
.spec .v{font-family:var(--mono);color:var(--ink);font-size:13px}

ol.mfg{counter-reset:m;list-style:none;padding:0;margin:12px 0 0}
ol.mfg li{counter-increment:m;position:relative;padding:10px 0 10px 44px;border-bottom:1px solid var(--rule);color:var(--ink2);font-size:14.5px}
ol.mfg li::before{content:"M" counter(m);position:absolute;left:0;top:10px;font-family:var(--mono);font-size:11px;
  font-weight:600;color:var(--acc);background:var(--acc-soft);padding:2px 6px;border-radius:2px}
ol.mfg li:last-child{border-bottom:0}
ul.qc{list-style:none;padding:0;margin:12px 0 0}
ul.qc li{padding:8px 0 8px 28px;border-bottom:1px solid var(--rule);position:relative;font-size:14px;color:var(--ink2)}
ul.qc li::before{content:"";position:absolute;left:2px;top:12px;width:12px;height:12px;border:1.5px solid var(--rule2);border-radius:2px}
ul.qc li:last-child{border-bottom:0}

.idx{width:100%;font-size:14.5px}
.idx td{padding:9px 10px;border-bottom:1px solid var(--rule)}
.idx td:first-child{font-family:var(--mono);font-size:12px;color:var(--acc);width:70px}
.idx td:nth-child(2){font-family:var(--mono);font-size:12.5px;color:var(--ink3);width:110px}
.idx td:last-child{text-align:right;font-family:var(--mono);font-size:12.5px;color:var(--ink3);width:74px}
.idx a{border:0;color:var(--ink);font-weight:500}
.idx tr:hover td{background:var(--band)}

.note{background:var(--band);border-left:3px solid var(--acc);padding:13px 17px;margin:16px 0;font-size:14.5px;color:var(--ink2)}
.note strong{color:var(--ink)}
.note.w{background:var(--warn-soft);border-left-color:var(--warn)}
.tree{font-family:var(--mono);font-size:13px;line-height:1.9;color:var(--ink2);background:var(--card);
      border:1px solid var(--rule);padding:18px 20px;overflow-x:auto;white-space:pre}
footer{padding:34px 0 60px;color:var(--ink3);font-size:13px}
@media print{
  @page{size:A4 landscape;margin:11mm}
  body{background:#fff;font-size:10pt}
  .ch,.cover,.idxpage{page-break-before:always}
  .cover{page-break-before:avoid}
  .sheetwrap{page-break-inside:avoid;border-color:#999}
  .two{page-break-inside:avoid}
  a{color:inherit}
}
"""

def spec_rows(p):
    r=[('Part number',p['pn']),('Description',p['name']),('Quantity per rack',str(p['qty'])),
       ('Material',p['mat']),('Mass each',p['mass'])]
    if p['kind']=='tube': r.append(('Cut length','%d mm'%p['L']))
    elif p['kind']=='tray': r.append(('Formed size','%d × %d × %d mm'%(p['L'],p['W'],p['H'])))
    else: r.append(('Blank size','%d × %d × %g mm'%(p['L'],p['W'],p['t'])))
    if p.get('holes') and 'pitch' in p['holes']:
        h=p['holes']; r.append(('Hole pattern','%d × Ø%g @ %d pitch, %d face(s)'%(h['count'],h['dia'],h['pitch'],h['faces'])))
    elif p.get('holes'):
        r.append(('Hole pattern','%d × Ø%g'%(len(p['holes']['pos']),p['holes']['dia'])))
    r.append(('Projection','First angle, ISO'))
    r.append(('Units','Millimetres'))
    return r

def chapter(i,p):
    pg=PAGE0+i+1
    cid='ch%s'%p['pn'].replace('-','')
    sv=sheet(p,'u%d'%i)
    rows=''.join('<tr><td>%s</td><td class="v">%s</td></tr>'%(esc(a),esc(b)) for a,b in spec_rows(p))
    mfg=''.join('<li>%s</li>'%m for m in p['mfg'])
    qc=''.join('<li>%s</li>'%esc(q) for q in p['qc'])
    return f"""
<section class="ch" id="{cid}">
 <div class="pg">
  <div class="chhead"><span class="chno">CH {i+1:02d}</span><h2>{esc(p['pn'])} · {esc(p['name'])}</h2><span class="pgno">Page {pg}</span></div>
  <p class="fn">{esc(p['fn'])}</p>
  <div class="sheetwrap">{sv}</div>
  <div class="two">
   <div><h3>Description</h3><p>{p['desc']}</p></div>
   <div><h3>Specification</h3><table class="spec"><tbody>{rows}</tbody></table></div>
  </div>
  <h3 class="b">Manufacturing guidelines</h3><ol class="mfg">{mfg}</ol>
  <h3 class="b">Inspection points</h3><ul class="qc">{qc}</ul>
 </div>
</section>"""

idx_rows=''.join(
 '<tr><td>CH %02d</td><td>%s</td><td><a href="#ch%s">%s</a></td><td>%d</td></tr>'
 %(i+1,esc(p['pn']),p['pn'].replace('-',''),esc(p['name']),PAGE0+i+1)
 for i,p in enumerate(PARTS))

tree = """RACK A  ·  RK-A-000  ·  4-TIER GROW  ·  STRUCTURAL SET, REV 2
│
├─ FRAME  ─────────────────────────────────────────────  34.8 kg
│   ├─ RK-A-101  Upright                      × 4    the accessory grid lives here
│   ├─ RK-A-102  Beam, long                   × 10   8 tier + 2 base
│   ├─ RK-A-103  Beam, short (base)           × 2
│   ├─ RK-A-104  Rear X-brace                 × 2    1797 long — corrected in Rev 2
│   ├─ RK-A-105  Levelling foot               × 4
│   ├─ RK-A-106  Wall anchor bracket          × 2    fitted; also bolts rack to rack
│   └─ RK-A-107  Beam-end L-bracket           × 12   deleted at volume
│
├─ DECK  (× 4, one per tier)  ─────────────────────────  27.4 kg
│   ├─ RK-A-201  Deck rail, long              × 8
│   ├─ RK-A-202  Deck rail, cross             × 16
│   └─ RK-A-203  Deck mesh panel              × 4    top face = BED DATUM
│
└─ WET MODULE  (× 4, interchangeable)  ────────────────   9.3 kg
    └─ RK-A-401  Flood tray                   × 4    moulded collar + 2 bosses

    HELD FROM THIS REVISION — issued when the plenum design closes
      RK-A-301  LED mounting rail             × 8
      RK-A-501  Reflective panel / plenum face × 4
      RK-A-502  Reflective panel, side        × 8

    FASTENERS  208 pcs  ·  see Manufacturing Pack §07"""

HTML=f"""<title>Rack A Part Drawings</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chivo:wght@400;500;700;900&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Sans+3:wght@400;600&display=swap">
<style>{CSS}</style>

<header class="cover">
 <div class="cover-in">
  <div class="eyebrow">RK-A-DWG · Revision 2 · 05 September 2026 · structural set</div>
  <h1>Rack A<br>Part Drawings</h1>
  <p class="st">The eleven structural parts, four views each, reissued against model Rev 5. First-angle projection, dimensions in millimetres, every view generated from the released model rather than redrawn. Lighting and enclosure drawings are held pending the plenum design.</p>
  <dl class="cvgrid">
   <div><dt>Assembly</dt><dd>RK-A-000</dd></div>
   <div><dt>Parts issued</dt><dd>11</dd></div>
   <div><dt>Parts held</dt><dd>3</dd></div>
   <div><dt>Pages</dt><dd>15</dd></div>
   <div><dt>Projection</dt><dd>First angle</dd></div>
   <div><dt>Units</dt><dd>mm</dd></div>
  </dl>
 </div>
</header>

<main>
<section class="ch idxpage" id="index">
 <div class="pg">
  <div class="chhead"><span class="chno">Index</span><h2>Contents</h2><span class="pgno">Page 2</span></div>
  <table class="idx"><tbody>
   <tr><td>—</td><td>RK-A-000</td><td><a href="#overview">Overview · the rack and how the parts relate</a></td><td>3</td></tr>
   {idx_rows}
   <tr><td>—</td><td>—</td><td><a href="#notes">Reading these drawings · tolerances · revision</a></td><td>15</td></tr>
  </tbody></table>
  <div class="note w"><strong>Structural set only.</strong> This revision issues the eleven parts a fabricator needs to quote and build the frame, decks and trays. Three parts are <strong>held</strong> and are not in this document: RK-A-301 LED mounting rail, and RK-A-501 / RK-A-502 reflective panels. They are held because the ventilation plenum is deliberately deferred to the second build phase, and the panel that serves as the plenum face cannot be dimensioned until the canopy velocity is measured on the first rack. Do not release them from Rev 1 — the mounting positions have moved.</div>
  <div class="note"><strong>How to use this document.</strong> Each chapter is one part and is self-contained — a fabricator can be sent a single chapter without the rest. The four views are front, end, plan and isometric, laid out in first angle. Long parts are drawn broken, with the true length always given as the overall dimension. Nothing here supersedes the STEP and DXF files; where a drawing and the model disagree, <strong>the model governs</strong>.</div>
 </div>
</section>

<section class="ch" id="overview">
 <div class="pg">
  <div class="chhead"><span class="chno">Overview</span><h2>The rack</h2><span class="pgno">Page 3</span></div>
  <p class="fn">A modular four-tier growing rack: galvanised structure, food-grade wet modules, and a 50 mm accessory grid that everything else bolts to.</p>
  <div class="two">
   <div>
    <h3>What it is</h3>
    <p>Rack A holds sixteen 1020 trays on four tiers at 300, 700, 1100 and 1500 mm, and floods each tier to 22 mm on a ten-minute dwell. The structural set drawn here is 1256 × 563 × 1960 mm and 72.0 kg; the complete rack with irrigation, drainage, lighting, ventilation, sensing and power installed is <strong>1456 × 690 × 1960 mm and 112.7 kg dry</strong>.</p>
    <p>The design separates three jobs that are usually bundled into one material. The <strong>structure</strong> carries load and sees humidity but never touches the crop, so it is pre-galvanised steel. The <strong>wet module</strong> holds the flood and touches the crop, so it alone is food-contact HDPE. The <strong>accessory plane</strong> — a 50 mm hole grid punched into every upright and beam — carries lighting, sensors, cabling and anything added later. Separating them is what let the frame cost fall by roughly a third without losing the modularity.</p>
    <p>The consequence for manufacturing is that almost every part is a cut length of hollow section with punched holes. There is <strong>no welding in the rack at all</strong>; every structural joint is bolted. That removes pickling and passivation, removes weld distortion from a frame that must hold 3 mm of bed flatness, and means a general fabrication shop can build it.</p>
   </div>
   <div>
    <h3>Principal data</h3>
    <table class="spec"><tbody>
     <tr><td>Assembly</td><td class="v">RK-A-000</td></tr>
     <tr><td>Envelope, structure</td><td class="v">1256 × 563 × 1960 mm</td></tr>
     <tr><td>Envelope, installed</td><td class="v">1456 × 690 × 1960 mm</td></tr>
     <tr><td>Bed size</td><td class="v">1176 × 560 mm</td></tr>
     <tr><td>Tiers</td><td class="v">4 · structure takes 3 to 5</td></tr>
     <tr><td>Bed heights</td><td class="v">300 · 700 · 1100 · 1500</td></tr>
     <tr><td>Trays</td><td class="v">16 × 1020</td></tr>
     <tr><td>Rated load</td><td class="v">80 kg UDL per tier</td></tr>
     <tr><td>Bed flatness</td><td class="v">≤ 3 mm · 0.50 in service</td></tr>
     <tr><td>Mass, structural set</td><td class="v">72.0 kg</td></tr>
     <tr><td>Mass, complete rack</td><td class="v">112.7 kg dry</td></tr>
     <tr><td>Floor clearance</td><td class="v">150 mm</td></tr>
     <tr><td>Joining</td><td class="v">Bolted throughout, no welding</td></tr>
    </tbody></table>
   </div>
  </div>
  <h3 class="b">Part tree</h3>
  <div class="tree">{tree}</div>
  <div class="note"><strong>The one rule that governs every vertical dimension.</strong> The top face of the deck mesh panel, RK-A-203, <em>is</em> the bed datum. Deck rail and beam hang below it; tray, canopy and LED are measured up from it. Build each deck to the datum, not to the beam it sits on — the tier section drawing in the Manufacturing Pack shows the full stack.</div>
  <div class="note w"><strong>Two open items carried from validation.</strong> The wall anchors RK-A-106 are a fitted item, not an option — an empty rack tips under a 139 N pull at the top bed. And the depth-plane bracing, with per-tier cross beams deleted, is closed only by acceptance test T16, the sway test. Both are recorded in the Engineering Validation Record, RK-A-QC.</div>
  <div class="note w"><strong>Two corrections in this revision are worth reading before you cut anything.</strong> The rear X-brace RK-A-104 was dimensioned at 1345 mm in Rev 1 and is <strong>1797 mm</strong> — Rev 1 would have produced a part 452 mm too short to fit. And the flood tray RK-A-401 now carries a moulded 30 mm overflow collar and two bosses off the tray centreline; those are form-tool dimensions, not site drilling.</div>
 </div>
</section>

{''.join(chapter(i,p) for i,p in enumerate(PARTS))}

<section class="ch" id="notes">
 <div class="pg">
  <div class="chhead"><span class="chno">Appendix</span><h2>Reading these drawings</h2><span class="pgno">Page 18</span></div>
  <div class="two">
   <div>
    <h3>Conventions</h3>
    <p><strong>First-angle projection</strong> throughout, per ISO and Indian practice — the symbol appears in every title block. Front view top left, end view to its right, plan below, isometric bottom right.</p>
    <p><strong>All dimensions in millimetres</strong>, unstated. Solid outlines are visible edges; dashed grey is hidden detail such as the inner wall of a hollow section; fine chain lines are centrelines.</p>
    <p><strong>Long parts are drawn broken.</strong> A zigzag break in the middle of a view means the part is shown shortened so the section stays legible. The overall dimension is always the true length — read the dimension, not the drawing.</p>
    <p><strong>Isometric views are illustrative</strong> and not to scale. They are there to orient the reader, not to be measured.</p>
   </div>
   <div>
    <h3>General tolerances</h3>
    <table class="spec"><tbody>
     <tr><td>Cut length, sections</td><td class="v">±1.0 mm</td></tr>
     <tr><td>Cut squareness</td><td class="v">±0.5°</td></tr>
     <tr><td>Hole diameter Ø9</td><td class="v">+0.2 / −0.0</td></tr>
     <tr><td>Hole position, general</td><td class="v">±0.3 mm from datum</td></tr>
     <tr><td>Grid pitch, cumulative</td><td class="v">±0.2 mm over any 400 mm</td></tr>
     <tr><td>Bend angle</td><td class="v">±0.5°</td></tr>
     <tr><td>Sheet blank size</td><td class="v">±1.0 mm</td></tr>
     <tr><td>Burr</td><td class="v">≤ 0.1 mm, both faces</td></tr>
     <tr><td>Edge condition</td><td class="v">All handled edges broken</td></tr>
    </tbody></table>
   </div>
  </div>
  <h3 class="b">Companion documents</h3>
  <table class="spec"><tbody>
   <tr><td>RK-A-MFG</td><td class="v">Manufacturing Pack — GA, BOM, cut list, fasteners, assembly manual, QC, validation, costing</td></tr>
   <tr><td>RACK-P0</td><td class="v">Requirement register — the decisions and evidence behind every dimension here</td></tr>
   <tr><td>RK-A-QC</td><td class="v">Engineering Validation Record — Stage 1 rack, Stage 2 room, 18 acceptance tests</td></tr>
   <tr><td>CAD release</td><td class="v">Desktop\\CEA_RACK_v1\\INTEGRATED_v2 — 45 STEP parts, assembly STEP and F3D, model Rev 5</td></tr>
  </tbody></table>
  <h3 class="b">Revision history</h3>
  <table class="spec"><tbody>
   <tr><td>Rev 1 · 04 Sep 2026</td><td class="v">First issue, 14 parts. From CEA_RACK_PLATFORM_RackA_v1. Base frame raised 120 → 180 mm for 150 mm floor clearance; wall anchor RK-A-106 added after the tip-over check.</td></tr>
   <tr><td>Rev 2 · 05 Sep 2026</td><td class="v">Structural set reissued against CEA_RACK_INTEGRATED_v2 Rev 5, after systems integration and the Stage 1 validation. Eleven parts issued, three held.</td></tr>
  </tbody></table>
  <h3 class="b">What changed in Rev 2</h3>
  <table class="spec"><tbody>
   <tr><td>RK-A-104</td><td class="v"><strong>Length 1345 → 1797 mm.</strong> Rev 1 did not match the model: the brace spans a 1195 × 1342 opening whose diagonal is 1797. Hole centres 1305 → 1757.</td></tr>
   <tr><td>RK-A-401</td><td class="v">Overflow is now a <strong>30 mm collar moulded into the tray floor</strong>, replacing the loose standpipe. Drain boss relocated off the tray centreline to 60 from the right end and 480 from the front edge; overflow collar at 120 from the right end on the same line. All three are form-tool dimensions.</td></tr>
   <tr><td>RK-A-203</td><td class="v">Mass reconciled at 1.98 kg per panel. The model had briefly carried a 35% open-area density; corrected to 1884 kg/m³ for ≥70% open expanded mesh. Rack dry mass 126.2 → <strong>112.7 kg</strong>.</td></tr>
   <tr><td>RK-A-106</td><td class="v">Back-to-back variant added: in the room layout rows B and C bolt to each other through this bracket rather than to a wall.</td></tr>
   <tr><td>RK-A-103</td><td class="v">Open sway item re-referenced from prototype test P3 to acceptance test T16 in the Engineering Validation Record.</td></tr>
   <tr><td>Held</td><td class="v">RK-A-301, RK-A-501, RK-A-502 withdrawn pending the plenum design. Their Rev 1 sheets are superseded and must not be used — mounting positions have moved.</td></tr>
  </tbody></table>
  <div class="note"><strong>Where a drawing and the released model disagree, the model governs</strong> — with one recorded exception. RK-A-203 is the case where the drawing was right and the model was wrong, and the model was corrected to match. Both are reconciled as of Rev 5.</div>
 </div>
</section>
</main>

<footer><div class="pg"><p>RK-A-DWG Rev 2 · 05 September 2026 · 11 structural parts issued, 3 held · 15 pages · First-angle projection · Dimensions in mm · Generated from CEA_RACK_INTEGRATED_v2 Rev 5</p></div></footer>
"""
open('/home/claude/cea_rack_structural_drawings.html','w').write(HTML)
print('written %d KB'%(len(HTML)//1024))
