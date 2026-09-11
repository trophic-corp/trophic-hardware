# Lighting BOM, Commercial and Programme Cash Model

**Status:** EARLY PLANNING MODEL, NOT COMMERCIAL TRUTH · **Generated:** 2026-09-11 by `lighting_cost_model.py` · **Owner:** main session

Every input carries an evidence class: **QUOTE** (none yet), **RMKT** researched market class (dated, see the supplier landscape and competitor reference), **EST** engineering estimate, **ASSUME** configurable planning assumption, **TBD**. No line is a supplier quotation. Regenerate by editing the script's assumption blocks; do not hand-edit this file. Gross revenue, revenue excluding GST, gross margin, contribution and net profit are kept distinct throughout; **nothing here is net profit** because fixed operating expenses, salaries, marketing and R&D amortisation are not included except where §7 says so.

## 1. Unit BOM at the 100-unit tier

### Core 30

| Line | ₹ at 100 | Category | Evidence | Note |
|---|---:|---|---|---|
| Extrusion body | 97 | extrusion | RMKT/ASSUME | 0.8 kg/m × 0.32 m × ₹380/kg; profile mass is an assumption |
| CNC end machining | 150 | machining | RMKT | ₹40–150 per end class, two ends |
| Bead-blast + Type II anodise | 110 | anodise | EST | per-piece incl. minimum-charge share |
| End caps, machined Al pair | 300 | endcaps | EST | moulded ₹80/pair at scale + tool |
| LEDs: mid-power white | 160 | leds | RMKT | 20 × ₹8 (Bridgelux/Nichia 3030 class, reel qty) |
| LEDs: 660 nm red | 100 | leds | RMKT | 4 × ₹25 (3030 red, reel qty) |
| MCPCB | 140 | pcbfab | RMKT | Indian fab ₹200/pc listing class at MOQ 100, scaled by length |
| CC driver stage | 110 | elec | EST | 1 buck CC string(s) × ₹110 (IC + inductor + passives) |
| Engine board: MCU, NTC, ID EEPROM, ideal diode/eFuse, UVLO/OVP, 5 V housekeeping buck, port load switch + TVS, FR-4 | 340 | elec | EST | Lighting/Electronics 2026-09-11: engine board excl. drivers ₹400–700 class at 100 incl. housekeeping; mid value used |
| DC input connector | 50 | connector | EST | barrel class; sealed circular ₹120+ |
| Control port connector | 80 | connector | EST | sealed 3–4 pin class, fixture side |
| PCBA (SMT labour, two boards) | 110 | pcba | EST | Coimbatore EMS; setup charged separately |
| Optical cover | 80 | optics | EST | PMMA cut sheet or profile |
| Thermal interface material | 12 | elec | EST |  |
| Mounting hardware (legs, pads, fasteners) | 200 | machining | EST | machined/sheet at low volume |
| Gaskets / seals | 35 | elec | EST | die-cut EPDM/silicone |
| External adapter (certified) | 480 | psu | RMKT | 24 V-class 36 W / 60 W BIS-registered adapter ₹400–700 class (Indian OEM); Mean Well GST higher |
| Final assembly labour | 130 | assembly | EST |  |
| EOL test | 35 | assembly | EST | jig speaks the control protocol |
| Packaging | 110 | packaging | EST | kraft carton + pulp/board insert + sleeve |
| **Subtotal + 3 % scrap/rework** | **2,914** | | | |

### Core 45

| Line | ₹ at 100 | Category | Evidence | Note |
|---|---:|---|---|---|
| Extrusion body | 143 | extrusion | RMKT/ASSUME | 0.8 kg/m × 0.47 m × ₹380/kg; profile mass is an assumption |
| CNC end machining | 160 | machining | RMKT | ₹40–150 per end class, two ends |
| Bead-blast + Type II anodise | 130 | anodise | EST | per-piece incl. minimum-charge share |
| End caps, machined Al pair | 300 | endcaps | EST | moulded ₹80/pair at scale + tool |
| LEDs: mid-power white | 240 | leds | RMKT | 30 × ₹8 (Bridgelux/Nichia 3030 class, reel qty) |
| LEDs: 660 nm red | 150 | leds | RMKT | 6 × ₹25 (3030 red, reel qty) |
| MCPCB | 190 | pcbfab | RMKT | Indian fab ₹200/pc listing class at MOQ 100, scaled by length |
| CC driver stage | 110 | elec | EST | 1 buck CC string(s) × ₹110 (IC + inductor + passives) |
| Engine board: MCU, NTC, ID EEPROM, ideal diode/eFuse, UVLO/OVP, 5 V housekeeping buck, port load switch + TVS, FR-4 | 340 | elec | EST | Lighting/Electronics 2026-09-11: engine board excl. drivers ₹400–700 class at 100 incl. housekeeping; mid value used |
| DC input connector | 50 | connector | EST | barrel class; sealed circular ₹120+ |
| Control port connector | 80 | connector | EST | sealed 3–4 pin class, fixture side |
| PCBA (SMT labour, two boards) | 115 | pcba | EST | Coimbatore EMS; setup charged separately |
| Optical cover | 110 | optics | EST | PMMA cut sheet or profile |
| Thermal interface material | 16 | elec | EST |  |
| Mounting hardware (legs, pads, fasteners) | 200 | machining | EST | machined/sheet at low volume |
| Gaskets / seals | 35 | elec | EST | die-cut EPDM/silicone |
| External adapter (certified) | 480 | psu | RMKT | 24 V-class 36 W / 60 W BIS-registered adapter ₹400–700 class (Indian OEM); Mean Well GST higher |
| Final assembly labour | 130 | assembly | EST |  |
| EOL test | 35 | assembly | EST | jig speaks the control protocol |
| Packaging | 125 | packaging | EST | kraft carton + pulp/board insert + sleeve |
| **Subtotal + 3 % scrap/rework** | **3,233** | | | |

### Core 60

| Line | ₹ at 100 | Category | Evidence | Note |
|---|---:|---|---|---|
| Extrusion body | 188 | extrusion | RMKT/ASSUME | 0.8 kg/m × 0.62 m × ₹380/kg; profile mass is an assumption |
| CNC end machining | 170 | machining | RMKT | ₹40–150 per end class, two ends |
| Bead-blast + Type II anodise | 150 | anodise | EST | per-piece incl. minimum-charge share |
| End caps, machined Al pair | 300 | endcaps | EST | moulded ₹80/pair at scale + tool |
| LEDs: mid-power white | 320 | leds | RMKT | 40 × ₹8 (Bridgelux/Nichia 3030 class, reel qty) |
| LEDs: 660 nm red | 200 | leds | RMKT | 8 × ₹25 (3030 red, reel qty) |
| MCPCB | 240 | pcbfab | RMKT | Indian fab ₹200/pc listing class at MOQ 100, scaled by length |
| CC driver stage | 220 | elec | EST | 2 buck CC string(s) × ₹110 (IC + inductor + passives) |
| Engine board: MCU, NTC, ID EEPROM, ideal diode/eFuse, UVLO/OVP, 5 V housekeeping buck, port load switch + TVS, FR-4 | 340 | elec | EST | Lighting/Electronics 2026-09-11: engine board excl. drivers ₹400–700 class at 100 incl. housekeeping; mid value used |
| DC input connector | 50 | connector | EST | barrel class; sealed circular ₹120+ |
| Control port connector | 80 | connector | EST | sealed 3–4 pin class, fixture side |
| PCBA (SMT labour, two boards) | 120 | pcba | EST | Coimbatore EMS; setup charged separately |
| Optical cover | 140 | optics | EST | PMMA cut sheet or profile |
| Thermal interface material | 20 | elec | EST |  |
| Mounting hardware (legs, pads, fasteners) | 200 | machining | EST | machined/sheet at low volume |
| Gaskets / seals | 35 | elec | EST | die-cut EPDM/silicone |
| External adapter (certified) | 650 | psu | RMKT | 24 V-class 36 W / 60 W BIS-registered adapter ₹400–700 class (Indian OEM); Mean Well GST higher |
| Final assembly labour | 130 | assembly | EST |  |
| EOL test | 35 | assembly | EST | jig speaks the control protocol |
| Packaging | 140 | packaging | EST | kraft carton + pulp/board insert + sleeve |
| **Subtotal + 3 % scrap/rework** | **3,840** | | | |

### WRGB 30

| Line | ₹ at 100 | Category | Evidence | Note |
|---|---:|---|---|---|
| Extrusion body | 97 | extrusion | RMKT/ASSUME | shared housing assumed (cost test pending); +20 % if a wider WRGB-only profile |
| CNC end machining | 170 | machining | RMKT |  |
| Bead-blast + Type II anodise | 110 | anodise | EST |  |
| End caps, machined Al pair | 300 | endcaps | EST |  |
| LEDs: colour (R/G/B/deep red) | 840 | leds | RMKT/EST | 24 × ₹35 (branded 3030 colour, reel/cut-tape mix) |
| LEDs: high-CRI white | 120 | leds | RMKT | 12 × ₹10 |
| MCPCB (denser, higher-k) | 200 | pcbfab | EST |  |
| CC driver stages | 525 | elec | EST | 5 channels × ₹105 |
| Engine board: MCU (≥5 PWM), NTC, ID EEPROM, protection, 5 V housekeeping, port switch + TVS, FR-4 | 420 | elec | EST | more PWM channels, 80 V-class parts if 48 V bus |
| DC input connector | 50 | connector | EST |  |
| Control port connector | 80 | connector | EST |  |
| PCBA (SMT labour, two boards) | 170 | pcba | EST |  |
| Optical cover / diffuser | 110 | optics | EST | mixing diffuser; lens array would be higher |
| Thermal interface material | 15 | elec | EST |  |
| Mounting hardware | 220 | machining | EST | rated for WRGB mass |
| Gaskets / seals | 35 | elec | EST |  |
| External adapter (certified) | 700 | psu | RMKT | 60 / 90 / 120 W class; Mean Well GST or Indian OEM |
| Final assembly labour | 220 | assembly | EST |  |
| EOL test | 70 | assembly | EST | per-channel photometric + thermal |
| Packaging | 180 | packaging | EST | heavier board grade |
| **Subtotal + 3 % scrap/rework** | **4,771** | | | |

### WRGB 45

| Line | ₹ at 100 | Category | Evidence | Note |
|---|---:|---|---|---|
| Extrusion body | 143 | extrusion | RMKT/ASSUME | shared housing assumed (cost test pending); +20 % if a wider WRGB-only profile |
| CNC end machining | 180 | machining | RMKT |  |
| Bead-blast + Type II anodise | 130 | anodise | EST |  |
| End caps, machined Al pair | 300 | endcaps | EST |  |
| LEDs: colour (R/G/B/deep red) | 1,260 | leds | RMKT/EST | 36 × ₹35 (branded 3030 colour, reel/cut-tape mix) |
| LEDs: high-CRI white | 180 | leds | RMKT | 18 × ₹10 |
| MCPCB (denser, higher-k) | 270 | pcbfab | EST |  |
| CC driver stages | 525 | elec | EST | 5 channels × ₹105 |
| Engine board: MCU (≥5 PWM), NTC, ID EEPROM, protection, 5 V housekeeping, port switch + TVS, FR-4 | 420 | elec | EST | more PWM channels, 80 V-class parts if 48 V bus |
| DC input connector | 50 | connector | EST |  |
| Control port connector | 80 | connector | EST |  |
| PCBA (SMT labour, two boards) | 180 | pcba | EST |  |
| Optical cover / diffuser | 140 | optics | EST | mixing diffuser; lens array would be higher |
| Thermal interface material | 20 | elec | EST |  |
| Mounting hardware | 220 | machining | EST | rated for WRGB mass |
| Gaskets / seals | 35 | elec | EST |  |
| External adapter (certified) | 900 | psu | RMKT | 60 / 90 / 120 W class; Mean Well GST or Indian OEM |
| Final assembly labour | 220 | assembly | EST |  |
| EOL test | 70 | assembly | EST | per-channel photometric + thermal |
| Packaging | 200 | packaging | EST | heavier board grade |
| **Subtotal + 3 % scrap/rework** | **5,689** | | | |

### WRGB 60

| Line | ₹ at 100 | Category | Evidence | Note |
|---|---:|---|---|---|
| Extrusion body | 188 | extrusion | RMKT/ASSUME | shared housing assumed (cost test pending); +20 % if a wider WRGB-only profile |
| CNC end machining | 190 | machining | RMKT |  |
| Bead-blast + Type II anodise | 150 | anodise | EST |  |
| End caps, machined Al pair | 300 | endcaps | EST |  |
| LEDs: colour (R/G/B/deep red) | 1,680 | leds | RMKT/EST | 48 × ₹35 (branded 3030 colour, reel/cut-tape mix) |
| LEDs: high-CRI white | 240 | leds | RMKT | 24 × ₹10 |
| MCPCB (denser, higher-k) | 340 | pcbfab | EST |  |
| CC driver stages | 525 | elec | EST | 5 channels × ₹105 |
| Engine board: MCU (≥5 PWM), NTC, ID EEPROM, protection, 5 V housekeeping, port switch + TVS, FR-4 | 420 | elec | EST | more PWM channels, 80 V-class parts if 48 V bus |
| DC input connector | 50 | connector | EST |  |
| Control port connector | 80 | connector | EST |  |
| PCBA (SMT labour, two boards) | 190 | pcba | EST |  |
| Optical cover / diffuser | 170 | optics | EST | mixing diffuser; lens array would be higher |
| Thermal interface material | 25 | elec | EST |  |
| Mounting hardware | 220 | machining | EST | rated for WRGB mass |
| Gaskets / seals | 35 | elec | EST |  |
| External adapter (certified) | 1,100 | psu | RMKT | 60 / 90 / 120 W class; Mean Well GST or Indian OEM |
| Final assembly labour | 220 | assembly | EST |  |
| EOL test | 70 | assembly | EST | per-channel photometric + thermal |
| Packaging | 220 | packaging | EST | heavier board grade |
| **Subtotal + 3 % scrap/rework** | **6,605** | | | |

### Smart Module

| Line | ₹ at 100 | Category | Evidence | Note |
|---|---:|---|---|---|
| MCU + radio module (ESP32-C3 class) | 160 | elec | RMKT | pre-approved module |
| RTC + supercapacitor backup | 150 | elec | RMKT | RV-3028 class + supercap |
| PCB (FR-4) | 35 | pcbfab | EST |  |
| Passives, port driver, protection, regulator | 90 | elec | EST |  |
| Buttons / status LED | 20 | elec | EST |  |
| Port connector + 1 m tether cable | 170 | connector | EST | sealed 3–4 pin + cable |
| Enclosure (machined Al or polymer puck) | 260 | endcaps | EST | moulded ₹70 at scale + ~₹3 lakh tool |
| Gasket | 20 | elec | EST |  |
| PCBA (SMT labour) | 90 | pcba | EST |  |
| Final assembly | 80 | assembly | EST |  |
| EOL test (radio, RTC, port) | 40 | assembly | EST |  |
| Packaging | 60 | packaging | EST |  |
| **Subtotal + 3 % scrap/rework** | **1,210** | | | |

## 2. Unit cost by volume tier

Volume factors per category (proto = hand-built on stock extrusion with cut-tape LEDs; scaled = 500 units with moulded end caps and puck). Scrap/rework 5 / 5 / 4 / 3 / 3 / 2 %.

| SKU | proto (5) | pilot (15) | 25 (25) | 50 (50) | 100 (100) | scaled (500) |
|---|---:|---:|---:|---:|---:|---:|
| Core 30 | ₹6,821 | ₹4,924 | ₹3,998 | ₹3,388 | ₹2,914 | ₹2,017 |
| Core 45 | ₹7,647 | ₹5,461 | ₹4,444 | ₹3,765 | ₹3,233 | ₹2,260 |
| Core 60 | ₹8,908 | ₹6,383 | ₹5,231 | ₹4,456 | ₹3,840 | ₹2,731 |
| WRGB 30 | ₹10,625 | ₹7,863 | ₹6,467 | ₹5,528 | ₹4,771 | ₹3,445 |
| WRGB 45 | ₹12,539 | ₹9,263 | ₹7,663 | ₹6,575 | ₹5,689 | ₹4,159 |
| WRGB 60 | ₹14,449 | ₹10,660 | ₹8,857 | ₹7,621 | ₹6,605 | ₹4,872 |
| Smart Module | ₹2,798 | ₹2,092 | ₹1,688 | ₹1,418 | ₹1,210 | ₹787 |

Owner planning figures for comparison (ASSUME, from the Phase 0 brief): Core small sizes ~₹1,400–1,600; WRGB ~₹10,000 / 14,000 / 19,000 at 100 units. **The bottom-up Core estimate is roughly 1.7–2× the owner figure at 100 units and approaches it only at the scaled tier with moulded caps; the bottom-up WRGB estimate is well below the owner figure.** Both gaps must be closed by RFQ, not by adjusting the model. See §8.

## 3. Commercial model per SKU

Assumptions: GST 18 %; payment gateway/platform 2 % of gross; packaging/shipping allowance Core ₹180, WRGB ₹260, module ₹90; warranty reserve Core 4 %, WRGB 5 % of COGS. Prices are positioning assumptions (see §5). Contribution = net revenue − COGS − gateway − shipping − warranty reserve. It is **not** net profit.

### At the 50-unit COGS tier

| SKU | Retail incl. GST | Net ex-GST | COGS | Gateway | Ship | Warranty | Gross margin % | Contribution ₹ | Contribution % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Core 30 Basic | ₹3,499 | ₹2,965 | ₹3,388 | ₹70 | ₹180 | ₹136 | -14 % | ₹-808 | -27 % |
| Core 30 Smart | ₹4,499 | ₹3,813 | ₹4,806 | ₹90 | ₹180 | ₹192 | -26 % | ₹-1,456 | -38 % |
| Core 45 Basic | ₹3,999 | ₹3,389 | ₹3,765 | ₹80 | ₹180 | ₹151 | -11 % | ₹-787 | -23 % |
| Core 45 Smart | ₹4,999 | ₹4,236 | ₹5,184 | ₹100 | ₹180 | ₹207 | -22 % | ₹-1,434 | -34 % |
| Core 60 Basic | ₹4,499 | ₹3,813 | ₹4,456 | ₹90 | ₹180 | ₹178 | -17 % | ₹-1,091 | -29 % |
| Core 60 Smart | ₹5,499 | ₹4,660 | ₹5,874 | ₹110 | ₹180 | ₹235 | -26 % | ₹-1,739 | -37 % |
| WRGB 30 Standalone | ₹7,999 | ₹6,779 | ₹5,528 | ₹160 | ₹260 | ₹276 | 18 % | ₹555 | 8 % |
| WRGB 30 Smart | ₹8,999 | ₹7,626 | ₹6,946 | ₹180 | ₹260 | ₹347 | 9 % | ₹-107 | -1 % |
| WRGB 45 Standalone | ₹9,999 | ₹8,474 | ₹6,575 | ₹200 | ₹260 | ₹329 | 22 % | ₹1,110 | 13 % |
| WRGB 45 Smart | ₹10,999 | ₹9,321 | ₹7,993 | ₹220 | ₹260 | ₹400 | 14 % | ₹448 | 5 % |
| WRGB 60 Standalone | ₹12,499 | ₹10,592 | ₹7,621 | ₹250 | ₹260 | ₹381 | 28 % | ₹2,080 | 20 % |
| WRGB 60 Smart | ₹13,499 | ₹11,440 | ₹9,039 | ₹270 | ₹260 | ₹452 | 21 % | ₹1,419 | 12 % |
| Smart Module (upgrade) | ₹1,499 | ₹1,270 | ₹1,418 | ₹30 | ₹90 | ₹71 | -12 % | ₹-339 | -27 % |

### At the 100-unit COGS tier

| SKU | Retail incl. GST | Net ex-GST | COGS | Gateway | Ship | Warranty | Gross margin % | Contribution ₹ | Contribution % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Core 30 Basic | ₹3,499 | ₹2,965 | ₹2,914 | ₹70 | ₹180 | ₹117 | 2 % | ₹-315 | -11 % |
| Core 30 Smart | ₹4,499 | ₹3,813 | ₹4,124 | ₹90 | ₹180 | ₹165 | -8 % | ₹-746 | -20 % |
| Core 45 Basic | ₹3,999 | ₹3,389 | ₹3,233 | ₹80 | ₹180 | ₹129 | 5 % | ₹-233 | -7 % |
| Core 45 Smart | ₹4,999 | ₹4,236 | ₹4,443 | ₹100 | ₹180 | ₹178 | -5 % | ₹-665 | -16 % |
| Core 60 Basic | ₹4,499 | ₹3,813 | ₹3,840 | ₹90 | ₹180 | ₹154 | -1 % | ₹-451 | -12 % |
| Core 60 Smart | ₹5,499 | ₹4,660 | ₹5,050 | ₹110 | ₹180 | ₹202 | -8 % | ₹-882 | -19 % |
| WRGB 30 Standalone | ₹7,999 | ₹6,779 | ₹4,771 | ₹160 | ₹260 | ₹239 | 30 % | ₹1,349 | 20 % |
| WRGB 30 Smart | ₹8,999 | ₹7,626 | ₹5,981 | ₹180 | ₹260 | ₹299 | 22 % | ₹906 | 12 % |
| WRGB 45 Standalone | ₹9,999 | ₹8,474 | ₹5,689 | ₹200 | ₹260 | ₹284 | 33 % | ₹2,041 | 24 % |
| WRGB 45 Smart | ₹10,999 | ₹9,321 | ₹6,899 | ₹220 | ₹260 | ₹345 | 26 % | ₹1,597 | 17 % |
| WRGB 60 Standalone | ₹12,499 | ₹10,592 | ₹6,605 | ₹250 | ₹260 | ₹330 | 38 % | ₹3,147 | 30 % |
| WRGB 60 Smart | ₹13,499 | ₹11,440 | ₹7,816 | ₹270 | ₹260 | ₹391 | 32 % | ₹2,703 | 24 % |
| Smart Module (upgrade) | ₹1,499 | ₹1,270 | ₹1,210 | ₹30 | ₹90 | ₹61 | 5 % | ₹-120 | -9 % |

### At the scaled-unit COGS tier

| SKU | Retail incl. GST | Net ex-GST | COGS | Gateway | Ship | Warranty | Gross margin % | Contribution ₹ | Contribution % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Core 30 Basic | ₹3,499 | ₹2,965 | ₹2,017 | ₹70 | ₹180 | ₹81 | 32 % | ₹617 | 21 % |
| Core 30 Smart | ₹4,499 | ₹3,813 | ₹2,804 | ₹90 | ₹180 | ₹112 | 26 % | ₹627 | 16 % |
| Core 45 Basic | ₹3,999 | ₹3,389 | ₹2,260 | ₹80 | ₹180 | ₹90 | 33 % | ₹778 | 23 % |
| Core 45 Smart | ₹4,999 | ₹4,236 | ₹3,047 | ₹100 | ₹180 | ₹122 | 28 % | ₹787 | 19 % |
| Core 60 Basic | ₹4,499 | ₹3,813 | ₹2,731 | ₹90 | ₹180 | ₹109 | 28 % | ₹703 | 18 % |
| Core 60 Smart | ₹5,499 | ₹4,660 | ₹3,518 | ₹110 | ₹180 | ₹141 | 25 % | ₹712 | 15 % |
| WRGB 30 Standalone | ₹7,999 | ₹6,779 | ₹3,445 | ₹160 | ₹260 | ₹172 | 49 % | ₹2,742 | 40 % |
| WRGB 30 Smart | ₹8,999 | ₹7,626 | ₹4,232 | ₹180 | ₹260 | ₹212 | 45 % | ₹2,743 | 36 % |
| WRGB 45 Standalone | ₹9,999 | ₹8,474 | ₹4,159 | ₹200 | ₹260 | ₹208 | 51 % | ₹3,647 | 43 % |
| WRGB 45 Smart | ₹10,999 | ₹9,321 | ₹4,946 | ₹220 | ₹260 | ₹247 | 47 % | ₹3,648 | 39 % |
| WRGB 60 Standalone | ₹12,499 | ₹10,592 | ₹4,872 | ₹250 | ₹260 | ₹244 | 54 % | ₹4,966 | 47 % |
| WRGB 60 Smart | ₹13,499 | ₹11,440 | ₹5,659 | ₹270 | ₹260 | ₹283 | 51 % | ₹4,968 | 43 % |
| Smart Module (upgrade) | ₹1,499 | ₹1,270 | ₹787 | ₹30 | ₹90 | ₹39 | 38 % | ₹324 | 26 % |

## 4. Sensitivity to COGS (contribution ₹ per unit at the 100-unit tier)

| SKU | COGS −20 % | −10 % | base | +10 % | +20 % | Retail floor for 25 % contribution (base COGS) |
|---|---:|---:|---:|---:|---:|---:|
| Core 30 Basic | ₹291 | ₹-12 | ₹-315 | ₹-618 | ₹-921 | ₹5,215 |
| Core 30 Smart | ₹111 | ₹-317 | ₹-746 | ₹-1,175 | ₹-1,604 | ₹7,260 |
| Core 45 Basic | ₹439 | ₹103 | ₹-233 | ₹-570 | ₹-906 | ₹5,755 |
| Core 45 Smart | ₹260 | ₹-203 | ₹-665 | ₹-1,127 | ₹-1,589 | ₹7,799 |
| Core 60 Basic | ₹348 | ₹-51 | ₹-451 | ₹-850 | ₹-1,249 | ₹6,780 |
| Core 60 Smart | ₹169 | ₹-357 | ₹-882 | ₹-1,407 | ₹-1,932 | ₹8,824 |
| WRGB 30 Standalone | ₹2,351 | ₹1,850 | ₹1,349 | ₹848 | ₹347 | ₹8,560 |
| WRGB 30 Smart | ₹2,162 | ₹1,534 | ₹906 | ₹278 | ₹-350 | ₹10,624 |
| WRGB 45 Standalone | ₹3,235 | ₹2,638 | ₹2,041 | ₹1,443 | ₹846 | ₹10,125 |
| WRGB 45 Smart | ₹3,046 | ₹2,322 | ₹1,597 | ₹873 | ₹149 | ₹12,190 |
| WRGB 60 Standalone | ₹4,534 | ₹3,840 | ₹3,147 | ₹2,453 | ₹1,760 | ₹11,689 |
| WRGB 60 Smart | ₹4,345 | ₹3,524 | ₹2,703 | ₹1,883 | ₹1,062 | ₹13,753 |
| Smart Module (upgrade) | ₹134 | ₹7 | ₹-120 | ₹-247 | ₹-375 | ₹2,210 |

## 5. Pricing rationale (positioning, not COGS × markup)

Reference points from `docs/references/lighting/COMPETITOR_LIGHTING_REFERENCE.md` (Indian retail, 2026-09-11): Neo Helios XP-300 ₹2,400–2,550, XP-450 ₹1,910–2,250, XP-600 ₹3,250–3,999 (white-only, no dimming, no schedule, no stated warranty); Week Aqua S-series ₹5,999–7,999 (entry WRGB, app); Chihiros WRGB II Slim 60 ₹15,525, WRGB II 60 ₹24,725, Pro 60 ₹28,275; Twinstar 600EA III ₹18,000, 600S III ₹27,499; ADA Aquasky RGB 60 ₹52,000.

- **Core Basic** sits at the top of the Neo Helios band, justified by dimming, a soft-start default profile, a published PPFD/spectrum sheet, a stated IP class, a stated warranty and an upgrade port. It cannot sit at the bottom of that band at pilot volumes: §3 shows the 50-unit COGS leaves no contribution below ~₹3,500 for 30 cm.
- **Core Smart** adds the module for ~₹1,000; the pair lands under Week Aqua S while offering app scheduling on a fixed spectrum.
- **WRGB Standalone** occupies the space above budget WRGB (Week Aqua S) and below Chihiros Slim; **WRGB Smart** at 60 cm lands ~₹2,000 under Slim 60 and ~₹11,000 under WRGB II 60, the premium-value position the owner asked for.
- **Dealer floor check:** at a future 25 % dealer margin off retail, the D2C contribution % in §3 falls by roughly that share of net revenue; Core Basic at the 100-unit tier does not survive a dealer margin, WRGB does. Dealer channel is therefore a scaled-tier question.
- Indian willingness to pay for a domestic brand above the Chinese incumbent is **unvalidated (TBD)**; the field pilot should test price acceptance directly.

## 6. Programme cash

| Item | ₹ | Evidence | Note | Cash class |
|---|---:|---|---|---|
| Extrusion die | ₹40,000 | RMKT/EST | ₹13.5k–35k listing class; finned profile assumed at the upper end | expense |
| Extrusion minimum run (150 kg negotiated) | ₹57,000 | ASSUME | 500 kg standard MOQ would be ₹1,90,000; ~187 m ≈ 400 fixtures at 45 cm → stock | inventory |
| MCPCB MOQ carry (6 artworks × 100 pcs) | ₹90,000 | RMKT/EST | Indian fab folds NRE into MOQ 100; overrun is usable stock | inventory |
| PCBA stencils + setup, batch 1 (9 artworks) | ₹72,000 | EST | ₹3–8k stencil + ₹5–15k setup per artwork, per run | expense |
| Packaging print run (sleeves, 2 designs) | ₹20,000 | EST | offset MOQ 500–1,000 | expense |
| Test instruments: quantum sensor | ₹60,000 | RMKT | Apogee MQ-500 class | expense |
| Test instruments: thermal camera, bench PSU, e-load, DMM | ₹85,000 | EST |  | expense |
| Spectroradiometer (rental / lab per design) | ₹30,000 | EST |  | expense |
| Lab tests: IEC 62471, EMC pre-scan, salt fog, damp-heat box | ₹105,000 | EST | 40k + 40k + 10k + 15k | expense |
| Regulatory: WPC ETA (module) + BIS scope consulting | ₹75,000 | EST | 25k + 50k contingency; adapter bought registered | expense |
| Firmware + app development (external contract) | ₹200,000 | ASSUME | set to 0 if fully in-house; founder labour not costed | expense |
| Prototype consumables, spare boards, stock extrusion, CNC | ₹60,000 | EST |  | expense |
| Field pilot logistics and support | ₹20,000 | EST | 12 serialised units from DVT stock | expense |
| Engineering prototypes (10 units, proto tier) | ₹72,833 | EST | {'Core 30': 1, 'Core 45': 2, 'WRGB 45': 2, 'WRGB 60': 1, 'Smart Module': 4} | expense |
| EVT/DVT build (32 units, pilot tier, first die run) | ₹159,148 | EST | {'Core 30': 3, 'Core 45': 4, 'Core 60': 3, 'WRGB 30': 2, 'WRGB 45': 4, 'WRGB 60': 2, 'Smart Module': 14} | expense (12 reused for field pilot) |
| First commercial batch (70 units, 50-unit tier) | ₹218,158 | EST | {'Core 30': 12, 'Core 45': 16, 'WRGB 30': 4, 'WRGB 45': 8, 'Smart Module': 30} | inventory |
| **Total cash before first meaningful sales** | **₹1,364,139** | | of which expense ₹998,981, inventory ₹365,158 | |
| Deferred tooling (not in the above) | ₹700,000 | RMKT/EST | End-cap injection mould ₹400,000 (₹2–8 lakh simple mould class; justified at ≥ ~300 units); Smart Module puck mould ₹300,000 (justified at ≥ ~300 modules) | later |

### Batch-1 scenarios sold through

**Scenario A, Core-led (40 fixtures + 30 modules, build cost ₹218,158)** (mix: {'Core 30 Basic': 6, 'Core 30 Smart': 6, 'Core 45 Basic': 6, 'Core 45 Smart': 10, 'WRGB 30 Standalone': 1, 'WRGB 30 Smart': 3, 'WRGB 45 Standalone': 2, 'WRGB 45 Smart': 6, 'Smart Module (upgrade)': 5}; COGS at the 50-unit tier): gross revenue incl. GST ₹250,455; net revenue ex-GST ₹212,250; COGS ₹218,158; **contribution after variable costs ₹-29,199** (-14 % of net).

**Scenario B, WRGB-led (36 fixtures + 36 modules, build cost ₹261,745)** (mix: {'Core 45 Smart': 10, 'WRGB 30 Smart': 6, 'WRGB 45 Smart': 12, 'WRGB 60 Smart': 8, 'Smart Module (upgrade)': 0}; COGS at the 50-unit tier): gross revenue incl. GST ₹343,964; net revenue ex-GST ₹291,495; COGS ₹261,745; **contribution after variable costs ₹1,741** (1 % of net).

Neither scenario recovers the programme expense; both are market-entry batches. Scenario B turns a negative variable contribution into a positive one because WRGB carries margin at pilot volume and Core does not. Scenario A is retained because it tests the volume product with real customers, which Scenario B does not. A hybrid (Scenario B plus ~10 Core Smart at a deliberately loss-making entry price, tracked as a marketing cost) is the recommended shape; OWNER DECISION REQUIRED.

**Approximate break-even quantity** (programme expense ₹998,981 ÷ weighted contribution per unit at the batch-1 mix): at 100-unit COGS ₹60/unit → **16,566 units**; at scaled COGS ₹1,373/unit → **728 units**. Excludes salaries, marketing and other operating expenses; with those included the figure is materially higher (ASSUME: add them as a line before relying on this).

**Working capital for batch 2** (180 units at the 100-unit tier, 60 cm launched): ₹512,453 plus PCBA setup ~₹72,000 and a second packaging run; the extrusion and MCPCB MOQ stock from batch 1 covers it. Assume 60–90 days between paying suppliers and D2C cash receipt (ASSUME).

## 7. What is not in this model

Salaries and founder time; marketing and content; D2C platform subscription; office and lab rent; insurance; product liability; returns beyond the warranty reserve; import duty and freight on LEDs and modules beyond the RMKT unit classes (see supplier landscape §3.3, duties unconfirmed); GST input credit timing; any dealer margin (see §5); price erosion; the owner's own COGS figures (see §8).

## 8. Reconciliation required with owner figures

| Item | Owner planning figure | Bottom-up estimate (100 units) | Gap | Likely cause | Action |
|---|---|---|---|---|---|
| Core small size COGS | ₹1,400–1,600 | ~₹2,700–3,000 | ~1.8× | Machined end caps (₹300), engine board with port (₹290), certified adapter (₹480), mounting (₹200) and Coimbatore low-volume labour; the owner figure is plausible only with moulded caps, an Indian-OEM adapter and ≥ 500-unit pricing, or a Chinese contract-manufactured fixture | RFQ packages A–D; decide whether Core Basic launches at the top of the band or as a loss-leader |
| WRGB COGS by size | ₹10k / 14k / 19k | ~₹4.4k / 5.4k / 6.4k | ~0.4× | Owner figure may be a contract-manufacturer finished-product quote including their margin and smart electronics, or premium high-power emitters; bottom-up assumes branded mid-power colour LEDs and a shared housing | Obtain the source of the owner figure; RFQ the WRGB LED board and driver stage |

